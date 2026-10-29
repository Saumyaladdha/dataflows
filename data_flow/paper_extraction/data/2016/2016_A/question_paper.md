# NEET (UG) 2016 · Code A

180 questions · source `NEET_Papers/2016/NEET_2016_Phase1_Code_A_official.pdf` · every image a CDN link (0 without one) · 0 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Rotational Motion

From a disc of radius $R$ and mass $M$, a circular hole of diameter $R$, whose rim passes through the centre is cut. What is the moment of inertia of the remaining part of the disc about a perpendicular axis, passing through the centre?

- (1) $15\,MR^{2}/32$
- **(2)** $13\,MR^{2}/32$
- (3) $11\,MR^{2}/32$
- (4) $9\,MR^{2}/32$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $I = \frac{MR^{2}}{2} - \frac{3\sigma}{2}\pi\left(\frac{R}{2}\right)^{2}\left(\frac{R}{2}\right)^{2}$
2. Where $\sigma = \frac{M}{\pi R^{2}}$

![printed figure: Disc of radius R and mass M with a hole of radius R/2 whose rim passes through the centre](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q001_sol_1_033be4bf_28102026.png?v=033be4bffb4b)

*Disc of radius R and mass M with a hole of radius R/2 whose rim passes through the centre*

3. $I = \frac{MR^{2}}{2} - \frac{3}{32}MR^{2}$
4. $I = \frac{13}{32}MR^{2}$

**Solved independently** (answer withheld)

1. The hole has radius $r = R/2$, so its mass is $m = M\frac{(R/2)^2}{R^2} = \frac{M}{4}$.
2. MI of the hole about its own centre: $I_c = \frac{1}{2} m r^2 = \frac{1}{2}\cdot\frac{M}{4}\cdot\frac{R^2}{4} = \frac{MR^2}{32}$.
3. The hole's centre is at distance $R/2$ from the disc centre, so by the parallel axis theorem $I_O = \frac{MR^2}{32} + \frac{M}{4}\left(\frac{R}{2}\right)^2 = \frac{3MR^2}{32}$.
4. Full disc: $I_{disc} = \frac{1}{2}MR^2 = \frac{16MR^2}{32}$.
5. Remaining: $I = \frac{16MR^2}{32} - \frac{3MR^2}{32} = \frac{13MR^2}{32}$, which is option $2$.

**Subtopic:** Moment of Inertia of a Circular Shape, Parallel Axis and Perpendicular Axis Theorem · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 1)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q001_76703d73_28102026.png?v=76703d733e9e)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q001_eea35212_28102026.png?v=eea352127532)

---

## Q2

Physics · Magnetic Effect of Electric Current

A square loop ABCD carrying a current i, is placed near and coplanar with a long straight conductor XY carrying a current I, the net force on the loop will be:

![printed figure: Square loop ABCD of side L carrying current i, at distance L/2 from a long straight wire XY carrying current I](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q002_f0aa6a97_28102026.png?v=f0aa6a976e36)

*Square loop ABCD of side L carrying current i, at distance L/2 from a long straight wire XY carrying current I*

- **(1)** $\dfrac{2\mu_0 Ii}{3\pi}$
- (2) $\dfrac{\mu_0 Ii}{2\pi}$
- (3) $\dfrac{2\mu_0 IiL}{3\pi}$
- (4) $\dfrac{\mu_0 IiL}{2\pi}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $F_1 = \frac{\mu_0 IiL}{2\pi \frac{L}{2}} = \frac{\mu_0 Ii}{\pi}$
2. $2 = \frac{\mu_0 IiL}{2\pi \frac{3L}{2}} = \frac{\mu_0 Ii}{3\pi}$

![printed figure: Long wire carrying I beside a square loop of side L at distance L/2, with forces F1 and F2 on the near and far sides](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q002_sol_1_5fb330cf_28102026.png?v=5fb330cf453e)

*Long wire carrying I beside a square loop of side L at distance L/2, with forces F1 and F2 on the near and far sides*

3. $\therefore F_{net} = F_1 - F_2$
4. $F_{net} = \frac{2}{3}\frac{\mu_0 Ii}{\pi}$

**Solved independently** (answer withheld)

1. Forces on the perpendicular sides BC and DA are equal and opposite, so they cancel.
2. Side AB is at distance $L/2$: $F_{AB} = \frac{\mu_0 I i L}{2\pi (L/2)} = \frac{\mu_0 I i}{\pi}$.
3. Side CD is at distance $3L/2$: $F_{CD} = \frac{\mu_0 I i L}{2\pi (3L/2)} = \frac{\mu_0 I i}{3\pi}$.
4. AB and CD carry opposite currents, so their forces are opposite: $F_{net} = \frac{\mu_0 I i}{\pi} - \frac{\mu_0 I i}{3\pi} = \frac{2\mu_0 I i}{3\pi}$, which is option $1$.

**Subtopic:** Force Between Two Parallel Current-Carrying Conductors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q002_9448d428_28102026.png?v=9448d4288d17)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q002_ed9d71ba_28102026.png?v=ed9d71ba9ed7)

---

## Q3

Physics · Magnetic Effect of Electric Current

The magnetic susceptibility is negative for:

- **(1)** diamagnetic material only
- (2) paramagnetic material only
- (3) ferromagnetic material only
- (4) paramagnetic and ferromagnetic materials

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Magnetic susceptibility $\chi_m$ is negative for diamagnetic substance only

**Solved independently** (answer withheld)

1. Diamagnetic materials develop magnetisation opposite to the applied field, so $\chi < 0$ (with $-1 \le \chi < 0$), while paramagnetic ($0 < \chi \ll 1$) and ferromagnetic ($\chi \gg 1$) materials have positive $\chi$; hence negative susceptibility is for diamagnetic material only, option $1$.

**Subtopic:** Diamagnetism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q003_146a8e98_28102026.png?v=146a8e98105a)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q003_5c10696c_28102026.png?v=5c10696ce6d9)

---

## Q4

Physics · Waves

A siren emitting a sound of frequency $800\,\mathrm{Hz}$ moves away from an observer towards a cliff at a speed of $15\,\mathrm{ms^{-1}}$. Then, the frequency of sound that the observer hears in the echo reflected from the cliff is : (Take velocity of sound in air $= 330\,\mathrm{ms^{-1}}$)

- (1) $765\,\mathrm{Hz}$
- (2) $800\,\mathrm{Hz}$
- **(3)** $838\,\mathrm{Hz}$
- (4) $885\,\mathrm{Hz}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $f_{0} = 800\,\mathrm{Hz}$
2. $V_{\mathrm{source}} = 15\,\mathrm{m/s}$

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q004_sol_1_ea630586_28102026.png?v=ea630586e677)

3. $f_{a} = \frac{330}{(330 - 15)}800 = \frac{330}{315} \times 800$
4. $f_{a} = 838\,\mathrm{Hz}$

**Solved independently** (answer withheld)

1. The siren (source) moves towards the stationary cliff at $v_s = 15\,\mathrm{m\,s^{-1}}$, so the cliff receives $f' = f\frac{v}{v - v_s}$.
2. $f' = 800 \times \frac{330}{330 - 15} = 800 \times \frac{330}{315}$.
3. $f' = 838.1\,\mathrm{Hz} \approx 838\,\mathrm{Hz}$.
4. The cliff is stationary and reflects $f'$; the observer is also stationary, so the echo is heard at $838\,\mathrm{Hz}$, which is option $3$.

**Subtopic:** Doppler Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q004_86ed28d1_28102026.png?v=86ed28d19fc9)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q004_a906b261_28102026.png?v=a906b261f911)

---

## Q5

Physics · Capacitance

A capacitor of $2\,\mu\mathrm{F}$ is charged as shown in the diagram. When the switch S is turned to position 2, the percentage of its stored energy dissipated is:

![printed figure: Cell V and a 2 μF capacitor joined through switch S at position 1; an 8 μF capacitor waits at position 2](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q005_bd031520_28102026.png?v=bd031520319b)

*Cell V and a 2 μF capacitor joined through switch S at position 1; an 8 μF capacitor waits at position 2*

- (1) $0\%$
- (2) $20\%$
- (3) $75\%$
- **(4)** $80\%$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $Q = 2V$
2. $U_{i} = \frac{1}{2} \times \frac{(2V)^{2}}{2} = V^{2}$

![printed figure: A cell V charging a 2 μF capacitor through a closed switch in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q005_sol_1_b2275b24_28102026.png?v=b2275b246a5e)

*A cell V charging a 2 μF capacitor through a closed switch in one loop*

3. $\therefore V_{y} = \frac{1}{2}\frac{64V^{2}}{25 \times 8}$
4. $\frac{2V - q}{2} = \frac{q}{8} + \frac{1}{2}\frac{4V^{2}}{25 \times 2}$
5. $\therefore 8V - 4q = q$
6. $U_{f} = \frac{5V^{2}}{25} = \frac{V^{2}}{5}$
7. $\therefore q = \frac{8V}{5}$
8. Energy dissipated $= \frac{4V^{2}}{5}$

![printed figure: The charged 2 μF capacitor connected across the 8 μF capacitor in one loop, charge q on the 8 μF](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q005_sol_2_115f31bd_28102026.png?v=115f31bddcad)

*The charged 2 μF capacitor connected across the 8 μF capacitor in one loop, charge q on the 8 μF*

9. $\therefore \%$ energy
10. Dissipated $= \frac{4V^{2}}{5V^{2}} \times 100$
11. $= 80\%$

**Solved independently** (answer withheld)

1. In position 1 the $2\,\mu\mathrm{F}$ capacitor charges to $V$: $U_i = \frac{1}{2}(2)V^2 = V^2$ (in $\mu\mathrm{J}$ units), $Q = 2V$.
2. In position 2 it connects in parallel with the uncharged $8\,\mu\mathrm{F}$ capacitor; charge is conserved, so $V' = \frac{Q}{C_1 + C_2} = \frac{2V}{10} = \frac{V}{5}$.
3. $U_f = \frac{1}{2}(10)\left(\frac{V}{5}\right)^2 = \frac{V^2}{5}$.
4. Energy dissipated $= U_i - U_f = \frac{4}{5}V^2$, i.e. $\frac{U_i - U_f}{U_i} = \frac{C_2}{C_1 + C_2} = \frac{8}{10} = 80\%$, which is option $4$.

**Subtopic:** Redistribution of Charges · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q005_6d57c391_28102026.png?v=6d57c391ba1a)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q005_a8d8900b_28102026.png?v=a8d8900b10d8)

---

## Q6

Physics · Wave Optics

In a diffraction pattern due to a single slit of width ‘a’, the first minimum is observed at an angle $30^{\circ}$ when light of wavelength $5000\,\text{Å}$ is incident on the slit. The first secondary maximum is observed at an angle of:

- (1) $\sin^{-1}\left(\frac{1}{4}\right)$
- (2) $\sin^{-1}\left(\frac{2}{3}\right)$
- (3) $\sin^{-1}\left(\frac{1}{2}\right)$
- **(4)** $\sin^{-1}\left(\frac{3}{4}\right)$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $a\sin 30 = \lambda$
2. $a\sin\theta = \frac{3\lambda}{2}$
3. $\frac{\sin\theta}{\sin 30} = \frac{3}{2}$
4. $\sin\theta = \frac{3}{2} \times \frac{1}{2}$
5. $\sin\theta = \frac{3}{4}$
6. $\theta = \sin\left(\frac{3}{4}\right)$

**Solved independently** (answer withheld)

1. First minimum of a single slit: $a\sin\theta_1 = \lambda$.
2. With $\theta_1 = 30^{\circ}$: $a \cdot \frac{1}{2} = \lambda \Rightarrow a = 2\lambda$.
3. First secondary maximum (approximately): $a\sin\theta = \frac{3\lambda}{2}$.
4. $\sin\theta = \frac{3\lambda}{2 \cdot 2\lambda} = \frac{3}{4}$.
5. $\theta = \sin^{-1}\left(\frac{3}{4}\right)$, which is option $4$.

**Subtopic:** Diffraction of Light · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q006_1a372df2_28102026.png?v=1a372df2d213)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q006_75f6fdee_28102026.png?v=75f6fdeebe9f)

---

## Q7

Physics · Gravitation

At what height from the surface of earth the gravitation potential and the value of g are $-5.4 \times 10^{7}\,\mathrm{J\,kg^{-2}}$ and $6.0\,\mathrm{ms^{-2}}$ respectively? Take the radius of earth as $6400\,\mathrm{km}$:

- **(1)** $2600\,\mathrm{km}$
- (2) $1600\,\mathrm{km}$
- (3) $1400\,\mathrm{km}$
- (4) $2000\,\mathrm{km}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $V = \frac{GM}{R + h} = -5.4 \times 10^{7}$
2. $g = \frac{GM}{(R + h)^{2}} = 6$
3. $\therefore \frac{5.4}{6} \times 10^{7} = R + h$
4. $\therefore a \times 10^{6} = 6.4 \times 10^{6} + h$
5. $\therefore h = 2600\,\mathrm{km}$

**Solved independently** (answer withheld)

1. At distance $r = R + h$ from the centre, $V = -\frac{GM}{r}$ and $g = \frac{GM}{r^2}$.
2. Dividing, $\frac{|V|}{g} = \frac{GM/r}{GM/r^2} = r$.
3. $r = \frac{5.4 \times 10^{7}}{6.0} = 9.0 \times 10^{6}\,\mathrm{m} = 9000\,\mathrm{km}$.
4. $h = r - R = 9000\,\mathrm{km} - 6400\,\mathrm{km} = 2600\,\mathrm{km}$, which is option $1$.

**Subtopic:** Variation in g Due to Height and Rotation, Calculation of Gravitational Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q007_007b3692_28102026.png?v=007b36920331)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q007_aa554a77_28102026.png?v=aa554a77ff0a)

---

## Q8

Physics · Electromagnetic Waves

Out of the following options which one can be used to produce a propagating electromagnetic wave?

- (1) A charge moving at constant velocity
- (2) A stationary charge
- (3) A chargeless particle
- **(4)** An accelerating charge

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. An accelerating charge can produce electromagnetic wave.

**Solved independently** (answer withheld)

1. A stationary charge produces only a static electric field, so it gives no propagating wave.
2. A charge moving at constant velocity produces a steady current-like field configuration (electric and magnetic fields that move with it) but does not radiate.
3. A chargeless particle produces no electromagnetic field at all.
4. An accelerating charge produces time-varying $\vec{E}$ and $\vec{B}$ fields that sustain each other and propagate, so it radiates an electromagnetic wave: option $4$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q008_d5030de7_28102026.png?v=d5030de7c78a)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q008_b2509e5d_28102026.png?v=b2509e5d9784)

---

## Q9

Physics · Electrostatics

Two identical charged spheres suspended from a common point by two massless strings of lengths $l$, are initially at a distance $\mathrm{d}(\mathrm{d} << l)$ apart because of their mutual repulsion. The charges begin to leak from both the spheres at a constant rate. As a result, the spheres approach each other with a velocity $\upsilon$. Then $\upsilon$ varies as a function of the distance $x$ between the spheres, as

- (1) $\upsilon \propto \mathrm{x}^{\frac{1}{2}}$
- (2) $\upsilon \propto \mathrm{x}$
- **(3)** $\upsilon \propto \mathrm{x}^{-\frac{1}{2}}$
- (4) $\upsilon \propto \mathrm{x}^{-1}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Two charged spheres hanging from a common point by strings of length l, with the forces on the left sphere](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q009_sol_1_673b5460_28102026.png?v=673b5460d6ea)

*Two charged spheres hanging from a common point by strings of length l, with the forces on the left sphere*

1. $\theta = \frac{\mathrm{x}}{2l}$
2. $\mathrm{f_e}\cos\theta = \mathrm{mgh}\lambda\theta$
3. $\mathrm{f_e} = \mathrm{mg}.\left(\frac{\mathrm{x}}{2}\right)$
4. $\frac{\mathrm{kq}^{2}}{\mathrm{x}^{2}} = \frac{\mathrm{mgx}}{2\mathrm{e}}$
5. $\mathrm{kq}^{2} = \frac{\mathrm{mg}}{2l}\mathrm{x}^{3}$
6. $\mathrm{q} \propto \mathrm{x}^{\frac{3}{2}}$
7. $\frac{\mathrm{dq}}{\mathrm{dt}} \propto \frac{3}{2}\,\mathrm{x}^{\frac{1}{2}}.\frac{\mathrm{dx}}{\mathrm{dt}}$
8. $\Rightarrow \mathrm{x}^{\frac{1}{2}}.\mathrm{v} = \mathrm{constant}$
9. $\mathrm{v} \propto \mathrm{x}^{-\frac{1}{2}}$

**Solved independently** (answer withheld)

1. For each sphere, balancing forces gives $\tan\theta = \frac{F}{mg}$ with $F = \frac{kq^2}{x^2}$.
2. Since $x \ll l$, $\tan\theta \approx \sin\theta = \frac{x/2}{l} = \frac{x}{2l}$.
3. $\frac{x}{2l} = \frac{kq^2}{x^2 mg} \Rightarrow q^2 = \frac{mg}{2lk}x^3 \Rightarrow q \propto x^{3/2}$.
4. Differentiate: $\frac{dq}{dt} \propto \frac{3}{2}x^{1/2}\frac{dx}{dt}$.
5. $\frac{dq}{dt}$ is constant, so $\upsilon = \frac{dx}{dt} \propto x^{-1/2}$, which is option $3$.

**Subtopic:** Coulomb's Law · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 6)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q009_93f729fb_28102026.png?v=93f729fb203d)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q009_d3768051_28102026.png?v=d37680510f8a)

---

## Q10

Physics · Waves

A uniform rope of length $L$ and mass $m_1$, hangs vertically from a rigid support. A block of mass $m_2$ is attached to the free end of the rope. A transverse pulse of wavelength $\lambda_1$ is produced at the lower end of the rope. The wavelength of the pulse when it reaches the top of the rope is $\lambda_2$. The ratio $\lambda_2/\lambda_1$ is:

- (1) $\sqrt{\dfrac{m_1}{m_2}}$
- **(2)** $\sqrt{\dfrac{m_1+m_2}{m_2}}$
- (3) $\sqrt{\dfrac{m_1}{m_2}}$
- (4) $\sqrt{\dfrac{m_1+m_2}{m_1}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. At bottom

![printed figure: A rope of length L and mass M1 hanging from a rigid support with a block M2 at its lower end](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q010_sol_1_3629c0e9_28102026.png?v=3629c0e91683)

*A rope of length L and mass M1 hanging from a rigid support with a block M2 at its lower end*

2. $v_1 = \sqrt{\frac{M_2 g L}{M_1}}$
3. $\therefore \lambda_1 = \sqrt{\frac{M_2}{M_1} g L \frac{1}{f}}$
4. At top.
5. $\therefore \frac{\lambda_2}{\lambda_1} = \sqrt{\frac{M_1 + M_2}{M_2}}$
6. $v_1 = \sqrt{\frac{(M_1 + M_2) g L}{M_1}}$
7. $\therefore \lambda_2 = \sqrt{\frac{(M_1 + M_2) g L}{M_1}} \frac{1}{f}$

**Solved independently** (answer withheld)

1. The frequency of the pulse is set by the source and does not change along the rope, so $\lambda = \frac{v}{f} \propto v$.
2. Wave speed on the rope is $v = \sqrt{\frac{T}{\mu}}$ with $\mu = \frac{m_1}{L}$ uniform, so $\lambda \propto \sqrt{T}$.
3. At the lower end the rope supports only the block: $T_1 = m_2 g$.
4. At the top the rope supports the block and the whole rope: $T_2 = (m_1 + m_2) g$.
5. $\frac{\lambda_2}{\lambda_1} = \sqrt{\frac{T_2}{T_1}} = \sqrt{\frac{m_1 + m_2}{m_2}}$, which is option $2$.

**Subtopic:** Speed of Different Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q010_95c1ad47_28102026.png?v=95c1ad4732ed)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q010_d0f0eb4d_28102026.png?v=d0f0eb4d2c07)

---

## Q11

Physics · Thermodynamics

A refrigerator works between $4^{\circ}\mathrm{C}$ and $30^{\circ}\mathrm{C}$. It is required to remove $600$ calories of heat every second in order to keep the temperature of the refrigerated space constant. The power required is: (Take $1\,\mathrm{cal} = 4.2$ Joules)

- (1) $2.365\,\mathrm{W}$
- (2) $23.65\,\mathrm{W}$
- **(3)** $236.5\,\mathrm{W}$
- (4) $2365\,\mathrm{W}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Refrigerator box: work W in from above, heat 600 = Q1 out to the right](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q011_sol_1_db57929b_28102026.png?v=db57929b035d)

*Refrigerator box: work W in from above, heat 600 = Q1 out to the right*

1. $\frac{600 + w}{600} = \frac{303}{277}$
2. $1 + \frac{w}{600} = 1 + \frac{26}{277}$
3. $w = 600 \times \frac{26}{277} \times 4.2$
4. $w = 236.5$

**Solved independently** (answer withheld)

1. $T_L = 4 + 273 = 277\,\mathrm{K}$, $T_H = 30 + 273 = 303\,\mathrm{K}$.
2. Heat removed per second $Q_L = 600 \times 4.2 = 2520\,\mathrm{J/s}$.
3. For an ideal refrigerator $\beta = \frac{Q_L}{W} = \frac{T_L}{T_H - T_L} = \frac{277}{26} \approx 10.654$.
4. $P = \frac{Q_L}{\beta} = \frac{2520 \times 26}{277} \approx 236.5\,\mathrm{W}$, which is option $3$.

**Subtopic:** Refrigerator and Heat Pump · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q011_ca233a4c_28102026.png?v=ca233a4c3cff)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q011_04d40e35_28102026.png?v=04d40e35aa17)

---

## Q12

Physics · Waves

An air column, closed at one end and open at the other, resonates with a tuning fork when the smallest length of the column is $50\,\mathrm{cm}$. The next larger length of the column resonating with the same tuning fork is:

- (1) $66.7\,\mathrm{cm}$
- (2) $100\,\mathrm{cm}$
- **(3)** $150\,\mathrm{cm}$
- (4) $200\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. First minimum resonating length for closed organ pipe $= \frac{\lambda}{4} = 50\,cm$
2. $\therefore$ Next larger length of air column $= \frac{3\lambda}{4} = 150\,cm$

**Solved independently** (answer withheld)

1. For a column closed at one end, resonance lengths are $l = \frac{(2n-1)\lambda}{4}$, i.e. $\frac{\lambda}{4}, \frac{3\lambda}{4}, \dots$
2. Smallest length: $\frac{\lambda}{4} = 50\,\mathrm{cm} \Rightarrow \lambda = 200\,\mathrm{cm}$.
3. Next length: $\frac{3\lambda}{4} = 3 \times 50\,\mathrm{cm} = 150\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q012_184c8cc5_28102026.png?v=184c8cc59b1b)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q012_fcf69a4b_28102026.png?v=fcf69a4bcd70)

---

## Q13

Physics · Semiconductor Electronics

Consider the junction diode as ideal. The value of current flowing through AB is:

![printed figure: Ideal diode and 1 kΩ resistor in series between A (+4 V) and B (−6 V)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q013_43a8b2a3_28102026.png?v=43a8b2a3e96f)

*Ideal diode and 1 kΩ resistor in series between A (+4 V) and B (−6 V)*

- (1) $0\,\mathrm{A}$
- **(2)** $10^{-2}\,A$
- (3) $10^{-1}\,A$
- (4) $10^{-3}\,A$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{V_A} - \mathrm{V_3} = 4 - (-6) = 10$
2. $\therefore\ \mathrm{i} = \frac{10}{1000} = 10^{-2}\,\mathrm{A}$

**Solved independently** (answer withheld)

1. The diode's arrow points from $A$ towards $B$, and $V_A = +4\,\mathrm{V} > V_B = -6\,\mathrm{V}$, so the diode is forward biased.
2. An ideal forward-biased diode has zero resistance, so the whole potential difference falls across the resistor: $V_A - V_B = 4 - (-6) = 10\,\mathrm{V}$.
3. $I = \frac{10\,\mathrm{V}}{1\times10^{3}\,\Omega} = 10^{-2}\,\mathrm{A}$, which is option $2$.

**Subtopic:** PN Junction Diode Under Forward Bias · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q013_daf727d0_28102026.png?v=daf727d041c6)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q013_5cd890ad_28102026.png?v=5cd890ad8228)

---

## Q14

Physics · Current Electricity

The charge flowing through a resistance $R$ varies with time $t$ as $Q = at - bt^{2}$ where $a$ and $b$ are positive constants. The total heat produced in $R$ is :

- **(1)** $\frac{a^{3}R}{6b}$
- (2) $\frac{a^{3}R}{3b}$
- (3) $\frac{a^{3}R}{2b}$
- (4) $\frac{a^{3}R}{b}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $Q = at - bt^{2}$
2. $\therefore t \in \left[0, \frac{a}{b}\right]$
3. $i = \frac{dq}{dt} = a - 2bt$
4. Note: $i$ is +ve $t \in \left(0, \frac{a}{2b}\right)$
5. And $i$ is – ve $t \in \left(\frac{a}{2b}, \frac{a}{b}\right)$
6. Positive current means current one direction and negative current means current in opposite direction.
7. $\therefore dH = i^{2}Rdt$
8. $= (a - 2bt)^{2}R\,dt$
9. $H = \int_{0}^{\frac{a}{b}} (a - 2bt)^{2}\,R\,dt$
10. $= \left.\frac{(a - 2bt)^{3}R}{3(-2b)}\right|_{0}^{\frac{a}{b}}$
11. $= \frac{1}{-b}\left[\left(a - 2b\frac{a}{b}\right)^{3} - (a)^{3}\right]R$
12. $= -\frac{1}{6b}[(-a)^{3} - a^{3}]R$
13. $H = \frac{a^{3}R}{3b}$

**Solved independently** (answer withheld)

1. The current is $I = \frac{dQ}{dt} = a - 2bt$.
2. The current becomes zero at $t_0 = \frac{a}{2b}$, so heat is produced over $0 \le t \le \frac{a}{2b}$.
3. $H = \int_0^{a/2b} I^2 R\,dt = R\int_0^{a/2b} (a - 2bt)^2\,dt$.
4. $\int (a-2bt)^2\,dt = -\frac{(a-2bt)^3}{6b}$.
5. $H = R\left[0 - \left(-\frac{a^3}{6b}\right)\right] = \frac{a^3 R}{6b}$, which is option $1$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q014_089d5e57_28102026.png?v=089d5e5720b8)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q014_cf064e76_28102026.png?v=cf064e769120)

---

## Q15

Physics · Thermal Properties of Matter

> ⚠ The independent solve chose (4); the booklet prints (3).

A black body is at a temperature of $5760\,\mathrm{K}$. The energy of radiation emitted by the body at wavelength $250\,\mathrm{nm}$ is $\mathrm{U_1}$, at wavelength $500\,\mathrm{nm}$ is $\mathrm{U_2}$ and that at $1000\,\mathrm{nm}$ is $\mathrm{U_3}$. Wien’s constant, $\mathrm{b} = 2.88 \times 10^{6}\,\mathrm{nmK}$. Which of the following is correct?

- (1) $\mathrm{U_1} = 0$
- (2) $\mathrm{U_3} = 0$
- **(3)** $\mathrm{U_1} > \mathrm{U_2}$
- (4) $\mathrm{U_2} > \mathrm{U_1}$

**Answer** — booklet: (3) · independent solve: (4) · differs

**Publisher's solution**

1. $\lambda_{\mathrm{min}}\,\mathrm{T} = \mathrm{b}$
2. $\lambda \propto \frac{1}{\mathrm{T}}$
3. $\mathrm{u} \propto (\mathrm{T})^{4} \propto \frac{1}{(\lambda)^{4}}$
4. So $\mathrm{u_1} > \mathrm{u_2}$

**Solved independently** (answer withheld)

1. Wien's displacement law: $\lambda_{max} T = b$.
2. $\lambda_{max} = \frac{b}{T} = \frac{2.88 \times 10^{6}\,\mathrm{nm\,K}}{5760\,\mathrm{K}} = 500\,\mathrm{nm}$.
3. The spectral emission peaks at $500\,\mathrm{nm}$, so $U_2$ is the largest of the three and $U_2 > U_1$.
4. A black body at $T > 0$ emits at every wavelength, so $U_1 \neq 0$ and $U_3 \neq 0$; options $1$ and $2$ fail, option $3$ contradicts the peak, leaving option $4$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q015_a7b96cb5_28102026.png?v=a7b96cb57810)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q015_e6f778ee_28102026.png?v=e6f778ee713f)

---

## Q16

Physics · Thermal Properties of Matter

Coefficient of linear expansion of brass and steel rods are $\alpha_1$ and $\alpha_2$. Lengths of brass and steel rods are $l_1$ and $l_2$ respectively. If $(l_2 - l_1)$ is maintained same at all temperatures, which one of the following relations holds good?

- (1) $\alpha_1^2 l_2 = \alpha_2^2 l_1$
- (2) $\alpha_1 l_2^2 = \alpha_2 l_1^2$
- (3) $\alpha_1^2 l_2 = \alpha_2^2 l_1$
- **(4)** $\alpha_1 l_1 = \alpha_2 l_2$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Difference in length are same so increase in length are equal
2. $\Delta l_1 = \Delta l_2$
3. $l_1 \alpha_2 \Delta T = l_2 \alpha_2 \Delta T$
4. $\Rightarrow l_1 \alpha_1 = l_2 \alpha_2$

**Solved independently** (answer withheld)

1. Expansion of each rod: $\Delta l_1 = l_1 \alpha_1 \Delta T$ and $\Delta l_2 = l_2 \alpha_2 \Delta T$.
2. For $(l_2 - l_1)$ to stay the same at all temperatures, $\Delta l_2 - \Delta l_1 = 0$.
3. $l_2 \alpha_2 \Delta T = l_1 \alpha_1 \Delta T \Rightarrow \alpha_1 l_1 = \alpha_2 l_2$, which is option $4$.

**Subtopic:** Thermal Expansion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q016_1f80f66c_28102026.png?v=1f80f66cb7a2)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q016_e880a39c_28102026.png?v=e880a39ce6b1)

---

## Q17

Physics · Semiconductor Electronics

A npn transistor is connected in common emitter configuration in a given amplifier. A load resistance of $800\,\Omega$ is connected in the collector circuit and the voltage drop across it is $0.8\,\mathrm{V}$. If the current amplification factor is $0.96$ and the input resistance of the circuit is $192\,\Omega$, the voltage gain and the power gain of the amplifier will respectively be:

