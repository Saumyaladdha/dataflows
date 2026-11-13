# NEET (UG) 2023 · Code H1

200 questions · source `NEET_Papers/2023/Set_H1/NEET_2023_Question_Paper_H1.pdf` · every image a CDN link (0 without one) · 0 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Rotational Motion

> ⚠ The independent solve found no printed option exactly right ("which no option shows"); its pick (3) is the closest fit, so treat this question as possibly misprinted.

> ⚠ The booklet prints "Answer (3*)" for the radius-of-gyration ratio (solid sphere : hollow sphere). The publisher's own solution (2023_E5 q032) says "* None of the option is correct (correct answer is sqrt(3/5))". The true ratio is sqrt(3):sqrt(5); the starred option (3), 3:5, is its square, so the square roots were lost from the printed options. Same question as 2023_F1 q001.

The ratio of radius of gyration of a solid sphere of mass $M$ and radius $R$ about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is

- (1) $2 : 5$
- (2) $5 : 2$
- **(3)** $3 : 5$
- (4) $5 : 3$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a solid sphere, $I_1 = \frac{2}{5}MR^2$, so $k_1 = R\sqrt{\frac{2}{5}}$.
2. For a thin hollow sphere, $I_2 = \frac{2}{3}MR^2$, so $k_2 = R\sqrt{\frac{2}{3}}$.
3. $\frac{k_1}{k_2} = \sqrt{\frac{2/5}{2/3}} = \sqrt{\frac{3}{5}} = \sqrt{3} : \sqrt{5}$.
4. No option shows $\sqrt{3} : \sqrt{5}$; option $3$ ($3 : 5$) has the right numbers and is the intended answer if the square roots were lost.

**Subtopic:** Radius of Gyration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q001_05072a6e_04112026.png?v=05072a6e5a4b)

---

## Q2

Physics · Electromagnetic Induction

The magnetic energy stored in an inductor of inductance $4\,\mu\mathrm{H}$ carrying a current of $2\,\mathrm{A}$ is

- (1) $8\,\mathrm{mJ}$
- **(2)** $8\,\mu\mathrm{J}$
- (3) $4\,\mu\mathrm{J}$
- (4) $4\,\mathrm{mJ}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$.
2. $U = \frac{1}{2} \times (4 \times 10^{-6}\,\mathrm{H}) \times (2\,\mathrm{A})^2$.
3. $U = \frac{1}{2} \times 4 \times 10^{-6} \times 4 = 8 \times 10^{-6}\,\mathrm{J}$.
4. $8 \times 10^{-6}\,\mathrm{J} = 8\,\mu\mathrm{J}$, which is option $2$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q002_ac8586f4_04112026.png?v=ac8586f4d2f8)

---

## Q3

Physics · Semiconductor Electronics

A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?

- **(1)** Capacitor
- (2) Load resistance
- (3) A centre-tapped transformer
- (4) p-n junction diodes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The capacitor placed across the load acts as a filter: it charges to the peak voltage and discharges slowly through the load between peaks, removing the ac ripple, so the answer is option $1$.

**Subtopic:** Use of PN Junction Diode as Rectifier · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q003_ad87c82c_04112026.png?v=ad87c82c5359)

---

## Q4

Physics · Electrostatics

An electric dipole is placed at an angle of $30^\circ$ with an electric field of intensity $2 \times 10^{5}\,\mathrm{N\,C^{-1}}$. It experiences a torque equal to $4\,\mathrm{N\,m}$. Calculate the magnitude of charge on the dipole, if the dipole length is $2\,\mathrm{cm}$.

- (1) $4\,\mathrm{mC}$
- **(2)** $2\,\mathrm{mC}$
- (3) $8\,\mathrm{mC}$
- (4) $6\,\mathrm{mC}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Torque on a dipole: $\tau = pE\sin\theta = qlE\sin\theta$.
2. Rearrange: $q = \frac{\tau}{lE\sin\theta}$.
3. $q = \frac{4}{(0.02)(2\times10^{5})(0.5)} = \frac{4}{2000}$.
4. $q = 2\times10^{-3}\,\mathrm{C} = 2\,\mathrm{mC}$, which is option $2$.

**Subtopic:** Torque and Work Done in Rotating Dipole in Uniform Electric Field · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q004_3a7840ca_04112026.png?v=3a7840ca710f)

---

## Q5

Physics · Capacitance

The equivalent capacitance of the system shown in the following circuit is

![printed figure: A 3 uF capacitor in series with two 3 uF capacitors in parallel, between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q005_05512e00_04112026.png?v=05512e0052fe)

*A 3 uF capacitor in series with two 3 uF capacitors in parallel, between A and B*

- (1) $6\,\mu\mathrm{F}$
- (2) $9\,\mu\mathrm{F}$
- **(3)** $2\,\mu\mathrm{F}$
- (4) $3\,\mu\mathrm{F}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The two $3\,\mu\mathrm{F}$ capacitors between the junction and $B$ are in parallel: $C_p = 3 + 3 = 6\,\mu\mathrm{F}$.
2. This combination is in series with the $3\,\mu\mathrm{F}$ capacitor from $A$: $C_{eq} = \frac{3 \times 6}{3 + 6}$.
3. $C_{eq} = \frac{18}{9} = 2\,\mu\mathrm{F}$, which is option $3$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q005_7ea532c8_04112026.png?v=7ea532c8ffa0)

---

## Q6

Physics · Modern Physics

In hydrogen spectrum, the shortest wavelength in the Balmer series is $\lambda$. The shortest wavelength in the Bracket series is

- (1) $9\lambda$
- (2) $16\lambda$
- (3) $2\lambda$
- **(4)** $4\lambda$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The shortest wavelength of a series is its series limit, $n_2 \to \infty$, so $\frac{1}{\lambda_{min}} = \frac{R}{n_1^2}$.
2. Balmer ($n_1 = 2$): $\frac{1}{\lambda} = \frac{R}{4}$, so $\lambda = \frac{4}{R}$.
3. Brackett ($n_1 = 4$): $\frac{1}{\lambda'} = \frac{R}{16}$, so $\lambda' = \frac{16}{R}$.
4. $\frac{\lambda'}{\lambda} = \frac{16}{4} = 4$, so $\lambda' = 4\lambda$, which is option $4$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q006_f95b31d2_04112026.png?v=f95b31d20ec2)

---

## Q7

Physics · Current Electricity

Resistance of a carbon resistor determined from colour codes is $(22000 \pm 5\%)\,\Omega$. The colour of third band must be

- **(1)** Orange
- (2) Yellow
- (3) Red
- (4) Green

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Write the value as two significant digits times a power of ten: $22000\,\Omega = 22 \times 10^{3}\,\Omega$.
2. The first two bands give the digits $2, 2$, and the third band gives the multiplier $10^{3}$.
3. In the colour code, multiplier $3$ is orange, so the third band is orange, option $1$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q007_33d4b571_04112026.png?v=33d4b5711cd2)

---

## Q8

Physics · Gravitation

Two bodies of mass $m$ and $9m$ are placed at a distance $R$. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be ($G$ = gravitational constant)

- **(1)** $-\dfrac{16Gm}{R}$
- (2) $-\dfrac{20Gm}{R}$
- (3) $-\dfrac{8Gm}{R}$
- (4) $-\dfrac{12Gm}{R}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. At the null point a distance $x$ from $m$: $\frac{Gm}{x^2} = \frac{G(9m)}{(R-x)^2}$.
2. Taking square roots: $R - x = 3x$, so $x = \frac{R}{4}$.
3. Distance from $9m$ is $R - \frac{R}{4} = \frac{3R}{4}$.
4. $V = -\frac{Gm}{R/4} - \frac{G(9m)}{3R/4} = -\frac{4Gm}{R} - \frac{12Gm}{R}$.
5. $V = -\frac{16Gm}{R}$, which is option $1$.

**Subtopic:** Calculation of Gravitational Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q008_a460b4d3_04112026.png?v=a460b4d3a254)

---

## Q9

Physics · Current Electricity

If the galvanometer $G$ does not show any deflection in the circuit shown, the value of $R$ is given by

![printed figure: Two cells (10 V and 2 V), a 400 ohm resistor, a resistor R and a galvanometer G](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q009_f618d1f9_04112026.png?v=f618d1f9f0e1)

*Two cells (10 V and 2 V), a 400 ohm resistor, a resistor R and a galvanometer G*

- **(1)** $100\,\Omega$
- (2) $400\,\Omega$
- (3) $200\,\Omega$
- (4) $50\,\Omega$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. With no deflection in $G$, no current flows through the $2\,\text{V}$ branch, so the potential difference across $R$ equals $2\,\text{V}$.
2. The $10\,\text{V}$ cell then drives current only through $400\,\Omega$ and $R$ in series: $I = \frac{10}{400 + R}$.
3. $V_R = IR = \frac{10R}{400 + R} = 2$.
4. $10R = 800 + 2R \Rightarrow 8R = 800 \Rightarrow R = 100\,\Omega$, which is option $1$.

**Subtopic:** Kirchhoff's Laws of Current Distribution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q009_e7ae1192_04112026.png?v=e7ae1192d7e6)

---

## Q10

Physics · Wave Optics

For Young’s double slit experiment, two statements are given below: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) If screen is moved away from the plane of slits, angular separation of the fringes remains constant.
- (Statement II) If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases.

- **(1)** Statement I is true but Statement II is false.
- (2) Statement I is false but Statement II is true.
- (3) Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Angular separation of fringes in YDSE is $\theta = \frac{\beta}{D} = \frac{\lambda}{d}$.
2. $\theta$ does not depend on $D$, so moving the screen away leaves it constant: Statement I is true.
3. $\theta \propto \lambda$, so a larger wavelength increases the angular separation: Statement II is false.
4. Statement I true, Statement II false is option $1$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q010_b93c2da2_04112026.png?v=b93c2da2d24a)

---

## Q11

Physics · Mechanical Properties of Fluids

The venturi-meter works on

- (1) The principle of parallel axes
- (2) The principle of perpendicular axes
- (3) Huygen’s principle
- **(4)** Bernoulli’s principle

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A venturi-meter measures flow speed from the pressure difference between its wide section and its throat; by continuity $A_1 v_1 = A_2 v_2$ and Bernoulli's principle $P_1 - P_2 = \frac{1}{2}\rho (v_2^2 - v_1^2)$, so it works on Bernoulli's principle, which is option $4$.

**Subtopic:** Venturi Tube and Aspirator Pump Problems · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q011_6323ce2e_04112026.png?v=6323ce2e128b)

---

## Q12

Physics · Mechanical Properties of Solids

Let a wire be suspended from the ceiling (rigid support) and stretched by a weight $W$ attached at its free end. The longitudinal stress at any point of cross-sectional area $A$ of the wire is

- (1) $W/2A$
- (2) Zero
- (3) $2W/A$
- **(4)** $W/A$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Neglecting the wire's own mass, equilibrium of the hanging weight gives tension $T = W$ at every cross-section of the wire.
2. Longitudinal stress $= \frac{T}{A} = \frac{W}{A}$, which is option $4$.

**Subtopic:** Stress and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q012_f53094cc_04112026.png?v=f53094cc446a)

---

## Q13

Physics · Rotational Motion

The angular acceleration of a body, moving along the circumference of a circle, is

- (1) Along the tangent to its position
- **(2)** Along the axis of rotation
- (3) Along the radius, away from centre
- (4) Along the radius towards the centre

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$, and for motion on a fixed circle $\vec{\omega}$ lies along the axis of rotation, so $\vec{\alpha}$ is along the axis of rotation, which is option $2$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 3)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q013_1742cfbc_04112026.png?v=1742cfbc1979)

---

## Q14

Physics · Kinetic Theory of Gases

The temperature of a gas is $-50\,^\circ\mathrm{C}$. To what temperature the gas should be heated so that the rms speed is increased by 3 times?

- (1) $3097\,\mathrm{K}$
- (2) $223\,\mathrm{K}$
- (3) $669\,^\circ\mathrm{C}$
- **(4)** $3295\,^\circ\mathrm{C}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $T = -50 + 273 = 223\,\mathrm{K}$.
2. $v_{rms} = \sqrt{\frac{3RT}{M}} \propto \sqrt{T}$.
3. Increased by 3 times: $v' = v + 3v = 4v$.
4. $\frac{T'}{T} = \left(\frac{v'}{v}\right)^2 = 16$.
5. $T' = 16 \times 223\,\mathrm{K} = 3568\,\mathrm{K}$.
6. $T' = 3568 - 273 = 3295^\circ\mathrm{C}$, which is option $4$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 4)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q014_d2488077_04112026.png?v=d2488077a59f)

---

## Q15

Physics · Modern Physics

The work functions of Caesium ($\mathrm{Cs}$), Potassium ($\mathrm{K}$) and Sodium ($\mathrm{Na}$) are $2.14\,\mathrm{eV}$, $2.30\,\mathrm{eV}$ and $2.75\,\mathrm{eV}$ respectively. If incident electromagnetic radiation has an incident energy of $2.20\,\mathrm{eV}$, which of these photosensitive surfaces may emit photoelectrons?

- (1) $\mathrm{K}$ only
- (2) $\mathrm{Na}$ only
- **(3)** $\mathrm{Cs}$ only
- (4) Both $\mathrm{Na}$ and $\mathrm{K}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Photoelectrons are emitted only if $E_{photon} \geq \phi$.
2. Cs: $\phi = 2.14\,\mathrm{eV} < 2.20\,\mathrm{eV}$, so Cs emits.
3. K: $\phi = 2.30\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so K does not emit.
4. Na: $\phi = 2.75\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so Na does not emit.
5. Only Cs emits, which is option $3$.

**Subtopic:** Photoelectric Effect · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q015_3df5403e_04112026.png?v=3df5403e58a6)

---

## Q16

Physics · Alternating Current

An ac source is connected to a capacitor $C$. Due to decrease in its operating frequency

- **(1)** Displacement current decreases
- (2) Capacitive reactance remains constant
- (3) Capacitive reactance decreases
- (4) Displacement current increases

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Capacitive reactance is $X_C = \frac{1}{2\pi f C}$.
2. As $f$ decreases, $X_C$ increases, ruling out options $2$ and $3$.
3. Conduction current $I = \frac{V}{X_C}$ therefore decreases.
4. The displacement current between the plates equals the conduction current, $I_d = I$, so $I_d$ decreases, which is option $1$.

**Subtopic:** Variation of Reactance with Frequency · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q016_e31c7033_04112026.png?v=e31c7033f8bd)

---

## Q17

Physics · Ray Optics

Light travels a distance $x$ in time $t_1$ in air and $10x$ in time $t_2$ in another denser medium. What is the critical angle for this medium?

- (1) $\sin^{-1}\left(\dfrac{t_1}{10\,t_2}\right)$
- **(2)** $\sin^{-1}\left(\dfrac{10\,t_1}{t_2}\right)$
- (3) $\sin^{-1}\left(\dfrac{t_2}{t_1}\right)$
- (4) $\sin^{-1}\left(\dfrac{10t_2}{t_1}\right)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Speed of light in air: $c = \frac{x}{t_1}$.
2. Speed of light in the medium: $v = \frac{10x}{t_2}$.
3. Refractive index: $n = \frac{c}{v} = \frac{x/t_1}{10x/t_2} = \frac{t_2}{10\,t_1}$.
4. Critical angle: $\sin C = \frac{1}{n} = \frac{10\,t_1}{t_2}$, so $C = \sin^{-1}\left(\frac{10\,t_1}{t_2}\right)$, which is option $2$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q017_ae2e5001_04112026.png?v=ae2e5001d6f7)

---

## Q18

Physics · Magnetic Effect of Electric Current

The net magnetic flux through any closed surface is

- (1) Infinity
- (2) Negative
- **(3)** Zero
- (4) Positive

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Gauss's law for magnetism (no isolated magnetic poles) gives $\oint \vec{B} \cdot d\vec{A} = 0$, so the net flux is zero, which is option $3$.

**Subtopic:** Magnetism and Gauss's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q018_a42f21a0_04112026.png?v=a42f21a0924e)

---

## Q19

Physics · Alternating Current

A $12\,\mathrm{V}$, $60\,\mathrm{W}$ lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of $220\,\mathrm{V}$. Assuming the transformer to be ideal, what is the current in the primary winding?

- (1) $3.7\,\mathrm{A}$
- (2) $0.37\,\mathrm{A}$
- **(3)** $0.27\,\mathrm{A}$
- (4) $2.7\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For an ideal transformer, power in the primary equals power in the secondary: $P_p = P_s = 60\,\mathrm{W}$.
2. $I_p = \frac{P_p}{V_p} = \frac{60\,\mathrm{W}}{220\,\mathrm{V}}$.
3. $I_p \approx 0.27\,\mathrm{A}$, which is option $3$.

**Subtopic:** Transformer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q019_ef62dba4_04112026.png?v=ef62dba49605)

---

## Q20

Physics · Units and Measurements

A metal wire has mass $(0.4 \pm 0.002)\,\mathrm{g}$, radius $(0.3 \pm 0.001)\,\mathrm{mm}$ and length $(5 \pm 0.02)\,\mathrm{cm}$. The maximum possible percentage error in the measurement of density will nearly be

- **(1)** $1.6\%$
- (2) $1.4\%$
- (3) $1.2\%$
- (4) $1.3\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Density of a wire: $\rho = \frac{m}{\pi r^2 l}$.
2. Maximum fractional error: $\frac{\Delta \rho}{\rho} = \frac{\Delta m}{m} + 2\frac{\Delta r}{r} + \frac{\Delta l}{l}$.
3. $\frac{\Delta m}{m} = \frac{0.002}{0.4} = 0.005 = 0.5\%$.
4. $2\frac{\Delta r}{r} = 2 \times \frac{0.001}{0.3} = 0.00667 = 0.667\%$.
5. $\frac{\Delta l}{l} = \frac{0.02}{5} = 0.004 = 0.4\%$.
6. $\frac{\Delta \rho}{\rho} = 0.5\% + 0.667\% + 0.4\% = 1.567\% \approx 1.6\%$, which is option $1$.

**Subtopic:** Errors in Measurement · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 4)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q020_950566f9_04112026.png?v=950566f9ee11)

---

## Q21

Physics · Semiconductor Electronics

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Photovoltaic devices can convert optical radiation into electricity.
- (Statement II) Zener diode is designed to operate under reverse bias in breakdown region.

- (1) Statement I is correct but Statement II is incorrect
- (2) Statement I is incorrect but Statement II is correct
- **(3)** Both Statement I and Statement II are correct
- (4) Both Statement I and Statement II are incorrect

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: a photovoltaic device such as a solar cell generates an emf when optical radiation falls on it, so it converts light into electricity; Statement I is correct.
2. Statement II: a Zener diode is heavily doped and is designed to operate under reverse bias in the breakdown region (used as a voltage regulator); Statement II is correct.
3. Both statements are correct, which is option $3$.

**Subtopic:** Special Purpose PN Junction Diodes · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 5)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q021_b8e553b7_04112026.png?v=b8e553b70862)

---

## Q22

Physics · Kinematics

A bullet is fired from a gun at the speed of $280\,\mathrm{m\,s^{-1}}$ in the direction $30^\circ$ above the horizontal. The maximum height attained by the bullet is ($g = 9.8\,\mathrm{m\,s^{-2}}$, $\sin 30^\circ = 0.5$)

- **(1)** $1000\,\mathrm{m}$
- (2) $3000\,\mathrm{m}$
- (3) $2800\,\mathrm{m}$
- (4) $2000\,\mathrm{m}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Maximum height of a projectile: $H = \frac{u^2 \sin^2\theta}{2g}$.
2. Vertical component: $u\sin\theta = 280 \times 0.5 = 140\,\mathrm{m\,s^{-1}}$.
3. $H = \frac{(140)^2}{2 \times 9.8} = \frac{19600}{19.6} = 1000\,\mathrm{m}$, which is option $1$.

**Subtopic:** Maximum Height Reached · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q022_fe3f3995_04112026.png?v=fe3f3995d671)

---

## Q23

Physics · Thermodynamics

A Carnot engine has an efficiency of $50\%$ when its source is at a temperature $327^\circ\mathrm{C}$. The temperature of the sink is

- (1) $100^\circ\mathrm{C}$
- (2) $200^\circ\mathrm{C}$
- **(3)** $27^\circ\mathrm{C}$
- (4) $15^\circ\mathrm{C}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Convert the source temperature to kelvin: $T_1 = 327 + 273 = 600\,\mathrm{K}$.
2. Carnot efficiency: $\eta = 1 - \frac{T_2}{T_1}$.
3. $0.5 = 1 - \frac{T_2}{600} \Rightarrow T_2 = 300\,\mathrm{K}$.
4. $T_2 = 300 - 273 = 27^{\circ}\mathrm{C}$, which is option $3$.

**Subtopic:** Carnot Engine · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 5)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q023_5d503f03_04112026.png?v=5d503f03609d)

---

## Q24

Physics · Mechanical Properties of Fluids

The amount of energy required to form a soap bubble of radius $2\,\mathrm{cm}$ from a soap solution is nearly (surface tension of soap solution $= 0.03\,\mathrm{N\,m^{-1}}$)

- **(1)** $3.01 \times 10^{-4}\,\mathrm{J}$
- (2) $50.1 \times 10^{-4}\,\mathrm{J}$
- (3) $30.16 \times 10^{-4}\,\mathrm{J}$
- (4) $5.06 \times 10^{-4}\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A soap bubble has two free surfaces, so the area created is $A = 2 \times 4\pi r^2 = 8\pi r^2$.
2. $r = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$, so $r^2 = 4 \times 10^{-4}\,\mathrm{m^2}$.
3. $A = 8\pi \times 4 \times 10^{-4} = 32\pi \times 10^{-4}\,\mathrm{m^2} \approx 1.005 \times 10^{-2}\,\mathrm{m^2}$.
4. $W = T A = 0.03 \times 1.005 \times 10^{-2} \approx 3.016 \times 10^{-4}\,\mathrm{J}$.
5. $3.01 \times 10^{-4}\,\mathrm{J}$ is option $1$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q024_17a3192c_04112026.png?v=17a3192c42cf)

