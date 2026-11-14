# NEET (UG) 2023 · Code E5

200 questions · source `NEET_Papers/2023/Set_E5/NEET_2023_Question_Paper_E5.pdf` · every image a CDN link (0 without one) · 47 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Current Electricity

If the galvanometer $G$ does not show any deflection in the circuit shown, the value of $R$ is given by

![printed figure: Galvanometer bridge: 10 V cell with 400 ohm, R in the middle branch, G and 2 V cell on the right](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q001_d39b97b6_04112026.png?v=d39b97b640ba)

*Galvanometer bridge: 10 V cell with 400 ohm, R in the middle branch, G and 2 V cell on the right*

![drawn: Galvanometer bridge: 10 V cell with 400 ohm, R in the middle branch, G and 2 V cell on the right](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q001_question_7c03d3fa_14112026.svg?v=7c03d3fa5cdd)  
*drawn by code/lib/physics_figure.py*

- (1) $200\,\Omega$
- (2) $50\,\Omega$
- **(3)** $100\,\Omega$
- (4) $400\,\Omega$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Since galvanometer does not show any deflection
2. $\Rightarrow i_g = 0$
3. $\frac{10 - 2}{400} = \frac{2}{R} \Rightarrow R = \frac{2 \times 400}{8} = 100\,\Omega$

**Solved independently** (answer withheld)

1. With no deflection in $G$, no current flows through the $2\,\text{V}$ branch, so the potential difference across $R$ equals $2\,\text{V}$.
2. The $10\,\text{V}$ cell then drives current only through $400\,\Omega$ and $R$ in series: $I = \frac{10}{400 + R}$.
3. $V_R = IR = \frac{10R}{400 + R} = 2$.
4. $10R = 800 + 2R \Rightarrow 8R = 800 \Rightarrow R = 100\,\Omega$, which is option $3$.

**Subtopic:** Kirchhoff's Laws of Current Distribution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q001_14a17212_04112026.png?v=14a17212be21)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q001_942c5831_04112026.png?v=942c58315d6e)

---

## Q2

Physics · Semiconductor Electronics

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Photovoltaic devices can convert optical radiation into electricity.
- (Statement II) Zener diode is designed to operate under reverse bias in breakdown region.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Both Statements are correct.
2. I: Photovoltaic devices convert optical radiation into electricity.
3. II: Zener diode is designed to operate under reverse bias in breakdown region.
4. e.g., Zener diode as a voltage regulator.

**Solved independently** (answer withheld)

1. Statement I: a photovoltaic device such as a solar cell generates an emf when optical radiation falls on it, so it converts light into electricity; Statement I is correct.
2. Statement II: a Zener diode is heavily doped and is designed to operate under reverse bias in the breakdown region (used as a voltage regulator); Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Special Purpose PN Junction Diodes · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q002_5d0140e1_04112026.png?v=5d0140e19c9c)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q002_fe92ece3_04112026.png?v=fe92ece3753e)

---

## Q3

Physics · Semiconductor Electronics

A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?

- (1) A centre-tapped transformer
- (2) p-n junction diodes
- **(3)** Capacitor
- (4) Load resistance

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Capacitor removes the ac ripple from rectified output.

**Solved independently** (answer withheld)

1. The capacitor placed across the load acts as a filter: it charges to the peak voltage and discharges slowly through the load between peaks, removing the ac ripple, so the answer is option $3$.

**Subtopic:** Use of PN Junction Diode as Rectifier · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q003_77995306_04112026.png?v=779953069910)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q003_1f158205_04112026.png?v=1f1582058788)

---

## Q4

Physics · Units and Measurements

The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are

- (1) Instrumental errors
- (2) Personal errors
- (3) Least count errors
- **(4)** Random errors

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The errors which cannot be associated with any systematic or constant cause are called random errors.
2. These errors can arise due to unpredictable fluctuations in experimental conditions. e.g., random change in pressure, temperature, voltage supply etc.

**Solved independently** (answer withheld)

1. NCERT defines random errors as those that occur irregularly and arise from unpredictable fluctuations in experimental conditions such as temperature and voltage supply, so the answer is option $4$.

**Subtopic:** Errors in Measurement · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q004_612d984f_04112026.png?v=612d984f3fa0)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q004_72a5cbaf_04112026.png?v=72a5cbaf0d25)

---

## Q5

Physics · Mechanical Properties of Solids

Let a wire be suspended from the ceiling (rigid support) and stretched by a weight $W$ attached at its free end. The longitudinal stress at any point of cross-sectional area $A$ of the wire is

- (1) $2W/A$
- **(2)** $W/A$
- (3) $W/2A$
- (4) Zero

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Longitudinal stress $= \frac{\text{Internal restoring force}}{\text{Area}} = \frac{F_{ext}}{\text{Area}}$
2. Stress $= \frac{W}{A}$

**Solved independently** (answer withheld)

1. Neglecting the wire's own mass, equilibrium of the hanging weight gives tension $T = W$ at every cross-section of the wire.
2. Longitudinal stress $= \frac{T}{A} = \frac{W}{A}$, which is option $2$.

**Subtopic:** Stress and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q005_a04e275e_04112026.png?v=a04e275ee68a)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q005_3f32f799_04112026.png?v=3f32f7990250)

---

## Q6

Physics · Kinetic Theory of Gases

The temperature of a gas is $-50^\circ\mathrm{C}$. To what temperature the gas should be heated so that the rms speed is increased by 3 times?

- (1) $669^\circ\mathrm{C}$
- **(2)** $3295^\circ\mathrm{C}$
- (3) $3097\,\mathrm{K}$
- (4) $223\,\mathrm{K}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $v_{\mathrm{rms}} = \sqrt{\frac{3RT}{m}}$
2. $T_1 = 273 - 50$
3. $v_{\mathrm{rms}} \propto \sqrt{T}$
4. $= 223\,\mathrm{K}$
5. $v_{\mathrm{rms}}$ is increased by 3 times
6. $T_2 = ?$
7. So, final rms speed $= v + 3v = 4v$
8. $\frac{v_1}{v_2} = \sqrt{\frac{T_1}{T_2}}$
9. $\frac{v}{4v} = \sqrt{\frac{223}{T_2}} \Rightarrow \frac{1}{16} = \frac{223}{T_2}$
10. $T_2 = 3568\,\mathrm{K}$
11. $T_2 = 3568 - 273 = 3295^\circ\mathrm{C}$

**Solved independently** (answer withheld)

1. $T = -50 + 273 = 223\,\mathrm{K}$.
2. $v_{rms} = \sqrt{\frac{3RT}{M}} \propto \sqrt{T}$.
3. Increased by 3 times: $v' = v + 3v = 4v$.
4. $\frac{T'}{T} = \left(\frac{v'}{v}\right)^2 = 16$.
5. $T' = 16 \times 223\,\mathrm{K} = 3568\,\mathrm{K}$.
6. $T' = 3568 - 273 = 3295^\circ\mathrm{C}$, which is option $2$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q006_19490420_04112026.png?v=194904208b0c)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q006_4ada8685_04112026.png?v=4ada8685b453)

---

## Q7

Physics · Electromagnetic Induction

The magnetic energy stored in an inductor of inductance $4\,\mu\mathrm{H}$ carrying a current of $2\,\mathrm{A}$ is

- (1) $4\,\mu\mathrm{J}$
- (2) $4\,\mathrm{mJ}$
- (3) $8\,\mathrm{mJ}$
- **(4)** $8\,\mu\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Magnetic energy stored in an inductor
2. $U = \frac{1}{2}Li^{2}$
3. $= \frac{1}{2} \times 4 \times 10^{-6} \times (2)^{2}$
4. $= 8 \times 10^{-6}\,\mathrm{J}$
5. $U = 8\,\mu\mathrm{J}$

**Solved independently** (answer withheld)

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$.
2. $U = \frac{1}{2} \times (4 \times 10^{-6}\,\mathrm{H}) \times (2\,\mathrm{A})^2$.
3. $U = \frac{1}{2} \times 4 \times 10^{-6} \times 4 = 8 \times 10^{-6}\,\mathrm{J}$.
4. $8 \times 10^{-6}\,\mathrm{J} = 8\,\mu\mathrm{J}$, which is option $4$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q007_493073f5_04112026.png?v=493073f525c2)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q007_112eac46_04112026.png?v=112eac463784)

---

## Q8

Physics · Capacitance

The equivalent capacitance of the system shown in the following circuit is

![printed figure: A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q008_a8664eda_04112026.png?v=a8664edaa59e)

*A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B*

![drawn: A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q008_question_01dd4765_14112026.svg?v=01dd4765869c)  
*drawn by code/lib/physics_figure.py*

- **(1)** $2\,\mu\mathrm{F}$
- (2) $3\,\mu\mathrm{F}$
- (3) $6\,\mu\mathrm{F}$
- (4) $9\,\mu\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For parallel grouping
2. $C_1 = 3 + 3 = 6\,\mu\mathrm{F}$
3. For series grouping
4. $C_{\mathrm{eq}} = \frac{C_1C_2}{C_1 + C_2} = \frac{3 \times 6}{3 + 6} = \frac{18}{9}$
5. $C_{\mathrm{eq}} = 2\,\mu\mathrm{F}$

**Solved independently** (answer withheld)

1. The two $3\,\mu\mathrm{F}$ capacitors between the junction and $B$ are in parallel: $C_p = 3 + 3 = 6\,\mu\mathrm{F}$.
2. This combination is in series with the $3\,\mu\mathrm{F}$ capacitor from $A$: $C_{eq} = \frac{3 \times 6}{3 + 6}$.
3. $C_{eq} = \frac{18}{9} = 2\,\mu\mathrm{F}$, which is option $1$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q008_1ef498c6_04112026.png?v=1ef498c6d101)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q008_110e1427_04112026.png?v=110e14276b64)

---

## Q9

Physics · Mechanical Properties of Fluids

The venturi-meter works on

- (1) Huygen’s principle
- **(2)** Bernoulli’s principle
- (3) The principle of parallel axes
- (4) The principle of perpendicular axes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Venturi-meter works on the Bernoulli’s principle.

**Solved independently** (answer withheld)

1. A venturi-meter measures flow speed from the pressure difference between its wide section and its throat; by continuity $A_1 v_1 = A_2 v_2$ and Bernoulli's principle $P_1 - P_2 = \frac{1}{2}\rho (v_2^2 - v_1^2)$, so it works on Bernoulli's principle, which is option $2$.

**Subtopic:** Venturi Tube and Aspirator Pump Problems · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q009_42a981c7_04112026.png?v=42a981c795ce)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q009_a1ff7e91_04112026.png?v=a1ff7e918ba2)

---

## Q10

Physics · Waves

The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is

- (1) $1:2$
- **(2)** $2:1$
- (3) $1:3$
- (4) $3:1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $f_{0} = f_{\text{open pipe}} = \frac{v}{2l}$
2. $f_{c} = f_{\text{closed pipe}} = \frac{v}{4l}$
3. $\frac{f_{0}}{f_{c}} = \frac{v}{2l} \times \frac{4l}{v}$
4. $f_{0} : f_{c} = 2 : 1$

**Solved independently** (answer withheld)

1. Fundamental of an open pipe: $f_o = \frac{v}{2L}$.
2. Fundamental of a closed pipe: $f_c = \frac{v}{4L}$.
3. $\frac{f_o}{f_c} = \frac{v/2L}{v/4L} = 2$, so the ratio is $2:1$, which is option $2$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q010_7c0b19db_04112026.png?v=7c0b19db27f0)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q010_94e6f14f_04112026.png?v=94e6f14fb317)

---

## Q11

Physics · Ray Optics

Light travels a distance $x$ in time $t_1$ in air and $10x$ in time $t_2$ in another denser medium. What is the critical angle for this medium?

- (1) $\sin^{-1}\left(\frac{t_2}{t_1}\right)$
- (2) $\sin^{-1}\left(\frac{10t_2}{t_1}\right)$
- (3) $\sin^{-1}\left(\frac{t_1}{10\,t_2}\right)$
- **(4)** $\sin^{-1}\left(\frac{10\,t_1}{t_2}\right)$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mu_2 \sin i_c = \mu_1$
2. $\sin i_c = \frac{\mu_1}{\mu_2}$
3. $\mu = \frac{c}{V}$
4. So $\sin i_c = \frac{\mu_1}{\mu_2} = \frac{V_2}{V_1}$
5. $\sin i_c = \frac{10xt_1}{t_2x}$
6. $i_c = \sin^{-1}\left(\frac{10t_1}{t_2}\right)$

**Solved independently** (answer withheld)

1. Speed in air: $c = \frac{x}{t_1}$.
2. Speed in the medium: $v = \frac{10x}{t_2}$.
3. Refractive index: $n = \frac{c}{v} = \frac{x/t_1}{10x/t_2} = \frac{t_2}{10\,t_1}$.
4. Critical angle: $\sin C = \frac{1}{n} = \frac{10\,t_1}{t_2}$.
5. $C = \sin^{-1}\left(\frac{10\,t_1}{t_2}\right)$, which is option $4$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q011_e3cf66c0_04112026.png?v=e3cf66c09040)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q011_c61a120b_04112026.png?v=c61a120b7eb3)

---

## Q12

Physics · Electrostatics

If $\oint_{s} \vec{E}\cdot\overrightarrow{dS} = 0$ over a surface, then

- **(1)** The number of flux lines entering the surface must be equal to the number of flux lines leaving it
- (2) The magnitude of electric field on the surface is constant
- (3) All the charges must necessarily be inside the surface
- (4) The electric field inside the surface is necessarily uniform

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\phi_{\mathrm{net}} = \oint_{s} \vec{E}\cdot\overrightarrow{dS} = 0$
2. $\Rightarrow$ Net flux through surface is zero.
3. $\Rightarrow$ Therefore, the number of flux lines entering the surface must be equal to the number of flux lines leaving it.

**Solved independently** (answer withheld)

1. By Gauss's law, $\oint_s \vec{E}\cdot d\vec{S} = \frac{q_{enc}}{\varepsilon_0}$.
2. Given the flux is $0$, so $q_{enc} = 0$; charges may be outside, so option $3$ is wrong.
3. Zero net flux does not require $|\vec{E}|$ constant on the surface or $\vec{E}$ uniform inside, so options $2$ and $4$ are wrong.
4. Net flux $= \Phi_{out} - \Phi_{in} = 0 \Rightarrow \Phi_{in} = \Phi_{out}$: lines entering equal lines leaving, which is option $1$.

**Subtopic:** Electric Flux · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q012_6a05fad0_04112026.png?v=6a05fad02ac6)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q012_4e425aa3_04112026.png?v=4e425aa3bd24)

---

## Q13

Physics · Alternating Current

A $12\,\mathrm{V}$, $60\,\mathrm{W}$ lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of $220\,\mathrm{V}$. Assuming the transformer to be ideal, what is the current in the primary winding?

- **(1)** $0.27\,\mathrm{A}$
- (2) $2.7\,\mathrm{A}$
- (3) $3.7\,\mathrm{A}$
- (4) $0.37\,\mathrm{A}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For ideal transformer
2. $P_{\mathrm{input}} = P_{\mathrm{output}}$
3. $(VI)_{\mathrm{in}} = 60$
4. $220 \times I = 60$
5. $I = 0.27\,\mathrm{A}$

**Solved independently** (answer withheld)

1. For an ideal transformer, power in the primary equals power in the secondary: $P_p = P_s = 60\,\mathrm{W}$.
2. $I_p = \frac{P_p}{V_p} = \frac{60\,\mathrm{W}}{220\,\mathrm{V}}$.
3. $I_p \approx 0.27\,\mathrm{A}$, which is option $1$.

**Subtopic:** Transformer · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q013_27174267_04112026.png?v=27174267e2b9)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q013_b4d6aa46_04112026.png?v=b4d6aa46bec3)

---

## Q14

Physics · Modern Physics

The minimum wavelength of $X$-rays produced by an electron accelerated through a potential difference of $V$ volts is proportional to

- (1) $\sqrt{V}$
- **(2)** $\frac{1}{V}$
- (3) $\frac{1}{\sqrt{V}}$
- (4) $V^{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $eV = \frac{hc}{\lambda_{\mathrm{min}}}$
2. $\lambda_{\mathrm{min}} = \frac{hc}{eV}$
3. $\lambda_{\mathrm{min}} \propto \frac{1}{V}$

**Solved independently** (answer withheld)

1. The shortest wavelength comes from an electron that gives all of its kinetic energy $eV$ to a single photon: $eV = \frac{hc}{\lambda_{min}}$.
2. $\lambda_{min} = \frac{hc}{eV}$, so $\lambda_{min} \propto \frac{1}{V}$, which is option $2$.

**Subtopic:** Continuous and Characteristic X-Ray Spectra · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q014_74534594_04112026.png?v=745345948303)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q014_d2117be5_04112026.png?v=d2117be521da)

---

## Q15

Physics · Mechanical Properties of Fluids

The amount of energy required to form a soap bubble of radius $2\,\mathrm{cm}$ from a soap solution is nearly (surface tension of soap solution = $0.03\,\mathrm{N\,m^{-1}}$)

- (1) $30.16 \times 10^{-4}\,\mathrm{J}$
- (2) $5.06 \times 10^{-4}\,\mathrm{J}$
- **(3)** $3.01 \times 10^{-4}\,\mathrm{J}$
- (4) $50.1 \times 10^{-4}\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Amount of energy required $= [S \times \Delta A] \times 2$
2. $\Rightarrow$ Energy required $= [0.03 \times 4 \times \pi \times 4 \times 10^{-4}] \times 2$
3. $= 3.015 \times 10^{-4}\,\mathrm{J}$

**Solved independently** (answer withheld)

1. A soap bubble has two free surfaces, so the area created is $A = 2 \times 4\pi r^2 = 8\pi r^2$.
2. $r = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$, so $r^2 = 4 \times 10^{-4}\,\mathrm{m^2}$.
3. $A = 8\pi \times 4 \times 10^{-4} = 32\pi \times 10^{-4}\,\mathrm{m^2} \approx 1.005 \times 10^{-2}\,\mathrm{m^2}$.
4. $W = T A = 0.03 \times 1.005 \times 10^{-2} \approx 3.016 \times 10^{-4}\,\mathrm{J}$.
5. $3.01 \times 10^{-4}\,\mathrm{J}$ is option $3$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q015_88daffd5_04112026.png?v=88daffd5041a)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q015_cff335f5_04112026.png?v=cff335f56332)

---

## Q16

Physics · Current Electricity

The magnitude and direction of the current in the following circuit is

![printed figure: Rectangular loop ABCD: 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm along top AB; 7 ohm along bottom DC](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q016_53bb16ca_04112026.png?v=53bb16ca03fe)

*Rectangular loop ABCD: 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm along top AB; 7 ohm along bottom DC*

![drawn: Rectangular loop ABCD: 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm along top AB; 7 ohm along bottom DC](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q016_question_c64c331e_14112026.svg?v=c64c331ed55e)  
*drawn by code/lib/physics_figure.py*

- (1) $0.2\,\mathrm{A}$ from $B$ to $A$ through $E$
- **(2)** $0.5\,\mathrm{A}$ from $A$ to $B$ through $E$
- (3) $\frac{5}{9}\,\mathrm{A}$ from $A$ to $B$ through $E$
- (4) $1.5\,\mathrm{A}$ from $B$ to $A$ through $E$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Using Kirchhoff's law
2. $i = \frac{10 - 5}{10} = \frac{5}{10}$
3. $i = 0.5\,\mathrm{A}$
4. In clock-wise direction (from $A$ to $B$)

**Solved independently** (answer withheld)

1. The two cells face each other (like terminals toward $E$), so their emfs oppose: $\varepsilon_{net} = 10\,\mathrm{V} - 5\,\mathrm{V} = 5\,\mathrm{V}$.
2. All resistors are in series: $R = 2\,\Omega + 1\,\Omega + 7\,\Omega = 10\,\Omega$.
3. $I = \frac{\varepsilon_{net}}{R} = \frac{5}{10} = 0.5\,\mathrm{A}$.
4. The stronger $10\,\mathrm{V}$ cell sets the direction, driving current from $A$ to $B$ through $E$, which is option $2$.

**Subtopic:** Combination of Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q016_942923e3_04112026.png?v=942923e3a3e1)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q016_1300baed_04112026.png?v=1300baed7570)

---

## Q17

Physics · Modern Physics

The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are $2.14\,\mathrm{eV}$, $2.30\,\mathrm{eV}$ and $2.75\,\mathrm{eV}$ respectively. If incident electromagnetic radiation has an incident energy of $2.20\,\mathrm{eV}$, which of these photosensitive surfaces may emit photoelectrons?

- **(1)** Cs only
- (2) Both Na and K
- (3) K only
- (4) Na only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Energy of incident radiation $= 2.80\,\mathrm{eV}$
2. Work function of $\mathrm{Cs} \rightarrow 2.14\,\mathrm{eV}$
3. Work function of $\mathrm{K} \rightarrow 2.30\,\mathrm{eV}$
4. Work function of $\mathrm{Na} \rightarrow 2.75\,\mathrm{eV}$
5. Since the work function of potassium and sodium are more than energy of incident radiation hence photons may be emitted from caesium.

**Solved independently** (answer withheld)

1. Photoelectrons are emitted only if $E_{photon} \geq \phi$.
2. Cs: $\phi = 2.14\,\mathrm{eV} < 2.20\,\mathrm{eV}$, so Cs emits.
3. K: $\phi = 2.30\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so K does not emit.
4. Na: $\phi = 2.75\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so Na does not emit.
5. Only Cs emits, which is option $1$.

**Subtopic:** Photoelectric Effect · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q017_b0e574fa_04112026.png?v=b0e574fa77e0)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q017_f9d1b33e_04112026.png?v=f9d1b33ef491)

---

## Q18

Physics · Magnetic Effect of Electric Current

The net magnetic flux through any closed surface is

- **(1)** Zero
- (2) Positive
- (3) Infinity
- (4) Negative

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\oint \vec{B} \cdot \overrightarrow{ds} = \text{zero}$
2. Magnetic monopole doesn't exist.
3. Hence net magnetic flux through any closed surface is zero.

**Solved independently** (answer withheld)

1. Gauss's law for magnetism (no isolated magnetic poles) gives $\oint \vec{B} \cdot d\vec{A} = 0$, so the net flux is zero, which is option $1$.

**Subtopic:** Magnetism and Gauss's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q018_26823a8d_04112026.png?v=26823a8d572e)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q018_e6152e52_04112026.png?v=e6152e520ebc)

---

## Q19

Physics · Electromagnetic Waves

In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of $2.0 \times 10^{10}\,\mathrm{Hz}$ and amplitude $48\,\mathrm{V\,m^{-1}}$. Then the amplitude of oscillating magnetic field is (Speed of light in free space $= 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$)

- (1) $1.6 \times 10^{-9}\,\mathrm{T}$
- (2) $1.6 \times 10^{-8}\,\mathrm{T}$
- **(3)** $1.6 \times 10^{-7}\,\mathrm{T}$
- (4) $1.6 \times 10^{-6}\,\mathrm{T}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. From the properties of electromagnetic wave we know that, $C = \frac{E_0}{B_0}$
2. $E_0 \Rightarrow$ Amplitude of oscillating electric field
3. $B_0 \Rightarrow$ Amplitude of oscillating magnetic field
4. $\Rightarrow B_0 = \frac{48}{3 \times 10^{8}} = 1.6 \times 10^{-7}\,\mathrm{T}$

**Solved independently** (answer withheld)

1. For a plane EM wave in free space the field amplitudes are related by $B_0 = \frac{E_0}{c}$.
2. $B_0 = \frac{48\,\mathrm{V\,m^{-1}}}{3 \times 10^{8}\,\mathrm{m\,s^{-1}}} = 16 \times 10^{-8}\,\mathrm{T}$.
3. $16 \times 10^{-8}\,\mathrm{T} = 1.6 \times 10^{-7}\,\mathrm{T}$, which is option $3$.

**Subtopic:** Relation Between E, B, and Speed of Light · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 8)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q019_7a444144_04112026.png?v=7a444144235a)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q019_17d63261_04112026.png?v=17d63261ae9f)

---

## Q20

Physics · Kinematics

A bullet is fired from a gun at the speed of $280\,\mathrm{m\,s^{-1}}$ in the direction $30^\circ$ above the horizontal. The maximum height attained by the bullet is ($g = 9.8\,\mathrm{m\,s^{-2}}$, $\sin 30^\circ = 0.5$)

- (1) $2800\,\mathrm{m}$
- (2) $2000\,\mathrm{m}$
- **(3)** $1000\,\mathrm{m}$
- (4) $3000\,\mathrm{m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $H = \frac{u^{2}\sin^{2}\theta}{2g}$
2. $H = \frac{(280)^{2}(\sin^{2}30)}{2 \times 9.8}$
3. $= \frac{280 \times 280 \times 0.5 \times 0.5}{2 \times 9.8}$
4. $H = 1000\,\mathrm{m}$

**Solved independently** (answer withheld)

1. Maximum height of a projectile: $H = \frac{u^2 \sin^2\theta}{2g}$.
2. Vertical component: $u\sin\theta = 280 \times 0.5 = 140\,\mathrm{m\,s^{-1}}$.
3. $H = \frac{(140)^2}{2 \times 9.8} = \frac{19600}{19.6} = 1000\,\mathrm{m}$, which is option $3$.

**Subtopic:** Maximum Height Reached · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q020_a73cb140_04112026.png?v=a73cb14039bb)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q020_8bf82056_04112026.png?v=8bf8205615d0)

---

## Q21

Physics · Electrostatics

An electric dipole is placed at an angle of $30^\circ$ with an electric field of intensity $2 \times 10^{5}\,\mathrm{N\,C^{-1}}$. It experiences a torque equal to $4\,\mathrm{N\,m}$. Calculate the magnitude of charge on the dipole, if the dipole length is $2\,\mathrm{cm}$.

- (1) $8\,\mathrm{mC}$
- (2) $6\,\mathrm{mC}$
- (3) $4\,\mathrm{mC}$
- **(4)** $2\,\mathrm{mC}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $E = 2 \times 10^{5}\,\mathrm{N/C}$
2. $l = 2\,\mathrm{cm}$
3. $\tau = 4\,\mathrm{Nm}$
4. $\vec{\tau} = \vec{p} \times \vec{E}$
5. $4 = pE\sin\theta$
6. $4 = p \times 2 \times 10^{5} \times \sin 30^\circ$
7. $p = 4 \times 10^{-5}\,\mathrm{cm}$
8. $q = \frac{p}{l} = \frac{4 \times 10^{-5}}{0.02} = 2\,\mathrm{mC}$

**Solved independently** (answer withheld)

1. Torque on a dipole: $\tau = pE\sin\theta = qlE\sin\theta$.
2. Rearrange: $q = \frac{\tau}{lE\sin\theta}$.
3. $q = \frac{4}{(0.02)(2\times10^{5})(0.5)} = \frac{4}{2000}$.
4. $q = 2\times10^{-3}\,\mathrm{C} = 2\,\mathrm{mC}$, which is option $4$.

**Subtopic:** Torque and Work Done in Rotating Dipole in Uniform Electric Field · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q021_6221e595_04112026.png?v=6221e5953aec)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q021_0cf8525c_04112026.png?v=0cf8525ceef3)

---

## Q22

Physics · Wave Optics

For Young’s double slit experiment, two statements are given below: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) If screen is moved away from the plane of slits, angular separation of the fringes remains constant.
- (Statement II) If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- **(3)** Statement I is true but Statement II is false.
- (4) Statement I is false but Statement II is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For YDSE, angular fringe width is given by $\alpha = \frac{\lambda}{d}$
2. It does not depend on the distance of screen from the slit, so statement I is correct.
3. Angular fringe width $\propto \lambda$
4. If $\lambda \uparrow \rightarrow$ angular separation of fringes increases
5. So, statement I is true and statement II is false.

**Solved independently** (answer withheld)

1. Angular separation of fringes in YDSE is $\theta = \frac{\beta}{D} = \frac{\lambda}{d}$.
2. $\theta$ does not depend on $D$, so moving the screen away leaves it constant: Statement I is true.
3. $\theta \propto \lambda$, so a larger wavelength increases the angular separation: Statement II is false.
4. Statement I true, Statement II false is option $3$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q022_5b3a6271_04112026.png?v=5b3a62710386)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q022_66e996ff_04112026.png?v=66e996ff2b38)

---

## Q23

Physics · Laws of Motion

A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is

- (1) Along eastward
- (2) Along northward
- **(3)** Along north-east
- (4) Along south-west

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\Delta\vec{P} = \vec{P}_f - \vec{P}_i$
2. $\vec{P}_f = mu\hat{i}$
3. $\vec{P}_i = mu(-\hat{j})$
4. $\Delta\vec{P} = mu\hat{i} - mu(-\hat{j})$
5. $\Delta\vec{P} = mu(\hat{i} + \hat{j})$
6. $\vec{F} = \frac{\Delta\vec{P}}{\Delta t}$
7. Direction of change of momentum and direction of force acting on the player will be same, so correct answer is North east direction

**Solved independently** (answer withheld)

1. Take east as $\hat{i}$ and north as $\hat{j}$; initial velocity $\vec{v}_1 = -v\hat{j}$ (southward).
2. Final velocity $\vec{v}_2 = v\hat{i}$ (eastward, same speed).
3. $\Delta\vec{v} = \vec{v}_2 - \vec{v}_1 = v\hat{i} + v\hat{j}$.
4. $\vec{F} \propto \Delta\vec{p} = m\Delta\vec{v}$, which is directed at $45^\circ$ between east and north, i.e. north-east, option $3$.

**Subtopic:** Newton's Second Law as Change in Momentum · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q023_fe3c2641_04112026.png?v=fe3c2641d0db)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q023_a58b5804_04112026.png?v=a58b58048b38)

---

## Q24

Physics · Units and Measurements

A metal wire has mass $(0.4 \pm 0.002)\,\mathrm{g}$, radius $(0.3 \pm 0.001)\,\mathrm{mm}$ and length $(5 \pm 0.02)\,\mathrm{cm}$. The maximum possible percentage error in the measurement of density will nearly be

- (1) $1.2\%$
- (2) $1.3\%$
- **(3)** $1.6\%$
- (4) $1.4\%$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know, $\rho = \frac{\text{Mass}}{\text{Volume}} = \frac{M}{\pi r^{2}\ell}$
2. Using the concept of errors we know,
3. $\frac{\Delta\rho}{\rho} = \frac{\Delta M}{M} + \frac{2\Delta r}{r} + \frac{\Delta\ell}{\ell}$
4. $= \left(\frac{0.002}{0.4} + \frac{2 \times 0.001}{0.3} + \frac{0.02}{5}\right)$
5. $\frac{\Delta\rho}{\rho} = 0.0156$
6. $\frac{\Delta\rho}{\rho}\% = 1.56\% \approx 1.6\%$

**Solved independently** (answer withheld)

1. Density of a wire: $\rho = \frac{m}{\pi r^2 l}$.
2. Maximum fractional error: $\frac{\Delta \rho}{\rho} = \frac{\Delta m}{m} + 2\frac{\Delta r}{r} + \frac{\Delta l}{l}$.
3. $\frac{\Delta m}{m} = \frac{0.002}{0.4} = 0.005 = 0.5\%$.
4. $2\frac{\Delta r}{r} = 2 \times \frac{0.001}{0.3} = 0.00667 = 0.667\%$.
5. $\frac{\Delta l}{l} = \frac{0.02}{5} = 0.004 = 0.4\%$.
6. $\frac{\Delta \rho}{\rho} = 0.5\% + 0.667\% + 0.4\% = 1.567\% \approx 1.6\%$, which is option $3$.

**Subtopic:** Errors in Measurement · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q024_4c76e38d_04112026.png?v=4c76e38dfa7c)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q024_9c2ebba4_04112026.png?v=9c2ebba45be0)

---

## Q25

Physics · Alternating Current

An ac source is connected to a capacitor $C$. Due to decrease in its operating frequency

- (1) Capacitive reactance decreases
- (2) Displacement current increases
- **(3)** Displacement current decreases
- (4) Capacitive reactance remains constant

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $X_C = \frac{1}{\omega C}$
2. Since $\omega$ decreasing $X_C$ will increases hence current will decreases also
3. conduction current = displacement current
4. Therefore displacement current will decrease.

**Solved independently** (answer withheld)

1. Capacitive reactance is $X_C = \frac{1}{2\pi f C}$.
2. As $f$ decreases, $X_C$ increases, ruling out options $4$ and $1$.
3. Conduction current $I = \frac{V}{X_C}$ therefore decreases.
4. The displacement current between the plates equals the conduction current, $I_d = I$, so $I_d$ decreases, which is option $3$.

**Subtopic:** Variation of Reactance with Frequency · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q025_bbe31ce6_04112026.png?v=bbe31ce6bd79)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q025_f1a068eb_04112026.png?v=f1a068eb04c1)

---

## Q26

Physics · Current Electricity

Resistance of a carbon resistor determined from colour codes is $(22000 \pm 5\%)\,\Omega$. The colour of third band must be

- (1) Red
- (2) Green
- **(3)** Orange
- (4) Yellow

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Resistance $= (22 \times 10^{3})\,\Omega \pm 5\%$
2. Third band corresponds to decimal multiplier.
3. Decimal multiplier $= 10^{3}$
4. $\Rightarrow$ Colour $\rightarrow$ Orange

**Solved independently** (answer withheld)

1. Write the value as two significant digits times a power of ten: $22000\,\Omega = 22 \times 10^{3}\,\Omega$.
2. The first two bands give the digits $2, 2$, and the third band gives the multiplier $10^{3}$.
3. In the colour code, multiplier $3$ is orange, so the third band is orange, option $3$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q026_36a31aaf_04112026.png?v=36a31aaf7634)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q026_d60cc838_04112026.png?v=d60cc8383176)