- **(1)** $4$, $3.84$
- (2) $3.69$, $3.84$
- (3) $4$, $4$
- (4) $4$, $3.69$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Voltage gain $= \beta.\left(\frac{\mathrm{R_C}}{\mathrm{R_B}}\right)$
2. $\mathrm{V} = 0.96\left(\frac{80}{192}\right)$
3. $\mathrm{V} = \frac{96 \times 8}{192} = 4$
4. And power gain of the amplifier is
5. $\beta_{\mathrm{ac}}.\mathrm{A_v}$
6. $= 0.96 \times 4$
7. $= 3.84$

**Solved independently** (answer withheld)

1. Take the given current amplification factor as the CE current gain: $\beta = 0.96$.
2. Voltage gain: $A_V = \beta \frac{R_L}{R_i} = 0.96 \times \frac{800}{192}$.
3. $\frac{800}{192} = 4.1\overline{6}$, so $A_V = 0.96 \times 4.1\overline{6} = 4$.
4. Power gain: $A_P = \beta \times A_V = 0.96 \times 4 = 3.84$.
5. $A_V = 4$, $A_P = 3.84$, which is option $1$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q017_433ff498_28102026.png?v=433ff498b4d4)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q017_ed5862ca_28102026.png?v=ed5862ca525e)

---

## Q18

Physics · Wave Optics

The intensity at the maximum in a Young’s double slit experiment is $\mathrm{I_0}$. Distance between two slits is $\mathrm{d} = 5\lambda$, where $\lambda$ is the wavelength of light used in the experiment. What will be the intensity in front of one of the slits on the screen placed at a distance $\mathrm{D} = 10\,\mathrm{d}$?

- (1) $\mathrm{I_0}$
- (2) $\frac{\mathrm{I_0}}{4}$
- (3) $\frac{3}{4}\mathrm{I_0}$
- **(4)** $\frac{\mathrm{I_0}}{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In YDSE $\mathrm{I_{max}} = \mathrm{I_0}$
2. Path difference at a point in front of one of shifts is
3. $\Delta\mathrm{x} = \mathrm{d}\left(\frac{\mathrm{y}}{\mathrm{D}}\right) = \mathrm{d}\left(\frac{\frac{\mathrm{d}}{2}}{\mathrm{D}}\right) = \frac{\mathrm{d}^{2}}{2\mathrm{D}}$
4. $\Delta\mathrm{x} = \frac{\mathrm{d}^{2}}{2(10\mathrm{d})} = \frac{\mathrm{d}}{20} = \frac{5\lambda}{20} = \frac{\lambda}{4}$
5. Path difference is
6. $\phi = \frac{2\pi}{\lambda} = (\Delta\mathrm{x}) = \frac{2\pi}{\lambda}\left(\frac{\lambda}{4}\right)$
7. $\phi = \frac{\pi}{2}$
8. So intensity at that pt is
9. $\mathrm{I} = \mathrm{I_{max}}\cos^{2}\left(\frac{\theta}{2}\right)$
10. $\mathrm{I} = \mathrm{I_0}\cos^{2}\left(\frac{\pi}{4}\right) = \frac{\mathrm{I_0}}{2}$

**Solved independently** (answer withheld)

1. The point in front of one slit is at $y = \frac{d}{2}$ from the central line.
2. Path difference $\Delta x = \frac{y d}{D} = \frac{(d/2)\,d}{10d} = \frac{d}{20}$.
3. With $d = 5\lambda$: $\Delta x = \frac{5\lambda}{20} = \frac{\lambda}{4}$.
4. Phase difference $\phi = \frac{2\pi}{\lambda}\cdot\frac{\lambda}{4} = \frac{\pi}{2}$.
5. $I = I_0 \cos^2\left(\frac{\phi}{2}\right) = I_0 \cos^2\left(\frac{\pi}{4}\right) = \frac{I_0}{2}$, which is option $4$.

**Subtopic:** Intensity Variation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q018_0dbd9eb4_28102026.png?v=0dbd9eb40e42)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q018_3ce36808_28102026.png?v=3ce3680829bc)

---

## Q19

Physics · Rotational Motion

A uniform circular disc of radius $50\,\mathrm{cm}$ at rest is free to tum about an axis which is perpendicular to its plane and passes through its centre. It is subjected to a torque which produces a constant angular acceleration of $2.0\,\mathrm{rad\,s^{-2}}$. Its net acceleration in $\mathrm{ms^{-2}}$ at the end of $2.0\,\mathrm{s}$ is approximately:

- **(1)** $8.0$
- (2) $7.0$
- (3) $6.0$
- (4) $3.0$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At the end of $2\,\mathrm{sec}$, $\mathrm{w} = \mathrm{w}_0 + \alpha t$
2. $\mathrm{w} = 0 + 2(2) = 4\,\mathrm{rad/sec}$
3. Particle acceleration towards the center is $= a_c = r\mathrm{w}^2$
4. $a_r = \frac{1}{2}(4)^2 = 8\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. Angular speed at $t = 2.0\,\mathrm{s}$: $\omega = \alpha t = 2.0 \times 2.0 = 4.0\,\mathrm{rad\,s^{-1}}$.
2. Tangential acceleration of a rim point: $a_t = r\alpha = 0.5 \times 2.0 = 1.0\,\mathrm{m\,s^{-2}}$.
3. Centripetal acceleration: $a_c = \omega^2 r = 4.0^2 \times 0.5 = 8.0\,\mathrm{m\,s^{-2}}$.
4. Net acceleration: $a = \sqrt{a_t^2 + a_c^2} = \sqrt{1^2 + 8^2} = \sqrt{65} \approx 8.06\,\mathrm{m\,s^{-2}}$.
5. $a \approx 8.0\,\mathrm{m\,s^{-2}}$, which is option $1$.

**Subtopic:** Tangential, Radial (Centripetal) and Net Acceleration in Non-Uniform Rotation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q019_204bdc9a_28102026.png?v=204bdc9a6321)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q019_2035d39d_28102026.png?v=2035d39dc9b9)

---

## Q20

Physics · Modern Physics

An electron of mass $m$ and a photon have same energy $E$. the ratio of de-Broglie wavelengths associated with them is: ($c$ being velocity of light)

- **(1)** $\frac{1}{c}\left(\frac{E}{2m}\right)^{\frac{1}{2}}$
- (2) $\left(\frac{E}{2m}\right)^{\frac{1}{2}}$
- (3) $c(2mE)^{\frac{1}{2}}$
- (4) $\frac{1}{c}\left(\frac{2m}{E}\right)^{\frac{1}{2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. De-Broglie wavelength is given by
2. $\lambda_e = \frac{h}{p} = \frac{h}{\sqrt{2m.E}}$ for electron
3. De-Broglie wavelength of photon is given by
4. $\lambda_p = \frac{h}{p} = \frac{h}{\frac{E}{c}} = \frac{hc}{E}$
5. $\frac{\lambda_e}{\lambda_p} = \frac{1}{\sqrt{2mE}}.\frac{E}{c} = \frac{1}{c}\sqrt{\frac{E}{2m}}$

**Solved independently** (answer withheld)

1. For the electron, $p_e = \sqrt{2mE}$, so $\lambda_e = \frac{h}{\sqrt{2mE}}$.
2. For the photon, $p_p = \frac{E}{c}$, so $\lambda_p = \frac{hc}{E}$.
3. $\frac{\lambda_e}{\lambda_p} = \frac{h}{\sqrt{2mE}} \cdot \frac{E}{hc} = \frac{E}{c\sqrt{2mE}}$.
4. $\frac{E}{c\sqrt{2mE}} = \frac{1}{c}\left(\frac{E}{2m}\right)^{1/2}$, which is option $1$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q020_78504577_28102026.png?v=78504577f040)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q020_20d8ebda_28102026.png?v=20d8ebda5612)

---

## Q21

Physics · Rotational Motion

A disk and a sphere of same radius but different masses roll off on two inclined planes of the same altitude and length. Which one of the two objects gets to the bottom of the plane first?

- (1) Disk
- **(2)** Sphere
- (3) Both reach at the same time
- (4) Depends on their masses

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Acceleration of the object on rough inclined plane is $a = \frac{g\sin\theta}{1+\frac{I}{mR^{2}}}$
2. For sphere $a_{1} = \frac{5g\sin\theta}{7}$
3. For disc $a_{2} = \frac{2g\sin\theta}{3}$
4. $a_{1} > a_{2}$, so sphere will reach bottom first.

**Solved independently** (answer withheld)

1. For rolling without slipping down an incline, $a = \frac{g\sin\theta}{1 + k^2/R^2}$, which is independent of mass and radius.
2. Disk: $k^2/R^2 = \frac{1}{2}$, so $a_{disk} = \frac{2}{3} g\sin\theta$.
3. Solid sphere: $k^2/R^2 = \frac{2}{5}$, so $a_{sphere} = \frac{5}{7} g\sin\theta$.
4. $\frac{5}{7} > \frac{2}{3}$, so $a_{sphere} > a_{disk}$.
5. Same length $L$ from rest: $t = \sqrt{\frac{2L}{a}}$, so the sphere takes less time and reaches first, which is option $2$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q021_0fded519_28102026.png?v=0fded5199b63)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q021_a901cdd9_28102026.png?v=a901cdd95063)

---

## Q22

Physics · Ray Optics

The angle of incidence for a ray of light at a refracting surface of a prism is $45^{\circ}$. The angle of prism is $60^{\circ}$. If the ray suffers minimum deviation through the prism, the angle of minimum deviation and refractive index of the material of the prism respectively, are:

- (1) $45^{\circ};\frac{1}{\sqrt{2}}$
- **(2)** $30^{\circ};\ \sqrt{2}$
- (3) $45^{\circ};\sqrt{2}$
- (4) $30^{\circ};\frac{1}{\sqrt{2}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. At minimum deviation $\delta_{min} = 2i - A$
2. $\delta_{min} = 2(45) - 60$
3. $\delta_{min} = 30^{o}$
4. Refractive index of material is
5. $\mu = \frac{\sin\left(\frac{\delta_{min} + A}{2}\right)}{\sin\left(\frac{A}{2}\right)} = \frac{\sin\left(\frac{30 + 60}{2}\right)}{\sin(30^{o})}$
6. $\mu = \frac{\sin 45^{o}}{\sin 30^{o}} = \frac{\frac{1}{\sqrt{2}}}{\frac{1}{2}} = \sqrt{2}$

**Solved independently** (answer withheld)

1. At minimum deviation the ray passes symmetrically, so $i = e = 45^{\circ}$.
2. $A + \delta_m = i + e = 2i \Rightarrow \delta_m = 2(45^{\circ}) - 60^{\circ} = 30^{\circ}$.
3. Inside the prism $r_1 = r_2 = \frac{A}{2} = 30^{\circ}$.
4. $n = \frac{\sin i}{\sin r} = \frac{\sin 45^{\circ}}{\sin 30^{\circ}} = \frac{1/\sqrt{2}}{1/2} = \sqrt{2}$.
5. $\delta_m = 30^{\circ}$, $n = \sqrt{2}$, which is option $2$.

**Subtopic:** Prism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q022_9ed1c5b6_28102026.png?v=9ed1c5b68b14)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q022_935634c3_28102026.png?v=935634c3b2c0)

---

## Q23

Physics · Modern Physics

When an $\alpha$-particle of mass ‘m’ moving with velocity ‘v’ bombards on a heavy nucleus of charge ‘Ze’, its distance of closest approach from the nucleus depends on m as:

- **(1)** $\frac{1}{\mathrm{m}}$
- (2) $\frac{1}{\sqrt{\mathrm{m}}}$
- (3) $\frac{1}{\mathrm{m}^2}$
- (4) $m$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At the distance of lowest approach, total K.E. of $\alpha$-particle changes to P.E. so
2. $\frac{1}{2}\mathrm{mv}^{2} = \frac{\mathrm{KQ.q}}{\mathrm{r}} = \frac{\mathrm{K(ze)(2e)}}{\mathrm{r}}$
3. $\mathrm{r} = \frac{4\mathrm{K\,ze}^{2}}{\mathrm{mv}^{2}} \Rightarrow \mathrm{r} \propto \frac{1}{\mathrm{m}}$
4. $\mathrm{r} \propto \frac{1}{\mathrm{m}}$

**Solved independently** (answer withheld)

1. At the distance of closest approach the $\alpha$-particle momentarily stops, so all its kinetic energy becomes electrostatic potential energy.
2. $\frac{1}{2}mv^2 = \frac{1}{4\pi\varepsilon_0}\frac{(2e)(Ze)}{r_0}$.
3. $r_0 = \frac{4Ze^2}{4\pi\varepsilon_0\, m v^2}$.
4. With $v$ and $Z$ fixed, $r_0 \propto \frac{1}{m}$, which is option $1$.

**Subtopic:** Distance of Closest Approach and Size of Nucleus · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q023_83e5b864_28102026.png?v=83e5b864b6fe)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q023_b76385ad_28102026.png?v=b76385ad0572)

---

## Q24

Physics · Kinematics

A particle of mass $10\,\mathrm{g}$ moves along a circle of radius $6.4\,\mathrm{cm}$ with a constant tangential acceleration. What is the magnitude of this acceleration if the kinetic energy of the particle becomes equal to $8 \times 10^{-4}\,\mathrm{J}$ by the end of the second revolution after the beginning of the motion?

- **(1)** $0.1\,\mathrm{m/s^2}$
- (2) $0.15\,\mathrm{m/s^2}$
- (3) $0.18\,\mathrm{m/s^2}$
- (4) $\frac{0.2\mathrm{m}}{\mathrm{s^2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Tangential acceleration $a_t = r\alpha = \text{constant} = K$
2. $\alpha = \frac{K}{r}$
3. At the end of second revoluation angular velocity is $w$ then
4. $w^2 - w_0^2 = 2 \propto \theta$
5. $w^2 - 0^2 = 2\left(\frac{K}{r}\right)(4\pi)$
6. $w^2 = \frac{8\pi K}{r}$
7. K.E. of the particle is $= \mathrm{K.E.} = \frac{1}{2}mv^2$
8. $\mathrm{K.E.} = \frac{1}{2}mr^2w^2$
9. $\mathrm{K.E.} = \frac{1}{2}m(r^2)\left(\frac{8\pi K}{r}\right)$
10. $8 \times 10^{-4} = \frac{1}{2} \times 10 \times 10^{-3} \times 6.4 \times 10^{-2} \times 3.14 \times K$
11. $K = \frac{2}{6.4 \times 3.14} = 0.1\,\frac{m}{ssec^2}$

**Solved independently** (answer withheld)

1. The particle starts from rest, so after a path length $s$ with constant tangential acceleration $a_t$: $v^2 = 2 a_t s$.
2. Distance covered in two revolutions: $s = 2 \times 2\pi r = 4\pi \times 0.064\,\mathrm{m} \approx 0.804\,\mathrm{m}$.
3. Kinetic energy: $K = \frac{1}{2} m v^2 = \frac{1}{2} m (2 a_t s) = m a_t s$.
4. $a_t = \frac{K}{m s} = \frac{8 \times 10^{-4}}{0.01 \times 0.804} \approx 0.0995\,\mathrm{m/s^2} \approx 0.1\,\mathrm{m/s^2}$, which is option $1$.

**Subtopic:** Non-Uniform Circular Motion · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 16)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q024_fb5e408b_28102026.png?v=fb5e408b2a01)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q024_1dfb2f49_28102026.png?v=1dfb2f491d3d)

---

## Q25

Physics · Kinetic Theory of Gases

The molecules of a given mass of a gas have r.m.s velocity of $200\,\mathrm{ms^{-1}}$ at $27^{\circ}\mathrm{C}$ and $1.0 \times 10^{5}\,\mathrm{Nm^{-2}}$ pressure. When the temperature and pressure of the gas are respectively, $127^{\circ}\mathrm{C}$ and $0.05 \times 10^{5}\,\mathrm{Nm^{-2}}$, the r.m.s. velocity of its molecules in $\mathrm{ms^{-1}}$ is:

- (1) $100\sqrt{2}$
- **(2)** $\frac{400}{\sqrt{3}}$
- (3) $\frac{100\sqrt{2}}{3}$
- (4) $\frac{100}{3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rms speed of molecules is $\mathrm{V_{ms}} = \sqrt{\frac{3\mathrm{RT}}{\mathrm{M}}}$
2. So it depends only on temperature
3. $\mathrm{V_{rms}} \propto \sqrt{\mathrm{T}}$
4. $\frac{\mathrm{V_1}}{\mathrm{V_2}} = \sqrt{\frac{\mathrm{T_1}}{\mathrm{T_2}}} \Rightarrow \frac{200}{\mathrm{V_2}} = \sqrt{\frac{300}{400}}$
5. $\frac{200}{\mathrm{V_2}} = \frac{\sqrt{3}}{2} \Rightarrow \mathrm{V_2} = \frac{400}{\sqrt{3}}\,\mathrm{m/sec}$

**Solved independently** (answer withheld)

1. $v_{rms} = \sqrt{\frac{3RT}{M}}$, so for a fixed gas $v_{rms} \propto \sqrt{T}$ and pressure does not matter.
2. $T_1 = 27 + 273 = 300\,\mathrm{K}$, $T_2 = 127 + 273 = 400\,\mathrm{K}$.
3. $\frac{v_2}{v_1} = \sqrt{\frac{400}{300}} = \frac{2}{\sqrt{3}}$.
4. $v_2 = 200 \times \frac{2}{\sqrt{3}} = \frac{400}{\sqrt{3}}\,\mathrm{ms^{-1}}$, which is option $2$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q025_232500ab_28102026.png?v=232500ab3be6)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q025_5d032c4d_28102026.png?v=5d032c4da626)

---

## Q26

Physics · Magnetic Effect of Electric Current

A long straight wire of radius $a$ carries a steady current $I$. the current is uniformly distributed over its cross-section. The ratio of the magnetic fields $B$ and $B'$, at radial distances $\frac{a}{2}$ and $2a$ respectively, from the axis of the wire is:

- (1) $\frac{1}{4}$
- (2) $\frac{1}{2}$
- **(3)** $1$
- (4) $4$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Inside the wire
2. By ampere's law
3. $\int \vec{B}.\vec{dl} = \mu_0(i_{\mathrm{enclosed}})$
4. $\int B.\,dl\cos 0 = \mu_0\left(\frac{I}{\pi a^2}.\,\pi\left(\frac{a}{2}\right)^2\right)$
5. $B\int dl = \mu_0\frac{I}{4}$
6. $B\left(2\pi\left(\frac{a}{2}\right)\right) = \frac{\mu_0 I}{4}$
7. $B = \frac{\mu_0 I}{4\pi a}$
8. Outside the wire,
9. $B' = \frac{\mu_0 I}{2\pi r} = \frac{\mu_0 I}{2\pi(2a)} = \frac{\mu_0 I}{4\pi a}$
10. So, $\frac{B}{B'} = 1$.

**Solved independently** (answer withheld)

1. Inside the wire ($r<a$), Ampere's law with enclosed current $I\frac{r^2}{a^2}$ gives $B = \frac{\mu_0 I r}{2\pi a^2}$.
2. At $r=\frac{a}{2}$: $B = \frac{\mu_0 I (a/2)}{2\pi a^2} = \frac{\mu_0 I}{4\pi a}$.
3. Outside the wire ($r>a$): $B' = \frac{\mu_0 I}{2\pi r}$, so at $r=2a$: $B' = \frac{\mu_0 I}{4\pi a}$.
4. $\frac{B}{B'} = 1$, which is option $3$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q026_09cd6c51_28102026.png?v=09cd6c51e808)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q026_c1fd7cd2_28102026.png?v=c1fd7cd21db3)

---

## Q27

Physics · Kinematics

A particle moves so that its position vector is given by $\vec{r} = \cos \omega t\,\hat{x} + \sin \omega t\,\hat{y}$. Where $\omega$ is a constant. Which of the following is true?

- (1) Velocity and acceleration both are perpendicular to $\vec{r}$.
- (2) Velocity and acceleration both are parallel to $\vec{r}$.
- **(3)** Velocity is perpendicular to $\vec{r}$ and acceleration is directed towards the origin.
- (4) Velocity is perpendicular to $\vec{r}$ and acceleration is directed away from the origin.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Position vector is $\vec{r} = \cos \omega + \hat{x} + \sin \omega + \hat{y}$
2. Velocity of particle is $\vec{v} = \frac{d\vec{r}}{dt}$
3. $\vec{v} = \sin \omega t.\,\omega\,\hat{x} + \cos \omega t\,.\,\omega\hat{y}$
4. $\vec{v} = \omega(-\sin \omega t\hat{x} + \cos \omega t\hat{y})$
5. Acceleration of the particle is
6. $\vec{a} = \frac{d\vec{v}}{dt}$
7. $\vec{a} = -\omega^{2}(\cos \omega t\,\hat{x} + \sin \omega t\hat{y})$
8. $\vec{a} = -\omega^{2}\vec{r},$
9. So direction of $\vec{r}$ and $\vec{a}$ are opposite.
10. $\vec{v}.\vec{a} = 0 \Rightarrow \vec{v} \perp \vec{a}$
11. $\vec{v}.\vec{r} = 0 \Rightarrow \vec{v} \perp \vec{r}$
12. So, ans is (Velocity is perpendicular to $\vec{r}$ and acceleration is directed towards the origin.)

**Solved independently** (answer withheld)

1. $\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t\,\hat{x} + \omega \cos \omega t\,\hat{y}$.
2. $\vec{v} \cdot \vec{r} = -\omega \sin \omega t \cos \omega t + \omega \sin \omega t \cos \omega t = 0$, so $\vec{v} \perp \vec{r}$.
3. $\vec{a} = \frac{d\vec{v}}{dt} = -\omega^2 (\cos \omega t\,\hat{x} + \sin \omega t\,\hat{y}) = -\omega^2 \vec{r}$.
4. $\vec{a}$ is antiparallel to $\vec{r}$, i.e. directed towards the origin, which is option $3$.

**Subtopic:** Uniform Circular Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q027_8024dabe_28102026.png?v=8024dabe7a79)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q027_8b785a86_28102026.png?v=8b785a865b54)

---

## Q28

Physics · Work, Energy and Power

What is the minimum velocity with which a body of mass $m$ must enter a vertical loop of radius $R$ so that it can complete the loop?

- (1) $\sqrt{gR}$
- (2) $\sqrt{2gR}$
- (3) $\sqrt{3gR}$
- **(4)** $\sqrt{5gR}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Minimum velocity required is $v = \sqrt{5gR}$

**Solved independently** (answer withheld)

1. At the top of the loop the minimum condition is that gravity alone provides the centripetal force: $mg = \frac{m v_t^2}{R}$.
2. So $v_t^2 = gR$.
3. Energy conservation from the bottom to the top (rise of $2R$): $\frac{1}{2} m v_b^2 = \frac{1}{2} m v_t^2 + mg(2R)$.
4. $v_b^2 = gR + 4gR = 5gR$.
5. $v_b = \sqrt{5gR}$, which is option $4$.

**Subtopic:** Motion in a Vertical Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q028_37be85bd_28102026.png?v=37be85bdd931)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q028_f6c147ec_28102026.png?v=f6c147ec926d)

---

## Q29

Physics · Modern Physics

When a metallic surface is illuminated with radiation of wavelength $\lambda$, the stopping potential is $V$. If the same surface is illuminated with radiation of wavelength $2\lambda$, the stopping potential is $\frac{V}{4}$. The threshold wavelength for the metallic surface is:

- (1) $4\lambda$
- (2) $5\lambda$
- (3) $\frac{5}{2}\lambda$
- **(4)** $3\lambda$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In photo electric effects
2. $\mathrm{e}V_0 = 48 - W$
3. $\mathrm{e}V_0 = \frac{hc}{\lambda} - W$
4. $\mathrm{e}V = \frac{hc}{\lambda} - W \quad \ldots(\mathrm{i})$
5. $\mathrm{e}\frac{V}{4} = \frac{hc}{2\lambda} - W \quad \ldots.(\mathrm{ii})$
6. From (i) and (ii)
7. $\frac{hc}{\lambda} - W = 4\left(\frac{hc}{2\lambda} - W\right)$
8. $\frac{hc}{\lambda} - W = \frac{2hc}{\lambda} - 4W$
9. $3W = \frac{hc}{\lambda} \Rightarrow W = \frac{hc}{3\lambda}$
10. $\frac{hc}{\lambda_{\mathrm{max}}} = \frac{hc}{3\lambda} \Rightarrow \lambda_{\mathrm{max}} =$ threshold wavelength $3\lambda$

**Solved independently** (answer withheld)

1. Einstein's equation for wavelength $\lambda$: $\frac{hc}{\lambda} - \phi = eV$.
2. For wavelength $2\lambda$: $\frac{hc}{2\lambda} - \phi = \frac{eV}{4}$.
3. Subtracting the second from the first: $\frac{hc}{2\lambda} = \frac{3eV}{4}$, so $eV = \frac{2hc}{3\lambda}$.
4. Then $\phi = \frac{hc}{\lambda} - \frac{2hc}{3\lambda} = \frac{hc}{3\lambda}$.
5. Since $\phi = \frac{hc}{\lambda_0}$, $\lambda_0 = 3\lambda$, which is option $4$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q029_4861ed20_28102026.png?v=4861ed20a6ef)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q029_9807fca9_28102026.png?v=9807fca9737e)

---

## Q30

Physics · Thermodynamics

A gas is compressed isothermally to half its initial volume. The same gas is compressed separately through an adiabatic process until its volume is again reduced to half. Then:

- (1) Compressing the gas isothermally will require more work to be done.
- **(2)** Compressing the gas through adiabatic process will require more work to be done.
- (3) Compressing the gas isothermally or adiabatically will require the same amount of work.
- (4) Which of the case (whether compression through isothermal or through adiabatic process) requires more work will depend upon the atomicity of the gas.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: P-v graph: adiabatic and isothermal compressions from v to v/2](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q030_sol_1_d0a9d591_28102026.png?v=d0a9d5918d37)

*P-v graph: adiabatic and isothermal compressions from v to v/2*

1. Isothermal curve lie below the adiabatic curve, So in adiabatic process more work to be done.

**Solved independently** (answer withheld)

1. Isothermal compression from $V$ to $V/2$: $W_{iso} = nRT\ln\frac{V_i}{V_f} = nRT\ln 2 \approx 0.693\,nRT$.
2. Adiabatic compression from $V$ to $V/2$: $T_f = T\,2^{\gamma-1}$, so $W_{adi} = \frac{nR(T_f - T)}{\gamma-1} = nRT\,\frac{2^{\gamma-1}-1}{\gamma-1}$.
3. Let $x = \gamma - 1 > 0$; since $e^{x\ln 2} - 1 > x\ln 2$, we get $\frac{2^{x}-1}{x} > \ln 2$, so $W_{adi} > W_{iso}$ for every $\gamma > 1$ (e.g. $\gamma = 1.4$: $0.799\,nRT > 0.693\,nRT$).
4. Hence adiabatic compression requires more work, independent of atomicity, which is option $2$.

**Subtopic:** Adiabatic Process, Isothermal Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q030_44e3a9ea_28102026.png?v=44e3a9ea3a19)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q030_675fb095_28102026.png?v=675fb095a293)

---

## Q31

Physics · Current Electricity

A potentiometer wire is $100\,\mathrm{cm}$ long and a constant potential difference is maintained across it. Two cells are connected in series first to support one another and then in opposite direction. The balance points are obtained at $50\,\mathrm{cm}$ and $10\,\mathrm{cm}$ from the positive end of the wire in the two cases. The ratio of emf’s is :

- (1) $5 : 1$
- (2) $5 : 4$
- (3) $3 : 4$
- **(4)** $3 : 2$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Potentiometer wire of length 100 cm drawn as a long thin bar](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q031_sol_1_9f0cf03d_28102026.png?v=9f0cf03d7b8a)

*Potentiometer wire of length 100 cm drawn as a long thin bar*

1. $\frac{E_1 + E_2 = \lambda 50}{E_1 - E_2 = \lambda 10}$
2. $E_1 + E_2 = 5E_1 - 5E_2$
3. $6E_2 = 4E_1$
4. $\frac{3}{2} = \frac{E_1}{E_2}$

**Solved independently** (answer withheld)

1. Cells supporting each other: $E_1 + E_2 = k\,l_1 = 50k$.
2. Cells opposing each other: $E_1 - E_2 = k\,l_2 = 10k$.
3. Adding: $2E_1 = 60k \Rightarrow E_1 = 30k$; subtracting: $2E_2 = 40k \Rightarrow E_2 = 20k$.
4. $\frac{E_1}{E_2} = \frac{30k}{20k} = \frac{3}{2}$, which is option $4$.

**Subtopic:** Potentiometer · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q031_0d807c30_28102026.png?v=0d807c30690c)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q031_f19bed32_28102026.png?v=f19bed32be52)

---

## Q32

Physics · Ray Optics

A astronomical telescope has objective and eyepiece of focal lengths $40\,\mathrm{cm}$ and $4\,\mathrm{cm}$ respectively. To view an object $200\,\mathrm{cm}$ away from the objective, the lenses must be separated by a distance:

- (1) $37.3\,\mathrm{cm}$
- (2) $46.0\,\mathrm{cm}$
- (3) $50.0\,\mathrm{cm}$
- **(4)** $54.0\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\frac{1}{V} - \frac{1}{-200} = \frac{1}{40}$
2. $\frac{1}{V} = \frac{5}{5}\frac{1}{40} - \frac{1}{200}$
3. $= \frac{5}{200} - \frac{1}{200}$

![printed figure: Objective (f0 = 40) and eyepiece (fe = 4 cm) on a common axis, object OC 200 cm from the objective, separations 50 and 4](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q032_sol_1_649ffb19_28102026.png?v=649ffb197b8f)

*Objective (f0 = 40) and eyepiece (fe = 4 cm) on a common axis, object OC 200 cm from the objective, separations 50 and 4*

4. $\frac{1}{V} = \frac{4}{200} = \frac{1}{50}$
5. $V = 50$
6. $\therefore d = 50 + 4 = 54\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Lens formula for the objective with $u = -200\,\mathrm{cm}$, $f_o = 40\,\mathrm{cm}$: $\frac{1}{v} - \frac{1}{u} = \frac{1}{f_o}$.
2. $\frac{1}{v} = \frac{1}{40} - \frac{1}{200} = \frac{5 - 1}{200} = \frac{4}{200}$, so $v = 50\,\mathrm{cm}$.
3. In normal adjustment the intermediate image lies at the focus of the eyepiece, so $L = v + f_e$.
4. $L = 50\,\mathrm{cm} + 4\,\mathrm{cm} = 54\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Telescope · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q032_cc4aeef5_28102026.png?v=cc4aeef5214f)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q032_9dc93d6b_28102026.png?v=9dc93d6b6aa4)

