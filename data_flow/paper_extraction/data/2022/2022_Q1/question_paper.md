# NEET (UG) 2022 · Code Q1

200 questions · source `NEET_Papers/2022/Set_Q1/Download_Here.pdf` · every image a CDN link (0 without one) · 66 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Electromagnetic Waves

Match List-I with List-II
List-I (Electromagnetic waves) | List-II (Wavelength)
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | AM radio waves | (i) | $10^{-10}\,\mathrm{m}$ |
| (b) | Microwaves | (ii) | $10^{2}\,\mathrm{m}$ |
| (c) | Infrared radiations | (iii) | $10^{-2}\,\mathrm{m}$ |
| (d) | X-rays | (iv) | $10^{-4}\,\mathrm{m}$ |

- (1) (a) - (iv), (b) - (iii), (c) - (ii), (d) - (i)
- (2) (a) - (iii), (b) - (ii), (c) - (i), (d) - (iv)
- (3) (a) - (iii), (b) - (iv), (c) - (ii), (d) - (i)
- **(4)** (a) - (ii), (b) - (iii), (c) - (iv), (d) - (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Table of electromagnetic waves and their wavelengths](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q001_sol_1_e1e094e9_02112026.svg?v=e1e094e91557)

*Table of electromagnetic waves and their wavelengths*

![drawn: Table of electromagnetic waves and their wavelengths](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q001_solution_1_cd016fad_02112026.svg?v=cd016fad503a)  
*drawn by code/lib/physics_figure.py*

1. (a) - (ii)
2. (b) - (iii)
3. (c) - (iv)
4. (d) - (i)

**Solved independently** (answer withheld)

1. AM radio waves have wavelengths of order $10^{2}\,\mathrm{m}$, so (a) - (ii).
2. Microwaves have wavelengths of order $10^{-2}\,\mathrm{m}$, so (b) - (iii).
3. Infrared radiation has wavelengths of order $10^{-4}\,\mathrm{m}$, so (c) - (iv).
4. X-rays have wavelengths of order $10^{-10}\,\mathrm{m}$, so (d) - (i).
5. The matching (a) - (ii), (b) - (iii), (c) - (iv), (d) - (i) is option $4$.

**Subtopic:** Electromagnetic Spectrum · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q001_62f8e426_02112026.png?v=62f8e4262c73)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q001_88f2e269_02112026.png?v=88f2e269597f)

---

## Q2

Physics · Thermodynamics

An ideal gas undergoes four different processes from the same initial state as shown in the figure below. Those processes are adiabatic, isothermal, isobaric and isochoric. The curve which represents the adiabatic process among 1, 2, 3 and 4 is

![printed figure: P-V diagram: four processes 1, 2, 3, 4 from the same initial state](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q002_381f43f0_02112026.png?v=381f43f0ebb4)

*P-V diagram: four processes 1, 2, 3, 4 from the same initial state*

![drawn: P-V diagram: four processes 1, 2, 3, 4 from the same initial state](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q002_question_87e49f2b_02112026.svg?v=87e49f2b2458)  
*drawn by code/lib/physics_figure.py*

- (1) 1
- **(2)** 2
- (3) 3
- (4) 4

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\left(\frac{dP}{dV}\right)_{\text{adiabatic}} = -\gamma P$
2. $\left(\frac{dP}{dV}\right)_{\text{isothermal}} = -P$
3. $\left(\frac{dP}{dV}\right)_{\text{adiabatic}} > \left(\frac{dP}{dV}\right)_{\text{isothermal}}$

![printed figure: P-V diagram of isobaric, isothermal, adiabatic and isochoric processes from one initial state](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q002_sol_1_cac8c971_02112026.png?v=cac8c971cba9)

*P-V diagram of isobaric, isothermal, adiabatic and isochoric processes from one initial state*

![drawn: P-V diagram of isobaric, isothermal, adiabatic and isochoric processes from one initial state](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q002_solution_1_b45af787_02112026.svg?v=b45af787b1e2)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Curve $1$ is vertical ($V$ constant), so it is isochoric.
2. Curve $4$ is horizontal ($P$ constant), so it is isobaric.
3. For the isothermal process $PV = \text{const}$, so $\frac{dP}{dV} = -\frac{P}{V}$.
4. For the adiabatic process $PV^{\gamma} = \text{const}$, so $\frac{dP}{dV} = -\gamma\frac{P}{V}$.
5. Since $\gamma > 1$, the adiabatic curve is steeper than the isothermal one from the same initial state.
6. Curve $2$ is steeper than curve $3$, so curve $2$ is adiabatic, which is option $2$.

**Subtopic:** Adiabatic Process · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q002_078eded8_02112026.png?v=078eded81a74)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q002_13e4a1ab_02112026.png?v=13e4a1ab604e)

---

## Q3

Physics · Rotational Motion

The angular speed of a fly wheel moving with uniform angular acceleration changes from $1200\,\mathrm{rpm}$ to $3120\,\mathrm{rpm}$ in $16$ seconds. The angular acceleration in $\mathrm{rad/s^2}$ is

- (1) $2\pi$
- **(2)** $4\pi$
- (3) $12\pi$
- (4) $104\pi$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Angular acceleration $\alpha = \frac{\omega_f - \omega_i}{t}$
2. $\omega_f = 3120 \times \frac{2\pi}{60}\,\mathrm{rad/s}$
3. $\omega_i = 1200 \times \frac{2\pi}{60}\,\mathrm{rad/s}$
4. $\Rightarrow \alpha = \frac{(3120 - 1200)}{16} \times \frac{2\pi}{60} = 4\pi$

**Solved independently** (answer withheld)

1. Change in angular speed: $\Delta n = 3120 - 1200 = 1920\,\mathrm{rpm}$.
2. Convert to rev/s: $\frac{1920}{60} = 32\,\mathrm{rev/s}$.
3. Convert to rad/s: $\Delta\omega = 2\pi \times 32 = 64\pi\,\mathrm{rad/s}$.
4. $\alpha = \frac{\Delta\omega}{t} = \frac{64\pi}{16} = 4\pi\,\mathrm{rad/s^2}$, which is option $2$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q003_f0af63fe_02112026.png?v=f0af63fe612f)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q003_da46117b_02112026.png?v=da46117bb655)

---

## Q4

Physics · Semiconductor Electronics

In the given circuits (a), (b) and (c), the potential drop across the two $p$-$n$ junctions are equal in

![printed figure: Three circuits (a), (b), (c): two p-n junctions joined in series across a cell](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q004_bd3c092a_02112026.png?v=bd3c092a34de)

*Three circuits (a), (b), (c): two p-n junctions joined in series across a cell*

![drawn: Three circuits (a), (b), (c): two p-n junctions joined in series across a cell](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q004_question_1face637_02112026.svg?v=1face6376a3f)  
*drawn by code/lib/physics_figure.py*

- (1) Circuit (a) only
- (2) Circuit (b) only
- (3) Circuit (c) only
- **(4)** Both circuits (a) and (c)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Potential drops across the $p$-$n$ junctions will be same if either both junctions are forward biased or both junction are reverse biased.
2. In figure (a) and (c), both junctions are forward biased therefore both have same potential.
3. In figure (b) first junction is forward biased and second junction is reverse biased, so both junctions have different potential difference.

**Solved independently** (answer withheld)

1. In circuit (a) both junctions are oriented $P\to N$ in series, so the same current flows through both with the same bias; identical junctions give $V_1 = V_2$.
2. In circuit (b) one junction is $P\to N$ and the other $N\to P$, so one is forward biased and the other reverse biased; $V_{\text{forward}} \ll V_{\text{reverse}}$, so the drops are unequal.
3. In circuit (c) both junctions are oriented $N\to P$ in series, so both have the same bias and $V_1 = V_2$.
4. Equal drops occur in (a) and (c), which is option $4$.

**Subtopic:** PN Junction Diode Under Forward Bias, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q004_e4616afc_02112026.png?v=e4616afcb790)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q004_5ab6e7fc_02112026.png?v=5ab6e7fc8d84)

---

## Q5

Physics · Ray Optics

A biconvex lens has radii of curvature, $20\,\mathrm{cm}$ each. If the refractive index of the material of the lens is $1.5$, the power of the lens is

- (1) $+2\,\mathrm{D}$
- (2) $+20\,\mathrm{D}$
- **(3)** $+5\,\mathrm{D}$
- (4) Infinity

**Answer** — booklet: (3) · independent solve: (3) · agree

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
4. $P = \frac{1}{f} = \frac{1}{0.2\,\mathrm{m}} = +5\,\mathrm{D}$, which is option $3$.

**Subtopic:** Lens Maker Formula, Power of Lens · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q005_d19cc70d_02112026.png?v=d19cc70d1752)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q005_68ff007a_02112026.png?v=68ff007a05cb)

---

## Q6

Physics · Modern Physics

The graph which shows the variation of the de Broglie wavelength ($\lambda$) of a particle and its associated momentum ($p$) is

- (1) ![printed figure: Graph of lambda against p: a straight line rising to the right that does not pass through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q006_option_1_c491031f_03112026.png?v=c491031ffeb1) *Graph of lambda against p: a straight line rising to the right that does not pass through the origin* ![drawn: Graph of lambda against p: a straight line rising to the right that does not pass through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q006_option_1_97d39c42_02112026.svg?v=97d39c42cfcc)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Straight line falling from upper left to lower right on lambda versus p axes](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q006_option_2_6f2716a7_03112026.png?v=6f2716a70962) *Straight line falling from upper left to lower right on lambda versus p axes* ![drawn: Straight line falling from upper left to lower right on lambda versus p axes](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q006_option_2_10260b86_02112026.svg?v=10260b86e6ea)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Graph of lambda against p: curve rising slowly then steeply upward](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q006_option_3_3bb74eb0_03112026.png?v=3bb74eb03681) *Graph of lambda against p: curve rising slowly then steeply upward* ![drawn: Graph of lambda against p: curve rising slowly then steeply upward](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q006_option_3_2e2e8bf6_02112026.svg?v=2e2e8bf6bad0)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: Graph of lambda against p: a curve falling steeply then flattening towards the p axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q006_option_4_1f440166_03112026.png?v=1f44016690cd) *Graph of lambda against p: a curve falling steeply then flattening towards the p axis* ![drawn: Graph of lambda against p: a curve falling steeply then flattening towards the p axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q006_option_4_053b02f8_02112026.svg?v=053b02f8b095)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. de-Broglie wavelength associated with a particle is given by
2. $\lambda = \frac{h}{p}$
3. $\lambda \propto \frac{1}{p}$

![printed figure: Graph of de Broglie wavelength lambda against momentum p: a falling hyperbola-like curve](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q006_sol_1_7c00b16a_02112026.png?v=7c00b16a6dd3)

*Graph of de Broglie wavelength lambda against momentum p: a falling hyperbola-like curve*

![drawn: Graph of de Broglie wavelength lambda against momentum p: a falling hyperbola-like curve](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q006_solution_1_8e1953e6_02112026.svg?v=8e1953e66a0e)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The de Broglie relation is $\lambda = \frac{h}{p}$.
2. So $\lambda p = h = \text{constant}$, i.e. $\lambda \propto \frac{1}{p}$.
3. A graph of $\lambda$ against $p$ is therefore a rectangular hyperbola, falling steeply at small $p$ and approaching the $p$-axis at large $p$, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q006_48a7c0e6_02112026.png?v=48a7c0e6e01d)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q006_0e91b2ef_02112026.png?v=0e91b2ef82ce)

---

## Q7

Physics · Current Electricity

As the temperature increases, the electrical resistance

- (1) Increases for both conductors and semiconductors
- (2) Decreases for both conductors and semiconductors
- **(3)** Increases for conductors but decreases for semiconductors
- (4) Decreases for conductors but increases for semiconductors

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. As the temperature increases the resistivity of the conductor increases hence the electrical resistance increases.
2. However for semiconductor the resistivity decreases with the temperature.
3. Hence electrical resistance of semiconductor decreases.

**Solved independently** (answer withheld)

1. For a conductor, $\rho_T = \rho_0[1 + \alpha (T - T_0)]$ with $\alpha > 0$, so resistance increases with temperature.
2. For a semiconductor, the number density of charge carriers $n$ increases with $T$, so $\rho = \frac{1}{n e \mu}$ decreases and resistance decreases (negative $\alpha$).
3. Resistance increases for conductors but decreases for semiconductors, which is option $3$.

**Subtopic:** Temperature Dependence of Resistivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q007_a2e59b5f_02112026.png?v=a2e59b5f3e1a)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q007_abc278e6_02112026.png?v=abc278e6f225)

---

## Q8

Physics · Mechanical Properties of Fluids

A spherical ball is dropped in a long column of a highly viscous liquid. The curve in the graph shown, which represents the speed of the ball ($v$) as a function of time ($t$) is

![printed figure: Speed v against time t: straight line A and curves B, C, D](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q008_ea5fff98_02112026.png?v=ea5fff98cc8c)

*Speed v against time t: straight line A and curves B, C, D*

![drawn: Speed v against time t: straight line A and curves B, C, D](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q008_question_64f6449e_02112026.svg?v=64f6449e9926)  
*drawn by code/lib/physics_figure.py*

- (1) A
- **(2)** B
- (3) C
- (4) D

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Initial speed of ball is zero and it finally attains terminal speed

![printed figure: Speed v of the ball against time t, rising to the terminal speed v_T (curve B)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q008_sol_1_022e2cf1_02112026.png?v=022e2cf1b0c5)

*Speed v of the ball against time t, rising to the terminal speed v_T (curve B)*

![drawn: Speed v of the ball against time t, rising to the terminal speed v_T (curve B)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q008_solution_1_505204d8_02112026.svg?v=505204d80fbe)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The ball is dropped, so $v(0) = 0$, which rules out curves $C$ and $D$ because they do not start at $v=0$.
2. Net force: $m\frac{dv}{dt} = mg - F_B - 6\pi\eta r v$, so the acceleration falls as $v$ grows.
3. Solving gives $v = v_t\left(1 - e^{-t/\tau}\right)$, which rises from zero and levels off at the terminal velocity $v_t$.
4. Curve $A$ is a straight line that keeps rising, so it has no terminal velocity. Curve $B$ rises and saturates, so the answer is option $2$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q008_66421b4a_02112026.png?v=66421b4a4ddc)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q008_c4584470_02112026.png?v=c45844706b32)

---

## Q9

Physics · Units and Measurements

The dimensions $[\mathrm{MLT^{-2}A^{-2}}]$ belong to the

- (1) Magnetic flux
- (2) Self inductance
- **(3)** Magnetic permeability
- (4) Electric permittivity

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Dimensional formula of magnetic permeability is $[\mathrm{MLT^{-2}A^{-2}}]$

**Solved independently** (answer withheld)

1. Force per unit length between parallel wires: $\frac{F}{l} = \frac{\mu_0 I_1 I_2}{2\pi d}$, so $\mu_0 = \frac{2\pi F d}{l I_1 I_2}$.
2. $[\mu_0] = \frac{[F]}{[I^2]} = \frac{[\mathrm{MLT^{-2}}]}{[\mathrm{A^2}]} = [\mathrm{MLT^{-2}A^{-2}}]$.
3. Check others: $[\phi] = [\mathrm{ML^2T^{-2}A^{-1}}]$, $[L] = [\mathrm{ML^2T^{-2}A^{-2}}]$, $[\varepsilon_0] = [\mathrm{M^{-1}L^{-3}T^4A^2}]$; none match.
4. So the dimensions belong to magnetic permeability, option $3$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q009_1f559048_02112026.png?v=1f5590485121)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q009_62f92e87_02112026.png?v=62f92e87b0e3)

---

## Q10

Physics · Semiconductor Electronics

In half wave rectification, if the input frequency is $60\,\mathrm{Hz}$, then the output frequency would be

- (1) Zero
- (2) $30\,\mathrm{Hz}$
- **(3)** $60\,\mathrm{Hz}$
- (4) $120\,\mathrm{Hz}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In half wave rectifier, the output frequency is same as that of input frequency.

**Solved independently** (answer withheld)

1. In half-wave rectification only one half-cycle of each input cycle is passed, giving one output pulse per input cycle.
2. Hence $f_{out} = f_{in} = 60\,\mathrm{Hz}$, which is option $3$.

**Subtopic:** Half Wave Rectifier · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q010_e54bdef1_02112026.png?v=e54bdef14d41)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q010_13386f42_02112026.png?v=13386f4238e0)

---

## Q11

Physics · Waves

If the initial tension on a stretched string is doubled, then the ratio of the initial and final speeds of a transverse wave along the string is

- (1) $1:1$
- (2) $\sqrt{2}:1$
- **(3)** $1:\sqrt{2}$
- (4) $1:2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know, velocity of transverse wave
2. $v = \sqrt{\frac{T}{\mu}}$
3. $\therefore\; v_i = \sqrt{\frac{T}{\mu}}$ and $v_f = \sqrt{\frac{2T}{\mu}}$
4. $\therefore\; \frac{v_i}{v_f} = \frac{1}{\sqrt{2}}$

**Solved independently** (answer withheld)

1. Speed of a transverse wave on a string: $v = \sqrt{\frac{T}{\mu}}$, with $\mu$ unchanged.
2. $\frac{v_1}{v_2} = \sqrt{\frac{T}{2T}} = \frac{1}{\sqrt{2}}$.
3. So $v_1 : v_2 = 1 : \sqrt{2}$, which is option $3$.

**Subtopic:** Speed of Different Waves · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q011_72c50dba_02112026.png?v=72c50dbacabd)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q011_88199e54_02112026.png?v=88199e54d086)

---

## Q12

Physics · Laws of Motion

A shell of mass $m$ is at rest initially. It explodes into three fragments having mass in the ratio $2:2:1$. If the fragments having equal mass fly off along mutually perpendicular directions with speed $v$, the speed of the third (lighter) fragment is

- (1) $v$
- (2) $\sqrt{2}v$
- **(3)** $2\sqrt{2}v$
- (4) $3\sqrt{2}v$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Momentum of the system would remain conserved.
2. Initial momentum $= 0$
3. Final momentum should also be zero.
4. Let masses be $2m$, $2m$, and $m$
5. Momentum along $x$-direction $= 2mv\hat{i}$
6. Momentum along $y$-direction $= 2mv\hat{j}$
7. Net momentum $= \sqrt{(2mv)^{2} + (2mv)^{2}} = \sqrt{2} \cdot 2mv$
8. Now, $2\sqrt{2}mv = mv'$
9. $v' = 2\sqrt{2}v$

**Solved independently** (answer withheld)

1. Mass ratio $2:2:1$ gives masses $\frac{2m}{5}, \frac{2m}{5}, \frac{m}{5}$.
2. Initial momentum is zero, so total momentum after the explosion is zero.
3. Resultant momentum of the two equal fragments moving perpendicularly: $p = \sqrt{2}\,\frac{2m}{5}v$.
4. The lighter fragment must carry equal and opposite momentum: $\frac{m}{5}u = \frac{2\sqrt{2}m}{5}v$.
5. $u = 2\sqrt{2}v$, which is option $3$.

**Subtopic:** Conservation of Momentum · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q012_ad7a333d_02112026.png?v=ad7a333d066c)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q012_951c80a6_02112026.png?v=951c80a67260)

---

## Q13

Physics · Center of Mass

Two objects of mass $10\,\mathrm{kg}$ and $20\,\mathrm{kg}$ respectively are connected to the two ends of a rigid rod of length $10\,\mathrm{m}$ with negligible mass. The distance of the center of mass of the system from the $10\,\mathrm{kg}$ mass is

- (1) $\frac{10}{3}\,\mathrm{m}$
- **(2)** $\frac{20}{3}\,\mathrm{m}$
- (3) $10\,\mathrm{m}$
- (4) $5\,\mathrm{m}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x-axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q013_sol_1_98a8fe26_02112026.png?v=98a8fe26a21d)

*Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x-axis*

![drawn: Masses 10 kg at (0, 0) and 20 kg at (10, 0) on the x-axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q013_solution_1_aeac04a5_02112026.svg?v=aeac04a5ff8d)  
*drawn by code/lib/physics_figure.py*

1. $X_{\mathrm{cm}} = \frac{m_1x_1 + m_2x_2}{m_1 + m_2}$
2. $= \frac{10 \times 0 + 20 \times 10}{10 + 20}$
3. $= \frac{200}{30}$
4. $= \frac{20}{3}\,\mathrm{m}$

**Solved independently** (answer withheld)

1. Place the $10\,\mathrm{kg}$ mass at $x=0$ and the $20\,\mathrm{kg}$ mass at $x=10\,\mathrm{m}$.
2. $x_{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = \frac{10(0) + 20(10)}{10+20}$.
3. $x_{cm} = \frac{200}{30} = \frac{20}{3}\,\mathrm{m}$, which is option $2$.

**Subtopic:** Center of Mass of Two Particles · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q013_a0a939f6_02112026.png?v=a0a939f64e62)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q013_537f2bbd_02112026.png?v=537f2bbd0678)

---

## Q14

Physics · Mechanical Properties of Fluids

If a soap bubble expands, the pressure inside the bubble

- **(1)** Decreases
- (2) Increases
- (3) Remains the same
- (4) Is equal to the atmospheric pressure

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Excess pressure inside the bubble = $\Delta P = \frac{4T}{R}$
2. $P_{\mathrm{in}} = P_{\mathrm{out}} + \frac{4T}{R}$
3. as '$R$' increases '$P$' decreases

**Solved independently** (answer withheld)

1. Pressure inside a soap bubble (two surfaces): $P_{in} = P_0 + \frac{4T}{R}$.
2. On expansion the radius $R$ increases, so $\frac{4T}{R}$ decreases.
3. Hence $P_{in}$ decreases, which is option $1$.

**Subtopic:** Excess Pressure on Curved Surface (General Case, Drop, Soap Bubbles, Air Bubbles) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q014_fd0ed885_02112026.png?v=fd0ed8859ebe)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q014_e0747506_02112026.png?v=e07475061b00)

---

## Q15

Physics · Work, Energy and Power

An electric lift with a maximum load of $2000\,\mathrm{kg}$ (lift + passengers) is moving up with a constant speed of $1.5\,\mathrm{m\,s^{-1}}$. The frictional force opposing the motion is $3000\,\mathrm{N}$. The minimum power delivered by the motor to the lift in watts is : ($g = 10\,\mathrm{m\,s^{-2}}$)

- (1) $23000$
- (2) $20000$
- **(3)** $34500$
- (4) $23500$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $F_{\mathrm{up}} = 2000g + 3000$
2. $= 23000\,\mathrm{N}$
3. Minimum power $P_{\mathrm{min}} = \vec{F} \cdot \vec{v}$
4. $P_{\mathrm{min}} = Fv = 23000 \times \frac{3}{2}$
5. $= 34500\,\mathrm{W}$

**Solved independently** (answer withheld)

1. At constant speed the net force is zero, so the motor force is $F = mg + f$.
2. $F = 2000 \times 10 + 3000 = 23000\,\mathrm{N}$.
3. $P = Fv = 23000 \times 1.5 = 34500\,\mathrm{W}$, which is option $3$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q015_3431460b_02112026.png?v=3431460ba597)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q015_3f2da260_02112026.png?v=3f2da2600e41)

---

## Q16

Physics · Electrostatics

The angle between the electric lines of force and the equipotential surface is

- (1) $0^\circ$
- (2) $45^\circ$
- **(3)** $90^\circ$
- (4) $180^\circ$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $dV = -\vec{E} \cdot d\vec{r}$
2. $dV = -E\,dr\cos\theta$
3. For equipotential surface,
4. $dV = 0$
5. $\cos\theta = 0$
6. $\Rightarrow \theta = 90^\circ$

**Solved independently** (answer withheld)

1. Along an equipotential surface $dV = -\vec{E}\cdot d\vec{l} = 0$, so $\vec{E} \perp d\vec{l}$ and the lines of force meet the surface at $90^\circ$, which is option $3$.

**Subtopic:** Equipotential Surfaces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q016_6f032941_02112026.png?v=6f032941a141)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q016_906ff99a_02112026.png?v=906ff99a270d)

---

## Q17

Physics · Modern Physics

When two monochromatic lights of frequency, $\nu$ and $\frac{\nu}{2}$ are incident on a photoelectric metal, their stopping potential becomes $\frac{V_s}{2}$ and $V_s$ respectively. The threshold frequency for this metal is

- (1) $2\nu$
- (2) $3\nu$
- (3) $\frac{2}{3}\nu$
- **(4)** $\frac{3}{2}\nu$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Since $k_{\max} = eV_s = h\nu - \phi$
2. $\frac{eV_S}{2} = h\nu - h\nu_0$ ...(i)
3. $eV_S = \frac{h\nu}{2} - h\nu_0$ ...(ii)
4. $\frac{1}{2}\left[\frac{h\nu}{2} - h\nu_0\right] = h\nu - h\nu_0$
5. $\Rightarrow h\nu_0 - \frac{h\nu_0}{2} = h\nu - \frac{h\nu}{4}$
6. $\Rightarrow \frac{h\nu_0}{2} = \frac{3h\nu}{4}$
7. $\nu_0 = \frac{3\nu}{2}$
8. * Language of question is wrongly framed. The values of stopping potentials should be interchanged.

**Solved independently** (answer withheld)

1. For frequency $\nu$: $e\frac{V_s}{2} = h\nu - h\nu_0$, so $eV_s = 2h\nu - 2h\nu_0$.
2. For frequency $\frac{\nu}{2}$: $eV_s = \frac{h\nu}{2} - h\nu_0$.
3. Equate: $2h\nu - 2h\nu_0 = \frac{h\nu}{2} - h\nu_0$.
4. $h\nu_0 = 2h\nu - \frac{h\nu}{2} = \frac{3}{2}h\nu$, so $\nu_0 = \frac{3}{2}\nu$, which is option $4$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q017_b97cb210_02112026.png?v=b97cb210d1bd)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q017_332808a8_02112026.png?v=332808a81df1)

---

## Q18

Physics · Magnetic Effect of Electric Current

A long solenoid of radius $1\,\mathrm{mm}$ has $100$ turns per $\mathrm{mm}$. If $1\,\mathrm{A}$ current flows in the solenoid, the magnetic field strength at the centre of the solenoid is

- (1) $6.28 \times 10^{-2}\,\mathrm{T}$
- **(2)** $12.56 \times 10^{-2}\,\mathrm{T}$
- (3) $12.56 \times 10^{-4}\,\mathrm{T}$
- (4) $6.28 \times 10^{-4}\,\mathrm{T}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. We know, magnetic field at centre of solenoid
2. $B = \mu_0 \frac{N}{\ell} I = \mu_0 n I \quad \left[n = \frac{N}{\ell}\right]$
3. $= 4\pi \times 10^{-7} \times 100 \times 10^{3} \times 1 \quad \left[n = \frac{100}{10^{-3}}\right]$
4. $= 4\pi \times 10^{-2}\,\mathrm{T}$
5. $B = 12.56 \times 10^{-2}\,\mathrm{T}$

**Solved independently** (answer withheld)

1. For a long solenoid the field inside is $B = \mu_0 n I$, independent of radius.
2. $n = 100\,\mathrm{mm^{-1}} = 10^{5}\,\mathrm{m^{-1}}$.
3. $B = 4\pi \times 10^{-7} \times 10^{5} \times 1 = 4\pi \times 10^{-2}\,\mathrm{T}$.
4. $4\pi \times 10^{-2} = 12.56 \times 10^{-2}\,\mathrm{T}$, which is option $2$.

**Subtopic:** Solenoid and Toroid · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q018_6af8f8b2_02112026.png?v=6af8f8b2abcf)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q018_65b83fcb_02112026.png?v=65b83fcbe5ef)

---

## Q19

Physics · Modern Physics

In the given nuclear reaction, the element $X$ is
$\mathrm{{}^{22}_{11}Na} \rightarrow X + e^{+} + \nu$

- (1) $\mathrm{{}^{23}_{11}Na}$
- (2) $\mathrm{{}^{23}_{10}Ne}$
- **(3)** $\mathrm{{}^{22}_{10}Ne}$
- (4) $\mathrm{{}^{22}_{12}Mg}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The nuclear reaction is given as
2. $\mathrm{{}^{22}_{11}Na} \rightarrow {}^{A}_{Z}X + {}_{+1}e^{0} + \nu$
3. From conservation of atomic number
4. $11 = Z + 1 \Rightarrow Z = 10 \Rightarrow \mathrm{Ne}$
5. From conservation of mass number
6. $22 = A + 0 \Rightarrow A = 22$
7. $\therefore\ {}^{A}_{Z}X = \mathrm{{}^{22}_{10}Ne}$

**Solved independently** (answer withheld)

1. Conserve mass number: $22 = A_X + 0 + 0 \Rightarrow A_X = 22$.
2. Conserve charge: $11 = Z_X + 1 + 0 \Rightarrow Z_X = 10$.
3. $Z = 10$ is neon, so $X = \mathrm{{}^{22}_{10}Ne}$, which is option $3$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q019_aca6e2a5_02112026.png?v=aca6e2a5573c)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q019_d0fcee88_02112026.png?v=d0fcee88ac29)

---

## Q20

Physics · Magnetic Effect of Electric Current

Given below are two statements
In light of above statements choose the most appropriate answer from the options given below

- (Statement I) Biot-Savart’s law gives us the expression for the magnetic field strength of an infinitesimal current element (Idl) of a current carrying conductor only.
- (Statement II) Biot-Savart’s law is analogous to Coulomb’s inverse square law of charge $q$, with the former being related to the field produced by a scalar source, Idl while the latter being produced by a vector source, $q$.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct and Statement II is incorrect
- (4) Statement I is incorrect and Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. According to Biot-Savart's law $d\vec{B} = \frac{\mu_0}{4\pi}\frac{Id\vec{l} \times \vec{r}}{r^3}$ which is applicable for infinitesimal element.
2. It is analogous to Coulomb's law, where $Id\vec{l}$ is vector source and electric field is produced by scalar source $q$.
3. Here statement I is correct and statement II is incorrect.

**Solved independently** (answer withheld)

1. Biot-Savart's law gives $d\vec{B} = \frac{\mu_0}{4\pi}\frac{I\,d\vec{l} \times \hat{r}}{r^2}$ for an infinitesimal current element $I\,d\vec{l}$, so Statement I is correct.
2. The source $I\,d\vec{l}$ is a vector, while the charge $q$ in Coulomb's law is a scalar; Statement II says the reverse, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect is option $3$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q020_e7c1038c_02112026.png?v=e7c1038ce2d5)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q020_148f39ef_02112026.png?v=148f39ef497c)

---

## Q21

Physics · Rotational Motion

The ratio of the radius of gyration of a thin uniform disc about an axis passing through its centre and normal to its plane to the radius of gyration of the disc about its diameter is

- (1) $2:1$
- **(2)** $\sqrt{2}:1$
- (3) $4:1$
- (4) $1:\sqrt{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A disc seen face-on with its axis normal to the plane (into the page) and a curved arrow showing rotation about it](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q021_sol_1_fd01c46a_02112026.png?v=fd01c46a8c22)

*A disc seen face-on with its axis normal to the plane (into the page) and a curved arrow showing rotation about it*

![drawn: A disc seen face-on with its axis normal to the plane (into the page) and a curved arrow showing rotation about it](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q021_solution_1_9bdc5146_02112026.svg?v=9bdc51461134)  
*drawn by code/lib/physics_figure.py*

1. $I_1 = \frac{MR^2}{2}$
2. $k_1 = \sqrt{\frac{I_1}{M}}$
3. $= \frac{R}{\sqrt{2}}$

![printed figure: A disc seen edge-on as a circle, with a vertical axis along its diameter and a curved rotation arrow at the top](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q021_sol_2_22839375_02112026.png?v=228393754af7)

*A disc seen edge-on as a circle, with a vertical axis along its diameter and a curved rotation arrow at the top*

![drawn: A disc seen edge-on as a circle, with a vertical axis along its diameter and a curved rotation arrow at the top](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q021_solution_2_633ecba3_02112026.svg?v=633ecba3b198)  
*drawn by code/lib/physics_figure.py*

4. $I_2 = \frac{MR^2}{4}$
5. $k_2 = \sqrt{\frac{I_2}{M}}$
6. $= \frac{R}{2}$
7. $\frac{k_1}{k_2} = \frac{\frac{R}{\sqrt{2}}}{\frac{R}{2}}$
8. $= \sqrt{2} : 1$

**Solved independently** (answer withheld)

1. For a thin uniform disc about the axis through the centre normal to its plane, $I_1 = \frac{MR^2}{2}$, so $k_1 = \sqrt{\frac{I_1}{M}} = \frac{R}{\sqrt{2}}$.
2. By the perpendicular axis theorem, $I_1 = 2I_d$, so $I_d = \frac{MR^2}{4}$.
3. Hence $k_2 = \sqrt{\frac{I_d}{M}} = \frac{R}{2}$.
4. $\frac{k_1}{k_2} = \frac{R/\sqrt{2}}{R/2} = \frac{2}{\sqrt{2}} = \sqrt{2}$, so the ratio is $\sqrt{2}:1$, which is option $2$.

**Subtopic:** Radius of Gyration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q021_d75ef9a8_02112026.png?v=d75ef9a84220)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q021_59323d41_02112026.png?v=59323d41c540)

---

## Q22

Physics · Alternating Current

The peak voltage of the ac source is equal to

- (1) The value of voltage supplied to the circuit
- (2) The rms value of the ac source
- **(3)** $\sqrt{2}$ times the rms value of the ac source
- (4) $1/\sqrt{2}$ times the rms value of the ac source

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know,
2. RMS value of A.C. $E_{\mathrm{rms}} = \frac{E_0}{\sqrt{2}}$
3. $E_0 = \sqrt{2}E_{\mathrm{rms}}$

**Solved independently** (answer withheld)

1. For a sinusoidal source, $V_{rms} = \frac{V_0}{\sqrt{2}}$, so $V_0 = \sqrt{2}\,V_{rms}$, which is option $3$.

**Subtopic:** RMS Voltage · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q022_2054202b_02112026.png?v=2054202b9d5a)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q022_3c819a18_02112026.png?v=3c819a18ddc6)

---

## Q23

Physics · Work, Energy and Power

The energy that will be ideally radiated by a $100\,\mathrm{kW}$ transmitter in $1\,\mathrm{hour}$ is

- **(1)** $36 \times 10^{7}\,\mathrm{J}$
- (2) $36 \times 10^{4}\,\mathrm{J}$
- (3) $36 \times 10^{5}\,\mathrm{J}$
- (4) $1 \times 10^{5}\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Energy $=$ Power $\times$ time
2. $E = 100 \times 10^{3} \times 3600$
3. $= 36 \times 10^{7}\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Energy radiated $E = P\,t$.
2. $P = 100\,\mathrm{kW} = 10^{5}\,\mathrm{W}$ and $t = 1\,\mathrm{h} = 3600\,\mathrm{s}$.
3. $E = 10^{5} \times 3600 = 3.6 \times 10^{8}\,\mathrm{J} = 36 \times 10^{7}\,\mathrm{J}$, which is option $1$.

**Subtopic:** Power · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q023_0d196c2d_02112026.png?v=0d196c2d84ef)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q023_f58b15f3_02112026.png?v=f58b15f3c3f8)

---

## Q24

Physics · Wave Optics

In a Young’s double slit experiment, a student observes 8 fringes in a certain segment of screen when a monochromatic light of $600\,\mathrm{nm}$ wavelength is used. If the wavelength of light is changed to $400\,\mathrm{nm}$, then the number of fringes he would observe in the same region of the screen is

- (1) 6
- (2) 8
- (3) 9
- **(4)** 12

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\beta = \frac{\lambda D}{d}$
2. Let length of segment of screen $= l$
3. $\Rightarrow l = 8\beta_1 = \frac{8\lambda_1 D}{d}$ ...(1)
4. and $l = n\beta_2 = \frac{n\lambda_2 D}{d}$ ...(2)
5. from (1) and (2)
6. $8\lambda_1 = n\lambda_2$
7. $8(600\,\mathrm{nm}) = n(400\,\mathrm{nm})$
8. $n = 12$