---

## Q27

Physics · Thermodynamics

A Carnot engine has an efficiency of $50\%$ when its source is at a temperature $327^\circ\mathrm{C}$. The temperature of the sink is

- **(1)** $27^\circ\mathrm{C}$
- (2) $15^\circ\mathrm{C}$
- (3) $100^\circ\mathrm{C}$
- (4) $200^\circ\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Efficiency $\eta = \frac{50}{100} = \frac{1}{2}$
2. Efficiency of Carnot engine
3. $\eta = 1 - \frac{T_2}{T_1}$
4. $\eta = 1 - \frac{T_2}{600}$
5. $\frac{1}{2} = 1 - \frac{T_2}{600}$
6. $\frac{T_2}{600} = \frac{1}{2} \Rightarrow T_2 = 300\,\mathrm{K}$
7. $T_2 = 300 - 273 = 27^\circ\mathrm{C}$

**Solved independently** (answer withheld)

1. Convert the source temperature to kelvin: $T_1 = 327 + 273 = 600\,\mathrm{K}$.
2. Carnot efficiency: $\eta = 1 - \frac{T_2}{T_1}$.
3. $0.5 = 1 - \frac{T_2}{600} \Rightarrow T_2 = 300\,\mathrm{K}$.
4. $T_2 = 300 - 273 = 27^{\circ}\mathrm{C}$, which is option $1$.

**Subtopic:** Carnot Engine · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 10)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q027_e57d0924_04112026.png?v=e57d09243022)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q027_5f6ff9da_04112026.png?v=5f6ff9da8697)

---

## Q28

Physics · Rotational Motion

The angular acceleration of a body, moving along the circumference of a circle, is

- (1) Along the radius, away from centre
- (2) Along the radius towards the centre
- (3) Along the tangent to its position
- **(4)** Along the axis of rotation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Angular acceleration of a body, moving along the circumference of a circle is along the axis of rotation.

**Solved independently** (answer withheld)

1. $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$, and for motion on a fixed circle $\vec{\omega}$ lies along the axis of rotation, so $\vec{\alpha}$ is along the axis of rotation, which is option $4$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 11)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q028_041db33e_04112026.png?v=041db33ea53b)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q028_b8bd2c19_04112026.png?v=b8bd2c190b63)

---

## Q29

Physics · Alternating Current

In a series $LCR$ circuit, the inductance $L$ is $10\,\mathrm{mH}$, capacitance $C$ is $1\,\mu\mathrm{F}$ and resistance $R$ is $100\,\Omega$. The frequency at which resonance occurs is

- (1) $15.9\,\mathrm{rad/s}$
- (2) $15.9\,\mathrm{kHz}$
- (3) $1.59\,\mathrm{rad/s}$
- **(4)** $1.59\,\mathrm{kHz}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For resonance frequency $= \frac{1}{2\pi\sqrt{LC}}$
2. $\Rightarrow f = \frac{1}{2\times\pi\times\sqrt{10\times10^{-3}\times1\times10^{-6}}} = \frac{10^{4}}{2\pi}$
3. $= 1.591\times10^{3}$
4. $= 1.591\,\mathrm{kHz}$

**Solved independently** (answer withheld)

1. At resonance $X_L = X_C$, so $\omega_0 = \frac{1}{\sqrt{LC}}$; the resistance $R$ plays no part.
2. $LC = (10\times10^{-3}\,\mathrm{H})(1\times10^{-6}\,\mathrm{F}) = 10^{-8}\,\mathrm{s^2}$.
3. $\sqrt{LC} = 10^{-4}\,\mathrm{s}$, so $\omega_0 = 10^{4}\,\mathrm{rad/s}$.
4. $f_0 = \frac{\omega_0}{2\pi} = \frac{10^4}{2\pi} \approx 1591.5\,\mathrm{Hz} \approx 1.59\,\mathrm{kHz}$, which is option $4$.

**Subtopic:** Resonance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q029_c5949896_04112026.png?v=c5949896666f)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q029_b6133ea1_04112026.png?v=b6133ea1a070)

---

## Q30

Physics · Kinematics

A vehicle travels half the distance with speed $v$ and the remaining distance with speed $2v$. Its average speed is

- (1) $\frac{v}{3}$
- (2) $\frac{2v}{3}$
- **(3)** $\frac{4v}{3}$
- (4) $\frac{3v}{4}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $v_{\mathrm{avg}} = \frac{2v_1v_2}{v_1 + v_2}$
2. $= \frac{2 \times v \times 2v}{v + 2v}$
3. $= \frac{4v}{3}$

**Solved independently** (answer withheld)

1. Let total distance be $d$; each half is $\frac{d}{2}$.
2. $t_1 = \frac{d/2}{v} = \frac{d}{2v}$.
3. $t_2 = \frac{d/2}{2v} = \frac{d}{4v}$.
4. $t = t_1 + t_2 = \frac{3d}{4v}$.
5. $v_{avg} = \frac{d}{t} = \frac{4v}{3}$, which is option $3$.

**Subtopic:** Average Speed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q030_8d67983d_04112026.png?v=8d67983d62c5)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q030_5dd7c7b5_04112026.png?v=5dd7c7b5c2cc)

---

## Q31

Physics · Modern Physics

In hydrogen spectrum, the shortest wavelength in the Balmer series is $\lambda$. The shortest wavelength in the Bracket series is

- (1) $2\lambda$
- **(2)** $4\lambda$
- (3) $9\lambda$
- (4) $16\lambda$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\frac{1}{\lambda} = R\left[\frac{1}{n_2^2} - \frac{1}{n_1^2}\right]$
2. For Balmer $[n_2 = 2,\ n_1 = \infty]$
3. $\frac{1}{\lambda} = R\left[\frac{1}{4} - \frac{1}{\infty}\right]$
4. $\lambda = \frac{4}{R}$ $\ldots(1)$
5. For Bracket, $(n_2 = 4,\ n_1 = \infty)$
6. $\frac{1}{\lambda'} = R\left[\frac{1}{16} - \frac{1}{\infty}\right]$
7. $\lambda' = \frac{16}{R}$ $\ldots(2)$
8. $\frac{\mathrm{Eq}^{n}(1)}{\mathrm{Eq}^{n}(2)}$
9. $\lambda' = 4\lambda$

**Solved independently** (answer withheld)

1. The shortest wavelength of a series is its series limit, $n_2 \to \infty$, so $\frac{1}{\lambda_{min}} = \frac{R}{n_1^2}$.
2. Balmer ($n_1 = 2$): $\frac{1}{\lambda} = \frac{R}{4}$, so $\lambda = \frac{4}{R}$.
3. Brackett ($n_1 = 4$): $\frac{1}{\lambda'} = \frac{R}{16}$, so $\lambda' = \frac{16}{R}$.
4. $\frac{\lambda'}{\lambda} = \frac{16}{4} = 4$, so $\lambda' = 4\lambda$, which is option $2$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 12)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q031_7223e0c9_04112026.png?v=7223e0c9aa93)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q031_8145f50c_04112026.png?v=8145f50c1fc5)

---

## Q32

Physics · Rotational Motion

> ⚠ The booklet prints "Answer (1*)" for the radius-of-gyration ratio (solid sphere : hollow sphere). The publisher's own solution (2023_E5 q032) says "* None of the option is correct (correct answer is sqrt(3/5))". The true ratio is sqrt(3):sqrt(5); the starred option (1), 3:5, is its square, so the square roots were lost from the printed options. Same question as 2023_F1 q001.

The ratio of radius of gyration of a solid sphere of mass $M$ and radius $R$ about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is

- **(1)** $3:5$
- (2) $5:3$
- (3) $2:5$
- (4) $5:2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Radius of gyration of solid sphere about its own axis $= \sqrt{\frac{2}{5}}R$
2. Radius of gyration of hollow sphere about its own axis $= \sqrt{\frac{2}{3}}R$
3. $\Rightarrow$ Required ratio $= \sqrt{\frac{2}{5}} \times \sqrt{\frac{3}{2}} = \sqrt{\frac{3}{5}}$
4. * None of the option is correct (correct answer is $\sqrt{\frac{3}{5}}$)

**Solved independently** (answer withheld)

1. For a solid sphere about a diameter, $I_1 = \frac{2}{5}MR^2 = Mk_1^2$, so $k_1 = \sqrt{\frac{2}{5}}\,R$.
2. For a thin hollow sphere about a diameter, $I_2 = \frac{2}{3}MR^2 = Mk_2^2$, so $k_2 = \sqrt{\frac{2}{3}}\,R$.
3. $\frac{k_1}{k_2} = \sqrt{\frac{2/5}{2/3}} = \sqrt{\frac{3}{5}}$, i.e. $\sqrt{3}:\sqrt{5}$.
4. No option is $\sqrt{3}:\sqrt{5}$; option $1$ ($3:5$) is the same ratio with the square roots dropped, so option $1$ is the best match.

**Subtopic:** Radius of Gyration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q032_c84098cc_04112026.png?v=c84098cc9204)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q032_b983e34f_04112026.png?v=b983e34fb076)

---

## Q33

Physics · Modern Physics

The half life of a radioactive substance is $20$ minutes. In how much time, the activity of substance drops to $\left(\frac{1}{16}\right)^{\text{th}}$ of its initial value?

- (1) $20$ minutes
- (2) $40$ minutes
- (3) $60$ minutes
- **(4)** $80$ minutes

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $A = \frac{A_0}{2^n}$
2. $\frac{A}{A_0} = \frac{1}{2^n}$
3. $\frac{1}{16} = \frac{1}{2^n}$
4. $\frac{1}{2^4} = \frac{1}{2^n}$
5. $n = 4$
6. $n = \frac{t}{T_{\frac{1}{2}}}$, $t = 4 \times T_{\frac{1}{2}} = 4 \times 20$
7. $= 80$ minutes

**Solved independently** (answer withheld)

1. Activity after $n$ half-lives: $\frac{A}{A_0} = \left(\frac{1}{2}\right)^n$.
2. $\frac{1}{16} = \left(\frac{1}{2}\right)^4 \Rightarrow n = 4$.
3. $t = n\,T_{1/2} = 4 \times 20\,\text{min} = 80\,\text{min}$, which is option $4$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 12)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q033_bbe5e8c6_04112026.png?v=bbe5e8c6c15c)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q033_a070d281_04112026.png?v=a070d281c27b)

---

## Q34

Physics · Gravitation

Two bodies of mass $m$ and $9m$ are placed at a distance $R$. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be ($G$ = gravitational constant)

- (1) $-\dfrac{8Gm}{R}$
- (2) $-\dfrac{12Gm}{R}$
- **(3)** $-\dfrac{16Gm}{R}$
- (4) $-\dfrac{20Gm}{R}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Let electric field at point $Q$ be zero
2. So,
3. $\frac{Gm}{x^{2}} = \frac{G(9m)}{(R - x)^{2}}$
4. $\frac{(R - x)^{2}}{x^{2}} = 9$
5. $x = \frac{R}{4}$
6. $V_{P} = \frac{-Gm}{x} - \frac{G(9m)}{R - x}$
7. $V_{P} = \frac{-Gm}{\frac{R}{4}} - \frac{G(9m)}{\frac{3R}{4}}$
8. $= \frac{-4Gm}{R} - \frac{12Gm}{R}$
9. $= \frac{-16Gm}{R}$

**Solved independently** (answer withheld)

1. At the null point a distance $x$ from $m$: $\frac{Gm}{x^2} = \frac{G(9m)}{(R-x)^2}$.
2. Taking square roots: $R - x = 3x$, so $x = \frac{R}{4}$.
3. Distance from $9m$ is $R - \frac{R}{4} = \frac{3R}{4}$.
4. $V = -\frac{Gm}{R/4} - \frac{G(9m)}{3R/4} = -\frac{4Gm}{R} - \frac{12Gm}{R}$.
5. $V = -\frac{16Gm}{R}$, which is option $3$.

**Subtopic:** Calculation of Gravitational Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q034_3bcee5be_04112026.png?v=3bcee5be526b)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q034_d9de01db_04112026.png?v=d9de01db0870)

---

## Q35

Physics · Work, Energy and Power

The potential energy of a long spring when stretched by $2\,\mathrm{cm}$ is $U$. If the spring is stretched by $8\,\mathrm{cm}$, potential energy stored in it will be

- (1) $2U$
- (2) $4U$
- (3) $8U$
- **(4)** $16U$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Potential energy stored in spring $U = \frac{1}{2}Kx^{2}$
2. $U = \frac{1}{2}K(2)^{2}$ where $x = 2\,\mathrm{cm}$
3. $U = \frac{1}{2}(K)\cdot(4)$
4. $U = 2\,K$ ....(i)
5. $U' = \frac{1}{2}K(8)^{2}$
6. $U' = \frac{1}{2}K \times 64 = 32K$ ....(ii)
7. On dividing (i) by (ii)
8. $\frac{U}{U'} = \frac{2K}{32K} = \frac{1}{16}$
9. $U' = 16\,U$

**Solved independently** (answer withheld)

1. Elastic potential energy of a spring: $U = \frac{1}{2}kx^2$, so $U \propto x^2$.
2. $\frac{U'}{U} = \left(\frac{8\,\mathrm{cm}}{2\,\mathrm{cm}}\right)^2 = 4^2 = 16$.
3. $U' = 16U$, which is option $4$.

**Subtopic:** Potential Energy of Spring · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 14)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q035_45796a93_04112026.png?v=45796a93d393)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q035_53fa7ebf_04112026.png?v=53fa7ebff30e)

---

## Q36

Physics · Semiconductor Electronics

For the following logic circuit, the truth table is

![printed figure: Inputs A and B each pass through a NOT gate into a NAND gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q036_40d42e79_04112026.png?v=40d42e7908bb)

*Inputs A and B each pass through a NOT gate into a NAND gate giving Y*

![drawn: Inputs A and B each pass through a NOT gate into a NAND gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q036_question_9c80b1b7_14112026.svg?v=9c80b1b759b9)  
*drawn by code/lib/physics_figure.py*

- (1) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- **(2)** $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{array}$
- (3) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (4) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $Y = \overline{\overline{A} \cdot \overline{B}} = A + B$
2. It is OR gate.
3. $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{array}$

**Solved independently** (answer withheld)

1. The figure shows $A$ and $B$ each inverted, then fed to a NAND gate, so $Y = \overline{\bar{A}\cdot\bar{B}}$.
2. By De Morgan's theorem, $\overline{\bar{A}\cdot\bar{B}} = \bar{\bar{A}} + \bar{\bar{B}} = A + B$.
3. So the circuit is an OR gate: $Y = 0, 1, 1, 1$ for $AB = 00, 01, 10, 11$, which is option $2$.

**Subtopic:** Logic Gates · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q036_75940793_04112026.png?v=759407937d95)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q036_49a22856_04112026.png?v=49a22856c20b)

---

## Q37

Physics · Laws of Motion

Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is $0.15$ ($g = 10\,\mathrm{m\,s^{-2}}$).

- (1) $1.2\,\mathrm{m\,s^{-2}}$
- (2) $150\,\mathrm{m\,s^{-2}}$
- **(3)** $1.5\,\mathrm{m\,s^{-2}}$
- (4) $50\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. w.r.t. car
2. $a_{b} = 0$
3. $ma_{\mathrm{max}} = \mu_{s}\,mg$
4. $a_{\mathrm{max}} = \mu_{s}\,g = 0.15 \times 10 = 1.5\,\mathrm{m/s^{2}}$

**Solved independently** (answer withheld)

1. To stay at rest relative to the car, the body must accelerate with the car, and only static friction can supply that force: $ma \le f_{s,\max} = \mu_s m g$.
2. Cancel $m$: $a_{\max} = \mu_s g$.
3. $a_{\max} = 0.15 \times 10 = 1.5\,\mathrm{m\,s^{-2}}$, which is option $3$.

**Subtopic:** Static Friction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q037_3df98939_04112026.png?v=3df98939bf4c)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q037_38d670d6_04112026.png?v=38d670d61e94)

---

## Q38

Physics · Modern Physics

The radius of inner most orbit of hydrogen atom is $5.3 \times 10^{-11}\,\mathrm{m}$. What is the radius of third allowed orbit of hydrogen atom?

- (1) $0.53\,\mathring{\mathrm{A}}$
- (2) $1.06\,\mathring{\mathrm{A}}$
- (3) $1.59\,\mathring{\mathrm{A}}$
- **(4)** $4.77\,\mathring{\mathrm{A}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $r_n = \frac{n^2}{Z}$
2. $\frac{r_1}{r_2} = \left(\frac{1}{3}\right)^2$
3. $r_2 = 9r_1 = 5.3 \times 10^{-11} \times 9$
4. $= 47.7 \times 10^{-11}$
5. $= 4.77\,\mathring{\mathrm{A}}$

**Solved independently** (answer withheld)

1. In the Bohr model $r_n = n^2 r_1$.
2. $r_1 = 5.3 \times 10^{-11}\,\mathrm{m} = 0.53\,\mathring{\mathrm{A}}$.
3. $r_3 = 3^2 \times 0.53\,\mathring{\mathrm{A}} = 4.77\,\mathring{\mathrm{A}}$, which is option $4$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q038_892c66af_04112026.png?v=892c66af1816)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q038_13df43f6_04112026.png?v=13df43f69327)

---

## Q39

Physics · Kinematics

A bullet from a gun is fired on a rectangular wooden block with velocity $u$. When bullet travels $24\,\mathrm{cm}$ through the block along its length horizontally, velocity of bullet becomes $\frac{u}{3}$. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is

- **(1)** $27\,\mathrm{cm}$
- (2) $24\,\mathrm{cm}$
- (3) $28\,\mathrm{cm}$
- (4) $30\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. between $1$ to $2$
2. $\left(\frac{u}{3}\right)^{2} = u^{2} - 2a \times 24$
3. $\Rightarrow 2a(24) = \frac{8u^{2}}{9} \quad \ldots(\mathrm{I})$
4. between $2$ to $3$
5. $0 = \left(\frac{u}{3}\right)^{2} - 2as \quad \ldots(\mathrm{II})$
6. From equation (I) and (II)
7. $2as = \frac{2a(24)}{8}$
8. $s = 3\,\mathrm{cm}$
9. Length of wooden block is $24 + 3 = 27\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Assume uniform retardation $a$ inside the block and apply $v^2 = u^2 - 2as$ to the first $24\,\mathrm{cm}$.
2. $u^2 - \left(\frac{u}{3}\right)^2 = 2a(24) \Rightarrow \frac{8u^2}{9} = 48a$.
3. $2a = \frac{8u^2}{9 \times 24} = \frac{u^2}{27}$.
4. For the remaining distance $x$ the bullet goes from $\frac{u}{3}$ to rest: $\left(\frac{u}{3}\right)^2 = 2a x$.
5. $\frac{u^2}{9} = \frac{u^2}{27} x \Rightarrow x = 3\,\mathrm{cm}$.
6. Total length $L = 24 + 3 = 27\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Third Equation of Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q039_f1235b8a_04112026.png?v=f1235b8ab103)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q039_6a0293b0_04112026.png?v=6a0293b0d447)

---

## Q40

Physics · Alternating Current

The net impedance of circuit (as shown in figure) will be

![printed figure: Series L, C, R across an AC source 220 V, 50 Hz](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q040_43e1199d_04112026.png?v=43e1199d3aaa)

*Series L, C, R across an AC source 220 V, 50 Hz*

![drawn: Series L, C, R across an AC source 220 V, 50 Hz](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q040_question_d92774e5_14112026.svg?v=d92774e58690)  
*drawn by code/lib/physics_figure.py*

- (1) $10\sqrt{2}\,\Omega$
- (2) $15\,\Omega$
- **(3)** $5\sqrt{5}\,\Omega$
- (4) $25\,\Omega$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $L = \frac{50}{\pi}\,\mathrm{mH}$
2. $X_L = 2\pi \times 50 \times \frac{50}{\pi} \times 10^{-3} = 5\,\Omega$
3. $C = \frac{10^{3}}{\pi} \times 10^{-6}$
4. $X_C = \frac{1 \times \pi}{2\pi \times 50 \times 10^{3} \times 10^{-6}} = \frac{10^{3}}{100} = 10\,\Omega$
5. $Z = \sqrt{(X_C - X_L)^{2} + R^{2}}$
6. $Z = \sqrt{(10 - 5)^{2} + 10^{2}} = \sqrt{125} = 5\sqrt{5}\,\Omega$

**Solved independently** (answer withheld)

1. Series LCR circuit with $R = 10\,\Omega$, $L = \frac{50}{\pi}\,\text{mH}$, $C = \frac{10^3}{\pi}\,\mu\text{F}$, $f = 50\,\text{Hz}$.
2. $X_L = 2\pi f L = 2\pi (50) \frac{50}{\pi}\times 10^{-3} = 5\,\Omega$.
3. $X_C = \frac{1}{2\pi f C} = \frac{1}{2\pi (50) \frac{10^3}{\pi}\times 10^{-6}} = \frac{1}{0.1} = 10\,\Omega$.
4. $Z = \sqrt{R^2 + (X_C - X_L)^2} = \sqrt{10^2 + 5^2} = \sqrt{125}$.
5. $\sqrt{125} = 5\sqrt{5}\,\Omega$, which is option $3$.

**Subtopic:** Impedance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q040_525cc46c_04112026.png?v=525cc46cbb1c)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q040_ba03fdc3_04112026.png?v=ba03fdc3c897)

---

## Q41

Physics · Gravitation

A satellite is orbiting just above the surface of the earth with period $T$. If $d$ is the density of the earth and $G$ is the universal constant of gravitation, the quantity $\frac{3\pi}{Gd}$ represents

- (1) $T$
- **(2)** $T^{2}$
- (3) $T^{3}$
- (4) $\sqrt{T}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Time period of satellite above earth surface
2. $T = 2\pi\sqrt{\frac{R^{3}}{GM}} = 2\pi\sqrt{\frac{R^{3}}{Gd\frac{4}{3}\pi R^{3}}}$
3. $T = 2\pi\sqrt{\frac{3}{4\pi Gd}}$
4. $T = \sqrt{\frac{3\pi}{Gd}}$
5. $T^{2} = \frac{3\pi}{Gd}$

**Solved independently** (answer withheld)

1. For an orbit just above the surface, $r \approx R$, so $T = 2\pi\sqrt{\frac{R^{3}}{GM}}$.
2. Squaring: $T^{2} = \frac{4\pi^{2}R^{3}}{GM}$.
3. Mass of the earth in terms of density: $M = \frac{4}{3}\pi R^{3} d$.
4. Substitute: $T^{2} = \frac{4\pi^{2}R^{3}}{G \cdot \frac{4}{3}\pi R^{3} d} = \frac{3\pi}{Gd}$.
5. So $\frac{3\pi}{Gd} = T^{2}$, which is option $2$.

**Subtopic:** Motion of a Satellite · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q041_af6e73b9_04112026.png?v=af6e73b940f5)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q041_464c0b94_04112026.png?v=464c0b945358)

---

## Q42

Physics · Magnetic Effect of Electric Current

A very long conducting wire is bent in a semi-circular shape from $A$ to $B$ as shown in figure. The magnetic field at point $P$ for steady current configuration is given by

![printed figure: Long wire with a semicircular bend of radius R from A to B; point P near its centre](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q042_ba5b125d_04112026.png?v=ba5b125df174)

*Long wire with a semicircular bend of radius R from A to B; point P near its centre*

![drawn: Long wire with a semicircular bend of radius R from A to B; point P near its centre](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q042_question_ddade8de_14112026.svg?v=ddade8dededa)  
*drawn by code/lib/physics_figure.py*

- (1) $\dfrac{\mu_0 i}{4R}$ pointed into the page
- (2) $\dfrac{\mu_0 i}{4R}$ pointed away from the page
- **(3)** $\dfrac{\mu_0 i}{4R}\left[1-\dfrac{2}{\pi}\right]$ pointed away from page
- (4) $\dfrac{\mu_0 i}{4R}\left[1-\dfrac{2}{\pi}\right]$ pointed into the page

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $B_P$ due to wire 1 $= \frac{\mu_0 i}{4\pi R} \otimes$
2. $B_P$ due to wire 3 $= \frac{\mu_0 i}{4\pi R} \otimes$
3. $B_P$ due to wire 2 $= \frac{\mu_0 i}{4R} \odot$
4. $B_{\mathrm{net}} = -\frac{\mu_0 i}{2\pi R} + \frac{\mu_0 i}{4R} = \frac{\mu_0 i}{4R}\left[-\frac{2}{\pi} + 1\right] = \frac{\mu_0 i}{4R}\left[1 - \frac{2}{\pi}\right]$
5. Pointed away from page.

**Solved independently** (answer withheld)

1. $P$ is the centre of the semicircle, and $A$, $B$ are the feet of the perpendiculars from $P$ to the two semi-infinite straight wires, each at distance $R$.
2. Semicircular arc (current from $A$ down the left side to $B$): $B_{arc} = \frac{\mu_0 i}{4R}$, directed out of the page by the right-hand rule.
3. Upper semi-infinite wire (current rightward, $P$ below it, ending at $A$): $B_1 = \frac{\mu_0 i}{4\pi R}$, into the page.
4. Lower semi-infinite wire (current leftward, $P$ above it, starting at $B$): $B_2 = \frac{\mu_0 i}{4\pi R}$, into the page.
5. Net: $B = \frac{\mu_0 i}{4R} - \frac{2\mu_0 i}{4\pi R} = \frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$, out of the page, which is option $3$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 17)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q042_886e16ff_04112026.png?v=886e16ff212a)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q042_65764927_04112026.png?v=6576492701df)

---

## Q43

Physics · Current Electricity

The resistance of platinum wire at $0^\circ\mathrm{C}$ is $2\,\Omega$ and $6.8\,\Omega$ at $80^\circ\mathrm{C}$. The temperature coefficient of resistance of the wire is

- (1) $3 \times 10^{-4}\,^\circ\mathrm{C}^{-1}$
- (2) $3 \times 10^{-3}\,^\circ\mathrm{C}^{-1}$
- **(3)** $3 \times 10^{-2}\,^\circ\mathrm{C}^{-1}$
- (4) $3 \times 10^{-1}\,^\circ\mathrm{C}^{-1}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Using $R = R_0(1 + \alpha\Delta T)$
2. where $\alpha$ is the thermal coefficient of resistance
3. $6.8 = 2\{1 + \alpha(80 - 0)\}$
4. $\frac{6.8}{2} - 1 = \alpha \times 80$
5. $\alpha = \frac{3.4 - 1}{80} = \frac{2.4}{80} = 0.03$
6. $\therefore\ \alpha = 3 \times 10^{-2}\,^\circ\mathrm{C}^{-1}$

**Solved independently** (answer withheld)

1. Use $R_T = R_0(1 + \alpha T)$, so $\alpha = \frac{R_T - R_0}{R_0 T}$.
2. $R_T - R_0 = 6.8\,\Omega - 2\,\Omega = 4.8\,\Omega$.
3. $R_0 T = 2\,\Omega \times 80^{\circ}\mathrm{C} = 160\,\Omega\,^{\circ}\mathrm{C}$.
4. $\alpha = \frac{4.8}{160} = 0.03 = 3 \times 10^{-2}\,^{\circ}\mathrm{C}^{-1}$, which is option $3$.

**Subtopic:** Temperature Coefficient of Resistance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q043_5a6c0b9d_04112026.png?v=5a6c0b9dde03)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q043_80157b49_04112026.png?v=80157b495ff6)

---

## Q44

Physics · Current Electricity

10 resistors, each of resistance $R$ are connected in series to a battery of emf $E$ and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased $n$ times. The value of $n$ is

- (1) $10$
- **(2)** $100$
- (3) $1$
- (4) $1000$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In series combination
2. $R_{\mathrm{eq}} = 10R$
3. $i = \frac{E}{10R}$
4. In parallel combination
5. $R_{\mathrm{eq}} = \frac{R}{10}$
6. $i' = \frac{E}{\frac{R}{10}} = \frac{10\,E}{R}$
7. $i' = 10 \times 10\,i = 100\,i$
8. $n = 100$

**Solved independently** (answer withheld)

1. In series, $R_s = 10R$, so $I_s = \frac{E}{10R}$.
2. In parallel, $R_p = \frac{R}{10}$, so $I_p = \frac{E}{R/10} = \frac{10E}{R}$.
3. $n = \frac{I_p}{I_s} = \frac{10E/R}{E/(10R)} = 100$, which is option $2$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q044_f5bdc444_04112026.png?v=f5bdc44448ff)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q044_59f3db4a_04112026.png?v=59f3db4adcc6)

---

## Q45

Physics · Oscillations

The $x$-$t$ graph of a particle performing simple harmonic motion is shown in the figure. The acceleration of the particle at $t = 2\,\mathrm{s}$ is

![printed figure: x-t graph of a particle in SHM: sine curve of amplitude 1 m and period 8 s](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q045_f9ac2788_04112026.png?v=f9ac2788cca8)

*x-t graph of a particle in SHM: sine curve of amplitude 1 m and period 8 s*

![drawn: x-t graph of a particle in SHM: sine curve of amplitude 1 m and period 8 s](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q045_question_8551b6fe_14112026.svg?v=8551b6fe5571)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$
- (2) $-\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$
- (3) $\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$
- **(4)** $-\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Position of particle as function of time
2. $x = A\sin\omega t$
3. From figure,
4. $A = 1$
5. $\omega = \frac{2\pi}{8}$
6. $x = \sin\frac{\pi}{4}t$
7. $v = \frac{dx}{dt}$
8. $v = \frac{\pi}{4}\cos\frac{\pi}{4}t$
9. $a = \frac{dv}{dt}$
10. $a = -\frac{\pi^2}{16}\sin\frac{\pi}{4}t$
11. at $t = 2\,\mathrm{s}$
12. $a = -\frac{\pi^2}{16}\,\mathrm{m/s^2}$

**Solved independently** (answer withheld)

1. From the graph, amplitude $A = 1\,\mathrm{m}$ and period $T = 8\,\mathrm{s}$, with $x = 0$ at $t = 0$, so $x = \sin\left(\frac{\pi t}{4}\right)$.
2. $\omega = \frac{2\pi}{T} = \frac{2\pi}{8} = \frac{\pi}{4}\,\mathrm{rad\,s^{-1}}$.
3. At $t = 2\,\mathrm{s}$, $x = \sin\left(\frac{\pi}{2}\right) = 1\,\mathrm{m}$.
4. $a = -\omega^2 x = -\left(\frac{\pi}{4}\right)^2 (1) = -\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$, which is option $4$.

**Subtopic:** Acceleration in SHM · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q045_ce681ec2_04112026.png?v=ce681ec27369)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q045_8309620e_04112026.png?v=8309620efbfb)

---

## Q46

Physics · Magnetic Effect of Electric Current

A wire carrying a current $I$ along the positive $x$-axis has length $L$. It is kept in a magnetic field $\vec{B} = (2\hat{i} + 3\hat{j} - 4\hat{k})\,\mathrm{T}$. The magnitude of the magnetic force acting on the wire is

- (1) $3\,IL$
- (2) $\sqrt{5}\,IL$
- **(3)** $5\,IL$
- (4) $\sqrt{3}\,IL$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Magnetic force acting on a current carrying wire is
2. $\vec{F} = I\vec{\ell} \times \vec{B}$
3. $= IL\hat{i} \times \left(2\hat{i} + 3\hat{j} - 4\hat{k}\right) = 3IL\hat{k} + 4IL\hat{j}$
4. Magnitude of force
5. $\left|\vec{F}\right| = \sqrt{(3IL)^{2} + (4IL)^{2}}$
6. $= 5IL$

**Solved independently** (answer withheld)

1. The force on a straight current-carrying wire is $\vec{F} = I\vec{L} \times \vec{B}$ with $\vec{L} = L\hat{i}$.
2. $\hat{i} \times (2\hat{i} + 3\hat{j} - 4\hat{k}) = 0 + 3\hat{k} + 4\hat{j}$, so $\vec{F} = IL(4\hat{j} + 3\hat{k})$.
3. $|\vec{F}| = IL\sqrt{4^2 + 3^2} = 5\,IL$, which is option $3$.

**Subtopic:** Magnetic Force · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q046_1ac9c992_04112026.png?v=1ac9c992a6a2)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q046_59ade24d_04112026.png?v=59ade24dd1d4)

---

## Q47

Physics · Ray Optics

In the figure shown here, what is the equivalent focal length of the combination of lenses (Assume that all layers are thin)?

![printed figure: A biconvex lens (n1 = 1.5) immersed in a liquid slab (n2 = 1.6), R1 = R2 = 20 cm](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q047_5fb0b620_04112026.png?v=5fb0b620d17f)

*A biconvex lens (n1 = 1.5) immersed in a liquid slab (n2 = 1.6), R1 = R2 = 20 cm*

![drawn: A biconvex lens (n1 = 1.5) immersed in a liquid slab (n2 = 1.6), R1 = R2 = 20 cm](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q047_question_8f413856_14112026.svg?v=8f413856bf87)  
*drawn by code/lib/physics_figure.py*