---

## Q33

Physics · Mechanical Properties of Fluids

Two non-mixing liquids of densities $\rho$ and $n\rho(n > 1)$ are put in a container. The height of each liquid is $h$. A solid cylinder of length $L$ and density $d$ is put in this container. The cylinder floats with its axis vertical and length $pL(p < 1)$ in the denser liquid. The density $d$ is equal to:

- (1) $\{1 + (n + 1)p\}\rho$
- (2) $\{2 + (n + 1)p\}\rho$
- (3) $\{2 + (n - 1)p\}\rho$
- **(4)** $\{1 + (n - 1)p\}\rho$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Cylinder floating across the interface of two liquid layers of height h each](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q033_sol_1_695aaa47_28102026.png?v=695aaa47a134)

*Cylinder floating across the interface of two liquid layers of height h each*

1. $f_0 = mg$
2. $PA(1 - P)Lg + n\rho ApLg = dALg$
3. $\rho(1 - p) + n\rho p = d$
4. $[1 - p + np]\rho = d$
5. $[1 + (n - 1)p]\rho = d$

**Solved independently** (answer withheld)

1. The cylinder floats, so its weight equals the total buoyant force from both liquids: $LAdg = F_{B}$.
2. Length $pL$ is in the denser liquid and the remaining $(1-p)L$ is in the lighter liquid above it: $F_B = (pL)A(n\rho)g + (1-p)LA\rho g$.
3. Cancel $LAg$: $d = np\rho + (1-p)\rho$.
4. $d = \{1 + (n-1)p\}\rho$, which is option $4$.

**Subtopic:** Archimedes' Principle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q033_4c1db739_28102026.png?v=4c1db7396ccc)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q033_7cad1238_28102026.png?v=7cad123836aa)

---

## Q34

Physics · Semiconductor Electronics

To get output 1 for the following circuit, the correct choice for the input is:

![printed figure: Inputs A and B into an OR gate, whose output and input C feed an AND gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q034_b65fb9dd_28102026.png?v=b65fb9dd7158)

*Inputs A and B into an OR gate, whose output and input C feed an AND gate giving output Y*

- (1) $\mathrm{A} = 0, \mathrm{B} = 1, \mathrm{C} = 0$
- (2) $\mathrm{A} = 1, \mathrm{B} = 0, \mathrm{C} = 0$
- (3) $\mathrm{A} = 1, \mathrm{B} = 1, \mathrm{C} = 0$
- **(4)** $\mathrm{A} = 1, \mathrm{B} = 0, \mathrm{C} = 1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: A OR B feeds an AND gate with C; inputs A=1, B=0, C=1 give output 1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q034_sol_1_76fe3bd8_28102026.png?v=76fe3bd81b04)

*A OR B feeds an AND gate with C; inputs A=1, B=0, C=1 give output 1*


**Solved independently** (answer withheld)

1. A and B enter an OR gate: its output is $A + B$.
2. That output and $C$ enter an AND gate: $Y = (A + B)\cdot C$.
3. Options 1, 2 and 3 have $C = 0$, so $Y = 0$ for each.
4. Option 4: $Y = (1 + 0)\cdot 1 = 1$, which is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q034_e893a7b4_28102026.png?v=e893a7b4d04c)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q034_81f361d3_28102026.png?v=81f361d37be5)

---

## Q35

Physics · Thermal Properties of Matter

A piece of ice falls from a height $h$ so that it melts completely. Only one-quarter of the heat produced is absorbed by the ice and all energy of ice gets converted into heat during its fall. The value of $h$ is: [Latent heat of ice is $3.4 \times 1^{5}\,\mathrm{J/kg}$ and $g = 10\,\mathrm{N/kg}$]

- (1) $34\,\mathrm{km}$
- (2) $544\,\mathrm{km}$
- **(3)** $136\,\mathrm{km}$
- (4) $68\,\mathrm{km}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\frac{1}{4}\mathrm{mgh} = \mathrm{mL}$
2. $\mathrm{h} = \frac{4\mathrm{L}}{\mathrm{g}} = \frac{4 \times 3.4 \times 10^{5}}{10} = 13.6 \times 10^{4}$
3. $= 136 \times 10^{3}\,\mathrm{km}$
4. $= 136\,\mathrm{km}$

**Solved independently** (answer withheld)

1. Heat produced equals the loss of potential energy, $mgh$; only $\frac{1}{4}$ of it is absorbed by the ice.
2. For complete melting: $\frac{1}{4} mgh = mL$.
3. $h = \frac{4L}{g} = \frac{4 \times 3.4 \times 10^{5}}{10}\,\mathrm{m}$.
4. $h = 1.36 \times 10^{5}\,\mathrm{m} = 136\,\mathrm{km}$, which is option $3$.

**Subtopic:** Mechanical Equivalent of Heat · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q035_9fd911a8_28102026.png?v=9fd911a86cf1)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q035_07ed4407_28102026.png?v=07ed44071062)

---

## Q36

Physics · Gravitation

The ratio of escape velocity at earth $(\upsilon_{\mathrm{e}})$ to the escape velocity at a planet $(\upsilon_{\mathrm{p}})$ whose radius and mean density are twice as that of earth is:

- (1) $1 : 2$
- **(2)** $1 : 2\sqrt{2}$
- (3) $1 : 4$
- (4) $1 : \sqrt{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\frac{\mathrm{V_e}}{\mathrm{V_P}} = \frac{\sqrt{2\frac{\mathrm{GM_e}}{\mathrm{R_e}}}}{\sqrt{2\frac{\mathrm{GM_P}}{\mathrm{R_P}}}} = \sqrt{\frac{\mathrm{M_R}}{\mathrm{M_P}}\frac{\mathrm{R_P}}{\mathrm{R_e}}} = \sqrt{\frac{\mathrm{P_e}\frac{4}{3}\pi \mathrm{R_e^3}\mathrm{R_P}}{\mathrm{P_P}\frac{4}{3}\pi \mathrm{R_P^3}\mathrm{R_e}}}$
2. $\frac{\mathrm{V_e}}{\mathrm{V_P}} = \sqrt{\frac{\mathrm{P_e}\mathrm{R_e^2}}{\mathrm{P_P}\mathrm{R_P^2}}} = \sqrt{\frac{1}{2\ 2^{2}}} = \frac{1}{2\sqrt{2}}$

**Solved independently** (answer withheld)

1. $v = \sqrt{\frac{2GM}{R}}$ with $M = \frac{4}{3}\pi R^3 \rho$.
2. $v = \sqrt{\frac{8\pi G \rho R^2}{3}} = R\sqrt{\frac{8\pi G\rho}{3}}$, so $v \propto R\sqrt{\rho}$.
3. $\frac{v_p}{v_e} = \frac{2R}{R}\sqrt{\frac{2\rho}{\rho}} = 2\sqrt{2}$.
4. $v_e : v_p = 1 : 2\sqrt{2}$, which is option $2$.

**Subtopic:** Escape Velocity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q036_92cb305f_28102026.png?v=92cb305f7ff8)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q036_a1b59b2a_28102026.png?v=a1b59b2a707a)

---

## Q37

Physics · Kinematics

If the magnitude of sum of two vectors is equal to the magnitude of difference of the two vectors, the angle between these vectors is:

- (1) $0^{o}$
- **(2)** $90^{o}$
- (3) $45^{o}$
- (4) $180^{o}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $|\vec{A} + \vec{B}| = |\vec{A} - \vec{B}|$
2. $A^{2} + B^{2} + 2AB\cos\theta = A^{2} + B^{2} = 2AB\cos\theta$
3. $4AB\cos\theta = 0$
4. $\cos\theta = 0$
5. $\theta = 90^{o}$

**Solved independently** (answer withheld)

1. $|\vec{A}+\vec{B}|^2 = A^2 + B^2 + 2AB\cos\theta$.
2. $|\vec{A}-\vec{B}|^2 = A^2 + B^2 - 2AB\cos\theta$.
3. Setting them equal gives $4AB\cos\theta = 0$, so $\cos\theta = 0$.
4. $\theta = 90^{o}$, which is option $2$.

**Subtopic:** Addition of Vectors, Subtraction of Vectors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q037_e74617f8_28102026.png?v=e74617f8f08c)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q037_d6c09d10_28102026.png?v=d6c09d108200)

---

## Q38

Physics · Modern Physics

Given the value of Rydberg constant is $10^{7}\,\mathrm{m^{-1}}$, the wave number of the last line of the Balmer series in hydrogen spectrum will be:

- (1) $0.025 \times 10^{4}\,\mathrm{m^{-1}}$
- (2) $0.5 \times 10^{7}\,\mathrm{m^{-1}}$
- **(3)** $0.25 \times 10^{7}\,\mathrm{m^{-1}}$
- (4) $2.5 \times 10^{7}\,\mathrm{m^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\frac{1}{\lambda} = \mathrm{R} = \left(\frac{1}{\mathrm{h}_{1}^{2}} - \frac{1}{\mathrm{h}_{2}^{2}}\right)$
2. Wavelength $= \frac{1}{\lambda} = \mathrm{R}\left[\frac{1}{2^{2}}\right] = \frac{\mathrm{R}}{4} = \frac{10^{7}}{4} = 0.25 \times 10^{7}\,\mathrm{m^{-1}}$

**Solved independently** (answer withheld)

1. The last line of the Balmer series is the series limit, the transition $n_2 = \infty \to n_1 = 2$.
2. $\bar{\nu} = R\left(\frac{1}{2^2} - \frac{1}{\infty^2}\right) = \frac{R}{4}$.
3. $\bar{\nu} = \frac{10^{7}}{4}\,\mathrm{m^{-1}} = 0.25 \times 10^{7}\,\mathrm{m^{-1}}$, which is option $3$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q038_72db01cc_28102026.png?v=72db01ccb206)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q038_c0b01370_28102026.png?v=c0b013708c16)

---

## Q39

Physics · Work, Energy and Power

A body of mass $1\,\mathrm{kg}$ begins to move under the action of a time dependent force $\vec{F} = (2t\,\hat{i} + 3t^{2}\,\hat{j})\,\mathrm{N}$, where $\hat{i}$ and $\hat{j}$ are unit vectors along x and y axis. What power will be developed by the force at the time t?

- (1) $(2t^{2} + 3t^{3})\,\mathrm{W}$
- (2) $(2t^{2} + 4t^{4})\,\mathrm{W}$
- (3) $(2t^{3} + 3t^{4})\,\mathrm{W}$
- **(4)** $(2t^{3} + 3t^{5})\,\mathrm{W}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\vec{a} = 2t\hat{i} + 3t^{2}\hat{j}$
2. $\vec{V} = 2t^{2}\hat{i} + \frac{3}{3}t^{3}\hat{j}$
3. $\vec{F} = 2t\hat{i} + 3t^{2}\hat{j}$
4. $P = \vec{F}.\vec{V} = 2t^{3} + 3t^{5}$

**Solved independently** (answer withheld)

1. With $m = 1\,\mathrm{kg}$, $\vec{a} = \vec{F}/m = 2t\,\hat{i} + 3t^{2}\,\hat{j}$.
2. The body starts from rest, so $\vec{v} = \int_0^t \vec{a}\,dt = t^{2}\,\hat{i} + t^{3}\,\hat{j}$.
3. $P = \vec{F}\cdot\vec{v} = (2t)(t^{2}) + (3t^{2})(t^{3})$.
4. $P = (2t^{3} + 3t^{5})\,\mathrm{W}$, which is option $4$.

**Subtopic:** Power · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q039_da1d12d0_28102026.png?v=da1d12d0d976)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q039_ceb77ae1_28102026.png?v=ceb77ae18782)

---

## Q40

Physics · Alternating Current

An inductor $20\,\mathrm{mH}$, a capacitor $50\,\mu\mathrm{F}$ and a resistor $40\,\Omega$ are connected in series across a source of emf $V = 10 \sin 340\, t$. The power loss in A.C. circuit is :

- **(1)** $0.51\,\mathrm{W}$
- (2) $0.67\,\mathrm{W}$
- (3) $0.76\,\mathrm{W}$
- (4) $0.89\,\mathrm{W}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{wL} = 340 \times 20 \times 10^{-3} = 68 \times 10^{-1} = 6.8$
2. $\frac{1}{\mathrm{wC}} = \frac{1}{340 \times 50 \times 10^{-6}} = \frac{10^{4}}{34 \times 5} = \frac{2}{34} \times 10^{3}$
3. $= 0.0588 \times 10^{3} = 58.82$
4. $2 = \sqrt{\left(\mathrm{wL} - \frac{1}{\mathrm{wc}}\right)^{2} + \mathrm{R}^{2}}$
5. $2 = \sqrt{2704 + 1600} \approx 65.6$
6. $\mathrm{i} = \frac{\mathrm{V}}{2}, \frac{10}{65 \times \sqrt{2}} = \frac{10}{65.6\sqrt{2}}$
7. Power $= \frac{100 \times 40}{(65.6)^{2} \times 2} = \frac{2000}{(65.6)^{2}}$
8. $= 0.51\,\mathrm{w}$

**Solved independently** (answer withheld)

1. From $V = 10\sin 340t$: $V_0 = 10\,\mathrm{V}$, $\omega = 340\,\mathrm{rad\,s^{-1}}$.
2. $X_L = \omega L = 340 \times 20\times10^{-3} = 6.8\,\Omega$.
3. $X_C = \frac{1}{\omega C} = \frac{1}{340 \times 50\times10^{-6}} = 58.82\,\Omega$.
4. $X_C - X_L = 58.82 - 6.8 = 52.02\,\Omega$.
5. $Z^2 = R^2 + (X_C - X_L)^2 = 1600 + 2706 = 4306\,\Omega^2$, so $Z \approx 65.6\,\Omega$.
6. $V_{rms}^2 = \frac{V_0^2}{2} = 50\,\mathrm{V^2}$.
7. $P = \frac{V_{rms}^2 R}{Z^2} = \frac{50 \times 40}{4306} \approx 0.46\,\mathrm{W}$.
8. No option equals $0.46\,\mathrm{W}$; the nearest is $0.51\,\mathrm{W}$, option $1$.

**Subtopic:** Power in an AC Circuit · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 25)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q040_7e073920_28102026.png?v=7e0739200fb4)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q040_ccd3b916_28102026.png?v=ccd3b9169d29)

---

## Q41

Physics · Kinematics

If the velocity of a particle is $\upsilon = \mathrm{A}t + \mathrm{B}t^{2}$, where A and B are constants, then the distance travelled by it between $1\,\mathrm{s}$ and $2\,\mathrm{s}$ is:

- (1) $\frac{3}{2}\mathrm{A} + 4\mathrm{B}$
- (2) $3\mathrm{A} + 7\mathrm{B}$
- **(3)** $\frac{3}{2}\mathrm{A} + \frac{7}{3}\mathrm{B}$
- (4) $\frac{\mathrm{A}}{2} + \frac{\mathrm{B}}{3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{V} = \mathrm{A}t + \mathrm{B}t^{2}$
2. $\mathrm{X} = \frac{\mathrm{A}t^{2}}{2} + \frac{\mathrm{B}t^{3}}{3}$
3. $t = 1$
4. $\mathrm{X}_{1} = \frac{\mathrm{A}}{2} + \frac{\mathrm{B}}{3}$
5. $t = 2$
6. $\mathrm{X}_{2} = 2\mathrm{A} + \frac{8\mathrm{B}}{3}$
7. $\mathrm{X}_{2} - \mathrm{X}_{1} = \frac{3\mathrm{A}}{2} + \frac{7\mathrm{B}}{3}$

**Solved independently** (answer withheld)

1. Distance travelled is $s = \int_{1}^{2} \upsilon\,dt = \int_{1}^{2} (At + Bt^{2})\,dt$ (velocity taken as not changing sign in the interval).
2. $s = \left[\frac{At^{2}}{2} + \frac{Bt^{3}}{3}\right]_{1}^{2}$.
3. $s = \frac{A(4-1)}{2} + \frac{B(8-1)}{3} = \frac{3}{2}A + \frac{7}{3}B$, which is option $3$.

**Subtopic:** Distance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q041_ef0f9b1e_28102026.png?v=ef0f9b1e418b)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q041_4f1521ce_28102026.png?v=4f1521ce39a5)

---

## Q42

Physics · Electromagnetic Induction

A long solenoid has 1000 turns. When a current of $4\,\mathrm{A}$ flows through it the magnetic flux linked with each turn of the solenoid is $4 \times 10^{-3}\,\mathrm{Wb}$. The self-inductance of the solenoid is:

- (1) $4\,\mathrm{H}$
- (2) $3\,\mathrm{H}$
- (3) $2\,\mathrm{H}$
- **(4)** $1\,\mathrm{H}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\phi = Li$
2. $1000 \times 4 \times 10^{-3} = L4$
3. $1 = L$

**Solved independently** (answer withheld)

1. Total flux linkage of the solenoid equals $L I$: $N\Phi = L I$.
2. $L = \frac{N\Phi}{I} = \frac{1000 \times 4 \times 10^{-3}\,\mathrm{Wb}}{4\,\mathrm{A}}$.
3. $L = \frac{4}{4}\,\mathrm{H} = 1\,\mathrm{H}$, which is option $4$.

**Subtopic:** Self Inductance of Solenoid · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q042_1d0bcb64_28102026.png?v=1d0bcb64f4c3)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q042_01518316_28102026.png?v=01518316b0b5)

---

## Q43

Physics · Alternating Current

A small signal voltage $V(t) = V_0 \sin \omega t$ is applied across an ideal capacitor C:

- (1) Current I(t), legs voltage V(t) by $90^{\circ}$
- **(2)** Over a full cycle the capacitor C does not consume any energy from the voltage source
- (3) Current I(t) is in phase with voltage V(t).
- (4) Current I(t) leads voltage V(t) by $180^{\circ}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In capacitor current leads the voltage.
2. Average power dissipated in capacitor is zero

**Solved independently** (answer withheld)

1. $V(t) = V_0 \sin \omega t$, and the capacitor current is $I(t) = C\frac{dV}{dt} = \omega C V_0 \cos \omega t$.
2. $\omega C V_0 \cos \omega t = I_0 \sin(\omega t + 90^{\circ})$, so the current leads the voltage by $90^{\circ}$. That rules out options $1$, $3$ and $4$.
3. Average power $P_{avg} = V_{rms} I_{rms} \cos\phi = V_{rms} I_{rms} \cos 90^{\circ} = 0$.
4. Over a full cycle the capacitor consumes no energy, which is option $2$.

**Subtopic:** AC Voltage Applied to a Capacitor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q043_3c6f9360_28102026.png?v=3c6f93608a5a)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q043_afa8cf86_28102026.png?v=afa8cf860fd1)

---

## Q44

Physics · Ray Optics

Match the corresponding entries of column 1 with column 2. [Where m is the magnification produced by the mirror]

| List-I | | List-II | |
|---|---|---|---|
| A | $m = -2$ | a | Convex mirror |
| B | $m = -\frac{1}{2}$ | b | Concave mirror |
| C | $m = +2$ | c | Real image |
| D | $m = +\frac{1}{2}$ | d | Virtual image |

- **(1)** A $\rightarrow$ b and c; B$\rightarrow$ b and c; C$\rightarrow$ b and d; D$\rightarrow$ a and d
- (2) A $\rightarrow$ a and c; B$\rightarrow$ a and d; d$\rightarrow$ a and b; D$\rightarrow$ c and d
- (3) A $\rightarrow$ a and d; B$\rightarrow$ b and c; C$\rightarrow$ b and d; D$\rightarrow$ b and c
- (4) A $\rightarrow$ c and d; B$\rightarrow$ b and d; C$\rightarrow$ b and c; D$\rightarrow$ a and d

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $m = \frac{-\mathrm{V}}{\mathrm{u}} = \frac{\mathrm{f}}{\mathrm{f} \times \mathrm{u}}$
2. $m = -2$ then “V” and “u” same given
3. $-2 = \frac{\mathrm{f}}{\mathrm{f} \times \mathrm{u}} - 2\mathrm{f} + 2\mathrm{u} = \mathrm{f}$
4. $= 3\mathrm{f} = -2\mathrm{u}$
5. $\frac{+3\mathrm{f}}{2} = 4$
6. For mirror so $4$ negative
7. $\therefore$ V has to be negative

**Solved independently** (answer withheld)

1. A negative magnification ($m<0$) means an inverted image, and an inverted image from a single mirror is always real, formed only by a concave mirror, so $A$ ($m=-2$) $\rightarrow$ b and c.
2. Likewise $B$ ($m=-\frac{1}{2}$) is inverted, so real and from a concave mirror: $B \rightarrow$ b and c.
3. A positive magnification ($m>0$) means an erect, virtual image; $m=+2$ is magnified, which only a concave mirror gives (object within $f$): $C \rightarrow$ b and d.
4. $m=+\frac{1}{2}$ is erect and diminished, which a convex mirror gives: $D \rightarrow$ a and d.
5. The matching A$\rightarrow$b,c; B$\rightarrow$b,c; C$\rightarrow$b,d; D$\rightarrow$a,d is option $1$.

**Subtopic:** Magnification in Mirror · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q044_f486363d_28102026.png?v=f486363de3f1)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q044_aad6489b_28102026.png?v=aad6489bd9a9)

---

## Q45

Physics · Laws of Motion

A car is negotiating a curved road of radius R. The road is banked at an angle $\theta$. The coefficient of friction between the tyres of the car and the road is $\mu_s$. The maximum safe velocity on this road is:

- (1) $\sqrt{gR^2\,\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}}$
- **(2)** $\sqrt{gR\,\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}}$
- (3) $\sqrt{\frac{g}{R}\,\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}}$
- (4) $\sqrt{\frac{g}{R^2}\,\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Forces on a car on a road banked at angle θ: N, friction f, mg sinθ and the components of mv²/r](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q045_sol_1_be88f35d_28102026.png?v=be88f35d25a4)

*Forces on a car on a road banked at angle θ: N, friction f, mg sinθ and the components of mv²/r*

1. $N = mg\cos\theta + \frac{mv^{2}}{r}\sin\theta$
2. $f_{\mathrm{max}} = \mu mg\cos\theta + \frac{\mu mv^{2}}{r}\sin\theta$
3. $mg\sin\theta + \mu mg\cos\theta + \frac{\mu mv^{2}}{r}\sin\theta = \frac{mv^{2}}{r}\cos\theta$
4. $g\sin\theta + g\cos\theta = \frac{V^{2}}{r}(\cos\theta - \mu\sin\theta)$
5. $gr\left[\frac{\tan\theta + \mu}{1 + \mu\tan\theta}\right] = V^{2}$

**Solved independently** (answer withheld)

1. At maximum speed, friction $f = \mu_s N$ acts down the slope.
2. Vertical balance: $N\cos\theta = mg + \mu_s N\sin\theta \Rightarrow N(\cos\theta - \mu_s\sin\theta) = mg$.
3. Horizontal (centripetal): $N\sin\theta + \mu_s N\cos\theta = \frac{mv^2}{R} \Rightarrow N(\sin\theta + \mu_s\cos\theta) = \frac{mv^2}{R}$.
4. Divide: $\frac{v^2}{Rg} = \frac{\sin\theta + \mu_s\cos\theta}{\cos\theta - \mu_s\sin\theta} = \frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}$.
5. $v_{max} = \sqrt{gR\,\frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}$, which is option $2$.

**Subtopic:** Maximum Speed Without Skidding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q045_19a03c67_28102026.png?v=19a03c676d8c)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q045_05a17e8e_28102026.png?v=05a17e8eaaac)

---

## Q46

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Consider the molecules $\mathrm{CH_4}$, $\mathrm{NH_3}$ and $\mathrm{H_2O}$. Which of the given statements is false?

- (1) The H – C – H bond angle in $\mathrm{CH_4}$, the H – N – H bond angle in $\mathrm{NH_3}$, and the H – O – H bond angle in $\mathrm{H_2O}$ are all greater than $90^{\circ}$.
- **(2)** The H – O – H bond angle in $\mathrm{H_2O}$ is larger than the H – C – H bond angle in $\mathrm{CH_4}$.
- (3) The H – O – H bond angle in $\mathrm{H_2O}$ is smaller than the H – N – H bond angle in $\mathrm{NH_3}$.
- (4) The H – C – H bond angle in $\mathrm{CH_4}$ is larger than the H – N – H bond angle in $\mathrm{NH_3}$.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Bond Angle | Molecule
2. $104.5^{\circ}$ | $\mathrm{H_2O}$
3. $107^{\circ}$ | $\mathrm{NH_3}$
4. $109^{\circ}28'$ | $\mathrm{CH_4}$
5. All the molecules are $sp^{3}$ hybridized and Bond angle of $\mathrm{H_2O}$ is smaller than $\mathrm{NH_3}$.

**Solved independently** (answer withheld)

1. All three central atoms are $sp^3$ hybridised; lone pairs compress the bond angle (VSEPR: lp-lp > lp-bp > bp-bp repulsion).
2. $\mathrm{CH_4}$ has no lone pair: $\angle HCH = 109.5^{\circ}$.
3. $\mathrm{NH_3}$ has one lone pair: $\angle HNH \approx 107^{\circ}$.
4. $\mathrm{H_2O}$ has two lone pairs: $\angle HOH \approx 104.5^{\circ}$.
5. Option 1: all angles $> 90^{\circ}$, true. Option 3: $104.5^{\circ} < 107^{\circ}$, true. Option 4: $109.5^{\circ} > 107^{\circ}$, true.
6. Option 2 claims $104.5^{\circ} > 109.5^{\circ}$, which is false, so the answer is option $2$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q046_877e6771_28102026.png?v=877e67711493)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q046_cd43252c_28102026.png?v=cd43252c06c6)

---

## Q47

Chemistry · organic · Hydrocarbons

In the reaction X and Y are:

![printed figure: ethyne →((1) NaNH₂ /liq. NH₃ (2) CH₃ CH₂ Br) X →((1) NaNH₂ /liq. NH₃ (2) CH₃ CH₂Br) Y](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q047_9204b0c0_28102026.png?v=9204b0c08d3a)

*ethyne →[(1) NaNH₂ /liq. NH₃ (2) CH₃ CH₂ Br] X →[(1) NaNH₂ /liq. NH₃ (2) CH₃ CH₂Br] Y*

Structures: ethyne `C#C`

- **(1)** X = 1 – Butyne ; Y = 3 – Hexyne
- (2) X = 2 – Butyne ; Y = 3 – Hexyne
- (3) X = 2 – Butyne ; Y = 2 – Hexyne
- (4) X = 1 – Butyne ; Y = 2 – Hexyne

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: ethyne →(NaNH₂/liq.NH₃) sodium ethynide (H−C≡C̄:Na⁺) →(CH₃CH₂Br) but-1-yne, 1-Butyne (x) →(NaNH₂/liq.NH₃) sodium but-1-yn-1-ide (Na⁺:C≡C̄−CH₂CH₃) →(CH₃CH₂Br) hex-3-yne, 3-Hexyne (y)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q047_sol_1_cd8adf46_28102026.png?v=cd8adf46ea28)

*ethyne →[NaNH₂/liq.NH₃] sodium ethynide (H−C≡C̄:Na⁺) →[CH₃CH₂Br] but-1-yne, 1-Butyne (x) →[NaNH₂/liq.NH₃] sodium but-1-yn-1-ide (Na⁺:C≡C̄−CH₂CH₃) →[CH₃CH₂Br] hex-3-yne, 3-Hexyne (y)*


**Solved independently** (answer withheld)

1. $\mathrm{NaNH_2}$ in liquid $\mathrm{NH_3}$ removes the acidic terminal H: $\mathrm{HC{\equiv}CH \rightarrow HC{\equiv}C^-Na^+}$.
2. The acetylide attacks $\mathrm{CH_3CH_2Br}$ ($S_N2$): $\mathrm{HC{\equiv}C^- + CH_3CH_2Br \rightarrow HC{\equiv}C\text{-}CH_2CH_3}$, which is 1-butyne, so $X$ = 1-butyne.
3. 1-Butyne still has a terminal H; $\mathrm{NaNH_2}$ gives $\mathrm{^-C{\equiv}C\text{-}CH_2CH_3}$.
4. Ethylation gives $\mathrm{CH_3CH_2\text{-}C{\equiv}C\text{-}CH_2CH_3}$, which is 3-hexyne, so $Y$ = 3-hexyne.
5. $X$ = 1-butyne, $Y$ = 3-hexyne matches option $1$.

**Subtopic:** Preparation of Alkynes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q047_9a89f114_28102026.png?v=9a89f1143046)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q047_58f817d7_28102026.png?v=58f817d75064)

---

## Q48

Chemistry · inorganic · The p–Block Elements

Among the following, the correct order of acidity is:

- (1) $\mathrm{HClO_3} < \mathrm{HClO_4} < \mathrm{HClO_2} < \mathrm{HClO}$
- **(2)** $\mathrm{HClO} < \mathrm{HClO_2} < \mathrm{HClO_3} < \mathrm{HClO_4}$
- (3) $\mathrm{HClO_2} < \mathrm{HClO} < \mathrm{HClO_3} < \mathrm{HClO_4}$
- (4) $\mathrm{HClO_4} < \mathrm{HClO_2} < \mathrm{HClO} < \mathrm{HClO_3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Oxidation state of chlorine $\propto$ Acidity of Oxo Acid.
2. $\mathrm{HClO} < \mathrm{HClO_2} < \mathrm{HClO_3} < \mathrm{HClO_4}$ is the correct increasing order.

**Solved independently** (answer withheld)

1. Oxidation states of Cl: $\mathrm{HClO}$ is $+1$, $\mathrm{HClO_2}$ is $+3$, $\mathrm{HClO_3}$ is $+5$, $\mathrm{HClO_4}$ is $+7$.
2. More O atoms on Cl spread the negative charge of the conjugate base $\mathrm{ClO_n^-}$ over more atoms, so it is more stable and the acid is stronger.
3. Hence $\mathrm{HClO} < \mathrm{HClO_2} < \mathrm{HClO_3} < \mathrm{HClO_4}$, which is option $2$.

**Subtopic:** Hydrogen Halides, Oxoacids of Halogens · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q048_5f9e9224_28102026.png?v=5f9e9224093d)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q048_fe310dcd_28102026.png?v=fe310dcdb353)