**Solved independently** (answer withheld)

1. Fringe width $\beta = \frac{\lambda D}{d}$, so $\beta \propto \lambda$.
2. For the same segment of length $L$, $L = n_1\beta_1 = n_2\beta_2$, so $n_1\lambda_1 = n_2\lambda_2$.
3. $n_2 = \frac{8 \times 600\,\mathrm{nm}}{400\,\mathrm{nm}} = 12$, which is option $4$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q024_2b35fa9c_02112026.png?v=2b35fa9c77d4)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q024_0612f7bc_02112026.png?v=0612f7bcc8ff)

---

## Q25

Physics · Electromagnetic Induction

A square loop of side $1\,\mathrm{m}$ and resistance $1\,\Omega$ is placed in a magnetic field of $0.5\,\mathrm{T}$. If the plane of loop is perpendicular to the direction of magnetic field, the magnetic flux through the loop is

- (1) $2\,\mathrm{weber}$
- **(2)** $0.5\,\mathrm{weber}$
- (3) $1\,\mathrm{weber}$
- (4) Zero weber

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Square loop of side 1 m with magnetic field perpendicular to its plane (dot at centre)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q025_sol_1_c143c888_02112026.png?v=c143c888e43f)

*Square loop of side 1 m with magnetic field perpendicular to its plane (dot at centre)*

![drawn: Square loop of side 1 m with magnetic field perpendicular to its plane (dot at centre)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q025_solution_1_1ec8de67_02112026.svg?v=1ec8de67f458)  
*drawn by code/lib/physics_figure.py*

1. Magnetic flux $(\phi_B) = \vec{B}\cdot\vec{A}$
2. $\vec{B}$ and $\vec{A}$ are in same direction, therefore
3. $\phi_B = B.A = 0.5 \times 1^{2}$
4. $= 0.5\,\mathrm{Wb}$

**Solved independently** (answer withheld)

1. Plane of loop perpendicular to $\vec B$ means the area vector is parallel to $\vec B$, so $\theta = 0^\circ$.
2. $A = (1\,\mathrm{m})^2 = 1\,\mathrm{m^2}$.
3. $\phi = BA\cos 0^\circ = 0.5 \times 1 \times 1 = 0.5\,\mathrm{Wb}$, which is option $2$.

**Subtopic:** Magnetic Flux · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q025_7892aa35_02112026.png?v=7892aa353274)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q025_c2ec099a_02112026.png?v=c2ec099ad53e)

---

## Q26

Physics · Current Electricity

Two resistors of resistance, $100\,\Omega$ and $200\,\Omega$ are connected in parallel in an electrical circuit. The ratio of the thermal energy developed in $100\,\Omega$ to that in $200\,\Omega$ in a given time is

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $1 : 4$
- (4) $4 : 1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For parallel combination
2. $P = \frac{V^2}{R}$
3. $\frac{P_1}{P_2} = \frac{R_2}{R_1}$
4. $\Rightarrow \frac{P_1}{P_2} = \frac{200}{100} = \frac{2}{1}$

**Solved independently** (answer withheld)

1. In a parallel connection both resistors have the same potential difference $V$.
2. Heat developed in time $t$ is $H = \frac{V^2 t}{R}$, so $H \propto \frac{1}{R}$.
3. $\frac{H_{100}}{H_{200}} = \frac{200\,\Omega}{100\,\Omega} = \frac{2}{1}$, which is option $2$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q026_78871770_02112026.png?v=78871770d954)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q026_73a7494e_02112026.png?v=73a7494e2caf)

---

## Q27

Physics · Kinematics

The ratio of the distances travelled by a freely falling body in the $1^{\text{st}}$, $2^{\text{nd}}$, $3^{\text{rd}}$ and $4^{\text{th}}$ second

- (1) $1:2:3:4$
- (2) $1:4:9:16$
- **(3)** $1:3:5:7$
- (4) $1:1:1:1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $S_{n^{\text{th}}} = u + \frac{1}{2}a(2n - 1)$
2. $S_{1^{\text{st}}} = \frac{1}{2}g(2 \times 1 - 1) = \frac{g}{2}$
3. $S_{2^{\text{nd}}} = \frac{1}{2}g(2 \times 2 - 1) = 3\left(\frac{1}{2}g\right)$
4. $S_{3^{\text{rd}}} = \frac{1}{2}g(2 \times 3 - 1) = 5 \times \left(\frac{1}{2}g\right)$
5. $S_{4^{\text{th}}} = \frac{1}{2}g(2 \times 4 - 1) = 7 \times \left(\frac{1}{2}g\right)$
6. $S_{1^{\text{st}}} : S_{2^{\text{nd}}} : S_{3^{\text{rd}}} : S_{4^{\text{th}}} = 1 : 3 : 5 : 7$

**Solved independently** (answer withheld)

1. For a body starting from rest ($u=0$), distance in the $n^{\text{th}}$ second is $s_n = u + \frac{g}{2}(2n-1) = \frac{g}{2}(2n-1)$.
2. For $n=1,2,3,4$: $s_1=\frac{g}{2}$, $s_2=\frac{3g}{2}$, $s_3=\frac{5g}{2}$, $s_4=\frac{7g}{2}$.
3. Ratio $s_1:s_2:s_3:s_4 = 1:3:5:7$, which is option $3$.

**Subtopic:** Galileo's Law of Odd Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q027_341096cd_02112026.png?v=341096cd0591)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q027_cf8d8824_02112026.png?v=cf8d8824fa2a)

---

## Q28

Physics · Gravitation

A body of mass $60\,\mathrm{g}$ experiences a gravitational force of $3.0\,\mathrm{N}$, when placed at a particular point. The magnitude of the gravitational field intensity at that point is

- (1) $0.05\,\mathrm{N/kg}$
- **(2)** $50\,\mathrm{N/kg}$
- (3) $20\,\mathrm{N/kg}$
- (4) $180\,\mathrm{N/kg}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $F = mE_{G}$
2. $3 = \frac{60}{1000}E_{G}$
3. $E_{G} = 50\,\mathrm{N/kg}$

**Solved independently** (answer withheld)

1. Convert mass: $m = 60\,\mathrm{g} = 0.060\,\mathrm{kg}$.
2. Gravitational field intensity is force per unit mass: $E = \frac{F}{m}$.
3. $E = \frac{3.0\,\mathrm{N}}{0.060\,\mathrm{kg}} = 50\,\mathrm{N/kg}$, which is option $2$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q028_24289081_02112026.png?v=24289081d8bf)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q028_3a1623bb_02112026.png?v=3a1623bb79a9)

---

## Q29

Physics · Ray Optics

A light ray falls on a glass surface of refractive index $\sqrt{3}$ , at an angle $60^\circ$. The angle between the refracted and reflected rays would be

- (1) $30^\circ$
- (2) $60^\circ$
- **(3)** $90^\circ$
- (4) $120^\circ$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Given $i = 60^\circ$ and $\mu = \sqrt{3}$
2. $\Rightarrow$ Here, angle of incidence $\Rightarrow i = \tan^{-1}(\mu)$
3. Hence, reflected and refracted rays would be perpendicular to each other.

**Solved independently** (answer withheld)

1. Snell's law: $\sin 60^\circ = \sqrt{3}\,\sin r$.
2. $\sin r = \frac{\sqrt{3}/2}{\sqrt{3}} = \frac{1}{2}$, so $r = 30^\circ$.
3. The reflected ray makes $60^\circ$ with the normal on the incident side; the refracted ray makes $30^\circ$ with the normal on the other side.
4. Angle between them $= 180^\circ - 60^\circ - 30^\circ = 90^\circ$, which is option $3$ (consistent with Brewster's law, $\tan 60^\circ = \sqrt{3}$).

**Subtopic:** Snell's Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q029_3eda572f_02112026.png?v=3eda572fe161)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q029_b0be840b_02112026.png?v=b0be840bbacd)

---

## Q30

Physics · Electromagnetic Waves

When light propagates through a material medium of relative permittivity $\varepsilon_r$ and relative permeability $\mu_r$, the velocity of light, $v$ is given by ($c$-velocity of light in vacuum)

- (1) $v = c$
- (2) $v = \sqrt{\dfrac{\mu_r}{\varepsilon_r}}$
- (3) $v = \sqrt{\dfrac{\varepsilon_r}{\mu_r}}$
- **(4)** $v = \dfrac{c}{\sqrt{\varepsilon_r \mu_r}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $v = \frac{1}{\sqrt{\varepsilon_m \mu_m}}$
2. $v = \frac{1}{\sqrt{\varepsilon_0 \varepsilon_r \mu_0 \mu_r}}$
3. Since $c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}$
4. $\Rightarrow v = \frac{c}{\sqrt{\varepsilon_r \mu_r}}$

**Solved independently** (answer withheld)

1. In a medium, $v = \frac{1}{\sqrt{\mu \varepsilon}}$ with $\mu = \mu_0 \mu_r$ and $\varepsilon = \varepsilon_0 \varepsilon_r$.
2. $v = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \cdot \frac{1}{\sqrt{\mu_r \varepsilon_r}}$.
3. Since $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, $v = \frac{c}{\sqrt{\varepsilon_r \mu_r}}$, which is option $4$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q030_a4c1001a_02112026.png?v=a4c1001adf5a)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q030_ba2c7c65_02112026.png?v=ba2c7c65feb9)

---

## Q31

Physics · Electrostatics

Two hollow conducting spheres of radii $R_1$ and $R_2$ $(R_1 >> R_2)$ have equal charges. The potential would be

- (1) More on bigger sphere
- **(2)** More on smaller sphere
- (3) Equal on both the spheres
- (4) Dependent on the material property of the sphere

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Potential of conducting hollow sphere $= \frac{KQ}{R}$
2. Now, $Q$ = same
3. $\Rightarrow V \propto \frac{1}{R} \Rightarrow$ more the radius less will be the potential.
4. $\Rightarrow$ Hence potential would be more on smaller sphere

**Solved independently** (answer withheld)

1. For a charged hollow conducting sphere, the potential is $V = \frac{kQ}{R}$.
2. With equal charges, $V \propto \frac{1}{R}$.
3. Since $R_1 \gg R_2$, $V_2 = \frac{kQ}{R_2} > V_1 = \frac{kQ}{R_1}$, so the potential is more on the smaller sphere, which is option $2$.

**Subtopic:** Potential Due to Linear and Surface Charge Distribution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q031_563f6435_02112026.png?v=563f64350888)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q031_2560f4e5_02112026.png?v=2560f4e5a4c8)

---

## Q32

Physics · Current Electricity

A copper wire of length $10\,\mathrm{m}$ and radius $\left(\frac{10^{-2}}{\sqrt{\pi}}\right)\,\mathrm{m}$ has electrical resistance of $10\,\Omega$. The current density in the wire for an electric field strength of $10\,(\mathrm{V/m})$ is

- (1) $10^{4}\,\mathrm{A/m^{2}}$
- (2) $10^{6}\,\mathrm{A/m^{2}}$
- (3) $10^{-5}\,\mathrm{A/m^{2}}$
- **(4)** $10^{5}\,\mathrm{A/m^{2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Resistance, $R = \rho\frac{L}{A} = \frac{L}{\sigma A}$
2. $\Rightarrow \sigma = \frac{L}{RA}$
3. Also current density $j = \sigma E = \frac{LE}{RA}$
4. $j = \frac{10 \times 10}{10 \times \pi\left(\frac{10^{-2}}{\sqrt{\pi}}\right)^{2}} = \frac{100}{10 \times \pi \times \left(\frac{10^{-4}}{\pi}\right)}$
5. $= 10^{5}\,\mathrm{A/m^{2}}$

**Solved independently** (answer withheld)

1. Cross-sectional area: $A = \pi r^2 = \pi \left(\frac{10^{-2}}{\sqrt{\pi}}\right)^2 = 10^{-4}\,\mathrm{m^2}$.
2. Resistivity: $\rho = \frac{RA}{l} = \frac{10 \times 10^{-4}}{10} = 10^{-4}\,\Omega\,\mathrm{m}$.
3. Current density: $J = \sigma E = \frac{E}{\rho} = \frac{10}{10^{-4}} = 10^{5}\,\mathrm{A/m^2}$, which is option $4$.

**Subtopic:** Current Density, Resistivity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q032_72eac28b_02112026.png?v=72eac28b2a17)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q032_aef8977c_02112026.png?v=aef8977c41d0)

---

## Q33

Physics · Kinematics

The displacement-time graphs of two moving particles make angles of $30^\circ$ and $45^\circ$ with the $x$-axis as shown in the figure. The ratio of their respective velocity is

![printed figure: Displacement-time graphs of two particles at 30 and 45 degrees to the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q033_0411033b_02112026.png?v=0411033b751b)

*Displacement-time graphs of two particles at 30 and 45 degrees to the time axis*

![drawn: Displacement-time graphs of two particles at 30 and 45 degrees to the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q033_question_3c44a8b3_02112026.svg?v=3c44a8b3f346)  
*drawn by code/lib/physics_figure.py*

- (1) $\sqrt{3}:1$
- (2) $1:1$
- (3) $1:2$
- **(4)** $1:\sqrt{3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Slope of $x$-$t$ curves gives the velocity
2. $\Rightarrow$ Ratio $= \frac{\tan 30^\circ}{\tan 45^\circ} = \frac{\frac{1}{\sqrt{3}}}{1} = 1 : \sqrt{3}$

**Solved independently** (answer withheld)

1. Velocity equals the slope of the displacement-time graph, $v = \tan\theta$.
2. $\frac{v_1}{v_2} = \frac{\tan 30^\circ}{\tan 45^\circ}$.
3. $\frac{1/\sqrt{3}}{1} = 1:\sqrt{3}$, which is option $4$.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q033_f2bda5ad_02112026.png?v=f2bda5ade2f5)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q033_a9f5aa28_02112026.png?v=a9f5aa289761)

---

## Q34

Physics · Units and Measurements

Plane angle and solid angle have

- **(1)** Units but no dimensions
- (2) Dimensions but no units
- (3) No units and no dimensions
- (4) Both units and dimensions

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Plane angle $= \frac{\text{Arc}}{\text{Radius}} = \frac{[\mathrm{L}]}{[\mathrm{L}]} \longrightarrow$ Unit $=$ Radian
2. $= [\mathrm{M^{0}L^{0}T^{0}}]$
3. Solid angle $= \frac{\text{Area}}{(\text{Radius})^{2}} \longrightarrow$ Unit $=$ Steradian
4. $= \frac{\mathrm{L^{2}}}{\mathrm{L^{2}}} = [\mathrm{M^{0}L^{0}T^{0}}]$
5. $\therefore$ Both have units but no dimensions

**Solved independently** (answer withheld)

1. Plane angle $\theta = \frac{\text{arc}}{r}$ has dimensions $\frac{[L]}{[L]} = [M^0L^0T^0]$ but unit radian (rad).
2. Solid angle $\Omega = \frac{A}{r^2}$ has dimensions $\frac{[L^2]}{[L^2]} = [M^0L^0T^0]$ but unit steradian (sr).
3. So both have units but no dimensions, which is option $1$.

**Subtopic:** SI Units and Prefixes, Dimensional Formulae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q034_1b897ef4_02112026.png?v=1b897ef4be27)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q034_ac990506_02112026.png?v=ac99050698a2)

---

## Q35

Physics · Modern Physics

Let $T_1$ and $T_2$ be the energy of an electron in the first and second excited states of hydrogen atoms, respectively. According to the Bohr’s model of an atom, the ratio $T_1 : T_2$ is

- (1) $1 : 4$
- (2) $4 : 1$
- (3) $4 : 9$
- **(4)** $9 : 4$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $E_n = \frac{E_0}{n^2}$, For first excited state $\Rightarrow n = 2$
2. For second excited state $\Rightarrow n = 3$
3. $\Rightarrow \frac{T_1}{T_2} = \frac{\frac{E_0}{4}}{\frac{E_0}{9}} = \frac{9}{4}$

**Solved independently** (answer withheld)

1. The first excited state is $n=2$ and the second excited state is $n=3$.
2. In Bohr's model $E_n = -\frac{13.6}{n^2}\,\text{eV}$, so $E_n \propto \frac{1}{n^2}$.
3. $\frac{T_1}{T_2} = \frac{1/2^2}{1/3^2} = \frac{9}{4}$.
4. $T_1 : T_2 = 9 : 4$, which is option $4$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q035_d755c902_02112026.png?v=d755c902a599)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q035_11a08b28_02112026.png?v=11a08b283bf8)

---

## Q36

Physics · Units and Measurements

Match List-I with List-II
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | Gravitational constant ($G$) | (i) | $[\mathrm{L^{2}T^{-2}}]$ |
| (b) | Gravitational potential energy | (ii) | $[\mathrm{M^{-1}L^{3}T^{-2}}]$ |
| (c) | Gravitational potential | (iii) | $[\mathrm{LT^{-2}}]$ |
| (d) | Gravitational intensity | (iv) | $[\mathrm{ML^{2}T^{-2}}]$ |

- (1) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii)
- **(2)** (a) - (ii), (b) - (iv), (c) - (i), (d) - (iii)
- (3) (a) - (ii), (b) - (iv), (c) - (iii), (d) - (i)
- (4) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (a) $[G] = \frac{Fr^{2}}{m_{1}m_{2}}$
2. $[G] = \frac{Fr^{2}}{m_{1}m_{2}} = \frac{[\mathrm{MLT^{-2}}]\,\mathrm{L^{2}}}{[\mathrm{MM}]} = [\mathrm{M^{-1}L^{3}T^{-2}}]$
3. (b) Gravitational potential energy $= [\mathrm{ML^{2}T^{-2}}]$
4. (c) Gravitational potential $= \frac{\mathrm{PE}}{m} = [\mathrm{L^{2}T^{-2}}]$
5. (d) Gravitational field intensity $= \frac{F}{m} = [\mathrm{LT^{-2}}]$

**Solved independently** (answer withheld)

1. $G = \frac{F r^2}{m_1 m_2} \Rightarrow [G] = \frac{[\mathrm{MLT^{-2}}][\mathrm{L^2}]}{[\mathrm{M^2}]} = [\mathrm{M^{-1}L^{3}T^{-2}}]$, so (a) - (ii).
2. Gravitational potential energy is an energy: $[U] = [\mathrm{ML^{2}T^{-2}}]$, so (b) - (iv).
3. Gravitational potential is energy per unit mass: $[V] = \frac{[\mathrm{ML^{2}T^{-2}}]}{[\mathrm{M}]} = [\mathrm{L^{2}T^{-2}}]$, so (c) - (i).
4. Gravitational intensity is force per unit mass: $[I] = \frac{[\mathrm{MLT^{-2}}]}{[\mathrm{M}]} = [\mathrm{LT^{-2}}]$, so (d) - (iii).
5. The match (a)-(ii), (b)-(iv), (c)-(i), (d)-(iii) is option $2$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q036_47887165_02112026.png?v=47887165825d)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q036_1983d6e5_02112026.png?v=1983d6e569f3)

---

## Q37

Physics · Oscillations

Two pendulums of length $121\,\mathrm{cm}$ and $100\,\mathrm{cm}$ start vibrating in phase. At some instant, the two are at their mean position in the same phase. The minimum number of vibrations of the shorter pendulum after which the two are again in phase at the mean position is:

- **(1)** 11
- (2) 9
- (3) 10
- (4) 8

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. The smallest whole-number solution is $n = 11$, $m = 10$, so the shorter pendulum makes $11$ vibrations, which is option $1$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q037_877022eb_02112026.png?v=877022ebf7e7)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q037_b06a331b_02112026.png?v=b06a331b0e03)

---

## Q38

Physics · Units and Measurements

The area of a rectangular field (in $\mathrm{m^2}$) of length $55.3\,\mathrm{m}$ and breadth $25\,\mathrm{m}$ after rounding off the value for correct significant digits is

- (1) $138 \times 10^{1}$
- (2) $1382$
- (3) $1382.5$
- **(4)** $14 \times 10^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Area $=$ Length $\times$ Breadth
2. $= 55.3 \times 25\,\mathrm{m^2}$
3. $= 1382.5\,\mathrm{m^2}$
4. $= 14 \times 10^{2}\,\mathrm{m^2}$ (Rounding off of two significant figures)

**Solved independently** (answer withheld)

1. $A = l \times b = 55.3\,\mathrm{m} \times 25\,\mathrm{m} = 1382.5\,\mathrm{m^2}$.
2. In multiplication the result keeps as many significant figures as the factor with the fewest: $55.3$ has 3, $25$ has 2, so keep 2.
3. Rounding $1382.5$ to 2 significant figures gives $1.4 \times 10^{3} = 14 \times 10^{2}\,\mathrm{m^2}$, which is option $4$.

**Subtopic:** Significant Figures · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q038_62c68e7d_02112026.png?v=62c68e7d69a7)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q038_d20899e9_02112026.png?v=d20899e974e5)

---

## Q39

Physics · Kinematics

A ball is projected with a velocity, $10\,\mathrm{ms^{-1}}$, at an angle of $60^\circ$ with the vertical direction. Its speed at the highest point of its trajectory will be

- (1) Zero
- **(2)** $5\sqrt{3}\,\mathrm{ms^{-1}}$
- (3) $5\,\mathrm{ms^{-1}}$
- (4) $10\,\mathrm{ms^{-1}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. At highest point vertical component of velocity become zero.

![printed figure: Ball projected at 10 m/s at 60 degrees to the vertical (30 degrees to the horizontal); velocity 10cos30° at the highest point](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q039_sol_1_75bcfee3_02112026.png?v=75bcfee33728)

*Ball projected at 10 m/s at 60 degrees to the vertical (30 degrees to the horizontal); velocity 10cos30° at the highest point*

![drawn: Ball projected at 10 m/s at 60 degrees to the vertical (30 degrees to the horizontal); velocity 10cos30° at the highest point](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q039_solution_1_7a4fde7b_02112026.svg?v=7a4fde7b72b1)  
*drawn by code/lib/physics_figure.py*

2. At highest point speed of object $= 10\cos 30^\circ$
3. $= 5\sqrt{3}\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. At the highest point the vertical velocity is zero, so the speed equals the horizontal component $u_x$.
2. The angle $60^\circ$ is with the vertical, so $u_x = u\sin 60^\circ$.
3. $u_x = 10 \times \frac{\sqrt{3}}{2} = 5\sqrt{3}\,\mathrm{ms^{-1}}$, which is option $2$.

**Subtopic:** Projectile Motion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q039_5420f012_02112026.png?v=5420f012640e)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q039_979f8981_02112026.png?v=979f89814f9c)

---

## Q40

Physics · Semiconductor Electronics

The truth table for the given logic circuit is

![printed figure: Two NAND gates (one input of the lower fed through a NOT from A, B crossing to the upper) feeding an AND gate with output C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q040_1941a81a_02112026.png?v=1941a81af889)

*Two NAND gates (one input of the lower fed through a NOT from A, B crossing to the upper) feeding an AND gate with output C*

![drawn: Two NAND gates (one input of the lower fed through a NOT from A, B crossing to the upper) feeding an AND gate with output C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q040_question_d583dfcf_02112026.svg?v=d583dfcfb56a)  
*drawn by code/lib/physics_figure.py*

- (1) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (2) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$
- **(3)** $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (4) $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $C = \left(\overline{A \cdot B}\right) \cdot \left(\overline{\bar{A} \cdot B}\right)$
2. $\Rightarrow C = \overline{A \cdot B + \bar{A} \cdot B}$
3. $\Rightarrow C = \overline{\left(A + \bar{A}\right)B}$
4. $\Rightarrow C = \bar{B}$
5. The truth table would be
6. $\begin{array}{cc|c} A & B & C \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$

![printed figure: A and B into a NAND; NOT A and B into a second NAND; both NAND outputs into an AND giving C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q040_sol_1_32d1a47e_02112026.png?v=32d1a47eb1e7)

*A and B into a NAND; NOT A and B into a second NAND; both NAND outputs into an AND giving C*

![drawn: A and B into a NAND; NOT A and B into a second NAND; both NAND outputs into an AND giving C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q040_solution_1_468e4945_02112026.svg?v=468e4945472a)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. From the figure, the top NAND gate takes inputs $A$ and $B$, so its output is $\overline{AB}$.
2. The bottom NAND gate takes $\bar{A}$ (through the NOT gate) and $B$, so its output is $\overline{\bar{A}B}$.
3. The AND gate gives $C = \overline{AB}\cdot\overline{\bar{A}B} = (\bar{A}+\bar{B})(A+\bar{B})$.
4. $(\bar{A}+\bar{B})(A+\bar{B}) = \bar{B} + A\bar{A} = \bar{B}$.
5. So $C = 1, 0, 1, 0$ for $AB = 00, 01, 10, 11$, which is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q040_acf64068_02112026.png?v=acf640680026)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q040_cc9c1c65_02112026.png?v=cc9c1c658a0c)

---

## Q41

Physics · Magnetic Effect of Electric Current

From Ampere’s circuital law for a long straight wire of circular cross-section carrying a steady current, the variation of magnetic field in the inside and outside region of the wire is

- (1) Uniform and remains constant for both the regions.
- (2) A linearly increasing function of distance upto the boundary of the wire and then linearly decreasing for the outside region.
- **(3)** A linearly increasing function of distance $r$ upto the boundary of the wire and then decreasing one with $\frac{1}{r}$ dependence for the outside region.
- (4) A linearly decreasing function of distance upto the boundary of the wire and then a linearly increasing one for the outside region.

**Answer** — booklet: (3) · independent solve: (3) · agree

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
4. Linear increase inside, $\frac{1}{r}$ decrease outside, which is option $3$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q041_974e3f5a_02112026.png?v=974e3f5aebc6)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q041_3e9c4b2c_02112026.png?v=3e9c4b2cff79)

---

## Q42

Physics · Alternating Current

A series LCR circuit with inductance $10\,\mathrm{H}$, capacitance $10\,\mu\mathrm{F}$, resistance $50\,\Omega$ is connected to an ac source of voltage, $V = 200\sin(100t)$ volt. If the resonant frequency of the LCR circuit is $\nu_0$ and the frequency of the ac source is $\nu$, then

- (1) $\nu_0 = \nu = 50\,\mathrm{Hz}$
- **(2)** $\nu_0 = \nu = \frac{50}{\pi}\,\mathrm{Hz}$
- (3) $\nu_0 = \frac{50}{\pi}\,\mathrm{Hz}$, $\nu = 50\,\mathrm{Hz}$
- (4) $\nu = 100\,\mathrm{Hz}$; $\nu_0 = \frac{100}{\pi}\,\mathrm{Hz}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\omega L = \frac{1}{\omega C}$
2. $\omega = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10 \times 10 \times 10^{-6}}}$
3. $\omega = 100$
4. $\omega = 2\pi f \Rightarrow f = \frac{\omega}{2\pi}$
5. $\nu_0 = f_0 = \frac{100}{2\pi} = \frac{50}{\pi}\,\mathrm{Hz}$, $\omega = 100$
6. $\nu = f = \frac{100}{2\pi} = \frac{50}{\pi}$

**Solved independently** (answer withheld)

1. $LC = 10\,\mathrm{H} \times 10 \times 10^{-6}\,\mathrm{F} = 10^{-4}\,\mathrm{s^2}$.
2. $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10^{-4}}} = 100\,\mathrm{rad/s}$.
3. $\nu_0 = \frac{\omega_0}{2\pi} = \frac{100}{2\pi} = \frac{50}{\pi}\,\mathrm{Hz}$.
4. From $V = 200\sin(100t)$, the source $\omega = 100\,\mathrm{rad/s}$, so $\nu = \frac{100}{2\pi} = \frac{50}{\pi}\,\mathrm{Hz}$.
5. $\nu_0 = \nu = \frac{50}{\pi}\,\mathrm{Hz}$, which is option $2$.

**Subtopic:** Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q042_2903fba9_02112026.png?v=2903fba9857f)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q042_02d66885_02112026.png?v=02d66885bd3a)

---

## Q43

Physics · Electrostatics

Two point charges $-q$ and $+q$ are placed at a distance of $L$, as shown in the figure. The magnitude of electric field intensity at a distance $R (R >> L)$ varies as:

![printed figure: Point charges -q and +q separated by distance L](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q043_7d11b1c3_02112026.png?v=7d11b1c358b4)

*Point charges -q and +q separated by distance L*

![drawn: Point charges -q and +q separated by distance L](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q043_question_6252b906_02112026.svg?v=6252b906019f)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{1}{R^{2}}$
- **(2)** $\frac{1}{R^{3}}$
- (3) $\frac{1}{R^{4}}$
- (4) $\frac{1}{R^{6}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For $R >> L$, arrangement is an electric dipole
2. $E = \frac{2p}{4\pi\varepsilon_0 R^{3}}$; where $p = qL$
3. $E \propto \frac{1}{R^{3}}$

**Solved independently** (answer withheld)

1. The charges $-q$ and $+q$ separated by $L$ form an electric dipole with moment $p = qL$.
2. For $R \gg L$, the dipole field at any point is $E = \frac{kp}{R^{3}}\sqrt{3\cos^{2}\theta + 1}$.
3. Hence $E \propto \frac{1}{R^{3}}$, which is option $2$.

**Subtopic:** Electric Field Due to Electric Dipole · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q043_a9f81476_02112026.png?v=a9f81476269f)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q043_8e6d25e0_02112026.png?v=8e6d25e0db49)

---

## Q44

Physics · Mechanical Properties of Solids

Given below are two statements : One is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the most appropriate answer from the options given below

- Assertion (A) The stretching of a spring is determined by the shear modulus of the material of the spring.
- Reason (R) A coil spring of copper has more tensile strength than a steel spring of same dimensions.

- (1) Both (A) and (R) are true and (R) is the correct explanation of (A)
- (2) Both (A) and (R) are true and (R) is not the correct explanation of (A)
- **(3)** (A) is true but (R) is false
- (4) (A) is false but (R) is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. It is true that stretching of spring is determined by shear modulus of the spring as when coil spring is stretched neither its length nor its volume changes, there is only change in its shape.
2. Tensile strength of steel is more than that of copper.
3. Hence Assertion is true and reason is false.

**Solved independently** (answer withheld)

1. When a coil spring is stretched, the wire of the spring is twisted, so its extension is governed by the shear (rigidity) modulus $G$: Assertion (A) is true.
2. Steel has a larger elastic modulus and tensile strength than copper ($Y_{steel} > Y_{Cu}$), so a copper spring is not stronger than a steel spring of the same dimensions: Reason (R) is false.
3. (A) true and (R) false corresponds to option $3$.

**Subtopic:** Shear Modulus of Rigidity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q044_61522513_02112026.png?v=61522513cfab)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q044_262e14d8_02112026.png?v=262e14d8e140)

---

## Q45

Physics · Electromagnetic Induction

A big circular coil of $1000$ turns and average radius $10\,\mathrm{m}$ is rotating about its horizontal diameter at $2\,\mathrm{rad\,s^{-1}}$. If the vertical component of earth’s magnetic field at that place is $2 \times 10^{-5}\,\mathrm{T}$ and electrical resistance of the coil is $12.56\,\Omega$, then the maximum induced current in the coil will be

- (1) $0.25\,\mathrm{A}$
- (2) $1.5\,\mathrm{A}$
- **(3)** $1\,\mathrm{A}$
- (4) $2\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\phi_{B} = NBA\cos\omega t$
2. $\varepsilon = \frac{-d\phi_{B}}{dt} = -NBA\omega(-\sin\omega t)$
3. $\varepsilon = NBA\omega\sin\omega t$
4. $i_{\mathrm{max}} = \frac{\varepsilon_{\mathrm{max}}}{R} = \frac{NBA\omega}{R}$
5. $= \frac{1000 \times 2 \times 10^{-5} \times \pi(10)^{2} \times 2}{12.56}$
6. $= 1\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Rotating about a horizontal diameter, the flux through the coil comes from the vertical component $B_V = 2\times10^{-5}\,\mathrm{T}$.
2. $A = \pi r^2 = \pi (10)^2 = 100\pi \approx 314\,\mathrm{m^2}$.
3. $\varepsilon_{max} = N B_V A \omega = 1000 \times 2\times10^{-5} \times 100\pi \times 2 = 4\pi \approx 12.56\,\mathrm{V}$.
4. $I_{max} = \frac{\varepsilon_{max}}{R} = \frac{12.56}{12.56} = 1\,\mathrm{A}$, which is option $3$.

**Subtopic:** AC Generator · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q045_908c2ee1_02112026.png?v=908c2ee1c790)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q045_c62fe789_02112026.png?v=c62fe789afa1)

---

## Q46

Physics · Thermodynamics

The volume occupied by the molecules contained in $4.5\,\mathrm{kg}$ water at STP, if the intermolecular forces vanish away is

- (1) $5.6 \times 10^{6}\,\mathrm{m^{3}}$
- (2) $5.6 \times 10^{3}\,\mathrm{m^{3}}$
- (3) $5.6 \times 10^{-3}\,\mathrm{m^{3}}$
- **(4)** $5.6\,\mathrm{m^{3}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. From ideal gas equation
2. $PV = nRT$
3. $\left[n = \frac{\text{mass of water}}{\text{mol. wt.}} = \frac{4.5 \times 10^{3}}{18}\right]$
4. $V = \frac{nRT}{P}$
5. At. STP $\Rightarrow T = 273\,\mathrm{K}$
6. $P = 10^{5}\,\mathrm{N/m^{2}}$
7. $V = \frac{4.5 \times 10^{3}}{18} \times \frac{8.3 \times 273}{10^{5}} = 5.66\,\mathrm{m^{3}}$

**Solved independently** (answer withheld)

1. If the intermolecular forces vanish, the molecules behave as an ideal gas, so at STP one mole occupies $22.4\,\mathrm{L}$.
2. $n = \frac{4500\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 250\,\mathrm{mol}$.
3. $V = 250 \times 22.4\,\mathrm{L} = 5600\,\mathrm{L}$.
4. $5600\,\mathrm{L} = 5600 \times 10^{-3}\,\mathrm{m^{3}} = 5.6\,\mathrm{m^{3}}$, which is option $4$.

**Subtopic:** Ideal Gas Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q046_54e0f95f_02112026.png?v=54e0f95fbdd1)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q046_1e03ee65_02112026.png?v=1e03ee65f388)

---

## Q47

Physics · Capacitance

A capacitor of capacitance $C = 900\,\mathrm{pF}$ is charged fully by $100\,\mathrm{V}$ battery $B$ as shown in figure (a). Then it is disconnected from the battery and connected to another uncharged capacitor of capacitance $C = 900\,\mathrm{pF}$ as shown in figure (b). The electrostatic energy stored by the system (b) is

![printed figure: (a) Capacitor C charged by 100 V battery B; (b) charged C connected across an uncharged C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q047_eb7c19b3_02112026.png?v=eb7c19b347f9)

*(a) Capacitor C charged by 100 V battery B; (b) charged C connected across an uncharged C*

![drawn: (a) Capacitor C charged by 100 V battery B; (b) charged C connected across an uncharged C](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q047_question_0421ece7_02112026.svg?v=0421ece75abd)  
*drawn by code/lib/physics_figure.py*

- (1) $4.5 \times 10^{-6}\,\mathrm{J}$
- (2) $3.25 \times 10^{-6}\,\mathrm{J}$
- **(3)** $2.25 \times 10^{-6}\,\mathrm{J}$
- (4) $1.5 \times 10^{-6}\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $q_1 = CV$
2. $= 900 \times 10^{-12} \times 100$
3. $= 9 \times 10^{-8}\,C$

![printed figure: Charged capacitor C with plate charges and 100 V across its open leads](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q047_sol_1_5da6abfc_02112026.png?v=5da6abfc4547)

*Charged capacitor C with plate charges and 100 V across its open leads*

![drawn: Charged capacitor C with plate charges and 100 V across its open leads](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q047_solution_1_59b98139_02112026.svg?v=59b9813954ff)  
*drawn by code/lib/physics_figure.py*