- (1) $40\,\mathrm{cm}$
- (2) $-40\,\mathrm{cm}$
- **(3)** $-100\,\mathrm{cm}$
- (4) $-50\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Effective focal length $\Rightarrow f_{\mathrm{eff}}$
2. $\frac{1}{f_{\mathrm{eff}}} = \frac{1}{f_1} + \frac{1}{f_2} + \frac{1}{f_3}$
3. Also, $\frac{1}{f} = (\mu - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$
4. $\frac{1}{f_1} = (1.6 - 1)\left(\frac{1}{\infty} - \frac{1}{20}\right) = \frac{-0.6}{20}$
5. $\frac{1}{f_2} = (1.5 - 1)\left(\frac{1}{20} - \frac{1}{-20}\right) = \frac{0.5}{10}$
6. $\frac{1}{f_3} = (1.6 - 1)\left(\frac{1}{-20} - \frac{1}{\infty}\right) = \frac{-0.6}{20}$
7. $\frac{1}{f_{\mathrm{eff}}} = \frac{-0.6}{20} + \frac{0.5}{10} - \frac{0.6}{20}$
8. $\frac{1}{f_{\mathrm{eff}}} = \frac{-0.6}{10} + \frac{0.5}{10} = \frac{-0.1}{10} = \frac{-1}{100}$
9. $\therefore\ f_{\mathrm{eff}} = -100\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. The combination is three thin lenses in contact in air: a central biconvex lens ($n_1 = 1.5$) and two plano-concave layers ($n_2 = 1.6$) on either side, each concave face of radius $20\,\mathrm{cm}$.
2. Biconvex lens: $\frac{1}{f_1} = (1.5-1)\left(\frac{1}{20}+\frac{1}{20}\right) = \frac{0.5 \times 2}{20} = 0.05\,\mathrm{cm^{-1}}$.
3. Each plano-concave layer: $\frac{1}{f_2} = \frac{1}{f_3} = (1.6-1)\left(\frac{1}{\infty} - \frac{1}{20}\right) = -0.03\,\mathrm{cm^{-1}}$.
4. Lenses in contact: $\frac{1}{F} = \frac{1}{f_1}+\frac{1}{f_2}+\frac{1}{f_3} = 0.05 - 0.03 - 0.03 = -0.01\,\mathrm{cm^{-1}}$.
5. $F = -100\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Combination of Thin Lenses in Contact, Lens Maker Formula · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 20)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q047_df13bbe3_04112026.png?v=df13bbe30eb8)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q047_7ecaf60f_04112026.png?v=7ecaf60f0fd8)

---

## Q48

Physics · Kinematics

A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity $4\,\mathrm{m\,s^{-1}}$. The ball strikes the water surface after $4\,\mathrm{s}$. The height of bridge above water surface is (Take $g = 10\,\mathrm{m\,s^{-2}}$)

- (1) $56\,\mathrm{m}$
- (2) $60\,\mathrm{m}$
- **(3)** $64\,\mathrm{m}$
- (4) $68\,\mathrm{m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $s = ut - \frac{1}{2}gt^{2}$
2. $= 16 - \frac{1}{2} \times 10 \times 16$
3. $= -64\,\mathrm{m}$
4. Height of bridge above water surface $= 64\,\mathrm{m}$

**Solved independently** (answer withheld)

1. Take upward as positive: $u = +4\,\mathrm{m\,s^{-1}}$, $a = -g = -10\,\mathrm{m\,s^{-2}}$, $t = 4\,\mathrm{s}$.
2. $s = ut - \frac{1}{2}gt^2$.
3. $s = 4 \times 4 - \frac{1}{2} \times 10 \times 4^2 = 16 - 80 = -64\,\mathrm{m}$.
4. The ball ends $64\,\mathrm{m}$ below the launch point, so the bridge height is $64\,\mathrm{m}$, which is option $3$.

**Subtopic:** Freely Falling Bodies · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 20)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q048_10521440_04112026.png?v=105214409d1a)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q048_53cf0182_04112026.png?v=53cf01824ca5)

---

## Q49

Physics · Ray Optics

Two thin lenses are of same focal lengths ($f$), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be

- (1) Zero
- (2) $\frac{f}{4}$
- (3) $\frac{f}{2}$
- **(4)** Infinite

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Convex lens $f_1 > 0$, concave lens $f_2 < 0$
2. $\frac{1}{f_{\mathrm{eq}}} = \frac{1}{f_1} + \frac{1}{f_2} = \frac{1}{f} - \frac{1}{f} = 0$
3. $f_{\mathrm{eq}} = \infty$

**Solved independently** (answer withheld)

1. For thin lenses in contact, $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}$.
2. Convex lens $f_1 = +f$, concave lens $f_2 = -f$, so $\frac{1}{F} = \frac{1}{f} - \frac{1}{f} = 0$.
3. $\frac{1}{F} = 0 \Rightarrow F = \infty$, which is option $4$ (Infinite).

**Subtopic:** Combination of Thin Lenses in Contact · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 21)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q049_a65e1c12_04112026.png?v=a65e1c12391e)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q049_cf40981d_04112026.png?v=cf40981da378)

---

## Q50

Physics · Electrostatics

An electric dipole is placed as shown in the figure. The electric potential (in $10^{2}\,\mathrm{V}$) at point $P$ due to the dipole is ($\epsilon_0$ = permittivity of free space and $\frac{1}{4\pi\epsilon_0} = K$)

![printed figure: Electric dipole -q and +q, 3 cm either side of 0, with point P on the axis at 5 cm from 0](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q050_2e5bdb65_04112026.png?v=2e5bdb652747)

*Electric dipole -q and +q, 3 cm either side of 0, with point P on the axis at 5 cm from 0*

![drawn: Electric dipole -q and +q, 3 cm either side of 0, with point P on the axis at 5 cm from 0](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q050_question_4e1d6ea3_14112026.svg?v=4e1d6ea3d694)  
*drawn by code/lib/physics_figure.py*

- **(1)** $\left(\frac{3}{8}\right)qK$
- (2) $\left(\frac{5}{8}\right)qK$
- (3) $\left(\frac{8}{5}\right)qK$
- (4) $\left(\frac{8}{3}\right)qK$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Electrostatic potential due to a point charge is given by $\frac{Kq}{r}$
2. $V_{\text{net at point } P} = \frac{Kq}{2 \times 10^{-2}} - \frac{Kq}{8 \times 10^{-2}}$
3. $= \frac{Kq \times 10^{2}}{2}\left(1 - \frac{1}{4}\right)$
4. $= \left(\frac{3}{8}Kq\right) \times 10^{2}\,\mathrm{V} = \frac{3}{8}qK$

**Solved independently** (answer withheld)

1. From the figure, $P$ is $5\,\mathrm{cm}$ from the centre $O$ on the axis, on the side of $+q$.
2. Distance from $+q$: $r_+ = 5 - 3 = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$.
3. Distance from $-q$: $r_- = 5 + 3 = 8\,\mathrm{cm} = 0.08\,\mathrm{m}$.
4. $V = Kq\left(\frac{1}{0.02} - \frac{1}{0.08}\right) = Kq(50 - 12.5) = 37.5\,Kq$.
5. $37.5\,Kq = \frac{3}{8}qK \times 10^{2}\,\mathrm{V}$, which is option $1$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q050_7bedff7f_04112026.png?v=7bedff7f60da)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q050_fe0f9d82_04112026.png?v=fe0f9d82a13f)

---

## Q51

Chemistry · inorganic · Hydrogen

Which of the following statements are NOT correct? Choose the most appropriate answer from the options given below:

- (A) Hydrogen is used to reduce heavy metal oxides to metals.
- (B) Heavy water is used to study reaction mechanism.
- (C) Hydrogen is used to make saturated fats from oils.
- (D) The $\mathrm{H{-}H}$ bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements.
- (E) Hydrogen reduces oxides of metals that are more active than iron.

- (1) B, C, D, E only
- (2) B, D only
- **(3)** D, E only
- (4) A, B, C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Statement A, B, C are correct
2. (D) $\mathrm{H - H}$ bond dissociation energy is maximum as compared to single bond between two atom of any element.
3. (E) Hydrogen reduces oxides of metal that are less active than iron.

**Solved independently** (answer withheld)

1. A is correct: hydrogen reduces heavy metal oxides to metals.
2. B is correct: heavy water ($\mathrm{D_2O}$) is used to study reaction mechanisms.
3. C is correct: hydrogenation of vegetable oils with $\mathrm{H_2}$ gives saturated fats.
4. D is NOT correct: the $\mathrm{H-H}$ bond dissociation enthalpy ($435.88\,\mathrm{kJ\,mol^{-1}}$) is the highest for a single bond between two atoms of any element, not the lowest.
5. E is NOT correct: hydrogen reduces oxides of metals less active than iron, not more active.
6. The incorrect statements are D and E, which is option $3$.

**Subtopic:** Isotopes of Hydrogen and Properties of Dihydrogen · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q051_05e82d6f_04112026.png?v=05e82d6f9918)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q051_633c8f73_04112026.png?v=633c8f73ada9)

---

## Q52

Chemistry · organic · Haloalkanes and Haloarenes

The given compound [figure] is an example of ______.

![printed figure: C6H5-CH=CH-CH(X)-CH2CH3 (3-X-1-phenylpent-1-ene, a benzene ring bearing CH=CH-CH(X)-CH2-CH3)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q052_4a27c3a4_04112026.png?v=4a27c3a4a09b)

*C6H5-CH=CH-CH(X)-CH2CH3 (3-X-1-phenylpent-1-ene, a benzene ring bearing CH=CH-CH(X)-CH2-CH3)*

![drawn: C6H5-CH=CH-CH(X)-CH2CH3 (3-X-1-phenylpent-1-ene, a benzene ring bearing CH=CH-CH(X)-CH2-CH3)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q052_question_b0edb7c1_14112026.svg?v=b0edb7c10100)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: (3-halopent-1-en-1-yl)benzene `*C(C=Cc1ccccc1)CC` ![(3-halopent-1-en-1-yl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q052_question_s1_91226912_14112026.svg?v=912269120ef1)

- (1) Benzylic halide
- (2) Aryl halide
- **(3)** Allylic halide
- (4) Vinylic halide

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\alpha$-carbon is $sp^{3}$ carbon which is right next to $\mathrm{>C=C<}$
2. This $\alpha$-position is known as allylic position
3. Hence,
4. is allylic halide

**Solved independently** (answer withheld)

1. The structure is $\mathrm{C_6H_5{-}CH{=}CH{-}CH(X){-}CH_2CH_3}$.
2. The carbon bearing $X$ is $sp^3$ and is bonded directly to a $\mathrm{C{=}C}$ carbon, so it is an allylic position (not on the ring, not on the vinylic carbon, not next to the ring).
3. Hence the compound is an allylic halide, which is option $3$.

**Subtopic:** Classification, Nomenclature, and Physical Properties of Haloalkanes and Haloarenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q052_bb5add7d_04112026.png?v=bb5add7d5555)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q052_76fa1e69_04112026.png?v=76fa1e699378)

---

## Q53

Chemistry · inorganic · The p–Block Elements

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Coke | I | Carbon atoms are $\mathrm{sp^3}$ hybridised |
| B | Diamond | II | Used as a dry lubricant |
| C | Fullerene | III | Used as a reducing agent |
| D | Graphite | IV | Cage like molecules |

- (1) A-II, B-IV, C-I, D-III
- (2) A-IV, B-I, C-II, D-III
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Coke is largely used as a reducing agent in metallurgy.
2. In diamond, each carbon atom undergoes $\mathrm{sp^3}$ hybridisation and linked to four other carbon atoms by using hybridised orbitals in tetrahedral fashion.
3. Buckminsterfullerene contains six membered and five membered rings and hence is a cage like molecule.
4. Graphite is very soft and slippery. Hence, it is used as a dry lubricant in machines running at high temperature.

**Solved independently** (answer withheld)

1. Coke is used as a reducing agent in metallurgy, so $A \to III$.
2. In diamond each carbon is $\mathrm{sp^{3}}$ hybridised, tetrahedrally bonded, so $B \to I$.
3. Fullerenes such as $\mathrm{C_{60}}$ are cage-like molecules, so $C \to IV$.
4. Graphite's layers slide over each other, so it is used as a dry lubricant: $D \to II$.
5. $A$-III, $B$-I, $C$-IV, $D$-II matches option $3$.

**Subtopic:** Catenation & Allotropy Group 14 · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 23)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q053_7c81d2e3_04112026.png?v=7c81d2e34c5a)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q053_7d066658_04112026.png?v=7d066658ff47)

---

## Q54

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with $\mathrm{Fe^{3+}}$ due to the formation of

- (1) $\mathrm{Fe_4[Fe(CN)_6]_3\cdot xH_2O}$
- (2) $\mathrm{NaSCN}$
- (3) $\mathrm{[Fe(CN)_5NOS]^{4-}}$
- **(4)** $\mathrm{[Fe(SCN)]^{2+}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In case, nitrogen and sulphur both are present in organic compound, sodium thiocyanate is formed.
2. It gives blood red colour and no Prussian blue since there are no free cyanide ions.
3. $\mathrm{Na + C + N + S \longrightarrow NaSCN}$
4. $\mathrm{Fe^{3+} + SCN^{-} \longrightarrow \underset{Blood\ red}{[Fe(SCN)]^{2+}}}$

**Solved independently** (answer withheld)

1. When N and S are both present, sodium fusion gives $\mathrm{NaSCN}$; with $\mathrm{Fe^{3+}}$ this forms $\mathrm{[Fe(SCN)]^{2+}}$, which is blood red, so the answer is option $4$.

**Subtopic:** Detection of Elements · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q054_b5793e0a_04112026.png?v=b5793e0ac654)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q054_6827f917_04112026.png?v=6827f917c737)

---

## Q55

Chemistry · physical · Chemical Kinetics

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A reaction can have zero activation energy.
- (Reasons R) The minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value, is called activation energy.

- (1) Both A and R are true and R is the correct explanation of A
- **(2)** Both A and R are true and R is NOT the correct explanation of A
- (3) A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Few reactions can have zero activation energy for example radical reactions.
2. Activation energy is defined as the minimum amount of extra energy absorbed by reactants to achieve threshold energy.

**Solved independently** (answer withheld)

1. Activation energy is $E_a = E_{threshold} - E_{reactants}$; if reactant molecules already possess the threshold energy, $E_a = 0$, so A is true.
2. R states the standard definition of activation energy as the extra energy needed to reach the threshold value, so R is true.
3. The definition in R does not account for why $E_a$ can be zero, so R is not the correct explanation of A, which is option $2$.

**Subtopic:** Activation Energy · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 23)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q055_5ba8e971_04112026.png?v=5ba8e971cbdc)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q055_63ebb71c_04112026.png?v=63ebb71c431a)

---

## Q56

Chemistry · organic · Alcohols, Phenols and Ethers

Consider the following reaction and identify the product (P). $\mathrm{CH_3-CH(CH_3)-CH(OH)-CH_3} \xrightarrow{\mathrm{HBr}}$ Product (P) [3-Methylbutan-2-ol]

![printed figure: 3-Methylbutan-2-ol →(HBr) P](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q056_4fd1c1cc_04112026.png?v=4fd1c1cce7ff)

*3-Methylbutan-2-ol →[HBr] P*

![drawn: 3-Methylbutan-2-ol →(HBr) P](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q056_question_958aaa11_14112026.svg?v=958aaa1168c6)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 3-methylbutan-2-ol `CC(C)C(C)O` ![3-methylbutan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q056_question_s1_ca11da3c_14112026.svg?v=ca11da3c56c5)

- **(1)** 2-bromo-2-methylbutane `CCC(C)(C)Br` ![2-bromo-2-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q056_option_1_s1_c5380da6_14112026.svg?v=c5380da663c8) — $\mathrm{CH_3-C(Br)(CH_3)-CH_2-CH_3}$
- (2) $\mathrm{CH3CH = CH - CH3}$
- (3) 2-bromo-3-methylbutane `CC(C)C(C)Br` ![2-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q056_option_3_s1_18faa9fe_14112026.svg?v=18faa9fe6ac0) — $\mathrm{CH_3-CH(CH_3)-CH(Br)-CH_3}$
- (4) 1-bromo-2,2-dimethylpropane `CC(C)(C)CBr` ![1-bromo-2,2-dimethylpropane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q056_option_4_s1_7ca1318b_14112026.svg?v=7ca1318b3106) — $\mathrm{CH_3-C(CH_3)_2-CH_2Br}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Protonation of the $-OH$ by $\mathrm{HBr}$ gives $\mathrm{(CH_3)_2CH-CH(OH_2^+)-CH_3}$.
2. Loss of $\mathrm{H_2O}$ gives the secondary carbocation $\mathrm{(CH_3)_2CH-\overset{+}{C}H-CH_3}$.
3. A 1,2-hydride shift converts it to the more stable tertiary carbocation $\mathrm{(CH_3)_2\overset{+}{C}-CH_2-CH_3}$.
4. $\mathrm{Br^-}$ attacks the tertiary carbocation giving $\mathrm{CH_3-C(Br)(CH_3)-CH_2-CH_3}$ (2-bromo-2-methylbutane), which is option $1$.

**Subtopic:** Reactions of Alcohols · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 24)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q056_f64bc5db_04112026.png?v=f64bc5dbf492)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q056_177ec9a7_04112026.png?v=177ec9a7059b)

---

## Q57

Chemistry · inorganic · The p–Block Elements

Taking stability as the factor, which one of the following represents correct relationship?

- (1) $\mathrm{T\ell Cl_3} > \mathrm{T\ell Cl}$
- (2) $\mathrm{InI_3} > \mathrm{InI}$
- (3) $\mathrm{AlCl} > \mathrm{AlCl_3}$
- **(4)** $\mathrm{T\ell I} > \mathrm{T\ell I_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. As we move down the group, due to poor shielding effect of intervening $d$ and $f$ orbitals, the increased effective nuclear charge holds $ns$ electrons tightly and therefore restricting their participation in bonding.
2. So, the relative stability of $+1$ O.S increases for heavier elements.
3. $E^\circ$ for $\mathrm{In^{3+}}|\mathrm{In^{+}} = -0.16\,\mathrm{V}$
4. $E^\circ$ for $\mathrm{T\ell^{3+}}|\mathrm{T\ell^{+}} = +1.6\,\mathrm{V}$
5. Hence, $\mathrm{T\ell I}$ is more stable than $\mathrm{T\ell I_3}$

**Solved independently** (answer withheld)

1. Down group 13 the $ns^2$ pair becomes reluctant to bond (inert pair effect), so the $+1$ state grows more stable relative to $+3$.
2. For Al, $+3$ is the stable state, so $\mathrm{AlCl_3} > \mathrm{AlCl}$ and option $3$ is wrong.
3. For Tl, $+1$ is the stable state, so $\mathrm{T\ell Cl} > \mathrm{T\ell Cl_3}$ and option $1$ is wrong.
4. Likewise $\mathrm{T\ell I} > \mathrm{T\ell I_3}$ (Tl$^{3+}$ is also strongly oxidising towards I$^-$), so option $4$ is correct.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q057_7061edf7_04112026.png?v=7061edf7e414)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q057_da47a001_04112026.png?v=da47a0016bab)

---

## Q58

Chemistry · physical · Structure of Atom

The relation between $n_m$, ($n_m$ = the number of permissible values of magnetic quantum number ($m$)) for a given value of azimuthal quantum number ($l$), is

- **(1)** $l = \frac{n_m - 1}{2}$
- (2) $l = 2n_m + 1$
- (3) $n_m = 2l^2 + 1$
- (4) $n_m = l + 2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Values of $n_m$(magnetic quantum number) for given azimuthal quantum number can be calculated as following
2. $n_m = 2l + 1$
3. $l = \frac{n_m - 1}{2}$

**Solved independently** (answer withheld)

1. For a given $l$, $m$ takes the values $-l, \ldots, 0, \ldots, +l$.
2. So $n_m = 2l + 1$.
3. Rearranging, $l = \frac{n_m - 1}{2}$, which is option $1$.

**Subtopic:** Quantum Numbers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q058_75f28b2a_04112026.png?v=75f28b2af3b7)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q058_8fd06972_04112026.png?v=8fd069725f0e)

---

## Q59

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Complete the following reaction
[A] $\xrightarrow{\mathrm{HCN}}$ [B] $\xrightarrow[\Delta]{\text{conc. }\mathrm{H_2SO_4}}$ [C]
[C] is ________

![printed figure: (A) cyclohexanone →(HCN) (B) 1-hydroxycyclohexane-1-carbonitrile →(conc. $\ce{H2SO4}$, Δ) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q059_063ba955_04112026.png?v=063ba9552bdb)

*[A] cyclohexanone →[HCN] [B] 1-hydroxycyclohexane-1-carbonitrile →[conc. $\ce{H2SO4}$, Δ] [C]*

![drawn: (A) cyclohexanone →(HCN) (B) 1-hydroxycyclohexane-1-carbonitrile →(conc. $\ce{H2SO4}$, Δ) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_question_7580a08a_14112026.svg?v=7580a08abe1d)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_question_s1_ecae2398_14112026.svg?v=ecae2398c700); 1-hydroxycyclohexane-1-carbonitrile `N#CC1(O)CCCCC1` ![1-hydroxycyclohexane-1-carbonitrile](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_question_s2_e264e18d_14112026.svg?v=e264e18da5d0)

- (1) cyclohexanol `OC1CCCCC1` ![cyclohexanol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_option_1_s1_b130dcca_14112026.svg?v=b130dccaeb49)
- (2) cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_option_2_s1_5fc26872_14112026.svg?v=5fc268722cd9)
- (3) cyclohex-1-ene-1-carbaldehyde `O=CC1=CCCCC1` ![cyclohex-1-ene-1-carbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_option_3_s1_47f14bf7_14112026.svg?v=47f14bf77a4c)
- **(4)** cyclohex-1-ene-1-carboxylic acid `O=C(O)C1=CCCCC1` ![cyclohex-1-ene-1-carboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q059_option_4_s1_9e69062a_14112026.svg?v=9e69062a7631)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $[A]$ is cyclohexanone; HCN adds across $\mathrm{C=O}$ to give the cyanohydrin $[B]$, 1-hydroxycyclohexane-1-carbonitrile.
2. Hot concentrated $\mathrm{H_2SO_4}$ (aqueous acid) hydrolyses $-\mathrm{C\equiv N}$ to $-\mathrm{COOH}$.
3. The same hot conc. $\mathrm{H_2SO_4}$ dehydrates the tertiary $-\mathrm{OH}$, forming a ring $\mathrm{C=C}$ conjugated with $-\mathrm{COOH}$.
4. $[C]$ is cyclohex-1-ene-1-carboxylic acid, the ring with a double bond bearing $-\mathrm{COOH}$, which is option $4$.

**Subtopic:** Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q059_3359a8dc_04112026.png?v=3359a8dc2f25)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q059_5602d930_04112026.png?v=5602d93059e9)

---

## Q60

Chemistry · physical · Basic Concepts of Chemistry

The right option for the mass of $\mathrm{CO_2}$ produced by heating $20\,\mathrm{g}$ of $20\%$ pure limestone is (Atomic mass of Ca = $40$) $\left[\mathrm{CaCO_3} \xrightarrow{1200\,\mathrm{K}} \mathrm{CaO} + \mathrm{CO_2}\right]$

- (1) $1.12\,\mathrm{g}$
- **(2)** $1.76\,\mathrm{g}$
- (3) $2.64\,\mathrm{g}$
- (4) $1.32\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CaCO_3} \xrightarrow{1200\,\mathrm{K}} \mathrm{CaO} + \mathrm{CO_2}$
2. From $100\,\mathrm{g}$ $\mathrm{CaCO_3} \rightarrow 44\,\mathrm{g}$ $\mathrm{CO_2}$ produced
3. As $\mathrm{CaCO_3}$ is $20\%$ pure
4. So, mass of pure $\mathrm{CaCO_3} = 20 \times \frac{20}{100} = 4\,\mathrm{g}$
5. So, $100\,\mathrm{g}$ $\mathrm{CaCO_3} \rightarrow 44\,\mathrm{g}$ $\mathrm{CO_2}$
6. $4\,\mathrm{g}$ $\mathrm{CaCO_3} \rightarrow \frac{44}{100} \times 4\,\mathrm{g}$ $\mathrm{CO_2}$
7. $= 1.76\,\mathrm{g}$ $\mathrm{CO_2}$

**Solved independently** (answer withheld)

1. Mass of pure $\mathrm{CaCO_3} = 0.20 \times 20\,\mathrm{g} = 4\,\mathrm{g}$.
2. Molar mass of $\mathrm{CaCO_3} = 40 + 12 + 3(16) = 100\,\mathrm{g\,mol^{-1}}$.
3. $n(\mathrm{CaCO_3}) = \frac{4}{100} = 0.04\,\mathrm{mol}$.
4. From $\mathrm{CaCO_3} \rightarrow \mathrm{CaO} + \mathrm{CO_2}$ (1:1), $n(\mathrm{CO_2}) = 0.04\,\mathrm{mol}$.
5. $m(\mathrm{CO_2}) = 0.04 \times 44 = 1.76\,\mathrm{g}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q060_1f0cbcdd_04112026.png?v=1f0cbcdd0831)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q060_1490c4e0_04112026.png?v=1490c4e00de3)

---

## Q61

Chemistry · physical · Electrochemistry

> ⚠ The independent solve chose (1); the booklet prints (2).

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R
In the light of the above statements, choose the correct answer from the options given below

- (A) In equation $\Delta_r G = -nFE_{\mathrm{cell}}$, value of $\Delta_r G$ depends on n.
- (R) $E_{cell}$ is an intensive property and $\Delta_r G$ is an extensive property.

- (1) Both A and R are true and R is the correct explanation of A
- **(2)** Both A and R are true and R is NOT the correct explanation of A
- (3) A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (2) · independent solve: (1) · differs

**Publisher's solution**

1. The value of $\Delta_r G$ depends on $n$ value as per the equation $\Delta_r G = -nFE_{\mathrm{cell}}$
2. Where $E$ is the emf of the cell and $nF$ is the amount of charge passed.
3. So, assertion statement is correct
4. $E_{\mathrm{cell}}$ is an intensive property while $\Delta_r G$ is an extensive thermodynamic property
5. So, reason is correct but not explaining the assertion

**Solved independently** (answer withheld)

1. In $\Delta_r G = -nFE_{cell}$, $F$ is a constant and $E_{cell}$ is an intensive property, so it does not change with the amount of reaction.
2. $\Delta_r G$ is an extensive property: doubling the reaction doubles $n$ and so doubles $\Delta_r G$, so $\Delta_r G$ depends on $n$ and A is true.
3. R is true, and because $E_{cell}$ is intensive while $\Delta_r G$ is extensive, the factor $n$ is what carries the extensive dependence. So R explains A, which is option $1$.

**Subtopic:** Nernst Equation · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 26)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q061_0f561c8c_04112026.png?v=0f561c8c8c36)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q061_23deae3b_04112026.png?v=23deae3b77e2)

---

## Q62

Chemistry · physical · Ionic Equilibrium

Amongst the given options which of the following molecules/ ion acts as a Lewis acid?

- (1) $\mathrm{NH_3}$
- (2) $\mathrm{H_2O}$
- **(3)** $\mathrm{BF_3}$
- (4) $\mathrm{OH^-}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Lewis acids are the one which accepts lone pair of electron due to presence of vacant orbital in outermost shell.

**Solved independently** (answer withheld)

1. A Lewis acid is an electron-pair acceptor.
2. In $\mathrm{BF_3}$, boron has only $6$ valence electrons (incomplete octet), so it can accept a lone pair: Lewis acid.
3. $\mathrm{H_2O}$, $\mathrm{OH^-}$ and $\mathrm{NH_3}$ all carry lone pairs and donate them: Lewis bases.
4. Hence the answer is $\mathrm{BF_3}$, option $3$.

**Subtopic:** Lewis Acids and Bases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q062_970a4245_04112026.png?v=970a4245d379)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q062_bf8c4ce2_04112026.png?v=bf8c4ce241c5)

---

## Q63

Chemistry · inorganic · Coordination Compounds – Practice

Homoleptic complex from the following complexes is

- **(1)** Potassium trioxalatoaluminate (III)
- (2) Diamminechloridonitrito-N-platinum (II)
- (3) Pentaamminecarbonatocobalt (III) chloride
- (4) Triamminetriaquachromium (III) chloride

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Complexes in which a metal is bound to only one kind of donor groups are called as homoleptic complexes
2. Potassium trioxalatoaluminate $(\mathrm{III})$
3. $\mathrm{K_3[Al(ox)_3]}$
4. It is a homoleptic complex

**Solved independently** (answer withheld)

1. A homoleptic complex has the metal bound to only one kind of ligand.
2. Option 2 is $[\mathrm{Pt(NH_3)_2Cl(NO_2)}]$ with $\mathrm{NH_3}$, $\mathrm{Cl^-}$ and $\mathrm{NO_2^-}$: heteroleptic.
3. Option 3 is $[\mathrm{Co(NH_3)_5(CO_3)}]\mathrm{Cl}$ with $\mathrm{NH_3}$ and $\mathrm{CO_3^{2-}}$: heteroleptic.
4. Option 4 is $[\mathrm{Cr(NH_3)_3(H_2O)_3}]\mathrm{Cl_3}$ with $\mathrm{NH_3}$ and $\mathrm{H_2O}$: heteroleptic.
5. Option 1 is $\mathrm{K_3[Al(C_2O_4)_3]}$ with only $\mathrm{C_2O_4^{2-}}$ ligands: homoleptic, so the answer is option $1$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 27)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q063_16c8b15f_04112026.png?v=16c8b15ffcdc)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q063_056067e7_04112026.png?v=056067e75acb)

---

## Q64

Chemistry · organic · General Organic Chemistry

The number of $\sigma$ bonds, $\pi$ bonds and lone pair of electrons in pyridine, respectively are:

- (1) 11, 2, 0
- (2) 12, 3, 0
- **(3)** 11, 3, 1
- (4) 12, 2, 1

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. No. of $\sigma$ bonds $= 11$
2. No. of $\pi$ bonds $= 3$
3. No. of lone pair of $e^{-} = 1$

**Solved independently** (answer withheld)

1. Pyridine is $\mathrm{C_5H_5N}$: a six-membered aromatic ring with one N and five C–H units.
2. Ring $\sigma$ bonds: $6$; C–H $\sigma$ bonds: $5$; total $\sigma = 6 + 5 = 11$.
3. The aromatic ring has $3$ alternating double bonds, so $\pi = 3$.
4. The $sp^2$ N carries $1$ lone pair (in the ring plane, not part of the aromatic sextet).
5. $(11, 3, 1)$ is option $3$.

**Subtopic:** Aromaticity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q064_48328899_04112026.png?v=48328899b5ea)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q064_5636a586_04112026.png?v=5636a5865109)

---

## Q65

Chemistry · physical · States of Matter

Intermolecular forces are forces of attraction and repulsion between interacting particles that will include : Choose the most appropriate answer from the options given below :

- (A) dipole - dipole forces
- (B) dipole - induced dipole forces
- (C) hydrogen bonding
- (D) covalent bonding
- (E) dispersion forces

- (1) B, C, D, E are correct
- (2) A, B, C, D are correct
- **(3)** A, B, C, E are correct
- (4) A, C, D, E are correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Intermolecular forces are the forces of attraction and repulsion between interacting molecules.
2. This term does not include covalent bonds as covalent bond holds atoms of a molecule together.
3. Hence, dipole - dipole forces, dipole - induced dipole forces, hydrogen bonding and dispersion forces are intermolecular forces.

**Solved independently** (answer withheld)

1. Dipole-dipole, dipole-induced dipole, hydrogen bonding and dispersion (London) forces act between molecules, so A, B, C and E are intermolecular forces.
2. Covalent bonding (D) holds atoms together within a molecule, so it is intramolecular and is excluded.
3. The correct set is A, B, C, E, which is option $3$.

**Subtopic:** Intermolecular Forces · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 28)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q065_60601862_04112026.png?v=60601862b340)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q065_89774550_04112026.png?v=89774550351a)

---

## Q66

Chemistry · physical · Structure of Atom

Select the correct statements from the following
Choose the correct answer from the options given below

- (A) Atoms of all elements are composed of two fundamental particles.
- (B) The mass of the electron is $9.10939 \times 10^{-31}\,\mathrm{kg}$.
- (C) All the isotopes of a given element show same chemical properties:
- (D) Protons and electrons are collectively known as nucleons.
- (E) Dalton’s atomic theory, regarded the atom as an ultimate particles of matter

- (1) A, B and C only
- (2) C, D and E only
- (3) A and E only
- **(4)** B, C and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Atoms consist of three fundamental particles : Electrons, protons and neutrons
2. The mass of the electron is $9.10939 \times 10^{-31}\,\mathrm{kg}$
3. All the isotopes of a given element show same chemical properties.
4. Protons and neutrons present in the nucleus are collectively called as nucleons.
5. Dalton’s atomic theory, regarded the atom as the ultimate particle of matter
6. So, the correct statements are B, C, E only

**Solved independently** (answer withheld)

1. A is false: atoms are made of three fundamental particles (electron, proton, neutron), not two.
2. B is true: $m_e = 9.10939 \times 10^{-31}\,\mathrm{kg}$.
3. C is true: isotopes have the same atomic number and electronic configuration, so they show the same chemical properties.
4. D is false: nucleons are protons and neutrons, not protons and electrons.
5. E is true: Dalton's atomic theory regarded the atom as the ultimate, indivisible particle of matter.
6. The correct statements are B, C and E, which is option $4$.

**Subtopic:** Discovery of Sub-Atomic Particles, Isobars and Isotopes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q066_f3654aa8_04112026.png?v=f3654aa84b79)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q066_98591a12_04112026.png?v=98591a1245de)

---

## Q67

Chemistry · organic · Chemistry in Everyday Life

Some tranquilizers are listed below. Which one from the following belongs to barbiturates?