---

## Q49

Chemistry · physical · Chemical Kinetics

The rate of a first-order reaction is $0.04\,\mathrm{mol\,l^{-1}s^{-1}}$ at 10 second and $0.03\,\mathrm{mol\,l^{-1}s^{-1}}$ at 20 seconds after initiation of the reaction. The half-life period of the reaction is:

- **(1)** $24.1\,\mathrm{s}$
- (2) $34.1\,\mathrm{s}$
- (3) $44.1\,\mathrm{s}$
- (4) $54.1\,\mathrm{s}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\begin{array}{cc} \text{Rate} & \text{Time} \\ 0.04 & 10 \\ 0.03 & 20 \end{array}$
2. For first order reaction $r \propto$ conc.
3. $\frac{r_1}{r_2} = \frac{C_1}{C_2} = \frac{4}{3}$
4. $\therefore k = \frac{2.303}{t_2 - t_1}\log\frac{C_1}{C_2}$
5. $\Rightarrow \frac{0.693}{t_{1/2}} = \frac{2.303}{20 - 10}\log\frac{4}{3}$
6. On solving $t_{1/2} = 24.1\,\mathrm{s}$

**Solved independently** (answer withheld)

1. For a first-order reaction $r = k[A]$, so $\frac{r_1}{r_2} = \frac{[A]_{10}}{[A]_{20}} = \frac{0.04}{0.03} = \frac{4}{3}$.
2. Over $\Delta t = 20 - 10 = 10\,\mathrm{s}$: $k = \frac{2.303}{10}\log\frac{4}{3} = 0.2303 \times 0.1249 = 0.02877\,\mathrm{s^{-1}}$.
3. $t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.02877} = 24.1\,\mathrm{s}$, which is option $1$.

**Subtopic:** Half-Life of a Reaction, First Order Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q049_8f499afb_28102026.png?v=8f499afb8fbc)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q049_c1f326f8_28102026.png?v=c1f326f8fc7f)

---

## Q50

Chemistry · physical · Surface Chemistry

Which one of the following characteristics is associated with adsorption?

- (1) $\Delta G$ is negative but $\Delta H$ and $\Delta S$ are positive
- **(2)** $\Delta G$, $\Delta H$ and $\Delta S$ all are negative
- (3) $\Delta G$ and $\Delta H$ are negative but $\Delta S$ is positive
- (4) $\Delta G$ and $\Delta S$ are negative but $\Delta H$ is positive

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\Delta\mathrm{H} < 0$ Adsorption process is exothermic
2. $\Delta\mathrm{G} < 0$ Adsorption process is Feasible
3. $\Delta S < 0$ Adsorption process is accompanied of decrease in entropy.

**Solved independently** (answer withheld)

1. Adsorption happens spontaneously, so $\Delta G < 0$.
2. Molecules on the surface lose freedom of movement, so $\Delta S < 0$.
3. For $\Delta G = \Delta H - T\Delta S$ to be negative while $-T\Delta S > 0$, $\Delta H$ must be negative: adsorption is exothermic.
4. $\Delta G$, $\Delta H$ and $\Delta S$ are all negative, which is option $2$.

**Subtopic:** Thermodynamics of Adsorption · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q050_986eed40_28102026.png?v=986eed404d1f)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q050_e3da3461_28102026.png?v=e3da3461d0e8)

---

## Q51

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

In which of the following options the order of arrangement does not agree with the variation of property indicated against it?

- (1) $\mathrm{Al^{3+}} < \mathrm{Mg^{2+}} < \mathrm{Na^{+}} < \mathrm{F^{-}}$ (increasing ionic size)
- **(2)** $\mathrm{B} < \mathrm{C} < \mathrm{N} < \mathrm{O}$ (increasing first ionization enthalpy)
- **(3)** $\mathrm{I} < \mathrm{Br} < \mathrm{Cl} < \mathrm{F}$ (increasing electron gain enthalpy)
- (4) $\mathrm{Li} < \mathrm{Na} < \mathrm{K} < \mathrm{Rb}$ (increasing metallic radius)

**Answer** — booklet: (2, 3) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{N}$ is having $ns^{2}\,np^{3}$ (Half filled configuration).
2. Hence has high IP than $\mathrm{O}$ which is having $ns^{2}\,np^{4}$ electronic configuration.

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{Al^{3+}}, \mathrm{Mg^{2+}}, \mathrm{Na^{+}}, \mathrm{F^{-}}$ are isoelectronic; size grows as nuclear charge falls, so $\mathrm{Al^{3+}} < \mathrm{Mg^{2+}} < \mathrm{Na^{+}} < \mathrm{F^{-}}$ is correct.
2. Option 4: metallic radius increases down Group 1, so $\mathrm{Li} < \mathrm{Na} < \mathrm{K} < \mathrm{Rb}$ is correct.
3. Option 2: N has a half-filled $2p^3$ configuration, so $\Delta_i H_1(\mathrm{N}) \approx 1402 > \Delta_i H_1(\mathrm{O}) \approx 1314\ \mathrm{kJ\,mol^{-1}}$; the true order is $\mathrm{B} < \mathrm{C} < \mathrm{O} < \mathrm{N}$, so option 2 is wrong.
4. Option 3: $|\Delta_{eg}H|$ is $\mathrm{I}\ (295) < \mathrm{Br}\ (325) < \mathrm{F}\ (328) < \mathrm{Cl}\ (349)\ \mathrm{kJ\,mol^{-1}}$; F is less negative than Cl due to its small, crowded 2p shell, so $\mathrm{I} < \mathrm{Br} < \mathrm{Cl} < \mathrm{F}$ is also wrong.
5. Both options $2$ and $3$ disagree with the stated property; option $2$ is the unambiguous error, so choose option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy, Trends in Chemical Properties – Electron Gain Enthalpy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q051_999f8dbf_28102026.png?v=999f8dbf5d35)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q051_9481f85a_28102026.png?v=9481f85ac67e)

---

## Q52

Chemistry · inorganic · The s-Block Elements

Which of the following statements is false?

- (1) $\mathrm{Mg^{2+}}$ ions form a complex with ATP.
- (2) $\mathrm{Ca^{2+}}$ ions are important in blood clotting.
- **(3)** $\mathrm{Ca^{2+}}$ ions are not important in maintaining the regular beating of the heart.
- (4) $\mathrm{Mg^{2+}}$ ions are important in the green parts of plants.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Monovalent sodium and potassium ions and divalent magnesium and calcium ions are found in large properties in biological fluids.
2. There ions perform important biological functions such as maintenance of heart and nerve impulse.

**Solved independently** (answer withheld)

1. $\mathrm{Mg^{2+}}$ binds ATP as the Mg-ATP complex used by kinases, so option $1$ is true.
2. $\mathrm{Ca^{2+}}$ (clotting factor IV) is required in the blood-clotting cascade, so option $2$ is true.
3. $\mathrm{Mg^{2+}}$ is the central ion of chlorophyll in green plant parts, so option $4$ is true.
4. $\mathrm{Ca^{2+}}$ is needed for contraction of cardiac muscle and the regular heartbeat, so saying it is not important is false: option $3$.

**Subtopic:** Biological Importance of Sodium, Potassium, Magnesium and Calcium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q052_4ab90486_28102026.png?v=4ab904860537)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q052_f7a28457_28102026.png?v=f7a28457e99f)

---

## Q53

Chemistry · inorganic · Hydrogen

Which of the following statements about hydrogen is incorrect?

- **(1)** Hydrogen has three isotopes of which tritium is the most common.
- (2) Hydrogen never acts as cation in ionic salts.
- (3) Hydronium ion, $\mathrm{H_3O^+}$ exists freely in solution.
- **(4)** Dihydrogen does not act as a reducing agent.

**Answer** — booklet: (1, 4) · independent solve: (1) · agree

**Publisher's solution**

1. Hydrogen is having three isotopes protium, Dentenium and tritium in which tritium is Radioactive and very rare.

**Solved independently** (answer withheld)

1. Hydrogen has three isotopes: protium ($^1_1\mathrm{H}$), deuterium ($^2_1\mathrm{H}$) and tritium ($^3_1\mathrm{H}$).
2. Protium makes up about $99.985\%$ of natural hydrogen, while tritium occurs only in trace amounts, so statement 1 is incorrect.
3. Statement 4 is also false as written: $\mathrm{H_2}$ does act as a reducing agent (e.g. $\mathrm{CuO + H_2 \rightarrow Cu + H_2O}$).
4. Statements 2 and 3 are taken as correct as the textbook presents them ($\mathrm{H^+}$ does not stay a free cation in salts; $\mathrm{H_3O^+}$ exists in aqueous solution).
5. Two options (1 and 4) read as incorrect; option $1$ is chosen as the most clearly intended answer.

**Subtopic:** Isotopes of Hydrogen and Properties of Dihydrogen · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q053_e3c311a4_28102026.png?v=e3c311a439f4)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q053_b90fa58e_28102026.png?v=b90fa58eb283)

---

## Q54

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The correct statement regarding a carbonyl compound with a hydrogen atom on its alpha carbon, is:

- (1) A carbonyl compound with a hydrogen atom on its alpha-carbon never equilibrates with its corresponding enol.
- (2) A carbonyl compound with a hydrogen atom on its alpha-carbon rapidly equilibrates with its corresponding enol and this process is known as aldehyde-ketone equilibration.
- (3) A carbonyl compound with a hydrogen atom on its alpha-carbon rapidly equilibrates with its corresponding enol and this process is known as carbonylation.
- **(4)** A carbonyl compound with a hydrogen atom on its alpha-carbon rapidly equilibrates with its corresponding enol and this process is known as keto-enol tautomerism.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: R-CH2-CO-CH2-R (keto form); R-CH=C(OH)-CH2-R enol form; Ketoenol tautomerism](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q054_sol_1_523de516_28102026.png?v=523de51669e6)

*R-CH2-CO-CH2-R (keto form); R-CH=C(OH)-CH2-R enol form; Ketoenol tautomerism*


**Solved independently** (answer withheld)

1. A carbonyl compound with an $\alpha$-H rapidly equilibrates with its enol ($\mathrm{-CH-C{=}O \rightleftharpoons -C{=}C-OH}$); this proton-shift isomerism is called keto-enol tautomerism, which is option $4$.

**Subtopic:** Keto-Enol Tautomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q054_39fac0bd_28102026.png?v=39fac0bdc68e)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q054_8ecfe67d_28102026.png?v=8ecfe67d1750)

---

## Q55

Chemistry · physical · Ionic Equilibrium

$\mathrm{MY}$ and $\mathrm{NY_3}$, two nearly insoluble salts, have the same $\mathrm{K_{sp}}$ values of $6.2 \times 10^{-13}$ at room temperature. Which statement would be true in regard to $\mathrm{MY}$ and $\mathrm{NY_3}$?

- (1) The molar solubilities of $\mathrm{MY}$ and $\mathrm{NY_3}$ in water are identical.
- **(2)** The molar solubility of $\mathrm{MY}$ in water is less than that of $\mathrm{NY_3}$.
- (3) The salts $\mathrm{MY}$ and $\mathrm{NY_3}$ are more soluble in $0.5\,\mathrm{M}$ $\mathrm{KY}$ than in pure water.
- (4) The addition of the salt of $\mathrm{KY}$ to solution of $\mathrm{MY}$ and $\mathrm{NY_3}$ will have no effect on their solubilities.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{MY}$ insoluble salt $\mathrm{K_{sp}} = \mathrm{s}^{2}$
2. $\mathrm{MY_{(s)}} \rightleftharpoons \mathrm{M^{+}_{(aq)}} + \mathrm{Y^{-}_{(aq)}}$
3. $\mathrm{NY_3}$ insoluble salt $\mathrm{K_{sp}} = 4\mathrm{s}^{3}$
4. $\mathrm{NY_{3(s)}} \rightleftharpoons \mathrm{N^{+}_{(aq)}} + 3\mathrm{Y^{-}_{(aq)}}$
5. $\therefore \mathrm{S_{(MY)}} = \sqrt{6.2 \times 10^{-13}} = 7.8 \times 10^{-7}$
6. Solubility values
7. $\therefore \mathrm{S_{(NY_3)}} = \left(\frac{6.2 \times 10^{-13}}{4}\right)^{1/3} = 5.2 \times 10^{-5}$
8. $\therefore \mathrm{S_{(MY)}} < \mathrm{S_{(NY_3)}}$

**Solved independently** (answer withheld)

1. For $\mathrm{MY} \rightleftharpoons \mathrm{M^+} + \mathrm{Y^-}$: $K_{sp} = s^2$.
2. $s_{\mathrm{MY}} = \sqrt{6.2 \times 10^{-13}} \approx 7.9 \times 10^{-7}\,\mathrm{M}$.
3. For $\mathrm{NY_3} \rightleftharpoons \mathrm{N^{3+}} + 3\mathrm{Y^-}$: $K_{sp} = s(3s)^3 = 27s^4$.
4. $s_{\mathrm{NY_3}} = \left(\frac{6.2 \times 10^{-13}}{27}\right)^{1/4} = (2.3 \times 10^{-14})^{1/4} \approx 3.9 \times 10^{-4}\,\mathrm{M}$.
5. $7.9 \times 10^{-7} < 3.9 \times 10^{-4}$, so $\mathrm{MY}$ is less soluble than $\mathrm{NY_3}$.
6. $\mathrm{KY}$ supplies the common ion $\mathrm{Y^-}$, which lowers both solubilities, so options $3$ and $4$ are false; the answer is option $2$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q055_d6313761_28102026.png?v=d63137612123)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q055_f7ece526_28102026.png?v=f7ece52646b2)

---

## Q56

Chemistry · organic · Biomolecules

In a protein molecule various amino acids are linked together by:

- (1) $\alpha$-glycosidic bond
- (2) $\beta$- glycosidic bond
- **(3)** Peptide bond
- (4) Dative bond

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: $\ce{H2NCH(R)-COOH}$ (alpha-amino acid) + $\ce{H2N-CH(R)-COOH}$ (alpha-amino acid) →($\ce{-H2O}$) $\ce{H2N-CH(R)-C(=O)-NH-CH(R)-COOH}$ (dipeptide); the -C(=O)-NH- link is boxed and labelled Peptide bond](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q056_sol_1_b1de5a92_28102026.png?v=b1de5a925d6a)

*$\ce{H2NCH(R)-COOH}$ (alpha-amino acid) + $\ce{H2N-CH(R)-COOH}$ (alpha-amino acid) →[$\ce{-H2O}$] $\ce{H2N-CH(R)-C(=O)-NH-CH(R)-COOH}$ (dipeptide); the -C(=O)-NH- link is boxed and labelled Peptide bond*


**Solved independently** (answer withheld)

1. Amino acids in a polypeptide are joined when the $-COOH$ of one condenses with the $-NH_2$ of the next, giving $-CO-NH-$ (a peptide bond) and releasing $H_2O$, so the answer is option $3$; $\alpha$/$\beta$-glycosidic bonds link monosaccharides.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q056_45f42bff_28102026.png?v=45f42bff6eb4)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q056_c97fcbf1_28102026.png?v=c97fcbf186f8)

---

## Q57

Chemistry · organic · Polymers

Nutural rubber has:

- **(1)** All cis – configuration
- (2) All trans – configuration
- (3) Alternate cis – and trans – configuration
- (4) Random cis – and trans – configuration

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: cis poly isoprene: $\ce{...-CH2-C(CH3)=CH-CH2-CH2-C(CH3)=CH-CH2-...}$ (two repeat units, each C=C drawn cis with both chain CH2 groups on the same side)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q057_sol_1_e3030c42_28102026.png?v=e3030c427aa9)

*cis poly isoprene: $\ce{...-CH2-C(CH3)=CH-CH2-CH2-C(CH3)=CH-CH2-...}$ (two repeat units, each C=C drawn cis with both chain CH2 groups on the same side)*


**Solved independently** (answer withheld)

1. Natural rubber is a linear polymer of isoprene ($\mathrm{CH_2{=}C(CH_3){-}CH{=}CH_2}$) joined 1,4 to give cis-1,4-polyisoprene, in which every $\mathrm{C{=}C}$ unit is cis, so the answer is option $1$ (all cis).

**Subtopic:** Natural Rubber (cis-1,4-Polyisoprene) and Vulcanisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q057_87744d8e_28102026.png?v=87744d8ed77a)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q057_b2fe6e3e_28102026.png?v=b2fe6e3e0348)

---

## Q58

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Match items of column I with the items of column II and assign the correct code:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cyanide process | (i) | Ultrapure $\mathrm{Ge}$ |
| (b) | Froth floatation process | (ii) | Dressing of $\mathrm{ZnS}$ |
| (c) | Electrolytic reduction | (iii) | Extraction of $\mathrm{Al}$ |
| (d) | Zone refining | (iv) | Extraction of $\mathrm{Au}$ |
|  |  | (v) | Purification of $\mathrm{Ni}$ |

- **(1)** (a) (b) (c) (d) (iv) (ii) (iii) (i)
- (2) (a) (b) (c) (d) (ii) (iii) (i) (v)
- (3) (a) (b) (c) (d) (i) (ii) (iii) (iv)
- (4) (a) (b) (c) (d) (iii) (iv) (v) (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. a] Cyanide process is used to extract and $\mathrm{Au}$ in hydrometallurgy.
2. b] Froth foundation process is used for dressing of sulfide ores.
3. c] Electrolytic reduction is used to extract $\mathrm{Al}$.
4. d] Zone refinining process is used for obtaining ultrapure $\mathrm{Ge}$.

**Solved independently** (answer withheld)

1. Cyanide (leaching) process is used for extraction of gold: (a) $\rightarrow$ (iv) Extraction of $\mathrm{Au}$.
2. Froth floatation concentrates sulphide ores: (b) $\rightarrow$ (ii) Dressing of $\mathrm{ZnS}$.
3. Electrolytic reduction (Hall-Heroult) is used for aluminium: (c) $\rightarrow$ (iii) Extraction of $\mathrm{Al}$.
4. Zone refining gives semiconductors of very high purity: (d) $\rightarrow$ (i) Ultrapure $\mathrm{Ge}$.
5. The code (iv), (ii), (iii), (i) is option $1$.

**Subtopic:** Concentration of Ores, Refining of Metals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q058_78ee9ffb_28102026.png?v=78ee9ffb750c)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q058_c27bdd2c_28102026.png?v=c27bdd2c21d7)

---

## Q59

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which one of the following statements is correct when $\mathrm{SO_2}$ is passed through acidified $\mathrm{K_2Cr_2O_7}$ solution?

- (1) The solution turns blue.
- (2) The solution is decolourized.
- (3) $\mathrm{SO_2}$ is reduced.
- **(4)** Green $\mathrm{Cr_2(SO_4)_3}$ is formed.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{K_2Cr_2O_7} + \mathrm{SO_2} + \mathrm{H_2SO_4} \rightarrow \mathrm{K_2SO_4} + \underset{\text{Green}}{\mathrm{Cr_2(SO_4)_3}} + \mathrm{H_2O}$

**Solved independently** (answer withheld)

1. In acid, $\mathrm{Cr_2O_7^{2-}}$ (orange) is an oxidising agent and $\mathrm{SO_2}$ is a reducing agent.
2. $\mathrm{K_2Cr_2O_7 + H_2SO_4 + 3SO_2 \rightarrow K_2SO_4 + Cr_2(SO_4)_3 + H_2O}$.
3. Chromium goes from $+6$ to $+3$ (reduced); sulphur goes from $+4$ to $+6$, so $\mathrm{SO_2}$ is oxidised, ruling out option $3$.
4. The colour changes from orange to green (not blue, not colourless), ruling out options $1$ and $2$.
5. Green $\mathrm{Cr_2(SO_4)_3}$ is formed, which is option $4$.

**Subtopic:** Potassium Dichromate (K2Cr2O7) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q059_c9f78e23_28102026.png?v=c9f78e23fe54)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q059_1205991e_28102026.png?v=1205991e46f2)

---

## Q60

Chemistry · inorganic · The D- and F-Block Elements – Practice

The electronic configurations of Eu (Atomic no. 63), Gd (Atomic NO. 64) and Tb (Atomic No. 65) are:

- (1) $[\mathrm{Xe}]4f^{7}6s^{2}$, $[\mathrm{Xe}]4f^{8}6s^{2}$ and $[\mathrm{Xe}]4f^{8}5d^{1}6s^{2}$
- (2) $[\mathrm{Xe}]4f^{6}5d^{1}6s^{2}$, $[\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$ and $[\mathrm{Xe}]4f^{9}6s^{2}$
- (3) $[\mathrm{Xe}]4f^{6}5d^{1}6s^{2}$, $[\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$ and $[\mathrm{Xe}]4f^{8}5d^{1}6s^{2}$
- **(4)** $[\mathrm{Xe}]4f^{7}6s^{2}$, $[\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$ and $[\mathrm{Xe}]4f^{9}6s^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{Eu} - [\mathrm{Xe}]4f^{7}, 6s^{2}$
2. $\mathrm{Gd} - [\mathrm{Xe}]4f^{7}, 5d^{1}, 6s^{2}$
3. $\mathrm{T_{6}} - [\mathrm{Xe}]4f^{9}, 6s^{2}$

**Solved independently** (answer withheld)

1. Eu ($Z=63$): $63-54 = 9$ electrons beyond Xe, giving $[\mathrm{Xe}]4f^{7}6s^{2}$ (half-filled $4f$).
2. Gd ($Z=64$): the extra electron goes to $5d$ to keep the stable half-filled $4f^{7}$, giving $[\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$.
3. Tb ($Z=65$): $11$ electrons beyond Xe settle as $[\mathrm{Xe}]4f^{9}6s^{2}$.
4. The set $4f^{7}6s^{2}$, $4f^{7}5d^{1}6s^{2}$, $4f^{9}6s^{2}$ is option $4$.

**Subtopic:** Electronic Configurations of the d-Block & f-Block · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q060_78869e5e_28102026.png?v=78869e5e1ac4)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q060_75b59057_28102026.png?v=75b59057d542)

---

## Q61

Chemistry · physical · Structure of Atom

Two electrons occupying the same orbital are distinguished by:

- (1) Principal quantum number
- (2) Magnetic quantum number
- (3) Azimuthal quantum number
- **(4)** Spin quantum number

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Electron occupying same orbital have different spin quantum number.

**Solved independently** (answer withheld)

1. Two electrons in the same orbital have the same $n$, $l$ and $m_l$.
2. By the Pauli exclusion principle no two electrons can have all four quantum numbers identical, so they differ in $m_s = +\frac{1}{2}$ and $-\frac{1}{2}$, which is option $4$.

**Subtopic:** Quantum Numbers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q061_452399ad_28102026.png?v=452399ad380b)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q061_12235e56_28102026.png?v=12235e564670)

---

## Q62

Chemistry · inorganic · The p–Block Elements

When copper is heated with conc. $\mathrm{HNO_3}$ it produces:

- **(1)** $\mathrm{Cu(NO_3)_2}$ and $\mathrm{NO_2}$
- (2) $\mathrm{Cu(NO_3)_2}$ and $\mathrm{NO}$
- (3) $\mathrm{Cu(NO_3)_2}$, $\mathrm{NO}$ and $\mathrm{NO_2}$
- (4) $\mathrm{Cu(NO_3)_2}$ and $\mathrm{N_2O}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Cu} + 4\mathrm{HNO_3} \rightarrow \mathrm{Cu(NO_3)_2} + 2\mathrm{NO_2} + \mathrm{O_2}$

**Solved independently** (answer withheld)

1. Concentrated nitric acid is reduced by copper to $\mathrm{NO_2}$: $\mathrm{Cu + 4HNO_3(conc.) \rightarrow Cu(NO_3)_2 + 2NO_2 + 2H_2O}$, which is option $1$.

**Subtopic:** Nitric Acid - Preparation, Properties and Oxidising Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q062_e63dd037_28102026.png?v=e63dd0379e01)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q062_606fc22b_28102026.png?v=606fc22b976f)

---

## Q63

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Which of the following reagents would distinguish cis-cyclopenta-1, 2-diol from the trans-isomer?

- **(1)** Acetone
- (2) Ozone
- (3) $\mathrm{MnO_2}$
- (4) Aluminium isopropoxide

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: acetone + cyclopentane-1,2-diol → 2,2-dimethyltetrahydro-3aH-cyclopenta(d)(1,3)dioxole](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q063_sol_1_150e95c7_28102026.png?v=150e95c7fa95)

*acetone + cyclopentane-1,2-diol → 2,2-dimethyltetrahydro-3aH-cyclopenta[d][1,3]dioxole*

1. Ketal formation

**Solved independently** (answer withheld)

1. In cis-cyclopentane-1,2-diol both $\mathrm{OH}$ groups lie on the same face of the ring, so they can close a five-membered ring onto one carbon.
2. Acetone condenses with such a 1,2-diol under acid to give a cyclic ketal: $\text{cis-diol} + \mathrm{(CH_3)_2C{=}O} \xrightarrow{\mathrm{H^+}} \text{acetonide} + \mathrm{H_2O}$.
3. In the trans-isomer the $\mathrm{OH}$ groups point to opposite faces of the rigid cyclopentane ring, so the fused ketal ring cannot form.
4. Ozone, $\mathrm{MnO_2}$ and aluminium isopropoxide act on both isomers alike (or not at all), so only acetone tells them apart, which is option $1$.

**Subtopic:** Nucleophilic Addition Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q063_0a085d1e_28102026.png?v=0a085d1e7b6c)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q063_3d7f78a7_28102026.png?v=3d7f78a7deff)

---

## Q64

Chemistry · physical · Thermodynamics

The correct thermodynamic conditions for the spontaneous reaction at all temperatures is:

- (1) $\Delta \mathrm{H} < 0$ and $\Delta \mathrm{S} = 0$
- (2) $\Delta \mathrm{H} > 0$ and $\Delta \mathrm{S} < 0$
- **(3)** $\Delta \mathrm{H} < 0$ and $\Delta \mathrm{S} > 0$
- (4) $\Delta \mathrm{H} < 0$ and $\Delta \mathrm{S} < 0$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\Delta \mathrm{G} = \Delta \mathrm{H} - \mathrm{T}\Delta \mathrm{S}$
2. Spontaneous at all temperature $\Delta \mathrm{H} < 0, \Delta \mathrm{S} > 0$

**Solved independently** (answer withheld)

1. Spontaneity requires $\Delta G = \Delta H - T\Delta S < 0$.
2. With $\Delta H < 0$ and $\Delta S > 0$, both $\Delta H$ and $-T\Delta S$ are negative for every $T > 0$, so $\Delta G < 0$ at all temperatures.
3. Option $1$ ($\Delta S = 0$) also gives $\Delta G = \Delta H < 0$ formally, but the textbook condition for spontaneity at all temperatures is $\Delta H < 0$, $\Delta S > 0$, which is option $3$.

**Subtopic:** Gibbs Energy and Spontaneity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q064_00ce0761_28102026.png?v=00ce0761d1c9)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q064_b01acc9a_28102026.png?v=b01acc9a41bb)

---

## Q65

Chemistry · physical · The Solid State

Lithium has a bcc structure. Its density is $530\,\mathrm{kg\,m^{-3}}$ and its atomic mass is $6.94\,\mathrm{g\,mol^{-1}}$. Calculated the edge length of a unit cell of Lithium metal. $(\mathrm{N_A} = 6.02 \times 10^{23}\,\mathrm{mol^{-1}})$

- (1) $154\,\mathrm{pm}$
- **(2)** $352\,\mathrm{pm}$
- (3) $527\,\mathrm{pm}$
- (4) $264\,\mathrm{pm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{d} = \frac{\mathrm{Z\,M}}{\mathrm{N_A\,a^{3}}}$
2. $\mathrm{a}^{3} = \frac{6.94 \times 2}{6.022 \times 10^{23} \times 530 \times 10^{-3}} = \frac{6.94 \times 200 \times 10^{-24}}{5.30 \times 6.022}$
3. $= 3.52 \times 10^{-8}\,\mathrm{cm}$
4. $= 352\,\mathrm{pm}$

**Solved independently** (answer withheld)

1. A bcc unit cell contains $Z = 2$ atoms.
2. Density relation: $\rho = \frac{Z M}{a^3 N_A}$, so $a^3 = \frac{Z M}{\rho N_A}$.
3. Convert molar mass: $M = 6.94\,\mathrm{g\,mol^{-1}} = 6.94 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}$.
4. $a^3 = \frac{2 \times 6.94 \times 10^{-3}}{530 \times 6.02 \times 10^{23}} = \frac{1.388 \times 10^{-2}}{3.1906 \times 10^{26}} = 4.350 \times 10^{-29}\,\mathrm{m^3}$.
5. Write $a^3 = 43.50 \times 10^{-30}\,\mathrm{m^3}$, so $a = (43.50)^{1/3} \times 10^{-10}\,\mathrm{m} \approx 3.52 \times 10^{-10}\,\mathrm{m}$.
6. $a \approx 352\,\mathrm{pm}$, which is option $2$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q065_6547d4a9_28102026.png?v=6547d4a95cd7)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q065_4b786d24_28102026.png?v=4b786d24ca18)

---

## Q66

Chemistry · inorganic · The p–Block Elements

Which one of the following orders is correct for the bond dissociation enthalpy of halogen molecules?

- (1) $\mathrm{I_2} > \mathrm{Br_2} > \mathrm{Cl_2} > \mathrm{F_2}$
- **(2)** $\mathrm{Cl_2} > \mathrm{Br_2} > \mathrm{F_2} > \mathrm{I_2}$
- (3) $\mathrm{Br_2} > \mathrm{I_2} > \mathrm{F_2} > \mathrm{Cl_2}$
- (4) $\mathrm{F_2} > \mathrm{Cl_2} > \mathrm{Br_2} > \mathrm{I_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Decreasing order of Bond energy, $\mathrm{Cl_2} > \mathrm{Br_2} > \mathrm{F_2} > \mathrm{I_2}$
2. The reason is anomalous behavior due to large electron – electron repulsion among the lone pairs in $\mathrm{F_2}$ molecule other than $\mathrm{Cl_2}$ and $\mathrm{Br_2}$.

**Solved independently** (answer withheld)

1. Down the group, bond dissociation enthalpy falls with increasing atomic size: $\mathrm{Cl_2} > \mathrm{Br_2} > \mathrm{I_2}$.
2. $\mathrm{F_2}$ is anomalously low because of strong lone pair-lone pair repulsion between the small F atoms, placing it below $\mathrm{Br_2}$ but above $\mathrm{I_2}$.
3. Order $\mathrm{Cl_2} > \mathrm{Br_2} > \mathrm{F_2} > \mathrm{I_2}$, which is option $2$.

**Subtopic:** General Properties & Trends of Group 17 (Halogens) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q066_17a8f1a2_28102026.png?v=17a8f1a2ce1b)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q066_88a9d53b_28102026.png?v=88a9d53b1f14)