4. $V = \frac{C_1V_1 + C_2V_2}{C_1 + C_2}$
5. $= \frac{9 \times 10^{-8} + 0}{1800 \times 10^{-12}} = \frac{100}{2} = 50\,\mathrm{V}$
6. $U = \frac{1}{2}(C_1 + C_2)V^2$
7. $= \frac{1}{2} \times 1800 \times 10^{-12} \times 50 \times 50$
8. $= 225 \times 10^{-8}$
9. $U = 2.25 \times 10^{-6}\,\mathrm{J}$

![printed figure: Charged capacitor C connected across an identical capacitor C in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q047_sol_2_7c5b3b3f_02112026.png?v=7c5b3b3fd47b)

*Charged capacitor C connected across an identical capacitor C in one loop*

![drawn: Charged capacitor C connected across an identical capacitor C in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q047_solution_2_4ee96185_02112026.svg?v=4ee96185df9a)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Initial charge: $Q = CV = 900\times10^{-12} \times 100 = 9\times10^{-8}\,\mathrm{C}$.
2. On connecting to an identical uncharged capacitor, charge is conserved and shared: $V_{common} = \frac{Q}{2C} = \frac{9\times10^{-8}}{1800\times10^{-12}} = 50\,\mathrm{V}$.
3. Energy of system (b): $U = \frac{1}{2}(2C)V_{common}^2 = \frac{1}{2}(1800\times10^{-12})(50)^2$.
4. $U = 2.25\times10^{-6}\,\mathrm{J}$, which is option $3$ (half the initial $4.5\times10^{-6}\,\mathrm{J}$).

**Subtopic:** Redistribution of Charges, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q047_961e0c49_02112026.png?v=961e0c49a265)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q047_47a31223_02112026.png?v=47a31223bd75)

---

## Q48

Physics · Current Electricity

A wheatstone bridge is used to determine the value of unknown resistance $X$ by adjusting the variable resistance $Y$ as shown in the figure. For the most precise measurement of $X$, the resistances $P$ and $Q$

![printed figure: Wheatstone bridge with P, Q, X, variable Y, galvanometer G and cell E](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q048_fc9c3de2_02112026.png?v=fc9c3de27a68)

*Wheatstone bridge with P, Q, X, variable Y, galvanometer G and cell E*

![drawn: Wheatstone bridge with P, Q, X, variable Y, galvanometer G and cell E](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q048_question_267f0673_02112026.svg?v=267f06732537)  
*drawn by code/lib/physics_figure.py*

- (1) Should be approximately equal to $2X$
- **(2)** Should be approximately equal and are small
- (3) Should be very large and unequal
- (4) Do not play any significant role

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. We know, a wheatstone bridge is said to be most precise when it is most sensitive.
2. This can be done by making ratio arms equal.
3. Thus (2) is correct option.

**Solved independently** (answer withheld)

1. At balance $\frac{P}{Q} = \frac{X}{Y}$, so $X = \frac{P}{Q}Y$.
2. Galvanometer sensitivity is greatest when all four arms are of the same order, $P \approx Q \approx X \approx Y$.
3. So $P$ and $Q$ should be approximately equal and comparable to (small, like) $X$; very large or unequal values reduce sensitivity, and they clearly matter.
4. This matches option $2$.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q048_afc3fc8c_02112026.png?v=afc3fc8cdbfc)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q048_e6fe1b20_02112026.png?v=e6fe1b2047bb)

---

## Q49

Physics · Ray Optics

Two transparent media $A$ and $B$ are separated by a plane boundary. The speed of light in those media are $1.5 \times 10^{8}\,\mathrm{m/s}$ and $2.0 \times 10^{8}\,\mathrm{m/s}$, respectively. The critical angle for a ray of light for these two media is

- (1) $\sin^{-1}(0.500)$
- **(2)** $\sin^{-1}(0.750)$
- (3) $\tan^{-1}(0.500)$
- (4) $\tan^{-1}(0.750)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Ray in medium A meeting the boundary with B at the critical angle and grazing along the boundary](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q049_sol_1_7421b940_02112026.png?v=7421b94002cb)

*Ray in medium A meeting the boundary with B at the critical angle and grazing along the boundary*

![drawn: Ray in medium A meeting the boundary with B at the critical angle and grazing along the boundary](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q049_solution_1_862ccb09_02112026.svg?v=862ccb0962b3)  
*drawn by code/lib/physics_figure.py*

1. $\mu_A = \frac{3 \times 10^{8}}{1.5 \times 10^{8}} = 2$
2. $\mu_B = \frac{3 \times 10^{8}}{2 \times 10^{8}} = 1.5$
3. For TIR, ray of light should travel from denser to rarer medium
4. $\mu_A \sin\theta_C = \mu_B \sin 90^\circ$
5. $2 \sin\theta_C = 1.5 \sin 90^\circ$
6. $\sin\theta_C = 0.75$
7. $\theta_C = \sin^{-1}(0.75)$

**Solved independently** (answer withheld)

1. Light is slower in $A$ ($1.5 \times 10^{8}\,\mathrm{m/s}$) than in $B$ ($2.0 \times 10^{8}\,\mathrm{m/s}$), so $A$ is the denser medium and total internal reflection happens for light going from $A$ to $B$.
2. $\sin C = \frac{n_B}{n_A}$.
3. $\frac{n_B}{n_A} = \frac{c/v_B}{c/v_A} = \frac{v_A}{v_B}$.
4. $\sin C = \frac{1.5 \times 10^{8}}{2.0 \times 10^{8}} = 0.750$.
5. $C = \sin^{-1}(0.750)$, which is option $2$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q049_3acb9cfa_02112026.png?v=3acb9cfa1437)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q049_d47e163e_02112026.png?v=d47e163e6c63)

---

## Q50

Physics · Modern Physics

A nucleus of mass number 189 splits into two nuclei having mass number 125 and 64. The ratio of radius of two daughter nuclei respectively is

- (1) $1 : 1$
- (2) $4 : 5$
- **(3)** $5 : 4$
- (4) $25 : 16$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Radius of nuclei with mass number $A$ varies as
2. $R = R_0 A^{1/3}$
3. $\frac{R_1}{R_2} = \left(\frac{125}{64}\right)^{1/3} = \frac{5}{4} = 5 : 4$

**Solved independently** (answer withheld)

1. Nuclear radius $R = R_0 A^{1/3}$.
2. $\frac{R_1}{R_2} = \left(\frac{125}{64}\right)^{1/3}$.
3. $\left(\frac{125}{64}\right)^{1/3} = \frac{5}{4}$, so the ratio is $5:4$, which is option $3$.

**Subtopic:** Distance of Closest Approach and Size of Nucleus · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q050_88a8b3b7_02112026.png?v=88a8b3b77e4f)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q050_3ceb5fa0_02112026.png?v=3ceb5fa0d8a9)

---

## Q51

Chemistry · physical · Thermodynamics

Which of the following p-V curve represents maximum work done?

- (1) ![printed figure: p-V graph labelled Isothermal: a closed elliptical cycle tilted downward from upper left to lower right, with arrows marking the direction around the loop (p on the vertical axis, V on the horizontal axis)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q051_option_1_b806231d_03112026.png?v=b806231d285d) *p-V graph labelled Isothermal: a closed elliptical cycle tilted downward from upper left to lower right, with arrows marking the direction around the loop (p on the vertical axis, V on the horizontal axis)*
- **(2)** ![printed figure: p-V graph labelled Isothermal: pressure constant, then a curve falling as V increases, then a vertical drop to the V axis (p on the vertical axis, V on the horizontal axis)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q051_option_2_e7a877c0_03112026.png?v=e7a877c0e022) *p-V graph labelled Isothermal: pressure constant, then a curve falling as V increases, then a vertical drop to the V axis (p on the vertical axis, V on the horizontal axis)*
- (3) ![printed figure: p-V graph labelled Isothermal: a vertical line at constant V (p on the vertical axis, V on the horizontal axis)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q051_option_3_5fdda57f_03112026.png?v=5fdda57f0292) *p-V graph labelled Isothermal: a vertical line at constant V (p on the vertical axis, V on the horizontal axis)*
- (4) ![printed figure: p-V graph labelled Isothermal: pressure constant, then a steep curve falling over a narrow range of V, then a vertical drop to the V axis (p on the vertical axis, V on the horizontal axis)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2022/2022_Q1/figures_agent/q051_option_4_2316bd3a_03112026.png?v=2316bd3ac64a) *p-V graph labelled Isothermal: pressure constant, then a steep curve falling over a narrow range of V, then a vertical drop to the V axis (p on the vertical axis, V on the horizontal axis)*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Work done under any thermodynamic process can be determined by area under the ‘$p$-$V$’ graph.
2. As it can be observed maximum area is covered in option ‘2’.

![printed figure: 1. p-V graph: a closed elliptical cycle with its enclosed area hatched](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q051_sol_1_fb264468_02112026.png?v=fb264468db00)

*1. p-V graph: a closed elliptical cycle with its enclosed area hatched*


![printed figure: 2. p-V graph: constant pressure, then a falling curve, then a vertical drop; the area under the curve is hatched and marked Maximum area](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q051_sol_2_cacc41ec_02112026.png?v=cacc41ec7985)

*2. p-V graph: constant pressure, then a falling curve, then a vertical drop; the area under the curve is hatched and marked Maximum area*


![printed figure: 3. p-V graph: a vertical line at constant V; w = 0](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q051_sol_3_62809ec8_02112026.png?v=62809ec84868)

*3. p-V graph: a vertical line at constant V; w = 0*


![printed figure: 4. p-V graph: constant pressure, then a steep falling curve over a narrow range of V, then a vertical drop; a small area under the curve is hatched](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q051_sol_4_85cbdcd0_02112026.png?v=85cbdcd02ed7)

*4. p-V graph: constant pressure, then a steep falling curve over a narrow range of V, then a vertical drop; a small area under the curve is hatched*


**Solved independently** (answer withheld)

1. Work done by a gas is $W = \int p\,dV$, which is the area under the $p$-$V$ curve.
2. Option $3$ is a vertical line, so $dV = 0$ and $W = 0$.
3. Option $1$ is a small closed loop, so the net work equals the small area enclosed by the loop.
4. Option $4$ covers only a small volume range, so the area under it is small.
5. Option $2$ has a similar shape spread over a much larger volume range, so it encloses the largest area and represents maximum work, which is option $2$.

**Subtopic:** Work Done · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q051_44fa49f6_02112026.png?v=44fa49f6c6f9)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q051_630e1ae7_02112026.png?v=630e1ae7e117)

---

## Q52

Chemistry · inorganic · The p–Block Elements

Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the most appropriate answer from the options given below:

- Assertion (A) $\mathrm{ICl}$ is more reactive than $\mathrm{I_2}$.
- Reason (R) $\mathrm{I{-}Cl}$ bond is weaker than $\mathrm{I{-}I}$ bond.

- **(1)** Both (A) and (R) are correct and (R) is the correct explanation of (A).
- (2) Both (A) and (R) are correct but (R) is not the correct explanation of (A).
- (3) (A) is correct but (R) is not correct
- (4) (A) is not correct but (R) is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In general, interhalogen compounds are more reactive than halogens (except fluorine).
2. This is because $\mathrm{X-X'}$ bond in interhalogens is weaker than $\mathrm{X-X}$ bond in halogens excepts $\mathrm{F-F}$ bond.
3. Therefore $\mathrm{I{-}Cl}$ is more reactive than $\mathrm{I_2}$ because of weaker $\mathrm{I{-}Cl}$ bond then $\mathrm{I{-}I}$ bond.

**Solved independently** (answer withheld)

1. NCERT teaches that interhalogen compounds are generally more reactive than the parent halogens (except $\mathrm{F_2}$), so $\mathrm{ICl}$ is more reactive than $\mathrm{I_2}$: (A) is correct.
2. NCERT gives the reason as the $\mathrm{X{-}X'}$ bond in interhalogens being weaker than the $\mathrm{X{-}X}$ bond in halogens, so (R) is correct and explains (A), which is option $1$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q052_1a53b474_02112026.png?v=1a53b4749152)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q052_7eec44b3_02112026.png?v=7eec44b3deb5)

---

## Q53

Chemistry · organic · General Organic Chemistry

Which compound amongst the following is **not** an aromatic compound?

- (1) cyclopenta-2,4-dien-1-ide `c1cc[cH-]c1` ![cyclopenta-2,4-dien-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_option_1_s1_8e072b02_02112026.svg?v=8e072b023b03)
- (2) cyclohepta-2,4,6-trien-1-ylium `c1ccc[cH+]cc1` ![cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_option_2_s1_64faace2_02112026.svg?v=64faace2872e)
- (3) cycloprop-2-en-1-ylium `c1c[cH+]1` ![cycloprop-2-en-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_option_3_s1_2a7002fa_02112026.svg?v=2a7002fa2056)
- **(4)** cyclohepta-1,3,5-triene `C1=CC=CCC=C1` ![cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_option_4_s1_ff78e6c0_02112026.svg?v=ff78e6c0c934)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Planar, cyclic, conjugated species containing $(4n + 2)\pi$ electrons will be aromatic in nature ($n$ is an integer)

![printed figure: cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q053_sol_1_9aed7fb0_02112026.png?v=9aed7fb0b33e)

*cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium*

![drawn: cycloprop-2-en-1-ylium, cyclopenta-2,4-dien-1-ide and cyclohepta-2,4,6-trien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_solution_1_2aa827a3_02112026.svg?v=2aa827a335e6)  
*drawn by RDKit (code/lib/chem_cards.py)*

2. [figure], [figure] and [figure] are aromatic species

![printed figure: cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q053_sol_2_7b387ea0_02112026.png?v=7b387ea02ee4)

*cyclohepta-1,3,5-triene*

![drawn: cyclohepta-1,3,5-triene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q053_solution_2_c1d981d7_02112026.svg?v=c1d981d73a89)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. [figure] is not an aromatic compound

**Solved independently** (answer withheld)

1. Option $1$, cyclopentadienyl anion $C_5H_5^-$: planar, fully conjugated, $6\,\pi$ electrons $= 4n+2$ with $n=1$, so aromatic.
2. Option $2$, tropylium (cycloheptatrienyl) cation $C_7H_7^+$: planar, fully conjugated, $6\,\pi$ electrons $= 4n+2$ with $n=1$, so aromatic.
3. Option $3$, cyclopropenyl cation $C_3H_3^+$: planar, fully conjugated, $2\,\pi$ electrons $= 4n+2$ with $n=0$, so aromatic.
4. Option $4$, cycloheptatriene $C_7H_8$: contains one $sp^3$ $CH_2$ carbon, so cyclic conjugation is broken and it is non-aromatic.
5. The compound that is not aromatic is option $4$.

**Subtopic:** Aromaticity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q053_46697e30_02112026.png?v=46697e30e0cd)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q053_ed5a0ab1_02112026.png?v=ed5a0ab1b332)

---

## Q54

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The IUPAC name of an element with atomic number 119 is

- **(1)** ununennium
- (2) unnilennium
- (3) unununnium
- (4) ununoctium

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. IUPAC name of element : $119$ : ununennium

**Solved independently** (answer withheld)

1. IUPAC numerical roots: $0$ = nil, $1$ = un, $9$ = enn, $8$ = oct.
2. Atomic number $119$ has digits $1, 1, 9$, giving roots un + un + enn.
3. Add the suffix -ium: ununennium, which is option $1$.

**Subtopic:** Nomenclature of Elements with Atomic Numbers Greater Than 100 · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q054_6d4c535b_02112026.png?v=6d4c535b1ab7)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q054_be392db7_02112026.png?v=be392db7646a)

---

## Q55

Chemistry · organic · Chemistry in Everyday Life

Match List-I with List-II.
List-I (Drug class) | List-II (Drug molecule)
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Antacids | (i) | Salvarsan |
| (b) | Antihistamines | (ii) | Morphine |
| (c) | Analgesics | (iii) | Cimetidine |
| (d) | Antimicrobials | (iv) | Seldane |

- (1) (a) - (iii), (b) – (ii), (c) – (iv), (d) – (i)
- **(2)** (a) - (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (3) (a) - (i), (b) – (iv), (c) – (ii), (d) – (iii)
- (4) (a) - (iv), (b) – (iii), (c) – (i), (d) – (ii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Cimetidine is an antacid
2. Seldane is an antihistamine
3. Morphine is an analgesic
4. Salvarsan is an antimicrobial drug

**Solved independently** (answer withheld)

1. Antacids: cimetidine reduces acid secretion, so $(a) \rightarrow (iii)$.
2. Antihistamines: Seldane (terfenadine) is an antihistamine, so $(b) \rightarrow (iv)$.
3. Analgesics: morphine is a narcotic analgesic, so $(c) \rightarrow (ii)$.
4. Antimicrobials: salvarsan (arsphenamine) is used against syphilis, so $(d) \rightarrow (i)$.
5. The match $(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)$ is option $2$.

**Subtopic:** Therapeutic Action of Different Classes of Drugs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q055_650edc48_02112026.png?v=650edc48ad80)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q055_d5be609e_02112026.png?v=d5be609e0a7f)

---

## Q56

Chemistry · inorganic · Hydrogen

Match List-I with List-II. Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{MgH_2}$ | (i) | Electron precise |
| (b) | $\mathrm{GeH_4}$ | (ii) | Electron deficient |
| (c) | $\mathrm{B_2H_6}$ | (iii) | Electron rich |
| (d) | $\mathrm{HF}$ | (iv) | Ionic |

- **(1)** (a) – (iv), (b) – (i), (c) – (ii), (d) – (iii)
- (2) (a) – (iii), (b) – (i), (c) – (ii), (d) – (iv)
- (3) (a) – (i), (b) – (ii), (c) – (iv), (d) – (iii)
- (4) (a) – (ii), (b) – (iii), (c) – (iv), (d) – (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. List – I (Hydrides) → List – II (Nature)
2. (a) $\mathrm{MgH_2}$ → Ionic
3. (b) $\mathrm{GeH_4}$ → Electron precise
4. (c) $\mathrm{B_2H_6}$ → Electron deficient
5. (d) $\mathrm{HF}$ → Electron rich
6. (a) – (iv), (b) – (i), (c) – (ii), (d) – (iii)

**Solved independently** (answer withheld)

1. $\mathrm{MgH_2}$ is a saline (ionic) hydride of an s-block metal, so (a) – (iv).
2. $\mathrm{GeH_4}$ is a group 14 molecular hydride with exactly enough electrons for its bonds, so it is electron precise: (b) – (i).
3. $\mathrm{B_2H_6}$ is a group 13 hydride with too few electrons for normal two-centre bonds, so it is electron deficient: (c) – (ii).
4. $\mathrm{HF}$ has lone pairs on F beyond those used in bonding, so it is electron rich: (d) – (iii).
5. The match (a)–(iv), (b)–(i), (c)–(ii), (d)–(iii) is option $1$.

**Subtopic:** Hydrides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q056_3d0985a3_02112026.png?v=3d0985a3cf77)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q056_a9b67cb4_02112026.png?v=a9b67cb43c1f)

---

## Q57

Chemistry · organic · Biomolecules

The incorrect statement regarding enzymes is

- (1) Enzymes are biocatalysts.
- (2) Like chemical catalysts enzymes reduce the activation energy of bio processes.
- **(3)** Enzymes are polysaccharides.
- (4) Enzymes are very specific for a particular reaction and substrate.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Enzymes are complex nitrogenous organic compounds which are produced by living plants and animals.
2. They are protein molecules of high molecular mass.
3. They are not polysaccharides.

**Solved independently** (answer withheld)

1. Enzymes are biocatalysts, reduce activation energy and are highly specific, so options $1$, $2$ and $4$ are correct; enzymes are proteins, not polysaccharides, so the incorrect statement is option $3$.

**Subtopic:** Enzymes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q057_0e7bddc7_02112026.png?v=0e7bddc7be0f)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q057_5fdd284c_02112026.png?v=5fdd284cb8b1)

---

## Q58

Chemistry · inorganic · Coordination Compounds – Practice

The IUPAC name of the complex- $\mathrm{[Ag(H_2O)_2][Ag(CN)_2]}$ is:

- (1) dicyanidosilver(II) diaquaargentate(II)
- (2) diaquasilver(II) dicyanidoargentate(II)
- (3) dicyanidosilver(I) diaquaargentate(I)
- **(4)** diaquasilver(I) dicyanidoargentate(I)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{[Ag(H_2O)_2][Ag(CN)_2]}$
2. IUPAC name : diaquasilver(I)dicyanidoargentate(I)

**Solved independently** (answer withheld)

1. The salt splits into the cation $[\mathrm{Ag(H_2O)_2}]^{+}$ and the anion $[\mathrm{Ag(CN)_2}]^{-}$; the cation is named first.
2. Cation: $x + 2(0) = +1 \Rightarrow x = +1$, so it is diaquasilver(I).
3. Anion: $x + 2(-1) = -1 \Rightarrow x = +1$, and an anionic complex of Ag takes the name argentate, so it is dicyanidoargentate(I).
4. Full name: diaquasilver(I) dicyanidoargentate(I), which is option $4$.

**Subtopic:** IUPAC Nomenclature and Formulae of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q058_5b17f15e_02112026.png?v=5b17f15e2643)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q058_239a370d_02112026.png?v=239a370d28c5)

---

## Q59

Chemistry · inorganic · The D- and F-Block Elements – Practice

Gadolinium has a low value of third ionisation enthalpy because of

- (1) small size
- **(2)** high exchange enthalpy
- (3) high electronegativity
- (4) high basic character

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Electronic configuration of Gadolinium
2. $\mathrm{Gd}$ :— $[\mathrm{Xe}]\,4f^{7}\,5d^{1}\,6s^{2}$
3. In case of $3^{\mathrm{rd}}$ ionisation enthalpy electron will be removed from $5d$ and resultant configuration will be $[\mathrm{Xe}]4f^{7}$ that is stable electronic configuration as it will have high exchange energy, hence less energy will be required to remove $3^{\mathrm{rd}}$ electron.

**Solved independently** (answer withheld)

1. Gd ($Z=64$) has configuration $[\mathrm{Xe}]\,4f^7 5d^1 6s^2$.
2. After two ionisations, $\mathrm{Gd^{2+}} = [\mathrm{Xe}]\,4f^7 5d^1$.
3. The third ionisation removes the $5d^1$ electron, giving $\mathrm{Gd^{3+}} = [\mathrm{Xe}]\,4f^7$, a half-filled $4f$ subshell.
4. The half-filled $4f^7$ state is stabilised by high exchange enthalpy, so $\Delta_i H_3$ is low, which is option $2$.

**Subtopic:** Ionisation Enthalpies, Formation of Coloured Ions & Formation of Complex Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q059_2d6ad96a_02112026.png?v=2d6ad96adfbe)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q059_e7f38a7d_02112026.png?v=e7f38a7d398b)

---

## Q60

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Amongst the following which one will have maximum ‘lone pair - lone pair’ electron repulsions?

- (1) $\mathrm{CIF_3}$
- (2) $\mathrm{IF_5}$
- (3) $\mathrm{SF_4}$
- **(4)** $\mathrm{XeF_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{SF_4} \rightarrow sp^{3}d + 1$ lone pair

![printed figure: sulfur tetrafluoride ($\ce{SF4}$): S bonded to four F with one lone pair drawn on S (see-saw shape)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q060_sol_1_8e4b6229_02112026.png?v=8e4b622962b2)

*sulfur tetrafluoride ($\ce{SF4}$): S bonded to four F with one lone pair drawn on S (see-saw shape)*

2. $\mathrm{XeF_2} \rightarrow sp^{3}d + 3$ lone pair

![printed figure: xenon difluoride ($\ce{XeF2}$): F-Xe-F linear with three lone pairs drawn on Xe](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q060_sol_2_d00c9e26_02112026.png?v=d00c9e26481b)

*xenon difluoride ($\ce{XeF2}$): F-Xe-F linear with three lone pairs drawn on Xe*

3. $\mathrm{ClF_3} \rightarrow sp^{3}d + 2$ lone pair

![printed figure: chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F with two lone pairs drawn on Cl (T-shape)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q060_sol_3_563cf92b_02112026.png?v=563cf92b11bb)

*chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F with two lone pairs drawn on Cl (T-shape)*

4. $\mathrm{IF_5} \rightarrow sp^{3}d^{2} + 1$ lone pair

![printed figure: iodine pentafluoride ($\ce{IF5}$): I bonded to five F with one lone pair drawn on I (square pyramidal)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q060_sol_4_7406ab4c_02112026.png?v=7406ab4ccadf)

*iodine pentafluoride ($\ce{IF5}$): I bonded to five F with one lone pair drawn on I (square pyramidal)*

5. $\mathrm{XeF_2}$ having maximum lone pairs, so, it has maximum ‘lone pair-lone pair’ electron repulsions.

**Solved independently** (answer withheld)

1. Count lone pairs on the central atom: $\mathrm{ClF_3}$: $\frac{7-3}{2} = 2$; $\mathrm{IF_5}$: $\frac{7-5}{2} = 1$; $\mathrm{SF_4}$: $\frac{6-4}{2} = 1$; $\mathrm{XeF_2}$: $\frac{8-2}{2} = 3$.
2. With only $1$ lone pair, $\mathrm{IF_5}$ and $\mathrm{SF_4}$ have no lp-lp repulsion.
3. $\mathrm{ClF_3}$ has $2$ equatorial lone pairs, i.e. $1$ lp-lp interaction.
4. $\mathrm{XeF_2}$ has $3$ equatorial lone pairs, i.e. $3$ lp-lp interactions, the maximum, which is option $4$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q060_e70ee571_02112026.png?v=e70ee5713ad5)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q060_475a09b6_02112026.png?v=475a09b6c0c0)

---

## Q61

Chemistry · inorganic · The p–Block Elements

Which of the following statement is not correct about diborane?

- (1) There are two 3-centre-2-electron bonds.
- (2) The four terminal $\mathrm{B-H}$ bonds are two centre two electron bonds.
- (3) The four terminal Hydrogen atoms and the two Boron atoms lie in one plane.
- **(4)** Both the Boron atoms are $sp^{2}$ hybridised.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Each boron atoms in diborane uses $sp^{3}$ hybrid orbitals for bonding.

![printed figure: diborane ($\ce{B2H6}$): two B atoms, each with two terminal H, joined by two bridging H (banana bonds); arrows point to both B atoms labelled sp³ hybridised](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q061_sol_1_26799b0b_02112026.png?v=26799b0bf28c)

*diborane ($\ce{B2H6}$): two B atoms, each with two terminal H, joined by two bridging H (banana bonds); arrows point to both B atoms labelled sp³ hybridised*


**Solved independently** (answer withheld)

1. In $\mathrm{B_2H_6}$ there are two bridging $\mathrm{B-H-B}$ bonds, each a 3-centre-2-electron bond, so option $1$ is correct.
2. The four terminal $\mathrm{B-H}$ bonds are ordinary 2-centre-2-electron bonds, so option $2$ is correct.
3. The four terminal H atoms and the two B atoms lie in one plane, with the bridging H atoms above and below it, so option $3$ is correct.
4. Each B uses four orbitals (two terminal and two bridging bonds), so B is $sp^{3}$ hybridised, not $sp^{2}$; option $4$ is the incorrect statement.

**Subtopic:** Important compounds of Boranes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q061_306c82ac_02112026.png?v=306c82ac18a3)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q061_5301ca6a_02112026.png?v=5301ca6aa0a6)

---

## Q62

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the given below

- (Statement I) The boiling points of aldehydes and ketones are higher than hydrocarbons of comparable molecular masses because of weak molecular association in aldehydes and ketones due to dipole - dipole interactions.
- (Statement II) The boiling points of aldehydes and ketones are lower than the alcohols of similar molecular masses due to the absence of H-bonding.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The boiling points of aldehydes and ketones are higher than hydrocarbons of comparable molecular masses due to weak molecular association in aldehydes and ketones arising out of the dipole - dipole interaction.
2. Alcohols involved intermolecular hydrogen bonding, because of which the boiling point of aldehydes and ketones are lower than the alcohols of similar molecular masses.

**Solved independently** (answer withheld)

1. Statement I: the polar $C=O$ group gives weak intermolecular association via dipole-dipole interactions, so aldehydes and ketones boil higher than hydrocarbons of comparable molecular mass; Statement I is correct.
2. Statement II: aldehydes and ketones lack $O-H$ and cannot form intermolecular H-bonds, so they boil lower than alcohols of similar molecular mass; Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q062_1a7911f6_02112026.png?v=1a7911f6db7e)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q062_ab56cfe5_02112026.png?v=ab56cfe595d2)

---

## Q63

Chemistry · physical · The Solid State

Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the most appropriate answer from the options given below:

- Assertion (A) In a particular point defect, an ionic solid is electrically neutral, even if few of its cations are missing from its unit cells.
- Reason (R) In an ionic solid, Frenkel defect arises due to dislocation of cation from its lattice site to interstitial site, maintaining overall electrical neutrality.

- (1) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- **(2)** Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- (3) (A) is correct but (R) is not correct
- (4) (A) is not correct but (R) is correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Assertion statement is classic explanation of Schottky defect in which cation and anion leaves their site, or impurity defect.
2. Reason statement is true but not correct explanation as it is defining Frenkel defect in which ion does not leave crystal.

**Solved independently** (answer withheld)

1. In a Schottky defect, equal numbers of cations and anions are missing, so the ionic solid stays electrically neutral even though some cations are missing: (A) is correct.
2. In a Frenkel defect, a cation leaves its lattice site and occupies an interstitial site; the charge is unchanged, so neutrality is maintained: (R) is correct.
3. In a Frenkel defect no cation is lost from the crystal, so (R) does not explain why a solid with missing cations is neutral: (R) is not the correct explanation of (A).
4. Both correct, (R) not the explanation, which is option $2$.

**Subtopic:** Imperfections in Solids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q063_9a59f0c7_02112026.png?v=9a59f0c77c71)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q063_fab21fbd_02112026.png?v=fab21fbdbfad)

---

## Q64

Chemistry · inorganic · The p–Block Elements

Given below are two statements In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The boiling points of the following hydrides of group 16 elements increases in the order – $\mathrm{H_2O} < \mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te}$
- (Statement II) The boiling points of these hydrides increase with increase in molar mass.

- (1) Both Statement I and Statement II are correct
- **(2)** Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Compound — Boiling point $(\mathrm{K})$
2. $\mathrm{H_2O}$ — $373$
3. $\mathrm{H_2S}$ — $213$
4. $\mathrm{H_2Se}$ — $232$
5. $\mathrm{H_2Te}$ — $269$
6. The boiling points of these hybrids not exactly increases with increase in molar mass.
7. $\mathrm{H_2O}$ has maximum boiling point due to intermolecular hydrogen bonding.

**Solved independently** (answer withheld)

1. Among group 16 hydrides, $\mathrm{H_2O}$ forms extensive intermolecular hydrogen bonds, giving it the highest boiling point (373 K).
2. Actual order: $\mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te} < \mathrm{H_2O}$, so Statement I ($\mathrm{H_2O} < \mathrm{H_2S} < \ldots$) is incorrect.
3. $\mathrm{H_2O}$ has the lowest molar mass yet the highest boiling point, so the boiling points of these hydrides do not increase with molar mass; Statement II is incorrect.
4. Both statements incorrect, which is option $2$.

**Subtopic:** Important Compounds & their Hydrides & Oxides Group 16 · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q064_cdc1322f_02112026.png?v=cdc1322fc2cb)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q064_b3a10a98_02112026.png?v=b3a10a98f05c)

---

## Q65

Chemistry · physical · Chemical Kinetics

The given graph is a representation of kinetics of a reaction. The $y$ and $x$ axes for zero and first order reactions, respectively are

![printed figure: graph of y against x at constant temperature T: a horizontal straight line parallel to the x axis (y constant as x changes)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q065_fd757693_02112026.png?v=fd757693365f)

*graph of y against x at constant temperature T: a horizontal straight line parallel to the x axis (y constant as x changes)*

- (1) zero order ($y$ = concentration and $x$ = time), first order ($y$ = $t_{\frac{1}{2}}$ and $x$ = concentration)
- (2) zero order ($y$ = concentration and $x$ = time), first order ($y$ = rate constant and $x$ = concentration)
- **(3)** zero order ($y$ = rate and $x$ = concentration), first order ($y$ = $t_{\frac{1}{2}}$ and $x$ = concentration)
- (4) zero order ($y$ = rate and $x$ = concentration), first order ($y$ = rate and $x$ = $t_{\frac{1}{2}}$)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For zero order reaction
2. $r = k[\mathrm{A}]^{0}$
3. $r = k$ (constant)
4. hence, '$y$' as 'rate' and '$x$' as concentration will give desired graph.
5. For first order reaction
6. $t_{\frac{1}{2}} = \frac{0.693}{k}$ (constant)
7. hence, '$y$' as '$t_{\frac{1}{2}}$' and '$x$' as concentration will give desired graph.

**Solved independently** (answer withheld)

1. The graph is a horizontal line, so $y$ stays constant as $x$ changes.
2. Zero order: $\text{rate} = k[A]^0 = k$, so rate vs concentration is a horizontal line.
3. First order: $t_{1/2} = \frac{0.693}{k}$, independent of $[A]_0$, so $t_{1/2}$ vs concentration is a horizontal line.
4. Concentration vs time for zero order is a falling straight line, not horizontal, which rules out options $1$ and $2$; rate constant vs concentration is also constant but option $2$ fails on the zero-order part; option $4$ gives first-order rate vs $t_{1/2}$, which is not the standard plot. So the answer is option $3$.

**Subtopic:** Zero Order Reactions, First Order Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q065_62c9eb3d_02112026.png?v=62c9eb3d2f53)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q065_fbf1aaae_02112026.png?v=fbf1aaaec3c3)

---

## Q66

Chemistry · organic · Isomerism in Organic Compounds

The incorrect statement regarding chirality is

- (1) $\mathrm{S_N1}$ reaction yields $1:1$ mixture of both enantiomers
- (2) The product obtained by $\mathrm{S_N2}$ reaction of haloalkane having chirality at the reactive site shows inversion of configuration
- **(3)** Enantiomers are superimposable mirror images on each other
- (4) A racemic mixture shows zero optical rotation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The stereoisomers related to each other as non-superimposable mirror image are called enantiomers.

**Solved independently** (answer withheld)

1. Enantiomers are, by definition, non-superimposable mirror images of each other, so option $3$ is incorrect.
2. Options $1$ (SN1 gives racemisation, $1:1$ mixture as NCERT teaches), $2$ (SN2 backside attack gives inversion) and $4$ (racemic mixture has zero net rotation) are correct, so the answer is option $3$.

**Subtopic:** Optical Isomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q066_3b194ef8_02112026.png?v=3b194ef8ca4b)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q066_615d1a50_02112026.png?v=615d1a500596)

---

## Q67

Chemistry · organic · Haloalkanes and Haloarenes

Which of the following sequence of reactions is suitable to synthesize chlorobenzene?

- **(1)** Benzene, $\mathrm{Cl_2}$, anhydrous $\mathrm{FeCl_3}$
- (2) Phenol, $\mathrm{NaNO_2}$, $\mathrm{HCl}$, $\mathrm{CuCl}$
- (3) benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q067_option_3_s1_dbf27a87_02112026.svg?v=dbf27a872e50) — , $\mathrm{HCl}$
- (4) aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q067_option_4_s1_ac26c148_02112026.svg?v=ac26c1483d05) — , $\mathrm{HCl}$, Heating

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: 1. benzene + $\ce{Cl2}$ →(anhydrous FeCl3) chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q067_sol_1_dd1aa418_02112026.png?v=dd1aa4180877)

*1. benzene + $\ce{Cl2}$ →[anhydrous FeCl3] chlorobenzene*

![drawn: 1. benzene + $\ce{Cl2}$ →(anhydrous FeCl3) chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q067_solution_1_4e9d403e_02112026.svg?v=4e9d403e4e96)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Benzene reacts with chlorine in presence of anhydrous $\mathrm{FeCl_3}$ to give chlorobenzene

**Solved independently** (answer withheld)