---

## Q25

Physics · Modern Physics

The minimum wavelength of $X$-rays produced by an electron accelerated through a potential difference of $V$ volts is proportional to

- (1) $\frac{1}{\sqrt{V}}$
- (2) $V^{2}$
- (3) $\sqrt{V}$
- **(4)** $\frac{1}{V}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The shortest wavelength comes from an electron that gives all of its kinetic energy $eV$ to a single photon: $eV = \frac{hc}{\lambda_{min}}$.
2. $\lambda_{min} = \frac{hc}{eV}$, so $\lambda_{min} \propto \frac{1}{V}$, which is option $4$.

**Subtopic:** Continuous and Characteristic X-Ray Spectra · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 5)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q025_c516e129_04112026.png?v=c516e129be0e)

---

## Q26

Physics · Alternating Current

In a series $LCR$ circuit, the inductance $L$ is $10\,\mathrm{mH}$, capacitance $C$ is $1\,\mu\mathrm{F}$ and resistance $R$ is $100\,\Omega$. The frequency at which resonance occurs is

- (1) $1.59\,\mathrm{rad/s}$
- **(2)** $1.59\,\mathrm{kHz}$
- (3) $15.9\,\mathrm{rad/s}$
- (4) $15.9\,\mathrm{kHz}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Resonance in series $LCR$ occurs at $\omega_0 = \frac{1}{\sqrt{LC}}$, independent of $R$.
2. $LC = (10\times10^{-3}\,\mathrm{H})(1\times10^{-6}\,\mathrm{F}) = 10^{-8}\,\mathrm{s^2}$.
3. $\sqrt{LC} = 10^{-4}\,\mathrm{s}$, so $\omega_0 = 10^{4}\,\mathrm{rad/s}$.
4. $f_0 = \frac{\omega_0}{2\pi} = \frac{10^4}{2\pi} \approx 1591.5\,\mathrm{Hz} = 1.59\,\mathrm{kHz}$, which is option $2$.

**Subtopic:** Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q026_f2757a11_04112026.png?v=f2757a11e3ef)

---

## Q27

Physics · Work, Energy and Power

The potential energy of a long spring when stretched by $2\,\mathrm{cm}$ is $U$. If the spring is stretched by $8\,\mathrm{cm}$, potential energy stored in it will be

- (1) $8\,U$
- **(2)** $16\,U$
- (3) $2\,U$
- (4) $4\,U$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Spring potential energy is $U = \frac{1}{2}kx^2$, so $U \propto x^2$.
2. $\frac{U'}{U} = \left(\frac{8\,\mathrm{cm}}{2\,\mathrm{cm}}\right)^2 = 4^2 = 16$.
3. $U' = 16\,U$, which is option $2$.

**Subtopic:** Potential Energy of Spring · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q027_81b82efb_04112026.png?v=81b82efba9e3)

---

## Q28

Physics · Modern Physics

The half life of a radioactive substance is $20\,\text{minutes}$. In how much time, the activity of substance drops to $\left(\frac{1}{16}\right)^{\text{th}}$ of its initial value?

- (1) $60\,\text{minutes}$
- **(2)** $80\,\text{minutes}$
- (3) $20\,\text{minutes}$
- (4) $40\,\text{minutes}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Activity after $n$ half-lives: $\frac{A}{A_0} = \left(\frac{1}{2}\right)^n$.
2. $\frac{1}{16} = \left(\frac{1}{2}\right)^4 \Rightarrow n = 4$.
3. $t = n\,T_{1/2} = 4 \times 20\,\text{min} = 80\,\text{min}$, which is option $2$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q028_694a77eb_04112026.png?v=694a77eb541e)

---

## Q29

Physics · Electrostatics

If $\oint_{s} \vec{E} \cdot \overrightarrow{dS} = 0$ over a surface, then

- (1) All the charges must necessarily be inside the surface
- (2) The electric field inside the surface is necessarily uniform
- **(3)** The number of flux lines entering the surface must be equal to the number of flux lines leaving it
- (4) The magnitude of electric field on the surface is constant

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. By Gauss's law, $\oint_s \vec{E}\cdot d\vec{S} = \frac{q_{enc}}{\varepsilon_0}$.
2. Given the flux is $0$, so $q_{enc} = 0$; charges may be outside, so option $1$ is wrong.
3. Zero net flux does not require $|\vec{E}|$ constant on the surface or $\vec{E}$ uniform inside, so options $4$ and $2$ are wrong.
4. Net flux $= \Phi_{out} - \Phi_{in} = 0 \Rightarrow \Phi_{in} = \Phi_{out}$: lines entering equal lines leaving, which is option $3$.

**Subtopic:** Electric Flux · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q029_0917c804_04112026.png?v=0917c804ce13)

---

## Q30

Physics · Waves

The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is

- (1) $1:3$
- (2) $3:1$
- (3) $1:2$
- **(4)** $2:1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Fundamental of an open pipe: $f_o = \frac{v}{2L}$.
2. Fundamental of a closed pipe: $f_c = \frac{v}{4L}$.
3. $\frac{f_o}{f_c} = \frac{v/2L}{v/4L} = 2$, so the ratio is $2:1$, which is option $4$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q030_a0853bad_04112026.png?v=a0853bad3100)

---

## Q31

Physics · Units and Measurements

The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are

- (1) Least count errors
- **(2)** Random errors
- (3) Instrumental errors
- (4) Personal errors

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT defines random errors as those that occur irregularly and arise from unpredictable fluctuations in experimental conditions such as temperature and voltage supply, so the answer is option $2$.

**Subtopic:** Errors in Measurement · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q031_ad60e050_04112026.png?v=ad60e0505fe4)

---

## Q32

Physics · Electromagnetic Waves

In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of $2.0 \times 10^{10}\,\mathrm{Hz}$ and amplitude $48\,\mathrm{V\,m^{-1}}$. Then the amplitude of oscillating magnetic field is (Speed of light in free space $= 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$)

- **(1)** $1.6 \times 10^{-7}\,\mathrm{T}$
- (2) $1.6 \times 10^{-6}\,\mathrm{T}$
- (3) $1.6 \times 10^{-9}\,\mathrm{T}$
- (4) $1.6 \times 10^{-8}\,\mathrm{T}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For a plane EM wave in free space the field amplitudes are related by $B_0 = \frac{E_0}{c}$.
2. $B_0 = \frac{48\,\mathrm{V\,m^{-1}}}{3 \times 10^{8}\,\mathrm{m\,s^{-1}}} = 16 \times 10^{-8}\,\mathrm{T}$.
3. $16 \times 10^{-8}\,\mathrm{T} = 1.6 \times 10^{-7}\,\mathrm{T}$, which is option $1$.

**Subtopic:** Relation Between E, B, and Speed of Light · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q032_92f4ab28_04112026.png?v=92f4ab28e0db)

---

## Q33

Physics · Laws of Motion

A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is

- **(1)** Along north-east
- (2) Along south-west
- (3) Along eastward
- (4) Along northward

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Take east as $\hat{i}$ and north as $\hat{j}$; initial velocity $\vec{v}_1 = -v\hat{j}$ (southward).
2. Final velocity $\vec{v}_2 = v\hat{i}$ (eastward, same speed).
3. $\Delta\vec{v} = \vec{v}_2 - \vec{v}_1 = v\hat{i} + v\hat{j}$.
4. $\vec{F} \propto \Delta\vec{p} = m\Delta\vec{v}$, which is directed at $45^\circ$ between east and north, i.e. north-east, option $1$.

**Subtopic:** Newton's Second Law as Change in Momentum · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q033_50f57be7_04112026.png?v=50f57be727df)

---

## Q34

Physics · Current Electricity

> ⚠ The independent solve found no printed option exactly right ("No option gives 0"); its pick (4) is the closest fit, so treat this question as possibly misprinted.

The magnitude and direction of the current in the following circuit is

![printed figure: Rectangular loop ABCD: 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm along AB; 7 ohm along DC](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q034_ad4a5eb3_04112026.png?v=ad4a5eb379b1)

*Rectangular loop ABCD: 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm along AB; 7 ohm along DC*

- (1) $\frac{5}{9}\,\mathrm{A}$ from $A$ to $B$ through $E$
- (2) $1.5\,\mathrm{A}$ from $B$ to $A$ through $E$
- (3) $0.2\,\mathrm{A}$ from $B$ to $A$ through $E$
- **(4)** $0.5\,\mathrm{A}$ from $A$ to $B$ through $E$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The two cells are connected with their like terminals facing $E$, so they oppose: $\varepsilon_{net} = 10\,\mathrm{V} - 5\,\mathrm{V} = 5\,\mathrm{V}$.
2. All resistors are in one series loop: $R = 2\,\Omega + 1\,\Omega + 7\,\Omega = 10\,\Omega$.
3. $I = \frac{\varepsilon_{net}}{R} = \frac{5}{10} = 0.5\,\mathrm{A}$.
4. The current is set by the larger $10\,\mathrm{V}$ cell; the only option with $0.5\,\mathrm{A}$ is option $4$ (from $A$ to $B$ through $E$).

**Subtopic:** Combination of Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q034_c21fdc80_04112026.png?v=c21fdc801b46)

---

## Q35

Physics · Kinematics

A vehicle travels half the distance with speed $v$ and the remaining distance with speed $2v$. Its average speed is

- **(1)** $\frac{4v}{3}$
- (2) $\frac{3v}{4}$
- (3) $\frac{v}{3}$
- (4) $\frac{2v}{3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Let total distance be $d$; each half is $\frac{d}{2}$.
2. $t_1 = \frac{d/2}{v} = \frac{d}{2v}$.
3. $t_2 = \frac{d/2}{2v} = \frac{d}{4v}$.
4. $t = t_1 + t_2 = \frac{3d}{4v}$.
5. $v_{avg} = \frac{d}{t} = \frac{4v}{3}$, which is option $1$.

**Subtopic:** Average Speed · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 7)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q035_3fc3d510_04112026.png?v=3fc3d51067a6)

---

## Q36

Physics · Modern Physics

The radius of inner most orbit of hydrogen atom is $5.3 \times 10^{-11}\,\mathrm{m}$. What is the radius of third allowed orbit of hydrogen atom?

- (1) $1.59\,\mathring{\mathrm{A}}$
- **(2)** $4.77\,\mathring{\mathrm{A}}$
- (3) $0.53\,\mathring{\mathrm{A}}$
- (4) $1.06\,\mathring{\mathrm{A}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In the Bohr model $r_n = r_1 n^2$ for hydrogen.
2. $r_1 = 5.3 \times 10^{-11}\,\mathrm{m} = 0.53\,\mathring{\mathrm{A}}$.
3. $r_3 = 3^2 \times 0.53\,\mathring{\mathrm{A}} = 4.77\,\mathring{\mathrm{A}}$, which is option $2$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q036_3d48355e_04112026.png?v=3d48355ed916)

---

## Q37

Physics · Current Electricity

10 resistors, each of resistance $R$ are connected in series to a battery of emf $E$ and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased $n$ times. The value of $n$ is

- (1) $1$
- (2) $1000$
- (3) $10$
- **(4)** $100$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In series, $R_s = 10R$, so $I_s = \frac{E}{10R}$.
2. In parallel, $R_p = \frac{R}{10}$, so $I_p = \frac{E}{R/10} = \frac{10E}{R}$.
3. $n = \frac{I_p}{I_s} = \frac{10E/R}{E/(10R)} = 100$, which is option $4$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q037_2c538680_04112026.png?v=2c538680ada2)

---

## Q38

Physics · Oscillations

The $x$-$t$ graph of a particle performing simple harmonic motion is shown in the figure. The acceleration of the particle at $t = 2\,\mathrm{s}$ is

![printed figure: x-t graph of SHM: x = sin(pi t/4), amplitude 1 m, period 8 s](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q038_2f84e543_04112026.png?v=2f84e5433c66)

*x-t graph of SHM: x = sin(pi t/4), amplitude 1 m, period 8 s*

- (1) $\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$
- **(2)** $-\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$
- (3) $\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$
- (4) $-\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. From the graph, amplitude $A = 1\,\mathrm{m}$ and period $T = 8\,\mathrm{s}$, with $x = A\sin\omega t$.
2. $\omega = \frac{2\pi}{T} = \frac{2\pi}{8} = \frac{\pi}{4}\,\mathrm{rad\,s^{-1}}$.
3. At $t = 2\,\mathrm{s}$, $x = \sin\frac{\pi}{2} = 1\,\mathrm{m}$.
4. $a = -\omega^2 x = -\frac{\pi^2}{16}\times 1 = -\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$, which is option $2$.

**Subtopic:** Acceleration in SHM · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q038_135701b1_04112026.png?v=135701b1175c)

---

## Q39

Physics · Ray Optics

Two thin lenses are of same focal lengths ($f$), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be

- (1) $\frac{f}{2}$
- **(2)** Infinite
- (3) Zero
- (4) $\frac{f}{4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For thin lenses in contact, $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}$.
2. Convex lens $f_1 = +f$, concave lens $f_2 = -f$, so $\frac{1}{F} = \frac{1}{f} - \frac{1}{f} = 0$.
3. $\frac{1}{F} = 0 \Rightarrow F = \infty$, which is option $2$ (Infinite).

**Subtopic:** Combination of Thin Lenses in Contact · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q039_d746e850_04112026.png?v=d746e850395b)

---

## Q40

Physics · Gravitation

A satellite is orbiting just above the surface of the earth with period $T$. If $d$ is the density of the earth and $G$ is the universal constant of gravitation, the quantity $\frac{3\pi}{Gd}$ represents

- (1) $T^{3}$
- (2) $\sqrt{T}$
- (3) $T$
- **(4)** $T^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For an orbit just above the surface, $r \approx R$, so $T = 2\pi\sqrt{\frac{R^{3}}{GM}}$.
2. Squaring: $T^{2} = \frac{4\pi^{2}R^{3}}{GM}$.
3. Mass of the earth in terms of density: $M = \frac{4}{3}\pi R^{3} d$.
4. Substitute: $T^{2} = \frac{4\pi^{2}R^{3}}{G \cdot \frac{4}{3}\pi R^{3} d} = \frac{3\pi}{Gd}$.
5. So $\frac{3\pi}{Gd} = T^{2}$, which is option $4$.

**Subtopic:** Motion of a Satellite · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q040_7d843366_04112026.png?v=7d843366774d)

---

## Q41

Physics · Laws of Motion

Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is $0.15$ ($g = 10\,\mathrm{m\,s^{-2}}$).

- **(1)** $1.5\,\mathrm{m\,s^{-2}}$
- (2) $50\,\mathrm{m\,s^{-2}}$
- (3) $1.2\,\mathrm{m\,s^{-2}}$
- (4) $150\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. To stay at rest relative to the car, the body must accelerate with the car, and only static friction can supply that force: $ma \le f_{s,\max} = \mu_s m g$.
2. Cancel $m$: $a_{\max} = \mu_s g$.
3. $a_{\max} = 0.15 \times 10 = 1.5\,\mathrm{m\,s^{-2}}$, which is option $1$.

**Subtopic:** Static Friction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q041_d5aa10d2_04112026.png?v=d5aa10d27d45)

---

## Q42

Physics · Electrostatics

An electric dipole is placed as shown in the figure. The electric potential (in $10^{2}\,\mathrm{V}$) at point $P$ due to the dipole is ($\epsilon_0$ = permittivity of free space and $\frac{1}{4\pi\epsilon_0} = K$)

![printed figure: Dipole -q and +q 6 cm apart on an axis, point P on the axis 5 cm from the centre 0](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q042_4a7dbde1_04112026.png?v=4a7dbde17cd9)

*Dipole -q and +q 6 cm apart on an axis, point P on the axis 5 cm from the centre 0*

- (1) $\left(\frac{8}{5}\right)qK$
- (2) $\left(\frac{8}{3}\right)qK$
- **(3)** $\left(\frac{3}{8}\right)qK$
- (4) $\left(\frac{5}{8}\right)qK$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. From the figure, $P$ is $5\,\mathrm{cm}$ from the centre $O$ on the axis, on the side of $+q$.
2. Distance from $+q$: $r_+ = 5 - 3 = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$.
3. Distance from $-q$: $r_- = 5 + 3 = 8\,\mathrm{cm} = 0.08\,\mathrm{m}$.
4. $V = Kq\left(\frac{1}{0.02} - \frac{1}{0.08}\right) = Kq(50 - 12.5) = 37.5\,Kq$.
5. $37.5\,Kq = \frac{3}{8}qK \times 10^{2}\,\mathrm{V}$, which is option $3$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q042_b737f9af_04112026.png?v=b737f9afe5cd)

---

## Q43

Physics · Alternating Current

The net impedance of circuit (as shown in figure) will be

![printed figure: Series LCR circuit with an AC source 220 V, 50 Hz](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q043_56ad3da6_04112026.png?v=56ad3da67735)

*Series LCR circuit with an AC source 220 V, 50 Hz*

- **(1)** $5\sqrt{5}\,\Omega$
- (2) $25\,\Omega$
- (3) $10\sqrt{2}\,\Omega$
- (4) $15\,\Omega$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Series LCR circuit with $R = 10\,\Omega$, $L = \frac{50}{\pi}\,\text{mH}$, $C = \frac{10^3}{\pi}\,\mu\text{F}$, $f = 50\,\text{Hz}$.
2. $X_L = 2\pi f L = 2\pi (50) \frac{50}{\pi}\times 10^{-3} = 5\,\Omega$.
3. $X_C = \frac{1}{2\pi f C} = \frac{1}{2\pi (50) \frac{10^3}{\pi}\times 10^{-6}} = \frac{1}{0.1} = 10\,\Omega$.
4. $Z = \sqrt{R^2 + (X_C - X_L)^2} = \sqrt{10^2 + 5^2} = \sqrt{125}$.
5. $\sqrt{125} = 5\sqrt{5}\,\Omega$, which is option $1$.

**Subtopic:** Impedance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q043_e6e7aedc_04112026.png?v=e6e7aedc0143)

---

## Q44

Physics · Semiconductor Electronics

For the following logic circuit, the truth table is

![printed figure: Inputs A and B each through a NOT gate into a NAND gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q044_5f84ecc0_04112026.png?v=5f84ecc0f42d)

*Inputs A and B each through a NOT gate into a NAND gate giving Y*

- (1) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (2) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$
- (3) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- **(4)** $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{array}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The figure shows $A$ and $B$ each inverted, then fed to a NAND gate, so $Y = \overline{\bar{A}\cdot\bar{B}}$.
2. By De Morgan's theorem, $\overline{\bar{A}\cdot\bar{B}} = \bar{\bar{A}} + \bar{\bar{B}} = A + B$.
3. So the circuit is an OR gate: $Y = 0, 1, 1, 1$ for $AB = 00, 01, 10, 11$, which is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q044_9826e7e8_04112026.png?v=9826e7e85741)

---

## Q45

Physics · Ray Optics

In the figure shown here, what is the equivalent focal length of the combination of lenses (Assume that all layers are thin)?

![printed figure: A thin biconvex lens of index n1 embedded in a medium of index n2, R1 = R2 = 20 cm](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q045_6b935cdd_04112026.png?v=6b935cdd8440)

*A thin biconvex lens of index n1 embedded in a medium of index n2, R1 = R2 = 20 cm*

- **(1)** $-100\,\mathrm{cm}$
- (2) $-50\,\mathrm{cm}$
- (3) $40\,\mathrm{cm}$
- (4) $-40\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The combination is three thin lenses in contact in air: a central biconvex lens of $n_1 = 1.5$ and two plano-concave layers of $n_2 = 1.6$ on either side.
2. Central lens: $\frac{1}{f_1} = (1.5-1)\left(\frac{1}{20}+\frac{1}{20}\right) = \frac{1}{20}\,\mathrm{cm^{-1}}$.
3. Each outer plano-concave layer: $\frac{1}{f_2} = \frac{1}{f_3} = (1.6-1)\left(\frac{1}{\infty}-\frac{1}{20}\right) = -\frac{3}{100}\,\mathrm{cm^{-1}}$.
4. Lenses in contact: $\frac{1}{F} = \frac{1}{f_1}+\frac{1}{f_2}+\frac{1}{f_3} = \frac{5}{100}-\frac{6}{100} = -\frac{1}{100}\,\mathrm{cm^{-1}}$.
5. $F = -100\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Combination of Thin Lenses in Contact, Lens Maker Formula · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q045_8e23f836_04112026.png?v=8e23f836cee5)

---

## Q46

Physics · Kinematics

A bullet from a gun is fired on a rectangular wooden block with velocity $u$. When bullet travels $24\,\mathrm{cm}$ through the block along its length horizontally, velocity of bullet becomes $\frac{u}{3}$. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is

- (1) $28\,\mathrm{cm}$
- (2) $30\,\mathrm{cm}$
- **(3)** $27\,\mathrm{cm}$
- (4) $24\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Assume uniform retardation $a$ inside the block and apply $v^2 = u^2 - 2as$ to the first $24\,\mathrm{cm}$.
2. $u^2 - \left(\frac{u}{3}\right)^2 = 2a(24) \Rightarrow \frac{8u^2}{9} = 48a$.
3. $2a = \frac{8u^2}{9 \times 24} = \frac{u^2}{27}$.
4. For the remaining distance $x$ the bullet goes from $\frac{u}{3}$ to rest: $\left(\frac{u}{3}\right)^2 = 2a x$.
5. $\frac{u^2}{9} = \frac{u^2}{27} x \Rightarrow x = 3\,\mathrm{cm}$.
6. Total length $L = 24 + 3 = 27\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Third Equation of Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q046_6c480557_04112026.png?v=6c4805578d4f)

---

## Q47

Physics · Current Electricity