---

## Q67

Chemistry · organic · Chemistry in Everyday Life

Which of the following is an analgesic?

- **(1)** Novalgin
- (2) Penicillin
- (3) Streptomycin
- (4) Chloromycetin

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Novalgin – It is analgesic. Used for treatment of pain.
2. Pencilin – Antibiotic
3. Streptomycin – Antibiotic
4. Chloromycetic – Used for treat infection.

**Solved independently** (answer withheld)

1. Novalgin is a non-narcotic analgesic, while penicillin, streptomycin and chloromycetin (chloramphenicol) are antibiotics, so the answer is option $1$.

**Subtopic:** Analgesics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q067_a4d28017_28102026.png?v=a4d280179c9c)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q067_daa4e6c5_28102026.png?v=daa4e6c54212)

---

## Q68

Chemistry · physical · States of Matter

Equal moles of hydrogen and oxygen gases are placed in a container with a pin-hole through which both can escape. What fraction of the oxygen escape in the time required for one-half of the hydrogen to escape?

- **(1)** $\frac{1}{8}$
- (2) $\frac{1}{4}$
- (3) $\frac{3}{8}$
- (4) $\frac{1}{2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\frac{\frac{n_1}{t_1}}{\frac{n_2}{t_2}} = \sqrt{\frac{M_2}{M_1}} \Rightarrow n_2 = \frac{1}{2}, n_1 = n'$
2. $\Rightarrow \frac{2t_2 n'}{t_1 x_1} = \sqrt{\frac{M_2}{M_1}} = \sqrt{\frac{2}{32}} = \sqrt{\frac{1}{16}} = \frac{1}{4}$
3. Assuming $t_2 = t_1$
4. $\frac{2n' t_2}{t_1} = \frac{1}{4}$
5. $\therefore n' = \frac{1}{8}$

**Solved independently** (answer withheld)

1. Graham's law: $\frac{r_{O_2}}{r_{H_2}} = \sqrt{\frac{M_{H_2}}{M_{O_2}}}$.
2. $\sqrt{\frac{2}{32}} = \sqrt{\frac{1}{16}} = \frac{1}{4}$.
3. Equal moles and equal time, so the fraction of $O_2$ escaped is $\frac{1}{4}$ of the fraction of $H_2$ escaped.
4. $\frac{1}{2} \times \frac{1}{4} = \frac{1}{8}$, which is option $1$.

**Subtopic:** Graham's Law of Diffusion and Effusion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q068_6c7fd925_28102026.png?v=6c7fd925d203)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q068_6c95ab00_28102026.png?v=6c95ab00ea13)

---

## Q69

Chemistry · organic · Hydrocarbons

Consider the nitration of benzene using mixed conc. $\mathrm{H_2SO_4}$ and $\mathrm{HNO_3}$. If a large amount of $\mathrm{KHSO_4}$ is added to the mixture, the rate of nitration will be:

- (1) Faster
- **(2)** Slower
- (3) Unchanged
- (4) Doubled

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: benzene + $\ce{H2SO4}$ + $\ce{HNO3}$ nitrobenzene + $\ce{HSO4-}$ + $\ce{H2O}$](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q069_sol_1_c857a82d_28102026.png?v=c857a82d3907)

*benzene + $\ce{H2SO4}$ + $\ce{HNO3}$ nitrobenzene + $\ce{HSO4-}$ + $\ce{H2O}$*

1. If we add $\mathrm{KHSO_4^-}$, conc. $\mathrm{HSO_4^-}$ increases, equilibrium shifts backward.

**Solved independently** (answer withheld)

1. The electrophile is generated by $\mathrm{HNO_3 + 2H_2SO_4 \rightleftharpoons NO_2^+ + H_3O^+ + 2HSO_4^-}$.
2. $\mathrm{KHSO_4}$ supplies a large amount of the common ion $\mathrm{HSO_4^-}$.
3. By Le Chatelier's principle the equilibrium shifts left, lowering $[\mathrm{NO_2^+}]$.
4. The rate-determining attack of $\mathrm{NO_2^+}$ on benzene depends on $[\mathrm{NO_2^+}]$, so the rate decreases: option $2$ (Slower).

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q069_2194cba1_28102026.png?v=2194cba179f0)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q069_8a4111fc_28102026.png?v=8a4111fcc9de)

---

## Q70

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Predict the correct order among the following:

- **(1)** Lone pair – lone pair > lone pair – bond pair > bond pair – bond pair
- (2) Lone pair – lone pair > bond pair – bond pair > lone pair – bond pair
- (3) Bond pair – bond pair > lone pair – bond pair > lone pair – lone pair
- (4) Lone pair – bond pair > bond pair – bond pair > lone pair – lone pair

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. As per VSEPR theory, overall order of Repulsion is
2. $\underset{\text{(Repulsion)}}{\mathrm{BP}-\mathrm{BP}} < \underset{\text{(Repulsion)}}{\mathrm{BP}-\mathrm{LP}} < \underset{\text{(Repulsion)}}{\mathrm{LP}-\mathrm{LP}}$

**Solved independently** (answer withheld)

1. By VSEPR theory, lone pairs are held only by one nucleus and occupy more space, so their repulsions are greatest: $\text{lp-lp} > \text{lp-bp} > \text{bp-bp}$, which is option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q070_bffb117e_28102026.png?v=bffb117eca86)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q070_3de1a0cd_28102026.png?v=3de1a0cde837)

---

## Q71

Chemistry · inorganic · The s-Block Elements

> ⚠ The booklet prints "Solution: (Bonus)": NTA dropped this question and gave every candidate its marks, so it has no keyed answer.

The product obtained as a result of a reaction of nitrogen with $\mathrm{CaC_2}$ is:

- (1) $\mathrm{Ca(CN)_2}$
- (2) $\mathrm{CaCN}$
- (3) $\mathrm{CaCN_3}$
- (4) $\mathrm{Ca_2CN}$

**Answer** — booklet: (none) · independent solve: (1) · unchecked

**Publisher's solution**

1. $\underset{\text{Calcium Carbide}}{\mathrm{CaC_2}} + \underset{\text{Nitrogen Gas}}{\mathrm{N_2}} \rightarrow \underset{\text{Calcium Cyanamide}}{\mathrm{CaCN_2}} + \mathrm{C}$
2. $\mathrm{CaCN_2}$ is not given in the option so it should be bonus.

**Solved independently** (answer withheld)

1. Nitrogen reacts with calcium carbide at high temperature: $\mathrm{CaC_2 + N_2 \xrightarrow{\Delta} CaCN_2 + C}$.
2. The true product is calcium cyanamide $\mathrm{CaCN_2}$ (anion $\mathrm{[N{=}C{=}N]^{2-}}$), which none of the four options shows exactly.
3. $\mathrm{CaCN}$, $\mathrm{CaCN_3}$ and $\mathrm{Ca_2CN}$ are not charge-balanced calcium compounds; $\mathrm{Ca(CN)_2}$ is a real Ca-C-N salt, so the best pick is option $1$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q071_833e950a_28102026.png?v=833e950a8b2b)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q071_46fa58f5_28102026.png?v=46fa58f5fcf3)

---

## Q72

Chemistry · physical · Chemical Equilibrium

Consider the following liquid – vapour equilibrium.
$\mathrm{Liquid} \rightleftharpoons \mathrm{Vapour}$
Which of the following relations is correct?

- (1) $\dfrac{d\ln G}{dT^{2}} = \dfrac{\Delta H_{\upsilon}}{RT^{2}}$
- (2) $\dfrac{d\ln P}{dT} = \dfrac{-\Delta H_{\upsilon}}{RT}$
- (3) $\dfrac{d\ln P}{dT^{2}} = \dfrac{-\Delta H_{\upsilon}}{T^{2}}$
- **(4)** $\dfrac{d\ln P}{dT} = \dfrac{\Delta H_{\upsilon}}{RT^{2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{P} = \mathrm{K}e^{-\Delta \mathrm{H}/\mathrm{RT}}$
2. $\ln \mathrm{P} = \ln \mathrm{K} - \frac{\Delta \mathrm{H}}{\mathrm{RT}}$
3. $\frac{d}{d\mathrm{T}}\ln \mathrm{P} = \frac{\Delta \mathrm{H}_{\upsilon}}{\mathrm{RT}^{2}}$
4. $\therefore \frac{d\ln \mathrm{P}}{d\mathrm{T}} = \frac{\Delta \mathrm{H}_{\upsilon}}{\mathrm{RT}^{2}}$

**Solved independently** (answer withheld)

1. For a phase equilibrium, the Clapeyron equation gives $\frac{dP}{dT} = \frac{\Delta H_v}{T\,\Delta V}$.
2. Neglect the liquid volume and treat the vapour as ideal: $\Delta V \approx V_g = \frac{RT}{P}$.
3. Substitute: $\frac{dP}{dT} = \frac{P\,\Delta H_v}{RT^2}$, so $\frac{d\ln P}{dT} = \frac{\Delta H_v}{RT^2}$, which is option $4$.

**Subtopic:** Temperature Dependence of the Equilibrium Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q072_cc6bce08_28102026.png?v=cc6bce084949)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q072_82c0a6c4_28102026.png?v=82c0a6c40f78)

---

## Q73

Chemistry · inorganic · The p–Block Elements

Match the compounds given in column I with the hybridization and shape given in column II and mark the correct option.

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{XeF_6}$ | (i) | Distorted octahedral |
| (b) | $\mathrm{XeO_3}$ | (ii) | Square planar |
| (c) | $\mathrm{XeOF_4}$ | (iii) | Pyramidal |
| (d) | $\mathrm{XeF_4}$ | (iv) | Square pyramidal |

- **(1)** (a) (i), (b) (iii), (c) (iv), (d) (ii)
- (2) (a) (i), (b) (ii), (c) (iv), (d) (iii)
- (3) (a) (iv), (b) (iii), (c) (i), (d) (ii)
- (4) (a) (iv), (b) (i), (c) (ii), (d) (iii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Molecule | Hybridization | Shape as per VSEPR Theory
2. 1 | $\mathrm{XeF_6}$ | $sp^{3}d^{3}$ | Distored octahedron
3. 2 | $\mathrm{XeO_3}$ | $sp^{3}$ | Pyramidal
4. 3 | $\mathrm{XeOF_4}$ | $sp^{3}d^{2}$ | Square Pyramidal
5. 4 | $\mathrm{XeF_4}$ | $sp^{3}d^{2}$ | Square planar

**Solved independently** (answer withheld)

1. $\mathrm{XeF_6}$: 6 bond pairs and 1 lone pair, $sp^3d^3$, so distorted octahedral, (a) $\to$ (i).
2. $\mathrm{XeO_3}$: 3 bond pairs and 1 lone pair, $sp^3$, so pyramidal, (b) $\to$ (iii).
3. $\mathrm{XeOF_4}$: 5 bond pairs and 1 lone pair, $sp^3d^2$, so square pyramidal, (c) $\to$ (iv).
4. $\mathrm{XeF_4}$: 4 bond pairs and 2 lone pairs, $sp^3d^2$, so square planar, (d) $\to$ (ii).
5. The match (a)(i), (b)(iii), (c)(iv), (d)(ii) is option $1$.

**Subtopic:** Important Compounds of Xenon · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q073_19c53565_28102026.png?v=19c53565f03f)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q073_5217013d_28102026.png?v=5217013d917c)

---

## Q74

Chemistry · inorganic · Coordination Compounds – Practice

Which of the following has longest $\mathrm{C-O}$ bond length? (Free $\mathrm{C-O}$ bond length in $\mathrm{CO}$ is $1.128\,\text{Å}$).

- (1) $\mathrm{Ni(CO)_4}$
- (2) $\mathrm{[Co(CO)_4]^{\ominus}}$
- **(3)** $\mathrm{[Fe(CO)_4]^{2-}}$
- (4) $\mathrm{[Mn(CO)_6]^{+}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Metal carbon bond in metal carbonyls possess both $\sigma$ and $\pi$ character.
2. $\mathrm{M-C}$ $\pi$ bond is formed by donation of a pair of electrons from filled orbital of metal into vacant antibonding $\pi$ orbital of $\mathrm{CO}$.
3. $\mathrm{CO}$ bond length increases if $\mathrm{M}$ has more tendency to donate lone pair by metal more $\mathrm{CO}$ bond length.

**Solved independently** (answer withheld)

1. In metal carbonyls the metal donates $d\pi$ electrons into the $\pi^*$ orbital of CO (synergic back-bonding), which lowers the $\mathrm{C-O}$ bond order and lengthens the bond.
2. Oxidation states of the metals: $\mathrm{Ni}(0)$ in $\mathrm{Ni(CO)_4}$, $\mathrm{Co}(-1)$ in $\mathrm{[Co(CO)_4]^{-}}$, $\mathrm{Fe}(-2)$ in $\mathrm{[Fe(CO)_4]^{2-}}$, $\mathrm{Mn}(+1)$ in $\mathrm{[Mn(CO)_6]^{+}}$.
3. Electron richness of the metal, and so the extent of back-donation, follows $\mathrm{Fe}^{2-} > \mathrm{Co}^{-} > \mathrm{Ni}^{0} > \mathrm{Mn}^{+}$.
4. Hence the $\mathrm{C-O}$ bond is longest in $\mathrm{[Fe(CO)_4]^{2-}}$, which is option $3$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q074_7a5c2e7f_28102026.png?v=7a5c2e7ffb25)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q074_4e9b605f_28102026.png?v=4e9b605f3dd8)

---

## Q75

Chemistry · physical · Electrochemistry

The pressure of $\mathrm{H_2}$ required to make the potential of $\mathrm{H_2}$ – electrode zero in pure water at $298\,\mathrm{k}$ is:

- **(1)** $10^{-14}\,\mathrm{atm}$
- (2) $10^{-12}\,\mathrm{atm}$
- (3) $10^{-10}\,\mathrm{atm}$
- (4) $10^{-4}\,\mathrm{atm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Pt},\frac{\mathrm{H_{2(g)}}}{\mathrm{H^{+}}}$ Hydrogen electrode $\mathrm{E^{o}_{H_2/H^{+}}} = 0.0\,\mathrm{Volt}$
2. $\mathrm{H_{2(g)}} \rightarrow 2\mathrm{H^{+}_{(aq)}} + 2\mathrm{e^{-}}$
3. $[\mathrm{H^{+}}] = 10^{-7}\,\mathrm{M}$ at $25^{\mathrm{o}}\mathrm{C}$ (for Pure water)
4. $\mathrm{E} = \frac{-0.0591}{2}\log\left(\frac{[\mathrm{H^{+}}]^{2}}{\mathrm{P_{H_2}}}\right)$
5. $\mathrm{E} = 0 = \log\frac{[\mathrm{H^{+}}]}{\mathrm{P_{H_2}}} = 0$
6. $\therefore [\mathrm{H^{+}}]^{2} = \mathrm{P_{H_2}}$
7. $\therefore \mathrm{P_{H_2}} = 10^{-14}\,\mathrm{atm}$

**Solved independently** (answer withheld)

1. Electrode reaction: $2\mathrm{H^+} + 2e^- \rightarrow \mathrm{H_2}$, with $E^\circ = 0$.
2. Nernst equation: $E = E^\circ - \frac{0.0591}{2}\log\frac{P_{\mathrm{H_2}}}{[\mathrm{H^+}]^2}$.
3. In pure water at $298\,\mathrm{K}$, $[\mathrm{H^+}] = 10^{-7}\,\mathrm{M}$, so $[\mathrm{H^+}]^2 = 10^{-14}$.
4. For $E = 0$ the log term must vanish: $\frac{P_{\mathrm{H_2}}}{10^{-14}} = 1$.
5. $P_{\mathrm{H_2}} = 10^{-14}\,\mathrm{atm}$, which is option $1$.

**Subtopic:** Nernst Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q075_92a492d3_28102026.png?v=92a492d38592)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q075_70f04cfa_28102026.png?v=70f04cfa102b)

---

## Q76

Chemistry · physical · Chemical Kinetics

The addition of a catalyst during a chemical reaction alters which of the following quantities?

- (1) Entropy
- (2) Internal energy
- (3) Enthalpy
- **(4)** Activation energy

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Catalyst is going to affect the activation energy of a chemical reaction.
2. Activation energy is the minimum energy required to from activated complex or Transition state.

**Solved independently** (answer withheld)

1. A catalyst provides an alternative pathway of lower activation energy $E_a$, while $\Delta H$, $\Delta U$ and $\Delta S$ are state functions independent of path and stay unchanged, so the answer is option $4$.

**Subtopic:** Effect of Catalyst · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q076_040f2cd6_28102026.png?v=040f2cd68ab8)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q076_e6eff92b_28102026.png?v=e6eff92b3d7b)

---

## Q77

Chemistry · physical · The Solid State

The ionic radii of $A^{+}$ and $B^{-}$ ions are $0.98 \times 10^{-10}\,m$ and $1.81 \times 10^{-10}\,m$. The coordination number of each ion in AB is

- **(1)** 6
- (2) 4
- (3) 8
- (4) 2

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Radius ratio of $\left(\frac{A^{+}}{B^{-}}\right) = \frac{0.98 \times 10^{-10}\,m}{1.81 \times 10^{-10}\,m} = \frac{0.98}{1.81} = 0.541$
2. If the radius ratio is between $0.414$ and $0.732$ then Co-ordination number is $6$.

**Solved independently** (answer withheld)

1. Radius ratio: $\frac{r_{+}}{r_{-}} = \frac{0.98 \times 10^{-10}\,m}{1.81 \times 10^{-10}\,m} \approx 0.541$.
2. The range $0.414 < \frac{r_{+}}{r_{-}} < 0.732$ corresponds to octahedral coordination.
3. Octahedral coordination means each ion has coordination number $6$, which is option $1$.

**Subtopic:** Radius Ratio Rule and Coordination Number in Ionic Solids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q077_f6fe80d4_28102026.png?v=f6fe80d48eac)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q077_4bea5192_28102026.png?v=4bea5192784d)

---

## Q78

Chemistry · inorganic · The p–Block Elements

Which is the correct statement for the given acids?

- (1) Phosphinic acid is a diprotic acid while phosphonic acid is a monoprotic acid.
- **(2)** Phosphinic acid is a monoprotic acid while phosphonic acid is a diprotic acid.
- (3) Both are triprotic acids
- (4) Both are diprotic acids

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Phosphinic acid is Hypophosphorous acid $\mathrm{H_3PO_2}$ which is Monobasic acid.
2. Phosphonic acid is phosphorous acid $\mathrm{H_3PO_3}$ which is Dibasic acid.

**Solved independently** (answer withheld)

1. Only H atoms bonded to O (P$-$OH) are ionisable; P$-$H hydrogens are not acidic.
2. Phosphinic (hypophosphorous) acid $\mathrm{H_3PO_2} = \mathrm{H_2P(=O)OH}$ has one P$-$OH, so it is monoprotic.
3. Phosphonic (phosphorous) acid $\mathrm{H_3PO_3} = \mathrm{HP(=O)(OH)_2}$ has two P$-$OH, so it is diprotic.
4. Phosphinic monoprotic, phosphonic diprotic, which is option $2$.

**Subtopic:** Important Compounds and Oxyacids of Phosphorus · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q078_9983d0b6_28102026.png?v=9983d0b63117)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q078_9cdcd78a_28102026.png?v=9cdcd78a6485)

---

## Q79

Chemistry · physical · Surface Chemistry

Fog is a colloidal solution of:

- **(1)** Liquid in gas
- (2) Gas in liquid
- (3) Solid in gas
- (4) Gas in gas

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fog is a colloidal solution in which liquid droplets are dispersed in gas.

**Solved independently** (answer withheld)

1. In fog, the dispersed phase is tiny liquid water droplets and the dispersion medium is air (a gas), so fog is an aerosol of liquid in gas, which is option $1$.

**Subtopic:** Classification of Colloids by Dispersed Phase and Dispersion Medium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q079_27877436_28102026.png?v=27877436af5f)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q079_60e115f6_28102026.png?v=60e115f6fb78)

---

## Q80

Chemistry · physical · Solutions

Which of the following statements about the composition of the vapour over an ideal $1:1$ molar mixture of benzene and toluene is correct? Assume that the temperature is constant at $25^{o}C$. (Given vapour pressure data at $25^{o}C$, benzene = $12.8\,\mathrm{kPa}$, toluene = $3.85\,\mathrm{kPa}$)

- **(1)** The vapour will contain a higher percentage of benzene.
- (2) The vapour will contain a higher percentage of toluene.
- (3) The vapour will contain equal amounts of benzene and toluene.
- (4) Not enough information is given to make a prediction.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $A$ – benzene, $B$ – Toluene
2. $P_T = P_A^{o}\,X_A + P_B^{o}\,X_B$
3. $= 12.8 \times 0.5 + 3.85 \times 0.5$
4. $= 6.2 + 1.925$
5. $= 8.125$
6. Also, mole fraction of benzene in vapour form
7. $Y_A = \frac{P_A^{o}\,X_A}{P_T} = \frac{6.2}{8.121} = 0.75$
8. And mole fraction of Toluene in vapour form
9. $Y_B = 1 - 0.75 = 0.25$

**Solved independently** (answer withheld)

1. For a $1:1$ molar mixture, $x_B = x_T = 0.5$.
2. Raoult's law: $p_B = x_B p_B^0 = 0.5 \times 12.8 = 6.4\,\mathrm{kPa}$.
3. $p_T = x_T p_T^0 = 0.5 \times 3.85 = 1.925\,\mathrm{kPa}$.
4. $P_{total} = 6.4 + 1.925 = 8.325\,\mathrm{kPa}$.
5. Dalton's law: $y_B = \frac{p_B}{P_{total}} = \frac{6.4}{8.325} \approx 0.77$, so $y_T \approx 0.23$.
6. The vapour is richer in benzene, which is option $1$.

**Subtopic:** Vapour Pressure of Liquid Solutions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q080_b9a4a100_28102026.png?v=b9a4a1005416)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q080_719109e2_28102026.png?v=719109e20367)

---

## Q81

Chemistry · organic · Hydrocarbons

The correct statement regarding the comparison of staggered and eclipsed conformations of ethane, is:

- (1) The staggered conformation of ethane is less stable than eclipsed conformation, because staggered conformation has torsional strain.
- (2) The eclipsed conformation of ethane is more stable than staggered conformation, because eclipsed conformation has no torsional strain.
- (3) The eclipsed conformation of ethane is more stable than staggered conformation even though the eclipsed conformation has torsional strain.
- **(4)** The staggered conformation of ethane is more stable than eclipsed conformation, because staggered conformation has no torsional strain.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CH_3 - CH_3}$

![printed figure: Newman projections of ethane: Eclipsed (front and rear C-H bonds aligned); Staggeredform (Morestable) (rear C-H bonds at 60° to the front ones)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q081_sol_1_09a74b09_28102026.png?v=09a74b09d201)

*Newman projections of ethane: Eclipsed (front and rear C-H bonds aligned); Staggeredform (Morestable) (rear C-H bonds at 60° to the front ones)*


**Solved independently** (answer withheld)

1. In the staggered conformation of ethane the $\mathrm{C{-}H}$ bonds on the two carbons are at a dihedral angle of $60^\circ$, so bond-pair repulsion is minimum and there is no torsional strain.
2. In the eclipsed conformation the dihedral angle is $0^\circ$, so repulsion is maximum and it has torsional strain (about $12.5\,\mathrm{kJ\,mol^{-1}}$ higher in energy).
3. Hence the staggered form is more stable than the eclipsed form because it has no torsional strain, which is option $4$.

**Subtopic:** Isomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q081_de31b869_28102026.png?v=de31b86932a5)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q081_4aeb502b_28102026.png?v=4aeb502b2c75)

---

## Q82

Chemistry · organic · Alcohols, Phenols and Ethers

The reaction [figure] Can be classified as:

![printed figure: cyclopentanol →(NaH) sodium cyclopentanolate →(Me - I) methoxycyclopentane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q082_e4d7a664_28102026.png?v=e4d7a66449a2)

*cyclopentanol →[NaH] sodium cyclopentanolate →[Me - I] methoxycyclopentane*

Structures: cyclopentanol `OC1CCCC1`; sodium cyclopentanolate `[Na+].[O-]C1CCCC1`; methoxycyclopentane `COC1CCCC1`

- **(1)** Williamson ether synthesis reaction
- (2) Alcohol formation reaction
- (3) Dehydration reaction
- (4) Williamson alcohol synthesis reaction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: cyclopentanol →(NaH) sodium cyclopentanolate (Ō: Na⁺) →(Me-I) methoxycyclopentane (O—Me); Williamson synthesis; Ether formation](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q082_sol_1_a1dbdb23_28102026.png?v=a1dbdb23a256)

*cyclopentanol →[NaH] sodium cyclopentanolate (Ō: Na⁺) →[Me-I] methoxycyclopentane (O—Me); Williamson synthesis; Ether formation*


**Solved independently** (answer withheld)

1. NaH removes the hydroxyl proton: $\mathrm{C_5H_9OH + NaH \rightarrow C_5H_9O^{-}Na^{+} + H_2}$.
2. The alkoxide attacks methyl iodide by $S_N2$: $\mathrm{C_5H_9O^{-}Na^{+} + CH_3I \rightarrow C_5H_9OCH_3 + NaI}$.
3. Alkoxide plus alkyl halide giving an ether is the Williamson ether synthesis, which is option $1$.

**Subtopic:** Preparation of Ethers by Williamson Ether Synthesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q082_d529fe9c_28102026.png?v=d529fe9c5bf9)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q082_3fe998dc_28102026.png?v=3fe998dc889c)

---

## Q83

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The product formed by the reaction of an aldehyde with a primary amine is:

- **(1)** Schiff base
- (2) Ketone
- (3) Carboxylic acid
- (4) Aromatic acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $>\mathrm{C}=\mathrm{O} + \mathrm{R}-\mathrm{NH_2} \rightarrow\ \underset{\text{Schiff base}}{>\mathrm{C}=\mathrm{N}-\mathrm{R}}$

**Solved independently** (answer withheld)

1. Nucleophilic addition of the primary amine to the carbonyl, then loss of water: $\mathrm{RCHO} + \mathrm{R'NH_2} \rightarrow \mathrm{RCH{=}NR'} + \mathrm{H_2O}$; the imine product is a Schiff base, option $1$.

**Subtopic:** Reactions with Ammonia and Decarboxylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q083_5a839757_28102026.png?v=5a839757f459)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q083_e944f687_28102026.png?v=e944f68724d6)

---

## Q84

Chemistry · organic · Isomerism in Organic Compounds

Which of the following biphenyls is optically active?

- (1) 1-iodo-3-(3-nitrophenyl)benzene `O=[N+]([O-])c1cccc(-c2cccc(I)c2)c1`
- **(2)** 1-bromo-2-(2-bromo-6-iodophenyl)-3-iodobenzene `Brc1cccc(I)c1-c1c(Br)cccc1I`
- (3) 1-iodo-2-(2-iodophenyl)benzene `Ic1ccccc1-c1ccccc1I`
- (4) 1,3-dimethyl-2-phenylbenzene `Cc1cccc(C)c1-c1ccccc1`

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: 2,2'-dibromo-6,6'-diiodobiphenyl (1-bromo-2-(2-bromo-6-iodophenyl)-3-iodobenzene) with a curved arrow from the central C-C bond labelled: restricted rotation around bond](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q084_sol_1_662ce0c1_28102026.png?v=662ce0c1814c)

*2,2'-dibromo-6,6'-diiodobiphenyl (1-bromo-2-(2-bromo-6-iodophenyl)-3-iodobenzene) with a curved arrow from the central C-C bond labelled: restricted rotation around bond*

1. Is optically active (Non super imposable on its mirror image)

**Solved independently** (answer withheld)

1. A biphenyl is optically active (atropisomerism) only if bulky ortho groups block rotation about the central $C\!-\!C$ bond and neither ring carries two identical ortho groups.
2. Option $1$: the $NO_2$ and $I$ groups are meta, so rotation is free and the molecule is not resolvable.
3. Option $2$: both rings carry ortho $Br$ and ortho $I$, so all four ortho positions are blocked and each ring is unsymmetrically substituted; the twisted molecule has no plane of symmetry and is chiral.
4. Option $3$: only one ortho $I$ on each ring, so the rotation barrier is too low for stable enantiomers.
5. Option $4$: one ring has two identical ortho $CH_3$ groups and the other ring is unsubstituted, giving a plane of symmetry, so it is achiral.
6. Hence the optically active biphenyl is option $2$.

**Subtopic:** Optical Isomerism · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 41)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q084_61e951f6_28102026.png?v=61e951f63e26)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q084_778e30f7_28102026.png?v=778e30f7686c)

---

## Q85

Chemistry · organic · Haloalkanes and Haloarenes

For the following reactions: a. $\mathrm{CH_3CH_2CH_2Br + KOH \rightarrow CH_3CH=CH_2 + KBr + H_2O}$ b. c. Which of the following statements is correct?

![printed figure: 2-bromopropane + $\ce{KOH}$ → propan-2-ol + $\ce{KBr}$; cyclohexene + $\ce{Br2}$ → 1,2-dibromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q085_901403fb_28102026.png?v=901403fbba8c)

*2-bromopropane + $\ce{KOH}$ → propan-2-ol + $\ce{KBr}$; cyclohexene + $\ce{Br2}$ → 1,2-dibromocyclohexane*

Structures: 2-bromopropane `CC(C)Br`; potassium hydroxide `[K+].[OH-]`; propan-2-ol `CC(C)O`; potassium bromide `[Br-].[K+]`; cyclohexene `C1=CCCCC1`; dibromine `BrBr`; 1,2-dibromocyclohexane `BrC1CCCCC1Br`

- (1) a and b are elimination reactions and c is addition reaction.
- **(2)** a is elimination, b is substitution and c is addition reaction.
- (3) a is elimination, b and c are substitution reactions.
- (4) a is substitution, b and c are addition reactions.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. a] $\mathrm{CH_3CH_2CH_2Br + KOH \rightarrow CH_3CH=CH_2 + KBr + H_2O}$ (Elimination)
2. b]