1. Benzene with $\mathrm{Cl_2}$ and anhydrous $\mathrm{FeCl_3}$ undergoes electrophilic substitution: $\mathrm{C_6H_6 + Cl_2 \xrightarrow{FeCl_3} C_6H_5Cl + HCl}$, giving chlorobenzene.
2. Phenol does not form a diazonium salt with $\mathrm{NaNO_2/HCl}$ (that needs a primary aromatic amine), so option $2$ fails.
3. Benzene does not react with $\mathrm{HCl}$ alone, so option $3$ fails.
4. Aniline with $\mathrm{HCl}$ on heating only forms anilinium chloride, not chlorobenzene (no diazotisation), so option $4$ fails.
5. Hence the suitable sequence is option $1$.

**Subtopic:** Preparation of Haloarenes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q067_ec83fa02_02112026.png?v=ec83fa020c4f)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q067_32ab8515_02112026.png?v=32ab85150568)

---

## Q68

Chemistry · physical · Structure of Atom

Identify the incorrect statement from the following.

- (1) All the five $5d$ orbitals are different in size when compared to the respective $4d$ orbitals.
- (2) All the five $4d$ orbitals have shapes similar to the respective $3d$ orbitals.
- (3) In an atom, all the five $3d$ orbitals are equal in energy in free state.
- **(4)** The shapes of $d_{xy}$, $d_{yz}$ and $d_{zx}$ orbitals are similar to each other; and $d_{x^2-y^2}$ and $d_{z^2}$ are similar to each other.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In an atom, all the five $3d$ orbitals are equal in energy in free state i.e., degenerate.
2. The shape of $d_{x^2-y^2}$ is different then shape of $d_{z^2}$

![printed figure: orbital shape diagrams: $d_{x^2-y^2}$ orbital (four lobes along the x and y axes) and $d_{z^2}$ orbital (two lobes along the z axis with a ring in the xy plane), each drawn on x, y axes](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q068_sol_1_15579d72_02112026.png?v=15579d729a79)

*orbital shape diagrams: $d_{x^2-y^2}$ orbital (four lobes along the x and y axes) and $d_{z^2}$ orbital (two lobes along the z axis with a ring in the xy plane), each drawn on x, y axes*

3. The size of orbital depends on principal quantum number 'n' therefore all the five $3d$ orbitals are different in size when compared to the respective $4d$ orbitals.
4. Shape of orbitals depends on azimuthal quantum number 'l' therefore shapes of $4d$ orbitals are similar to the respective $3d$ orbitals.

**Solved independently** (answer withheld)

1. Options 1, 2 and 3 are correct: $5d$ orbitals are larger than $4d$, $4d$ and $3d$ orbitals have the same shapes, and the five $3d$ orbitals are degenerate in a free atom.
2. $d_{xy}$, $d_{yz}$, $d_{zx}$ and $d_{x^2-y^2}$ all have four cloverleaf lobes, whereas $d_{z^2}$ has two lobes along $z$ plus a ring in the $xy$ plane, so $d_{x^2-y^2}$ and $d_{z^2}$ are not similar and option $4$ is the incorrect statement.

**Subtopic:** Atomic Orbitals: Shapes, Energies and Nodes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q068_a9f8d2b6_02112026.png?v=a9f8d2b63a1e)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q068_46fd790f_02112026.png?v=46fd790fb05b)

---

## Q69

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

The Kjeldahl’s method for the estimation of nitrogen can be used to estimate the amount of nitrogen in which one of the following compounds?

- (1) nitrobenzene `O=[N+]([O-])c1ccccc1` ![nitrobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q069_option_1_s1_017308e0_02112026.svg?v=017308e0a06d)
- (2) pyridine `c1ccncc1` ![pyridine](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q069_option_2_s1_9a27e894_02112026.svg?v=9a27e8945a7d)
- **(3)** aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q069_option_3_s1_3051b9a1_02112026.svg?v=3051b9a1f0bc)
- (4) azobenzene `c1ccc(N=Nc2ccccc2)cc1` ![azobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q069_option_4_s1_c6c0919e_02112026.svg?v=c6c0919ef009)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Kjeldahl method is not applicable to compounds containing nitrogen in nitro group, azo groups and nitrogen present in the ring (e.g., pyridine) as nitrogen of these compounds does not change to ammonium sulphate under these conditions.

**Solved independently** (answer withheld)

1. Kjeldahl's method does not work for compounds with nitrogen in nitro or azo groups or nitrogen in a ring, because that nitrogen is not converted to $(NH_4)_2SO_4$ on digestion with conc. $H_2SO_4$.
2. Option $1$ is nitrobenzene ($-NO_2$), option $2$ is pyridine (ring N) and option $4$ is azobenzene ($-N=N-$), so all three are excluded.
3. Option $3$ is aniline ($C_6H_5NH_2$), whose $-NH_2$ nitrogen becomes $(NH_4)_2SO_4$, so the method works: option $3$.

**Subtopic:** Quantitative Analysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q069_0d3996b3_02112026.png?v=0d3996b348ce)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q069_3153901c_02112026.png?v=3153901c4306)

---

## Q70

Chemistry · inorganic · The p–Block Elements

Choose the correct statement:

- (1) Diamond and graphite have two dimensional network.
- (2) Diamond is covalent and graphite is ionic.
- **(3)** Diamond is $\mathrm{sp^3}$ hybridised and graphite is $\mathrm{sp^2}$ hybridized.
- (4) Both diamond and graphite are used as dry lubricants.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Diamond : $sp^{3}$ hybridised carbon atom
2. Covalent solid
3. 3-D structure
4. Cannot be used as dry lubricant
5. Graphite : $sp^{2}$ hybridised carbon atom
6. Covalent solid
7. 3-D structure
8. Used as dry lubricant

**Solved independently** (answer withheld)

1. Diamond: each C is tetrahedrally bonded to four C atoms, so it is $\mathrm{sp^3}$ with a three-dimensional network; option $1$ is false.
2. Graphite: each C is bonded to three C atoms in hexagonal layers, so it is $\mathrm{sp^2}$; both solids are covalent, so option $2$ is false.
3. Only graphite (slippery layers) is a dry lubricant, so option $4$ is false.
4. Diamond $\mathrm{sp^3}$ and graphite $\mathrm{sp^2}$ is correct: option $3$.

**Subtopic:** Catenation & Allotropy Group 14 · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q070_e9c5115b_02112026.png?v=e9c5115b3e11)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q070_3ad80fbd_02112026.png?v=3ad80fbdbd33)

---

## Q71

Chemistry · inorganic · The s-Block Elements

Identify the incorrect statement from the following

- (1) Alkali metals react with water to form their hydroxides.
- **(2)** The oxidation number of K in $\mathrm{KO_2}$ is $+4$.
- (3) Ionisation enthalpy of alkali metals decreases from top to bottom in the group.
- (4) Lithium is the strongest reducing agent among the alkali metals.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Alkali metals show only ‘$+1$’ oxidation state in all of their compounds.
2. $\mathrm{KO_2}$ is a super-oxide in which $\mathrm{O_2^{-}}$ is anion and $\mathrm{K^{+}}$ is cation oxidation state of $\mathrm{K}$ is $+1$.

**Solved independently** (answer withheld)

1. $\mathrm{KO_2}$ is a superoxide containing the $\mathrm{O_2^-}$ ion, so each O has oxidation number $-\tfrac{1}{2}$.
2. $x + 2\left(-\tfrac{1}{2}\right) = 0 \Rightarrow x = +1$, so the statement that K is $+4$ is incorrect.
3. Alkali metals react with water to give $\mathrm{MOH}$ and $\mathrm{H_2}$; ionisation enthalpy decreases down the group; Li has the most negative $E^\circ$ and is the strongest reducing agent in aqueous solution, so statements 1, 3 and 4 are correct.
4. The incorrect statement is option $2$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q071_bc786654_02112026.png?v=bc78665441f7)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q071_550c2b1a_02112026.png?v=550c2b1aac1d)

---

## Q72

Chemistry · physical · States of Matter

Which one is not correct mathematical equation for Dalton’s Law of partial pressure? Here $p$ = total pressure of gaseous mixture

- (1) $p = p_1 + p_2 + p_3$
- (2) $p = n_1\frac{RT}{V} + n_2\frac{RT}{V} + n_3\frac{RT}{V}$
- (3) $p_i = \chi_i p$, where $p_i$ = partial pressure of $i^{\mathrm{th}}$ gas $\chi_i$ = mole fraction of $i^{\mathrm{th}}$ gas in gaseous mixture
- **(4)** $p_i = \chi_i p_i^{\circ}$, where $\chi_i$ = mole fraction of $i^{\mathrm{th}}$ gas in gaseous mixture $p_i^{\circ}$ = pressure of $i^{\mathrm{th}}$ gas in pure state

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Dalton’s law of partial pressure states that the total pressure by the mixture of non-reactive gases is equal to the sum of the partial pressures of individual gases.
2. $p_{\mathrm{Total}} = p_1 + p_2 + p_3$
3. Also, $p_i = \chi_i p$ ; where $p_i$ and $\chi_i$ are the partial pressure and mole fraction of $i^{\mathrm{th}}$ gas respectively and $p$ is the total pressure.
4. $p_{\mathrm{Total}} = p_1 + p_2 + p_3$
5. $= n_1\frac{RT}{V} + n_2\frac{RT}{V} + n_3\frac{RT}{V}$
6. $= (n_1 + n_2 + n_3)\frac{RT}{V}$

**Solved independently** (answer withheld)

1. Dalton's law: $p = p_1 + p_2 + p_3$, so option $1$ is correct.
2. With $p_i = n_i\frac{RT}{V}$, $p = n_1\frac{RT}{V} + n_2\frac{RT}{V} + n_3\frac{RT}{V}$, so option $2$ is correct.
3. $p_i = \frac{n_i}{n}p = \chi_i p$, so option $3$ is correct.
4. $p_i = \chi_i p_i^{\circ}$ is Raoult's law for the vapour pressure of a solution component, not Dalton's law, so option $4$ is the incorrect one.

**Subtopic:** Dalton's Law of Partial Pressures · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q072_4cb86fe5_02112026.png?v=4cb86fe5c914)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q072_795ff2d7_02112026.png?v=795ff2d70fa5)

---

## Q73

Chemistry · organic · Alcohols, Phenols and Ethers

Given below are two statements
Statement I: The acidic strength of monosubstituted nitrophenol is higher than phenol because of electron withdrawing nitro group.
Statement II: o-nitrophenol, m-nitrophenol and p-nitrophenol will have same acidic strength as they have one nitro group attached to the phenolic ring.
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The acidic strength of monosubstituted nitrophenol is higher than phenol because of electron withdrawing nitro group.
- (Statement II) o-nitrophenol, m-nitrophenol and p-nitrophenol will have same acidic strength as they have one nitro group attached to the phenolic ring.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: I. nitrophenol (benzene ring with OH and an NO₂ group drawn from the ring centre, position not fixed)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q073_sol_1_e78367ae_02112026.png?v=e78367aeecb7)

*I. nitrophenol (benzene ring with OH and an NO₂ group drawn from the ring centre, position not fixed)*

![drawn: I. nitrophenol (benzene ring with OH and an NO₂ group drawn from the ring centre, position not fixed)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q073_solution_1_85ed0a2e_02112026.svg?v=85ed0a2e6227)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Nitro group has electron withdrawing tendency. It can withdraw electrons both by $-I$ effect and $-R$ effect. Thus the acidic strength of monosubstituted nitrophenol is higher than phenol.
2. Nitro group present at o- and p-positions will have strong $-R$ effect while nitro group present at m-position will influence only $-I$ effect hence acidity or o/p isomer will be more meta isomer.

**Solved independently** (answer withheld)

1. Statement I: $-\mathrm{NO_2}$ is electron-withdrawing ($-I$, and $-R$ at the o/p positions), so it stabilises the phenoxide ion, and every mononitrophenol is more acidic than phenol. Statement I is true.
2. Statement II: the $-R$ effect works only from the ortho and para positions, and o-nitrophenol has intramolecular H-bonding, so the acidity order is $p > o > m$ ($\mathrm{p}K_a \approx 7.1, 7.2, 8.3$). The acidities are not the same, so Statement II is false.
3. I is correct and II is incorrect, which is option $3$.

**Subtopic:** Acidity of Phenols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q073_3a3c0161_02112026.png?v=3a3c0161d988)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q073_71dee6e2_02112026.png?v=71dee6e26a70)

---

## Q74

Chemistry · physical · Electrochemistry

At $298\,\mathrm{K}$, the standard electrode potentials of $\mathrm{Cu^{2+}}$ / $\mathrm{Cu}$, $\mathrm{Zn^{2+}}$ / $\mathrm{Zn}$, $\mathrm{Fe^{2+}}$ / $\mathrm{Fe}$ and $\mathrm{Ag^{+}}$ / $\mathrm{Ag}$ are $0.34\,\mathrm{V}$, $-0.76\,\mathrm{V}$, $-0.44\,\mathrm{V}$ and $0.80\,\mathrm{V}$, respectively. On the basis of standard electrode potential, predict which of the following reaction cannot occur?

- (1) $\mathrm{CuSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Cu(s)}$
- (2) $\mathrm{CuSO_4(aq) + Fe(s) \rightarrow FeSO_4(aq) + Cu(s)}$
- (3) $\mathrm{FeSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Fe(s)}$
- **(4)** $\mathrm{2CuSO_4(aq) + 2Ag(s) \rightarrow 2Cu(s) + Ag_2SO_4(aq)}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For a reaction to be spontaneous, $E^{o}_{\mathrm{cell}}$ must be positive.
2. For, $\mathrm{FeSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Fe(s)}$
3. $E^{o}_{\mathrm{cell}} = E^{o}_{\mathrm{cathode}} - E^{o}_{\mathrm{anode}}$
4. $= -0.44\,\mathrm{V} - (-0.76\,\mathrm{V})$
5. $= 0.32\,\mathrm{V}$
6. For, $\mathrm{2CuSO_4(aq) + 2Ag(s) \rightarrow 2Cu(s) + Ag_2SO_4(aq)}$
7. $E^{o}_{\mathrm{cell}} = 0.34\,\mathrm{V} - 0.80\,\mathrm{V}$
8. $= -0.46\,\mathrm{V}$
9. For, $\mathrm{CuSO_4(aq) + Zn(s) \rightarrow ZnSO_4(aq) + Cu(s)}$
10. $E^{o}_{\mathrm{cell}} = 0.34\,\mathrm{V} - (-0.76\,\mathrm{V})$
11. $= 1.1\,\mathrm{V}$
12. For, $\mathrm{CuSO_4(aq) + Fe(s) \rightarrow FeSO_4(aq) + Cu(s)}$
13. $E^{o}_{\mathrm{cell}} = 0.80\,\mathrm{V} - (-0.44\,\mathrm{V})$
14. $= 1.24\,\mathrm{V}$

**Solved independently** (answer withheld)

1. A displacement reaction occurs if $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} > 0$.
2. Option 1: $E^\circ_{cell} = 0.34 - (-0.76) = +1.10\,\mathrm{V}$, feasible.
3. Option 2: $E^\circ_{cell} = 0.34 - (-0.44) = +0.78\,\mathrm{V}$, feasible.
4. Option 3: $E^\circ_{cell} = -0.44 - (-0.76) = +0.32\,\mathrm{V}$, feasible.
5. Option 4: $E^\circ_{cell} = 0.34 - 0.80 = -0.46\,\mathrm{V} < 0$, so it cannot occur; answer is option $4$.

**Subtopic:** Electrochemical Series · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q074_1136a5a4_02112026.png?v=1136a5a40937)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q074_daba2c7e_02112026.png?v=daba2c7e051a)

---

## Q75

Chemistry · physical · Surface Chemistry

Given below are two statements
In the light of the above statements, choose the most appropriate answer from the options given below

- (Statement I) In the coagulation of a negative sol, the flocculating power of the three given ions is in the order $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$
- (Statement II) In the coagulation of a positive sol, the flocculating power of the three given salts is in the order $\mathrm{NaCl} > \mathrm{Na_2SO_4} > \mathrm{Na_3PO_4}$

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

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
4. Statement II gives the reverse order, so it is incorrect; the answer is option $3$.

**Subtopic:** Coagulation of Colloids and Hardy-Schulze Rule · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q075_4aa92151_02112026.png?v=4aa921516153)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q075_39ac8e2f_02112026.png?v=39ac8e2f20c1)

---

## Q76

Chemistry · inorganic · The s-Block Elements

Match List-I with List-II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{Li}$ | (i) | absorbent for carbon dioxide |
| (b) | $\mathrm{Na}$ | (ii) | electrochemical cells |
| (c) | $\mathrm{KOH}$ | (iii) | coolant in fast breeder reactors |
| (d) | $\mathrm{Cs}$ | (iv) | photoelectric cell |

- (1) (a) - (iv), (b) – (i), (c) – (iii), (d) – (ii)
- (2) (a) - (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (3) (a) - (i), (b) – (iii), (c) – (iv), (d) – (ii)
- **(4)** (a) - (ii), (b) – (iii), (c) – (i), (d) – (iv)

**Answer** — booklet: (4) · independent solve: (4) · agree

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
5. The match (a)-(ii), (b)-(iii), (c)-(i), (d)-(iv) is option $4$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q076_579d78ef_02112026.png?v=579d78ef81ac)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q076_324d4769_02112026.png?v=324d4769e8ad)

---

## Q77

Chemistry · organic · Amines

Given below are two statements In the light of the above statements, choose the most appropriate answer from the options given below

- (Statement I) Primary aliphatic amines react with $\mathrm{HNO_2}$ to give unstable diazonium salts.
- (Statement II) Primary aromatic amines react with $\mathrm{HNO_2}$ to form diazonium salts which are stable even above $300\,\mathrm{K}$.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Primary aliphatic amines react with $\mathrm{HNO_2}$ and give unstable diazonium salt which turns into alcohol
2. $\mathrm{R-NH_2 + HNO_2 \longrightarrow \left[R-N_2^{+}-Cl^{-}\right] \xrightarrow{H_2O} ROH + N_2 + HCl}$
3. Primary aromatic amines reacts with $\mathrm{HNO_2}$ and give stable diazonium salt which are stable at $273$ to $278\,\mathrm{K}$.
4. $\mathrm{C_6H_5-NH_2 + HNO_2 \xrightarrow{273-278\,K} C_6H_5N_2^{+}Cl^{-}}$

**Solved independently** (answer withheld)

1. Statement I: $\mathrm{RNH_2} + \mathrm{HNO_2} \rightarrow [\mathrm{RN_2^+}]$, an unstable aliphatic diazonium salt that decomposes to alcohol and $\mathrm{N_2}$, so Statement I is correct.
2. Statement II: arenediazonium salts are stable only in the cold ($273$-$278\,\mathrm{K}$) and decompose on warming, so they are not stable above $300\,\mathrm{K}$; Statement II is incorrect.
3. Statement I correct, Statement II incorrect, which is option $3$.

**Subtopic:** Diazotization and Its Method of Preparation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q077_d7782e16_02112026.png?v=d7782e16488a)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q077_fd35ee3f_02112026.png?v=fd35ee3f7631)

---

## Q78

Chemistry · organic · Polymers

Which statement regarding polymers is not correct?

- (1) Elastomers have polymer chains held together by weak intermolecular forces
- (2) Fibers possess high tensile strength
- (3) Thermoplastic polymers are capable of repeatedly softening and hardening on heating and cooling respectively
- **(4)** Thermosetting polymers are reusable

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Thermoplastic polymers are the linear or slightly long chain molecules capable of repeatedly softening and hardening on cooling.
2. Thermosetting polymers are cross-linked or heavily branched molecules, which on heating undergo extensive cross-linking in moulds and again become infusible. These cannot be reused.
3. Elastomers have polymer chains held together by weak intermolecular forces.
4. Fibres possess high tensile strength.

**Solved independently** (answer withheld)

1. Elastomers have polymer chains held by the weakest intermolecular forces, so option $1$ is correct.
2. Fibres have strong intermolecular forces (e.g. H-bonding), giving high tensile strength, so option $2$ is correct.
3. Thermoplastics can be repeatedly softened on heating and hardened on cooling, so option $3$ is correct.
4. Thermosetting polymers become extensively cross-linked and infusible on heating and cannot be reused, so option $4$ is the incorrect statement.

**Subtopic:** Classification of Polymers Based on Molecular Forces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q078_b13f1fca_02112026.png?v=b13f1fcafcd6)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q078_38aa9d58_02112026.png?v=38aa9d585dea)

---

## Q79

Chemistry · physical · Solutions

In one molal solution that contains $0.5$ mole of a solute, there is

- (1) $500\,\mathrm{mL}$ of solvent
- **(2)** $500\,\mathrm{g}$ of solvent
- (3) $100\,\mathrm{mL}$ of solvent
- (4) $1000\,\mathrm{g}$ of solvent

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Molality is the moles of solute dissolved per kg of solvent therefore $500\,\mathrm{g}$, $1$ molal solution contains $0.5$ of solute, as
2. $m = \frac{\text{Moles of solute}}{\text{Mass of solvent (in kg)}}$
3. $1 = \frac{0.5}{\text{Mass of solvent (in kg)}}$
4. $\therefore$ Mass of solvent (in kg) $= 0.5$
5. $= 500\,\mathrm{g}$

**Solved independently** (answer withheld)

1. Molality is defined as $m = \frac{n_{\text{solute}}}{W_{\text{solvent}}\,(\mathrm{kg})}$.
2. Rearranging, $W_{\text{solvent}} = \frac{n_{\text{solute}}}{m} = \frac{0.5\,\mathrm{mol}}{1\,\mathrm{mol\,kg^{-1}}} = 0.5\,\mathrm{kg}$.
3. $0.5\,\mathrm{kg} = 500\,\mathrm{g}$ of solvent, which is option $2$.

**Subtopic:** Molality · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q079_c7e44e18_02112026.png?v=c7e44e18177a)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q079_39c8c1e5_02112026.png?v=39c8c1e55698)

---

## Q80

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

$\mathrm{RMgX + CO_2 \xrightarrow[\text{ether}]{\text{dry}} Y \xrightarrow{H_3O^+} RCOOH}$
What is Y in the above reaction?

- **(1)** $\mathrm{RCOO^{-}Mg^{+}X}$
- (2) $\mathrm{R_3CO^{-}Mg^{+}X}$
- (3) $\mathrm{RCOO^{-}X^{+}}$
- (4) $\mathrm{(RCOO)_2Mg}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →($\ce{H3O+}$) $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q080_sol_1_2911d722_02112026.png?v=2911d72263c6)

*carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →[$\ce{H3O+}$] $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$*

![drawn: carbon dioxide + $\ce{R^{-}Mg^{+}X}$ → $\ce{R-C(=O)-O^{-}Mg^{+}X}$ (Y); (Y) →($\ce{H3O+}$) $\ce{R-C(=O)-OH}$ + $\ce{Mg(OH)X}$](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q080_solution_1_487c9f29_02112026.svg?v=487c9f29119c)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Here Y is $\mathrm{RCOO^{-}Mg^{+}X}$

**Solved independently** (answer withheld)

1. The nucleophilic $\mathrm{R^-}$ of $\mathrm{RMgX}$ attacks the carbon of $\mathrm{CO_2}$: $\mathrm{RMgX + CO_2 \rightarrow RCOO^{-}Mg^{+}X}$, so $Y = \mathrm{RCOO^{-}Mg^{+}X}$.
2. Acid hydrolysis: $\mathrm{RCOO^{-}Mg^{+}X \xrightarrow{H_3O^+} RCOOH + Mg(OH)X}$, matching the given product, which is option $1$.

**Subtopic:** Methods of Preparation of Carboxylic Acids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q080_a2c891e7_02112026.png?v=a2c891e79bf6)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q080_3ea83ba1_02112026.png?v=3ea83ba1f304)

---

## Q81

Chemistry · physical · Electrochemistry

Given below are half cell reactions:
$\mathrm{MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O}$,
$E^{\circ}_{\mathrm{Mn^{2+}/MnO_4^-}} = -1.510\,\mathrm{V}$
$\frac{1}{2}\mathrm{O_2 + 2H^+ + 2e^- \rightarrow H_2O}$,
$E^{\circ}_{\mathrm{O_2/H_2O}} = +1.223\,\mathrm{V}$
Will the permanganate ion, $\mathrm{MnO_4^-}$ liberate $\mathrm{O_2}$ from water in the presence of an acid?

- **(1)** Yes, because $E^{\circ}_{\mathrm{cell}} = +0.287\,\mathrm{V}$
- (2) No, because $E^{\circ}_{\mathrm{cell}} = -0.287\,\mathrm{V}$
- (3) Yes, because $E^{\circ}_{\mathrm{cell}} = +2.733\,\mathrm{V}$
- (4) No, because $E^{\circ}_{\mathrm{cell}} = -2.733\,\mathrm{V}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{MnO_4^- + 8H^+ + 5e^- \longrightarrow Mn^{2+} + 4H_2O}$ $\quad \ldots(\mathrm{i})$
2. $E^{\circ}_{\mathrm{MnO_4^-/Mn^{2+}}} = -E^{\circ}_{\mathrm{Mn^{2+}/MnO_4^-}} = 1.51\,\mathrm{V}$
3. $\mathrm{H_2O \longrightarrow \frac{1}{2}O_2 + 2H^+ + 2e^-}$ $\quad \ldots(\mathrm{ii})$
4. $E^{\circ}_{\mathrm{O_2/H_2O}} = 1.223\,\mathrm{V}$
5. Using $2 \times (\mathrm{i}) + 5 \times (\mathrm{ii})$, net cell reactions is
6. $\mathrm{2MnO_4^- + 6H^+ \longrightarrow 2Mn^{2+} + \frac{5}{2}O_2 + 3H_2O}$
7. $E^{\circ}_{\mathrm{cell}} = E^{\circ}_{\mathrm{C}} - E^{\circ}_{\mathrm{A}} = E^{\circ}_{\mathrm{MnO_4^-/Mn^{2+}}} - E^{\circ}_{\mathrm{O_2/H_2O}} = 1.51 - 1.223 = 0.287\,\mathrm{V}$
8. Since $E^{\circ}_{\mathrm{cell}} > 0$, therefore net cell reaction is spontaneous and so $\mathrm{MnO_4^-}$ liberate $\mathrm{O_2}$ from $\mathrm{H_2O}$ in presence of an acid.

**Solved independently** (answer withheld)

1. The given $E^{\circ}_{\mathrm{Mn^{2+}/MnO_4^-}} = -1.510\,\mathrm{V}$ is an oxidation potential, so $E^{\circ}_{\mathrm{MnO_4^-/Mn^{2+}}} = +1.510\,\mathrm{V}$.
2. Permanganate is reduced (cathode) and water is oxidised to $\mathrm{O_2}$ (anode).
3. $E^{\circ}_{\mathrm{cell}} = E^{\circ}_{\mathrm{cathode}} - E^{\circ}_{\mathrm{anode}} = 1.510 - 1.223 = +0.287\,\mathrm{V}$.
4. $E^{\circ}_{\mathrm{cell}} > 0$, so the reaction is spontaneous: yes, $\mathrm{O_2}$ is liberated, which is option $1$.

**Subtopic:** Cell Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q081_7d296db4_02112026.png?v=7d296db4ba52)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q081_3d7e503f_02112026.png?v=3d7e503fa3a8)

---

## Q82

Chemistry · physical · Basic Concepts of Chemistry

What mass of $95\%$ pure $\mathrm{CaCO_3}$ will be required to neutralise $50\,\mathrm{mL}$ of $0.5\,\mathrm{M}$ $\mathrm{HCl}$ solution according to the following reaction?
$\mathrm{CaCO_{3(s)} + 2HCl_{(aq)} \rightarrow CaCl_{2(aq)} + CO_{2(g)} + 2H_2O_{(l)}}$
[Calculate upto second place of decimal point]

- (1) $1.25\,\mathrm{g}$
- **(2)** $1.32\,\mathrm{g}$
- (3) $3.65\,\mathrm{g}$
- (4) $9.50\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Let $m$ gram mass of $\mathrm{CaCO_3}$ is required
2. Pure $\mathrm{CaCO_3}$ in $m$ gram $= \frac{95}{100} \times m$
3. Moles of $\mathrm{CaCO_3} = \frac{95}{100} \times \frac{m}{100}$
4. Moles of $\mathrm{HCl}$ required $= 2 \times$ moles of $\mathrm{CaCO_3}$
5. $= 2 \times \frac{95}{100} \times \frac{m}{100}$
6. $2 \times \frac{95}{100} \times \frac{m}{100} = \frac{50}{1000} \times 0.5$
7. $m = 1.315\,\mathrm{g} \approx 1.32\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $n_{\mathrm{HCl}} = 0.050\,\mathrm{L} \times 0.5\,\mathrm{M} = 0.025\,\mathrm{mol}$.
2. From the equation, $1\,\mathrm{mol\ CaCO_3}$ reacts with $2\,\mathrm{mol\ HCl}$, so $n_{\mathrm{CaCO_3}} = \frac{0.025}{2} = 0.0125\,\mathrm{mol}$.
3. Mass of pure $\mathrm{CaCO_3} = 0.0125 \times 100\,\mathrm{g\,mol^{-1}} = 1.25\,\mathrm{g}$.
4. The sample is $95\%$ pure, so required mass $= \frac{1.25}{0.95} = 1.3158\,\mathrm{g} \approx 1.32\,\mathrm{g}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 32)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q082_df0c4fc9_02112026.png?v=df0c4fc9d8d8)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q082_17e962f5_02112026.png?v=17e962f51622)

---

## Q83

Chemistry · physical · Ionic Equilibrium

The pH of the solution containing $50\,\mathrm{mL}$ each of $0.10\,\mathrm{M}$ sodium acetate and $0.01\,\mathrm{M}$ acetic acid is [Given $\mathrm{p}K_{\mathrm{a}}$ of $\mathrm{CH_3COOH} = 4.57$]

- **(1)** $5.57$
- (2) $3.57$
- (3) $4.57$
- (4) $2.57$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{CH_3COONa} + \mathrm{CH_3COOH}$, $\mathrm{CH_3COOH}(\mathrm{p}K_{\mathrm{a}}) = 4.57$
2. $0.1\,\mathrm{M}$ \quad $0.01\,\mathrm{M}$
3. $50\,\mathrm{mL}$ \quad $50\,\mathrm{mL}$
4. It is a mixture of weak acid and salt of its conjugate base. Hence it is acidic buffer.
5. $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \log\frac{[\mathrm{Salt}]}{[\mathrm{Acid}]}$
6. $= 4.57 + \log\left(\frac{0.1}{0.01}\right)$
7. $= 4.57 + 1$
8. $= 5.57$

**Solved independently** (answer withheld)

1. Sodium acetate with acetic acid forms an acidic buffer, so $\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\text{salt}]}{[\text{acid}]}$.
2. Equal volumes ($50\,\mathrm{mL}$ each) are mixed, so the ratio is $\frac{[\text{salt}]}{[\text{acid}]} = \frac{0.10}{0.01} = 10$.
3. $\mathrm{pH} = 4.57 + \log 10 = 4.57 + 1 = 5.57$, which is option $1$.

**Subtopic:** Buffer Solutions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q083_c2348631_02112026.png?v=c2348631f231)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q083_f631a328_02112026.png?v=f631a328d863)

---

## Q84

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List-I with List-II.
List – I (Products formed) | List – II (Reaction of carbonyl compound with)
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cyanohydrin | (i) | $\mathrm{NH_2OH}$ |
| (b) | Acetal | (ii) | $\mathrm{RNH_2}$ |
| (c) | Schiff's base | (iii) | alcohol |
| (d) | Oxime | (iv) | $\mathrm{HCN}$ |

- (1) (a) – (iii), (b) – (iv), (c) – (ii), (d) – (i)
- (2) (a) – (ii), (b) – (iii), (c) – (iv), (d) – (i)
- (3) (a) – (i), (b) – (iii), (c) – (ii), (d) – (iv)
- **(4)** (a) – (iv), (b) – (iii), (c) – (ii), (d) – (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. List – I (Products formed) | List – II (Reaction of carbonyl compound with)
2. (a) Cyanohydrin $\rightarrow$ $\mathrm{HCN}$
3. (b) Acetal $\rightarrow$ Alcohol
4. (c) Schiff's base $\rightarrow$ $\mathrm{RNH_2}$
5. (d) Oxime $\rightarrow$ $\mathrm{NH_2OH}$
6. (a) – (iv), (b) – (iii), (c) – (ii), (d) – (i)

![printed figure: acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q084_sol_1_8c6e5a3e_02112026.png?v=8c6e5a3e61c1)

*acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)*

![drawn: acetaldehyde + hydrogen cyanide → 2-hydroxypropanenitrile (Cyanohydrin)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q084_solution_1_c70c2837_02112026.svg?v=c70c2837e4b4)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + R–OH (Alcohol) ⇌(H⁺) 1,1-dialkoxyethane (Acetal)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q084_sol_2_342bf761_02112026.png?v=342bf7619565)

*acetaldehyde + R–OH (Alcohol) ⇌[H⁺] 1,1-dialkoxyethane (Acetal)*

![drawn: acetaldehyde + R–OH (Alcohol) ⇌(H⁺) 1,1-dialkoxyethane (Acetal)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q084_solution_2_d0341abb_02112026.svg?v=d0341abb155f)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + R–NH₂ → N-alkylethanimine (Schiff's base)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q084_sol_3_74f88447_02112026.png?v=74f88447b9e8)

*acetaldehyde + R–NH₂ → N-alkylethanimine (Schiff's base)*

![drawn: acetaldehyde + R–NH₂ → N-alkylethanimine (Schiff's base)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q084_solution_3_015e2ada_02112026.svg?v=015e2ada37e4)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q084_sol_4_1af65303_02112026.png?v=1af65303b336)

*acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)*

![drawn: acetaldehyde + hydroxylamine ⇌ acetaldehyde oxime (Oxime)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q084_solution_4_8a679325_02112026.svg?v=8a679325abc5)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Carbonyl $+ \mathrm{HCN}$ gives cyanohydrin, so (a)–(iv).
2. Carbonyl $+$ alcohol (dry HCl) gives acetal, so (b)–(iii).
3. Carbonyl $+ \mathrm{RNH_2}$ gives a Schiff's base (imine), so (c)–(ii).
4. Carbonyl $+ \mathrm{NH_2OH}$ gives oxime, so (d)–(i).
5. The set (a)–(iv), (b)–(iii), (c)–(ii), (d)–(i) is option $4$.

**Subtopic:** Nucleophilic Addition Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q084_c147c5e4_02112026.png?v=c147c5e4d36c)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q084_25a159bc_02112026.png?v=25a159bce498)

---

## Q85

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which amongst the following is incorrect statement?

- (1) The bond orders of $\mathrm{O_2^{+}}$, $\mathrm{O_2}$, $\mathrm{O_2^{-}}$ and $\mathrm{O_2^{2-}}$ are 2.5, 2, 1.5 and 1, respectively
- (2) $\mathrm{C_2}$ molecule has four electrons in its two degenerate $\pi$ molecular orbitals
- (3) $\mathrm{H_2^{+}}$ ion has one electron
- **(4)** $\mathrm{O_2^{+}}$ ion is diamagnetic

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\sigma 1s^{2}\sigma^{*}1s^{2}\sigma 2s^{2}\sigma^{*}2s^{2}\sigma 2p_{z}^{2}\begin{array}{c}\pi 2p_{x}^{2}\\ | \\ \pi 2p_{y}^{2}\end{array}\begin{array}{c}\pi^{*}2p_{x}^{1}\\ | \\ \pi 2p_{y}\end{array}$
2. Due to one unpaired electron in $\pi^{*}2p$ molecular orbital, $\mathrm{O_2^{+}}$ is a paramagnetic ion.

**Solved independently** (answer withheld)

1. Option 1: bond order $= \frac{N_b - N_a}{2}$; $\mathrm{O_2^{+}} = \frac{10-5}{2} = 2.5$, $\mathrm{O_2} = \frac{10-6}{2} = 2$, $\mathrm{O_2^{-}} = \frac{10-7}{2} = 1.5$, $\mathrm{O_2^{2-}} = \frac{10-8}{2} = 1$, so the statement is correct.
2. Option 2: $\mathrm{C_2}$ (12 electrons) has configuration $\sigma 1s^2 \sigma^* 1s^2 \sigma 2s^2 \sigma^* 2s^2 (\pi 2p_x^2 = \pi 2p_y^2)$, i.e. four electrons in the two degenerate $\pi$ MOs, so the statement is correct.
3. Option 3: $\mathrm{H_2^{+}}$ has $1 + 1 - 1 = 1$ electron, so the statement is correct.
4. Option 4: $\mathrm{O_2^{+}}$ has 15 electrons, leaving one unpaired electron in $\pi^* 2p$, so it is paramagnetic; calling it diamagnetic is incorrect.
5. The incorrect statement is option $4$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q085_0d273818_02112026.png?v=0d273818c8bf)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q085_bb57e9f7_02112026.png?v=bb57e9f7fd16)

