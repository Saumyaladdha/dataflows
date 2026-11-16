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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Moment of inertia of a disc with a hole in it: subtract the hole's moment about the SAME axis, carried there by the parallel-axis theorem
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The hole's moment about its own centre, $\frac{1}{2}\cdot\frac{M}{4}\cdot\left(\frac{R}{2}\right)^{2} = \frac{MR^{2}}{32}$, is taken straight out of $\frac{MR^{2}}{2}$, and $\frac{16MR^{2}}{32} - \frac{MR^{2}}{32}$ is exactly the printed $\frac{15MR^{2}}{32}$.
- **Why:** This question requires subtracting the cut hole's moment of inertia about the stated axis from the whole disc's, demonstrated by 'a circular hole of diameter R, whose rim passes through the centre is cut', which fixes the hole's own centre $R/2$ away from the axis asked about.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The net force on a coplanar loop beside a straight wire is the difference between the pulls on its two sides parallel to the wire, which lie at different distances
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The stored wire-pair force $F = \frac{\mu_0 I i L}{2\pi d}$ carries $L$ in the numerator, and here the distances $L/2$ and $3L/2$ are themselves multiples of $L$; a student who does not cancel the $L$ turns $\frac{\mu_0 I i L}{2\pi}\cdot\frac{4}{3L}$ into the printed $\frac{2\mu_0 I i L}{3\pi}$.
- **Why:** This question requires computing the net force as the difference of the two side forces at their separate distances, demonstrated by the stem's 'coplanar with a long straight conductor XY' together with the figure's $L/2$ and $L$ labels, which place the near and far sides at $L/2$ and $3L/2$.
- **Note:** The figure was supplied — a printed PNG plus a spec whose labels read L/2, L, X, Y, A, B, C, D, I and i — so the near and far side distances are read off the paper rather than inferred. Options 3 and 4 do not have the dimensions of force, which is a check available on the printed options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Magnetic susceptibility is negative only for diamagnetic materials; it is small and positive for paramagnetic and large and positive for ferromagnetic ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The table of $\chi$ ranges is held as two weak rows and one enormous one, so a student who remembers the magnitudes but not which weak row carries the minus sign takes the row printed beside the right one.
- **Why:** This question requires the stored line on which class of material has negative susceptibility, demonstrated by the stem 'the magnetic susceptibility is negative for' with no material, field or condition supplied to apply a rule to.
- **Note:** nearby_fact rather than look_alike_term by the swap test: put any other class from the same susceptibility table into option 2 and the same sign slip lands on it, so what carries the student is the adjacent row and the matching small magnitude, not the shared '-magnetic' ending of the two words.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Doppler effect with a reflector: the cliff receives the approaching-source frequency and returns that same value to the observer at rest
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  765 Hz is a real frequency in this problem — the direct sound of the receding siren, $800\times\frac{330}{345}$ — so a student who fixes on the stem's 'moves away from an observer' computes the shift those words name and stops before the echo.
- **Why:** This question requires computing the frequency the cliff receives from an approaching source and passing it on unchanged, demonstrated by 'the frequency of sound that the observer hears in the echo reflected from the cliff'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Sharing charge between a charged capacitor and an uncharged one always loses energy, and the fraction lost is $C_2/(C_1+C_2)$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $\frac{U_f}{U_i} = \frac{\frac{1}{2}(10)(V/5)^{2}}{\frac{1}{2}(2)V^{2}} = 0.2$, so 20% is a true number here — the share of the energy still stored — and a student who divides the two energies reads that ratio off as the answer.
- **Why:** This question requires computing the energy before and after the charge redistributes and taking the lost share, demonstrated by 'when the switch S is turned to position 2, the percentage of its stored energy dissipated'.
- **Note:** The figure was supplied — a printed PNG plus a spec carrying a netlist and the labels V, S, 1, 2, 2 μF and 8 μF — so the 8 μF arm standing uncharged at position 2 while S is at 1 is read off the paper.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Single-slit pattern: minima at $a\sin\theta = n\lambda$, and the first secondary maximum lies beyond the first minimum at $a\sin\theta = 3\lambda/2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student holding the secondary maxima as 'odd multiples of $\lambda/2$' and starting the count at $n = 0$ uses $a\sin\theta = \lambda/2$, which with $a = 2\lambda$ gives the printed $\sin\theta = 1/4$.
- **Why:** This question requires finding the slit width from the given minimum and then applying the secondary-maximum condition to it, demonstrated by 'the first minimum is observed at an angle $30^{\circ}$ ... the first secondary maximum is observed at an angle of'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At a point above the earth $V=-GM/r$ and $g=GM/r^2$, so $V/g$ hands you the distance from the centre, and the height is what is left after the radius is taken off
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The one conceptual slip this stem offers is reporting $V/g = 9000$ km, the distance from the centre, instead of subtracting the radius — and 9000 km is not printed. Dividing $5.4\times10^{7}$ by 6.0, 9.8 or 10, doubling or halving that quotient, and rooting or squaring it, all miss 1400, 1600 and 2000 km.
- **Why:** This question requires computing a height from two field quantities measured at the same point, demonstrated by the stem supplying both 'the gravitation potential and the value of g' and 'the radius of earth as 6400 km', so that $V/g$ fixes the distance from the centre and the radius must then be taken off.
- **Note:** The pattern label multi_part_respectively fired on the word 'respectively', but that word attaches to the two data supplied, not to the answer: the options are single heights, so the printed shape is mcq. The stem also prints the potential as $\mathrm{J\,kg^{-2}}$, which must be $\mathrm{J\,kg^{-1}}$; the arithmetic is unaffected and the key stands.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only an accelerated charge radiates: a charge at rest or in uniform motion carries fields but launches no wave
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A charge in steady motion is a current, so it supplies a magnetic field as well as an electric one, and a student holding 'an electromagnetic wave is an E field and a B field together' reads that as enough. Neither field varies in time, so nothing detaches from the charge and nothing propagates.
- **Why:** This question requires the stated fact about which source radiates, demonstrated by the four options being the chapter's own four cases — 'a stationary charge', 'a charge moving at constant velocity', 'a chargeless particle', 'an accelerating charge' — with no quantity to compute and no condition printed to apply.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The small-angle equilibrium of the two hanging spheres ties charge to separation as $q^2 \propto x^3$, and a constant leak rate turns that into the approach speed through $dq/dt = (dq/dx)\,v$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  With $q \propto x^{3/2}$ in hand, a student who differentiates the charge with respect to the separation and reads the result straight off as the speed gets $v \propto x^{1/2}$. The constant leak rate fixes the PRODUCT $(dq/dx)\,v$, so the power enters the speed inverted and the answer is $x^{-1/2}$.
- **Why:** This question requires deriving how the speed depends on the separation by chaining the small-angle force balance with the leak rate, demonstrated by 'the charges begin to leak from both the spheres at a constant rate' together with options that are bare powers of $x$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A travelling pulse keeps its frequency, so its wavelength scales with the speed $\sqrt{T/\mu}$, and the tension at the top of the rope carries the rope's own weight as well as the block's
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 1 and 3 are printed identically as $\sqrt{m_1/m_2}$ in this record, so the option set cannot be audited and no route can be tied to a named option
- **Why:** This question requires deriving the wavelength ratio from the tension at the two ends of the rope, demonstrated by 'a uniform rope of length $L$ and mass $m_1$' carrying 'a block of mass $m_2$', so that the tension rises from $m_2g$ to $(m_1+m_2)g$ while the frequency stays fixed.
- **Note:** Options 1 and 3 are character-for-character identical here, both $\sqrt{m_1/m_2}$, which §5a treats as a duplicated option and therefore as damage in our record rather than a property of the question; the key (2) and the physics are untouched. A reviewer holding the printed paper should check two mechanisms: $\sqrt{m_1/m_2}$, reached by using the rope's own weight as the tension at the top and leaving the block out of the sum, and the inverted ratio, reached by taking $\lambda \propto 1/\sqrt{T}$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A refrigerator's work per second is the heat removed per second divided by its coefficient of performance $T_c/(T_h-T_c)$, with both temperatures in kelvin
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The whole method can be right and still land here: the coefficient of performance is $277/26$, and reading that division as 1.065 instead of 10.65 makes the work ten times too large — $2520/1.065 = 2365$ W against $2520/10.65 = 236.5$ W.
- **Why:** This question requires computing the compressor work from the coefficient of performance, demonstrated by the stem fixing both reservoir temperatures, '$4^{\circ}$C and $30^{\circ}$C', and the heat rate, '600 calories of heat every second'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A column closed at one end resonates only at odd quarter-wavelengths, so for one tuning fork the resonating lengths run 50, 150, 250 cm
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Resonating lengths that run $L$, $2L$, $3L$ belong to a pipe open at BOTH ends; a student who carries that sequence past the printed 'closed at one end' doubles 50 cm and gets 100 cm, where a closed end would sit at an antinode instead of a node.
- **Why:** This question requires applying the closed-column resonance condition to produce a length, demonstrated by 'closed at one end and open at the other' together with 'the smallest length of the column is $50\,\mathrm{cm}$'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An ideal diode conducts with no drop of its own once its anode is the higher-potential end, so the whole $10\,\mathrm{V}$ between A and B falls across the $1\,\mathrm{k\Omega}$ resistor
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The $-6\,\mathrm{V}$ printed at B reads as a supply driving current backwards through the diode, so the branch is taken as reverse biased, and an ideal diode in reverse bias gives exactly $0\,\mathrm{A}$.
- **Why:** This question requires the potential difference read off the figure and divided by the one resistance in the branch, demonstrated by the figure labelling '+4 V' at A and '-6 V' at B across a single '1 kΩ' resistor while the stem says 'Consider the junction diode as ideal'.
- **Note:** The figure was supplied to this step as a spec with its labels and netlist (diode from the A side into n1, then the resistor to B), so the bias direction and the arithmetic could both be audited; the key (2) follows from forward bias.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Heat in a resistor is $\int I^{2}R\,dt$ with $I=dQ/dt$, and for $Q=at-bt^{2}$ the current dies at $t=a/2b$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The charge is the quantity the stem prints, so the span of the process is read off $Q$: $Q$ is back to zero at $t=a/b$, and integrating $I^{2}R$ from $0$ to $a/b$ gives exactly $\frac{a^{3}R}{3b}$.
- **Why:** This question requires $I=dQ/dt$ squared and integrated over the time the current actually flows, demonstrated by the stem's '$Q = at - bt^{2}$' and by the four options differing only in the denominators $6b$, $3b$, $2b$ and $b$.
- **Note:** Option 2 is also the value of $\int I^{2}R\,dt$ carried on to $t=a/b$, where the charge expression returns to zero; the tag follows the printed key, which stops the integral at $t=a/2b$ where the current vanishes.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Wien's displacement law puts the peak of a black body's emission at $\lambda_{max}=b/T$, and the emission falls away on both sides of that peak without reaching zero
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stem's own numbers: $\lambda_{max}=b/T=\frac{2.88\times10^{6}}{5760}=500\,\mathrm{nm}$, which is the wavelength of $U_2$ and so makes $U_2$ the largest of the three and picks out option 4's '$U_2 > U_1$'. The stored key names option 3, '$U_1 > U_2$'. With the same comparison printed twice in opposite senses, the record cannot tell which of the two is the wrong option, so no route to any option can be audited.
- **Why:** This question requires Wien's displacement law applied to this body to order the energy emitted at three wavelengths, demonstrated by the stem printing 'Wien's constant, b = 2.88 × 10^6 nmK' beside 'a temperature of 5760 K' and by the options being bare inequalities.
- **Note:** The tag follows the printed key and nothing here overturns it; what is recorded is an internal inconsistency in our record, which needs a repair task. $2.88\times10^{6}/5760 = 500\,\mathrm{nm}$ exactly, i.e. the second of the three wavelengths the stem lists, so the stem's numbers support '$U_2 > U_1$' (stored as option 4) while the key reads (3), '$U_1 > U_2$'. A reviewer holding the printed booklet should check the order of options 3 and 4 and the answer digit. Once that is settled, the mechanism to expect sits on options 1 and 2, which are wrong on either reading: '$U_1 = 0$' and '$U_3 = 0$' are reached by taking the Planck curve to fall to zero away from its peak, and NCERT's black-body figure rises off the axis on the short-wavelength side, which is what would carry a student to '$U_1 = 0$' rather than to '$U_3 = 0$'. I could not confirm that as the question's one trap while the key and the stem disagree.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Keeping a difference in length fixed under heating requires the two rods to expand by equal absolute amounts, which is $l_1\alpha_1=l_2\alpha_2$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 1 and 3 are stored as the same string, '$\alpha_1^2 l_2 = \alpha_2^2 l_1$', character for character, so one of the four printed answers is absent from the record; a trap named on either of them would sit on an option the paper may never have carried.
- **Why:** This question requires the expansions of the two rods equated so that their difference does not change, demonstrated by the stem's 'If $(l_2 - l_1)$ is maintained same at all temperatures' and by every option being a bare relation between the $\alpha$'s and the $l$'s.
- **Note:** The key is unaffected and is not in question: $l_2(1+\alpha_2\Delta T)-l_1(1+\alpha_1\Delta T)=l_2-l_1$ cancels to $l_2\alpha_2=l_1\alpha_1$, which is option 4 as printed. What is damaged is the option set: options 1 and 3 are identical, so the record is missing one distractor and a repair task is needed. The device to expect once it is restored is a misplaced power, since $\Delta T$ cancels out of the condition and the surviving distractors differ from the key only in where a square is put -- $\alpha$ squared in options 1 and 3, the length squared in option 2.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a common-emitter amplifier the voltage gain is the current gain times $R_L/R_{in}$, and the power gain is the voltage gain times the current gain once more
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The voltage gain comes out at $4$, and then 'the power gain carries the square of the current gain' is applied to that $4$ instead of to the resistance ratio: $4\times0.96^{2}=3.69$, so a correct first number is printed beside a wrong second one.
- **Why:** This question requires the collector current, then the voltage gain, then the power gain computed in turn from the printed resistances, demonstrated by the stem asking for 'the voltage gain and the power gain of the amplifier will respectively be' and by every option printing two numbers that must both hold.
- **Note:** The stem calls $0.96$ the 'current amplification factor' of a common-emitter stage, where that factor is normally greater than one; the key's arithmetic uses $0.96$ as the current gain throughout ($A_v=0.96\times800/192=4$, $A_p=4\times0.96=3.84$) and the tags follow it.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The point in front of one slit sits at $y=d/2$, where the path difference is $\frac{d^{2}}{2D}=\frac{\lambda}{4}$, and $I=I_0\cos^{2}(\phi/2)$ then gives half the maximum
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The light at a point facing slit 1 is taken to be slit 1's own, and one slit alone gives a quarter of the two-slit maximum, so $I_0/4$ is written down -- a true intensity for one open slit, not the intensity with both open.
- **Why:** This question requires the path difference at the point facing one slit, and then the intensity computed from it, demonstrated by the stem's 'the intensity in front of one of the slits' together with '$d = 5\lambda$' and '$D = 10\,d$'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A point on a rotating disc carries two perpendicular accelerations, tangential $\alpha r$ and radial $\omega^2 r$, and the net acceleration is their vector sum
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  $v=\omega r$ is the relation nearest to hand for a spinning disc, so the radial part gets written as $\omega r = 2.0$ instead of $\omega^2 r = 8.0$; set beside the tangential $1.0$ it gives $3.0$, the printed option.
- **Why:** This question requires computing two acceleration components from the stem's numbers and combining them, demonstrated by 'Its net acceleration in $\mathrm{ms^{-2}}$ at the end of $2.0\,\mathrm{s}$' with only a radius and a constant angular acceleration supplied.
- **Note:** The stem reads 'free to tum about an axis', a scanning slip for 'turn'; it does not change what is asked, and the key checks out at $\sqrt{65} = 8.06 \approx 8.0$. Worth recording for a reviewer that the stem's 'approximately' makes the radial-only value $8.0$ and the full $8.06$ land on the same keyed option, so dropping the tangential component is not punished here.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A particle's de Broglie wavelength is $h/\sqrt{2mE}$ while a photon's is $hc/E$, so comparing them at equal energy leaves a factor $1/c$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The photon stored as $\lambda = h/E$ instead of $\lambda = hc/E$ loses the $c$, and the ratio then collapses to exactly $\left(\frac{E}{2m}\right)^{1/2}$ — the keyed expression with its $1/c$ stripped off.
- **Why:** This question requires building one symbolic expression out of two different wavelength relations, demonstrated by options such as '$\frac{1}{c}\left(\frac{E}{2m}\right)^{\frac{1}{2}}$' that combine $E$, $m$ and $c$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In rolling from rest down an incline only the shape factor $k^2/R^2$ decides the race, mass and radius cancelling, and the sphere's $2/5$ beats the disc's $1/2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  With the altitude, the length and the radii all equalised and mass cancelling out of $Mgh = \frac12 Mv^2$, there seems to be nothing left to separate the two bodies, so the free-fall result $v = \sqrt{2gh}$ is applied and the race is called a tie.
- **Why:** This question requires applying the rolling-race rule to two named bodies with no quantity produced, demonstrated by options that are bodies and verdicts: 'Disk', 'Sphere', 'Both reach at the same time'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At minimum deviation the ray crosses the prism symmetrically, so $r = A/2$, $\delta_m = 2i - A$ and $\mu = \sin i/\sin(A/2)$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The symmetry at minimum deviation is remembered as 'the angles are equal here', and the equal angle to hand is the printed $i = 45^\circ$, so the deviation is reported as $45^\circ$ while the index $\sqrt2$ is worked out correctly.
- **Why:** This question requires computing two values from the stem's numbers, demonstrated by 'the angle of minimum deviation and refractive index of the material of the prism respectively' with $i = 45^{\circ}$ and $A = 60^{\circ}$ given.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At closest approach the whole kinetic energy has turned into Coulomb potential energy, so $r_0 = 4kZe^2/(mv^2)$ and at fixed speed $r_0$ falls as $1/m$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Two remembered proportionalities get chained without inverting the second: $r_0 \propto 1/E$ and $E \propto m$ are read straight through as $r_0 \propto m$.
- **Why:** This question requires only how one quantity varies with another, demonstrated by the stem asking what 'its distance of closest approach from the nucleus depends on m as' and by options that are bare powers of $m$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Under a constant tangential acceleration the speed grows along the arc as $v^2 = 2a_t s$, and two revolutions from rest means $s = 2 \times 2\pi r$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Counting the path as one circumference instead of two halves the distance, and $a_t = 0.16/(2 \times 0.402)$ comes out at $0.199$ — exactly the printed $0.2\,\mathrm{m/s^2}$.
- **Why:** This question requires computing an acceleration from the stem's numbers, demonstrated by 'What is the magnitude of this acceleration if the kinetic energy of the particle becomes equal to $8 \times 10^{-4}\,\mathrm{J}$ by the end of the second revolution'.
- **Note:** Option 4 is stored as '$\frac{0.2\mathrm{m}}{\mathrm{s^2}}$', a LaTeX rendering of $0.2\,\mathrm{m/s^2}$ as a fraction while the other three options print their units inline. The value is legible and unchanged, so the record is not treated as damaged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a fixed mass of a given gas the r.m.s. speed is set by temperature alone, $v_{rms}\propto\sqrt{T}$, so changing the pressure changes nothing
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each named mis-step on the printed numbers was run against the options: dropping the square root gives $266.7$, using $127/27$ in place of $400/300$ gives $433.6$, inverting the temperature ratio gives $100\sqrt{3}=173.2$, and carrying the pressure ratio into $v=\sqrt{3p/\rho}$ with $\rho$ held fixed gives $44.7$. The three wrong options are $141.4$, $47.1$ and $33.3$, so no route reaches any of them.
- **Why:** This question requires the factor by which $v_{rms}$ changes when the temperature moves from $300\,\mathrm{K}$ to $400\,\mathrm{K}$, demonstrated by the second pressure '$0.05 \times 10^{5}\,\mathrm{Nm^{-2}}$' never entering the answer $\frac{400}{\sqrt{3}}$.
- **Note:** The pressure data is not used by the answer. All three wrong options lie below the given $200\,\mathrm{ms^{-1}}$ while the temperature rises, so the direction of the change alone separates the key from the rest. Key (2) checks out: $200\sqrt{4/3}=400/\sqrt{3}$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Ampere's law counts only the current enclosed, so $B\propto r$ inside a uniformly conducting wire and $B\propto 1/r$ outside it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The exterior law $B=\mu_0 I/2\pi r$ is the one carried for a straight wire, and used at both $\frac{a}{2}$ and $2a$ it gives $B/B'=\frac{2a}{a/2}=4$.
- **Why:** This question requires the factor between the field at two radial distances, demonstrated by the stem fixing them as '$\frac{a}{2}$ and $2a$' with the current 'uniformly distributed over its cross-section', which puts one point under a different law from the other.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A position vector of constant length turning at constant $\omega$ is uniform circular motion: the velocity is tangential and the acceleration is centripetal, $\vec{a}=-\omega^2\vec{r}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The outward 'centrifugal' picture of circular motion keeps the correct tangential velocity and flips the sense of the acceleration, which is exactly what option 4 prints.
- **Why:** This question requires the uniform-circular-motion rule applied to a printed position vector, demonstrated by option 3's clauses 'Velocity is perpendicular to $\vec{r}$ and acceleration is directed towards the origin' being read off $\vec{v}$ and $\vec{a}=-\omega^2\vec{r}$ with no quantity produced.
- **Note:** E1's pattern label was `statement_options`, retired vocabulary; recorded as `statements` because the stem prints the judge-the-claims instruction 'Which of the following is true?'. `half_right` is also legal on option 4, which has two clauses, but the clause that fails does so by inverting a direction, and `reversed` names that mechanism while `half_right` only reports that one clause failed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A body completes a vertical loop only if gravity alone can supply the centripetal force at the top, which with the climb of $2R$ fixes the entry speed at $\sqrt{5gR}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\sqrt{gR}$ is the minimum speed AT THE TOP of the loop, the companion result stored alongside $\sqrt{5gR}$, so reaching for the stored loop number lands on the top-of-loop speed the stem did not ask for.
- **Why:** This question requires computing the entry speed from the top-of-loop condition chained to the climb of $2R$, demonstrated by the stem asking for 'the minimum velocity with which a body of mass $m$ must enter a vertical loop of radius $R$' while every option is a $\sqrt{ngR}$ expression.
- **Note:** $\sqrt{4gR}$, the value from letting the body just reach the top with zero speed, is not printed, so that particular slip lands nowhere in the option set. The three wrong options are the loop's other stored speeds plus the height-$R$ energy slip.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Two illuminations of the same surface share one work function, and eliminating it between the two Einstein equations fixes the threshold wavelength
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $4\lambda$ is the threshold for the standard version of this setup, where the stopping potentials are $3V_0$ at $\lambda$ and $V_0$ at $2\lambda$; this paper prints $V$ and $\frac{V}{4}$, whose answer is $3\lambda$, and the stored $4\lambda$ is sitting in the options.
- **Why:** This question requires eliminating the work function between two Einstein equations, demonstrated by the stem supplying the second illumination 'with radiation of wavelength $2\lambda$, the stopping potential is $\frac{V}{4}$', which is the only thing that pins the common $\varphi$ down.
- **Note:** Option 1's route is the stored answer to the $3V_0$-at-$\lambda$, $V_0$-at-$2\lambda$ version of this problem, whose threshold is $4\lambda$. If that version is an NCERT exercise then `old_ncert_answer` would be the sharper label, but the NCERT line cannot be named from this packet, so the live family `answers_other_question` is used instead.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The adiabat through a point is steeper than the isotherm through it, so for the same halving of volume the adiabatic path encloses the larger area and costs more work
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The comparison stored for these two curves is the expansion one, where the isotherm lies above the adiabat and yields more work; the stem prints 'compressed', which flips it, and option 1 is the un-flipped version.
- **Why:** This question requires telling two neighbouring processes apart over the same volume change, demonstrated by option 3 offering that the two 'require the same amount of work' and option 4 making the verdict 'depend upon the atomicity of the gas'.
- **Note:** E1's pattern label was `statement_options`, retired vocabulary. The stem ends at 'Then:' and only supplies a scenario, so under rule 1 sentence-length options alone leave this `mcq` — the opposite call from q027 in this group, decided on the printed instruction.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On a potentiometer the balance length is proportional to the emf actually balanced, so the supporting and opposing connections balance $\varepsilon_1+\varepsilon_2$ and $\varepsilon_1-\varepsilon_2$, not the two cells separately
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $\varepsilon \propto l$ is applied to each printed balance length as though one cell were in the circuit at a time, giving $50:10 = 5:1$, when the two lengths balance the series sum and the series difference
- **Why:** This question requires the two balance lengths read as balancing $\varepsilon_1+\varepsilon_2$ and $\varepsilon_1-\varepsilon_2$ and the pair solved, demonstrated by 'connected in series first to support one another and then in opposite direction'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a near object the telescope's tube length is the objective's image distance plus the eyepiece focal length, because the eyepiece must receive that image at its own focus
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $1/v = 1/40 - 1/200$ puts the objective's image at exactly 50 cm and 50.0 cm is printed, so the solution ends one step early — that distance answers where the image forms, not how far apart the lenses sit
- **Why:** This question requires the objective's image distance computed and the eyepiece focal length added to it, demonstrated by 'To view an object $200\,\mathrm{cm}$ away from the objective' — the object is not at infinity, so $f_o+f_e$ is not the separation.
- **Note:** E1 called this multi_part_respectively, but 'respectively' in the stem only distributes the two focal lengths over the two lenses; one distance is asked and each option is a single length, so the printed shape is a plain mcq. Worth recording: $f_o+f_e = 44$ cm, the separation for an object at infinity, is not among the options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A floating body's density is the length-weighted average of the densities it is immersed in, because its weight equals the buoyancy from each liquid layer it displaces
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The balance $dL = \rho(1-p)L + n\rho pL$ is set up correctly and the $-p$ is carried in as $+p$, turning $\rho\{1-p+np\}$ into $\rho\{1+p+np\} = \{1+(n+1)p\}\rho$
- **Why:** This question requires the floating condition written across both liquids and solved for $d$, demonstrated by 'the cylinder floats with its axis vertical and length $pL(p < 1)$ in the denser liquid'.
- **Note:** The four options form a 2x2 grid — a leading 1 or 2 crossed with $(n-1)p$ or $(n+1)p$ — and the stem's 'The height of each liquid is h' is never needed for the answer.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** $Y=(A+B)\cdot C$: an AND output is 1 only when both its inputs are 1, so a 1 leaving the OR gate does nothing unless C is also 1
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A=1 with B=1 drives the OR output to 1, and that is a true statement about the OR gate's output rather than about Y, which also needs C=1 at the AND gate
- **Why:** This question requires the two gates and their wiring read off the figure before any truth table can be applied, demonstrated by 'To get output 1 for the following circuit' with the gate identities printed only in the diagram.
- **Note:** E1 called this statement_options, but the options are input assignments such as 'A = 1, B = 0, C = 1', not statements to be judged, so the printed shape is a plain mcq carrying a figure. The figure reached this step as caption and spec — A and B into an OR gate, that output and C into an AND gate — giving $Y=(A+B)\cdot C$, which agrees with the printed key. All three wrong options set C=0, so one mechanism covers the whole distractor set; wrong_site_attacked (the output read at the earlier stage) was considered and answers_other_question chosen because option 3 is a true answer about the OR node.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Mechanical equivalent of heat: the fall's potential energy turns into heat, and only the stated fraction of that heat supplies the latent heat the ice needs to melt
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Setting $mgh = mL$ gives $h = L/g = 3.4\times10^{5}/10 = 34$ km, which is the height if all the heat melted the ice, while the stem allows only one-quarter of it
- **Why:** This question requires the fall energy equated to the latent heat with the stated fraction kept in, demonstrated by 'Only one-quarter of the heat produced is absorbed by the ice'.
- **Note:** Our stem prints the latent heat as $3.4 \times 1^{5}\,\mathrm{J/kg}$: the exponent has lost its zero and must read $3.4\times10^{5}\,\mathrm{J/kg}$, which the printed key confirms, since $4L/g = 136$ km is option 3. Tagged as printed, with every route checked against $3.4\times10^{5}$; the stem needs that one repair.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Escape velocity goes as $R\sqrt{\rho}$, because a body's own surface gravity rises with both its density and its radius
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Using $v_e = \sqrt{2gR}$ with the earth's $g$ makes $v \propto \sqrt{R}$, so doubling the radius alone gives $1:\sqrt{2}$, but $g$ is not the same on a planet of twice the density and twice the radius
- **Why:** This question requires escape velocity re-expressed in density and radius so that both doublings can be scaled, demonstrated by 'whose radius and mean density are twice as that of earth'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The magnitudes of the sum and the difference of two vectors are equal only when the cross-term vanishes, that is when the vectors are perpendicular
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Subtraction is addition of the reversed vector, so a student testing the extreme angles reads $180^{o}$ as the angle where the sum and the difference trade places and therefore match; at $180^{o}$ they are $|A-B|$ and $A+B$, which are equal only if one of the vectors is zero
- **Why:** This question requires computing the angle that satisfies a stated vector condition, demonstrated by "the magnitude of sum of two vectors is equal to the magnitude of difference", which only yields an angle after the two magnitudes are squared and compared.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The last line of a spectral series is the series limit, the $n=\infty$ transition, so the Balmer limit has wave number $R/4$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Writing the Rydberg formula with the quantum numbers unsquared, $\bar{\nu}=R\left(\frac{1}{2}-\frac{1}{\infty}\right)$, gives $0.5\times10^{7}\,\mathrm{m^{-1}}$ instead of $R/2^{2}$
- **Why:** This question requires computing a wave number from the given constant, demonstrated by "Given the value of Rydberg constant is $10^{7}\,\mathrm{m^{-1}}$" together with options that are numbers rather than transitions.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Instantaneous power is $\vec{F}\cdot\vec{v}$, and when the force varies with time the velocity has to be got by integrating $\vec{a}=\vec{F}/m$ component by component
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Integrating the $y$ acceleration by dividing by the coefficient but not raising the power, $\int 3t^{2}\,dt$ read as $t^{2}$ instead of $t^{3}$, and then dotting correctly gives $2t^{3}+3t^{4}$
- **Why:** This question requires computing an expression from the given force law, demonstrated by "What power will be developed by the force at the time t?" with options that are expressions in $t$ rather than named quantities.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average power in a series LCR circuit is $V_{rms}I_{rms}\cos\phi=I_{rms}^{2}R$; the reactances store energy and dissipate none
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Using $P=V_{rms}I_{rms}$ and leaving out the power factor gives $\frac{(10/\sqrt{2})^{2}}{65.6}=0.76\,\mathrm{W}$, the printed option
- **Why:** This question requires computing a dissipated power from circuit values, demonstrated by "The power loss in A.C. circuit is" with four numerical watt values as options.
- **Note:** Tagged as printed and the key is left alone. Working the stem's own numbers through $P=V_{rms}^{2}R/Z^{2}$ with $\omega=340\,\mathrm{rad\,s^{-1}}$ gives about $0.46\,\mathrm{W}$, which is nearest to the printed answer $0.51\,\mathrm{W}$ but not equal to it; a reviewer with the printed solution should check the rounding used for $X_C$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Distance covered over a time interval is the definite integral of the speed between the two times, not the speed function evaluated at an end point
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Integrating by raising each power but forgetting to divide by the new power turns $\int_1^2(\mathrm{A}t+\mathrm{B}t^{2})dt$ into $\mathrm{A}(2^{2}-1^{2})+\mathrm{B}(2^{3}-1^{3})=3\mathrm{A}+7\mathrm{B}$
- **Why:** This question requires computing a symbolic distance from a given speed law, demonstrated by "the distance travelled by it between $1\,\mathrm{s}$ and $2\,\mathrm{s}$" with options that are expressions in A and B.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Self-inductance is the flux linkage per unit current, $L=N\Phi/I$, so the number of turns and the current both have to enter
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Multiplying $1000$ turns by $4\times10^{-3}\,\mathrm{Wb}$ gives the flux linkage $4$, and the division by $I=4\,\mathrm{A}$ is never done, so the printed $4\,\mathrm{H}$ is the linkage read as an inductance
- **Why:** This question requires computing an inductance from turns, current and flux, demonstrated by "the magnetic flux linked with each turn of the solenoid is $4 \times 10^{-3}\,\mathrm{Wb}$" with henry values as options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In an ideal capacitor the current leads the applied voltage by a quarter cycle, so the average power over a full cycle is zero: the capacitor stores energy and returns it instead of consuming it
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The $90^{\circ}$ is held but the sense is taken from the L circuit, where the current does sit behind the voltage; in a capacitor the charge has to arrive before the voltage across it exists, so $I=\omega C V_0\cos\omega t$ runs a quarter cycle ahead.
- **Why:** This question requires the capacitor's phase relation applied to this source in order to grade four rival claims about it, demonstrated by option 2 reading "Over a full cycle the capacitor C does not consume any energy from the voltage source" against three phase claims, with no quantity asked for.
- **Note:** Option 1 is printed in our record as "Current I(t), legs voltage V(t) by $90^{\circ}$"; read as "lags" it is false and the key stands, read as "leads" it would be true and the item would carry two correct answers, so it is tagged on the "lags" reading and a reviewer with the printed paper should confirm the word. Trap axis: I applied the swap test of §5.1 - the inductor result does sit beside the capacitor result in the chapter, so nearby_fact is reachable, but what the option does to the printed relation is invert its direction while keeping its magnitude, which is what reversed names. Shape: E1 called this statement_options because each option is a full claim; on the current axis rule 1 needs a printed lettered block or an instruction to judge statements, and this stem has neither, so qtype is mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** For mirrors the sign of the magnification settles real against virtual -- $m<0$ is real and inverted, $m>0$ is virtual and erect -- while a convex mirror is confined to virtual images with $|m|<1$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Real against virtual is decided from the SIZE of $m$ instead of its sign, so $|m|=\frac{1}{2}$ is read as a small virtual image and $|m|=2$ as a big real one. That hands B the virtual image and C the real one, which is the opposite of what the signs say.
- **Why:** This question requires the mirror sign convention applied to four printed magnifications, demonstrated by column 1 supplying only '$m = -2$', '$m = -\frac{1}{2}$', '$m = +2$', '$m = +\frac{1}{2}$' and column 2 asking which mirror and which image each one implies.
- **Note:** Option 2's third entry reads 'd $\rightarrow$ a and b', a column-2 label where a column-1 label belongs, and its fourth entry pairs two image types with no mirror; option 4's A entry likewise reads 'c and d', two image types and no mirror. These three entries read like transcription slips and should be checked against the printed paper. The trap recorded does not rest on them -- option 4's B, C and D rows are intact and carry the route. The key as printed, (1), is consistent with the sign convention: $m=-2$ and $m=-\frac{1}{2}$ are real and so concave, $m=+2$ is virtual and enlarged and so concave, $m=+\frac{1}{2}$ is virtual and diminished and so convex.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On a banked road friction and the bank angle add to supply the centripetal force, and the force balance fixes the skid speed at $v=\sqrt{gR\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The balance gives $\frac{v^2}{R}=g\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}$, and the R is cleared by dividing instead of multiplying, leaving $\sqrt{\frac{g}{R}(\cdots)}$ - a reciprocal time rather than a speed.
- **Why:** This question requires the maximum-speed expression to be derived from the banked-road force balance, demonstrated by all four options printing the same factor $\frac{\mu_s+\tan\theta}{1-\mu_s\tan\theta}$ and differing only in whether it multiplies $gR$, $gR^2$, $g/R$ or $g/R^2$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** A lone pair presses bonding pairs together, so the bond angle falls from 109.5 degrees in CH4 to 107 degrees in NH3 to 104.5 degrees in H2O
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A lone pair takes more room than a bond pair, and carried one step too far that becomes 'more lone pairs, wider angle', which puts water above ammonia and makes statement 3 read as the false one. The extra room is taken from the bonding pairs, not given to them, so H2O's 104.5 degrees sits below NH3's 107 degrees.
- **Why:** This question requires the taught bond angles of CH4, NH3 and H2O to be compared pairwise, demonstrated by the option 'The H - O - H bond angle in $\mathrm{H_2O}$ is larger than the H - C - H bond angle in $\mathrm{CH_4}$', which is settled only by 104.5 degrees against 109.5 degrees.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** NaNH2 removes the acidic hydrogen from a terminal alkyne and the alkyl halide joins at that same carbon, so ethyne gives 1-butyne and 1-butyne gives 3-hexyne
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  NaNH2 is met twice in this chapter, as the base that makes an acetylide and as the reagent that shifts a triple bond along a chain, and a student who lets the second meaning run writes the internal alkyne for X while still reaching 3-hexyne for Y by the second ethylation. Seeing the half they are sure of printed correctly carries the wrong half with it.
- **Why:** This question requires the product of each acetylide alkylation to be named, demonstrated by the stem 'In the reaction X and Y are:' over two identical arrows reading '(1) NaNH₂ /liq. NH₃' and '(2) CH₃ CH₂ Br', with every option fixing X and Y together.
- **Note:** E1's pattern called this statement_options; the printed options are 'X = … ; Y = …' pairs accepted or rejected whole, so the shape recorded here is two_part. The scheme was supplied both as transcribed text and as a printed figure, so the question is complete as stored.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Acid strength of the chlorine oxoacids rises with chlorine's oxidation state, because each added oxygen pulls charge away from the O-H bond and stabilises the anion
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The chapter prints a second series for these same four acids - oxidising power, HClO > HClO2 > HClO3 > HClO4 - and a student who reaches for that series here wants HClO at the strong end of an increasing order. Acid strength runs the other way, climbing with chlorine's oxidation state from +1 in HClO to +7 in HClO4.
- **Why:** This question requires the four chlorine oxoacids to be ranked by acid strength, demonstrated by the stem 'the correct order of acidity is' over options that differ only in where $\mathrm{HClO}$ and $\mathrm{HClO_4}$ sit in the sequence.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a first-order reaction the rate is proportional to concentration, so two rates ten seconds apart give $k=\frac{1}{10}\ln\frac{0.04}{0.03}$ and the half-life is $0.693/k$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I worked the named wrong routes this rate pair invites and none of them lands on a printed value: using $\log$ in place of $\ln$ gives $k=0.0125\,\mathrm{s^{-1}}$ and $t_{1/2}=55.5\,\mathrm{s}$, taking the interval as the 20 s reading instead of the 10 s gap gives $k=0.0144\,\mathrm{s^{-1}}$ and $48.2\,\mathrm{s}$, and treating the fall as linear gives about 20 s. The three distractors are the answer plus 10, 20 and 30 s.
- **Why:** This question requires $k$ to be recovered from two rates of the same first-order reaction and converted to a half-life, demonstrated by the stem giving '$0.04\,\mathrm{mol\,l^{-1}s^{-1}}$ at 10 second and $0.03\,\mathrm{mol\,l^{-1}s^{-1}}$ at 20 seconds' and asking for 'The half-life period of the reaction'.
- **Note:** The three distractors sit on a 10 s ladder above the answer (24.1, 34.1, 44.1, 54.1 s), which is why no_trap is recorded as the finding rather than left as an unexamined gap; the closest named wrong route, log for ln, gives 55.5 s and not the printed 54.1 s.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Adsorption gives out heat and takes away the gas molecules' freedom of movement, so $\Delta H$ and $\Delta S$ are both negative while $\Delta G$ stays negative as long as $|\Delta H|$ exceeds $|T\Delta S|$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Spontaneity and 'entropy increases' are stored together, so once $\Delta H$ is set negative for an exothermic process and $\Delta G$ negative for one that proceeds on its own, the third sign is read off the second law and made positive. A gas molecule held on a surface has lost its freedom to move, so the system's $\Delta S$ is negative, and it is the exothermic $\Delta H$ that keeps $\Delta G$ negative.
- **Why:** This question requires the three thermodynamic signs stated for adsorption to be held together as one set, demonstrated by the stem 'Which one of the following characteristics is associated with adsorption?' over options that each fix $\Delta G$, $\Delta H$ and $\Delta S$ at once.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Each periodic trend has to be matched to the species it governs: isoelectronic ions shrink as nuclear charge rises, nitrogen's half-filled $ns^2np^3$ shell lifts its ionisation enthalpy above oxygen's, and chlorine's electron gain enthalpy is more negative than fluorine's
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Fluorine is the smallest atom in the period, and a student who reads the four species as atoms rather than as ions marks this order as the one placed backwards. All four here carry ten electrons, and across an isoelectronic set size is fixed by nuclear charge, which falls from Al to F, so $\mathrm{F^-}$ really is the largest.
- **Why:** This question requires four printed orders each to be checked against the property named against it, demonstrated by the option '$\mathrm{Al^{3+}} < \mathrm{Mg^{2+}} < \mathrm{Na^{+}} < \mathrm{F^{-}}$ (increasing ionic size)' carrying its own property label rather than sharing one with the others.
- **Note:** The printed answer line accepts two options, 'Solution: (2,3)', and explains only option 2 (N's half-filled $ns^2np^3$ against O's $ns^2np^4$). Option 3 fails as well, chlorine's electron gain enthalpy being more negative than fluorine's. Tagged as printed; with 2 and 3 both accepted, only options 1 and 4 are wrong, so only those two are accounted for.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** $\mathrm{Mg^{2+}}$ is the ion of chlorophyll and of ATP complexes, while $\mathrm{Ca^{2+}}$ is the ion of bone, blood clotting, muscle contraction and the regular heartbeat
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The magnesium roles and the calcium roles are printed as two paragraphs of one section, so a student who holds the roles as a single pool reads ATP as calcium's job and marks the ATP statement as the false one. The ion complexed to ATP is $\mathrm{Mg^{2+}}$, so statement 1 is true and the negated heartbeat statement is the false one. Test applied: 'magnesium' and 'calcium' do not resemble each other as words, so what makes the swap reachable is that the two lists sit side by side, which is nearby_fact rather than look_alike_term.
- **Why:** This question requires the role the textbook assigns to each named s-block ion, demonstrated by option 3 printing the heartbeat role negated as '$\mathrm{Ca^{2+}}$ ions are not important in maintaining the regular beating of the heart'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hydrogen's taught properties: protium is the abundant isotope and tritium the rare radioactive one, dihydrogen is a reducing agent, and in ionic salts hydrogen appears as the hydride anion $\mathrm{H^-}$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Hydrogen ionises to $\mathrm{H^+}$ in every acid a student has handled, so a sentence denying a hydrogen cation reads as the incorrect one. The statement is fenced to ionic salts, where hydrogen sits as the hydride anion $\mathrm{H^-}$ in $\mathrm{NaH}$ or $\mathrm{CaH_2}$, and a bare proton has no lattice to occupy.
- **Why:** This question requires the printed facts about hydrogen's isotopes and dihydrogen's reducing behaviour, demonstrated by option 1's claim that hydrogen 'has three isotopes of which tritium is the most common'.
- **Note:** accepted_answers holds both '1' and '4', and answer_line_as_printed reads 'Solution: (1,4)', so options 1 and 4 are both official answers and carry no trap or filler entry; only options 2 and 3 are accounted for. Tagged as printed, with no re-judging of the key.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The rapid interconversion of a carbonyl compound carrying an alpha-hydrogen with its enol form is called keto-enol tautomerism
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Carbonylation' is built from the stem's own word 'carbonyl', so a student who is sure the equilibrium is real but has not fixed its name takes the name that echoes the compound. Carbonylation is the insertion of carbon monoxide into a bond; the alpha-hydrogen equilibrium is keto-enol tautomerism. Test applied: replace 'carbonylation' with an unlike coinage and the pull vanishes, so the resemblance to 'carbonyl' is doing the work, not the position of a neighbouring fact.
- **Why:** This question requires the name the textbook gives the alpha-hydrogen equilibrium, demonstrated by options 2, 3 and 4 carrying one identical sentence that differs only in its final term - 'aldehyde-ketone equilibration', 'carbonylation', 'keto-enol tautomerism'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Equal $K_{sp}$ does not mean equal solubility: $s=\sqrt{K_{sp}}$ for an $\mathrm{MY}$ salt but $s=(K_{sp}/27)^{1/4}$ for an $\mathrm{NY_3}$ salt, so the 1:3 salt dissolves more
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Reading $K_{sp}$ as a measure of solubility itself makes two salts sharing a $K_{sp}$ equally soluble. The expression carries the stoichiometry: $K_{sp}=s^2$ gives $s=7.9\times10^{-7}$ M for $\mathrm{MY}$, while $K_{sp}=27s^4$ gives $s=3.9\times10^{-4}$ M for $\mathrm{NY_3}$.
- **Why:** This question requires each salt's molar solubility worked out from the shared $K_{sp}$ through its own stoichiometry, demonstrated by option 1's claim that 'the molar solubilities of $\mathrm{MY}$ and $\mathrm{NY_3}$ in water are identical'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amino acid residues in a protein are joined by peptide bonds, the amide link formed between $-\mathrm{COOH}$ and $-\mathrm{NH_2}$; glycosidic bonds join sugar units instead
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The Biomolecules chapter names its linkages class by class, and the glycosidic bond - first met as the alpha-1,4 link of maltose and starch - is the one printed before proteins are reached. A student who reaches for 'the linkage that joins monomers' lands on the alpha-glycosidic bond, which joins sugars, not amino acids. Test applied: 'glycosidic' and 'peptide' do not resemble each other at all, so position in the chapter is carrying the student, which is nearby_fact.
- **Why:** This question requires the name the textbook gives the amino-acid linkage, demonstrated by the stem 'In a protein molecule various amino acids are linked together by' set against two glycosidic options and a dative option.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Natural rubber is cis-1,4-polyisoprene, with the cis configuration at every double bond; the all-trans isomer of polyisoprene is gutta percha
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  All-trans polyisoprene is printed in the same lines as natural rubber, as gutta percha, so a student who holds both configurations but not which name owns which takes trans. The cis arrangement is what stops the chains packing and leaves rubber elastic, while the all-trans isomer is the hard, inelastic one. Test applied: 'cis' and 'trans' are not look-alike words, and what makes trans reachable is that the chapter prints it beside natural rubber, so this is nearby_fact.
- **Why:** This question requires the configuration the textbook states for natural rubber, demonstrated by the options offering 'All cis', 'All trans', alternate and random configurations with no criterion printed to work it out from.
- **Note:** type_patterns called this statement_options on '15 full-statement options', but the printed shape is a stem completed by four short configuration phrases, so the shape recorded here is mcq. The stem reads 'Nutural rubber has:', an apparent typo for 'Natural'; tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each metallurgical operation belongs to a particular metal: cyanide leaching for gold, froth floatation for sulphide ores, electrolysis of molten alumina for aluminium, zone refining for semiconductor-grade germanium
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Option 3 carries both of the pairs a student can verify at once -- froth floatation with dressing of $\mathrm{ZnS}$ and electrolytic reduction with extraction of $\mathrm{Al}$ -- so the two rows that are actually in question, (a) and (d), get taken on trust; the cyanide process leaches $\mathrm{Au}$ and zone refining gives ultrapure $\mathrm{Ge}$, so both untested rows are the wrong way round.
- **Why:** This question requires the use NCERT states for each isolation process -- which metal it is carried out on, demonstrated by the rows 'Zone refining' against 'Ultrapure $\mathrm{Ge}$' and 'Froth floatation process' against 'Dressing of $\mathrm{ZnS}$', where nothing in the stem supplies a criterion to work the pairing out from.
- **Note:** Column II carries five entries against column I's four, so '(v) Purification of Ni' is never used by the key; it appears only inside options 2 and 4. The retired §5.2 name for option 3's layout is parallel_order_decoy; per §5.0 it was mapped to its live §5.1 family, half_right, since what the option offers is a four-part code correct in two parts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Acidified dichromate oxidises $\mathrm{SO_2}$ to sulphate and is itself reduced from orange Cr(VI) to green Cr(III) as $\mathrm{Cr_2(SO_4)_3}$
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Acidified $\mathrm{KMnO_4}$ is the oxidant $\mathrm{SO_2}$ discharges the colour of, and it is printed in the same short list of $\mathrm{SO_2}$'s reducing reactions, so 'decolourized' is carried across to dichromate. Dichromate does not lose its colour — orange Cr(VI) becomes green Cr(III).
- **Why:** This question requires the product and the colour change of the acidified dichromate–$\mathrm{SO_2}$ redox reaction, demonstrated by the option 'Green $\mathrm{Cr_2(SO_4)_3}$ is formed.'
- **Note:** E1's pattern called this plain_mcq; the stem reads 'Which one of the following statements is correct' and each option is a whole claim to be graded, so the printed shape is statements.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lanthanoids fill $4f$ straight through, and $5d$ takes an electron only where that leaves $4f$ half-filled, as in Gd
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Gd's $4f^{7}5d^{1}6s^{2}$ is the one configuration in the lanthanoid table printed with a $5d$ electron, and sitting between Eu and Tb it is read as the pattern of the row, so the $5d^{1}$ is carried onto both neighbours. Only Gd gains anything by it: Eu stops at $4f^{7}6s^{2}$ and Tb goes on to $4f^{9}6s^{2}$.
- **Why:** This question requires the lanthanoid filling rule applied to three given atomic numbers, demonstrated by the stem printing '(Atomic no. 63)', '(Atomic NO. 64)' and '(Atomic No. 65)' instead of naming the elements' configurations.
- **Note:** E1's pattern called this statement_options on option length; each option is a triple of electronic configurations accepted or rejected whole, and all three terms vary across the options, so the printed shape is a multi-part answer and qtype is two_part. On the trap axis the nearby_fact / look_alike_term test was applied: Eu, Gd and Tb do not resemble one another as names, so what carries the $5d^{1}$ across is their adjacency in the printed table — position, hence nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** One orbital fixes $n$, $l$ and $m_l$, so by Pauli's exclusion principle its two electrons can differ only in spin
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The magnetic quantum number is the one taught as 'the number that tells orbitals apart' — it separates $p_x$, $p_y$ and $p_z$ — so it is offered here for telling two electrons apart. It answers which orbital, and the stem has already put both electrons in the same one.
- **Why:** This question requires the stated fact that the two electrons of one orbital differ only in spin, demonstrated by the stem 'Two electrons occupying the same orbital are distinguished by' with the four quantum numbers as the options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Copper reduces concentrated nitric acid only as far as $\mathrm{NO_2}$, while dilute nitric acid is reduced to NO
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  NO is the gas in the copper-and-dilute-$\mathrm{HNO_3}$ equation, and a student carrying 'copper plus nitric acid gives NO' with no concentration attached drops the stem's printed 'conc.'. Concentrated acid stops at $\mathrm{NO_2}$; NO belongs to the other equation.
- **Why:** This question requires the product of a named reagent on a named substrate under a printed condition, demonstrated by the stem's 'heated with conc. $\mathrm{HNO_3}$' and four options that differ only in the nitrogen oxide.
- **Note:** All four options repeat $\mathrm{Cu(NO_3)_2}$, so only the nitrogen product carries a decision and the options are not pairs judged whole; qtype stays mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A cis-1,2-diol closes a cyclic ketal with acetone because both OH groups lie on one face; the trans-diol cannot reach the same carbon
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  'cis-' in front of the name reads as double-bond geometry, and ozonolysis is the reagent drilled for cutting a C=C, so ozone is picked as the reagent that settles cis/trans questions. There is no C=C in a cyclopentane-1,2-diol, and ozonolysis gives the same fragments from a cis and a trans alkene in any case.
- **Why:** This question requires which reagent brings about a transformation on one isomer only, demonstrated by the stem's 'would distinguish cis-cyclopenta-1, 2-diol from the trans-isomer' with four reagents as the options.
- **Note:** The compound is printed as 'cyclopenta-1, 2-diol'; the species the key treats is cyclopentane-1,2-diol. Tagged as printed, and the clipped name is part of what keeps the ozone route open.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\Delta G = \Delta H - T\Delta S$ stays negative at every temperature only when both terms drive it that way: $\Delta H < 0$ with $\Delta S > 0$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Dropping the stem's 'at all temperatures' and asking only whether the pair can be spontaneous, $\Delta H < 0$ is enough to make $\Delta G$ negative and $\Delta S < 0$ goes unchallenged. With $\Delta S < 0$ the $-T\Delta S$ term is positive and grows with $T$, so this pair is spontaneous only below $T = \Delta H / \Delta S$.
- **Why:** This question requires the sign criterion of $\Delta G = \Delta H - T\Delta S$ applied over a stated temperature range, demonstrated by the stem's 'spontaneous reaction at all temperatures'.
- **Note:** Option 1 is defensible on the subject: with $\Delta S = 0$ exactly, $\Delta G = \Delta H < 0$ at every temperature, so it too meets 'spontaneous at all temperatures'. The printed key is (3) and the tag follows it; the doubt is recorded here, and the route under option 1 names the textbook convention the key rests on.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Edge length of a cubic cell from density: $a^{3}=\frac{ZM}{\rho N_A}$, with $Z=2$ atoms in a bcc cell
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The bcc relation $r=\frac{\sqrt{3}}{4}a$ is the step that normally follows a density calculation, and applying it to the correct $a=352$ pm gives $152$ pm, which lands on the printed $154$ pm - a real lithium length, but the atomic radius and not the edge the stem asked for.
- **Why:** This question requires a cell edge computed from density, demonstrated by the stem supplying $530\,\mathrm{kg\,m^{-3}}$, $6.94\,\mathrm{g\,mol^{-1}}$ and $N_A$ and then asking for 'the edge length of a unit cell of Lithium metal'.
- **Note:** The stem as stored reads 'Calculated the edge length', a grammatical oddity in the source that does not change the task. The units are deliberately mixed - density in kg m$^{-3}$ against an atomic mass in g mol$^{-1}$ - so a conversion to $0.530$ g cm$^{-3}$ precedes the substitution.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Bond dissociation enthalpy falls down group 17 from $\mathrm{Cl_2}$, but $\mathrm{F_2}$ breaks the series: lone-pair crowding across the very short F-F bond leaves it weaker than Br-Br
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Applying 'bigger atoms, longer bond, weaker bond' to all four halogens at once keeps $\mathrm{Cl_2}>\mathrm{Br_2}>\mathrm{I_2}$ in the right relative order and lifts $\mathrm{F_2}$ to the top. The F-F bond is the one place the rule fails, because the lone pairs on two small atoms crowd each other and drop it below $\mathrm{Br_2}$.
- **Why:** This question requires the order of one named property across group 17, demonstrated by 'Which one of the following orders is correct for the bond dissociation enthalpy of halogen molecules?' with four complete sequences as options.
- **Note:** type_patterns returned statement_options, but each option is a sequence of species rather than a statement to be judged and no lettered block is printed, so the shape recorded is mcq. On the trap label, `reversed` was ruled out because only $\mathrm{F_2}$ changes place in option 4 and the codebook excludes one misplaced member of a longer order from `reversed`; option 4 is the primary rather than option 1 because it is what NCERT's own general group statement yields unmodified, while option 1 additionally requires inverting Cl/Br/I.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Drugs are filed by therapeutic action: Novalgin is an analgesic, while penicillin, streptomycin and chloromycetin are antibiotics
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option for a route into the asked class: all three are antibiotics printed in the same NCERT drugs chapter, and the only property the chapter attaches to any of them is bactericidal or bacteriostatic action, so no half-remembered rule turns an antibiotic into a pain-reliever. The question tests only whether the brand name Novalgin is stored as an analgesic.
- **Why:** This question requires one stated classification of a named drug, demonstrated by 'Which of the following is an analgesic?' standing against four bare drug names with no criterion printed to apply.
- **Note:** Recorded as no_trap rather than forcing a mechanism: the three wrong options are all antibiotics from one NCERT list, so the item separates two drug classes and nothing leads from the antibiotic class into the analgesic one. Three fillers is the finding here, not a gap - the item discriminates on whether one brand name is stored.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Graham's law: effusion rate goes as $1/\sqrt{M}$, so in the same time the moles escaping stand in the inverse square-root ratio of the molar masses
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Graham's law gives $r_{\mathrm{H_2}}/r_{\mathrm{O_2}}=\sqrt{32/2}=4$, and handing that $\frac{1}{4}$ in as the answer leaves out the factor $\frac{1}{2}$ the stem fixes: oxygen leaves four times slower, so a quarter of the half that has gone is $\frac{1}{8}$.
- **Why:** This question requires a fraction computed from two molar masses, demonstrated by 'What fraction of the oxygen escape in the time required for one-half of the hydrogen to escape?'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Nitration runs on $\mathrm{NO_2^+}$ made by $\mathrm{HNO_3}+\mathrm{H_2SO_4} \rightleftharpoons \mathrm{NO_2^+}+\mathrm{HSO_4^-}+\mathrm{H_2O}$, so adding $\mathrm{HSO_4^-}$ as a common ion pushes that equilibrium back and starves the ring of electrophile
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $\mathrm{KHSO_4}$ reads as more of the acid already in the flask, so the rule 'nitration is acid-driven, more acid means more rate' gets applied; what the salt actually supplies is $\mathrm{HSO_4^-}$, which sits on the product side of the nitronium equilibrium and suppresses it.
- **Why:** This question requires a stated equilibrium rule applied to an added species, demonstrated by 'If a large amount of $\mathrm{KHSO_4}$ is added to the mixture, the rate of nitration will be', whose options are bare outcomes with no number to produce.
- **Note:** The deciding idea is the common-ion effect on the nitronium-generating equilibrium rather than any property of benzene; chapter and subtopic are left exactly as supplied. `condition_missed` was ruled out because the stem prints no condition that is being dropped - the added salt is the whole of the new information - and `reversed` was ruled out because the route to 'Faster' is a different rule applied, not this rule run backwards, which is recorded as the second way instead.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** VSEPR repulsion strength runs lone pair - lone pair > lone pair - bond pair > bond pair - bond pair, because a lone pair is held by one nucleus only and spreads over more angular space
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Holding only the opening term of the series - lone pair - lone pair repulsion is the greatest - leaves the last two places to be settled by intuition, and 'two bonds repelling must beat one bond against a lone pair' puts bond pair - bond pair second. Any pair involving a lone pair outranks bond pair - bond pair, so the tail is the wrong way round.
- **Why:** This question requires the taught ranking of electron-pair repulsions, demonstrated by four options that are three-term orders of 'Lone pair - lone pair', 'Lone pair - bond pair' and 'Bond pair - bond pair'.
- **Note:** The stem, 'Predict the correct order among the following:', names no molecule and no quantity - the options alone say that electron-pair repulsion is what is being ordered. type_patterns returned statement_options; the options are orderings rather than statements to judge, so the shape recorded is mcq. Option 3 is the exact inverse of the key and was the other candidate for the primary trap, which would have been `reversed`; option 2 was taken as primary because it keeps the term the rule is stated by and fails only in its tail, whereas option 3 requires inverting the whole series. Both are recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Calcium carbide heated in nitrogen gives calcium cyanamide, $\mathrm{CaCN_2}$ (nitrolim), not a calcium cyanide
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The paper's own answer line reads 'Solution: (Bonus)' and no option is keyed, so with no right option printed there is no wrong option that a student can be shown to be pulled away from; the formula resemblance a reviewer should check is recorded in the note.
- **Why:** This question requires naming the product a stated reagent pair gives, demonstrated by the stem 'The product obtained as a result of a reaction of nitrogen with $\mathrm{CaC_2}$ is' over four rival calcium-carbon-nitrogen formulae.
- **Note:** No key: the answer line is 'Solution: (Bonus)' and accepted_answers is empty. Tagged as printed, not re-judged. For a reviewer holding a key: the product of $\mathrm{CaC_2}$ with $\mathrm{N_2}$ is calcium cyanamide, $\mathrm{CaCN_2}$, which is absent from the four printed formulae, and option 1 $\mathrm{Ca(CN)_2}$ differs from it only in where the brackets sit. If a key is ever restored to this question, look_alike_term on option 1 is the mechanism to confirm.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** For a liquid-vapour equilibrium the equilibrium constant is the vapour pressure, so the van 't Hoff relation reads $\frac{d\ln P}{dT} = \frac{\Delta H_v}{RT^{2}}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The integrated Clausius-Clapeyron line $\ln P = -\frac{\Delta H_v}{RT} + C$ is quoted where the differential form is asked, so the group $-\Delta H_v/RT$ is read off as though it were the derivative.
- **Why:** This question requires the temperature-dependence relation chosen for a specific equilibrium, demonstrated by the stem 'Consider the following liquid – vapour equilibrium' followed by 'Which of the following relations is correct?' over four rival derivative expressions.
- **Note:** E1 read this as statement_options (no lettered block is printed; each option is a full relation to be judged), which category_retired.qtype maps to statements. The options are equations rather than sentences, so mcq is the arguable alternative; the mapping was followed. Stem prints '298 k' style lower-case units elsewhere in this packet but nothing in this item is ambiguous.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Molecular shape follows from the bond pairs plus lone pairs round xenon: 6 bonds and 1 lone pair give a distorted octahedron, 5 and 1 a square pyramid, 4 and 2 a square plane, 3 and 1 a pyramid
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who counts six electron pairs round Xe in $\mathrm{XeOF_4}$ names that arrangement rather than the shape and calls it distorted octahedral, which leaves square pyramidal for $\mathrm{XeF_6}$; the two rows they are sure of, $\mathrm{XeO_3}$ pyramidal and $\mathrm{XeF_4}$ square planar, sit in this code untouched, so nothing warns them off.
- **Why:** This question requires VSEPR applied to each xenon compound in turn, demonstrated by column II printing four shapes -- 'Distorted octahedral', 'Square planar', 'Pyramidal', 'Square pyramidal' -- which are separated only by how many atoms and lone pairs surround Xe in the compound named in column I.
- **Note:** The stem says column II gives 'the hybridization and shape', but column II prints shapes only and no hybridisation appears in either list or in the options; tagged as printed, and a reviewer should check the printed paper for a dropped hybridisation column.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The more electron-rich the metal centre, the more M$\rightarrow$CO $\pi^{*}$ back-donation, so the C-O bond lengthens as the charge on the carbonyl becomes more negative
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The charge effect is run backwards: a student who fixes the direction by how hard the metal pulls on electrons, rather than by how much electron density it has to give, picks the only cation in the set.
- **Why:** This question requires the charge-to-back-donation rule applied across four carbonyls, demonstrated by the stem supplying the comparison standard '(Free $\mathrm{C-O}$ bond length in $\mathrm{CO}$ is $1.128\,\text{Å}$)' while the options differ essentially in the charge on the complex.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In the Nernst equation for the hydrogen electrode the potential is zero only when $\log p_{\mathrm{H_2}} = 2\log[\mathrm{H^+}]$, which at pH 7 fixes the pressure at $10^{-14}$ atm
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Every slip that moves the exponent was tried against the printed set: dropping the square on $[\mathrm{H^+}]$ gives $10^{-7}$ and reading $K_w$ itself as $[\mathrm{H^+}]$ gives $10^{-28}$, and neither is printed, while dropping or keeping the factor of 2 in $0.0591/2$ both return $10^{-14}$, the key. The three wrong options are other powers of ten with no route from pure water at $298\,\mathrm{K}$.
- **Why:** This question requires the Nernst equation solved for a pressure, demonstrated by the stem 'The pressure of $\mathrm{H_2}$ required to make the potential of $\mathrm{H_2}$ – electrode zero in pure water at $298\,\mathrm{k}$' with four pressures in atm as options.
- **Note:** The one wrong exponent a named slip produces, $10^{-7}$ from dropping the square on $[\mathrm{H^+}]$, is not among the options, which is why this is no_trap rather than arithmetic_slip. Stem prints the unit as '298 k'; lower-case k for kelvin is how our record carries it and does not change what is asked.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A catalyst opens a path over a lower barrier, so it changes the activation energy only; the reaction's $\Delta H$, $\Delta U$ and $\Delta S$ are left where they were
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The catalyst is remembered as 'lowering the energy', and on the energy-profile diagram the lowered hump and $\Delta H$ are drawn against the same enthalpy axis, so the quantity printed beside $E_a$ is taken as the one that changes.
- **Why:** This question requires the stated fact about which quantity a catalyst changes, demonstrated by three thermodynamic state functions printed against 'Activation energy' with no numbers or conditions supplied to work on.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The radius ratio $r_{+}/r_{-}$ decides the packing: 0.414-0.732 is the octahedral band, so each ion in AB is six-coordinate
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The ratio is taken upside down — $1.81/0.98 = 1.85$ — and the only band above $0.732$ is the eight-coordinate one, so the inverted division lands exactly on a printed option.
- **Why:** This question requires a radius ratio computed and then matched to its coordination band, demonstrated by the stem giving '$0.98 \times 10^{-10}\,m$ and $1.81 \times 10^{-10}\,m$' and asking for 'The coordination number of each ion in AB'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Basicity of a phosphorus oxyacid is set by its P-OH hydrogens, so phosphinic acid $\mathrm{H_3PO_2}$ with one OH is monoprotic while phosphonic acid $\mathrm{H_3PO_3}$ with two OH is diprotic
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Phosphinic and phosphonic differ by one letter, so a student holding only the shape of the fact, that one of the pair gives up one proton and the other two, can attach the counts the wrong way round and find that exact assignment printed.
- **Why:** This question requires telling two similarly named phosphorus oxyacids apart by how many protons each releases, demonstrated by option 1 printing the key's own two protic counts with 'Phosphinic' and 'phosphonic' exchanged. Swap test applied: replace the two names with unlike words and the reversal has nothing left to carry it, so the label is look_alike_term rather than nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A colloid is named as dispersed phase in dispersion medium, and fog is liquid water droplets dispersed in air
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Fog and smoke are filed under the same type name, aerosol, so a student carrying 'fog is an aerosol' without the phase pair can take the solid-in-gas line printed beside the liquid-in-gas one.
- **Why:** This question requires the stored table line saying which phase is dispersed in which medium, demonstrated by the stem asking what fog 'is a colloidal solution of' and the four options differing only in the two phases and their order.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In an ideal solution each partial pressure is $p^{\circ}x$, so the vapour is always richer in the component with the higher vapour pressure
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The printed $1:1$ ratio is the liquid's composition, and carrying that mole fraction straight into the vapour gives equal amounts, the one option that uses the stem's ratio and leaves $12.8$ and $3.85\,\mathrm{kPa}$ untouched.
- **Why:** This question requires Raoult's law applied to the printed pressures with no number produced, demonstrated by the options being 'The vapour will contain a higher percentage of benzene' against the same claim made for toluene.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Staggered ethane is the stable conformer because eclipsing the C-H bonds pushes their electron clouds together, which is torsional strain
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Its second clause, that the eclipsed conformation has torsional strain, is the printed fact, so a student scanning the options for that phrase takes the only option that attaches strain to the right conformer and never tests the stability claim in front of it.
- **Why:** This question requires the reason the book gives for one conformer being the stable one, demonstrated by every option carrying a strain clause, 'because staggered conformation has no torsional strain', which is what separates them.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Williamson synthesis makes an ether by having an alkoxide displace halide from an alkyl halide
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  It differs from the key by one word, and the scheme's starting material is an alcohol, so a student who has the name Williamson attached to this chapter but not to its product picks the version whose noun matches what is printed to the left of the first arrow.
- **Why:** This question requires naming the transformation a printed reagent pair carries out, demonstrated by the scheme running cyclopentanol to its sodium salt under NaH and on to methoxycyclopentane under 'Me - I'. Swap test applied to option 4: rename 'Williamson alcohol synthesis' to anything unlike the key and nothing is left to pull, so the label is look_alike_term rather than nearby_fact.
- **Note:** The stem reads 'The reaction [figure] Can be classified as' and the packet supplies the figure as a transcribed scheme, cyclopentanol to sodium cyclopentanolate under NaH to methoxycyclopentane under Me - I, with confidence 'certain' and a printed PNG; this rating rests on that transcription, not on an unseen image.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** An aldehyde and a primary amine condense at the carbonyl carbon and lose water, giving the C=N imine called a Schiff base
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Carboxylic acid is the product of the aldehyde's other standard reaction, its oxidation, so a student who answers from the substrate rather than from the printed reagent supplies it here.
- **Why:** This question requires the product a named reagent gives with a named substrate, demonstrated by the stem fixing both partners as 'an aldehyde' and 'a primary amine' and asking only for 'the product formed'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A biphenyl is chiral only when bulky ortho substituents stop rotation about the ring-ring bond and neither ring carries a symmetry plane
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are drawn biphenyl structures and the record stores all four as empty strings with no figure attached, so there is no option set against which any route could be tested.
- **Why:** This question requires the criterion for optical activity applied to printed structures, demonstrated by the stem asking which of four drawn "biphenyls is optically active" rather than asking for a stated fact.
- **Note:** Options 1-4 are stored as four empty strings and figure_image is null with has_figure false, although the paper prints four biphenyl structures as the options, so an option is missing from the record and no trap may be written. E1 called it plain_mcq; the printed shape is structure options, for which the current qtype list holds no value, so mcq is recorded. A reviewer holding the structures should check the mechanism I would expect but cannot confirm: a biphenyl that is ortho-substituted, and so looks crowded enough to be locked, but still has a symmetry plane through one ring, which the "crowded therefore chiral" reading accepts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Classify a reaction from the change between reactant and product - HBr lost is elimination, OH in place of Br is substitution, Br2 across a C=C is addition - not from the reagent
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Reagent-first classification puts both KOH reactions in one box: a loses HBr to give propene, so b, carrying the same KOH, is read as an elimination too. Two of this option's three verdicts are right and only b fails, since b's printed product propan-2-ol keeps all three carbons with OH where Br was.
- **Why:** This question requires each printed transformation to be classified from its own product, demonstrated by the key splitting the two KOH reactions - "a is elimination, b is substitution and c is addition reaction".
- **Note:** Reactions b and c are absent from the stem text and are carried by the figure transcription (2-bromopropane + KOH gives propan-2-ol + KBr; cyclohexene + Br2 gives 1,2-dibromocyclohexane), so the record is complete enough to tag. The figure note records that nothing is printed over or under either arrow, so no aqueous or alcoholic condition is given and the classification can only be read off the products.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Relative lowering of vapour pressure fixes the solute's mole fraction, the mole fraction gives the molality, and $K_b$ times molality is the boiling-point elevation
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The molality step needs the 100 g of water as 0.1 kg. Dividing the 0.21 mol of solute by 1 kg instead gives 0.21 mol/kg, so $\Delta T_b = 0.52 \times 0.21 = 0.11$ and the boiling point comes back to the printed $100^{\circ}$C.
- **Why:** This question requires the vapour-pressure lowering turned into a molality and then into an elevation, demonstrated by the stem supplying 732 mm alongside "$K_b = 0.52$" and asking for "the boiling point of this solution".
- **Note:** Worked through, the mole fraction 28/760 gives molality 2.05 and $\Delta T_b = 1.07$, and 28/732 gives 2.13 and 1.11; both round to the printed key, $101^{\circ}$C.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** RNA carries ribose and DNA carries 2'-deoxyribose; arabinose is the sugar of neither
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The DNA half of this option is word for word the remembered fact, 2'-deoxyribose, so a student who checks the half they hold securely, finds it right and stops carries "arabinose" for RNA along with it.
- **Why:** This question requires the stated sugar of each nucleic acid, demonstrated by the four options differing only in which of ribose, 2'-deoxyribose and arabinose is placed with "RNA and DNA, respectively".
- **Note:** look_alike_term was ruled out by the swap test: replace "arabinose" with any other non-nucleic-acid sugar and option 1 keeps its pull, because what carries the student is the correct DNA half, not a resemblance between arabinose and ribose. The option carries two parts and one fails, so half_right applies.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In aryl amines the nitrogen lone pair is delocalized into the ring, so it is less available to a proton and aniline is a weaker base than an alkyl amine
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  This option is the key with both halves flipped, and the flip is reached by reading the ring as the electron source: a student who recalls that the ring and the lone pair interact, but stores the interaction as ring-feeds-nitrogen, concludes the lone pair stays put and the amine is the stronger base.
- **Why:** This question requires the reason aryl amines are the weaker bases, demonstrated by all four options pairing a direction with a "because" clause and the key's clause naming the lone pair "delocalized by interaction with the aromatic ring $\pi$ electron system".
- **Note:** negative_words_seen records "NOT", but it is the "not delocalized" inside option 2's own premise, not a negation of the task.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sucrose joins glucose and fructose through both anomeric carbons and so has no free reducing group, while maltose and lactose each keep one
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The three disaccharides are settled in one stretch of the chapter, and a student who carries away "the glycosidic linkage ties up the reducing group" without carrying away which member of the trio it holds for picks the disaccharide standing first among the options.
- **Why:** This question requires the stated reducing status of each named sugar, demonstrated by the options being three taught disaccharides and glucose with no criterion printed to apply to them.
- **Note:** look_alike_term was ruled out by the swap test: "maltose" and "sucrose" do not resemble each other, and replacing maltose with any unlike disaccharide name keeps the pull, because what carries the student is the three sugars being printed together, so position is doing the work.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Hybridisation is counted from sigma bonds plus lone pairs, so the lone pair of an alkynyl anion sits in the $sp$ orbital the hydrogen vacated while both remaining $2p$ orbitals stay in the two $\pi$ bonds
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The taught picture of a carbanion — pyramidal, $sp^3$, like ammonia — is carried straight onto this anion and the printed $\mathrm{C\equiv C}$ is never used. That picture holds for a saturated carbanion carbon; here two $\pi$ bonds hold the carbon linear, so the pair is in an $sp$ orbital.
- **Why:** This question requires the sigma-bonds-plus-lone-pairs rule applied to the printed species rather than a stored hybridisation value, demonstrated by the stem printing $\mathrm{CH_3C\equiv C^{\ominus}}$ and asking which orbital holds "the pair of electron", with all four options being the plain hybridisation menu $2p$ / $sp^3$ / $sp^2$ / $sp$.
- **Note:** Stem phrase "The pair of electron" is kept as printed. Option 2 is reachable by two separate routes, the generic carbanion shape and the methyl carbon of the same printed formula, so both are recorded as named ways under the one trap.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Two species drawing on the same limiting resource cannot share one niche indefinitely; the inferior competitor is eliminated
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  NCERT prints Connell's barnacle experiment beside the principle, where the larger Balanus excludes the smaller Chthamalus, and this option is that sentence generalised. Body size is a feature of one illustration, not a term in the principle, which turns on sharing a limiting resource.
- **Why:** This question requires the stated wording of a named principle, demonstrated by the stem 'Gause's principle of competitive exclusion states that' set against option 3's 'same niche indefinitely for the same limiting resources'.
- **Note:** E1's pattern called this statement_options on 15 full-statement options, and the printed shape is indeed four rival full sentences. The current qtype axis reserves `statements` for a stem that asks you to judge statements or prints a lettered list, and this stem names a principle, so it is recorded as mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Human insulin is two polypeptide chains, A and B, held to each other by disulphide bridges
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Hydrogen bonding is the linkage carried for 'two chains held together', from the DNA double helix and from a polypeptide's own coiling, and the stem's 'linked together' is the same wording. Hydrogen bonds shape a chain, while the link between insulin's A and B chains is printed as disulphide bridges.
- **Why:** This question requires the one linkage the source names between insulin's two chains, demonstrated by the stem 'The two polypeptides of human insulin are linked together by' with four bond names as the options.
- **Note:** Option 3 is chemically true of the key's own answer, since a disulphide bridge is a covalent bond, so the key rests on the convention of choosing the most specific linkage rather than on the chemistry; tagged as printed. On the nearby_fact / look_alike_term test for option 1: swapping 'hydrogen bonds' and 'disulphide bridges' for two unlike words leaves the pull intact, because what carries the student is the remembered 'chains held together by hydrogen bonds' fact and not any likeness between the names.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The primary endosperm nucleus divides without wall formation first, so the liquid in a tender coconut is free-nuclear endosperm, not fruit wall
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Free nuclear proembryo' is the key's own phrase with one word changed, so a student who stored 'free nuclear' without storing what is free-nuclear cannot be separated by the remembered phrase. Free-nuclear division belongs to the endosperm; the zygote's first divisions give a cellular proembryo.
- **Why:** This question requires the stated identity of the liquid in a tender coconut, demonstrated by options that set two fruit-wall layers, 'Endocarp' and 'Fleshy mesocarp', against two post-fertilisation products.
- **Note:** On the nearby_fact / look_alike_term test for option 3: replace 'free nuclear proembryo' with an unlike term and the pull dies, so the likeness of the printed phrases is doing the work rather than position, and under the rulebook's tie-break the likeness wins even though the embryo and endosperm paragraphs also sit side by side.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A viroid is naked infectious RNA of low molecular weight, smaller than a virus and without a protein coat
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The missing protein coat is the line that defines a viroid and gives it its name, so it is the statement a student reaches for when viroids are the subject. The stem asks which statement is WRONG, and this one is right.
- **Why:** This question requires each printed property of viroids to be checked against the stated ones, demonstrated by the stem 'Which of the following statements is wrong for viroids?' against option 4's 'RNA is of high molecular weight'.
- **Note:** E1's pattern took the default plain_mcq here, but the stem asks which of the following statements is wrong, which is the case rule 1 reserves `statements` for, so the shape is recorded as statements.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Arthropods have a chitinous exoskeleton, a segmented body and jointed appendages; parapodia are the annelid locomotory structures
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The answer has to be the annelid feature, and metameric segmentation sits in the Annelida account alongside parapodia, so a student working from that paragraph picks the annelid feature held most firmly. Arthropods are segmented too, which is why parapodia alone is absent.
- **Why:** This question requires the printed characteristics of one phylum, demonstrated by the stem 'not present in the Phylum - Arthropoda' against the option 'Parapodia'.
- **Note:** On the nearby_fact / look_alike_term test for option 2: swap 'parapodia' and 'metameric segmentation' for two unlike words and the pull survives, because what carries the student is both terms sitting in the Annelida paragraph, not any resemblance between the names. The generic route of reading the negation as a positive would reach any true option here and so singles out none of them; it is not attributed to options 1 or 4.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Haemophilia is a single-gene recessive disorder carried on the X chromosome, so carrier mothers pass it to sons
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Haemophilia is a recessive gene disorder, so a student who fixed its recessive inheritance and not its location stops at the option that says exactly that. The stem asks for the most appropriate description, and the X-linkage is the part that explains the carrier mother to affected son pattern.
- **Why:** This question requires the inheritance class the source assigns to haemophilia, demonstrated by the stem's 'most appropriately describes' set against option 1's bare 'Recessive gene disorder'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Red drop and Emerson's enhancement effect were the evidence that photosynthesis runs on two pigment systems, PS I and PS II, working together
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Non-cyclic electron transport is what two photosystems in series actually do, so a student who has the Z scheme right but reads 'discovery of' loosely names the process instead of the systems. The two observations established that two photosystems exist; the electron route and ATP formation were shown by other experiments.
- **Why:** This question requires the discovery NCERT attributes to two named observations, demonstrated by the stem naming 'Emerson's enhancement effect and Red drop' and asking what they were 'instrumental in the discovery of'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's essential-element list fixes the macronutrients - C, H, O, N, P, S, K, Ca, Mg - and everything else on the list is a micronutrient
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Magnesium is a genuine macronutrient sitting between two look-alike M-names, so a student who verifies the name he recognises lets the set through. Molybdenum and manganese are both micronutrients, so the stem's 'all three' is what the option fails.
- **Why:** This question requires the printed macronutrient list to be applied to every name in a set, demonstrated by the stem asking in which option 'all three are macronutrients'.
- **Note:** The printed solution line reads 'Solution: (4) or bonus', and nickel in the keyed option is on NCERT's micronutrient list, so strictly no option has all three macronutrients; tagged as printed, with the key recorded here as arguable rather than re-judged. On the trap axis the magnesium/manganese resemblance strengthens the pull on option 3, but the failure that decides it is the set as a whole, which is half_right rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Emphysema is the chronic disorder NCERT ties to cigarette smoking: alveolar walls break down and respiratory surface is lost
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Asthma is the other chronic respiratory disorder in the same NCERT paragraph, so a student who stored the pair as one line without the cause beside each reaches for the better-known name. Asthma is inflammation triggered by allergens, and no smoking cause is attached to it.
- **Why:** This question requires the cause NCERT prints beside a named disorder, demonstrated by the stem asking to 'Name the chronic respiratory disorder caused mainly by cigarette smoking'.
- **Note:** Swap test on the trap axis: 'asthma' and 'emphysema' do not resemble each other as words, so what carries the student is NCERT printing them in the same disorders paragraph - nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ley farming is the rotation that puts a legume or grass pasture into the cropping cycle so the soil regains structure and fertility
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Strip cropping is the other practice on the same conservation list that puts grass and legume bands between crops, so a student who remembers 'grass strips' and not 'in the rotation' stops there. Strip farming separates crops across a slope at one time and rotates no pasture through the field.
- **Why:** This question requires the term attached to a printed description of a practice, demonstrated by the stem defining 'a system of rotating crops with legume or grass pasture to improve soil structure and fertility' and asking what it 'is called'.
- **Note:** Swap test on the trap axis: 'ley' resembles none of the other names, and all four are terms from the same soil-conservation list, so position is doing the work - nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mitochondria and chloroplasts are semi-autonomous: they divide by fission of pre-existing organelles and carry their own DNA and their own ribosomes, so they build part of their protein themselves
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Statement (ii) opens with two lines NCERT does print - these organelles arise by division of pre-existing organelles and contain DNA - so a student who verifies those two clauses and stops endorses the statement whole and marks both correct. Its last clause, 'lack protein synthesizing machinery', is the part that fails, because the organelles carry their own ribosomes.
- **Why:** This question requires the stated facts about what mitochondria and chloroplasts possess, demonstrated by statement (ii)'s clause 'they contain DNA but lack protein synthesizing machinery' being the only part of the printed block that separates the four options.
- **Note:** E1 gave statement_options, but a labelled two-statement block is printed above the options, so the shape visible on the page is a Statement (i)/(ii) list; both map to qtype statements.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amniocentesis reads cultured fetal cells from amniotic fluid, so it detects chromosomal and genetic disorders and not a structural defect such as cleft palate
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Prenatal sex determination is the use the chapter prints as forbidden, so a student grading the four sentences on legality strikes this one out. The stem asks which statement is factually incorrect, and the fetal karyotype does show the sex, which is exactly why the misuse exists.
- **Why:** This question requires the printed uses and timing of a named procedure to be checked sentence by sentence, demonstrated by the stem asking 'which of the following statement is incorrect' about amniocentesis.
- **Note:** qtype is statements, not mcq: the stem asks which statement is incorrect and each option is a whole claim to be judged, which is the case rule 1 names, even though no lettered block is printed; E1's statement_options reading agrees. The deciding option, cleft palate, is judged against the printed scope of the test (chromosomal and genetic disorders), so asks stays fact_line with the rest of the group.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the light reaction protons are released by water splitting and carried into the thylakoid lumen, so the lumen is the compartment that becomes proton-rich
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The intermembrane space is where protons pile up in a mitochondrion, so a student carrying one chemiosmosis picture across puts the gradient in the chloroplast's envelope space. In a chloroplast the pumping is across the thylakoid membrane, into its lumen.
- **Why:** This question requires the compartment named as the proton sink of the light reaction, demonstrated by the stem asking where 'in a chloroplast the highest number of protons are found' with four chloroplast compartments as the options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Rhodopsin, the visual pigment of the rods, is the protein opsin bound to retinal, the aldehyde of vitamin A
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 1 and 4 are character-for-character identical ('Guanosine and Retinol'), so one printed option is not in our record; the option set as stored is incomplete and any mechanism read off it would be a guess
- **Why:** This question requires the stated composition of the eye's photosensitive pigment, demonstrated by the stem 'Photosensitive compound in human eye is made up of:' with every option printing two named molecules to be accepted together.
- **Note:** Stored options 1 and 4 are the same string, 'Guanosine and Retinol', which a printed paper would not do, so one option has been lost or miscopied in extraction. Under rulebook 5a that is source_damage_artifact and never a trap tag, so no trap is written. A reviewer holding the printed paper should check the retinal / retinol pull on option 3 ('Opsin and Retinol' against the key's 'Opsin and Retinal'): retinol is the alcohol, retinal the aldehyde that binds opsin, and the resemblance of the two names would be the expected look_alike_term mechanism. E1 read this as plain_mcq; the printed shape is options that are pairs judged whole, so qtype is recorded as two_part.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Spindle microtubules bind the kinetochore, the disc-shaped structure sitting on the surface of the centromere, not the centromere itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The centromere is the chromosome part named first and the kinetochore is introduced as a disc lying on its surface, so a student carrying 'the spindle attaches at the centromere' stops one layer short of the structure that does the binding.
- **Why:** This question requires the one stated fact about where the spindle fibre binds, demonstrated by the stem 'Spindle fibres attach on to:' followed by four named parts of the same chromosome with no criterion printed to apply.
- **Note:** Swap test applied: replace 'centromere' with a word unlike 'kinetochore' and the pull survives, because what carries the student is the centromere being the part printed beside and under the kinetochore, so nearby_fact rather than look_alike_term. Option 4 'kinetosome' is the likeness case, and it is recorded as the second route rather than the primary. E1 read this as statement_options; by qtype rule 1 naming a part with a trailing 'of the chromosome' is not a statement to judge, so qtype is mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** India's National Aquatic Animal is the Ganges river dolphin, chosen as an indicator of clean fresh water
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The designation is stored as 'the dolphin of the Ganga', and 'Gangetic shark' is the other Ganga animal on this list, so a student who kept the river and lost the animal takes the option that prints the river's name.
- **Why:** This question requires one designated fact held in memory, demonstrated by the stem 'Which is the National Aquatic Animal of India?' with four coordinate aquatic animals and nothing printed from which the answer could be worked out.
- **Note:** Swap test applied: replace 'Gangetic shark' with the name of any other unlike Ganga species and the pull survives, because the shared Ganga association, not any resemblance between 'shark' and 'dolphin', is what carries the student - hence nearby_fact. The fact itself is a government notification rather than a sentence of NCERT; fact_line is used in its broader sense of one stated fact with nothing to apply, which is the only value on this axis that describes the task.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lactose is the inducer of the lac operon: it binds the repressor and frees the operator, while its breakdown products and glucose do not induce
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The stem's 'inducer(s)' leaves room for more than one molecule, and galactose is the sugar carried in the operon's own enzyme name, so a student who is sure of lactose adds galactose to cover the plural.
- **Why:** This question requires the named inducer of a taught regulatory system, demonstrated by option 4 printing 'Lactose and galactose' so that the inducing molecule has to be held apart from its breakdown product.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Antagonistic hormones push the same variable in opposite directions; relaxin and inhibin act on different processes, so neither opposes the other
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Atrial natriuretic factor is remembered through the action printed for it, that it dilates vessels and lowers blood pressure, and a student holding only that sees nothing for aldosterone's salt handling to oppose, so this pair reads as the one with no opposite effects.
- **Why:** This question requires the two hormones inside each printed pair to be set against each other to see whether they move one variable in opposite directions, demonstrated by the stem's gloss 'not antagonistic (having opposite effects) to each other' applied to four pairs of the same kind.
- **Note:** Swap test applied to the primary trap: replace 'Atrial Natriuretic Factor' with an unlike hormone name and the pull survives, because what carries the student is which of the two actions printed for ANF they retrieve, not any resemblance between the names - so nearby_fact, not look_alike_term. E1 read this as plain_mcq; each option is a set of same-kind items taken whole, so qtype is two_part, consistently with q104. The polarity route (picking a famous antagonistic pair after reading past 'not') lands equally on options 1 and 2 rather than on one option, which is why it is recorded there and not as the single trap.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Microtubules build the cytoskeletal machinery - cilia, flagella, centrioles, centrosome and spindle fibres - and not membrane-bound microbodies or DNA-protein complexes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'Cilia and flagella are microtubule-based' is the phrase the chapter prints, so a student who finds both of them at the head of option 1 accepts the whole set and never tests the third item.
- **Why:** This question requires each item of a printed set to be checked against the stated fact of what microtubules build, demonstrated by option 1 putting the correct 'Cilia, Flagella' in front of 'Peroxisomes' so that two right items sit in a failing set.
- **Note:** E1 read this as statement_options on option length; the options are sets of three same-kind cell structures accepted or rejected whole, not statements to be judged, so qtype is two_part as on q104 and q108. All three wrong options carry a route here and none is filler, which is a property of how the sets were built: each pairs two genuine microtubular structures with one non-microtubular item.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Many ribosomes translating one mRNA at the same time are together a polysome; the polypeptide is what they build, not what the assembly is called
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Three of the four options open with 'Poly', and polypeptide is the poly- word from the same translation sentence, so a student recalling the shape of the right word rather than the word itself puts the product's name in the assembly's slot.
- **Why:** This question requires the name NCERT gives one stated structure, demonstrated by the stem 'A complex of ribosomes attached to single strand of RNA is known as:' with four bare terms as options.
- **Note:** answers_other_question was weighed for option 3, since polypeptide is a true fact about translation, but the device here is the shared 'Poly' opening carried by three of the four options, so look_alike_term is recorded. answer_line_as_printed is cut off mid-sentence ('This is known as'); the key, stem and options are all present, so the rating stands.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fertilisation happens at the ampullary-isthmic junction of the fallopian tube, so ovum and sperm have to reach that spot at the same time
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  Option 3 repeats the remembered phrase 'ampullary - isthmic junction' and swaps only the organ it belongs to, so a student who stored the site as a phrase rather than as a place ticks it without reading 'cervix'.
- **Why:** This question requires the site and timing NCERT fixes for fertilisation, demonstrated by the stem 'Fertilization in humans is practically feasible only if:' completed by options that differ only in the place and the moment they name.
- **Note:** E1 recorded statement_options because the options are full sentences. Under the current vocabulary qtype statements needs a printed lettered block or a stem that asks for statements to be judged, and this stem asks one question, so mcq is recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Asthma is an allergic hypersensitivity - mast cells release histamine and the bronchial muscles go into spasm - not an infection
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The chapter's asthma line reads 'inflammation of bronchi and bronchioles', so a student who kept the word inflammation but not the place it names picks the inflammation option, which has moved it up to the trachea.
- **Why:** This question requires the cause NCERT assigns to a named disorder, demonstrated by the stem 'Asthma may be attributed to:' with four rival causes as options.
- **Note:** E1 recorded statement_options from the full-sentence options; qtype mcq is recorded for the same reason as q111. The chapter's own asthma sentence names inflammation of bronchi and bronchioles, which is what makes option 3 reachable - this is not a doubt about the key, since option 3 names the trachea.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Avena coleoptile curvature test is the bioassay for auxin - how far the coleoptile bends measures how much IAA was applied
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Auxin and gibberellin stand in the same printed list of growth promoters and both are taught as lengthening shoots, so a student who remembers that the Avena test measures growth, but not which hormone it was built for, reaches for the other elongation hormone.
- **Why:** This question requires the stated pairing of a named bioassay with the hormone it tests, demonstrated by the stem 'The avena curvature is used for bioassay of:' with four hormone names as options and no setup printed to interpret.
- **Note:** asks 'experiment' was weighed and ruled out: nothing is supplied to interpret, only the assay's name, so what is wanted is the stated pairing. On the trap axis the swap test was applied - replace GA3 with an unlike name and the pull survives, because what carries the student is gibberellin standing in the same printed list of promoters, not any likeness to IAA.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a papilionaceous corolla the large standard petal is the vexillum, the two side petals are the wings and the two fused inner ones are the keel or carina
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Carina is the other Latin petal name printed in the same description as vexillum, so a student who holds 'a standard, two wings and two keel petals' as a set, without which Latin name sits on which petal, takes the one that is not the wings.
- **Why:** This question requires the name NCERT prints for one named petal, demonstrated by the stem 'The standard petal of papilionaceous corolla is also called:' with four floral terms as options.
- **Note:** Swap test applied: replace carina with an unlike word and the pull survives, because it is carried by carina being printed in the same corolla description, not by resemblance to vexillum. The likeness route in this question (corona against corolla) sits on a different option, which is why it is recorded under other_options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Liliaceae has a tricarpellary, syncarpous gynoecium, while Solanaceae is bicarpellary and syncarpous and Fabaceae monocarpellary
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The family descriptions run one after another in the same chapter, and the Solanaceae entry prints 'bicarpellary, syncarpous', which differs from the stem by one count, so a student who keeps 'syncarpous' as the Solanaceae word answers from that line.
- **Why:** This question requires the stated floral characteristic of one named family, demonstrated by the stem 'Tricarpellary, syncarpous gynoecium is found in flowers of:' with four family names as options.
- **Note:** Swap test applied: all four options end in -aceae, so likeness does not single out option 2; what carries the student is the printed phrase 'syncarpous' in the neighbouring family's description, so nearby_fact rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fungal cell walls are built of chitin, while bacteria build theirs from peptidoglycan and plants theirs from cellulose
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cellulose is the wall material the course names first and all four options come from the same printed set of wall polysaccharides, so a student carrying 'cell wall means cellulose' but not 'fungus means chitin' takes the neighbour. Cellulose is the plant wall; the wall named for fungi is chitin.
- **Why:** This question requires the stated composition of the fungal wall, demonstrated by the stem asking for 'One of the major components of cell wall of most fungi' with four wall polysaccharides as options and no criterion printed to apply.
- **Note:** answer_line_as_printed reads 'Solution: (1) Peptidoglycan - Bacterial cell wall', which carries the key's number but the text of option 2; key 1 = Chitin is right for this stem, so the question is tagged as printed. nearby_fact over look_alike_term by the swap test: chitin and cellulose do not resemble each other, and renaming them leaves the trap standing because what carries the student is the four options all being wall materials printed together.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** FSH acts on the Sertoli cells and LH on the Leydig cells, and both gonadotropins rise through the follicular phase to a mid-cycle peak
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Spermiogenesis' sits one syllable from 'spermatogenesis', so a student hunting for the planted error in a negated stem reads the unfamiliar twin as the substituted word. Both words are real and the Sertoli cells are tied to spermiogenesis, so nothing in option 1 fails.
- **Why:** This question requires the stated hormone-to-target facts of the reproductive cycle, demonstrated by the stem 'Select the incorrect statement' set over four standalone claims such as 'LH triggers ovulation in ovary'.
- **Note:** look_alike_term rather than nearby_fact by the swap test: replace spermiogenesis with an unlike word and the pull on option 1 dies completely, so the likeness to spermatogenesis is doing the work, not position on the page.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Crossing over begins in pachytene, where recombination nodules appear on the already synapsed bivalents; zygotene is synapsis and diplotene is where chiasmata become visible
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Zygotene is the stage printed immediately before pachytene and is where the homologues pair, so a student reading 'initiated' takes the start of pairing for the start of exchange. Pairing only builds the bivalent; the recombination nodules that carry out the exchange appear in pachytene.
- **Why:** This question requires the stated prophase-I substage at which exchange begins, demonstrated by the stem 'In meiosis crossing over is initiated at' with the four substages as the options.
- **Note:** nearby_fact over look_alike_term by the swap test: the four names share the -tene ending, but renaming them to unlike words leaves the trap standing, because what carries the student is where synapsis and visible chiasmata sit in the printed sequence rather than any likeness between the names.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Selfing the F1 of a tall x dwarf cross gives genotypes 1 homozygous tall : 2 heterozygous tall : 1 dwarf, a split the 3 : 1 phenotype ratio hides
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  3 : 1 tall to dwarf is the ratio printed with this very cross, so a student who recognises the cross answers with the number pair attached to it. That pair counts phenotypes, and the stem asked what the genotypes came out in.
- **Why:** This question requires Mendel's segregation applied to a stated cross, demonstrated by the stem specifying 'A tall true breeding garden pea plant is crossed with a dwarf true breeding garden pea plant' and then asking what 'the resulting genotypes' were in.
- **Note:** E1 recorded statement_options on 'full-statement options', but the printed options are a ratio plus its class labels, accepted or rejected whole, with no statements to judge; recorded as mcq. asks is apply_rule, not fact_line, because the stem supplies a cross to be worked rather than a term to be named, and no quantity is computed from printed numbers.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The evil quartet of causes of biodiversity loss, in which habitat loss and fragmentation is named the single most important cause
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Over-exploitation is printed as the next member of the same quartet and carries the chapter's named extinctions, so a student who holds the list but not its ranking answers with the cause they can illustrate. The member printed first, and named most important, is habitat loss and fragmentation.
- **Why:** This question requires the ranking printed inside the evil quartet, demonstrated by the stem asking for 'the most important cause of animals and plants being driven to extinction' while offering all four quartet members.
- **Note:** A new_trap named true_but_not_superlative was considered, since all three wrong options are genuine causes and fail only on the superlative. nearby_fact already covers it: membership of the one printed quartet is what carries the student, and the swap test survives renaming the four causes, so no new value was proposed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A cropland is a man-made ecosystem sown with a single crop variety, so it holds the least genetic diversity, while its weeds, soil organisms and human-arrested succession all stay in place
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Succession is the one thing the course prints about farmland, as secondary succession beginning on abandoned farm land, so a student who recognises the word answers with the remembered pairing. That line is about a field once it is abandoned; a sown and weeded field is held at one stage on purpose.
- **Why:** This question requires the stated property of a man-made single-crop ecosystem, demonstrated by the option the key accepts, 'Least genetic diversity', standing against two claimed absences and one process.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** After puberty the ovary's own estrogen and progesterone feed back on the hypothalamus and set how fast GnRH is released
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Inhibin is the hormone this chapter names as a brake on gonadotropin release, so a student keeps estrogen and puts inhibin in the second slot. Estrogen is right and inhibin is not, and a pair with one hormone wrong scores nothing.
- **Why:** This question requires the stored pair of ovarian hormones that set GnRH pulsing, demonstrated by the stem asking what the change is 'controlled by circulating levels of' while every option is a bundle of one or two hormone names.
- **Note:** All four options bundle hormones that are accepted or rejected whole, which is why rule 2's condition for half_right is met on option 2. The pulse-frequency wording is not an NCERT sentence; the fact is stored from the hormone-feedback account rather than quoted from a line, so asks stays fact_line.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A plasmid is a small extrachromosomal circle of double-stranded DNA that replicates on its own inside the bacterium
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The definition carried in memory is 'extrachromosomal, self-replicating, circular DNA', and transferability is not in it, so a student unsure about the strands ticks the property the definition never mentioned. Plasmids do pass between cells, so this option answers which feature plasmids HAVE.
- **Why:** This question requires the stated properties of a plasmid, demonstrated by the stem asking which 'is not a feature of the plasmids' while three options restate the taught definition.
- **Note:** The stem is negated and all three wrong options are true features, so beyond option 3 the only question-level device is dropping the printed 'not', which lands on no option in particular; that is recorded here rather than tagged on an arbitrary option.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The cockroach carries the arthropod characters -- schizocoelic body cavity, chitinous exoskeleton, metameric segmentation -- and as a protostome its cleavage is spiral, not radial
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The body cavity stored for the cockroach is the haemocoel, read off the blood-filled spaces of its open circulatory system, so 'schizocoelom' reads as some other animal's cavity and gets ticked as the absent feature. Schizocoely is how that same cavity forms in arthropods, so the option names a feature the cockroach has.
- **Why:** This question requires the stored diagnostic features of the cockroach, demonstrated by the stem asking which feature 'is not present in Periplaneta americana' while three options restate taught arthropod characters.
- **Note:** The printed solution reads 'indeterminate and spiral cleavage', so it faults only the word 'radial' in option 2; the usual teaching for protostomes is determinate and spiral cleavage, which makes the solution's 'indeterminate' arguable. Either way option 2 fails on 'radial', so the printed key stands and the question is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Immunity rests on telling self from non-self; when that recognition is lost and lymphocytes attack the body's own cells, the disorder is called autoimmune disease
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  'Self and non-self' is the wording used to explain why a transplanted organ is attacked, so a student who recognises the phrase reaches for graft rejection. Here the recognition is LOST and the attack falls on the body's own cells, which is the disorder printed a few lines away.
- **Why:** This question requires the named disorder that follows from lost self recognition, demonstrated by the stem's 'attacks self – cells' with four coordinate immunity terms as options.
- **Note:** nearby_fact over look_alike_term by the swap test: 'graft rejection' and 'auto – immune disease' resemble each other in no way, and replacing the option with any unlike phrase leaves the pull intact, because what carries the student is the stem echoing the self/non-self sentence printed with graft rejection.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Dominance and codominance say how the two alleles of one gene show up in a heterozygote, while pleiotropy is one gene affecting many characters and polygenic inheritance is many genes affecting one character
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Pleiotropy and polygenic inheritance are carried as the gene-and-character pair with the direction of the arrow left loose, so "Many genes govern a single character" gets read onto pleiotropy, and (c) (i) is printed in only one option, which settles the whole code before the other rows are looked at.
- **Why:** This question requires the definition NCERT states for each of four inheritance patterns, demonstrated by Column II printing those definitions as finished sentences — "A single gene influences many characters" against "Many genes govern a single character" — with no criterion to apply and nothing to compute.
- **Note:** The stem as stored holds only the column headers "Column – I    Column – II" with no "Match the following" instruction line; the two printed lists and the pairing-code options fix the shape as match_columns anyway, and E1's match_the_lists agrees. Key (2) checks out row by row against the printed definitions. Also worth recording for whoever reviews the distractor design: no option corresponds to a single clean swap of either mirror pair, so every wrong option misfiles at least two rows, and each puts an allele sentence on a gene term or a gene sentence on an allele term, which means the "allele" versus "gene / character" wording of Column II alone strikes out all three.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Joint Forest Management, the government's move to run forests together with the local communities, dates from the 1980s
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The people's-participation story in this chapter opens with the Chipko movement of 1974, printed beside the Joint Forest Management sentence, so a student holding one date for villagers protecting forests carries the Chipko decade across. The JFM line carries its own decade, and this paper's answer line gives 1988.
- **Why:** This question requires the decade printed for the introduction of Joint Forest Management, demonstrated by the stem 'was introduced in India during' with four bare decades as options.
- **Note:** nearby_fact over look_alike_term by the swap test: decades carry no resemblance to each other, and the pull survives any relabelling because it comes from the 1974 Chipko date printed beside the JFM line. Not old_ncert_answer: no value in the question has been altered, so neither of the two numbers that label requires can be named.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each inherited disorder carries a fixed mode of inheritance: haemophilia is sex-linked recessive, phenylketonuria and sickle-cell anaemia are autosomal recessive, and Down's syndrome is an aneuploidy rather than a gene disorder
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each of the four stored statements against the source lines: haemophilia sex-linked recessive, Down's syndrome due to aneuploidy, phenylketonuria autosomal recessive and sickle-cell anaemia autosomal recessive are all stated facts, and no printed option lists all four, so as stored no option is correct and any route to a wrong option would rest on wording this record cannot be relied on.
- **Why:** This question requires the stated mode of inheritance for each named disorder, demonstrated by the four statements each asserting one classification ('is a sex - linked recessive disease', 'is due to aneuploidy', 'is an autosomal recessive gene disorder') with no criterion printed to apply.
- **Note:** Tagged as printed, key 4, and no trap written. As stored, statements (iii) and (iv) make the identical claim in identical words ('is an autosomal recessive gene disorder'), yet the key counts (iii) in and (iv) out; and since every one of the four statements as stored is a stated fact, no option covers them all. So statement (iv)'s stored wording cannot be what the paper printed, and it needs checking against a printed paper before a trap is recorded - per the rulebook's worked resistor-code case, a trap built on this text would be a confident wrong finding. The key is not re-judged here. Separately, E1 gave statement_options, but a labelled block of four statements is printed above the options, so the shape visible on the page is a lettered statement list; qtype statements either way.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each taught group carries an alternative name -- cyanobacteria are blue-green algae, golden algae are desmids, phycomycetes are algal fungi -- and eubacteria are the TRUE bacteria
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Chrysophytes are stored as 'diatoms' and desmids are met as a green-alga name, so this is the one synonym whose two names were never filed together and it reads as the misattached one. The classification chapter prints golden algae and desmids as the same thing, so the statement is correct and answers which statement is right.
- **Why:** This question requires the alternative name taught for each named group, demonstrated by option 3 reading 'Eubacteria are also called false bacteria' against the answer line's 'Eubacteria are called true bacteria'.
- **Note:** qtype is statements on brief rule 1: the stem reads 'Which one of the following statements is wrong?' and each option is a full claim to be judged, which is also what E1's pattern classifier recorded as statement_options. The key's own device is a one-word swap, true to false, inside the key; the trap axis records a wrong option, so that is noted here rather than tagged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A stamen is a stalk fixed at its base to the thalamus or petal, carrying the anther at its free upper end
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student holding 'the filament carries the anther' and never fixing which end is which answers with the attachment at the far end, which is the distal one, not the proximal end the stem names.
- **Why:** This question requires the stated attachment point of a stamen's filament, demonstrated by the stem 'Proximal end of the filament of stamen is attached to the:' listing four named flower parts with no criterion printed to apply.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each contraceptive method has one defined mode of action, and vasectomy blocks the transport of sperm rather than their production
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who files one headline action per method reads 'prevent/retard entry of sperms' as the barrier method's job, so the hormonal pairing looks like the swapped one; the taught line on oral contraceptives gives the pill that action too, through the cervical mucus.
- **Why:** This question requires the action defined for each named contraceptive, demonstrated by option 4 'Vasectomy — Prevents spermatogenesis', which fails on the stated action alone while the method itself is correctly a contraceptive.
- **Note:** nearby_fact over look_alike_term: swap 'barrier methods' and 'hormonal contraceptives' for two unlike words and the trap still stands, because what carries the student is the two methods sitting side by side in the same taught list, not any likeness between their names. The pattern classifier called this statement_options, which maps onto statements here because the stem grades a printed method-and-action claim rather than naming a lettered block.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** PCR needs a polymerase that survives the denaturation heat, and taq polymerase is named after its hot-spring source, Thermus aquaticus
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  A student holding 'taq is thermostable, so it comes from a Th- bacterium that survives punishing conditions' but unable to finish the name takes Thiobacillus ferroxidans, the other Th- species on the list.
- **Why:** This question requires the named source organism of a stated enzyme, demonstrated by the stem 'The taq polymerase enzyme is obtained from:' with four species names as the options.
- **Note:** look_alike_term over nearby_fact: replace the two genus names with unlike words and the pull dies, since no printed word ties an iron-oxidising bacterium to PCR; the shared Th- opening is what carries the student.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inhibin, from the granulosa cells of the ovary, feeds back on FSH alone and not on LH
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who has fixed inhibin's source but not its target takes LH, the gonadotropin printed beside FSH on every line of the chapter; the first half of this option is the key's own wording, so only one word is changed.
- **Why:** This question requires two stated facts about inhibin together, its source and the gonadotropin it suppresses, demonstrated by option 3 'Is produced by granulose cells in ovary and inhibits the secretion of LH', which keeps the source and changes the hormone.
- **Note:** All three wrong options are built from the same two halves as the key, source and target, so each carries a route and none is filler. The trap is recorded on option 3 because it keeps the key's source wording and alters one word.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Meloidogyne incognita is the root-knot nematode of tobacco, which is why the RNAi protection is aimed at the root
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  Tobacco is the crop grown for its leaf, so a student who knows the nematode cuts the yield but not the organ puts the infection where the harvest is; the nematode works below ground and stunts the plant from the root.
- **Why:** This question requires the stated site of infection of a named pest, demonstrated by the stem 'Which part of the tobacco plant is infected by Meloidogyne incognita?' offering four plant parts and no criterion to apply.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A vaccine hands the body a weakened pathogen so it makes its own antibodies, while an antiserum hands over ready-made antibodies
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  A student who remembers that the vaccine holds a treated pathogen but not which treatment reaches for 'activated', a word one syllable away from 'attenuated' and reading as something done to the pathogen.
- **Why:** This question requires what a vaccine preparation contains, demonstrated by the stem 'polio drops that are administered into the body contain:' set against its own 'Antivenom injection contains preformed antibodies'.
- **Note:** look_alike_term over nearby_fact: swap 'activated' for an unlike word and the pull is gone, because nothing in the stem suggests a pathogen being switched on; the near-identity of attenuated and activated is the whole route. The printed solution line is cut off at 'OPV is of 2 types:', but the stem, all four options and the key are present, so the tagging does not rest on it.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lysosomes are single-membrane vesicles of the endomembrane system, while mitochondria, chloroplasts and the nucleus are each bounded by two membranes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The outer membrane of the nuclear envelope is printed as continuous with the ER, so the nucleus gets filed with the one-membrane endomembrane compartments. The envelope is still two parallel membranes with the perinuclear space between them.
- **Why:** This question requires the stated membrane count for each named organelle, demonstrated by the stem asking which is 'enclosed by a single membrane' with four coordinate organelles and no criterion printed to apply. Lysosome and nucleus are not alike as names, so the swap test leaves position doing the work: nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In tetanus the stimuli arrive before the muscle can relax, so successive twitches fuse into one sustained contraction
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Tonus is defined as a sustained state of partial contraction, so the stem's phrase 'sustained muscle contraction' lands on it. Tonus is held without any train of stimuli, and it is stimuli arriving before relaxation that the stem describes.
- **Why:** This question requires the stated name for one muscle response, demonstrated by the stem's defining clause 'lack of relaxation between successive stimuli' with four muscle-state terms as options. Replacing 'Tonus' with the unlike words 'muscle tone' leaves the pull intact, so adjacency and not likeness carries the student: nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tendrils of cucumber, thorns of Citrus and the flattened phylloclade of Opuntia are modified stems; the pitcher of Nepenthes is a modified leaf
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The tendril is the one item printed in both taught lists, and the pea tendril is the leaf list's standard example, so 'tendril equals modified leaf' marks cucumber as the non-stem case. The cucumber tendril arises from an axillary bud, which is why it sits in the stem list.
- **Why:** This question requires the organ each taught example is a modification of, demonstrated by option 1's 'Pitcher of Nepenthes' sitting in the leaf list while the other three are printed entries of the stem list. Nepenthes and cucumber are not alike as names, so the swap test leaves list position doing the work: nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Anthocyanins are the water-soluble pigments held in the vacuole, while chlorophylls, carotenoids and xanthophylls are fat-soluble pigments inside plastids
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Carotenoids are the pigments printed as the carriers of yellow, orange and red colour in plants, so 'the pigment that colours the plant' lands there. The same line calls them fat soluble and places them in chromoplasts, not in the vacuole.
- **Why:** This question requires the stated pigment of one named compartment, demonstrated by the stem's 'water soluble pigments found in plant cell vacuoles' against three options that are plastid pigments. Anthocyanin and carotenoid are unlike as names, so the swap test shows the pull comes from the colour fact printed beside it: nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperms are heterosporous and their leaves withstand climatic extremes; Sequoia is among the tallest trees and Salvinia is a pteridophyte, not a gymnosperm
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Ginkgo and Pinus are the two gymnosperms every list prints, so a set opening with them reads as a gymnosperm set. Salvinia is an aquatic fern, and the statement is accepted or rejected whole.
- **Why:** This question requires each printed claim about gymnosperms to be graded separately against the stated line, demonstrated by 'Select the correct statement' over four standalone claims of which option 3's 'Sequoia is one of the tallest trees' survives. Option 2 bundles 'Salvinia, ginkgo and pinus' so that two correct members cannot save it, which is why the trap is half_right and not a lone wrong name.
- **Note:** The only NOT in this question sits inside option 4; the task itself is the plain instruction 'Select the correct statement'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA fingerprinting runs on restriction digestion, electrophoresis, blotting, probe hybridisation and, in present-day practice, PCR amplification; zinc finger analysis is a DNA-binding protein motif and no part of it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The printed step list of DNA fingerprinting carries restriction digestion and probe hybridisation but not PCR, which is taught in another chapter, so the item missing from that list reads as the item not needed. The stem asks about 'the techniques of DNA fingerprinting available at present', and present-day profiling amplifies the repeat regions by PCR first.
- **Why:** This question requires the printed inventory of what DNA fingerprinting uses, demonstrated by 'Polymerase chain reaction', 'Restriction enzymes' and 'DNA – DNA hybridization' all being parts of the method while 'Zinc finger analysis' names a DNA-binding protein motif. PCR and zinc finger are unlike as names, so the swap test leaves position in the remembered step list doing the work: nearby_fact.
- **Note:** 'Zinc finger analysis' carries the word finger, which echoes 'fingerprinting', but that resemblance sits on the keyed answer, so it is not recorded as the trap — a trap is written only for a wrong option.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Every animal tissue has a named location in NCERT, and smooth muscle is the muscle of the walls of hollow visceral organs such as the intestine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  "Lining of stomach" is the location NCERT prints for columnar epithelium, the type listed immediately beside cuboidal, so a student holding only "the gut is lined by a simple epithelium" accepts the pair. Cuboidal is NCERT's epithelium of gland ducts and the tubular parts of nephrons.
- **Why:** This question requires the location NCERT states for each named tissue, demonstrated by the option "Cuboidal epithelium | Lining of stomach", which attaches to cuboidal the location NCERT gives to columnar epithelium.
- **Note:** E1_question_type reads statement_options, but each option is printed as a Tissue | Location pair accepted or rejected whole, so the shape recorded here is two_part. Likeness test applied on the trap axis: the wrong names (areolar, cuboidal, transitional) do not resemble the right one, and each is reachable because NCERT prints it in the same list as the tissue that owns the location, so nearby_fact rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** C4 plants concentrate CO2 in the bundle sheath, so they lose nothing to photorespiration, peak at high temperature, and need less Rubisco and less water per unit of carbon fixed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  CAM is the other carbon-concentrating adaptation NCERT prints for hot dry habitats, so a student reading "improved water use efficiency" and "high temperatures" stops at the adjacent adaptation. CAM keeps its stomata shut by day and fixes carbon slowly, which contradicts the printed "high rates of photosynthesis".
- **Why:** This question requires the properties NCERT states for one physiological group, demonstrated by the stem asking "In which of the following physiological groups would you assign this plant?" after printing four of the traits listed for C4 plants.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Homology is shared ancestral structure -- the same forelimb bones reshaped for different jobs -- while analogy is shared function built from different structures
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The wing of an insect against the wing of a bird is the pair NCERT prints to illustrate ANALOGY, so a student who recognises the pair answers with it. It is the true answer to a question about analogous organs, and this stem asked for a homologous one.
- **Why:** This question requires the homology criterion applied to four named structures, demonstrated by the stem asking which structure is "homologus to the wing of a bird" while printing the moth wing, which shares the function and none of the bones.
- **Note:** look_alike_term was ruled out for option 2: the pull is not that two names resemble each other but that the moth wing is the printed answer to the analogy question, which is what answers_other_question names. "homologus" is the spelling as printed in the stem.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A class feature holds only as far as NCERT states it: the reptilian three-chambered heart and mammalian viviparity each carry a printed exception, while the cartilaginous endoskeleton of Chondrichthyes carries none
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  "Heart is usually three-chambered" is NCERT's own line for Reptilia, so a student who checks the feature against the class and not against the stem's word "always" accepts it. NCERT prints the exception in the same sentence -- the crocodile heart is four-chambered.
- **Why:** This question requires a class feature that the source states without exception, demonstrated by the stem's "always holds true" set against the option "3 - chambered heart with one incompletely divided ventricle | Reptilia".
- **Note:** E1_question_type reads plain_mcq, but each option is printed as a feature | group pair judged whole, the same shape as q142, so two_part is recorded. The printed solution line is cut off mid-sentence ("In mammals, prototheria group"), though it names both exceptions that decide the key and all four options are present, so the key stands as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cancer cells switch telomerase ON -- the enzyme that rebuilds telomeres and lets the line divide without limit -- so the mutations that matter remove brakes rather than add them
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  "Destroy telomerase inhibitor" carries two negatives, and a student who collapses them to one reads the option as telomerase being shut down, which is the false claim, and ticks it as the statement that is not true. Destroying the inhibitor raises telomerase activity, which is what cancer cells do.
- **Why:** This question requires the direction in which cancer mutations move telomerase activity, demonstrated by the key option "Mutations inhibit production of telomerase" standing against "Mutations destroy telomerase inhibitor".
- **Note:** look_alike_term was weighed for options 2 and 4, which share the word telomerase, but the pull is the inverted net direction of a double negative rather than two different names resembling each other, so reversed is recorded. The printed solution line is cut off mid-sentence; it states the direction that decides the key, and the key is option 4 as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tryptophan is the amino acid from which serotonin and melatonin are built, while the thyroid hormones come from tyrosine and the gonadal and adrenal cortex hormones from cholesterol
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Tryptophan and tyrosine are the two hormone-precursor amino acids whose names open alike, and the thyroid pair is the one taught as built from an amino acid, so a student holding "amino-acid-derived hormone means thyroid hormone" reads the stem's tryptophan as tyrosine. Thyroxine and triiodothyronine are iodinated tyrosine.
- **Why:** This question requires the precursor the source states for a named hormone pair, demonstrated by the stem "The amino acid Tryptophan is the precursor for the synthesis of:" with the tyrosine-derived thyroid pair printed as option 2.
- **Note:** Likeness test applied: replace tryptophan and tyrosine with two unlike names and the pull on option 2 dies, so look_alike_term rather than nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Life began on an oxygen-free earth: the first organisms were non-green anaerobic heterotrophs and the first autotrophs were chemoautotrophs, with oxygen-releasing photosynthesis arriving only at a later stage
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The oxygen-releasing stage is printed just after the chemoautotrophs in the same origin-of-life sequence, so a student carrying 'the first photosynthesisers released oxygen and changed the atmosphere' reads that fact back onto the first autotrophs and marks (ii) false while keeping (i), which is exactly option 1.
- **Why:** This question requires two printed origin-of-life facts to be checked one at a time against the stated sequence, demonstrated by statement (ii) 'The first autotrophic organisms were the chemoautotrophs that never released oxygen', which is settled by what the book states about that stage and not by any criterion the stem supplies.
- **Note:** Trap tie-breaks applied. Against look_alike_term: the swap test — replace 'chemoautotroph' and the later photoautotrophs with two unlike words and the pull survives, because what carries the student is the adjacent printed stage of one sequence, not any likeness between the names, so nearby_fact. Against half_right: in the Statement I/II format every mixed verdict is literally two parts, so shape alone would put half_right on all such options and the label would carry no information; the thinking that actually fails here is the substitution of the neighbouring stage's fact. Against wrong_site_attacked: the option is a truth verdict and relocates nothing itself; no site or stage is named in the printed option. Stem as supplied reads as two sentences run together ('Following are the two statements ... Of the above statements which one of the following options is correct?'), with the two statements carried in the statements block; the answer line is cut off mid-sentence after 'oxygen was not available on', which does not affect the key or the labels.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bohr effect: a fall in blood pH lowers haemoglobin's affinity for oxygen, so oxyhaemoglobin unloads O2 in the tissues
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  A fall in blood pH is answered in the body by bicarbonate, so a student holding 'bicarbonate buffers the acid' picks the bicarbonate option without checking the organ; that bicarbonate comes from CO2 hydration inside the erythrocyte and from the kidney, not from the liver
- **Why:** This question requires the stated effect of a pH fall on haemoglobin's oxygen binding, demonstrated by the stem "Reduction in $\mathrm{pH}$ of blood will:" standing over four rival outcomes with no quantity to compute and no criterion printed to apply.
- **Note:** E1's pattern recorded statement_options. The printed shape is a completion stem whose options are rival outcomes of a stated change, not a lettered block and not an instruction to grade statements, so on the current axis this is mcq; q153 is the member of this group whose stem does ask for a statement verdict.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Analogy means similar function from unrelated ancestry and is produced by convergent evolution, while homology comes from one ancestral plan diverging
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Divergent and convergent are stored as one matched pair of -vergent terms with homology on one side and analogy on the other, so a student who holds the pair but not its direction writes in divergent; divergence is what turns a single ancestral plan into homologous organs
- **Why:** This question requires the named process printed as the cause of analogy, demonstrated by the stem "Analogous structures are a result of:" over four process names with no structures given to compare.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Restriction endonucleases cut DNA only at their own recognition sequence, which is what separates them from general nucleases
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  DNase I is the other DNA-cutting nuclease that sits in the same enzyme family as restriction enzymes, so a student holding only 'a restriction enzyme is the enzyme that cuts DNA' stops at the option with DNA in its name; DNase I cuts DNA anywhere, and the recognition sequence is what the definition turns on
- **Why:** This question requires the stated membership of one named enzyme in the restriction-endonuclease class, demonstrated by the stem "Which of the following is a restriction endonuclease?" over four bare enzyme names with no substrate or site printed to reason from.
- **Note:** Swap test applied: replacing Hind II and DNase I with two unlike words leaves the trap standing, because what carries the student is DNase I belonging to the same DNA-cutting family, not any resemblance between the two names — so nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Attribution of ecological terms: ecosystem is Tansley's 1935 coinage, while ecology is Haeckel's and Odum's work is the later functional account
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Odum is the name fastened to the ecosystem concept in all the energy-flow, trophic-level and productivity material, so a student who stores one name per topic reads that attachment as the coinage; the word itself is Tansley's and Odum's contribution was describing how the unit works
- **Why:** This question requires one stored attribution, demonstrated by the stem "The term ecosystem was coined by:" over four ecologists' names, with nothing in the stem that could be reasoned from instead.
- **Note:** Swap test applied: replacing Odum and Tansley with two unlike names leaves the trap standing, since the pull is both names belonging to the same ecosystem attribution cluster rather than any resemblance between them.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Glycine is the simplest amino acid, with hydrogen as its side chain; cysteine and methionine are the sulphur-containing ones
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Purine and pyrimidine are held as one paired set of class names and uracil has to be filed under one of them, so a student carrying the pair the wrong way round reads "Uracil is a pyrimidine" as the false statement and stops before reaching glycine
- **Why:** This question requires four separate stored classification facts, each checked on its own, demonstrated by the stem "Which one of the following statements is wrong?" over claims about sucrose, cellulose, uracil and glycine that share no single criterion.
- **Note:** E1's pattern recorded statement_options and the stem does ask for a verdict on statements, so qtype is statements here; the negated task word WRONG is what puts the pull on the three true statements rather than on a false one.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bryophyte and pteridophyte male gametes are flagellate, so fertilisation needs a film of water and ties these groups to moist habitats
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Wind is an agent these two groups genuinely depend on — for carrying spores, not gametes — so a student who remembers that moss and fern spores are blown about answers the dispersal question instead of the one asked; the antherozoids are flagellate and still have to swim
- **Why:** This question requires the stated requirement for fertilisation in these two groups, demonstrated by the stem "In bryophytes and pteridophytes, transport of male gametes requires:" over four carrying agents with no structure or condition given to reason from.
- **Note:** answers_other_question was taken over wrong_site_attacked because wind is not the right agent misplaced to another stage — it is the true answer to a different printed question, spore dispersal, whereas q149's bicarbonate option is the right change moved to the wrong organ.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In the logistic equation the growth rate is the product $rN(1 - N/K)$, so it reaches zero when the population exactly equals the carrying capacity and the bracket vanishes
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The S-curve is carried in memory as a curve that levels off as the population approaches K, so "nears the carrying capacity" reads as the place where growth has stopped. While N only nears K the bracket $(1 - N/K)$ is small but still positive, so that answers when growth slows, not when $dN/dt$ is zero.
- **Why:** This question requires the printed logistic relation to be applied to find the condition that makes the rate vanish, demonstrated by the stem supplying "$dN/dt = rN(1 - N/K)$" and the options offering rival values of $N/K$.
- **Note:** On a literal reading option 3 also gives a zero rate, since $N/K = 0$ means $N = 0$ and $rN(1 - N/K)$ is then zero; the key rests on the non-degenerate reading of a population that stops growing. Tagged as printed, with the doubt recorded here.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The anther wall divides the labour: the tapetum nourishes the developing pollen grains, while dehiscence is carried out by the stomium of the endothecium
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Exine and intine are learnt as a pair of near-identical names, and sporopollenin is stored against whichever of the two the ear supplies; with the pair the wrong way round, "exine is made up of sporopollenin" is the sentence that reads false, and the stem is asking for the false one.
- **Why:** This question requires the stated function of one named anther wall layer, demonstrated by option 1 "Tapetum helps in the dehiscence of anther" having to be graded against the printed role of the tapetum in nourishing the developing pollen.
- **Note:** Option 3 reads "allegies" for "allergies" in our record; the meaning is unaffected and the question is tagged as stored. The §5.1 test was applied to the trap: swap exine and intine for two unlike words and the pull dies, so the likeness is doing the work rather than position.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lichens are the pioneer community of succession on bare rock, and bryophytes can only follow after lichens have corroded the rock into a film of soil
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The Plant Kingdom line that mosses, along with lichens, are among the first organisms to colonise rocks is the sentence a student retrieves here, and it prints the two names together. On bare rock the lichen stage comes first, and the moss stage needs the soil film the lichens make.
- **Why:** This question requires the named pioneer community of a bare-rock succession, demonstrated by the stem's "pioneer organisms on bare rocks" set against four coordinate groups with no criterion printed to apply.
- **Note:** The §5.1 test was applied: lichen and moss do not resemble each other as words, and swapping them for unlike names leaves the pull intact because it rests on the sentence that prints the two together, so the label is nearby_fact rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** AUG is the single initiation codon and also codes for methionine, while UAA, UAG and UGA are the three codons that terminate translation
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The start codon is stored as the one built from A, U and G, and UAG carries exactly those three letters in another order, so the memory of the letters alone settles on it. Order is what makes a codon, and UAG with A in the middle is a termination codon.
- **Why:** This question requires one stored triplet, the codon at which translation begins, demonstrated by the stem's "the starter codon" with four codons as the options.
- **Note:** The §5.1 test was applied: replace AUG and UAG with two triplets sharing no letters and the pull disappears, so the resemblance is carrying the student, not the table position that UAA and UGA share with UAG.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Birds and mammals share ossified bone, lung breathing and warm blood as the two endothermic classes; viviparity is the mammalian character that no bird has
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The Aves description states in one breath that the endoskeleton is fully ossified and that the long bones are hollow with air cavities, and the pneumatic half is the half a flight-adaptation answer keeps. Hollow bone is still ossified bone, so ossification is shared and is not what the stem is after.
- **Why:** This question requires two warm-blooded classes to be held against each other across four characters, demonstrated by the stem's "not shared by birds and mammals" with three of the four characters belonging to both classes.
- **Note:** asks is compare rather than fact_line because the work is sorting which characters both classes carry; the deciding fact, that birds are oviparous, only becomes usable once the other three are confirmed as shared.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The agreed conventions of binomial nomenclature are Latinised names, genus first and specific epithet second, italics in print and underlining by hand, which leaves no room for writing a biological name in any language
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Beside the italics rule the source records that the names are taken from Latin or Greek and are Latinised whatever their origin, and a student holding that line reads "written in Latin" as too narrow and marks it the rule-breaker. Latinisation is the rule itself, so this option states the convention rather than breaking it.
- **Why:** This question requires the agreed rules of binomial nomenclature as the source states them, demonstrated by "Biological names can be written in any language" standing against "The names are written in Latin and are italicized".
- **Note:** The §5.1 test was applied: Latin and Greek are unlike words, and the pull survives their replacement because it rests on the origin line printed beside the italics rule, so nearby_fact rather than look_alike_term. The printed solution attributes the rules to IUCN, which governs conservation status rather than nomenclature; the question is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Within one circuit pressure falls from artery to vein, and the whole pulmonary circuit runs far below the systemic one
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The 120/80 mm Hg figure is printed for the systemic artery leaving the left ventricle, so a student carrying 'arterial blood pressure is 120/80' applies the one stored figure to the other great artery leaving the heart and reads the pulmonary artery as equal to the aorta. The right ventricle pumps only to the lungs, so the pulmonary artery runs at roughly a fifth of the aortic pressure.
- **Why:** This question requires the pressure in the pulmonary artery to be ranked against four other named vessels, demonstrated by every option being a comparison - 'Same as that in the aorta', 'More than that in the carotid', 'Less than that in the venae cavae'.
- **Note:** E1_question_type reads statement_options, but the stem is a sentence the options complete, no statement block is printed and nothing is asked to be judged, so the printed shape is recorded as mcq. The stored answer line stops at 'Blood pressure in different blood vessels:' and the table it introduces is not in our record; the keyed option text is unambiguous on its own and the question is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The maize grain's single shield-shaped cotyledon is the scutellum; the coleoptile and coleorhiza are sheaths over the plumule and radicle
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Coleoptile is printed in the same grain paragraph as scutellum and is the name most often attached to maize, so a student who remembers that the maize embryo has specially named parts but not which name labels which part reaches for the familiar one. The coleoptile is the sheath enclosing the plumule, not a cotyledon.
- **Why:** This question requires the stated name given to the maize cotyledon, demonstrated by the stem 'Cotyledon of maize grain is called' with four coordinate grain-part names as options. Swap test applied: replace 'coleoptile' with an unlike word for another part printed in the same paragraph and the pull survives, because what carries the student is that the name sits beside scutellum in the grain description - so nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** HCl comes from the parietal (oxyntic) cells of the gastric glands, while gastrin is the hormone that stimulates them
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Gastrin' and 'gastric acid' differ by a syllable, so the hormone's name is read as belonging to the acid's own cells, and the genuine link - gastrin drives HCl secretion - closes the identification. Gastrin is only the signal; the acid is released by the parietal cells it acts on.
- **Why:** This question requires the stated gastric gland cell that secretes HCl, demonstrated by the stem 'gastric acid is secreted by the' with four named cell types as options. Swap test applied: replace 'gastrin' with an unlike hormone name and the pull dies, because nothing then connects that cell to the words 'gastric acid' - the resemblance is doing the work, and by the tie-break resemblance wins over the fact that gastrin is printed in the same chapter.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stratospheric ozone absorbs UV-B, so a thinner ozone layer lets UV-B reach the skin and raises skin-cancer incidence
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each of the other three gases against both halves of the stem. Ozone is the only one of the four that the chapter discusses as being lost from the atmosphere, and the UV-B-to-skin-cancer line is printed with it; nitrous oxide and methane appear as gases that accumulate and warm, and ammonia appears in neither discussion, so reaching any of them means discarding the stem's own word 'depletion'.
- **Why:** This question requires the stated gas whose thinning admits UV-B, demonstrated by the stem 'Depletion of which gas in the atmosphere can lead to an increased incidence of skin cancers'.
- **Note:** no_trap is recorded after testing all three wrong options separately, not as a gap: the decisive printed word is 'depletion', and of the four gases only ozone is ever discussed as being depleted.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Kingdom Protista holds the eukaryotic unicellular groups - chrysophytes, euglenoids, dinoflagellates - together with the saprophytic slime moulds
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Slime mould' carries the word mould, and the moulds a student meets by name are fungi, so the one unfamiliar member of the printed list is filed under the kingdom its name resembles. Slime moulds are saprophytic protists and have no fungal mycelium.
- **Why:** This question requires the kingdom assigned to these four groups, demonstrated by the stem naming 'Chrysophytes, Euglenoids, Dinoflagellates and Slime moulds' with four kingdoms as options. Swap test applied: position also holds, since Fungi is the kingdom printed next to Protista in the five-kingdom scheme, but renaming slime moulds to an unlike word kills the pull to Fungi, so the resemblance is doing the work and by the tie-break resemblance wins.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Water vapour leaving and $\mathrm{CO_2}$ entering share the same open stomata at the same time, each gas diffusing down its own gradient at its own rate
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A student who has learnt that CAM plants open their stomata at night to take in $\mathrm{CO_2}$ and shut them by day to save water uses that timetable to settle the stem's apparent clash, separating the two fluxes in time. Night opening is a condition of arid-adapted CAM plants, and the stem describes an ordinary leaf in photosynthesis, where both fluxes run together.
- **Why:** This question requires the reason two opposite fluxes can share one pore, demonstrated by the stem's instruction to 'Reason out the above statements' and the keyed option 'Both processes can happen together because the diffusion coefficient of water and $\mathrm{CO_2}$ is different'.
- **Note:** E1_question_type reads statement_options, but two statements are printed in the stem and the instruction is to reason them out, with each option a full rival statement to be judged, so the shape is recorded as statements. It is not assertion_reason: nothing is labelled Assertion or Reason and the options are explanations rather than truth verdicts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Urea is made in the liver, so the vein draining the liver carries the most urea, while a vessel entering the liver or leaving the kidney carries less
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Urea is made in the liver, so a student looks for the liver's vessel and takes the other option that also says 'hepatic' — but the hepatic portal vein runs gut to liver and carries the ammonia and amino acids going in, not the urea coming out
- **Why:** This question requires the site of urea synthesis to be combined with the direction a named vessel carries blood, demonstrated by the stem asking 'which blood vessel would normally carry largest amount of urea' over options that print one organ's inflow and outflow side by side, 'Hepatic vein' and 'Hepatic portal vein'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Apomixis is seed formation without fertilisation — a seed produced on a flowering plant by an asexual route
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Without fertilization' reads as 'asexual', and sporulation is one of the asexual routes printed in the same reproduction list, so the student answers the category instead of the question — but spores are not seeds
- **Why:** This question requires the single term the source gives for seed set without fertilisation, demonstrated by the stem 'Seed formation without fertilization in flowering plants involves the process of:' standing over four coordinate process names with no criterion printed to apply.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each bioactive molecule NCERT lists belongs to one named microbe - cyclosporin A to Trichoderma, statins to Monascus purpureus, streptokinase to Streptococcus - while Clostridium butylicum's product is butyric acid, not lipase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Trichoderma is the fungus NCERT names in the biocontrol section of this same chapter, so a student holding 'Trichoderma works on plant pathogens' sees a human transplant drug in its row and flags that row as the planted mismatch. The same genus is also the book's source of cyclosporin A, so the row is matched correctly.
- **Why:** This question requires the microbe-to-product-to-use pairings NCERT prints for bioactive molecules, demonstrated by the stem asking which row is 'wrongly matched' while every option prints nothing but a microbe, its product and that product's application.
- **Note:** E1's statement_options is carried across as qtype statements: no statement block is printed, the stem is a bare instruction, and each option is one claim graded whole. The claim is rendered as a three-column row (Microbe / Product / Application) rather than as a sentence, which is the 'table' structure this group was formed on; it is not match_columns, since no two columns are printed to pair and the answer is not a pairing code. Separately, answer_line_as_printed stops mid-sentence at 'Candida lipolyticum is the source of' - the stem, all four options and the key are complete, so this is not a damaged record and the truncation is in the solution text only. One mechanism is deliberately left untagged: option 4's product and application cells are right (lipase does remove oily stains) and only its microbe is wrong, so a student who checks product against application validates the key row and hunts elsewhere - but a trap may not be written on the official answer.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** A dihybrid testcross gives parental and recombinant classes in equal numbers when the genes are on different chromosomes, so an excess of parental types means the genes are linked on one chromosome
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Dropping the stem's word 'testcross' and reaching for the F2 dihybrid 9:3:3:1, in which the both-dominant parental class is the largest, makes an excess of parental offspring look like ordinary independent assortment on two chromosomes
- **Why:** This question requires a supplied cross result to be interpreted before anything else can start, demonstrated by the stem reporting that 'more parental - type offspring were produced than the recombinant - type offspring' and then asking what it 'indicates'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Metabolic rate per unit body mass rises as animals get smaller, and that rate is what sustains the power for a climb
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  A small animal does lift less weight uphill, so the statement is true as printed — but it answers how much work the climb costs, not why the small animal copes better, since the small animal's muscle is proportionally smaller too
- **Why:** This question requires the reason behind a fact the stem grants, demonstrated by the stem ending 'because:' after stating that it 'is much easier for a small animal to run uphill', with each option offering a rival cause.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Synapsis, the pairing of homologous chromosomes, belongs to prophase I of meiosis; mitosis in somatic cells has spindle fibres, nucleolar disappearance and chromosome movement but no pairing
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The single word 'not' is what sets this task; read as 'which is a characteristic feature during mitosis', the stem makes spindle fibres the answer, and spindle fibres are a true mitotic feature answering the question that was not asked
- **Why:** This question requires the stated fact that synapsis is a meiotic event, demonstrated by the stem asking for what is 'not a characteristic feature during mitosis in somatic cells' while the other three options name events the mitotic account already contains.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Many pollen grains of the right species can germinate and send tubes into the style; the pistil screens pollen by compatibility, not by a one-tube limit
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 4  
  The pollinator list a student carries is bees, butterflies, birds and bats, and 'some reptiles' sits outside it, so in a question asking which statement is NOT correct the unfamiliar-looking true line is the one that gets struck out
- **Proposed:** `unfamiliar_true_line` — the option is a true line from the source, printed once and outside the list the student rehearsed, and a negated stem turns that unfamiliarity into a reason to grade it false; `answers_other_question` does not fit because the student picks it believing it FALSE rather than because it answers something else, and `nearby_fact` needs the option itself to be a wrong fact printed beside the right one, whereas here the option is correct
- **Why:** This question requires one printed claim about pollen-pistil interaction to be graded false, demonstrated by option 1's 'only one pollen tube of the same species grows into the style' against a stem asking which statement 'is not correct'.
- **Note:** The keyed option reads as the source's own sentence about pollen grains of many species germinating on the stigma, with a one-tube limit substituted for the compatibility clause; tagged as printed, and the printed solution supplies that reading ('More the one pollen tube of same species can grow into the style').
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Subsidiary cells are the modified epidermal cells that flank the guard cells of a stoma; complementary cells belong to the lenticel instead
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who has filed 'the helper cells at an epidermal opening' under complementary cells, the name the same chapter uses for the loose cells of a lenticel, carries that pairing across to the stomatal pore, where the flanking cells are the subsidiary cells.
- **Why:** This question requires the stated name of the cells beside the guard cells, demonstrated by 'Specialized epidermal cells surrounding the guard cells are called' with four coordinate epidermal terms as options and no criterion printed to apply. Swap test applied to the trap: rename complementary cells to an unlike word and the pull survives, because what carries the student is its being printed as the cells at the chapter's other opening, so nearby_fact rather than look_alike_term.
- **Note:** answer_line_as_printed is cut off mid-sentence at 'guard cells have', but the stem, all four options and the key are complete, so the question is rated as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each junction along the gut has its own guard: the hepatopancreatic duct opens into the duodenum through the sphincter of Oddi, while the pyloric sphincter guards the stomach's outlet
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  Anchoring on the word 'duodenum' retrieves the sphincter learnt as the duodenum's guard, the pyloric sphincter at the stomach's outlet, so the right kind of structure is named for the wrong opening.
- **Why:** This question requires the stated fact of which sphincter guards one named opening, demonstrated by 'guards the opening of hepatopancreatic duct into the duodenum', which supplies the site and leaves only the structure's name to be filled in.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A phylloclade is a flattened green stem doing the leaf's work; a phyllode is a flattened petiole, and a cladode is the one-or-two-internode case of a phylloclade
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Phyllode' and 'phylloclade' differ by two letters in the middle, and the stem's 'performing the functions of leaves' pulls on the shared phyll- root, so the half-held name arrives in place of its twin.
- **Why:** This question requires the printed term that goes with one stem modification, demonstrated by 'Stems modified into flat green organs performing the functions of leaves are known as'. Swap test applied to the trap: replace 'phyllode' with an unlike word and the pull dies, because 'Stems modified' already rules a petiole out on content and only the resemblance to 'phylloclade' could have carried the student there, so look_alike_term rather than nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Methanogens are the archaebacteria of the ruminant gut and of the biogas plant; halophiles and thermoacidophiles are the other two habitat groups of the same primitive division
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Primitive prokaryotes' places the answer among the archaebacteria, and a student then has to choose one of the three habitat groups printed in a single line, taking the first-named one instead of the methane-maker.
- **Why:** This question requires the named prokaryote group tied to one product, demonstrated by 'primitive prokaryotes responsible for the production of biogas from the dung of ruminant animals'. Swap test applied to the trap: rename halophiles to an unlike word and the pull survives, because being printed in the same list as methanogens is what carries the student, so nearby_fact rather than look_alike_term.
- **Note:** All three wrong options carry a route here, so no filler is recorded: options 1 and 2 are the other two members of the same printed archaebacterial list, and option 4 is reached by dropping the stem's word 'primitive'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Organic sewage feeds decomposers that strip the dissolved oxygen, so the fish suffocate even though the nutrient load has gone up
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Reading sewage as fertiliser — biodegradable nutrients feeding the food chain — turns the fish response the wrong way round, because the microbes that eat those nutrients take the oxygen the fish breathe.
- **Why:** This question requires the causal chain the book gives between an organic load and fish mortality, demonstrated by 'An increased production of fish due to biodegradable nutrients' standing against 'Death of fish due to lack of oxygen' — two opposite directions for the single change the stem states.
- **Note:** E1_question_type reads statement_options because each option is a full sentence. Under the current qtype axis, long sentences as options do not make a question statements: no lettered block is printed and the stem asks for an outcome rather than for statements to be judged, so the shape recorded here is mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A failed cell plate at telophase leaves both whole chromosome sets in one cell, which is polyploidy; aneuploidy is the gain or loss of one or a few chromosomes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The stem's 'more number of chromosomes' is read as a changed chromosome count, and the chapter prints aneuploidy and polyploidy together as the two chromosomal number changes, so the companion term is supplied in place of the right one.
- **Why:** This question requires a definition applied to a described observation, demonstrated by 'There is no formation of cell plate and thus the cell is containing more number of chromosomes as compared to other dividing cells', which supplies the observation and leaves the student to classify it. Swap test applied to the trap: rename aneuploidy to an unlike word and the pull survives, because it is its being printed as the other member of the same chromosomal-number pair that carries the student, so nearby_fact rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A fat is a triglyceride: one glycerol esterified with three fatty acids, one at each of glycerol's three hydroxyl groups
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The remembered shape of a fat is 'three of one component and one of the other', and the word triglyceride puts the three next to glycerol, so the counts get attached the wrong way round; glycerol is the single backbone, and the three sits on the fatty acids.
- **Why:** This question requires the stated composition of a fat molecule, demonstrated by four options that differ only in how many of each component they name, the key reading 'One glycerol and three fatty acid molecules'.
- **Note:** E1's pattern returned statement_options on '15 full-statement options', but no statement block is printed and the stem gives no instruction to judge statements, so by the qtype rule on long options this is mcq. The stem as stored reads 'A typical fat molecules is made up of:' - a grammatical slip in the source that does not change what is asked; tagged as printed.
<!--/ecat-->

