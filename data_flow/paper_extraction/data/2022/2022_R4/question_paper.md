# NEET (UG) 2022 · Code R4

200 questions · source `NEET_Papers/2022/Set_R4/Download_Now.pdf` · every image a CDN link (0 without one) · 66 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Modern Physics

> ⚠ The booklet prints "Answer (1*)", and its own printed solution says: "* Language of question is wrongly framed. The values of stopping potentials should be interchanged." As printed, the two stopping potentials are swapped; the starred answer is the one the publisher gets after swapping them back. The same question is 2022_Q1 q017.

When two monochromatic lights of frequency, $\nu$ and $\frac{\nu}{2}$ are incident on a photoelectric metal, their stopping potential becomes $\frac{V_s}{2}$ and $V_s$ respectively. The threshold frequency for this metal is

- **(1)** $\frac{3}{2}\nu$
- (2) $2\nu$
- (3) $3\nu$
- (4) $\frac{2}{3}\nu$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Since $k_{\max} = eV_S = h\nu - \phi$
2. $\frac{eV_S}{2} = h\nu - h\nu_0$  \quad \ldots(i)
3. $eV_S = \frac{h\nu}{2} - h\nu_0$ \quad \ldots(ii)
4. $\frac{1}{2}\left[\frac{h\nu}{2} - h\nu_0\right] = h\nu - h\nu_0$
5. $\Rightarrow\ h\nu_0 - \frac{h\nu_0}{2} = h\nu - \frac{h\nu}{4}$
6. $\Rightarrow\ \frac{h\nu_0}{2} = \frac{3h\nu}{4}$
7. $\nu_0 = \frac{3\nu}{2}$
8. * Language of question is wrongly framed. The values of stopping potentials should be interchanged.

**Solved independently** (answer withheld)

1. For frequency $\nu$: $e\frac{V_s}{2} = h\nu - h\nu_0$, so $eV_s = 2h\nu - 2h\nu_0$.
2. For frequency $\frac{\nu}{2}$: $eV_s = \frac{h\nu}{2} - h\nu_0$.
3. Equate: $2h\nu - 2h\nu_0 = \frac{h\nu}{2} - h\nu_0$.
4. $h\nu_0 = 2h\nu - \frac{h\nu}{2} = \frac{3}{2}h\nu$, so $\nu_0 = \frac{3}{2}\nu$, which is option $1$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q001_6b055734_04112026.png?v=6b0557343bda)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q001_8ed181a8_04112026.png?v=8ed181a85563)

---

## Q2

Physics · Thermodynamics

An ideal gas undergoes four different processes from the same initial state as shown in the figure below. Those processes are adiabatic, isothermal, isobaric and isochoric. The curve which represents the adiabatic process among 1, 2, 3 and 4 is

![printed figure: P-V diagram: four processes 1, 2, 3, 4 from the same initial state](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q002_05b91132_04112026.png?v=05b9113225eb)

*P-V diagram: four processes 1, 2, 3, 4 from the same initial state*

![drawn: P-V diagram: four processes 1, 2, 3, 4 from the same initial state](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q002_question_91258673_14112026.svg?v=91258673b82e)  
*drawn by code/lib/physics_figure.py*

- (1) 4
- (2) 1
- **(3)** 2
- (4) 3

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\left(\frac{dP}{dV}\right)_{\text{adiabatic}} = -\gamma P$
2. $\left(\frac{dP}{dV}\right)_{\text{isothermal}} = -P$
3. $\left(\frac{dP}{dV}\right)_{\text{adiabatic}} > \left(\frac{dP}{dV}\right)_{\text{isothermal}}$

![printed figure: P-V diagram: four processes from a common initial state — isobaric, isothermal, adiabatic, isochoric](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q002_sol_1_1efbd714_04112026.png?v=1efbd714190c)

*P-V diagram: four processes from a common initial state — isobaric, isothermal, adiabatic, isochoric*

![drawn: P-V diagram: four processes from a common initial state — isobaric, isothermal, adiabatic, isochoric](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q002_solution_1_5d340d22_14112026.svg?v=5d340d22ba1d)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Curve $1$ is vertical ($V$ constant), so it is isochoric.
2. Curve $4$ is horizontal ($P$ constant), so it is isobaric.
3. For the isothermal process $PV = \text{const}$, so $\frac{dP}{dV} = -\frac{P}{V}$.
4. For the adiabatic process $PV^{\gamma} = \text{const}$, so $\frac{dP}{dV} = -\gamma\frac{P}{V}$.
5. Since $\gamma > 1$, the adiabatic curve is steeper than the isothermal one from the same initial state.
6. Curve $2$ is steeper than curve $3$, so curve $2$ is adiabatic, which is option $3$.

**Subtopic:** Adiabatic Process · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q002_4261bbdc_04112026.png?v=4261bbdcdf34)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q002_788906af_04112026.png?v=788906af0305)

---

## Q3

Physics · Semiconductor Electronics

In the given circuits (a), (b) and (c), the potential drop across the two $p$-$n$ junctions are equal in

![printed figure: Three circuits (a), (b), (c): two p-n junction boxes in series with a cell in a loop](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q003_6752a91f_04112026.png?v=6752a91ffded)

*Three circuits (a), (b), (c): two p-n junction boxes in series with a cell in a loop*

![drawn: Three circuits (a), (b), (c): two p-n junction boxes in series with a cell in a loop](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q003_question_4473d654_14112026.svg?v=4473d654f43f)  
*drawn by code/lib/physics_figure.py*

- **(1)** Both circuits (a) and (c)
- (2) Circuit (a) only
- (3) Circuit (b) only
- (4) Circuit (c) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Potential drops across the $p$-$n$ junctions will be same if either both junctions are forward biased or both junction are reverse biased.
2. In figure (a) and (c), both junctions are forward biased therefore both have same potential.
3. In figure (b) first junction is forward biased and second junction is reverse biased, so both junctions have different potential difference.

**Solved independently** (answer withheld)

1. In circuit (a) both junctions are oriented $P\to N$ in series, so the same current flows through both with the same bias; identical junctions give $V_1 = V_2$.
2. In circuit (b) one junction is $P\to N$ and the other $N\to P$, so one is forward biased and the other reverse biased; $V_{\text{forward}} \ll V_{\text{reverse}}$, so the drops are unequal.
3. In circuit (c) both junctions are oriented $N\to P$ in series, so both have the same bias and $V_1 = V_2$.
4. Equal drops occur in (a) and (c), which is option $1$.

**Subtopic:** PN Junction Diode Under Forward Bias, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q003_f269afdd_04112026.png?v=f269afddb2dd)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q003_1522f07a_04112026.png?v=1522f07a7dcc)

---

## Q4

Physics · Electromagnetic Waves

When light propagates through a material medium of relative permittivity $\varepsilon_r$ and relative permeability $\mu_r$, the velocity of light, $v$ is given by ($c$-velocity of light in vacuum)

- **(1)** $v = \dfrac{c}{\sqrt{\varepsilon_r \mu_r}}$
- (2) $v = c$
- (3) $v = \sqrt{\dfrac{\mu_r}{\varepsilon_r}}$
- (4) $v = \sqrt{\dfrac{\varepsilon_r}{\mu_r}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $v = \frac{1}{\sqrt{\varepsilon_m \mu_m}}$
2. $v = \frac{1}{\sqrt{\varepsilon_0 \varepsilon_r \mu_0 \mu_r}}$
3. Since $c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}$
4. $\Rightarrow v = \frac{c}{\sqrt{\varepsilon_r \mu_r}}$

**Solved independently** (answer withheld)

1. In a medium, $v = \frac{1}{\sqrt{\mu \varepsilon}}$ with $\mu = \mu_0 \mu_r$ and $\varepsilon = \varepsilon_0 \varepsilon_r$.
2. $v = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \cdot \frac{1}{\sqrt{\mu_r \varepsilon_r}}$.
3. Since $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, $v = \frac{c}{\sqrt{\varepsilon_r \mu_r}}$, which is option $1$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q004_8e321b7e_04112026.png?v=8e321b7e8ebd)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q004_464b870f_04112026.png?v=464b870f2911)

---

## Q5

Physics · Units and Measurements

Plane angle and solid angle have

- (1) Both units and dimensions
- **(2)** Units but no dimensions
- (3) Dimensions but no units
- (4) No units and no dimensions

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Plane angle $=\frac{\text{Arc}}{\text{Radius}}=\frac{[\mathrm{L}]}{[\mathrm{L}]}\longrightarrow$ Unit $=$ Radian
2. $=[\mathrm{M^0L^0T^0}]$
3. Solid angle $=\frac{\text{Area}}{(\text{Radius})^2}\longrightarrow$ Unit $=$ Steradian
4. $=\frac{\mathrm{L}^2}{\mathrm{L}^2}=[\mathrm{M^0L^0T^0}]$
5. $\therefore$ Both have units but no dimensions

**Solved independently** (answer withheld)

1. Plane angle $\theta = \frac{\text{arc}}{r}$ has dimensions $\frac{[L]}{[L]} = [M^0L^0T^0]$ but unit radian (rad).
2. Solid angle $\Omega = \frac{A}{r^2}$ has dimensions $\frac{[L^2]}{[L^2]} = [M^0L^0T^0]$ but unit steradian (sr).
3. So both have units but no dimensions, which is option $2$.

**Subtopic:** SI Units and Prefixes, Dimensional Formulae · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 4)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q005_49154a40_04112026.png?v=49154a404ac8)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q005_c2f3cef6_04112026.png?v=c2f3cef6f5b7)

---

## Q6

Physics · Electrostatics

The angle between the electric lines of force and the equipotential surface is

- (1) $180^\circ$
- (2) $0^\circ$
- (3) $45^\circ$
- **(4)** $90^\circ$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $dV = -\vec{E}\cdot d\vec{r}$
2. $dV = -E\,dr\cos\theta$
3. For equipotential surface,
4. $dV = 0$
5. $\cos\theta = 0$
6. $\Rightarrow \theta = 90^\circ$

**Solved independently** (answer withheld)

1. Along an equipotential surface $dV = -\vec{E}\cdot d\vec{l} = 0$, so $\vec{E} \perp d\vec{l}$ and the lines of force meet the surface at $90^\circ$, which is option $4$.

**Subtopic:** Equipotential Surfaces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q006_9d519aaa_04112026.png?v=9d519aaa4c8b)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q006_dde5d790_04112026.png?v=dde5d79016ed)

---

## Q7

Physics · Wave Optics

In a Young's double slit experiment, a student observes 8 fringes in a certain segment of screen when a monochromatic light of $600\,\mathrm{nm}$ wavelength is used. If the wavelength of light is changed to $400\,\mathrm{nm}$, then the number of fringes he would observe in the same region of the screen is

- **(1)** 12
- (2) 6
- (3) 8
- (4) 9

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\beta = \frac{\lambda D}{d}$
2. Let length of segment of screen $= l$
3. $\Rightarrow l = 8\beta_1 = \frac{8\lambda_1 D}{d}$ \quad ...(1)
4. and $l = n\beta_2 = \frac{n\lambda_2 D}{d}$ \quad ...(2)
5. from (1) and (2)
6. $8\lambda_1 = n\lambda_2$
7. $8(600\,\mathrm{nm}) = n(400\,\mathrm{nm})$
8. $n = 12$

**Solved independently** (answer withheld)

1. Fringe width $\beta = \frac{\lambda D}{d}$, so $\beta \propto \lambda$.
2. For the same segment of length $L$, $L = n_1\beta_1 = n_2\beta_2$, so $n_1\lambda_1 = n_2\lambda_2$.
3. $n_2 = \frac{8 \times 600\,\mathrm{nm}}{400\,\mathrm{nm}} = 12$, which is option $1$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q007_618cd557_04112026.png?v=618cd55748b1)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q007_ddfa3bea_04112026.png?v=ddfa3beaa5d1)

---

## Q8

Physics · Mechanical Properties of Fluids

If a soap bubble expands, the pressure inside the bubble

- (1) Is equal to the atmospheric pressure
- **(2)** Decreases
- (3) Increases
- (4) Remains the same

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Excess pressure inside the bubble $= \Delta P = \frac{4T}{R}$
2. $P_{\mathrm{in}} = P_{\mathrm{out}} + \frac{4T}{R}$
3. as '$R$' increases '$P$' decreases

**Solved independently** (answer withheld)

1. Pressure inside a soap bubble (two surfaces): $P_{in} = P_0 + \frac{4T}{R}$.
2. On expansion the radius $R$ increases, so $\frac{4T}{R}$ decreases.
3. Hence $P_{in}$ decreases, which is option $2$.

**Subtopic:** Excess Pressure on Curved Surface (General Case, Drop, Soap Bubbles, Air Bubbles) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q008_83f4d11e_04112026.png?v=83f4d11e0c5b)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q008_d6b439bf_04112026.png?v=d6b439bf740a)

---

## Q9

Physics · Mechanical Properties of Fluids

A spherical ball is dropped in a long column of a highly viscous liquid. The curve in the graph shown, which represents the speed of the ball ($v$) as a function of time ($t$) is

![printed figure: Speed v versus time t graph with four curves A, B, C, D](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q009_c10390f9_04112026.png?v=c10390f90f8c)

*Speed v versus time t graph with four curves A, B, C, D*

![drawn: Speed v versus time t graph with four curves A, B, C, D](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q009_question_e43cfedc_14112026.svg?v=e43cfedc2a2b)  
*drawn by code/lib/physics_figure.py*

- (1) D
- (2) A
- **(3)** B
- (4) C

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Initial speed of ball is zero and it finally attains terminal speed

![printed figure: Speed v of the ball against time t rising to terminal speed v_T (curve B)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q009_sol_1_84fd0a6c_04112026.png?v=84fd0a6c16c0)

*Speed v of the ball against time t rising to terminal speed v_T (curve B)*

![drawn: Speed v of the ball against time t rising to terminal speed v_T (curve B)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q009_solution_1_f26545aa_14112026.svg?v=f26545aaa3e5)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The ball is dropped, so $v(0) = 0$, which rules out curves $C$ and $D$ because they do not start at $v=0$.
2. Net force: $m\frac{dv}{dt} = mg - F_B - 6\pi\eta r v$, so the acceleration falls as $v$ grows.
3. Solving gives $v = v_t\left(1 - e^{-t/\tau}\right)$, which rises from zero and levels off at the terminal velocity $v_t$.
4. Curve $A$ is a straight line that keeps rising, so it has no terminal velocity. Curve $B$ rises and saturates, so the answer is option $3$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q009_81e8f806_04112026.png?v=81e8f8060283)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q009_07222114_04112026.png?v=072221142350)

---

## Q10

Physics · Magnetic Effect of Electric Current

Given below are two statements
In light of above statements choose the most appropriate answer from the options given below

- (Statement I) Biot-Savart's law gives us the expression for the magnetic field strength of an infinitesimal current element ($I\,dl$) of a current carrying conductor only.
- (Statement II) Biot-Savart's law is analogous to Coulomb's inverse square law of charge $q$, with the former being related to the field produced by a scalar source, $I\,dl$ while the latter being produced by a vector source, $q$.

- (1) Statement I is incorrect and Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct and Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to Biot-Savart's law $d\vec{B} = \frac{\mu_0}{4\pi}\frac{I d\vec{l} \times \vec{r}}{r^3}$ which is applicable for infinitesimal element.
2. It is analogous to Coulomb's law, where $I d\vec{l}$ is vector source and electric field is produced by scalar source $q$.
3. Here statement I is correct and statement II is incorrect.

**Solved independently** (answer withheld)

1. Biot-Savart's law gives $d\vec{B} = \frac{\mu_0}{4\pi}\frac{I\,d\vec{l} \times \hat{r}}{r^2}$ for an infinitesimal current element $I\,d\vec{l}$, so Statement I is correct.
2. The source $I\,d\vec{l}$ is a vector, while the charge $q$ in Coulomb's law is a scalar; Statement II says the reverse, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect is option $4$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q010_77593d13_04112026.png?v=77593d13fb64)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q010_d11bb058_04112026.png?v=d11bb058d79f)

---

## Q11

Physics · Current Electricity

As the temperature increases, the electrical resistance

- (1) Decreases for conductors but increases for semiconductors
- (2) Increases for both conductors and semiconductors
- (3) Decreases for both conductors and semiconductors
- **(4)** Increases for conductors but decreases for semiconductors

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. As the temperature increases the resistivity of the conductor increases hence the electrical resistance increases.
2. However for semiconductor the resistivity decreases with the temperature. Hence electrical resistance of semiconductor decreases.

**Solved independently** (answer withheld)

1. For a conductor, $\rho_T = \rho_0[1 + \alpha (T - T_0)]$ with $\alpha > 0$, so resistance increases with temperature.
2. For a semiconductor, the number density of charge carriers $n$ increases with $T$, so $\rho = \frac{1}{n e \mu}$ decreases and resistance decreases (negative $\alpha$).
3. Resistance increases for conductors but decreases for semiconductors, which is option $4$.

**Subtopic:** Temperature Dependence of Resistivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q011_2ec586f8_04112026.png?v=2ec586f8edf2)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q011_fb04c462_04112026.png?v=fb04c46235be)

---

## Q12

Physics · Work, Energy and Power

The energy that will be ideally radiated by a $100\,\mathrm{kW}$ transmitter in $1$ hour is

- (1) $1 \times 10^{5}\,\mathrm{J}$
- **(2)** $36 \times 10^{7}\,\mathrm{J}$
- (3) $36 \times 10^{4}\,\mathrm{J}$
- (4) $36 \times 10^{5}\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Energy = Power $\times$ time
2. $E = 100 \times 10^{3} \times 3600$
3. $= 36 \times 10^{7}\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Energy radiated $E = P\,t$.
2. $P = 100\,\mathrm{kW} = 10^{5}\,\mathrm{W}$ and $t = 1\,\mathrm{h} = 3600\,\mathrm{s}$.
3. $E = 10^{5} \times 3600 = 3.6 \times 10^{8}\,\mathrm{J} = 36 \times 10^{7}\,\mathrm{J}$, which is option $2$.

**Subtopic:** Power · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q012_fcc26ed5_04112026.png?v=fcc26ed54299)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q012_79939100_04112026.png?v=799391004894)

---

## Q13

Physics · Electrostatics

Two hollow conducting spheres of radii $R_1$ and $R_2$ ($R_1 >> R_2$) have equal charges. The potential would be

- (1) Dependent on the material property of the sphere
- (2) More on bigger sphere
- **(3)** More on smaller sphere
- (4) Equal on both the spheres

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Potential of conducting hollow sphere $=\frac{KQ}{R}$
2. Now, $Q =$ same
3. $\Rightarrow V \propto \frac{1}{R} \Rightarrow$ more the radius less will be the potential.
4. $\Rightarrow$ Hence potential would be more on smaller sphere

**Solved independently** (answer withheld)

1. For a charged hollow conducting sphere, the potential is $V = \frac{kQ}{R}$.
2. With equal charges, $V \propto \frac{1}{R}$.
3. Since $R_1 \gg R_2$, $V_2 = \frac{kQ}{R_2} > V_1 = \frac{kQ}{R_1}$, so the potential is more on the smaller sphere, which is option $3$.

**Subtopic:** Potential Due to Linear and Surface Charge Distribution · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q013_1e7c3fdb_04112026.png?v=1e7c3fdbb286)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q013_b568cac7_04112026.png?v=b568cac73b35)

---

## Q14

Physics · Work, Energy and Power

An electric lift with a maximum load of $2000\,\mathrm{kg}$ (lift + passengers) is moving up with a constant speed of $1.5\,\mathrm{ms^{-1}}$. The frictional force opposing the motion is $3000\,\mathrm{N}$. The minimum power delivered by the motor to the lift in watts is : ($g = 10\,\mathrm{m\ s^{-2}}$)

- (1) $23500$
- (2) $23000$
- (3) $20000$
- **(4)** $34500$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $F_{\mathrm{up}} = 2000g + 3000$
2. $= 23000\,\mathrm{N}$
3. Minimum power $P_{\min} = \vec{F}\cdot\vec{v}$
4. $P_{\min} = Fv = 23000 \times \frac{3}{2}$
5. $= 34500\,\mathrm{W}$

**Solved independently** (answer withheld)

1. At constant speed the net force is zero, so the motor force is $F = mg + f$.
2. $F = 2000 \times 10 + 3000 = 23000\,\mathrm{N}$.
3. $P = Fv = 23000 \times 1.5 = 34500\,\mathrm{W}$, which is option $4$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q014_1463556d_04112026.png?v=1463556dc1a2)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q014_c3f71302_04112026.png?v=c3f71302c28d)

---

## Q15

Physics · Modern Physics

The graph which shows the variation of the de Broglie wavelength ($\lambda$) of a particle and its associated momentum ($p$) is

- **(1)** ![printed figure: Option (1): λ falls off hyperbolically with p](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q015_option_1_db45a475_04112026.png?v=db45a4752feb) *Option (1): λ falls off hyperbolically with p* ![drawn: Option (1): λ falls off hyperbolically with p](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q015_option_1_81d28a7b_14112026.svg?v=81d28a7bd13f)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Straight line of de Broglie wavelength λ increasing with momentum p](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q015_option_2_ac65aab4_04112026.png?v=ac65aab49411) *Straight line of de Broglie wavelength λ increasing with momentum p* ![drawn: Straight line of de Broglie wavelength λ increasing with momentum p](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q015_option_2_105e1f08_14112026.svg?v=105e1f08c9f3)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Option (3): λ decreases linearly with p](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q015_option_3_67df796b_04112026.png?v=67df796bca9c) *Option (3): λ decreases linearly with p* ![drawn: Option (3): λ decreases linearly with p](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q015_option_3_ddf618ef_14112026.svg?v=ddf618ef8851)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: de Broglie wavelength λ rising steeply with momentum p](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q015_option_4_035191c9_04112026.png?v=035191c9bb2f) *de Broglie wavelength λ rising steeply with momentum p* ![drawn: de Broglie wavelength λ rising steeply with momentum p](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q015_option_4_bce9cfdc_14112026.svg?v=bce9cfdca59f)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. de-Broglie wavelength associated with a particle is given by
2. $\lambda = \frac{h}{p}$
3. $\lambda \propto \frac{1}{p}$

![printed figure: de Broglie wavelength lambda falling with momentum p as a hyperbola](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q015_sol_1_b57d12a9_04112026.png?v=b57d12a9dc4f)

*de Broglie wavelength lambda falling with momentum p as a hyperbola*

![drawn: de Broglie wavelength lambda falling with momentum p as a hyperbola](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q015_solution_1_1880fcc2_14112026.svg?v=1880fcc2eb69)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The de Broglie relation is $\lambda = \frac{h}{p}$.
2. This means $\lambda \propto \frac{1}{p}$, an inverse relationship.
3. Such a relationship is represented by a rectangular hyperbola, matching option 1's curve.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q015_8d184b46_04112026.png?v=8d184b46bf82)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q015_7847c491_04112026.png?v=7847c4916a99)

---

## Q16

Physics · Current Electricity

Two resistors of resistance, $100\,\Omega$ and $200\,\Omega$ are connected in parallel in an electrical circuit. The ratio of the thermal energy developed in $100\,\Omega$ to that in $200\,\Omega$ in a given time is

- (1) $4 : 1$
- (2) $1 : 2$
- **(3)** $2 : 1$
- (4) $1 : 4$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For parallel combination
2. $P = \frac{V^{2}}{R}$
3. $\frac{P_1}{P_2} = \frac{R_2}{R_1}$
4. $\Rightarrow \frac{P_1}{P_2} = \frac{200}{100} = \frac{2}{1}$

**Solved independently** (answer withheld)

1. In a parallel connection both resistors have the same potential difference $V$.
2. Heat developed in time $t$ is $H = \frac{V^2 t}{R}$, so $H \propto \frac{1}{R}$.
3. $\frac{H_{100}}{H_{200}} = \frac{200\,\Omega}{100\,\Omega} = \frac{2}{1}$, which is option $3$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q016_992fc0e9_04112026.png?v=992fc0e9b3e8)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q016_e273e224_04112026.png?v=e273e2244438)

---

## Q17

Physics · Magnetic Effect of Electric Current

A long solenoid of radius $1\,\mathrm{mm}$ has $100$ turns per mm. If $1\,\mathrm{A}$ current flows in the solenoid, the magnetic field strength at the centre of the solenoid is

- (1) $6.28 \times 10^{-4}\,\mathrm{T}$
- (2) $6.28 \times 10^{-2}\,\mathrm{T}$
- **(3)** $12.56 \times 10^{-2}\,\mathrm{T}$
- (4) $12.56 \times 10^{-4}\,\mathrm{T}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know, magnetic field at centre of solenoid
2. $B = \mu_0 \frac{N}{\ell} I = \mu_0 n I$ $\qquad \left[n = \frac{N}{\ell}\right]$
3. $= 4\pi \times 10^{-7} \times 100 \times 10^{3} \times 1$ $\qquad \left[n = \frac{100}{10^{-3}}\right]$
4. $= 4\pi \times 10^{-2}\,\mathrm{T}$
5. $B = 12.56 \times 10^{-2}\,\mathrm{T}$

**Solved independently** (answer withheld)

1. For a long solenoid the field inside is $B = \mu_0 n I$, independent of radius.
2. $n = 100\,\mathrm{mm^{-1}} = 10^{5}\,\mathrm{m^{-1}}$.
3. $B = 4\pi \times 10^{-7} \times 10^{5} \times 1 = 4\pi \times 10^{-2}\,\mathrm{T}$.
4. $4\pi \times 10^{-2} = 12.56 \times 10^{-2}\,\mathrm{T}$, which is option $3$.

**Subtopic:** Solenoid and Toroid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q017_1e82cf44_04112026.png?v=1e82cf44ed4c)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q017_8497b63a_04112026.png?v=8497b63a8167)

---

## Q18

Physics · Electromagnetic Induction

A square loop of side $1\,\mathrm{m}$ and resistance $1\,\Omega$ is placed in a magnetic field of $0.5\,\mathrm{T}$. If the plane of loop is perpendicular to the direction of magnetic field, the magnetic flux through the loop is

- (1) Zero weber
- (2) $2$ weber
- **(3)** $0.5$ weber
- (4) $1$ weber

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Square loop of side 1 m with the magnetic field perpendicular to its plane (dot at centre)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q018_sol_1_defe810a_04112026.png?v=defe810aa474)

*Square loop of side 1 m with the magnetic field perpendicular to its plane (dot at centre)*

![drawn: Square loop of side 1 m with the magnetic field perpendicular to its plane (dot at centre)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q018_solution_1_7a6db1ed_14112026.svg?v=7a6db1ed2b81)  
*drawn by code/lib/physics_figure.py*

1. Magnetic flux $(\phi_B) = \vec{B}\cdot\vec{A}$
2. $\vec{B}$ and $\vec{A}$ are in same direction, therefore
3. $\phi_B = B.A = 0.5 \times 1^2$
4. $= 0.5\,\mathrm{Wb}$

**Solved independently** (answer withheld)

1. Plane of loop perpendicular to $\vec B$ means the area vector is parallel to $\vec B$, so $\theta = 0^\circ$.
2. $A = (1\,\mathrm{m})^2 = 1\,\mathrm{m^2}$.
3. $\phi = BA\cos 0^\circ = 0.5 \times 1 \times 1 = 0.5\,\mathrm{Wb}$, which is option $3$.

**Subtopic:** Magnetic Flux · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q018_9127a48a_04112026.png?v=9127a48ab94c)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q018_db315357_04112026.png?v=db31535712ee)

---

## Q19

Physics · Current Electricity

A copper wire of length $10\,\mathrm{m}$ and radius $\left(\dfrac{10^{-2}}{\sqrt{\pi}}\right)\,\mathrm{m}$ has electrical resistance of $10\,\Omega$. The current density in the wire for an electric field strength of $10\,(\mathrm{V/m})$ is

- **(1)** $10^{5}\,\mathrm{A/m^{2}}$
- (2) $10^{4}\,\mathrm{A/m^{2}}$
- (3) $10^{6}\,\mathrm{A/m^{2}}$
- (4) $10^{-5}\,\mathrm{A/m^{2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Resistance, $R = \rho\frac{L}{A} = \frac{L}{\sigma A}$
2. $\Rightarrow\ \sigma = \frac{L}{RA}$
3. Also current density $j = \sigma E = \frac{LE}{RA}$
4. $j = \frac{10\times 10}{10\times\pi\left(\frac{10^{-2}}{\sqrt{\pi}}\right)^{2}} = \frac{100}{10\times\pi\times\left(\frac{10^{-4}}{\pi}\right)}$
5. $= 10^{5}\,\mathrm{A/m^{2}}$

**Solved independently** (answer withheld)

1. $A = \pi r^2 = \pi \left(\frac{10^{-2}}{\sqrt{\pi}}\right)^2 = 10^{-4}\,\mathrm{m^2}$.
2. $\rho = \frac{RA}{l} = \frac{10 \times 10^{-4}}{10} = 10^{-4}\,\Omega\,\mathrm{m}$.
3. $J = \frac{E}{\rho} = \frac{10}{10^{-4}} = 10^{5}\,\mathrm{A/m^2}$, which is option $1$.

**Subtopic:** Current Density, Resistivity · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 8)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q019_d837acdc_04112026.png?v=d837acdcd3e0)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q019_2cd5024c_04112026.png?v=2cd5024c0412)

---

## Q20

Physics · Center of Mass

Two objects of mass $10\,\mathrm{kg}$ and $20\,\mathrm{kg}$ respectively are connected to the two ends of a rigid rod of length $10\,\mathrm{m}$ with negligible mass. The distance of the center of mass of the system from the $10\,\mathrm{kg}$ mass is

- (1) $5\,\mathrm{m}$
- (2) $\dfrac{10}{3}\,\mathrm{m}$
- **(3)** $\dfrac{20}{3}\,\mathrm{m}$
- (4) $10\,\mathrm{m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q020_sol_1_67f00a03_04112026.png?v=67f00a03530c)

*Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x axis*

![drawn: Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x axis](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q020_solution_1_7d62cfa9_14112026.svg?v=7d62cfa931b7)  
*drawn by code/lib/physics_figure.py*

1. $X_{\mathrm{cm}} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$
2. $= \frac{10 \times 0 + 20 \times 10}{10 + 20}$
3. $= \frac{200}{30}$
4. $= \frac{20}{3}\,\mathrm{m}$

**Solved independently** (answer withheld)

1. Place the $10\,\mathrm{kg}$ mass at $x=0$ and the $20\,\mathrm{kg}$ mass at $x=10\,\mathrm{m}$.
2. $x_{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = \frac{10(0) + 20(10)}{10+20}$.
3. $x_{cm} = \frac{200}{30} = \frac{20}{3}\,\mathrm{m}$, which is option $3$.

**Subtopic:** Center of Mass of Two Particles · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q020_bddf6aa9_04112026.png?v=bddf6aa90b56)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q020_b9336a6e_04112026.png?v=b9336a6e9e33)

---

## Q21

Physics · Laws of Motion

A shell of mass $m$ is at rest initially. It explodes into three fragments having mass in the ratio $2 : 2 : 1$. If the fragments having equal mass fly off along mutually perpendicular directions with speed $v$, the speed of the third (lighter) fragment is

- (1) $3\sqrt{2}v$
- (2) $v$
- (3) $\sqrt{2}v$
- **(4)** $2\sqrt{2}v$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Momentum of the system would remain conserved.
2. Initial momentum $= 0$
3. Final momentum should also be zero.
4. Let masses be $2m$, $2m$, and $m$
5. Momentum along $x$-direction $= 2mv\hat{i}$
6. Momentum along $y$-direction $= 2mv\hat{j}$
7. Net momentum $= \sqrt{(2mv)^2 + (2mv)^2} = \sqrt{2}\cdot 2mv$
8. Now, $2\sqrt{2}mv = mv'$
9. $v' = 2\sqrt{2}v$

**Solved independently** (answer withheld)

1. Mass ratio $2:2:1$ gives masses $\frac{2m}{5}, \frac{2m}{5}, \frac{m}{5}$.
2. Initial momentum is zero, so total momentum after the explosion is zero.
3. Resultant momentum of the two equal fragments moving perpendicularly: $p = \sqrt{2}\,\frac{2m}{5}v$.
4. The lighter fragment must carry equal and opposite momentum: $\frac{m}{5}u = \frac{2\sqrt{2}m}{5}v$.
5. $u = 2\sqrt{2}v$, which is option $4$.

**Subtopic:** Conservation of Momentum · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q021_bc0949d1_04112026.png?v=bc0949d12ba0)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q021_39acbc01_04112026.png?v=39acbc013e05)

---

## Q22

Physics · Gravitation

A body of mass $60\,\mathrm{g}$ experiences a gravitational force of $3.0\,\mathrm{N}$, when placed at a particular point. The magnitude of the gravitational field intensity at that point is

- (1) $180\,\mathrm{N/kg}$
- (2) $0.05\,\mathrm{N/kg}$
- **(3)** $50\,\mathrm{N/kg}$
- (4) $20\,\mathrm{N/kg}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $F = mE_G$
2. $3 = \frac{60}{1000} E_G$
3. $E_G = 50\,\mathrm{N/kg}$

**Solved independently** (answer withheld)

1. Convert mass: $m = 60\,\mathrm{g} = 0.060\,\mathrm{kg}$.
2. Gravitational field intensity is force per unit mass: $E = \frac{F}{m}$.
3. $E = \frac{3.0\,\mathrm{N}}{0.060\,\mathrm{kg}} = 50\,\mathrm{N/kg}$, which is option $3$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q022_588db22d_04112026.png?v=588db22d9a64)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q022_7bc379af_04112026.png?v=7bc379af185e)

---

## Q23

Physics · Kinematics

The ratio of the distances travelled by a freely falling body in the $1^{\mathrm{st}}$, $2^{\mathrm{nd}}$, $3^{\mathrm{rd}}$ and $4^{\mathrm{th}}$ second

- (1) $1 : 1 : 1 : 1$
- (2) $1 : 2 : 3 : 4$
- (3) $1 : 4 : 9 : 16$
- **(4)** $1 : 3 : 5 : 7$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $S_{n^{\mathrm{th}}} = u + \frac{1}{2}a(2n-1)$
2. $S_{1^{\mathrm{st}}} = \frac{1}{2}g(2\times 1 - 1) = \frac{g}{2}$
3. $S_{2^{\mathrm{nd}}} = \frac{1}{2}g(2\times 2 - 1) = 3\left(\frac{1}{2}g\right)$
4. $S_{3^{\mathrm{rd}}} = \frac{1}{2}g(2\times 3 - 1) = 5\times\left(\frac{1}{2}g\right)$
5. $S_{4^{\mathrm{th}}} = \frac{1}{2}g(2\times 4 - 1) = 7\times\left(\frac{1}{2}g\right)$
6. $S_{1^{\mathrm{st}}} : S_{2^{\mathrm{nd}}} : S_{3^{\mathrm{rd}}} : S_{4^{\mathrm{th}}}$
7. $= 1 : 3 : 5 : 7$

**Solved independently** (answer withheld)

1. For a body starting from rest, distance in nth second $s_n = \frac{g}{2}(2n-1)$.
2. For n=1,2,3,4: $s_n \propto 1, 3, 5, 7$.
3. This matches option 4.

**Subtopic:** Galileo's Law of Odd Number · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 10)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q023_55a6f892_04112026.png?v=55a6f892130b)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q023_9d107886_04112026.png?v=9d10788677ce)

---

## Q24

Physics · Ray Optics

A biconvex lens has radii of curvature, $20\,\mathrm{cm}$ each. If the refractive index of the material of the lens is $1.5$, the power of the lens is

- (1) Infinity
- (2) $+2\,\mathrm{D}$
- (3) $+20\,\mathrm{D}$
- **(4)** $+5\,\mathrm{D}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Power of lens is given by
2. $P = \frac{1}{f(m)}$
3. $\frac{1}{f} = (\mu - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$
4. $\frac{1}{f} = \left\{\frac{3}{2} - 1\right\}\left(\frac{1}{20} + \frac{1}{20}\right)$
5. $f = 20\,\mathrm{cm}$
6. $P = \frac{1}{20 \times 10^{-2}}$
7. $= 5\,\mathrm{D}$

**Solved independently** (answer withheld)

1. For a biconvex lens, $R_1 = +20\,\mathrm{cm}$ and $R_2 = -20\,\mathrm{cm}$.
2. $\frac{1}{f} = (\mu - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = (1.5 - 1)\left(\frac{1}{20} + \frac{1}{20}\right)\,\mathrm{cm^{-1}}$.
3. $\frac{1}{f} = 0.5 \times \frac{2}{20} = \frac{1}{20}\,\mathrm{cm^{-1}}$, so $f = 20\,\mathrm{cm} = 0.2\,\mathrm{m}$.
4. $P = \frac{1}{f} = \frac{1}{0.2\,\mathrm{m}} = +5\,\mathrm{D}$, which is option $4$.

**Subtopic:** Lens Maker Formula, Power of Lens · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q024_b7acbf1e_04112026.png?v=b7acbf1e0c7c)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q024_47bb3e98_04112026.png?v=47bb3e98f256)