---

## Q86

Chemistry · organic · Alcohols, Phenols and Ethers

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) In Lucas test, primary, secondary and tertiary alcohols are distinguished on the basis of their reactivity with conc. $\mathrm{HCl} + \mathrm{ZnCl_2}$, known as Lucas Reagent.
- (Statement II) Primary alcohols are most reactive and immediately produce turbidity at room temperature on reaction with Lucas Reagent.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Primary, secondary and tertiary alcohols can be differentiated by their reaction with $(\mathrm{HCl} + \text{anhy } \mathrm{ZnCl_2})$
2. Lucas reagent
3. $3^{\circ}$ alcohol $\xrightarrow{\mathrm{ZnCl_2 + HCl}}$ Immediate turbidity at room temperature
4. $2^{\circ}$ alcohol $\xrightarrow{\mathrm{ZnCl_2 + HCl}}$ Turbidity after $5$ minutes at room temperature
5. $1^{\circ}$ alcohol $\xrightarrow{\mathrm{ZnCl_2 + HCl}}$ Do not gives turbidity at room temperature

**Solved independently** (answer withheld)

1. Statement I: Lucas reagent (conc. $\mathrm{HCl} + \mathrm{ZnCl_2}$) distinguishes $1^\circ$, $2^\circ$ and $3^\circ$ alcohols by their rate of reaction, so it is correct.
2. Statement II: reactivity order is $3^\circ > 2^\circ > 1^\circ$ (carbocation stability); tertiary alcohols give immediate turbidity, primary alcohols give none at room temperature, so it is incorrect.
3. Statement I correct and Statement II incorrect is option $3$.

**Subtopic:** Test of Alcohol · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q086_b7e5de10_02112026.png?v=b7e5de10ed39)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q086_087def0c_02112026.png?v=087def0c378a)

---

## Q87

Chemistry · physical · Structure of Atom

If radius of second Bohr orbit of the $\mathrm{He^{+}}$ ion is $105.8\,\mathrm{pm}$, what is the radius of third Bohr orbit of $\mathrm{Li^{2+}}$ ion?

- **(1)** $158.7\,\mathrm{pm}$
- (2) $15.87\,\mathrm{pm}$
- (3) $1.587\,\mathrm{pm}$
- (4) $158.7\,\mathring{\mathrm{A}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $r_n \propto \frac{n^2}{Z}$
2. $\frac{r_3(\mathrm{Li^{2+}})}{r_2(\mathrm{He^{+}})} = \frac{(n_3)^2}{Z(\mathrm{Li^{2+}})} \times \frac{Z(\mathrm{He^{+}})}{(n_2)^2}$
3. $\frac{r_3(\mathrm{Li^{2+}})}{105.8} = \frac{(3)^2}{3} \times \frac{2}{(2)^2}$
4. $= 105.8 \times \frac{3}{2}$
5. $r_3(\mathrm{Li^{2+}}) = 158.7\,\mathrm{pm}$

**Solved independently** (answer withheld)

1. Bohr radius: $r_n = a_0 \frac{n^2}{Z}$, so $r \propto \frac{n^2}{Z}$.
2. For $\mathrm{He^{+}}$, $n=2, Z=2$: $\frac{n^2}{Z} = \frac{4}{2} = 2$, so $2a_0 = 105.8\,\mathrm{pm}$.
3. For $\mathrm{Li^{2+}}$, $n=3, Z=3$: $\frac{n^2}{Z} = \frac{9}{3} = 3$.
4. $r = 105.8 \times \frac{3}{2} = 158.7\,\mathrm{pm}$, which is option $1$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q087_7396cfdf_02112026.png?v=7396cfdfe7dd)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q087_fc53dd61_02112026.png?v=fc53dd6174c1)

---

## Q88

Chemistry · physical · Chemical Kinetics

For a first order reaction $\mathrm{A} \rightarrow$ Products, initial concentration of A is $0.1\,\mathrm{M}$, which becomes $0.001\,\mathrm{M}$ after $5$ minutes. Rate constant for the reaction in $\mathrm{min^{-1}}$ is

- (1) $1.3818$
- **(2)** $0.9212$
- (3) $0.4606$
- (4) $0.2303$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For first order reaction,
2. $K = \frac{2.303}{t}\log\frac{[A_0]}{[A]}$; where $A_0$ is the initial concentration of reactant A.
3. $A_0 = 0.1\,\mathrm{M}$
4. $A = 0.001\,\mathrm{M}$
5. $t = 5$ minute
6. $K = \frac{2.303}{5}\log\frac{0.1}{0.001} = \frac{2.303}{5}\log 10^{2}$
7. $= \frac{2.303}{5} \times 2$
8. $K = 0.9212\,\mathrm{min^{-1}}$

**Solved independently** (answer withheld)

1. For a first order reaction, $k = \frac{2.303}{t}\log\frac{[A]_0}{[A]}$.
2. $\frac{[A]_0}{[A]} = \frac{0.1}{0.001} = 100$, so $\log 100 = 2$.
3. $k = \frac{2.303}{5} \times 2 = \frac{4.606}{5} = 0.9212\,\mathrm{min^{-1}}$, which is option $2$.

**Subtopic:** First Order Reactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q088_70892978_02112026.png?v=708929783cc5)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q088_ab0866dc_02112026.png?v=ab0866dc3187)

---

## Q89

Chemistry · physical · States of Matter

A $10.0\,\mathrm{L}$ flask contains $64\,\mathrm{g}$ of oxygen at $27^{\circ}\mathrm{C}$. (Assume $\mathrm{O_2}$ gas is behaving ideally). The pressure inside the flask in bar is (Given $R = 0.0831\,\mathrm{L\,bar\,K^{-1}\,mol^{-1}}$)

- (1) $2.5$
- (2) $498.6$
- (3) $49.8$
- **(4)** $4.9$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. We know for ideal gas
2. $PV = nRT$
3. $P = n\frac{RT}{V}$
4. $P = \frac{64}{32} \times \frac{0.0831 \times 300}{10}$
5. $P = 4.9\,\mathrm{bar}$
6. Pressure of $\mathrm{O_2}$ gas inside the flask $= 4.9\,\mathrm{bar}$

**Solved independently** (answer withheld)

1. $n = \frac{64\,\mathrm{g}}{32\,\mathrm{g\,mol^{-1}}} = 2\,\mathrm{mol}$.
2. $T = 27 + 273 = 300\,\mathrm{K}$.
3. $P = \frac{nRT}{V} = \frac{2 \times 0.0831 \times 300}{10.0}$.
4. $P = \frac{49.86}{10.0} = 4.986\,\mathrm{bar} \approx 4.9\,\mathrm{bar}$, which is option $4$.

**Subtopic:** Gas Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q089_6039f136_02112026.png?v=6039f1363579)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q089_5cbfb8a0_02112026.png?v=5cbfb8a0da64)

---

## Q90

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The correct IUPAC name of the following compound is

![printed figure: 1-bromo-5-chloro-4-methylhexan-3-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q090_7c773cf2_02112026.png?v=7c773cf24b06)

*1-bromo-5-chloro-4-methylhexan-3-ol*

![drawn: 1-bromo-5-chloro-4-methylhexan-3-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q090_question_373d9359_02112026.svg?v=373d93597a9e)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-bromo-5-chloro-4-methylhexan-3-ol `CC(Cl)C(C)C(O)CCBr` ![1-bromo-5-chloro-4-methylhexan-3-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q090_question_s1_b0fc92e9_02112026.svg?v=b0fc92e9b0c8)

- **(1)** 1-bromo-5-chloro-4-methylhexan-3-ol
- (2) 6-bromo-2-chloro-4-methythexan-4-ol
- (3) 1-bromo-4-methyl-5-chlorohexan-3-ol
- (4) 6-bromo-4-methyl-2-chlorohexan-4-ol

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: 1-bromo-5-chloro-4-methylhexan-3-ol with chain carbons numbered 1 (CH2Br end) to 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q090_sol_1_30e48ec0_02112026.png?v=30e48ec0b4e1)

*1-bromo-5-chloro-4-methylhexan-3-ol with chain carbons numbered 1 (CH2Br end) to 6*

![drawn: 1-bromo-5-chloro-4-methylhexan-3-ol with chain carbons numbered 1 (CH2Br end) to 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q090_solution_1_10e0781b_02112026.svg?v=10e0781b91b2)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. 1-bromo-5-chloro-4-methylhexan-3-ol

**Solved independently** (answer withheld)

1. The longest chain containing $\ce{-OH}$ runs from the $\ce{CH2Br}$ carbon to the terminal $\ce{CH3}$ next to $\ce{CHCl}$: $6$ carbons, so the parent is hexan-ol.
2. Numbering from the Br end puts $\ce{-OH}$ at $C_3$; from the other end it would be $C_4$, so number from the Br end.
3. Substituents then sit at: Br on $C_1$, $\ce{CH3}$ on $C_4$, Cl on $C_5$.
4. Prefixes in alphabetical order: bromo, chloro, methyl $\Rightarrow$ 1-bromo-5-chloro-4-methylhexan-3-ol, which is option $1$.

**Subtopic:** Nomenclature of Organic Compounds Having Functional Group(s) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q090_6f941d64_02112026.png?v=6f941d642c1c)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q090_52037a55_02112026.png?v=52037a5502a5)

---

## Q91

Chemistry · inorganic · Environmental Chemistry

The pollution due to oxides of sulphur gets enhanced due to the presence of:
Choose the most appropriate answer from the options given below:

- (a) particulate matter
- (b) ozone
- (c) hydrocarbons
- (d) hydrogen peroxide

- (1) (a), (d) only
- **(2)** (a), (b), (d) only
- (3) (b), (c), (d) only
- (4) (a), (c), (d) only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Presence of particulate matter in polluted air catalyzes the oxidation of $\mathrm{SO_2}$ to $\mathrm{SO_3}$
2. i.e., $\mathrm{2SO_2(g) + O_2(g) \longrightarrow 2SO_3(g)}$
3. This reaction can also be promoted by $\mathrm{O_3}$ and $\mathrm{H_2O_2}$, as
4. $\mathrm{SO_2(g) + O_3(g) \longrightarrow SO_3(g) + O_2(g)}$
5. $\mathrm{SO_2(g) + H_2O_2(l) \longrightarrow H_2SO_4(aq)}$

**Solved independently** (answer withheld)

1. Particulate matter in polluted air catalyses the oxidation $\mathrm{2SO_2 + O_2 \rightarrow 2SO_3}$, so (a) enhances the pollution.
2. Ozone ($\mathrm{O_3}$) and hydrogen peroxide ($\mathrm{H_2O_2}$) also promote the oxidation of $\mathrm{SO_2}$ to $\mathrm{SO_3}$, so (b) and (d) enhance it.
3. Hydrocarbons are not an agent of $\mathrm{SO_2}$ oxidation, so (c) is excluded.
4. The set (a), (b), (d) only is option $2$.

**Subtopic:** Air Pollution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q091_2581cc17_02112026.png?v=2581cc172e1d)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q091_8707a289_02112026.png?v=8707a28945ce)

---

## Q92

Chemistry · physical · The Solid State

Copper crystallises in fcc unit cell with cell edge length of $3.608 \times 10^{-8}\,\mathrm{cm}$. The density of copper is $8.92\,\mathrm{g\,cm^{-3}}$. Calculate the atomic mass of copper.

- **(1)** $63.1\,\mathrm{u}$
- (2) $31.55\,\mathrm{u}$
- (3) $60\,\mathrm{u}$
- (4) $65\,\mathrm{u}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $d = \frac{ZM}{N_A(a)^3}$
2. $Z = 4(\mathrm{FCC})$, $d = 8.92\,\mathrm{g\,cm^{-3}}$, $N_A = 6.023 \times 10^{23}$, $a = 3.608 \times 10^{-8}\,\mathrm{cm}$
3. $M = \frac{dN_A(a)^3}{Z}$
4. $= \frac{8.92 \times 6.023 \times 10^{23} \times (3.608 \times 10^{-8})^3}{4}$
5. $= \frac{8.92 \times 6.023 \times 10^{23} \times 46.97 \times 10^{-24}}{4} = \frac{2523.47 \times 10^{-1}}{4}$
6. $= 630.8 \times 10^{-1} = 63.08 \simeq 63.1\,\mathrm{u}$

**Solved independently** (answer withheld)

1. For an fcc unit cell, $Z = 4$ atoms per cell.
2. Density relation: $d = \frac{Z M}{a^3 N_A}$, so $M = \frac{d\,a^3 N_A}{Z}$.
3. $a^3 = (3.608 \times 10^{-8}\,\mathrm{cm})^3 = 46.97 \times 10^{-24}\,\mathrm{cm^3}$.
4. $d\,a^3 = 8.92 \times 46.97 \times 10^{-24} = 418.96 \times 10^{-24}\,\mathrm{g}$.
5. $d\,a^3 N_A = 418.96 \times 10^{-24} \times 6.022 \times 10^{23} = 252.3\,\mathrm{g\,mol^{-1}}$.
6. $M = \frac{252.3}{4} = 63.07 \approx 63.1\,\mathrm{u}$, which is option $1$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q092_edb755e2_02112026.png?v=edb755e2f782)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q092_053238bd_02112026.png?v=053238bd0132)

---

## Q93

Chemistry · physical · Electrochemistry

> ⚠ The booklet prints "Answer (NA)": none of the four options is correct as printed, so there is no keyed answer to check a solve against.

> ⚠ The independent solve found no printed option exactly right ("No option matches the printed values: with E°cell = 10"); its pick (unsure) is the closest fit, so treat this question as possibly misprinted.

Find the emf of the cell in which the following reaction takes place at $298\,\mathrm{K}$
$\mathrm{Ni(s)+2Ag^{+}(0.001\,M)\rightarrow Ni^{2+}(0.001\,M)+2Ag(s)}$
$\left(\text{Given that } E^{\circ}_{\mathrm{cell}}=10.5\,\mathrm{V},\ \dfrac{2.303\,RT}{F}=0.059 \text{ at } 298\,\mathrm{K}\right)$

- (1) $1.0385\,\mathrm{V}$
- (2) $1.385\,\mathrm{V}$
- (3) $0.9615\,\mathrm{V}$
- (4) $1.05\,\mathrm{V}$

**Answer** — booklet: (none) · independent solve: (unsure) · publisher_no_valid_option

**Publisher's solution**

1. $\mathrm{Ni(s) + 2Ag^{+}\,(0.001\,M) \rightarrow Ni^{2+}\,(0.001\,M) + 2Ag(s)}$
2. $E^{\circ}_{\mathrm{cell}} = 10.5\,\mathrm{V}$
3. $E_{\mathrm{cell}} = E^{\circ}_{\mathrm{cell}} - \frac{0.059}{n}\log\frac{\left[\mathrm{Ni^{2+}}\right]}{\left[\mathrm{Ag^{+}}\right]^{2}}$
4. $= 10.5 - \frac{0.059}{2}\log\frac{\left(10^{-3}\right)}{\left(10^{-3}\right)^{2}}$
5. $\Rightarrow 10.5 - \frac{0.059}{2}\log(10)^{3}$
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

**Printed in the booklet** (page 37)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q093_b15c0e3d_02112026.png?v=b15c0e3dcb78)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q093_c493fbda_02112026.png?v=c493fbda8272)

---

## Q94

Chemistry · organic · Amines

The product formed from the following reaction sequence is

![printed figure: benzonitrile →((i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O) ?](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q094_ad201cb8_02112026.png?v=ad201cb85ba1)

*benzonitrile →[(i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O] ?*

![drawn: benzonitrile →((i) LiAlH₄, H₂O; (ii) NaNO₂ + HCl; (iii) H₂O) ?](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_question_8e3e5f1c_02112026.svg?v=8e3e5f1c2a60)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzonitrile `N#Cc1ccccc1` ![benzonitrile](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_question_s1_a95268da_02112026.svg?v=a95268da86c1)

- (1) benzamide `NC(=O)c1ccccc1` ![benzamide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_option_1_s1_2caebd61_02112026.svg?v=2caebd61a953)
- (2) phenylmethanediazonium chloride `N#[N+]Cc1ccccc1.[Cl-]` ![phenylmethanediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_option_2_s1_91c64fcc_02112026.svg?v=91c64fccaff9)
- (3) benzyl chloride `ClCc1ccccc1` ![benzyl chloride](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_option_3_s1_d91fbed0_02112026.svg?v=d91fbed0f992)
- **(4)** benzyl alcohol `OCc1ccccc1` ![benzyl alcohol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_option_4_s1_76b1501e_02112026.svg?v=76b1501e4315)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: benzonitrile →((i) (a) LiAlH₄ (b) H₂O) benzylamine →((ii) NaNO₂ + HCl) phenylmethanediazonium chloride →((iii) H₂O) benzyl alcohol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q094_sol_1_70b904e8_02112026.png?v=70b904e85d17)

*benzonitrile →[(i) (a) LiAlH₄ (b) H₂O] benzylamine →[(ii) NaNO₂ + HCl] phenylmethanediazonium chloride →[(iii) H₂O] benzyl alcohol*

![drawn: benzonitrile →((i) (a) LiAlH₄ (b) H₂O) benzylamine →((ii) NaNO₂ + HCl) phenylmethanediazonium chloride →((iii) H₂O) benzyl alcohol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q094_solution_1_7838c3d3_02112026.svg?v=7838c3d39cda)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. $\mathrm{C_6H_5CN} \xrightarrow{\mathrm{LiAlH_4},\ \mathrm{H_2O}} \mathrm{C_6H_5CH_2NH_2}$ (benzylamine).
2. $\mathrm{C_6H_5CH_2NH_2} \xrightarrow{\mathrm{NaNO_2 + HCl}} [\mathrm{C_6H_5CH_2N_2^+Cl^-}]$, an aliphatic diazonium salt that is unstable.
3. $[\mathrm{C_6H_5CH_2N_2^+}] \xrightarrow{\mathrm{H_2O}} \mathrm{C_6H_5CH_2OH} + \mathrm{N_2}$, benzyl alcohol, which is option $4$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q094_648a12f3_02112026.png?v=648a12f3e973)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q094_04bfcab8_02112026.png?v=04bfcab8e35f)

---

## Q95

Chemistry · inorganic · Coordination Compounds – Practice

The order of energy absorbed which is responsible for the color of complexes (A) $\mathrm{[Ni(H_2O)_2(en)_2]^{2+}}$ (B) $\mathrm{[Ni(H_2O)_4(en)]^{2+}}$ and (C) $\mathrm{[Ni(en)_3]^{2+}}$ is

- (A) $\mathrm{[Ni(H_2O)_2(en)_2]^{2+}}$
- (B) $\mathrm{[Ni(H_2O)_4(en)]^{2+}}$ and
- (C) $\mathrm{[Ni(en)_3]^{2+}}$

- (1) (A) > (B) > (C)
- (2) (C) > (B) > (A)
- **(3)** (C) > (A) > (B)
- (4) (B) > (A) > (C)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Stronger the field strength of ligand, higher will be the energy absorbed by the complex.
2. $\Rightarrow$ ‘en’ has a stronger field strength than ‘$\mathrm{H_2O}$’ according to spectrochemical series
3. $\therefore$ Correct order of energy absorbed will be:
4. $\mathrm{[Ni(en)_3]^{2+}} > \mathrm{[Ni(H_2O)_2(en)_2]^{2+}} > \mathrm{[Ni(H_2O)_4(en)]^{2+}}$
5. i.e. (C) > (A) > (B)

**Solved independently** (answer withheld)

1. In the spectrochemical series $\mathrm{en}$ is a stronger field ligand than $\mathrm{H_2O}$, so replacing $\mathrm{H_2O}$ by $\mathrm{en}$ increases $\Delta_o$.
2. Count the $\mathrm{en}$ ligands: (C) $\mathrm{[Ni(en)_3]^{2+}}$ has 3, (A) $\mathrm{[Ni(H_2O)_2(en)_2]^{2+}}$ has 2, (B) $\mathrm{[Ni(H_2O)_4(en)]^{2+}}$ has 1.
3. Energy absorbed equals $\Delta_o$, so the order is $(C) > (A) > (B)$, which is option $3$.

**Subtopic:** Colour in Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q095_1ea1b56b_02112026.png?v=1ea1b56b810c)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q095_aecd81f0_02112026.png?v=aecd81f0c9c6)

---

## Q96

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Match List-I with List-II.
List-I (Ores) | List-II (Composition)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Haematite | (i) | $\mathrm{Fe_3O_4}$ |
| (b) | Magnetite | (ii) | $\mathrm{ZnCO_3}$ |
| (c) | Calamine | (iii) | $\mathrm{Fe_2O_3}$ |
| (d) | Kaolinite | (iv) | $\mathrm{[Al_2(OH)_4Si_2O_5]}$ |

- (1) (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)
- **(2)** (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)
- (3) (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)
- (4) (a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (Ores) (Composition)
2. (a) Haematite $\rightarrow$ $\mathrm{Fe_2O_3}$
3. (b) Magnetite $\rightarrow$ $\mathrm{Fe_3O_4}$
4. (c) Calamine $\rightarrow$ $\mathrm{ZnCO_3}$
5. (d) Kaolinite $\rightarrow$ $\mathrm{[Al_2(OH)_4Si_2O_5]}$

**Solved independently** (answer withheld)

1. Haematite is $\mathrm{Fe_2O_3}$ (iii), magnetite is $\mathrm{Fe_3O_4}$ (i), calamine is $\mathrm{ZnCO_3}$ (ii) and kaolinite is $\mathrm{[Al_2(OH)_4Si_2O_5]}$ (iv), which is option $2$.

**Subtopic:** Occurrence of Metals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q096_40c347c9_02112026.png?v=40c347c97868)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q096_50cf52ba_02112026.png?v=50cf52ba359a)

---

## Q97

Chemistry · inorganic · The D- and F-Block Elements – Practice

In the neutral or faintly alkaline medium, $\mathrm{KMnO_4}$ oxidises iodide into iodate. The change in oxidation state of manganese in this reaction is from

- **(1)** $+7$ to $+4$
- (2) $+6$ to $+4$
- (3) $+7$ to $+3$
- (4) $+6$ to $+5$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In neutral or faintly alkaline solution.
2. $2\overset{+7}{\mathrm{Mn}}\mathrm{O_4^-} + \mathrm{H_2O} + \underset{(\text{iodide})}{\overset{-1}{\mathrm{I^-}}} \rightarrow 2\overset{+4}{\mathrm{Mn}}\mathrm{O_2} + 2\mathrm{OH^-} + \underset{(\text{iodate})}{\overset{+5}{\mathrm{I}}\mathrm{O_3^-}}$
3. Manganese ($\mathrm{Mn}$) oxidation state change from $+7$ to $+4$.

**Solved independently** (answer withheld)

1. In neutral or faintly alkaline medium, $\mathrm{MnO_4^-}$ is reduced to $\mathrm{MnO_2}$: $2\mathrm{MnO_4^-} + \mathrm{I^-} + \mathrm{H_2O} \rightarrow 2\mathrm{MnO_2} + \mathrm{IO_3^-} + 2\mathrm{OH^-}$.
2. Oxidation state of Mn in $\mathrm{KMnO_4}$: $+1 + x + 4(-2) = 0 \Rightarrow x = +7$.
3. Oxidation state of Mn in $\mathrm{MnO_2}$: $x + 2(-2) = 0 \Rightarrow x = +4$.
4. Change is $+7$ to $+4$, which is option $1$.

**Subtopic:** Potassium Permanganate (KMnO4) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q097_825c4577_02112026.png?v=825c4577e32f)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q097_55e712ce_02112026.png?v=55e712ce60f8)

---

## Q98

Chemistry · organic · Hydrocarbons

Compound X on reaction with $\mathrm{O_3}$ followed by $\mathrm{Zn/H_2O}$ gives formaldehyde and 2-methyl propanal as products. The compound X is

- **(1)** 3-Methylbut-1-ene
- (2) 2-Methylbut-1-ene
- (3) 2-Methylbut-2-ene
- (4) Pent-2-ene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: 2-Methylpropanal; Formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q098_sol_1_4b8f6b7b_02112026.png?v=4b8f6b7bc035)

*2-Methylpropanal; Formaldehyde*

![drawn: 2-Methylpropanal; Formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q098_solution_1_5eb5c5f2_02112026.svg?v=5eb5c5f2f589)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. The given reaction is the reductive ozonolysis of an alkene. The alkene will be

![printed figure: 3-methylbut-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q098_sol_2_b9274feb_02112026.png?v=b9274feb3002)

*3-methylbut-1-ene*

![drawn: 3-methylbut-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q098_solution_2_bf651f87_02112026.svg?v=bf651f877a83)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 3-Methylbut-1-ene →((i) $\ce{O3}$; (ii) $\ce{Zn/H2O}$) 2-methylpropanal + formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q098_sol_3_40914308_02112026.png?v=409143080327)

*3-Methylbut-1-ene →[(i) $\ce{O3}$; (ii) $\ce{Zn/H2O}$] 2-methylpropanal + formaldehyde*

![drawn: 3-Methylbut-1-ene →((i) $\ce{O3}$; (ii) $\ce{Zn/H2O}$) 2-methylpropanal + formaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q098_solution_3_b3effec2_02112026.svg?v=b3effec25c27)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Reductive ozonolysis splits the $\mathrm{C=C}$ bond and turns each alkene carbon into a $\mathrm{C=O}$ group.
2. Formaldehyde $\mathrm{HCHO}$ comes from a terminal $\mathrm{=CH_2}$ group, and 2-methylpropanal $\mathrm{(CH_3)_2CH{-}CHO}$ comes from a $\mathrm{=CH{-}CH(CH_3)_2}$ fragment.
3. Join the two carbonyl carbons with a double bond: $\mathrm{CH_2{=}CH{-}CH(CH_3)_2}$.
4. $\mathrm{CH_2{=}CH{-}CH(CH_3)_2}$ is 3-methylbut-1-ene, which is option $1$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q098_e3654ea9_02112026.png?v=e3654ea9e933)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q098_e3356b15_02112026.png?v=e3356b15a75d)

---

## Q99

Chemistry · physical · Chemical Equilibrium

$\mathrm{3O_2(g) \rightleftharpoons 2O_3(g)}$
for the above reaction at $298\,\mathrm{K}$, $K_\mathrm{C}$ is found to be $3.0 \times 10^{-59}$. If the concentration of $\mathrm{O_2}$ at equilibrium is $0.040\,\mathrm{M}$ then concentration of $\mathrm{O_3}$ in M is

- **(1)** $4.38 \times 10^{-32}$
- (2) $1.9 \times 10^{-63}$
- (3) $2.4 \times 10^{31}$
- (4) $1.2 \times 10^{21}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{3O_2(g) \rightleftharpoons 2O_3(g)}$
2. $K_\mathrm{C} = \frac{[\mathrm{O_3}]^{2}}{[\mathrm{O_2}]^{3}}$
3. $[\mathrm{O_3}]^{2} = K_\mathrm{C}[\mathrm{O_2}]^{3} = 3 \times 10^{-59} \times (0.04)^{3}$
4. $[\mathrm{O_3}]^{2} = 1.9 \times 10^{-63} = 19 \times 10^{-64}$
5. $[\mathrm{O_3}] = 4.38 \times 10^{-32}$
6. Concentration of $\mathrm{O_3}$ at equilibrium $= 4.38 \times 10^{-32}\,\mathrm{M}$

**Solved independently** (answer withheld)

1. $K_C = \frac{[\mathrm{O_3}]^2}{[\mathrm{O_2}]^3}$.
2. $[\mathrm{O_2}]^3 = (0.040)^3 = 6.4 \times 10^{-5}$.
3. $[\mathrm{O_3}]^2 = 3.0 \times 10^{-59} \times 6.4 \times 10^{-5} = 1.92 \times 10^{-63} = 19.2 \times 10^{-64}$.
4. $[\mathrm{O_3}] = \sqrt{19.2} \times 10^{-32} \approx 4.38 \times 10^{-32}\,\mathrm{M}$, which is option $1$.

**Subtopic:** Calculating Equilibrium Concentrations · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q099_2155f86f_02112026.png?v=2155f86f1bd8)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q099_53e6a686_02112026.png?v=53e6a686220b)

---

## Q100

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Which one of the following is not formed when acetone reacts with 2-pentanone in the presence of dilute $\mathrm{NaOH}$ followed by heating?

- (1) 4-methylpent-3-en-2-one `CC(=O)C=C(C)C` ![4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_option_1_s1_15fe930f_02112026.svg?v=15fe930f4a06)
- **(2)** 5-ethyl-4-methylhept-4-en-3-one `CCC(=O)C(C)=C(CC)CC` ![5-ethyl-4-methylhept-4-en-3-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_option_2_s1_1bfa134b_02112026.svg?v=1bfa134bd650)
- (3) 4-methylhept-3-en-2-one `CCCC(C)=CC(C)=O` ![4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_option_3_s1_cb45c8ef_02112026.svg?v=cb45c8efc96c)
- (4) 3-ethyl-4-methylpent-3-en-2-one `CCC(C(C)=O)=C(C)C` ![3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_option_4_s1_66feab5b_02112026.svg?v=66feab5b6d50)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Cross Aldol condensation reaction:
2. Both reactants contain $\alpha$-Hydrogens, so multiple products are possible which are as follows:

![printed figure: propan-2-one + pentan-2-one →(dil NaOH, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_1_d7be0700_02112026.png?v=d7be070029cc)

*propan-2-one + pentan-2-one →[dil NaOH, Δ]*

![drawn: propan-2-one + pentan-2-one →(dil NaOH, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_1_ac7a4928_02112026.svg?v=ac7a4928d157)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 1. 4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_2_eb0f4572_02112026.png?v=eb0f457227f4)

*1. 4-methylhept-3-en-2-one*

![drawn: 1. 4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_2_61d1bc27_02112026.svg?v=61d1bc27d125)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 2. 2-methylhept-2-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_3_19cf2570_02112026.png?v=19cf25705641)

*2. 2-methylhept-2-en-4-one*

![drawn: 2. 2-methylhept-2-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_3_25399d64_02112026.svg?v=25399d64b68c)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 3. 3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_4_323095e4_02112026.png?v=323095e46091)

*3. 3-ethyl-4-methylpent-3-en-2-one*

![drawn: 3. 3-ethyl-4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_4_7340308d_02112026.svg?v=7340308d3d28)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 4. 4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_5_8a07951d_02112026.png?v=8a07951da601)

*4. 4-methylpent-3-en-2-one*

![drawn: 4. 4-methylpent-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_5_20886cd7_02112026.svg?v=20886cd7232d)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 5. 6-methylnon-5-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_6_fffbef07_02112026.png?v=fffbef075910)

*5. 6-methylnon-5-en-4-one*

![drawn: 5. 6-methylnon-5-en-4-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_6_fbf8996f_02112026.svg?v=fbf8996f2f01)  
*drawn by RDKit (code/lib/chem_cards.py)*


![printed figure: 6. 3-ethyl-4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q100_sol_7_ed7f9b95_02112026.png?v=ed7f9b955c94)

*6. 3-ethyl-4-methylhept-3-en-2-one*

![drawn: 6. 3-ethyl-4-methylhept-3-en-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_drawn/q100_solution_7_139d368c_02112026.svg?v=139d368c6449)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. $\Rightarrow$ (2) is not possible.

**Solved independently** (answer withheld)

1. Reactants: acetone $\mathrm{CH_3COCH_3}$ and 2-pentanone $\mathrm{CH_3COCH_2CH_2CH_3}$; dilute NaOH then heat gives aldol condensation products ($\alpha,\beta$-unsaturated ketones).
2. Acetone self-condensation: $2\,\mathrm{CH_3COCH_3} \rightarrow \mathrm{(CH_3)_2C{=}CHCOCH_3}$, which is option $1$, so it is formed.
3. Acetone enolate $\mathrm{^-CH_2COCH_3}$ adds to the C=O of 2-pentanone and dehydrates: $\mathrm{CH_3COCH{=}C(CH_3)CH_2CH_2CH_3}$, which is option $3$, so it is formed.
4. 2-Pentanone enolate at C-3, $\mathrm{CH_3CO\overset{-}{C}H(C_2H_5)}$, adds to acetone C=O and dehydrates: $\mathrm{CH_3COC(C_2H_5){=}C(CH_3)_2}$, which is option $4$, so it is formed.
5. Option $2$, $\mathrm{CH_3CH_2COC(CH_3){=}C(C_2H_5)_2}$, contains an ethyl ketone $\mathrm{C_2H_5CO-}$ unit that neither acetone nor 2-pentanone can provide, so it is not formed; answer option $2$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 40)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q100_7ba0f87a_02112026.png?v=7ba0f87a7024)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q100_0d9cadb5_02112026.png?v=0d9cadb5f266)

---

## Q101

Biology · botany · Biodiversity and Conservation

Which of the following is not a method of ex situ conservation?

- (1) In vitro fertilization
- **(2)** National Parks
- (3) Micropropagation
- (4) Cryopreservation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In-situ conservation means on site conservation i.e. when we conserve and protect the whole ecosystem, its biodiversity at all levels is protected.
2. National parks are type of in-situ conservation.
3. Whereas, micropropagation, cryopreservation and in-vitro fertilisation are methods of ex-situ conservation.

**Solved independently** (answer withheld)

1. National Parks conserve organisms in their natural habitat, which is in situ conservation, whereas in vitro fertilization, micropropagation and cryopreservation are ex situ methods, so the answer is option $2$.

**Subtopic:** Ex Situ Conservation, In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q101_fd566da2_02112026.png?v=fd566da29749)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q101_41dc0f93_02112026.png?v=41dc0f93b84c)

---

## Q102

Biology · botany · Morphology of Flowering Plants

Identify the correct set of statements : Choose the correct answer from the options given below :

- (a) The leaflets are modified into pointed hard thorns in Citrus and Bougainvillea
- (b) Axillary buds form slender and spirally coiled tendrils in cucumber and pumpkin
- (c) Stem is flattened and fleshy in Opuntia and modified to perform the function of leaves
- (d) Rhizophora shows vertically upward growing roots that help to get oxygen for respiration
- (e) Subaerially growing stems in grasses and strawberry help in vegetative propagation

- (1) (b) and (c) Only
- (2) (a) and (d) Only
- **(3)** (b), (c), (d) and (e) Only
- (4) (a), (b), (d) and (e) Only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Axillary buds of stems get modified into woody, straight and pointed thorns.
2. Thorns are found in many plants such as Citrus and Bougainvillea.

**Solved independently** (answer withheld)

1. (a) is false: in $Citrus$ and $Bougainvillea$ the thorns are modified axillary buds (stem modification), not leaflets.
2. (b) is true: stem tendrils arising from axillary buds are slender and spirally coiled in cucumber and pumpkin.
3. (c) is true: $Opuntia$ has a flattened, fleshy green stem (phylloclade) that performs the function of leaves.
4. (d) is true: $Rhizophora$ has pneumatophores, roots growing vertically upward to obtain oxygen for respiration.
5. (e) is true: subaerially growing stems (runners/stolons) in grasses and strawberry help in vegetative propagation.
6. Correct set is (b), (c), (d) and (e) only, which is option $3$.

**Subtopic:** The Stem, The Root · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q102_3d4090bf_02112026.png?v=3d4090bff60a)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q102_10c95997_02112026.png?v=10c9599720f7)

---

## Q103