![printed figure: 2-bromopropane → propan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q085_sol_1_1a41007d_28102026.png?v=1a41007d572b)

*2-bromopropane → propan-2-ol*

3. (substitution)
4. c]

![printed figure: cyclohexene + $\ce{Br2}$ → 1,2-dibromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q085_sol_2_8a041c03_28102026.png?v=8a041c036682)

*cyclohexene + $\ce{Br2}$ → 1,2-dibromocyclohexane*

5. (addition)

**Solved independently** (answer withheld)

1. In a, $\mathrm{CH_3CH_2CH_2Br}$ loses $\mathrm{HBr}$ to give the alkene $\mathrm{CH_3CH=CH_2}$, so a is an elimination reaction.
2. In b, $\mathrm{(CH_3)_2CHBr + KOH \rightarrow (CH_3)_2CHOH + KBr}$: $\mathrm{-Br}$ is replaced by $\mathrm{-OH}$, so b is a substitution reaction.
3. In c, $\mathrm{Br_2}$ adds across the $\mathrm{C=C}$ of cyclohexene to give 1,2-dibromocyclohexane, so c is an addition reaction.
4. a elimination, b substitution, c addition matches option $2$.

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions, Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q085_538b3f91_28102026.png?v=538b3f91b2ba)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q085_9c67a289_28102026.png?v=9c67a2897d41)

---

## Q86

Chemistry · physical · Solutions

At $100^{o}C$ the vapour pressure of a solution of $6.5\,\mathrm{g}$ of a solute in $100\,\mathrm{g}$ water is $732\,\mathrm{mm}$. If $K_b = 0.52$, the boiling point of this solution will be:

- **(1)** $101^{o}C$
- (2) $100^{o}C$
- (3) $102^{o}C$
- (4) $103^{o}C$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At $100^{o}C$ (boiling point)
2. Vapour pressure of water $P^{o} = P_{atm} = 760\,ml$
3. $\therefore \frac{P^{o} - \mathrm{P_s}}{\mathrm{P^o}} = \mathrm{X_{solute}}$
4. $\Rightarrow \frac{760 - 732}{760} = \frac{\mathrm{n_{solute}}}{\mathrm{n_{solvent}}}$
5. $\Rightarrow \frac{28}{760} = \frac{6.5/\mathrm{m}}{100/18}$
6. $\Rightarrow \mathrm{m} = \frac{6.5 \times 18 \times 760}{28 \times 100} \approx 32$
7. Now,
8. $\Delta \mathrm{T_b} = \mathrm{K_b}\ \mathrm{molality}$
9. $= 0.52 \times \frac{6.5/32}{0.1}$
10. $= \frac{0.52 \times 6.5}{32 \times 0.1}$
11. $= 1.05 \approx 1\mathrm{s}$
12. $\therefore$ Boiling point of solution $= 100 + 1 = 101^{\mathrm{o}}\mathrm{C}$

**Solved independently** (answer withheld)

1. At $100^{o}C$ pure water has $P^0 = 760\,\mathrm{mm}$, so $\Delta P = 760 - 732 = 28\,\mathrm{mm}$.
2. $\frac{\Delta P}{P^0} = \frac{28}{760} = 0.0368 \approx \frac{n_2}{n_1}$ for a dilute solution.
3. $n_1 = \frac{100}{18} = 5.556\,\mathrm{mol}$, so $n_2 = 0.0368 \times 5.556 = 0.205\,\mathrm{mol}$.
4. Molality $m = \frac{0.205}{0.1\,\mathrm{kg}} = 2.05\,\mathrm{mol\,kg^{-1}}$.
5. $\Delta T_b = K_b m = 0.52 \times 2.05 = 1.06\,\mathrm{K}$.
6. $T_b = 100 + 1.06 \approx 101^{o}C$, which is option $1$.

**Subtopic:** Elevation of Boiling Point, Relative Lowering of Vapour Pressure · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 43)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q086_71d25995_28102026.png?v=71d259951ec8)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q086_d6de9ab9_28102026.png?v=d6de9ab9d6ca)

---

## Q87

Chemistry · organic · Biomolecules

The correct statement regarding RNA and DNA, respectively is:

- (1) The sugar component in RNA is arabinose and the sugar component in DNA is 2’-deoxyribose.
- **(2)** The sugar component in RNA is ribose and the sugar component in DNA is 2’-deoxyribose.
- (3) The sugar component in RNA is arabinose and the sugar component in DNA is ribose.
- (4) The sugar component in RNA is 2’-deoxyribose and the sugar component in DNA is arabinose.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: beta-D-ribofuranose (Haworth projection)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q087_sol_1_2a95421c_28102026.png?v=2a95421c699b)

*beta-D-ribofuranose (Haworth projection)*

1. $\beta$-D-ribose Sugar component of RNA

![printed figure: 2-deoxy-beta-D-ribofuranose (Haworth projection)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q087_sol_2_57578e49_28102026.png?v=57578e494bb1)

*2-deoxy-beta-D-ribofuranose (Haworth projection)*

2. $\beta$-D-2deoxyribose Sugar component of DNA

**Solved independently** (answer withheld)

1. RNA nucleotides contain the pentose $\text{ribose}$ and DNA nucleotides contain $2'\text{-deoxyribose}$ (no $-OH$ at $C_{2'}$), so the correct pair is option $2$.

**Subtopic:** Structure and Function of Nucleic Acids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q087_3e128a30_28102026.png?v=3e128a305d23)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q087_0d2b8836_28102026.png?v=0d2b8836e9cf)

---

## Q88

Chemistry · organic · Amines

The correct statement regarding the basicity of aryl amines is:

- **(1)** Aryl amines are generally less basic than alkyl amines because the nitrogen lone-pair electrons are delocalized by interaction with the aromatic ring $\pi$ electron system.
- (2) Aryl amines are generally more basic than alkyl amines because the nitrogen lone-pair electrons are not delocalized by interaction with the aromatic ring $\pi$ electron system.
- (3) Aryl amines are generally more basic than alkyl amines because of aryl group.
- (4) Aryl amines are generally more basic than alkyl amines, because the nitrogen atom in aryl amines is sp-hybridized.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: aniline (lone pair drawn on N)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q088_sol_1_5d44666f_28102026.png?v=5d44666fa828)

*aniline (lone pair drawn on N)*

1. Here lone pair is in conjugation with double bond so basic strength decreased
2. $\mathrm{R-\ddot{N}H_2}$ (No conjugation)

**Solved independently** (answer withheld)

1. In an aryl amine ($\mathrm{C_6H_5NH_2}$) the nitrogen lone pair takes part in resonance with the aromatic ring $\pi$ electron system, so it is delocalized and less available to accept a proton.
2. In alkyl amines the alkyl group's $+I$ effect increases electron density on nitrogen, so the lone pair is more available and they are more basic.
3. Hence aryl amines are less basic than alkyl amines because of lone-pair delocalization, which is option $1$; options $2$, $3$ and $4$ wrongly claim aryl amines are more basic (and nitrogen in aryl amines is not $sp$-hybridized).

**Subtopic:** Chemical Reactions of Amines (Basicity, Alkylation and Acylation) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q088_63881051_28102026.png?v=63881051e740)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q088_e9cdd13c_28102026.png?v=e9cdd13c9552)

---

## Q89

Chemistry · organic · Biomolecules

Which one given below is a non-reducing sugar?

- (1) Maltose
- (2) Lactose
- (3) Glucose
- **(4)** Sucrose

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Haworth structure of the disaccharide with its glucose ring labelled α -D-glucose and its fructose ring labelled β -D-Fructose, joined through O: (2S,3R,4S,5S,6R)-2-((2S,3S,4S,5R)-3,4-dihydroxy-2,5-bis(hydroxymethyl)oxolan-2-yl)oxy-6-(hydroxymethyl)oxane-2,3,4,5-tetrol (sucrose as printed, with OH drawn on glucose C-1)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q089_sol_1_68322de9_28102026.png?v=68322de97167)

*Haworth structure of the disaccharide with its glucose ring labelled α -D-glucose and its fructose ring labelled β -D-Fructose, joined through O: (2S,3R,4S,5S,6R)-2-[(2S,3S,4S,5R)-3,4-dihydroxy-2,5-bis(hydroxymethyl)oxolan-2-yl]oxy-6-(hydroxymethyl)oxane-2,3,4,5-tetrol (sucrose as printed, with OH drawn on glucose C-1)*

1. Glycosidic bond involves reducing groups.
2. Sucrose (No reducing sugar)

**Solved independently** (answer withheld)

1. A sugar is reducing only if it has a free anomeric (hemiacetal) carbon that can open to an aldehyde or ketone group.
2. Glucose has a free aldehyde group, maltose ($\alpha$-1,4 glucose-glucose) and lactose ($\beta$-1,4 galactose-glucose) each keep one free anomeric carbon, so all three are reducing.
3. In sucrose the glycosidic bond joins glucose $C_1$ to fructose $C_2$, so both anomeric carbons are tied up and sucrose is non-reducing, which is option $4$.

**Subtopic:** Disaccharides: Sucrose, Maltose and Lactose · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q089_c63596c1_28102026.png?v=c63596c1f9fb)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q089_611642c3_28102026.png?v=611642c31bfa)

---

## Q90

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The pair of electron in the given carbanion, $\mathrm{CH_3C\equiv C^{\ominus}}$ is present in which of the following orbitals?

- (1) $2p$
- (2) $sp^3$
- (3) $sp^2$
- **(4)** $sp$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CH_3-C\equiv C^{\ominus}}$: In the carbanian the carbon is having $1$ sigma bond, $2\pi$ bonds and $1$ lone pair
2. therefore $\mathrm{C}$ is $sp$ hybridized.

**Solved independently** (answer withheld)

1. The anionic carbon in $\mathrm{CH_3C\equiv C^{\ominus}}$ forms one $\sigma$ bond and two $\pi$ bonds to the adjacent carbon and carries one lone pair.
2. Its $\sigma$ framework has $2$ domains (one $\sigma$ bond and the lone pair), so the carbon is $sp$ hybridised, with its two $2p$ orbitals used in the $\pi$ bonds.
3. The lone pair therefore occupies an $sp$ hybrid orbital, which is option $4$.

**Subtopic:** Hybridisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q090_81dab52a_28102026.png?v=81dab52a8b16)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q090_2d1fb11a_28102026.png?v=2d1fb11a7beb)

---

## Q91

Biology · botany · Organisms and Populations

Gause's principle of competitive exclusion states that:

- (1) More abundant species will exclude the less abundant species through competition
- (2) Competition for the same resources excludes species having different food preferences
- **(3)** No two species can occupy the same niche indefinitely for the same limiting resources
- (4) Larger organisms exclude smaller ones through competition

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Gause’s principle of competitive exclusion states that no two species can occupy the same niche indefinitely for the same limiting resources.

**Solved independently** (answer withheld)

1. Gause's competitive exclusion principle states that two closely related species competing for the same limiting resources cannot coexist indefinitely, so no two species can occupy the same niche indefinitely for the same limiting resources, which is option $3$.

**Subtopic:** Competition · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q091_56f0eb3c_28102026.png?v=56f0eb3c2a21)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q091_3796339b_28102026.png?v=3796339ba078)

---

## Q92

Biology · both · Biotechnology and Its Applications

The two polypeptides of human insulin are linked together by:

- (1) Hydrogen bonds
- (2) Phosphodiester bond
- (3) Covalent bond
- **(4)** Disulphide bridges

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The human insulin has two polypeptide chains A and B linked together by disulphide bridges.

**Solved independently** (answer withheld)

1. Human insulin is made of two polypeptide chains, $A$ and $B$, which are linked together by inter-chain disulphide bridges ($-S-S-$), which is option $4$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q092_57ba172c_28102026.png?v=57ba172c8389)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q092_e2279d51_28102026.png?v=e2279d51dd9b)

---

## Q93

Biology · botany · Sexual Reproduction in Flowering Plants

The coconut water from tender coconut represents:

- (1) Endocarp
- (2) Fleshy mesocarp
- (3) Free nuclear proembryo
- **(4)** Free nuclear endosperm

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In tender coconuts, the coconut water represents free nuclear endosperm.

**Solved independently** (answer withheld)

1. In coconut the endosperm develops by the free-nuclear method; the coconut water of a tender coconut is this free-nuclear endosperm (the white kernel is cellular endosperm), so the answer is option $4$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q093_6b9c9663_28102026.png?v=6b9c9663ecad)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q093_d04d9e53_28102026.png?v=d04d9e53b330)

---

## Q94

Biology · botany · Biological Classification

Which of the following statements is wrong for viroids?

- (1) They lack a protein coat
- (2) They are smaller than viruses
- (3) They cause infections
- **(4)** Their RNA is of high molecular weight

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In viroids, $\mathrm{RNA}$ is of low molecular weight.

**Solved independently** (answer withheld)

1. Viroids are free RNA lacking a protein coat, smaller than viruses, and cause infections such as potato spindle tuber disease; their RNA is of low molecular weight, so the wrong statement is option $4$.

**Subtopic:** Viroids, Prions & Lichens · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q094_fdf2e4f9_28102026.png?v=fdf2e4f906c2)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q094_1d9057b4_28102026.png?v=1d9057b46a81)

---

## Q95

Biology · zoology · Animal Kingdom

Which of the following features is not present in the Phylum – Arthropoda?

- (1) Chitinous exoskeleton
- (2) Metameric segmentation
- **(3)** Parapodia
- (4) Jointed appendages

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Parapodia is a characteristic of Annelida and it helps in swimming.

**Solved independently** (answer withheld)

1. Arthropods have a chitinous exoskeleton, a metamerically segmented body and jointed appendages, so options $1$, $2$ and $4$ are present; parapodia are the lateral locomotory appendages of annelids such as Nereis, so the absent feature is option $3$.

**Subtopic:** Phylum – Arthropoda · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q095_b43d5f26_28102026.png?v=b43d5f26b839)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q095_47b1bf09_28102026.png?v=47b1bf090caf)

---

## Q96

Biology · both · Principles of Inheritance and Variation

Which of the following most appropriately describes hemophilia?

- (1) Recessive gene disorder
- **(2)** X – linked recessive gene disorder
- (3) Chromosomal disorder
- (4) Dominant gene disorder

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Genes related with hemophilia are always present on X chromosome and it is a recessive gene disorder as it expresses itself in females when it comes a homozygous condition.
2. It causes a defect in the clotting factor formation, thus a simple cut can bleed continuously leading to even death.
3. Thus, it is also known as ‘Bleeders’ disease or ‘Royal Disease’ as Queen Victoria is a carrier for this disease.

**Solved independently** (answer withheld)

1. Haemophilia is caused by a recessive allele carried on the X chromosome, so it is an X-linked recessive gene disorder, which is option $2$.

**Subtopic:** Phenylketonuria & Haemophilia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q096_9815dca2_28102026.png?v=9815dca29eb6)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q096_d027d203_28102026.png?v=d027d203c15d)

---

## Q97

Biology · botany · Photosynthesis in Higher Plants

Emerson’s enhancement effect and Red drop have been instrumental in the discovery of:

- (1) Photophosphorylation and non – cyclic electron transport
- **(2)** Two photosystems operating simultaneously
- (3) Photophosphorylation and cyclic electron transport
- (4) Oxidative phosphorylation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Red drop occurs due decreased functioning of PS-II beyond $680\,\mathrm{nm}$ and when both PS-I and PS-II are functioning together there is enhancement in quantum yield.

**Solved independently** (answer withheld)

1. Red drop: quantum yield of photosynthesis falls sharply for light of wavelength beyond $680\,\text{nm}$.
2. Emerson enhancement: supplying shorter-wavelength light together with far-red light ($>680\,\text{nm}$) gives a rate greater than the sum of the two lights given separately.
3. This shows two photochemical systems (PS I and PS II) operating together, which is option $2$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q097_956cf9f0_28102026.png?v=956cf9f06995)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q097_d712cf9b_28102026.png?v=d712cf9be444)

---

## Q98

Biology · botany · Mineral Nutrition

> ⚠ The printed solution says "None of the options are correct w.r.t. question statement. However, the option (4) seems to be more appropriate than the rest.": the question has no correct option as printed, and the printed answer comes from a corrected reading.

In which of the following, all three are macronutrients?

- (1) Boron, zinc, manganese
- (2) Iron, copper, molybdenum
- (3) Molybdenum, magnesium, manganese
- **(4)** Nitrogen, nickel, phosphorus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Macronutrients are required in greater amount which is $1\,\text{mg-gram}$ of plant dry weight.
2. None of the options are correct w.r.t. question statement. However, the option (4) seems to be more appropriate than the rest.

**Solved independently** (answer withheld)

1. NCERT macronutrients: $\mathrm{C, H, O, N, P, K, S, Ca, Mg}$; micronutrients: $\mathrm{Fe, Mn, Cu, Mo, Zn, B, Cl, Ni}$.
2. Option $1$ (B, Zn, Mn) and option $2$ (Fe, Cu, Mo) are all micronutrients.
3. Option $3$ (Mo, Mg, Mn) has only Mg as a macronutrient.
4. Option $4$ (N, Ni, P) has N and P as macronutrients but Ni is a micronutrient, so no option fully fits; option $4$ is the best available.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q098_2c454f46_28102026.png?v=2c454f46c6a8)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q098_a6a5268d_28102026.png?v=a6a5268d244c)

---

## Q99

Biology · zoology · Breathing and Exchange of Gases

Name the chronic respiratory disorder caused mainly by cigarette smoking:

- **(1)** Emphysema
- (2) Asthma
- (3) Respiratory acidosis
- (4) Respiratory alkalosis

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Emphysema is a chronic respiratory disorder caused due chronic cigarette smoking in which the alveolar walls are damaged due to which the respiratory surface is decreased.

**Solved independently** (answer withheld)

1. Emphysema is a chronic disorder that damages the alveolar walls, reducing the respiratory surface, and it is caused mainly by cigarette smoking, so the answer is option $1$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q099_504c7a39_28102026.png?v=504c7a3922fb)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q099_5a156bc4_28102026.png?v=5a156bc45518)

---

## Q100

Biology · botany · Environmental Issues

A system of rotating crops with legume or grass pasture to improve soil structure and fertility is called:

- **(1)** Ley farming
- (2) Contour farming
- (3) Strip farming
- (4) Shifting agriculture

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ley agriculture helps to increase soil fertility and improve the physical texture of soil.

**Solved independently** (answer withheld)

1. Growing crops in rotation with a period of legume or grass pasture (a ley) to rebuild soil structure and fertility is called ley farming, which is option $1$.

**Subtopic:** Soil Erosion, Desertification and Soil Conservation Practices · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q100_cdad3693_28102026.png?v=cdad36939ed9)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q100_d847aae3_28102026.png?v=d847aae36301)

---

## Q101

Biology · both · Cell: The Unit of Life

Mitochondria and chloroplast are:
Which one of the following options is correct?

- **((i))** Semi – autonomous organelles
- **((ii))** Formed by division of pre – existing organelles and they contain DNA but lack protein synthesizing machinery

- (1) Both (i) and (ii) are correct
- (2) (ii) is true but (i) is false
- **(3)** (i) is true but (ii) is false
- (4) Both (i) and (ii) are false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Mitochondria and chloroplast are semi-autonomous organelles and they have their own ribosomes with help of which they can synthesize protein.

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts have their own circular DNA, $70S$ ribosomes and make some of their own proteins, so they are semi-autonomous: statement (i) is true.
2. They do arise by division of pre-existing organelles and contain DNA, but statement (ii) says they lack protein-synthesizing machinery, which is wrong because they have $70S$ ribosomes: statement (ii) is false.
3. (i) true and (ii) false matches option $3$.

**Subtopic:** Mitochondria, Plastids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q101_7f57ece5_28102026.png?v=7f57ece5fd54)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q101_593c5cdf_28102026.png?v=593c5cdf2362)

---

## Q102

Biology · zoology · Reproductive Health

In context of Amniocentesis, which of the following statement is incorrect?

- (1) It is usually done when a woman is between 14 – 16 weeks pregnant
- (2) It is used for prenatal sex determination
- (3) It can be used for detection of Down syndrome
- **(4)** It can be used for detection of Cleft palate

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Amniocentesis is a medical procedure used in prenatal diagnosis of chromosomal and genetic abnormalities such as Down’s syndrome. Turner’s syndrome, etc.
2. It also helps in prenatal sex determination, hence there is a statutory ban on it to prevent female foeticide.
3. It is done when woman is between $14$ – $16$ weeks pregnant and it does not help in detection of cleft palate.

**Solved independently** (answer withheld)

1. Amniocentesis takes amniotic fluid holding foetal cells, which are cultured and karyotyped.
2. A karyotype shows the sex chromosomes, so options $2$ (prenatal sex determination) and $3$ (Down syndrome, trisomy $21$) are correct uses.
3. It is typically done in the second trimester, around $14$-$16$ weeks, so option $1$ is acceptable.
4. Cleft palate is a structural developmental defect not shown by chromosome analysis, so option $4$ is the incorrect statement.

**Subtopic:** MTP and Amniocentesis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q102_06e4b99e_28102026.png?v=06e4b99e5bef)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q102_da6af445_28102026.png?v=da6af4454075)

---

## Q103

Biology · botany · Photosynthesis in Higher Plants

In a chloroplast the highest number of protons are found in:

- (1) Stroma
- **(2)** Lumen of thylakoids
- (3) Inter membrane space
- (4) Antennae complex

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Photolysis of water occurs in the lumen of thylakoids which has the highest number of protons.

**Solved independently** (answer withheld)

1. Photolysis of water happens on the lumen side of the thylakoid membrane and releases $H^+$ into the lumen; the cytochrome $b_6f$ complex also moves $H^+$ from the stroma into the lumen, and NADP reductase on the stroma side takes $H^+$ out of the stroma. So the proton concentration is highest in the lumen of the thylakoids, which is option $2$.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q103_1e259781_28102026.png?v=1e2597819280)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q103_f2a44f2b_28102026.png?v=f2a44f2b36ec)

---

## Q104

Biology · zoology · Neural Control and Coordination

Photosensitive compound in human eye is made up of:

- (1) Guanosine and Retinol
- **(2)** Opsin and Retinal
- (3) Opsin and Retinol
- (4) Guanosine and Retinol

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rhodopsin which is a photosensitive pigment present in the human eye is made of opsin and retinal.

**Solved independently** (answer withheld)

1. The photosensitive pigments of the human retina (rhodopsin in rods, iodopsins in cones) are made of the protein opsin plus retinal, an aldehyde of vitamin A, as NCERT teaches. Retinol is the alcohol form and is not the chromophore, so the answer is option $2$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q104_d1c0b544_28102026.png?v=d1c0b544a350)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q104_bf10dadc_28102026.png?v=bf10dadcb26e)

---

## Q105

Biology · both · Cell Cycle and Cell Division

Spindle fibres attach on to:

- (1) Telomere of the chromosome
- **(2)** Kinetochore of the chromosome
- (3) Centromere of the chromosome
- (4) Kinetosome of the chromosome

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Kinetochore of chromosomes facilitates the attachment of spindle fibre (chromosomal fibre) and the poles.

**Solved independently** (answer withheld)

1. NCERT teaches that the disc-shaped kinetochores at the surface of the centromere are the sites where spindle fibres attach, so the answer is option $2$.

**Subtopic:** Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q105_7896e23d_28102026.png?v=7896e23d8571)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q105_6a086944_28102026.png?v=6a0869448128)

---

## Q106

Biology · botany · Biodiversity and Conservation

Which is the National Aquatic Animal of India?

- (1) Gangetic shark
- **(2)** River dolphin
- (3) Blue whale
- (4) Sea – horse

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. River Dolphin represents the purity of the holy Ganga as it can only survive in pure and fresh water.

**Solved independently** (answer withheld)

1. The Gangetic river dolphin ($Platanista\ gangetica$) is India's National Aquatic Animal, so the answer is option $2$.

**Subtopic:** National Symbols and Flagship Protected Species of India · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q106_5ecdf80a_28102026.png?v=5ecdf80a5f68)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q106_7cb77b08_28102026.png?v=7cb77b0816c3)

---

## Q107

Biology · both · Molecular Basis of Inheritance

Which of the following is required as inducer(s) for the expression of Lac operon?

- (1) Glucose
- (2) Galactose
- **(3)** Lactose
- (4) Lactose and galactose

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Lac operon becomes active only after inducing lactose as it is a substrate for the enzyme beta-galactosidase and it also regulates the switching on and off of the operon which cannot be done by glucose and galactose.

**Solved independently** (answer withheld)

1. As NCERT teaches, lactose binds the repressor, inactivates it, and the lac operon is transcribed, so lactose is the inducer, which is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q107_1cbd876d_28102026.png?v=1cbd876d5c1c)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q107_5cb003c6_28102026.png?v=5cb003c6f46d)

---

## Q108

Biology · zoology · Chemical Coordination and Integration

Which of the following pairs of hormones are not antagonistic (having opposite effects) to each other?

- (1) Parathormone - Calcitonin
- (2) Insulin - Glucagon
- (3) Aldosterone - Atrial Natriuretic Factor
- **(4)** Relaxin - Inhibin

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Parathormone $\rightarrow$ Increases blood $\mathrm{Ca^{+2}}$ level
2. Calcitonin $\rightarrow$ Decreases blood $\mathrm{Ca^{+2}}$ level
3. Insulin $\rightarrow$ Decreases blood glucose level
4. Glucagon $\rightarrow$ Increases blood glucose level
5. Aldosterone $\rightarrow$ Increases B.P.
6. ANF $\rightarrow$ Decreases B.P.
7. Relaxin $\rightarrow$ Causes pelvic musculature relaxation
8. Inhibin $\rightarrow$ Inhibits FSH

**Solved independently** (answer withheld)

1. Parathormone raises blood $\mathrm{Ca^{2+}}$ and calcitonin lowers it, so this pair is antagonistic.
2. Insulin lowers blood glucose and glucagon raises it, so this pair is antagonistic.
3. Aldosterone causes $\mathrm{Na^{+}}$ and water retention, raising blood pressure, while ANF causes natriuresis and vasodilation, lowering it. This pair is antagonistic.
4. Relaxin relaxes the pelvic ligaments at parturition and inhibin inhibits FSH secretion. Their actions are unrelated, not opposite, so the answer is option $4$.

**Subtopic:** Gonads · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q108_59c530b4_28102026.png?v=59c530b488fa)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q108_85361b76_28102026.png?v=85361b76d7d3)

---

## Q109

Biology · both · Cell: The Unit of Life

Microtubules are the constituents of:

- (1) Cilia, Flagella and Peroxisomes
- **(2)** Spindle fibres, centrioles and cilia
- (3) Centrioles, spindle fibres and chromatin
- (4) Centrosome, Nucleosome and Centrioles

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Peroxisomes is a microbody.
2. Chromatin consists of DNA and proteins and it condenses to form chromosomes.
3. Nucleosome is the basic unit of chromatin.
4. Microtubules are structures present in cilia, flagella, centrioles and spindle fibres.

**Solved independently** (answer withheld)

1. Microtubules form the axoneme of cilia and flagella, the triplet fibrils of centrioles (and hence centrosomes), and the spindle fibres.
2. Peroxisomes are membrane-bound organelles, and chromatin and nucleosomes are DNA wound on histones, so options $1$, $3$ and $4$ each contain a non-microtubule structure.
3. Spindle fibres, centrioles and cilia are all microtubule structures, which is option $2$.

**Subtopic:** Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q109_742e17e3_28102026.png?v=742e17e3dcb9)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q109_311a3f89_28102026.png?v=311a3f890655)

---

## Q110

Biology · both · Cell: The Unit of Life

A complex of ribosomes attached to single strand of RNA is known as:

- **(1)** Polysome
- (2) Polymer
- (3) Polypeptide
- (4) Okazaki fragment

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Many ribosomes are attached to a single strand of mRNA during protein synthesis.
2. This is known as Polysome.

**Solved independently** (answer withheld)

1. Several ribosomes attached to one mRNA strand, translating it at the same time, form a polysome (polyribosome), which is option $1$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q110_78be48db_28102026.png?v=78be48dbeb98)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q110_0a3e7302_28102026.png?v=0a3e7302e611)

---

## Q111

Biology · zoology · Human Reproduction

Fertilization in humans is practically feasible only if:

- (1) The sperms are transported into vagina just after the release of ovum in fallopian tube
- **(2)** The ovum and sperms are transported simultaneously to ampullary – isthmic junction of the fallopian tube
- (3) The ovum and sperms are transported simultaneously to ampullary – isthmic junction of the cervix
- (4) The sperms are transported into cervix within $48$ hrs. of release of ovum in uterus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Fertilization is practically only feasible if the ovum and sperms are transported simultaneously into the ampulla isthmus region of fallopian tube.

**Solved independently** (answer withheld)

1. Fertilization happens in the ampullary-isthmic junction of the fallopian tube, and only when the ovum and sperms reach it at the same time, which is option $2$ (option $3$ puts the junction in the cervix, which is wrong).

**Subtopic:** Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q111_74a32729_28102026.png?v=74a327299136)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q111_88c5c755_28102026.png?v=88c5c75581e9)

---

## Q112

Biology · zoology · Breathing and Exchange of Gases

Asthma may be attributed to:

- (1) Bacterial infection of the lungs
- **(2)** Allergic reaction of the mast cells in the lungs
- (3) Inflammation of the trachea
- (4) Accumulation of fluid in the lung

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Asthma is an allergic reaction characterized by spasm of bronchi muscles because of effect of histamine released by mast cells.

**Solved independently** (answer withheld)

1. Asthma is an allergic disorder in which mast cells in the lungs release mediators such as histamine, causing inflammation and spasm of the bronchi and bronchioles, which matches option $2$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q112_d38f0343_28102026.png?v=d38f0343ab2a)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q112_e2921573_28102026.png?v=e2921573f4aa)

---

## Q113

Biology · botany · Plant Growth and Development

The avena curvature is used for bioassay of:

- (1) ABA
- (2) $\mathrm{GA_3}$
- **(3)** IAA
- (4) Ethylene

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Avena curvature bioassay is done to test the function of $\mathrm{IAA}$.

**Solved independently** (answer withheld)

1. The Avena curvature test measures how much a decapitated oat coleoptile bends when an agar block containing the hormone is placed on one side; this bending is caused by auxin, so it is the bioassay for auxin ($\mathrm{IAA}$), option $3$.