- (1) Chlordiazepoxide
- (2) Meprobamate
- (3) Valium
- **(4)** Veronal

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Veronal is the derivative of Barbituric acid and considered as barbiturate.
2. Meprobamate, valium and chlordiazepoxide are other tranquilizers.

**Solved independently** (answer withheld)

1. Barbiturates are derivatives of barbituric acid; NCERT lists veronal, amytal, nembutal, luminal and seconal as barbiturate tranquilizers, so Veronal (option $4$) is the barbiturate while meprobamate, Valium and chlordiazepoxide are non-barbiturate tranquilizers.

**Subtopic:** Tranquilizers · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q067_cc72dd24_04112026.png?v=cc72dd2445d9)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q067_04b86201_04112026.png?v=04b86201aa05)

---

## Q68

Chemistry · inorganic · The p–Block Elements

> ⚠ The booklet keys (2) "Both A and R are true and R is NOT the correct explanation of A", but Reason R says helium has HIGH solubility in O2, and the publisher's own printed solution (2023_E5 q068) says helium is used "because of its very low solubility in blood", which makes R false. By the publisher's own reasoning the answer is "A is true but R is false". The printed key is kept as printed. Same question as 2023_F1 q064.

> ⚠ The independent solve chose (3); the booklet prints (2).

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R
In the light of the above statements, choose the correct answer from the options given below

- (Assertion A) Helium is used to dilute oxygen in diving apparatus.
- (Reason R) Helium has high solubility in $\mathrm{O_2}$.

- (1) Both A and R are true and R is the correct explanation of A
- **(2)** Both A and R are true and R is NOT the correct explanation of A
- (3) A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (2) · independent solve: (3) · differs

**Publisher's solution**

1. Helium is used as diluent for oxygen in modern diving apparatus because of its very low solubility in blood.
2. Gases diffuses easily with each other.

**Solved independently** (answer withheld)

1. Assertion A is true: helium is mixed with oxygen in diving apparatus to dilute it.
2. It is used because helium has very low solubility in blood, unlike $\mathrm{N_2}$, so it does not cause bends; Reason R ('high solubility in $\mathrm{O_2}$') is false, so the answer is option $3$.

**Subtopic:** Applications & Special Features of Group 18 · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q068_1c560950_04112026.png?v=1c5609500c4f)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q068_9db228ca_04112026.png?v=9db228cab5ff)

---

## Q69

Chemistry · inorganic · The s-Block Elements

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Metallic sodium dissolves in liquid ammonia giving a deep blue solution, which is paramagnetic.
- (Reason R) The deep blue solution is due to the formation of amide.

- (1) Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- **(3)** A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. On dissolving alkali metal (sodium) in liquid ammonia, a deep blue solution is developed due to ammoniated electron which absorbs energy in visible region of light and imparts blue colour.
2. Due to unpaired electron, solution is paramagnetic.
3. $\mathrm{M} + (x + y)\mathrm{NH_3} \rightarrow [\mathrm{M(NH_3)}_{x}]^{+} + [\mathrm{e(NH_3)}y]^{-}$
4. So, assertion statement is correct but reason is incorrect.

**Solved independently** (answer withheld)

1. Sodium dissolves in liquid ammonia: $\mathrm{Na} + (x+y)\mathrm{NH_3} \rightarrow [\mathrm{Na(NH_3)_x}]^+ + [e(\mathrm{NH_3})_y]^-$.
2. The deep blue colour and paramagnetism come from the unpaired ammoniated electron $[e(\mathrm{NH_3})_y]^-$, so Assertion A is true.
3. Amide $\mathrm{NaNH_2}$ forms only on standing ($\mathrm{Na^+} + e^- + \mathrm{NH_3} \rightarrow \mathrm{NaNH_2} + \tfrac{1}{2}\mathrm{H_2}$) and the blue colour is not due to it, so Reason R is false.
4. A true, R false, which is option $3$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q069_739e3cc0_04112026.png?v=739e3cc0e147)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q069_c2b47910_04112026.png?v=c2b47910df91)

---

## Q70

Chemistry · organic · Hydrocarbons

Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is :

- (1) $16$
- **(2)** $32$
- (3) $30$
- (4) $18$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. This reaction is called soda lime decarboxylation
2. Molar mass of $\mathrm{CH_4} = 16\,\mathrm{g/mol}$
3. Weight of $2$ moles of $\mathrm{CH_4} = 16 \times 2 = 32\,\mathrm{g}$

**Solved independently** (answer withheld)

1. Heating sodium ethanoate with NaOH and CaO (soda lime) is decarboxylation: $\mathrm{CH_3COONa + NaOH \xrightarrow{CaO,\,\Delta} CH_4 + Na_2CO_3}$.
2. Molar mass of $\mathrm{CH_4} = 12 + 4(1) = 16\,\mathrm{g\,mol^{-1}}$.
3. Mass of 2 mol $= 2 \times 16 = 32\,\mathrm{g}$, which is option $2$.

**Subtopic:** Preparation of Alkane · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q070_f28032c8_04112026.png?v=f28032c880d4)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q070_7283da39_04112026.png?v=7283da39a991)

---

## Q71

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The correct order of energies of molecular orbitals of $\mathrm{N_2}$ molecule, is

- **(1)** $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$
- (2) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$
- (3) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < \sigma^{*}2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y)$
- (4) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma 2p_z < \sigma^{*}2p_z$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For molecules like $\mathrm{B_2}$, $\mathrm{C_2}$, $\mathrm{N_2}$ etc. the increasing order of energies of various molecular orbitals is
2. $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$

**Solved independently** (answer withheld)

1. For molecules up to $\mathrm{N_2}$ (total electrons $\le 14$), $2s$-$2p$ mixing raises the energy of $\sigma 2p_z$ above the degenerate $\pi 2p_x = \pi 2p_y$ pair.
2. So the order is $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$, which is option $1$.

**Subtopic:** Energy Level Diagram for Molecular Orbitals · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q071_2e52fdc6_04112026.png?v=2e52fdc67540)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q071_b90cfc6b_04112026.png?v=b90cfc6bfaaa)

---

## Q72

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Amongst the following, the total number of species NOT having eight electrons around central atom in its outermost shell, is $\mathrm{NH_3}$, $\mathrm{AlCl_3}$, $\mathrm{BeCl_2}$, $\mathrm{CCl_4}$, $\mathrm{PCl_5}$ :

- **(1)** $3$
- (2) $2$
- (3) $4$
- (4) $1$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\rightarrow 8\,e^{-}$ in nitrogen
2. $\rightarrow 6\,e^{-}$ in $\mathrm{Al}$
3. $\mathrm{Cl-Be-Cl} \rightarrow 4\,e^{-}$ in $\mathrm{Be}$
4. $\rightarrow 8\,e^{-}$ in '$\mathrm{C}$'
5. $\rightarrow 10\,e^{-}$ in '$\mathrm{P}$'

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: N has 3 bond pairs + 1 lone pair $= 8$ electrons (octet).
2. $\mathrm{AlCl_3}$: Al has 3 bond pairs $= 6$ electrons (incomplete octet).
3. $\mathrm{BeCl_2}$: Be has 2 bond pairs $= 4$ electrons (incomplete octet).
4. $\mathrm{CCl_4}$: C has 4 bond pairs $= 8$ electrons (octet).
5. $\mathrm{PCl_5}$: P has 5 bond pairs $= 10$ electrons (expanded octet).
6. Species not having 8 electrons: $\mathrm{AlCl_3}, \mathrm{BeCl_2}, \mathrm{PCl_5}$ $= 3$, which is option $1$.

**Subtopic:** Octet Rule · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q072_19375ddf_04112026.png?v=19375ddf4a27)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q072_de0fccea_04112026.png?v=de0fcceadc30)

---

## Q73

Chemistry · physical · Surface Chemistry

Which one is an example of heterogenous catalysis?

- (1) Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen
- (2) Hydrolysis of sugar catalysed by $\mathrm{H^+}$ ions
- (3) Decomposition of ozone in presence of nitrogen monoxide
- **(4)** Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Combination of $\mathrm{N_2}$ and $\mathrm{H_2}$ to form $\mathrm{NH_3}$ in presence of finely divided $\mathrm{Fe}$ is an example of heterogeneous catalysis.
2. $\mathrm{N_2(g) + 3H_2(g) \xrightarrow{Fe(s)} 2NH_3(g)}$
3. All other are examples of homogeneous catalysis.
4. $\mathrm{C_{12}H_{22}O_{11}(aq) + H_2O(l) \xrightarrow{H_2SO_4(l)} Glucose(aq) + Fructose(aq)}$
5. $\mathrm{2SO_2(g) + O_2(g) \xrightarrow{NO(g)} 2SO_3(g)}$

**Solved independently** (answer withheld)

1. Heterogeneous catalysis means the catalyst is in a different phase from the reactants.
2. Option 2: sugar solution and $\mathrm{H^{+}}$ ions are both in the aqueous phase, so homogeneous.
3. Option 3: $\mathrm{O_3(g)}$ with $\mathrm{NO(g)}$ are both gases, so homogeneous.
4. Option 1: $\mathrm{2SO_2(g) + O_2(g) \xrightarrow{NO(g)} 2SO_3(g)}$ is all gas phase, so homogeneous (lead chamber process).
5. Option 4: $\mathrm{N_2(g) + 3H_2(g) \xrightarrow{Fe(s)} 2NH_3(g)}$ has a solid catalyst with gaseous reactants, so heterogeneous, which is option $4$.

**Subtopic:** Homogeneous and Heterogeneous Catalysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q073_154be24c_04112026.png?v=154be24cfca0)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q073_77443ea2_04112026.png?v=77443ea276f3)

---

## Q74

Chemistry · inorganic · The s-Block Elements

Which one of the following statements is correct?

- **(1)** The daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ in the human body is estimated to be $0.2\text{-}0.3\,\mathrm{g}$
- (2) All enzymes that utilise ATP in phosphate transfer require $\mathrm{Ca}$ as the cofactor
- (3) The bone in human body is an inert and unchanging substance
- (4) $\mathrm{Mg}$ plays roles in neuromuscular function and interneuronal transmission

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. All enzymes that utilize $\mathrm{ATP}$ in phosphate transfer require $\mathrm{Mg}$ as the co-factor.
2. Bone in human body is not an inert and unchanging substance but is continuously being solubilised and redeposited.
3. $\mathrm{Ca}$ plays important role in neuromuscular function, interneuronal transmission, cell membrane integrity and blood coagulation.
4. The daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ in the human body is estimated to be $200 - 300\,\mathrm{mg}$ $(0.2 - 0.3\,\mathrm{g})$.

**Solved independently** (answer withheld)

1. Option $2$: enzymes that use ATP in phosphate transfer need $\mathrm{Mg}$ as cofactor, not $\mathrm{Ca}$, so it is false.
2. Option $3$: bone is not inert; it is constantly being solubilised and redeposited, so it is false.
3. Option $4$: the role in neuromuscular function and interneuronal transmission is that of $\mathrm{Ca}$, not $\mathrm{Mg}$, so it is false.
4. Option $1$: the daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ is $200\text{-}300\,\mathrm{mg} = 0.2\text{-}0.3\,\mathrm{g}$, so it is correct, which is option $1$.

**Subtopic:** Biological Importance of Sodium, Potassium, Magnesium and Calcium · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 31)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q074_f7654bb1_04112026.png?v=f7654bb1ba47)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q074_3c531400_04112026.png?v=3c53140040ea)

---

## Q75

Chemistry · physical · States of Matter

Which amongst the following options are correct graphical representation of Boyle’s law?

- (1) ![printed figure: graph of P (y-axis) against V (x-axis): three hyperbolic isotherms labelled T1 (top), T2, T3 (bottom), with T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q075_option_1_7876951e_04112026.png?v=7876951eb855) *graph of P (y-axis) against V (x-axis): three hyperbolic isotherms labelled T1 (top), T2, T3 (bottom), with T3 > T2 > T1*
- **(2)** ![printed figure: graph of P (y-axis) against 1/V (x-axis): three straight lines through the origin labelled T3 (steepest), T2, T1 (least steep), with T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q075_option_2_9697cfef_04112026.png?v=9697cfef0ecd) *graph of P (y-axis) against 1/V (x-axis): three straight lines through the origin labelled T3 (steepest), T2, T1 (least steep), with T3 > T2 > T1*
- (3) ![printed figure: graph of P (y-axis) against 1/V (x-axis): three hyperbolic curves labelled T3 (top), T2, T1 (bottom), with T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q075_option_3_16bb3ae9_04112026.png?v=16bb3ae90ea5) *graph of P (y-axis) against 1/V (x-axis): three hyperbolic curves labelled T3 (top), T2, T1 (bottom), with T3 > T2 > T1*
- (4) ![printed figure: graph of P (y-axis) against T (x-axis): three straight lines through the origin labelled V1 (steepest), V2, V3 (least steep), with V1 < V2 < V3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q075_option_4_d0e94f3a_04112026.png?v=d0e94f3a289d) *graph of P (y-axis) against T (x-axis): three straight lines through the origin labelled V1 (steepest), V2, V3 (least steep), with V1 < V2 < V3*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to Boyle’s law,
2. $PV = nRT$
3. $P = nRT\left(\frac{1}{V}\right)$
4. $P$ versus $\left(\frac{1}{V}\right)$ gives straight line graph with slope $nRT$.

**Solved independently** (answer withheld)

1. Boyle's law at constant $T$: $PV = nRT$, so $P = nRT\cdot\frac{1}{V}$.
2. A plot of $P$ against $\frac{1}{V}$ is a straight line through the origin with slope $nRT$.
3. Since $T_3 > T_2 > T_1$, slope$(T_3)$ > slope$(T_2)$ > slope$(T_1)$, so $T_3$ is the steepest line, as drawn in option $2$.
4. Option $1$: on a $P$–$V$ plot, a higher-$T$ isotherm lies farther from the origin, so the labels are reversed; incorrect.
5. Option $3$: $P$ vs $\frac{1}{V}$ should be linear, not hyperbolic; incorrect.
6. Option $4$ is $P$ vs $T$ at constant $V$ (Gay-Lussac's law), not a Boyle's law plot, so the answer is option $2$.

**Subtopic:** Gas Laws · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 31)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q075_74f1193f_04112026.png?v=74f1193fd39c)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q075_86f9d40c_04112026.png?v=86f9d40ccb20)

---

## Q76

Chemistry · organic · Amines

Identify the product in the following reaction:

![printed figure: benzenediazonium chloride →((i) $\ce{Cu2Br2/HBr}$ (ii) Mg/dry ether (iii) $\ce{H2O}$) Product](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q076_4227cf0f_04112026.png?v=4227cf0fb8a4)

*benzenediazonium chloride →[(i) $\ce{Cu2Br2/HBr}$ (ii) Mg/dry ether (iii) $\ce{H2O}$] Product*

![drawn: benzenediazonium chloride →((i) $\ce{Cu2Br2/HBr}$ (ii) Mg/dry ether (iii) $\ce{H2O}$) Product](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_question_1dabe2c4_14112026.svg?v=1dabe2c43a8b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzenediazonium chloride `N#[N+]c1ccccc1.[Cl-]` ![benzenediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_question_s1_746dd923_14112026.svg?v=746dd923bd81)

- (1) phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_option_1_s1_b51d9a3a_14112026.svg?v=b51d9a3a6eec)
- **(2)** benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_option_2_s1_dbf27a87_14112026.svg?v=dbf27a872e50)
- (3) phenylmagnesium bromide `[Br][Mg][c]1ccccc1` ![phenylmagnesium bromide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_option_3_s1_c9815f06_14112026.svg?v=c9815f069863)
- (4) 4-bromophenol `Oc1ccc(Br)cc1` ![4-bromophenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q076_option_4_s1_fbd34b5b_14112026.svg?v=fbd34b5b0836)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Sandmeyer reaction: $\mathrm{C_6H_5N_2^+Cl^-} \xrightarrow{\mathrm{Cu_2Br_2/HBr}} \mathrm{C_6H_5Br} + \mathrm{N_2}$.
2. Grignard formation: $\mathrm{C_6H_5Br} \xrightarrow{\mathrm{Mg/dry\ ether}} \mathrm{C_6H_5MgBr}$.
3. Hydrolysis: $\mathrm{C_6H_5MgBr} + \mathrm{H_2O} \rightarrow \mathrm{C_6H_6} + \mathrm{Mg(OH)Br}$.
4. The product is benzene, which is option $2$.

**Subtopic:** Chemical Reactions of Diazonium Salts and Coupling Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q076_befadaa8_04112026.png?v=befadaa82c10)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q076_edb7982f_04112026.png?v=edb7982fc5bf)

---

## Q77

Chemistry · organic · Polymers

Which amongst the following molecules on polymerization produces neoprene?

- (1) $\mathrm{H_2C=CH-CH=CH_2}$
- **(2)** $\mathrm{H_2C=\overset{\overset{\displaystyle Cl}{|}}{C}-CH=CH_2}$
- (3) $\mathrm{H_2C=CH-C\equiv CH}$
- (4) $\mathrm{H_2C=\overset{\overset{\displaystyle CH_3}{|}}{C}-CH=CH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Neoprene is formed by free radical polymerisation of chloroprene.

**Solved independently** (answer withheld)

1. Neoprene is the addition polymer of chloroprene, $\mathrm{H_2C=C(Cl)-CH=CH_2}$ (2-chloro-1,3-butadiene), which is option $2$.

**Subtopic:** Natural Rubber (cis-1,4-Polyisoprene) and Vulcanisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q077_5464d0a4_04112026.png?v=5464d0a49aa6)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q077_96332abf_04112026.png?v=96332abf397b)

---

## Q78

Chemistry · physical · Electrochemistry

The conductivity of centimolar solution of $\mathrm{KCl}$ at $25^{\circ}\mathrm{C}$ is $0.0210\,\mathrm{ohm^{-1}\,cm^{-1}}$ and the resistance of the cell containing the solution at $25^{\circ}\mathrm{C}$ is $60\,\mathrm{ohm}$. The value of cell constant is

- (1) $1.34\,\mathrm{cm^{-1}}$
- (2) $3.28\,\mathrm{cm^{-1}}$
- **(3)** $1.26\,\mathrm{cm^{-1}}$
- (4) $3.34\,\mathrm{cm^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Conductivity = conductance $\times$ cell constant
2. $k = G\,G^{*}$
3. $= \frac{1}{R}G^{*}$
4. $G^{*} = k \times R = 0.0210 \times 60 = 1.26\,\mathrm{cm^{-1}}$

**Solved independently** (answer withheld)

1. Conductivity relates to resistance by $\kappa = \frac{G^*}{R}$, so $G^* = \kappa R$.
2. $G^* = 0.0210\,\mathrm{ohm^{-1}\,cm^{-1}} \times 60\,\mathrm{ohm} = 1.26\,\mathrm{cm^{-1}}$, which is option $3$.

**Subtopic:** Some Important Terms Related to Conductance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q078_59d9ad21_04112026.png?v=59d9ad2123fc)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q078_32246581_04112026.png?v=322465817376)

---

## Q79

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify product (A) in the following reaction:

![printed figure: 1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one →(Zn–Hg, conc. HCl) (A) + 2$\ce{H2O}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q079_19cb421d_04112026.png?v=19cb421dfc74)

*1-[3-(3-acetylcyclohexyl)phenyl]ethan-1-one →[Zn–Hg, conc. HCl] (A) + 2$\ce{H2O}$*

![drawn: 1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one →(Zn–Hg, conc. HCl) (A) + 2$\ce{H2O}$](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_question_5a86a14d_14112026.svg?v=5a86a14d5c1b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-[3-(3-acetylcyclohexyl)phenyl]ethan-1-one `CC(=O)c1cccc(C2CCCC(C(C)=O)C2)c1` ![1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_question_s1_b0bcb60f_14112026.svg?v=b0bcb60f4403); water `O` ![water](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_question_s2_795507b0_14112026.svg?v=795507b0c355)

- **(1)** 1-ethyl-3-(3-ethylcyclohexyl)benzene `CCc1cccc(C2CCCC(CC)C2)c1` ![1-ethyl-3-(3-ethylcyclohexyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_option_1_s1_04d2848e_14112026.svg?v=04d2848ee871)
- (2) 1-[3-[3-(1-hydroxyethyl)phenyl]cyclohexyl]ethan-1-ol `CC(O)c1cccc(C2CCCC(C(C)O)C2)c1` ![1-(3-(3-(1-hydroxyethyl)phenyl)cyclohexyl)ethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_option_2_s1_c64f9ecf_14112026.svg?v=c64f9ecf1ada)
- (3) [3-[3-(hydroxymethyl)cyclohexyl]phenyl]methanol `OCc1cccc(C2CCCC(CO)C2)c1` ![(3-(3-(hydroxymethyl)cyclohexyl)phenyl)methanol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_option_3_s1_2c5d719a_14112026.svg?v=2c5d719a19e2)
- (4) 1-methyl-3-(3-methylcyclohexyl)benzene `Cc1cccc(C2CCCC(C)C2)c1` ![1-methyl-3-(3-methylcyclohexyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q079_option_4_s1_1c1a93da_14112026.svg?v=1c1a93da0fd1)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. This reaction is Clemmensen reduction

**Solved independently** (answer withheld)

1. Zn-Hg with conc. HCl is the Clemmensen reduction, which converts a ketone $>C=O$ to $>CH_2$.
2. Each acetyl group $-COCH_3$ (on the cyclohexane ring and on the benzene ring) becomes an ethyl group $-CH_2CH_3$.
3. Two carbonyls reduced release $2H_2O$, matching the equation; the product with two ethyl groups is option $1$.

**Subtopic:** Reduction of Aldehydes and Ketones · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 33)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q079_3feb7d5f_04112026.png?v=3feb7d5f247a)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q079_139bcdaf_04112026.png?v=139bcdaf04d2)

---

## Q80

Chemistry · inorganic · The D- and F-Block Elements – Practice

The stability of $\mathrm{Cu^{2+}}$ is more than $\mathrm{Cu^{+}}$ salts in aqueous solution due to

- (1) First ionisation enthalpy
- (2) Enthalpy of atomization
- **(3)** Hydration energy
- (4) Second ionisation enthalpy

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The stability of $\mathrm{Cu^{2+}(aq)}$ is more than $\mathrm{Cu^{+}(aq)}$ is due to the much more negative $\Delta_{\mathrm{hyd}}H^{\circ}$ of $\mathrm{Cu^{2+}(aq)}$ than $\mathrm{Cu^{+}(aq)}$, which more than compensates for second ionisation enthalpy of $\mathrm{Cu}$.
2. $\Delta_{\mathrm{hyd}}H^{\circ}$ of $\mathrm{Cu^{2+}(aq)} = -2121\,\mathrm{kJ\,mol^{-1}}$
3. $\Delta_{i}H_{1}^{\circ}$ of $\mathrm{Cu} = +745\,\mathrm{kJ\,mol^{-1}}$
4. $\Delta_{i}H_{2}^{\circ}$ of $\mathrm{Cu} = +1960\,\mathrm{kJ\,mol^{-1}}$

**Solved independently** (answer withheld)

1. The greater stability of $\mathrm{Cu^{2+}}(aq)$ over $\mathrm{Cu^{+}}(aq)$ comes from the much more negative $\Delta_{hyd}H$ of $\mathrm{Cu^{2+}}$, which more than compensates for the second ionisation enthalpy of Cu, so the answer is option $3$.

**Subtopic:** Oxidation State · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q080_e42c3b15_04112026.png?v=e42c3b15363a)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q080_04da9314_04112026.png?v=04da9314fca4)

---

## Q81

Chemistry · physical · Chemical Kinetics

For a certain reaction, the rate $= k[\mathrm{A}]^{2}[\mathrm{B}]$, when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would

- (1) Decrease by a factor of nine
- (2) Increase by a factor of six
- **(3)** Increase by a factor of nine
- (4) Increase by a factor of three

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Rate $(r) = k[\mathrm{A}]^{2}[\mathrm{B}]$
2. When concentration of A is tripled
3. $[\mathrm{A}'] = [3\mathrm{A}]$
4. New rate, $r' = k[\mathrm{A}']^{2}[\mathrm{B}] = k[3\mathrm{A}]^{2}[\mathrm{B}] = 9k[\mathrm{A}]^{2}[\mathrm{B}]$
5. $r' = 9r$

**Solved independently** (answer withheld)

1. Initial rate: $r = k[\mathrm{A}]^2[\mathrm{B}]$.
2. With $[\mathrm{A}]$ tripled and $[\mathrm{B}]$ constant: $r' = k(3[\mathrm{A}])^2[\mathrm{B}]$.
3. $r' = 9k[\mathrm{A}]^2[\mathrm{B}] = 9r$, so the rate increases by a factor of nine, which is option $3$.

**Subtopic:** Rate Expression · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q081_167dbe46_04112026.png?v=167dbe46b99b)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q081_4ff07d45_04112026.png?v=4ff07d457f15)

---

## Q82

Chemistry · organic · Biomolecules

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) A unit formed by the attachment of a base to $1'$ position of sugar is known as nucleoside.
- (Statement II) When nucleoside is linked to phosphorous acid at $5'$-position of sugar moiety, we get nucleotide.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A unit formed by the attachment of a base to $1'$ position of sugar is known as nucleoside.
2. In nucleosides, the sugar carbons are numbered as $1'$, $2'$, $3'$, etc. in order to distinguish these from the bases (Fig.(a)).
3. When nucleoside is linked to phosphoric acid at $5'$-position of sugar moiety, we get a nucleotide (Fig.(b)).

**Solved independently** (answer withheld)

1. A nitrogenous base attached at the $1'$ position of the pentose sugar forms a nucleoside, so Statement I is true.
2. NCERT: a nucleotide forms when a nucleoside is linked to phosphoric acid ($\mathrm{H_3PO_4}$) at the $5'$ position; Statement II says phosphorous acid ($\mathrm{H_3PO_3}$), so as worded it is false.
3. Statement I true, Statement II false, which is option $3$.

**Subtopic:** Structure and Function of Nucleic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q082_855cb37b_04112026.png?v=855cb37b0e19)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q082_8bc1728d_04112026.png?v=8bc1728d8daf)

---

## Q83

Chemistry · organic · Amines

Which of the following reactions will NOT give primary amine as the product?

- (1) $\mathrm{CH_3CONH_2} \xrightarrow{\mathrm{Br_2/KOH}} \mathrm{Product}$
- (2) $\mathrm{CH_3CN} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{Product}$
- **(3)** $\mathrm{CH_3NC} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{Product}$
- (4) $\mathrm{CH_3CONH_2} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{Product}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (1) $\mathrm{CH_3{-}\overset{\overset{\Large O}{\|}}{C}{-}NH_2} \xrightarrow[\text{Hoffmann bromamide degradation reaction}]{\mathrm{Br_2/KOH}} \mathrm{CH_3{-}NH_2}$ (Primary amine)
2. (2) $\mathrm{CH_3{-}C{\equiv}N} \xrightarrow[\text{(ii) } \mathrm{H_3O^{+}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{CH_3{-}CH_2{-}NH_2}$ (Primary amine)
3. (3) $\mathrm{CH_3NC} \xrightarrow[\text{(ii) } \mathrm{H_3O^{+}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{CH_3{-}\overset{\overset{\Large H}{|}}{N}{-}CH_3}$ (Secondary amine)
4. (4) $\mathrm{CH_3{-}\overset{\overset{\Large O}{\|}}{C}{-}NH_2} \xrightarrow[\text{(ii) } \mathrm{H_3O^{+}}]{\text{(i) } \mathrm{LiAlH_4}} \mathrm{CH_3{-}CH_2{-}NH_2}$ (Primary amine)

**Solved independently** (answer withheld)

1. Option 2: $\mathrm{CH_3C{\equiv}N \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
2. Option 3: $\mathrm{CH_3N{\equiv}C \xrightarrow{LiAlH_4} CH_3NHCH_3}$, a secondary amine.
3. Option 4: $\mathrm{CH_3CONH_2 \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
4. Option 1: Hofmann bromamide degradation, $\mathrm{CH_3CONH_2 \xrightarrow{Br_2/KOH} CH_3NH_2}$, a primary amine.
5. Only option $3$ does not give a primary amine.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q083_df43ae49_04112026.png?v=df43ae49ef2a)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q083_170421d4_12112026.png?v=170421d418e3)

---

## Q84

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The element expected to form largest ion to achieve the nearest noble gas configuration is

- (1) $\mathrm{O}$
- (2) $\mathrm{F}$
- **(3)** $\mathrm{N}$
- (4) $\mathrm{Na}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For isoelectronic species, as the charge on anion increases, ionic size increases
2. So, $\mathrm{N}$ forms $\mathrm{N^{3-}}$ anion with largest ionic size

**Solved independently** (answer withheld)

1. To reach the nearest noble gas configuration (Ne) the elements form $\mathrm{N^{3-}}$, $\mathrm{O^{2-}}$, $\mathrm{F^{-}}$ and $\mathrm{Na^{+}}$, which all have $10$ electrons.
2. For isoelectronic ions, radius falls as nuclear charge rises: $Z = 7 < 8 < 9 < 11$.
3. So $\mathrm{N^{3-}} > \mathrm{O^{2-}} > \mathrm{F^{-}} > \mathrm{Na^{+}}$; the largest ion comes from $\mathrm{N}$, which is option $3$.

**Subtopic:** Trends in Chemical Properties – Atomic and Ionic Radius · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q084_1e190144_04112026.png?v=1e190144d08d)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q084_269bff9c_04112026.png?v=269bff9cde4d)

---

## Q85

Chemistry · physical · The Solid State

A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy $1/3$ of tetrahedral voids. If the formula of the compound is $\mathrm{A_xB_y}$, then the value of $x + y$ is in option

- **(1)** $5$
- (2) $4$
- (3) $3$
- (4) $2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Number of atoms of element $\mathrm{B}$ is $N$
2. So, the number of atoms of element $\mathrm{A}$ is $\frac{1}{3} \times 2N$
3. $\therefore$ The formula of the compound is $\mathrm{A}_{\frac{2}{3}N}\mathrm{B}_{N} = \mathrm{A_2B_3}$
4. So, $x = 2$
5. $y = 3$
6. $\therefore$ $x + y = 5$

**Solved independently** (answer withheld)

1. Let the number of B atoms in the ccp lattice be $N$.
2. A ccp lattice has $2N$ tetrahedral voids.
3. A occupies $\frac{1}{3}$ of them: $n_A = \frac{1}{3}(2N) = \frac{2N}{3}$.
4. $A : B = \frac{2N}{3} : N = 2 : 3$, so the formula is $\mathrm{A_2B_3}$.
5. $x + y = 2 + 3 = 5$, which is option $1$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q085_3cede93a_04112026.png?v=3cede93a8ca5)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q085_3ba47dda_04112026.png?v=3ba47dda8c0e)

---

## Q86

Chemistry · organic · Alcohols, Phenols and Ethers

Which amongst the following will be most readily dehydrated under acidic conditions?

- (1) 4-nitropentan-2-ol `CC(O)CC(C)[N+](=O)[O-]` ![4-nitropentan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q086_option_1_s1_82acc902_14112026.svg?v=82acc902dc27)
- **(2)** pentane-2,4-diol `CC(O)CC(C)O` ![pentane-2,4-diol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q086_option_2_s1_c43e7c26_14112026.svg?v=c43e7c26414c)
- (3) 3-nitrobutane-1,2-diol `CC(C(O)CO)[N+](=O)[O-]` ![3-nitrobutane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q086_option_3_s1_0c486a98_14112026.svg?v=0c486a9853f8)
- (4) 5-nitrohexan-2-ol `CC(O)CCC(C)[N+](=O)[O-]` ![5-nitrohexan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q086_option_4_s1_c55c2efe_14112026.svg?v=c55c2efed6a2)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Under acidic conditions alcohols dehydrate by the E1 path: $\mathrm{R{-}OH} + \mathrm{H^+} \rightarrow \mathrm{R{-}OH_2^+} \rightarrow \mathrm{R^+} + \mathrm{H_2O}$.
2. Carbocation formation is the slow step, so the substrate giving the most stable carbocation dehydrates most readily.
3. In options $1$, $3$ and $4$ the $-\mathrm{NO_2}$ group exerts a strong $-I$ effect that destabilises the nearby carbocation (option $3$ also has a primary $-\mathrm{CH_2OH}$).
4. Option $2$ (pentane-2,4-diol) has no $-\mathrm{NO_2}$ and gives an unhindered secondary carbocation, so it is dehydrated most readily: option $2$.

**Subtopic:** Reactions of Alcohols · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 36)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q086_a6b18740_04112026.png?v=a6b187402206)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q086_ca9761f5_04112026.png?v=ca9761f5c9cb)

---

## Q87

Chemistry · physical · Thermodynamics

Which amongst the following options is the correct relation between change in enthalpy and change in internal energy?

- (1) $\Delta H = \Delta U - \Delta n_g RT$
- **(2)** $\Delta H = \Delta U + \Delta n_g RT$
- (3) $\Delta H - \Delta U = -\Delta nRT$
- (4) $\Delta H + \Delta U = \Delta nR$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct relation between change in enthalpy and change in internal energy is
2. $\Delta H = \Delta U + \Delta n_{g}RT$

**Solved independently** (answer withheld)

1. By definition $H = U + pV$, so at constant pressure $\Delta H = \Delta U + p\Delta V$.
2. For gaseous species treated as ideal, $p\Delta V = \Delta n_g RT$.
3. Hence $\Delta H = \Delta U + \Delta n_g RT$, which is option $2$.

**Subtopic:** Enthalpy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q087_6c3457f4_04112026.png?v=6c3457f499e1)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q087_4f205dd3_04112026.png?v=4f205dd3330e)

---