Biology · botany · Ecosystem

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Decomposition is a process in which the detritus is degraded into simpler substances by microbes.
- (Statement II) Decomposition is faster if the detritus is rich in lignin and chitin.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Decomposition is the process by which decomposers breakdown complex organic matter into inorganic substances.
2. The rate of decomposition is controlled by chemical composition of detritus and climatic factors.
3. Decomposition is slower if detritus is rich in lignin and chitin and quicker, if detritus is rich in nitrogen and water soluble substances like sugars.

**Solved independently** (answer withheld)

1. Statement I: decomposers (microbes) break down detritus into simpler inorganic substances, so Statement I is correct.
2. Statement II: decomposition is slower, not faster, when detritus is rich in lignin and chitin, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect, which is option $3$.

**Subtopic:** Decomposition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q103_703454af_02112026.png?v=703454afad96)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q103_5e0d1c7b_02112026.png?v=5e0d1c7bb505)

---

## Q104

Biology · botany · Plant Kingdom

Hydrocolloid carrageen is obtained from:

- (1) Chlorophyceae and Phaeophyceae
- (2) Phaeophyceae and Rhodophyceae
- **(3)** Rhodophyceae only
- (4) Phaeophyceae only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Hydrocolloids are water holding substances for eg. carrageen obtained from red algae (Rhodophyceae).

**Solved independently** (answer withheld)

1. NCERT Class 11 states that algin is obtained from brown algae (Phaeophyceae) and carrageen from red algae (Rhodophyceae), so carrageen comes from $\text{Rhodophyceae}$ only, which is option $3$.

**Subtopic:** Rhodophyceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q104_3370b25b_02112026.png?v=3370b25beb84)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q104_6402bfa5_02112026.png?v=6402bfa57778)

---

## Q105

Biology · botany · Morphology of Flowering Plants

Which one of the following plants shows vexillary aestivation and diadelphous stamens?

- (1) Colchicum autumnale
- **(2)** Pisum sativum
- (3) Allium cepa
- (4) Solanum nigrum

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Vexillary aestivation and diadelphous stamens are the characteristic features of family Fabaceae.
2. Pisum sativum (garden pea) belongs to family Fabaceae.
3. Allium cepa (onion) and Colchicum autumnale (colchicine) belong to family Liliaceae.
4. Solanum nigrum belongs to Solanaceae.

**Solved independently** (answer withheld)

1. Vexillary aestivation and diadelphous stamens $(9)+1$ are characteristic of Fabaceae; Pisum sativum belongs to Fabaceae, while Colchicum and Allium are Liliaceae and Solanum is Solanaceae, so the answer is option $2$.

**Subtopic:** Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q105_2872575a_02112026.png?v=2872575a63c3)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q105_da7addc6_02112026.png?v=da7addc6f006)

---

## Q106

Biology · botany · Plant Kingdom

Which of the following is incorrectly matched?

- (1) Ectocarpus – Fucoxanthin
- **(2)** Ulothrix – Mannitol
- (3) Porphyra – Floridian Starch
- (4) Volvox – Starch

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ulothrix is a member of Chlorophyceae (green algae), with reserve food material, starch.
2. Mannitol is stored food material of Phaeophyceae (brown algae).

**Solved independently** (answer withheld)

1. $\text{Ectocarpus}$ is a brown alga (Phaeophyceae) whose characteristic pigment is fucoxanthin, so option $1$ is correctly matched.
2. $\text{Ulothrix}$ is a green alga (Chlorophyceae) whose reserve food is starch; mannitol is stored by brown algae, so option $2$ is incorrectly matched.
3. $\text{Porphyra}$ is a red alga (Rhodophyceae) storing floridean starch, so option $3$ is correctly matched.
4. $\text{Volvox}$ is a green alga storing starch, so option $4$ is correctly matched.
5. The only incorrect pair is option $2$.

**Subtopic:** Chlorophyceae, Phaeophyceae · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q106_162ea16d_02112026.png?v=162ea16d8ef9)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q106_885dc649_02112026.png?v=885dc6497953)

---

## Q107

Biology · botany · Molecular Basis of Inheritance

The process of translation of mRNA to proteins begins as soon as :

- **(1)** The small subunit of ribosome encounters mRNA
- (2) The larger subunit of ribosome encounters mRNA
- (3) Both the subunits join together to bind with mRNA
- (4) The tRNA is activated and the larger subunit of ribosome encounters mRNA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. When the small subunit of ribosome encounters an mRNA, the process of translation of the mRNA to protein begins.
2. This process is followed by the binding of bigger/larger subunit.
3. t-RNA is activated by the addition of amino acid prior to the attachment of ribosome, in the first phase.

**Solved independently** (answer withheld)

1. An inactive ribosome exists as two separate subunits, and translation of mRNA into protein begins as soon as the small subunit encounters the mRNA, which is option $1$.

**Subtopic:** Translation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q107_921c25e4_02112026.png?v=921c25e4a48f)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q107_8402edd7_02112026.png?v=8402edd7c1a5)

---

## Q108

Biology · botany · Mineral Nutrition

Match List-I with List-II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Manganese | (i) | Activates the enzyme catalase |
| (b) | Magnesium | (ii) | Required for pollen germination |
| (c) | Boron | (iii) | Activates enzymes of respiration |
| (d) | Iron | (iv) | Functions in splitting of water during photosynthesis |

- (1) (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)
- **(2)** (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)
- (3) (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii
- (4) (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Manganese plays a major role in the splitting of water to liberate oxygen during photosynthesis.
2. Magnesium activates several enzymes involved in photosynthesis and respiration.
3. Boron is involved in pollen germination.
4. Iron activates the catalase and some other enzymes.

**Solved independently** (answer withheld)

1. Manganese is needed for the photolysis (splitting) of water during photosynthesis, so (a)-(iv).
2. Magnesium activates enzymes of respiration and photosynthesis, so (b)-(iii).
3. Boron is required for pollen germination, so (c)-(ii).
4. Iron activates the enzyme catalase, so (d)-(i).
5. The match (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i) is option $2$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q108_b83e4d8f_02112026.png?v=b83e4d8f24e7)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q108_11e6201e_02112026.png?v=11e6201e5304)

---

## Q109

Biology · botany · Cell Cycle and Cell Division

Which one of the following never occurs during mitotic cell division?

- (1) Spindle fibres attach to kinetochores of chromosomes
- (2) Movement of centrioles towards opposite poles
- **(3)** Pairing of homologous chromosomes
- (4) Coiling and condensation of the chromatids

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pairing of homologous chromosomes occurs during prophase I of meiosis.
2. Coiling and condensation of chromatids, spindle fibres attachment to the kinetochores and movement of centrioles towards opposite poles occur in both mitosis and meiosis.

**Solved independently** (answer withheld)

1. Homologous chromosome pairing (synapsis) happens only in zygotene of meiosis I, so it never occurs in mitosis; options 1, 2 and 4 all occur in mitosis, so the answer is option $3$.

**Subtopic:** Prophase and Metaphase, Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q109_da4836bb_02112026.png?v=da4836bbb48f)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q109_260bd711_02112026.png?v=260bd7111211)

---

## Q110

Biology · botany · Photosynthesis in Higher Plants

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The primary $\mathrm{CO_2}$ acceptor in $\mathrm{C_4}$ plants is phosphoenolpyruvate and is found in the mesophyll cells.
- (Statement II) Mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCo enzyme.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The primary $\mathrm{CO_2}$ acceptor is a $3$-carbon molecule, phosphoenol pyruvate (PEP) and is present in the mesophyll cells.
2. Mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCO enzyme.

**Solved independently** (answer withheld)

1. Statement I: in $\mathrm{C_4}$ plants the primary $\mathrm{CO_2}$ acceptor is phosphoenolpyruvate (PEP), a 3-carbon molecule found in the mesophyll cells, so it is correct.
2. Statement II: the mesophyll cells of $\mathrm{C_4}$ plants lack RuBisCO, which is present in the bundle sheath cells, so it is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** The C₄ Pathway · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q110_2eb79910_02112026.png?v=2eb7991061d4)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q110_d05a71f4_02112026.png?v=d05a71f4a274)

---

## Q111

Biology · botany · Photosynthesis in Higher Plants

Which one of the following is not true regarding the release of energy during ATP synthesis through chemiosmosis? It involves:

- (1) Breakdown of proton gradient
- **(2)** Breakdown of electron gradient
- (3) Movement of protons across the membrane to the stroma
- (4) Reduction of $\mathrm{NADP}$ to $\mathrm{NADPH_2}$ on the stroma side of the membrane

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient and ATP synthase.
2. Energy is used to pump protons across a membrane to create a gradient or a high concentration of protons within the thylakoid lumen.
3. The $\mathrm{NADP}$ reductase enzyme is located on the stroma side of the membrane.
4. Along with the electrons that come from the acceptor of electrons of PS I, protons are necessary for reduction of $\mathrm{NADP^{+}}$ to $\mathrm{NADPH + H^{+}}$.
5. The process does not involve breaking of electron gradient.

**Solved independently** (answer withheld)

1. In chemiosmosis, a proton gradient forms across the thylakoid membrane; its breakdown, as protons move through CF$_0$ of ATP synthase to the stroma, releases energy for ATP synthesis, so options $1$ and $3$ are true; NADP reductase on the stroma side reduces NADP to NADPH, so option $4$ is true; no electron gradient exists, so option $2$ is not true.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q111_60e2edea_02112026.png?v=60e2edeaeeab)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q111_a4942908_02112026.png?v=a49429082e9d)

---

## Q112

Biology · botany · Biodiversity and Conservation

Habitat loss and fragmentation, over exploitation, alien species invasion and co-extinction are causes for:

- (1) Population explosion
- (2) Competition
- **(3)** Biodiversity loss
- (4) Natality

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Habitat loss and fragmentation, over exploitation, alien species invasion and co-extinction are causes for biodiversity loss.

**Solved independently** (answer withheld)

1. Habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions are the 'Evil Quartet', the four major causes of biodiversity loss, which is option $3$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q112_73fbefd0_02112026.png?v=73fbefd0c8bc)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q112_963a7590_02112026.png?v=963a759087ad)

---

## Q113

Biology · botany · Respiration in Plants

What is the net gain of ATP when each molecule of glucose is converted to two molecules of pyruvic acid?

- (1) Four
- (2) Six
- **(3)** Two
- (4) Eight

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. During glycolysis, total $4$ ATPs are produced from one glucose molecule with a net gain of $2$ ATPs.

**Solved independently** (answer withheld)

1. Glycolysis converts one glucose into two pyruvic acid molecules and uses $2$ ATP (hexokinase and phosphofructokinase steps).
2. It forms $4$ ATP by substrate-level phosphorylation ($2$ per triose).
3. Net gain $= 4 - 2 = 2$ ATP, which is option $3$ (Two).

**Subtopic:** Glycolysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q113_373c914b_02112026.png?v=373c914b6c58)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q113_2175eb19_02112026.png?v=2175eb19df0e)

---

## Q114

Biology · botany · Transport in Plants

“Girdling Experiment” was performed by Plant Physiologists to identify the plant tissue through which:

- (1) water is transported
- **(2)** food is transported
- (3) for both water and food transportation
- (4) osmosis is observed

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The girdling experiment shows that phloem is the tissue responsible for translocation of food; and that transport takes place in one direction i.e. towards the root.

**Solved independently** (answer withheld)

1. Girdling removes a ring of bark including phloem but leaves xylem intact; food accumulates above the ring and tissue below starves, showing phloem transports food (option $2$).

**Subtopic:** Phloem Transport: Flow from Source to Sink · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q114_f50ac61b_02112026.png?v=f50ac61b3085)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q114_a5550afd_02112026.png?v=a5550afd364e)

---

## Q115

Biology · botany · Transport in Plants

Which of the following is not observed during apoplastic pathway ?

- (1) Movement of water occurs through intercellular spaces and wall of the cells
- (2) The movement does not involve crossing of cell membrane
- **(3)** The movement is aided by cytoplasmic streaming
- (4) Apoplast is continuous and does not provide any barrier to water movement

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The symplastic system is system of interconnected protoplasts.
2. Neighbouring cells are connected through cytoplasmic strands that extend through plasmodesmata.
3. The water travels through cell cytoplasm and plasmodesmata, hence the movement is relatively slower.
4. Symplastic movement is aided by cytoplasmic streaming.

**Solved independently** (answer withheld)

1. The apoplastic pathway moves water through cell walls and intercellular spaces without crossing any membrane, and the apoplast is continuous, so options $1$, $2$ and $4$ are observed; cytoplasmic streaming aids only the symplastic pathway, so option $3$ is not observed.

**Subtopic:** Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q115_3b19b135_02112026.png?v=3b19b135c2fd)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q115_8b6becc7_02112026.png?v=8b6becc7d992)

---

## Q116

Biology · botany · Plant Growth and Development

Which one of the following plants does not show plasticity?

- (1) Cotton
- (2) Coriander
- (3) Buttercup
- **(4)** Maize

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Plants follow different pathways in response to environment or phases of life to form different kinds of structures.
2. This ability is called plasticity e.g. heterophylly in cotton, coriander and larkspur.
3. In such plants, leaves of juvenile plant are different in a shape from those in mature plants.
4. Maize does not show plasticity.

**Solved independently** (answer withheld)

1. Plasticity (heterophylly) is shown by cotton, coriander, larkspur and buttercup per NCERT, while maize shows no heterophylly, so the answer is option $4$.

**Subtopic:** Development and Plasticity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q116_057a6b44_02112026.png?v=057a6b445a35)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q116_90670b38_02112026.png?v=90670b38c257)

---

## Q117

Biology · botany · Molecular Basis of Inheritance

DNA polymorphism forms the basis of :

- (1) Genetic mapping
- (2) DNA finger printing
- **(3)** Both genetic mapping and DNA finger printing
- (4) Translation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Polymorphism in $\mathrm{DNA}$ sequence is the basis of genetic mapping of human genome as well as of $\mathrm{DNA}$ fingerprinting.

**Solved independently** (answer withheld)

1. DNA polymorphism (inheritable variation in DNA sequence, such as VNTRs/satellite DNA) forms the basis of genetic mapping of the human genome as well as of DNA fingerprinting, so option $3$.

**Subtopic:** DNA Fingerprinting · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q117_08e9c5f8_02112026.png?v=08e9c5f8ffab)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q117_5dcc1aaf_02112026.png?v=5dcc1aafd06e)

---

## Q118

Biology · botany · Principles of Inheritance and Variation

XO type of sex determination can be found in :

- (1) Drosophila
- (2) Birds
- **(3)** Grasshoppers
- (4) Monkeys

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Grasshopper is an example of XO type of sex determination in which the males have only one X-chromosome besides the autosomes, whereas females have a pair of X-chromosomes.

**Solved independently** (answer withheld)

1. In XO sex determination males carry a single X chromosome and no Y ($XO$), while females are $XX$; this is seen in grasshoppers, so the answer is option $3$ (Drosophila and monkeys are $XY$, birds are $ZW$).

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q118_fdd5173f_02112026.png?v=fdd5173f75a9)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q118_38310cc6_02112026.png?v=38310cc69da6)

---

## Q119

Biology · botany · Biotechnology: Principles and Processes

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below :

- Assertion (A) Polymerase chain reaction is used in DNA amplification.
- Reason (R) The ampicillin resistant gene is used as a selectable marker to check transformation

- (1) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- **(2)** Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- (3) (A) is correct but (R) is not correct
- (4) (A) is not correct but (R) is correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because both the statements are correct but the given reason is not the correct explanation.
2. Polymerase chain reaction is used in DNA amplification.
3. Ampicillin resistance gene is a selectable marker that helps to check transformation by selection of transformants.

**Solved independently** (answer withheld)

1. Polymerase chain reaction makes many copies of a target DNA segment, so (A) is correct.
2. The ampicillin resistance gene (e.g. $amp^R$ in pBR322) is used as a selectable marker to identify transformants, so (R) is correct.
3. Selection of transformants by antibiotic resistance has no bearing on how PCR amplifies DNA, so (R) is not the explanation of (A): option $2$.

**Subtopic:** Amplification of Gene of Interest Using PCR, ORI and Selectable Marker · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q119_4504c74e_02112026.png?v=4504c74e7028)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q119_694322b3_02112026.png?v=694322b39e5a)

---

## Q120

Biology · botany · Plant Growth and Development

The gaseous plant growth regulator is used in plants to :

- (1) speed up the malting process
- **(2)** promote root growth and roothair formation to increase the absorption surface
- (3) help overcome apical dominance
- (4) kill dicotyledonous weeds in the fields

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ethylene is a gaseous plant hormone.
2. It induces development of adventitious roots on various types of cutting.
3. It promotes the development of lateral roots and growth of root hairs.
4. Cytokinin helps to overcome the apical dominance.
5. Auxin is used to kill dicot weeds.
6. Gibberellin speeds up the malting process

**Solved independently** (answer withheld)

1. The only gaseous plant growth regulator is ethylene; per NCERT it promotes root growth and root hair formation to increase the absorption surface, while options 1, 3 and 4 describe gibberellins, cytokinins and auxin (2,4-D) respectively, so the answer is option $2$.

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q120_69f73118_02112026.png?v=69f73118fe95)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q120_d870b048_02112026.png?v=d870b048fdaf)

---

## Q121

Biology · botany · Environmental Issues

The device which can remove particulate matter present in the exhaust from a thermal power plant is :

- (1) STP
- (2) Incinerator
- **(3)** Electrostatic Precipitator
- (4) Catalytic Convertor

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Electrostatic precipitator can remove over $99\%$ particulate matter present in the exhaust from a thermal power plant.
2. Catalytic converters are fitted into automobiles for reducing emission of poisonous gases.
3. STPs are associated with sewage treatment.

**Solved independently** (answer withheld)

1. An electrostatic precipitator charges the dust particles in the exhaust and collects them on oppositely charged plates, removing particulate matter from thermal power plant exhaust, which is option $3$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q121_3a382874_02112026.png?v=3a382874bdc0)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q121_b856e12b_02112026.png?v=b856e12b97a1)

---

## Q122

Biology · botany · Sexual Reproduction in Flowering Plants

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Cleistogamous flowers are invariably autogamous
- (Statement II) Cleistogamy is disadvantageous as there is no chance for cross pollination

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cleistogamous flowers does not open at all.
2. In such flowers autogamy occurs.
3. Lack of cross pollination is a disadvantage of cleistogamy.

**Solved independently** (answer withheld)

1. Cleistogamous flowers do not open at all, so anthers and stigma lie close together inside the closed flower.
2. Pollen can reach only the stigma of the same flower, so cleistogamous flowers are invariably autogamous: Statement I is correct.
3. Because the flower never opens, there is no chance of cross-pollination, so no new genetic recombination; this is a disadvantage: Statement II is correct.
4. Both statements correct $\Rightarrow$ option $1$.

**Subtopic:** Pollination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q122_e4e14959_02112026.png?v=e4e14959f1d2)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q122_c43484e6_02112026.png?v=c43484e6536a)

---

## Q123

Biology · botany · Biomolecules

Exoskeleton of arthropods is composed of :

- (1) Cutin
- (2) Cellulose
- **(3)** Chitin
- (4) Glucosamine

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as chitin forms the exoskeleton in arthropods and is found in fungal cell wall.
2. N-acetyl glucosamine is the monomeric unit.
3. Cellulose is a polysaccharide.
4. Cutin is a derived lipid.

**Solved independently** (answer withheld)

1. The arthropod body is covered by a chitinous exoskeleton, so the answer is chitin, option $3$.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q123_ac2be5f3_02112026.png?v=ac2be5f3acbb)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q123_03e4c5e5_02112026.png?v=03e4c5e5a268)

---

## Q124

Biology · botany · Molecular Basis of Inheritance

Read the following statements and choose the set of correct statements :
Choose the correct answer from the options given below :

- (a) Euchromatin is loosely packed chromatin
- (b) Heterochromatin is transcriptionally active
- (c) Histone octomer is wrapped by negatively charged DNA in nucleosome
- (d) Histones are rich in lysine and arginine
- (e) A typical nucleosome contains $400\,\mathrm{bp}$ of DNA helix

- (1) (b), (d), (e) Only
- **(2)** (a), (c), (d) Only
- (3) (b), (e) Only
- (4) (a), (c), (e) Only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Heterochromatin is transcriptionally inactive.
2. A typical nucleosome contains $200\,\mathrm{bp}$ of DNA helix.
3. Euchromatin is the loosely packed chromatin region.
4. The negatively charged DNA is wrapped around the positively charged histone octamer to form a structure called nucleosome.
5. Histones are rich in basic amino acid residues lysine and arginine.

**Solved independently** (answer withheld)

1. (a) Euchromatin is loosely packed chromatin: true.
2. (b) Heterochromatin is densely packed and transcriptionally inactive: false.
3. (c) Negatively charged DNA wraps the positively charged histone octamer in a nucleosome: true.
4. (d) Histones are rich in the basic residues lysine and arginine: true.
5. (e) A typical nucleosome contains $200\,\mathrm{bp}$ of DNA, not $400\,\mathrm{bp}$: false.
6. True set is (a), (c), (d), which is option $2$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q124_24184131_02112026.png?v=24184131d1da)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q124_f5435a62_02112026.png?v=f5435a624b03)

---

## Q125

Biology · botany · Organisms and Populations

Which one of the following statements cannot be connected to Predation?

- (1) It helps in maintaining species diversity in a community
- (2) It might lead to extinction of a species
- **(3)** Both the interacting species are negatively impacted
- (4) It is necessitated by nature to maintain the ecological balance

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. One of the species in predation gains benefit on the expense of the other.
2. Predators help in maintaining species diversity in a community, by reducing the intensity of competition among competing prey species.
3. If a predator is too efficient and overexploits its prey, then the prey might become extinct.

**Solved independently** (answer withheld)

1. Predation is a $(+,-)$ interaction: the predator gains and the prey is harmed; an interaction where both species are harmed $(-,-)$ is competition, so option $3$ cannot be connected to predation.

**Subtopic:** Predation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q125_f59a83a6_02112026.png?v=f59a83a620d4)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q125_0ad4287e_02112026.png?v=0ad4287ed9bf)

---

## Q126

Biology · botany · Morphology of Flowering Plants

The flowers are Zygomorphic in:
Choose the correct answer from the options given below:

- (a) Mustard
- (b) Gulmohar
- (c) Cassia
- (d) Datura
- (e) Chilly

- (1) (a), (b), (c) Only
- **(2)** (b), (c) Only
- (3) (d), (e) Only
- (4) (c), (d), (e) Only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When a flower can be divided into two similar halves only in one particular vertical plane, it is zygomorphic for e.g. pea, gulmohar, bean, Cassia.
2. Mustard, Datura and Chilli show actinomorphic flowers.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Morphology of Flowering Plants) gives mustard, datura and chilli as examples of actinomorphic flowers, so (a), (d) and (e) are not zygomorphic.
2. The same text gives pea, gulmohur, bean and Cassia as examples of zygomorphic flowers, so (b) and (c) are zygomorphic.
3. Only (b) and (c) are zygomorphic, which is option $2$.

**Subtopic:** The Flower · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 46)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q126_9297842e_02112026.png?v=9297842e6571)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q126_ffe0488f_02112026.png?v=ffe0488f5c35)

---

## Q127

Biology · botany · Mineral Nutrition

Which one of the following produces nitrogen fixing nodules on the roots of Alnus?

- (1) Rhizobium
- **(2)** Frankia
- (3) Rhodospirillum
- (4) Beijerinckia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The microbe, Frankia, produces nitrogen fixing nodules on the roots of non-leguminous plants (e.g. Alnus)

**Solved independently** (answer withheld)

1. Nitrogen-fixing nodules on the roots of the non-leguminous plant $Alnus$ are formed by the actinomycete $Frankia$, which is option $2$.

**Subtopic:** Nitrogen Fixation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q127_cc9ba600_02112026.png?v=cc9ba60001fb)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q127_8ccba729_02112026.png?v=8ccba7294044)

---

## Q128

Biology · botany · Anatomy of Flowering Plants

> ⚠ The booklet prints "Answer (NA) No option is correct": none of the four options is correct as printed, so there is no keyed answer to check a solve against.

> ⚠ The printed solution says "All the statements are correct regarding vascular bundles but none of the options with such combination is given.": the question has no correct option as printed, and the printed answer comes from a corrected reading.

> ⚠ The independent solve found no printed option exactly right ("No option lists exactly the set of true statements: by NCERT all five statements (a)-(e) are true, but every option omits at least one"); its pick (unsure) is the closest fit, so treat this question as possibly misprinted.

Read the following statements about the vascular bundles : Choose the correct answer from the options given below :

- (a) In roots, xylem and phloem in a vascular bundle are arranged in an alternate manner along the different radii.
- (b) Conjoint closed vascular bundles do not possess cambium
- (c) In open vascular bundles, cambium is present in between xylem and phloem
- (d) The vascular bundles of dicotyledonous stem possess endarch protoxylem
- (e) In monocotyledonous root, usually there are more than six xylem bundles present

- (1) (a), (b) and (d) Only
- (2) (b), (c), (d) and (e) Only
- (3) (a), (b), (c) and (d) Only
- (4) (a), (c), (d) and (e) Only

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

**Printed in the booklet** (page 46)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q128_d31e3a2c_02112026.png?v=d31e3a2c8843)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q128_1f1ffe35_02112026.png?v=1f1ffe354baf)

---

## Q129

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the incorrect statement related to Pollination :

- (1) Pollination by water is quite rare in flowering plants
- (2) Pollination by wind is more common amongst abiotic pollination
- (3) Flowers produce foul odours to attract flies and beetles to get pollinated
- **(4)** Moths and butterflies are the most dominant pollinating agents among insects

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Among the animals, insects, particularly bees are the dominant biotic pollinating agents.

**Solved independently** (answer withheld)

1. Statement 1: pollination by water is quite rare in flowering plants (about 30 genera, mostly monocots) $\Rightarrow$ correct.
2. Statement 2: among abiotic agents, wind pollination is more common than water pollination $\Rightarrow$ correct.
3. Statement 3: some flowers produce foul odours to attract flies and beetles for pollination $\Rightarrow$ correct.
4. Statement 4: among insects, bees are the dominant pollinating agents, not moths and butterflies $\Rightarrow$ incorrect, so the answer is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q129_815092c9_02112026.png?v=815092c9e876)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q129_c1b9c0d3_02112026.png?v=c1b9c0d3e714)

---

## Q130

Biology · botany · Biotechnology: Principles and Processes

Which one of the following statement is not true regarding gel electrophoresis technique?

- (1) The process of extraction of separated DNA strands from gel is called elution.
- (2) The separated DNA fragments are stained by using ethidium bromide.
- **(3)** The presence of chromogenic substrate gives blue coloured DNA bands on the gel.
- (4) Bright orange coloured bands of DNA can be observed in the gel when exposed to UV light.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the incorrect statement, as bright colored bands of DNA can be observed in the gel when EtBr (Ethidium bromide) treated DNA is exposed to UV light.

**Solved independently** (answer withheld)

1. Elution (1), ethidium bromide staining (2) and bright orange bands under UV light (4) are all true of gel electrophoresis; a chromogenic substrate giving blue colour relates to blue-white selection of recombinant colonies, not to DNA bands on a gel, so statement $3$ is not true.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q130_ab1f2527_02112026.png?v=ab1f252749ac)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q130_9eb3479d_02112026.png?v=9eb3479d1abb)

---

## Q131

Biology · botany · Plant Growth and Development

Production of Cucumber has increased manifold in recent years. Application of which of the following phytohormones has resulted in this increased yield as the hormone is known to produce female flowers in the plants :

- (1) ABA
- (2) Gibberellin
- **(3)** Ethylene
- (4) Cytokinin

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ethylene increases the number of female flowers and fruits in certain plants such as cucumber.
2. Gibberellins are used to increase the size of fruits in some plants.

**Solved independently** (answer withheld)

1. Ethylene is the phytohormone that promotes female flowers in cucumbers and so increases yield, which is option $3$.

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q131_35e6474e_02112026.png?v=35e6474ea614)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q131_d5465ae1_02112026.png?v=d5465ae176a9)

---

## Q132

Biology · botany · Respiration in Plants

What amount of energy is released from glucose during lactic acid fermentation?

- (1) Approximately $15\%$
- (2) More than $18\%$
- (3) About $10\%$
- **(4)** Less than $7\%$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Less than seven percent of the energy in glucose is released during lactic acid fermentation and not all of it is trapped as high energy bonds of ATP.

**Solved independently** (answer withheld)

1. In fermentation glucose is only partly oxidised, so less than $7\%$ of its energy is released, which is option $4$.

**Subtopic:** Fermentation and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q132_5b9d0e24_02112026.png?v=5b9d0e2461f7)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q132_4f1110f8_02112026.png?v=4f1110f82298)

---

## Q133

Biology · botany · Anatomy of Flowering Plants

In old trees the greater part of secondary xylem is dark brown and resistant to insect attack due to : Choose the correct answer from the options given below:

- (a) secretion of secondary metabolities and their deposition in the lumen of vessels.
- (b) deposition of organic compounds like tannins and resins in the central layers of stem.
- (c) deposition of suberin and aromatic substances in the outer layer of stem.
- (d) deposition of tannins, gum, resin and aromatic substances in the peripheral layers of stem.
- (e) presence of parenchyma cells, functionally active xylem elements and essential oils.

- **(1)** (a) and (b) Only
- (2) (c) and (d) Only
- (3) (d) and (e) Only
- (4) (b) and (d) Only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In old trees, the greater part of secondary xylem is dark brown due to deposition of organic compounds like tannins, resins, oils, gums, aromatic substances and essential oils in the central or innermost layers of the stem.
2. These substances make it hard, durable and resistant to the attacks of micro-organisms and insects.

**Solved independently** (answer withheld)

1. The dark, insect-resistant inner part of old secondary xylem is heartwood.
2. Heartwood is dark because organic compounds such as tannins, resins, oils, gums and aromatic substances (secondary metabolites) are deposited in it, filling the lumen of its vessels, so $(a)$ and $(b)$ are true.
3. These deposits are in the central (innermost) layers, not the outer or peripheral layers, so $(c)$ and $(d)$ are false.
4. Living parenchyma and functionally active xylem elements describe sapwood, so $(e)$ is false.
5. Only $(a)$ and $(b)$ are correct, which is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q133_9d53531e_02112026.png?v=9d53531e5367)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q133_8211bc82_02112026.png?v=8211bc82755c)

---

## Q134

Biology · botany · Cell Cycle and Cell Division

The appearance of recombination nodules on homologous chromosomes during meiosis characterizes :

- (1) Synaptonemal complex
- (2) Bivalent
- **(3)** Sites at which crossing over occurs
- (4) Terminalization

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pachytene stage of meiosis is characterised by the appearance of recombination nodules, the sites at which crossing over occurs between non sister chromatids of homologous chromosomes.

**Solved independently** (answer withheld)

1. In pachytene of prophase I, NCERT describes the appearance of recombination nodules as marking the sites at which crossing over occurs between non-sister chromatids of homologous chromosomes, which is option $3$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q134_0796f57a_02112026.png?v=0796f57a04d3)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q134_5ad1d121_02112026.png?v=5ad1d1215866)

---

## Q135

Biology · botany · Principles of Inheritance and Variation

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Mendel studied seven pairs of contrasting traits in pea plants and proposed the Laws of Inheritance.
- (Statement II) Seven characters examined by Mendel in his experiment on pea plants were seed shape and colour, flower colour, pod shape and colour, flower position and stem height.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Gregor J. Mendel, conducted hybridisation experiments on garden peas and selected $14$ true breeding pea plant varieties (seven contrasting traits).
2. Contrasting traits studied were smooth or wrinkled seeds, yellow or green seeds, inflated on constricted pods, green or yellow pods, tall or dwarf plants, violet or white flowers and axial or terminal flower positions.

**Solved independently** (answer withheld)

1. Statement I: Mendel worked with $7$ pairs of contrasting traits in garden pea and proposed the Laws of Inheritance, so it is correct.
2. Statement II lists seed shape, seed colour, flower colour, pod shape, pod colour, flower position and stem height, which is $7$ characters matching Mendel's set, so it is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Contrasting Traits Studied by Mendel in Pea · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q135_ae0cc4be_02112026.png?v=ae0cc4be9769)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q135_9c5622fb_02112026.png?v=9c5622fb87b5)

---

## Q136

Biology · botany · Biotechnology and Its Applications

Transposons can be used during which one of the following ?

- (1) Polymerase Chain Reaction
- **(2)** Gene Silencing
- (3) Autoradiography
- (4) Gene sequencing

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer as the source of the complementary RNA for RNAi could be mobile genetic elements (transposons) that replicate via an RNA intermediate.
2. Option (3) is incorrect as autoradiography usally follows hybridisation.
3. Option (1) is incorrect because polymerase chain reaction is used to make copies of the DNA sample and does not need transposons.
4. Option (4) is incorrect because transposons are not required during gene sequencing.

**Solved independently** (answer withheld)

1. RNAi (gene silencing) uses complementary dsRNA from viruses with RNA genomes or from transposons replicating via an RNA intermediate, so the answer is option $2$, Gene Silencing.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q136_160e351c_02112026.png?v=160e351c3091)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q136_a93d40d6_02112026.png?v=a93d40d64e57)

---

## Q137

Biology · botany · Organisms and Populations

While explaining interspecific interaction of population, (+) sign is assigned for beneficial interaction, (–) sign is assigned for detrimental interaction and (0) for neutral interaction. Which of the following interactions can be assigned (+) for one specifies and (–) for another specifies involved in the interaction ?

- **(1)** Predation
- (2) Amensalim
- (3) Commensalism
- (4) Competition

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In predation, one species is benefitted where as the other is harmed.
2. It is $(+\,-)$ type of population interaction.

**Solved independently** (answer withheld)

1. Predation is $(+,-)$, amensalism $(-,0)$, commensalism $(+,0)$ and competition $(-,-)$, so the $(+,-)$ interaction is predation, option $1$.

**Subtopic:** Predation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q137_352a09fc_02112026.png?v=352a09fc289b)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q137_91280a88_02112026.png?v=91280a88e869)

---

## Q138

Biology · botany · Sexual Reproduction in Flowering Plants

Which part of the fruit, labelled in the given figure makes it a false fruit?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q138_d072f45d_02112026.png?v=d072f45d3f55)

- (1) A $\rightarrow$ Mesocarp
- (2) B $\rightarrow$ Endocarp
- **(3)** C $\rightarrow$ Thalamus
- (4) D $\rightarrow$ Seed

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The given figure is of a false fruit.
2. False fruit develops from other floral parts and thalamus alongwith the development of ovary wall.

**Solved independently** (answer withheld)

1. The figure is a transverse section of an apple (a pome), where the outer fleshy region C is the thalamus, which grows around the ovary; the thalamus taking part in fruit formation makes it a false fruit, so the answer is option $3$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q138_79bed53a_02112026.png?v=79bed53a8764)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q138_7905139f_02112026.png?v=7905139f8317)

---

## Q139

Biology · botany · Plant Kingdom

Match the plant with the kind of life cycle it exhibits:
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Spirogyra | (i) | Dominant diploid sporophyte vascular plant, with highly reduced male or female gametophyte |
| (b) | Fern | (ii) | Dominant haploid free-living gametophyte |
| (c) | Funaria | (iii) | Dominant diploid sporophyte alternating with reduced gametophyte called prothallus |
| (d) | Cycas | (iv) | Dominant haploid leafy gametophyte alternating with partially dependent multicellular sporophyte |

- (1) (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)
- **(2)** (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)
- (3) (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)
- (4) (a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spirogyra is an alga. It shows haplontic life-cycle.
2. Fern is pteridophyte. The dominant phase of life-cycle is diploid sporophyte. Its gametophyte is called prothallus.
3. Funaria is a bryophyte. Its gametophyte is a leafy stage.
4. Cycas is a gymnosperm. The main plant body in gymnosperm is sporophyte. They have highly reduced gametophyte stage.

**Solved independently** (answer withheld)

1. Spirogyra (alga) is haplontic: dominant haploid free-living gametophyte, so $(a)-(ii)$.
2. Fern (pteridophyte): dominant diploid sporophyte alternating with a reduced gametophyte called prothallus, so $(b)-(iii)$.
3. Funaria (moss): dominant haploid leafy gametophyte with a partially dependent multicellular sporophyte, so $(c)-(iv)$.
4. Cycas (gymnosperm): dominant diploid vascular sporophyte with highly reduced male or female gametophyte, so $(d)-(i)$.
5. The match $(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)$ is option $2$.

**Subtopic:** Plant Life Cycles and Alternation of Generations · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q139_b20ddaf9_02112026.png?v=b20ddaf9a4bc)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q139_538afa36_02112026.png?v=538afa365ce3)