---

## Q25

Physics · Units and Measurements

The dimensions $[\mathrm{MLT^{-2}A^{-2}}]$ belong to the

- (1) Electric permittivity
- (2) Magnetic flux
- (3) Self inductance
- **(4)** Magnetic permeability

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Dimensional formula of magnetic permeability is $[\mathrm{MLT^{-2}A^{-2}}]$

**Solved independently** (answer withheld)

1. Force per unit length between parallel wires: $\frac{F}{l} = \frac{\mu_0 I_1 I_2}{2\pi d}$, so $\mu_0 = \frac{2\pi F d}{l I_1 I_2}$.
2. $[\mu_0] = \frac{[F]}{[I^2]} = \frac{[\mathrm{MLT^{-2}}]}{[\mathrm{A^2}]} = [\mathrm{MLT^{-2}A^{-2}}]$.
3. Check others: $[\phi] = [\mathrm{ML^2T^{-2}A^{-1}}]$, $[L] = [\mathrm{ML^2T^{-2}A^{-2}}]$, $[\varepsilon_0] = [\mathrm{M^{-1}L^{-3}T^4A^2}]$; none match.
4. So the dimensions belong to magnetic permeability, option $4$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q025_fa957ff0_04112026.png?v=fa957ff0f47b)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q025_ed8c0c63_04112026.png?v=ed8c0c63e64f)

---

## Q26

Physics · Rotational Motion

The angular speed of a fly wheel moving with uniform angular acceleration changes from 1200 rpm to 3120 rpm in 16 seconds. The angular acceleration in $\mathrm{rad/s^2}$ is

- (1) $104\pi$
- (2) $2\pi$
- **(3)** $4\pi$
- (4) $12\pi$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Angular acceleration $\alpha = \frac{\omega_f - \omega_i}{t}$
2. $\omega_f = 3120 \times \frac{2\pi}{60}$ rad/s
3. $\omega_i = 1200 \times \frac{2\pi}{60}$ rad/s
4. $\Rightarrow \alpha = \frac{(3120 - 1200)}{16} \times \frac{2\pi}{60} = 4\pi$

**Solved independently** (answer withheld)

1. Change in angular speed: $\Delta n = 3120 - 1200 = 1920\,\mathrm{rpm}$.
2. Convert to rev/s: $\frac{1920}{60} = 32\,\mathrm{rev/s}$.
3. Convert to rad/s: $\Delta\omega = 2\pi \times 32 = 64\pi\,\mathrm{rad/s}$.
4. $\alpha = \frac{\Delta\omega}{t} = \frac{64\pi}{16} = 4\pi\,\mathrm{rad/s^2}$, which is option $3$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q026_09544b27_04112026.png?v=09544b270aff)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q026_3c59c079_04112026.png?v=3c59c0796756)

---

## Q27

Physics · Electromagnetic Waves

Match List-I with List-II

Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | AM radio waves | (i) | $10^{-10}\,\mathrm{m}$ |
| (b) | Microwaves | (ii) | $10^{2}\,\mathrm{m}$ |
| (c) | Infrared radiations | (iii) | $10^{-2}\,\mathrm{m}$ |
| (d) | X-rays | (iv) | $10^{-4}\,\mathrm{m}$ |

- **(1)** (a) - (ii), (b) - (iii), (c) - (iv), (d) - (i)
- (2) (a) - (iv), (b) - (iii), (c) - (ii), (d) - (i)
- (3) (a) - (iii), (b) - (ii), (c) - (i), (d) - (iv)
- (4) (a) - (iii), (b) - (iv), (c) - (ii), (d) - (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Table of waves and their wavelengths (AM radio waves, microwaves, infrared radiations, X-rays)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q027_sol_1_98cb5cb1_04112026.png?v=98cb5cb1ef35)

*Table of waves and their wavelengths (AM radio waves, microwaves, infrared radiations, X-rays)*

![drawn: Table of waves and their wavelengths (AM radio waves, microwaves, infrared radiations, X-rays)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q027_solution_1_4d1b5149_14112026.svg?v=4d1b5149e0ba)  
*drawn by code/lib/physics_figure.py*

1. (a) - (ii)
2. (b) - (iii)
3. (c) - (iv)
4. (d) - (i)

**Solved independently** (answer withheld)

1. AM radio waves have typical wavelengths of order $10^{2}\,\mathrm{m}$, matching (ii).
2. Microwaves have wavelengths of order $10^{-2}\,\mathrm{m}$, matching (iii).
3. Infrared radiation has wavelengths of order $10^{-4}\,\mathrm{m}$, matching (iv).
4. X-rays have wavelengths of order $10^{-10}\,\mathrm{m}$, matching (i).
5. This combination corresponds to option 1.

**Subtopic:** Electromagnetic Spectrum · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q027_cf829268_04112026.png?v=cf8292681c82)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q027_2bcf7194_04112026.png?v=2bcf7194c494)

---

## Q28

Physics · Alternating Current

The peak voltage of the ac source is equal to

- (1) $1/\sqrt{2}$ times the rms value of the ac source
- (2) The value of voltage supplied to the circuit
- (3) The rms value of the ac source
- **(4)** $\sqrt{2}$ times the rms value of the ac source

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. We know,
2. RMS value of A.C. $E_{\mathrm{rms}} = \frac{E_0}{\sqrt{2}}$
3. $E_0 = \sqrt{2}E_{\mathrm{rms}}$

**Solved independently** (answer withheld)

1. For a sinusoidal source, $V_{rms} = \frac{V_0}{\sqrt{2}}$, so $V_0 = \sqrt{2}\,V_{rms}$, which is option $4$.

**Subtopic:** RMS Voltage · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q028_c5081536_04112026.png?v=c50815360ad8)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q028_5b751deb_04112026.png?v=5b751deb15f6)

---

## Q29

Physics · Waves

If the initial tension on a stretched string is doubled, then the ratio of the initial and final speeds of a transverse wave along the string is

- (1) $1 : 2$
- (2) $1 : 1$
- (3) $\sqrt{2} : 1$
- **(4)** $1 : \sqrt{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. We know, velocity of transverse wave
2. $v = \sqrt{\frac{T}{\mu}}$
3. $\therefore\; v_i = \sqrt{\frac{T}{\mu}}$ and $v_f = \sqrt{\frac{2T}{\mu}}$
4. $\therefore\; \frac{v_i}{v_f} = \frac{1}{\sqrt{2}}$

**Solved independently** (answer withheld)

1. Speed of transverse wave on string: $v = \sqrt{T/\mu}$.
2. $\frac{v_1}{v_2} = \sqrt{\frac{T}{2T}} = \frac{1}{\sqrt{2}}$.
3. So ratio of initial to final speed is $1:\sqrt{2}$, matching option 4.

**Subtopic:** Speed of Different Waves · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 12)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q029_72c16ca8_04112026.png?v=72c16ca80f20)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q029_e063b043_04112026.png?v=e063b0436070)

---

## Q30

Physics · Kinematics

The displacement-time graphs of two moving particles make angles of $30^\circ$ and $45^\circ$ with the $x$-axis as shown in the figure. The ratio of their respective velocity is

![printed figure: Displacement-time graph: two straight lines from origin at 30° and 45° to the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q030_21f0d362_04112026.png?v=21f0d3620644)

*Displacement-time graph: two straight lines from origin at 30° and 45° to the time axis*

![drawn: Displacement-time graph: two straight lines from origin at 30° and 45° to the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q030_question_4ca7d7cd_14112026.svg?v=4ca7d7cd46e6)  
*drawn by code/lib/physics_figure.py*

- **(1)** $1:\sqrt{3}$
- (2) $\sqrt{3}:1$
- (3) $1:1$
- (4) $1:2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Slope of $x\text{-}t$ curves gives the velocity
2. $\Rightarrow$ Ratio $=\frac{\tan 30^\circ}{\tan 45^\circ}=\frac{1}{\frac{\sqrt{3}}{1}}=1:\sqrt{3}$

**Solved independently** (answer withheld)

1. Velocity equals the slope of the displacement-time graph, $v = \tan\theta$.
2. $\frac{v_1}{v_2} = \frac{\tan 30^\circ}{\tan 45^\circ}$.
3. $\frac{1/\sqrt{3}}{1} = 1:\sqrt{3}$, which is option $1$.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q030_a09cbce0_04112026.png?v=a09cbce0d106)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q030_d102a1c7_04112026.png?v=d102a1c7a019)

---

## Q31

Physics · Semiconductor Electronics

In half wave rectification, if the input frequency is 60 Hz, then the output frequency would be

- (1) $120\,\mathrm{Hz}$
- (2) Zero
- (3) $30\,\mathrm{Hz}$
- **(4)** $60\,\mathrm{Hz}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In half wave rectifier, the output frequency is same as that of input frequency.

**Solved independently** (answer withheld)

1. In half-wave rectification only one half-cycle of each input cycle is passed, giving one output pulse per input cycle.
2. Hence $f_{out} = f_{in} = 60\,\mathrm{Hz}$, which is option $4$.

**Subtopic:** Half Wave Rectifier · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q031_5b6f8ede_04112026.png?v=5b6f8ede788e)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q031_e6787216_04112026.png?v=e6787216d561)

---

## Q32

Physics · Rotational Motion

The ratio of the radius of gyration of a thin uniform disc about an axis passing through its centre and normal to its plane to the radius of gyration of the disc about its diameter is

- (1) $1:\sqrt{2}$
- (2) $2:1$
- **(3)** $\sqrt{2}:1$
- (4) $4:1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: A thin disc with its rotation axis normal to the plane through the centre (into the page), with a curved arrow showing rotation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q032_sol_1_595e113b_04112026.png?v=595e113b0160)

*A thin disc with its rotation axis normal to the plane through the centre (into the page), with a curved arrow showing rotation*

![drawn: A thin disc with its rotation axis normal to the plane through the centre (into the page), with a curved arrow showing rotation](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q032_solution_1_ea8f6624_14112026.svg?v=ea8f6624c997)  
*drawn by code/lib/physics_figure.py*

1. $I_1 = \frac{MR^2}{2}$
2. $k_1 = \sqrt{\frac{I_1}{M}}$
3. $= \frac{R}{\sqrt{2}}$

![printed figure: A thin disc seen edge-on in its plane with a vertical axis along a diameter and a rotation arrow](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q032_sol_2_8624314b_04112026.png?v=8624314b9561)

*A thin disc seen edge-on in its plane with a vertical axis along a diameter and a rotation arrow*

![drawn: A thin disc seen edge-on in its plane with a vertical axis along a diameter and a rotation arrow](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q032_solution_2_f6b54f46_14112026.svg?v=f6b54f464613)  
*drawn by code/lib/physics_figure.py*

4. $I_2 = \frac{MR^2}{4}$
5. $k_2 = \sqrt{\frac{I_2}{M}}$
6. $= \frac{R}{2}$
7. $\frac{k_1}{k_2} = \frac{\frac{R}{\sqrt{2}}}{\frac{R}{2}}$
8. $= \sqrt{2}:1$

**Solved independently** (answer withheld)

1. For a thin uniform disc about the axis through the centre normal to its plane, $I_1 = \frac{MR^2}{2}$, so $k_1 = \sqrt{\frac{I_1}{M}} = \frac{R}{\sqrt{2}}$.
2. By the perpendicular axis theorem, $I_1 = 2I_d$, so $I_d = \frac{MR^2}{4}$.
3. Hence $k_2 = \sqrt{\frac{I_d}{M}} = \frac{R}{2}$.
4. $\frac{k_1}{k_2} = \frac{R/\sqrt{2}}{R/2} = \frac{2}{\sqrt{2}} = \sqrt{2}$, so the ratio is $\sqrt{2}:1$, which is option $3$.

**Subtopic:** Radius of Gyration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q032_e0c21690_04112026.png?v=e0c21690a68a)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q032_1b2d5f23_04112026.png?v=1b2d5f230c89)

---

## Q33

Physics · Ray Optics

A light ray falls on a glass surface of refractive index $\sqrt{3}$ , at an angle $60^\circ$. The angle between the refracted and reflected rays would be

- (1) $120^\circ$
- (2) $30^\circ$
- (3) $60^\circ$
- **(4)** $90^\circ$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Given $i = 60^\circ$ and $\mu = \sqrt{3}$
2. $\Rightarrow$ Here, angle of incidence $\Rightarrow i = \tan^{-1}(\mu)$
3. Hence, reflected and refracted rays would be perpendicular to each other.

**Solved independently** (answer withheld)

1. Snell's law: $\sin 60^\circ = \sqrt{3}\,\sin r$.
2. $\sin r = \frac{\sqrt{3}/2}{\sqrt{3}} = \frac{1}{2}$, so $r = 30^\circ$.
3. The reflected ray makes $60^\circ$ with the normal on the incident side; the refracted ray makes $30^\circ$ with the normal on the other side.
4. Angle between them $= 180^\circ - 60^\circ - 30^\circ = 90^\circ$, which is option $4$ (consistent with Brewster's law, $\tan 60^\circ = \sqrt{3}$).

**Subtopic:** Snell's Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q033_87ab1d64_04112026.png?v=87ab1d64872e)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q033_825667de_04112026.png?v=825667de707a)

---

## Q34

Physics · Modern Physics

In the given nuclear reaction, the element $X$ is
$^{22}_{11}\mathrm{Na} \rightarrow X + e^{+} + \nu$

- (1) $^{22}_{12}\mathrm{Mg}$
- (2) $^{23}_{11}\mathrm{Na}$
- (3) $^{23}_{10}\mathrm{Ne}$
- **(4)** $^{22}_{10}\mathrm{Ne}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The nuclear reaction is given as
2. $^{22}_{11}\mathrm{Na} \rightarrow\, ^{A}_{Z}X + \,_{+1}e^{0} + \nu$
3. From conservation of atomic number
4. $11 = Z + 1 \Rightarrow Z = 10 \Rightarrow \mathrm{Ne}$
5. From conservation of mass number
6. $22 = A + 0 \Rightarrow A = 22$
7. $\therefore\ ^{A}_{Z}X = \,^{22}_{10}\mathrm{Ne}$

**Solved independently** (answer withheld)

1. Conserve mass number: $22 = A_X + 0 + 0 \Rightarrow A_X = 22$.
2. Conserve charge: $11 = Z_X + 1 + 0 \Rightarrow Z_X = 10$.
3. $Z = 10$ is neon, so $X = \mathrm{{}^{22}_{10}Ne}$, which is option $4$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q034_be5f8049_04112026.png?v=be5f8049fedd)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q034_ac6e6957_04112026.png?v=ac6e6957fe95)

---

## Q35

Physics · Modern Physics

Let $T_1$ and $T_2$ be the energy of an electron in the first and second excited states of hydrogen atoms, respectively. According to the Bohr's model of an atom, the ratio $T_1 : T_2$ is

- **(1)** $9 : 4$
- (2) $1 : 4$
- (3) $4 : 1$
- (4) $4 : 9$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $E_n = \frac{E_0}{n^2}$, For first excited state $\Rightarrow n = 2$
2. For second excited state $\Rightarrow n = 3$
3. $\Rightarrow \frac{T_1}{T_2} = \frac{\frac{E_0}{4}}{\frac{E_0}{9}} = \frac{9}{4}$

**Solved independently** (answer withheld)

1. The first excited state is $n=2$ and the second excited state is $n=3$.
2. In Bohr's model $E_n = -\frac{13.6}{n^2}\,\text{eV}$, so $E_n \propto \frac{1}{n^2}$.
3. $\frac{T_1}{T_2} = \frac{1/2^2}{1/3^2} = \frac{9}{4}$.
4. $T_1 : T_2 = 9 : 4$, which is option $1$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q035_70cbaf5c_04112026.png?v=70cbaf5ccc1d)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q035_8612d129_04112026.png?v=8612d12948d1)

---

## Q36

Physics · Alternating Current

A series LCR circuit with inductance $10\,\mathrm{H}$, capacitance $10\,\mu\mathrm{F}$ , resistance $50\,\Omega$ is connected to an ac source of voltage, $V = 200\sin(100t)$ volt. If the resonant frequency of the LCR circuit is $\nu_0$ and the frequency of the ac source is $\nu$ , then

- (1) $\nu = 100\,\mathrm{Hz}$; $\nu_0 = \dfrac{100}{\pi}\,\mathrm{Hz}$
- (2) $\nu_0 = \nu = 50\,\mathrm{Hz}$
- **(3)** $\nu_0 = \nu = \dfrac{50}{\pi}\,\mathrm{Hz}$
- (4) $\nu_0 = \dfrac{50}{\pi}\,\mathrm{Hz}$, $\nu = 50\,\mathrm{Hz}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\omega L = \frac{1}{\omega C}$
2. $\omega = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10\times 10\times 10^{-6}}}$
3. $\omega = 100$
4. $\omega = 2\pi f \Rightarrow f = \frac{\omega}{2\pi}$
5. $\nu_0 = f_0 = \frac{100}{2\pi} = \frac{50}{\pi}\ \mathrm{Hz},\quad \omega = 100$
6. $\nu = f = \frac{100}{2\pi} = \frac{50}{\pi}$

**Solved independently** (answer withheld)

1. $LC = 10\,\mathrm{H} \times 10 \times 10^{-6}\,\mathrm{F} = 10^{-4}\,\mathrm{s^2}$.
2. $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10^{-4}}} = 100\,\mathrm{rad/s}$.
3. $\nu_0 = \frac{\omega_0}{2\pi} = \frac{100}{2\pi} = \frac{50}{\pi}\,\mathrm{Hz}$.
4. From $V = 200\sin(100t)$, the source $\omega = 100\,\mathrm{rad/s}$, so $\nu = \frac{100}{2\pi} = \frac{50}{\pi}\,\mathrm{Hz}$.
5. $\nu_0 = \nu = \frac{50}{\pi}\,\mathrm{Hz}$, which is option $3$.

**Subtopic:** Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q036_ac64cd68_04112026.png?v=ac64cd6843f3)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q036_cc36e654_04112026.png?v=cc36e65467ff)

---

## Q37

Physics · Kinematics

A ball is projected with a velocity, $10\,\mathrm{ms^{-1}}$, at an angle of $60^\circ$ with the vertical direction. Its speed at the highest point of its trajectory will be

- (1) $10\,\mathrm{ms^{-1}}$
- (2) Zero
- **(3)** $5\sqrt{3}\,\mathrm{ms^{-1}}$
- (4) $5\,\mathrm{ms^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. At highest point vertical component of velocity become zero.

![printed figure: Projectile launched at 10 m/s, 60 degrees from the vertical (30 degrees above horizontal), with horizontal velocity 10cos30 at the top](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q037_sol_1_880b8811_04112026.png?v=880b881108a7)

*Projectile launched at 10 m/s, 60 degrees from the vertical (30 degrees above horizontal), with horizontal velocity 10cos30 at the top*

![drawn: Projectile launched at 10 m/s, 60 degrees from the vertical (30 degrees above horizontal), with horizontal velocity 10cos30 at the top](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q037_solution_1_5be095eb_14112026.svg?v=5be095eb3b19)  
*drawn by code/lib/physics_figure.py*

2. At highest point speed of object $= 10\cos 30^\circ$
3. $= 5\sqrt{3}\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. At the highest point the vertical velocity is zero, so the speed equals the horizontal component $u_x$.
2. The angle $60^\circ$ is with the vertical, so $u_x = u\sin 60^\circ$.
3. $u_x = 10 \times \frac{\sqrt{3}}{2} = 5\sqrt{3}\,\mathrm{ms^{-1}}$, which is option $3$.

**Subtopic:** Projectile Motion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q037_35e92f99_04112026.png?v=35e92f9917ac)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q037_d180c12e_04112026.png?v=d180c12ea4c0)

---

## Q38

Physics · Capacitance

A capacitor of capacitance $C = 900\,\mathrm{pF}$ is charged fully by $100\,\mathrm{V}$ battery $B$ as shown in figure (a). Then it is disconnected from the battery and connected to another uncharged capacitor of capacitance $C = 900\,\mathrm{pF}$ as shown in figure (b). The electrostatic energy stored by the system (b) is

![printed figure: (a) capacitor C charged by a 100 V battery B; (b) the charged capacitor C connected across an uncharged capacitor C](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q038_f259af5a_04112026.png?v=f259af5a25a5)

*(a) capacitor C charged by a 100 V battery B; (b) the charged capacitor C connected across an uncharged capacitor C*

![drawn: (a) capacitor C charged by a 100 V battery B; (b) the charged capacitor C connected across an uncharged capacitor C](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q038_question_056df138_14112026.svg?v=056df138d6b0)  
*drawn by code/lib/physics_figure.py*

- (1) $1.5 \times 10^{-6}\,\mathrm{J}$
- (2) $4.5 \times 10^{-6}\,\mathrm{J}$
- (3) $3.25 \times 10^{-6}\,\mathrm{J}$
- **(4)** $2.25 \times 10^{-6}\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $q_1 = CV$
2. $= 900 \times 10^{-12} \times 100$
3. $= 9 \times 10^{-8}\,\mathrm{C}$

![printed figure: Charged capacitor C with +/- charges across a 100 V potential difference (open leads)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q038_sol_1_399746ed_04112026.png?v=399746ed8b21)

*Charged capacitor C with +/- charges across a 100 V potential difference (open leads)*

![drawn: Charged capacitor C with +/- charges across a 100 V potential difference (open leads)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q038_solution_1_29bd3241_14112026.svg?v=29bd3241fdb7)  
*drawn by code/lib/physics_figure.py*

4. $V = \frac{C_1V_1 + C_2V_2}{C_1 + C_2}$
5. $= \frac{9 \times 10^{-8} + 0}{1800 \times 10^{-12}} = \frac{100}{2} = 50\,\mathrm{V}$
6. $U = \frac{1}{2}\left(C_1 + C_2\right)V^2$
7. $= \frac{1}{2} \times 1800 \times 10^{-12} \times 50 \times 50$
8. $= 225 \times 10^{-8}$
9. $U = 2.25 \times 10^{-6}\,\mathrm{J}$

![printed figure: Charged capacitor C connected in a loop with an identical capacitor C, charges shown](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q038_sol_2_cb24b9df_04112026.png?v=cb24b9df663e)

*Charged capacitor C connected in a loop with an identical capacitor C, charges shown*

![drawn: Charged capacitor C connected in a loop with an identical capacitor C, charges shown](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q038_solution_2_905277a5_14112026.svg?v=905277a54424)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Initial charge: $Q = CV = 900\times10^{-12} \times 100 = 9\times10^{-8}\,\mathrm{C}$.
2. On connecting to an identical uncharged capacitor, charge is conserved and shared: $V_{common} = \frac{Q}{2C} = \frac{9\times10^{-8}}{1800\times10^{-12}} = 50\,\mathrm{V}$.
3. Energy of system (b): $U = \frac{1}{2}(2C)V_{common}^2 = \frac{1}{2}(1800\times10^{-12})(50)^2$.
4. $U = 2.25\times10^{-6}\,\mathrm{J}$, which is option $4$ (half the initial $4.5\times10^{-6}\,\mathrm{J}$).

**Subtopic:** Redistribution of Charges, Energy Stored in a Capacitor · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q038_db23c208_04112026.png?v=db23c2082a32)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q038_8714b675_04112026.png?v=8714b675c6f0)

---

## Q39

Physics · Modern Physics

A nucleus of mass number $189$ splits into two nuclei having mass number $125$ and $64$. The ratio of radius of two daughter nuclei respectively is

- (1) $25 : 16$
- (2) $1 : 1$
- (3) $4 : 5$
- **(4)** $5 : 4$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Radius of nuclei with mass number $A$ varies as
2. $R = R_0 A^{1/3}$
3. $\frac{R_1}{R_2} = \left(\frac{125}{64}\right)^{1/3} = \frac{5}{4} = 5:4$

**Solved independently** (answer withheld)

1. Nuclear radius $R = R_0 A^{1/3}$.
2. $\frac{R_1}{R_2} = \left(\frac{125}{64}\right)^{1/3}$.
3. $\left(\frac{125}{64}\right)^{1/3} = \frac{5}{4}$, so the ratio is $5:4$, which is option $4$.

**Subtopic:** Distance of Closest Approach and Size of Nucleus · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q039_a0d0a1ad_04112026.png?v=a0d0a1ad7753)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q039_989ae74c_04112026.png?v=989ae74c3e7d)

---

## Q40

Physics · Current Electricity

A wheatstone bridge is used to determine the value of unknown resistance $X$ by adjusting the variable resistance $Y$ as shown in the figure. For the most precise measurement of $X$, the resistances $P$ and $Q$

![printed figure: Wheatstone bridge: P, X in upper arms, Q, Y in lower arms, galvanometer across, cell E in outer loop](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q040_7716611f_04112026.png?v=7716611fcf3a)

*Wheatstone bridge: P, X in upper arms, Q, Y in lower arms, galvanometer across, cell E in outer loop*

![drawn: Wheatstone bridge: P, X in upper arms, Q, Y in lower arms, galvanometer across, cell E in outer loop](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q040_question_67110dc8_14112026.svg?v=67110dc8f816)  
*drawn by code/lib/physics_figure.py*

- (1) Do not play any significant role
- (2) Should be approximately equal to $2X$
- **(3)** Should be approximately equal and are small
- (4) Should be very large and unequal

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know, a wheatstone bridge is said to be most precise when it is most sensitive. This can be done by making ratio arms equal.
2. Thus (3) is correct option.

**Solved independently** (answer withheld)

1. At balance $\frac{P}{Q} = \frac{X}{Y}$, so $X = \frac{P}{Q}Y$.
2. Galvanometer sensitivity is greatest when all four arms are of the same order, $P \approx Q \approx X \approx Y$.
3. So $P$ and $Q$ should be approximately equal and comparable to (small, like) $X$; very large or unequal values reduce sensitivity, and they clearly matter.
4. This matches option $3$.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 17)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q040_3c808e62_04112026.png?v=3c808e62e5d0)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q040_ed249d64_04112026.png?v=ed249d643687)

---

## Q41

Physics · Thermodynamics

The volume occupied by the molecules contained in $4.5\,\mathrm{kg}$ water at STP, if the intermolecular forces vanish away is

- **(1)** $5.6\,\mathrm{m^3}$
- (2) $5.6 \times 10^{6}\,\mathrm{m^3}$
- (3) $5.6 \times 10^{3}\,\mathrm{m^3}$
- (4) $5.6 \times 10^{-3}\,\mathrm{m^3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. From ideal gas equation
2. $PV = nRT$
3. $\left[n = \frac{\text{mass of water}}{\text{mol. wt.}} = \frac{4.5\times10^{3}}{18}\right]$
4. $V = \frac{nRT}{P}$
5. At. STP $\Rightarrow T = 273\,\mathrm{K}$
6. $P = 10^{5}\,\mathrm{N/m^{2}}$
7. $V = \frac{4.5\times10^{3}}{18}\times\frac{8.3\times273}{10^{5}} = 5.66\,\mathrm{m^{3}}$

**Solved independently** (answer withheld)

1. Moles of water: $n = \frac{4500\,\text{g}}{18\,\text{g/mol}} = 250\,\text{mol}$.
2. If intermolecular forces vanish, the molecules behave as an ideal gas occupying molar volume at STP: $V_m = 22.4\,\text{L/mol}$.
3. Total volume: $V = 250 \times 22.4\,\text{L} = 5600\,\text{L} = 5.6\,\text{m}^3$, matching option 1.

**Subtopic:** Ideal Gas Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q041_d62f7f20_04112026.png?v=d62f7f20350f)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q041_8982a1ed_04112026.png?v=8982a1ed5252)

---

## Q42

Physics · Electrostatics

Two point charges $-q$ and $+q$ are placed at a distance of $L$, as shown in the figure. The magnitude of electric field intensity at a distance $R(R \gg L)$ varies as:

![printed figure: Two point charges −q and +q separated by distance L, with a double arrow marking L](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q042_11503738_04112026.png?v=11503738f1e9)

*Two point charges −q and +q separated by distance L, with a double arrow marking L*

![drawn: Two point charges −q and +q separated by distance L, with a double arrow marking L](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q042_question_cb0787e0_14112026.svg?v=cb0787e0fc16)  
*drawn by code/lib/physics_figure.py*

- (1) $\dfrac{1}{R^{6}}$
- (2) $\dfrac{1}{R^{2}}$
- **(3)** $\dfrac{1}{R^{3}}$
- (4) $\dfrac{1}{R^{4}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For $R \gg L$, arrangement is an electric dipole
2. $E = \frac{2p}{4\pi\varepsilon_0 R^{3}}$; where $p = qL$
3. $E \propto \frac{1}{R^{3}}$

**Solved independently** (answer withheld)

1. The charges $-q$ and $+q$ separated by $L$ form an electric dipole with moment $p = qL$.
2. For $R \gg L$, the dipole field at any point is $E = \frac{kp}{R^{3}}\sqrt{3\cos^{2}\theta + 1}$.
3. Hence $E \propto \frac{1}{R^{3}}$, which is option $3$.

**Subtopic:** Electric Field Due to Electric Dipole · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q042_635b0017_04112026.png?v=635b00174680)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q042_c7e2daa9_04112026.png?v=c7e2daa95a1e)

---

## Q43

Physics · Mechanical Properties of Solids

Given below are two statements : One is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.
In the light of the above statements, choose the most appropriate answer from the options given below

- Assertion (A) The stretching of a spring is determined by the shear modulus of the material of the spring.
- Reason (R) A coil spring of copper has more tensile strength than a steel spring of same dimensions.

- (1) (A) is false but (R) is true
- (2) Both (A) and (R) are true and (R) is the correct explanation of (A)
- (3) Both (A) and (R) are true and (R) is not the correct explanation of (A)
- **(4)** (A) is true but (R) is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. It is true that stretching of spring is determined by shear modulus of the spring as when coil spring is stretched neither its length nor its volume changes, there is only change in its shape.
2. Tensile strength of steel is more than that of copper.
3. Hence Assertion is true and reason is false.

**Solved independently** (answer withheld)

1. Assertion: For a helical spring, the wire undergoes torsion/shear when stretched, so the spring constant depends on the shear modulus $G$ of the material — this is correct physics.
2. Reason: Tensile strength of steel is greater than that of copper, so a copper spring does NOT have more tensile strength than a steel spring of same dimensions — this statement is false.
3. Hence (A) is true but (R) is false, matching option 4.

**Subtopic:** Shear Modulus of Rigidity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q043_767c8c80_04112026.png?v=767c8c80e69c)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q043_1e7e543d_04112026.png?v=1e7e543d4975)

---

## Q44

Physics · Units and Measurements

Match List-I with List-II

| List-I | | List-II | |
|---|---|---|---|
| (a) | Gravitational constant (G) | (i) | $[\mathrm{L^2T^{-2}}]$ |
| (b) | Gravitational potential energy | (ii) | $[\mathrm{M^{-1}L^3T^{-2}}]$ |
| (c) | Gravitational potential | (iii) | $[\mathrm{LT^{-2}}]$ |
| (d) | Gravitational intensity | (iv) | $[\mathrm{ML^2T^{-2}}]$ |

- (1) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii)
- (2) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii)
- **(3)** (a) - (ii), (b) - (iv), (c) - (i), (d) - (iii)
- (4) (a) - (ii), (b) - (iv), (c) - (iii), (d) - (i)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (a) $[\mathrm{G}] = \frac{Fr^{2}}{m_1 m_2}$
2. $[\mathrm{G}] = \frac{Fr^{2}}{m_1 m_2} = \frac{[\mathrm{MLT^{-2}}]\,\mathrm{L^{2}}}{[\mathrm{MM}]} = [\mathrm{M^{-1}L^{3}T^{-2}}]$
3. (b) Gravitational potential energy $= [\mathrm{ML^{2}T^{-2}}]$
4. (c) Gravitational potential $= \frac{\mathrm{PE}}{m} = [\mathrm{L^{2}T^{-2}}]$
5. (d) Gravitational field intensity $= \frac{F}{m} = [\mathrm{LT^{-2}}]$

**Solved independently** (answer withheld)

1. Gravitational constant: from $F=Gm_1m_2/r^2$, $G=[M^{-1}L^3T^{-2}]$ → matches (ii).
2. Gravitational potential energy: same as energy, $[ML^2T^{-2}]$ → matches (iv).
3. Gravitational potential: energy per unit mass, $[ML^2T^{-2}]/[M]=[L^2T^{-2}]$ → matches (i).
4. Gravitational intensity: force per unit mass = acceleration, $[LT^{-2}]$ → matches (iii).
5. This combination corresponds to option 3.

**Subtopic:** Dimensional Formulae · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 18)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q044_01e3d61f_04112026.png?v=01e3d61f3504)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q044_128e917c_04112026.png?v=128e917c042f)

---

## Q45

Physics · Semiconductor Electronics

The truth table for the given logic circuit is

![printed figure: Logic circuit: A and B feed two NAND gates (one via a NOT gate) whose outputs feed an AND gate giving C](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q045_b5dce54a_04112026.png?v=b5dce54acfe4)

*Logic circuit: A and B feed two NAND gates (one via a NOT gate) whose outputs feed an AND gate giving C*

![drawn: Logic circuit: A and B feed two NAND gates (one via a NOT gate) whose outputs feed an AND gate giving C](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q045_question_4ae4f3fd_14112026.svg?v=4ae4f3fde52e)  
*drawn by code/lib/physics_figure.py*

- (1) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$
- (2) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (3) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$
- **(4)** $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $C = \left(\overline{A \cdot B}\right) \cdot \left(\overline{\bar{A} \cdot B}\right)$
2. $\Rightarrow\ C = \overline{A \cdot B + \bar{A} \cdot B}$
3. $\Rightarrow\ C = \overline{\left(A + \bar{A}\right)B}$
4. $\Rightarrow\ C = \bar{B}$
5. The truth table would be
6. $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$

![printed figure: Two NAND gates (one input of the lower one through a NOT gate) feeding an AND gate with output C](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q045_sol_1_783ab0af_04112026.png?v=783ab0afeced)

*Two NAND gates (one input of the lower one through a NOT gate) feeding an AND gate with output C*

![drawn: Two NAND gates (one input of the lower one through a NOT gate) feeding an AND gate with output C](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q045_solution_1_b63a688a_14112026.svg?v=b63a688a4b88)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. From the figure, the top NAND gate takes inputs $A$ and $B$, so its output is $\overline{AB}$.
2. The bottom NAND gate takes $\bar{A}$ (through the NOT gate) and $B$, so its output is $\overline{\bar{A}B}$.
3. The AND gate gives $C = \overline{AB}\cdot\overline{\bar{A}B} = (\bar{A}+\bar{B})(A+\bar{B})$.
4. $(\bar{A}+\bar{B})(A+\bar{B}) = \bar{B} + A\bar{A} = \bar{B}$.
5. So $C = 1, 0, 1, 0$ for $AB = 00, 01, 10, 11$, which is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 19)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q045_a38e8fbb_04112026.png?v=a38e8fbb2170)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q045_73b1727d_04112026.png?v=73b1727d2e5a)

---

## Q46

Physics · Ray Optics

Two transparent media $A$ and $B$ are separated by a plane boundary. The speed of light in those media are $1.5 \times 10^{8}\,\mathrm{m/s}$ and $2.0 \times 10^{8}\,\mathrm{m/s}$, respectively. The critical angle for a ray of light for these two media is

- (1) $\tan^{-1}(0.750)$
- (2) $\sin^{-1}(0.500)$
- **(3)** $\sin^{-1}(0.750)$
- (4) $\tan^{-1}(0.500)$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Ray in medium A meeting the A-B boundary at the critical angle and grazing along it](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q046_sol_1_df9ad742_04112026.png?v=df9ad7423fb3)

*Ray in medium A meeting the A-B boundary at the critical angle and grazing along it*

![drawn: Ray in medium A meeting the A-B boundary at the critical angle and grazing along it](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q046_solution_1_17fe58c7_14112026.svg?v=17fe58c74c8e)  
*drawn by code/lib/physics_figure.py*

1. $\mu_A = \frac{3\times 10^{8}}{1.5\times 10^{8}} = 2$
2. $\mu_B = \frac{3\times 10^{8}}{2\times 10^{8}} = 1.5$
3. For TIR, ray of light should travel from denser to rarer medium
4. $\mu_A \sin\theta_C = \mu_B \sin 90^\circ$
5. $2\sin\theta_C = 1.5\sin 90^\circ$
6. $\sin\theta_C = 0.75$
7. $\theta_C = \sin^{-1}(0.75)$

**Solved independently** (answer withheld)

1. Light is slower in $A$ ($1.5 \times 10^{8}\,\mathrm{m/s}$) than in $B$ ($2.0 \times 10^{8}\,\mathrm{m/s}$), so $A$ is the denser medium and total internal reflection happens for light going from $A$ to $B$.
2. $\sin C = \frac{n_B}{n_A}$.
3. $\frac{n_B}{n_A} = \frac{c/v_B}{c/v_A} = \frac{v_A}{v_B}$.
4. $\sin C = \frac{1.5 \times 10^{8}}{2.0 \times 10^{8}} = 0.750$.
5. $C = \sin^{-1}(0.750)$, which is option $3$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q046_fc4dc160_04112026.png?v=fc4dc160803f)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q046_7a28852d_04112026.png?v=7a28852de6b8)