## Q88

Chemistry · inorganic · The p–Block Elements

Match List-I with List-II :
List-I (Oxoacids of Sulphur) | List-II (Bonds)
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | Peroxodisulphuric acid | I | Two $\mathrm{S{-}OH}$, Four $\mathrm{S{=}O}$, One $\mathrm{S{-}O{-}S}$ |
| B | Sulphuric acid | II | Two $\mathrm{S{-}OH}$, One $\mathrm{S{=}O}$ |
| C | Pyrosulphuric acid | III | Two $\mathrm{S{-}OH}$, Four $\mathrm{S{=}O}$, One $\mathrm{S{-}O{-}O{-}S}$ |
| D | Sulphurous acid | IV | Two $\mathrm{S{-}OH}$, Two $\mathrm{S{=}O}$ |

- (1) A–I, B–III, C–II, D–IV
- **(2)** A–III, B–IV, C–I, D–II
- (3) A–I, B–III, C–IV, D–II
- (4) A–III, B–IV, C–II, D–I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Peroxodisulphuric acid $\mathrm{H_2S_2O_8}$: $\mathrm{HO{-}S(O_2){-}O{-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}O{-}S}$, so $A \to III$.
2. Sulphuric acid $\mathrm{H_2SO_4}$: $\mathrm{(HO)_2S(=O)_2}$ has two $\mathrm{S{-}OH}$ and two $\mathrm{S{=}O}$, so $B \to IV$.
3. Pyrosulphuric acid $\mathrm{H_2S_2O_7}$: $\mathrm{HO{-}S(O_2){-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}S}$, so $C \to I$.
4. Sulphurous acid $\mathrm{H_2SO_3}$: $\mathrm{(HO)_2S{=}O}$ has two $\mathrm{S{-}OH}$ and one $\mathrm{S{=}O}$, so $D \to II$.
5. $A{-}III,\ B{-}IV,\ C{-}I,\ D{-}II$ is option $2$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 37)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q088_7ad49b3b_04112026.png?v=7ad49b3bceee)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q088_6a4766e5_04112026.png?v=6a4766e59d9b)

---

## Q89

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which of the following statements are INCORRECT? Choose the correct answer from the options given below:

- (A) All the transition metals except scandium form MO oxides which are ionic.
- (B) The highest oxidation number corresponding to the group number in transition metal oxides is attained in $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$.
- (C) Basic character increases from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_4}$ to $\mathrm{V_2O_5}$.
- (D) $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO_4^{3-}}$ salts.
- (E) CrO is basic but $\mathrm{Cr_2O_3}$ is amphoteric.

- (1) A and E only
- (2) B and D only
- **(3)** C and D only
- (4) B and C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. All transitions metals except $\mathrm{Sc}$ from $\mathrm{MO}$ oxides which are ionic.
2. The highest oxidation number corresponding to the group number in transition metal oxides in attained in $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$.
3. Acidic character increases from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_4}$ to $\mathrm{V_2O_5}$.
4. $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO^{2+}}$.
5. $\mathrm{CrO}$ is basic but $\mathrm{Cr_2O_3}$ is amphoteric.

**Solved independently** (answer withheld)

1. A: all transition metals except Sc form ionic $\mathrm{MO}$ oxides, so A is correct.
2. B: oxides from $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$ show the highest oxidation state equal to the group number, so B is correct.
3. C: as oxidation state of V rises, $\mathrm{V_2O_3}$ (basic) $\to$ $\mathrm{V_2O_4}$ (less basic) $\to$ $\mathrm{V_2O_5}$ (amphoteric), so basic character decreases and C is incorrect.
4. D: $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO^{2+}}$ salts, not $\mathrm{VO_4^{3-}}$, so D is incorrect.
5. E: $\mathrm{CrO}$ is basic and $\mathrm{Cr_2O_3}$ is amphoteric, so E is correct.
6. Incorrect statements are C and D, which is option $3$.

**Subtopic:** Transition Elements (d-Block) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q089_4cea312d_04112026.png?v=4cea312dafc8)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q089_7c428249_04112026.png?v=7c428249b897)

---

## Q90

Chemistry · inorganic · Coordination Compounds – Practice

Which complex compound is most stable?

- (1) $\mathrm{[Co(NH_3)_4(H_2O)Br](NO_3)_2}$
- (2) $\mathrm{[Co(NH_3)_3(NO_3)_3]}$
- **(3)** $\mathrm{[CoCl_2(en)_2]NO_3}$
- (4) $\mathrm{[Co(NH_3)_6]_2(SO_4)_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Chelating ligands in general form more stable complexes than their monodentate analogs
2. $\therefore$ The most stable complex is $\mathrm{[CoCl_2(en)_2]NO_3}$

**Solved independently** (answer withheld)

1. Options $2$, $4$ and $1$ contain only monodentate ligands ($\mathrm{NH_3}$, $\mathrm{NO_3^-}$, $\mathrm{H_2O}$, $\mathrm{Br^-}$).
2. Option $3$, $\mathrm{[CoCl_2(en)_2]NO_3}$, contains two bidentate $\mathrm{en}$ ligands that form chelate rings with $\mathrm{Co^{3+}}$.
3. Chelation (chelate effect) greatly increases complex stability, so option $3$ is the most stable.

**Subtopic:** Ligands · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q090_cc63d1bc_04112026.png?v=cc63d1bc5993)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q090_69da524c_04112026.png?v=69da524ce73b)

---

## Q91

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

The reaction that does NOT take place in a blast furnace between $900\,\mathrm{K}$ to $1500\,\mathrm{K}$ temperature range during extraction of iron is :

- **(1)** $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$
- (2) $\mathrm{FeO + CO \rightarrow Fe + CO_2}$
- (3) $\mathrm{C + CO_2 \rightarrow 2CO}$
- (4) $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At $900$ -$1500\,\mathrm{K}$ (higher temperature range in the blast furnace)
2. Reaction which take place are :–
3. $\mathrm{C + CO_2 \rightarrow 2CO}$
4. $\mathrm{FeO + CO \rightarrow Fe + CO_2}$
5. $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$ (Slag formation)
6. $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$ $\rightarrow$ This take place at $500$ - $800\,\mathrm{K}$.

**Solved independently** (answer withheld)

1. In the blast furnace, the $500$-$800\,\mathrm{K}$ zone has $\mathrm{3Fe_2O_3 + CO \rightarrow 2Fe_3O_4 + CO_2}$, $\mathrm{Fe_3O_4 + 4CO \rightarrow 3Fe + 4CO_2}$ and $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$.
2. The $900$-$1500\,\mathrm{K}$ zone has $\mathrm{C + CO_2 \rightarrow 2CO}$ and $\mathrm{FeO + CO \rightarrow Fe + CO_2}$; limestone decomposes and $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$ forms slag in the hotter region.
3. So $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$ does not take place at $900$-$1500\,\mathrm{K}$, which is option $1$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q091_870ac21d_04112026.png?v=870ac21d6467)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q091_ed31ff0d_04112026.png?v=ed31ff0d257c)

---

## Q92

Chemistry · physical · Chemical Equilibrium

The equilibrium concentrations of the species in the reaction $\mathrm{A + B \rightleftharpoons C + D}$ are 2, 3, 10 and $6\,\mathrm{mol\,L^{-1}}$, respectively at $300\,\mathrm{K}$. $\Delta G^\circ$ for the reaction is ($R = 2\,\mathrm{cal/mol\,K}$)

- (1) $1372.60\,\mathrm{cal}$
- (2) $-137.26\,\mathrm{cal}$
- **(3)** $-1381.80\,\mathrm{cal}$
- (4) $-13.73\,\mathrm{cal}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{A + B \rightleftharpoons C + D}$
2. at equilibrium $2 \quad 3 \quad 10 \quad 6$
3. $k_{eq} = [\mathrm{C}]\,[\mathrm{D}] / [\mathrm{A}]\,[\mathrm{B}]$
4. $k_{eq} = \frac{10 \times 6}{2 \times 3} = 10$
5. $\Delta G^{\circ} = -RT \ln K$
6. $= -2.303\,RT \log K$
7. $= -2.303 \times 2 \times 300 \times \log 10$
8. $= -1381.8\,\mathrm{cal}$

**Solved independently** (answer withheld)

1. $K = \frac{[\mathrm{C}][\mathrm{D}]}{[\mathrm{A}][\mathrm{B}]} = \frac{10 \times 6}{2 \times 3} = 10$.
2. $\Delta G^{\circ} = -2.303\,RT \log K$.
3. $\Delta G^{\circ} = -2.303 \times 2 \times 300 \times \log 10 = -2.303 \times 600 \times 1$.
4. $\Delta G^{\circ} = -1381.8\,\mathrm{cal}$, which is option $3$.

**Subtopic:** Relationship Between K, Q and G · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q092_8a405d53_04112026.png?v=8a405d5358b4)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q092_f4e772d2_04112026.png?v=f4e772d2b6f9)

---

## Q93

Chemistry · organic · General Organic Chemistry

Consider the following compounds/species:
[figure: structures i–vii]
The number of compounds/species which obey Huckel’s rule is ______.

![printed figure: i. naphthalene; ii. cyclopentadienyl anion (cyclopenta-2,4-dien-1-ide); iii. cyclobutadiene; iv. cyclopropenyl anion (cycloprop-2-en-1-ide); v. cyclopropenyl cation (cycloprop-2-en-1-ylium); vi. cyclooctatetraene; vii. anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q093_29b12399_04112026.png?v=29b12399dea7)

*i. naphthalene; ii. cyclopentadienyl anion (cyclopenta-2,4-dien-1-ide); iii. cyclobutadiene; iv. cyclopropenyl anion (cycloprop-2-en-1-ide); v. cyclopropenyl cation (cycloprop-2-en-1-ylium); vi. cyclooctatetraene; vii. anthracene*

![drawn: i. naphthalene; ii. cyclopentadienyl anion (cyclopenta-2,4-dien-1-ide); iii. cyclobutadiene; iv. cyclopropenyl anion (cycloprop-2-en-1-ide); v. cyclopropenyl cation (cycloprop-2-en-1-ylium); vi. cyclooctatetraene; vii. anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_486ac994_14112026.svg?v=486ac99419f4)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: naphthalene `c1ccc2ccccc2c1` ![naphthalene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s1_1c4ddda0_14112026.svg?v=1c4ddda09622); cyclopenta-2,4-dien-1-ide `c1cc[cH-]c1` ![cyclopenta-2,4-dien-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s2_3e03e8a7_14112026.svg?v=3e03e8a741d1); cyclobutadiene `C1=CC=C1` ![cyclobutadiene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s3_68eaa57e_14112026.svg?v=68eaa57ee7c4); cycloprop-2-en-1-ide `C1=C[CH-]1` ![cycloprop-2-en-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s4_743bf84c_14112026.svg?v=743bf84c231a); cycloprop-2-en-1-ylium `c1c[cH+]1` ![cycloprop-2-en-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s5_afa2b3f9_14112026.svg?v=afa2b3f913ea); cycloocta-1,3,5,7-tetraene `C1=CC=CC=CC=C1` ![cycloocta-1,3,5,7-tetraene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s6_05a705c0_14112026.svg?v=05a705c03822); anthracene `c1ccc2cc3ccccc3cc2c1` ![anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q093_question_s7_d63f99db_14112026.svg?v=d63f99db8ebd)

- **(1)** 4
- (2) 6
- (3) 2
- (4) 5

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Criteria for Huckel’s rule:
2. (i) Planarity
3. (ii) Complete delocalisation of $\pi$ electrons
4. (iii) Presence of $(4n + 2)\pi$ electrons in ring where $n$ is an integer ($n = 0, 1, 2, \ldots$)
5. The compounds which follow Huckel’s rule are:

**Solved independently** (answer withheld)

1. i. Naphthalene: planar, cyclic, conjugated with $10\,\pi$ electrons $= 4(2)+2$, so it obeys Huckel's rule.
2. ii. Cyclopentadienyl anion: $4\,\pi$ electrons from two C=C plus the lone pair gives $6\,\pi$ electrons $= 4(1)+2$, so it obeys.
3. iii. Cyclobutadiene: $4\,\pi$ electrons $= 4n$ with $n=1$, antiaromatic, does not obey.
4. iv. Cyclopropenyl anion: $2\,\pi$ from C=C plus the lone pair gives $4\,\pi$ electrons $= 4n$, does not obey.
5. v. Cyclopropenyl cation: $2\,\pi$ electrons $= 4(0)+2$, so it obeys.
6. vi. Cyclooctatetraene: $8\,\pi$ electrons $= 4n$ and tub-shaped (non-planar), does not obey.
7. vii. Anthracene: $14\,\pi$ electrons $= 4(3)+2$, so it obeys.
8. Species obeying: i, ii, v, vii, so the count is $4$, which is option $1$.

**Subtopic:** Aromaticity · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 39)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q093_f15a4d4d_04112026.png?v=f15a4d4d690c)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q093_e7a1f6d6_04112026.png?v=e7a1f6d602e5)

---

## Q94

Chemistry · physical · Redox Reactions

On balancing the given redox reaction,
$\mathrm{aCr_2O_7^{2-} + bSO_3^{2-}(aq) + cH^{+}(aq) \rightarrow 2aCr^{3+}(aq) + bSO_4^{2-}(aq) + \frac{c}{2}H_2O(l)}$
the coefficients a, b and c are found to be, respectively-

- **(1)** 1, 3, 8
- (2) 3, 8, 1
- (3) 1, 8, 3
- (4) 8, 1, 3

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Using Ion electron method :
2. Reduction Half reaction : $\mathrm{Cr_2O_7^{2-} + 6e^{-} \longrightarrow 2Cr^{3+}}$
3. Oxidation Half reaction : $\mathrm{SO_3^{2-} \longrightarrow SO_4^{2-} + 2\bar{e}} \times 3$
4. Overall reaction : $\mathrm{Cr_2O_7^{2-} + 3SO_3^{2-} \longrightarrow 2Cr^{3+} + 3SO_4^{2-}}$
5. To balance 'O' atoms, adding $\mathrm{H_2O}$ on LHS
6. $\mathrm{Cr_2O_7^{2-} + 3SO_3^{2-} \longrightarrow 2Cr^{3+} + 3SO_4^{2-} + 4H_2O}$
7. To balance 'H' atoms, adding $\mathrm{H^{+}}$ on RHS
8. $\mathrm{Cr_2O_7^{2-} + 3SO_3^{2-} + 8H^{+} \longrightarrow 2Cr^{3+} + 3SO_4^{2-} + 4H_2O}$
9. $\therefore$ $a = 1$
10. $b = 3$
11. $c = 8$

**Solved independently** (answer withheld)

1. Oxidation states: Cr in $\mathrm{Cr_2O_7^{2-}}$ is $+6$, in $\mathrm{Cr^{3+}}$ is $+3$; S in $\mathrm{SO_3^{2-}}$ is $+4$, in $\mathrm{SO_4^{2-}}$ is $+6$.
2. Electrons gained per $\mathrm{Cr_2O_7^{2-}}$: $2 \times 3 = 6$; electrons lost per $\mathrm{SO_3^{2-}}$: $2$.
3. Equate electrons: $6a = 2b \Rightarrow b = 3a$; take $a = 1$, $b = 3$.
4. Charge balance: left $-2 - 6 + c$, right $2(+3) + 3(-2) = 0$, so $c - 8 = 0 \Rightarrow c = 8$.
5. Check oxygen: left $7 + 9 = 16$, right $12 + \frac{c}{2} = 12 + 4 = 16$. Balanced.
6. $a, b, c = 1, 3, 8$, which is option $1$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 40)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q094_773ef813_04112026.png?v=773ef813c847)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q094_d74ecb41_12112026.png?v=d74ecb4173cc)

---

## Q95

Chemistry · organic · Haloalkanes and Haloarenes

Identify the final product [D] obtained in the following sequence of reactions.
$\mathrm{CH_3CHO} \xrightarrow[\text{ii) } \mathrm{H_3O^+}]{\text{i) } \mathrm{LiAlH_4}} [\mathrm{A}] \xrightarrow[\Delta]{\mathrm{H_2SO_4}} [\mathrm{B}]$
$\xrightarrow{\mathrm{HBr}} [\mathrm{C}] \xrightarrow[\text{Na/dry ether}]{\text{[structure: bromobenzene, see figure]}} [\mathrm{D}]$

![printed figure: →(HBr) (C) →(bromobenzene, Na/dry ether) (D)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q095_3f4390ea_04112026.png?v=3f4390eabe5c)

*→[HBr] [C] →[bromobenzene, Na/dry ether] [D]*

![drawn: →(HBr) (C) →(bromobenzene, Na/dry ether) (D)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q095_question_999c1d5d_14112026.svg?v=999c1d5dd059)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q095_question_s1_61d2ed9e_14112026.svg?v=61d2ed9ebe04)

- **(1)** ethylbenzene `CCc1ccccc1` ![ethylbenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q095_option_1_s1_c3cd0ee9_14112026.svg?v=c3cd0ee97328)
- (2) biphenyl `c1ccc(-c2ccccc2)cc1` ![biphenyl](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q095_option_2_s1_96946bcf_14112026.svg?v=96946bcfe353)
- (3) $\mathrm{C_4H_{10}}$
- (4) $\mathrm{HC \equiv C^{\ominus}Na^{+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CHO} \xrightarrow{\mathrm{LiAlH_4},\ \mathrm{H_3O^+}} \mathrm{CH_3CH_2OH}$ = [A] (the aldehyde is reduced to a primary alcohol).
2. $\mathrm{CH_3CH_2OH} \xrightarrow{\mathrm{conc.\ H_2SO_4},\ \Delta} \mathrm{CH_2{=}CH_2}$ = [B] (dehydration).
3. $\mathrm{CH_2{=}CH_2} + \mathrm{HBr} \rightarrow \mathrm{CH_3CH_2Br}$ = [C].
4. $\mathrm{C_6H_5Br} + \mathrm{CH_3CH_2Br} \xrightarrow{\mathrm{Na/dry\ ether}} \mathrm{C_6H_5CH_2CH_3}$ = [D] (Wurtz-Fittig reaction).
5. Ethylbenzene is the structure in option $1$.

**Subtopic:** Reactions of Haloarenes · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 40)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q095_4c1c5bd2_04112026.png?v=4c1c5bd2972a)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q095_b092ed55_04112026.png?v=b092ed55ba14)

---

## Q96

Chemistry · organic · Alcohols, Phenols and Ethers

Consider the following reaction : $\mathrm{C_6H_5{-}CH_2{-}O{-}C_6H_5} \xrightarrow[\Delta]{\mathrm{HI}} \mathrm{A + B}$ Identify products A and B.

![printed figure: benzyl phenyl ether →(HI, Δ) A + B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q096_f25d7663_04112026.png?v=f25d766386dd)

*benzyl phenyl ether →[HI, Δ] A + B*

![drawn: benzyl phenyl ether →(HI, Δ) A + B](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_question_31e1793b_14112026.svg?v=31e1793b1d75)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzyl phenyl ether `c1ccc(COc2ccccc2)cc1` ![benzyl phenyl ether](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_question_s1_ddf58708_14112026.svg?v=ddf587088e3e)

- (1) toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_1_s1_b4bc3ebf_14112026.svg?v=b4bc3ebff656); phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_1_s2_26093786_14112026.svg?v=26093786dda8) — $\mathrm{A} = \mathrm{C_6H_5{-}CH_3}$ and $\mathrm{B} = \mathrm{C_6H_5{-}OH}$
- (2) benzyl alcohol `OCc1ccccc1` ![benzyl alcohol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_2_s1_76b1501e_14112026.svg?v=76b1501e4315); iodobenzene `Ic1ccccc1` ![iodobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_2_s2_1d87e391_14112026.svg?v=1d87e3910938) — $\mathrm{A} = \mathrm{C_6H_5{-}CH_2OH}$ and $\mathrm{B} = \mathrm{C_6H_5{-}I}$
- **(3)** benzyl iodide `ICc1ccccc1` ![benzyl iodide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_3_s1_c8defd7a_14112026.svg?v=c8defd7a0f2d); phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_3_s2_26093786_14112026.svg?v=26093786dda8) — $\mathrm{A} = \mathrm{C_6H_5{-}CH_2I}$ and $\mathrm{B} = \mathrm{C_6H_5{-}OH}$
- (4) toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_4_s1_b4bc3ebf_14112026.svg?v=b4bc3ebff656); iodobenzene `Ic1ccccc1` ![iodobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q096_option_4_s2_1d87e391_14112026.svg?v=1d87e3910938) — $\mathrm{A} = \mathrm{C_6H_5{-}CH_3}$ and $\mathrm{B} = \mathrm{C_6H_5{-}I}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The ether oxygen is protonated by HI: $\mathrm{C_6H_5CH_2{-}\overset{+}{O}H{-}C_6H_5}$.
2. The $\mathrm{O{-}C_6H_5}$ bond has partial double-bond character from resonance, so $\mathrm{I^-}$ cannot attack the phenyl carbon.
3. $\mathrm{I^-}$ attacks the benzylic carbon instead, breaking the $\mathrm{CH_2{-}O}$ bond.
4. Products: $\mathrm{A} = \mathrm{C_6H_5CH_2I}$ and $\mathrm{B} = \mathrm{C_6H_5OH}$, which is option $3$.

**Subtopic:** Reactions of Ethers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q096_bd4f00c2_04112026.png?v=bd4f00c2ec8e)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q096_86a09bd7_04112026.png?v=86a09bd7b008)

---

## Q97

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the major product obtained in the following reaction: [figure] $+\,2[\mathrm{Ag(NH_3)_2}]^{+}\,+\,3\,^{-}\mathrm{OH} \xrightarrow{\Delta}$ major product

![printed figure: 2-acetylbenzaldehyde + 2 $\ce{(Ag(NH3)2)+}$ + 3 $\ce{OH-}$ →(Δ) major product](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q097_4784c8a2_04112026.png?v=4784c8a20ea2)

*2-acetylbenzaldehyde + 2 $\ce{[Ag(NH3)2]+}$ + 3 $\ce{OH-}$ →[Δ] major product*

![drawn: 2-acetylbenzaldehyde + 2 $\ce{(Ag(NH3)2)+}$ + 3 $\ce{OH-}$ →(Δ) major product](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_question_23e46c77_14112026.svg?v=23e46c773fb8)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2-acetylbenzaldehyde `CC(=O)c1ccccc1C=O` ![2-acetylbenzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_question_s1_a0144de1_14112026.svg?v=a0144de11df3); diamminesilver(I) `[NH3]->[Ag+]<-[NH3]` ![diamminesilver(I)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_question_s2_919f617f_14112026.svg?v=919f617f4899); hydroxide `[OH-]` ![hydroxide](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_question_s3_0dcb3471_14112026.svg?v=0dcb3471c0a1)

- (1) 1-[2-(hydroxymethyl)phenyl]ethan-1-ol `CC(O)c1ccccc1CO` ![1-(2-(hydroxymethyl)phenyl)ethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_option_1_s1_94ca89a2_14112026.svg?v=94ca89a2ada8)
- (2) 1-[2-(hydroxymethyl)phenyl]ethan-1-one `CC(=O)c1ccccc1CO` ![1-(2-(hydroxymethyl)phenyl)ethan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_option_2_s1_7d7073d0_14112026.svg?v=7d7073d0e417)
- **(3)** 2-acetylbenzoate `CC(=O)c1ccccc1C(=O)[O-]` ![2-acetylbenzoate](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_option_3_s1_b2b6129c_14112026.svg?v=b2b6129c94a6)
- (4) 2-(1-hydroxyethyl)benzoate `CC(O)c1ccccc1C(=O)[O-]` ![2-(1-hydroxyethyl)benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2023/2023_E5/figures_drawn/q097_option_4_s1_ad108def_14112026.svg?v=ad108def0c1a)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ammoniacal silver nitrate solution is Tollens’ reagent.
2. Tollens’ reagent can be used to distinguish aldehyde & ketone as aldehyde upon warming with Tollens’ reagent produces a silver mirror due to formation of silver metal in alkaline medium.
3. Aldehyde is oxidised to corresponding carboxylate anion.

**Solved independently** (answer withheld)

1. Tollens' reagent $[\mathrm{Ag(NH_3)_2}]^{+}$ is a mild oxidant that oxidises aldehydes but not ketones.
2. $\mathrm{R{-}CHO} + 2[\mathrm{Ag(NH_3)_2}]^{+} + 3\,\mathrm{OH^-} \rightarrow \mathrm{R{-}COO^-} + 2\mathrm{Ag} + 4\mathrm{NH_3} + 2\mathrm{H_2O}$, matching the stoichiometry given.
3. The $-\mathrm{COCH_3}$ group is not oxidised or reduced, so the product is $o$-acetylbenzoate, which is option $3$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q097_bb572f54_04112026.png?v=bb572f5427bf)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q097_764978e7_04112026.png?v=764978e77e26)

---

## Q98

Chemistry · inorganic · Environmental Chemistry

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below:

- (I) The nutrient deficient water bodies lead to eutrophication
- (II) Eutrophication leads to decrease in the level of oxygen in the water bodies.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is correct but Statement II is false.
- **(4)** Statement I is incorrect but Statement II is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Nutrient enriched water bodies support a dense plant population, which kills animal life by depriving it of oxygen and results in subsequent loss of biodiversity.
2. This process is called as eutrophication.

**Solved independently** (answer withheld)

1. Statement I is false: eutrophication results from nutrient enrichment (e.g. nitrates, phosphates) of water bodies, not nutrient deficiency.
2. Statement II is true: algal blooms and their decomposition by microbes reduce the dissolved oxygen in the water.
3. Statement I incorrect and Statement II true, which is option $4$.

**Subtopic:** Water Pollution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q098_2d4ce297_04112026.png?v=2d4ce297c2e3)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q098_f13aa697_04112026.png?v=f13aa6970d10)

---

## Q99

Chemistry · physical · The Solid State

What fraction of one edge centred octahedral void lies in one unit cell of fcc?

- (1) $\frac{1}{2}$
- (2) $\frac{1}{3}$
- **(3)** $\frac{1}{4}$
- (4) $\frac{1}{12}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The total number of octahedral voids in FCC are four
2. Octahedral voids in FCC = Edge centres + Body centre
3. The contribution of edge centre = $\frac{1}{4}$
4. $\therefore$ Fraction of one edge centred octahedral void in one unit cell of FCC = $\frac{1}{4}$

**Solved independently** (answer withheld)

1. An octahedral void at an edge centre of the fcc cell lies on an edge shared by $4$ unit cells.
2. Fraction belonging to one unit cell $= \frac{1}{4}$, which is option $3$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q099_e1cb0577_04112026.png?v=e1cb05772aae)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q099_1d88ee49_04112026.png?v=1d88ee49904a)

---

## Q100

Chemistry · physical · Surface Chemistry

Pumice stone is an example of

- (1) Sol
- (2) Gel
- **(3)** Solid sol
- (4) Foam

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pumice stone is a solid sol.
2. Dispersed phase : Gas
3. Dispersed medium : Solid

**Solved independently** (answer withheld)

1. Pumice stone has gas as the dispersed phase in a solid dispersion medium; per the NCERT colloid table, gas-in-solid is a solid sol, which is option $3$.

**Subtopic:** Classification of Colloids by Dispersed Phase and Dispersion Medium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q100_1a6e0d16_04112026.png?v=1a6e0d161a8c)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q100_89fa76d8_12112026.png?v=89fa76d86712)

---

## Q101

Biology · botany · Photosynthesis in Higher Plants

How many ATP and $\mathrm{NADPH_2}$ are required for the synthesis of one molecule of Glucose during Calvin cycle?

- (1) 12 ATP and 12 $\mathrm{NADPH_2}$
- **(2)** 18 ATP and 12 $\mathrm{NADPH_2}$
- (3) 12 ATP and 16 $\mathrm{NADPH_2}$
- (4) 18 ATP and 16 $\mathrm{NADPH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For every $\mathrm{CO_2}$ molecule entering the Calvin cycle, $3$ molecules of $\mathrm{ATP}$ and $2$ of $\mathrm{NADPH_2}$ are required.
2. To make one molecule of glucose, $6$ turns of the cycle are required.
3. Thus, $\mathrm{ATP}$ and $\mathrm{NADPH_2}$ molecules required for synthesis of one molecule of glucose during Calvin cycle will be
4. $\rightarrow 6 \times \begin{bmatrix} 3\,\mathrm{ATP} \\ 2\,\mathrm{NADPH_2} \end{bmatrix} = \begin{matrix} 18\,\mathrm{ATP}\ \text{and} \\ 12\,\mathrm{NADPH_2} \end{matrix}$

**Solved independently** (answer withheld)

1. Fixing one $\mathrm{CO_2}$ in the Calvin cycle uses $3$ ATP and $2$ $\mathrm{NADPH}$.
2. One glucose ($\mathrm{C_6}$) needs $6$ turns of the cycle.
3. ATP: $6 \times 3 = 18$; $\mathrm{NADPH}$: $6 \times 2 = 12$, which is option $2$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 43)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q101_4a00798c_04112026.png?v=4a00798c6d0b)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q101_1887742a_04112026.png?v=1887742aceca)

---

## Q102

Biology · botany · Sexual Reproduction in Flowering Plants

Large, colourful, fragrant flowers with nectar are seen in

- **(1)** Insect pollinated plants
- (2) Bird pollinated plants
- (3) Bat pollinated plants
- (4) Wind pollinated plants

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Large, colourful, fragrant flowers with nectar attract biotic pollinators (insects), thus, they are seen in insect pollinated plants.

**Solved independently** (answer withheld)

1. NCERT describes insect-pollinated flowers as large, colourful, fragrant and rich in nectar, so the answer is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 43)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q102_8073b275_04112026.png?v=8073b2753871)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q102_8669688f_04112026.png?v=8669688ffcef)

---

## Q103

Biology · botany · Principles of Inheritance and Variation

The phenomenon of pleiotropism refers to

- (1) Presence of several alleles of a single gene controlling a single crossover
- (2) Presence of two alleles, each of the two genes controlling a single trait
- **(3)** A single gene affecting multiple phenotypic expression
- (4) More than two genes affecting a single character

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When a single gene affects multiple phenotypic expression, the gene is called pleiotropic gene and the phenomenon is called pleiotropism.

**Solved independently** (answer withheld)

1. Pleiotropy is defined as a single gene affecting multiple phenotypic traits, so the answer is option $3$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q103_c40bd7d6_04112026.png?v=c40bd7d66463)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q103_8236a399_04112026.png?v=8236a399772d)

---

## Q104

Biology · botany · Principles of Inheritance and Variation

Frequency of recombination between gene pairs on same chromosome as a measure of the distance between genes to map their position on chromosome, was used for the first time by

- (1) Thomas Hunt Morgan
- (2) Sutton and Boveri
- **(3)** Alfred Sturtevant
- (4) Henking

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Alfred Sturtevant used the frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes and ‘mapped’ their position on the chromosome.
2. Sutton and Boveri proposed chromosomal theory of inheritance.
3. Henking discovered $\mathrm{X}$-chromosome.
4. Thomas Hunt Morgan proved chromosomal theory of inheritance and proposed the concept of linkage.

**Solved independently** (answer withheld)

1. NCERT: Sturtevant used the frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes and mapped their position on the chromosome, which is option $3$.

**Subtopic:** Linkage & Recombination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 43)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q104_6ffb5439_04112026.png?v=6ffb54392e40)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q104_a73857d1_04112026.png?v=a73857d162e6)

---

## Q105

Biology · botany · Transport in Plants

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The forces generated transpiration can lift a xylem-sized column of water over $130$ meters height.
- (Statement II) Transpiration cools leaf surfaces sometimes $10$ to $15$ degrees evaporative cooling.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Statement I is correct as measurements reveal that the forces generated by transpiration can create pressures sufficient to lift a xylem sized column of water up to $130$ meters high.
2. Statement II is also correct as transpiration cools leaf surfaces, sometimes $10$ to $15$ degrees, by evaporative cooling.

**Solved independently** (answer withheld)

1. Statement I: the transpiration pull is strong enough to lift a xylem-sized column of water more than $130\,\text{m}$, so it is correct.
2. Statement II: evaporative cooling from transpiration lowers leaf surface temperature, sometimes by $10$ to $15$ degrees, so it is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q105_668bc389_04112026.png?v=668bc38928e6)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q105_e92c95b5_04112026.png?v=e92c95b5ab45)

---

## Q106

Biology · botany · Mineral Nutrition

Which micronutrient is required for splitting of water molecule during photosynthesis?

- **(1)** Manganese
- (2) Molybdenum
- (3) Magnesium
- (4) Copper

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Manganese plays a major role in the splitting of water to liberate oxygen during photosynthesis.
2. Copper is essential for the overall metabolism in plants.
3. Molybdenum is included in nitrogen metabolism.
4. Magnesium activates several enzymes involved in photosynthesis and respiration.

**Solved independently** (answer withheld)

1. Photolysis of water in photosystem II requires $\mathrm{Mn}^{2+}$ (with $\mathrm{Ca}^{2+}$ and $\mathrm{Cl}^{-}$); manganese is a micronutrient, so the answer is option $1$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 44)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q106_5e4cfc84_04112026.png?v=5e4cfc844f54)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q106_248765df_04112026.png?v=248765dfe4ae)

---

## Q107

Biology · botany · Photosynthesis in Higher Plants

The reaction centre in PS II has an absorption maxima at