**Subtopic:** Plant Growth & Regulators – Discovery and Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q113_0f3675ce_28102026.png?v=0f3675ced16e)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q113_b3e974be_28102026.png?v=b3e974be7959)

---

## Q114

Biology · botany · Morphology of Flowering Plants

The standard petal of papilionaceous corolla is also called:

- (1) Carina
- (2) Pappus
- **(3)** Vexillum
- (4) Corona

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q114_sol_1_b9bb0a25_28102026.png?v=b9bb0a254215)

1. Papillionaceous corolla.

**Solved independently** (answer withheld)

1. In papilionaceous (vexillary) aestivation the largest posterior petal, the standard, is called the $\text{vexillum}$; the lateral petals are the wings (alae) and the two anterior petals form the keel (carina), so the answer is option $3$.

**Subtopic:** Corolla: Types and Aestivation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q114_b4af3981_28102026.png?v=b4af39813f4d)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q114_13e04442_28102026.png?v=13e04442ae0f)

---

## Q115

Biology · botany · Morphology of Flowering Plants

Tricarpellary, syncarpous gynoecium is found in flowers of:

- **(1)** Liliaceae
- (2) Solanaceae
- (3) Fabaceae
- (4) Poaceae

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Liliaceae family is a monocot family characterized by tricarpellary, syncarpous gynoceium with superior, trilocular ovary with two ovules in each loculus and placentation axile.

**Solved independently** (answer withheld)

1. NCERT gives the Liliaceae gynoecium as tricarpellary, syncarpous, ovary superior and trilocular ($\underline{G}_{(3)}$).
2. Solanaceae is bicarpellary syncarpous ($\underline{G}_{(2)}$) and Fabaceae is monocarpellary ($\underline{G}_{1}$), so options $2$ and $3$ are out.
3. Poaceae is not described in NCERT with this gynoecium, so the answer is Liliaceae, option $1$.

**Subtopic:** Liliaceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q115_f732490d_28102026.png?v=f732490dabc0)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q115_01808189_28102026.png?v=01808189162c)

---

## Q116

Biology · botany · Biological Classification

One of the major components of cell wall of most fungi is:

- **(1)** Chitin
- (2) Peptidoglycan
- (3) Cellulose
- (4) Hemicellulose

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Peptidoglycan – Bacterial cell wall
2. Cellulose and Hemicellulose – Plant cell wall
3. Chitin – Fungal cell wall

**Solved independently** (answer withheld)

1. Most fungi have a cell wall made of chitin and polysaccharides (peptidoglycan is bacterial; cellulose and hemicellulose are plant), so the answer is option $1$.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q116_bd1ef532_28102026.png?v=bd1ef532c6b1)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q116_61fd48ae_28102026.png?v=61fd48aec215)

---

## Q117

Biology · zoology · Human Reproduction

Select the incorrect statement:

- (1) FSH stimulates the sertoli cells which help in spermiogenesis
- (2) LH triggers ovulation in ovary
- **(3)** LH and FSH decrease gradually during the follicular phase
- (4) LH triggers secretion of androgens from the Leydig cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. LH and FSH both increase during follicular phase.

**Solved independently** (answer withheld)

1. In males, FSH acts on the Sertoli cells and stimulates secretion of factors that help in spermiogenesis, so statement $1$ is correct.
2. The mid-cycle LH surge induces rupture of the Graafian follicle, i.e. ovulation, so statement $2$ is correct.
3. LH acts on the Leydig cells and stimulates synthesis and secretion of androgens, so statement $4$ is correct.
4. During the follicular phase the levels of LH and FSH increase gradually (not decrease), so statement $3$ is the incorrect one, which is option $3$.

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 54)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q117_792c3d68_28102026.png?v=792c3d68fb7d)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q117_97c83b7b_28102026.png?v=97c83b7baa0b)

---

## Q118

Biology · both · Cell Cycle and Cell Division

In meiosis crossing over is initiated at:

- **(1)** Pachytene
- (2) Leptotene
- (3) Zygotene
- (4) Diplotene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In pachytene recombination nodule is formed after which crossing over occurs.

**Solved independently** (answer withheld)

1. In NCERT's account of prophase I, leptotene is condensation, zygotene is synapsis (bivalent formation), pachytene is the stage where recombination nodules appear and crossing over between non-sister chromatids takes place, and diplotene shows chiasmata as the synaptonemal complex dissolves; so crossing over is initiated at pachytene, option $1$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q118_d67043ed_28102026.png?v=d67043ed119a)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q118_c108839d_28102026.png?v=c108839d5f6d)

---

## Q119

Biology · both · Principles of Inheritance and Variation

A tall true breeding garden pea plant is crossed with a dwarf true breeding garden pea plant. When the $F_1$ plants were selfed the resulting genotypes were in the ratio

- **(1)** 1 : 2 : 1 :: Tall homozygous : Tall heterozygous : Dwarf
- (2) 1 : 2 : 1 :: Tall heterozygous : Tall homozygous : Dwarf
- (3) 3 : 1 :: Tall : Dwarf
- (4) 3 : 1 :: Dwarf : Tall

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/figures_agent/q119_sol_1_bc4c1dd2_28102026.png?v=bc4c1dd2b935)

1. Phenotypic ratio : tall : dwarf
2. Genotypic ratio : $\mathrm{TT}$ : $\mathrm{Tt}$ : $\mathrm{tt}$
3. $1 : 2 : 1$

**Solved independently** (answer withheld)

1. Parents: true breeding tall $TT$ and dwarf $tt$, so $F_1$ is all $Tt$.
2. Selfing $F_1$: $Tt \times Tt \rightarrow 1\,TT : 2\,Tt : 1\,tt$.
3. $TT$ is tall homozygous, $Tt$ is tall heterozygous, $tt$ is dwarf, so the genotypic ratio is $1:2:1$ in that order, which is option $1$ (3 : 1 is the phenotypic ratio).

**Subtopic:** Monohybrid Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q119_a46d8236_28102026.png?v=a46d823648b3)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q119_0d070dd3_28102026.png?v=0d070dd3f771)

---

## Q120

Biology · botany · Biodiversity and Conservation

Which of the following is the most important cause of animals and plants being driven to extinction ?

- (1) Over – exploitation
- (2) Alien species invasion
- **(3)** Habitat loss and fragmentation
- (4) Co – extinctions

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. From the evil quartet, habitat loss and fragmentation due to over population, urbanization and industrialization is the major cause of extinction.

**Solved independently** (answer withheld)

1. Of the four major causes of biodiversity loss (habitat loss and fragmentation, over-exploitation, alien species invasion, co-extinctions), NCERT calls habitat loss and fragmentation the most important cause of extinction, which is option $3$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q120_bb9aa54e_28102026.png?v=bb9aa54ee871)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q120_e98ef046_28102026.png?v=e98ef04670e2)

---

## Q121

Biology · botany · Ecosystem

Which one of the following is a characteristic feature of cropland ecosystem?

- (1) Absence of soil organisms
- **(2)** Least genetic diversity
- (3) Absence of weeds
- (4) Ecological succession

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Cropland ecosystem has same type of crop plants so it has the least genetic diversity.

**Solved independently** (answer withheld)

1. A cropland is a man-made ecosystem grown as a monoculture of one crop variety, so its genetic diversity is the least; soil organisms and weeds are present and human management stops ecological succession, so option $2$ is correct.

**Subtopic:** Types of Ecosystems · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q121_14d9361a_28102026.png?v=14d9361aaee9)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q121_e2aa9908_28102026.png?v=e2aa990817c1)

---

## Q122

Biology · zoology · Human Reproduction

Changes in GnRH pulse frequency in females is controlled by circulating levels of:

- **(1)** Estrogen and progesterone
- (2) Estrogen and inhibin
- (3) Progesterone only
- (4) Progesterone and inhibin

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. GnRH pulse frequency in controlled by estrogen and progesterone both after puberty.

**Solved independently** (answer withheld)

1. GnRH is secreted in pulses by the hypothalamus, and its pulse frequency is changed by feedback from the ovarian steroid hormones $\text{estrogen}$ and $\text{progesterone}$; inhibin acts directly on the anterior pituitary to lower $\text{FSH}$, not on GnRH, so the answer is option $1$.

**Subtopic:** Hormonal Regulation of Reproduction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q122_df106caf_28102026.png?v=df106caf4e88)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q122_b0f4ce02_28102026.png?v=b0f4ce029899)

---

## Q123

Biology · both · Biotechnology: Principles and Processes

Which of the following is not a feature of the plasmids?

- (1) Independent replication
- (2) Circular structure
- (3) Transferable
- **(4)** Single – stranded

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Plasmids are extrachromosomal, double stranded circular DNA.

**Solved independently** (answer withheld)

1. Plasmids are extrachromosomal, autonomously replicating, circular, double-stranded DNA molecules that can be transferred between bacteria, so they are not single-stranded, which is option $4$.

**Subtopic:** Cloning Vectors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q123_5303c651_28102026.png?v=5303c651f796)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q123_87c8a72a_28102026.png?v=87c8a72aa965)

---

## Q124

Biology · zoology · Animal Kingdom

Which of the following features is not present in Periplaneta americana?

- (1) Schizocoelom as body cavity
- **(2)** Indeterminate and radial cleavage during embryonic development
- (3) Exoskeleton composed of N – acetylglucosamine
- (4) Metamerically segmented body

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Periplaneta americana shows indeterminate and spiral cleavage.

**Solved independently** (answer withheld)

1. $Periplaneta\ americana$ is an arthropod, a protostome with a schizocoelom, a chitinous exoskeleton (polymer of $N$-acetylglucosamine) and a metamerically segmented body, so options $1$, $3$ and $4$ are present.
2. Protostomes show spiral, determinate cleavage; indeterminate and radial cleavage is characteristic of deuterostomes, so it is absent in the cockroach, which is option $2$.

**Subtopic:** Phylum – Arthropoda · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 56)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q124_cd7e095a_28102026.png?v=cd7e095a9cb0)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q124_a448acf3_28102026.png?v=a448acf3db0b)

---

## Q125

Biology · zoology · Human Health and Disease

In higher vertebrates, the immune system can distinguish self – cells and non – self. If this property is lost due to genetic abnormality and it attacks self – cells, then it leads to:

- (1) Allergic response
- (2) Graft rejection
- **(3)** Auto – immune disease
- (4) Active immunity

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. If self and non – self recognition power is lost then immune cells can attack our own body cells and cause an auto immune disease.

**Solved independently** (answer withheld)

1. Loss of self/non-self discrimination makes the immune system attack the body's own cells, which NCERT calls an auto-immune disease (e.g. rheumatoid arthritis), so the answer is option $3$.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q125_f0605bcc_28102026.png?v=f0605bcc9153)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q125_b0fa4759_28102026.png?v=b0fa47597979)

---

## Q126

Biology · both · Principles of Inheritance and Variation

Column – I    Column – II

| List-I | | List-II | |
|---|---|---|---|
| (a) | Dominance | (i) | Many genes govern a single character |
| (b) | Codominance | (ii) | In a heterozygous organism only one allele expresses itself |
| (c) | Pleiotropy | (iii) | In a heterozygous organism both alleles express themselves fully |
| (d) | Polygenic inheritance | (iv) | A single gene influences many characters |

- (1) (a) (ii), (b) (i), (c) (iv), (d) (iii)
- **(2)** (a) (ii), (b) (iii), (c) (iv), (d) (i)
- (3) (a) (iv), (b) (i), (c) (ii), (d) (iii)
- (4) (a) (iv), (b) (iii), (c) (i), (d) (ii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Dominance – In a heterozygous organism only one allele expresses itself.
2. Codominance – In a heterozygous organism both alleles express themselves equally.
3. Pleiotropy – A single gene influences many characters.
4. Polygenic Inheritance – Many genes govern a single character.

**Solved independently** (answer withheld)

1. Dominance: in a heterozygote only one allele expresses itself, so (a) $\rightarrow$ (ii).
2. Codominance: in a heterozygote both alleles express themselves fully, so (b) $\rightarrow$ (iii).
3. Pleiotropy: a single gene influences many characters, so (c) $\rightarrow$ (iv).
4. Polygenic inheritance: many genes govern a single character, so (d) $\rightarrow$ (i).
5. The match (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i) is option $2$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance, Incomplete Dominance & Co-dominance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q126_9b947853_28102026.png?v=9b94785373c4)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q126_dcb24f3f_28102026.png?v=dcb24f3f7af8)

---

## Q127

Biology · botany · Environmental Issues

Joint Forest Management Concept was introduced in India during:

- (1) 1960s
- (2) 1970s
- **(3)** 1980s
- (4) 1990s

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Joint Forest Management Concept was introduced to protect forest cover in India in 1988.

**Solved independently** (answer withheld)

1. As NCERT teaches it, the Government of India introduced Joint Forest Management (JFM) in the $1980\text{s}$, so the answer is option $3$.

**Subtopic:** Deforestation and People's Participation in Forest Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q127_fea99ab0_28102026.png?v=fea99ab02c88)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q127_e44290c8_28102026.png?v=e44290c8e501)

---

## Q128

Biology · both · Principles of Inheritance and Variation

> ⚠ The independent solve chose (3); the booklet prints (4).

Pick out the correct statements:

- **(i)** Hemophilia is a sex – linked recessive disease
- **(ii)** Down’s syndrome is due to aneuploidy
- **(iii)** Phenylketonuria is an autosomal recessive gene disorder
- **(iv)** Sickle cell anaemia is an autosomal recessive gene disorder

- (1) (i) and (iv) are correct
- (2) (ii) and (iv) are correct
- (3) (i), (iii) and (iv) are correct
- **(4)** (i), (ii) and (iii) are correct

**Answer** — booklet: (4) · independent solve: (3) · differs

**Publisher's solution**

1. Hemophilia is a sex – linked recessive disease in which there is a problem in clotting of blood.
2. Down’s syndrome (trisomy 21) is caused due to aneuploidy.
3. Phenylketonuria is an autosomal recessive gene disorder.
4. Sickle cell anaemia is autosomal recessive gene disorder.

**Solved independently** (answer withheld)

1. Statement (i): haemophilia is an $X$-linked (sex-linked) recessive disorder, so (i) is true.
2. Statement (ii): Down's syndrome is trisomy 21 ($2n+1 = 47$), a gain of one chromosome, which is aneuploidy, so (ii) is true.
3. Statement (iii): phenylketonuria is an inborn error of metabolism inherited as an autosomal recessive trait, so (iii) is true.
4. Statement (iv): sickle cell anaemia is an autosomal recessive disorder ($Hb^S Hb^S$), so (iv) is true.
5. All four statements are true, but no option lists (i), (ii), (iii) and (iv); options $3$ and $4$ are each partly complete, and $3$ is chosen as a best guess only.

**Subtopic:** Mendelian Disorders, Chromosomal Disorders · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 58)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q128_7f113206_28102026.png?v=7f113206db90)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q128_6490ff52_28102026.png?v=6490ff52353d)

---

## Q129

Biology · botany · Biological Classification

Which one of the following statements is wrong?

- (1) Cyanobacteria are also called blue – green algae
- (2) Golden algae are also called desmids
- **(3)** Eubacteria are also called false bacteria
- (4) Phycomycetes are also called algal fungi

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Eubacteria are called true bacteria.

**Solved independently** (answer withheld)

1. Cyanobacteria are also called blue-green algae, so option $1$ is correct.
2. NCERT groups chrysophytes as diatoms and golden algae (desmids), so option $2$ is correct as the textbook teaches it.
3. Phycomycetes are called algal fungi, so option $4$ is correct.
4. Eubacteria means 'true bacteria', not 'false bacteria', so option $3$ is the wrong statement.

**Subtopic:** Eubacteria · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q129_bc8cb2a0_28102026.png?v=bc8cb2a09773)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q129_37185cd6_28102026.png?v=37185cd69150)

---

## Q130

Biology · botany · Morphology of Flowering Plants

Proximal end of the filament of stamen is attached to the:

- (1) Anther
- (2) Connective
- (3) Placenta
- **(4)** Thalamus or petal

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Proximal end of the filament of stamen is attached to the thalamus or petal and distal end is attached to anther.

**Solved independently** (answer withheld)

1. A stamen has a long slender stalk, the filament, whose proximal end is attached to the thalamus or the petal of the flower and whose distal end bears the anther, which is option $4$.

**Subtopic:** Androecium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q130_9678a844_28102026.png?v=9678a84415dd)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q130_1c4c04d1_28102026.png?v=1c4c04d1b70b)

---

## Q131

Biology · zoology · Reproductive Health

Which of the following approaches does not give the defined action of contraceptive?

- (1) Barrier methods — Prevent fertilization
- (2) Intra uterine devices — Increase phagocytosis of sperms, suppress sperm motility and fertilizing capacity of sperms
- (3) Hormonal contraceptives — Prevent /retard entry of sperms, prevent ovulation and fertilization
- **(4)** Vasectomy — Prevents spermatogenesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Vasectomy causes sterilization by preventing transfer of sperms.

**Solved independently** (answer withheld)

1. Barrier methods, IUDs and hormonal contraceptives are listed with the actions the textbook gives them, but vasectomy blocks the vas deferens and so stops sperm transport, not spermatogenesis. The wrong pairing is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q131_f5682bf0_28102026.png?v=f5682bf09bb6)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q131_f6c59020_28102026.png?v=f6c59020aa2c)

---

## Q132

Biology · both · Biotechnology: Principles and Processes

The taq polymerase enzyme is obtained from:

- **(1)** Thermus aquaticus
- (2) Thiobacillus ferroxidans
- (3) Bacillus subtilis
- (4) Pseudomonas putida

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The enzyme taq polymerase is a thermostable enzyme which is obtained from Thermus aquaticus.

**Solved independently** (answer withheld)

1. Taq polymerase is the thermostable DNA polymerase used in PCR, isolated from the bacterium $Thermus\ aquaticus$, which is option $1$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q132_bcb34e6c_28102026.png?v=bcb34e6cda90)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q132_20079304_28102026.png?v=20079304048b)

---

## Q133

Biology · zoology · Human Reproduction

Identify the correct statement on ‘inhibin’:

- (1) Inhibits the secretion of LH, FSH and Prolactin
- **(2)** Is produced by granulose cells in ovary and inhibits the secretion of FSH
- (3) Is produced by granulose cells in ovary and inhibits the secretion of LH
- (4) Is produced by nurse cells in testes and inhibits the secretion of LH

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Inhibin is produced by granulosa cells in the ovary and inhibits the secretion of $\mathrm{FSH}$ – follicle stimulating hormone.

**Solved independently** (answer withheld)

1. Inhibin is a glycoprotein hormone made by granulosa cells in the ovary and by Sertoli (nurse) cells in the testis; it selectively suppresses FSH secretion from the anterior pituitary, so option $2$ is correct and options $1$, $3$, $4$ (which name LH or prolactin) are wrong.

**Subtopic:** Hormonal Regulation of Reproduction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q133_09506682_28102026.png?v=095066823e75)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q133_4563e3df_28102026.png?v=4563e3df4f4b)

---

## Q134

Biology · both · Biotechnology and Its Applications

Which part of the tobacco plant is infected by Meloidogyne incognita?

- (1) Flower
- (2) Leaf
- (3) Stem
- **(4)** Root

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Meloidogyne incognita infects the root of tobacco plant.

**Solved independently** (answer withheld)

1. $Meloidogyne\ incognita$ is a root-knot nematode that infects the roots of tobacco plants, so the answer is option $4$ (Root).

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q134_05c1b008_28102026.png?v=05c1b008b04b)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q134_36319f7b_28102026.png?v=36319f7b4659)

---

## Q135

Biology · zoology · Human Health and Disease

Antivenom injection contains preformed antibodies while polio drops that are administered into the body contain:

- (1) Activated pathogens
- (2) Harvested antibodies
- (3) Gamma globulin
- **(4)** Attenuated pathogens

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. OPV is of $2$ types:
2. (i) OPV sabin – Live attenuated vaccine
3. (ii) OPV salk – Killed vaccine

**Solved independently** (answer withheld)

1. Antivenom supplies preformed antibodies, which is passive immunisation.
2. Oral polio drops are a vaccine: they contain weakened (attenuated) live poliovirus that stimulates the body to make its own antibodies (active immunisation), so the answer is option $4$.

**Subtopic:** Vaccination and Immunisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q135_f7cef7ce_28102026.png?v=f7cef7ce72fa)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q135_4369c765_28102026.png?v=4369c765bddd)

---

## Q136

Biology · both · Cell: The Unit of Life

Which one of the following cell organelles is enclosed by a single membrane?

- (1) Mitochondria
- (2) Chloroplasts
- **(3)** Lysosomes
- (4) Nuclei

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Except lysosomes, all three are bounded by double membrane.

**Solved independently** (answer withheld)

1. Mitochondria, chloroplasts and the nucleus are each enclosed by a double membrane (envelope), while lysosomes are single-membrane vesicles formed from the Golgi, so the answer is option $3$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q136_22a5751f_28102026.png?v=22a5751f8bf7)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q136_a046001b_28102026.png?v=a046001bcb72)

---

## Q137

Biology · zoology · Locomotion and Movement

Lack of relaxation between successive stimuli in sustained muscle contraction is known as:

- (1) Spasm
- (2) Fatigue
- **(3)** Tetanus
- (4) Tonus

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Tonus $\rightarrow$ low level activity of muscles at rest to maintain posture
2. Spasm $\rightarrow$ Sudden involuntary muscle contraction
3. Fatigue $\rightarrow$ Decline in muscle activity
4. Tetanus $\rightarrow$ Sustained muscle contraction in response to successive stimuli

**Solved independently** (answer withheld)

1. When stimuli arrive so fast that the muscle cannot relax between them, the twitches fuse into one smooth, sustained contraction, which is tetanus (option $3$).

**Subtopic:** Simple Muscle Twitch, Summation and Tetanus · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q137_d26ededa_28102026.png?v=d26ededa757d)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q137_db6e93bb_28102026.png?v=db6e93bbdac7)

---

## Q138

Biology · botany · Morphology of Flowering Plants

Which of the following is not a stem modification?

- **(1)** Pitcher of Nepenthes
- (2) Thorns of citrus
- (3) Tendrils of cucumber
- (4) Flattened structures of Opuntia

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Pitcher of Nepenthes is modification of the leaf.

**Solved independently** (answer withheld)

1. Citrus thorns, cucumber tendrils (axillary-bud origin) and Opuntia's flattened green phylloclade are stem modifications, while the Nepenthes pitcher is a leaf modification, so the answer is option $1$.

**Subtopic:** The Stem, The Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q138_9568e8c9_28102026.png?v=9568e8c9b17b)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q138_5a15b5e3_28102026.png?v=5a15b5e3f857)

---

## Q139

Biology · both · Cell: The Unit of Life

Water soluble pigments found in plant cell vacuoles are:

- (1) Xanthophylls
- (2) Chlorophylls
- (3) Carotenoids
- **(4)** Anthocyanins

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Anthocyanin is stored in vacuoles.

**Solved independently** (answer withheld)

1. Chlorophylls, carotenoids and xanthophylls are lipid-soluble pigments held in plastids, while anthocyanins are water-soluble pigments dissolved in the cell sap of the vacuole, so the answer is option $4$.

**Subtopic:** Vacuole and Cell Sap · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q139_a4617e12_28102026.png?v=a4617e1274c5)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q139_e9ce128e_28102026.png?v=e9ce128e4163)

---

## Q140

Biology · botany · Plant Kingdom

Select the correct statement:

- (1) Gymnosperms are both homosporous and heterosporous
- (2) Salvinia, ginkgo and pinus all are gymnosperms
- **(3)** Sequoia is one of the tallest trees
- (4) The leaves of gymnosperms are not well adapted to extremes of climate

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Sequoia is one of the tallest tree which is a gymnosperm and it can be $130$ – $140$ metres tall.

**Solved independently** (answer withheld)

1. Option $1$: gymnosperms are heterosporous (microspores and megaspores) only, not homosporous, so it is false.
2. Option $2$: Salvinia is a heterosporous pteridophyte (water fern), not a gymnosperm, so it is false.
3. Option $3$: the giant redwood Sequoia is one of the tallest tree species, so it is true.
4. Option $4$: gymnosperm leaves (needle-like, thick cuticle, sunken stomata) are well adapted to extremes of temperature, humidity and wind, so it is false.
5. The correct statement is option $3$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q140_816e8859_28102026.png?v=816e88592b8a)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q140_3d8d799a_28102026.png?v=3d8d799ac9e0)

---

## Q141

Biology · both · Molecular Basis of Inheritance

Which of the following is not required for any of the techniques of DNA fingerprinting available at present?

- (1) Polymerase chain reaction
- **(2)** Zinc finger analysis
- (3) Restriction enzymes
- (4) DNA – DNA hybridization

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Zinc finger analysis does not contribute to DNA fingerprinting.

**Solved independently** (answer withheld)

1. DNA fingerprinting (as taught in NCERT) involves DNA isolation, digestion by restriction enzymes, separation by electrophoresis, blotting, hybridization with labelled VNTR probes (DNA-DNA hybridization), and PCR to amplify small samples; zinc finger analysis is not part of any of these techniques, so the answer is option $2$.

**Subtopic:** DNA Fingerprinting · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q141_3207db04_28102026.png?v=3207db042417)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q141_fb44a54e_28102026.png?v=fb44a54ede69)

---

## Q142

Biology · zoology · Structural Organisation in Animals

Which type of tissue correctly matches with its location?

- **(1)** Tissue | Location
Smooth muscle | Wall of intestine
- (2) Tissue | Location
Areolar tissue | Tendons
- (3) Tissue | Location
Transitional epithelium | Tip of nose
- (4) Tissue | Location
Cuboidal epithelium | Lining of stomach

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Wall of intestine is composed of smooth muscle.
2. Tendon is a dense regular white fibrous connective tissue and areolar tissue is a loose connective tissue.
3. Tip of nose is made up of elastic cartilage.
4. Lining of stomach is composed of columnar epithelium.

**Solved independently** (answer withheld)

1. Smooth muscle fibres are found in the walls of hollow visceral organs such as the intestine, so option $1$ is a correct match.
2. Tendons are dense regular connective tissue, not areolar tissue, so option $2$ is wrong.
3. The tip of the nose is supported by cartilage; transitional epithelium lines the urinary bladder, so option $3$ is wrong.
4. The stomach is lined by simple columnar epithelium, not cuboidal epithelium, so option $4$ is wrong; the answer is option $1$.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q142_30b0be41_28102026.png?v=30b0be4109e6)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q142_b991a2ec_28102026.png?v=b991a2ec221a)

---

## Q143

Biology · botany · Photosynthesis in Higher Plants

A plant in your garden avoids photorespiratory losses, has improved water use efficiency, shows high rates of photosynthesis at high temperatures and has improved efficiency of nitrogen utilization. In which of the following physiological groups would you assign this plant?

- (1) $C_3$
- **(2)** $C_4$
- (3) CAM
- (4) Nitrogen fixer

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $C_4$ plants have high rate of photosynthesis at higher temperature.

**Solved independently** (answer withheld)

1. C$_4$ plants concentrate $CO_2$ around RuBisCO in bundle sheath cells, so photorespiratory losses are avoided, and they have higher water-use and nitrogen-use efficiency and a higher temperature optimum for photosynthesis, so the plant is $C_4$, which is option $2$.

**Subtopic:** The C₄ Pathway · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q143_b76fa9dc_28102026.png?v=b76fa9dc75f2)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q143_b085a118_28102026.png?v=b085a11824c8)

---

## Q144

Biology · both · Evolution

Which of the following structures is homologus to the wing of a bird?

- (1) Dorsal fin of a shark
- (2) Wing of a moth
- (3) Hind limb of rabbit
- **(4)** Flipper of whale

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Flipper of whale is homologous to the wing of a bird.

**Solved independently** (answer withheld)

1. Homologous organs share the same basic structure and embryonic origin, even when their functions differ.
2. A bird's wing is a modified vertebrate forelimb (humerus, radius--ulna, carpals, metacarpals, phalanges).
3. A whale's flipper is also a modified forelimb with the same bone pattern, so it is homologous to the bird's wing, which is option $4$.
4. A moth's wing does the same job but has a different structure, so it is analogous. A shark's dorsal fin is not a limb, and a rabbit's hind limb is not the matching forelimb.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 63)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q144_cf73b678_28102026.png?v=cf73b678e84b)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q144_33da0fc7_28102026.png?v=33da0fc74030)

---

## Q145

Biology · zoology · Animal Kingdom

Which of the following characteristic features always holds true for the corresponding group of animals?

- **(1)** Cartilaginous endoskeleton | Chondrichthyes
- (2) Viviparous | Mammalia
- (3) Possess a mouth with an upper and a lower jaw | Chordata
- (4) 3 – chambered heart with one incompletely divided ventricle | Reptilia

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Reptillia has an order crocodilian which shows $4$ chambered heart.
2. In mammals, prototheria group shows oviparity while metatheria and eutherian show viviparity.
3. Chordates can be gnathostomata and agnatha (without jaws).
4. Only cartilaginous fishes (chondrichthyes) show cartilaginous endoskeleton without exception.

**Solved independently** (answer withheld)

1. Chondrichthyes: endoskeleton is cartilaginous in all members, so option $1$ always holds.
2. Mammalia: monotremes such as the platypus are oviparous, so viviparity is not universal; option $2$ fails.
3. Chordata: cyclostomes (Agnatha) lack jaws, so jaws are not universal in chordates; option $3$ fails.
4. Reptilia: crocodiles have a 4-chambered heart, so a 3-chambered heart is not universal; option $4$ fails.
5. Hence the answer is option $1$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q145_ae54232b_28102026.png?v=ae54232b1368)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q145_b163b814_28102026.png?v=b163b8145c01)

---

## Q146

Biology · zoology · Human Health and Disease

Which of the following statements is not true for cancer cells in relation to mutations?

- (1) Mutations in proto – oncogenes accelerate the cell cycle
- (2) Mutations destroy telomerase inhibitor
- (3) Mutations inactivate the cell control
- **(4)** Mutations inhibit production of telomerase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Cancer will be caused by increased telomerase activity making the cancerous cells immortal and not by inhibition of telomerase production.

**Solved independently** (answer withheld)