---

## Q47

Physics · Units and Measurements

The area of a rectangular field (in $\mathrm{m^2}$) of length $55.3\,\mathrm{m}$ and breadth $25\,\mathrm{m}$ after rounding off the value for correct significant digits is

- **(1)** $14 \times 10^{2}$
- (2) $138 \times 10^{1}$
- (3) $1382$
- (4) $1382.5$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Area $=$ Length $\times$ Breadth
2. $= 55.3 \times 25\,\mathrm{m^2}$
3. $= 1382.5\,\mathrm{m^2}$
4. $= 14 \times 10^{2}\,\mathrm{m^2}$ (Rounding off of two significant figures)

**Solved independently** (answer withheld)

1. $A = l \times b = 55.3\,\mathrm{m} \times 25\,\mathrm{m} = 1382.5\,\mathrm{m^2}$.
2. In multiplication the result keeps as many significant figures as the factor with the fewest: $55.3$ has 3, $25$ has 2, so keep 2.
3. Rounding $1382.5$ to 2 significant figures gives $1.4 \times 10^{3} = 14 \times 10^{2}\,\mathrm{m^2}$, which is option $1$.

**Subtopic:** Significant Figures · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q047_c3313eab_04112026.png?v=c3313eab3614)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q047_cbafeaec_04112026.png?v=cbafeaecdb33)

---

## Q48

Physics · Electromagnetic Induction

A big circular coil of 1000 turns and average radius $10\,\mathrm{m}$ is rotating about its horizontal diameter at $2\,\mathrm{rad\ s^{-1}}$. If the vertical component of earth's magnetic field at that place is $2\times10^{-5}\,\mathrm{T}$ and electrical resistance of the coil is $12.56\,\Omega$, then the maximum induced current in the coil will be

- (1) $2\,\mathrm{A}$
- (2) $0.25\,\mathrm{A}$
- (3) $1.5\,\mathrm{A}$
- **(4)** $1\,\mathrm{A}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\phi_B = NBA\cos\omega t$
2. $\varepsilon = \frac{-d\phi_B}{dt} = -NBA\omega(-\sin\omega t)$
3. $\varepsilon = NBA\omega\sin\omega t$
4. $i_{\max} = \frac{\varepsilon_{\max}}{R} = \frac{NBA\omega}{R}$
5. $= \frac{1000\times 2\times 10^{-5}\times \pi(10)^{2}\times 2}{12.56}$
6. $= 1\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Rotating about a horizontal diameter, the flux through the coil comes from the vertical component $B_V = 2\times10^{-5}\,\mathrm{T}$.
2. $A = \pi r^2 = \pi (10)^2 = 100\pi \approx 314\,\mathrm{m^2}$.
3. $\varepsilon_{max} = N B_V A \omega = 1000 \times 2\times10^{-5} \times 100\pi \times 2 = 4\pi \approx 12.56\,\mathrm{V}$.
4. $I_{max} = \frac{\varepsilon_{max}}{R} = \frac{12.56}{12.56} = 1\,\mathrm{A}$, which is option $4$.

**Subtopic:** AC Generator · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q048_f456bf3b_04112026.png?v=f456bf3bce98)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q048_1683eaee_04112026.png?v=1683eaee7f13)

---

## Q49

Physics · Magnetic Effect of Electric Current

From Ampere's circuital law for a long straight wire of circular cross-section carrying a steady current, the variation of magnetic field in the inside and outside region of the wire is

- (1) A linearly decreasing function of distance upto the boundary of the wire and then a linearly increasing one for the outside region.
- (2) Uniform and remains constant for both the regions.
- (3) A linearly increasing function of distance upto the boundary of the wire and then linearly decreasing for the outside region.
- **(4)** A linearly increasing function of distance $r$ upto the boundary of the wire and then decreasing one with $\frac{1}{r}$ dependence for the outside region.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For solid wire
2. Inside point
3. $B = \frac{\mu_0 I r^2}{R^2 \times 2\pi r}$
4. $= \frac{\mu_0 I r}{R^2 \times 2\pi}$
5. $B \propto r$
6. Outside point
7. $B = \frac{\mu_0 I}{2\pi r}$
8. $B \propto \frac{1}{r}$

**Solved independently** (answer withheld)

1. For $r < R$, the enclosed current is $I_{enc} = I\frac{r^2}{R^2}$ (uniform current density).
2. Ampere's law: $B(2\pi r) = \mu_0 I \frac{r^2}{R^2} \Rightarrow B = \frac{\mu_0 I r}{2\pi R^2} \propto r$.
3. For $r > R$, $I_{enc} = I$, so $B(2\pi r) = \mu_0 I \Rightarrow B = \frac{\mu_0 I}{2\pi r} \propto \frac{1}{r}$.
4. Linear increase inside, $\frac{1}{r}$ decrease outside, which is option $4$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 21)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q049_906d96a5_04112026.png?v=906d96a597c3)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q049_2446bb0a_04112026.png?v=2446bb0aa684)

---

## Q50

Physics · Oscillations

Two pendulums of length $121\,\mathrm{cm}$ and $100\,\mathrm{cm}$ start vibrating in phase. At some instant, the two are at their mean position in the same phase. The minimum number of vibrations of the shorter pendulum after which the two are again in phase at the mean position is:

- (1) 8
- **(2)** 11
- (3) 9
- (4) 10

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $T = 2\pi\sqrt{\frac{L}{g}}$
2. Let $n_1$ and $n_2$ be integer.
3. $n_1 T_1 = n_2 T_2$
4. $2\pi n_1\sqrt{\frac{1.21}{g}} = 2\pi n_2\sqrt{\frac{1.00}{g}}$
5. $\Rightarrow \frac{n_2}{n_1} = \frac{11}{10}$
6. $\therefore$ After completion of $11^{\mathrm{th}}$ oscillation of shorter pendulum, it will be in phase with longer pendulum.

**Solved independently** (answer withheld)

1. For a simple pendulum $T = 2\pi\sqrt{\frac{l}{g}}$, so $T \propto \sqrt{l}$.
2. $\frac{T_{long}}{T_{short}} = \sqrt{\frac{121}{100}} = \frac{11}{10}$.
3. They are again in phase at the mean position when $n\,T_{short} = m\,T_{long}$ for whole numbers $n, m$.
4. $n\,T_{short} = m \cdot \frac{11}{10} T_{short} \Rightarrow 10n = 11m$.
5. The smallest whole-number solution is $n = 11$, $m = 10$, so the shorter pendulum makes $11$ vibrations, which is option $2$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 21)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q050_4e824b76_04112026.png?v=4e824b76f370)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q050_010d0d4b_04112026.png?v=010d0d4b2299)

---

## Q51

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The IUPAC name of an element with atomic number 119 is

- (1) ununoctium
- **(2)** ununennium
- (3) unnilennium
- (4) unununnium

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. IUPAC name of element : $119$ : ununennium

**Solved independently** (answer withheld)

1. IUPAC numerical roots: $0$ = nil, $1$ = un, $9$ = enn, $8$ = oct.
2. Atomic number $119$ has digits $1, 1, 9$, giving roots un + un + enn.
3. Add the suffix -ium: ununennium, which is option $2$.

**Subtopic:** Nomenclature of Elements with Atomic Numbers Greater Than 100 · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q051_bbbb8298_04112026.png?v=bbbb82988fd2)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q051_a2c7ed39_04112026.png?v=a2c7ed398afb)

---

## Q52

Chemistry · organic · Chemistry in Everyday Life

Match **List-I** with **List-II**.

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Antacids | (i) | Salvarsan |
| (b) | Antihistamines | (ii) | Morphine |
| (c) | Analgesics | (iii) | Cimetidine |
| (d) | Antimicrobials | (iv) | Seldane |

- (1) (a) - (iv), (b) – (iii), (c) – (i), (d) – (ii)
- (2) (a) - (iii), (b) – (ii), (c) – (iv), (d) – (i)
- **(3)** (a) - (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (4) (a) - (i), (b) – (iv), (c) – (ii), (d) – (iii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Cimetidine is an antacid
2. Seldane is an antihistamine
3. Morphine is an analgesic
4. Salvarsan is an antimicrobial drug

**Solved independently** (answer withheld)

1. Antacids: Cimetidine (iii) reduces gastric acid secretion by blocking H2 receptors.
2. Antihistamines: Seldane/terfenadine (iv) blocks H1 receptors for allergy relief.
3. Analgesics: Morphine (ii) is a classic opioid analgesic.
4. Antimicrobials: Salvarsan (i) is an early arsenic-based antimicrobial agent.
5. This matches option 3: (a)-(iii), (b)-(iv), (c)-(ii), (d)-(i).

**Subtopic:** Therapeutic Action of Different Classes of Drugs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q052_412a5375_04112026.png?v=412a53750751)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q052_91dac0eb_04112026.png?v=91dac0eb6478)

---

## Q53

Chemistry · physical · Basic Concepts of Chemistry

In one molal solution that contains $0.5$ mole of a solute, there is

- (1) $1000\,\mathrm{g}$ of solvent
- (2) $500\,\mathrm{mL}$ of solvent
- **(3)** $500\,\mathrm{g}$ of solvent
- (4) $100\,\mathrm{mL}$ of solvent

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Molality is the moles of solute dissolved per kg of solvent therefore $500$ g, $1$ molal solution contains $0.5$ of solute, as
2. $\mathrm{m} = \frac{\text{Moles of solute}}{\text{Mass of solvent (in kg)}}$
3. $1 = \frac{0.5}{\text{Mass of solvent (in kg)}}$
4. $\therefore$ Mass of solvent (in kg) $= 0.5 = 500\,\mathrm{g}$

**Solved independently** (answer withheld)

1. Molality is defined as $m = \frac{n_{\text{solute}}}{W_{\text{solvent}}\,(\mathrm{kg})}$.
2. Rearranging, $W_{\text{solvent}} = \frac{n_{\text{solute}}}{m} = \frac{0.5\,\mathrm{mol}}{1\,\mathrm{mol\,kg^{-1}}} = 0.5\,\mathrm{kg}$.
3. $0.5\,\mathrm{kg} = 500\,\mathrm{g}$ of solvent, which is option $3$.

**Subtopic:** Molality · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 22)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q053_13f1cd49_04112026.png?v=13f1cd49a2fe)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q053_2a1217c7_04112026.png?v=2a1217c736e2)

---

## Q54

Chemistry · organic · Polymers

Which statement regarding polymers is **not correct**?

- **(1)** Thermosetting polymers are reusable
- (2) Elastomers have polymer chains held together by weak intermolecular forces
- (3) Fibers possess high tensile strength
- (4) Thermoplastic polymers are capable of repeatedly softening and hardening on heating and cooling respectively

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Thermoplastic polymers are the linear or slightly long chain molecules capable of repeatedly softening and hardening on cooling.
2. Thermosetting polymers are cross-linked or heavily branched molecules, which on heating undergo extensive cross-linking in moulds and again become infusible. These cannot be reused.
3. Elastomers have polymer chains held together by weak intermolecular forces.
4. Fibres possess high tensile strength.

**Solved independently** (answer withheld)

1. Elastomers have polymer chains held by the weakest intermolecular forces, so option $2$ is correct.
2. Fibres have strong intermolecular forces (e.g. H-bonding), giving high tensile strength, so option $3$ is correct.
3. Thermoplastics can be repeatedly softened on heating and hardened on cooling, so option $4$ is correct.
4. Thermosetting polymers become extensively cross-linked and infusible on heating and cannot be reused, so option $1$ is the incorrect statement.

**Subtopic:** Classification of Polymers Based on Molecular Forces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q054_24e73be9_04112026.png?v=24e73be982c1)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q054_c8ec34d3_04112026.png?v=c8ec34d3f514)

---

## Q55

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

$\mathrm{RMgX} + \mathrm{CO_2} \xrightarrow[\text{ether}]{\text{dry}} \mathrm{Y} \xrightarrow{\mathrm{H_3O^+}} \mathrm{RCOOH}$
What is Y in the above reaction?

- (1) $\mathrm{(RCOO)_2Mg}$
- **(2)** $\mathrm{RCOO^-Mg^+X}$
- (3) $\mathrm{R_3CO^-Mg^+X}$
- (4) $\mathrm{RCOO^-X^+}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →($\ce{H3O+}$) $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q055_sol_1_56f11704_04112026.png?v=56f1170467f5)

*I. carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →[$\ce{H3O+}$] $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$*

![drawn: I. carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →($\ce{H3O+}$) $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q055_solution_1_6bdde457_14112026.svg?v=6bdde4579939)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Here Y is $\mathrm{RCOO^-Mg^+X}$

**Solved independently** (answer withheld)

1. Grignard reagent attacks the electrophilic carbon of CO2 to form a magnesium carboxylate salt.
2. This intermediate Y is RCOO^-Mg^+X.
3. On acidic hydrolysis (H3O+), Y gives RCOOH.

**Subtopic:** Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q055_aa410ef5_04112026.png?v=aa410ef5372d)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q055_751bcaa3_04112026.png?v=751bcaa37371)

---

## Q56

Chemistry · organic · Haloalkanes and Haloarenes

Which of the following sequence of reactions is suitable to synthesize chlorobenzene?

- (1) aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q056_option_1_s1_328bf375_14112026.svg?v=328bf375ec34) — , $\mathrm{HCl}$, Heating
- **(2)** Benzene, $\mathrm{Cl_2}$, anhydrous $\mathrm{FeCl_3}$
- (3) Phenol, $\mathrm{NaNO_2}$, $\mathrm{HCl}$, $\mathrm{CuCl}$
- (4) benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q056_option_4_s1_dbf27a87_14112026.svg?v=dbf27a872e50) — , $\mathrm{HCl}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. benzene + $\ce{Cl2}$ →(anhydrous FeCl3) chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q056_sol_1_6729b789_04112026.png?v=6729b7898e7a)

*I. benzene + $\ce{Cl2}$ →[anhydrous FeCl3] chlorobenzene*

![drawn: I. benzene + $\ce{Cl2}$ →(anhydrous FeCl3) chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q056_solution_1_f1cbb3e7_14112026.svg?v=f1cbb3e7e35e)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Benzene reacts with chlorine in presence of anhydrous $\mathrm{FeCl_3}$ to give chlorobenzene

**Solved independently** (answer withheld)

1. Benzene with $\mathrm{Cl_2}$ and anhydrous $\mathrm{FeCl_3}$ undergoes electrophilic substitution: $\mathrm{C_6H_6 + Cl_2 \xrightarrow{FeCl_3} C_6H_5Cl + HCl}$, giving chlorobenzene.
2. Phenol does not form a diazonium salt with $\mathrm{NaNO_2/HCl}$ (that needs a primary aromatic amine), so option $3$ fails.
3. Benzene does not react with $\mathrm{HCl}$ alone, so option $4$ fails.
4. Aniline with $\mathrm{HCl}$ on heating only forms anilinium chloride, not chlorobenzene (no diazotisation), so option $1$ fails.
5. Hence the suitable sequence is option $2$.

**Subtopic:** Preparation of Haloarenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q056_c44b9eaa_04112026.png?v=c44b9eaa6705)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q056_0af6fdb3_04112026.png?v=0af6fdb3f876)

---

## Q57

Chemistry · physical · Ionic Equilibrium

The pH of the solution containing $50\,\mathrm{mL}$ each of $0.10\,\mathrm{M}$ sodium acetate and $0.01\,\mathrm{M}$ acetic acid is [Given $\mathrm{p}K_a$ of $\mathrm{CH_3COOH} = 4.57$]

- (1) $2.57$
- **(2)** $5.57$
- (3) $3.57$
- (4) $4.57$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CH_3COONa} + \mathrm{CH_3COOH}$, $\mathrm{CH_3COOH}(\mathrm{p}K_a) = 4.57$
2. $0.1\,\mathrm{M}$        $0.01\,\mathrm{M}$
3. $50\,\mathrm{mL}$        $50\,\mathrm{mL}$
4. It is a mixture of weak acid and salt of its conjugate base. Hence it is acidic buffer.
5. $\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{Salt}]}{[\mathrm{Acid}]}$
6. $= 4.57 + \log\left(\frac{0.1}{0.01}\right)$
7. $= 4.57 + 1$
8. $= 5.57$

**Solved independently** (answer withheld)

1. Sodium acetate with acetic acid forms an acidic buffer, so $\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\text{salt}]}{[\text{acid}]}$.
2. Equal volumes ($50\,\mathrm{mL}$ each) are mixed, so the ratio is $\frac{[\text{salt}]}{[\text{acid}]} = \frac{0.10}{0.01} = 10$.
3. $\mathrm{pH} = 4.57 + \log 10 = 4.57 + 1 = 5.57$, which is option $2$.

**Subtopic:** Buffer Solutions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q057_0ccf1086_04112026.png?v=0ccf1086ce6b)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q057_e9191d5c_04112026.png?v=e9191d5c4cf5)

---

## Q58

Chemistry · inorganic · Coordination Compounds – Practice

The IUPAC name of the complex- $\mathrm{[Ag(H_2O)_2][Ag(CN)_2]}$ is:

- **(1)** diaquasilver(I) dicyanidoargentate(I)
- (2) dicyanidosilver(II) diaquaargentate(II)
- (3) diaquasilver(II) dicyanidoargentate(II)
- (4) dicyanidosilver(I) diaquaargentate(I)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{[Ag(H_2O)_2][Ag(CN)_2]}$
2. IUPAC name : diaquasilver(I)dicyanidoargentate(I)

**Solved independently** (answer withheld)

1. The salt splits into the cation $[\mathrm{Ag(H_2O)_2}]^{+}$ and the anion $[\mathrm{Ag(CN)_2}]^{-}$; the cation is named first.
2. Cation: $x + 2(0) = +1 \Rightarrow x = +1$, so it is diaquasilver(I).
3. Anion: $x + 2(-1) = -1 \Rightarrow x = +1$, and an anionic complex of Ag takes the name argentate, so it is dicyanidoargentate(I).
4. Full name: diaquasilver(I) dicyanidoargentate(I), which is option $1$.

**Subtopic:** IUPAC Nomenclature and Formulae of Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q058_10cd41bf_04112026.png?v=10cd41bf638e)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q058_edb4c474_04112026.png?v=edb4c47436a1)

---

## Q59

Chemistry · physical · Thermodynamics

Which of the following p-V curve represents maximum work done?

- (1) ![printed figure: p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a horizontal line at high p, then a curve falling steeply as V increases, ending at a short vertical drop to the V axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_option_1_a212e244_04112026.png?v=a212e24491ce) *p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a horizontal line at high p, then a curve falling steeply as V increases, ending at a short vertical drop to the V axis*
- (2) ![printed figure: p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a closed tilted elliptical cycle with arrows showing direction around the loop](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_option_2_436b941b_04112026.png?v=436b941b16b4) *p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a closed tilted elliptical cycle with arrows showing direction around the loop*
- **(3)** ![printed figure: p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a horizontal line at high p, then a curve falling gradually over a wide range of V, ending at a vertical drop to the V axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_option_3_b2e5571e_04112026.png?v=b2e5571eff1f) *p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a horizontal line at high p, then a curve falling gradually over a wide range of V, ending at a vertical drop to the V axis*
- (4) ![printed figure: p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a single vertical line at constant V](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_option_4_61beeca2_04112026.png?v=61beeca29cfb) *p-V graph labelled Isothermal: p on the vertical axis, V on the horizontal axis; a single vertical line at constant V*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Work done under any thermodynamic process can be determined by area under the 'p-V' graph.
2. As it can be observed maximum area is covered in option '3'.

![printed figure: 1. p-V graph: p on the vertical axis, V on the horizontal axis; a steeply falling curve with the area under it hatched](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_sol_1_211d6391_04112026.png?v=211d6391a87f)

*1. p-V graph: p on the vertical axis, V on the horizontal axis; a steeply falling curve with the area under it hatched*


![printed figure: 2. p-V graph: p on the vertical axis, V on the horizontal axis; a closed tilted ellipse with its enclosed area hatched](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_sol_2_8331ca98_04112026.png?v=8331ca986e80)

*2. p-V graph: p on the vertical axis, V on the horizontal axis; a closed tilted ellipse with its enclosed area hatched*


![printed figure: 3. p-V graph: p on the vertical axis, V on the horizontal axis; a gradually falling curve over a wide V range with the area under it hatched, pointed to by the label 'Maximum area'](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_sol_3_57083ce8_04112026.png?v=57083ce837e0)

*3. p-V graph: p on the vertical axis, V on the horizontal axis; a gradually falling curve over a wide V range with the area under it hatched, pointed to by the label 'Maximum area'*


![printed figure: 4. p-V graph: p on the vertical axis, V on the horizontal axis; a single vertical line at constant V, with w = 0 printed below](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q059_sol_4_5395f5c0_04112026.png?v=5395f5c0dfff)

*4. p-V graph: p on the vertical axis, V on the horizontal axis; a single vertical line at constant V, with w = 0 printed below*


**Solved independently** (answer withheld)

1. Work done equals the area under the $p$-$V$ curve, $W = \int p\,dV$.
2. Option $4$ is a vertical line ($\Delta V = 0$), so $W = 0$.
3. Option $2$ is a small closed cycle; its work is only the small enclosed loop area.
4. Options $1$ and $3$ are similar isothermal expansions, but option $3$ extends over a much larger $\Delta V$ and has the larger area under it.
5. So the maximum work is option $3$.

**Subtopic:** Work Done · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q059_27918e82_04112026.png?v=27918e820c68)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q059_4876f467_04112026.png?v=4876f467a7e3)

---

## Q60

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Amongst the following which one will have maximum ‘lone pair - lone pair’ electron repulsions?

- **(1)** $\mathrm{XeF_2}$
- (2) $\mathrm{ClF_3}$
- (3) $\mathrm{IF_5}$
- (4) $\mathrm{SF_4}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{SF_4} \rightarrow sp^3d + 1$ lone pair

![printed figure: sulfur tetrafluoride ($\ce{SF4}$): S with four F atoms and one lone pair](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q060_sol_1_e73d955b_04112026.png?v=e73d955b1fef)

*sulfur tetrafluoride ($\ce{SF4}$): S with four F atoms and one lone pair*

2. $\mathrm{XeF_2} \rightarrow sp^3d + 3$ lone pair

![printed figure: xenon difluoride ($\ce{XeF2}$): F–Xe–F linear with three lone pairs on Xe](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q060_sol_2_25bf9272_04112026.png?v=25bf92721690)

*xenon difluoride ($\ce{XeF2}$): F–Xe–F linear with three lone pairs on Xe*

3. $\mathrm{ClF_3} \rightarrow sp^3d + 2$ lone pair

![printed figure: chlorine trifluoride ($\ce{ClF3}$): Cl with three F atoms and two lone pairs (T-shaped)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q060_sol_3_43d4f0fb_04112026.png?v=43d4f0fb060e)

*chlorine trifluoride ($\ce{ClF3}$): Cl with three F atoms and two lone pairs (T-shaped)*

4. $\mathrm{IF_5} \rightarrow sp^3d^2 + 1$ lone pair

![printed figure: iodine pentafluoride ($\ce{IF5}$): I with five F atoms and one lone pair (square pyramidal)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q060_sol_4_b2e02e67_04112026.png?v=b2e02e67271b)

*iodine pentafluoride ($\ce{IF5}$): I with five F atoms and one lone pair (square pyramidal)*

5. $\mathrm{XeF_2}$ having maximum lone pairs, so, it has maximum ‘lone pair-lone pair’ electron repulsions.

**Solved independently** (answer withheld)

1. Determine electron geometry and lone pairs for each molecule using VSEPR (AXE notation).
2. $\mathrm{XeF_2}$: AX$_2$E$_3$ (sp$^3$d, trigonal bipyramidal) — 3 lone pairs occupy equatorial positions, giving 3 pairwise lp-lp interactions.
3. $\mathrm{ClF_3}$: AX$_3$E$_2$ (sp$^3$d, T-shaped) — 2 lone pairs equatorial, giving only 1 lp-lp interaction.
4. $\mathrm{IF_5}$: AX$_5$E$_1$ (sp$^3$d$^2$, square pyramidal) — only 1 lone pair, so no lp-lp repulsion.
5. $\mathrm{SF_4}$: AX$_4$E$_1$ (sp$^3$d, see-saw) — only 1 lone pair, so no lp-lp repulsion.
6. XeF2 has the greatest number of lone pairs and lp-lp interactions, hence maximum lone pair-lone pair repulsion.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q060_290ab96f_04112026.png?v=290ab96f14f1)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q060_d3e2eece_04112026.png?v=d3e2eece3e35)

---

## Q61

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

The Kjeldahl's method for the estimation of nitrogen can be used to estimate the amount of nitrogen in which one of the following compounds?

- (1) azobenzene `c1ccc(N=Nc2ccccc2)cc1` ![azobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q061_option_1_s1_c6c0919e_14112026.svg?v=c6c0919ef009)
- (2) 4-nitroaniline `Nc1ccc([N+](=O)[O-])cc1` ![4-nitroaniline](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q061_option_2_s1_931c9334_14112026.svg?v=931c9334e80a)
- (3) pyridine `c1ccncc1` ![pyridine](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q061_option_3_s1_8f43a2bd_14112026.svg?v=8f43a2bd6b55)
- **(4)** aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q061_option_4_s1_3051b9a1_14112026.svg?v=3051b9a1f0bc)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Kjeldahl method is not applicable to compounds containing nitrogen in nitro group, azo groups and nitrogen present in the ring (e.g., pyridine) as nitrogen of these compounds does not change to ammonium sulphate under these conditions.

**Solved independently** (answer withheld)

1. Kjeldahl's method cannot be used for nitro compounds, azo compounds or nitrogen present in a ring, since that N is not converted to $(\mathrm{NH_4})_2\mathrm{SO_4}$.
2. Option $1$ is azobenzene ($-N=N-$), option $2$ nitrobenzene ($-\mathrm{NO_2}$), option $3$ pyridine (ring N): all excluded.
3. Option $4$ is aniline ($\mathrm{C_6H_5NH_2}$), whose N is fully converted to ammonium sulfate, so option $4$.

**Subtopic:** Quantitative Analysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q061_a1914f05_04112026.png?v=a1914f05831b)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q061_e2204325_04112026.png?v=e220432560d8)

---

## Q62

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List-I with List-II.
List – I (Products formed)
List – II (Reaction of carbonyl compound with)
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cyanohydrin | (i) | $\mathrm{NH_2OH}$ |
| (b) | Acetal | (ii) | $\mathrm{RNH_2}$ |
| (c) | Schiff's base | (iii) | alcohol |
| (d) | Oxime | (iv) | $\mathrm{HCN}$ |

- **(1)** (a) – (iv), (b) – (iii), (c) – (ii), (d) – (i)
- (2) (a) – (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (3) (a) – (ii), (b) – (iii), (c) – (iv), (d) – (i)
- (4) (a) – (i), (b) – (iii), (c) – (ii), (d) – (iv)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. List – I (Products formed)    List – II (Reaction of carbonyl compound with)
2. (a) Cyanohydrin        (i) $\mathrm{HCN}$
3. (b) Acetal        (ii) Alcohol
4. (c) Schiff's base        (iii) $\mathrm{RNH_2}$
5. (d) Oxime        (iv) $\mathrm{NH_2OH}$
6. (a) – (iv), (b) – (iii), (c) – (ii), (d) – (i)

![printed figure: acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q062_sol_1_a48f8145_04112026.png?v=a48f814578e5)

*acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)*

![drawn: acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q062_solution_1_c70c2837_14112026.svg?v=c70c2837e4b4)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + R-OH (Alcohol) ⇌(H⁺) CH3-CH(OR)2 (Acetal)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q062_sol_2_391840d8_04112026.png?v=391840d838f1)

*acetaldehyde + R-OH (Alcohol) ⇌[H⁺] CH3-CH(OR)2 (Acetal)*

![drawn: acetaldehyde + R-OH (Alcohol) ⇌(H⁺) CH3-CH(OR)2 (Acetal)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q062_solution_2_148e129d_14112026.svg?v=148e129d0ace)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + R-NH2 → CH3-CH=N-R (Schiff's base)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q062_sol_3_fa90d1e0_04112026.png?v=fa90d1e0788d)

*acetaldehyde + R-NH2 → CH3-CH=N-R (Schiff's base)*

![drawn: acetaldehyde + R-NH2 → CH3-CH=N-R (Schiff's base)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q062_solution_3_015e2ada_14112026.svg?v=015e2ada37e4)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q062_sol_4_7b3b0359_04112026.png?v=7b3b0359696e)

*acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)*

![drawn: acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q062_solution_4_28bf2e4b_14112026.svg?v=28bf2e4b8fdb)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Carbonyl $+ \mathrm{HCN}$ gives cyanohydrin, so (a)–(iv).
2. Carbonyl $+$ alcohol (dry HCl) gives acetal, so (b)–(iii).
3. Carbonyl $+ \mathrm{RNH_2}$ gives a Schiff's base (imine), so (c)–(ii).
4. Carbonyl $+ \mathrm{NH_2OH}$ gives oxime, so (d)–(i).
5. The set (a)–(iv), (b)–(iii), (c)–(ii), (d)–(i) is option $1$.

**Subtopic:** Nucleophilic Addition Reactions · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 25)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q062_48626bae_04112026.png?v=48626bae7619)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q062_109f3bdb_04112026.png?v=109f3bdbbe15)

---

## Q63

Chemistry · inorganic · The D- and F-Block Elements – Practice

Gadolinium has a low value of third ionisation enthalpy because of

- (1) high basic character
- (2) small size
- **(3)** high exchange enthalpy
- (4) high electronegativity

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Electronic configuration of Gadolinium
2. $\mathrm{Gd}$ :— $[\mathrm{Xe}]\ 4f^{7}\ 5d^{1}\ 6s^{2}$
3. In case of $3^{\mathrm{rd}}$ ionisation enthalpy electron will be removed from $5d$ and resultant configuration will be $[\mathrm{Xe}]4f^{7}$ that is stable electronic configuration as it will have high exchange energy, hence less energy will be required to remove $3^{\mathrm{rd}}$ electron.

**Solved independently** (answer withheld)

1. Gd ($Z=64$) has configuration $[\mathrm{Xe}]\,4f^7 5d^1 6s^2$.
2. After two ionisations, $\mathrm{Gd^{2+}} = [\mathrm{Xe}]\,4f^7 5d^1$.
3. The third ionisation removes the $5d^1$ electron, giving $\mathrm{Gd^{3+}} = [\mathrm{Xe}]\,4f^7$, a half-filled $4f$ subshell.
4. The half-filled $4f^7$ state is stabilised by high exchange enthalpy, so $\Delta_i H_3$ is low, which is option $3$.

**Subtopic:** Ionisation Enthalpies, Formation of Coloured Ions & Formation of Complex Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q063_8aef9e91_04112026.png?v=8aef9e91f173)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q063_a99a511c_04112026.png?v=a99a511cf97b)

---

## Q64

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which amongst the following is **incorrect** statement?

- **(1)** $\mathrm{O_2^+}$ ion is diamagnetic
- (2) The bond orders of $\mathrm{O_2^+}, \mathrm{O_2}, \mathrm{O_2^-}$ and $\mathrm{O_2^{2-}}$ are 2.5, 2, 1.5 and 1, respectively
- (3) $\mathrm{C_2}$ molecule has four electrons in its two degenerate $\pi$ molecular orbitals
- (4) $\mathrm{H_2^+}$ ion has one electron

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\sigma 1s^{2}\sigma^{*}1s^{2}\sigma 2s^{2}\sigma^{*}2s^{2}\sigma 2p_{z}^{2}\ \begin{matrix}\pi 2p_{x}^{2}\\ \pi 2p_{y}^{2}\end{matrix}\ \begin{matrix}\pi^{*}2p_{x}^{1}\\ \pi 2p_{y}\end{matrix}$
2. Due to one unpaired electron in $\pi^{*}2p$ molecular orbital, $\mathrm{O_2^{+}}$ is a paramagnetic ion.

**Solved independently** (answer withheld)

1. Option 2: bond order $= \frac{N_b - N_a}{2}$; $\mathrm{O_2^{+}} = \frac{10-5}{2} = 2.5$, $\mathrm{O_2} = \frac{10-6}{2} = 2$, $\mathrm{O_2^{-}} = \frac{10-7}{2} = 1.5$, $\mathrm{O_2^{2-}} = \frac{10-8}{2} = 1$, so the statement is correct.
2. Option 3: $\mathrm{C_2}$ (12 electrons) has configuration $\sigma 1s^2 \sigma^* 1s^2 \sigma 2s^2 \sigma^* 2s^2 (\pi 2p_x^2 = \pi 2p_y^2)$, i.e. four electrons in the two degenerate $\pi$ MOs, so the statement is correct.
3. Option 4: $\mathrm{H_2^{+}}$ has $1 + 1 - 1 = 1$ electron, so the statement is correct.
4. Option 1: $\mathrm{O_2^{+}}$ has 15 electrons, leaving one unpaired electron in $\pi^* 2p$, so it is paramagnetic; calling it diamagnetic is incorrect.
5. The incorrect statement is option $1$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q064_36f3727a_04112026.png?v=36f3727a7a1f)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q064_d7527cb6_04112026.png?v=d7527cb6bcc6)

---

## Q65

Chemistry · physical · States of Matter

Which one is not correct mathematical equation for Dalton's Law of partial pressure? Here $p$ = total pressure of gaseous mixture

- **(1)** $p_i = \chi_i p_i^{\circ}$, where $\chi_i$ = mole fraction of $i^{th}$ gas in gaseous mixture, $p_i^{\circ}$ = pressure of $i^{th}$ gas in pure state
- (2) $p = p_1 + p_2 + p_3$
- (3) $p = n_1\dfrac{RT}{V} + n_2\dfrac{RT}{V} + n_3\dfrac{RT}{V}$
- (4) $p_i = \chi_i p$, where $p_i$ = partial pressure of $i^{th}$ gas, $\chi_i$ = mole fraction of $i^{th}$ gas in gaseous mixture

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Dalton's law of partial pressure states that the total pressure by the mixture of non-reactive gases is equal to the sum of the partial pressures of individual gases.
2. $p_{\mathrm{Total}} = p_1 + p_2 + p_3$
3. Also, $p_i = \chi_i p$ ; where $p_i$ and $\chi_i$ are the partial pressure and mole fraction of $i^{\mathrm{th}}$ gas respectively and $p$ is the total pressure.
4. $p_{\mathrm{Total}} = p_1 + p_2 + p_3$
5. $= n_1\dfrac{RT}{V} + n_2\dfrac{RT}{V} + n_3\dfrac{RT}{V}$
6. $= \left(n_1 + n_2 + n_3\right)\dfrac{RT}{V}$

**Solved independently** (answer withheld)

1. Dalton's law: $p = p_1 + p_2 + p_3$, so option $2$ is correct.
2. With $p_i = n_i\frac{RT}{V}$, $p = n_1\frac{RT}{V} + n_2\frac{RT}{V} + n_3\frac{RT}{V}$, so option $3$ is correct.
3. $p_i = \frac{n_i}{n}p = \chi_i p$, so option $4$ is correct.
4. $p_i = \chi_i p_i^{\circ}$ is Raoult's law for the vapour pressure of a solution component, not Dalton's law, so option $1$ is the incorrect one.

**Subtopic:** Dalton's Law of Partial Pressures · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q065_0293b8a3_04112026.png?v=0293b8a327f0)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q065_687231f1_04112026.png?v=687231f16ca5)

---

## Q66

Chemistry · inorganic · Hydrogen

Match List-I with List-II.

List – I (Hydrides) / List – II (Nature)

Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{MgH_2}$ | (i) | Electron precise |
| (b) | $\mathrm{GeH_4}$ | (ii) | Electron deficient |
| (c) | $\mathrm{B_2H_6}$ | (iii) | Electron rich |
| (d) | $\mathrm{HF}$ | (iv) | Ionic |

- (1) (a) – (ii), (b) – (iii), (c) – (iv), (d) – (i)
- **(2)** (a) – (iv), (b) – (i), (c) – (ii), (d) – (iii)
- (3) (a) – (iii), (b) – (i), (c) – (ii), (d) – (iv)
- (4) (a) – (i), (b) – (ii), (c) – (iv), (d) – (iii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. List – I (Hydrides) : List – II (Nature)
2. $\mathrm{MgH_2}$ — Ionic
3. $\mathrm{GeH_4}$ — Electron precise
4. $\mathrm{B_2H_6}$ — Electron deficient
5. $\mathrm{HF}$ — Electron rich
6. (a) – (iv), (b) – (i), (c) – (ii), (d) – (iii)

**Solved independently** (answer withheld)

1. $\mathrm{MgH_2}$ is a saline (ionic) hydride of an s-block metal, so (a) – (iv).
2. $\mathrm{GeH_4}$ is a group 14 molecular hydride with exactly enough electrons for its bonds, so it is electron precise: (b) – (i).
3. $\mathrm{B_2H_6}$ is a group 13 hydride with too few electrons for normal two-centre bonds, so it is electron deficient: (c) – (ii).
4. $\mathrm{HF}$ has lone pairs on F beyond those used in bonding, so it is electron rich: (d) – (iii).
5. The match (a)–(iv), (b)–(i), (c)–(ii), (d)–(iii) is option $2$.

**Subtopic:** Hydrides · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q066_b51002bc_04112026.png?v=b51002bc93cf)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q066_96098eb5_04112026.png?v=96098eb5d0bd)