The resistance of platinum wire at $0\,^\circ\mathrm{C}$ is $2\,\Omega$ and $6.8\,\Omega$ at $80\,^\circ\mathrm{C}$. The temperature coefficient of resistance of the wire is

- **(1)** $3 \times 10^{-2}\,^\circ\mathrm{C}^{-1}$
- (2) $3 \times 10^{-1}\,^\circ\mathrm{C}^{-1}$
- (3) $3 \times 10^{-4}\,^\circ\mathrm{C}^{-1}$
- (4) $3 \times 10^{-3}\,^\circ\mathrm{C}^{-1}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Use $R_T = R_0(1 + \alpha T)$, so $\alpha = \frac{R_T - R_0}{R_0 T}$.
2. $R_T - R_0 = 6.8\,\Omega - 2\,\Omega = 4.8\,\Omega$.
3. $R_0 T = 2\,\Omega \times 80^{\circ}\mathrm{C} = 160\,\Omega\,^{\circ}\mathrm{C}$.
4. $\alpha = \frac{4.8}{160} = 0.03 = 3 \times 10^{-2}\,^{\circ}\mathrm{C}^{-1}$, which is option $1$.

**Subtopic:** Temperature Coefficient of Resistance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q047_157cc18f_04112026.png?v=157cc18f4e4c)

---

## Q48

Physics · Kinematics

A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity $4\,\mathrm{m\,s^{-1}}$. The ball strikes the water surface after $4\,\mathrm{s}$. The height of bridge above water surface is (Take $g = 10\,\mathrm{m\,s^{-2}}$)

- **(1)** $64\,\mathrm{m}$
- (2) $68\,\mathrm{m}$
- (3) $56\,\mathrm{m}$
- (4) $60\,\mathrm{m}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Take upward as positive: $u = +4\,\mathrm{m\,s^{-1}}$, $a = -g = -10\,\mathrm{m\,s^{-2}}$, $t = 4\,\mathrm{s}$.
2. $s = ut - \frac{1}{2}gt^2$.
3. $s = 4 \times 4 - \frac{1}{2} \times 10 \times 4^2 = 16 - 80 = -64\,\mathrm{m}$.
4. The ball ends $64\,\mathrm{m}$ below the launch point, so the bridge height is $64\,\mathrm{m}$, which is option $1$.

**Subtopic:** Freely Falling Bodies · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 10)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q048_e7d6972b_04112026.png?v=e7d6972b786a)

---

## Q49

Physics · Magnetic Effect of Electric Current

A very long conducting wire is bent in a semi-circular shape from $A$ to $B$ as shown in figure. The magnetic field at point $P$ for steady current configuration is given by

![printed figure: Long wire with a semicircular bend of radius R from A to B around point P](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q049_f8f93788_04112026.png?v=f8f93788b483)

*Long wire with a semicircular bend of radius R from A to B around point P*

- **(1)** $\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$ pointed away from page
- (2) $\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$ pointed into the page
- (3) $\frac{\mu_0 i}{4R}$ pointed into the page
- (4) $\frac{\mu_0 i}{4R}$ pointed away from the page

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $P$ is the centre of the semicircle, and $A$, $B$ are the feet of the perpendiculars from $P$ to the two semi-infinite straight wires, each at distance $R$.
2. Semicircular arc (current from $A$ down the left side to $B$): $B_{arc} = \frac{\mu_0 i}{4R}$, directed out of the page by the right-hand rule.
3. Upper semi-infinite wire (current rightward, $P$ below it, ending at $A$): $B_1 = \frac{\mu_0 i}{4\pi R}$, into the page.
4. Lower semi-infinite wire (current leftward, $P$ above it, starting at $B$): $B_2 = \frac{\mu_0 i}{4\pi R}$, into the page.
5. Net: $B = \frac{\mu_0 i}{4R} - \frac{2\mu_0 i}{4\pi R} = \frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$, out of the page, which is option $1$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q049_6d946ace_04112026.png?v=6d946acec3a2)

---

## Q50

Physics · Magnetic Effect of Electric Current

A wire carrying a current $I$ along the positive $x$-axis has length $L$. It is kept in a magnetic field $\vec{B} = (2\hat{i} + 3\hat{j} - 4\hat{k})\,\mathrm{T}$. The magnitude of the magnetic force acting on the wire is

- **(1)** $5\,IL$
- (2) $\sqrt{3}\,IL$
- (3) $3\,IL$
- (4) $\sqrt{5}\,IL$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The force on a straight current-carrying wire is $\vec{F} = I\vec{L} \times \vec{B}$ with $\vec{L} = L\hat{i}$.
2. $\hat{i} \times (2\hat{i} + 3\hat{j} - 4\hat{k}) = 0 + 3\hat{k} + 4\hat{j}$, so $\vec{F} = IL(4\hat{j} + 3\hat{k})$.
3. $|\vec{F}| = IL\sqrt{4^2 + 3^2} = 5\,IL$, which is option $1$.

**Subtopic:** Magnetic Force · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 10)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q050_7ddcdc03_04112026.png?v=7ddcdc033d4c)

---

## Q51

Chemistry · physical · Chemical Kinetics

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R :
In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A reaction can have zero activation energy.
- (Reasons R) The minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value, is called activation energy.

- (1) A is true but R is false
- (2) A is false but R is true
- (3) Both A and R are true and R is the correct explanation of A
- **(4)** Both A and R are true and R is NOT the correct explanation of A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Activation energy is $E_a = E_{threshold} - E_{reactants}$; if reactant molecules already have energy equal to the threshold, $E_a = 0$ (e.g. radical recombination), so Assertion A is true.
2. Reason R states the textbook definition of activation energy (extra energy needed to reach the threshold), so R is true.
3. R merely defines $E_a$ and does not account for why a reaction can have $E_a = 0$, so R is not the correct explanation of A, which is option $4$.

**Subtopic:** Activation Energy · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 11)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q051_d0e38a00_04112026.png?v=d0e38a0015a8)

---

## Q52

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The correct order of energies of molecular orbitals of $\mathrm{N_2}$ molecule, is

- (1) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < \sigma^{*}2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y)$
- (2) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma 2p_z < \sigma^{*}2p_z$
- **(3)** $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$
- (4) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For molecules up to $\mathrm{N_2}$ (total electrons $\le 14$), $2s$-$2p$ mixing raises the energy of $\sigma 2p_z$ above the degenerate $\pi 2p_x = \pi 2p_y$ pair.
2. So the order is $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$, which is option $3$.

**Subtopic:** Energy Level Diagram for Molecular Orbitals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q052_3925ed20_04112026.png?v=3925ed207ca4)

---

## Q53

Chemistry · organic · Haloalkanes and Haloarenes

The given compound [figure] is an example of ______.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q053_10b9fa98_04112026.png?v=10b9fa98b5c5)

- **(1)** Allylic halide
- (2) Vinylic halide
- (3) Benzylic halide
- (4) Aryl halide

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The structure is $\mathrm{C_6H_5{-}CH{=}CH{-}CH(X){-}CH_2CH_3}$.
2. The carbon bearing $X$ is $sp^3$ and is bonded directly to a $\mathrm{C{=}C}$ carbon, so it is an allylic position (not on the ring, not on the vinylic carbon, not next to the ring).
3. Hence the compound is an allylic halide, which is option $1$.

**Subtopic:** Classification, Nomenclature, and Physical Properties of Haloalkanes and Haloarenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q053_b617fc6f_04112026.png?v=b617fc6f7848)

---

## Q54

Chemistry · inorganic · Coordination Compounds – Practice

Homoleptic complex from the following complexes is

- (1) Pentaamminecarbonatocobalt (III) chloride
- (2) Triamminetriaquachromium (III) chloride
- **(3)** Potassium trioxalatoaluminate (III)
- (4) Diamminechloridonitrito-N-platinum (II)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A homoleptic complex has the metal bound to only one kind of ligand.
2. Option 4 is $[\mathrm{Pt(NH_3)_2Cl(NO_2)}]$ with $\mathrm{NH_3}$, $\mathrm{Cl^-}$ and $\mathrm{NO_2^-}$: heteroleptic.
3. Option 1 is $[\mathrm{Co(NH_3)_5(CO_3)}]\mathrm{Cl}$ with $\mathrm{NH_3}$ and $\mathrm{CO_3^{2-}}$: heteroleptic.
4. Option 2 is $[\mathrm{Cr(NH_3)_3(H_2O)_3}]\mathrm{Cl_3}$ with $\mathrm{NH_3}$ and $\mathrm{H_2O}$: heteroleptic.
5. Option 3 is $\mathrm{K_3[Al(C_2O_4)_3]}$ with only $\mathrm{C_2O_4^{2-}}$ ligands: homoleptic, so the answer is option $3$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 11)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q054_8a9e82e3_04112026.png?v=8a9e82e319da)

---

## Q55

Chemistry · physical · Basic Concepts of Chemistry

The **right** option for the mass of $\mathrm{CO_2}$ produced by heating $20\,\mathrm{g}$ of $20\%$ pure limestone is (Atomic mass of $\mathrm{Ca} = 40$) $\left[\mathrm{CaCO_3} \xrightarrow{1200\,\mathrm{K}} \mathrm{CaO} + \mathrm{CO_2}\right]$

- (1) $2.64\,\mathrm{g}$
- (2) $1.32\,\mathrm{g}$
- (3) $1.12\,\mathrm{g}$
- **(4)** $1.76\,\mathrm{g}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Mass of pure $\mathrm{CaCO_3} = 0.20 \times 20\,\mathrm{g} = 4\,\mathrm{g}$.
2. Molar mass of $\mathrm{CaCO_3} = 40 + 12 + 3(16) = 100\,\mathrm{g\,mol^{-1}}$.
3. $n(\mathrm{CaCO_3}) = \frac{4}{100} = 0.04\,\mathrm{mol}$.
4. From $\mathrm{CaCO_3} \rightarrow \mathrm{CaO} + \mathrm{CO_2}$ (1:1), $n(\mathrm{CO_2}) = 0.04\,\mathrm{mol}$.
5. $m(\mathrm{CO_2}) = 0.04 \times 44 = 1.76\,\mathrm{g}$, which is option $4$.

**Subtopic:** Stoichiometry · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 12)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q055_00d048f1_04112026.png?v=00d048f16f13)

---

## Q56

Chemistry · physical · Structure of Atom

The relation between $n_m$, ($n_m$ = the number of permissible values of magnetic quantum number ($m$)) for a given value of azimuthal quantum number ($l$), is

- (1) $n_m = 2l^2 + 1$
- (2) $n_m = l + 2$
- **(3)** $l = \frac{n_m - 1}{2}$
- (4) $l = 2n_m + 1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a given $l$, $m$ takes the values $-l, \ldots, 0, \ldots, +l$.
2. So $n_m = 2l + 1$.
3. Rearranging, $l = \frac{n_m - 1}{2}$, which is option $3$.

**Subtopic:** Quantum Numbers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q056_c010f8b7_04112026.png?v=c010f8b79351)

---

## Q57

Chemistry · physical · Structure of Atom

Select the correct statements from the following
Choose the correct answer from the options given below

- (A) Atoms of all elements are composed of two fundamental particles.
- (B) The mass of the electron is $9.10939 \times 10^{-31}\,\mathrm{kg}$.
- (C) All the isotopes of a given element show same chemical properties:
- (D) Protons and electrons are collectively known as nucleons.
- (E) Dalton's atomic theory, regarded the atom as an ultimate particles of matter

- (1) A and E only
- **(2)** B, C and E only
- (3) A, B and C only
- (4) C, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A is false: atoms are made of three fundamental particles (electron, proton, neutron), not two.
2. B is true: $m_e = 9.10939 \times 10^{-31}\,\mathrm{kg}$.
3. C is true: isotopes have the same atomic number and electronic configuration, so they show the same chemical properties.
4. D is false: nucleons are protons and neutrons, not protons and electrons.
5. E is true: Dalton's atomic theory regarded the atom as the ultimate, indivisible particle of matter.
6. The correct statements are B, C and E, which is option $2$.

**Subtopic:** Discovery of Sub-Atomic Particles, Isobars and Isotopes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q057_59c177a3_04112026.png?v=59c177a34462)

---

## Q58

Chemistry · physical · Surface Chemistry

Which one is an example of heterogenous catalysis?

- (1) Decomposition of ozone in presence of nitrogen monoxide
- **(2)** Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron
- (3) Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen
- (4) Hydrolysis of sugar catalysed by $\mathrm{H^+}$ ions

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Heterogeneous catalysis means the catalyst is in a different phase from the reactants.
2. Option 4: sugar solution and $\mathrm{H^{+}}$ ions are both in the aqueous phase, so homogeneous.
3. Option 1: $\mathrm{O_3(g)}$ with $\mathrm{NO(g)}$ are both gases, so homogeneous.
4. Option 3: $\mathrm{2SO_2(g) + O_2(g) \xrightarrow{NO(g)} 2SO_3(g)}$ is all gas phase, so homogeneous (lead chamber process).
5. Option 2: $\mathrm{N_2(g) + 3H_2(g) \xrightarrow{Fe(s)} 2NH_3(g)}$ has a solid catalyst with gaseous reactants, so heterogeneous, which is option $2$.

**Subtopic:** Homogeneous and Heterogeneous Catalysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q058_a89eab65_04112026.png?v=a89eab65aba3)

---

## Q59

Chemistry · organic · Hydrocarbons

Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is :

- (1) $30$
- (2) $18$
- (3) $16$
- **(4)** $32$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Heating sodium ethanoate with NaOH and CaO (soda lime) is decarboxylation: $\mathrm{CH_3COONa + NaOH \xrightarrow{CaO,\,\Delta} CH_4 + Na_2CO_3}$.
2. Molar mass of $\mathrm{CH_4} = 12 + 4(1) = 16\,\mathrm{g\,mol^{-1}}$.
3. Mass of 2 mol $= 2 \times 16 = 32\,\mathrm{g}$, which is option $4$.

**Subtopic:** Preparation of Alkane · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 13)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q059_bddb964d_04112026.png?v=bddb964d1187)

---

## Q60

Chemistry · organic · General Organic Chemistry

The number of $\sigma$ bonds, $\pi$ bonds and lone pair of electrons in pyridine, respectively are:

- **(1)** 11, 3, 1
- (2) 12, 2, 1
- (3) 11, 2, 0
- (4) 12, 3, 0

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Pyridine is $\mathrm{C_5H_5N}$: a six-membered aromatic ring with one N and five C–H units.
2. Ring $\sigma$ bonds: $6$; C–H $\sigma$ bonds: $5$; total $\sigma = 6 + 5 = 11$.
3. The aromatic ring has $3$ alternating double bonds, so $\pi = 3$.
4. The $sp^2$ N carries $1$ lone pair (in the ring plane, not part of the aromatic sextet).
5. $(11, 3, 1)$ is option $1$.

**Subtopic:** Aromaticity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q060_2996e5e5_04112026.png?v=2996e5e5ea02)

---

## Q61

Chemistry · organic · Polymers

Which amongst the following molecules on polymerization produces neoprene?

- (1) $\mathrm{H_2C=CH-C\equiv CH}$
- (2) $\mathrm{H_2C=\overset{\displaystyle CH_3}{\overset{|}{C}}-CH=CH_2}$
- (3) $\mathrm{H_2C=CH-CH=CH_2}$
- **(4)** $\mathrm{H_2C=\overset{\displaystyle Cl}{\overset{|}{C}}-CH=CH_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Neoprene is the addition polymer of chloroprene, $\mathrm{H_2C=C(Cl)-CH=CH_2}$ (2-chloro-1,3-butadiene), which is option $4$.

**Subtopic:** Natural Rubber (cis-1,4-Polyisoprene) and Vulcanisation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q061_02909df4_04112026.png?v=02909df49a8c)

---

## Q62

Chemistry · inorganic · The D- and F-Block Elements – Practice

The stability of $\mathrm{Cu^{2+}}$ is more than $\mathrm{Cu^{+}}$ salts in aqueous solution due to

- **(1)** Hydration energy
- (2) Second ionisation enthalpy
- (3) First ionisation enthalpy
- (4) Enthalpy of atomization

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The greater stability of $\mathrm{Cu^{2+}}(aq)$ over $\mathrm{Cu^{+}}(aq)$ comes from the much more negative $\Delta_{hyd}H$ of $\mathrm{Cu^{2+}}$, which more than compensates for the second ionisation enthalpy of Cu, so the answer is option $1$.

**Subtopic:** Oxidation State · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q062_6fdee3cc_04112026.png?v=6fdee3cc1f6b)

---

## Q63

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Complete the following reaction [C] is ________

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q063_26a175a6_04112026.png?v=26a175a631d7)

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q063_option_1_41d1f423_04112026.png?v=41d1f423ca3f) — $\mathrm{CHO}$
- **(2)** ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q063_option_2_b3c6db94_04112026.png?v=b3c6db94f94c) — $\mathrm{COOH}$
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q063_option_3_2bfec110_04112026.png?v=2bfec1108580) — $\mathrm{OH}$
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q063_option_4_66c32455_04112026.png?v=66c32455e088) — $\mathrm{COOH}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $[A]$ cyclohexanone adds $\mathrm{HCN}$ to give the cyanohydrin $[B]$, 1-hydroxycyclohexane-1-carbonitrile.
2. Hot conc. $\mathrm{H_2SO_4}$ (aqueous acid) hydrolyses $-\mathrm{C{\equiv}N}$ to $-\mathrm{COOH}$.
3. Conc. $\mathrm{H_2SO_4}$ with $\Delta$ also dehydrates the tertiary $-\mathrm{OH}$, forming a $\mathrm{C{=}C}$ conjugated with $-\mathrm{COOH}$.
4. $[C]$ = cyclohex-1-ene-1-carboxylic acid, which is option $2$.

**Subtopic:** Nucleophilic Addition Reactions, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q063_1079f4c1_04112026.png?v=1079f4c1921e)

---

## Q64

Chemistry · organic · Amines

Which of the following reactions will NOT give primary amine as the product?

- **(1)** $\mathrm{CH_3NC} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$
- (2) $\mathrm{CH_3CONH_2} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$
- (3) $\mathrm{CH_3CONH_2} \xrightarrow{\mathrm{Br_2/KOH}} \text{Product}$
- (4) $\mathrm{CH_3CN} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Option 4: $\mathrm{CH_3C{\equiv}N \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
2. Option 1: $\mathrm{CH_3N{\equiv}C \xrightarrow{LiAlH_4} CH_3NHCH_3}$, a secondary amine.
3. Option 2: $\mathrm{CH_3CONH_2 \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
4. Option 3: Hofmann bromamide degradation, $\mathrm{CH_3CONH_2 \xrightarrow{Br_2/KOH} CH_3NH_2}$, a primary amine.
5. Only option $1$ does not give a primary amine.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q064_3873de76_04112026.png?v=3873de769b46)

---

## Q65

Chemistry · inorganic · The p–Block Elements

> ⚠ The booklet keys (4) "Both A and R are true and R is NOT the correct explanation of A", but Reason R says helium has HIGH solubility in O2, and the publisher's own printed solution (2023_E5 q068) says helium is used "because of its very low solubility in blood", which makes R false. By the publisher's own reasoning the answer is "A is true but R is false". The printed key is kept as printed. Same question as 2023_F1 q064.

> ⚠ The independent solve chose (1); the booklet prints (4).

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R
In the light of the above statements, choose the correct answer from the options given below

- (Assertion A) Helium is used to dilute oxygen in diving apparatus.
- (Reason R) Helium has high solubility in $\mathrm{O_2}$.

- (1) A is true but R is false
- (2) A is false but R is true
- (3) Both A and R are true and R correct explanation of A
- **(4)** Both A and R are true and R is NOT the correct explanation of A

**Answer** — booklet: (4) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Assertion A: helium is mixed with $\mathrm{O_2}$ in diving apparatus, so A is true.
2. Helium is used because of its very low solubility in blood, which avoids the bends; 'high solubility in $\mathrm{O_2}$' is not the property, so R is false.
3. A true and R false gives option $1$.

**Subtopic:** Applications & Special Features of Group 18 · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q065_97f8edf0_04112026.png?v=97f8edf0e4ff)

---

## Q66

Chemistry · organic · Amines

Identify the product in the following reaction:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q066_f1bce453_04112026.png?v=f1bce453488d)

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q066_option_1_3fb9ae42_04112026.png?v=3fb9ae42856a)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q066_option_2_03682065_04112026.png?v=03682065124e)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q066_option_3_2f90fd07_04112026.png?v=2f90fd070111)
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q066_option_4_3e44683b_04112026.png?v=3e44683b2267)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Sandmeyer reaction: $\mathrm{C_6H_5N_2^+Cl^-} \xrightarrow{\mathrm{Cu_2Br_2/HBr}} \mathrm{C_6H_5Br} + \mathrm{N_2}$.
2. Grignard formation: $\mathrm{C_6H_5Br} \xrightarrow{\mathrm{Mg/dry\ ether}} \mathrm{C_6H_5MgBr}$.
3. Hydrolysis: $\mathrm{C_6H_5MgBr} + \mathrm{H_2O} \rightarrow \mathrm{C_6H_6} + \mathrm{Mg(OH)Br}$.
4. The product is benzene, which is option $4$.

**Subtopic:** Chemical Reactions of Diazonium Salts and Coupling Reactions · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 14)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q066_26304e1e_04112026.png?v=26304e1ed872)

---

## Q67

Chemistry · organic · Alcohols, Phenols and Ethers