---

## Q140

Biology · botany · Cell: The Unit of Life

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Metacentric chromosome | (i) | Centromere situated close to the end forming one extremely short and one very long arms |
| (b) | Acrocentric chromosome | (ii) | Centromere at the terminal end |
| (c) | Submetacentric | (iii) | Centromere in the middle forming two equal arms of chromosomes |
| (d) | Telocentric chromosome | (iv) | Centromere slightly away from the middle forming one shorter arm and one longer arm |

- **(1)** (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)
- (2) (a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)
- (3) (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)
- (4) (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. The set $(a)\text{-}(iii), (b)\text{-}(i), (c)\text{-}(iv), (d)\text{-}(ii)$ is option $1$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q140_37b2d14d_02112026.png?v=37b2d14d3e55)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q140_5a8dec6b_02112026.png?v=5a8dec6b0bdb)

---

## Q141

Biology · botany · Transport in Plants

Addition of more solutes in a given solution will :

- (1) raise its water potential
- **(2)** lower its water potential
- (3) make its water potential zero
- (4) not affect the water potential at all

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. If some solute is dissolved in pure water, the solution has lower free water and the concentration of water decreases, reducing it’s water potential.
2. The magnitude of this lowering due to dissolution of a solute is called solute potential.

**Solved independently** (answer withheld)

1. Water potential is $\Psi_w = \Psi_s + \Psi_p$; adding more solute makes $\Psi_s$ more negative, so $\Psi_w$ is lowered, which is option $2$.

**Subtopic:** Water Potential · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q141_76eb657e_02112026.png?v=76eb657e0d12)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q141_e8eac5e1_02112026.png?v=e8eac5e144e4)

---

## Q142

Biology · botany · Principles of Inheritance and Variation

Which of the following occurs due to the presence of autosome linked dominant trait ?

- (1) Sickle cell anaemia
- **(2)** Myotonic dystrophy
- (3) Haemophilia
- (4) Thalessemia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Haemophilia is a X-linked recessive disorder.
2. Thalassemia is an autosomal recessive disorder.
3. Sickle cell anaemia is an autosomal recessive disorder.
4. Myotonic dystrophy is an autosomal dominant disorder i.e. it occurs due to the presence of autosomal linked dominant trait.

**Solved independently** (answer withheld)

1. Sickle cell anaemia and thalassemia are autosomal recessive, haemophilia is X-linked recessive, and myotonic dystrophy is autosomal dominant, so the answer is option $2$.

**Subtopic:** Mendelian Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q142_c4b22052_02112026.png?v=c4b22052447b)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q142_8d873514_02112026.png?v=8d873514539f)

---

## Q143

Biology · botany · Ecosystem

Which one of the following will accelerate phosphorus cycle?

- (1) Burning of fossil fuels
- (2) Volcanic activity
- **(3)** Weathering of rocks
- (4) Rain fall and storms

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Phosphorus cycle is a sedimentary cycle.
2. Reservoir pool of phosphorus in ecosystem is the earth’s crust or lithosphere.
3. Weathering of rocks accelerate phosphorus cycle.

**Solved independently** (answer withheld)

1. The natural reservoir of phosphorus is rock containing phosphates; weathering of rocks releases these phosphates into soil solution for plant uptake, speeding up the phosphorus cycle, which is option $3$.

**Subtopic:** Nutrient Cycling · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q143_93e5bc24_02112026.png?v=93e5bc24c2db)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q143_bd42ebca_02112026.png?v=bd42ebcacbdb)

---

## Q144

Biology · botany · Biotechnology: Principles and Processes

In the following palindromic base sequences of DNA, which one can be cut easily by particular restriction enzyme?

- (1) $5'\mathrm{GATACT}3'$; $3'\mathrm{CTATGA}5'$
- **(2)** $5'\mathrm{GAATTC}3'$; $3'\mathrm{CTTAAG}5'$
- (3) $5'\mathrm{CTCAGT}3'$; $3'\mathrm{GAGTCA}5'$
- (4) $5'\mathrm{GTATTC}3'$; $3'\mathrm{CATAAG}5'$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer as a palindromic DNA sequence is a DNA sequence of base pairs that reads same on the two strands when orientation of reading is kept the same.
2. Out of the four options, option (2) is the only palindromic sequence.
3. $5'\mathrm{GAATTC}3'$
4. $3'\mathrm{CTTAAG}5'$

**Solved independently** (answer withheld)

1. A restriction enzyme recognises a palindromic sequence, one that reads the same on both strands in the $5' \to 3'$ direction.
2. Option 2: top $5'\mathrm{GAATTC}3'$; bottom read $5' \to 3'$ is $\mathrm{GAATTC}$, so it is palindromic and is the EcoRI recognition site.
3. Options 1, 3, 4: bottom strands read $5' \to 3'$ are $\mathrm{AGTATC}$, $\mathrm{TGACTC}$, $\mathrm{GAATAC}$, which differ from the top strands, so they are not palindromes.
4. Hence the answer is option $2$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q144_8cdd32dc_02112026.png?v=8cdd32dc37f4)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q144_cbee87a1_02112026.png?v=cbee87a152d3)

---

## Q145

Biology · botany · Biomolecules

Read the following statements on lipids and find out correct set of statements:
Choose the correct answer from the option given below:

- (a) Lecithin found in the plasma membrane is a glycolipid
- (b) Saturated fatty acids possess one or more $\mathrm{c = c}$ bonds
- (c) Gingely oil has lower melting point, hence remains as oil in winter
- (d) Lipids are generally insoluble in water but soluble in some organic solvents
- (e) When fatty acid is esterified with glycerol, monoglycerides are formed

- (1) (a), (b) and (c) only
- (2) (a), (d) and (e) only
- **(3)** (c), (d) and (e) only
- (4) (a), (b) and (d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because statements (c), (d) and (e) are correct as oils have lower melting point and hence remain oil in winters.
2. Lipids are generally insoluble in water but soluble in some organic solvents.
3. Option (1), (2) and (4) are incorrect because statements (a) and (b) are incorrect.
4. Lecithin is a type of phospholipid found in plasma membrane.
5. Saturated fatty acids are without double bond.

**Solved independently** (answer withheld)

1. (a) is false: lecithin is a phospholipid, not a glycolipid.
2. (b) is false: saturated fatty acids have no $\mathrm{C=C}$ bonds; unsaturated ones have one or more.
3. (c) is true: gingelly oil has a lower melting point and stays liquid in winter.
4. (d) is true: lipids are generally insoluble in water but soluble in organic solvents.
5. (e) is true: one fatty acid esterified with glycerol gives a monoglyceride.
6. True statements are (c), (d) and (e), which is option $3$.

**Subtopic:** Lipids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 50)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q145_f9485541_02112026.png?v=f9485541eb7c)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q145_d022ad65_02112026.png?v=d022ad659caa)

---

## Q146

Biology · botany · Photosynthesis in Higher Plants

What is the role of large bundle sheath cells found around the vascular bundles in $\mathrm{C_4}$ plants?

- (1) To provide the site for photorespiratory pathway
- **(2)** To increase the number of chloroplast for the operation of Calvin cycle
- (3) To enable the plant to tolerate high temperature
- (4) To protect the vascular tissue from high light intensity

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The large cells around the vascular bundles of $\mathrm{C_4}$ plants form bundle sheath.
2. These cells have large number of chloroplasts to perform calvin cycle.

**Solved independently** (answer withheld)

1. In $\mathrm{C_4}$ plants (Kranz anatomy), the large bundle sheath cells hold many chloroplasts and carry out the Calvin cycle, while photorespiration is suppressed, so option $2$ fits.

**Subtopic:** The C₄ Pathway · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q146_2939d2c7_02112026.png?v=2939d2c7e915)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q146_17c6e188_02112026.png?v=17c6e1882a9f)

---

## Q147

Biology · botany · Molecular Basis of Inheritance

If a geneticist uses the blind approach for sequencing the whole genome of an organism, followed by assignment of function to different segments, the methodology adopted by him is called as :

- **(1)** Sequence annotation
- (2) Gene mapping
- (3) Expressed sequence tags
- (4) Bioinformatics

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Sequencing the whole set of genome that contained all the coding and non-coding sequences and later assigning different regions in the sequence with fuctions is called sequence annotation.

**Solved independently** (answer withheld)

1. NCERT (HGP) describes two approaches: identifying expressed genes as RNA (Expressed Sequence Tags), and the blind approach of sequencing the whole genome and later assigning functions to different regions, termed Sequence Annotation, so option $1$.

**Subtopic:** Human Genome Project · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q147_921ece2d_02112026.png?v=921ece2ddeb8)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q147_ddf69e30_02112026.png?v=ddf69e30bfb4)

---

## Q148

Biology · botany · Principles of Inheritance and Variation

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below:

- Assertion (A) Mendel’s law of Independent assortment does not hold good for the genes that are located closely on the same chromosome.
- Reason (R) Closely located genes assort independently.

- (1) Both (A) and (R) are correct and (R) is the correct explanation of (A)
- (2) Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- **(3)** (A) is correct but (R) is not correct
- (4) (A) is not correct but (R) is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Closely located genes do not show independent assortment.
2. Mendel’s law of independent assortment holds good for those genes which are located on different chromosomes.

**Solved independently** (answer withheld)

1. Genes located close together on the same chromosome are linked and are usually inherited together, so Mendel's law of independent assortment does not apply to them: (A) is correct.
2. (R) says closely located genes assort independently, which contradicts linkage, so (R) is not correct; this is option $3$.

**Subtopic:** Linkage & Recombination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q148_92716c07_02112026.png?v=92716c07ddfb)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q148_11e2b7f8_02112026.png?v=11e2b7f8c3ff)

---

## Q149

Biology · botany · Anatomy of Flowering Plants

The anatomy of springwood shows some peculiar features. Identify the correct set of statements about springwood.
Choose the correct answer from the options given below :

- (a) It is also called as the earlywood
- (b) In spring season cambium produces xylem elements with narrow vessels
- (c) It is lighter in colour
- (d) The springwood along with autumnwood shows alternate concentric rings forming annual rings
- (e) It has lower density

- (1) (a), (b), (d) and (e) Only
- **(2)** (a), (c), (d) and (e) Only
- (3) (a), (b) and (d) Only
- (4) (c), (d) and (e) Only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spring wood is also called early wood.
2. It is lighter in colour and has a lower density.
3. The vessels are produced with the wider lumens to transport more water to meet the requirement by increased transpiring surface in spring season.
4. The spring and autumn wood appear as alternate concentric rings of light and dark colour forming annual rings.

**Solved independently** (answer withheld)

1. (a) Springwood is also called earlywood: true.
2. (b) In spring the cambium is very active and forms xylem with wider vessels, not narrow: false.
3. (c) Springwood is lighter in colour: true.
4. (d) Springwood and autumnwood appear as alternate concentric rings forming annual rings: true.
5. (e) Springwood has lower density: true.
6. True set is $(a), (c), (d), (e)$, which is option $2$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 51)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q149_1ba6380e_02112026.png?v=1ba6380ed537)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q149_797eaa25_02112026.png?v=797eaa254e1a)

---

## Q150

Biology · botany · Environmental Issues

The entire fleet of buses in Delhi were converted to CNG from diesel. In reference to this, which one of the following statements is false?

- (1) CNG burns more efficiently than diesel
- **(2)** The same diesel engine is used in CNG buses making the cost of conversion low
- (3) It is cheaper than diesel
- (4) It cannot be adulterated like diesel

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. CNG is cheaper then petrol and it burns more efficiently unlike petrol or diesel.
2. It also cannot be adulterated like diesel and petrol.
3. The same diesel engine cannot be used in CNG buses for making the cost conversion low.

**Solved independently** (answer withheld)

1. NCERT lists CNG advantages: it burns most efficiently, is cheaper than petrol or diesel, and cannot be siphoned off or adulterated, so options $1$, $3$ and $4$ are true; the statement that the same diesel engine is used with low conversion cost is not an NCERT advantage and is false, so the answer is option $2$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q150_5e4872b5_02112026.png?v=5e4872b554ab)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q150_68db92bd_02112026.png?v=68db92bd2ac9)

---

## Q151

Biology · zoology · Biodiversity and Conservation

In-situ conservation refers to:

- **(1)** Protect and conserve the whole ecosystem
- (2) Conserve only high-risk species
- (3) Conserve only endangered species
- (4) Conserve only extinct species

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. When we conserve and protect the whole ecosystem, its biodiversity at all levels is protected.
2. This is in-situ or on site conservation strategy.

**Solved independently** (answer withheld)

1. In-situ (on site) conservation protects organisms in their natural habitat by protecting and conserving the whole ecosystem, as in biosphere reserves, national parks and sanctuaries, which is option $1$.

**Subtopic:** In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q151_9e8fa82d_02112026.png?v=9e8fa82dc5ea)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q151_0ec2e464_02112026.png?v=0ec2e4645133)

---

## Q152

Biology · zoology · Animal Kingdom

In which of the following animals, digestive tract has additional chambers like crop and gizzard?

- (1) Corvus ,Columba ,Chameleon
- (2) Bufo, Balaenoptera, Bangarus
- (3) Catla ,Columba ,Crocodilus
- **(4)** Pavo, Psittacula, Corvus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because two additional chambers like crop and gizzard in alimentary canal are present in birds.
2. Pavo (Peacock), Psittacula (Parrot), Corvus (Crow) and Columba (Pigeon) are birds.
3. Option (1), (2) and (3) are incorrect because Catla is a bony fish, Crocodilus, Chameleon and Bangarus are reptiles, Bufo is an amphibian and Balaenoptera is an aquatic mammal.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Animal Kingdom, Aves) states that the digestive tract of birds has additional chambers, the crop and the gizzard; Pavo, Psittacula and Corvus are all birds, while options 1, 2 and 3 each include a non-bird (Chameleon; Bufo, Balaenoptera, Bangarus; Catla, Crocodilus), so the answer is option $4$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q152_f052a45c_02112026.png?v=f052a45c2cca)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q152_e9fb0697_02112026.png?v=e9fb0697c97c)

---

## Q153

Biology · zoology · Molecular Basis of Inheritance

If the length of a DNA molecule is $1.1$ metres, what will be the approximate number of base pairs?

- **(1)** $3.\ 3\times$ bp $10^{9}$
- (2) $6.\ \times\ 610$bp $^{9}$
- (3) $3.\ 3\times$ bp $10^{6}$
- (4) $6.\ 6\times$ bp $10^{6}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Number of base pairs $\times$ distance between $2$ consecutive base pairs $=$ Length of DNA molecule
2. $x \cdot 0.34 \times 10^{-9}\,\mathrm{m} = 1.1\,\mathrm{m}$
3. $x = \frac{1.1}{0.3 \times 10^{-9}}$
4. $= 3.6 \times 10^{9}$
5. $\simeq 3.3 \times 10^{9}\,\mathrm{bp}$

**Solved independently** (answer withheld)

1. Adjacent base pairs in B-DNA are $0.34\,\text{nm} = 0.34 \times 10^{-9}\,\text{m}$ apart.
2. $N = \frac{1.1\,\text{m}}{0.34 \times 10^{-9}\,\text{m}} \approx 3.24 \times 10^{9}$.
3. $N \approx 3.3 \times 10^{9}$ bp, which is option $1$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q153_3244ab45_02112026.png?v=3244ab45514c)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q153_d606f92d_02112026.png?v=d606f92d8d49)

---

## Q154

Biology · zoology · Digestion and Absorption

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Fatty acids and glycerols cannot be absorbed into the blood.
- (Statement II) Specialized lymphatic capillaries called lacteals carry chylomicrons into lymphatic vessels and ultimately into the blood.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because both the statements I and II are correct as fatty acids and glycerol being insoluble in water, cannot be absorbed into the blood.
2. They are first incorporated into small droplets called micelles which move into the intestinal mucosa.
3. They are re-formed into very small protein coated fat globules called chylomicrons which are transported into the lymph vessels (lacteals) in the villi.
4. These lymph vessels ultimately release the absorbed substances into the blood stream.

**Solved independently** (answer withheld)

1. Statement I: fatty acids and glycerol are insoluble and cannot be absorbed directly into the blood, so Statement I is correct.
2. Statement II: they are incorporated into chylomicrons, which lacteals carry into lymphatic vessels and finally into the blood, so Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Absorption of Digested Products · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q154_26e50655_02112026.png?v=26e50655d45a)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q154_af544f76_02112026.png?v=af544f76f3d6)

---

## Q155

Biology · zoology · Human Health and Disease

Given below are two statements:
Statement I: Autoimmune disorder is a condition where body defense mechanism recognizes its own cells as foreign bodies.
Statement II: Rheumatoid arthritis is a condition where body does not attack self cells.
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Autoimmune disorder is a condition where body defense mechanism recognizes its own cells as foreign bodies.
- (Statement II) Rheumatoid arthritis is a condition where body does not attack self cells.

- (1) are correct Statement II and Statement I Both
- (2) Both Statement I and Statement II are incorrect
- **(3)** is incorrect Statement II is correct but Statement I
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as autoimmune disorder is a condition where body defense mechanism recognises its own cells as foreign bodies.
2. Sometimes, due to genetic and other unknown reasons, the body attacks self- cells.
3. Rheumatoid arthritis is an example where body attacks self cells (synovial membrane).
4. So Statement I is correct but Statement II is incorrect.

**Solved independently** (answer withheld)

1. Statement I: in autoimmune disorders the immune system treats self cells as foreign, so Statement I is correct.
2. Statement II: rheumatoid arthritis is an autoimmune disease in which the body does attack self cells, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect corresponds to option $3$ (whose text is word-scrambled).

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 53)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q155_1c73b548_02112026.png?v=1c73b5484b3b)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q155_a9ece01e_02112026.png?v=a9ece01e0848)

---

## Q156

Biology · zoology · Human Reproduction

Which of the following statements are true for spermatogenesis but do not hold true for Oogenesis? Choose the most appropriate answer from the options given below:

- (a) It results in the formation of haploid gametes
- (b) Differentiation of gamete occurs after the completion of meiosis
- (c) Meiosis occurs continuously in a mitotically dividing stem cell population
- (d) It is controlled by the Luteinising hormone (LH) and Follicle Stimulating Hormone (FSH) secreted by the anterior pituitary
- (e) It is initiated at puberty

- (1) (c) and (e) only
- (2) (b) and (c) only
- (3) (b), (d) and (e) only
- **(4)** (b), (c) and (e) only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer.
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
6. Hence (b), (c) and (e) only, which is option $4$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Female Gametogenesis (Oogenesis) · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 53)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q156_b2b7bf3c_02112026.png?v=b2b7bf3ca195)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q156_71d96b0d_02112026.png?v=71d96b0d6c2b)

---

## Q157

Biology · zoology · Locomotion and Movement

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the most appropriate answer from the options given below.

- Assertion (A) Osteoporosis is characterised by decreased bone mass and increased chance of fractures.
- Reason (R) Common cause of osteoporosis is increased levels of estrogen.

- (1) ) BothA) and (R) are correct and (R) of explanation is the correct (A(
- (2) Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- **(3)** (A) is correct but (Ris not correct )
- (4) (A) is not correct but (R) is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer as osteoporosis is due to decreased levels of oestrogen.
2. Osteoporosis is an age-related disorder characterised by decreased bone mass hence, the chances of fractures increase.

**Solved independently** (answer withheld)

1. Osteoporosis is an age-related disorder with decreased bone mass and increased chance of fractures, so (A) is correct.
2. A common cause of osteoporosis is decreased levels of estrogen, not increased levels, so (R) is not correct.
3. (A) correct and (R) not correct matches option $3$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q157_388e23bd_02112026.png?v=388e23bdb7ce)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q157_d1a86479_02112026.png?v=d1a86479e30d)

---

## Q158

Biology · zoology · Biotechnology: Principles and Processes

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Restriction endonucleases recognise specific sequence to cut DNA known as palindromic nucleotide sequence.
- (Statement II) Restriction endonucleases cut the DNA strand a little away from the centre of the palindromic site.

- **(1)** are correct Statement II and Statement I Both
- (2) are incorrect Statement II and Statement I Both
- (3) is incorrect Statement II is correct but Statement I
- (4) is correct Statement II is incorrect but Statement I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option)1( is the correct answer because both the statements I and II are correct.
2. Each restriction endonuclease recognises a specific palindromic nucleotide sequences in the DNA.
3. It will bind to the DNA and cut each of the two strands of double helix at specific points.
4. Restriction enzymes cut the strand of DNA a little away from the centre of the palindrome site; but between the same two bases on the opposite strands.
5. So both the statements I and II are correct.

**Solved independently** (answer withheld)

1. Restriction endonucleases recognise a specific palindromic nucleotide sequence, so Statement I is correct.
2. They cut each strand a little away from the centre of the palindromic site, between the same two bases, giving sticky ends, so Statement II is correct.
3. Both statements correct matches option $1$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 54)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q158_950ab0d8_02112026.png?v=950ab0d89d20)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q158_daf1f5e9_02112026.png?v=daf1f5e9fa71)

---

## Q159

Biology · zoology · Reproductive Health

Lippe’s loop is a type of contraceptive used as:

- (1) Cervical barrier
- (2) Vault barrier
- **(3)** Non-Medicated IUD
- (4) Copper releasing IUD

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because the intrauterine device (IUD) presently available as the non-medicated IUDs, is Lippe’s loop.
2. Option (4) is incorrect as copper releasing IUDs are CuT, Cu7 and multiload 375.
3. Option (1) and (2) are incorrect as diaphragms, cervical caps and vaults are included in barrier method of contraception.

**Solved independently** (answer withheld)

1. NCERT classifies IUDs as non-medicated (e.g. Lippes loop), copper-releasing (CuT, Cu7, Multiload 375) and hormone-releasing (Progestasert, LNG-20), so Lippes loop is a non-medicated IUD, option $3$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q159_d9ac38b5_02112026.png?v=d9ac38b537b2)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q159_bcc30494_02112026.png?v=bcc30494492f)

---

## Q160

Biology · zoology · Breathing and Exchange of Gases

Under normal physiological conditions in human being every $100\,\mathrm{ml}$ of oxygenated blood can deliver ________ $\mathrm{ml}$ of $\mathrm{O_2}$ to the tissues.

- (1) $2\mathrm{ml}$
- **(2)** $5\,\mathrm{ml}$
- (3) $4\mathrm{ml}$
- (4) $10\,\mathrm{ml}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because every $100\,\mathrm{mL}$ of oxygenated blood can deliver around $5\,\mathrm{mL}$ of $\mathrm{O_2}$ to the tissues under normal physiological conditions.
2. Option (3), (4) and (1) are incorrect because every $100\,\mathrm{mL}$ of deoxygenated blood delivers approximately $4\,\mathrm{mL}$ of $\mathrm{CO_2}$ to the alveoli.

**Solved independently** (answer withheld)

1. Under normal physiological conditions, every $100\,\mathrm{ml}$ of oxygenated blood delivers about $5\,\mathrm{ml}$ of $\mathrm{O_2}$ to the tissues, which is option $2$.

**Subtopic:** Transport of Gases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q160_a04bd09a_02112026.png?v=a04bd09a3389)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q160_6a5924e4_02112026.png?v=6a5924e41794)

---

## Q161

Biology · zoology · Animal Kingdom

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the most appropriate answer from the option given below :

- Assertion (A) All vertebrates are chordates but all chordates are not vertebrates.
- Reason (R) Notochord is replaced by vertebral column in the adult vertebrates.

- **(1)** ) BothA) and (R) are correct and (R) is the correct explanation of (A(
- (2) Both (A) and (R) are correct but (R) is not the correct explanation of (A)
- (3) (A) is correct but (Ris not correct )
- (4) (A) is not correct but (Ris correct )

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because all chordates are divided into three subphyla – Urochordata, Cephalochordata and Vertebrata.
2. In subphylum Vertebrata, notochord is replaced by bony or cartilaginous vertebral column in adults.
3. Therefore, all vertebrates are chordates but all chordates are not vertebrates.

**Solved independently** (answer withheld)

1. Assertion: vertebrates are a subphylum of Chordata, while urochordates and cephalochordates are chordates without a vertebral column, so (A) is true.
2. Reason: in vertebrates the embryonic notochord is replaced by a cartilaginous or bony vertebral column in the adult, so (R) is true.
3. Having a vertebral column that replaces the notochord is what separates vertebrates from other chordates; NCERT gives (R) as the basis for (A), so (R) explains (A), which is option $1$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 55)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q161_9981c7c6_02112026.png?v=9981c7c6e368)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q161_935a3876_02112026.png?v=935a3876237c)

---

## Q162

Biology · zoology · Structural Organisation in Animals

Which of the following is not a connective tissue?

- (1) Blood
- (2) Adipose tissue
- (3) Cartilage
- **(4)** Neuroglia

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as neuroglia are a part of nervous tissue.
2. Neuroglia are the supportive cells of nervous tissue. They make up more than half the volume of neural tissue. Neurons, the unit of neural system are excitable cells.
3. Cartilage and blood are specialised type of connective tissues.
4. Adipose tissue is a type of loose connective tissue.

**Solved independently** (answer withheld)

1. Blood (fluid), adipose tissue (loose) and cartilage (specialised) are all connective tissues, while neuroglia belong to neural tissue, so the answer is option $4$.

**Subtopic:** Connective Tissue, Muscle Tissue and Neural Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q162_42474cb9_02112026.png?v=42474cb9f0a3)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q162_10071903_02112026.png?v=100719032561)

---

## Q163

Biology · zoology · Excretory Products and Their Elimination

Nitrogenous waste is excreted in the form of pellet or paste by :

- (1) Ornithorhynchus
- (2) Salamandra
- (3) Hippocampus
- **(4)** Pavo

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because birds (Pavo) excrete nitrogenous wastes as uric acid in the form of pellet or paste with a minimum loss of water.
2. Option (3) and (2) are incorrect because many bony fishes (like Hippocampus) and aquatic amphibians (like Salamandra) are ammonotelic in nature.
3. Option (1) is incorrect because mammals (like Ornithorhynchus) mainly excrete urea and are called ureotelic animals.

**Solved independently** (answer withheld)

1. Uricotelic animals (reptiles, birds, land snails, insects) excrete uric acid as a pellet or paste; Ornithorhynchus is a ureotelic mammal, Salamandra a ureotelic amphibian, Hippocampus an ammonotelic bony fish, and Pavo a uricotelic bird, so the answer is option $4$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q163_6f07d19a_02112026.png?v=6f07d19a41eb)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q163_7942c93a_02112026.png?v=7942c93a3236)

---

## Q164

Biology · zoology · Cell Cycle and Cell Division

Regarding Meiosis, which of the statements is incorrect?

- (1) There are two stages in Meiosis, Meiosis-I and II
- **(2)** in S phase of Meiosis DNA replication occurs-II
- (3) Pairing of homologous chromosomes and recombination occurs in Meiosis-I
- (4) Four haploid cells are formed at the end of Meiosis-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Meiosis involves two sequential cycles of nuclear and cell division called meiosis-I and meiosis-II but only single cycle of DNA replication.
2. The stage between two meiotic divisions is called interkinesis and is generally short lived and involves no DNA replication.

**Solved independently** (answer withheld)

1. Meiosis has two divisions (Meiosis-I and II), homologous pairing and recombination occur in prophase I, and four haploid cells result after Meiosis-II, so options $1$, $3$ and $4$ are correct; DNA replication does not occur before Meiosis-II (no S phase in interkinesis), so option $2$ is the incorrect statement.

**Subtopic:** Meiosis and Meiosis I · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q164_b6209d29_02112026.png?v=b6209d2951c1)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q164_f454fc3a_02112026.png?v=f454fc3aa0e1)

---

## Q165

Biology · zoology · Molecular Basis of Inheritance

In an E. Coli strain i gene gets mutated and its product can not bind the inducer molecule. If growth medium is provided with lactose, what will be the outcome?

- (1) Only z gene will get transcribed
- (2) z, y, a genes will be transcribed
- **(3)** z ,y ,a genes will not be translated
- (4) RNA polymerase will bind the promoter region

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. As the product of ‘i’ gene binds with the operator region and blocks the transcription and translation of z, y and a genes.
2. It’s product is prevented from binding to the operator by attaching it with the inducer.
3. As the inducer can now no more capable of binding with the repressor, thus, in all the cases, operator always gets attached with the repressor thereby preventing the transcription and transmission of z, y and a.
4. Even in the presence of lactose, transcription and translation of z, y and a would not occur.

**Solved independently** (answer withheld)

1. The $i$ gene codes for the repressor; normally the inducer (allolactose) binds the repressor and releases it from the operator.
2. Here the mutated repressor cannot bind the inducer, so even with lactose present it stays bound to the operator.
3. The bound repressor blocks RNA polymerase, so $z$, $y$, $a$ are not transcribed and therefore not translated, which is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 56)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q165_ad9d12d4_02112026.png?v=ad9d12d438e3)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q165_c68f8887_02112026.png?v=c68f888774a0)

---

## Q166

Biology · zoology · Locomotion and Movement

Which of the following is a correct match for disease and its symptoms?

- **(1)** Arthritis – Inflammed joints
- (2) Tetany – High $\mathrm{Ca^{2+}}$ level causing rapid spasms.
- (3) Myasthenia gravis – Genetic disorder resulting in weakening and paralysis of skeletal muscle
- (4) Muscular dystrophy – An auto immune disorder causing progressive degeneration of skeletal muscle

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because Arthritis is inflammation of joints.
2. Option (3) is incorrect because myasthenia gravis is an immune disorder affecting neuro-muscular junction leading to fatigue, weakening and paralysis of skeletal muscle.
3. Option (4) is incorrect because muscular dystrophy is progressive degeneration of skeletal muscle mostly due to genetic disorder.
4. Option (2) is incorrect because tetany is rapid spasms in muscle due to low $\mathrm{Ca^{++}}$ in body fluid.

**Solved independently** (answer withheld)

1. Arthritis is inflammation of the joints, so option $1$ is a correct match.
2. Tetany is caused by low $\mathrm{Ca^{2+}}$ in body fluid, not high, so option $2$ is wrong.
3. Myasthenia gravis is an auto-immune disorder, not a genetic one, so option $3$ is wrong.
4. Muscular dystrophy is a genetic disorder, not auto-immune, so option $4$ is wrong; the answer is option $1$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 57)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q166_d0f0f684_02112026.png?v=d0f0f684ef7e)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q166_8588db9c_02112026.png?v=8588db9c5a49)

---

## Q167

Biology · zoology · Microbes in Human Welfare

Identify the microorganism which is responsible for the production of an immunosuppressive molecule cyclosporin A :

- **(1)** Trichoderma polysporum
- (2) Clostridium butylicum
- (3) Aspergillus niger
- (4) Streptococcus cerevisiae

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Bioactive molecule, cyclosporin A, that is used as an immunosuppressive agent in organ transplant patients, is produced by the fungus, Trichoderma polysporum.

**Solved independently** (answer withheld)

1. Cyclosporin A, used as an immunosuppressive agent in organ-transplant patients, is produced by the fungus $\textit{Trichoderma polysporum}$, which is option $1$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q167_870352f0_02112026.png?v=870352f0a221)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q167_a8fc0f8f_02112026.png?v=a8fc0f8f1eef)

---

## Q168

Biology · zoology · Biological Classification

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below

- (Statement I) Mycoplasma can pass through less than $1$ micron filter size.
- (Statement II) Mycoplasma are bacteria with cell wall.

- (1) correct are Both Statement I and Statement II
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Mycoplasma are the smallest cells and are only $0.3\,\mu\mathrm{m}$ in length.
2. So it can pass through less than $1\,\mu\mathrm{m}$ filter size.
3. Mycoplasma lack cell wall.

**Solved independently** (answer withheld)

1. Mycoplasma are the smallest living cells (about $0.1\,\mu m$), so they can pass through filters smaller than $1\,\mu m$: Statement I is correct.
2. Mycoplasma completely lack a cell wall, so Statement II is incorrect; this matches option $3$.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q168_f994d4a1_02112026.png?v=f994d4a1a49b)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q168_2957d3c6_02112026.png?v=2957d3c6f5ee)

---

## Q169

Biology · zoology · Digestion and Absorption

Which of the following functions is not performed by secretions from salivary glands?

- (1) Control bacterial population in mouth
- (2) Digestion of complex carbohydrates
- (3) Lubrication of oral cavity
- **(4)** Digestion of disaccharides

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because digestion of polysaccharides like starch occurs in mouth and digestion of disaccharides occurs in small intestine.
2. Option (3) is incorrect because saliva contains mucus which helps in the lubrication of oral cavity.
3. Option (1) is incorrect because saliva contains an antibacterial agent-lysozyme so that it controls bacterial population in mouth.
4. Option (2) is incorrect because digestion of complex carbohydrates are performed by secretions from salivary glands.

**Solved independently** (answer withheld)

1. Saliva contains lysozyme, which acts as an antibacterial agent and controls the bacterial population in the mouth, so option $1$ is performed.
2. Salivary amylase hydrolyses starch, a complex carbohydrate (polysaccharide), so option $2$ is performed.
3. Mucus in saliva lubricates the oral cavity and helps form the bolus, so option $3$ is performed.
4. Salivary amylase converts starch into the disaccharide maltose but does not break disaccharides down further; that happens in the intestine (maltase, sucrase, lactase), so option $4$ is not performed.

**Subtopic:** Digestion of Food · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q169_b28bebd3_02112026.png?v=b28bebd35562)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q169_04d78f87_02112026.png?v=04d78f87948f)

---

## Q170

Biology · zoology · Body Fluids and Circulation

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The coagulum is formed of network of threads called thrombins.
- (Statement II) Spleen is the graveyard of erythrocytes.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- **(4)** Statement I is incorrect but Statement II is correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because coagulum or clot is formed mainly of a network of threads called fibrins.
2. Hence, Statement I is incorrect.
3. RBCs are destroyed in the spleen so spleen is known as the graveyard of erythrocytes.
4. Hence, Statement II is correct.

**Solved independently** (answer withheld)

1. Statement I: the coagulum (clot) is a network of $\text{fibrin}$ threads in which formed elements are trapped; thrombin is the enzyme that turns fibrinogen into fibrin, so Statement I is incorrect.
2. Statement II: the spleen destroys worn-out erythrocytes and is called the graveyard of RBCs, so Statement II is correct.
3. Statement I incorrect and Statement II correct is option $4$.

**Subtopic:** Coagulation of Blood, Formed Elements And Their Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q170_14665afa_02112026.png?v=14665afa5873)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q170_9a905e40_02112026.png?v=9a905e403223)

---

## Q171

Biology · zoology · Biomolecules

A dehydration reaction links two glucose molecules to product maltose. If the formula for glucose is $\mathrm{C_6H_{12}O_6}$ then what is the formula for maltose?

- (1) $\mathrm{C_{12}H_{20}O_{10}}$
- (2) $\mathrm{C_{12}H_{24}O_{12}}$
- **(3)** $\mathrm{C_{12}H_{22}O_{11}}$
- (4) $\mathrm{C_{12}H_{24}O_{11}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option $(3)$ is correct because maltose is a disaccharide formed by dehydration process i.e., synthesis by elimination of one water molecule to form a glycosidic bond in between two glucose molecules. So, its molecular formula is.
2. $\mathrm{C_6H_{12}O_6} \times 2 \xrightarrow[\mathrm{H_2O}]{} \mathrm{C_{12}H_{22}O_{11}}$

**Solved independently** (answer withheld)

1. Two glucose molecules together contain $2 \times \mathrm{C_6H_{12}O_6} = \mathrm{C_{12}H_{24}O_{12}}$.
2. A dehydration (condensation) reaction forming one glycosidic bond removes one $\mathrm{H_2O}$.
3. $\mathrm{C_{12}H_{24}O_{12}} - \mathrm{H_2O} = \mathrm{C_{12}H_{22}O_{11}}$, which is option $3$.

**Subtopic:** Polysaccharides · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q171_83c9a46f_02112026.png?v=83c9a46f765b)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q171_50ac20cd_02112026.png?v=50ac20cdcf18)