---

## Q67

Chemistry · inorganic · The p–Block Elements

Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.
In the light of the above statements, choose the most **appropriate** answer from the options given below:

- Assertion (A) $\mathrm{ICl}$ is more reactive than $\mathrm{I_2}$.
- Reason (R) I-Cl bond is weaker than I-I bond.

- (1) (A) is not correct but (R) is correct
- **(2)** Both (A) and (R) are correct and (R) is the correct explanation of (A).
- (3) Both (A) and (R) are correct but (R) is not the correct explanation of (A).
- (4) (A) is correct but (R) is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In general, interhalogen compounds are more reactive than halogens (except fluorine). This is because $\mathrm{X-X'}$ bond in interhalogens is weaker than $\mathrm{X-X}$ bond in halogens excepts $\mathrm{F-F}$ bond.
2. Therefore $\mathrm{I-Cl}$ is more reactive than $\mathrm{I_2}$ because of weaker $\mathrm{I-Cl}$ bond then $\mathrm{I-I}$ bond.

**Solved independently** (answer withheld)

1. NCERT teaches that interhalogen compounds are generally more reactive than the parent halogens (except $\mathrm{F_2}$), so $\mathrm{ICl}$ is more reactive than $\mathrm{I_2}$: (A) is correct.
2. NCERT gives the reason as the $\mathrm{X{-}X'}$ bond in interhalogens being weaker than the $\mathrm{X{-}X}$ bond in halogens, so (R) is correct and explains (A), which is option $2$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q067_41f5d040_04112026.png?v=41f5d040e8a1)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q067_81f4f7c3_04112026.png?v=81f4f7c394b4)

---

## Q68

Chemistry · inorganic · The p–Block Elements

Given below are two statements
Statement I
Statement II
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The boiling points of the following hydrides of group 16 elements increases in the order $-$ $\mathrm{H_2O} < \mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te}$
- (Statement II) The boiling points of these hydrides increase with increase in molar mass.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- **(3)** Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Compound — Boiling point (K)
2. $\mathrm{H_2O}$ — $373$
3. $\mathrm{H_2S}$ — $213$
4. $\mathrm{H_2Se}$ — $232$
5. $\mathrm{H_2Te}$ — $269$
6. • The boiling points of these hybrids not exactly increases with increase in molar mass.
7. • $\mathrm{H_2O}$ has maximum boiling point due to intermolecular hydrogen bonding.

**Solved independently** (answer withheld)

1. Hydrogen bonding in H2O causes anomalously high boiling point compared to other group 16 hydrides.
2. Actual boiling point order: $H_2S < H_2Se < H_2Te < H_2O$, not $H_2O < H_2S < H_2Se < H_2Te$ as stated in Statement I — so Statement I is incorrect.
3. Statement II claims boiling point increases with molar mass, but H2O has the lowest molar mass yet the highest boiling point, so this general statement is also incorrect.
4. Hence both statements are incorrect, matching option 3.

**Subtopic:** Important Compounds & their Hydrides & Oxides Group 16 · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 28)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q068_146bfec6_04112026.png?v=146bfec63513)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q068_91fbc044_04112026.png?v=91fbc04447ec)

---

## Q69

Chemistry · physical · Electrochemistry

At 298 K, the standard electrode potentials of $\mathrm{Cu^{2+}}$ / $\mathrm{Cu}$, $\mathrm{Zn^{2+}}$ / $\mathrm{Zn}$, $\mathrm{Fe^{2+}}$ / $\mathrm{Fe}$ and $\mathrm{Ag^{+}}$ / $\mathrm{Ag}$ are $0.34\,\mathrm{V}$, $-0.76\,\mathrm{V}$, $-0.44\,\mathrm{V}$ and $0.80\,\mathrm{V}$, respectively.
On the basis of standard electrode potential, predict which of the following reaction cannot occur?

- **(1)** $\mathrm{2CuSO_4(aq) + 2Ag(s) \rightarrow 2Cu(s) + Ag_2SO_4(aq)}$
- (2) $\mathrm{CuSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Cu(s)}$
- (3) $\mathrm{CuSO_4(aq) + Fe(s) \rightarrow FeSO_4(aq) + Cu(s)}$
- (4) $\mathrm{FeSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Fe(s)}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For a reaction to be spontaneous, $\mathrm{E^{o}_{cell}}$ must be positive.
2. For, $\mathrm{FeSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Fe(s)}$
3. $\mathrm{E^{o}_{cell} = E^{o}_{cathode} - E^{o}_{anode}}$
4. $= -0.44\,\mathrm{V} - (-0.76\,\mathrm{V})$
5. $= 0.32\,\mathrm{V}$
6. For, $\mathrm{2CuSO_4(aq) + 2Ag(s) \rightarrow 2Cu(s) + Ag_2SO_4(aq)}$
7. $\mathrm{E^{o}_{cell}} = 0.34\,\mathrm{V} - 0.80\,\mathrm{V}$
8. $= -0.46\,\mathrm{V}$
9. For, $\mathrm{CuSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Cu(s)}$
10. $\mathrm{E^{o}_{cell}} = 0.34\,\mathrm{V} - (-0.76\,\mathrm{V})$
11. $= 1.1\,\mathrm{V}$
12. For, $\mathrm{CuSO_4(aq) + Fe(s) \rightarrow FeSO_4(aq) + Cu(s)}$
13. $\mathrm{E^{o}_{cell}} = 0.80\,\mathrm{V} - (-0.44\,\mathrm{V})$
14. $= 1.24\,\mathrm{V}$

**Solved independently** (answer withheld)

1. A displacement reaction occurs if $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} > 0$.
2. Option 2: $E^\circ_{cell} = 0.34 - (-0.76) = +1.10\,\mathrm{V}$, feasible.
3. Option 3: $E^\circ_{cell} = 0.34 - (-0.44) = +0.78\,\mathrm{V}$, feasible.
4. Option 4: $E^\circ_{cell} = -0.44 - (-0.76) = +0.32\,\mathrm{V}$, feasible.
5. Option 1: $E^\circ_{cell} = 0.34 - 0.80 = -0.46\,\mathrm{V} < 0$, so it cannot occur; answer is option $1$.

**Subtopic:** Electrochemical Series · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q069_474d0921_04112026.png?v=474d09215aae)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q069_688fd9cc_04112026.png?v=688fd9cc3f42)

---

## Q70

Chemistry · physical · Basic Concepts of Chemistry

What mass of 95% pure $\mathrm{CaCO_3}$ will be required to neutralise $50\,\mathrm{mL}$ of $0.5\,\mathrm{M}$ $\mathrm{HCl}$ solution according to the following reaction?
$\mathrm{CaCO_{3(s)} + 2HCl_{(aq)} \rightarrow CaCl_{2(aq)} + CO_{2(g)} + 2H_2O_{(l)}}$
[Calculate upto second place of decimal point]

- (1) $9.50\,\mathrm{g}$
- (2) $1.25\,\mathrm{g}$
- **(3)** $1.32\,\mathrm{g}$
- (4) $3.65\,\mathrm{g}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Let m gram mass of $\mathrm{CaCO_3}$ is required
2. Pure $\mathrm{CaCO_3}$ in m gram $= \frac{95}{100} \times \mathrm{m}$
3. Moles of $\mathrm{CaCO_3} = \frac{95}{100} \times \frac{\mathrm{m}}{100}$
4. Moles of $\mathrm{HCl}$ required $= 2 \times$ moles of $\mathrm{CaCO_3}$
5. $= 2 \times \frac{95}{100} \times \frac{\mathrm{m}}{100}$
6. $2 \times \frac{95}{100} \times \frac{\mathrm{m}}{100} = \frac{50}{1000} \times 0.5$
7. $\mathrm{m} = 1.315\,\mathrm{g} \approx 1.32\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $n_{\mathrm{HCl}} = 0.050\,\mathrm{L} \times 0.5\,\mathrm{M} = 0.025\,\mathrm{mol}$.
2. From the equation, $1\,\mathrm{mol\ CaCO_3}$ reacts with $2\,\mathrm{mol\ HCl}$, so $n_{\mathrm{CaCO_3}} = \frac{0.025}{2} = 0.0125\,\mathrm{mol}$.
3. Mass of pure $\mathrm{CaCO_3} = 0.0125 \times 100\,\mathrm{g\,mol^{-1}} = 1.25\,\mathrm{g}$.
4. The sample is $95\%$ pure, so required mass $= \frac{1.25}{0.95} = 1.3158\,\mathrm{g} \approx 1.32\,\mathrm{g}$, which is option $3$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 29)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q070_bca1b196_04112026.png?v=bca1b196e99f)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q070_45a7425a_04112026.png?v=45a7425a857b)

---

## Q71

Chemistry · inorganic · The p–Block Elements

Which of the following statement is not correct about diborane?

- **(1)** Both the Boron atoms are $sp^2$ hybridised.
- (2) There are two 3-centre-2-electron bonds.
- (3) The four terminal B-H bonds are two centre two electron bonds.
- (4) The four terminal Hydrogen atoms and the two Boron atoms lie in one plane.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Each boron atoms in diborane uses $sp^{3}$ hybrid orbitals for bonding.

![printed figure: bonding diagram of diborane ($\ce{B2H6}$): each B carries two terminal H atoms, the two B atoms are joined by two bridging H atoms through curved 3-centre-2-electron (banana) bonds; arrows point to both B atoms labelled 'sp³ hybridised'](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q071_sol_1_0e394dfa_04112026.png?v=0e394dfa90f1)

*bonding diagram of diborane ($\ce{B2H6}$): each B carries two terminal H atoms, the two B atoms are joined by two bridging H atoms through curved 3-centre-2-electron (banana) bonds; arrows point to both B atoms labelled 'sp³ hybridised'*


**Solved independently** (answer withheld)

1. In $\mathrm{B_2H_6}$ there are two bridging $\mathrm{B-H-B}$ bonds, each a 3-centre-2-electron bond, so option $2$ is correct.
2. The four terminal $\mathrm{B-H}$ bonds are ordinary 2-centre-2-electron bonds, so option $3$ is correct.
3. The four terminal H atoms and the two B atoms lie in one plane, with the bridging H atoms above and below it, so option $4$ is correct.
4. Each B uses four orbitals (two terminal and two bridging bonds), so B is $sp^{3}$ hybridised, not $sp^{2}$; option $1$ is the incorrect statement.

**Subtopic:** Important compounds of Boranes · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 29)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q071_a0bdf9f4_04112026.png?v=a0bdf9f43096)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q071_3cb5c89f_04112026.png?v=3cb5c89f9dd4)

---

## Q72

Chemistry · organic · Amines

Given below are two statements
In the light of the above statements, choose the most **appropriate** answer from the options given below

- (Statement I) Primary aliphatic amines react with $\mathrm{HNO_2}$ to give unstable diazonium salts.
- (Statement II) Primary aromatic amines react with $\mathrm{HNO_2}$ to form diazonium salts which are stable even above $300\,\mathrm{K}$.

- (1) Statement I is incorrect but Statement II is correct.
- (2) Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- **(4)** Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Primary aliphatic amines react with $\mathrm{HNO_2}$ and give unstable diazonium salt which turns into alcohol
2. $\mathrm{R-NH_2} + \mathrm{HNO_2} \longrightarrow \left[\mathrm{R-\overset{+}{N_2}-Cl^-}\right] \xrightarrow{\mathrm{H_2O}} \mathrm{ROH} + \mathrm{N_2} + \mathrm{HCl}$
3. Primary aromatic amines reacts with $\mathrm{HNO_2}$ and give stable diazonium salt which are stable at $273$ to $278\,\mathrm{K}$.
4. $\mathrm{C_6H_5-NH_2} + \mathrm{HNO_2} \xrightarrow{273-278\,\mathrm{K}} \mathrm{C_6H_5\overset{+}{N_2}Cl^-}$

**Solved independently** (answer withheld)

1. Statement I: $\mathrm{RNH_2} + \mathrm{HNO_2} \rightarrow [\mathrm{RN_2^+}]$, an unstable aliphatic diazonium salt that decomposes to alcohol and $\mathrm{N_2}$, so Statement I is correct.
2. Statement II: arenediazonium salts are stable only in the cold ($273$-$278\,\mathrm{K}$) and decompose on warming, so they are not stable above $300\,\mathrm{K}$; Statement II is incorrect.
3. Statement I correct, Statement II incorrect, which is option $4$.

**Subtopic:** Diazotization and Its Method of Preparation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q072_9bc2ad02_04112026.png?v=9bc2ad02fbd6)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q072_2981dd82_04112026.png?v=2981dd82491c)

---

## Q73

Chemistry · physical · Structure of Atom

Identify the **incorrect** statement from the following.

- **(1)** The shapes of $d_{xy}$, $d_{yz}$ and $d_{zx}$ orbitals are similar to each other; and $d_{x^2-y^2}$ and $d_{z^2}$ are similar to each other.
- (2) All the five $5d$ orbitals are different in size when compared to the respective $4d$ orbitals.
- (3) All the five $4d$ orbitals have shapes similar to the respective $3d$ orbitals.
- (4) In an atom, all the five $3d$ orbitals are equal in energy in free state.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In an atom, all the five $3d$ orbitals are equal in energy in free state $i.e.$, degenerate.
2. The shape of $d_{x^2-y^2}$ is different then shape of $d_{z^2}$

![printed figure: orbital shape diagrams of the $d_{x^2-y^2}$ orbital (four lobes along the x and y axes) and the $d_{z^2}$ orbital (two lobes along the z axis with a ring around the centre), each drawn on x, y axes](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q073_sol_1_248775d3_04112026.png?v=248775d3aef9)

*orbital shape diagrams of the $d_{x^2-y^2}$ orbital (four lobes along the x and y axes) and the $d_{z^2}$ orbital (two lobes along the z axis with a ring around the centre), each drawn on x, y axes*

3. The size of orbital depends on principal quantum number 'n' therefore all the five $3d$ orbitals are different in size when compared to the respective $4d$ orbitals.
4. Shape of orbitals depends on azimuthal quantum number 'l' therefore shapes of $4d$ orbitals are similar to the respective $3d$ orbitals.

**Solved independently** (answer withheld)

1. The three orbitals $d_{xy}, d_{yz}, d_{zx}$ have identical four-lobed shapes oriented between the axes, so they are correctly grouped as similar.
2. $d_{x^2-y^2}$ has four lobes along the axes, while $d_{z^2}$ has two lobes along the z-axis plus a torus in the xy-plane — these are distinct shapes, not similar to each other.
3. Hence option 1's claim that $d_{x^2-y^2}$ and $d_{z^2}$ are similar is false, making it the incorrect statement.
4. Options 2, 3, and 4 are standard correct facts about d-orbitals (size increases with principal quantum number, same shape across different n for same l, and degeneracy in free atom).

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q073_c9f0a9d1_04112026.png?v=c9f0a9d1c8f6)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q073_418644b9_04112026.png?v=418644b920f8)

---

## Q74

Chemistry · physical · Chemical Kinetics

The given graph is a representation of kinetics of a reaction.

The $y$ and $x$ axes for zero and first order reactions, respectively are

![printed figure: graph with y on the vertical axis and x on the horizontal axis, a horizontal straight line parallel to the x axis, labelled 'Constant temperature T'](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q074_126204eb_04112026.png?v=126204eb59a5)

*graph with y on the vertical axis and x on the horizontal axis, a horizontal straight line parallel to the x axis, labelled 'Constant temperature T'*

- (1) zero order ($y$ = rate and $x$ = concentration), first order ($y$ = rate and $x$ = $t_{1/2}$)
- (2) zero order ($y$ = concentration and $x$ = time), first order ($y$ = $t_{1/2}$ and $x$ = concentration)
- (3) zero order ($y$ = concentration and $x$ = time), first order ($y$ = rate constant and $x$ = concentration)
- **(4)** zero order ($y$ = rate and $x$ = concentration), first order ($y$ = $t_{1/2}$ and $x$ = concentration)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For zero order reaction
2. $r = k[A]^{0}$
3. $r = k$ (constant)
4. hence, 'y' as 'rate' and 'x' as concentration will give desired graph.
5. For first order reaction
6. $t_{1/2} = \frac{0.693}{k}$ (constant)
7. hence, 'y' as '$t_{1/2}$' and 'x' as concentration will give desired graph.

**Solved independently** (answer withheld)

1. The graph is a horizontal line, so $y$ stays constant as $x$ changes.
2. Zero order: $\text{rate} = k[A]^0 = k$, so rate vs concentration is a horizontal line.
3. First order: $t_{1/2} = \frac{0.693}{k}$, independent of $[A]_0$, so $t_{1/2}$ vs concentration is a horizontal line.
4. Concentration vs time for zero order is a falling straight line, not horizontal, which rules out options $2$ and $3$; rate constant vs concentration is also constant but option $3$ fails on the zero-order part; option $1$ gives first-order rate vs $t_{1/2}$, which is not the standard plot. So the answer is option $4$.

**Subtopic:** Zero Order Reactions, First Order Reactions · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 31)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q074_89925bf1_04112026.png?v=89925bf19eb4)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q074_86e2eb8b_04112026.png?v=86e2eb8b2cd5)

---

## Q75

Chemistry · physical · Electrochemistry

Given below are half cell reactions:
$\mathrm{MnO_4^-} + 8\mathrm{H^+} + 5\mathrm{e^-} \rightarrow \mathrm{Mn^{2+}} + 4\mathrm{H_2O}$
$E^{\circ}_{\mathrm{Mn^{2+}/MnO_4^-}} = -1.510\,\mathrm{V}$
$\frac{1}{2}\mathrm{O_2} + 2\mathrm{H^+} + 2\mathrm{e^-} \rightarrow \mathrm{H_2O}$
$E^{\circ}_{\mathrm{O_2/H_2O}} = +1.223\,\mathrm{V}$
Will the permanganate ion, $\mathrm{MnO_4^-}$ liberate $\mathrm{O_2}$ from water in the presence of an acid?

- (1) No, because $E^{\circ}_{\mathrm{cell}} = -\,2.733\,\mathrm{V}$
- **(2)** Yes, because $E^{\circ}_{\mathrm{cell}} = +\,0.287\,\mathrm{V}$
- (3) No, because $E^{\circ}_{\mathrm{cell}} = -\,0.287\,\mathrm{V}$
- (4) Yes, because $E^{\circ}_{\mathrm{cell}} = +\,2.733\,\mathrm{V}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{MnO_4^-} + 8\mathrm{H^+} + 5\mathrm{e^-} \longrightarrow \mathrm{Mn^{2+}} + 4\mathrm{H_2O}$ \quad ...(i)
2. $E^{\circ}_{\mathrm{MnO_4^-/Mn^{2+}}} = -\,E^{\circ}_{\mathrm{Mn^{2+}/MnO_4^-}} = 1.51\,\mathrm{V}$
3. $\mathrm{H_2O} \longrightarrow \frac{1}{2}\mathrm{O_2} + 2\mathrm{H^+} + 2\mathrm{e^-}$ \quad ...(ii)
4. $E^{\circ}_{\mathrm{O_2/H_2O}} = 1.223\,\mathrm{V}$
5. Using $2 \times$ (i) $+\ 5 \times$ (ii), net cell reactions is
6. $2\mathrm{MnO_4^-} + 6\mathrm{H^+} \longrightarrow 2\mathrm{Mn^{2+}} + \frac{5}{2}\mathrm{O_2} + 3\mathrm{H_2O}$
7. $E^{\circ}_{\mathrm{cell}} = E^{\circ}_{\mathrm{C}} - E^{\circ}_{\mathrm{A}} = E^{\circ}_{\mathrm{MnO_4^-/Mn^{2+}}} - E^{\circ}_{\mathrm{O_2/H_2O}} = 1.51 - 1.223 = 0.287\,\mathrm{V}$
8. Since $E^{\circ}_{\mathrm{cell}} > 0$, therefore net cell reaction is spontaneous and so $\mathrm{MnO_4^-}$ liberate $\mathrm{O_2}$ from $\mathrm{H_2O}$ in presence of an acid.

**Solved independently** (answer withheld)

1. Identify cathode (reduction) half-reaction: $\mathrm{MnO_4^-} + 8H^+ + 5e^- \rightarrow \mathrm{Mn^{2+}} + 4H_2O$, with actual reduction potential $E^{\circ} = +1.510\,V$ (the given $-1.510\,V$ corresponds to the oxidation direction $\mathrm{Mn^{2+}} \rightarrow \mathrm{MnO_4^-}$).
2. Identify anode (oxidation) half-reaction: $H_2O \rightarrow \frac{1}{2}O_2 + 2H^+ + 2e^-$, which is the reverse of the given reduction $\frac{1}{2}O_2 + 2H^+ + 2e^- \rightarrow H_2O$ ($E^{\circ} = +1.223\,V$), so oxidation potential = $-1.223\,V$.
3. $E^{\circ}_{cell} = E^{\circ}_{reduction} + E^{\circ}_{oxidation} = 1.510 + (-1.223) = +0.287\,V$.
4. Since $E^{\circ}_{cell} > 0$, the reaction is spontaneous, meaning $\mathrm{MnO_4^-}$ can indeed liberate $O_2$ from water in acidic medium — matching option 2.

**Subtopic:** Cell Potential · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 31)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q075_c2e9df26_04112026.png?v=c2e9df26c06a)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q075_bf1f4e18_04112026.png?v=bf1f4e184cb0)

---

## Q76

Chemistry · inorganic · The s-Block Elements

Identify the incorrect statement from the following

- (1) Lithium is the strongest reducing agent among the alkali metals.
- (2) Alkali metals react with water to form their hydroxides.
- **(3)** The oxidation number of K in $\mathrm{KO_2}$ is $+4$.
- (4) Ionisation enthalpy of alkali metals decreases from top to bottom in the group.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Alkali metals show only '+1' oxidation state in all of their compounds.
2. $\mathrm{KO_2}$ is a super-oxide in which $\mathrm{O_2^-}$ is anion and $\mathrm{K^+}$ is cation oxidation state of K is $+1$.

**Solved independently** (answer withheld)

1. KO2 contains the superoxide ion $O_2^-$, giving overall charge balance $K^{+1} + O_2^{-1} = 0$.
2. Thus oxidation number of K in KO2 is $+1$, not $+4$ as stated in option 3.
3. Options 1, 2, and 4 correctly describe alkali metal properties (Li strongest reducing agent, hydroxide formation with water, decreasing ionisation enthalpy down the group).

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q076_9038ef21_04112026.png?v=9038ef21c694)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q076_b77a4690_04112026.png?v=b77a4690f593)

---

## Q77

Chemistry · organic · Alcohols, Phenols and Ethers

Given below are two statements
In the light of the above statements, choose the **most appropriate** answer from the options given below:

- (Statement I) The acidic strength of monosubstituted nitrophenol is higher than phenol because of electron withdrawing nitro group.
- (Statement II) $o$-nitrophenol, $m$-nitrophenol and $p$-nitrophenol will have same acidic strength as they have one nitro group attached to the phenolic ring.

- (1) **Statement I** is incorrect but **Statement II** is correct.
- (2) Both **Statement I** and **Statement II** are correct.
- (3) Both **Statement I** and **Statement II** are incorrect.
- **(4)** **Statement I** is correct but **Statement II** is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: I. nitrophenol (benzene ring with OH and an NO2 group drawn from the ring centre, position unspecified)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q077_sol_1_b38f20a9_04112026.png?v=b38f20a9cc2e)

*I. nitrophenol (benzene ring with OH and an NO2 group drawn from the ring centre, position unspecified)*

![drawn: I. nitrophenol (benzene ring with OH and an NO2 group drawn from the ring centre, position unspecified)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q077_solution_1_85ed0a2e_14112026.svg?v=85ed0a2e6227)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Nitro group has electron withdrawing tendency. It can withdraw electrons both by $-\mathrm{I}$ effect and $-\mathrm{R}$ effect. Thus the acidic strength of monosubstituted nitrophenol is higher than phenol.
2. Nitro group present at $o$- and $p$-positions will have strong $-\mathrm{R}$ effect while nitro group present at $m$-position will influence only $-\mathrm{I}$ effect hence acidity or $o/p$ isomer will be more meta isomer.

**Solved independently** (answer withheld)

1. Statement I: NO2 is electron-withdrawing, stabilizes phenoxide ion, increasing acidity relative to phenol — true.
2. Statement II: Position of NO2 (ortho/meta/para) affects resonance and inductive contributions differently, so acidic strengths differ (o- and p- > m- generally) — false.

**Subtopic:** Acidity of Phenols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q077_92526a0b_04112026.png?v=92526a0b6215)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q077_fae6e055_04112026.png?v=fae6e05531d8)

---

## Q78

Chemistry · inorganic · The p–Block Elements

Choose the correct statement:

- (1) Both diamond and graphite are used as dry lubricants.
- (2) Diamond and graphite have two dimensional network.
- (3) Diamond is covalent and graphite is ionic.
- **(4)** Diamond is $\mathrm{sp^3}$ hybridised and graphite is $\mathrm{sp^2}$ hybridized.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Diamond : • $sp^{3}$ hybridised carbon atom
2. • Covalent solid
3. • 3-D structure
4. • Cannot be used as dry lubricant
5. Graphite : • $sp^{2}$ hybridised carbon atom
6. • Covalent solid
7. • 3-D structure
8. • Used as dry lubricant

**Solved independently** (answer withheld)

1. Diamond: each C is tetrahedrally bonded to four C atoms, so it is $\mathrm{sp^3}$ with a three-dimensional network; option $2$ is false.
2. Graphite: each C is bonded to three C atoms in hexagonal layers, so it is $\mathrm{sp^2}$; both solids are covalent, so option $3$ is false.
3. Only graphite (slippery layers) is a dry lubricant, so option $1$ is false.
4. Diamond $\mathrm{sp^3}$ and graphite $\mathrm{sp^2}$ is correct: option $4$.

**Subtopic:** Catenation & Allotropy Group 14 · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q078_c60065c1_04112026.png?v=c60065c1c391)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q078_4591c20d_04112026.png?v=4591c20dd307)

---

## Q79

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Given below are two statements :
In the light of the above statements, choose the **most appropriate** answer from the given below

- (Statement I) The boiling points of aldehydes and ketones are higher than hydrocarbons of comparable molecular masses because of weak molecular association in aldehydes and ketones due to dipole - dipole interactions.
- (Statement II) The boiling points of aldehydes and ketones are lower than the alcohols of similar molecular masses due to the absence of H-bonding.

- (1) **Statement I** is incorrect but **Statement II** is correct
- **(2)** Both **Statement I** and **Statement II** are correct
- (3) Both **Statement I** and **Statement II** are incorrect
- (4) **Statement I** is correct but **Statement II** is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The boiling points of aldehydes and ketones are higher than hydrocarbons of comparable molecular masses due to weak molecular association in aldehydes and ketones arising out of the dipole - dipole interaction.
2. Alcohols involved intermolecular hydrogen bonding, because of which the boiling point of aldehydes and ketones are lower than the alcohols of similar molecular masses.

**Solved independently** (answer withheld)

1. Statement I: the polar $C=O$ group gives weak intermolecular association via dipole-dipole interactions, so aldehydes and ketones boil higher than hydrocarbons of comparable molecular mass; Statement I is correct.
2. Statement II: aldehydes and ketones lack $O-H$ and cannot form intermolecular H-bonds, so they boil lower than alcohols of similar molecular mass; Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q079_2ffb1846_04112026.png?v=2ffb1846ba4d)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q079_40ac561f_04112026.png?v=40ac561fed1b)

---

## Q80

Chemistry · physical · The Solid State

Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.

**Assertion (A):**

**Reason (R):**

In the light of the above statements, choose the most appropriate answer from the options given below:

- Assertion (A) In a particular point defect, an ionic solid is electrically neutral, even if few of its cations are missing from its unit cells.
- Reason (R) In an ionic solid, Frenkel defect arises due to dislocation of cation from its lattice site to interstitial site, maintaining overall electrical neutrality.

- (1) (A) is not correct but (R) is correct
- (2) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- **(3)** Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- (4) (A) is correct but (R) is not correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Assertion statement is classic explanation of Schottky defect in which cation and anion leaves their site, or impurity defect.
2. Reason statement is true but not correct explanation as it is defining Frenkel defect in which ion does not leave crystal.

**Solved independently** (answer withheld)

1. Assertion: cations missing from unit cell, but solid stays neutral — true, but this matches 'metal deficiency defect', not Frenkel defect.
2. Reason: Frenkel defect = cation moves from lattice site to interstitial site, no cation is actually missing, neutrality maintained — this statement itself is correct.
3. Since A's scenario (missing cations) is not the mechanism described in R (displaced cations), R does not explain A.
4. Hence both A and R are individually correct, but R is not the correct explanation of A — option 3.

**Subtopic:** Imperfections in Solids · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 34)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q080_50b208dc_04112026.png?v=50b208dc31aa)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q080_4340ce17_04112026.png?v=4340ce17fed1)

---

## Q81

Chemistry · organic · Isomerism in Organic Compounds

The **incorrect** statement regarding chirality is

- (1) A racemic mixture shows zero optical rotation
- (2) $\mathrm{S_N}1$ reaction yields $1 : 1$ mixture of both enantiomers
- (3) The product obtained by $\mathrm{S_N}2$ reaction of haloalkane having chirality at the reactive site shows inversion of configuration
- **(4)** Enantiomers are superimposable mirror images on each other

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The stereoisomers related to each other as non-superimposable mirror image are called enantiomers.

**Solved independently** (answer withheld)

1. Enantiomers are, by definition, non-superimposable mirror images of each other, so option $4$ is incorrect.
2. Options $2$ (SN1 gives racemisation, $1:1$ mixture as NCERT teaches), $2$ (SN2 backside attack gives inversion) and $4$ (racemic mixture has zero net rotation) are correct, so the answer is option $4$.

**Subtopic:** Optical Isomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q081_59e738d3_04112026.png?v=59e738d316aa)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q081_b3d34ca3_04112026.png?v=b3d34ca37c86)

---

## Q82

Chemistry · inorganic · The s-Block Elements

Match **List-I** with **List-II**

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{Li}$ | (i) | absorbent for carbon dioxide |
| (b) | $\mathrm{Na}$ | (ii) | electrochemical cells |
| (c) | $\mathrm{KOH}$ | (iii) | coolant in fast breeder reactors |
| (d) | $\mathrm{Cs}$ | (iv) | photoelectric cell |

- **(1)** (a) - (ii), (b) – (iii), (c) – (i), (d) – (iv)
- (2) (a) - (iv), (b) – (i), (c) – (iii), (d) – (ii)
- (3) (a) - (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (4) (a) - (i), (b) – (iii), (c) – (iv), (d) – (ii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Cs}$ is used in photoelectric cell due to its low ionisation enthalpy
2. $\mathrm{KOH}$ used to adsorb $\mathrm{CO_2}$ and changes into $\mathrm{K_2CO_3}$
3. Liquid sodium metal is used as a coolant in fast breeder nuclear reactor
4. Lithium is used in electrochemical cells

**Solved independently** (answer withheld)

1. $\mathrm{Li}$ is used in electrochemical cells (lithium batteries), so (a) $\to$ (ii).
2. Liquid $\mathrm{Na}$ is a coolant in fast breeder reactors, so (b) $\to$ (iii).
3. $\mathrm{KOH}$ absorbs $\mathrm{CO_2}$ ($2\mathrm{KOH} + \mathrm{CO_2} \to \mathrm{K_2CO_3} + \mathrm{H_2O}$), so (c) $\to$ (i).
4. $\mathrm{Cs}$ has a very low ionisation enthalpy and is used in photoelectric cells, so (d) $\to$ (iv).
5. The match (a)-(ii), (b)-(iii), (c)-(i), (d)-(iv) is option $1$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 34)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q082_26174194_04112026.png?v=26174194d94d)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q082_f8ee3dda_04112026.png?v=f8ee3ddaf12e)

---

## Q83

Chemistry · organic · General Organic Chemistry

Which compound amongst the following is **not** an aromatic compound?

- **(1)** cyclohepta-1,3,5-triene `C1=CC=CCC=C1` ![cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_option_1_s1_24e5e938_14112026.svg?v=24e5e9386046)
- (2) cyclopenta-2,4-dien-1-ide `c1cc[cH-]c1` ![cyclopenta-2,4-dien-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_option_2_s1_3e03e8a7_14112026.svg?v=3e03e8a741d1)
- (3) cyclohepta-2,4,6-trien-1-ylium `c1ccc[cH+]cc1` ![cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_option_3_s1_d55ef558_14112026.svg?v=d55ef5582745)
- (4) cycloprop-2-en-1-ylium `c1c[cH+]1` ![cycloprop-2-en-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_option_4_s1_be7d509b_14112026.svg?v=be7d509be003)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Planar, cyclic, conjugated species containing $(4n+2)\pi$ electrons will be aromatic in nature ($n$ is an integer)
2. and are aromatic species

![printed figure: cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q083_sol_1_35c49257_04112026.png?v=35c49257f1d6)

*cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium*

![drawn: cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_solution_1_88184d3a_14112026.svg?v=88184d3ad2b4)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. is not an aromatic compound

![printed figure: cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q083_sol_2_41bcc4e9_04112026.png?v=41bcc4e97d3d)

*cyclohepta-1,3,5-triene*

![drawn: cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q083_solution_2_5b415bc2_14112026.svg?v=5b415bc2887f)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Option $1$ is cycloheptatriene: one ring carbon is $sp^3$ ($\mathrm{CH_2}$), so the ring is not fully conjugated and cannot be aromatic.
2. Option $2$, cyclopentadienyl anion, is planar and fully conjugated with $6\pi$ electrons ($4n+2$, $n=1$): aromatic.
3. Option $3$, tropylium (cycloheptatrienyl) cation, has $6\pi$ electrons: aromatic.
4. Option $4$, cyclopropenyl cation, has $2\pi$ electrons ($n=0$): aromatic.
5. The non-aromatic compound is option $1$.

**Subtopic:** Aromaticity · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 35)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q083_1709c61d_04112026.png?v=1709c61d42b4)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q083_2dca2387_04112026.png?v=2dca2387c10a)

---

## Q84

Chemistry · organic · Biomolecules

The **incorrect** statement regarding enzymes is

- (1) Enzymes are very specific for a particular reaction and substrate.
- (2) Enzymes are biocatalysts.
- (3) Like chemical catalysts enzymes reduce the activation energy of bio processes.
- **(4)** Enzymes are polysaccharides.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Enzymes are complex nitrogenous organic compounds which are produced by living plants and animals.
2. They are protein molecules of high molecular mass.
3. They are not polysaccharides.

**Solved independently** (answer withheld)

1. Enzymes are biocatalysts, reduce activation energy and are highly specific, so options $2$, $3$ and $1$ are correct; enzymes are proteins, not polysaccharides, so the incorrect statement is option $4$.

**Subtopic:** Enzymes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q084_48c80d6b_04112026.png?v=48c80d6b950f)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q084_9f21e689_04112026.png?v=9f21e689ea48)

---

## Q85

Chemistry · physical · Surface Chemistry

Given below are two statements
In the light of the above statements, choose the most **appropriate** answer from the options given below

- (Statement I) In the coagulation of a negative sol, the flocculating power of the three given ions is in the order $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$
- (Statement II) In the coagulation of a positive sol, the flocculating power of the three given salts is in the order $\mathrm{NaCl} > \mathrm{Na_2SO_4} > \mathrm{Na_3PO_4}$

- (1) Statement I is incorrect but Statement II is correct.
- (2) Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- **(4)** Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to hardy Schulze rule
2. Flocculating power of cation increases with increases in charge on cation of electrolyte in case of negatively charge colloid, hence order is
3. $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$
4. Flocculating power of anion increases with increases in charge on anion of electrolyte in case of positively charge colloids
5. Hence order is
6. $\mathrm{NaCl} < \mathrm{Na_2SO_4} < \mathrm{Na_3PO_4}$

**Solved independently** (answer withheld)

1. By the Hardy-Schulze rule, the coagulating ion carries the charge opposite to the sol, and its flocculating power increases with its charge.
2. For a negative sol the cations coagulate: $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$, so Statement I is correct.
3. For a positive sol the anions coagulate: $\mathrm{PO_4^{3-}} > \mathrm{SO_4^{2-}} > \mathrm{Cl^{-}}$, so $\mathrm{Na_3PO_4} > \mathrm{Na_2SO_4} > \mathrm{NaCl}$.
4. Statement II gives the reverse order, so it is incorrect; the answer is option $4$.

**Subtopic:** Coagulation of Colloids and Hardy-Schulze Rule · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q085_041512b4_04112026.png?v=041512b41c5f)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q085_dea0a5c1_04112026.png?v=dea0a5c102ed)

---

## Q86