Consider the following reaction and identify the product (P).
$\mathrm{CH_3-CH(CH_3)-CH(OH)-CH_3} \xrightarrow{\mathrm{HBr}}$ Product (P)
3-Methylbutan-2-ol

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q067_a4fe6355_04112026.png?v=a4fe6355ca66)

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q067_option_1_4d9ecc02_04112026.png?v=4d9ecc02e04f) — $\mathrm{CH_3-CH(CH_3)-CH(Br)-CH_3}$
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q067_option_2_60b617a5_04112026.png?v=60b617a5493a) — $\mathrm{CH_3-C(CH_3)_2-CH_2Br}$
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q067_option_3_b9229a8b_04112026.png?v=b9229a8b8bd6) — $\mathrm{CH_3-C(Br)(CH_3)-CH_2-CH_3}$
- (4) $\mathrm{CH_3CH=CH-CH_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. HBr protonates the $-\mathrm{OH}$: $\mathrm{(CH_3)_2CH-CH(OH_2^+)-CH_3}$.
2. Loss of $\mathrm{H_2O}$ gives the secondary carbocation $\mathrm{(CH_3)_2CH-\overset{+}{C}H-CH_3}$.
3. A 1,2-hydride shift from C-3 gives the more stable tertiary carbocation $\mathrm{(CH_3)_2\overset{+}{C}-CH_2-CH_3}$.
4. $\mathrm{Br^-}$ attacks the tertiary carbon: $\mathrm{CH_3-C(Br)(CH_3)-CH_2-CH_3}$ (2-bromo-2-methylbutane), which is option $3$.

**Subtopic:** Reactions of Alcohols · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q067_44ca2d35_04112026.png?v=44ca2d3541b7)

---

## Q68

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify product (A) in the following reaction:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q068_76f33e59_04112026.png?v=76f33e59a7e4)

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q068_option_1_45b66089_04112026.png?v=45b66089ae25)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q068_option_2_36ff0a36_04112026.png?v=36ff0a36b5f6)
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q068_option_3_cdd50691_04112026.png?v=cdd5069114fd)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q068_option_4_be9d0dc3_04112026.png?v=be9d0dc32c76)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Zn-Hg with conc. HCl is the Clemmensen reduction, which converts a ketone $>C=O$ into $>CH_2$.
2. Both acetyl groups react: $-COCH_3 \rightarrow -CH_2CH_3$ on the cyclohexane ring and on the benzene ring.
3. Two carbonyl oxygens removed matches the $2H_2O$ shown in the equation.
4. The product with two ethyl groups and no OH is option $3$.

**Subtopic:** Reduction of Aldehydes and Ketones · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q068_98584fb8_04112026.png?v=98584fb8d4f4)

---

## Q69

Chemistry · inorganic · The p–Block Elements

Taking stability as the factor, which one of the following represents correct relationship?

- (1) $\mathrm{AlCl} > \mathrm{AlCl_3}$
- **(2)** $\mathrm{TlI} > \mathrm{TlI_3}$
- (3) $\mathrm{TlCl_3} > \mathrm{TlCl}$
- (4) $\mathrm{InI_3} > \mathrm{InI}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Down group 13 the inert pair effect makes the $+1$ oxidation state increasingly stable relative to $+3$.
2. For Al, $+3$ is the stable state, so $\mathrm{AlCl_3} > \mathrm{AlCl}$; option $1$ is wrong.
3. For Tl, $+1$ is more stable than $+3$, so $\mathrm{TlCl} > \mathrm{TlCl_3}$ (option $3$ wrong) and $\mathrm{TlI} > \mathrm{TlI_3}$, which is option $2$.
4. Option $4$ ($\mathrm{InI_3} > \mathrm{InI}$) is not the intended relationship; the clear inert-pair case is Tl, so the answer is option $2$.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q069_8e166a63_04112026.png?v=8e166a63beab)

---

## Q70

Chemistry · physical · Electrochemistry

The conductivity of centimolar solution of $\mathrm{KCl}$ at $25^{\circ}\mathrm{C}$ is $0.0210\,\mathrm{ohm^{-1}\,cm^{-1}}$ and the resistance of the cell containing the solution at $25^{\circ}\mathrm{C}$ is $60\,\mathrm{ohm}$. The value of cell constant is

- **(1)** $1.26\,\mathrm{cm^{-1}}$
- (2) $3.34\,\mathrm{cm^{-1}}$
- (3) $1.34\,\mathrm{cm^{-1}}$
- (4) $3.28\,\mathrm{cm^{-1}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Conductivity relates to cell constant by $\kappa = \frac{G^*}{R}$, so $G^* = \kappa R$.
2. $G^* = 0.0210\,\mathrm{ohm^{-1}\,cm^{-1}} \times 60\,\mathrm{ohm} = 1.26\,\mathrm{cm^{-1}}$, which is option $1$.

**Subtopic:** Some Important Terms Related to Conductance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q070_6e3dfa27_04112026.png?v=6e3dfa27e548)

---

## Q71

Chemistry · inorganic · The s-Block Elements

Which one of the following statements is **correct**?

- (1) The bone in human body is an inert and unchanging substance
- (2) $\mathrm{Mg}$ plays roles in neuromuscular function and interneuronal transmission
- **(3)** The daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ in the human body is estimated to be $0.2\text{-}0.3\,\mathrm{g}$
- (4) All enzymes that utilise ATP in phosphate transfer require $\mathrm{Ca}$ as the cofactor

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Option $4$: enzymes that use ATP in phosphate transfer need $\mathrm{Mg}$ as cofactor, not $\mathrm{Ca}$, so it is false.
2. Option $1$: bone is not inert; it is constantly being solubilised and redeposited, so it is false.
3. Option $2$: the role in neuromuscular function and interneuronal transmission is that of $\mathrm{Ca}$, not $\mathrm{Mg}$, so it is false.
4. Option $3$: the daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ is $200\text{-}300\,\mathrm{mg} = 0.2\text{-}0.3\,\mathrm{g}$, so it is correct, which is option $3$.

**Subtopic:** Biological Importance of Sodium, Potassium, Magnesium and Calcium · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 16)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q071_4a3a29c5_04112026.png?v=4a3a29c5f55d)

---

## Q72

Chemistry · inorganic · The p–Block Elements

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Coke | I | Carbon atoms are $\mathrm{sp^3}$ hybridised |
| B | Diamond | II | Used as a dry lubricant |
| C | Fullerene | III | Used as a reducing agent |
| D | Graphite | IV | Cage like molecules |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-III, B-IV, C-I, D-II
- (3) A-II, B-IV, C-I, D-III
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Coke is used as a reducing agent in metallurgy, so $A \to III$.
2. In diamond each carbon is $\mathrm{sp^{3}}$ hybridised, tetrahedrally bonded, so $B \to I$.
3. Fullerenes such as $\mathrm{C_{60}}$ are cage-like molecules, so $C \to IV$.
4. Graphite's layers slide over each other, so it is used as a dry lubricant: $D \to II$.
5. $A$-III, $B$-I, $C$-IV, $D$-II matches option $1$.

**Subtopic:** Catenation & Allotropy Group 14 · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 16)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q072_224179e2_04112026.png?v=224179e2afa5)

---

## Q73

Chemistry · inorganic · The s-Block Elements

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Metallic sodium dissolves in liquid ammonia giving a deep blue solution, which is paramagnetic.
- (Reason R) The deep blue solution is due to the formation of amide.

- **(1)** A is true but R is false
- (2) A is false but R is true
- (3) Both A and R are true and R is the correct explanation of A
- (4) Both A and R are true but R is NOT the correct explanation of A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{Na + (x+y)NH_3 \rightarrow [Na(NH_3)_x]^+ + [e(NH_3)_y]^-}$; the ammoniated electron gives the deep blue colour and makes the solution paramagnetic, so A is true.
2. The blue colour is due to ammoniated electrons, not amide; amide ($\mathrm{NaNH_2}$) forms only on standing ($\mathrm{Na^+ + e^- + NH_3 \rightarrow NaNH_2 + \tfrac{1}{2}H_2}$) and the blue colour is lost, so R is false: option $1$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q073_0e6b459e_04112026.png?v=0e6b459e9a16)

---

## Q74

Chemistry · inorganic · Hydrogen

Which of the following statements are NOT correct?
Choose the most appropriate answer from the options given below:

- (A) Hydrogen is used to reduce heavy metal oxides to metals.
- (B) Heavy water is used to study reaction mechanism.
- (C) Hydrogen is used to make saturated fats from oils.
- (D) The $\mathrm{H{-}H}$ bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements.
- (E) Hydrogen reduces oxides of metals that are more active than iron.

- **(1)** D, E only
- (2) A, B, C only
- (3) B, C, D, E only
- (4) B, D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A is correct: hydrogen reduces heavy metal oxides to metals.
2. B is correct: heavy water ($\mathrm{D_2O}$) is used to study reaction mechanisms.
3. C is correct: hydrogenation of vegetable oils with $\mathrm{H_2}$ gives saturated fats.
4. D is NOT correct: the $\mathrm{H-H}$ bond dissociation enthalpy ($435.88\,\mathrm{kJ\,mol^{-1}}$) is the highest for a single bond between two atoms of any element, not the lowest.
5. E is NOT correct: hydrogen reduces oxides of metals less active than iron, not more active.
6. The incorrect statements are D and E, which is option $1$.

**Subtopic:** Isotopes of Hydrogen and Properties of Dihydrogen · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q074_4aec7836_04112026.png?v=4aec783641c1)

---

## Q75

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The element expected to form largest ion to achieve the nearest noble gas configuration is

- **(1)** $\mathrm{N}$
- (2) $\mathrm{Na}$
- (3) $\mathrm{O}$
- (4) $\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. To reach the nearest noble gas configuration (Ne) the elements form $\mathrm{N^{3-}}$, $\mathrm{O^{2-}}$, $\mathrm{F^{-}}$ and $\mathrm{Na^{+}}$, which all have $10$ electrons.
2. For isoelectronic ions, radius falls as nuclear charge rises: $Z = 7 < 8 < 9 < 11$.
3. So $\mathrm{N^{3-}} > \mathrm{O^{2-}} > \mathrm{F^{-}} > \mathrm{Na^{+}}$; the largest ion comes from $\mathrm{N}$, which is option $1$.

**Subtopic:** Trends in Chemical Properties – Atomic and Ionic Radius · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q075_273aaf5b_04112026.png?v=273aaf5b52cb)

---

## Q76

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with $\mathrm{Fe^{3+}}$ due to the formation of

- (1) $\mathrm{[Fe(CN)_5NOS]^{4-}}$
- **(2)** $\mathrm{[Fe(SCN)]^{2+}}$
- (3) $\mathrm{Fe_4[Fe(CN)_6]_3\cdot xH_2O}$
- (4) $\mathrm{NaSCN}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. When N and S are both present, sodium fusion gives $\mathrm{NaSCN}$; with $\mathrm{Fe^{3+}}$ this forms $\mathrm{[Fe(SCN)]^{2+}}$, which is blood red, so the answer is option $2$.

**Subtopic:** Detection of Elements · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q076_bf97776c_04112026.png?v=bf97776c27ef)

---

## Q77

Chemistry · physical · States of Matter

Intermolecular forces are forces of attraction and repulsion between interacting particles that will include :
Choose the most appropriate answer from the options given below :

- (A) dipole - dipole forces
- (B) dipole - induced dipole forces
- (C) hydrogen bonding
- (D) covalent bonding
- (E) dispersion forces

- **(1)** A, B, C, E are correct
- (2) A, C, D, E are correct
- (3) B, C, D, E are correct
- (4) A, B, C, D are correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Dipole-dipole, dipole-induced dipole, hydrogen bonding and dispersion (London) forces act between molecules, so A, B, C and E are intermolecular forces.
2. Covalent bonding (D) holds atoms together within a molecule, so it is intramolecular and is excluded.
3. The correct set is A, B, C, E, which is option $1$.

**Subtopic:** Intermolecular Forces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q077_8e35dfef_04112026.png?v=8e35dfefbd75)

---

## Q78

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Amongst the following the total number of species NOT having eight electrons around central atom in its outermost shell, is $\mathrm{NH_3}$, $\mathrm{AlCl_3}$, $\mathrm{BeCl_2}$, $\mathrm{CCl_4}$, $\mathrm{PCl_5}$ :

- (1) 4
- (2) 1
- **(3)** 3
- (4) 2

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: N has 3 bond pairs + 1 lone pair $= 8$ electrons (octet).
2. $\mathrm{AlCl_3}$: Al has 3 bond pairs $= 6$ electrons (incomplete octet).
3. $\mathrm{BeCl_2}$: Be has 2 bond pairs $= 4$ electrons (incomplete octet).
4. $\mathrm{CCl_4}$: C has 4 bond pairs $= 8$ electrons (octet).
5. $\mathrm{PCl_5}$: P has 5 bond pairs $= 10$ electrons (expanded octet).
6. Species not having 8 electrons: $\mathrm{AlCl_3}, \mathrm{BeCl_2}, \mathrm{PCl_5}$ $= 3$, which is option $3$.

**Subtopic:** Octet Rule · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q078_36cf8b13_04112026.png?v=36cf8b13d40e)

---

## Q79

Chemistry · physical · The Solid State

A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy $1/3$ of tetrahedral voids. If the formula of the compound is $\mathrm{A_xB_y}$, then the value of $x + y$ is in option

- (1) $3$
- (2) $2$
- **(3)** $5$
- (4) $4$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Let the number of B atoms in the ccp lattice be $N$.
2. A ccp lattice has $2N$ tetrahedral voids.
3. A occupies $\frac{1}{3}$ of them: $n_A = \frac{1}{3}(2N) = \frac{2N}{3}$.
4. $A : B = \frac{2N}{3} : N = 2 : 3$, so the formula is $\mathrm{A_2B_3}$.
5. $x + y = 2 + 3 = 5$, which is option $3$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q079_d8745854_04112026.png?v=d87458544f60)

---

## Q80

Chemistry · physical · States of Matter

Which amongst the following options are correct graphical representation of Boyle’s law?

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q080_option_1_18501f11_04112026.png?v=18501f1165b7) — [graph]
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q080_option_2_bf04ac54_04112026.png?v=bf04ac540f5d) — [graph]
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q080_option_3_b7d4de04_04112026.png?v=b7d4de04238b) — [graph]
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q080_option_4_fbfea634_04112026.png?v=fbfea6348773) — [graph]

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Boyle's law: at constant $T$ and $n$, $PV = nRT = \text{const}$.
2. So $P = nRT \cdot \frac{1}{V}$: a plot of $P$ vs $\frac{1}{V}$ is a straight line through the origin with slope $nRT$.
3. Higher $T$ gives a larger slope, so with $T_3 > T_2 > T_1$ the $T_3$ line must be steepest; option $4$ shows this.
4. Option $1$ draws $P$ vs $\frac{1}{V}$ as curves, which contradicts the linear relation.
5. Option $2$ plots $P$ vs $T$ at constant $V$ (Gay-Lussac's law), not Boyle's law.
6. Option $3$ plots $P$ vs $V$ hyperbolas, but the outermost isotherm should be the highest temperature $T_3$; it is labelled $T_1$, so the order is wrong.
7. Only option $4$ is a correct Boyle's law plot.

**Subtopic:** Gas Laws · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 18)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q080_bf7b7c0b_04112026.png?v=bf7b7c0b7b3e)

---

## Q81

Chemistry · organic · Chemistry in Everyday Life

Some tranquilizers are listed below. Which one from the following belongs to barbiturates?

- (1) Valium
- **(2)** Veronal
- (3) Chlordiazepoxide
- (4) Meprobamate

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Barbiturates are derivatives of barbituric acid; NCERT lists veronal, amytal, nembutal, luminal and seconal as barbiturate tranquilizers, so Veronal (option $2$) is the barbiturate while meprobamate, Valium and chlordiazepoxide are non-barbiturate tranquilizers.

**Subtopic:** Tranquilizers · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 18)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q081_9ac5816e_04112026.png?v=9ac5816e64ff)

---

## Q82

Chemistry · physical · Electrochemistry

> ⚠ The independent solve chose (3); the booklet prints (4).

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R
In the light of the above statements, choose the correct answer from the options given below

- (Assertion A) In equation $\Delta_r G = -nFE_{\mathrm{cell}}$, value of $\Delta_r G$ depends on n.
- (Reasons R) $E_{\mathrm{cell}}$ is an intensive property and $\Delta_r G$ is an extensive property.

- (1) A is true but R is false
- (2) A is false but R is true
- (3) Both A and R are true and R is the correct explanation of A
- **(4)** Both A and R are true and R is NOT the correct explanation of A

**Answer** — booklet: (4) · independent solve: (3) · differs

**Solved independently** (answer withheld)

1. $\Delta_r G = -nFE_{\mathrm{cell}}$, where $n$ is the number of moles of electrons transferred in the reaction as written, so $\Delta_r G$ changes with $n$: A is true.
2. $E_{\mathrm{cell}}$ does not depend on the amount of reactants (intensive), while $\Delta_r G$ scales with the amount of reaction (extensive): R is true.
3. Because $E_{\mathrm{cell}}$ is fixed but $\Delta_r G$ must scale with amount, the factor $n$ carries that dependence, so R correctly explains A, which is option $3$.

**Subtopic:** Nernst Equation · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 18)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q082_8e370fd3_04112026.png?v=8e370fd3dc68)

---

## Q83

Chemistry · organic · Biomolecules

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) A unit formed by the attachment of a base to $1'$ position of sugar is known as nucleoside.
- (Statement II) When nucleoside is linked to phosphorous acid at $5'$-position of sugar moiety, we get nucleotide.

- **(1)** Statement I is true but Statement II is false
- (2) Statement I is false but Statement II is true
- (3) Both Statement I and Statement II are true
- (4) Both Statement I and Statement II are false

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A nitrogenous base attached at the $1'$ position of the pentose sugar forms a nucleoside, so Statement I is true.
2. NCERT: a nucleotide forms when a nucleoside is linked to phosphoric acid ($\mathrm{H_3PO_4}$) at the $5'$ position; Statement II says phosphorous acid ($\mathrm{H_3PO_3}$), so as worded it is false.
3. Statement I true, Statement II false, which is option $1$.

**Subtopic:** Structure and Function of Nucleic Acids · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 18)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q083_9dd3ae89_04112026.png?v=9dd3ae89741a)

---

## Q84

Chemistry · physical · Chemical Kinetics

For a certain reaction, the rate $= k[\mathrm{A}]^{2}[\mathrm{B}]$, when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would

- **(1)** Increase by a factor of nine
- (2) Increase by a factor of three
- (3) Decrease by a factor of nine
- (4) Increase by a factor of six

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Initial rate: $r = k[\mathrm{A}]^2[\mathrm{B}]$.
2. With $[\mathrm{A}]$ tripled and $[\mathrm{B}]$ constant: $r' = k(3[\mathrm{A}])^2[\mathrm{B}]$.
3. $r' = 9k[\mathrm{A}]^2[\mathrm{B}] = 9r$, so the rate increases by a factor of nine, which is option $1$.

**Subtopic:** Rate Expression · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q084_4dd77f19_04112026.png?v=4dd77f19303a)

---

## Q85

Chemistry · physical · Ionic Equilibrium

Amongst the given options which of the following molecules/ ion acts as a Lewis acid?

- **(1)** $\mathrm{BF_3}$
- (2) $\mathrm{OH^-}$
- (3) $\mathrm{NH_3}$
- (4) $\mathrm{H_2O}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A Lewis acid is an electron-pair acceptor.
2. In $\mathrm{BF_3}$, boron has only $6$ valence electrons (incomplete octet), so it can accept a lone pair: Lewis acid.
3. $\mathrm{H_2O}$, $\mathrm{OH^-}$ and $\mathrm{NH_3}$ all carry lone pairs and donate them: Lewis bases.
4. Hence the answer is $\mathrm{BF_3}$, option $1$.

**Subtopic:** Lewis Acids and Bases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q085_e4398994_04112026.png?v=e4398994625b)

---

## Q86

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which of the following statements are INCORRECT?
Choose the correct answer from the options given below:

- (A) All the transition metals except scandium form $\mathrm{MO}$ oxides which are ionic.
- (B) The highest oxidation number corresponding to the group number in transition metal oxides is attained in $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$.
- (C) Basic character increases from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_4}$ to $\mathrm{V_2O_5}$.
- (D) $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO_4^{3-}}$ salts.
- (E) $\mathrm{CrO}$ is basic but $\mathrm{Cr_2O_3}$ is amphoteric.

- **(1)** C and D only
- (2) B and C only
- (3) A and E only
- (4) B and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A: all transition metals except Sc form ionic $\mathrm{MO}$ oxides, so A is correct.
2. B: oxides from $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$ show the highest oxidation state equal to the group number, so B is correct.
3. C: as oxidation state of V rises, $\mathrm{V_2O_3}$ (basic) $\to$ $\mathrm{V_2O_4}$ (less basic) $\to$ $\mathrm{V_2O_5}$ (amphoteric), so basic character decreases and C is incorrect.
4. D: $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO^{2+}}$ salts, not $\mathrm{VO_4^{3-}}$, so D is incorrect.
5. E: $\mathrm{CrO}$ is basic and $\mathrm{Cr_2O_3}$ is amphoteric, so E is correct.
6. Incorrect statements are C and D, which is option $1$.

**Subtopic:** Transition Elements (d-Block) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 19)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q086_621b0929_04112026.png?v=621b092917f7)

---

## Q87

Chemistry · physical · The Solid State

What fraction of one edge centred octahedral void lies in one unit cell of fcc?

- **(1)** $\frac{1}{4}$
- (2) $\frac{1}{12}$
- (3) $\frac{1}{2}$
- (4) $\frac{1}{3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. An octahedral void at an edge centre of the fcc cell lies on an edge shared by $4$ unit cells.
2. Fraction belonging to one unit cell $= \frac{1}{4}$, which is option $1$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q087_76542663_04112026.png?v=7654266321a4)

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