---

## Q172

Biology · zoology · Cell: The Unit of Life

Which of the following statements with respect to Endoplasmic Reticulum is incorrect?

- (1) RER has ribosomes attached to ER
- (2) SER is devoid of ribosomes
- **(3)** prokaryotes only RER are present In
- (4) SER are the sites for lipid synthesis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In prokaryotes, ER is absent be it RER or SER.

**Solved independently** (answer withheld)

1. Prokaryotic cells lack membrane-bound organelles, including the endoplasmic reticulum, so the statement that only RER is present in prokaryotes is incorrect, which is option $3$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q172_74b2c9ec_02112026.png?v=74b2c9ec0e11)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q172_0f9794e2_02112026.png?v=0f9794e2e3dc)

---

## Q173

Biology · zoology · Structural Organisation in Animals

Which of the following is present between the adjacent bones of the vertebral column?

- (1) Intercalated discs
- **(2)** Cartilage
- (3) Areolar tissue
- (4) Smooth muscle

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because cartilage forming the intervertebral disc is present between the adjacent bones of the vertebral column and it is a type of cartilaginous joint.
2. Option (3) is incorrect because areolar tissue present beneath the skin is a type of loose connective tissue.
3. Option (4) is incorrect because smooth muscles are present in the visceral organs.
4. Option (1) is incorrect because intercalated discs are characteristic feature of cardiac muscles present in heart.

**Solved independently** (answer withheld)

1. Adjacent vertebrae are joined by intervertebral discs made of cartilage (fibrocartilage); intercalated discs belong to cardiac muscle, so the answer is option $2$.

**Subtopic:** Cartilage, Bone and Blood · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q173_964b9b93_02112026.png?v=964b9b93ed9a)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q173_d3d3b0aa_02112026.png?v=d3d3b0aac4d1)

---

## Q174

Biology · zoology · Structural Organisation in Animals

Tegmina in cockroach, arises from

- (1) Prothorax
- **(2)** Mesothorax
- (3) Metathorax
- (4) Prothorax and Mesothorax

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because tegmina or forewings (the first pair of wings) in cockroach arises from mesothorax.
2. Options (1), (3) and (4) are incorrect because no wing arises from prothorax and hindwings arise from metathorax.

**Solved independently** (answer withheld)

1. Tegmina (the opaque, leathery forewings of cockroach) arise from the mesothorax, while the hindwings arise from the metathorax, so the answer is option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q174_531f591e_02112026.png?v=531f591eeaef)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q174_43881cee_02112026.png?v=43881cee4187)

---

## Q175

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The release of sperms into the seminiferous tubules is called spermiation.
- (Statement II) Spermiogenesis is the process of formation of sperms from spermatogonia.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because Statement II is incorrect as the transformation of spermatids into spermatozoa (sperms) are called spermiogenesis.
2. After this, sperm head becomes embedded in the Sertoli cells and are finally released from the seminiferous tubules by the process called spermiation.
3. Hence, Statement I is a correct statement.
4. Spermatogenesis is the process of formation of sperms from spermatogonia.

**Solved independently** (answer withheld)

1. Statement I: after spermiogenesis, sperm heads embedded in Sertoli cells are released from the seminiferous tubules (into the lumen) by spermiation, so Statement I is correct.
2. Statement II: spermiogenesis is the transformation of spermatids into spermatozoa; formation of sperms from spermatogonia is spermatogenesis, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect matches option $3$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q175_fe5434f7_02112026.png?v=fe5434f7f484)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q175_6189d8bc_02112026.png?v=6189d8bcf730)

---

## Q176

Biology · zoology · Organisms and Populations

If ‘8’ Drosophila in a laboratory population of ‘80’ died during a week, the death rate in the population is ______ individuals per Drosophila per week.

- **(1)** $0.1$
- (2) $10$
- (3) $1.0$
- (4) zero

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. If $8$ Drosophila in a laboratory population of $80$ died during a week, the death rate in the population is
2. $\frac{8}{80} = 0.1$ individuals per Drosophila per week.

**Solved independently** (answer withheld)

1. Death rate $d = \frac{\text{number of deaths}}{\text{population size}}$ over the given period.
2. $d = \frac{8}{80} = 0.1$ individuals per Drosophila per week, which is option $1$.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q176_acaf4681_02112026.png?v=acaf4681fc93)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q176_942e0bfd_02112026.png?v=942e0bfdb9db)

---

## Q177

Biology · zoology · Evolution

Natural selection where more individuals acquire specific character value other than the mean character value, leads to

- (1) Stabilising change
- **(2)** Directional change
- (3) Disruptive change
- (4) Random change

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is correct because in directional natural selection more individuals acquire value other than the mean character value.
2. Option (3) is incorrect because in disruptive change, more individuals acquire peripheral character value at both ends of the distribution curve.
3. Option (4) is incorrect because there is no random change in natural selection.
4. Option (1) is incorrect because natural selection leads to stabilisation when more individuals acquire mean character value.

**Solved independently** (answer withheld)

1. As NCERT teaches it, in directional selection more individuals acquire a value other than the mean character value, so the peak shifts in one direction; this is option $2$ (Directional change).

**Subtopic:** Types of Natural Selection · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q177_aa7cdff8_02112026.png?v=aa7cdff87999)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q177_14112aa7_02112026.png?v=14112aa756ea)

---

## Q178

Biology · zoology · Breathing and Exchange of Gases

Which of the following is not the function of conducting part of respiratory system?

- (1) It clears inhaled air from foreign particles
- (2) Inhaled air is humidified
- (3) Temperature of inhaled air is brought to body temperature
- **(4)** Provides surface for diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is correct because the part starting with the external nostrils upto the terminal bronchioles constitute the conducting part; whereas the alveoli and their ducts form the respiratory or exchange part of the respiratory system.
2. The conducting part transports the atmospheric air to the alveoli, clears it from foreign particles, humidifies and also bring the air to body temperature.
3. Exchange part is the site of actual diffusion of $\mathrm{O_2}/\mathrm{CO_2}$ between blood and atmospheric air.

**Solved independently** (answer withheld)

1. The conducting part (nose to terminal bronchioles) clears foreign particles from inhaled air, humidifies it and brings it to body temperature, while diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$ happens across the alveoli of the exchange part, so the answer is option $4$.

**Subtopic:** Human Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q178_09adac3f_02112026.png?v=09adac3f0691)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q178_b5bc25d9_02112026.png?v=b5bc25d990f7)

---

## Q179

Biology · zoology · Strategies for Enhancement in Food Production

Breeding crops with higher levels of vitamins and minerals or higher proteins and healthier fats is called :

- (1) Bio-magnification
- (2) Bio-remediation
- **(3)** Bio-fortification
- (4) Bio-accumulation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Breeding crops with higher levels of vitamins and minerals, or higher protein and healthier fats is known as Biofortification.
2. Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.
3. Bioremediation is the phenomenon of using biological organism to handle pollution.

**Solved independently** (answer withheld)

1. Breeding crops with higher levels of vitamins, minerals, proteins and healthier fats to improve nutritional quality is termed $\text{biofortification}$, which is option $3$.

**Subtopic:** Biofortification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q179_f7fbd2ec_02112026.png?v=f7fbd2ecf2ea)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q179_190a4fe5_02112026.png?v=190a4fe5fa82)

---

## Q180

Biology · zoology · The Living World

> ⚠ The printed solution says "None of the options are matching with the language of the question": the question has no correct option as printed, and the printed answer comes from a corrected reading.

> ⚠ The independent solve chose (unsure); the booklet prints (1).

In the taxonomic categories which hierarchical arrangement in ascending order is correct in case of animals?

- **(1)** Kingdom, Phylum, Class, Order, Family, Genus, Species
- (2) Kingdom, Class, Phylum, Family, Order, Genus, Species
- (3) Kingdom, Order, Class, Phylum, Family, Genus, Species
- (4) Kingdom, Order, Phylum, Class, Family, Genus, Species

**Answer** — booklet: (1) · independent solve: (unsure) · publisher_contradicts_itself

**Publisher's solution**

1. None of the options are matching with the language of the question
2. The correct ascending order of taxonomic categories in case of animals is
3. species $\rightarrow$ genus $\rightarrow$ family $\rightarrow$ order $\rightarrow$ class $\rightarrow$ phylum $\rightarrow$ kingdom

**Solved independently** (answer withheld)

1. The animal hierarchy from lowest to highest rank is Species, Genus, Family, Order, Class, Phylum, Kingdom.
2. Ascending order therefore begins with Species and ends with Kingdom.
3. All four options begin with Kingdom, so all are written in descending direction; none is ascending.
4. Option 1 is the correct sequence only if read as descending.

**Subtopic:** Taxonomic Categories · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q180_0ed9ea1d_02112026.png?v=0ed9ea1d65a8)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q180_1c960f11_02112026.png?v=1c960f11209a)

---

## Q181

Biology · zoology · Human Reproduction

At which stage of life the oogenesis process is initiated?

- (1) Puberty
- **(2)** Embryonic development stage
- (3) Birth
- (4) Adult

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer as oogenesis is initiated during the embryonic development stage when a couple of million gamete mother cells (oogonia) are formed within each foetal ovary.
2. No more oogonia are formed and added after birth in a human female.
3. At puberty only $60{,}000$ to $80{,}000$ primary follicles are left in each ovary, rest degenerate during the phase from birth to puberty.

**Solved independently** (answer withheld)

1. Oogenesis starts in the embryonic stage: oogonia form in the foetal ovary and begin meiosis I, arresting as primary oocytes, so the answer is option $2$.

**Subtopic:** Female Gametogenesis (Oogenesis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q181_51834d7a_02112026.png?v=51834d7ac6bc)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q181_6b7258b8_02112026.png?v=6b7258b87ec2)

---

## Q182

Biology · zoology · Reproduction in Organisms

Identify the asexual reproductive structure associated with Penicillium :

- (1) Zoospores
- **(2)** Conidia
- (3) Gemmules
- (4) Buds

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Conidia are the asexual reproductive structures produced in Penicillium.
2. Gemmules are produced in sponge
3. Buds are produced in Hydra
4. Zoospores are produced in Chlamydomonas

**Solved independently** (answer withheld)

1. Penicillium (an ascomycete fungus) reproduces asexually by conidia borne on conidiophores, which is option $2$.

**Subtopic:** Asexual Reproduction and Vegetative Propagation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q182_cd16581c_02112026.png?v=cd16581c0ecd)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q182_3e66baeb_02112026.png?v=3e66baebbaa7)

---

## Q183

Biology · zoology · Biotechnology and Its Applications

In gene therapy of Adenosine Deaminase (ADA) deficiency, the patient requires periodic infusion of genetically engineered lymphocytes because :

- (1) Retroviral vector is introduced into these lymphocytes.
- (2) Gene isolated from marrow cells producing ADA is introduced into cells at embryonic stages
- (3) Lymphocytes from patient's blood are grown in culture, outside the body.
- **(4)** Genetically engineered lymphocytes are not immortal cells.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as genetically engineered lymphocyctes are not immortal cells and die after some time.
2. Option (3) is not the correct answer as the lymphocytes from patient’s blood are grown in culture, outside the body but it is not the correct reason.
3. In option (2), if the gene isolated from bone marrow cells producing ADA is introduced into cells at early embryonic stages, it could be a permanent cure.

**Solved independently** (answer withheld)

1. Engineered lymphocytes have a limited life span (they are not immortal), so the patient needs periodic infusions of them, which is option $4$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q183_60b7cc7c_02112026.png?v=60b7cc7c0585)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q183_ef4ef827_02112026.png?v=ef4ef827b234)

---

## Q184

Biology · zoology · Cell Cycle and Cell Division

Select the incorrect statement with reference to mitosis:

- (1) All the chromosomes lie at the equator at metaphase
- **(2)** Spindle fibres attach to centromere of chromosomes
- (3) Chromosomes decondense at telophase
- (4) Splitting of centromere occurs at anaphase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spindle fibres attach to the kinetochores of chromosomes.
2. Kinetochores are the disc shaped structures present on sides of primary constriction or centromere of chromosomes.

**Solved independently** (answer withheld)

1. Options 1, 3 and 4 match NCERT: chromosomes align at the equator in metaphase, the centromere splits at anaphase, and chromosomes decondense at telophase.
2. NCERT says spindle fibres attach to the kinetochores, small disc-shaped structures at the surface of the centromere, so option $2$ is the incorrect statement.

**Subtopic:** Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q184_3a1b25e6_02112026.png?v=3a1b25e678ca)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q184_5df06965_02112026.png?v=5df06965a347)

---

## Q185

Biology · zoology · Ecosystem

Detritivores breakdown detritus into smaller particles. This process is called:

- (1) Catabolism
- **(2)** Fragmentation
- (3) Humification
- (4) Decomposition

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Detritivores)eg. earthworm( break down detritus into smaller particles.
2. This process is called fragmentation.

**Solved independently** (answer withheld)

1. Per NCERT, the breakdown of detritus into smaller particles by detritivores such as earthworm is called $\text{fragmentation}$, which is option $2$.

**Subtopic:** Decomposition · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q185_3d7085c0_02112026.png?v=3d7085c053ee)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q185_3af3d750_02112026.png?v=3af3d75014ed)

---

## Q186

Biology · zoology · Principles of Inheritance and Variation

If a colour blind female marries a man whose mother was also colour blind, what are the chances of her progeny having colour blindness?

- (1) $25\%$
- (2) $50\%$
- (3) $75\%$
- **(4)** $100\%$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. If mother of man is colourblind, then man will also be colourblind as colour blindness is a X-linked recessive trait and shows criss-cross inheritance.

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q186_sol_1_0b102401_02112026.png?v=0b102401bc28)


**Solved independently** (answer withheld)

1. The colour blind female is homozygous: $X^cX^c$.
2. The man's mother was colour blind ($X^cX^c$), so she passes $X^c$ to him; the man is $X^cY$ (colour blind).
3. Cross $X^cX^c \times X^cY$: daughters $X^cX^c$, sons $X^cY$.
4. All progeny are colour blind, i.e. $100\%$, which is option $4$.

**Subtopic:** Colour Blindness · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 62)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q186_f1723a93_02112026.png?v=f1723a930f15)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q186_a6ad96cd_02112026.png?v=a6ad96cdf9a8)

---

## Q187

Biology · zoology · Human Health and Disease

Select the incorrect statement with respect to acquired immunity.

- (1) Primary response is produced when our body encounters a pathogen for the first time.
- (2) Anamnestic response is elicited on subsequent encounters with the same pathogen.
- (3) Anamnestic response is due to memory of first encounter.
- **(4)** Acquired immunity is non-specific type of defense present at the time of birth.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as acquired immunity is a specific type of defence which is not present at the time of birth.
2. Option (3), (1) and (2) are true statements and hence cannot be the answer.
3. Anamnestic response or secondary immune response is a highly intensified response due to memory of first encounter.
4. When our body encounters a pathogen for the first time then the body elicits the primary immune response.
5. When there is a subsequent encounter with the same pathogen, secondary or anamnestic immune response is elicited.

**Solved independently** (answer withheld)

1. Acquired immunity is pathogen-specific, has memory and is not present at birth; innate immunity is the non-specific defence present at birth, so statement $4$ is the incorrect one.

**Subtopic:** Acquired Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q187_9d5c6169_02112026.png?v=9d5c6169fe45)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q187_61603e3f_02112026.png?v=61603e3f1564)

---

## Q188

Biology · zoology · Biotechnology and Its Applications

Statements related to human Insulin are given below. Which statement(s) is/are correct about genetically engineered Insulin? Choose the most appropriate answer from the options given below:

- (a) Pro-hormone insulin contain extra stretch of C-peptide
- (b) A-peptide and B-peptide chains of insulin were produced separately in E.coli, extracted and combined by creating disulphide bond between them.
- (c) Insulin used for treating Diabetes was extracted from Cattles and Pigs.
- (d) Pro-hormone Insulin needs to be processed for converting into a mature and functional hormone.
- (e) Some patients develop allergic reactions to the foreign insulin.

- (1) (a), (b) and (d) only
- **(2)** (b) only
- (3) (c) and (d) only
- (4) (c), (d) and (e) only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer as genetically engineered insulin has A-peptide and B-peptide chains of insulin which are produced separately in $\textit{E.coli}$, then they are extracted and combined by creating disulphide bond between them.
2. Statement (a) is incorrect as genetically engineered insulin does not have an extra stretch of C-peptide.
3. Statement (c) is incorrect as insulin obtained from cattles and pigs is not genetically engineered insulin.
4. Statement (d) is incorrect because conversion of pro-insulin to insulin is not required during production of insulin by genetic engineering as A-peptide and B-peptide chains are produced separately.
5. Statement (e) is incorrect as allergic reactions to insulin are mostly seen when the insulin is obtained from animals.

**Solved independently** (answer withheld)

1. Statement (b) is the NCERT account of genetically engineered insulin: A and B chains produced separately in $E.\ coli$, extracted and joined by disulphide bridges, so (b) applies.
2. Statements (a) and (d) describe natural pro-insulin with its C-peptide that must be processed to mature insulin; in the engineered route the C-peptide is avoided, so they do not describe engineered insulin.
3. Statements (c) and (e) describe insulin from cattle and pigs and the allergic reactions to it, which is the problem engineered insulin solved, so they are not about engineered insulin.
4. Only (b) is correct about genetically engineered insulin, which is option $2$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q188_8426cd31_02112026.png?v=8426cd31dd7b)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q188_000518fc_02112026.png?v=000518fc30e0)

---

## Q189

Biology · zoology · Body Fluids and Circulation

Which one of the following statements is correct?

- (1) The atrio-ventricular node (AVN) generates an action potential to stimulate atrial contraction
- (2) The tricuspid and the bicuspid valves open due to the pressure exerted by the simultaneous contraction of the atria
- **(3)** Blood moves freely from atrium to the ventricle during joint diastole.
- (4) Increased ventricular pressure causes closing of the semilunar valves.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because during joint diastole, blood moves freely from atrium to ventricle as atrioventricular valve remain open during joint diastole.
2. Option (4) is incorrect because decrease in ventricular pressure, during ventricular diastole closes semilunar valves to produce ‘dub’ heart sound.
3. Option (1) is incorrect because SA node generates action potential to stimulate atrial contraction.
4. Option (2) is incorrect because bicuspid and tricuspid valves open due to pressure exerted by blood present in atria and decrease in pressure in ventricles during ventricular diastole.

**Solved independently** (answer withheld)

1. Option 1 is false: the SA node, not the AV node, generates the action potential that stimulates atrial contraction.
2. Option 2 is false: the tricuspid and bicuspid valves are already open during joint diastole; atrial systole only adds about 30% more blood.
3. Option 4 is false: increased ventricular pressure closes the AV valves and opens the semilunar valves; semilunar valves close when ventricular pressure falls below arterial pressure.
4. Option 3 is true: during joint diastole the AV valves are open, so blood moves freely from atria into ventricles, giving option $3$.

**Subtopic:** Cardiac Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q189_2bfcea03_02112026.png?v=2bfcea030a2a)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q189_2317b8db_02112026.png?v=2317b8db5eaa)

---

## Q190

Biology · zoology · Biomolecules

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Match List-I with List-II
List-I (Biological Molecules) | List-II (Biological functions)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Glycogen | (i) | Hormone |
| (b) | Globulin | (ii) | Biocatalyst |
| (c) | Steroids | (iii) | Antibody |
| (d) | Thrombin | (iv) | Storage product |

- (1) (a) - (iii), (b) - (ii), (c) - (iv), (d) - (i)
- (2) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii)
- (3) (a) - (ii), (b) - (iv), (c) - (iii), (d) - (i)
- **(4)** (a) - (iv), (b) - (iii), (c) - (i), (d) - (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as glycogen is a polysaccharide and is a storage product in animals.
2. Globulins form antibodies which are also known as immunoglobulins.
3. Steroids form hormones like testosterone.
4. Thrombin is a biocatalyst which converts soluble fibrinogen to insoluble fibrin.

**Solved independently** (answer withheld)

1. Glycogen is the storage polysaccharide in animals, so $(a) \to (iv)$.
2. Globulins (immunoglobulins) function as antibodies, so $(b) \to (iii)$.
3. Steroids such as testosterone and oestrogen act as hormones, so $(c) \to (i)$.
4. Thrombin is an enzyme in blood clotting, i.e. a biocatalyst, so $(d) \to (ii)$.
5. The match $a$-$iv$, $b$-$iii$, $c$-$i$, $d$-$ii$ is option $4$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q190_f44d841b_02112026.png?v=f44d841b16cf)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q190_6fecd20f_02112026.png?v=6fecd20f0a79)

---

## Q191

Biology · zoology · Molecular Basis of Inheritance

Ten E.coli cells with $\mathrm{^{15}N}$ - dsDNA are incubated in medium containing $\mathrm{^{14}N}$ nucleotide. After $60\,\text{minutes}$, how many E.coli cells will have DNA totally free from $\mathrm{^{15}N}$?

- (1) 20 cells
- (2) 40 cells
- **(3)** 60 cells
- (4) 80 cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. From $10$ parent \textit{E.coli} cells
2. $1^{\mathrm{st}}$ generation

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q191_sol_1_f9af16f7_02112026.png?v=f9af16f73619)

3. $2^{\mathrm{nd}}$ generation

![printed figure: solution_2](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q191_sol_2_6ad75d8a_02112026.png?v=6ad75d8a9f8b)

4. $3^{\mathrm{rd}}$ generation

![printed figure: solution_3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q191_sol_3_adcd5f94_02112026.png?v=adcd5f9457c1)

5. Therefore, after $60$ minutes, $60$ \textit{E.coli} cells will have DNA totally free from $\mathrm{^{15}N}$.

**Solved independently** (answer withheld)

1. E. coli divides once every $20\,\text{min}$, so in $60\,\text{min}$ there are $\frac{60}{20} = 3$ generations.
2. Total cells after 3 generations: $10 \times 2^3 = 80$.
3. Replication is semiconservative: the two original $^{15}N$ strands of each parent DNA stay intact and end up in 2 cells, so cells carrying $^{15}N$ $= 10 \times 2 = 20$.
4. Cells totally free of $^{15}N$ $= 80 - 20 = 60$, which is option $3$.

**Subtopic:** Experimental Proof that DNA is Semiconservative · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 65)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q191_0d20bc40_02112026.png?v=0d20bc40d24d)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q191_019a8c6a_02112026.png?v=019a8c6afd4a)

---

## Q192

Biology · zoology · Principles of Inheritance and Variation

The recombination frequency between the genes a & c is $5\%$, b & c is $15\%$, b & d is $9\%$, a & b is $20\%$, c & d is $24\%$ and a & d is $29\%$. What will be the sequence of these genes on a linear chromosome?

- (1) a, d, b, c
- (2) d, b, a, c
- (3) a, b, c, d
- **(4)** a, c, b, d

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $1\%$ recombination frequency = $1$ centi Morgan
2. To place the genes on a linear chromosome, decreasing order of recombination frequency will be considered.

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/figures_agent/q192_sol_1_1e0aa7c1_02112026.png?v=1e0aa7c1d2de)


**Solved independently** (answer withheld)

1. Recombination frequency is proportional to map distance, so the farthest pair $a$–$d$ ($29\%$) are the two ends.
2. $a$–$c = 5\%$ is smallest from $a$, so $c$ lies next to $a$: $a, c, \dots$
3. $c$–$b = 15\%$ places $b$ after $c$: $a$–$b = 5 + 15 = 20\%$, matching the given value.
4. $b$–$d = 9\%$ places $d$ last: $c$–$d = 15 + 9 = 24\%$ and $a$–$d = 5 + 15 + 9 = 29\%$, both matching.
5. The order is $a, c, b, d$, which is option $4$.

**Subtopic:** Linkage & Recombination · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 65)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q192_a0f4ee43_02112026.png?v=a0f4ee434e22)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q192_2dc95f7f_02112026.png?v=2dc95f7f2ded)

---

## Q193

Biology · zoology · Chemical Coordination and Integration

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Which of the following are not the effects of Parathyroid hormone? Choose the most appropriate answer from the options given below:

- (a) Stimulates the process of bone resorption
- (b) Decreases $\mathrm{Ca^{2+}}$ level in blood
- (c) Reabsorption of $\mathrm{Ca^{2+}}$ by renal tubules
- (d) Decreases the absorption of $\mathrm{Ca^{2+}}$ from digested food
- (e) Increases metabolism of carbohydrates

- (1) (a )and (c )only
- **(2)** (b), (d) and (e) only
- (3) (a )and (e )only
- (4) (b) and (c) only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because parathyroid hormone is a hypercalcemic hormone i.e, it increases the blood calcium levels.
2. It also increases the absorption of calcium from digested food.
3. Glucocorticoids regulate the carbohydrate metabolism.
4. Option (3) is not the answer because parathyroid hormone stimulates the process of bone resorption.
5. Option (1) and (4) are not the answers because reabsorption of $\mathrm{Ca^{2+}}$ by renal tubules is a function of PTH.

**Solved independently** (answer withheld)

1. PTH is hypercalcaemic: it stimulates bone resorption, so (a) is an effect.
2. PTH stimulates $\mathrm{Ca^{2+}}$ reabsorption by renal tubules, so (c) is an effect.
3. PTH increases blood $\mathrm{Ca^{2+}}$ and increases $\mathrm{Ca^{2+}}$ absorption from digested food, so (b) and (d) are not effects; carbohydrate metabolism is not a PTH action, so (e) is not an effect.
4. Not effects: (b), (d) and (e), which is option $2$.

**Subtopic:** Thyroid Gland and Parathyroid Gland · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 65)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q193_aab6a7a6_02112026.png?v=aab6a7a63076)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q193_558b4f10_02112026.png?v=558b4f101d3c)

---

## Q194

Biology · zoology · Biotechnology: Principles and Processes

Which of the following is not a desirable feature of a cloning vector?

- (1) Presence of origin of replication
- (2) Presence of a marker gene
- (3) Presence of single restriction enzyme site
- **(4)** Presence of two or more recognition sites

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer.
2. Cloning vectors are the carriers of the desired gene in the host cell.
3. The features desirable in a cloning vector are:-
4. Presence of origin of replication
5. Presence of marker genes
6. Presence of very few, preferably single recognition site for the commonly used restriction enzymes

**Solved independently** (answer withheld)

1. Desirable vector features are an origin of replication (ori), a selectable marker gene and a single (unique) recognition site for a restriction enzyme; two or more recognition sites for the same enzyme would fragment the vector, so the undesirable feature is option $4$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q194_8aa79e42_02112026.png?v=8aa79e42202d)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q194_b18bdebf_02112026.png?v=b18bdebf4afb)

---

## Q195

Biology · zoology · Evolution

Which of the following statements is not true?

- (1) Analogous structures are a result of convergent evolution
- (2) Sweet potato and potato is an example of analogy
- (3) Homology indicates common ancestry
- **(4)** Flippers of penguins and dolphins are a pair of homologous organs

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because flippers of penguins and dolphins are analogous organs as they help in swimming but do not have the same structure.
2. Option (3), (1) and (2) are true statements and hence cannot be the correct answer.
3. Homologous organs have the same structure but have different functions according to the needs of the organisms.
4. Hence, homology indicates common ancestry.
5. Analogous structures have developed for the same function but do not show a similarity in structure.
6. Hence, they are a result of convergent evolution.
7. Sweet potato is a root modification for food storage whereas potato is an underground stem modification for storage.
8. Hence they are analogous.

**Solved independently** (answer withheld)

1. Analogous structures arise from convergent evolution, so statement 1 is true; homology indicates common ancestry, so statement 3 is true; sweet potato (root) and potato (stem) are analogous, so statement 2 is true.
2. Flippers of penguins and dolphins perform the same function but evolved independently, so they are analogous, not homologous; statement $4$ is not true, which is option $4$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q195_3454cff8_02112026.png?v=3454cff871a3)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q195_d4d3ef7c_02112026.png?v=d4d3ef7cd3ed)

---

## Q196

Biology · zoology · Neural Control and Coordination

Select the incorrect statement regarding synapses :

- (1) The membranes of presynaptic and postsynaptic neurons are in close proximity in an electrical synapse.
- (2) Electrical current can flow directly from one neuron into the other across the electrical synapse.
- (3) Chemical synapses use neurotransmitters
- **(4)** Impulse transmission across a chemical synapse is always faster than that across an electrical synapse.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer as impulse transmission across an electrical synapse is always faster than that across a chemical synapse.
2. Chemical synapses use chemicals for transmission which are known as neurotransmitters.
3. The membranes of presynaptic and postsynaptic neurons are in close proximity in an electrical synapse.
4. In an electrical synapse, the transmission of the impulse occurs in the form of an electrical current from one neuron to the next neuron.

**Solved independently** (answer withheld)

1. Options 1, 2 and 3 are true: in an electrical synapse the membranes are very close and current flows directly between neurons, and chemical synapses use neurotransmitters; impulse transmission across an electrical synapse is always faster than across a chemical synapse, so option $4$ is the incorrect statement.

**Subtopic:** Transmission of Impulses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q196_ada166e7_02112026.png?v=ada166e751dc)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q196_e60c8582_02112026.png?v=e60c8582ff0a)

---

## Q197

Biology · zoology · Structural Organisation in Animals

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Match List-I with List-II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Bronchioles | (i) | Dense Regular Connective Tissue |
| (b) | Goblet Cell | (ii) | Loose Connective Tissue |
| (c) | Tendons | (iii) | Glandular Tissue |
| (d) | Adipose Tissue | (iv) | Ciliated Epithelium |

- **(1)** (a) - (iv), (b) - (iii), (c) - (i), (d) - (ii)
- (2) (a) - (i), (b) - (ii), (c) - (iii), (d) - (iv)
- (3) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii)
- (4) (a) - (iii), (b) - (iv), (c) - (ii), (d) - (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because
2. Ciliated epithelium is mainly present in the inner surface of hollow organs like bronchioles and fallopian tubes.
3. The function is to move particles or mucus in a specific direction over the epithelium.
4. Some of the columnar or cuboidal cells get specialised for secretion and are called glandular epithelium.
5. Goblet cells are unicellular glands.
6. Tendons are dense regular connective tissues.
7. They attach skeletal muscles to bones.
8. Adipose tissue is a type of loose connective tissue located mainly beneath the skin.
9. The cells of this tissue are specialised to store fats.

**Solved independently** (answer withheld)

1. Bronchioles are lined by ciliated epithelium, so $(a) \to (iv)$.
2. Goblet cells are unicellular glands of glandular epithelium, so $(b) \to (iii)$.
3. Tendons are dense regular connective tissue, so $(c) \to (i)$.
4. Adipose tissue is a type of loose connective tissue, so $(d) \to (ii)$.
5. The match $(a)-(iv), (b)-(iii), (c)-(i), (d)-(ii)$ is option $1$.

**Subtopic:** Animal Tissues: Epithelial Tissue, Connective Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q197_70755d87_02112026.png?v=70755d87ff5b)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q197_1cbeb861_02112026.png?v=1cbeb8619973)

---

## Q198

Biology · zoology · Reproductive Health

> ⚠ The booklet prints this question's brackets backwards (for example ")a) - (iii("); they are shown the right way round here. The printed form is unchanged in the source crop.

Match List-I with List-II with respect to methods of Contraception and their respective actions. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Diaphragms | (i) | Inhibit ovulation and Implantation |
| (b) | Contraceptive Pills | (ii) | Increase phagocytosis of sperm within Uterus |
| (c) | Intra Uterine Devices | (iii) | Absence of Menstrual cycle and ovulation following parturition |
| (d) | Lactational Amenorrhea | (iv) | They cover the cervix blocking the entry of sperms |

- (1) (a) - (iv), (b) - (i), (c) - (iii), (d) - (ii)
- **(2)** (a) - (iv), (b) - (i), (c) - (ii), (d) - (iii)
- (3) (a) - (ii), (b) - (iv), (c) - (i), (d) - (iii)
- (4) (a) - (iii), (b) - (ii), (c) - (i), (d) - (iv)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because
2. Diaphragms are barrier methods of contraception. They cover the cervix and block the entry of sperms.
3. Contraceptive pills are preparations containing either progestogens alone or combination of progestogen and oestrogen. They inhibit ovulation and implantation as well as alter the quality of cervical mucus to prevent entry of sperms.
4. Intra uterine devices increase the phagocytosis of sperms within the uterus.
5. Lactational amenorrhoea is a natural method of contraception and it is based on the fact that the ovulation and therefore menstrual cycle do not occur during the period of intense lactation following parturition.

**Solved independently** (answer withheld)

1. Diaphragms are barriers that cover the cervix and block sperm entry: $(a) \to (iv)$.
2. Contraceptive pills inhibit ovulation and implantation: $(b) \to (i)$.
3. Intra uterine devices increase phagocytosis of sperm within the uterus: $(c) \to (ii)$.
4. Lactational amenorrhea is the absence of menstruation and ovulation following parturition: $(d) \to (iii)$.
5. The match $a$-$iv$, $b$-$i$, $c$-$ii$, $d$-$iii$ is option $2$.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q198_92f54cbe_02112026.png?v=92f54cbeaa0b)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q198_ead2d451_02112026.png?v=ead2d4512a2f)

---

## Q199

Biology · zoology · Biological Classification

Which of the following is a correct statement?

- **(1)** autotrophic organisms classified under kingdom Monera Cyanobacteria are a group of.
- (2) Bacteria are exclusively heterotrophic organisms.
- (3) Slime moulds are saprophytic organisms classified under Kingdom Monera.
- (4) Mycoplasma have DNA, ribosome and cell wall.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Slime moulds are classified under kingdom Protista.
2. Mycoplasma lack cell wall.
3. Bacteria can be autotrophic as well as heterotrophic.

**Solved independently** (answer withheld)

1. Option 1: cyanobacteria are photosynthetic autotrophs placed in kingdom Monera, so it is true.
2. Option 2: many bacteria are autotrophic (photosynthetic or chemosynthetic), so 'exclusively heterotrophic' is false.
3. Option 3: slime moulds are saprophytic protists placed in kingdom Protista, not Monera, so it is false.
4. Option 4: Mycoplasma lack a cell wall, so it is false; the answer is option $1$.

**Subtopic:** Eubacteria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q199_cf06bca6_02112026.png?v=cf06bca60d6c)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q199_56766cc2_02112026.png?v=56766cc273fc)

---

## Q200

Biology · zoology · Environmental Issues

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statements I) In a scrubber the exhaust from the thermal plant is passed through the electric wires to charge the dust particles.
- (Statement II) Particulate matter (PM 2.5) cannot be removed by scrubber but can be removed by an electrostatic precipitator.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- **(4)** Statement I is incorrect but Statement II is correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Scrubber is used by the industries which produce $\mathrm{SO_2}$ as a by product.
2. The limestone present in slurry of scrubber remove $\mathrm{SO_2}$ from the exhaust.
3. Electrostatic precipitator is the most effective device to remove $99\%$ of particulate matter, ‘even $\mathrm{PM}\ 2.5$’ present in the exhaust.

**Solved independently** (answer withheld)

1. Statement I: passing exhaust through electrode wires to charge dust particles is how an electrostatic precipitator works; a scrubber sprays water or lime to remove gases such as $SO_2$, so Statement I is incorrect.
2. Statement II: a scrubber removes gases, not fine particulate matter, while an electrostatic precipitator removes over $99\%$ of particulate matter, so Statement II is taken as correct.
3. I incorrect and II correct gives option $4$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/crops/q200_1cfe9850_02112026.png?v=1cfe98500609)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2022/2022_Q1/solutions/q200_af91eb61_02112026.png?v=af91eb611b50)