Chemistry · inorganic · Coordination Compounds – Practice

The order of energy absorbed which is responsible for the color of complexes

- (A) $\mathrm{[Ni(H_2O)_2(en)_2]^{2+}}$
- (B) $\mathrm{[Ni(H_2O)_4(en)]^{2+}}$ and
- (C) $\mathrm{[Ni(en)_3]^{2+}}$

- (1) (B) > (A) > (C)
- (2) (A) > (B) > (C)
- (3) (C) > (B) > (A)
- **(4)** (C) > (A) > (B)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Stronger the field strength of ligand, higher will be the energy absorbed by the complex.
2. $\Rightarrow$ 'en' has a stronger field strength than '$\mathrm{H_2O}$' according to spectrochemical series
3. $\therefore$ Correct order of energy absorbed will be:
4. $\mathrm{[Ni(en)_3]^{2+}} > \mathrm{[Ni(H_2O)_2(en)_2]^{2+}} > \mathrm{[Ni(H_2O)_4(en)]^{2+}}$
5. i.e. (C) > (A) > (B)

**Solved independently** (answer withheld)

1. Ethylenediamine (en) lies higher than H2O in the spectrochemical series, so it causes greater crystal field splitting ($\Delta$).
2. As more H2O ligands are replaced by en, $\Delta$ increases, increasing the energy of the absorbed light responsible for color.
3. Ranking by number of en ligands: $[Ni(en)_3]^{2+}$ (3 en) > $[Ni(H_2O)_2(en)_2]^{2+}$ (2 en) > $[Ni(H_2O)_4(en)]^{2+}$ (1 en), i.e. C > A > B.

**Subtopic:** Colour in Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q086_3815a021_04112026.png?v=3815a021fa9a)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q086_0e74b37c_04112026.png?v=0e74b37c4811)

---

## Q87

Chemistry · physical · Electrochemistry

> ⚠ The booklet prints "Answer (NA)": none of the four options is correct as printed, so there is no keyed answer to check a solve against.

> ⚠ The independent solve found no printed option exactly right ("No option matches the printed values: with E°cell = 10"); its pick (unsure) is the closest fit, so treat this question as possibly misprinted.

Find the emf of the cell in which the following reaction takes place at $298\,\mathrm{K}$
$\mathrm{Ni(s)} + 2\mathrm{Ag}^{+}\,(0.001\,\mathrm{M}) \rightarrow \mathrm{Ni}^{2+}\,(0.001\,\mathrm{M}) + 2\mathrm{Ag(s)}$
$\left(\text{Given that } \mathrm{E}^{\circ}_{\text{cell}} = 10.5\,\mathrm{V},\ \dfrac{2.303\,RT}{F} = 0.059 \text{ at } 298\,\mathrm{K}\right)$

- (1) $1.05\,\mathrm{V}$
- (2) $1.0385\,\mathrm{V}$
- (3) $1.385\,\mathrm{V}$
- (4) $0.9615\,\mathrm{V}$

**Answer** — booklet: (none) · independent solve: (unsure) · publisher_no_valid_option

**Publisher's solution**

1. $\mathrm{Ni(s)} + 2\mathrm{Ag}^{+}\,(0.001\,\mathrm{M}) \rightarrow \mathrm{Ni}^{2+}\,(0.001\,\mathrm{M}) + 2\mathrm{Ag(s)}$
2. $\mathrm{E}^{\circ}_{\mathrm{cell}} = 10.5\,\mathrm{V}$
3. $\mathrm{E}_{\mathrm{cell}} = \mathrm{E}^{\circ}_{\mathrm{cell}} - \frac{0.059}{n}\log\frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}}$
4. $= 10.5 - \frac{0.059}{2}\log\frac{\left(10^{-3}\right)}{\left(10^{-3}\right)^{2}}$
5. $\Rightarrow 10.5 - \frac{0.059}{2}\log\left(10\right)^{3}$
6. $\Rightarrow 10.5 - 0.0295 \times 3$
7. $= 10.5 - 0.0885$
8. $= 10.4115\,\mathrm{V}$

**Solved independently** (answer withheld)

1. The reaction transfers $n = 2$ electrons.
2. $Q = \frac{[\mathrm{Ni^{2+}}]}{[\mathrm{Ag^{+}}]^2} = \frac{0.001}{(0.001)^2} = 10^{3}$.
3. $\log Q = 3$.
4. $E = E^{\circ}_{\mathrm{cell}} - \frac{0.059}{2}\log Q = 10.5 - 0.0295 \times 3$.
5. $E = 10.5 - 0.0885 = 10.4115\,\mathrm{V}$.
6. No option equals $10.4115\,\mathrm{V}$, so no option matches.

**Subtopic:** Nernst Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q087_6b421d98_04112026.png?v=6b421d9874e7)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q087_46627709_04112026.png?v=4662770942f8)

---

## Q88

Chemistry · physical · Structure of Atom

If radius of second Bohr orbit of the $\mathrm{He^{+}}$ ion is $105.8\,\mathrm{pm}$, what is the radius of third Bohr orbit of $\mathrm{Li^{2+}}$ ion?

- (1) $158.7\,\mathrm{\AA}$
- **(2)** $158.7\,\mathrm{pm}$
- (3) $15.87\,\mathrm{pm}$
- (4) $1.587\,\mathrm{pm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $r_n \propto \frac{n^2}{Z}$
2. $\frac{r_3(\mathrm{Li^{2+}})}{r_2(\mathrm{He^{+}})} = \frac{(n_3)^2}{Z(\mathrm{Li^{2+}})} \times \frac{Z(\mathrm{He^{+}})}{(n_2)^2}$
3. $\frac{r_3(\mathrm{Li^{2+}})}{105.8} = \frac{(3)^2}{3} \times \frac{2}{(2)^2}$
4. $= 105.8 \times \frac{3}{2}$
5. $r_3(\mathrm{Li^{2+}}) = 158.7\,\mathrm{pm}$

**Solved independently** (answer withheld)

1. Bohr radius formula: $r_n = 0.529\,\text{Å} \times \frac{n^2}{Z}$, i.e. $r_n = 52.9\,\text{pm} \times \frac{n^2}{Z}$.
2. Verify with He$^+$ ($Z=2$, $n=2$): $r = 52.9 \times \frac{4}{2} = 105.8\,\text{pm}$, matches given data.
3. For Li$^{2+}$ ($Z=3$, $n=3$): $r = 52.9 \times \frac{9}{3} = 52.9 \times 3 = 158.7\,\text{pm}$.
4. This matches option 2.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q088_ae565919_04112026.png?v=ae5659193aa8)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q088_0d3e54ff_04112026.png?v=0d3e54fffa3d)

---

## Q89

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The correct IUPAC name of the following compound is

![printed figure: 1-bromo-5-chloro-4-methylhexan-3-ol (skeletal structure: CH3-CH(Cl)-CH(CH3)-CH(OH)-CH2-CH2Br)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q089_81ca281f_04112026.png?v=81ca281f778e)

*1-bromo-5-chloro-4-methylhexan-3-ol (skeletal structure: CH3-CH(Cl)-CH(CH3)-CH(OH)-CH2-CH2Br)*

![drawn: 1-bromo-5-chloro-4-methylhexan-3-ol (skeletal structure: CH3-CH(Cl)-CH(CH3)-CH(OH)-CH2-CH2Br)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q089_question_373d9359_14112026.svg?v=373d93597a9e)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-bromo-5-chloro-4-methylhexan-3-ol `CC(Cl)C(C)C(O)CCBr` ![1-bromo-5-chloro-4-methylhexan-3-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q089_question_s1_b0fc92e9_14112026.svg?v=b0fc92e9b0c8)

- (1) 6-bromo-4-methyl-2-chlorohexan-4-ol
- **(2)** 1-bromo-5-chloro-4-methylhexan-3-ol
- (3) 6-bromo-2-chloro-4-methylhexan-4-ol
- (4) 1-bromo-4-methyl-5-chlorohexan-3-ol

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: 1-bromo-5-chloro-4-methylhexan-3-ol with main-chain carbons numbered 1 (CH2Br end) to 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q089_sol_1_31d00d96_04112026.png?v=31d00d962b54)

*1-bromo-5-chloro-4-methylhexan-3-ol with main-chain carbons numbered 1 (CH2Br end) to 6*

![drawn: 1-bromo-5-chloro-4-methylhexan-3-ol with main-chain carbons numbered 1 (CH2Br end) to 6](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q089_solution_1_10e0781b_14112026.svg?v=10e0781b91b2)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. 1-bromo-5-chloro-4-methylhexan-3-ol

**Solved independently** (answer withheld)

1. The longest chain containing $\ce{-OH}$ runs from the $\ce{CH2Br}$ carbon to the terminal $\ce{CH3}$ next to $\ce{CHCl}$: $6$ carbons, so the parent is hexan-ol.
2. Numbering from the Br end puts $\ce{-OH}$ at $C_3$; from the other end it would be $C_4$, so number from the Br end.
3. Substituents then sit at: Br on $C_1$, $\ce{CH3}$ on $C_4$, Cl on $C_5$.
4. Prefixes in alphabetical order: bromo, chloro, methyl $\Rightarrow$ 1-bromo-5-chloro-4-methylhexan-3-ol, which is option $2$.

**Subtopic:** Nomenclature of Organic Compounds Having Functional Group(s) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 37)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q089_aa0c3f2f_04112026.png?v=aa0c3f2fb897)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q089_e727eb1f_04112026.png?v=e727eb1fe4ff)

---

## Q90

Chemistry · organic · Amines

The product formed from the following reaction sequence is

![printed figure: benzonitrile →((i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O) (product not shown)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q090_dec3c451_04112026.png?v=dec3c451d35d)

*benzonitrile →[(i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O] (product not shown)*

![drawn: benzonitrile →((i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O) (product not shown)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_question_9422f0ae_14112026.svg?v=9422f0ae9ed5)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzonitrile `N#Cc1ccccc1` ![benzonitrile](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_question_s1_a95268da_14112026.svg?v=a95268da86c1)

- **(1)** phenylmethanol `OCc1ccccc1` ![phenylmethanol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_option_1_s1_76b1501e_14112026.svg?v=76b1501e4315)
- (2) benzamide `NC(=O)c1ccccc1` ![benzamide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_option_2_s1_2caebd61_14112026.svg?v=2caebd61a953)
- (3) phenylmethanediazonium chloride `N#[N+]Cc1ccccc1.[Cl-]` ![phenylmethanediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_option_3_s1_91c64fcc_14112026.svg?v=91c64fccaff9)
- (4) (chloromethyl)benzene `ClCc1ccccc1` ![(chloromethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_option_4_s1_d91fbed0_14112026.svg?v=d91fbed0f992)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: benzonitrile →((i) (a) LiAlH₄, (b) H₂O) phenylmethanamine →((ii) NaNO₂ + HCl) phenylmethanediazonium chloride →((iii) H₂O) phenylmethanol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q090_sol_1_9ab0ac88_04112026.png?v=9ab0ac8816c0)

*benzonitrile →[(i) (a) LiAlH₄, (b) H₂O] phenylmethanamine →[(ii) NaNO₂ + HCl] phenylmethanediazonium chloride →[(iii) H₂O] phenylmethanol*

![drawn: benzonitrile →((i) (a) LiAlH₄, (b) H₂O) phenylmethanamine →((ii) NaNO₂ + HCl) phenylmethanediazonium chloride →((iii) H₂O) phenylmethanol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q090_solution_1_7838c3d3_14112026.svg?v=7838c3d39cda)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. $\mathrm{LiAlH_4}$ then $\mathrm{H_2O}$ reduces the nitrile: $\mathrm{C_6H_5CN \rightarrow C_6H_5CH_2NH_2}$ (benzylamine).
2. $\mathrm{NaNO_2 + HCl}$ forms $\mathrm{HNO_2}$, which diazotises the primary aliphatic amine: $\mathrm{C_6H_5CH_2NH_2 \rightarrow C_6H_5CH_2N_2^+Cl^-}$.
3. An aliphatic diazonium salt is unstable; with $\mathrm{H_2O}$ it loses $\mathrm{N_2}$ to give $\mathrm{C_6H_5CH_2OH}$ (benzyl alcohol).
4. Benzyl alcohol is the structure in option $1$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 37)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q090_da4c8f3e_04112026.png?v=da4c8f3ee660)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q090_4b788c79_04112026.png?v=4b788c79f170)

---

## Q91

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Which one of the following is not formed when acetone reacts with 2-pentanone in the presence of dilute $\mathrm{NaOH}$ followed by heating?

- (1) 3-ethyl-4-methylpent-3-en-2-one `CCC(C(C)=O)=C(C)C` ![3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_option_1_s1_66feab5b_14112026.svg?v=66feab5b6d50)
- (2) 4-methylpent-3-en-2-one `CC(=O)C=C(C)C` ![4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_option_2_s1_15fe930f_14112026.svg?v=15fe930f4a06)
- **(3)** 5-ethyl-4-methylhept-4-en-3-one `CCC(=O)C(C)=C(CC)CC` ![5-ethyl-4-methylhept-4-en-3-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_option_3_s1_1bfa134b_14112026.svg?v=1bfa134bd650)
- (4) 4-methylhept-3-en-2-one `CCCC(C)=CC(C)=O` ![4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_option_4_s1_cb45c8ef_14112026.svg?v=cb45c8efc96c)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Cross Aldol condensation reaction:
2. Both reactants contain $\alpha$-Hydrogens, so multiple products are possible which are as follows:

![printed figure: acetone + pentan-2-one →(dil NaOH / Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_1_2c501bc1_04112026.png?v=2c501bc14a8b)

*acetone + pentan-2-one →[dil NaOH / Δ]*

![drawn: acetone + pentan-2-one →(dil NaOH / Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_1_ac7a4928_14112026.svg?v=ac7a4928d157)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 1. 4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_2_c0e7d3c2_04112026.png?v=c0e7d3c26bc3)

*1. 4-methylhept-3-en-2-one*

![drawn: 1. 4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_2_61d1bc27_14112026.svg?v=61d1bc27d125)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 2. 2-methylhept-2-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_3_13bc033b_04112026.png?v=13bc033bf082)

*2. 2-methylhept-2-en-4-one*

![drawn: 2. 2-methylhept-2-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_3_25399d64_14112026.svg?v=25399d64b68c)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 3. 3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_4_a1f35a86_04112026.png?v=a1f35a865f04)

*3. 3-ethyl-4-methylpent-3-en-2-one*

![drawn: 3. 3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_4_7340308d_14112026.svg?v=7340308d3d28)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 4. 4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_5_8dacabe1_04112026.png?v=8dacabe13293)

*4. 4-methylpent-3-en-2-one*

![drawn: 4. 4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_5_20886cd7_14112026.svg?v=20886cd7232d)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 5. 6-methylnon-5-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_6_7704d35d_04112026.png?v=7704d35dfd2a)

*5. 6-methylnon-5-en-4-one*

![drawn: 5. 6-methylnon-5-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_6_fbf8996f_14112026.svg?v=fbf8996f2f01)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 6. 3-ethyl-4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q091_sol_7_a672ddd1_04112026.png?v=a672ddd16360)

*6. 3-ethyl-4-methylhept-3-en-2-one*

![drawn: 6. 3-ethyl-4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q091_solution_7_139d368c_14112026.svg?v=139d368c6449)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. $\Rightarrow$ (3) is not possible.

**Solved independently** (answer withheld)

1. Aldol condensation joins an enolate $\alpha$-carbon to another carbonyl carbon, then dehydrates on heating to give an $\alpha,\beta$-unsaturated ketone.
2. Acetone + acetone gives $(\mathrm{CH_3})_2C=CH\text{-}CO\text{-}CH_3$, option $2$.
3. Acetone enolate + 2-pentanone carbonyl gives $\mathrm{CH_3COCH}=C(\mathrm{CH_3})\mathrm{CH_2CH_2CH_3}$, option $4$.
4. 2-Pentanone enolate at C-3 + acetone carbonyl gives $\mathrm{CH_3CO}C(\mathrm{C_2H_5})=C(\mathrm{CH_3})_2$, option $1$.
5. Option $3$, $\mathrm{C_2H_5CO}C(\mathrm{CH_3})=C(\mathrm{C_2H_5})_2$, requires 3-pentanone as both enolate and carbonyl partner, so it cannot form here: option $3$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 38)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q091_ef0c993d_04112026.png?v=ef0c993dca9f)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q091_88fc6c82_04112026.png?v=88fc6c829f61)

---

## Q92

Chemistry · physical · The Solid State

Copper crystallises in fcc unit cell with cell edge length of $3.608 \times 10^{-8}\,\mathrm{cm}$. The density of copper is $8.92\,\mathrm{g\,cm^{-3}}$. Calculate the atomic mass of copper.

- (1) $65\,\mathrm{u}$
- **(2)** $63.1\,\mathrm{u}$
- (3) $31.55\,\mathrm{u}$
- (4) $60\,\mathrm{u}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $d = \frac{ZM}{N_A (a)^3}$
2. $Z = 4(\mathrm{FCC})$, $d = 8.92\,\mathrm{g\,cm^{-3}}$, $N_A = 6.023 \times 10^{23}$, $a = 3.608 \times 10^{-8}\,\mathrm{cm}$
3. $M = \frac{d N_A (a)^3}{Z}$
4. $= \frac{8.92 \times 6.023 \times 10^{23} \times (3.608 \times 10^{-8})^3}{4}$
5. $= \frac{8.92 \times 6.023 \times 10^{23} \times 46.97 \times 10^{-24}}{4} = \frac{2523.47 \times 10^{-1}}{4}$
6. $= 630.8 \times 10^{-1} = 63.08 \simeq 63.1\,\mathrm{u}$

**Solved independently** (answer withheld)

1. For an fcc unit cell, $Z = 4$ atoms per cell.
2. Density relation: $d = \frac{Z M}{a^3 N_A}$, so $M = \frac{d\,a^3 N_A}{Z}$.
3. $a^3 = (3.608 \times 10^{-8}\,\mathrm{cm})^3 = 46.97 \times 10^{-24}\,\mathrm{cm^3}$.
4. $d\,a^3 = 8.92 \times 46.97 \times 10^{-24} = 418.96 \times 10^{-24}\,\mathrm{g}$.
5. $d\,a^3 N_A = 418.96 \times 10^{-24} \times 6.022 \times 10^{23} = 252.3\,\mathrm{g\,mol^{-1}}$.
6. $M = \frac{252.3}{4} = 63.07 \approx 63.1\,\mathrm{u}$, which is option $2$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 38)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q092_0d62d92a_04112026.png?v=0d62d92ac271)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q092_b5e035cf_04112026.png?v=b5e035cfa70f)

---

## Q93

Chemistry · physical · States of Matter

A $10.0\,\mathrm{L}$ flask contains $64\,\mathrm{g}$ of oxygen at $27^\circ\mathrm{C}$. (Assume $\mathrm{O_2}$ gas is behaving ideally). The pressure inside the flask in bar is (Given $R = 0.0831\,\mathrm{L\ bar\ K^{-1}\ mol^{-1}}$)

- **(1)** $4.9$
- (2) $2.5$
- (3) $498.6$
- (4) $49.8$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. We know for ideal gas
2. $\mathrm{PV} = \mathrm{nRT}$
3. $\mathrm{P} = \mathrm{n}\frac{\mathrm{RT}}{\mathrm{V}}$
4. $\mathrm{P} = \frac{64}{32} \times \frac{0.0831 \times 300}{10}$
5. $\mathrm{P} = 4.9\ \mathrm{bar}$
6. Pressure of $\mathrm{O_2}$ gas inside the flask $= 4.9\ \mathrm{bar}$

**Solved independently** (answer withheld)

1. $n = \frac{64\,\mathrm{g}}{32\,\mathrm{g\,mol^{-1}}} = 2\,\mathrm{mol}$.
2. $T = 27 + 273 = 300\,\mathrm{K}$.
3. $P = \frac{nRT}{V} = \frac{2 \times 0.0831 \times 300}{10.0}$.
4. $P = \frac{49.86}{10.0} = 4.986\,\mathrm{bar} \approx 4.9\,\mathrm{bar}$, which is option $1$.

**Subtopic:** Gas Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q093_fad22d07_04112026.png?v=fad22d074353)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q093_b55b1483_04112026.png?v=b55b1483510f)

---

## Q94

Chemistry · inorganic · Environmental Chemistry

The pollution due to oxides of sulphur gets enhanced due to the presence of:
Choose the most appropriate answer from the options given below:

- (a) particulate matter
- (b) ozone
- (c) hydrocarbons
- (d) hydrogen peroxide

- (1) (a), (c), (d) only
- (2) (a), (d) only
- **(3)** (a), (b), (d) only
- (4) (b), (c), (d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Presence of particulate matter in polluted air catalyzes the oxidation of $\mathrm{SO_2}$ to $\mathrm{SO_3}$
2. i.e., $2\mathrm{SO_2}\left(g\right)+\mathrm{O_2}\left(g\right)\longrightarrow 2\mathrm{SO_3}\left(g\right)$
3. This reaction can also be promoted by $\mathrm{O_3}$ and $\mathrm{H_2O_2}$, as
4. $\mathrm{SO_2}\left(g\right)+\mathrm{O_3}\left(g\right)\longrightarrow \mathrm{SO_3}\left(g\right)+\mathrm{O_2}\left(g\right)$
5. $\mathrm{SO_2}\left(g\right)+\mathrm{H_2O_2}\left(l\right)\longrightarrow \mathrm{H_2SO_4}\left(aq\right)$

**Solved independently** (answer withheld)

1. Particulate matter in polluted air catalyses the oxidation $\mathrm{2SO_2 + O_2 \rightarrow 2SO_3}$, so (a) enhances the pollution.
2. Ozone ($\mathrm{O_3}$) and hydrogen peroxide ($\mathrm{H_2O_2}$) also promote the oxidation of $\mathrm{SO_2}$ to $\mathrm{SO_3}$, so (b) and (d) enhance it.
3. Hydrocarbons are not an agent of $\mathrm{SO_2}$ oxidation, so (c) is excluded.
4. The set (a), (b), (d) only is option $3$.

**Subtopic:** Air Pollution · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 39)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q094_84e9ca18_04112026.png?v=84e9ca18fbd8)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q094_99a80979_04112026.png?v=99a809790f47)

---

## Q95

Chemistry · physical · Chemical Equilibrium

$\mathrm{3O_2(g)} \rightleftharpoons \mathrm{2O_3(g)}$
for the above reaction at $298\,\mathrm{K}$, $\mathrm{K_C}$ is found to be $3.0 \times 10^{-59}$. If the concentration of $\mathrm{O_2}$ at equilibrium is $0.040\,\mathrm{M}$ then concentration of $\mathrm{O_3}$ in M is

- (1) $1.2 \times 10^{21}$
- **(2)** $4.38 \times 10^{-32}$
- (3) $1.9 \times 10^{-63}$
- (4) $2.4 \times 10^{31}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{3O_2(g)} \rightleftharpoons \mathrm{2O_3(g)}$
2. $\mathrm{K_C} = \frac{[\mathrm{O_3}]^2}{[\mathrm{O_2}]^3}$
3. $[\mathrm{O_3}]^2 = \mathrm{K_C}[\mathrm{O_2}]^3 = 3 \times 10^{-59} \times (0.04)^3$
4. $[\mathrm{O_3}]^2 = 1.9 \times 10^{-63} = 19 \times 10^{-64}$
5. $[\mathrm{O_3}] = 4.38 \times 10^{-32}$
6. Concentration of $\mathrm{O_3}$ at equilibrium $= 4.38 \times 10^{-32}\,\mathrm{M}$

**Solved independently** (answer withheld)

1. $K_C = \frac{[\mathrm{O_3}]^2}{[\mathrm{O_2}]^3}$.
2. $[\mathrm{O_2}]^3 = (0.040)^3 = 6.4 \times 10^{-5}$.
3. $[\mathrm{O_3}]^2 = 3.0 \times 10^{-59} \times 6.4 \times 10^{-5} = 1.92 \times 10^{-63} = 19.2 \times 10^{-64}$.
4. $[\mathrm{O_3}] = \sqrt{19.2} \times 10^{-32} \approx 4.38 \times 10^{-32}\,\mathrm{M}$, which is option $2$.

**Subtopic:** Calculating Equilibrium Concentrations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 39)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q095_36bb80c1_04112026.png?v=36bb80c12012)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q095_b16c8a91_04112026.png?v=b16c8a91a827)

---

## Q96

Chemistry · physical · Chemical Kinetics

For a first order reaction A $\rightarrow$ Products, initial concentration of A is $0.1\,\mathrm{M}$, which becomes $0.001\,\mathrm{M}$ after 5 minutes. Rate constant for the reaction in $\mathrm{min^{-1}}$ is

- (1) $0.2303$
- (2) $1.3818$
- **(3)** $0.9212$
- (4) $0.4606$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For first order reaction,
2. $\mathrm{K} = \frac{2.303}{t}\log\frac{[\mathrm{A_0}]}{[\mathrm{A}]}$;   where $\mathrm{A_0}$ is the initial concentration of reactant A.
3. $\mathrm{A_0} = 0.1\,\mathrm{M}$
4. $\mathrm{A} = 0.001\,\mathrm{M}$
5. $t = 5$ minute
6. $\mathrm{K} = \frac{2.303}{5}\log\frac{0.1}{0.001} = \frac{2.303}{5}\log 10^{2}$
7. $= \frac{2.303}{5}\times 2$
8. $\mathrm{K} = 0.9212\,\mathrm{min^{-1}}$

**Solved independently** (answer withheld)

1. For a first order reaction, $k = \frac{2.303}{t}\log\frac{[A]_0}{[A]}$.
2. $\frac{[A]_0}{[A]} = \frac{0.1}{0.001} = 100$, so $\log 100 = 2$.
3. $k = \frac{2.303}{5} \times 2 = \frac{4.606}{5} = 0.9212\,\mathrm{min^{-1}}$, which is option $3$.

**Subtopic:** First Order Reactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q096_a5fbf6f7_04112026.png?v=a5fbf6f77fe3)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q096_4c60d05c_04112026.png?v=4c60d05c34c6)

---

## Q97

Chemistry · inorganic · The D- and F-Block Elements – Practice

In the neutral or faintly alkaline medium, $\mathrm{KMnO_4}$ oxidises iodide into iodate. The change in oxidation state of manganese in this reaction is from

- (1) $+6$ to $+5$
- **(2)** $+7$ to $+4$
- (3) $+6$ to $+4$
- (4) $+7$ to $+3$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In neutral or faintly alkaline solution.
2. $2\overset{+7}{\mathrm{Mn}}\mathrm{O_4^-} + \mathrm{H_2O} + \overset{-1}{\mathrm{I^-}}\ (\text{iodide}) \rightarrow 2\overset{+4}{\mathrm{Mn}}\mathrm{O_2} + 2\mathrm{OH^-} + \overset{+5}{\mathrm{I}}\mathrm{O_3^-}\ (\text{iodate})$
3. Manganese $(\mathrm{Mn})$ oxidation state change from $+7$ to $+4$.

**Solved independently** (answer withheld)

1. In neutral or faintly alkaline medium, $\mathrm{MnO_4^-}$ is reduced to $\mathrm{MnO_2}$: $2\mathrm{MnO_4^-} + \mathrm{I^-} + \mathrm{H_2O} \rightarrow 2\mathrm{MnO_2} + \mathrm{IO_3^-} + 2\mathrm{OH^-}$.
2. Oxidation state of Mn in $\mathrm{KMnO_4}$: $+1 + x + 4(-2) = 0 \Rightarrow x = +7$.
3. Oxidation state of Mn in $\mathrm{MnO_2}$: $x + 2(-2) = 0 \Rightarrow x = +4$.
4. Change is $+7$ to $+4$, which is option $2$.

**Subtopic:** Potassium Permanganate (KMnO4) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q097_64ea7c04_04112026.png?v=64ea7c042674)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q097_9b6e2e01_04112026.png?v=9b6e2e0127a5)

---

## Q98

Chemistry · organic · Hydrocarbons

Compound X on reaction with $\mathrm{O_3}$ followed by $\mathrm{Zn/H_2O}$ gives formaldehyde and 2-methyl propanal as products. The compound X is

- (1) Pent-2-ene
- **(2)** 3-Methylbut-1-ene
- (3) 2-Methylbut-1-ene
- (4) 2-Methylbut-2-ene

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. 2-Methylpropanal; Formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q098_sol_1_77690a08_04112026.png?v=77690a0829e6)

*I. 2-Methylpropanal; Formaldehyde*

![drawn: I. 2-Methylpropanal; Formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q098_solution_1_b0f0f39e_14112026.svg?v=b0f0f39e5ee7)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. The given reaction is the reductive ozonolysis of an alkene. The alkene will be

![printed figure: 3-methylbut-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q098_sol_2_1e628d0d_04112026.png?v=1e628d0da60a)

*3-methylbut-1-ene*

![drawn: 3-methylbut-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q098_solution_2_bf651f87_14112026.svg?v=bf651f877a83)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 3-Methylbut-1-ene →((i) $\ce{O3}$ (ii) $\ce{Zn/H2O}$) 2-methylpropanal + formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q098_sol_3_6e736f18_04112026.png?v=6e736f183803)

*3-Methylbut-1-ene →[(i) $\ce{O3}$ (ii) $\ce{Zn/H2O}$] 2-methylpropanal + formaldehyde*

![drawn: 3-Methylbut-1-ene →((i) $\ce{O3}$ (ii) $\ce{Zn/H2O}$) 2-methylpropanal + formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2022/2022_R4/figures_drawn/q098_solution_3_b3effec2_14112026.svg?v=b3effec25c27)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Reductive ozonolysis splits the $\mathrm{C=C}$ bond and turns each alkene carbon into a $\mathrm{C=O}$ group.
2. Formaldehyde $\mathrm{HCHO}$ comes from a terminal $\mathrm{=CH_2}$ group, and 2-methylpropanal $\mathrm{(CH_3)_2CH{-}CHO}$ comes from a $\mathrm{=CH{-}CH(CH_3)_2}$ fragment.
3. Join the two carbonyl carbons with a double bond: $\mathrm{CH_2{=}CH{-}CH(CH_3)_2}$.
4. $\mathrm{CH_2{=}CH{-}CH(CH_3)_2}$ is 3-methylbut-1-ene, which is option $2$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 40)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q098_d7094671_04112026.png?v=d70946713c72)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q098_58c630c5_04112026.png?v=58c630c598a9)

---

## Q99

Chemistry · organic · Alcohols, Phenols and Ethers

Given below are two statements:

- (Statement I) In Lucas test, primary, secondary and tertiary alcohols are distinguished on the basis of their reactivity with conc. $\mathrm{HCl}$ + $\mathrm{ZnCl_2}$, known as Lucas Reagent.
- (Statement II) Primary alcohols are most reactive and immediately produce turbidity at room temperature on reaction with Lucas Reagent.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Primary, secondary and tertiary alcohols can be differentiated by their reaction with ($\mathrm{HCl}$ + anhy $\mathrm{ZnCl_2}$) Lucas reagent
2. $3^\circ$ alcohol $\xrightarrow{\mathrm{ZnCl_2}+\mathrm{HCl}}$ Immediate turbidity at room temperature
3. $2^\circ$ alcohol $\xrightarrow{\mathrm{ZnCl_2}+\mathrm{HCl}}$ Turbidity after 5 minutes at room temperature
4. $1^\circ$ alcohol $\xrightarrow{\mathrm{ZnCl_2}+\mathrm{HCl}}$ Do not gives turbidity at room temperature

**Solved independently** (answer withheld)

1. Statement I: Lucas reagent (conc. HCl + anhydrous ZnCl₂) distinguishes 1°, 2°, 3° alcohols via SN1 reactivity — this is correct as per NCERT.
2. Statement II: Reactivity order with Lucas reagent is 3° > 2° > 1° because tertiary carbocations form fastest; primary alcohols do not react at room temperature, they need heating.
3. Thus Statement I is correct but Statement II is incorrect, matching option 4.

**Subtopic:** Test of Alcohol · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q099_422324d7_04112026.png?v=422324d7a317)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q099_f5a90ddf_04112026.png?v=f5a90ddf6aeb)

---

## Q100

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Match List-I with List-II.

List-I (Ores) ; List-II (Composition)

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Haematite | (i) | $\mathrm{Fe_3O_4}$ |
| (b) | Magnetite | (ii) | $\mathrm{ZnCO_3}$ |
| (c) | Calamine | (iii) | $\mathrm{Fe_2O_3}$ |
| (d) | Kaolinite | (iv) | $[\mathrm{Al_2(OH)_4Si_2O_5}]$ |

- (1) (a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)
- (2) (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)
- **(3)** (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)
- (4) (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (Ores) — (Composition)
2. (a) Haematite $\rightarrow$ $\mathrm{Fe_2O_3}$
3. (b) Magnetite $\rightarrow$ $\mathrm{Fe_3O_4}$
4. (c) Calamine $\rightarrow$ $\mathrm{ZnCO_3}$
5. (d) Kaolinite $\rightarrow$ $[\mathrm{Al_2(OH)_4Si_2O_5}]$

**Solved independently** (answer withheld)

1. Haematite is $\mathrm{Fe_2O_3}$ (iii), magnetite is $\mathrm{Fe_3O_4}$ (i), calamine is $\mathrm{ZnCO_3}$ (ii) and kaolinite is $\mathrm{[Al_2(OH)_4Si_2O_5]}$ (iv), which is option $3$.

**Subtopic:** Occurrence of Metals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q100_104f1b85_04112026.png?v=104f1b859f67)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q100_419184c3_04112026.png?v=419184c3c494)

---

## Q101

Biology · botany · Biotechnology: Principles and Processes

Which one of the following statement is **not true** regarding gel electrophoresis technique?

- (1) Bright orange coloured bands of DNA can be observed in the gel when exposed to UV light.
- (2) The process of extraction of separated DNA strands from gel is called elution.
- (3) The separated DNA fragments are stained by using ethidium bromide.
- **(4)** The presence of chromogenic substrate gives blue coloured DNA bands on the gel.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option $(4)$ is the incorrect statement, as bright colored bands of DNA can be observed in the gel when EtBr (Ethidium bromide) treated DNA is exposed to UV light.

**Solved independently** (answer withheld)

1. Elution (2), ethidium bromide staining (3) and bright orange bands under UV light (1) are all true of gel electrophoresis; a chromogenic substrate giving blue colour relates to blue-white selection of recombinant colonies, not to DNA bands on a gel, so statement $3$ is not true.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q101_3b170c42_04112026.png?v=3b170c429da6)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q101_e863eaac_04112026.png?v=e863eaac83ea)

---

## Q102

Biology · botany · Mineral Nutrition

Which one of the following produces nitrogen fixing nodules on the roots of *Alnus*?

- (1) *Beijerinckia*
- (2) *Rhizobium*
- **(3)** *Frankia*
- (4) *Rhodospirillum*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The microbe, *Frankia*, produces nitrogen fixing nodules on the roots of non-leguminous plants (e.g. *Alnus*)

**Solved independently** (answer withheld)

1. Nitrogen-fixing nodules on the roots of the non-leguminous plant $Alnus$ are formed by the actinomycete $Frankia$, which is option $3$.

**Subtopic:** Nitrogen Fixation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q102_51e9de43_04112026.png?v=51e9de430ba8)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q102_bbc5cdff_04112026.png?v=bbc5cdff3609)

---

## Q103

Biology · botany · Principles of Inheritance and Variation

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Mendel studied seven pairs of contrasting traits in pea plants and proposed the Laws of Inheritance.
- (Statement II) Seven characters examined by Mendel in his experiment on pea plants were seed shape and colour, flower colour, pod shape and colour, flower position and stem height.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Gregor J. Mendel, conducted hybridisation experiments on garden peas and selected $14$ true breeding pea plant varieties (seven contrasting traits).
2. Contrasting traits studied were smooth or wrinkled seeds, yellow or green seeds, inflated on constricted pods, green or yellow pods, tall or dwarf plants, violet or white flowers and axial or terminal flower positions.

**Solved independently** (answer withheld)

1. Statement I: Mendel worked with $7$ pairs of contrasting traits in garden pea and proposed the Laws of Inheritance, so it is correct.
2. Statement II lists seed shape, seed colour, flower colour, pod shape, pod colour, flower position and stem height, which is $7$ characters matching Mendel's set, so it is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Contrasting Traits Studied by Mendel in Pea · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q103_99baf5f2_04112026.png?v=99baf5f295ff)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q103_b2315fc1_04112026.png?v=b2315fc162fe)

---

## Q104

Biology · botany · Biodiversity and Conservation

Which of the following is **not** a method of *ex situ* conservation?

- (1) Cryopreservation
- (2) *In vitro* fertilization
- **(3)** National Parks
- (4) Micropropagation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. *In-situ* conservation means on site conservation i.e. when we conserve and protect the whole ecosystem, its biodiversity at all levels is protected.
2. National parks are type of *in-situ* conservation.
3. Whereas, micropropagation, cryopreservation and *in-vitro* fertilisation are methods of *ex-situ* conservation.

**Solved independently** (answer withheld)