- (1) A–I, B–III, C–IV, D–II
- (2) A–III, B–IV, C–II, D–I
- (3) A–I, B–III, C–II, D–IV
- **(4)** A–III, B–IV, C–I, D–II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Peroxodisulphuric acid $\mathrm{H_2S_2O_8}$: $\mathrm{HO{-}S(O_2){-}O{-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}O{-}S}$, so $A \to III$.
2. Sulphuric acid $\mathrm{H_2SO_4}$: $\mathrm{(HO)_2S(=O)_2}$ has two $\mathrm{S{-}OH}$ and two $\mathrm{S{=}O}$, so $B \to IV$.
3. Pyrosulphuric acid $\mathrm{H_2S_2O_7}$: $\mathrm{HO{-}S(O_2){-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}S}$, so $C \to I$.
4. Sulphurous acid $\mathrm{H_2SO_3}$: $\mathrm{(HO)_2S{=}O}$ has two $\mathrm{S{-}OH}$ and one $\mathrm{S{=}O}$, so $D \to II$.
5. $A{-}III,\ B{-}IV,\ C{-}I,\ D{-}II$ is option $4$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q088_b868e4da_04112026.png?v=b868e4da68c7)

---

## Q89

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the major product obtained in the following reaction: [figure] $+\,2\left[\mathrm{Ag(NH_3)_2}\right]^{+}\,+\,3\,{}^{-}\mathrm{OH}\xrightarrow{\Delta}$ major product

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q089_4f60714d_04112026.png?v=4f60714df2fa)

- **(1)** ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q089_option_1_054f26d9_04112026.png?v=054f26d9f1f5)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q089_option_2_3cf3e09c_04112026.png?v=3cf3e09c4b28)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q089_option_3_241dbf73_04112026.png?v=241dbf7306d6)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q089_option_4_feb66f92_04112026.png?v=feb66f9258fd)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The substrate is 2-acetylbenzaldehyde: it carries one $-\mathrm{CHO}$ group and one $-\mathrm{COCH_3}$ group.
2. Tollens' reagent $[\mathrm{Ag(NH_3)_2}]^{+}/{}^{-}\mathrm{OH}$ is a mild oxidant that oxidises aldehydes but not ketones: $\mathrm{RCHO} + 2[\mathrm{Ag(NH_3)_2}]^{+} + 3\,{}^{-}\mathrm{OH} \rightarrow \mathrm{RCOO^-} + 2\mathrm{Ag} + 4\mathrm{NH_3} + 2\mathrm{H_2O}$.
3. The stoichiometry $2[\mathrm{Ag(NH_3)_2}]^{+}$ and $3\,{}^{-}\mathrm{OH}$ matches exactly one aldehyde oxidation, and no reducing agent is present, so neither carbonyl is reduced to $-\mathrm{OH}$.
4. Product: $\mathrm{-CHO} \rightarrow \mathrm{-COO^-}$ with the acetyl group intact, i.e. 2-acetylbenzoate, which is option $1$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q089_cb899354_04112026.png?v=cb899354498a)

---

## Q90

Chemistry · organic · General Organic Chemistry

Consider the following compounds/species:
[Figure: structures i–vii]
The number of compounds/species which obey Huckel’s rule is ______.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q090_29faaee2_04112026.png?v=29faaee2cdb2)

- (1) $2$
- (2) $5$
- **(3)** $4$
- (4) $6$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. i. Naphthalene: planar, cyclic, conjugated with $10\,\pi$ electrons $= 4(2)+2$, so it obeys Huckel's rule.
2. ii. Cyclopentadienyl anion: $4\,\pi$ electrons from two C=C plus the lone pair gives $6\,\pi$ electrons $= 4(1)+2$, so it obeys.
3. iii. Cyclobutadiene: $4\,\pi$ electrons $= 4n$ with $n=1$, antiaromatic, does not obey.
4. iv. Cyclopropenyl anion: $2\,\pi$ from C=C plus the lone pair gives $4\,\pi$ electrons $= 4n$, does not obey.
5. v. Cyclopropenyl cation: $2\,\pi$ electrons $= 4(0)+2$, so it obeys.
6. vi. Cyclooctatetraene: $8\,\pi$ electrons $= 4n$ and tub-shaped (non-planar), does not obey.
7. vii. Anthracene: $14\,\pi$ electrons $= 4(3)+2$, so it obeys.
8. Species obeying: i, ii, v, vii, so the count is $4$, which is option $3$.

**Subtopic:** Aromaticity · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 20)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q090_eefabc25_04112026.png?v=eefabc258e14)

---

## Q91

Chemistry · physical · Thermodynamics

Which amongst the following options is the correct relation between change in enthalpy and change in internal energy?

- (1) $\Delta H - \Delta U = -\Delta nRT$
- (2) $\Delta H + \Delta U = \Delta nR$
- (3) $\Delta H = \Delta U - \Delta n_g RT$
- **(4)** $\Delta H = \Delta U + \Delta n_g RT$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. By definition $H = U + PV$, so at constant pressure $\Delta H = \Delta U + P\Delta V$.
2. For gaseous reactants and products (ideal gases) at constant $T$ and $P$, $P\Delta V = \Delta n_g RT$.
3. Hence $\Delta H = \Delta U + \Delta n_g RT$, which is option $4$.

**Subtopic:** Enthalpy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q091_c3725016_04112026.png?v=c3725016e167)

---

## Q92

Chemistry · inorganic · Environmental Chemistry

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The nutrient deficient water bodies lead to eutrophication
- (Statement II) Eutrophication leads to decrease in the level of oxygen in the water bodies.

- (1) Statement I is correct but Statement II is false.
- **(2)** Statement I is incorrect but Statement II is true.
- (3) Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Eutrophication is the natural ageing of a water body by nutrient enrichment (e.g. nitrates, phosphates), so nutrient-deficient water bodies do not lead to it: Statement I is incorrect.
2. Nutrient enrichment causes algal blooms; their decomposition consumes dissolved oxygen, so oxygen levels fall: Statement II is true.
3. Statement I incorrect and Statement II true matches option $2$.

**Subtopic:** Water Pollution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q092_6316dd02_04112026.png?v=6316dd0262af)

---

## Q93

Chemistry · physical · Surface Chemistry

Pumice stone is an example of

- **(1)** Solid sol
- (2) Foam
- (3) Sol
- (4) Gel

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Pumice stone has gas as the dispersed phase in a solid dispersion medium; per the NCERT colloid table, gas-in-solid is a solid sol, which is option $1$.

**Subtopic:** Classification of Colloids by Dispersed Phase and Dispersion Medium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q093_ce83df9e_04112026.png?v=ce83df9e5be6)

---

## Q94

Chemistry · inorganic · Coordination Compounds – Practice

Which complex compound is most stable?

- **(1)** $\mathrm{\left[CoCl_2(en)_2\right]NO_3}$
- (2) $\mathrm{\left[Co(NH_3)_6\right]_2(SO_4)_3}$
- (3) $\mathrm{\left[Co(NH_3)_4(H_2O)Br\right](NO_3)_2}$
- (4) $\mathrm{\left[Co(NH_3)_3(NO_3)_3\right]}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Options $4$, $2$ and $3$ contain only monodentate ligands ($\mathrm{NH_3}$, $\mathrm{NO_3^-}$, $\mathrm{H_2O}$, $\mathrm{Br^-}$).
2. Option $1$, $\mathrm{[CoCl_2(en)_2]NO_3}$, contains two bidentate $\mathrm{en}$ ligands that form chelate rings with $\mathrm{Co^{3+}}$.
3. Chelation (chelate effect) greatly increases complex stability, so option $1$ is the most stable.

**Subtopic:** Ligands · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q094_58843393_04112026.png?v=588433934e9d)

---

## Q95

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

The reaction that does NOT take place in a blast furnace between $900\,\mathrm{K}$ to $1500\,\mathrm{K}$ temperature range during extraction of iron is :

- (1) $\mathrm{C + CO_2 \rightarrow 2CO}$
- (2) $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$
- **(3)** $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$
- (4) $\mathrm{FeO + CO \rightarrow Fe + CO_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the blast furnace, the $500$-$800\,\mathrm{K}$ zone has $\mathrm{3Fe_2O_3 + CO \rightarrow 2Fe_3O_4 + CO_2}$, $\mathrm{Fe_3O_4 + 4CO \rightarrow 3Fe + 4CO_2}$ and $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$.
2. The $900$-$1500\,\mathrm{K}$ zone has $\mathrm{C + CO_2 \rightarrow 2CO}$ and $\mathrm{FeO + CO \rightarrow Fe + CO_2}$; limestone decomposes and $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$ forms slag in the hotter region.
3. So $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$ does not take place at $900$-$1500\,\mathrm{K}$, which is option $3$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 21)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q095_98c82797_04112026.png?v=98c82797bb97)

---

## Q96

Chemistry · physical · Chemical Equilibrium

The equilibrium concentrations of the species in the reaction $\mathrm{A + B \rightleftharpoons C + D}$ are 2, 3, 10 and $6\,\mathrm{mol\,L^{-1}}$, respectively at $300\,\mathrm{K}$. $\Delta G^{\circ}$ for the reaction is ($R = 2\,\mathrm{cal/mol\,K}$)

- **(1)** $-1381.80\,\mathrm{cal}$
- (2) $-13.73\,\mathrm{cal}$
- (3) $1372.60\,\mathrm{cal}$
- (4) $-137.26\,\mathrm{cal}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $K = \frac{[\mathrm{C}][\mathrm{D}]}{[\mathrm{A}][\mathrm{B}]} = \frac{10 \times 6}{2 \times 3} = 10$.
2. $\Delta G^{\circ} = -2.303\,RT \log K$.
3. $\Delta G^{\circ} = -2.303 \times 2 \times 300 \times \log 10 = -2.303 \times 600 \times 1$.
4. $\Delta G^{\circ} = -1381.8\,\mathrm{cal}$, which is option $1$.

**Subtopic:** Relationship Between K, Q and G · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 21)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q096_f444b10a_04112026.png?v=f444b10a06e4)

---

## Q97

Chemistry · organic · Alcohols, Phenols and Ethers

Consider the following reaction : $\mathrm{C_6H_5{-}CH_2{-}O{-}C_6H_5} \xrightarrow[\Delta]{\mathrm{HI}} \mathrm{A + B}$ Identify products A and B.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q097_d1e22c5b_04112026.png?v=d1e22c5b2bb0)

- **(1)** ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q097_option_1_a1e7cbd1_04112026.png?v=a1e7cbd18542) — A = $\mathrm{C_6H_5{-}CH_2I}$ and B = $\mathrm{C_6H_5{-}OH}$
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q097_option_2_1c375bd1_04112026.png?v=1c375bd19e51) — A = $\mathrm{C_6H_5{-}CH_3}$ and B = $\mathrm{C_6H_5{-}I}$
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q097_option_3_97fbfd89_04112026.png?v=97fbfd890092) — A = $\mathrm{C_6H_5{-}CH_3}$ and B = $\mathrm{C_6H_5{-}OH}$
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q097_option_4_fe4ecffb_04112026.png?v=fe4ecffbc99c) — A = $\mathrm{C_6H_5{-}CH_2OH}$ and B = $\mathrm{C_6H_5{-}I}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In an alkyl aryl ether the $\mathrm{O{-}C_{aryl}}$ bond has partial double-bond character from resonance, so it is not cleaved by $\mathrm{HI}$.
2. Protonation gives $\mathrm{C_6H_5CH_2{-}\overset{+}{O}H{-}C_6H_5}$; $\mathrm{I^-}$ attacks the benzylic carbon (stable benzylic carbocation / good $S_N$ site), breaking the $\mathrm{CH_2{-}O}$ bond.
3. Products: $\mathrm{A} = \mathrm{C_6H_5CH_2I}$ and $\mathrm{B} = \mathrm{C_6H_5OH}$, which is option $1$.

**Subtopic:** Reactions of Ethers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q097_e72d7976_04112026.png?v=e72d7976423f)

---

## Q98

Chemistry · organic · Alcohols, Phenols and Ethers

> ⚠ The independent solve chose (1); the booklet prints (4).

Which amongst the following will be most readily dehydrated under acidic conditions?

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q098_option_1_2d4f0de2_04112026.png?v=2d4f0de2b062)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q098_option_2_a7a26893_04112026.png?v=a7a268930852)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q098_option_3_db954a5a_04112026.png?v=db954a5a5300)
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q098_option_4_98dd3391_04112026.png?v=98dd33911424)

**Answer** — booklet: (4) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Dehydration is easiest when the H removed is acidic and the alkene formed is stabilised by conjugation.
2. In option $1$, $\mathrm{CH_3{-}CH(NO_2){-}CH(OH){-}CH_2OH}$, the H on C3 is $\alpha$ to $\mathrm{-NO_2}$ and therefore acidic.
3. Loss of $\mathrm{H_2O}$ across C2-C3 gives $\mathrm{CH_3{-}C(NO_2){=}CH{-}CH_2OH}$, in which the $\mathrm{C{=}C}$ is conjugated with $\mathrm{-NO_2}$.
4. In options $2$ and $3$ the OH carbon is not next to the $\mathrm{NO_2}$-bearing carbon, so no conjugated nitroalkene forms; option $4$ has no activating group.
5. Hence option $1$ is dehydrated most readily.

**Subtopic:** Reactions of Alcohols · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 22)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q098_9552a92d_04112026.png?v=9552a92d4917)

---

## Q99

Chemistry · organic · Haloalkanes and Haloarenes

Identify the final product [D] obtained in the following sequence of reactions.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q099_4ae88a58_04112026.png?v=4ae88a5809ab)

- (1) $\mathrm{C_4H_{10}}$
- (2) $\mathrm{HC\equiv C^{\ominus}Na^{+}}$
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q099_option_3_fae2facc_04112026.png?v=fae2facc1151)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q099_option_4_d44684e3_04112026.png?v=d44684e3576a)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CHO} \xrightarrow{\text{i) LiAlH_4,\ ii) H_3O^+}} \mathrm{CH_3CH_2OH}$ = [A].
2. $\mathrm{CH_3CH_2OH} \xrightarrow{\mathrm{H_2SO_4},\ \Delta} \mathrm{CH_2{=}CH_2}$ = [B].
3. $\mathrm{CH_2{=}CH_2} + \mathrm{HBr} \rightarrow \mathrm{CH_3CH_2Br}$ = [C].
4. Wurtz-Fittig: $\mathrm{C_6H_5Br} + \mathrm{CH_3CH_2Br} + 2\mathrm{Na} \xrightarrow{\text{dry ether}} \mathrm{C_6H_5CH_2CH_3}$ = [D], ethylbenzene, which is option $3$.

**Subtopic:** Reactions of Haloalkanes with Metals, Reactions of Haloarenes · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 22)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q099_8d4bb7e6_04112026.png?v=8d4bb7e64a4d)

---

## Q100

Chemistry · physical · Redox Reactions

On balancing the given redox reaction,
$\mathrm{aCr_2O_7^{2-} + bSO_3^{2-}(aq) + cH^{+}(aq) \rightarrow 2aCr^{3+}(aq) + bSO_4^{2-}(aq) + \frac{c}{2}H_2O(l)}$
the coefficients a, b and c are found to be, respectively-

- (1) 1, 8, 3
- (2) 8, 1, 3
- **(3)** 1, 3, 8
- (4) 3, 8, 1

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Oxidation states: Cr in $\mathrm{Cr_2O_7^{2-}}$ is $+6$, in $\mathrm{Cr^{3+}}$ is $+3$; S in $\mathrm{SO_3^{2-}}$ is $+4$, in $\mathrm{SO_4^{2-}}$ is $+6$.
2. Electrons gained per $\mathrm{Cr_2O_7^{2-}}$: $2 \times 3 = 6$; electrons lost per $\mathrm{SO_3^{2-}}$: $2$.
3. Equate electrons: $6a = 2b \Rightarrow b = 3a$; take $a = 1$, $b = 3$.
4. Charge balance: left $-2 - 6 + c$, right $2(+3) + 3(-2) = 0$, so $c - 8 = 0 \Rightarrow c = 8$.
5. Check oxygen: left $7 + 9 = 16$, right $12 + \frac{c}{2} = 12 + 4 = 16$. Balanced.
6. $a, b, c = 1, 3, 8$, which is option $3$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q100_e9811c8b_04112026.png?v=e9811c8b9f17)

---

## Q101

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Late wood has fewer xylary elements with narrow vessels.
- (Reason R) Cambium is less active in winters.

- (1) A is true but R is false
- (2) A is false but R is true
- **(3)** Both A and R are true and R is the correct explanation of A
- (4) Both A and R are true but R is NOT the correct explanation of A

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In winter the cambium is less active, so it forms fewer xylary elements with narrow vessels (late wood); both A and R are true and R explains A, which is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q101_5c8e2c80_04112026.png?v=5c8e2c80d90b)

---

## Q102

Biology · botany · Biodiversity and Conservation

The historic Convention on Biological Diversity, ‘The Earth Summit’ was held in Rio de Janeiro in the year

- (1) 1986
- (2) 2002
- (3) 1985
- **(4)** 1992

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The historic Convention on Biological Diversity, the Earth Summit, was held in Rio de Janeiro in $1992$, which is option $4$.

**Subtopic:** How Do We Conserve Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q102_78225a77_04112026.png?v=78225a77e99c)

---

## Q103

Biology · botany · Ecosystem

In the equation $\boxed{\mathrm{GPP} - \mathrm{R} = \mathrm{NPP}}$
GPP is Gross Primary Productivity
NPP is Net Primary Productivity
R here is ________.

- **(1)** Respiratory loss
- (2) Reproductive allocation
- (3) Photosynthetically active radiation
- (4) Respiratory quotient

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{NPP} = \mathrm{GPP} - \mathrm{R}$, where $\mathrm{R}$ is the respiration losses of producers, i.e. respiratory loss (option $1$).

**Subtopic:** Productivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q103_db4ab368_04112026.png?v=db4ab36802a1)

---

## Q104

Biology · botany · Sexual Reproduction in Flowering Plants

What is the function of tassels in the corn cob?

- (1) To disperse pollen grains
- (2) To protect seeds
- (3) To attract insects
- **(4)** To trap pollen grains

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Corn tassels (silks on the cob) are the feathery stigma and style of the wind-pollinated female flowers, which wave in the wind to trap airborne pollen grains, so the answer is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q104_50411e26_04112026.png?v=50411e268c97)

---

## Q105

Biology · botany · Molecular Basis of Inheritance

What is the role of RNA polymerase III in the process of transcription in Eukaryotes?

- (1) Transcription of precursor of mRNA
- (2) Transcription of only snRNAs
- (3) Transcription of rRNAs (28S, 18S and 5.8S)
- **(4)** Transcription of tRNA, 5S rRNA and snRNA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In eukaryotes, RNA polymerase III transcribes tRNA, $5\,S$ rRNA and snRNAs (NCERT), which is option $4$.

**Subtopic:** Transcription · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q105_e5811c4a_04112026.png?v=e5811c4a49e7)

---

## Q106

Biology · botany · Biotechnology: Principles and Processes

Upon exposure to UV radiation, DNA stained with ethidium bromide will show

- (1) Bright yellow colour
- **(2)** Bright orange colour
- (3) Bright red colour
- (4) Bright blue colour

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In gel electrophoresis, separated DNA fragments stained with ethidium bromide are viewed under UV radiation and appear as bright orange coloured bands, which is option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 24)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q106_64a1967a_04112026.png?v=64a1967aa367)

---

## Q107

Biology · botany · Environmental Issues

The thickness of ozone in a column of air in the atmosphere is measured in terms of :

- (1) Decameter
- (2) Kilobase
- **(3)** Dobson units
- (4) Decibels

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The thickness of ozone in a column of air from the ground to the top of the atmosphere is measured in Dobson units (DU), which is option $3$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q107_f8f400a8_04112026.png?v=f8f400a89645)

---

## Q108

Biology · botany · Principles of Inheritance and Variation

The phenomenon of pleiotropism refers to

- **(1)** A single gene affecting multiple phenotypic expression
- (2) More than two genes affecting a single character
- (3) Presence of several alleles of a single gene controlling a single crossover
- (4) Presence of two alleles, each of the two genes controlling a single trait

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Pleiotropy is defined as a single gene affecting multiple phenotypic traits, so the answer is option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 24)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q108_18d35a7f_04112026.png?v=18d35a7fec3d)

---

## Q109

Biology · botany · Plant Growth and Development

Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period, that leads early seed production?

- (1) Zeatin
- (2) Abscisic Acid
- (3) Indole-3-butyric Acid
- **(4)** Gibberellic Acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT states that spraying juvenile conifers with gibberellins ($GA_3$) hastens maturity and leads to early seed production, so the answer is option $4$, Gibberellic Acid.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q109_5f0f243f_04112026.png?v=5f0f243f94ad)

---

## Q110

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R: In the light of the above statements, choose the most appropriate answer from options given below:

- (Assertion A) The first stage of gametophyte in the life cycle of moss is protonema stage.
- (Reason R) Protonema develops directly from spores produced in capsule.

- (1) A is correct but R is not correct
- (2) A is not correct but R is correct
- **(3)** Both A and R are correct and R is the correct explanation of A
- (4) Both A and R are correct but R is NOT the correct explanation of A

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Assertion A: in moss the gametophyte begins as the creeping, green, filamentous protonema, so A is correct.
2. Reason R: the protonema develops directly from a haploid spore released from the capsule, so R is correct.
3. Since the spore germinates directly into the protonema, R explains why protonema is the first gametophyte stage, which is option $3$.

**Subtopic:** Mosses · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 24)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q110_47ec9456_04112026.png?v=47ec9456b223)

---

## Q111

Biology · botany · Biotechnology: Principles and Processes

During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out

- (1) Histones
- (2) Polysaccharides
- (3) RNA
- **(4)** DNA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. After treating with lysozyme/cellulase, RNase and protease to remove other macromolecules, adding chilled ethanol makes the purified DNA precipitate out as fine threads, so the answer is option $4$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q111_6000508f_04112026.png?v=6000508f81fe)

---

## Q112

Biology · botany · Photosynthesis in Higher Plants

The reaction centre in PS II has an absorption maxima at