1. Mutations in proto-oncogenes turn them into oncogenes that speed up the cell cycle, so option $1$ is true.
2. Cancer cells keep telomerase active, which fits mutations that destroy a telomerase inhibitor, so option $2$ is true.
3. Mutations remove normal growth control (contact inhibition is lost), so option $3$ is true.
4. Mutations that stopped telomerase being made would contradict the high telomerase activity of cancer cells, so option $4$ is not true and is the answer.

**Subtopic:** Cancer · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q146_8c521bc1_28102026.png?v=8c521bc17a2a)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q146_0e9e8739_28102026.png?v=0e9e87398d71)

---

## Q147

Biology · zoology · Chemical Coordination and Integration

The amino acid Tryptophan is the precursor for the synthesis of:

- **(1)** Melatonin and Serotonin
- (2) Thyroxine and Triiodothyronine
- (3) Estrogen and Progesterone
- (4) Cortisol and Cortisone

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Amino acid tryptophan is the precursor for the synthesis of melatonin and serotonin.

**Solved independently** (answer withheld)

1. Tryptophan is hydroxylated and decarboxylated to give serotonin ($5$-hydroxytryptamine), and the pineal gland converts serotonin to melatonin, so option $1$ fits.
2. Thyroxine ($T_4$) and triiodothyronine ($T_3$) are iodinated tyrosine derivatives, and estrogen, progesterone, cortisol and cortisone are steroids made from cholesterol, so options $2$, $3$ and $4$ are ruled out; the answer is option $1$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 64)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q147_f15e4eab_28102026.png?v=f15e4eabcbcd)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q147_90702e65_28102026.png?v=90702e6560e1)

---

## Q148

Biology · both · Evolution

Following are the two statements regarding the origin of life: Of the above statements which one of the following options is correct?

- **((i))** The earliest organisms that appeared on the earth were non-green and presumably anaerobes.
- **((ii))** The first autotrophic organisms were the chemoautotrophs that never released oxygen.

- (1) (i) is correct but (ii) is false
- (2) (ii) is correct but (i) is false
- **(3)** Both (i) and (ii) are correct
- (4) Both (i) and (ii) are false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The first originated organisms were prokaryotic chemoheterotrophs and oxygen was not available on earth at that time so it must be anaerobic too.
2. Even the first autotrophs were dependent on chemicals as oxygen was not released.

**Solved independently** (answer withheld)

1. Statement (i): early life arose in an oxygen-free primitive atmosphere, so the first organisms were non-green (no chlorophyll) and presumably anaerobic. True.
2. Statement (ii): the first autotrophs were chemoautotrophs, which fix carbon using energy from oxidising inorganic compounds, not light, so they released no $O_2$. True.
3. Both (i) and (ii) are correct, which is option $3$.

**Subtopic:** Introduction and Origin of Life · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 65)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q148_2a2e5ef3_28102026.png?v=2a2e5ef3fa8f)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q148_8ad2cd17_28102026.png?v=8ad2cd178eee)

---

## Q149

Biology · zoology · Breathing and Exchange of Gases

Reduction in $\mathrm{pH}$ of blood will:

- (1) Reduce the rate of heart beat
- (2) Reduce the blood supply to the brain
- **(3)** Decrease the affinity of hemoglobin with oxygen
- (4) Release bicarbonate ions by the liver

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Reduction in $\mathrm{pH}$ of blood decreases the affinity of hemoglobin with oxygen.

**Solved independently** (answer withheld)

1. A fall in blood $\mathrm{pH}$ means a higher $[\mathrm{H^+}]$, which shifts the oxygen dissociation curve to the right (Bohr effect), so haemoglobin's affinity for $\mathrm{O_2}$ decreases, which is option $3$.

**Subtopic:** Transport of Gases · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q149_700e56ae_28102026.png?v=700e56aec754)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q149_b87ce80d_28102026.png?v=b87ce80d58b5)

---

## Q150

Biology · both · Evolution

Analogous structures are a result of:

- (1) Divergent evolution
- **(2)** Convergent evolution
- (3) Shared ancestry
- (4) Stabilizing selection

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Analogous structures are a result of convergent evolution.

**Solved independently** (answer withheld)

1. Analogous structures (e.g. wings of butterfly and bird) perform the same function but are not anatomically similar and do not share common ancestry; they arise when different groups adapt to similar conditions, which is convergent evolution, option $2$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q150_a40c6633_28102026.png?v=a40c66332916)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q150_1c3a1e20_28102026.png?v=1c3a1e20f363)

---

## Q151

Biology · both · Biotechnology: Principles and Processes

Which of the following is a restriction endonuclease?

- **(1)** Hind II
- (2) Protease
- (3) DNase I
- (4) RNase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Hind II is a type of restriction endonuclease.

**Solved independently** (answer withheld)

1. Hind II recognises a specific palindromic sequence and cuts DNA there, so it is a restriction endonuclease (option $1$); protease, DNase I and RNase are not.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q151_7aa087f6_28102026.png?v=7aa087f629f9)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q151_0f89df20_28102026.png?v=0f89df20f365)

---

## Q152

Biology · botany · Ecosystem

The term ecosystem was coined by:

- (1) E.P. Odum
- **(2)** A.G. Tansley
- (3) E. Haeckel
- (4) E. Warming

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The term ecosystem was coined by A.G. Tansley in 1935.

**Solved independently** (answer withheld)

1. The term $\text{ecosystem}$ was coined by A.G. Tansley in $1935$, which is option $2$.

**Subtopic:** Introduction of Ecosystem · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q152_ae719d4b_28102026.png?v=ae719d4b3054)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q152_e11c8341_28102026.png?v=e11c83411693)

---

## Q153

Biology · both · Biomolecules

Which one of the following statements is wrong?

- (1) Sucrose is a disaccharide
- (2) Cellulose is a polysaccharide
- (3) Uracil is a pyrimidine
- **(4)** Glycine is a sulphur containing amino acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Glycine is the simplest amino acid which is devoid of sulphur content.

**Solved independently** (answer withheld)

1. Sucrose (glucose + fructose) is a disaccharide, cellulose is a polysaccharide of glucose, and uracil is a pyrimidine base, so options $1$, $2$ and $3$ are correct; glycine's R group is $\mathrm{H}$ and it has no sulphur (cysteine and methionine contain S), so the wrong statement is option $4$.

**Subtopic:** Amino Acids and Their Classification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q153_cb510e93_28102026.png?v=cb510e938206)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q153_03166322_28102026.png?v=0316632210bc)

---

## Q154

Biology · botany · Plant Kingdom

In bryophytes and pteridophytes, transport of male gametes requires:

- (1) Wind
- (2) Insects
- (3) Birds
- **(4)** Water

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In bryophytes and pteridophytes, the male gametes are motile and it requires water for fertilization.

**Solved independently** (answer withheld)

1. In bryophytes and pteridophytes the male gametes are motile, flagellated antherozoids that must swim through water to reach the egg in the archegonium, so transport requires $\text{water}$, which is option $4$.

**Subtopic:** Bryophytes, Pteridophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q154_4d51a6e2_28102026.png?v=4d51a6e22d3d)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q154_db92dee4_28102026.png?v=db92dee42887)

---

## Q155

Biology · botany · Organisms and Populations

When does the growth rate of a population following the logistic model equal zero? The logistic model is given as $dN/dt = rN(1 - N/K)$:

- **(1)** When $N/K$ is exactly one
- (2) When N nears the carrying capacity of the habitat
- (3) When $N/K$ equals zero
- (4) When death rate is greater than birth rate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$
2. $\frac{dN}{dt} = rN(1 - 1) = 0$

**Solved independently** (answer withheld)

1. Growth stops when $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right) = 0$.
2. For a living population ($N > 0$, $r > 0$), this needs $1 - \frac{N}{K} = 0$, i.e. $\frac{N}{K} = 1$ ($N = K$).
3. So the growth rate is zero when $N/K$ is exactly one, which is option $1$.

**Subtopic:** Logistic Growth · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 66)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q155_8cf69aca_28102026.png?v=8cf69aca9545)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q155_a1f85e12_28102026.png?v=a1f85e120fde)

---

## Q156

Biology · botany · Sexual Reproduction in Flowering Plants

Which one of the following statements is not true?

- **(1)** Tapetum helps in the dehiscence of anther
- (2) Exine of pollen grains is made up of sporopollenin
- (3) Pollen grains of many species cause severe allegies
- (4) Stored pollen in liquid nitrogen can be used in the crop breeding programmes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Dehiscence of anther occurs due to stomium cells of endothecium

**Solved independently** (answer withheld)

1. The tapetum is the innermost wall layer of the microsporangium and nourishes the developing pollen grains. It plays no part in the anther's dehiscence, so statement $1$ is not true.
2. The exine of the pollen grain is made of sporopollenin, so statement $2$ is true.
3. Pollen grains of many species, e.g. $Parthenium$, cause severe allergies, so statement $3$ is true.
4. Pollen stored in liquid nitrogen at $-196^{\circ}\mathrm{C}$ stays viable for years and is used in crop breeding programmes, so statement $4$ is true. The answer is option $1$.

**Subtopic:** Microsporangium and Microsporogenesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q156_34954e4a_28102026.png?v=34954e4a8a11)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q156_b7a095fd_28102026.png?v=b7a095fd4b23)

---

## Q157

Biology · botany · Ecosystem

Which of the following would appear as the pioneer organisms on bare rocks?

- **(1)** Lichens
- (2) Liverworts
- (3) Mosses
- (4) Green algae

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Lichens are pioneer organisms on bare rocks as they corrode the rocks by secreting enzymes and convert it into soil.

**Solved independently** (answer withheld)

1. In primary succession on bare rock, the first colonisers are lichens, which secrete acids that weather the rock and begin soil formation; mosses come only later, so the answer is option $1$.

**Subtopic:** Ecological Succession · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q157_ab0a9b56_28102026.png?v=ab0a9b56c835)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q157_3d88790a_28102026.png?v=3d88790ae08b)

---

## Q158

Biology · both · Molecular Basis of Inheritance

Which one of the following is the starter codon?

- **(1)** AUG
- (2) UGA
- (3) UAA
- (4) UAG

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. AUG is start codon that codes for methionine whereas UGA, UAA and UAG are stop codons.

**Solved independently** (answer withheld)

1. The start (initiator) codon is $\mathrm{AUG}$, coding for methionine, while $\mathrm{UAA}$, $\mathrm{UAG}$ and $\mathrm{UGA}$ are stop codons, so the answer is option $1$.

**Subtopic:** Genetic Code and Its Features · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q158_0beec4e1_28102026.png?v=0beec4e151db)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q158_16954840_28102026.png?v=16954840351c)

---

## Q159

Biology · zoology · Animal Kingdom

Which one of the following characteristics is not shared by birds and mammals?

- (1) Ossified endoskeleton
- (2) Breathing using lungs
- **(3)** Viviparity
- (4) Warm blooded nature

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Birds are oviparous while mammals are oviparous (prototherians) and viviparous (metatherians and eutherians).

**Solved independently** (answer withheld)

1. Both birds and mammals have an ossified endoskeleton, breathe with lungs and are homoiothermous (warm blooded); birds are oviparous whereas mammals are viviparous (barring a few), so viviparity, option $3$, is not shared.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q159_a028f938_28102026.png?v=a028f938ec9f)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q159_ed9aed39_28102026.png?v=ed9aed39e9ab)

---

## Q160

Biology · botany · The Living World

Nomenclature is governed by certain universal rules. Which one of the following is contrary to the rules of nomenclature?

- **(1)** Biological names can be written in any language
- (2) The first words in a biological name represents the genus name, and the second is a specific epithet
- (3) The names are written in Latin and are italicized
- (4) When written by hand, the names are to be underlined

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. According to the rules of IUCN the original names were taken from Latin or Greek languages.
2. New names are now derived either from Latin language or are Latinized.

**Solved independently** (answer withheld)

1. The rules of binomial nomenclature say names are in Latin or Latinised, italicised in print and underlined separately when handwritten, with the genus name first and the specific epithet second; so options $2$, $3$ and $4$ follow the rules, and option $1$ ('any language') goes against them.

**Subtopic:** Diversity in Living World and Binomial Nomenclature · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q160_9657a2b4_28102026.png?v=9657a2b4a7dd)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q160_aeebce9d_28102026.png?v=aeebce9dc82b)

---

## Q161

Biology · zoology · Body Fluids and Circulation

Blood pressure in the pulmonary artery is:

- (1) Same as that in the aorta
- (2) More than that in the carotid
- **(3)** More than that in the pulmonary vein
- (4) Less than that in the venae cavae

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Blood pressure in different blood vessels:
2. Artery $>$ Arteriole $>$ Capillary $>$ Venule $>$ Vein (Vena cava)

**Solved independently** (answer withheld)

1. Blood flows from high to low pressure, so $P_{\text{pulmonary artery}} > P_{\text{pulmonary capillaries}} > P_{\text{pulmonary vein}}$.
2. The pulmonary (low-pressure) circuit runs at about $25/8\,\text{mmHg}$, well below the systemic aorta and carotid at about $120/80\,\text{mmHg}$, so options $1$ and $2$ are false.
3. The venae cavae carry blood at near $0$ to $5\,\text{mmHg}$, below the pulmonary artery, so option $4$ is false.
4. Hence the pulmonary artery pressure is more than that in the pulmonary vein, which is option $3$.

**Subtopic:** Blood Pressure in the Pulmonary and Systemic Circuits · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 68)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q161_ccd17733_28102026.png?v=ccd17733e76f)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q161_0b07f46a_28102026.png?v=0b07f46a2df4)

---

## Q162

Biology · botany · Sexual Reproduction in Flowering Plants

Cotyledon of maize grain is called:

- (1) Plumule
- (2) Coleorhiza
- (3) Coleoptile
- **(4)** Scutellum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In maize grains, the single large shield shaped cotyledon is called scutellum.

**Solved independently** (answer withheld)

1. In the monocot (grass) embryo of maize, the single large shield-shaped cotyledon is called the scutellum, so the answer is option $4$; plumule is the shoot tip, the coleoptile is the sheath over the plumule and the coleorhiza is the sheath over the radicle.

**Subtopic:** Embryo and Seed · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q162_c28256bb_28102026.png?v=c28256bbfad5)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q162_338eb473_28102026.png?v=338eb473775e)

---

## Q163

Biology · zoology · Digestion and Absorption

In the stomach, gastric acid is secreted by the:

- (1) Gastrin secreting cells
- **(2)** Parietal cells
- (3) Peptic cells
- (4) Acidic cells

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Gastric acid i.e. $\mathrm{HCl}$ is secreted by parietal or oxyntic cells.

**Solved independently** (answer withheld)

1. Gastric glands have mucus neck cells, peptic (chief) cells secreting pepsinogen, and parietal (oxyntic) cells secreting $\mathrm{HCl}$ and intrinsic factor, so gastric acid comes from parietal cells, option $2$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q163_b818fffd_28102026.png?v=b818fffdd990)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q163_37d7143a_28102026.png?v=37d7143a80bf)

---

## Q164

Biology · botany · Environmental Issues

Depletion of which gas in the atmosphere can lead to an increased incidence of skin cancers:

- (1) Nitrous oxide
- **(2)** Ozone
- (3) Ammonia
- (4) Methane

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ozone is found in the upper part of the atmosphere called stratosphere and it acts as a shield absorbing ultraviolet radiation from sun and so its depletion can lead to incidence of skin cancers.

**Solved independently** (answer withheld)

1. Stratospheric ozone absorbs harmful UV-B radiation; its depletion lets more UV-B reach the surface, which damages DNA and increases skin cancer incidence, so the answer is option $2$ (Ozone).

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q164_c12724f2_28102026.png?v=c12724f23473)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q164_2dabefde_28102026.png?v=2dabefdeacc8)

---

## Q165

Biology · botany · Biological Classification

Chrysophytes, Euglenoids, Dinoflagellates and Slime moulds are included in the kingdom:

- (1) Monera
- **(2)** Protista
- (3) Fungi
- (4) Animalia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Protista is a group created by Haeckel which includes all Eukaryotic unicellular organisms.

**Solved independently** (answer withheld)

1. In the five-kingdom system taught in NCERT, kingdom Protista comprises Chrysophytes, Dinoflagellates, Euglenoids, Slime moulds and Protozoans, so the answer is option $2$ (Protista).

**Subtopic:** Kingdom Protista · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q165_60066607_28102026.png?v=600666075475)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q165_8bd0f8fc_28102026.png?v=8bd0f8fce8e9)

---

## Q166

Biology · botany · Transport in Plants

Water vapour comes out from the plant leaf through the stomatal opening. Through the same stomatal opening carbon dioxide diffuses into the plant during photosynthesis. Reason out the above statements using one of following options:

- (1) Both processes cannot happen simultaneously
- **(2)** Both processes can happen together because the diffusion coefficient of water and $\mathrm{CO_2}$ is different
- (3) The above processes happen only during night time
- (4) One process occurs during day time, and the other at night

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Water vapour comes out and $\mathrm{CO_2}$ diffuses simultaneously through stomatal opening because diffusion coefficient of water and $\mathrm{CO_2}$ is different and it moves along its concentration gradient.

**Solved independently** (answer withheld)

1. During the day the stomata are open, and both transpiration and photosynthesis go on, so options $1$, $3$ and $4$ are ruled out.
2. Each gas diffuses down its own concentration gradient: $\mathrm{H_2O}$ from leaf to air, $\mathrm{CO_2}$ from air to leaf, and the two gases have different diffusion coefficients, so both processes happen together, which is option $2$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q166_0980f35d_28102026.png?v=0980f35d25c3)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q166_622ba3c1_28102026.png?v=622ba3c1f335)

---

## Q167

Biology · zoology · Excretory Products and Their Elimination

In mammals, which blood vessel would normally carry largest amount of urea?

- (1) Renal vein
- (2) Dorsal aorta
- **(3)** Hepatic vein
- (4) Hepatic portal vein

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Urea – Ornithine cycle takes place in liver so the vein leaving liver possesses maximum urea which is hepatic vein.

**Solved independently** (answer withheld)

1. Urea is made in the liver from ammonia via the ornithine (urea) cycle and released into blood leaving the liver through the hepatic vein, so the hepatic vein carries the largest amount of urea, which is option $3$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q167_28bb0039_28102026.png?v=28bb0039e459)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q167_41d81edb_28102026.png?v=41d81edb737b)

---

## Q168

Biology · botany · Sexual Reproduction in Flowering Plants

Seed formation without fertilization in flowering plants involves the process of:

- (1) Sporulation
- (2) Budding
- (3) Somatic hybridization
- **(4)** Apomixis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Apomixis is a special mechanism to produce seeds without fertilization.

**Solved independently** (answer withheld)

1. Seed formation without fertilization is defined as apomixis, a form of asexual reproduction that mimics sexual reproduction, so the answer is option $4$.

**Subtopic:** Apomixis and Polyembryony · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q168_e1d08598_28102026.png?v=e1d085981dd1)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q168_0c3751a0_28102026.png?v=0c3751a0f678)

---

## Q169

Biology · botany · Microbes in Human Welfare

Which of the following is wrongly matched in the given table?

- (1) | Microbe | Product | Application |
|---|---|---|
| Trichoderma polysporum | Cyclosporin A | Immunosuppressive drug |
- (2) | Microbe | Product | Application |
|---|---|---|
| Monascus purpureus | Statins | Lowering of blood cholesterol |
- (3) | Microbe | Product | Application |
|---|---|---|
| Streptococcus | Streptokinase | Removal of clot from blood vessel |
- **(4)** | Microbe | Product | Application |
|---|---|---|
| Clostridium butylicum | Lipase | Removal of oil stains |

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Clostridium butylicum is used for the production of butyric acid.
2. Candida lipolyticum is the source of lipase.

**Solved independently** (answer withheld)

1. Row 1: $Trichoderma\ polysporum$ yields Cyclosporin A, used as an immunosuppressive drug in organ transplants, so it is correctly matched.
2. Row 2: $Monascus\ purpureus$ (a yeast) yields statins, which lower blood cholesterol, so it is correctly matched.
3. Row 3: $Streptococcus$ yields streptokinase, used as a clot buster in blood vessels, so it is correctly matched.
4. Row 4: $Clostridium\ butylicum$ is the source of butyric acid, not lipase, so this row is wrongly matched, which is option $4$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q169_26f29b79_28102026.png?v=26f29b797394)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q169_b6a6781a_28102026.png?v=b6a6781afcb3)

---

## Q170

Biology · both · Principles of Inheritance and Variation

In a testcross involving $F_1$ dihybrid flies, more parental – type offspring were produced than the recombinant – type offspring. This indicates:

- (1) The two genes are located on two different chromosomes
- (2) Chromosomes failed to separate during meiosis
- **(3)** The two genes are linked and present on the same chromosome
- (4) Both of the characters are controlled by more than one gene

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. If a plant genotype Aa Bb is crossed with aabb then Independent Assortment would result in production of $4$ type of offsprings in equal proportion.
2. Aa Bb – gametes     AB     Ab     aB     ab
3. Aa bb – Gametes     ab     ab     ab     ab
4. Offspring according to independent assortment
5. AaBb     Aabb     aaBb     aabb
6. $1 : 1 : 1 : 1$
7. (Parental)     (Recombinants)     (Parental)
8. Since parental percentage is more than recombinants it is due to linkage between genes A and B.

**Solved independently** (answer withheld)

1. Genes on different chromosomes assort independently, so a dihybrid testcross gives parental and recombinant types in equal numbers (1:1:1:1).
2. More parental than recombinant types means the genes tend to be inherited together, i.e. they are linked on the same chromosome, which is option $3$.

**Subtopic:** Linkage & Recombination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 71)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q170_efba16cb_28102026.png?v=efba16cb6bdd)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q170_7792542b_28102026.png?v=7792542b6084)

---

## Q171

Biology · botany · Organisms and Populations

It is much easier for a small animal to run uphill than for a large animal, because:

- (1) It is easier to carry a small body weight.
- **(2)** Smaller animals have a higher metabolic rate.
- (3) Small animals have a lower $\mathrm{O_2}$ requirement
- (4) The efficiency of muscles in large animals is less than in the small animals.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Smaller animals have higher BMR related with sustained energy production and delayed muscle fatigue.

**Solved independently** (answer withheld)

1. Running uphill needs work $W = mgh$, so the work per unit mass $\frac{W}{m} = gh$ is the same for small and large animals.
2. Small animals have a larger surface-area-to-volume ratio and a higher metabolic rate per unit body mass, so they release energy (ATP) faster per kg of body.
3. Higher energy output per unit mass lets the small animal meet the uphill demand more easily, which is option $2$.

**Subtopic:** Homeostasis, Adaptations and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 71)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q171_1e93b728_28102026.png?v=1e93b72852a8)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q171_03dfbad6_28102026.png?v=03dfbad64515)

---

## Q172

Biology · both · Cell Cycle and Cell Division

Which of the following is not a characteristic feature during mitosis in somatic cells?

- (1) Spindle fibres
- (2) Disappearance of nucleolus
- (3) Chromosome movement
- **(4)** Synapsis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Synapsis is pairing of homologous chromosomes which occurs during meiosis but it is absent in mitosis.

**Solved independently** (answer withheld)

1. Synapsis is the pairing of homologous chromosomes, which happens in zygotene of prophase I of meiosis and does not happen in mitosis, so it is not a feature of mitosis in somatic cells; spindle fibres, disappearance of the nucleolus and chromosome movement all occur in mitosis, so the answer is option $4$.

**Subtopic:** Prophase I and Its Types, Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q172_ccab931f_28102026.png?v=ccab931fd134)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q172_fbdbb80b_28102026.png?v=fbdbb80b016c)

---

## Q173

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following statements is not correct?

- **(1)** Pollen grains of many species can germinate on the stigma of a flower, but only one pollen tube of the same species grows into the style.
- (2) Insects that consume pollen or nectar without bringing about pollination are called pollen/nerctar robbers.
- (3) Pollen germination and pollen tube growth are regulated by chemical components of pollen interacting with those of the pistil.
- (4) Some reptiles have also been reported as pollinators in some plant species.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. More the one pollen tube of same species can grow into the style.
2. It is frequently found in nature.

**Solved independently** (answer withheld)

1. Option $2$ is true: NCERT calls insects that eat pollen or nectar without pollinating pollen/nectar robbers.
2. Option $3$ is true: the pistil recognises compatible pollen through chemical interaction between pollen and pistil components.
3. Option $4$ is true: some reptiles, such as lizards, pollinate some plant species.
4. Option $1$ is false: the pistil rejects incompatible (other-species) pollen and allows compatible pollen to germinate, and the claim that only one same-species tube grows is not what NCERT teaches.
5. The statement that is not correct is option $1$.

**Subtopic:** Pollen-Pistil Interaction and Artificial Hybridisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q173_2cd873a9_28102026.png?v=2cd873a9d8b5)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q173_ac0ad02a_28102026.png?v=ac0ad02a5e61)

---

## Q174

Biology · botany · Anatomy of Flowering Plants

Specialized epidermal cells surrounding the guard cells are called:

- (1) Complementary cells
- **(2)** Subsidiary cells
- (3) Bulliform cells
- (4) Lenticels

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. As subsidiary cells and guard cells both are modification of epidermal cells in which guard cells have chloroplasts which is absent in surrounding subsidiary cells.

**Solved independently** (answer withheld)

1. In NCERT, the epidermal cells next to the guard cells become specialised in shape and size and are called subsidiary cells, which is option $2$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q174_a373419b_28102026.png?v=a373419b387f)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q174_64998961_28102026.png?v=649989615e0f)

---

## Q175

Biology · zoology · Digestion and Absorption

Which of the following guards the opening of hepatopancreatic duct into the duodenum?

- (1) Semilunar valve
- (2) Ileocaecal valve
- (3) Pyloric sphincter
- **(4)** Sphincter of Oddi

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The opening of hepatopancreatic duct into the duodenum is guarded by sphincter of Oddi

**Solved independently** (answer withheld)

1. NCERT: the bile duct and pancreatic duct open together into the duodenum as the common hepato-pancreatic duct, which is guarded by a sphincter called the sphincter of Oddi, so the answer is option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q175_10525216_28102026.png?v=1052521637bf)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q175_f0259687_28102026.png?v=f0259687a839)

---

## Q176

Biology · botany · Morphology of Flowering Plants

Stems modified into flat green organs performing the functions of leaves are known as:

- (1) Cladodes
- (2) Phyllodes
- **(3)** Phylloclades
- (4) Scales

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Stem modified into flat green organs performing the functions of leaves are known as phylloclade whereas phyllode is modification of petiole.

**Solved independently** (answer withheld)

1. Stems flattened into green, leaf-like photosynthetic organs (e.g. $Opuntia$) are called phylloclades, which is option $3$.

**Subtopic:** The Stem · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q176_2b707d76_28102026.png?v=2b707d764071)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q176_f686d2c6_28102026.png?v=f686d2c61245)

---

## Q177

Biology · botany · Microbes in Human Welfare

The primitive prokaryotes responsible for the production of biogas from the dung of ruminant animals, include the:

- (1) Halophiles
- (2) Thermoacidophiles
- **(3)** Methanogens
- (4) Eubacteria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Archaebacteria are considered as most primitive prokaryote which appeared on earth for the first time as it could survive through the anaerobic harsh environment present that time.
2. Halophilus, Thermoacidophiles and Methanogens are Archaebacteria.
3. Methanogens are present in the rumen of cattle that is present in dung as well.
4. It helps in production of methane gas that is a component of biogas.

**Solved independently** (answer withheld)

1. Biogas from cattle dung is mainly methane, made under anaerobic conditions by methanogens such as Methanobacterium, which are primitive prokaryotes (archaebacteria). That is option $3$.

**Subtopic:** Microbes in Production of Biogas · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q177_bfb06974_28102026.png?v=bfb06974e8d0)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q177_f64a831b_28102026.png?v=f64a831be240)

---

## Q178

Biology · botany · Environmental Issues

A river with an inflow of domestic sewage rich in organic waste may result in:

- (1) Drying of the river very soon due to algal bloom.
- (2) Increased population of aquatic food web organisms.
- (3) An increased production of fish due to biodegradable nutrients.
- **(4)** Death of fish due to lack of oxygen.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A river with an inflow of domestic sewage rich in organic waste will reduce the dissolved oxygen (DO) and may result in death of fish due to lack of oxygen.

**Solved independently** (answer withheld)

1. Domestic sewage rich in organic matter is decomposed by aerobic microbes, which consume dissolved oxygen, so the $\text{BOD}$ of the river rises and dissolved $\text{O}_2$ falls sharply, causing death of fish (option $4$).

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q178_d4b12e63_28102026.png?v=d4b12e63eb64)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q178_4003515d_28102026.png?v=4003515d1823)

---

## Q179

Biology · both · Principles of Inheritance and Variation

A cell at telophase stage is observed by a student in a plant brought from the field. He tells his teacher that this cell is not like other cells at telophase stage. There is no formation of cell plate and thus the cell is containing more number of chromosomes as compared to other dividing cells. This would result in:

- (1) Aneuploidy
- **(2)** Polyploidy
- (3) Somaclonal variation
- (4) Polyteny

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Polyploidy cells have a chromosome number that is more than double the haploid number.

**Solved independently** (answer withheld)

1. At telophase the chromosomes have separated and two sets of $2n$ chromosomes are present.
2. No cell plate forms, so cytokinesis fails and both sets stay in one cell, giving $2n + 2n = 4n$.
3. An increase by whole chromosome sets is polyploidy (NCERT: failure of cytokinesis after telophase gives polyploidy), not aneuploidy, which is gain or loss of single chromosomes; so option $2$.

**Subtopic:** Aneuploidy & Polyploidy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 74)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q179_da5141e0_28102026.png?v=da5141e085ac)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q179_35e10229_28102026.png?v=35e10229b5b6)

---

## Q180

Biology · both · Biomolecules

A typical fat molecules is made up of:

- (1) Three glycerol molecules and one fatty acid molecules
- **(2)** One glycerol and three fatty acid molecules
- (3) One glycerol and one fatty acid molecule
- (4) Three glycerol and three fatty acid molecules

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Fat is a triglyceride which is made up of $3$ molecules of fatty acids and one molecule of glycerol.

**Solved independently** (answer withheld)

1. A typical fat is a triglyceride: the three $-OH$ groups of one glycerol molecule are each esterified with one fatty acid, so it is $1$ glycerol $+ 3$ fatty acids, which is option $2$.

**Subtopic:** Lipids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/crops/q180_30d7bbdf_28102026.png?v=30d7bbdf2714)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2016/2016_A/solutions/q180_60c72402_28102026.png?v=60c72402f0d7)