1. National Parks conserve organisms in their natural habitat, which is in situ conservation, whereas in vitro fertilization, micropropagation and cryopreservation are ex situ methods, so the answer is option $3$.

**Subtopic:** Ex Situ Conservation, In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q104_660a5acb_04112026.png?v=660a5acbf5ac)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q104_7ac26920_04112026.png?v=7ac26920faa1)

---

## Q105

Biology · botany · Organisms and Populations

Which one of the following statements cannot be connected to Predation?

- (1) It is necessitated by nature to maintain the ecological balance
- (2) It helps in maintaining species diversity in a community
- (3) It might lead to extinction of a species
- **(4)** Both the interacting species are negatively impacted

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. One of the species in predation gains benefit on the expense of the other.
2. Predators help in maintaining species diversity in a community, by reducing the intensity of competition among competing prey species.
3. If a predator is too efficient and overexploits its prey, then the prey might become extinct.

**Solved independently** (answer withheld)

1. Predation is a $(+,-)$ interaction: the predator gains and the prey is harmed; an interaction where both species are harmed $(-,-)$ is competition, so option $4$ cannot be connected to predation.

**Subtopic:** Predation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q105_839e7ae8_04112026.png?v=839e7ae89eeb)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q105_f0d8f25f_04112026.png?v=f0d8f25ff9ac)

---

## Q106

Biology · botany · Mineral Nutrition

Match **List-I** with **List-II**

Choose the **correct answer** from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Manganese | (i) | Activates the enzyme catalase |
| (b) | Magnesium | (ii) | Required for pollen germination |
| (c) | Boron | (iii) | Activates enzymes of respiration |
| (d) | Iron | (iv) | Functions in splitting of water during photosynthesis |

- (1) (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)
- (2) (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)
- **(3)** (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)
- (4) (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Manganese plays a major role in the splitting of water to liberate oxygen during photosynthesis.
2. Magnesium activates several enzymes involved in photosynthesis and respiration.
3. Boron is involved in pollen germination. Iron activates the catalase and some other enzymes.

**Solved independently** (answer withheld)

1. Manganese is needed for the photolysis (splitting) of water during photosynthesis, so (a)-(iv).
2. Magnesium activates enzymes of respiration and photosynthesis, so (b)-(iii).
3. Boron is required for pollen germination, so (c)-(ii).
4. Iron activates the enzyme catalase, so (d)-(i).
5. The match (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i) is option $3$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 43)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q106_b3e816c1_04112026.png?v=b3e816c118de)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q106_fe9d3008_04112026.png?v=fe9d30084739)

---

## Q107

Biology · botany · Plant Growth and Development

The gaseous plant growth regulator is used in plants to :

- (1) kill dicotyledonous weeds in the fields
- (2) speed up the malting process
- **(3)** promote root growth and roothair formation to increase the absorption surface
- (4) help overcome apical dominance

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ethylene is a gaseous plant hormone. It induces development of adventitious roots on various types of cutting.
2. It promotes the development of lateral roots and growth of root hairs.
3. Cytokinin helps to overcome the apical dominance.
4. Auxin is used to kill dicot weeds. Gibberellin speeds up the malting process

**Solved independently** (answer withheld)

1. The only gaseous plant growth regulator is ethylene; per NCERT it promotes root growth and root hair formation to increase the absorption surface, while options 2, 4 and 1 describe gibberellins, cytokinins and auxin (2,4-D) respectively, so the answer is option $3$.

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q107_6b7cd1a5_04112026.png?v=6b7cd1a555f7)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q107_466af5fb_04112026.png?v=466af5fbec14)

---

## Q108

Biology · botany · Cell Cycle and Cell Division

The appearance of recombination nodules on homologous chromosomes during meiosis characterizes :

- (1) Terminalization
- (2) Synaptonemal complex
- (3) Bivalent
- **(4)** Sites at which crossing over occurs

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Pachytene stage of meiosis is characterised by the appearance of recombination nodules, the sites at which crossing over occurs between non sister chromatids of homologous chromosomes.

**Solved independently** (answer withheld)

1. In pachytene of prophase I, NCERT describes the appearance of recombination nodules as marking the sites at which crossing over occurs between non-sister chromatids of homologous chromosomes, which is option $4$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 43)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q108_9306b3a2_04112026.png?v=9306b3a2bd07)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q108_c0da6752_04112026.png?v=c0da6752efe7)

---

## Q109

Biology · botany · Anatomy of Flowering Plants

In old trees the greater part of secondary xylem is dark brown and resistant to insect attack due to :

- (a) secretion of secondary metabolities and their deposition in the lumen of vessels.
- (b) deposition of organic compounds like tannins and resins in the central layers of stem.
- (c) deposition of suberin and aromatic substances in the outer layer of stem.
- (d) deposition of tannins, gum, resin and aromatic substances in the peripheral layers of stem.
- (e) presence of parenchyma cells, functionally active xylem elements and essential oils.

- (1) (b) and (d) Only
- **(2)** (a) and (b) Only
- (3) (c) and (d) Only
- (4) (d) and (e) Only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In old trees, the greater part of secondary xylem is dark brown due to deposition of organic compounds like tannins, resins, oils, gums, aromatic substances and essential oils in the central or innermost layers of the stem.
2. These substances make it hard, durable and resistant to the attacks of micro-organisms and insects.

**Solved independently** (answer withheld)

1. Heartwood is the central, dark, durable part of secondary xylem in old trees.
2. Its resistance arises from secretion of tannins, resins, gums, and aromatic substances that get deposited in the lumen of vessels (statement a) and in the central layers of the stem (statement b).
3. Statements (c) and (d) wrongly place these deposits in the peripheral/outer layers, which actually describes sapwood region, not heartwood.
4. Statement (e) describes sapwood (functionally active xylem), not heartwood.
5. Hence only (a) and (b) are correct, matching option 2.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q109_ca2546b6_04112026.png?v=ca2546b61c1d)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q109_9ea10e37_04112026.png?v=9ea10e371ac1)

---

## Q110

Biology · botany · Morphology of Flowering Plants

Identify the **correct** set of statements :
Choose the **correct answer** from the options given below :

- (a) The leaflets are modified into pointed hard thorns in Citrus and Bougainvillea
- (b) Axillary buds form slender and spirally coiled tendrils in cucumber and pumpkin
- (c) Stem is flattened and fleshy in Opuntia and modified to perform the function of leaves
- (d) Rhizophora shows vertically upward growing roots that help to get oxygen for respiration
- (e) Subaerially growing stems in grasses and strawberry help in vegetative propagation

- (1) (a), (b), (d) and (e) Only
- (2) (b) and (c) Only
- (3) (a) and (d) Only
- **(4)** (b), (c), (d) and (e) Only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Axillary buds of stems get modified into woody, straight and pointed thorns.
2. Thorns are found in many plants such as $\textit{Citrus}$ and $\textit{Bougainvillea}$.

**Solved independently** (answer withheld)

1. (a) is false: in $Citrus$ and $Bougainvillea$ the thorns are modified axillary buds (stem modification), not leaflets.
2. (b) is true: stem tendrils arising from axillary buds are slender and spirally coiled in cucumber and pumpkin.
3. (c) is true: $Opuntia$ has a flattened, fleshy green stem (phylloclade) that performs the function of leaves.
4. (d) is true: $Rhizophora$ has pneumatophores, roots growing vertically upward to obtain oxygen for respiration.
5. (e) is true: subaerially growing stems (runners/stolons) in grasses and strawberry help in vegetative propagation.
6. Correct set is (b), (c), (d) and (e) only, which is option $4$.

**Subtopic:** The Stem, The Root · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 44)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q110_04892054_04112026.png?v=04892054c3a9)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q110_b2918ec7_04112026.png?v=b2918ec7fa2e)

---

## Q111

Biology · botany · Principles of Inheritance and Variation

XO type of sex determination can be found in :

- (1) Monkeys
- (2) $\textit{Drosophila}$
- (3) Birds
- **(4)** Grasshoppers

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Grasshopper is an example of XO type of sex determination in which the males have only one X-chromosome besides the autosomes, whereas females have a pair of X-chromosomes.

**Solved independently** (answer withheld)

1. In grasshoppers, males are XO (only one sex chromosome) and females are XX, a classic example of the XO type of sex determination.
2. Drosophila and monkeys use the XX-XY system, while birds use the ZW system, so these are ruled out.

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q111_3a5f5259_04112026.png?v=3a5f525933f8)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q111_e7325928_04112026.png?v=e7325928161b)

---

## Q112

Biology · botany · Anatomy of Flowering Plants

> ⚠ The booklet prints "Answer (NA) No option is correct": none of the four options is correct as printed, so there is no keyed answer to check a solve against.

> ⚠ The printed solution says "All the statements are correct regarding vascular bundles but none of the options with such combination is given.": the question has no correct option as printed, and the printed answer comes from a corrected reading.

> ⚠ The independent solve found no printed option exactly right ("No option lists exactly the set of true statements: by NCERT all five statements (a)-(e) are true, but every option omits at least one"); its pick (unsure) is the closest fit, so treat this question as possibly misprinted.

Read the following statements about the vascular bundles :
Choose the **correct answer** from the options given below :

- (a) In roots, xylem and phloem in a vascular bundle are arranged in an alternate manner along the different radii.
- (b) Conjoint closed vascular bundles do not possess cambium
- (c) In open vascular bundles, cambium is present in between xylem and phloem
- (d) The vascular bundles of dicotyledonous stem possess endarch protoxylem
- (e) In monocotyledonous root, usually there are more than six xylem bundles present

- (1) (a), (c), (d) and (e) Only
- (2) (a), (b) and (d) Only
- (3) (b), (c), (d) and (e) Only
- (4) (a), (b), (c) and (d) Only

**Answer** — booklet: (none) · independent solve: (unsure) · publisher_no_valid_option

**Publisher's solution**

1. All the statements are correct regarding vascular bundles but none of the options with such combination is given.

**Solved independently** (answer withheld)

1. (a) In roots xylem and phloem lie on alternate radii (radial bundles): true.
2. (b) Conjoint closed bundles have no cambium: true.
3. (c) In open bundles cambium lies between xylem and phloem: true.
4. (d) Dicot stem vascular bundles have endarch protoxylem: true.
5. (e) Monocot root is polyarch, usually more than six xylem bundles: true.
6. True set $= \{a, b, c, d, e\}$; options give $\{a,b,d\}$, $\{b,c,d,e\}$, $\{a,b,c,d\}$, $\{a,c,d,e\}$; none matches exactly.

**Subtopic:** The Tissue System · **Difficulty:** hard (6 steps)

**Printed in the booklet** (page 44)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q112_0c40c4e9_04112026.png?v=0c40c4e93b7a)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q112_4341d4cb_04112026.png?v=4341d4cb22d9)

---

## Q113

Biology · botany · Molecular Basis of Inheritance

The process of translation of mRNA to proteins begins as soon as :

- (1) The tRNA is activated and the larger subunit of ribosome encounters mRNA
- **(2)** The small subunit of ribosome encounters mRNA
- (3) The larger subunit of ribosome encounters mRNA
- (4) Both the subunits join together to bind with mRNA

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When the small subunit of ribosome encounters an mRNA, the process of translation of the mRNA to protein begins. This process is followed by the binding of bigger/larger subunit.
2. t-RNA is activated by the addition of amino acid prior to the attachment of ribosome, in the first phase.

**Solved independently** (answer withheld)

1. An inactive ribosome exists as two separate subunits, and translation of mRNA into protein begins as soon as the small subunit encounters the mRNA, which is option $2$.

**Subtopic:** Translation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 45)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q113_6546ece2_04112026.png?v=6546ece29add)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q113_cad0c3d7_04112026.png?v=cad0c3d7c3c7)

---

## Q114

Biology · botany · Environmental Issues

The device which can remove particulate matter present in the exhaust from a thermal power plant is :

- (1) Catalytic Convertor
- (2) STP
- (3) Incinerator
- **(4)** Electrostatic Precipitator

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Electrostatic precipitator can remove over $99\%$ particulate matter present in the exhaust from a thermal power plant.
2. Catalytic converters are fitted into automobiles for reducing emission of poisonous gases.
3. STPs are associated with sewage treatment.

**Solved independently** (answer withheld)

1. An electrostatic precipitator charges the dust particles in the exhaust and collects them on oppositely charged plates, removing particulate matter from thermal power plant exhaust, which is option $4$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q114_b846e357_04112026.png?v=b846e357ed80)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q114_3de9f173_04112026.png?v=3de9f1735cb9)

---

## Q115

Biology · botany · Morphology of Flowering Plants

The flowers are Zygomorphic in:
Choose the **correct answer** from the options given below:

- (a) Mustard
- (b) Gulmohar
- (c) Cassia
- (d) Datura
- (e) Chilly

- (1) (c), (d), (e) Only
- (2) (a), (b), (c) Only
- **(3)** (b), (c) Only
- (4) (d), (e) Only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When a flower can be divided into two similar halves only in one particular vertical plane, it is zygomorphic for e.g. pea, gulmohar, bean, $Cassia$.
2. Mustard, $Datura$ and Chilli show actinomorphic flowers.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Morphology of Flowering Plants) gives mustard, datura and chilli as examples of actinomorphic flowers, so (a), (d) and (e) are not zygomorphic.
2. The same text gives pea, gulmohur, bean and Cassia as examples of zygomorphic flowers, so (b) and (c) are zygomorphic.
3. Only (b) and (c) are zygomorphic, which is option $3$.

**Subtopic:** The Flower · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q115_a545c11e_04112026.png?v=a545c11e454c)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q115_0214f86e_04112026.png?v=0214f86e112b)

---

## Q116

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the **incorrect** statement related to Pollination :

- **(1)** Moths and butterflies are the most dominant pollinating agents among insects
- (2) Pollination by water is quite rare in flowering plants
- (3) Pollination by wind is more common amongst abiotic pollination
- (4) Flowers produce foul odours to attract flies and beetles to get pollinated

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Among the animals, insects, particularly bees are the dominant biotic pollinating agents.

**Solved independently** (answer withheld)

1. Statement 1: pollination by water is quite rare in flowering plants (about 30 genera, mostly monocots) $\Rightarrow$ correct.
2. Statement 2: among abiotic agents, wind pollination is more common than water pollination $\Rightarrow$ correct.
3. Statement 3: some flowers produce foul odours to attract flies and beetles for pollination $\Rightarrow$ correct.
4. Statement 4: among insects, bees are the dominant pollinating agents, not moths and butterflies $\Rightarrow$ incorrect, so the answer is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q116_dad4058d_04112026.png?v=dad4058d6363)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q116_06684c15_04112026.png?v=06684c152a4e)

---

## Q117

Biology · botany · Transport in Plants

Which of the following is **not** observed during apoplastic pathway ?

- (1) Apoplast is continuous and does not provide any barrier to water movement
- (2) Movement of water occurs through intercellular spaces and wall of the cells
- (3) The movement does not involve crossing of cell membrane
- **(4)** The movement is aided by cytoplasmic streaming

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The symplastic system is system of interconnected protoplasts.
2. Neighbouring cells are connected through cytoplasmic strands that extend through plasmodesmata.
3. The water travels through cell cytoplasm and plasmodesmata, hence the movement is relatively slower.
4. Symplastic movement is aided by cytoplasmic streaming.

**Solved independently** (answer withheld)

1. The apoplastic pathway moves water through cell walls and intercellular spaces without crossing any membrane, and the apoplast is continuous, so options $2$, $3$ and $1$ are observed; cytoplasmic streaming aids only the symplastic pathway, so option $4$ is not observed.

**Subtopic:** Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 45)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q117_b978f1e2_04112026.png?v=b978f1e2a3c4)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q117_50c3ed18_04112026.png?v=50c3ed184d06)

---

## Q118

Biology · botany · Respiration in Plants

What is the net gain of ATP when each molecule of glucose is converted to two molecules of pyruvic acid?

- (1) Eight
- (2) Four
- (3) Six
- **(4)** Two

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During glycolysis, total 4 ATPs are produced from one glucose molecule with a net gain of 2 ATPs.

**Solved independently** (answer withheld)

1. Glycolysis converts one glucose into two pyruvic acid molecules and uses $2$ ATP (hexokinase and phosphofructokinase steps).
2. It forms $4$ ATP by substrate-level phosphorylation ($2$ per triose).
3. Net gain $= 4 - 2 = 2$ ATP, which is option $4$ (Two).

**Subtopic:** Glycolysis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 46)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q118_3b335f6c_04112026.png?v=3b335f6cd459)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q118_b572fce6_04112026.png?v=b572fce6ff73)

---

## Q119

Biology · botany · Transport in Plants

“Girdling Experiment” was performed by Plant Physiologists to identify the plant tissue through which:

- (1) osmosis is observed
- (2) water is transported
- **(3)** food is transported
- (4) for both water and food transportation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The girdling experiment shows that phloem is the tissue responsible for translocation of food; and that transport takes place in one direction $i.e.$ towards the root.

**Solved independently** (answer withheld)

1. Girdling removes a ring of bark including phloem but leaves xylem intact; food accumulates above the ring and tissue below starves, showing phloem transports food (option $3$).

**Subtopic:** Phloem Transport: Flow from Source to Sink · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q119_562f322c_04112026.png?v=562f322caa28)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q119_6e75c2d5_04112026.png?v=6e75c2d5edb9)

---

## Q120

Biology · botany · Ecosystem

Given below are two statements:

In the light of the above statements, choose the **correct** answer from the options given below:

- (Statement I) Decomposition is a process in which the detritus is degraded into simpler substances by microbes.
- (Statement II) Decomposition is faster if the detritus is rich in lignin and chitin.

- (1) **Statement I** is incorrect but **Statement II** is correct
- (2) Both **Statement I** and **Statement II** are correct
- (3) Both **Statement I** and **Statement II** are incorrect
- **(4)** **Statement I** is correct but **Statement II** is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Decomposition is the process by which decomposers breakdown complex organic matter into inorganic substances.
2. The rate of decomposition is controlled by chemical composition of detritus and climatic factors.
3. Decomposition is slower if detritus is rich in lignin and chitin and quicker, if detritus is rich in nitrogen and water soluble substances like sugars.

**Solved independently** (answer withheld)

1. Statement I: decomposers (microbes) break down detritus into simpler inorganic substances, so Statement I is correct.
2. Statement II: decomposition is slower, not faster, when detritus is rich in lignin and chitin, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect, which is option $4$.

**Subtopic:** Decomposition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 46)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q120_10ff9e5c_04112026.png?v=10ff9e5c662c)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q120_c5eee635_04112026.png?v=c5eee6359dbd)

---

## Q121

Biology · botany · Morphology of Flowering Plants

Which one of the following plants shows vexillary aestivation and diadelphous stamens?

- (1) Solanum nigrum
- (2) Colchicum autumnale
- **(3)** Pisum sativum
- (4) Allium cepa

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Vexillary aestivation and diadelphous stamens are the characteristic features of family Fabaceae.
2. $Pisum$ $sativum$ (garden pea) belongs to family Fabaceae.
3. $Allium$ $cepa$ (onion) and $Colchicum$ $autumnale$ (colchicine) belong to family Liliaceae.
4. $Solanum$ $nigrum$ belongs to Solanaceae.

**Solved independently** (answer withheld)

1. Vexillary aestivation and diadelphous stamens $(9)+1$ are characteristic of Fabaceae; Pisum sativum belongs to Fabaceae, while Colchicum and Allium are Liliaceae and Solanum is Solanaceae, so the answer is option $3$.

**Subtopic:** Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q121_7347cccc_04112026.png?v=7347cccc13be)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q121_1c84ea48_04112026.png?v=1c84ea486d8d)

---

## Q122

Biology · botany · Sexual Reproduction in Flowering Plants

Given below are two statements :
Statement I :
Statement II :
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Cleistogamous flowers are invariably autogamous
- (Statement II) Cleistogamy is disadvantageous as there is no chance for cross pollination

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Cleistogamous flowers does not open at all. In such flowers autogamy occurs.
2. Lack of cross pollination is a disadvantage of cleistogamy.

**Solved independently** (answer withheld)

1. Cleistogamous flowers do not open at all, so pollination occurs within the closed flower itself, making them invariably autogamous — Statement I is correct.
2. Since the flower never opens, pollen from other plants cannot reach the stigma, so no cross-pollination is possible, which is a disadvantage as it reduces genetic variation — Statement II is correct.
3. Both statements are correct, matching option 2.

**Subtopic:** Pollination · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q122_b535acc4_04112026.png?v=b535acc48d7e)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q122_68c634af_04112026.png?v=68c634af7cd2)

---

## Q123

Biology · botany · Biomolecules

Exoskeleton of arthropods is composed of :

- (1) Glucosamine
- (2) Cutin
- (3) Cellulose
- **(4)** Chitin

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as chitin forms the exoskeleton in arthropods and is found in fungal cell wall. N-acetyl glucosamine is the monomeric unit. Cellulose is a polysaccharide. Cutin is a derived lipid.

**Solved independently** (answer withheld)

1. The arthropod body is covered by a chitinous exoskeleton, so the answer is chitin, option $4$.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q123_37a78378_04112026.png?v=37a78378716d)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q123_67fc4df4_04112026.png?v=67fc4df4fb8f)

---

## Q124

Biology · botany · Biotechnology: Principles and Processes

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R).
In the light of the above statements, choose the correct answer from the options given below :

- Assertion (A) Polymerase chain reaction is used in DNA amplification.
- Reason (R) The ampicillin resistant gene is used as a selectable marker to check transformation

- (1) (A) is not correct but (R) is correct
- (2) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- **(3)** Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- (4) (A) is correct but (R) is not correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because both the statements are correct but the given reason is not the correct explanation. Polymerase chain reaction is used in DNA amplification.
2. Ampicillin resistance gene is a selectable marker that helps to check transformation by selection of transformants.

**Solved independently** (answer withheld)

1. Polymerase chain reaction makes many copies of a target DNA segment, so (A) is correct.
2. The ampicillin resistance gene (e.g. $amp^R$ in pBR322) is used as a selectable marker to identify transformants, so (R) is correct.
3. Selection of transformants by antibiotic resistance has no bearing on how PCR amplifies DNA, so (R) is not the explanation of (A): option $3$.

**Subtopic:** Amplification of Gene of Interest Using PCR, ORI and Selectable Marker · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q124_fcc65b60_04112026.png?v=fcc65b604cf7)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q124_45173a4b_04112026.png?v=45173a4b622e)

---

## Q125

Biology · botany · Plant Kingdom

Which of the following is **incorrectly** matched?

- (1) *Volvox* – Starch
- (2) *Ectocarpus* – Fucoxanthin
- **(3)** *Ulothrix* – Mannitol
- (4) *Porphyra* – Floridian Starch

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. *Ulothrix* is a member of Chlorophyceae (green algae), with reserve food material, starch.
2. Mannitol is stored food material of Phaeophyceae (brown algae).

**Solved independently** (answer withheld)

1. $\text{Ectocarpus}$ is a brown alga (Phaeophyceae) whose characteristic pigment is fucoxanthin, so option $2$ is correctly matched.
2. $\text{Ulothrix}$ is a green alga (Chlorophyceae) whose reserve food is starch; mannitol is stored by brown algae, so option $3$ is incorrectly matched.
3. $\text{Porphyra}$ is a red alga (Rhodophyceae) storing floridean starch, so option $4$ is correctly matched.
4. $\text{Volvox}$ is a green alga storing starch, so option $1$ is correctly matched.
5. The only incorrect pair is option $3$.

**Subtopic:** Chlorophyceae, Phaeophyceae · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 47)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q125_b9b8afad_04112026.png?v=b9b8afada28f)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q125_6b5d0def_04112026.png?v=6b5d0defdaa8)

---

## Q126

Biology · botany · Plant Growth and Development

Production of Cucumber has increased manifold in recent years. Application of which of the following phytohormones has resulted in this increased yield as the hormone is known to produce female flowers in the plants :

- (1) Cytokinin
- (2) ABA
- (3) Gibberellin
- **(4)** Ethylene

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ethylene increases the number of female flowers and fruits in certain plants such as cucumber.
2. Gibberellins are used to increase the size of fruits in some plants.

**Solved independently** (answer withheld)

1. Ethylene is the phytohormone that promotes female flowers in cucumbers and so increases yield, which is option $4$.

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q126_441076ec_04112026.png?v=441076eca86c)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q126_2d397f82_04112026.png?v=2d397f82d2ed)

---

## Q127

Biology · botany · Photosynthesis in Higher Plants

Which one of the following is **not** true regarding the release of energy during ATP synthesis through chemiosmosis? It involves:

- (1) Reduction of NADP to $\mathrm{NADPH_2}$ on the stroma side of the membrane
- (2) Breakdown of proton gradient
- **(3)** Breakdown of electron gradient
- (4) Movement of protons across the membrane to the stroma

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient and ATP synthase. Energy is used to pump protons across a membrane to create a gradient or a high concentration of protons within the thylakoid lumen.
2. The NADP reductase enzyme is located on the stroma side of the membrane. Along with the electrons that come from the acceptor of electrons of PS I, protons are necessary for reduction of $\mathrm{NADP^{+}}$ to $\mathrm{NADPH + H^{+}}$.
3. The process does not involve breaking of electron gradient.

**Solved independently** (answer withheld)

1. In chemiosmosis, a proton gradient forms across the thylakoid membrane; its breakdown, as protons move through CF$_0$ of ATP synthase to the stroma, releases energy for ATP synthesis, so options $2$ and $4$ are true; NADP reductase on the stroma side reduces NADP to NADPH, so option $1$ is true; no electron gradient exists, so option $3$ is not true.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q127_484f94ce_04112026.png?v=484f94cefb37)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q127_5060e1fe_04112026.png?v=5060e1fe8fce)

---

## Q128

Biology · botany · Molecular Basis of Inheritance

DNA polymorphism forms the basis of :

- (1) Translation
- (2) Genetic mapping
- (3) DNA finger printing
- **(4)** Both genetic mapping and DNA finger printing

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Polymorphism in DNA sequence is the basis of genetic mapping of human genome as well as of DNA fingerprinting.

**Solved independently** (answer withheld)

1. DNA polymorphism (inheritable variation in DNA sequence, such as VNTRs/satellite DNA) forms the basis of genetic mapping of the human genome as well as of DNA fingerprinting, so option $4$.

**Subtopic:** DNA Fingerprinting · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q128_576f9745_04112026.png?v=576f9745a2e1)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q128_4fea2ae3_04112026.png?v=4fea2ae3eaf7)

---

## Q129

Biology · botany · Photosynthesis in Higher Plants

Given below are two statements :
In the light of the above statements, choose the **correct** answer from the options given below:

- (Statement I) The primary $\mathrm{CO_2}$ acceptor in $\mathrm{C_4}$ plants is phosphoenolpyruvate and is found in the mesophyll cells.
- (Statement II) Mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCo enzyme.

- (1) **Statement I** is incorrect but **Statement II** is correct
- **(2)** Both **Statement I** and **Statement II** are correct
- (3) Both **Statement I** and **Statement II** are incorrect
- (4) **Statement I** is correct but **Statement II** is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The primary $\mathrm{CO_2}$ acceptor is a 3-carbon molecule, phosphoenol pyruvate (PEP) and is present in the mesophyll cells.
2. Mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCO enzyme.

**Solved independently** (answer withheld)

1. Statement I: in $\mathrm{C_4}$ plants the primary $\mathrm{CO_2}$ acceptor is phosphoenolpyruvate (PEP), a 3-carbon molecule found in the mesophyll cells, so it is correct.
2. Statement II: the mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCO, which is present in the bundle sheath cells, so it is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** The C₄ Pathway · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q129_063f0430_04112026.png?v=063f0430daed)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q129_bbd87340_04112026.png?v=bbd87340fc5e)

---

## Q130

Biology · botany · Biodiversity and Conservation

Habitat loss and fragmentation, over exploitation, alien species invasion and co-extinction are causes for:

- (1) Natality
- (2) Population explosion
- (3) Competition
- **(4)** Biodiversity loss

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Habitat loss and fragmentation, over exploitation, alien species invasion and co-extinction are causes for biodiversity loss.

**Solved independently** (answer withheld)

1. Habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions are the 'Evil Quartet', the four major causes of biodiversity loss, which is option $4$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q130_dcdcf17c_04112026.png?v=dcdcf17c3c13)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q130_b06851c8_04112026.png?v=b06851c80295)

---

## Q131

Biology · botany · Respiration in Plants

What amount of energy is released from glucose during lactic acid fermentation?

- **(1)** Less than $7\%$
- (2) Approximately $15\%$
- (3) More than $18\%$
- (4) About $10\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Less than seven percent of the energy in glucose is released during lactic acid fermentation and not all of it is trapped as high energy bonds of ATP.

**Solved independently** (answer withheld)

1. In fermentation glucose is only partly oxidised, so less than $7\%$ of its energy is released, which is option $1$.

**Subtopic:** Fermentation and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q131_d8446f7d_04112026.png?v=d8446f7d7e9a)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q131_3f224081_04112026.png?v=3f224081c5fc)

---

## Q132

Biology · botany · Molecular Basis of Inheritance

Read the following statements and choose the set of **correct** statements :

- (a) Euchromatin is loosely packed chromatin
- (b) Heterochromatin is transcriptionally active
- (c) Histone octomer is wrapped by negatively charged DNA in nucleosome
- (d) Histones are rich in lysine and arginine
- (e) A typical nucleosome contains $400$ bp of DNA helix

- (1) (a), (c), (e) Only
- (2) (b), (d), (e) Only
- **(3)** (a), (c), (d) Only
- (4) (b), (e) Only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Heterochromatin is transcriptionally inactive. A typical nucleosome contains $200$ bp of DNA helix.
2. Euchromatin is the loosely packed chromatin region.
3. The negatively charged DNA is wrapped around the positively charged histone octamer to form a structure called nucleosome. Histones are rich in basic amino acid residues lysine and arginine.

**Solved independently** (answer withheld)

1. (a) Euchromatin is loosely packed chromatin: true.
2. (b) Heterochromatin is densely packed and transcriptionally inactive: false.
3. (c) Negatively charged DNA wraps the positively charged histone octamer in a nucleosome: true.
4. (d) Histones are rich in the basic residues lysine and arginine: true.
5. (e) A typical nucleosome contains $200\,\mathrm{bp}$ of DNA, not $400\,\mathrm{bp}$: false.
6. True set is (a), (c), (d), which is option $3$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 49)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q132_22616eac_04112026.png?v=22616eaca927)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q132_82b1bd8f_04112026.png?v=82b1bd8f552c)

---

## Q133

Biology · botany · Cell Cycle and Cell Division

Which one of the following never occurs during mitotic cell division?

- (1) Coiling and condensation of the chromatids
- (2) Spindle fibres attach to kinetochores of chromosomes
- (3) Movement of centrioles towards opposite poles
- **(4)** Pairing of homologous chromosomes

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Pairing of homologous chromosomes occurs during prophase I of meiosis.
2. Coiling and condensation of chromatids, spindle fibres attachment to the kinetochores and movement of centrioles towards opposite poles occur in both mitosis and meiosis.

**Solved independently** (answer withheld)

1. Homologous chromosome pairing (synapsis) happens only in zygotene of meiosis I, so it never occurs in mitosis; options 2, 3 and 1 all occur in mitosis, so the answer is option $4$.

**Subtopic:** Prophase and Metaphase, Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q133_d0448a18_04112026.png?v=d0448a182008)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q133_92fc7030_04112026.png?v=92fc703029a3)

---

## Q134

Biology · botany · Plant Kingdom

Hydrocolloid carrageen is obtained from:

- (1) Phaeophyceae only
- (2) Chlorophyceae and Phaeophyceae
- (3) Phaeophyceae and Rhodophyceae
- **(4)** Rhodophyceae only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Hydrocolloids are water holding substances for eg. carrageen obtained from red algae (Rhodophyceae).

**Solved independently** (answer withheld)

1. NCERT Class 11 states that algin is obtained from brown algae (Phaeophyceae) and carrageen from red algae (Rhodophyceae), so carrageen comes from $\text{Rhodophyceae}$ only, which is option $4$.

**Subtopic:** Rhodophyceae · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q134_d9305132_04112026.png?v=d9305132c4d9)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q134_800e9577_04112026.png?v=800e95770156)

---

## Q135

Biology · botany · Plant Growth and Development

Which one of the following plants does **not** show plasticity?

- **(1)** Maize
- (2) Cotton
- (3) Coriander
- (4) Buttercup

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Plants follow different pathways in response to environment or phases of life to form different kinds of structures. This ability is called plasticity e.g. heterophylly in cotton, coriander and larkspur. In such plants, leaves of juvenile plant are different in a shape from those in mature plants.
2. Maize does not show plasticity.

**Solved independently** (answer withheld)

1. Plasticity (heterophylly) is shown by cotton, coriander, larkspur and buttercup per NCERT, while maize shows no heterophylly, so the answer is option $1$.

**Subtopic:** Development and Plasticity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q135_cef4dcb7_04112026.png?v=cef4dcb7da42)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q135_790bdaee_04112026.png?v=790bdaeed3ad)

---

## Q136

Biology · botany · Ecosystem

Which one of the following will accelerate phosphorus cycle?

- (1) Rain fall and storms
- (2) Burning of fossil fuels
- (3) Volcanic activity
- **(4)** Weathering of rocks

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Phosphorus cycle is a sedimentary cycle.
2. Reservoir pool of phosphorus in ecosystem is the earth's crust or lithosphere.
3. Weathering of rocks accelerate phosphorus cycle.

**Solved independently** (answer withheld)

1. The natural reservoir of phosphorus is rock containing phosphates; weathering of rocks releases these phosphates into soil solution for plant uptake, speeding up the phosphorus cycle, which is option $4$.

**Subtopic:** Nutrient Cycling · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q136_b521463b_04112026.png?v=b521463bb325)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q136_dc8f81eb_04112026.png?v=dc8f81eb57d2)

---

## Q137

Biology · botany · Sexual Reproduction in Flowering Plants

Which part of the fruit, labelled in the given figure makes it a false fruit?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q137_403e6b24_04112026.png?v=403e6b24e307)

- (1) D $\rightarrow$ Seed
- (2) A $\rightarrow$ Mesocarp
- (3) B $\rightarrow$ Endocarp
- **(4)** C $\rightarrow$ Thalamus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The given figure is of a false fruit. False fruit develops from other floral parts and thalamus alongwith the development of ovary wall.

**Solved independently** (answer withheld)

1. The figure is a transverse section of an apple (a pome), where the outer fleshy region C is the thalamus, which grows around the ovary; the thalamus taking part in fruit formation makes it a false fruit, so the answer is option $4$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 50)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q137_cb3caef6_04112026.png?v=cb3caef64535)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q137_45030cc1_04112026.png?v=45030cc1b3a1)

---

## Q138

Biology · botany · Photosynthesis in Higher Plants

What is the role of large bundle sheath cells found around the vascular bundles in $\mathrm{C_4}$ plants?

- (1) To protect the vascular tissue from high light intensity
- (2) To provide the site for photorespiratory pathway
- **(3)** To increase the number of chloroplast for the operation of Calvin cycle
- (4) To enable the plant to tolerate high temperature

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The large cells around the vascular bundles of $\mathrm{C_4}$ plants form bundle sheath.
2. These cells have large number of chloroplasts to perform calvin cycle.

**Solved independently** (answer withheld)

1. In $\mathrm{C_4}$ plants (Kranz anatomy), the large bundle sheath cells hold many chloroplasts and carry out the Calvin cycle, while photorespiration is suppressed, so option $3$ fits.

**Subtopic:** The C₄ Pathway · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 50)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q138_3ffc38f7_04112026.png?v=3ffc38f7a8df)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q138_cd7b78db_04112026.png?v=cd7b78db2204)

---

## Q139

Biology · botany · Biotechnology: Principles and Processes

In the following palindromic base sequences of DNA, which one can be cut easily by particular restriction enzyme?

- (1) $5'$GTATTC$3'$; $3'$CATAAG$5'$
- (2) $5'$GATACT$3'$; $3'$CTATGA$5'$
- **(3)** $5'$GAATTC$3'$; $3'$CTTAAG$5'$
- (4) $5'$CTCAGT$3'$; $3'$GAGTCA$5'$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as a palindromic DNA sequence is a DNA sequence of base pairs that reads same on the two strands when orientation of reading is kept the same. Out of the four options, option (3) is the only palindromic sequence.
2. $5'$GAATTC$3'$
3. $3'$CTTAAG$5'$

**Solved independently** (answer withheld)

1. A restriction enzyme recognises a palindromic sequence, one that reads the same on both strands in the $5' \to 3'$ direction.
2. Option 3: top $5'\mathrm{GAATTC}3'$; bottom read $5' \to 3'$ is $\mathrm{GAATTC}$, so it is palindromic and is the EcoRI recognition site.
3. Options 2, 4, 1: bottom strands read $5' \to 3'$ are $\mathrm{AGTATC}$, $\mathrm{TGACTC}$, $\mathrm{GAATAC}$, which differ from the top strands, so they are not palindromes.
4. Hence the answer is option $3$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q139_c53252e4_04112026.png?v=c53252e41718)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q139_90988efa_04112026.png?v=90988efa0e32)