- **(1)** $680\,\mathrm{nm}$
- (2) $700\,\mathrm{nm}$
- (3) $660\,\mathrm{nm}$
- (4) $780\,\mathrm{nm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In PS-I, the reaction centre chlorophyll $a$ has an absorption peak at $700\,\mathrm{nm}$, while in PS-II, reaction centre has an absorption maxima at $680\,\mathrm{nm}$.

**Solved independently** (answer withheld)

1. In NCERT, the reaction centre of PS II is chlorophyll $a$ with absorption peak at $680\,\mathrm{nm}$ (P680), while PS I is P700, so the answer is option $1$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 44)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q107_c5f65dee_04112026.png?v=c5f65dee9c13)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q107_9afc95db_04112026.png?v=9afc95db2dd8)

---

## Q108

Biology · botany · Ecosystem

Identify the correct statements:
Choose the correct answer from the options given below:

- (A) Detrivores perform fragmentation.
- (B) The humus is further degraded by some microbes during mineralization.
- (C) Water soluble inorganic nutrients go down into the soil and get precipitated by a process called leaching.
- (D) The detritus food chain begins with living organisms.
- (E) Earthworms break down detritus into smaller particles by a process called catabolism.

- **(1)** A, B, C only
- (2) B, C, D only
- (3) C, D, E only
- (4) D, E, A only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The detritus food chain begins with detritus that is dead organic matter.
2. The saprotrophic bacteria and fungi breakdown detritus into simpler inorganic substances by a process called catabolism.

**Solved independently** (answer withheld)

1. A: detritivores such as earthworms break detritus into smaller particles (fragmentation), so A is true.
2. B: humus is degraded very slowly by some microbes and releases inorganic nutrients by mineralization, so B is true.
3. C: water-soluble inorganic nutrients go down into the soil horizon and get precipitated as unavailable salts by leaching, so C is true.
4. D: the detritus food chain begins with dead organic matter (detritus), not living organisms, so D is false.
5. E: earthworms breaking detritus into smaller particles is fragmentation; catabolism is enzymatic degradation by bacteria and fungi, so E is false.
6. True set is $\{A, B, C\}$, which is option $1$.

**Subtopic:** Decomposition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q108_3eeb192d_04112026.png?v=3eeb192d9fd3)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q108_e27cca84_04112026.png?v=e27cca84f268)

---

## Q109

Biology · botany · Environmental Issues

The thickness of ozone in a column of air in the atmosphere is measured in terms of :

- **(1)** Dobson units
- (2) Decibels
- (3) Decameter
- (4) Kilobase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The thickness of the ozone in a column of air from the ground to the top of the atmosphere is measured in terms of Dobson units (DU).
2. Noise is measured in decibels.

**Solved independently** (answer withheld)

1. The thickness of ozone in a column of air from the ground to the top of the atmosphere is measured in Dobson units (DU), which is option $1$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q109_7ad89623_04112026.png?v=7ad89623e663)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q109_432a7861_04112026.png?v=432a7861f031)

---

## Q110

Biology · botany · Plant Growth and Development

In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as

- (1) Differentiation
- **(2)** Dedifferentiation
- (3) Development
- (4) Senescence

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as dedifferentiation.
2. Dedifferentiation is a phenomenon by which the living differentiated plant cells, that by now have lost the capacity to divide can regain the capacity of division under certain conditions.

**Solved independently** (answer withheld)

1. Mature, differentiated mesophyll cells regain the ability to divide and form an undifferentiated mass (callus); NCERT calls this dedifferentiation, which is option $2$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 45)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q110_b3968c2f_04112026.png?v=b3968c2f348d)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q110_f02e895a_04112026.png?v=f02e895a6618)

---

## Q111

Biology · botany · Respiration in Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) ATP is used at two steps in glycolysis.
- (Reason R) First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1, 6-diphosphate.

- **(1)** Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true but R is NOT the correct explanation of A.
- (3) A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. ATP in glycolysis is used at two steps of conversion that are
2. Glucose $\rightarrow$ Glucose-6-phosphate
3. Fructose-6-phosphate $\rightarrow$ Fructose-1, 6-bisphosphate
4. The reason of the utilisation of ATP is for phosphorylation the substrates.

**Solved independently** (answer withheld)

1. Glycolysis consumes ATP at exactly two steps, so $A$ is true.
2. Step 1: glucose $\xrightarrow{ATP}$ glucose-6-phosphate; step 2: fructose-6-phosphate $\xrightarrow{ATP}$ fructose-1,6-bisphosphate, so $R$ is true.
3. $R$ names the two ATP-using steps that $A$ refers to, so $R$ correctly explains $A$: option $1$.

**Subtopic:** Glycolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q111_c6342ede_04112026.png?v=c6342eded375)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q111_ca28115f_04112026.png?v=ca28115f08c4)

---

## Q112

Biology · botany · Ecosystem

In the equation $\boxed{\mathrm{GPP} - \mathrm{R} = \mathrm{NPP}}$
GPP is Gross Primary Productivity
NPP is Net Primary Productivity
R here is ________.

- (1) Photosynthetically active radiation
- (2) Respiratory quotient
- **(3)** Respiratory loss
- (4) Reproductive allocation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A considerable amount of GPP is utilised by plants in respiration.
2. Gross primary productivity minus respiration losses (R), is the net primary productivity.
3. So $\mathrm{R}$ = Respiratory loss

**Solved independently** (answer withheld)

1. $\mathrm{NPP} = \mathrm{GPP} - \mathrm{R}$, where $\mathrm{R}$ is the respiration losses of producers, i.e. respiratory loss (option $3$).

**Subtopic:** Productivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q112_8f0d5848_04112026.png?v=8f0d5848139d)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q112_d9b20e4f_04112026.png?v=d9b20e4f9b25)

---

## Q113

Biology · botany · Biodiversity and Conservation

Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?

- **(1)** Habitat loss and fragmentation
- (2) Over exploitation for economic gain
- (3) Alien species invasions
- (4) Co-extinctions

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Habitat loss and fragmentation is the most important cause driving animals and plants to extinction.

**Solved independently** (answer withheld)

1. Of the four causes in the Evil Quartet, NCERT names habitat loss and fragmentation as the most important cause of extinction, which is option $1$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 46)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q113_49fda146_04112026.png?v=49fda146d2ef)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q113_c3c0b69d_04112026.png?v=c3c0b69d26b3)

---

## Q114

Biology · botany · Plant Growth and Development

Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period, that leads early seed production?

- (1) Indole-3-butyric Acid
- **(2)** Gibberellic Acid
- (3) Zeatin
- (4) Abscisic Acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spraying juvenile conifers with gibberellins (GAs) hastens the maturity period, thus leading to early seed production.

**Solved independently** (answer withheld)

1. NCERT states that spraying juvenile conifers with gibberellins ($GA_3$) hastens maturity and leads to early seed production, so the answer is option $2$, Gibberellic Acid.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q114_09afb718_04112026.png?v=09afb718de13)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q114_a7c34b97_04112026.png?v=a7c34b97f67c)

---

## Q115

Biology · botany · Molecular Basis of Inheritance

Unequivocal proof that DNA is the genetic material was first proposed by

- (1) Frederick Griffith
- **(2)** Alfred Hershey and Martha Chase
- (3) Avery, Macleoid and McCarthy
- (4) Wilkins and Franklin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The unequivocal proof that DNA is the genetic material came from the experiment of Alfred Hershey and Martha Chase.
2. Avery, Macleoid and McCarty gave the biochemical characterisation of Transforming Principle.
3. The transformation experiments by using Pneumococcus was conducted by Frederick Griffith.
4. Wilkins and Franklin produced X-ray diffraction data of DNA.

**Solved independently** (answer withheld)

1. Hershey and Chase (1952) grew bacteriophages with $^{32}P$ (labels DNA) and $^{35}S$ (labels protein); only $^{32}P$ entered the bacteria, giving the unequivocal proof that DNA is the genetic material, which is option $2$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 46)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q115_e7b3e314_04112026.png?v=e7b3e314c90d)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q115_ad77d25a_04112026.png?v=ad77d25ae8d5)

---

## Q116

Biology · botany · Molecular Basis of Inheritance

What is the role of RNA polymerase III in the process of transcription in Eukaryotes?

- (1) Transcription of rRNAs (28S, 18S and 5.8S)
- **(2)** Transcription of tRNA, 5S rRNA and snRNA
- (3) Transcription of precursor of mRNA
- (4) Transcription of only snRNAs

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In eukaryotes there are three major types of RNA polymerases.
2. RNA polymerase I transcribes : 5.8S, 18S, 28S rRNAs
3. RNA polymerase II transcribes : hnRNAs (precurssor of mRNA)
4. RNA polymerase III transcribes : tRNAs, ScRNA, 5S rRNA and snRNA

**Solved independently** (answer withheld)

1. In eukaryotes, RNA polymerase III transcribes tRNA, $5\,S$ rRNA and snRNAs (NCERT), which is option $2$.

**Subtopic:** Transcription · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 46)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q116_4d66eaf4_04112026.png?v=4d66eaf420a8)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q116_ff5d3cd7_04112026.png?v=ff5d3cd754c7)

---

## Q117

Biology · botany · Cell Cycle and Cell Division

Among eukaryotes, replication of DNA takes place in :

- (1) M phase
- **(2)** S phase
- (3) $\mathrm{G_1}$ phase
- (4) $\mathrm{G_2}$ phase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Replication of DNA takes place in S-phase of cell cycle in eukaryotes.
2. Most of the cell organelles duplicate in $\mathrm{G_1}$ phase.

**Solved independently** (answer withheld)

1. In the eukaryotic cell cycle, DNA synthesis (replication) happens in the $\mathrm{S}$ phase of interphase, which is option $2$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q117_ead6b21a_04112026.png?v=ead6b21ad70d)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q117_c38e9e49_04112026.png?v=c38e9e49f990)

---

## Q118

Biology · botany · Cell Cycle and Cell Division

Which of the following stages of meiosis involves division of centromere?

- (1) Metaphase I
- (2) Metaphase II
- **(3)** Anaphase II
- (4) Telophase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Splitting of centromere occurs during anaphase of mitosis or anaphase II of meiosis.
2. During Metaphase I and II, chromosomes align at the equator.
3. During telophase, chromosomes reach the respective poles.

**Solved independently** (answer withheld)

1. At anaphase II the centromere of each chromosome splits, letting sister chromatids move to opposite poles, so the answer is option $3$.

**Subtopic:** Anaphase II and Telophase II · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q118_ed160f25_04112026.png?v=ed160f255d77)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q118_a60ebb68_04112026.png?v=a60ebb680965)

---

## Q119

Biology · botany · Biodiversity and Conservation

The historic Convention on Biological Diversity, ‘The Earth Summit’ was held in Rio de Janeiro in the year

- (1) 1985
- **(2)** 1992
- (3) 1986
- (4) 2002

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The historic convention on Biological Diversity, “The Earth Summit” was held in Rio de Janeiro in the year 1992.
2. It called upon all nations to take appropriate measures for conservation of biodiversity and sustainable utilisation of its benefits.

**Solved independently** (answer withheld)

1. The historic Convention on Biological Diversity, the Earth Summit, was held in Rio de Janeiro in $1992$, which is option $2$.

**Subtopic:** How Do We Conserve Biodiversity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 47)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q119_8fc23683_04112026.png?v=8fc23683ad3e)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q119_33fea10f_04112026.png?v=33fea10f8fc8)

---

## Q120

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R: In the light of the above statements, choose the most appropriate answer from options given below:

- (Assertion A) The first stage of gametophyte in the life cycle of moss is protonema stage.
- (Reason R) Protonema develops directly from spores produced in capsule.

- **(1)** Both A and R are correct and R is the correct explanation of A
- (2) Both A and R are correct but R is NOT the correct explanation of A
- (3) A is correct but R is not correct
- (4) A is not correct but R is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The predominant stage of the life cycle of a moss is the gametophyte which consists of two stages.
2. The first stage is the protonema stage, which develops directly from a spore.
3. Capsule of the sporophyte contains spore which gives rise to protonema.
4. Thus, reason correctly explains the assertion.

**Solved independently** (answer withheld)

1. Assertion A: in moss the gametophyte begins as the creeping, green, filamentous protonema, so A is correct.
2. Reason R: the protonema develops directly from a haploid spore released from the capsule, so R is correct.
3. Since the spore germinates directly into the protonema, R explains why protonema is the first gametophyte stage, which is option $1$.

**Subtopic:** Mosses · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q120_75624a22_04112026.png?v=75624a22525d)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q120_7a2d1ea0_04112026.png?v=7a2d1ea07599)

---

## Q121

Biology · botany · Biotechnology: Principles and Processes

In gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used.

- (1) Copper
- (2) Zinc
- **(3)** Tungsten or gold
- (4) Silver

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because in gene gun method, microparticles of tungsten or gold are used.
2. Gold or tungsten are inert in nature so they do not alter the chemical composition of cells.

**Solved independently** (answer withheld)

1. In the biolistic (gene gun) method, high-velocity microparticles of gold or tungsten coated with DNA are fired into host cells, so the answer is option $3$.

**Subtopic:** Competent Host & Insertion of rDNA into Host Cell · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q121_470a79f7_04112026.png?v=470a79f76933)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q121_f17394de_04112026.png?v=f17394dea7b5)

---

## Q122

Biology · botany · Biomolecules

Cellulose does not form blue colour with Iodine because

- (1) It is a disaccharide
- (2) It is a helical molecule
- **(3)** It does not contain complex helices and hence cannot hold iodine molecules
- (4) It breaks down when iodine reacts with it

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because cellulose does not contain complex helices and hence cannot hold iodine molecules.
2. Option (1), (2) and (4) are not correct as cellulose is a polysaccharide.

**Solved independently** (answer withheld)

1. Starch forms helical secondary structures that hold $I_2$ molecules, giving blue colour; cellulose has no complex helices, so it cannot hold iodine, which is option $3$.

**Subtopic:** Polysaccharides · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q122_7f7234c1_04112026.png?v=7f7234c1d06b)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q122_fa9a8f71_04112026.png?v=fa9a8f7189c8)

---

## Q123

Biology · botany · Sexual Reproduction in Flowering Plants

What is the function of tassels in the corn cob?

- (1) To attract insects
- **(2)** To trap pollen grains
- (3) To disperse pollen grains
- (4) To protect seeds

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Tassels in the com cob represents stigma and style which wave in the wind to trap pollen grains.

**Solved independently** (answer withheld)

1. Corn tassels (silks on the cob) are the feathery stigma and style of the wind-pollinated female flowers, which wave in the wind to trap airborne pollen grains, so the answer is option $2$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q123_a9635cd9_04112026.png?v=a9635cd9c4b5)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q123_722f19f2_04112026.png?v=722f19f2fa13)

---

## Q124

Biology · botany · Morphology of Flowering Plants

Axile placentation is observed in

- (1) Mustard, Cucumber and Primrose
- (2) China rose, Beans and Lupin
- (3) Tomato, Dianthus and Pea
- **(4)** China rose, Petunia and Lemon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. China rose, Tomato, Petunia and Lemon show axile placentation.
2. Dianthus and Primrose show free central placentation.
3. Pea, Lupin and Beans show marginal placentation.
4. Cucumber and mustard show parietal placentation.

**Solved independently** (answer withheld)

1. In NCERT, axile placentation is shown by China rose, tomato and lemon, and Petunia (Solanaceae) also has axile placentation. Beans, lupin and pea are marginal, mustard and cucumber are parietal, and Dianthus and Primrose are free central, so only option $4$ lists all axile examples.

**Subtopic:** Gynoecium · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 48)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q124_6011b59f_04112026.png?v=6011b59f7668)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q124_2693b382_04112026.png?v=2693b382e911)

---

## Q125

Biology · botany · Sexual Reproduction in Flowering Plants

In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :

- (1) Synergids, Primary endosperm nucleus and zygote
- (2) Antipodals, synergids, and primary endosperm nucleus
- **(3)** Synergids, Zygote and Primary endosperm nucleus
- (4) Synergids, antipodals and Polar nuclei

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Synergids are the cells of gametophyte and hence these are haploid Zygote is formed by fusion of two gametes and thus it is diploid.
2. Primary endosperm nucleus is formed by the fusion of diploid secondary nucleus with a male gamete.
3. Therefore, it is triploid.

**Solved independently** (answer withheld)

1. Synergids are cells of the egg apparatus, formed from the haploid megaspore, so they are haploid ($n$).
2. Syngamy fuses the egg ($n$) with one male gamete ($n$): zygote $= n + n = 2n$ (diploid).
3. Triple fusion joins two polar nuclei ($n + n$) with the second male gamete ($n$): PEN $= 3n$ (triploid).
4. The order haploid, diploid, triploid is synergids, zygote, primary endosperm nucleus, which is option $3$.

**Subtopic:** Double Fertilisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q125_18011984_04112026.png?v=18011984f3dc)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q125_3109c0fa_04112026.png?v=3109c0fa2ad5)

---

## Q126

Biology · botany · Molecular Basis of Inheritance

Expressed Sequence Tags (ESTs) refers to

- **(1)** All genes that are expressed as RNA.
- (2) All genes that are expressed as proteins.
- (3) All genes whether expressed or unexpressed.
- (4) Certain important expressed genes.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. All the genes that are expressed as RNA are referred to as Expressed Sequence Tags (ESTs).

**Solved independently** (answer withheld)

1. NCERT (Human Genome Project) defines Expressed Sequence Tags as the approach that identifies all genes expressed as RNA, which is option $1$.

**Subtopic:** Human Genome Project · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q126_bacf6e43_04112026.png?v=bacf6e437fce)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q126_5ad32a54_04112026.png?v=5ad32a5449d5)

---

## Q127

Biology · botany · Morphology of Flowering Plants

Family Fabaceae differs from Solanaceae and Liliaceae. With respect to the stamens, pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae.

- **(1)** Diadelphous and Dithecous anthers
- (2) Polyadelphous and epipetalous stamens
- (3) Monoadelphous and Monothecous anthers
- (4) Epiphyllous and Dithecous anthers

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fabaceae $\rightarrow$ Diadelphous and dithecous anther.
2. Solanaceae $\rightarrow$ Polyandrous, epipetalous and dithecous anther.
3. Liliaceae $\rightarrow$ Polyandrous, epiphyllous and dithecous anther.

**Solved independently** (answer withheld)

1. Fabaceae androecium: ten stamens, diadelphous $(9)+1$, anthers dithecous; Solanaceae has epipetalous stamens and Liliaceae has epiphyllous (epitepalous) stamens, so the Fabaceae-specific feature is diadelphous with dithecous anthers, option $1$.

**Subtopic:** Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q127_c77639e1_04112026.png?v=c77639e13501)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q127_355ba734_04112026.png?v=355ba7341612)

---

## Q128

Biology · botany · Cell Cycle and Cell Division

The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?

- (1) Zygotene
- **(2)** Pachytene
- (3) Diplotene
- (4) Diakinesis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The process of recombination occurs at Pachytene stage of prophase I.
2. This stage is characterised by the appearance of recombination nodules.

**Solved independently** (answer withheld)

1. Per NCERT, during pachytene bivalents become tetrads and recombination nodules appear at the sites where crossing over occurs between non-sister chromatids of homologous chromosomes, so the answer is option $2$ (Pachytene).

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q128_f3721bbf_04112026.png?v=f3721bbf4a18)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q128_f94652a8_04112026.png?v=f94652a85e0b)

---

## Q129

Biology · botany · Plant Growth and Development

Which hormone promotes internode/petiole elongation in deep water rice?

- (1) $\mathrm{GA_3}$
- (2) Kinetin
- **(3)** Ethylene
- (4) 2, 4-D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ethylene promotes rapid internode/petiole elongation in deep water rice plants.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Plant Growth) states that ethylene promotes rapid internode/petiole elongation in deep water rice plants, so the answer is option $3$ (Ethylene).

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q129_8926b87c_04112026.png?v=8926b87c02f5)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q129_13bf7f2c_04112026.png?v=13bf7f2c89b5)

---

## Q130

Biology · botany · Biotechnology: Principles and Processes

Upon exposure to UV radiation, DNA stained with ethidium bromide will show

- (1) Bright red colour
- (2) Bright blue colour
- (3) Bright yellow colour
- **(4)** Bright orange colour

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because in recombinant DNA technology the separated DNA fragments can be visualised only after staining the DNA with a substance known as ethidium bromide followed by exposure to U.V. radiation.
2. You can see bright orange coloured bands of DNA in an ethidium bromide stained gel exposed to U.V. light.

**Solved independently** (answer withheld)

1. In gel electrophoresis, separated DNA fragments stained with ethidium bromide are viewed under UV radiation and appear as bright orange coloured bands, which is option $4$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q130_c25c3ec0_04112026.png?v=c25c3ec05f41)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q130_4ba39a79_04112026.png?v=4ba39a796d05)

---

## Q131

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body.
- (Statement II) Exarch condition is the most common feature of the root system.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is correct but Statement II is false
- **(4)** Statement I is incorrect but Statement II is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Endarch and exarch are the terms often used for describing the position of primary xylem in the plant body.
2. Primary xylem is of two types protoxylem and metaxylem.
3. On the basis of relative position of protoxylem and metaxylem in the organ the arrangement of primary xylem can be endarch or exarch.
4. Exarch type of primary xylem is seen in roots.
5. Therefore, Statement I is false and Statement II is true.

**Solved independently** (answer withheld)

1. Endarch/exarch refer to the position of protoxylem relative to metaxylem in primary xylem, not secondary xylem, so Statement I is incorrect.
2. In roots the protoxylem lies towards the periphery (exarch), so Statement II is true; this matches option $4$.

**Subtopic:** Complex Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q131_2680e3a4_04112026.png?v=2680e3a49792)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q131_d13255c6_04112026.png?v=d13255c65fc0)

---

## Q132

Biology · botany · Transport in Plants

Movement and accumulation of ions across a membrane against their concentration gradient can be explained by

- (1) Osmosis
- (2) Facilitated Diffusion
- (3) Passive Transport
- **(4)** Active Transport

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Movement and accumulation of ions across a membrane against their concentration gradient can be explained by active transport.
2. It uses energy to transport molecules from lower concentration to a higher concentration.

**Solved independently** (answer withheld)

1. Movement against a concentration gradient needs energy (ATP) and carrier proteins, which is active transport, so the answer is option $4$; facilitated diffusion, passive transport and osmosis all go down the gradient.

**Subtopic:** Uptake and Transport of Mineral Nutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q132_a06dffaf_04112026.png?v=a06dffaf4b04)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q132_36f9d753_04112026.png?v=36f9d75386c8)

---

## Q133

Biology · botany · Biotechnology: Principles and Processes

During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out

- (1) RNA
- **(2)** DNA
- (3) Histones
- (4) Polysaccharides

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer as, during isolation of the genetic material, purified DNA ultimately precipitates out after the addition of chilled ethanol.
2. Option (3) is not the answer as, proteins can be removed by treatment with proteases.
3. Option (1) is not the answer as RNA can be removed by treatment with ribonuclease.

**Solved independently** (answer withheld)

1. After treating with lysozyme/cellulase, RNase and protease to remove other macromolecules, adding chilled ethanol makes the purified DNA precipitate out as fine threads, so the answer is option $2$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q133_c531c1c5_04112026.png?v=c531c1c558c4)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q133_ff128dd7_04112026.png?v=ff128dd7ce8d)

---

## Q134

Biology · botany · Plant Kingdom

Identify the pair of heterosporous pteridophytes among the following :

- (1) Lycopodium and Selaginella
- **(2)** Selaginella and Salvinia
- (3) Psilotum and Salvinia
- (4) Equisetum and Salvinia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Selaginella and Salvinia are heterosporous pteridophytes.
2. They produces two different kind of spores.
3. Psilotum, Lycopodium and Equisetum are homosporous pteridophytes.

**Solved independently** (answer withheld)

1. NCERT names Selaginella and Salvinia as heterosporous pteridophytes (they produce microspores and megaspores), while Psilotum, Equisetum and Lycopodium are homosporous, so only option $2$ has two heterosporous genera.

**Subtopic:** Pteridophytes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q134_b1c736ba_04112026.png?v=b1c736ba8c05)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q134_090c7c2a_04112026.png?v=090c7c2a0b44)

---

## Q135

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Late wood has fewer xylary elements with narrow vessels.
- (Reason R) Cambium is less active in winters.

- **(1)** Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- (3) A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In winter, the cambium is less active and forms fewer xylary elements that have narrow vessels, and this wood is called autumn wood or late wood.

**Solved independently** (answer withheld)

1. In winter the cambium is less active, so it forms fewer xylary elements with narrow vessels (late wood); both A and R are true and R explains A, which is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 51)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q135_27d7b654_04112026.png?v=27d7b6542e9a)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q135_b341bccc_04112026.png?v=b341bccc7a16)

---

## Q136

Biology · botany · Molecular Basis of Inheritance

How many different proteins does the ribosome consist of?

- **(1)** 80
- (2) 60
- (3) 40
- (4) 20

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The ribosome consists of structural RNAs and about $80$ different proteins.

**Solved independently** (answer withheld)

1. NCERT teaches that the ribosome consists of structural RNAs and about $80$ different proteins, which is option $1$.

**Subtopic:** Translation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 51)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q136_2a1e3490_04112026.png?v=2a1e3490180e)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q136_2f83ea9e_04112026.png?v=2f83ea9e588c)

---

## Q137

Biology · botany · Respiration in Plants

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Oxidative decarboxylation | I | Citrate synthase |
| B | Glycolysis | II | Pyruvate dehydrogenase |
| C | Oxidative phosphorylation | III | Electron transport system |
| D | Tricarboxylic acid cycle | IV | EMP pathway |

- (1) A – III, B – IV, C – II, D – I
- (2) A – II, B – IV, C – I, D – III
- (3) A – III, B – I, C – II, D – IV
- **(4)** A – II, B – IV, C – III, D – I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Pyruvate, which is formed by the glycolytic catabolism of carbohydrates in the cytosol, after it enters mitochondrial matrix undergoes oxidative decarboxylation by a complex set of reactions catalyzed by pyruvate dehydrogenase.
2. The scheme of glycolysis was given by Gustav Embden, Otto Meyrhof and J. Parnas, and is often referred to as the EMP pathway.
3. In electron transport system, the energy of oxidation-reduction is utilized for the production of proton gradient required for phosphorylation, thus, this process is also called oxidative phosphorylation.
4. The TCA (tricarboxylic acid cycle) starts with the condensation of acetyl group with oxaloacetic acid (OAA) and water to yield citric acid.
5. The reaction is catalysed by the enzyme citrate synthase.
6. Thus, option (4) is correct.

**Solved independently** (answer withheld)

1. Oxidative decarboxylation of pyruvate to acetyl CoA is catalysed by pyruvate dehydrogenase, so $A \to II$.
2. Glycolysis is also called the EMP (Embden-Meyerhof-Parnas) pathway, so $B \to IV$.
3. Oxidative phosphorylation is coupled to the electron transport system, so $C \to III$.
4. The TCA cycle begins with acetyl CoA + OAA forming citrate via citrate synthase, so $D \to I$.
5. $A-II, B-IV, C-III, D-I$ matches option $4$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 51)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q137_fb143c84_04112026.png?v=fb143c8419fe)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q137_c73f63c6_04112026.png?v=c73f63c6262b)

---

## Q138

Biology · botany · Transport in Plants

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Cohesion | I | More attraction in liquid phase |
| B | Adhesion | II | Mutual attraction among water molecules |
| C | Surface tension | III | Water loss in liquid phase |
| D | Guttation | IV | Attraction towards polar surfaces |

- **(1)** A – II, B – IV, C – I, D – III
- (2) A – IV, B – III, C – II, D – I
- (3) A – III, B – I, C – IV, D – II
- (4) A – II, B – I, C – IV, D – III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cohesion represents mutual attraction between water molecules.
2. Adhesion represents attraction of water molecules to polar surfaces
3. Surface tension represents water molecules are attracted to each other in the liquid phase more than to water in the gas phase.
4. Guttation represent loss of water in liquid phase.
5. Thus, option (1) is correct.

**Solved independently** (answer withheld)

1. Cohesion is the mutual attraction among water molecules, so $A \rightarrow II$.
2. Adhesion is the attraction of water molecules to polar surfaces, so $B \rightarrow IV$.
3. Surface tension arises because water molecules are more attracted to each other in the liquid phase than in the gas phase, so $C \rightarrow I$.
4. Guttation is the loss of water in liquid form (from hydathodes), so $D \rightarrow III$.
5. $A-II,\ B-IV,\ C-I,\ D-III$ matches option $1$.

**Subtopic:** Transpiration and Stomatal Opening and Closing, Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q138_f36b7b7b_04112026.png?v=f36b7b7b6696)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q138_b2a4da87_04112026.png?v=b2a4da87abe2)

---

## Q139

Biology · botany · Organisms and Populations

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Gause’s ‘Competitive Exclusion Principle’ states that two closely related species competing for the same resources cannot co-exist indefinitely and competitively inferior one will be eliminated eventually.
- (Statement II) In general, carnivores are more adversely affected by competition than herbivores.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- **(3)** Statement I is correct but Statement II is false.
- (4) Statement I is incorrect but Statement II is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Gause's 'Competitive Exclusion Principle' states that two closely related species competing for the same resources cannot co-exist indefinitely and the competitively inferior one will be eliminated eventaully.
2. Thus, statement I is correct.
3. Statement II is incorrect as in general, herbivores and plants appear to be more adversely affected by competition than carnivores.

**Solved independently** (answer withheld)

1. Statement I: Gause's Competitive Exclusion Principle says two closely related species competing for the same resources cannot co-exist indefinitely and the competitively inferior one is eliminated, so Statement I is correct.
2. Statement II: in general, herbivores are more adversely affected by competition than carnivores, so Statement II is false.
3. Statement I correct and Statement II false matches option $3$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q139_06a3ce08_04112026.png?v=06a3ce08c466)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q139_b9151522_04112026.png?v=b9151522ef2b)

---

## Q140

Biology · botany · Cell Cycle and Cell Division

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | M Phase | I | Proteins are synthesized |
| B | $\mathrm{G_2}$ Phase | II | Inactive phase |
| C | Quiescent stage | III | Interval between mitosis and initiation of DNA replication |
| D | $\mathrm{G_1}$ Phase | IV | Equational division |

- (1) A-III, B-II, C-IV, D-I
- (2) A-IV, B-II, C-I, D-III
- **(3)** A-IV, B-I, C-II, D-III
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. M phase or mitosis is the phase where the actual cell division occurs. Mitosis is also called equational division.
2. During $\mathrm{G_2}$ phase DNA synthesis stops but cell synthesis RNA, proteins, etc. for next phase.
3. Quiescent stage is inactive phase in which non-dividing cells enters.
4. $\mathrm{G_1}$ phase is the interval between mitosis and initiation of DNA replication.
5. Therefore, option (3) is correct.

**Solved independently** (answer withheld)

1. M phase (mitosis) is the equational division, so A-IV.
2. In $\mathrm{G_2}$ phase proteins are synthesised in preparation for mitosis, so B-I.
3. The quiescent stage ($\mathrm{G_0}$) is an inactive phase, so C-II.
4. $\mathrm{G_1}$ phase is the interval between mitosis and the initiation of DNA replication, so D-III.
5. A-IV, B-I, C-II, D-III matches option $3$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 53)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q140_576ee1e1_04112026.png?v=576ee1e14a0a)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q140_844fa024_04112026.png?v=844fa024b893)

---

## Q141

Biology · botany · Environmental Issues

Which one of the following statements is NOT correct?

- (1) The micro-organisms involved in biodegradation of organic matter in a sewage polluted water body consume a lot of oxygen causing the death of aquatic organisms
- **(2)** Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries
- (3) Water hyacinth grows abundantly in eutrophic water bodies and leads to an imbalance in the ecosystem dynamics of the water body
- (4) The amount of some toxic substances of industrial waste water increases in the organisms at successive trophic levels

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Algal bloom imparts a distinct colour to the water bodies.
2. It causes deterioration of the water quantity and fish mortality.

**Solved independently** (answer withheld)

1. Algal blooms from nutrient enrichment deteriorate water quality, deplete dissolved oxygen and cause fish mortality, so statement $1$ is NOT correct.
2. Water hyacinth thriving in eutrophic water and upsetting ecosystem balance (statement $2$), biomagnification of toxic industrial substances along trophic levels (statement $3$), and high oxygen use by sewage-degrading microbes killing aquatic life (statement $4$) are all correct, so the answer is option $2$.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q141_ba29df9c_04112026.png?v=ba29df9ccd93)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q141_95a3ca70_04112026.png?v=95a3ca708019)

---

## Q142

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) In gymnosperms the pollen grains are released from the microsporangium and carried by air currents.
- (Reason R) Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed.

- (1) Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the current explanation of A
- **(3)** A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Assertion is correct but reason is false as in gymnosperms the pollen grains are released from the microsporangium and they are carried in air currents.
2. They come in contact with the opening of the ovules borne on megasporophylls.
3. The pollen tube carrying the male gametes grows towards archegonia in the ovules and discharge their contents near the mouth of the archegonia.

**Solved independently** (answer withheld)

1. Assertion A: in gymnosperms pollen grains are released from the microsporangium and carried by air currents, so A is true.
2. Reason R: pollen grains reach the micropyle of the ovule and form a pollen tube that carries the male gametes towards the archegonia, so the claim that no pollen tube is formed is false.
3. A true and R false matches option $3$.

**Subtopic:** Gymnosperms · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 53)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q142_a613fccf_04112026.png?v=a613fccf2611)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q142_c0f36c05_04112026.png?v=c0f36c05f983)

---

## Q143

Biology · botany · Photosynthesis in Higher Plants

Which of the following combinations is required for chemiosmosis?

- **(1)** Membrane, proton pump, proton gradient, ATP synthase
- (2) Membrane, proton pump, proton gradient, NADP synthase
- (3) Proton pump, electron gradient, ATP synthase
- (4) Proton pump, electron gradient, NADP synthase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient and ATP synthase.