- (1) $660\,\mathrm{nm}$
- (2) $780\,\mathrm{nm}$
- **(3)** $680\,\mathrm{nm}$
- (4) $700\,\mathrm{nm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In NCERT, the reaction centre of PS II is chlorophyll $a$ with absorption peak at $680\,\mathrm{nm}$ (P680), while PS I is P700, so the answer is option $3$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q112_8438b8d7_04112026.png?v=8438b8d74df9)

---

## Q113

Biology · botany · Morphology of Flowering Plants

Family Fabaceae differs from Solanaceae and Liliaceae. With respect to the stamens, pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae.

- (1) Monoadelphous and Monothecous anthers
- (2) Epiphyllous and Dithecous anthers
- **(3)** Diadelphous and Dithecous anthers
- (4) Polyadelphous and epipetalous stamens

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Fabaceae androecium: ten stamens, diadelphous $(9)+1$, anthers dithecous; Solanaceae has epipetalous stamens and Liliaceae has epiphyllous (epitepalous) stamens, so the Fabaceae-specific feature is diadelphous with dithecous anthers, option $3$.

**Subtopic:** Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q113_b92e6cfd_04112026.png?v=b92e6cfd40b1)

---

## Q114

Biology · botany · Mineral Nutrition

Which micronutrient is required for splitting of water molecule during photosynthesis?

- (1) Magnesium
- (2) Copper
- **(3)** Manganese
- (4) Molybdenum

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Photolysis of water in photosystem II requires $\mathrm{Mn}^{2+}$ (with $\mathrm{Ca}^{2+}$ and $\mathrm{Cl}^{-}$); manganese is a micronutrient, so the answer is option $3$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q114_a38bd165_04112026.png?v=a38bd1655926)

---

## Q115

Biology · botany · Biodiversity and Conservation

Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?

- (1) Alien species invasions
- (2) Co-extinctions
- **(3)** Habitat loss and fragmentation
- (4) Over exploitation for economic gain

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Of the four causes in the Evil Quartet, NCERT names habitat loss and fragmentation as the most important cause of extinction, which is option $3$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q115_aef5360f_04112026.png?v=aef5360f1d98)

---

## Q116

Biology · botany · Transport in Plants

Movement and accumulation of ions across a membrane against their concentration gradient can be explained by

- (1) Passive Transport
- **(2)** Active Transport
- (3) Osmosis
- (4) Facilitated Diffusion

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Movement against a concentration gradient needs energy (ATP) and carrier proteins, which is active transport, so the answer is option $2$; facilitated diffusion, passive transport and osmosis all go down the gradient.

**Subtopic:** Uptake and Transport of Mineral Nutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q116_691066b0_04112026.png?v=691066b07a27)

---

## Q117

Biology · botany · Plant Growth and Development

In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as

- (1) Development
- (2) Senescence
- (3) Differentiation
- **(4)** Dedifferentiation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Mature, differentiated mesophyll cells regain the ability to divide and form an undifferentiated mass (callus); NCERT calls this dedifferentiation, which is option $4$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q117_c4cc6a3b_04112026.png?v=c4cc6a3baf36)

---

## Q118

Biology · botany · Cell Cycle and Cell Division

The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?

- (1) Diplotene
- (2) Diakinesis
- (3) Zygotene
- **(4)** Pachytene

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, during pachytene bivalents become tetrads and recombination nodules appear at the sites where crossing over occurs between non-sister chromatids of homologous chromosomes, so the answer is option $4$ (Pachytene).

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q118_4e3f1367_04112026.png?v=4e3f1367f63f)

---

## Q119

Biology · botany · Transport in Plants

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The forces generated transpiration can lift a xylem-sized column of water over $130$ meters height.
- (Statement II) Transpiration cools leaf surfaces sometimes $10$ to $15$ degrees evaporative cooling.

- (1) Statement I is correct but Statement II is incorrect
- (2) Statement I is incorrect but Statement II is correct
- **(3)** Both Statement I and Statement II are correct
- (4) Both Statement I and Statement II are incorrect

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: the cohesion-tension forces generated by transpiration can lift a xylem-sized column of water over $130\,\text{m}$, so Statement I is correct.
2. Statement II: transpiration cools leaf surfaces, sometimes by $10$ to $15$ degrees, through evaporative cooling, so Statement II is correct.
3. Both statements are correct, which is option $3$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 26)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q119_fe3a615d_04112026.png?v=fe3a615d64f3)

---

## Q120

Biology · botany · Morphology of Flowering Plants

Axile placentation is observed in

- (1) Tomato, Dianthus and Pea
- **(2)** China rose, Petunia and Lemon
- (3) Mustard, Cucumber and Primrose
- (4) China rose, Beans and Lupin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In NCERT, axile placentation is shown by China rose, tomato and lemon, and Petunia (Solanaceae) also has axile placentation. Beans, lupin and pea are marginal, mustard and cucumber are parietal, and Dianthus and Primrose are free central, so only option $2$ lists all axile examples.

**Subtopic:** Gynoecium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q120_80ce3e0b_04112026.png?v=80ce3e0b7a9a)

---

## Q121

Biology · botany · Cell Cycle and Cell Division

Which of the following stages of meiosis involves division of centromere?

- **(1)** Anaphase II
- (2) Telophase
- (3) Metaphase I
- (4) Metaphase II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. At anaphase II the centromere of each chromosome splits, letting sister chromatids move to opposite poles, so the answer is option $1$.

**Subtopic:** Anaphase II and Telophase II · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q121_b1f675cc_04112026.png?v=b1f675cc3752)

---

## Q122

Biology · botany · Principles of Inheritance and Variation

Frequency of recombination between gene pairs on same chromosome as a measure of the distance between genes to map their position on chromosome, was used for the first time by

- **(1)** Alfred Sturtevant
- (2) Henking
- (3) Thomas Hunt Morgan
- (4) Sutton and Boveri

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT: Sturtevant used the frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes and mapped their position on the chromosome, which is option $1$.

**Subtopic:** Linkage & Recombination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q122_9f7dded7_04112026.png?v=9f7dded76d45)

---

## Q123

Biology · botany · Biomolecules

Cellulose does not form blue colour with Iodine because

- **(1)** It does not contain complex helices and hence cannot hold iodine molecules
- (2) It breaks down when iodine reacts with it
- (3) It is a disaccharide
- (4) It is a helical molecule

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Starch forms helical secondary structures that hold $I_2$ molecules, giving blue colour; cellulose has no complex helices, so it cannot hold iodine, which is option $1$.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q123_38037f81_04112026.png?v=38037f811749)

---

## Q124

Biology · botany · Biotechnology: Principles and Processes

In gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used.

- **(1)** Tungsten or gold
- (2) Silver
- (3) Copper
- (4) Zinc

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the biolistic (gene gun) method, high-velocity microparticles of gold or tungsten coated with DNA are fired into host cells, so the answer is option $1$.

**Subtopic:** Competent Host & Insertion of rDNA into Host Cell · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q124_172b3df3_04112026.png?v=172b3df39fa6)

---

## Q125

Biology · botany · Plant Kingdom

Identify the pair of heterosporous pteridophytes among the following :

- (1) Psilotum and Salvinia
- (2) Equisetum and Salvinia
- (3) Lycopodium and Selaginella
- **(4)** Selaginella and Salvinia

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT names Selaginella and Salvinia as heterosporous pteridophytes (they produce microspores and megaspores), while Psilotum, Equisetum and Lycopodium are homosporous, so only option $4$ has two heterosporous genera.

**Subtopic:** Pteridophytes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q125_1663ca11_04112026.png?v=1663ca11712d)

---

## Q126

Biology · botany · Molecular Basis of Inheritance

Unequivocal proof that DNA is the genetic material was first proposed by

- (1) Avery, Macleoid and McCarthy
- (2) Wilkins and Franklin
- (3) Frederick Griffith
- **(4)** Alfred Hershey and Martha Chase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Hershey and Chase (1952) grew bacteriophages with $^{32}P$ (labels DNA) and $^{35}S$ (labels protein); only $^{32}P$ entered the bacteria, giving the unequivocal proof that DNA is the genetic material, which is option $4$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q126_be0f38c8_04112026.png?v=be0f38c89e68)

---

## Q127

Biology · botany · Photosynthesis in Higher Plants

How many ATP and $\mathrm{NADPH_2}$ are required for the synthesis of one molecule of Glucose during Calvin cycle?

- (1) 12 ATP and 16 $\mathrm{NADPH_2}$
- (2) 18 ATP and 16 $\mathrm{NADPH_2}$
- (3) 12 ATP and 12 $\mathrm{NADPH_2}$
- **(4)** 18 ATP and 12 $\mathrm{NADPH_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Fixing one $\mathrm{CO_2}$ in the Calvin cycle uses $3$ ATP and $2$ $\mathrm{NADPH}$.
2. One glucose ($\mathrm{C_6}$) needs $6$ turns of the cycle.
3. ATP: $6 \times 3 = 18$; $\mathrm{NADPH}$: $6 \times 2 = 12$, which is option $4$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q127_a4c8b45a_04112026.png?v=a4c8b45a535c)

---

## Q128

Biology · botany · Ecosystem

Identify the correct statements:
Choose the correct answer from the options given below:

- (A) Detrivores perform fragmentation.
- (B) The humus is further degraded by some microbes during mineralization.
- (C) Water soluble inorganic nutrients go down into the soil and get precipitated by a process called leaching.
- (D) The detritus food chain begins with living organisms.
- (E) Earthworms break down detritus into smaller particles by a process called catabolism.

- (1) C, D, E only
- (2) D, E, A only
- **(3)** A, B, C only
- (4) B, C, D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A: detritivores such as earthworms break detritus into smaller particles (fragmentation), so A is true.
2. B: humus is degraded very slowly by some microbes and releases inorganic nutrients by mineralization, so B is true.
3. C: water-soluble inorganic nutrients go down into the soil horizon and get precipitated as unavailable salts by leaching, so C is true.
4. D: the detritus food chain begins with dead organic matter (detritus), not living organisms, so D is false.
5. E: earthworms breaking detritus into smaller particles is fragmentation; catabolism is enzymatic degradation by bacteria and fungi, so E is false.
6. True set is $\{A, B, C\}$, which is option $3$.

**Subtopic:** Decomposition · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 27)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q128_62e97e15_04112026.png?v=62e97e15b192)

---

## Q129

Biology · botany · Sexual Reproduction in Flowering Plants

In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :

- **(1)** Synergids, Zygote and Primary endosperm nucleus
- (2) Synergids, antipodals and Polar nuclei
- (3) Synergids, Primary endosperm nucleus and zygote
- (4) Antipodals, synergids, and primary endosperm nucleus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Synergids are cells of the egg apparatus, formed from the haploid megaspore, so they are haploid ($n$).
2. Syngamy fuses the egg ($n$) with one male gamete ($n$): zygote $= n + n = 2n$ (diploid).
3. Triple fusion joins two polar nuclei ($n + n$) with the second male gamete ($n$): PEN $= 3n$ (triploid).
4. The order haploid, diploid, triploid is synergids, zygote, primary endosperm nucleus, which is option $1$.

**Subtopic:** Double Fertilisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q129_7c7d4891_04112026.png?v=7c7d489175da)

---

## Q130

Biology · botany · Respiration in Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) ATP is used at two steps in glycolysis.
- (Reason R) First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1, 6-diphosphate.

- (1) A is true but R is false.
- (2) A is false but R is true.
- **(3)** Both A and R are true and R is the correct explanation of A.
- (4) Both A and R are true but R is NOT the correct explanation of A.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Glycolysis consumes ATP at exactly two steps, so $A$ is true.
2. Step 1: glucose $\xrightarrow{ATP}$ glucose-6-phosphate; step 2: fructose-6-phosphate $\xrightarrow{ATP}$ fructose-1,6-bisphosphate, so $R$ is true.
3. $R$ names the two ATP-using steps that $A$ refers to, so $R$ correctly explains $A$: option $3$.

**Subtopic:** Glycolysis · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 28)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q130_39a94393_04112026.png?v=39a943935c7f)

---

## Q131

Biology · botany · Molecular Basis of Inheritance

Expressed Sequence Tags (ESTs) refers to

- (1) All genes whether expressed or unexpressed.
- (2) Certain important expressed genes.
- **(3)** All genes that are expressed as RNA.
- (4) All genes that are expressed as proteins.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT (Human Genome Project) defines Expressed Sequence Tags as the approach that identifies all genes expressed as RNA, which is option $3$.

**Subtopic:** Human Genome Project · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q131_c3ddd68c_04112026.png?v=c3ddd68c28f8)

---

## Q132

Biology · botany · Cell Cycle and Cell Division

Among eukaryotes, replication of DNA takes place in :

- (1) $\mathrm{G_1}$ phase
- (2) $\mathrm{G_2}$ phase
- (3) M phase
- **(4)** S phase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the eukaryotic cell cycle, DNA synthesis (replication) happens in the $\mathrm{S}$ phase of interphase, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q132_54df4d84_04112026.png?v=54df4d845d02)

---

## Q133

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body.
- (Statement II) Exarch condition is the most common feature of the root system.

- (1) Statement I is correct but Statement II is false
- **(2)** Statement I is incorrect but Statement II is true
- (3) Both Statement I and Statement II are true
- (4) Both Statement I and Statement II are false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Endarch/exarch refer to the position of protoxylem relative to metaxylem in primary xylem, not secondary xylem, so Statement I is incorrect.
2. In roots the protoxylem lies towards the periphery (exarch), so Statement II is true; this matches option $2$.

**Subtopic:** Complex Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q133_b961ec3c_04112026.png?v=b961ec3c268a)

---

## Q134

Biology · botany · Sexual Reproduction in Flowering Plants

Large, colourful, fragrant flowers with nectar are seen in

- (1) Bat pollinated plants
- (2) Wind pollinated plants
- **(3)** Insect pollinated plants
- (4) Bird pollinated plants

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT describes insect-pollinated flowers as large, colourful, fragrant and rich in nectar, so the answer is option $3$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q134_1eb7786a_04112026.png?v=1eb7786ab0d2)

---

## Q135

Biology · botany · Plant Growth and Development

Which hormone promotes internode/petiole elongation in deep water rice?

- **(1)** Ethylene
- (2) 2, 4-D
- (3) $\mathrm{GA_3}$
- (4) Kinetin

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT Class 11 (Plant Growth) states that ethylene promotes rapid internode/petiole elongation in deep water rice plants, so the answer is option $1$ (Ethylene).

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q135_5c920318_04112026.png?v=5c920318902f)

---

## Q136

Biology · botany · Morphology of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem.
- (Reason R) Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves.

- (1) A is true but R is false
- (2) A is false but R is true
- **(3)** Both A and R are true and R is the correct explanation of A
- (4) Both A and R are true but R is NOT the correct explanation of A

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Assertion A matches the NCERT definition: the flower is a modified shoot in which the shoot apical meristem changes to a floral meristem, so A is true.
2. Reason R is true: internodes do not elongate, the axis condenses, and floral appendages form laterally at successive nodes instead of leaves.
3. R describes how the shoot is modified into a flower, so R explains A, which is option $3$.

**Subtopic:** The Flower · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 29)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q136_89766257_04112026.png?v=8976625773d5)

---

## Q137

Biology · botany · Cell Cycle and Cell Division

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | M Phase | I | Proteins are synthesized |
| B | $\mathrm{G_2}$ Phase | II | Inactive phase |
| C | Quiescent stage | III | Interval between mitosis and initiation of DNA replication |
| D | $\mathrm{G_1}$ Phase | IV | Equational division |

- **(1)** A-IV, B-I, C-II, D-III
- (2) A-II, B-IV, C-I, D-III
- (3) A-III, B-II, C-IV, D-I
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. M phase (mitosis) is the equational division, so A-IV.
2. In $\mathrm{G_2}$ phase proteins are synthesised in preparation for mitosis, so B-I.
3. The quiescent stage ($\mathrm{G_0}$) is an inactive phase, so C-II.
4. $\mathrm{G_1}$ phase is the interval between mitosis and the initiation of DNA replication, so D-III.
5. A-IV, B-I, C-II, D-III matches option $1$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q137_f495054c_04112026.png?v=f495054cd068)

---

## Q138

Biology · botany · Molecular Basis of Inheritance

How many different proteins does the ribosome consist of?

- (1) $40$
- (2) $20$
- **(3)** $80$
- (4) $60$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT teaches that the ribosome consists of structural RNAs and about $80$ different proteins, which is option $3$.

**Subtopic:** Translation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q138_300e06c0_04112026.png?v=300e06c0ede1)

---

## Q139

Biology · botany · Environmental Issues

Which one of the following statements is NOT correct?

- (1) Water hyacinth grows abundantly in eutrophic water bodies and leads to an imbalance in the ecosystem dynamics of the water body
- (2) The amount of some toxic substances of industrial waste water increases in the organisms at successive trophic levels
- (3) The micro-organisms involved in biodegradation of organic matter in a sewage polluted water body consume a lot of oxygen causing the death of aquatic organisms
- **(4)** Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Algal blooms from nutrient enrichment deteriorate water quality, deplete dissolved oxygen and cause fish mortality, so statement $1$ is NOT correct.
2. Water hyacinth thriving in eutrophic water and upsetting ecosystem balance (statement $2$), biomagnification of toxic industrial substances along trophic levels (statement $3$), and high oxygen use by sewage-degrading microbes killing aquatic life (statement $4$) are all correct, so the answer is option $4$.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q139_d18987e9_04112026.png?v=d18987e90817)

---

## Q140

Biology · botany · Photosynthesis in Higher Plants

Which of the following combinations is required for chemiosmosis?

- (1) Proton pump, electron gradient, ATP synthase
- (2) Proton pump, electron gradient, NADP synthase
- **(3)** Membrane, proton pump, proton gradient, ATP synthase
- (4) Membrane, proton pump, proton gradient, NADP synthase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient across the membrane and ATP synthase through which protons flow to make ATP, which is option $3$.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q140_480a3394_04112026.png?v=480a3394e0a4)

---

## Q141

Biology · botany · Transport in Plants

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Cohesion | I | More attraction in liquid phase |
| B | Adhesion | II | Mutual attraction among water molecules |
| C | Surface tension | III | Water loss in liquid phase |
| D | Guttation | IV | Attraction towards polar surfaces |

- (1) A – III, B – I, C – IV, D – II
- (2) A – II, B – I, C – IV, D – III
- **(3)** A – II, B – IV, C – I, D – III
- (4) A – IV, B – III, C – II, D – I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cohesion is the mutual attraction among water molecules, so $A \rightarrow II$.
2. Adhesion is the attraction of water molecules to polar surfaces, so $B \rightarrow IV$.
3. Surface tension arises because water molecules are more attracted to each other in the liquid phase than in the gas phase, so $C \rightarrow I$.
4. Guttation is the loss of water in liquid form (from hydathodes), so $D \rightarrow III$.
5. $A-II,\ B-IV,\ C-I,\ D-III$ matches option $3$.

**Subtopic:** Transpiration and Stomatal Opening and Closing, Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q141_e9ffdf3e_04112026.png?v=e9ffdf3e9b28)

---

## Q142

Biology · botany · Mineral Nutrition

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Iron | I | Synthesis of auxin |
| B | Zinc | II | Component of nitrate reductase |
| C | Boron | III | Activator of catalase |
| D | Molybdenum | IV | Cell elongation and differentiation |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-II, B-IV, C-I, D-III
- (3) A-III, B-II, C-I, D-IV
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Iron (A) is an activator of catalase, so $A \rightarrow III$.
2. Zinc (B) is needed for the synthesis of auxin, so $B \rightarrow I$.
3. Boron (C) is required for cell elongation and differentiation, so $C \rightarrow IV$.
4. Molybdenum (D) is a component of nitrate reductase, so $D \rightarrow II$.
5. $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ matches option $1$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 31)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q142_376187ba_04112026.png?v=376187baffc8)

---

## Q143

Biology · botany · Organisms and Populations

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Gause’s ‘Competitive Exclusion Principle’ states that two closely related species competing for the same resources cannot co-exist indefinitely and competitively inferior one will be eliminated eventually.
- (Statement II) In general, carnivores are more adversely affected by competition than herbivores.

- **(1)** Statement I is correct Statement II is false.
- (2) Statement I is incorrect but Statement II is true.
- (3) Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: Gause's Competitive Exclusion Principle says two closely related species competing for the same resources cannot co-exist indefinitely and the competitively inferior one is eliminated, so Statement I is correct.
2. Statement II: in general, herbivores are more adversely affected by competition than carnivores, so Statement II is false.
3. Statement I correct and Statement II false matches option $1$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q143_1cef9396_04112026.png?v=1cef93963bcb)

---

## Q144

Biology · botany · Biomolecules

Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of

- (1) Lipase
- (2) Dinitrogenase
- **(3)** Succinic dehydrogenase
- (4) Amylase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Malonate resembles succinate in structure, so it binds the active site of succinic dehydrogenase as a competitive inhibitor; this is option $3$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q144_adf29d20_04112026.png?v=adf29d207ce9)

---

## Q145

Biology · botany · Anatomy of Flowering Plants

Identify the correct statements: Choose the correct answer from the options given below:

- (A) Lenticels are the lens-shaped openings permitting the exchange of gases.
- (B) Bark formed early in the season is called hard bark.
- (C) Bark is a technical term that refers to all tissues exterior to vascular cambium.
- (D) Bark refers to periderm and secondary phloem.
- (E) Phellogen is single-layered in thickness.

- (1) A, B and D only
- (2) B and C only
- (3) B, C and E only
- **(4)** A and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A: lenticels are lens-shaped openings in the periderm that permit gas exchange, so $A$ is true.
2. B: bark formed early in the season is soft (early) bark, not hard bark, so $B$ is false.
3. C: bark is a non-technical term for all tissues exterior to the vascular cambium, so calling it a technical term makes $C$ false.
4. D: bark includes the periderm and the secondary phloem, so $D$ is true.
5. E: phellogen is a couple of layers thick, not single-layered, so $E$ is false.
6. True statements are $A$ and $D$ only, which is option $4$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q145_8eb77076_04112026.png?v=8eb770767636)