---

## Q140

Biology · botany · Biomolecules

Read the following statements on lipids and find out correct set of statements:

- (a) Lecithin found in the plasma membrane is a glycolipid
- (b) Saturated fatty acids possess one or more $c = c$ bonds
- (c) Gingely oil has lower melting point, hence remains as oil in winter
- (d) Lipids are generally insoluble in water but soluble in some organic solvents
- (e) When fatty acid is esterified with glycerol, monoglycerides are formed

- (1) (a), (b) and (d) only
- (2) (a), (b) and (c) only
- (3) (a), (d) and (e) only
- **(4)** (c), (d) and (e) only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because statements (c), (d) and (e) are correct as oils have lower melting point and hence remain oil in winters. Lipids are generally insoluble in water but soluble in some organic solvents.
2. Option (1), (2) and (3) are incorrect because statements (a) and (b) are incorrect. Lecithin is a type of phospholipid found in plasma membrane. Saturated fatty acids are without double bond.

**Solved independently** (answer withheld)

1. Lecithin in plasma membrane is a phospholipid, not a glycolipid, so statement (a) is false.
2. Saturated fatty acids by definition have no C=C double bonds, so statement (b) is false.
3. Gingely (sesame) oil, being unsaturated, has a low melting point and stays liquid even in winter, so statement (c) is true.
4. Lipids are hydrophobic, insoluble in water, but dissolve in organic solvents like ether/chloroform, so statement (d) is true.
5. Esterification of one fatty acid molecule with glycerol yields a monoglyceride, so statement (e) is true.
6. Thus the correct set is (c), (d) and (e), matching option 4.

**Subtopic:** Lipids · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 51)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q140_dcc15d66_04112026.png?v=dcc15d669a31)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q140_5582852e_04112026.png?v=5582852ec7b6)

---

## Q141

Biology · botany · Principles of Inheritance and Variation

Given below are two statements : one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**. In the light of the above statements, choose the **correct** answer from the options given below:

- Assertion (A) Mendel’s law of Independent assortment does not hold good for the genes that are located closely on the same chromosome.
- Reason (R) Closely located genes assort independently.

- (1) (A) is not correct but (R) is correct
- (2) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- (3) Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- **(4)** (A) is correct but (R) is not correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Closely located genes do not show independent assortment.
2. Mendel's law of independent assortment holds good for those genes which are located on different chromosomes.

**Solved independently** (answer withheld)

1. Genes located close together on the same chromosome are linked and are usually inherited together, so Mendel's law of independent assortment does not apply to them: (A) is correct.
2. (R) says closely located genes assort independently, which contradicts linkage, so (R) is not correct; this is option $4$.

**Subtopic:** Linkage & Recombination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q141_27919da3_04112026.png?v=27919da3462f)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q141_c3ca3abb_04112026.png?v=c3ca3abb202c)

---

## Q142

Biology · botany · Environmental Issues

The entire fleet of buses in Delhi were converted to CNG from diesel. In reference to this, which one of the following statements is false?

- (1) It cannot be adulterated like diesel
- (2) CNG burns more efficiently than diesel
- **(3)** The same diesel engine is used in CNG buses making the cost of conversion low
- (4) It is cheaper than diesel

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. CNG is cheaper then petrol and it burns more efficiently unlike petrol or diesel.
2. It also cannot be adulterated like diesel and petrol.
3. The same diesel engine cannot be used in CNG buses for making the cost conversion low.

**Solved independently** (answer withheld)

1. NCERT lists CNG advantages: it burns most efficiently, is cheaper than petrol or diesel, and cannot be siphoned off or adulterated, so options $2$, $4$ and $1$ are true; the statement that the same diesel engine is used with low conversion cost is not an NCERT advantage and is false, so the answer is option $3$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q142_2d64a2c0_04112026.png?v=2d64a2c059c2)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q142_aa8b18ea_04112026.png?v=aa8b18ea23c6)

---

## Q143

Biology · botany · Plant Kingdom

Match the plant with the kind of life cycle it exhibits:

Choose the **correct answer** from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Spirogyra | (i) | Dominant diploid sporophyte vascular plant, with highly reduced male or female gametophyte |
| (b) | Fern | (ii) | Dominant haploid free-living gametophyte |
| (c) | Funaria | (iii) | Dominant diploid sporophyte alternating with reduced gametophyte called prothallus |
| (d) | Cycas | (iv) | Dominant haploid leafy gametophyte alternating with partially dependent multicellular sporophyte |

- (1) (a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)
- (2) (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)
- **(3)** (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)
- (4) (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. *Spirogyra* is an alga. It shows haplontic life-cycle.
2. Fern is pteridophyte. The dominant phase of life-cycle is diploid sporophyte. Its gametophyte is called prothallus.
3. *Funaria* is a bryophyte. Its gametophyte is a leafy stage.
4. *Cycas* is a gymnosperm. The main plant body in gymnosperm is sporophyte. They have highly reduced gametophyte stage.

**Solved independently** (answer withheld)

1. Spirogyra (alga) is haplontic: dominant haploid free-living gametophyte, so $(a)-(ii)$.
2. Fern (pteridophyte): dominant diploid sporophyte alternating with a reduced gametophyte called prothallus, so $(b)-(iii)$.
3. Funaria (moss): dominant haploid leafy gametophyte with a partially dependent multicellular sporophyte, so $(c)-(iv)$.
4. Cycas (gymnosperm): dominant diploid vascular sporophyte with highly reduced male or female gametophyte, so $(d)-(i)$.
5. The match $(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)$ is option $3$.

**Subtopic:** Plant Life Cycles and Alternation of Generations · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 52)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q143_a17dc966_04112026.png?v=a17dc966228b)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q143_80294b68_04112026.png?v=80294b6869a0)

---

## Q144

Biology · botany · Cell: The Unit of Life

Match List-I with List-II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Metacentric chromosome | (i) | Centromere situated close to the end forming one extremely short and one very long arms |
| (b) | Acrocentric chromosome | (ii) | Centromere at the terminal end |
| (c) | Submetacentric | (iii) | Centromere in the middle forming two equal arms of chromosomes |
| (d) | Telocentric chromosome | (iv) | Centromere slightly away from the middle forming one shorter arm and one longer arm |

- (1) (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)
- **(2)** (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)
- (3) (a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)
- (4) (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In metacentric chromosome, centromere is in the middle of the chromosomes.
2. Acrocentric chromosome has centromere close to the end of the chromosome.
3. In submetacentric chromosome, centromere is slightly away from the middle of the chromosome.
4. Telocentric chromosome has terminal centromere.

**Solved independently** (answer withheld)

1. Metacentric chromosome: centromere in the middle forming two equal arms, so $(a) \to (iii)$.
2. Acrocentric chromosome: centromere close to the end giving one extremely short and one very long arm, so $(b) \to (i)$.
3. Submetacentric: centromere slightly away from the middle giving one shorter and one longer arm, so $(c) \to (iv)$.
4. Telocentric chromosome: centromere at the terminal end, so $(d) \to (ii)$.
5. The set $(a)\text{-}(iii), (b)\text{-}(i), (c)\text{-}(iv), (d)\text{-}(ii)$ is option $2$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q144_762cd8b2_04112026.png?v=762cd8b2e101)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q144_1d131964_04112026.png?v=1d131964c3ad)

---

## Q145

Biology · botany · Biotechnology and Its Applications

Transposons can be used during which one of the following ?

- (1) Gene sequencing
- (2) Polymerase Chain Reaction
- **(3)** Gene Silencing
- (4) Autoradiography

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as the source of the complementary RNA for RNAi could be mobile genetic elements (transposons) that replicate via an RNA intermediate.
2. Option (4) is incorrect as autoradiography usally follows hybridisation.
3. Option (2) is incorrect because polymerase chain reaction is used to make copies of the DNA sample and does not need transposons.
4. Option (1) is incorrect because transposons are not required during gene sequencing.

**Solved independently** (answer withheld)

1. RNAi (gene silencing) uses complementary dsRNA from viruses with RNA genomes or from transposons replicating via an RNA intermediate, so the answer is option $3$, Gene Silencing.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 53)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q145_13f65af0_04112026.png?v=13f65af06469)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q145_ef9dc9ef_04112026.png?v=ef9dc9ef92b4)

---

## Q146

Biology · botany · Principles of Inheritance and Variation

Which of the following occurs due to the presence of autosome linked dominant trait ?

- (1) Thalessemia
- (2) Sickle cell anaemia
- **(3)** Myotonic dystrophy
- (4) Haemophilia

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Haemophilia is a X-linked recessive disorder. Thalassemia is an autosomal recessive disorder. Sickle cell anaemia is an autosomal recessive disorder.
2. Myotonic dystrophy is an autosomal dominant disorder $i.e.$ it occurs due to the presence of autosomal linked dominant trait.

**Solved independently** (answer withheld)

1. Sickle cell anaemia and thalassemia are autosomal recessive, haemophilia is X-linked recessive, and myotonic dystrophy is autosomal dominant, so the answer is option $3$.

**Subtopic:** Mendelian Disorders · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 53)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q146_ba18458c_04112026.png?v=ba18458c8db8)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q146_792e3e07_04112026.png?v=792e3e07094b)

---

## Q147

Biology · botany · Organisms and Populations

While explaining interspecific interaction of population, (+) sign is assigned for beneficial interaction, (–) sign is assigned for detrimental interaction and (0) for neutral interaction. Which of the following interactions can be assigned (+) for one specifies and (–) for another specifies involved in the interaction ?

- (1) Competition
- **(2)** Predation
- (3) Amensalim
- (4) Commensalism

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In predation, one species is benefitted where as the other is harmed. It is $(+\;-)$ type of population interaction.

**Solved independently** (answer withheld)

1. Predation is $(+,-)$, amensalism $(-,0)$, commensalism $(+,0)$ and competition $(-,-)$, so the $(+,-)$ interaction is predation, option $2$.

**Subtopic:** Predation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q147_9b7981f6_04112026.png?v=9b7981f63610)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q147_0ded1d32_04112026.png?v=0ded1d328527)

---

## Q148

Biology · botany · Transport in Plants

Addition of more solutes in a given solution will :

- (1) not affect the water potential at all
- (2) raise its water potential
- **(3)** lower its water potential
- (4) make its water potential zero

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. If some solute is dissolved in pure water, the solution has lower free water and the concentration of water decreases, reducing it's water potential. The magnitude of this lowering due to dissolution of a solute is called solute potential.

**Solved independently** (answer withheld)

1. Water potential is $\Psi_w = \Psi_s + \Psi_p$; adding more solute makes $\Psi_s$ more negative, so $\Psi_w$ is lowered, which is option $3$.

**Subtopic:** Water Potential · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q148_8747c59a_04112026.png?v=8747c59aa974)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q148_da08aad8_04112026.png?v=da08aad8b4a5)

---

## Q149

Biology · botany · Molecular Basis of Inheritance

If a geneticist uses the blind approach for sequencing the whole genome of an organism, followed by assignment of function to different segments, the methodology adopted by him is called as :

- (1) Bioinformatics
- **(2)** Sequence annotation
- (3) Gene mapping
- (4) Expressed sequence tags

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sequencing the whole set of genome that contained all the coding and non-coding sequences and later assigning different regions in the sequence with fuctions is called sequence annotation.

**Solved independently** (answer withheld)

1. NCERT (HGP) describes two approaches: identifying expressed genes as RNA (Expressed Sequence Tags), and the blind approach of sequencing the whole genome and later assigning functions to different regions, termed Sequence Annotation, so option $2$.

**Subtopic:** Human Genome Project · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 54)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q149_7e0d0e0a_04112026.png?v=7e0d0e0ab7fa)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q149_20ab8e72_04112026.png?v=20ab8e7280af)

---

## Q150

Biology · botany · Anatomy of Flowering Plants

The anatomy of springwood shows some peculiar features. Identify the **correct** set of statements about springwood.

Choose the correct answer from the options given below :

- (a) It is also called as the earlywood
- (b) In spring season cambium produces xylem elements with narrow vessels
- (c) It is lighter in colour
- (d) The springwood along with autumnwood shows alternate concentric rings forming annual rings
- (e) It has lower density

- (1) (c), (d) and (e) Only
- (2) (a), (b), (d) and (e) Only
- **(3)** (a), (c), (d) and (e) Only
- (4) (a), (b) and (d) Only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Spring wood is also called early wood. It is lighter in colour and has a lower density. The vessels are produced with the wider lumens to transport more water to meet the requirement by increased transpiring surface in spring season.
2. The spring and autumn wood appear as alternate concentric rings of light and dark colour forming annual rings.

**Solved independently** (answer withheld)

1. (a) Springwood is also called earlywood: true.
2. (b) In spring the cambium is very active and forms xylem with wider vessels, not narrow: false.
3. (c) Springwood is lighter in colour: true.
4. (d) Springwood and autumnwood appear as alternate concentric rings forming annual rings: true.
5. (e) Springwood has lower density: true.
6. True set is $(a), (c), (d), (e)$, which is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 54)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q150_c475d017_04112026.png?v=c475d017a93e)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q150_d04f8ff9_04112026.png?v=d04f8ff97696)

---

## Q151

Biology · zoology · Digestion and Absorption

Which of the following functions is **not** performed by secretions from salivary glands?

- **(1)** Digestion of disaccharides
- (2) Control bacterial population in mouth
- (3) Digestion of complex carbohydrates
- (4) Lubrication of oral cavity

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because digestion of polysaccharides like starch occurs in mouth and digestion of disaccharides occurs in small intestine.
2. Option (4) is incorrect because saliva contains mucus which helps in the lubrication of oral cavity.
3. Option (2) is incorrect because saliva contains an antibacterial agent-lysozyme so that it controls bacterial population in mouth.
4. Option (3) is incorrect because digestion of complex carbohydrates are performed by secretions from salivary glands.

**Solved independently** (answer withheld)

1. Saliva contains lysozyme, which acts as an antibacterial agent and controls the bacterial population in the mouth, so option $2$ is performed.
2. Salivary amylase hydrolyses starch, a complex carbohydrate (polysaccharide), so option $3$ is performed.
3. Mucus in saliva lubricates the oral cavity and helps form the bolus, so option $4$ is performed.
4. Salivary amylase converts starch into the disaccharide maltose but does not break disaccharides down further; that happens in the intestine (maltase, sucrase, lactase), so option $1$ is not performed.

**Subtopic:** Digestion of Food · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q151_b83444ad_04112026.png?v=b83444ad13aa)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q151_67609a10_04112026.png?v=67609a10262f)

---

## Q152

Biology · zoology · Organisms and Populations

If '8' \textit{Drosophila} in a laboratory population of '80' died during a week, the death rate in the population is ______ individuals per \textit{Drosophila} per week.

- (1) zero
- **(2)** $0.1$
- (3) $10$
- (4) $1.0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. If $8$ \textit{Drosophila} in a laboratory population of $80$ died during a week, the death rate in the population is $\frac{8}{80} = 0.1$ individuals per \textit{Drosophila} per week.

**Solved independently** (answer withheld)

1. Death rate is defined as number of deaths per individual per unit time: $D = \frac{\text{number died}}{\text{initial population}}$.
2. $D = \frac{8}{80} = 0.1$ individuals per Drosophila per week.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q152_daa51d70_04112026.png?v=daa51d70fc07)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q152_3d1fb9c9_04112026.png?v=3d1fb9c95841)

---

## Q153

Biology · zoology · Human Reproduction

Given below are two statements:
Statement I :
Statement II :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (I) The release of sperms into the seminiferous tubules is called spermiation.
- (II) Spermiogenesis is the process of formation of sperms from spermatogonia.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because Statement II is incorrect as the transformation of spermatids into spermatozoa (sperms) are called spermiogenesis. After this, sperm head becomes embedded in the Sertoli cells and are finally released from the seminiferous tubules by the process called spermiation.  Hence, Statement I is a correct statement.
2. Spermatogenesis is the process of formation of sperms from spermatogonia.

**Solved independently** (answer withheld)

1. Statement I: Spermiation = release of mature spermatozoa from Sertoli cells into the lumen of seminiferous tubules — this is correct as per NCERT.
2. Statement II: Spermiogenesis is the transformation of spermatids into spermatozoa, not formation of sperms directly from spermatogonia — so this statement is incorrect.
3. Hence Statement I is correct but Statement II is incorrect, matching option 4.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 55)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q153_3d1abebb_04112026.png?v=3d1abebb29ab)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q153_f50ec469_04112026.png?v=f50ec469ac1d)

---

## Q154

Biology · zoology · Biodiversity and Conservation

*In-situ* conservation refers to:

- (1) Conserve only extinct species
- **(2)** Protect and conserve the whole ecosystem
- (3) Conserve only high-risk species
- (4) Conserve only endangered species

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When we conserve and protect the whole ecosystem, its biodiversity at all levels is protected.
2. This is $in\text{-}situ$ or on site conservation strategy.

**Solved independently** (answer withheld)

1. In-situ (on site) conservation protects organisms in their natural habitat by protecting and conserving the whole ecosystem, as in biosphere reserves, national parks and sanctuaries, which is option $2$.

**Subtopic:** In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q154_102ca2eb_04112026.png?v=102ca2ebd1de)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q154_f006bdb0_04112026.png?v=f006bdb05222)

---

## Q155

Biology · zoology · Cell Cycle and Cell Division

Select the **incorrect** statement with reference to mitosis:

- (1) Splitting of centromere occurs at anaphase
- (2) All the chromosomes lie at the equator at metaphase
- **(3)** Spindle fibres attach to centromere of chromosomes
- (4) Chromosomes decondense at telophase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Spindle fibres attach to the kinetochores of chromosomes.
2. Kinetochores are the disc shaped structures present on sides of primary constriction or centromere of chromosomes.

**Solved independently** (answer withheld)

1. Options 2, 4 and 1 match NCERT: chromosomes align at the equator in metaphase, the centromere splits at anaphase, and chromosomes decondense at telophase.
2. NCERT says spindle fibres attach to the kinetochores, small disc-shaped structures at the surface of the centromere, so option $3$ is the incorrect statement.

**Subtopic:** Prophase and Metaphase · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 56)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q155_ab2641d4_04112026.png?v=ab2641d4c7f7)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q155_9b7493d5_04112026.png?v=9b7493d57aff)

---

## Q156

Biology · zoology · Molecular Basis of Inheritance

If the length of a DNA molecule is $1.1$ metres, what will be the approximate number of base pairs?

- (1) $6.6 \times 10^{6}$ bp
- **(2)** $3.3 \times 10^{9}$ bp
- (3) $6.6 \times 10^{9}$ bp
- (4) $3.3 \times 10^{6}$ bp

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Number of base pairs $\times$ distance between $2$ consecutive base pairs = Length of DNA molecule
2. $x \cdot 0.34 \times 10^{-9}\,\mathrm{m} = 1.1\,\mathrm{m}$
3. $x = \frac{1.1}{0.3 \times 10^{-9}}$
4. $= 3.6 \times 10^{9}$
5. $\simeq 3.3 \times 10^{9}$ bp

**Solved independently** (answer withheld)

1. Length per base pair in B-DNA = $0.34\,nm = 0.34\times10^{-9}\,m$.
2. Number of base pairs = $\frac{1.1\,m}{0.34\times10^{-9}\,m} \approx 3.23\times10^{9}$.
3. This rounds to $3.3\times10^{9}$ bp, matching option 2.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q156_52747e47_04112026.png?v=52747e474463)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q156_928f9b66_04112026.png?v=928f9b6648c9)

---

## Q157

Biology · zoology · Body Fluids and Circulation

Given below are two statements :
Statement I :
Statement II :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The coagulum is formed of network of threads called thrombins.
- (Statement II) Spleen is the graveyard of erythrocytes.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because coagulum or clot is formed mainly of a network of threads called fibrins. Hence, Statement I is incorrect.
2. RBCs are destroyed in the spleen so spleen is known as the graveyard of erythrocytes. Hence, Statement II is correct.

**Solved independently** (answer withheld)

1. Statement I: the clot network threads are called fibrin, not thrombin, so Statement I is incorrect.
2. Statement II: spleen destroys old/worn-out erythrocytes, hence termed the graveyard of RBCs, so Statement II is correct.
3. Thus Statement I is incorrect but Statement II is correct, matching option 1.

**Subtopic:** Coagulation of Blood, Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 56)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q157_4dcb3903_04112026.png?v=4dcb39032afd)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q157_40795252_04112026.png?v=407952529afe)

---

## Q158

Biology · zoology · Structural Organisation in Animals

Tegmina in cockroach, arises from

- (1) Prothorax and Mesothorax
- (2) Prothorax
- **(3)** Mesothorax
- (4) Metathorax

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because tegmina or forewings (the first pair of wings) in cockroach arises from mesothorax.
2. Options (1), (2) and (4) are incorrect because no wing arises from prothorax and hindwings arise from metathorax.

**Solved independently** (answer withheld)

1. Tegmina (the opaque, leathery forewings of cockroach) arise from the mesothorax, while the hindwings arise from the metathorax, so the answer is option $3$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 57)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q158_70905386_04112026.png?v=70905386cfe8)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q158_1191fa87_04112026.png?v=1191fa87f4d9)

---

## Q159

Biology · zoology · Biotechnology and Its Applications

In gene therapy of Adenosine Deaminase (ADA) deficiency, the patient requires periodic infusion of genetically engineered lymphocytes because :

- **(1)** Genetically engineered lymphocytes are not immortal cells.
- (2) Retroviral vector is introduced into these lymphocytes.
- (3) Gene isolated from marrow cells producing ADA is introduced into cells at embryonic stages
- (4) Lymphocytes from patient's blood are grown in culture, outside the body.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer as genetically engineered lymphocyctes are not immortal cells and die after some time.
2. Option (4) is not the correct answer as the lymphocytes from patient's blood are grown in culture, outside the body but it is not the correct reason.
3. In option (3), if the gene isolated from bone marrow cells producing ADA is introduced into cells at early embryonic stages, it could be a permanent cure.

**Solved independently** (answer withheld)

1. Engineered lymphocytes have a limited life span (they are not immortal), so the patient needs periodic infusions of them, which is option $1$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 57)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q159_a89b42b8_04112026.png?v=a89b42b80a9b)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q159_fe493056_04112026.png?v=fe493056909c)

---

## Q160

Biology · zoology · Human Health and Disease

Given below are two statements:
Statement I:
Statement II:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Autoimmune disorder is a condition where body defense mechanism recognizes its own cells as foreign bodies.
- (Statement II) Rheumatoid arthritis is a condition where body does not attack self cells.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as autoimmune disorder is a condition where body defense mechanism recognises its own cells as foreign bodies. Sometimes, due to genetic and other unknown reasons, the body attacks self- cells.
2. Rheumatoid arthritis is an example where body attacks self cells (synovial membrane).
3. So Statement I is correct but Statement II is incorrect.

**Solved independently** (answer withheld)

1. Statement I correctly defines autoimmune disorder as immune attack on self cells.
2. Rheumatoid arthritis is a classic autoimmune disease, meaning the body does attack self cells, making Statement II false.
3. Hence Statement I is correct, Statement II is incorrect.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 57)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q160_171434f2_04112026.png?v=171434f26bab)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q160_f0758f26_04112026.png?v=f0758f26aa70)

---

## Q161

Biology · zoology · Human Reproduction

At which stage of life the oogenesis process is initiated?

- (1) Adult
- (2) Puberty
- **(3)** Embryonic development stage
- (4) Birth

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as oogenesis is initiated during the embryonic development stage when a couple of million gamete mother cells (oogonia) are formed within each foetal ovary.
2. No more oogonia are formed and added after birth in a human female.
3. At puberty only $60,000$ to $80,000$ primary follicles are left in each ovary, rest degenerate during the phase from birth to puberty.

**Solved independently** (answer withheld)

1. Oogenesis starts in the embryonic stage: oogonia form in the foetal ovary and begin meiosis I, arresting as primary oocytes, so the answer is option $3$.

**Subtopic:** Female Gametogenesis (Oogenesis) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 58)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q161_cfefd8bd_04112026.png?v=cfefd8bde9bc)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q161_ed97cd9f_04112026.png?v=ed97cd9f65e6)

---

## Q162

Biology · zoology · Locomotion and Movement

Which of the following is a correct match for disease and its symptoms?

- (1) Muscular dystrophy – An auto immune disorder causing progressive degeneration of skeletal muscle
- **(2)** Arthritis – Inflammed joints
- (3) Tetany – High $\mathrm{Ca^{2+}}$ level causing rapid spasms.
- (4) Myasthenia gravis – Genetic disorder resulting in weakening and paralysis of skeletal muscle

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because Arthritis is inflammation of joints.
2. Option (4) is incorrect because myasthenia gravis is an immune disorder affecting neuro-muscular junction leading to fatigue, weakening and paralysis of skeletal muscle.
3. Option (1) is incorrect because muscular dystrophy is progressive degeneration of skeletal muscle mostly due to genetic disorder.
4. Option (3) is incorrect because tetany is rapid spasms in muscle due to low $\mathrm{Ca^{++}}$ in body fluid.

**Solved independently** (answer withheld)

1. Arthritis is inflammation of the joints, so option $2$ is a correct match.
2. Tetany is caused by low $\mathrm{Ca^{2+}}$ in body fluid, not high, so option $3$ is wrong.
3. Myasthenia gravis is an auto-immune disorder, not a genetic one, so option $4$ is wrong.
4. Muscular dystrophy is a genetic disorder, not auto-immune, so option $1$ is wrong; the answer is option $2$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 58)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q162_836ac1eb_04112026.png?v=836ac1eb3847)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q162_f058d25d_04112026.png?v=f058d25d194d)

---

## Q163

Biology · zoology · Structural Organisation in Animals

Which of the following is present between the adjacent bones of the vertebral column?

- (1) Smooth muscle
- (2) Intercalated discs
- **(3)** Cartilage
- (4) Areolar tissue

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because cartilage forming the intervertebral disc is present between the adjacent bones of the vertebral column and it is a type of cartilaginous joint.
2. Option (4) is incorrect because areolar tissue present beneath the skin is a type of loose connective tissue.
3. Option (1) is incorrect because smooth muscles are present in the visceral organs.
4. Option (2) is incorrect because intercalated discs are characteristic feature of cardiac muscles present in heart.

**Solved independently** (answer withheld)

1. Adjacent vertebrae are joined by intervertebral discs made of cartilage (fibrocartilage); intercalated discs belong to cardiac muscle, so the answer is option $3$.

**Subtopic:** Cartilage, Bone and Blood · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q163_2f8ac64c_04112026.png?v=2f8ac64caee9)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q163_71896197_04112026.png?v=71896197592c)

---

## Q164

Biology · zoology · The Living World

> ⚠ The printed solution says "None of the options are matching with the language of the question": the question has no correct option as printed, and the printed answer comes from a corrected reading.

> ⚠ The independent solve chose (unsure); the booklet prints (2).

In the taxonomic categories which hierarchical arrangement in ascending order is correct in case of animals?

- (1) Kingdom, Order, Phylum, Class, Family, Genus, Species
- **(2)** Kingdom, Phylum, Class, Order, Family, Genus, Species
- (3) Kingdom, Class, Phylum, Family, Order, Genus, Species
- (4) Kingdom, Order, Class, Phylum, Family, Genus, Species

**Answer** — booklet: (2) · independent solve: (unsure) · publisher_contradicts_itself

**Publisher's solution**

1. None of the options are matching with the language of the question
2. The correct ascending order of taxonomic categories in case of animals is
3. species $\rightarrow$ genus $\rightarrow$ family $\rightarrow$ order $\rightarrow$ class $\rightarrow$ phylum $\rightarrow$ kingdom

**Solved independently** (answer withheld)

1. The animal hierarchy from lowest to highest rank is Species, Genus, Family, Order, Class, Phylum, Kingdom.
2. Ascending order therefore begins with Species and ends with Kingdom.
3. All four options begin with Kingdom, so all are written in descending direction; none is ascending.
4. Option 2 is the correct sequence only if read as descending.

**Subtopic:** Taxonomic Categories · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q164_3e61f506_04112026.png?v=3e61f5063318)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q164_217aae12_04112026.png?v=217aae1275dd)

---

## Q165

Biology · zoology · Biomolecules

A dehydration reaction links two glucose molecules to product maltose. If the formula for glucose is $\mathrm{C_6H_{12}O_6}$ then what is the formula for maltose?

- (1) $\mathrm{C_{12}H_{24}O_{11}}$
- (2) $\mathrm{C_{12}H_{20}O_{10}}$
- (3) $\mathrm{C_{12}H_{24}O_{12}}$
- **(4)** $\mathrm{C_{12}H_{22}O_{11}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option $(4)$ is correct because maltose is a disaccharide formed by dehydration process $i.e.$, synthesis by elimination of one water molecule to form a glycosidic bond in between two glucose molecules. So, its molecular formula is.
2. $\mathrm{C_6H_{12}O_6} \times 2 \xrightarrow[\mathrm{H_2O}]{} \mathrm{C_{12}H_{22}O_{11}}$

**Solved independently** (answer withheld)

1. Two glucose molecules together contain $2 \times \mathrm{C_6H_{12}O_6} = \mathrm{C_{12}H_{24}O_{12}}$.
2. A dehydration (condensation) reaction forming one glycosidic bond removes one $\mathrm{H_2O}$.
3. $\mathrm{C_{12}H_{24}O_{12}} - \mathrm{H_2O} = \mathrm{C_{12}H_{22}O_{11}}$, which is option $4$.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q165_65561521_04112026.png?v=655615210644)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q165_cac39837_04112026.png?v=cac39837747d)

---

## Q166

Biology · zoology · Ecosystem

Detritivores breakdown detritus into smaller particles. This process is called:

- (1) Decomposition
- (2) Catabolism
- **(3)** Fragmentation
- (4) Humification

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Detritivores (eg. earthworm) break down detritus into smaller particles. This process is called fragmentation.

**Solved independently** (answer withheld)

1. Per NCERT, the breakdown of detritus into smaller particles by detritivores such as earthworm is called $\text{fragmentation}$, which is option $3$.

**Subtopic:** Decomposition · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 59)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q166_21c6cca0_04112026.png?v=21c6cca04e44)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q166_e4322d9d_04112026.png?v=e4322d9d24e7)

---

## Q167

Biology · zoology · Breathing and Exchange of Gases

Under normal physiological conditions in human being every $100\,\mathrm{ml}$ of oxygenated blood can deliver \_\_\_\_\_\_\_\_ $\mathrm{ml}$ of $\mathrm{O_2}$ to the tissues.

- (1) $10\,\mathrm{ml}$
- (2) $2\,\mathrm{ml}$
- **(3)** $5\,\mathrm{ml}$
- (4) $4\,\mathrm{ml}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because every $100\,\mathrm{mL}$ of oxygenated blood can deliver around $5\,\mathrm{mL}$ of $\mathrm{O_2}$ to the tissues under normal physiological conditions.
2. Option (1), (2) and (4) are incorrect because every $100\,\mathrm{mL}$ of deoxygenated blood delivers approximately $4\,\mathrm{mL}$ of $\mathrm{CO_2}$ to the alveoli.

**Solved independently** (answer withheld)

1. Under normal physiological conditions, every $100\,\mathrm{ml}$ of oxygenated blood delivers about $5\,\mathrm{ml}$ of $\mathrm{O_2}$ to the tissues, which is option $3$.

**Subtopic:** Transport of Gases · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 59)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q167_bf5f1ef9_04112026.png?v=bf5f1ef9e5a4)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q167_da0b3f9c_04112026.png?v=da0b3f9cfebc)

---

## Q168

Biology · zoology · Digestion and Absorption

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Fatty acids and glycerols cannot be absorbed into the blood.
- (Statement II) Specialized lymphatic capillaries called lacteals carry chylomicrons into lymphatic vessels and ultimately into the blood.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because both the statements I and II are correct as fatty acids and glycerol being insoluble in water, cannot be absorbed into the blood.
2. They are first incorporated into small droplets called micelles which move into the intestinal mucosa.
3. They are re-formed into very small protein coated fat globules called chylomicrons which are transported into the lymph vessels (lacteals) in the villi.
4. These lymph vessels ultimately release the absorbed substances into the blood stream.

**Solved independently** (answer withheld)

1. Statement I: fatty acids and glycerol are insoluble and cannot be absorbed directly into the blood, so Statement I is correct.
2. Statement II: they are incorporated into chylomicrons, which lacteals carry into lymphatic vessels and finally into the blood, so Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Absorption of Digested Products · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q168_da9b9f86_04112026.png?v=da9b9f864da9)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q168_093cd028_04112026.png?v=093cd0283ceb)

---

## Q169

Biology · zoology · Breathing and Exchange of Gases

Which of the following is not the function of conducting part of respiratory system?

- **(1)** Provides surface for diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$
- (2) It clears inhaled air from foreign particles
- (3) Inhaled air is humidified
- (4) Temperature of inhaled air is brought to body temperature

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is correct because the part starting with the external nostrils upto the terminal bronchioles constitute the conducting part; whereas the alveoli and their ducts form the respiratory or exchange part of the respiratory system.
2. The conducting part transports the atmospheric air to the alveoli, clears it from foreign particles, humidifies and also bring the air to body temperature. Exchange part is the site of actual diffusion of $\mathrm{O_2}/\mathrm{CO_2}$ between blood and atmospheric air.

**Solved independently** (answer withheld)

1. The conducting part (nose to terminal bronchioles) clears foreign particles from inhaled air, humidifies it and brings it to body temperature, while diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$ happens across the alveoli of the exchange part, so the answer is option $1$.

**Subtopic:** Human Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q169_5992354e_04112026.png?v=5992354e746d)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q169_d6ecac22_04112026.png?v=d6ecac22c0a2)

---

## Q170

Biology · zoology · Microbes in Human Welfare

Identify the microorganism which is responsible for the production of an immunosuppressive molecule cyclosporin A :

- (1) $\textit{Streptococcus cerevisiae}$
- **(2)** $\textit{Trichoderma polysporum}$
- (3) $\textit{Clostridium butylicum}$
- (4) $\textit{Aspergillus niger}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Bioactive molecule, cyclosporin A, that is used as an immunosuppressive agent in organ transplant patients, is produced by the fungus, $\textit{Trichoderma polysporum}$.

**Solved independently** (answer withheld)

1. Cyclosporin A is produced by the fungus $\textit{Trichoderma polysporum}$, as per NCERT Biotechnology/Microbes chapter.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q170_ea30ea79_04112026.png?v=ea30ea7901e9)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q170_76c486f6_04112026.png?v=76c486f65ee3)

---

## Q171

Biology · zoology · Cell Cycle and Cell Division

Regarding Meiosis, which of the statements is **incorrect**?

- (1) Four haploid cells are formed at the end of Meiosis-II
- (2) There are two stages in Meiosis, Meiosis-I and II
- **(3)** DNA replication occurs in S phase of Meiosis-II
- (4) Pairing of homologous chromosomes and recombination occurs in Meiosis-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Meiosis involves two sequential cycles of nuclear and cell division called meiosis-I and meiosis-II but only single cycle of DNA replication.
2. The stage between two meiotic divisions is called interkinesis and is generally short lived and involves no DNA replication.

**Solved independently** (answer withheld)

1. Meiosis has two divisions: Meiosis-I and Meiosis-II, consistent with option 2.
2. DNA replication occurs once, in the S phase preceding Meiosis-I, not before Meiosis-II, making option 3 incorrect.
3. Homologous pairing and recombination (crossing over) occur during Prophase-I, consistent with option 4.
4. At the end of Meiosis-II, four haploid cells are produced, consistent with option 1.
5. Thus the incorrect statement is option 3.

**Subtopic:** Meiosis and Meiosis I · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q171_df0380cb_04112026.png?v=df0380cb9ce2)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q171_367f6130_04112026.png?v=367f6130ac24)

---

## Q172

Biology · zoology · Human Reproduction

Which of the following statements are true for spermatogenesis but do not hold true for Oogenesis?

Choose the most appropriate answer from the options given below:

- (a) It results in the formation of haploid gametes
- (b) Differentiation of gamete occurs after the completion of meiosis
- (c) Meiosis occurs continuously in a mitotically dividing stem cell population
- (d) It is controlled by the Luteinising hormone (LH) and Follicle Stimulating Hormone (FSH) secreted by the anterior pituitary
- (e) It is initiated at puberty

- **(1)** (b), (c) and (e) only
- (2) (c) and (e) only
- (3) (b) and (c) only
- (4) (b), (d) and (e) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer.
2. In both, spermatogenesis and oogenesis haploid gametes are formed. So (a) is true for both.
3. The spermatids are transformed into spermatozoa (sperms) by the process called spermiogenesis. Hence, (b) is true for spermatogenesis only.
4. Spermatogenesis and oogenesis both are controlled by LH and FSH secreted by the anterior pituitary. Hence (d) is true for both.
5. Spermatogenesis is a continuous process that begins at puberty. So (e) is true for spermatogenesis. Oogenesis on the other hand begins during embryonic development of the female.

**Solved independently** (answer withheld)