**Solved independently** (answer withheld)

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient across the membrane and ATP synthase through which protons flow to make ATP, which is option $1$.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q143_0dd405ae_04112026.png?v=0dd405ae0a42)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q143_0d74faf0_04112026.png?v=0d74faf0a42d)

---

## Q144

Biology · botany · Biotechnology: Principles and Processes

Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence.

Choose the correct answer from the options given below :

- (A) Insertion of recombinant DNA into the host cell
- (B) Cutting of DNA at specific location by restriction enzyme
- (C) Isolation of desired DNA fragment
- (D) Amplification of gene of interest using PCR

- **(1)** B, C, D, A
- (2) C, A, B, D
- (3) C, B, D, A
- (4) B, D, A, C

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) because recombinant DNA technology involves several steps in specific sequence such as isolation of DNA, fragmentation of DNA by restriction endonucleases, isolation of desired DNA fragment, ligation of the DNA fragment into a vector, transferring the recombinant DNA into the host, culturing the host cells in a medium at large scale and extraction of the desired product.

**Solved independently** (answer withheld)

1. Genomic DNA is first cut at specific locations by a restriction enzyme: step $B$.
2. The desired DNA fragment is then separated and isolated (e.g. by gel electrophoresis): step $C$.
3. The gene of interest is amplified using PCR: step $D$.
4. The recombinant DNA is finally inserted into the host cell: step $A$.
5. Sequence $B \to C \to D \to A$ matches option $1$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 54)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q144_490f2d05_04112026.png?v=490f2d059587)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q144_d9bfa494_04112026.png?v=d9bfa494ee48)

---

## Q145

Biology · botany · Morphology of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem.
- (Reason R) Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves.

- **(1)** Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- (3) A is true but R is false
- (4) A is false but R is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A flower is a modified shoot wherein the shoot apical meristem changes to floral meristem.
2. Internodes do not elongate and the axis gets condensed.
3. The apex produces different kinds of floral appendages laterally at the successive nodes instead of leaves.
4. Therefore, both A and R are true and R is correct explanation of A.

**Solved independently** (answer withheld)

1. Assertion A matches the NCERT definition: the flower is a modified shoot in which the shoot apical meristem changes to a floral meristem, so A is true.
2. Reason R is true: internodes do not elongate, the axis condenses, and floral appendages form laterally at successive nodes instead of leaves.
3. R describes how the shoot is modified into a flower, so R explains A, which is option $1$.

**Subtopic:** The Flower · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 54)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q145_74500774_04112026.png?v=745007746907)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q145_c83d1854_04112026.png?v=c83d1854fdf9)

---

## Q146

Biology · botany · Mineral Nutrition

Match List I with List II:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Iron | I | Synthesis of auxin |
| B | Zinc | II | Component of nitrate reductase |
| C | Boron | III | Activator of catalase |
| D | Molybdenum | IV | Cell elongation and differentiation |

- (1) A-III, B-II, C-I, D-IV
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Iron activates catalase enzyme.
2. Zinc is needed in the synthesis of auxin.
3. Boron is required for cell elongation and cell differentiation.
4. Molybdenum is component of nitrogenase and nitrate reductase enzyme.
5. Therefore, option (3) is correct.

**Solved independently** (answer withheld)

1. Iron (A) is an activator of catalase, so $A \rightarrow III$.
2. Zinc (B) is needed for the synthesis of auxin, so $B \rightarrow I$.
3. Boron (C) is required for cell elongation and differentiation, so $C \rightarrow IV$.
4. Molybdenum (D) is a component of nitrate reductase, so $D \rightarrow II$.
5. $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ matches option $3$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q146_b1318ed6_04112026.png?v=b1318ed6fa26)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q146_6f6ab38d_04112026.png?v=6f6ab38d7d76)

---

## Q147

Biology · botany · Anatomy of Flowering Plants

Identify the correct statements:

Choose the correct answer from the options given below:

- (A) Lenticels are the lens-shaped openings permitting the exchange of gases.
- (B) Bark formed early in the season is called hard bark.
- (C) Bark is a technical term that refers to all tissues exterior to vascular cambium.
- (D) Bark refers to periderm and secondary phloem.
- (E) Phellogen is single-layered in thickness.

- (1) B, C and E only
- **(2)** A and D only
- (3) A, B and D only
- (4) B and C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Lenticels are lens shaped opening permitting exchange of gases between the outer atmosphere and internal tissue of the stem.
2. Bark that is formed early in the season is called early or soft bark. Towards the end of the season late or hard bark is formed.
3. Bark is non-technical term that refer to all tissues exterior to vascular cambium.
4. Bark refers to a number of tissue types, viz periderm and secondary phloem.
5. Phellogen is couple of layers thick
6. Therefore, only statement A and D are correct.

**Solved independently** (answer withheld)

1. A: lenticels are lens-shaped openings in the periderm that permit gas exchange, so $A$ is true.
2. B: bark formed early in the season is soft (early) bark, not hard bark, so $B$ is false.
3. C: bark is a non-technical term for all tissues exterior to the vascular cambium, so calling it a technical term makes $C$ false.
4. D: bark includes the periderm and the secondary phloem, so $D$ is true.
5. E: phellogen is a couple of layers thick, not single-layered, so $E$ is false.
6. True statements are $A$ and $D$ only, which is option $2$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 55)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q147_2f95deca_04112026.png?v=2f95deca6556)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q147_6cf6e78b_04112026.png?v=6cf6e78b676b)

---

## Q148

Biology · botany · Principles of Inheritance and Variation

Which of the following statements are correct about Klinefelter’s Syndrome? Choose the correct answer from the options given below:

- (A) This disorder was first described by Langdon Down (1866).
- (B) Such an individual has overall masculine development. However, the feminine developement is also expressed.
- (C) The affected individual is short statured.
- (D) Physical, psychomotor and mental development is retarded.
- (E) Such individuals are sterile.

- (1) A and B only
- (2) C and D only
- **(3)** B and E only
- (4) A and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Klinefelter's syndrome is caused due to the presence of an additional copy of X-chromosome resulting into a karyotype of $47,\ \mathrm{XXY}$.
2. Such an individual has overall masculine development, however, the feminine development is also expressed.
3. Such individuals are sterile.
4. Thus, statement B and E are correct regarding Klinefelter's syndrome.
5. Statement A, C and D are incorrect w.r.t. Klinefelter’s syndrome as they are associated with Down’s syndrome.

**Solved independently** (answer withheld)

1. A is false: Langdon Down (1866) described Down's syndrome, not Klinefelter's syndrome.
2. B is true: a $47,XXY$ individual has overall masculine development but also feminine traits such as gynaecomastia.
3. C is false: short stature is a feature of Down's syndrome; Klinefelter's individuals are not short statured.
4. D is false: retarded physical, psychomotor and mental development is described for Down's syndrome.
5. E is true: Klinefelter's individuals are sterile.
6. Correct statements are B and E only, which is option $3$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q148_73552012_04112026.png?v=735520127dd0)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q148_e8971502_04112026.png?v=e8971502483a)

---

## Q149

Biology · botany · Biomolecules

Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of

- **(1)** Succinic dehydrogenase
- (2) Amylase
- (3) Lipase
- (4) Dinitrogenase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is correct answer of this question because malonate is a competitive inhibitor of enzyme succinate dehydrogenase.
2. Inhibition of succinic dehydrogenase by malonate occurs due to close resemblance of malonate with substrate succinate in structure.
3. Competitive inhibitors are often used in the control of bacterial pathogens.

**Solved independently** (answer withheld)

1. Malonate resembles succinate in structure, so it binds the active site of succinic dehydrogenase as a competitive inhibitor; this is option $1$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q149_6fa72b86_04112026.png?v=6fa72b863938)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q149_caa9501a_04112026.png?v=caa9501a7233)

---

## Q150

Biology · botany · Organisms and Populations

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
|  | (Interaction) |  | (Species A and B) |
| A | Mutualism | I | $+(\mathrm{A}),\ 0(\mathrm{B})$ |
| B | Commensalism | II | $-(\mathrm{A}),\ 0(\mathrm{B})$ |
| C | Amensalism | III | $+(\mathrm{A}),\ -(\mathrm{B})$ |
| D | Parasitism | IV | $+(\mathrm{A}),\ +(\mathrm{B})$ |

- (1) A-IV, B-II, C-I, D-III
- **(2)** A-IV, B-I, C-II, D-III
- (3) A-IV, B-III, C-I, D-II
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $(+,\ +)$ Mutualism : In this interaction, both the interacting species are benefitted.
2. $(+,\ 0)$ Commensalism : Only one species is benefitted and the other species remains unharmed.
3. $(-,\ 0)$ Amensalism : Neither species is benefitted. One remains unharmed and the other is harmed.
4. $(+,\ -)$ Parasitism : One species is benefitted and other is negatively effected.

**Solved independently** (answer withheld)

1. Mutualism benefits both species: $+(A), +(B)$, so A-IV.
2. Commensalism benefits one and leaves the other unaffected: $+(A), 0(B)$, so B-I.
3. Amensalism harms one and leaves the other unaffected: $-(A), 0(B)$, so C-II.
4. Parasitism benefits the parasite and harms the host: $+(A), -(B)$, so D-III.
5. A-IV, B-I, C-II, D-III is option $2$.

**Subtopic:** Population Interactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q150_8cecc777_04112026.png?v=8cecc777c91c)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q150_b75bd189_04112026.png?v=b75bd1898d7f)

---

## Q151

Biology · zoology · Reproductive Health

Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?

- (1) Genital herpes
- **(2)** Gonorrhoea
- (3) Hepatitis-B
- (4) HIV Infection

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) because except for hepatitis-B, genital herpes and HIV infection other STIs are completely curable if detected early and treated properly.
2. Gonorrhoea is a bacterial disease which can be treated and cured completely, other diseases mentioned are viral diseases.

**Solved independently** (answer withheld)

1. NCERT states that, except for hepatitis-B, genital herpes and HIV infection, the other STDs are completely curable if detected early and treated properly, so gonorrhoea (option $2$) is the answer.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q151_eff781e3_04112026.png?v=eff781e3f10e)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q151_90a6604e_04112026.png?v=90a6604e4c35)

---

## Q152

Biology · zoology · Human Reproduction

Which of the following statements are correct regarding female reproductive cycle? Choose the most appropriate answer from the options given below.

- (A) In non-primate mammals cyclical changes during reproduction are called oestrus cycle.
- (B) First menstrual cycle begins at puberty and is called menopause.
- (C) Lack of menstruation may be indicative of pregnancy.
- (D) Cyclic menstruation extends between menarche and menopause.

- (1) A and D only
- (2) A and B only
- (3) A, B and C only
- **(4)** A, C and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as first menstrual cycle that begins at puberty is called menarche.
2. Cyclic menstruation is an indicator of normal reproductive phase and extends between menarche and menopause.
3. In primates, cyclical changes during reproduction are called menstrual cycle.

**Solved independently** (answer withheld)

1. Statement A: in non-primate mammals the reproductive cyclical changes are called the oestrus cycle, so $A$ is true.
2. Statement B: the first menstruation at puberty is called menarche, not menopause, so $B$ is false.
3. Statement C: lack of menstruation may indicate pregnancy, so $C$ is true.
4. Statement D: cyclic menstruation extends between menarche and menopause, so $D$ is true.
5. True set is $\{A, C, D\}$, which matches option $4$ (A, C and D only).

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 57)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q152_809406ea_04112026.png?v=809406ea719d)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q152_918bac92_04112026.png?v=918bac92f1db)

---

## Q153

Biology · zoology · Reproductive Health

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Vasectomy | I | Oral method |
| B | Coitus interruptus | II | Barrier method |
| C | Cervical caps | III | Surgical method |
| D | Saheli | IV | Natural method |

- (1) A-III, B-I, C-IV, D-II
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-II, B-III, C-I, D-IV
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because
2. (i) Vasectomy is a surgical method of contraception
3. (ii) Coitus interruptus is a natural method of contraception
4. (iii) Cervical cap is a barrier method of contraception
5. (iv) Saheli is an oral method of contraception which is a non-steroidal pill

**Solved independently** (answer withheld)

1. Vasectomy (A) is a surgical sterilisation method, so $A \rightarrow III$.
2. Coitus interruptus (B) is a natural method, so $B \rightarrow IV$.
3. Cervical caps (C) are a barrier method, so $C \rightarrow II$.
4. Saheli (D) is a once-a-week oral contraceptive pill, so $D \rightarrow I$.
5. $A$-III, $B$-IV, $C$-II, $D$-I matches option $2$.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 57)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q153_72420994_04112026.png?v=72420994f54e)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q153_4f3a05da_04112026.png?v=4f3a05da7c7d)

---

## Q154

Biology · zoology · Reproductive Health

Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below.

- (Assertion A) Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme.
- (Reason R) Ban on amniocentesis checks increasing menace of female foeticide.

- (1) Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true and R is NOT the correct explanation of A.
- (3) A is true but R is false.
- **(4)** A is false but R is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as ‘Reproductive and Child Health Care (RCH) programme’ deals with creating awareness among people about various reproduction related aspects and providing facilities and support for building up a reproductively healthy society.
2. Amniocentesis is basically used to test for the presence of certain genetic disorders such as Down’s syndrome, haemophilia, etc., to determine the survivability of the foetus.
3. Amniocentesis is not a sex determination technique in India and is not a strategy of RCH.

**Solved independently** (answer withheld)

1. Under the RCH programme, one strategy is the statutory ban on amniocentesis for sex determination, so using amniocentesis for sex determination is not a strategy: Assertion $A$ is false.
2. The ban on amniocentesis for sex determination is meant to check the rising menace of female foeticide, so Reason $R$ is true.
3. $A$ false and $R$ true matches option $4$.

**Subtopic:** Reproductive Health – Problems and Strategies, MTP and Amniocentesis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q154_2861ed02_04112026.png?v=2861ed02fbc8)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q154_f7ddc59f_04112026.png?v=f7ddc59fcd0b)

---

## Q155

Biology · zoology · Cell: The Unit of Life

Which of the following are NOT considered as the part of endomembrane system? Choose the most appropriate answer from the options given below:

- (A) Mitochondria
- (B) Endoplasmic reticulum
- (C) Chloroplasts
- (D) Golgi complex
- (E) Peroxisomes

- (1) B and D only
- **(2)** A, C and E only
- (3) A and D only
- (4) A, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The endomembrane system include endoplasmic reticulum (ER), golgi complex, lysosomes and vacuoles.
2. Since the functions of the mitochondria, chloroplast and peroxisomes are not coordinated with the above components, these are not considered as part of endomembrane system.

**Solved independently** (answer withheld)

1. Per NCERT, the endomembrane system comprises the endoplasmic reticulum, Golgi complex, lysosomes and vacuoles, whose functions are coordinated; mitochondria, chloroplasts and peroxisomes are not included, so the answer is A, C and E only, option $2$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 58)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q155_9e26873d_04112026.png?v=9e26873d5955)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q155_96bd5157_12112026.png?v=96bd51579971)

---

## Q156

Biology · zoology · Breathing and Exchange of Gases

Vital capacity of lung is _________.

- (1) $\mathrm{IRV} + \mathrm{ERV}$
- (2) $\mathrm{IRV} + \mathrm{ERV} + \mathrm{TV} + \mathrm{RV}$
- (3) $\mathrm{IRV} + \mathrm{ERV} + \mathrm{TV} - \mathrm{RV}$
- **(4)** $\mathrm{IRV} + \mathrm{ERV} + \mathrm{TV}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because vital capacity is the maximum volume of air a person can breathe in after forced expiration.
2. This includes $\mathrm{ERV}$, $\mathrm{TV}$ and $\mathrm{IRV}$.

**Solved independently** (answer withheld)

1. Vital capacity is the maximum volume of air a person can breathe out after a forced inspiration, $\mathrm{VC} = \mathrm{IRV} + \mathrm{TV} + \mathrm{ERV}$, which is option $4$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 58)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q156_4060a92e_04112026.png?v=4060a92e6f9e)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q156_e4cfaed6_04112026.png?v=e4cfaed68c24)

---

## Q157

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Gene ‘a’ | I | $\beta$-galactosidase |
| B | Gene ‘y’ | II | Transacetylase |
| C | Gene ‘i’ | III | Permease |
| D | Gene ‘z’ | IV | Repressor protein |

- (1) A-II, B-I, C-IV, D-III
- **(2)** A-II, B-III, C-IV, D-I
- (3) A-III, B-IV, C-I, D-II
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In a lac operon,
2. Gene a codes for enzyme transacetylase.
3. Gene y codes for enzyme permease.
4. Gene i codes for repressor protein
5. Gene z codes for enzyme $\beta$-galactosidase.

**Solved independently** (answer withheld)

1. In the lac operon, gene $a$ codes for transacetylase, so A-II; gene $y$ codes for permease, so B-III; gene $i$ codes for the repressor protein, so C-IV; gene $z$ codes for $\beta$-galactosidase, so D-I. This is option $2$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q157_11bc8246_04112026.png?v=11bc82462324)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q157_f3e6fdd6_04112026.png?v=f3e6fdd69997)

---

## Q158

Biology · zoology · Chemical Coordination and Integration

Match List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | CCK | I | Kidney |
| B | GIP | II | Heart |
| C | ANF | III | Gastric gland |
| D | ADH | IV | Pancreas |

- **(1)** A-IV, B-III, C-II, D-I
- (2) A-III, B-II, C-IV, D-I
- (3) A-II, B-IV, C-I, D-III
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as
2. Cholecystokinin (CCK) acts on both gall bladder and pancreas and stimulates the secretion of bile juice and pancreatic enzymes respectively.
3. GIP inhibits gastric secretion and motility.
4. Atrial Natriuretic Factor (ANF) is released from the atrial wall of our heart.
5. Anti-diuretic hormone (ADH) acts mainly on the kidney and stimulates resorption of water and electrolytes by the distal tubules.

**Solved independently** (answer withheld)

1. CCK acts on the pancreas (pancreatic enzyme secretion) and gall bladder, so $A \to IV$.
2. GIP inhibits gastric secretion and motility, so it relates to the gastric gland: $B \to III$.
3. ANF is secreted by the atrial wall of the heart: $C \to II$.
4. ADH acts on the distal tubules of the kidney: $D \to I$.
5. $A-IV, B-III, C-II, D-I$ is option $1$.

**Subtopic:** Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 59)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q158_0029dcd0_04112026.png?v=0029dcd0df65)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q158_1231d982_04112026.png?v=1231d982bdad)

---

## Q159

Biology · zoology · Organisms and Populations

Match List I with List II.
List I (Interacting species) | List II (Name of interaction)
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | A Leopard and a Lion in a forest/grassland | I | Competition |
| B | A Cuckoo laying egg in a Crow’s nest | II | Brood parasitism |
| C | Fungi and root of a higher plant in Mycorrhizae | III | Mutualism |
| D | A cattle egret and a Cattle in a field | IV | Commensalism |

- **(1)** A-I, B-II, C-III, D-IV
- (2) A-I, B-II, C-IV, D-III
- (3) A-III, B-IV, C-I, D-II
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A leopard and a lion in a forest/grassland exemplify competition where both the species are competing for the same resources.
2. A cuckoo laying egg in a crow’s nest is brood parasitism where cuckoo is the parasitic bird that lays its egg in the nest of crow (host bird).
3. Fungi and root of a higher plant in mycorrhizae exemplify mutualism where both the species are benefitted.
4. The fungi help the plant in the absorption of essential nutrients from the soil while the plant in turn provides the fungi with energy yielding carbohydrates.
5. A cattle egret and a cattle in a field exemplify commensalism where one species benefits and the other remains unaffected.
6. The egrets always forage close to where cattle are grazing because the cattle, as they move, stir up and flush out insects from the vegetation that otherwise might be difficult for the egrets to find and catch.

**Solved independently** (answer withheld)

1. A leopard and a lion share prey in the same habitat, so A is competition: $A \to I$.
2. A cuckoo lays its eggs in a crow's nest for the host to incubate, so B is brood parasitism: $B \to II$.
3. In mycorrhizae the fungus and the plant root both benefit, so C is mutualism: $C \to III$.
4. The cattle egret feeds on insects stirred up by grazing cattle and the cattle are unaffected, so D is commensalism: $D \to IV$.
5. $A-I, B-II, C-III, D-IV$ matches option $1$.

**Subtopic:** Mutualism, Commensalism and Ammensalism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q159_b4b8d294_04112026.png?v=b4b8d2947ed5)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q159_1678e4e3_04112026.png?v=1678e4e3cd30)

---

## Q160

Biology · zoology · Biomolecules

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.
- (Statement II) When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor.

- **(1)** Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is true but Statement II is false.
- (4) Statement I is false but Statement II is true.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.
2. Competitive inhibitor due to its close structural similarity with the substrate, competes with the substrate for the substrate-binding site of the enzyme.

**Solved independently** (answer withheld)

1. Statement I: low temperature keeps an enzyme temporarily inactive, while high temperature denatures the protein and destroys its activity, so Statement I is true.
2. Statement II: an inhibitor that closely resembles the substrate in molecular structure and inhibits the enzyme is a competitive inhibitor, so Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q160_15d12a23_04112026.png?v=15d12a234479)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q160_6d82876d_04112026.png?v=6d82876d8e35)

---

## Q161

Biology · zoology · Evolution

Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.

- (1) Tasmanian wolf, Bobcat, Marsupial mole
- **(2)** Numbat, Spotted cuscus, Flying phalanger
- (3) Mole, Flying squirrel, Tasmanian tiger cat
- (4) Lemur, Anteater, Wolf

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because numbat, spotted cuscus and flying phalanger are Australian marsupials exhibiting adaptive radiation.
2. Option (3) is incorrect because mole and flying squirrel are placental mammals.
3. Option (4) is incorrect because lemur and wolf are placental mammals.
4. Option (1) is incorrect because bobcat is a placental mammal.

**Solved independently** (answer withheld)

1. Numbat, spotted cuscus and flying phalanger are all Australian marsupials from the adaptive radiation; options 3, 4 and 1 each include placental mammals (mole, flying squirrel, lemur, anteater, wolf, bobcat), so the answer is option $2$.

**Subtopic:** What is Adaptive Radiation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q161_8dacdc7e_04112026.png?v=8dacdc7e768d)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q161_38cee1ae_04112026.png?v=38cee1aed4a5)

---

## Q162

Biology · zoology · Digestion and Absorption

Match List I with List II
List I (Cells) List II (Secretion)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Peptic cells | I | Mucus |
| B | Goblet cells | II | Bile juice |
| C | Oxyntic cells | III | Proenzyme pepsinogen |
| D | Hepatic cells | IV | $\mathrm{HCl}$ and intrinsic factor for absorption of vitamin $\mathrm{B_{12}}$ |

- (1) A-IV, B-III, C-II, D-I
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because gastric glands have three major types of cells namely
2. (i) Mucus neck cells which secrete mucus
3. (ii) Peptic or chief cells which secrete the proenzyme pepsinogen
4. (iii) Parietal or oxyntic cells which secrete $\mathrm{HCl}$ and intrinsic factor for absorption of vitamin $\mathrm{B_{12}}$.

**Solved independently** (answer withheld)

1. Peptic (chief) cells secrete the proenzyme pepsinogen: $A \rightarrow III$.
2. Goblet cells secrete mucus: $B \rightarrow I$.
3. Oxyntic (parietal) cells secrete HCl and intrinsic factor for vitamin $B_{12}$ absorption: $C \rightarrow IV$.
4. Hepatic cells secrete bile juice: $D \rightarrow II$.
5. The match $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ is option $3$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 60)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q162_e9a2f558_04112026.png?v=e9a2f5588f15)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q162_a97355fd_04112026.png?v=a97355fd7fa4)

---

## Q163

Biology · zoology · Biotechnology and Its Applications

Which one of the following techniques does not serve the purpose of early diagnosis of a disease for its early treatment?

- (1) Recombinant DNA Technology
- **(2)** Serum and Urine analysis
- (3) Polymerase Chain Reaction (PCR) technique
- (4) Enzyme Linked Immuno-Sorbent Assay (ELISA) technique

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) because using conventional methods of diagnosis like serum and urine analysis, etc, do not help in early diagnosis.
2. Recombinant DNA technology, Polymerase Chain Reaction [PCR] and Enzyme Linked Immuno-Sorbent Assay (ELISA) are some of the techniques that serve the purpose of early diagnosis.

**Solved independently** (answer withheld)

1. Conventional methods of diagnosis (serum and urine analysis) detect a pathogen only after symptoms appear, when its concentration is already high, so they do not give early detection; Recombinant DNA technology, PCR and ELISA do give early diagnosis, so the answer is option $2$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 61)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q163_506b6e8f_04112026.png?v=506b6e8f2522)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q163_5452748c_04112026.png?v=5452748c14c8)

---

## Q164

Biology · zoology · Neural Control and Coordination

Match List I with List II with respect to human eye. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Fovea | I | Visible coloured portion of eye that regulates diameter of pupil. |
| B | Iris | II | External layer of eye formed of dense connective tissue. |
| C | Blind spot | III | Point of greatest visual acuity or resolution. |
| D | Sclera | IV | Point where optic nerve leaves the eyeball and photoreceptor cells are absent. |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-IV, B-III, C-II, D-I
- (3) A-I, B-IV, C-III, D-II
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because
2. (i) Fovea is the point of greatest visual acuity or resolution.
3. (ii) Iris is the visible coloured portion of the eye that regulates diameter of pupil.
4. (iii) Blind spot is the point where optic nerve leaves the eye-ball and photoreceptor cells are absent.
5. (iv) Sclera is the external layer of eye formed of dense connective tissue.

**Solved independently** (answer withheld)

1. Fovea is the point of greatest visual acuity: $A \to III$.
2. Iris is the visible coloured portion that regulates pupil diameter: $B \to I$.
3. Blind spot is where the optic nerve leaves the eyeball and photoreceptors are absent: $C \to IV$.
4. Sclera is the external layer of dense connective tissue: $D \to II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $1$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q164_58990e22_04112026.png?v=58990e22227e)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q164_7d5d53fc_04112026.png?v=7d5d53fc1ed8)

---

## Q165

Biology · zoology · Cell: The Unit of Life

Which of the following functions is carried out by cytoskeleton in a cell?

- (1) Nuclear division
- (2) Protein synthesis
- **(3)** Motility
- (4) Transportation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. An elaborate network of filamentous proteinaceous structures consisting of microtubules, microfilaments and intermediate filaments present in cytoplasm is collectively referred to as the cytoskeleton.
2. It is involved in many functions such as mechanical support, motility, maintenance of the shape of the cell.

**Solved independently** (answer withheld)

1. NCERT lists the cytoskeleton's functions as mechanical support, motility and maintenance of cell shape, so the answer is option $3$ (Motility).

**Subtopic:** Cytoskeleton · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 61)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q165_cf15fb22_04112026.png?v=cf15fb22ef7b)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q165_d560becf_04112026.png?v=d560becfae3f)

---

## Q166

Biology · zoology · Principles of Inheritance and Variation

Broad palm with single palm crease is visible in a person suffering from-

- **(1)** Down’s syndrome
- (2) Turner’s syndrome
- (3) Klinefelter’s syndrome
- (4) Thalassemia

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Down’s syndrome is caused by an additional copy of chromosome number $21$. Its symptoms include–
2. a. Broad palm with characteristic palm crease
3. b. Short statured with small round head
4. c. Furrowed tongue and partially open mouth, etc.

**Solved independently** (answer withheld)

1. Per NCERT, Down's syndrome (trisomy of chromosome $21$) shows a broad palm with a characteristic single palm crease, so the answer is option $1$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q166_4d1df841_04112026.png?v=4d1df8417c5e)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q166_d0ada1d9_12112026.png?v=d0ada1d9061a)

---

## Q167

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid.
- (Statement II) In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is correct but Statement II is false.
- **(4)** Statement I is incorrect but Statement II is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In prokaryotes, the negatively charged DNA is held with some positively charged proteins in a region termed as nucleoid.
2. In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form a structure called nucleosome.

**Solved independently** (answer withheld)

1. DNA is negatively charged because of its phosphate groups, so the phrase 'positively charged DNA' in Statement I is wrong; in prokaryotes the DNA is held by positively charged proteins in the nucleoid. Statement I is incorrect.
2. In eukaryotes, the negatively charged DNA wraps around a positively charged histone octamer to form the nucleosome. Statement II is true.
3. Statement I incorrect and Statement II true is option $4$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q167_36b153c4_04112026.png?v=36b153c48b4b)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q167_474e2063_04112026.png?v=474e20638283)

---

## Q168

Biology · zoology · Human Health and Disease

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Heroin | I | Effect on cardiovascular system |
| B | Marijuana | II | Slow down body function |
| C | Cocaine | III | Painkiller |
| D | Morphine | IV | Interfere with transport of dopamine |

- **(1)** A-II, B-I, C-IV, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as
2. Heroin belongs to the category of opioids and it is a depressant that slows down body functions.
3. Marijuana is known for its effect on the cardiovascular system of the body.
4. Cocaine interferes with the transport of the neurotransmitter dopamine.
5. Morphine is used is a sedative and painkiller.

**Solved independently** (answer withheld)

1. Heroin (smack) is a depressant and slows down body functions: $A \rightarrow II$.
2. Cannabinoids such as marijuana mainly affect the cardiovascular system: $B \rightarrow I$.
3. Cocaine interferes with the transport of the neurotransmitter dopamine: $C \rightarrow IV$.
4. Morphine is a very effective sedative and painkiller: $D \rightarrow III$.
5. The match $A-II, B-I, C-IV, D-III$ is option $1$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q168_29b007f7_04112026.png?v=29b007f71ee6)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q168_1aaffcc2_04112026.png?v=1aaffcc2fc4c)

---

## Q169

Biology · zoology · Structural Organisation in Animals

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (I) Ligaments are dense irregular tissue.
- (II) Cartilage is dense regular tissue.

- (1) Both Statement I and Statement II are true
- **(2)** Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because ligament is an example of dense regular connective tissue so Statement I is incorrect and cartilage is an example of specialised connective tissue and not dense regular tissue.
2. Therefore Statement II is also incorrect.

**Solved independently** (answer withheld)

1. Statement I: ligaments (bone to bone) are dense regular connective tissue with parallel collagen fibres, so calling them dense irregular is false.
2. Statement II: cartilage is a specialised connective tissue, not dense regular tissue, so Statement II is false.
3. Both statements false, which is option $2$.

**Subtopic:** Connective Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 63)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q169_cba34cb1_04112026.png?v=cba34cb18623)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q169_b2a7d87a_12112026.png?v=b2a7d87a0b5b)

---

## Q170

Biology · zoology · Human Health and Disease

In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?

- **(1)** $\mathrm{T_H}$ cells
- (2) B-lymphocytes
- (3) Basophils
- (4) Eosinophils

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) because HIV enters into helper T-lymphocytes ($\mathrm{T_H}$), replicates and produces progeny viruses.
2. The progeny viruses released into blood attack other helper lymphocytes.

**Solved independently** (answer withheld)

1. Per NCERT, HIV enters macrophages, its RNA is reverse-transcribed into DNA, and the virus then enters helper T-lymphocytes ($\mathrm{T_H}$ cells), where it replicates and produces progeny viruses, so the answer is option $1$.

**Subtopic:** AIDS · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q170_5f17f07f_04112026.png?v=5f17f07fa733)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q170_5014de81_04112026.png?v=5014de8147ef)

---

## Q171

Biology · zoology · Environmental Issues

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Electrostatic precipitator is most widely used in thermal power plant.
- (Statement II) Electrostatic precipitator in thermal power plant removes ionising radiations.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Electrostatic precipitator is most widely used in thermal power plants.
2. It can remove over $99$ percent particulate matter present in the exhaust from a thermal power plant.

**Solved independently** (answer withheld)

1. Statement I: the electrostatic precipitator is the most widely used method to remove particulate matter from thermal power plant exhaust, so Statement I is correct.
2. Statement II: an electrostatic precipitator charges and collects particulate matter (dust) using electrodes; it does not remove ionising radiation, so Statement II is incorrect.
3. Statement I correct, Statement II incorrect, which is option $3$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 63)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q171_ce754c97_04112026.png?v=ce754c976969)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q171_05210d53_04112026.png?v=05210d5383bf)

---

## Q172

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct.
- (Statement II) The cavity of the cervix is called cervical canal which along with vagina forms birth canal.

- **(1)** Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is correct but Statement II is false.
- (4) Statement I is incorrect but Statement II is true.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer to this question because statement I and statement II both are correct.
2. Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct.
3. The cavity of cervix is called cervical canal which along with vagina forms the birth canal.

**Solved independently** (answer withheld)

1. Statement I: the vas deferens receives a duct from the seminal vesicle and opens into the urethra as the ejaculatory duct, so Statement I is true.
2. Statement II: the cavity of the cervix is the cervical canal, which together with the vagina forms the birth canal, so Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** The Male Reproductive System, The Female Reproductive System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 63)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q172_59f0f279_04112026.png?v=59f0f279e7f4)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q172_6fe56452_04112026.png?v=6fe56452fe73)

---

## Q173

Biology · zoology · Locomotion and Movement

Match List I with List II.
List I (Type of Joint)
List II (Found between)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cartilaginous Joint | I | Between flat skull bones |
| B | Ball and Socket Joint | II | Between adjacent vertebrae in vertebral column |
| C | Fibrous Joint | III | Between carpal and metacarpal of thumb |
| D | Saddle Joint | IV | Between Humerus and Pectoral girdle |