---

## Q146

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) In gymnosperms the pollen grains are released from the microsporangium and carried by air currents.
- (Reason R) Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed.

- **(1)** A is true but R is false
- (2) A is false but R is true
- (3) Both A and R are true and R is the correct explanation of A
- (4) Both A and R are true but R is NOT the current explanation of A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Assertion A: in gymnosperms pollen grains are released from the microsporangium and carried by air currents, so A is true.
2. Reason R: pollen grains reach the micropyle of the ovule and form a pollen tube that carries the male gametes towards the archegonia, so the claim that no pollen tube is formed is false.
3. A true and R false matches option $1$.

**Subtopic:** Gymnosperms · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 32)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q146_3a6b1fb3_04112026.png?v=3a6b1fb3ee70)

---

## Q147

Biology · botany · Principles of Inheritance and Variation

Which of the following statements are correct about Klinefelter’s Syndrome? Choose the correct answer from the options given below:

- (A) This disorder was first described by Langdon Down (1866).
- (B) Such an individual has overall masculine development. However, the feminine developement is also expressed.
- (C) The affected individual is short statured.
- (D) Physical, psychomotor and mental development is retarded.
- (E) Such individuals are sterile.

- **(1)** B and E only
- (2) A and E only
- (3) A and B only
- (4) C and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Klinefelter's syndrome has karyotype $47,XXY$ (an extra $X$ chromosome).
2. Statement A is false: Langdon Down (1866) described Down's syndrome, not Klinefelter's.
3. Statement B is true: overall masculine development with feminine traits such as gynaecomastia.
4. Statements C and D are false: short stature and retarded physical, psychomotor and mental development are features of Down's syndrome.
5. Statement E is true: such individuals are sterile.
6. Correct statements are B and E only, which is option $1$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q147_c4378820_04112026.png?v=c43788209032)

---

## Q148

Biology · botany · Biotechnology: Principles and Processes

Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence. Choose the correct answer from the options given below :

- (A) Insertion of recombinant DNA into the host cell
- (B) Cutting of DNA at specific location by restriction enzyme
- (C) Isolation of desired DNA fragment
- (D) Amplification of gene of interest using PCR

- (1) C, B, D, A
- (2) B, D, A, C
- **(3)** B, C, D, A
- (4) C, A, B, D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Genomic DNA is first cut at specific locations by a restriction enzyme: step $B$.
2. The desired DNA fragment is then separated and isolated (e.g. by gel electrophoresis): step $C$.
3. The gene of interest is amplified using PCR: step $D$.
4. The recombinant DNA is finally inserted into the host cell: step $A$.
5. Sequence $B \to C \to D \to A$ matches option $3$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q148_e99b921a_04112026.png?v=e99b921a22dc)

---

## Q149

Biology · botany · Respiration in Plants

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Oxidative decarboxylation | I | Citrate synthase |
| B | Glycolysis | II | Pyruvate dehydrogenase |
| C | Oxidative phosphorylation | III | Electron transport system |
| D | Tricarboxylic acid cycle | IV | EMP pathway |

- (1) A – III, B – I, C – II, D – IV
- **(2)** A – II, B – IV, C – III, D – I
- (3) A – III, B – IV, C – II, D – I
- (4) A – II, B – IV, C – I, D – III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Oxidative decarboxylation of pyruvate to acetyl CoA is catalysed by pyruvate dehydrogenase, so $A \to II$.
2. Glycolysis is also called the EMP (Embden-Meyerhof-Parnas) pathway, so $B \to IV$.
3. Oxidative phosphorylation is coupled to the electron transport system, so $C \to III$.
4. The TCA cycle begins with acetyl CoA + OAA forming citrate via citrate synthase, so $D \to I$.
5. $A-II, B-IV, C-III, D-I$ matches option $2$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 33)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q149_28d472f0_04112026.png?v=28d472f05f8c)

---

## Q150

Biology · botany · Organisms and Populations

Match List I with List II :
List I (Interaction) | List II (Species A and B)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Mutualism | I | $+(\mathrm{A}),\ 0(\mathrm{B})$ |
| B | Commensalism | II | $-(\mathrm{A}),\ 0(\mathrm{B})$ |
| C | Amensalism | III | $+(\mathrm{A}),\ -(\mathrm{B})$ |
| D | Parasitism | IV | $+(\mathrm{A}),\ +(\mathrm{B})$ |

- (1) A-IV, B-III, C-I, D-II
- (2) A-III, B-I, C-IV, D-II
- (3) A-IV, B-II, C-I, D-III
- **(4)** A-IV, B-I, C-II, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Mutualism benefits both species: $+(A),\ +(B)$, so A-IV.
2. Commensalism benefits one and leaves the other unaffected: $+(A),\ 0(B)$, so B-I.
3. Amensalism harms one and leaves the other unaffected: $-(A),\ 0(B)$, so C-II.
4. Parasitism benefits the parasite and harms the host: $+(A),\ -(B)$, so D-III.
5. A-IV, B-I, C-II, D-III is option $4$.

**Subtopic:** Population Interactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q150_c3ba96c9_04112026.png?v=c3ba96c943f7)

---

## Q151

Biology · zoology · Principles of Inheritance and Variation

Broad palm with single palm crease is visible in a person suffering from-

- (1) Klinefelter’s syndrome
- (2) Thalassemia
- **(3)** Down’s syndrome
- (4) Turner’s syndrome

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Per NCERT, Down's syndrome (trisomy of chromosome $21$) shows a broad palm with a characteristic single palm crease, so the answer is option $3$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q151_c41ea054_04112026.png?v=c41ea054a3a7)

---

## Q152

Biology · zoology · Biomolecules

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal).
- (Statement II) Adult human haemoglobin, consists of 4 subunits (two subunits of $\alpha$ type and two subunits of $\beta$ type.)

- (1) Statement I is true but Statement II is false.
- **(2)** Statement I is false but Statement II is true.
- (3) Both Statement I and Statement II are true
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement I: by convention the first amino acid at the left end is the N-terminal and the last at the right end is the C-terminal; the statement swaps them, so it is false.
2. Statement II: adult human haemoglobin is a tetramer of two $\alpha$ and two $\beta$ subunits, so it is true.
3. I false, II true, which is option $2$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q152_8e860ce6_04112026.png?v=8e860ce6744a)

---

## Q153

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R.
In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Nephrons are of two types: Cortical & Juxta medullary, based on their relative position in cortex and medulla.
- (Reason R) Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle.

- **(1)** A is true but R is false.
- (2) A is false but R is true.
- (3) Both A and R are true and R is the correct explanation of A.
- (4) Both A and R are true but R is NOT the correct explanation of A.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Nephrons are classed as cortical or juxta medullary by their position in the cortex and medulla, so $A$ is true.
2. Cortical nephrons have a short loop of Henle reaching only a little into the medulla, while juxta medullary nephrons have a long loop running deep into the medulla, so $R$ reverses the facts and is false.
3. $A$ true and $R$ false gives option $1$.

**Subtopic:** Human Excretory System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q153_ee970c3b_04112026.png?v=ee970c3bc2c7)

---

## Q154

Biology · zoology · Human Health and Disease

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Heroin | I | Effect on cardiovascular system |
| B | Marijuana | II | Slow down body function |
| C | Cocaine | III | Painkiller |
| D | Morphine | IV | Interfere with transport of dopamine |

- (1) A-IV, B-III, C-II, D-I
- (2) A-III, B-IV, C-I, D-II
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Heroin (smack) is a depressant and slows down body functions: $A \rightarrow II$.
2. Cannabinoids such as marijuana mainly affect the cardiovascular system: $B \rightarrow I$.
3. Cocaine interferes with the transport of the neurotransmitter dopamine: $C \rightarrow IV$.
4. Morphine is a very effective sedative and painkiller: $D \rightarrow III$.
5. The match $A-II, B-I, C-IV, D-III$ is option $3$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q154_8681827a_04112026.png?v=8681827a61c5)

---

## Q155

Biology · zoology · Breathing and Exchange of Gases

Vital capacity of lung is _________.

- (1) $\mathrm{IRV + ERV + TV - RV}$
- **(2)** $\mathrm{IRV + ERV + TV}$
- (3) $\mathrm{IRV + ERV}$
- (4) $\mathrm{IRV + ERV + TV + RV}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Vital capacity is the maximum volume of air a person can breathe out after a forced inspiration, so $VC = IRV + ERV + TV$, which is option $2$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q155_c3b6cb85_04112026.png?v=c3b6cb855756)

---

## Q156

Biology · zoology · Body Fluids and Circulation

Match List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P-wave | I | Beginning of systole |
| B | Q-wave | II | Repolarisation of ventricles |
| C | QRS complex | III | Depolarisation of atria |
| D | T-wave | IV | Depolarisation of ventricles |

- (1) A-II, B-IV, C-I, D-III
- (2) A-I, B-II, C-III, D-IV
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the NCERT ECG, the P-wave is depolarisation of the atria ($A \to III$), the QRS complex is depolarisation of the ventricles ($C \to IV$), the T-wave is repolarisation of the ventricles ($D \to II$), and the Q-wave marks the beginning of systole ($B \to I$), so the match is option $3$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 35)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q156_b5b062db_04112026.png?v=b5b062db70a7)

---

## Q157

Biology · zoology · Digestion and Absorption

Match List I with List II
List I (Cells) | List II (Secretion)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Peptic cells | I | Mucus |
| B | Goblet cells | II | Bile juice |
| C | Oxyntic cells | III | Proenzyme pepsinogen |
| D | Hepatic cells | IV | $\mathrm{HCl}$ and intrinsic factor for absorption of vitamin $\mathrm{B_{12}}$ |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-II, B-IV, C-I, D-III
- (3) A-IV, B-III, C-II, D-I
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Peptic (chief) cells secrete the proenzyme pepsinogen: $A \rightarrow III$.
2. Goblet cells secrete mucus: $B \rightarrow I$.
3. Oxyntic (parietal) cells secrete HCl and intrinsic factor for vitamin $B_{12}$ absorption: $C \rightarrow IV$.
4. Hepatic cells secrete bile juice: $D \rightarrow II$.
5. The match $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ is option $1$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q157_e45f472d_04112026.png?v=e45f472d3c23)

---

## Q158

Biology · zoology · Reproductive Health

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Vasectomy | I | Oral method |
| B | Coitus interruptus | II | Barrier method |
| C | Cervical caps | III | Surgical method |
| D | Saheli | IV | Natural method |

- (1) A-II, B-III, C-I, D-IV
- (2) A-IV, B-II, C-I, D-III
- (3) A-III, B-I, C-IV, D-II
- **(4)** A-III, B-IV, C-II, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Vasectomy (A) is a surgical sterilisation method, so $A \rightarrow III$.
2. Coitus interruptus (B) is a natural method, so $B \rightarrow IV$.
3. Cervical caps (C) are a barrier method, so $C \rightarrow II$.
4. Saheli (D) is a once-a-week oral contraceptive pill, so $D \rightarrow I$.
5. $A$-III, $B$-IV, $C$-II, $D$-I matches option $4$.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 35)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q158_132a38e5_04112026.png?v=132a38e5bde0)

---

## Q159

Biology · zoology · Reproductive Health

Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?

- (1) Hepatitis-B
- (2) HIV Infection
- (3) Genital herpes
- **(4)** Gonorrhoea

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT states that, except for hepatitis-B, genital herpes and HIV infection, the other STDs are completely curable if detected early and treated properly, so gonorrhoea (option $4$) is the answer.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q159_d214e6dd_04112026.png?v=d214e6dd3530)

---

## Q160

Biology · zoology · Human Health and Disease

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Ringworm | I | Haemophilus influenzae |
| B | Filariasis | II | Trichophyton |
| C | Malaria | III | Wuchereria bancrofti |
| D | Pneumonia | IV | Plasmodium vivax |

- (1) A-III, B-II, C-I, D-IV
- (2) A-III, B-II, C-IV, D-I
- **(3)** A-II, B-III, C-IV, D-I
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Ringworm is a fungal disease caused by $Trichophyton$ (A-II); filariasis is caused by $Wuchereria\ bancrofti$ (B-III); malaria is caused by $Plasmodium\ vivax$ (C-IV); pneumonia is caused by $Haemophilus\ influenzae$ (D-I), so A-II, B-III, C-IV, D-I is option $3$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 35)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q160_3b6780fd_04112026.png?v=3b6780fd7639)

---

## Q161

Biology · zoology · Cell: The Unit of Life

Which of the following are NOT considered as the part of endomembrane system?
Choose the most appropriate answer from the options given below:

- (A) Mitochondria
- (B) Endoplasmic reticulum
- (C) Chloroplasts
- (D) Golgi complex
- (E) Peroxisomes

- (1) A and D only
- (2) A, D and E only
- (3) B and D only
- **(4)** A, C and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the endomembrane system comprises the endoplasmic reticulum, Golgi complex, lysosomes and vacuoles, whose functions are coordinated; mitochondria, chloroplasts and peroxisomes are not included, so the answer is A, C and E only, option $4$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 36)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q161_3224f557_04112026.png?v=3224f5575475)

---

## Q162

Biology · zoology · Biotechnology: Principles and Processes

Which of the following is not a cloning vector?

- (1) pBR322
- **(2)** Probe
- (3) BAC
- (4) YAC

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. YAC, pBR322 and BAC are vectors used to carry foreign DNA, while a probe is a labelled DNA/RNA used for detection, so the answer is option $2$.

**Subtopic:** Cloning Vectors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q162_95cf7c6a_04112026.png?v=95cf7c6ae90e)

---

## Q163

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

- (1) A-III, B-IV, C-I, D-II
- (2) A-II, B-III, C-I, D-IV
- **(3)** A-I, B-II, C-III, D-IV
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A leopard and a lion share prey in the same habitat, so A is competition: $A \to I$.
2. A cuckoo lays its eggs in a crow's nest for the host to incubate, so B is brood parasitism: $B \to II$.
3. In mycorrhizae the fungus and the plant root both benefit, so C is mutualism: $C \to III$.
4. The cattle egret feeds on insects stirred up by grazing cattle and the cattle are unaffected, so D is commensalism: $D \to IV$.
5. $A-I, B-II, C-III, D-IV$ matches option $3$.

**Subtopic:** Mutualism, Commensalism and Ammensalism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q163_25f80796_04112026.png?v=25f80796ed59)

---

## Q164

Biology · zoology · Principles of Inheritance and Variation

Which one of the following symbols represents mating between relatives in human pedigree analysis?

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q164_option_1_b6102ba0_04112026.png?v=b6102ba02010)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q164_option_2_3d9290cb_04112026.png?v=3d9290cb0920)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q164_option_3_0490dd67_04112026.png?v=0490dd67af1a)
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/figures_agent/q164_option_4_c56f7cb1_04112026.png?v=c56f7cb1e48a)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option $1$ shows a mating line with an affected (shaded) male offspring, i.e. parents with an affected son.
2. Option $2$ shows shaded square, circle and diamond, i.e. affected individuals.
3. Option $3$ shows a single line joining male and female, i.e. an ordinary mating.
4. Option $4$ shows a double line joining male and female, which NCERT defines as consanguineous mating (mating between relatives), so the answer is option $4$.

**Subtopic:** Pedigree Analysis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 36)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q164_850e09f0_04112026.png?v=850e09f0065e)

---

## Q165

Biology · zoology · Excretory Products and Their Elimination

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Taenia | I | Nephridia |
| B | Paramoecium | II | Contractile vacuole |
| C | Periplaneta | III | Flame cells |
| D | Pheretima | IV | Urecose gland |

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-II, B-I, C-IV, D-III
- (3) A-I, B-II, C-III, D-IV
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Taenia (Platyhelminthes) excretes through flame cells: $A \rightarrow III$.
2. Paramoecium (protist) uses a contractile vacuole for osmoregulation and excretion: $B \rightarrow II$.
3. Periplaneta (cockroach) has urecose glands that help in excretion: $C \rightarrow IV$.
4. Pheretima (earthworm) excretes through nephridia: $D \rightarrow I$.
5. $A-III, B-II, C-IV, D-I$ is option $1$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 36)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q165_d67fab33_04112026.png?v=d67fab33ea93)

---

## Q166

Biology · zoology · Digestion and Absorption

Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by

- (1) Gastro-oesophageal sphincter
- (2) Pyloric sphincter
- (3) Sphincter of Oddi
- **(4)** Ileo-caecal valve

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The ileo-caecal valve guards the opening of the ileum into the caecum and prevents backflow of undigested matter, so the answer is option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q166_3219a2c0_04112026.png?v=3219a2c0171e)

---

## Q167

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Gene ‘a’ | I | $\beta$-galactosidase |
| B | Gene ‘y’ | II | Transacetylase |
| C | Gene ‘i’ | III | Permease |
| D | Gene ‘z’ | IV | Repressor protein |

- (1) A-III, B-IV, C-I, D-II
- (2) A-III, B-I, C-IV, D-II
- (3) A-II, B-I, C-IV, D-III
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the lac operon, gene $a$ codes for transacetylase, so A-II; gene $y$ codes for permease, so B-III; gene $i$ codes for the repressor protein, so C-IV; gene $z$ codes for $\beta$-galactosidase, so D-I. This is option $4$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q167_e4ca0635_04112026.png?v=e4ca06359c1d)

---

## Q168

Biology · zoology · Biotechnology and Its Applications

Which one of the following techniques does not serve the purpose of early diagnosis of a disease for its early treatment?

- (1) Polymerase Chain Reaction (PCR) technique
- (2) Enzyme Linked Immuno-Sorbent Assay (ELISA) technique
- (3) Recombinant DNA Technology
- **(4)** Serum and Urine analysis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Conventional methods of diagnosis (serum and urine analysis) detect a pathogen only after symptoms appear, when its concentration is already high, so they do not give early detection; Recombinant DNA technology, PCR and ELISA do give early diagnosis, so the answer is option $4$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 37)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q168_02185092_04112026.png?v=02185092c276)

---

## Q169

Biology · zoology · Biomolecules

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below :

- (I) Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.
- (II) When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor.

- (1) Statement I is true but Statement II is false.
- (2) Statement I is false but Statement II is true.
- **(3)** Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: at low temperature an enzyme is only temporarily inactive, but high temperature denatures the protein and destroys its activity, so Statement I is true.
2. Statement II: an inhibitor that closely resembles the substrate in molecular structure competes for the active site and is a competitive inhibitor, so Statement II is true.
3. Both statements are true, which is option $3$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 37)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q169_5ebb2daf_04112026.png?v=5ebb2daf26b2)

---

## Q170

Biology · zoology · Human Reproduction

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R.
In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Endometrium is necessary for implantation of blastocyst.
- (Reason R) In the absence of fertilization, the corpus luteum degenerates that causes disintegration of endometrium.

- (1) A is true but R is false.
- (2) A is false but R is true.
- (3) Both A and R are true and R is the correct explanation of A.
- **(4)** Both A and R are true but R is NOT the correct explanation of A.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Assertion A: the blastocyst becomes embedded in the endometrium of the uterus (implantation), so A is true.
2. Reason R: without fertilization the corpus luteum degenerates, progesterone falls and the endometrium disintegrates (menstruation), so R is true.
3. R describes what happens to the endometrium when there is no fertilization; it does not explain why the endometrium is necessary for implantation, so R is not the correct explanation of A — option $4$.

**Subtopic:** Implantation and Embryonic Development, Menstrual Cycle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 37)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q170_bc04193b_04112026.png?v=bc04193b0760)

---

## Q171

Biology · zoology · Reproductive Health

Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below.

- (Assertion A) Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme.
- (Reason R) Ban on amniocentesis checks increasing menace of female foeticide.

- (1) A is true but R is false.
- **(2)** A is false but R is true.
- (3) Both A and R are true and R is the correct explanation of A.
- (4) Both A and R are true and R is NOT the correct explanation of A.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Under the RCH programme, one strategy is the statutory ban on amniocentesis for sex determination, so using amniocentesis for sex determination is not a strategy: Assertion $A$ is false.
2. The ban on amniocentesis for sex determination is meant to check the rising menace of female foeticide, so Reason $R$ is true.
3. $A$ false and $R$ true matches option $2$.

**Subtopic:** Reproductive Health – Problems and Strategies, MTP and Amniocentesis · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 38)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q171_d090896d_04112026.png?v=d090896dc61f)

---

## Q172

Biology · zoology · Environmental Issues

Which of the following statements is correct?

- (1) Presence of large amount of nutrients in water restricts ‘Algal Bloom’
- (2) Algal Bloom decreases fish mortality
- (3) Eutrophication refers to increase in domestic sewage and waste water in lakes.
- **(4)** Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option 4 is the NCERT definition of biomagnification (increase in toxicant concentration at successive trophic levels), so it is correct; options 1, 2 and 3 are false because nutrients cause algal blooms, algal blooms increase fish mortality, and eutrophication is the natural ageing of a lake by nutrient enrichment.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 38)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q172_f6774e3a_04112026.png?v=f6774e3a095b)

---

## Q173

Biology · zoology · Human Reproduction

Which of the following statements are correct regarding female reproductive cycle? Choose the most appropriate answer from the options given below.

- (A) In non-primate mammals cyclical changes during reproduction are called oestrus cycle.
- (B) First menstrual cycle begins at puberty and is called menopause.
- (C) Lack of menstruation may be indicative of pregnancy.
- (D) Cyclic menstruation extends between menarche and menopause.

- (1) A, B and C only
- **(2)** A, C and D only
- (3) A and D only
- (4) A and B only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement A: in non-primate mammals the reproductive cyclical changes are called the oestrus cycle, so $A$ is true.
2. Statement B: the first menstruation at puberty is called menarche, not menopause, so $B$ is false.
3. Statement C: lack of menstruation may indicate pregnancy, so $C$ is true.
4. Statement D: cyclic menstruation extends between menarche and menopause, so $D$ is true.
5. True set is $\{A, C, D\}$, which matches option $2$ (A, C and D only).

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q173_e77c8c79_04112026.png?v=e77c8c791f87)