1. (a) Both spermatogenesis and oogenesis form haploid gametes, so (a) is not exclusive to spermatogenesis.
2. (b) Spermatids differentiate into sperms (spermiogenesis) after meiosis is complete; in oogenesis meiosis II finishes only after sperm entry, so (b) applies to spermatogenesis only.
3. (c) Spermatogonia form a mitotically dividing stem-cell population that keeps entering meiosis; oogonia stop multiplying before birth, so (c) applies to spermatogenesis only.
4. (d) Both processes are regulated by pituitary LH and FSH, so (d) is not exclusive.
5. (e) Spermatogenesis begins at puberty, whereas oogenesis begins during foetal development, so (e) applies to spermatogenesis only.
6. Hence (b), (c) and (e) only, which is option $1$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Female Gametogenesis (Oogenesis) · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 61)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q172_ac2c6641_04112026.png?v=ac2c6641df65)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q172_a19961b7_04112026.png?v=a19961b7a0e4)

---

## Q173

Biology · zoology · Animal Kingdom

In which of the following animals, digestive tract has additional chambers like crop and gizzard?

- **(1)** *Pavo*, *Psittacula*, *Corvus*
- (2) *Corvus*, *Columba*, *Chameleon*
- (3) *Bufo*, *Balaenoptera*, *Bangarus*
- (4) *Catla*, *Columba*, *Crocodilus*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because two additional chambers like crop and gizzard in alimentary canal are present in birds.
2. *Pavo* (Peacock), *Psittacula* (Parrot), *Corvus* (Crow) and *Columba* (Pigeon) are birds.
3. Option (2), (3) and (4) are incorrect because *Catla* is a bony fish, *Crocodilus*, *Chameleon* and *Bangarus* are reptiles, *Bufo* is an amphibian and *Balaenoptera* is an aquatic mammal.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Animal Kingdom, Aves) states that the digestive tract of birds has additional chambers, the crop and the gizzard; Pavo, Psittacula and Corvus are all birds, while options 2, 3 and 4 each include a non-bird (Chameleon; Bufo, Balaenoptera, Bangarus; Catla, Crocodilus), so the answer is option $1$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 61)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q173_c53dc12e_04112026.png?v=c53dc12eaa57)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q173_4b8529df_04112026.png?v=4b8529df7575)

---

## Q174

Biology · zoology · Strategies for Enhancement in Food Production

Breeding crops with higher levels of vitamins and minerals or higher proteins and healthier fats is called :

- (1) Bio-accumulation
- (2) Bio-magnification
- (3) Bio-remediation
- **(4)** Bio-fortification

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Breeding crops with higher levels of vitamins and minerals, or higher protein and healthier fats is known as Biofortification.
2. Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.
3. Bioremediation is the phenomenon of using biological organism to handle pollution.

**Solved independently** (answer withheld)

1. Breeding crops with higher levels of vitamins, minerals, proteins and healthier fats to improve nutritional quality is termed $\text{biofortification}$, which is option $4$.

**Subtopic:** Biofortification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q174_158b9193_04112026.png?v=158b91932bd8)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q174_c8226759_04112026.png?v=c82267599237)

---

## Q175

Biology · zoology · Reproduction in Organisms

Identify the asexual reproductive structure associated with $\textit{Penicillium}$ :

- (1) Buds
- (2) Zoospores
- **(3)** Conidia
- (4) Gemmules

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Conidia are the asexual reproductive structures produced in $\textit{Penicillium}$.
2. Gemmules are produced in sponge
3. Buds are produced in $\textit{Hydra}$
4. Zoospores are produced in $\textit{Chlamydomonas}$

**Solved independently** (answer withheld)

1. Penicillium (an ascomycete fungus) reproduces asexually by conidia borne on conidiophores, which is option $3$.

**Subtopic:** Asexual Reproduction and Vegetative Propagation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q175_a56a43b1_04112026.png?v=a56a43b196bd)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q175_e7404ca0_04112026.png?v=e7404ca0282f)

---

## Q176

Biology · zoology · Biotechnology: Principles and Processes

Given below are two statements:
In the light of the above statements, choose the **most appropriate** answer from the options given below:

- (Statement I) Restriction endonucleases recognise specific sequence to cut DNA known as palindromic nucleotide sequence.
- (Statement II) Restriction endonucleases cut the DNA strand a little away from the centre of the palindromic site.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because both the statements I and II are correct.
2. Each restriction endonuclease recognises a specific palindromic nucleotide sequences in the DNA. It will bind to the DNA and cut each of the two strands of double helix at specific points.
3. Restriction enzymes cut the strand of DNA a little away from the centre of the palindrome site; but between the same two bases on the opposite strands. So both the statements I and II are correct.

**Solved independently** (answer withheld)

1. Statement I: Restriction endonucleases indeed recognize specific palindromic nucleotide sequences - this is correct as per NCERT.
2. Statement II: NCERT explicitly describes that the enzyme cuts the DNA strand a little away from the centre of the palindromic site, generating sticky ends - this is also correct.
3. Both statements match NCERT text, so option 2 is correct.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q176_fb0d7657_04112026.png?v=fb0d7657abec)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q176_a203e6e3_04112026.png?v=a203e6e37b75)

---

## Q177

Biology · zoology · Molecular Basis of Inheritance

In an E. Coli strain i gene gets mutated and its product can not bind the inducer molecule. If growth medium is provided with lactose, what will be the outcome?

- (1) RNA polymerase will bind the promoter region
- (2) Only z gene will get transcribed
- (3) z, y, a genes will be transcribed
- **(4)** z, y, a genes will not be translated

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. As the product of '$i$' gene binds with the operator region and blocks the transcription and translation of $z$, $y$ and $a$ genes.
2. It's product is prevented from binding to the operator by attaching it with the inducer. As the inducer can now no more capable of binding with the repressor, thus, in all the cases, operator always gets attached with the repressor thereby preventing the transcription and transmission of $z$, $y$ and $a$.
3. Even in the presence of lactose, transcription and translation of $z$, $y$ and $a$ would not occur.

**Solved independently** (answer withheld)

1. The $i$ gene codes for the repressor; normally the inducer (allolactose) binds the repressor and releases it from the operator.
2. Here the mutated repressor cannot bind the inducer, so even with lactose present it stays bound to the operator.
3. The bound repressor blocks RNA polymerase, so $z$, $y$, $a$ are not transcribed and therefore not translated, which is option $4$.

**Subtopic:** The Lac Operon · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 63)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q177_cf0fcaef_04112026.png?v=cf0fcaef0420)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q177_f88d89fa_04112026.png?v=f88d89fa4834)

---

## Q178

Biology · zoology · Reproductive Health

Lippe’s loop is a type of contraceptive used as:

- (1) Copper releasing IUD
- (2) Cervical barrier
- (3) Vault barrier
- **(4)** Non-Medicated IUD

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because the intrauterine device (IUD) presently available as the non-medicated IUDs, is Lippe's loop.
2. Option (1) is incorrect as copper releasing IUDs are CuT, Cu7 and multiload 375.
3. Option (2) and (3) are incorrect as diaphragms, cervical caps and vaults are included in barrier method of contraception.

**Solved independently** (answer withheld)

1. NCERT classifies IUDs as non-medicated (e.g. Lippes loop), copper-releasing (CuT, Cu7, Multiload 375) and hormone-releasing (Progestasert, LNG-20), so Lippes loop is a non-medicated IUD, option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 63)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q178_2f72a001_04112026.png?v=2f72a00131f7)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q178_ccc28acb_04112026.png?v=ccc28acbf29b)

---

## Q179

Biology · zoology · Animal Kingdom

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R).
In the light of the above statements, choose the **most appropriate** answer from the option given below :

- Assertion (A) All vertebrates are chordates but all chordates are not vertebrates.
- Reason (R) Notochord is replaced by vertebral column in the adult vertebrates.

- (1) **(A)** is not correct but **(R)** is correct
- **(2)** Both **(A)** and **(R)** are correct and **(R)** is the correct explanation of **(A)**
- (3) Both **(A)** and **(R)** are correct but **(R)** is not the correct explanation of **(A)**
- (4) **(A)** is correct but **(R)** is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because all chordates are divided into three subphyla – Urochordata, Cephalochordata and Vertebrata.
2. In subphylum Vertebrata, notochord is replaced by bony or cartilaginous vertebral column in adults.
3. Therefore, all vertebrates are chordates but all chordates are not vertebrates.

**Solved independently** (answer withheld)

1. Assertion: vertebrates are a subphylum of Chordata, while urochordates and cephalochordates are chordates without a vertebral column, so (A) is true.
2. Reason: in vertebrates the embryonic notochord is replaced by a cartilaginous or bony vertebral column in the adult, so (R) is true.
3. Having a vertebral column that replaces the notochord is what separates vertebrates from other chordates; NCERT gives (R) as the basis for (A), so (R) explains (A), which is option $2$.

**Subtopic:** Phylum – Chordata · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 63)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q179_d121a9e3_04112026.png?v=d121a9e391e1)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q179_3f0bec54_04112026.png?v=3f0bec5435f6)

---

## Q180

Biology · zoology · Cell: The Unit of Life

Which of the following statements with respect to Endoplasmic Reticulum is incorrect?

- (1) SER are the sites for lipid synthesis
- (2) RER has ribosomes attached to ER
- (3) SER is devoid of ribosomes
- **(4)** In prokaryotes only RER are present

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In prokaryotes, ER is absent be it RER or SER.

**Solved independently** (answer withheld)

1. Prokaryotic cells lack membrane-bound organelles, including the endoplasmic reticulum, so the statement that only RER is present in prokaryotes is incorrect, which is option $4$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q180_af832f77_04112026.png?v=af832f77dd99)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q180_28874e82_04112026.png?v=28874e82ba40)

---

## Q181

Biology · zoology · Biological Classification

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below

- (Statement I) Mycoplasma can pass through less than $1$ micron filter size.
- (Statement II) Mycoplasma are bacteria with cell wall.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Mycoplasma are the smallest cells and are only $0.3\ \mu\mathrm{m}$ in length. So it can pass through less than $1\ \mu\mathrm{m}$ filter size.
2. Mycoplasma lack cell wall.

**Solved independently** (answer withheld)

1. Statement I: Mycoplasma are the smallest known bacteria, small enough to pass through bacterial filters (<1 micron) - correct.
2. Statement II: Mycoplasma lack a cell wall entirely, unlike typical bacteria - incorrect.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q181_7e4b186f_04112026.png?v=7e4b186f6855)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q181_f75d9406_04112026.png?v=f75d94060a0f)

---

## Q182

Biology · zoology · Evolution

Natural selection where more individuals acquire specific character value other than the mean character value, leads to

- (1) Random change
- (2) Stabilising change
- **(3)** Directional change
- (4) Disruptive change

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is correct because in directional natural selection more individuals acquire value other than the mean character value.
2. Option (4) is incorrect because in disruptive change, more individuals acquire peripheral character value at both ends of the distribution curve.
3. Option (1) is incorrect because there is no random change in natural selection.
4. Option (2) is incorrect because natural selection leads to stabilisation when more individuals acquire mean character value.

**Solved independently** (answer withheld)

1. As NCERT teaches it, in directional selection more individuals acquire a value other than the mean character value, so the peak shifts in one direction; this is option $3$ (Directional change).

**Subtopic:** Types of Natural Selection · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 64)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q182_c345aa1a_04112026.png?v=c345aa1a1e55)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q182_77323ab3_04112026.png?v=77323ab331f6)

---

## Q183

Biology · zoology · Locomotion and Movement

Given below are two statements : one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.

**Assertion (A):**

**Reason (R):**

In the light of the above statements, choose the **most appropriate** answer from the options given below.

- Assertion (A) Osteoporosis is characterised by decreased bone mass and increased chance of fractures.
- Reason (R) Common cause of osteoporosis is increased levels of estrogen.

- (1) **(A)** is not correct but **(R)** is correct
- (2) Both **(A)** and **(R)** are correct and **(R)** is the correct explanation of **(A)**
- (3) Both **(A)** and **(R)** are correct but **(R)** is not the correct explanation of **(A)**
- **(4)** **(A)** is correct but **(R)** is not correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as osteoporosis is due to decreased levels of oestrogen.
2. Osteoporosis is an age-related disorder characterised by decreased bone mass hence, the chances of fractures increase.

**Solved independently** (answer withheld)

1. Assertion: Osteoporosis = decreased bone mass + increased fracture risk — this is true per NCERT.
2. Reason: Osteoporosis is actually caused by decreased estrogen levels (as in menopause), not increased levels, so R is false.
3. Thus A is correct, R is incorrect, matching option 4.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q183_3aa24007_04112026.png?v=3aa24007ccb1)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q183_8056d763_04112026.png?v=8056d7638cbe)

---

## Q184

Biology · zoology · Structural Organisation in Animals

Which of the following is **not** a connective tissue?

- **(1)** Neuroglia
- (2) Blood
- (3) Adipose tissue
- (4) Cartilage

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer as neuroglia are a part of nervous tissue.
2. Neuroglia are the supportive cells of nervous tissue. They make up more than half the volume of neural tissue. Neurons, the unit of neural system are excitable cells.
3. Cartilage and blood are specialised type of connective tissues.
4. Adipose tissue is a type of loose connective tissue.

**Solved independently** (answer withheld)

1. Blood (fluid), adipose tissue (loose) and cartilage (specialised) are all connective tissues, while neuroglia belong to neural tissue, so the answer is option $1$.

**Subtopic:** Connective Tissue, Muscle Tissue and Neural Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q184_8f48c247_04112026.png?v=8f48c24786ab)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q184_c9f38376_04112026.png?v=c9f38376c7f5)

---

## Q185

Biology · zoology · Excretory Products and Their Elimination

Nitrogenous waste is excreted in the form of pellet or paste by :

- **(1)** $Pavo$
- (2) $Ornithorhynchus$
- (3) $Salamandra$
- (4) $Hippocampus$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because birds ($Pavo$) excrete nitrogenous wastes as uric acid in the form of pellet or paste with a minimum loss of water.
2. Option (3) and (4) are incorrect because many bony fishes (like $Hippocampus$) and aquatic amphibians (like $Salamandra$) are ammonotelic in nature.
3. Option (2) is incorrect because mammals (like $Ornithorhynchus$) mainly excrete urea and are called ureotelic animals.

**Solved independently** (answer withheld)

1. Uricotelic animals (reptiles, birds, land snails, insects) excrete uric acid as a pellet or paste; Ornithorhynchus is a ureotelic mammal, Salamandra a ureotelic amphibian, Hippocampus an ammonotelic bony fish, and Pavo a uricotelic bird, so the answer is option $1$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q185_ca31428f_04112026.png?v=ca31428fa265)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q185_d07e5279_04112026.png?v=d07e52794348)

---

## Q186

Biology · zoology · Body Fluids and Circulation

Which one of the following statements is **correct**?

- (1) Increased ventricular pressure causes closing of the semilunar valves.
- (2) The atrio-ventricular node (AVN) generates an action potential to stimulate atrial contraction
- (3) The tricuspid and the bicuspid valves open due to the pressure exerted by the simultaneous contraction of the atria
- **(4)** Blood moves freely from atrium to the ventricle during joint diastole.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because during joint diastole, blood moves freely from atrium to ventricle as atrioventricular valve remain open during joint diastole.
2. Option (1) is incorrect because decrease in ventricular pressure, during ventricular diastole closes semilunar valves to produce 'dub' heart sound.
3. Option (2) is incorrect because SA node generates action potential to stimulate atrial contraction.
4. Option (3) is incorrect because bicuspid and tricuspid valves open due to pressure exerted by blood present in atria and decrease in pressure in ventricles during ventricular diastole.

**Solved independently** (answer withheld)

1. Option 2 is false: the SA node, not the AV node, generates the action potential that stimulates atrial contraction.
2. Option 3 is false: the tricuspid and bicuspid valves are already open during joint diastole; atrial systole only adds about 30% more blood.
3. Option 1 is false: increased ventricular pressure closes the AV valves and opens the semilunar valves; semilunar valves close when ventricular pressure falls below arterial pressure.
4. Option 4 is true: during joint diastole the AV valves are open, so blood moves freely from atria into ventricles, giving option $4$.

**Subtopic:** Cardiac Cycle · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 66)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q186_2bdf5177_04112026.png?v=2bdf51772a6a)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q186_cbe164c8_04112026.png?v=cbe164c8fd84)

---

## Q187

Biology · zoology · Evolution

Which of the following statements **is not** true?

- **(1)** Flippers of penguins and dolphins are a pair of homologous organs
- (2) Analogous structures are a result of convergent evolution
- (3) Sweet potato and potato is an example of analogy
- (4) Homology indicates common ancestry

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because flippers of penguins and dolphins are analogous organs as they help in swimming but do not have the same structure.
2. Option (2), (3) and (4) are true statements and hence cannot be the correct answer.
3. Homologous organs have the same structure but have different functions according to the needs of the organisms. Hence, homology indicates common ancestry.
4. Analogous structures have developed for the same function but do not show a similarity in structure. Hence, they are a result of convergent evolution.
5. Sweet potato is a root modification for food storage whereas potato is an underground stem modification for storage. Hence they are analogous.

**Solved independently** (answer withheld)

1. Analogous structures arise from convergent evolution, so statement 1 is true; homology indicates common ancestry, so statement 3 is true; sweet potato (root) and potato (stem) are analogous, so statement 2 is true.
2. Flippers of penguins and dolphins perform the same function but evolved independently, so they are analogous, not homologous; statement $4$ is not true, which is option $1$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 66)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q187_fa6da5a3_04112026.png?v=fa6da5a3cb31)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q187_f5b4ad4e_04112026.png?v=f5b4ad4e87aa)

---

## Q188

Biology · zoology · Biotechnology and Its Applications

Statements related to human Insulin are given below.
Which statement(s) is/are correct about genetically engineered Insulin?
Choose the most appropriate answer from the options given below:

- (a) Pro-hormone insulin contain extra stretch of C-peptide
- (b) A-peptide and B-peptide chains of insulin were produced separately in E.coli, extracted and combined by creating disulphide bond between them.
- (c) Insulin used for treating Diabetes was extracted from Cattles and Pigs.
- (d) Pro-hormone Insulin needs to be processed for converting into a mature and functional hormone.
- (e) Some patients develop allergic reactions to the foreign insulin.

- (1) (c), (d) and (e) only
- (2) (a), (b) and (d) only
- **(3)** (b) only
- (4) (c) and (d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as genetically engineered insulin has A-peptide and B-peptide chains of insulin which are produced separately in $E.coli$, then they are extracted and combined by creating disulphide bond between them.
2. Statement (a) is incorrect as genetically engineered insulin does not have an extra stretch of C-peptide.
3. Statement (c) is incorrect as insulin obtained from cattles and pigs is not genetically engineered insulin.
4. Statement (d) is incorrect because conversion of pro-insulin to insulin is not required during production of insulin by genetic engineering as A-peptide and B-peptide chains are produced separately.
5. Statement (e) is incorrect as allergic reactions to insulin are mostly seen when the insulin is obtained from animals.

**Solved independently** (answer withheld)

1. Statement (b) is the NCERT account of genetically engineered insulin: A and B chains produced separately in $E.\ coli$, extracted and joined by disulphide bridges, so (b) applies.
2. Statements (a) and (d) describe natural pro-insulin with its C-peptide that must be processed to mature insulin; in the engineered route the C-peptide is avoided, so they do not describe engineered insulin.
3. Statements (c) and (e) describe insulin from cattle and pigs and the allergic reactions to it, which is the problem engineered insulin solved, so they are not about engineered insulin.
4. Only (b) is correct about genetically engineered insulin, which is option $3$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** hard (6 steps)

**Printed in the booklet** (page 66)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q188_c46f7994_04112026.png?v=c46f7994e195)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q188_40f8fa86_04112026.png?v=40f8fa86c20c)

---

## Q189

Biology · zoology · Human Health and Disease

Select the **incorrect** statement with respect to acquired immunity.

- **(1)** Acquired immunity is non-specific type of defense present at the time of birth.
- (2) Primary response is produced when our body encounters a pathogen for the first time.
- (3) Anamnestic response is elicited on subsequent encounters with the same pathogen.
- (4) Anamnestic response is due to memory of first encounter.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer as acquired immunity is a specific type of defence which is not present at the time of birth.
2. Option (2), (3) and (4) are true statements and hence cannot be the answer.
3. Anamnestic response or secondary immune response is a highly intensified response due to memory of first encounter.
4. When our body encounters a pathogen for the first time then the body elicits the primary immune response.
5. When there is a subsequent encounter with the same pathogen, secondary or anamnestic immune response is elicited.

**Solved independently** (answer withheld)

1. Acquired immunity is pathogen-specific, has memory and is not present at birth; innate immunity is the non-specific defence present at birth, so statement $4$ is the incorrect one.

**Subtopic:** Acquired Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q189_a16df052_04112026.png?v=a16df0529918)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q189_b4b4ca47_04112026.png?v=b4b4ca47815c)

---

## Q190

Biology · zoology · Neural Control and Coordination

Select the **incorrect** statement regarding synapses :

- **(1)** Impulse transmission across a chemical synapse is always faster than that across an electrical synapse.
- (2) The membranes of presynaptic and postsynaptic neurons are in close proximity in an electrical synapse.
- (3) Electrical current can flow directly from one neuron into the other across the electrical synapse.
- (4) Chemical synapses use neurotransmitters

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer as impulse transmission across an electrical synapse is always faster than that across a chemical synapse.
2. $\rightarrow$ Chemical synapses use chemicals for transmission which are known as neurotransmitters.
3. $\rightarrow$ The membranes of presynaptic and postsynaptic neurons are in close proximity in an electrical synapse.
4. $\rightarrow$ In an electrical synapse, the transmission of the impulse occurs in the form of an electrical current from one neuron to the next neuron.

**Solved independently** (answer withheld)

1. Options 2, 3 and 4 are true: in an electrical synapse the membranes are very close and current flows directly between neurons, and chemical synapses use neurotransmitters; impulse transmission across an electrical synapse is always faster than across a chemical synapse, so option $1$ is the incorrect statement.

**Subtopic:** Transmission of Impulses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q190_d0740469_04112026.png?v=d074046972c9)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q190_c64480d4_04112026.png?v=c64480d4a377)

---

## Q191

Biology · zoology · Principles of Inheritance and Variation

If a colour blind female marries a man whose mother was also colour blind, what are the chances of her progeny having colour blindness?

- **(1)** $100\%$
- (2) $25\%$
- (3) $50\%$
- (4) $75\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. If mother of man is colourblind, then man will also be colourblind as colour blindness is a X-linked recessive trait and shows criss-cross inheritance.

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q191_sol_1_d887c771_04112026.png?v=d887c771a1ee)


**Solved independently** (answer withheld)

1. The colour blind female is homozygous: $X^cX^c$.
2. The man's mother was colour blind ($X^cX^c$), so she passes $X^c$ to him; the man is $X^cY$ (colour blind).
3. Cross $X^cX^c \times X^cY$: daughters $X^cX^c$, sons $X^cY$.
4. All progeny are colour blind, i.e. $100\%$, which is option $1$.

**Subtopic:** Colour Blindness · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 68)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q191_5d579dab_04112026.png?v=5d579dab29d9)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q191_04fbad24_04112026.png?v=04fbad24351a)

---

## Q192

Biology · zoology · Principles of Inheritance and Variation

The recombination frequency between the genes a & c is $5\%$, b & c is $15\%$, b & d is $9\%$, a & b is $20\%$, c & d is $24\%$ and a & d is $29\%$. What will be the sequence of these genes on a linear chromosome?

- **(1)** a, c, b, d
- (2) a, d, b, c
- (3) d, b, a, c
- (4) a, b, c, d

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $1\%$ recombination frequency $=1$ centi Morgan
2. To place the genes on a linear chromosome, decreasing order of recombination frequency will be considered.

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q192_sol_1_c99eb47c_04112026.png?v=c99eb47c83b9)


**Solved independently** (answer withheld)

1. Recombination frequency is proportional to map distance, so the farthest pair $a$–$d$ ($29\%$) are the two ends.
2. $a$–$c = 5\%$ is smallest from $a$, so $c$ lies next to $a$: $a, c, \dots$
3. $c$–$b = 15\%$ places $b$ after $c$: $a$–$b = 5 + 15 = 20\%$, matching the given value.
4. $b$–$d = 9\%$ places $d$ last: $c$–$d = 15 + 9 = 24\%$ and $a$–$d = 5 + 15 + 9 = 29\%$, both matching.
5. The order is $a, c, b, d$, which is option $1$.

**Subtopic:** Linkage & Recombination · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 68)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q192_8c61d882_04112026.png?v=8c61d882e3dc)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q192_e5ed0bc2_04112026.png?v=e5ed0bc2f598)

---

## Q193

Biology · zoology · Biological Classification

Which of the following is a **correct** statement?

- (1) Mycoplasma have DNA, ribosome and cell wall.
- **(2)** Cyanobacteria are a group of autotrophic organisms classified under kingdom Monera.
- (3) Bacteria are exclusively heterotrophic organisms.
- (4) Slime moulds are saprophytic organisms classified under Kingdom Monera.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Slime moulds are classified under kingdom Protista.
2. Mycoplasma lack cell wall.
3. Bacteria can be autotrophic as well as heterotrophic.

**Solved independently** (answer withheld)

1. Mycoplasma lack a cell wall (have DNA and ribosomes but no cell wall), so option 1 is false.
2. Cyanobacteria are photosynthetic (autotrophic) prokaryotes under Kingdom Monera, so option 2 is correct.
3. Bacteria show diverse modes of nutrition (autotrophic and heterotrophic), so option 3 is false.
4. Slime moulds are classified under Kingdom Protista, not Monera, so option 4 is false.

**Subtopic:** Eubacteria · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 69)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q193_60c1e28a_04112026.png?v=60c1e28a5b40)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q193_f1fc69c9_04112026.png?v=f1fc69c92be9)

---

## Q194

Biology · zoology · Reproductive Health

Match **List-I** with **List-II** with respect to methods of Contraception and their respective actions.

Choose the **correct answer** from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Diaphragms | (i) | Inhibit ovulation and Implantation |
| (b) | Contraceptive Pills | (ii) | Increase phagocytosis of sperm within Uterus |
| (c) | Intra Uterine Devices | (iii) | Absence of Menstrual cycle and ovulation following parturition |
| (d) | Lactational Amenorrhea | (iv) | They cover the cervix blocking the entry of sperms |

- (1) (a) - (iii), (b) - (ii), (c) - (i), (d) - (iv)
- (2) (a) - (iv), (b) - (i), (c) - (iii), (d) - (ii)
- **(3)** (a) - (iv), (b) - (i), (c) - (ii), (d) - (iii)
- (4) (a) - (ii), (b) - (iv), (c) - (i), (d) - (iii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because
2. Diaphragms are barrier methods of contraception. They cover the cervix and block the entry of sperms.
3. Contraceptive pills are preparations containing either progestogens alone or combination of progestogen and oestrogen. They inhibit ovulation and implantation as well as alter the quality of cervical mucus to prevent entry of sperms.
4. Intra uterine devices increase the phagocytosis of sperms within the uterus.
5. Lactational amenorrhoea is a natural method of contraception and it is based on the fact that the ovulation and therefore menstrual cycle do not occur during the period of intense lactation following parturition.

**Solved independently** (answer withheld)

1. Diaphragms are barriers that cover the cervix and block sperm entry: $(a) \to (iv)$.
2. Contraceptive pills inhibit ovulation and implantation: $(b) \to (i)$.
3. Intra uterine devices increase phagocytosis of sperm within the uterus: $(c) \to (ii)$.
4. Lactational amenorrhea is the absence of menstruation and ovulation following parturition: $(d) \to (iii)$.
5. The match $a$-$iv$, $b$-$i$, $c$-$ii$, $d$-$iii$ is option $3$.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 69)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q194_4ff799ff_04112026.png?v=4ff799ffd311)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q194_491010c1_04112026.png?v=491010c15f62)

---

## Q195

Biology · zoology · Chemical Coordination and Integration

Which of the following are **not** the effects of Parathyroid hormone?

Choose the **most appropriate** answer from the options given below:

- (a) Stimulates the process of bone resorption
- (b) Decreases $\mathrm{Ca^{2+}}$ level in blood
- (c) Reabsorption of $\mathrm{Ca^{2+}}$ by renal tubules
- (d) Decreases the absorption of $\mathrm{Ca^{2+}}$ from digested food
- (e) Increases metabolism of carbohydrates

- (1) (b) and (c) only
- (2) (a) and (c) only
- **(3)** (b), (d) and (e) only
- (4) (a) and (e) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option $(3)$ is the correct answer because parathyroid hormone is a hypercalcemic hormone $i.e$, it increases the blood calcium levels. It also increases the absorption of calcium from digested food. Glucocorticoids regulate the carbohydrate metabolism.
2. Option $(4)$ is not the answer because parathyroid hormone stimulates the process of bone resorption.
3. Option $(1)$ and $(2)$ are not the answers because reabsorption of $\mathrm{Ca^{2+}}$ by renal tubules is a function of PTH.

**Solved independently** (answer withheld)

1. PTH is hypercalcaemic: it stimulates bone resorption, so (a) is an effect.
2. PTH stimulates $\mathrm{Ca^{2+}}$ reabsorption by renal tubules, so (c) is an effect.
3. PTH increases blood $\mathrm{Ca^{2+}}$ and increases $\mathrm{Ca^{2+}}$ absorption from digested food, so (b) and (d) are not effects; carbohydrate metabolism is not a PTH action, so (e) is not an effect.
4. Not effects: (b), (d) and (e), which is option $3$.

**Subtopic:** Thyroid Gland and Parathyroid Gland · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 69)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q195_bec93ad0_04112026.png?v=bec93ad0981d)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q195_b6a9d093_04112026.png?v=b6a9d093af59)

---

## Q196

Biology · zoology · Structural Organisation in Animals

Match **List-I** with **List-II**

Choose the **correct answer** from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Bronchioles | (i) | Dense Regular Connective Tissue |
| (b) | Goblet Cell | (ii) | Loose Connective Tissue |
| (c) | Tendons | (iii) | Glandular Tissue |
| (d) | Adipose Tissue | (iv) | Ciliated Epithelium |

- (1) (a) - (iii), (b) - (iv), (c) - (ii), (d) - (i)
- **(2)** (a) - (iv), (b) - (iii), (c) - (i), (d) - (ii)
- (3) (a) - (i), (b) - (ii), (c) - (iii), (d) - (iv)
- (4) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because
2. Ciliated epithelium is mainly present in the inner surface of hollow organs like bronchioles and fallopian tubes. The function is to move particles or mucus in a specific direction over the epithelium.
3. Some of the columnar or cuboidal cells get specialised for secretion and are called glandular epithelium. Goblet cells are unicellular glands.
4. Tendons are dense regular connective tissues. They attach skeletal muscles to bones.
5. Adipose tissue is a type of loose connective tissue located mainly beneath the skin. The cells of this tissue are specialised to store fats.

**Solved independently** (answer withheld)

1. Bronchioles are lined by ciliated epithelium, so $(a) \to (iv)$.
2. Goblet cells are unicellular glands of glandular epithelium, so $(b) \to (iii)$.
3. Tendons are dense regular connective tissue, so $(c) \to (i)$.
4. Adipose tissue is a type of loose connective tissue, so $(d) \to (ii)$.
5. The match $(a)-(iv), (b)-(iii), (c)-(i), (d)-(ii)$ is option $2$.

**Subtopic:** Animal Tissues: Epithelial Tissue, Connective Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q196_4c2f43df_04112026.png?v=4c2f43df034d)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q196_48e3f2b3_04112026.png?v=48e3f2b308c9)

---

## Q197

Biology · zoology · Environmental Issues

Given below are two statements:

In the light of the above statements, choose the **most appropriate** answer from the options given below :

- (Statements I) In a scrubber the exhaust from the thermal plant is passed through the electric wires to charge the dust particles.
- (Statement II) Particulate matter (PM 2.5) cannot be removed by scrubber but can be removed by an electrostatic precipitator.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Scrubber is used by the industries which produce $\mathrm{SO_2}$ as a by product.
2. The limestone present in slurry of scrubber remove $\mathrm{SO_2}$ from the exhaust.
3. Electrostatic precipitator is the most effective device to remove $99\%$ of particulate matter, 'even PM 2.5' present in the exhaust.

**Solved independently** (answer withheld)

1. Statement I: passing exhaust through electrode wires to charge dust particles is how an electrostatic precipitator works; a scrubber sprays water or lime to remove gases such as $SO_2$, so Statement I is incorrect.
2. Statement II: a scrubber removes gases, not fine particulate matter, while an electrostatic precipitator removes over $99\%$ of particulate matter, so Statement II is taken as correct.
3. I incorrect and II correct gives option $1$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 70)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q197_aed4716f_04112026.png?v=aed4716f624f)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q197_9164493d_04112026.png?v=9164493d1407)

---

## Q198

Biology · zoology · Molecular Basis of Inheritance

Ten $E.coli$ cells with $^{15}\mathrm{N}$ - dsDNA are incubated in medium containing $^{14}\mathrm{N}$ nucleotide. After 60 minutes, how many $E.coli$ cells will have DNA totally free from $^{15}\mathrm{N}$?

- (1) 80 cells
- (2) 20 cells
- (3) 40 cells
- **(4)** 60 cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. From 10 parent $E.coli$ cells
2. $1^{\mathrm{st}}$ generation

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q198_sol_1_884d266e_04112026.png?v=884d266e2707)

3. $2^{\mathrm{nd}}$ generation

![printed figure: solution_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q198_sol_2_6958a3ab_04112026.png?v=6958a3abc337)

4. $3^{\mathrm{rd}}$ generation

![printed figure: solution_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/figures_agent/q198_sol_3_168c227d_04112026.png?v=168c227d49bc)

5. Therefore, after 60 minutes, 60 $E.coli$ cells will have DNA totally free from $^{15}\mathrm{N}$.

**Solved independently** (answer withheld)

1. E. coli divides once every $20\,\text{min}$, so in $60\,\text{min}$ there are $\frac{60}{20} = 3$ generations.
2. Total cells after 3 generations: $10 \times 2^3 = 80$.
3. Replication is semiconservative: the two original $^{15}N$ strands of each parent DNA stay intact and end up in 2 cells, so cells carrying $^{15}N$ $= 10 \times 2 = 20$.
4. Cells totally free of $^{15}N$ $= 80 - 20 = 60$, which is option $4$.

**Subtopic:** Experimental Proof that DNA is Semiconservative · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 71)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q198_f6debd8f_04112026.png?v=f6debd8f0e08)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q198_00e2418a_04112026.png?v=00e2418adcf3)

---

## Q199

Biology · zoology · Biotechnology: Principles and Processes

Which of the following is **not** a desirable feature of a cloning vector?

- **(1)** Presence of two or more recognition sites
- (2) Presence of origin of replication
- (3) Presence of a marker gene
- (4) Presence of single restriction enzyme site

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer. Cloning vectors are the carriers of the desired gene in the host cell. The features desirable in a cloning vector are:-
2. Presence of origin of replication
3. Presence of marker genes
4. Presence of very few, preferably single recognition site for the commonly used restriction enzymes

**Solved independently** (answer withheld)

1. Desirable vector features are an origin of replication (ori), a selectable marker gene and a single (unique) recognition site for a restriction enzyme; two or more recognition sites for the same enzyme would fragment the vector, so the undesirable feature is option $1$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 71)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q199_4287989b_04112026.png?v=4287989b609f)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q199_ea832745_04112026.png?v=ea83274509b2)

---

## Q200

Biology · zoology · Biomolecules

Match List-I with List-II

List-I (Biological Molecules)

List-II (Biological functions)

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Glycogen | (i) | Hormone |
| (b) | Globulin | (ii) | Biocatalyst |
| (c) | Steroids | (iii) | Antibody |
| (d) | Thrombin | (iv) | Storage product |

- **(1)** (a) - (iv), (b) - (iii), (c) - (i), (d) - (ii)
- (2) (a) - (iii), (b) - (ii), (c) - (iv), (d) - (i)
- (3) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii)
- (4) (a) - (ii), (b) - (iv), (c) - (iii), (d) - (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer as glycogen is a polysaccharide and is a storage product in animals.
2. Globulins form antibodies which are also known as immunoglobulins.
3. Steroids form hormones like testosterone.
4. Thrombin is a biocatalyst which converts soluble fibrinogen to insoluble fibrin.

**Solved independently** (answer withheld)

1. Glycogen is the storage polysaccharide in animals, so $(a) \to (iv)$.
2. Globulins (immunoglobulins) function as antibodies, so $(b) \to (iii)$.
3. Steroids such as testosterone and oestrogen act as hormones, so $(c) \to (i)$.
4. Thrombin is an enzyme in blood clotting, i.e. a biocatalyst, so $(d) \to (ii)$.
5. The match $a$-$iv$, $b$-$iii$, $c$-$i$, $d$-$ii$ is option $1$.

**Subtopic:** Biomacromolecules · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/crops/q200_51f3ef69_04112026.png?v=51f3ef693c43)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2022/2022_R4/solutions/q200_2e22f550_04112026.png?v=2e22f550c570)