- (1) A-III, B-I, C-II, D-IV
- **(2)** A-II, B-IV, C-I, D-III
- (3) A-I, B-IV, C-III, D-II
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because cartilaginous joint is present in between the adjacent vertebrae in the vertebral column.
2. Option (3) is not the answer because cartilaginous joint is not present between flat skull bones.
3. Option (4) is not the answer because fibrous joint is not present in between the carpal and metacarpal of thumb.
4. Option (1) is not the answer because saddle joint is not present in between humerus and pectoral girdle.

**Solved independently** (answer withheld)

1. Cartilaginous joint: adjacent vertebrae of the vertebral column are joined by cartilage, so $A \rightarrow II$.
2. Ball and socket joint: between the humerus and the pectoral girdle, so $B \rightarrow IV$.
3. Fibrous joint: sutures between the flat skull bones, so $C \rightarrow I$.
4. Saddle joint: between the carpal and metacarpal of the thumb, so $D \rightarrow III$.
5. $A$-$II$, $B$-$IV$, $C$-$I$, $D$-$III$ matches option $2$.

**Subtopic:** Joints · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 64)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q173_5d5958e7_04112026.png?v=5d5958e711ce)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q173_aacde70a_04112026.png?v=aacde70a8819)

---

## Q174

Biology · zoology · Human Health and Disease

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Ringworm | I | Haemophilus influenzae |
| B | Filariasis | II | Trichophyton |
| C | Malaria | III | Wuchereria bancrofti |
| D | Pneumonia | IV | Plasmodium vivax |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-II, B-III, C-I, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because:
2. (i) Ringworm is caused by Trichophyton.
3. (ii) Filariasis is caused by Wuchereria bancrofti.
4. (iii) Malaria is caused by Plasmodium species.
5. (iv) Pneumonia is caused by Haemophilus influenzae.

**Solved independently** (answer withheld)

1. Ringworm is a fungal disease caused by $Trichophyton$ (A-II); filariasis is caused by $Wuchereria\ bancrofti$ (B-III); malaria is caused by $Plasmodium\ vivax$ (C-IV); pneumonia is caused by $Haemophilus\ influenzae$ (D-I), so A-II, B-III, C-IV, D-I is option $1$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 64)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q174_95accc3b_04112026.png?v=95accc3b668b)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q174_bcf66d09_04112026.png?v=bcf66d097605)

---

## Q175

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Nephrons are of two types: Cortical & Juxta medullary, based on their relative position in cortex and medulla.
- (Reason R) Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle.

- (1) Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true but R is NOT the correct explanation of A.
- **(3)** A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) because Assertion is true as there are two types of nephrons, i.e., cortical nephrons and juxtamedullary nephrons based on their relative position in the cortex and medulla.
2. Reason is not correct as loop of Henle in juxtamedullary nephrons is very long and runs deep into the medulla.
3. Therefore, Assertion is true but Reason is false.

**Solved independently** (answer withheld)

1. Assertion A: nephrons are classed as cortical or juxtamedullary by their position in cortex and medulla, so $A$ is true.
2. Reason R: cortical nephrons have a short loop of Henle reaching only a little into the medulla, while juxtamedullary nephrons have a very long loop running deep into the medulla; R reverses this, so $R$ is false.
3. $A$ true, $R$ false gives option $3$.

**Subtopic:** Human Excretory System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 64)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q175_41d965ea_04112026.png?v=41d965ea3c7b)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q175_7f44bc20_04112026.png?v=7f44bc203231)

---

## Q176

Biology · zoology · Biomolecules

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal).
- (Statement II) Adult human haemoglobin, consists of 4 subunits (two subunits of $\alpha$ type and two subunits of $\beta$ type.)

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false.
- (3) Statement I is true but Statement II is false.
- **(4)** Statement I is false but Statement II is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as a protein is imagined as a line, the left end represented by the first amino acid and the right end is represented by the last amino acid.
2. The first amino acid is also called N-terminal amino acid.
3. The last amino acid is called the C-terminal amino acid.

**Solved independently** (answer withheld)

1. Statement I: by convention the first amino acid at the left end is the N-terminal and the last at the right end is the C-terminal; the statement swaps them, so it is false.
2. Statement II: adult human haemoglobin is a tetramer of two $\alpha$ and two $\beta$ subunits, so it is true.
3. I false, II true, which is option $4$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q176_9503bcf4_04112026.png?v=9503bcf48020)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q176_06f8dc4f_12112026.png?v=06f8dc4f6318)

---

## Q177

Biology · zoology · Environmental Issues

Which of the follwoing statements is correct?

- (1) Eutrophication refers to increase in domestic sewage and waste water in lakes.
- **(2)** Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.
- (3) Presence of large amount of nutrients in water restricts ‘Algal Bloom’
- (4) Algal Bloom decreases fish mortality

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Increase in the concentration of the toxicant at successive trophic level is called biomagnification.
2. Large amount of nutrients in water promotes growth of algal bloom.
3. Algal bloom increases fish mortality.
4. Eutrophication refers to the natural aging of a lake by nutrient enrichment of its water.

**Solved independently** (answer withheld)

1. Option 2 is the NCERT definition of biomagnification (increase in toxicant concentration at successive trophic levels), so it is correct; options 3, 4 and 1 are false because nutrients cause algal blooms, algal blooms increase fish mortality, and eutrophication is the natural ageing of a lake by nutrient enrichment.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 65)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q177_797d9ede_04112026.png?v=797d9ede645b)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q177_5890b6fd_12112026.png?v=5890b6fd914d)

---

## Q178

Biology · zoology · Animal Kingdom

Radial symmetry is NOT found in adults of phylum ______.

- (1) Ctenophora
- **(2)** Hemichordata
- (3) Coelenterata
- (4) Echinodermata

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct  answer because hemichrodates are bilaterally symmetrical animals.
2. Option (3) is not the answer because coelenterates are radially symmetrical organisms.
3. Option (4) is not the answer because adult echinoderms are radially symmetrical in adult stage.
4. Option (1) is not the answer because ctenophores are radially symmetrical organisms.

**Solved independently** (answer withheld)

1. Coelenterata, Ctenophora and adult Echinodermata are radially symmetrical, while Hemichordata are bilaterally symmetrical, so the answer is option $2$.

**Subtopic:** Phylum – Echinodermata and Hemichordata · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 65)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q178_738564c7_04112026.png?v=738564c78981)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q178_b9e6a08a_04112026.png?v=b9e6a08af025)

---

## Q179

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (I) RNA mutates at a faster rate.
- (II) Viruses having RNA genome and shorter life span mutate and evolve faster.

- **(1)** Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is true but Statement II is false.
- (4) Statement I is false but Statement II is true.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. RNA being unstable, mutate at a faster rate.
2. Consequently, viruses having RNA genome and having shorter life span mutate and evolve faster.

**Solved independently** (answer withheld)

1. Statement I: RNA, with its reactive $2'$-OH group, is labile and mutates at a faster rate than DNA, so it is true.
2. Statement II: viruses with an RNA genome and a shorter life span therefore mutate and evolve faster, so it is true.
3. Both statements are true, which is option $1$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 66)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q179_53ffdbf2_04112026.png?v=53ffdbf270ec)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q179_1986d07c_04112026.png?v=1986d07ccdaf)

---

## Q180

Biology · zoology · Principles of Inheritance and Variation

Which one of the following symbols represents mating between relatives in human pedigree analysis?

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q180_option_1_0ea5c9de_04112026.png?v=0ea5c9de8d65)
- **(2)** ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q180_option_2_6c760446_04112026.png?v=6c760446a2b5)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q180_option_3_81a84c3f_04112026.png?v=81a84c3ff254)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/figures_agent/q180_option_4_3a714c9e_04112026.png?v=3a714c9e5c49)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The symbol representing mating between relatives (consanguineous mating) in human pedigree analysis is

**Solved independently** (answer withheld)

1. In human pedigree analysis a single line joining $\square$ and ○ denotes ordinary mating (option $1$), while a double line denotes consanguineous mating, i.e. mating between relatives, so the answer is option $2$.

**Subtopic:** Pedigree Analysis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 66)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q180_15f6ca9e_04112026.png?v=15f6ca9e2b59)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q180_db01dde2_04112026.png?v=db01dde2ae65)

---

## Q181

Biology · zoology · Human Reproduction

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Endometrium is necessary for implantation of blastocyst.
- (Reason R) In the absence of fertilization, the corpus luteum degenerates that causes disintegration of endometrium.

- (1) Both A and R are true and R is the correct explanation of A.
- **(2)** Both A and R are true but R is NOT the correct explanation of A.
- (3) A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because both Assertion and Reason are true.
2. Implantation is embedding of the blastocyst into endometrium of uterus.
3. Correct explanation of reason is
4. Corpus luteum secretes large amount of progesterone which is essential for maintenance of endometrium of uterus. In absence of fertilisation, the corpus luteum degenerates hence the decrease in the level of progesterone hormone will cause disintegration of endometrium leading to menstruation.

**Solved independently** (answer withheld)

1. Assertion A is true: the blastocyst becomes embedded in the endometrium of the uterus (implantation), so the endometrium is necessary.
2. Reason R is true: without fertilization the corpus luteum degenerates, progesterone falls and the endometrium disintegrates (menstruation).
3. R describes what happens to the endometrium without fertilization; it does not explain why the endometrium is required for implantation, so R is not the correct explanation of A: option $2$.

**Subtopic:** Implantation and Embryonic Development, Menstrual Cycle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 66)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q181_bd8dbe7f_04112026.png?v=bd8dbe7f53a9)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q181_84090c8f_04112026.png?v=84090c8f5261)

---

## Q182

Biology · zoology · Digestion and Absorption

Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by

- (1) Sphincter of Oddi
- **(2)** Ileo-caecal valve
- (3) Gastro-oesophageal sphincter
- (4) Pyloric sphincter

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because the undigested food (faeces) enters into caecum of the large intestine through ileo-caecal valve, which prevents the backflow of the faecal matter.
2. Option (3) is not the answer because a muscular sphincter i.e., the gastro-oesophageal sphincter regulates the opening of oesophagus into the stomach.
3. Option (4) is not the answer because pyloric sphincter regulates the opening in between stomach and duodenum.
4. Option (1) is not the answer because the opening of common hepato-pancreatic duct is guarded by sphincter of Oddi.

**Solved independently** (answer withheld)

1. The ileo-caecal valve guards the opening of the ileum into the caecum and prevents backflow of undigested matter, so the answer is option $2$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q182_1fa43038_04112026.png?v=1fa430389f30)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q182_64779deb_04112026.png?v=64779deb8397)

---

## Q183

Biology · zoology · Excretory Products and Their Elimination

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Taenia | I | Nephridia |
| B | Paramoecium | II | Contractile vacuole |
| C | Periplaneta | III | Flame cells |
| D | Pheretima | IV | Urecose gland |

- (1) A-I, B-II, C-III, D-IV
- (2) A-I, B-II, C-IV, D-III
- **(3)** A-III, B-II, C-IV, D-I
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because protonephridia or flame cells are the excretory structures in platyhelminthes.
2. Nephridia are the tubular excretory structures of earthworms (Pheretima) and other annelids.
3. Single celled organisms like Paramoecium have contractile vacuoles for excretion.
4. Urecose glands are present in cockroach.

**Solved independently** (answer withheld)

1. Taenia (Platyhelminthes) excretes through flame cells: $A \rightarrow III$.
2. Paramoecium (protist) uses a contractile vacuole for osmoregulation and excretion: $B \rightarrow II$.
3. Periplaneta (cockroach) has urecose glands that help in excretion: $C \rightarrow IV$.
4. Pheretima (earthworm) excretes through nephridia: $D \rightarrow I$.
5. $A-III, B-II, C-IV, D-I$ is option $3$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 67)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q183_b10119ac_04112026.png?v=b10119ac0942)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q183_5781f7d9_04112026.png?v=5781f7d95205)

---

## Q184

Biology · zoology · Biotechnology: Principles and Processes

Which of the following is not a cloning vector?

- (1) BAC
- (2) YAC
- (3) pBR322
- **(4)** Probe

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is correct answer because a single stranded DNA or RNA tagged with a radioactive molecule is called a probe and it helps in the detection of mutated gene.
2. Option (2), (3) and (1) are not correct because YAC, BAC, pBR322 are vectors.

**Solved independently** (answer withheld)

1. YAC, pBR322 and BAC are vectors used to carry foreign DNA, while a probe is a labelled DNA/RNA used for detection, so the answer is option $4$.

**Subtopic:** Cloning Vectors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q184_88c4061a_04112026.png?v=88c4061af6a5)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q184_98237b89_04112026.png?v=98237b89d1bc)

---

## Q185

Biology · zoology · Body Fluids and Circulation

Match List I with List II.
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P-wave | I | Beginning of systole |
| B | Q-wave | II | Repolarisation of ventricles |
| C | QRS complex | III | Depolarisation of atria |
| D | T-wave | IV | Depolarisation of ventricles |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-IV, B-III, C-II, D-I
- (3) A-II, B-IV, C-I, D-III
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as in a standard ECG, P-wave represents the electrical excitation (or depolarisation) of the atria which leads to the contraction of both the atria.
2. QRS complex represents the depolarisation of ventricles which initiates the ventricular contraction.
3. T-wave represents the return of the ventricles from excited to normal state.

**Solved independently** (answer withheld)

1. In the NCERT ECG, the P-wave is depolarisation of the atria ($A \to III$), the QRS complex is depolarisation of the ventricles ($C \to IV$), the T-wave is repolarisation of the ventricles ($D \to II$), and the Q-wave marks the beginning of systole ($B \to I$), so the match is option $1$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q185_714d1d24_04112026.png?v=714d1d240729)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q185_fcc638bf_04112026.png?v=fcc638bf5d7f)

---

## Q186

Biology · zoology · Chemical Coordination and Integration

Which of the following are NOT under the control of thyroid hormone? Choose the correct answer from the options given below:

- (A) Maintenance of water and electrolyte balance
- (B) Regulation of basal metabolic rate
- (C) Normal rhythm of sleep-wake cycle
- (D) Development of immune system
- (E) Support the process of RBCs formation

- (1) A and D only
- (2) B and C only
- **(3)** C and D only
- (4) D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because thyroid hormones play an important role in the regulation of basal metabolic rate, maintenance of water and electrolyte balance and support the process of RBCs formation, whereas this hormone is not involved in regulating normal rhythm of sleep-wake cycle and development of immune system.

**Solved independently** (answer withheld)

1. Per NCERT, thyroid hormones regulate $\text{BMR}$ (B), support the process of RBC formation (E) and maintain water and electrolyte balance (A).
2. Normal rhythm of the sleep-wake cycle (C) is regulated by melatonin from the pineal gland, not thyroid hormone.
3. Development of the immune system (D) is promoted by thymosins from the thymus, not thyroid hormone.
4. So the items NOT under thyroid control are C and D, which is option $3$.

**Subtopic:** Thyroid Gland and Parathyroid Gland · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q186_a2bc306c_04112026.png?v=a2bc306c0ce8)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q186_f0b12823_12112026.png?v=f0b12823e196)

---

## Q187

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements are correct?
Choose the correct answer from the options given below:

- (A) An excessive loss of body fluid from the body switches off osmoreceptors.
- (B) ADH facilitates water reabsorption to prevent diuresis.
- (C) ANF causes vasodilation.
- (D) ADH causes increase in blood pressure.
- (E) ADH is responsible for decrease in GFR.

- (1) A and B only
- **(2)** B, C and D only
- (3) A, B and E only
- (4) C, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because statements B, C and D are true statements.
2. ADH facilitates water reabsorption from DCT of nephron to prevent diuresis, which causes increase in blood pressure.
3. ANF which is secreted by the heart is a vasodilator.
4. Options (3), (4) and (1) are not correct because statements A and E are false.
5. Excessive loss of body fluid from the body switches on the osmoreceptors.

**Solved independently** (answer withheld)

1. A: excessive loss of body fluid activates osmoreceptors, which trigger ADH release, so A is false.
2. B: ADH facilitates water reabsorption in the distal tubule and collecting duct, preventing diuresis, so B is true.
3. C: ANF causes vasodilation and lowers blood pressure, so C is true.
4. D: ADH constricts blood vessels, raising blood pressure, so D is true.
5. E: by raising blood pressure, ADH can increase glomerular blood flow and GFR, not decrease it, so E is false.
6. True set $= \{B, C, D\}$, which is option $2$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 68)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q187_e568f27a_04112026.png?v=e568f27a7dec)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q187_c893e0f4_04112026.png?v=c893e0f411ea)

---

## Q188

Biology · zoology · Structural Organisation in Animals

In cockroach, excretion is brought about by-
Choose the correct answer from the options given below :

- (A) Phallic gland
- (B) Urecose gland
- (C) Nephrocytes
- (D) Fat body
- (E) Collaterial glands

- (1) A and E only
- (2) A, B and E only
- **(3)** B, C and D only
- (4) B and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the answer because,
2. In cockroach, excretion is brought about by Malpighian tubules, fat body, nephrocytes and urecose glands.
3. Urecose glands are present in male cockroach of some species. They synthesise uric acid.
4. Nephrocytes are large, colourless, ovoid, binucleate cells attached to the dorsal diaphragm in the body cavity.
5. Fat body accumulates, produces and stores uric acid.
6. Phallic gland is the structure of male reproductive system of cockroach and it secretes the outer layer of spermatophore.
7. Collaterial gland is the structure of female reproductive system of cockroach and it secretes the hard egg-case or ootheca around fertilised eggs.

**Solved independently** (answer withheld)

1. In cockroach, excretion is mainly by Malpighian tubules, assisted by the fat body, nephrocytes, cuticle and urecose glands.
2. Phallic gland (A) is a male accessory reproductive gland and collaterial glands (E) are female accessory reproductive glands, so A and E are excluded.
3. Urecose gland (B), nephrocytes (C) and fat body (D) are excretory, giving 'B, C and D only', which is option $3$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 68)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q188_707fc7fe_04112026.png?v=707fc7fe2e2a)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q188_032e92ba_04112026.png?v=032e92ba075e)

---

## Q189

Biology · zoology · Neural Control and Coordination

The parts of human brain that helps in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:

- **(1)** Limbic system and hypothalamus
- (2) Corpora quadrigemina and hippocampus
- (3) Brain stem and epithalamus
- (4) Corpus callosum and thalamus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is the correct answer because limbic system along with hypothalamus regulate the sexual behaviour, expression of excitement, pleasure, rage, fear, etc.
2. Option (2), (3) and (4) are not correct because corpora quadrigemina is a part of the midbrain and consists of four round swellings.
3. Corpus callosum is a tract of nerve fibres that connects right and left cerebral hemispheres.
4. Thalamus is a major coordinating centre in the forebrain for sensory and motor signalling.
5. Midbrain, pons and medulla oblongata together form the brain stem.

**Solved independently** (answer withheld)

1. NCERT states that the inner parts of the cerebral hemispheres and associated deep structures (amygdala, hippocampus) form the limbic system, which along with the hypothalamus regulates sexual behaviour and emotional expression (excitement, pleasure, rage, fear), so the answer is option $1$.

**Subtopic:** Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q189_bbeb1a06_04112026.png?v=bbeb1a06de88)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q189_e06a4e74_04112026.png?v=e06a4e74dfa5)

---

## Q190

Biology · zoology · Body Fluids and Circulation

Which of the following statements are correct?
Choose the **correct** answer from the options given below:

- (A) Basophils are most abundant cells of the total WBCs
- (B) Basophils secrete histamine, serotonin and heparin
- (C) Basophils are involved in inflammatory response
- (D) Basophils have kidney shaped nucleus
- (E) Basophils are agranulocytes

- (1) D and E only
- (2) C and E only
- **(3)** B and C only
- (4) A and B only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the answer because, basophils secrete histamine, serotonin, heparin \textit{etc.} and are involved in inflammatory response.
2. Option (2) is not the answer because, basophils are granulocytes.
3. Option (4) is not the answer because, neutrophils are the most abundant cells ($60\text{–}65\,\%$) of the total WBCs whereas basophils are least ($0.5\text{–}1\%$) abundant of all WBCs.
4. Option (1) is not the answer because, monocytes have a kidney-shaped nucleus.

**Solved independently** (answer withheld)

1. A is false: neutrophils are the most abundant WBCs ($60$-$65\%$); basophils are the least ($0.5$-$1\%$).
2. B is true: basophils secrete histamine, serotonin and heparin.
3. C is true: basophils are involved in inflammatory reactions.
4. D is false: a kidney-shaped nucleus is a feature of monocytes, not basophils.
5. E is false: basophils are granulocytes, not agranulocytes.
6. Only B and C are correct, which is option $3$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 69)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q190_08b2fa56_04112026.png?v=08b2fa568bdd)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q190_a6b0dc1e_12112026.png?v=a6b0dc1e300e)

---

## Q191

Biology · zoology · Molecular Basis of Inheritance

Which one of the following is the sequence on corresponding coding strand, if the sequence on mRNA formed is as follows 5’AUCGAUCGAUCGAUCGAUCGAUCG AUCG 3’?

- (1) 5’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 3’
- (2) 3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’
- **(3)** 5’ ATCGATCGATCGATCGATCGATCGATCG 3’
- (4) 3’ ATCGATCGATCGATCGATCGATCGATCG 5’

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The sequence of coding strand is same as RNA except thymine at the place of uracil.
2. Template strand $\rightarrow$ $3'$-TAGCTAGCTAGCTAGCTAGCTAGCTAGC-$5'$
3. Coding strand $\rightarrow$ $5'$-ATCGATCGATCG ATCGATCGATCGATCG-$3'$
4. $\downarrow$ Transcription
5. mRNA $\rightarrow$ $5'$ AUCGAUCGAUCGAUCGAUCGAUCG AUCG $3'$

**Solved independently** (answer withheld)

1. The coding strand has the same sequence and the same $5' \rightarrow 3'$ polarity as the mRNA, except that DNA has $T$ where RNA has $U$.
2. Replacing $U$ with $T$ in $5'\,AUCG\ldots AUCG\,3'$ gives $5'\,ATCG\ldots ATCG\,3'$, which is option $3$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q191_2ad11cbc_04112026.png?v=2ad11cbc75a4)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q191_968937d8_04112026.png?v=968937d8770f)

---

## Q192

Biology · zoology · Locomotion and Movement

Which of the following statements are correct regarding skeletal muscle? Choose the most appropriate answer from the options given below:

- (A) Muscle bundles are held together by collagenous connective tissue layer called fascicle.
- (B) Sarcoplasmic reticulum of muscle fibre is a store house of calcium ions.
- (C) Striated appearance of skeletal muscle fibre is due to distribution pattern of actin and myosin proteins.
- (D) M line is considered as functional unit of contraction called sarcomere.

- (1) A, B and C only
- **(2)** B and C only
- (3) A, C and D only
- (4) C and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because statements B and C are only correct statements while A and D are incorrect statements.
2. Muscle bundles are held together by collagenous connective tissue layer called fascia.
3. Muscle bundles are called fascicles.
4. The portion of the myofibril between two successive ‘Z’ lines is considered as functional unit of contraction called sarcomere.

**Solved independently** (answer withheld)

1. Statement A: muscle bundles (fascicles) are held together by a collagenous connective tissue layer called fascia, not fascicle, so $A$ is false.
2. Statement B: the sarcoplasmic reticulum stores $\mathrm{Ca^{2+}}$ ions, so $B$ is true.
3. Statement C: the striations come from the distribution pattern of actin and myosin, so $C$ is true.
4. Statement D: the sarcomere is the part of the myofibril between two successive Z lines, not the M line, so $D$ is false.
5. Correct set is $\{B, C\}$, which is option $2$.

**Subtopic:** Structure of Skeletal Muscle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 70)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q192_817d2507_04112026.png?v=817d2507126f)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q192_072a42b2_04112026.png?v=072a42b250cc)

---

## Q193

Biology · zoology · Animal Kingdom

The unique mammalian characteristics are:

- (1) hairs, tympanic membrane and mammary glands
- **(2)** hairs, pinna and mammary glands
- (3) hairs, pinna and indirect development
- (4) pinna, monocondylic skull and mammary glands

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is correct answer because presence of hairs, pinna and mammary glands are unique features of mammals.
2. Options (1), (3) and (4) are not correct because, monocondylic skull is present in reptiles and aves whereas mammals have dicondylic skull.
3. Tympanic membrane is present in amphibians also, so it is not considered as unique feature.

**Solved independently** (answer withheld)

1. NCERT: the most unique mammalian characteristics are mammary glands, hair on the skin and external ears (pinnae), so option $2$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 70)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q193_8ea1a154_04112026.png?v=8ea1a1540e42)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q193_aa3b5a05_04112026.png?v=aa3b5a05fa9d)

---

## Q194

Biology · zoology · Structural Organisation in Animals

Match List I with List II. Choose the correct answer from the options give below:

| List-I | | List-II | |
|---|---|---|---|
| A | Mast cells | I | Ciliated epithelium |
| B | Inner surface of bronchiole | II | Areolar connective tissue |
| C | Blood | III | Cuboidal epithelium |
| D | Tubular parts of nephron | IV | Specialised connective tissue |

- (1) A-I, B-II, C-IV, D-III
- (2) A-II, B-III, C-I, D-IV
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Option (3) is the correct answer because,
2. Areolar connective tissue contains fibroblasts (cells that produce and secrete fibres), macrophages and mast cells.
3. Inner surface of bronchioles is lined by ciliated epithelium.
4. Blood is a specialised connective tissue.
5. Tubular parts of nephron are lined by cuboidal epithelium.

**Solved independently** (answer withheld)

1. Mast cells are a cell type found in areolar connective tissue, so $A \to II$.
2. The inner surface of bronchioles is lined by ciliated epithelium, so $B \to I$.
3. Blood is a specialised (fluid) connective tissue, so $C \to IV$.
4. The tubular parts of the nephron are lined by cuboidal epithelium, so $D \to III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $3$.

**Subtopic:** Connective Tissue, Animal Tissues: Epithelial Tissue · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 70)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q194_34543afc_04112026.png?v=34543afc72d1)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q194_25001497_04112026.png?v=25001497401f)

---

## Q195

Biology · zoology · Animal Kingdom

Select the correct statements with reference to chordates. Choose the **correct** answer from the options given below:

- (A) Presence of a mid-dorsal, solid and double nerve cord.
- (B) Presence of closed circulatory system.
- (C) Presence of paired pharyngeal gill slits.
- (D) Presence of dorsal heart
- (E) Triploblastic pseudocoelomate animals.

- (1) A, C and D only
- **(2)** B and C only
- (3) B, D and E only
- (4) C, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because statements B and C only are correct.
2. Option (1), (3) and (4) are not correct.
3. The chordate characters are presence of closed circulatory system and presence of pharyngeal gill slits.
4. Nerve cord is dorsal, hollow and single.
5. Heart is ventral.
6. They are triploblastic and coelomate.

**Solved independently** (answer withheld)

1. A is false: the chordate nerve cord is dorsal, hollow and single, not solid and double.
2. B is true: chordates have a closed circulatory system.
3. C is true: chordates have paired pharyngeal gill slits.
4. D is false: the chordate heart is ventral.
5. E is false: chordates are triploblastic coelomates, not pseudocoelomates.
6. Only B and C are correct, which is option $2$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 71)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q195_e7e02693_04112026.png?v=e7e026932418)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q195_9b6f7de9_04112026.png?v=9b6f7de9a395)

---

## Q196

Biology · zoology · Strategies for Enhancement in Food Production

Which one of the following is NOT an advantage of inbreeding?

- (1) It decreases homozygosity.
- (2) It exposes harmful recessive genes but are eliminated by selection.
- (3) Elimination of less desirable genes and accumulation of superior genes takes place due to it.
- **(4)** It decreases the productivity of inbred population, after continuous inbreeding.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Option (4) is the correct answer because decreasing the productivity of inbred population is not an advantage of inbreeding.
2. Options (2) and (3) are not the answers because they are the advantages of inbreeding.
3. Option (1) is an incorrect statement.

**Solved independently** (answer withheld)

1. Inbreeding is mating of closely related individuals for $4$-$6$ generations, so it $\textit{increases}$ homozygosity.
2. Exposing harmful recessive genes so selection removes them (option $2$) is an advantage.
3. Eliminating less desirable genes and accumulating superior genes (option $3$) is an advantage.
4. Continued inbreeding reduces fertility and productivity, i.e. inbreeding depression (option $4$), which is a disadvantage.
5. Option $1$ is factually false (inbreeding increases homozygosity), so it is also not an advantage; the intended disadvantage is option $4$.

**Subtopic:** Animal Breeding · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 71)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q196_3da307d8_04112026.png?v=3da307d832d3)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q196_b19dcdc7_04112026.png?v=b19dcdc73b14)

---

## Q197

Biology · zoology · Cell Cycle and Cell Division

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) During $\mathrm{G_0}$ phase of cell cycle, the cell is metabolically inactive.
- (Statement II) The centrosome undergoes duplication during S phase of interphase.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- **(4)** Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Cells in the $\mathrm{G_0}$ stage remain metabolically active but no longer proliferate unless called on to do so depending on the requirement of the organism.
2. In animal cells, during the S-phase, DNA replication begins in the nucleus, and the centriole duplicates in the cytoplasm.

**Solved independently** (answer withheld)

1. Cells in the $\mathrm{G_0}$ (quiescent) phase remain metabolically active but no longer proliferate, so Statement I is incorrect.
2. During S phase of interphase the centriole (centrosome) duplicates in the cytoplasm, so Statement II is correct.
3. Statement I incorrect and Statement II correct is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 71)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q197_19ed99f8_04112026.png?v=19ed99f8f8ed)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q197_2f1aeb77_04112026.png?v=2f1aeb7783bb)

---

## Q198

Biology · zoology · Organisms and Populations

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Logistic growth | I | Unlimited resource availability condition |
| B | Exponential growth | II | Limited resource availability condition |
| C | Expanding age pyramid | III | The percent individuals of pre-reproductive age is largest followed by reproductive and post reproductive age groups |
| D | Stable age pyramid | IV | The percent individuals of pre-reproductives and reproductive age group are same |

- **(1)** A-II, B-I, C-III, D-IV
- (2) A-II, B-III, C-I, D-IV
- (3) A-II, B-IV, C-I, D-III
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Logistic growth occurs when there is limited resource availability condition.
2. Exponential growth occurs when there is unlimited resource availability condition.
3. Expanding age pyramid reflects growing population where the percent individuals of pre-reproductive age is largest followed by reproductive and post-reproductive age groups.
4. Stable age pyramid shows stable population where the percent individuals of pre-reproductive and reproductive age group are same.

**Solved independently** (answer withheld)

1. Logistic growth: resources are limited, so $A \to II$.
2. Exponential growth: resources are unlimited, so $B \to I$.
3. Expanding age pyramid: pre-reproductive individuals are largest, then reproductive, then post-reproductive, so $C \to III$.
4. Stable age pyramid: pre-reproductive and reproductive groups are about equal, so $D \to IV$.
5. $A\text{-}II, B\text{-}I, C\text{-}III, D\text{-}IV$ is option $1$.

**Subtopic:** Life History Variation and Population Attributes, Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q198_4deccfa9_04112026.png?v=4deccfa90ba5)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2023/2023_E5/solutions/q198_d39edf56_12112026.png?v=d39edf5616e1)

---

## Q199

Biology · zoology · Cell Cycle and Cell Division

Select the correct statements. Choose the **correct** answer from the options given below:

- (A) Tetrad formation is seen during Leptotene.
- (B) During Anaphase, the centromeres split and chromatids separate.
- (C) Terminalization takes place during Pachytene.
- (D) Nucleolus, Golgi complex and ER are reformed during Telophase.
- (E) Crossing over takes place between sister chromatids of homologous chromosome.

- (1) A and C only
- **(2)** B and D only
- (3) A, C and E only
- (4) B and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Tetrad formation is seen during zygotene stage
2. During Anaphase, the centromeres split and chromatids separate.
3. Terminalisation of chiasmata takes place during diakinesis.
4. Nucleolus, golgi complex and ER are reformed during telophase.
5. Crossing over takes place between non-sister chromatids of homologus chromosomes.

**Solved independently** (answer withheld)

1. A: tetrads are seen in pachytene after synapsis in zygotene, not leptotene, so A is false.
2. B: in (mitotic) anaphase the centromeres split and sister chromatids separate, so B is true.
3. C: terminalisation of chiasmata occurs in diakinesis, not pachytene, so C is false.
4. D: in telophase the nucleolus, Golgi complex and ER reform, so D is true.
5. E: crossing over occurs between non-sister chromatids of homologous chromosomes, so E is false.
6. True statements are B and D only, which is option $2$.

**Subtopic:** Phases of Cell Cycle, Prophase I and Its Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 72)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q199_1fa6e977_04112026.png?v=1fa6e9777ae4)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q199_ab61464e_04112026.png?v=ab61464eccf1)

---

## Q200

Biology · zoology · Structural Organisation in Animals

Which of the following is characteristic feature of cockroach regarding sexual dimorphism?

- (1) Dark brown body colour and anal cerci
- **(2)** Presence of anal styles
- (3) Presence of sclerites
- (4) Presence of anal cerci

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is the correct answer because anal styles are present in male cockroaches and absent in female cockroaches.
2. Option (1), (3) and (4) are not the correct answers because sclerites, anal cerci and dark brown body colour are common features of both male and female cockroaches.

**Solved independently** (answer withheld)

1. In cockroach, anal cerci, sclerites and the dark brown body colour are found in both sexes, whereas a pair of short, thread-like anal styles is present only in males, so anal styles show sexual dimorphism: option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 73)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/crops/q200_72f603c0_04112026.png?v=72f603c0f10e)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_E5/solutions/q200_b5c73678_04112026.png?v=b5c73678db38)