---

## Q174

Biology · zoology · Chemical Coordination and Integration

Match List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | CCK | I | Kidney |
| B | GIP | II | Heart |
| C | ANF | III | Gastric gland |
| D | ADH | IV | Pancreas |

- (1) A-II, B-IV, C-I, D-III
- (2) A-IV, B-II, C-III, D-I
- **(3)** A-IV, B-III, C-II, D-I
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. CCK acts on the pancreas (pancreatic enzyme secretion) and gall bladder, so $A \to IV$.
2. GIP inhibits gastric secretion and motility, so it relates to the gastric gland: $B \to III$.
3. ANF is secreted by the atrial wall of the heart: $C \to II$.
4. ADH acts on the distal tubules of the kidney: $D \to I$.
5. $A-IV, B-III, C-II, D-I$ is option $3$.

**Subtopic:** Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 38)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q174_4a88517e_04112026.png?v=4a88517e3b24)

---

## Q175

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid.
- (Statement II) In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome.

- (1) Statement I is correct but Statement II is false.
- **(2)** Statement I is incorrect but Statement II is true.
- (3) Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. DNA is negatively charged because of its phosphate groups, so the phrase 'positively charged DNA' in Statement I is wrong; in prokaryotes the DNA is held by positively charged proteins in the nucleoid. Statement I is incorrect.
2. In eukaryotes, the negatively charged DNA wraps around a positively charged histone octamer to form the nucleosome. Statement II is true.
3. Statement I incorrect and Statement II true is option $2$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q175_a66378e3_04112026.png?v=a66378e32488)

---

## Q176

Biology · zoology · Locomotion and Movement

Match List I with List II. List I (Type of Joint) List II (Found between) Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cartilaginous Joint | I | Between flat skull bones |
| B | Ball and Socket Joint | II | Between adjacent vertebrae in vertebral column |
| C | Fibrous Joint | III | Between carpal and metacarpal of thumb |
| D | Saddle Joint | IV | Between Humerus and Pectoral girdle |

- (1) A-I, B-IV, C-III, D-II
- (2) A-II, B-IV, C-III, D-I
- (3) A-III, B-I, C-II, D-IV
- **(4)** A-II, B-IV, C-I, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Cartilaginous joint: adjacent vertebrae of the vertebral column are joined by cartilage, so $A \rightarrow II$.
2. Ball and socket joint: between the humerus and the pectoral girdle, so $B \rightarrow IV$.
3. Fibrous joint: sutures between the flat skull bones, so $C \rightarrow I$.
4. Saddle joint: between the carpal and metacarpal of the thumb, so $D \rightarrow III$.
5. $A$-$II$, $B$-$IV$, $C$-$I$, $D$-$III$ matches option $4$.

**Subtopic:** Joints · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 39)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q176_9c98126d_04112026.png?v=9c98126dd490)

---

## Q177

Biology · zoology · Structural Organisation in Animals

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Ligaments are dense irregular tissue.
- (Statement II) Cartilage is dense regular tissue.

- (1) Statement I is true but Statement II is false
- (2) Statement I is false but Statement II is true
- (3) Both Statement I and Statement II are true
- **(4)** Both Statement I and Statement II are false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: ligaments (bone to bone) are dense regular connective tissue with parallel collagen fibres, so calling them dense irregular is false.
2. Statement II: cartilage is a specialised connective tissue, not dense regular tissue, so Statement II is false.
3. Both statements false, which is option $4$.

**Subtopic:** Connective Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q177_b70f442b_04112026.png?v=b70f442b480f)

---

## Q178

Biology · zoology · Human Health and Disease

In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?

- (1) Basophils
- (2) Eosinophils
- **(3)** $\mathrm{T_H}$ cells
- (4) B-lymphocytes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Per NCERT, HIV enters macrophages, its RNA is reverse-transcribed into DNA, and the virus then enters helper T-lymphocytes ($\mathrm{T_H}$ cells), where it replicates and produces progeny viruses, so the answer is option $3$.

**Subtopic:** AIDS · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q178_d811653b_04112026.png?v=d811653b304c)

---

## Q179

Biology · zoology · Animal Kingdom

Radial symmetry is NOT found in adults of phylum ______.

- (1) Coelenterata
- (2) Echinodermata
- (3) Ctenophora
- **(4)** Hemichordata

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Coelenterata, Ctenophora and adult Echinodermata are radially symmetrical, while Hemichordata are bilaterally symmetrical, so the answer is option $4$.

**Subtopic:** Phylum – Echinodermata and Hemichordata · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 39)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q179_94a90b9b_04112026.png?v=94a90b9b1a2a)

---

## Q180

Biology · zoology · Cell: The Unit of Life

Which of the following functions is carried out by cytoskeleton in a cell?

- **(1)** Motility
- (2) Transportation
- (3) Nuclear division
- (4) Protein synthesis

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT lists the cytoskeleton's functions as mechanical support, motility and maintenance of cell shape, so the answer is option $1$ (Motility).

**Subtopic:** Cytoskeleton · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 39)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q180_ffe79467_04112026.png?v=ffe794679008)

---

## Q181

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct.
- (Statement II) The cavity of the cervix is called cervical canal which along with vagina forms birth canal.

- (1) Statement I is correct but Statement II is false.
- (2) Statement I is incorrect but Statement II is true.
- **(3)** Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: the vas deferens receives a duct from the seminal vesicle and opens into the urethra as the ejaculatory duct, so Statement I is true.
2. Statement II: the cavity of the cervix is the cervical canal, which together with the vagina forms the birth canal, so Statement II is true.
3. Both statements are true, which is option $3$.

**Subtopic:** The Male Reproductive System, The Female Reproductive System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q181_5dfe597c_04112026.png?v=5dfe597cd37a)

---

## Q182

Biology · zoology · Evolution

Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.

- (1) Mole, Flying squirrel, Tasmanian tiger cat
- (2) Lemur, Anteater, Wolf
- (3) Tasmanian wolf, Bobcat, Marsupial mole
- **(4)** Numbat, Spotted cuscus, Flying phalanger

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Numbat, spotted cuscus and flying phalanger are all Australian marsupials from the adaptive radiation; options 1, 2 and 3 each include placental mammals (mole, flying squirrel, lemur, anteater, wolf, bobcat), so the answer is option $4$.

**Subtopic:** What is Adaptive Radiation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q182_bc1171b0_04112026.png?v=bc1171b040b6)

---

## Q183

Biology · zoology · Environmental Issues

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Electrostatic precipitator is most widely used in thermal power plant
- (Statement II) Electrostatic precipitator in thermal power plant removes ionising radiations

- **(1)** Statement I is correct but Statement II is incorrect.
- (2) Statement I is incorrect but Statement II is correct.
- (3) Both Statement I and Statement II are correct.
- (4) Both Statement I and Statement II are incorrect.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: the electrostatic precipitator is the most widely used method for removing particulate matter from thermal power plant exhaust, so Statement I is correct.
2. Statement II: an electrostatic precipitator removes about $99\%$ of particulate matter (charged dust particles); it does not remove ionising radiations, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect gives option $1$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 40)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q183_5dc8358e_04112026.png?v=5dc8358e77b1)

---

## Q184

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) RNA mutates at a faster rate.
- (Statement II) Viruses having RNA genome and shorter life span mutate and evolve faster.

- (1) Statement I is true but Statement II is false.
- (2) Statement I is false but Statement II is true.
- **(3)** Both Statement I and Statement II are true.
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: RNA is chemically less stable (reactive 2'-OH) and mutates at a faster rate than DNA, so it is true.
2. Statement II: because RNA mutates fast, viruses with an RNA genome and a short life span mutate and evolve faster, so it is true; both true is option $3$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q184_b5387c27_04112026.png?v=b5387c274d2f)

---

## Q185

Biology · zoology · Neural Control and Coordination

Match List I with List II with respect to human eye. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Fovea | I | Visible coloured portion of eye that regulates diameter of pupil. |
| B | Iris | II | External layer of eye formed of dense connective tissue. |
| C | Blind spot | III | Point of greatest visual acuity or resolution. |
| D | Sclera | IV | Point where optic nerve leaves the eyeball and photoreceptor cells are absent. |

- (1) A-I, B-IV, C-III, D-II
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Fovea is the point of greatest visual acuity: $A \to III$.
2. Iris is the visible coloured portion that regulates pupil diameter: $B \to I$.
3. Blind spot is where the optic nerve leaves the eyeball and photoreceptors are absent: $C \to IV$.
4. Sclera is the external layer of dense connective tissue: $D \to II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $3$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q185_0caa10a2_04112026.png?v=0caa10a28ef6)

---

## Q186

Biology · zoology · Cell Cycle and Cell Division

Select the correct statements. Choose the correct answer from the options given below:

- (A) Tetrad formation is seen during Leptotene.
- (B) During Anaphase, the centromeres split and chromatids separate.
- (C) Terminalization takes place during Pachytene.
- (D) Nucleolus, Golgi complex and ER are reformed during Telophase.
- (E) Crossing over takes place between sister chromatids of homologous chromosome.

- (1) A, C and E only
- (2) B and E only
- (3) A and C only
- **(4)** B and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A: tetrads are seen in pachytene after synapsis in zygotene, not leptotene, so A is false.
2. B: in (mitotic) anaphase the centromeres split and sister chromatids separate, so B is true.
3. C: terminalisation of chiasmata occurs in diakinesis, not pachytene, so C is false.
4. D: in telophase the nucleolus, Golgi complex and ER reform, so D is true.
5. E: crossing over occurs between non-sister chromatids of homologous chromosomes, so E is false.
6. True statements are B and D only, which is option $4$.

**Subtopic:** Phases of Cell Cycle, Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q186_7c5c0348_04112026.png?v=7c5c0348f974)

---

## Q187

Biology · zoology · Animal Kingdom

Select the correct statements with reference to chordates.
Choose the correct answer from the options given below:

- (A) Presence of a mid-dorsal, solid and double nerve cord.
- (B) Presence of closed circulatory system.
- (C) Presence of paired pharyngeal gill slits.
- (D) Presence of dorsal heart
- (E) Triploblastic pseudocoelomate animals.

- (1) B, D and E only
- (2) C, D and E only
- (3) A, C and D only
- **(4)** B and C only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A is false: the chordate nerve cord is dorsal, hollow and single, not solid and double.
2. B is true: chordates have a closed circulatory system.
3. C is true: chordates have paired pharyngeal gill slits.
4. D is false: the chordate heart is ventral.
5. E is false: chordates are triploblastic coelomates, not pseudocoelomates.
6. Only B and C are correct, which is option $4$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q187_9212b899_04112026.png?v=9212b89945b9)

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

- **(1)** B, C and D only
- (2) B and D only
- (3) A and E only
- (4) A, B and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In cockroach, excretion is by Malpighian tubules, aided by the fat body, nephrocytes and urecose glands, so $B$, $C$ and $D$ are excretory.
2. Phallic gland ($A$) is a male accessory reproductive gland and collaterial glands ($E$) are female reproductive glands, so $A$ and $E$ are not excretory.
3. Correct set is $B$, $C$ and $D$ only, which is option $1$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q188_3d27f275_04112026.png?v=3d27f275915a)

---

## Q189

Biology · zoology · Structural Organisation in Animals

Match List I with List II. Choose the correct answer from the options give below:

| List-I | | List-II | |
|---|---|---|---|
| A | Mast cells | I | Ciliated epithelium |
| B | Inner surface of bronchiole | II | Areolar connective tissue |
| C | Blood | III | Cuboidal epithelium |
| D | Tubular parts of nephron | IV | Specialised connective tissue |

- **(1)** A-II, B-I, C-IV, D-III
- (2) A-III, B-IV, C-II, D-I
- (3) A-I, B-II, C-IV, D-III
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Mast cells are a cell type found in areolar connective tissue, so $A \to II$.
2. The inner surface of bronchioles is lined by ciliated epithelium, so $B \to I$.
3. Blood is a specialised (fluid) connective tissue, so $C \to IV$.
4. The tubular parts of the nephron are lined by cuboidal epithelium, so $D \to III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $1$.

**Subtopic:** Connective Tissue, Animal Tissues: Epithelial Tissue · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 41)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q189_d43638f0_04112026.png?v=d43638f056a8)

---

## Q190

Biology · zoology · Cell Cycle and Cell Division

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (I) During $\mathrm{G_0}$ phase of cell cycle, the cell is metabolically inactive.
- (II) The centrosome undergoes duplication during S phase of interphase.

- (1) Statement I is correct but Statement II is incorrect.
- **(2)** Statement I is incorrect but Statement II is correct.
- (3) Both Statement I and Statement II are correct
- (4) Both Statement I and Statement II are incorrect.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Cells in the $\mathrm{G_0}$ (quiescent) phase remain metabolically active but no longer proliferate, so Statement I is incorrect.
2. During S phase of interphase the centriole (centrosome) duplicates in the cytoplasm, so Statement II is correct.
3. Statement I incorrect and Statement II correct is option $2$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q190_7412bde2_04112026.png?v=7412bde29a26)

---

## Q191

Biology · zoology · Strategies for Enhancement in Food Production

Which one of the following is NOT an advantage of inbreeding?

- (1) Elimination of less desirable genes and accumulation of superior genes takes place due to it.
- **(2)** It decreases the productivity of inbred population, after continuous inbreeding.
- (3) It decreases homozygosity.
- (4) It exposes harmful recessive genes but are eliminated by selection.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Inbreeding is mating of closely related individuals for $4$-$6$ generations, so it $\textit{increases}$ homozygosity.
2. Exposing harmful recessive genes so selection removes them (option $4$) is an advantage.
3. Eliminating less desirable genes and accumulating superior genes (option $1$) is an advantage.
4. Continued inbreeding reduces fertility and productivity, i.e. inbreeding depression (option $2$), which is a disadvantage.
5. Option $3$ is factually false (inbreeding increases homozygosity), so it is also not an advantage; the intended disadvantage is option $2$.

**Subtopic:** Animal Breeding · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q191_f7c6dbd0_04112026.png?v=f7c6dbd06be3)

---

## Q192

Biology · zoology · Structural Organisation in Animals

Which of the following is characteristic feature of cockroach regarding sexual dimorphism?

- (1) Presence of sclerites
- (2) Presence of anal cerci
- (3) Dark brown body colour and anal cerci
- **(4)** Presence of anal styles

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In cockroach, anal cerci, sclerites and the dark brown body colour are found in both sexes, whereas a pair of short, thread-like anal styles is present only in males, so anal styles show sexual dimorphism: option $4$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q192_908d5567_04112026.png?v=908d5567daf3)

---

## Q193

Biology · zoology · Neural Control and Coordination

The parts of human brain that helps in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:

- (1) Brain stem and epithalamus
- (2) Corpus callosum and thalamus
- **(3)** Limbic system and hypothalamus
- (4) Corpora quadrigemina and hippocampus

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT states that the inner parts of the cerebral hemispheres and associated deep structures (amygdala, hippocampus) form the limbic system, which along with the hypothalamus regulates sexual behaviour and emotional expression (excitement, pleasure, rage, fear), so the answer is option $3$.

**Subtopic:** Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q193_caac91bf_04112026.png?v=caac91bf99fc)

---

## Q194

Biology · zoology · Body Fluids and Circulation

Which of the following statements are correct? Choose the correct answer from the options given below:

- (A) Basophils are most abundant cells of the total WBCs
- (B) Basophils secrete histamine, serotonin and heparin
- (C) Basophils are involved in inflammatory response
- (D) Basophils have kidney shaped nucleus
- (E) Basophils are agranulocytes

- **(1)** B and C only
- (2) A and B only
- (3) D and E only
- (4) C and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A is false: neutrophils are the most abundant WBCs ($60$-$65\%$); basophils are the least ($0.5$-$1\%$).
2. B is true: basophils secrete histamine, serotonin and heparin.
3. C is true: basophils are involved in inflammatory reactions.
4. D is false: a kidney-shaped nucleus is a feature of monocytes, not basophils.
5. E is false: basophils are granulocytes, not agranulocytes.
6. Only B and C are correct, which is option $1$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q194_06b01277_04112026.png?v=06b012777ac7)

---

## Q195

Biology · zoology · Molecular Basis of Inheritance

Which one of the following is the sequence on corresponding coding strand, if the sequence on mRNA formed is as follows 5’AUCGAUCGAUCGAUCGAUCGAUCG AUCG 3’?

- **(1)** 5’ ATCGATCGATCGATCGATCGATCGATCG 3’
- (2) 3’ ATCGATCGATCGATCGATCGATCGATCG 5’
- (3) 5’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 3’
- (4) 3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The coding strand has the same sequence and the same $5' \rightarrow 3'$ polarity as the mRNA, except that DNA has $T$ where RNA has $U$.
2. Replacing $U$ with $T$ in $5'\,AUCG\ldots AUCG\,3'$ gives $5'\,ATCG\ldots ATCG\,3'$, which is option $1$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q195_39e94976_04112026.png?v=39e94976e727)

---

## Q196

Biology · zoology · Organisms and Populations

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Logistic growth | I | Unlimited resource availability condition |
| B | Exponential growth | II | Limited resource availability condition |
| C | Expanding age pyramid | III | The percent individuals of pre-reproductive age is largest followed by reproductive and post reproductive age groups |
| D | Stable age pyramid | IV | The percent individuals of pre-reproductives and reproductive age group are same |

- (1) A-II, B-IV, C-I, D-III
- (2) A-II, B-IV, C-III, D-I
- **(3)** A-II, B-I, C-III, D-IV
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Logistic growth: resources are limited, so $A \to II$.
2. Exponential growth: resources are unlimited, so $B \to I$.
3. Expanding age pyramid: pre-reproductive individuals are largest, then reproductive, then post-reproductive, so $C \to III$.
4. Stable age pyramid: pre-reproductive and reproductive groups are about equal, so $D \to IV$.
5. $A\text{-}II, B\text{-}I, C\text{-}III, D\text{-}IV$ is option $3$.

**Subtopic:** Life History Variation and Population Attributes, Logistic Growth · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 43)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q196_f38da4ee_04112026.png?v=f38da4eebf0a)

---

## Q197

Biology · zoology · Chemical Coordination and Integration

Which of the following are NOT under the control of thyroid hormone? Choose the correct answer from the options given below:

- (A) Maintenance of water and electrolyte balance
- (B) Regulation of basal metabolic rate
- (C) Normal rhythm of sleep-wake cycle
- (D) Development of immune system
- (E) Support the process of RBCs formation

- **(1)** C and D only
- (2) D and E only
- (3) A and D only
- (4) B and C only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Per NCERT, thyroid hormones regulate $\text{BMR}$ (B), support the process of RBC formation (E) and maintain water and electrolyte balance (A).
2. Normal rhythm of the sleep-wake cycle (C) is regulated by melatonin from the pineal gland, not thyroid hormone.
3. Development of the immune system (D) is promoted by thymosins from the thymus, not thyroid hormone.
4. So the items NOT under thyroid control are C and D, which is option $1$.

**Subtopic:** Thyroid Gland and Parathyroid Gland · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 43)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q197_8ef07cd1_04112026.png?v=8ef07cd12989)

---

## Q198

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements are correct? Choose the correct answer from the options given below:

- (A) An excessive loss of body fluid from the body switches off osmoreceptors.
- (B) ADH facilitates water reabsorption to prevent diuresis.
- (C) ANF causes vasodilation.
- (D) ADH causes increase in blood pressure.
- (E) ADH is responsible for decrease in GFR.

- (1) A, B and E only
- (2) C, D and E only
- (3) A and B only
- **(4)** B, C and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A: excessive loss of body fluid activates osmoreceptors, which trigger ADH release, so A is false.
2. B: ADH facilitates water reabsorption in the distal tubule and collecting duct, preventing diuresis, so B is true.
3. C: ANF causes vasodilation and lowers blood pressure, so C is true.
4. D: ADH constricts blood vessels, raising blood pressure, so D is true.
5. E: by raising blood pressure, ADH can increase glomerular blood flow and GFR, not decrease it, so E is false.
6. True set $= \{B, C, D\}$, which is option $4$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 43)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q198_1ae45738_04112026.png?v=1ae4573861f4)

---

## Q199

Biology · zoology · Locomotion and Movement

Which of the following statements are correct regarding skeletal muscle? Choose the most appropriate answer from the options given below:

- (A) Muscle bundles are held together by collagenous connective tissue layer called fascicle.
- (B) Sarcoplasmic reticulum of muscle fibre is a store house of calcium ions.
- (C) Striated appearance of skeletal muscle fibre is due to distribution pattern of actin and myosin proteins.
- (D) M line is considered as functional unit of contraction called sarcomere.

- (1) A, C and D only
- (2) C and D only
- (3) A, B and C only
- **(4)** B and C only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement A: muscle bundles (fascicles) are held together by a collagenous connective tissue layer called fascia, not fascicle, so $A$ is false.
2. Statement B: the sarcoplasmic reticulum stores $\mathrm{Ca^{2+}}$ ions, so $B$ is true.
3. Statement C: the striations come from the distribution pattern of actin and myosin, so $C$ is true.
4. Statement D: the sarcomere is the part of the myofibril between two successive Z lines, not the M line, so $D$ is false.
5. Correct set is $\{B, C\}$, which is option $4$.

**Subtopic:** Structure of Skeletal Muscle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 43)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q199_9574e387_04112026.png?v=9574e38742c1)

---

## Q200

Biology · zoology · Animal Kingdom

The unique mammalian characteristics are:

- (1) hairs, pinna and indirect development
- (2) pinna, monocondylic skull and mammary glands
- (3) hairs, tympanic membrane and mammary glands
- **(4)** hairs, pinna and mammary glands

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT: the most unique mammalian characteristics are mammary glands, hair on the skin and external ears (pinnae), so option $4$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2023/2023_H1/crops/q200_d02f2042_04112026.png?v=d02f204203ec)

