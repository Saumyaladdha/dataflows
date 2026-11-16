# NEET (UG) 2019 · Code P1

180 questions · source `NEET_Papers/2019/NEET_2019_Code_P1_official.pdf` · every image a CDN link (0 without one) · 32 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Mechanical Properties of Solids

When a block of mass $M$ is suspended by a long wire of lenght $L$, the length of the wire becomes $(L + l)$. The elastic potential energy stored in the extended wire is:

- (1) $Mgl$
- (2) $MgL$
- **(3)** $\frac{1}{2}Mgl$
- (4) $\frac{1}{2}MgL$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The stretching force on the wire is $F = Mg$ and the extension is $\Delta L = (L + l) - L = l$.
2. Elastic potential energy stored in a stretched wire is $U = \frac{1}{2} F \, \Delta L$.
3. $U = \frac{1}{2}(Mg)(l) = \frac{1}{2}Mgl$, which is option $3$.

**Subtopic:** Elastic Potential Energy of a Strained Body · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q001_01c379d2_28102026.png?v=01c379d2fcb5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The load on a stretching wire grows from zero to $Mg$ as the wire extends, so the energy stored is the average force times the extension, $\tfrac{1}{2}Mgl$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Taking the stored energy as force times distance, $Mg\times l$, uses the work formula for a CONSTANT force, but the restoring force in the wire climbs from $0$ to $Mg$, so the right expression carries a factor $\tfrac{1}{2}$
- **Why:** This question requires an expression derived from a stated relation, demonstrated by the stem giving the extension as "the length of the wire becomes $(L + l)$" and asking for "the elastic potential energy stored".
<!--/ecat-->

## Q2

Physics · Laws of Motion

A mass $m$ is attached to a thin wire and whirled in a vertical circle. The wire is most likely to break when:

- (1) the mass is at the highest point
- (2) the wire is horizontal
- **(3)** the mass is at the lowest point
- (4) inclined at an angle of $60^\circ$ from vertical

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Radial equation at angle $\theta$ from the lowest point: $T - mg\cos\theta = \frac{mv^2}{r}$.
2. So $T = \frac{mv^2}{r} + mg\cos\theta$.
3. Energy conservation gives $v$ largest at the lowest point ($\theta = 0$), where $\cos\theta = 1$ is also largest.
4. Hence $T_{max} = \frac{mv_{low}^2}{r} + mg$ at the lowest point, so the wire is most likely to break there: option $3$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q002_dcbe9df4_28102026.png?v=dcbe9df4eb8a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In a vertical circle the wire's tension is largest where it must both turn the mass and carry its full weight, which is the lowest point: $T = \frac{mv^2}{r} + mg$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The highest point is the answer to "where is the tension least and where does the string go slack", which is the condition every vertical-circle derivation is built around, so a student reaches for it when asked where the wire is most stressed
- **Why:** This question requires a known force relation applied to a new position, demonstrated by the stem asking when "the wire is most likely to break" with no numbers printed and four positions on the circle offered.
- **Note:** The E1 pattern called this `statement_options` on option length, but the stem is a trailing "when:" and the options are positions, not statements to be graded true or false, so the printed shape is a plain MCQ.
<!--/ecat-->

## Q3

Physics · Magnetic Effect of Electric Current

Ionized hydrogen atoms and $\alpha$-particles with same momenta enters perpendicular to a constant magnetic field, $B$. The ratio of their radii of their paths $r_H : r_\alpha$ will be :

- **(1)** $2 : 1$
- (2) $1 : 2$
- (3) $4 : 1$
- (4) $1 : 4$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For a charge moving perpendicular to $B$: $qvB = \frac{mv^2}{r}$, so $r = \frac{mv}{qB} = \frac{p}{qB}$.
2. With the same $p$ and $B$, $r \propto \frac{1}{q}$.
3. $q_H = e$ (proton) and $q_\alpha = 2e$.
4. $\frac{r_H}{r_\alpha} = \frac{q_\alpha}{q_H} = \frac{2e}{e} = 2$, so $r_H : r_\alpha = 2 : 1$, which is option $1$.

**Subtopic:** Motion in a Magnetic Field · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q003_c52f0081_28102026.png?v=c52f0081e214)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a charge moving perpendicular to a magnetic field $r = \frac{p}{qB}$, so at equal momentum the radius depends on charge alone and the doubly charged particle turns on half the radius
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  With $p$ and $B$ fixed, $r$ goes as $1/q$, so writing the ratio as $r_H : r_\alpha = q_H : q_\alpha = 1 : 2$ puts the charge on the wrong side of the fraction and inverts the answer
- **Why:** This question requires how one quantity scales with another, demonstrated by the stem supplying "same momenta" and "a constant magnetic field, $B$" and asking only for "the ratio of their radii".
<!--/ecat-->

## Q4

Physics · Work, Energy and Power

Body A of mass $4m$ moving with speed $u$ collides with another body B of mass $2m$, at rest. The collision is head on and elastic in nature. After the collision the fraction of energy lost by the colliding body A is :

- (1) $\frac{1}{9}$
- **(2)** $\frac{8}{9}$
- (3) $\frac{4}{9}$
- (4) $\frac{5}{9}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For a 1-D elastic collision with B at rest, $v_A = \frac{m_1 - m_2}{m_1 + m_2} u$.
2. $v_A = \frac{4m - 2m}{4m + 2m} u = \frac{u}{3}$.
3. $\frac{K_A'}{K_A} = \left(\frac{v_A}{u}\right)^2 = \frac{1}{9}$.
4. Fraction of energy lost by A $= 1 - \frac{1}{9} = \frac{8}{9}$, which is option $2$.

**Subtopic:** Problems on Elastic Collision · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q004_8726c4ce_28102026.png?v=8726c4ceb476)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a head-on elastic collision the striker leaves with $v = \frac{m_1-m_2}{m_1+m_2}u$, so here it keeps $u/3$ and therefore one ninth of its energy, having lost the other eight ninths
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\tfrac{1}{9}$ is the fraction of its energy A KEEPS: $v = u/3$ makes the final kinetic energy $\left(\tfrac{1}{3}\right)^2$ of the initial, and reporting that answers "how much is left" rather than "how much was lost"
- **Why:** This question requires a number computed from the stem's masses and speed, demonstrated by the stem printing "mass $4m$ moving with speed $u$", "mass $2m$, at rest" and "head on and elastic" and asking for "the fraction of energy lost".
<!--/ecat-->

## Q5

Physics · Wave Optics

In a double slit experiment, when light of wavelength $400\,\mathrm{nm}$ was used, the angular width of the first minima formed on a screen placed $1\,\mathrm{m}$ away, was found to be $0.2^\circ$. What will be the angular width of the first minima, if the entire experimental apparatus is immersed in water? $(\mu_{\mathrm{water}} = 4/3)$

- (1) $0.266^\circ$
- **(2)** $0.15^\circ$
- (3) $0.05^\circ$
- (4) $0.1^\circ$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The angular width of a fringe is $\theta = \frac{\lambda}{d}$, which does not depend on the screen distance $D$.
2. In water the wavelength becomes $\lambda' = \frac{\lambda}{\mu} = \frac{400\,\mathrm{nm}}{4/3} = 300\,\mathrm{nm}$.
3. So $\theta' = \frac{\lambda'}{d} = \frac{\theta}{\mu}$.
4. $\theta' = 0.2^\circ \times \frac{3}{4} = 0.15^\circ$, which is option $2$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q005_201fc1dd_28102026.png?v=201fc1dd7c14)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular fringe width goes as the wavelength, and immersing the apparatus shortens the wavelength to $\lambda/\mu$, so every angular width shrinks by the same factor $\mu$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  $0.2^\circ \times \tfrac{4}{3} = 0.266^\circ$ is what multiplying by $\mu$ gives, but water SHORTENS the wavelength to $\lambda/\mu$, so the angular width must be divided by $\tfrac{4}{3}$, not multiplied
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing an angular width of $0.2^\circ$ in air and $(\mu_{\mathrm{water}} = 4/3)$ for the immersed apparatus.
<!--/ecat-->

## Q6

Physics · Electromagnetic Induction

In which of the following devices, the eddy current effect is not used?

- (1) Induction furnace
- (2) Magnetic braking in train
- (3) Electromagnet
- **(4)** Electric heater

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT lists the applications of eddy currents: magnetic braking in trains, electromagnetic damping, induction furnaces and electric power meters.
2. An induction furnace heats metal through eddy currents set up by a high-frequency alternating field, so it uses the effect.
3. Magnetic braking in trains uses eddy currents induced in the rails or discs to oppose the motion, so it uses the effect.
4. An electric heater produces heat as $H = I^2 R t$ in its resistive element (Joule heating), with no eddy currents involved, so option $4$.

**Subtopic:** Eddy Currents · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q006_40381d0f_28102026.png?v=40381d0f5f8b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Eddy currents are the induced loops that a changing flux drives through a solid conductor, and the devices built on them are the induction furnace, magnetic braking, electromagnetic damping and the energy meter
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The induction furnace is the first application listed for eddy currents, so it is the right answer to this question with the "not" removed, and a student working down the list for the device that DOES use the effect stops here
- **Why:** This question requires the stated list of a named effect's applications read against a negated task, demonstrated by the stem "In which of the following devices, the eddy current effect is not used?" with two listed applications among the four options.
- **Note:** Two options satisfy the stem as written: an electromagnet uses no eddy currents either, since its core is laminated to suppress them and a steady current induces none, so option 3 is defensible on the physics while the key rests on the textbook's application list. The tag follows the printed key, option 4, and the doubt is recorded here and in the flag.
<!--/ecat-->

## Q7

Physics · Mechanical Properties of Fluids

A soap bubble, having radius of $1\,\mathrm{mm}$, is blown from a detergent solution having a surface tension of $2.5 \times 10^{-2}\,\mathrm{N/m}$. The pressure inside the bubble equals at a point $Z_0$ below the free surface of water in a container. Taking $g = 10\,\mathrm{m/s^2}$, density of water $= 10^3\,\mathrm{kg/m^3}$, the value of $Z_0$ is :

- (1) $100\,\mathrm{cm}$
- (2) $10\,\mathrm{cm}$
- **(3)** $1\,\mathrm{cm}$
- (4) $0.5\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A soap bubble has two free surfaces, so the excess pressure inside is $\Delta P = \frac{4T}{r}$.
2. $\Delta P = \frac{4 \times 2.5 \times 10^{-2}}{1 \times 10^{-3}} = 100\,\mathrm{Pa}$.
3. Pressure inside the bubble $= P_0 + \Delta P$, and pressure at depth $Z_0$ in water $= P_0 + \rho g Z_0$.
4. Equating: $\rho g Z_0 = \Delta P \Rightarrow Z_0 = \frac{100}{10^3 \times 10} = 0.01\,\mathrm{m}$.
5. $Z_0 = 0.01\,\mathrm{m} = 1\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Excess Pressure on Curved Surface (General Case, Drop, Soap Bubbles, Air Bubbles) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q007_1ecf6159_28102026.png?v=1ecf61594498)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A soap bubble has two liquid surfaces, so its excess pressure is $\frac{4S}{r}$, and setting that equal to $\rho g Z_0$ gives the depth at which the water pressure matches it
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Using $\frac{2S}{r}$, the excess pressure for a single-surface drop, gives $50\,\mathrm{Pa}$ instead of $100\,\mathrm{Pa}$ and so $Z_0 = 0.5\,\mathrm{cm}$; a bubble blown from solution has an inner and an outer surface, which is where the $4$ comes from
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing $r = 1\,\mathrm{mm}$, $S = 2.5\times10^{-2}\,\mathrm{N/m}$, $g = 10\,\mathrm{m/s^2}$ and $\rho = 10^3\,\mathrm{kg/m^3}$ and asking for "the value of $Z_0$".
<!--/ecat-->

## Q8

Physics · Electromagnetic Waves

Which colour of the light has the longest wavelength?

- **(1)** Red
- (2) Blue
- (3) Green
- (4) Violet

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the visible spectrum the wavelengths are ordered $\lambda_{\text{violet}} < \lambda_{\text{blue}} < \lambda_{\text{green}} < \lambda_{\text{red}}$, so red ($\approx 700\,\text{nm}$) is the longest, which is option $1$.

**Subtopic:** Electromagnetic Spectrum · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q008_64d4431b_28102026.png?v=64d4431b7354)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Across the visible spectrum wavelength falls from red to violet, so red is the long-wavelength end and violet the short
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Violet is the other end of the same spectrum, so a student who holds the sequence but not which end is which reads "longest" off the wrong end of VIBGYOR
- **Why:** This question requires one stated fact about the spectrum, demonstrated by the stem "Which colour of the light has the longest wavelength?" with four colour names and no wavelengths printed.
- **Note:** The answer is a single name rather than a sequence, which is why this is fact_line and not order, even though what decides it is the spectral trend.
<!--/ecat-->

## Q9

Physics · Rotational Motion

A disc of radius $2\,\mathrm{m}$ and mass $100\,\mathrm{kg}$ rolls on a horizontal floor. Its centre of mass has speed of $20\,\mathrm{cm/s}$. How much work is needed to stop it?

- **(1)** $3\,\mathrm{J}$
- (2) $30\,\mathrm{kJ}$
- (3) $2\,\mathrm{J}$
- (4) $1\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Work needed to stop the disc equals its total kinetic energy (work-energy theorem).
2. For rolling without slipping, $KE = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$ with $I = \frac{1}{2}mR^2$ and $\omega = \frac{v}{R}$.
3. $KE = \frac{1}{2}mv^2 + \frac{1}{4}mv^2 = \frac{3}{4}mv^2$.
4. $v = 20\,\mathrm{cm/s} = 0.2\,\mathrm{m/s}$, so $KE = \frac{3}{4} \times 100 \times (0.2)^2 = 3\,\mathrm{J}$, which is option $1$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q009_3bc22f0d_28102026.png?v=3bc22f0db8f4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A rolling body carries translational and rotational kinetic energy together, so for a disc the work needed to stop it is $\tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2 = \tfrac{3}{4}mv^2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  $\tfrac{1}{2}mv^2 = \tfrac{1}{2}\times100\times(0.2)^2 = 2\,\mathrm{J}$ is the translational energy alone, which leaves out the $\tfrac{1}{2}I\omega^2$ the disc also carries because it is rolling, not sliding
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing a radius of $2\,\mathrm{m}$, a mass of $100\,\mathrm{kg}$ and a centre-of-mass speed of $20\,\mathrm{cm/s}$ and asking "how much work is needed to stop it".
- **Note:** The radius is printed but cancels, since $\omega = v/r$ and $I = \tfrac{1}{2}mr^2$ leave the energy depending on $m$ and $v$ alone.
<!--/ecat-->

## Q10

Physics · Oscillations

The displacement of a particle executing simple harmonic motion is given by $y = A_0 + A\sin\omega t + B\cos\omega t$ Then the amplitude of its oscillation is given by :

- (1) $A_0 + \sqrt{A^2 + B^2}$
- **(2)** $\sqrt{A^2 + B^2}$
- (3) $\sqrt{A_0^2 + (A + B)^2}$
- (4) $A + B$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Write $y - A_0 = A\sin\omega t + B\cos\omega t$; the constant $A_0$ only shifts the mean position and does not change the amplitude.
2. Set $A = R\cos\phi$ and $B = R\sin\phi$, so $A\sin\omega t + B\cos\omega t = R\sin(\omega t + \phi)$.
3. Squaring and adding: $R^2 = A^2 + B^2$, so $R = \sqrt{A^2 + B^2}$.
4. Hence $y = A_0 + \sqrt{A^2 + B^2}\,\sin(\omega t + \phi)$ and the amplitude is $\sqrt{A^2 + B^2}$, which is option $2$.

**Subtopic:** Calculate Amplitude of SHM, Composition of Two SHMs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q010_7bde941f_28102026.png?v=7bde941f5489)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A sine and a cosine of the same frequency are a quarter cycle apart, so they combine to one SHM of amplitude $\sqrt{A^2+B^2}$ about a mean position shifted by the constant $A_0$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $A_0 + \sqrt{A^2+B^2}$ is the largest value $y$ ever reaches, which is a real quantity in this problem, but the amplitude is measured from the mean position $y = A_0$, so the constant does not belong in it
- **Why:** This question requires an expression derived from the printed displacement, demonstrated by the stem giving $y = A_0 + A\sin\omega t + B\cos\omega t$ and asking for "the amplitude of its oscillation".
<!--/ecat-->

## Q11

Physics · Ray Optics

Two similar thin equi-convex lenses, of focal length $f$ each, are kept coaxially in contact with each other such that the focal length of the combination is $F_1$. When the space between the two lenses is filled with glycerin (which has the same refractive index ($\mu = 1.5$) as that of glass) then the equivalent focal length is $F_2$. The ratio $F_1 : F_2$ will be :

- (1) $2 : 1$
- **(2)** $1 : 2$
- (3) $2 : 3$
- (4) $3 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For each equi-convex glass lens, $\frac{1}{f} = (\mu - 1)\left(\frac{2}{R}\right) = 0.5 \times \frac{2}{R} = \frac{1}{R}$, so $R = f$.
2. Two lenses in contact: $\frac{1}{F_1} = \frac{1}{f} + \frac{1}{f} = \frac{2}{f}$, so $F_1 = \frac{f}{2}$.
3. Glycerin filling the gap forms an equi-concave lens with radii $R$: $\frac{1}{f_g} = (1.5 - 1)\left(-\frac{2}{R}\right) = -\frac{1}{f}$.
4. Combination of three lenses: $\frac{1}{F_2} = \frac{2}{f} - \frac{1}{f} = \frac{1}{f}$, so $F_2 = f$.
5. $F_1 : F_2 = \frac{f}{2} : f = 1 : 2$, which is option $2$.

**Subtopic:** Combination of Thin Lenses in Contact, Lens Maker Formula · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 3)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q011_e9ce14de_28102026.png?v=e9ce14deafa0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Powers add for lenses in contact, and glycerin of the same refractive index as the glass acts as a diverging lens of equal and opposite power, so filling the gap cancels one of the two lenses
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  $F_1 = f/2$ for the two lenses in contact and $F_2 = f$ once the glycerin cancels one of them, so the ratio asked for is $1:2$; writing it as $2:1$ reports the same two numbers in the order they were computed rather than in the order the stem names them
- **Why:** This question requires how one quantity stands to the same quantity after a change, demonstrated by the stem defining $F_1$ before and $F_2$ after the gap is filled and asking "the ratio $F_1 : F_2$".
<!--/ecat-->

## Q12

Physics · Kinetic Theory of Gases

Increase in temperature of a gas filled in a container would lead to :

- (1) Increase in its mass
- **(2)** Increase in its kinetic energy
- (3) Decrease in its pressure
- (4) Decrease in intermolecular distance

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Average kinetic energy per molecule is $\bar{E}_k = \frac{3}{2} k_B T$, so a rise in $T$ raises the kinetic energy, which is option $2$; mass stays the same, and in a fixed container $P \propto T$ rises while intermolecular distance does not decrease, so options $1$, $3$ and $4$ are wrong.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q012_689eeba5_28102026.png?v=689eeba528bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Temperature is the measure of the mean kinetic energy of the molecules, so heating a gas raises that energy whatever the container does
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A gas heated at constant pressure expands, and a student who carries that picture into a closed container turns the expansion into a fall in pressure, when a fixed volume gives the opposite: faster molecules hitting the walls harder raise the pressure
- **Why:** This question requires a known rule applied to a stated change, demonstrated by the stem "Increase in temperature of a gas filled in a container would lead to :" with the container fixed and four outcomes offered.
- **Note:** The E1 pattern called this `statement_options` on option length, but the stem is a trailing "would lead to :" and the options are outcomes rather than statements graded true or false, so the shape is a plain MCQ.
<!--/ecat-->

## Q13

Physics · Modern Physics

An electron is accelerated through a potential difference of $10{,}000\,\mathrm{V}$. Its de Broglie wavelength is, (nearly) : ($m_e = 9 \times 10^{-31}\,\mathrm{kg}$)

- (1) $12.2 \times 10^{-13}\,\mathrm{m}$
- **(2)** $12.2 \times 10^{-12}\,\mathrm{m}$
- (3) $12.2 \times 10^{-14}\,\mathrm{m}$
- (4) $12.2\,\mathrm{nm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Kinetic energy gained: $\frac{p^2}{2m} = eV$, so $p = \sqrt{2meV}$.
2. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2meV}}$.
3. $\sqrt{2meV} = \sqrt{2 \times 9\times10^{-31} \times 1.6\times10^{-19} \times 10^{4}} = \sqrt{2.88\times10^{-45}} \approx 5.37\times10^{-23}\,\mathrm{kg\,m/s}$.
4. $\lambda = \frac{6.63\times10^{-34}}{5.37\times10^{-23}} \approx 1.23\times10^{-11}\,\mathrm{m}$ (equivalently $\frac{1.227}{\sqrt{10^4}}\,\mathrm{nm} = 0.01227\,\mathrm{nm}$).
5. $\lambda \approx 12.2\times10^{-12}\,\mathrm{m}$, which is option $2$.

**Subtopic:** de Broglie Wavelength of an Accelerated Charged Particle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q013_2508539b_28102026.png?v=2508539bc04f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An electron accelerated through $V$ carries momentum $\sqrt{2meV}$, so its de Broglie wavelength is $\frac{h}{\sqrt{2meV}}$, which the shortcut writes as $\frac{12.27}{\sqrt{V}}$ ångström
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The wavelength comes out as $1.22\times10^{-11}\,\mathrm{m}$ and every option is printed with the mantissa $12.2$, so the last move is to shift the decimal one place; shifting it while dropping the exponent by two instead of one gives $12.2\times10^{-13}$
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing "a potential difference of $10{,}000\,\mathrm{V}$" and "$m_e = 9\times10^{-31}\,\mathrm{kg}$" and asking for the de Broglie wavelength.
- **Note:** All four options share the mantissa $12.2$, so the whole option set turns on the power of ten and the unit; that is why both routes recorded here are exponent-and-unit routes rather than physics routes.
<!--/ecat-->

## Q14

Physics · Thermal Properties of Matter

A copper rod of $88\,\mathrm{cm}$ and an aluminium rod of unknown length have their increase in length independent of increase in temperature. The length of aluminium rod is : ($\alpha_{\mathrm{Cu}} = 1.7 \times 10^{-5}\,\mathrm{K^{-1}}$ and $\alpha_{\mathrm{Al}} = 2.2 \times 10^{-5}\,\mathrm{K^{-1}}$)

- (1) $6.8\,\mathrm{cm}$
- (2) $113.9\,\mathrm{cm}$
- (3) $88\,\mathrm{cm}$
- **(4)** $68\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The difference in lengths stays the same at every temperature only if $\Delta L_{\mathrm{Cu}} = \Delta L_{\mathrm{Al}}$.
2. $L_{\mathrm{Cu}}\,\alpha_{\mathrm{Cu}}\,\Delta T = L_{\mathrm{Al}}\,\alpha_{\mathrm{Al}}\,\Delta T \Rightarrow L_{\mathrm{Al}} = \frac{L_{\mathrm{Cu}}\,\alpha_{\mathrm{Cu}}}{\alpha_{\mathrm{Al}}}$.
3. $L_{\mathrm{Al}} = \frac{88 \times 1.7 \times 10^{-5}}{2.2 \times 10^{-5}} = \frac{149.6}{2.2} = 68\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Thermal Expansion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q014_adf24824_28102026.png?v=adf248246ea3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Two rods keep a constant difference in length only if each expands by the same amount, which needs $L_{\mathrm{Cu}}\alpha_{\mathrm{Cu}} = L_{\mathrm{Al}}\alpha_{\mathrm{Al}}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  $88\times\frac{2.2}{1.7} = 113.9\,\mathrm{cm}$ is the ratio taken the wrong way up; aluminium expands MORE per unit length, so to expand by the same amount it must be the SHORTER rod
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing the copper rod as $88\,\mathrm{cm}$ with $\alpha_{\mathrm{Cu}} = 1.7\times10^{-5}\,\mathrm{K^{-1}}$ and $\alpha_{\mathrm{Al}} = 2.2\times10^{-5}\,\mathrm{K^{-1}}$.
<!--/ecat-->

## Q15

Physics · Ray Optics

Pick the wrong answer in the context with rainbow.

- (1) When the light rays undergo two internal reflections in a water drop, a secondary rainbow is formed
- (2) The order of colours is reversed in the secondary rainbow
- **(3)** An observer can see a rainbow when his front is towards the sun
- (4) Rainbow is a combined effect of dispersion refraction and reflection of sunlight

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A secondary rainbow comes from two internal reflections inside the drop, so option $1$ is correct.
2. In the secondary rainbow the order of colours is reversed (violet outside, red inside), so option $2$ is correct.
3. A rainbow comes from dispersion, refraction and internal reflection of sunlight in drops, so option $4$ is correct.
4. The rainbow is seen only with the sun behind the observer (antisolar point in front), so option $3$ is the wrong statement.

**Subtopic:** Dispersion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q015_46c34083_28102026.png?v=46c340835c2c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A rainbow is seen only with the sun behind the observer, because the light that reaches the eye has been refracted into the drop, internally reflected at its back and refracted out again
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The colour order really is reversed in the secondary bow, so a student who holds the secondary bow as "the same colours, fainter and higher" reads this true line as the planted error and marks it
- **Why:** This question requires printed statements about one phenomenon graded one by one against a negated task, demonstrated by the stem "Pick the wrong answer in the context with rainbow" above three true statements and one false one.
- **Note:** All three wrong options are true statements, so each is reached by grading a true line as the false one; the trap is placed on option 2 because it is the one a specific stored belief, that the secondary bow shows the same colour order, marks as wrong.
<!--/ecat-->

## Q16

Physics · Gravitation

A body weighs $200\,\mathrm{N}$ on the surface of the earth. How much will it weigh half way down to the centre of the earth ?

- (1) $150\,\mathrm{N}$
- (2) $200\,\mathrm{N}$
- (3) $250\,\mathrm{N}$
- **(4)** $100\,\mathrm{N}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Below the surface, $g_d = g\left(1 - \frac{d}{R}\right)$.
2. Half way down, $d = \frac{R}{2}$, so $g_d = g\left(1 - \frac{1}{2}\right) = \frac{g}{2}$.
3. $W' = m g_d = \frac{mg}{2} = \frac{200\,\mathrm{N}}{2} = 100\,\mathrm{N}$, which is option $4$.

**Subtopic:** Variation in g Due to Depth Inside the Earth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q016_881b5824_28102026.png?v=881b58247bfd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Inside the earth only the mass below you pulls, so $g$ falls linearly with depth: $g' = g\left(1-\frac{d}{R}\right)$, which halves the weight halfway to the centre
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $200\times\left(1-\frac{1}{4}\right) = 150\,\mathrm{N}$ is what $g' = g\left(1-\frac{d}{2R}\right)$ gives, the depth formula written with the $2$ that belongs to the small-height expansion $g\left(1-\frac{2h}{R}\right)$ above the surface
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing a surface weight of $200\,\mathrm{N}$ and the position "half way down to the centre of the earth".
<!--/ecat-->

## Q17

Physics · Current Electricity

Six similar bulbs are connected as shown in the figure with a DC source of emf $E$ and zero internal resistance. The ratio of power consumption by the bulbs when (i) all are glowing and (ii) in the situation when two from section A and one from section B are glowing, will be :

![printed figure: Six similar bulbs: three in parallel in section A, in series with three in parallel in section B, across a cell E](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q017_0decd398_28102026.svg?v=0decd3983e9d)

*Six similar bulbs: three in parallel in section A, in series with three in parallel in section B, across a cell E*

![drawn: Six similar bulbs: three in parallel in section A, in series with three in parallel in section B, across a cell E](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q017_question_ff8f7fef_28102026.svg?v=ff8f7fef0267)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $4:9$
- **(2)** $9:4$
- (3) $1:2$
- (4) $2:1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. From the figure, section A has 3 bulbs in parallel, section B has 3 bulbs in parallel, and A and B are in series across $E$; let each bulb have resistance $R$.
2. Case (i): $R_1 = \frac{R}{3} + \frac{R}{3} = \frac{2R}{3}$.
3. $P_1 = \frac{E^2}{R_1} = \frac{3E^2}{2R}$.
4. Case (ii): two bulbs in A give $\frac{R}{2}$, one bulb in B gives $R$, so $R_2 = \frac{R}{2} + R = \frac{3R}{2}$.
5. $P_2 = \frac{E^2}{R_2} = \frac{2E^2}{3R}$.
6. $\frac{P_1}{P_2} = \frac{3/2}{2/3} = \frac{9}{4}$, which is option $2$.

**Subtopic:** Electrical Energy and Power, Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q017_b00c1c9a_28102026.png?v=b00c1c9a74ef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Three identical bulbs in parallel present a third of one bulb's resistance, so removing bulbs raises the circuit's resistance and the total power drawn falls as $P = E^2/R_{\mathrm{total}}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The two totals are $\frac{2R}{3}$ with all six glowing and $\frac{3R}{2}$ with three glowing, so the powers stand as $\frac{3}{2}:\frac{2}{3}$, which is $9:4$; writing $4:9$ reports the resistances' ratio instead, and power goes inversely with resistance
- **Why:** This question requires how one quantity stands to the same quantity in a second situation, demonstrated by the stem asking for "the ratio of power consumption by the bulbs when (i) all are glowing and (ii) ... two from section A and one from section B are glowing".
- **Note:** The figure is needed and was supplied: three bulbs in parallel in section A, in series with three in parallel in section B, across a cell of zero internal resistance. The answer is still a ratio of one quantity to itself in two situations, which is why `asks` is relation rather than read_diagram.
<!--/ecat-->

## Q18

Physics · Semiconductor Electronics

For a p-type semiconductor, which of the following statements is true ?

- (1) Electrons are the majority carriers and trivalent atoms are the dopants.
- **(2)** Holes are the majority carriers and trivalent atoms are the dopants.
- (3) Holes are the majority carriers and pentavalent atoms are the dopants.
- (4) Electrons are the majority carriers and pentavalent atoms are the dopants.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Doping with trivalent (acceptor) atoms leaves one bond incomplete per dopant, creating a hole, so $n_h \gg n_e$ and holes are the majority carriers in a p-type semiconductor, which is option $2$.

**Subtopic:** P-Type Semiconductor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q018_acb0ad22_28102026.png?v=acb0ad227126)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Doping silicon with a trivalent atom leaves a vacancy in the bonding, so a p-type semiconductor conducts chiefly by holes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first half is right, holes are the majority carriers, and the second half takes the dopant from the letter: "p" and "pentavalent" share it, so the pentavalent atom is attached to the p-type crystal
- **Why:** This question requires two stated facts about one named material, demonstrated by the stem "For a p-type semiconductor, which of the following statements is true ?" above four statements each pairing a carrier type with a dopant valency.
- **Note:** The stem asks which printed statement is true, which is what makes the shape `statements`; each of those statements is itself two claims joined by "and", which is what allows the half_right label on an option whose carrier half is correct.
<!--/ecat-->

## Q19

Physics · Oscillations

Average velocity of a particle executing SHM in one complete vibration is :

- (1) $\frac{A\omega}{2}$
- (2) $A\omega$
- (3) $\frac{A\omega^{2}}{2}$
- **(4)** Zero

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Average velocity is $\bar{v} = \frac{\Delta x}{\Delta t}$.
2. After one full period $T$, $x(T) = A\sin(\omega T + \phi) = A\sin(2\pi + \phi) = x(0)$, so $\Delta x = 0$.
3. $\bar{v} = \frac{0}{T} = 0$, which is option $4$.

**Subtopic:** Velocity in SHM · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q019_18a2943e_28102026.png?v=18a2943eba0d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Average velocity is net displacement divided by time, and over one full vibration the particle returns to where it started, so the displacement and hence the average velocity are zero
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Averaging the two extreme speeds, $0$ at the ends and $A\omega$ at the centre, gives $\frac{A\omega}{2}$, but an average over a cycle is the net displacement over the time, not the arithmetic mean of a maximum and a minimum
- **Why:** This question requires a definition applied to a stated interval, demonstrated by the stem asking for the average velocity "in one complete vibration" with no numbers printed.
<!--/ecat-->

## Q20

Physics · Thermal Properties of Matter

The unit of thermal conductivity is :

- (1) $\mathrm{J\,m\,K^{-1}}$
- (2) $\mathrm{J\,m^{-1}\,K^{-1}}$
- (3) $\mathrm{W\,m\,K^{-1}}$
- **(4)** $\mathrm{W\,m^{-1}\,K^{-1}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Fourier's law of heat conduction: $H = \frac{Q}{t} = K A \frac{\Delta T}{\Delta x}$.
2. Rearrange: $K = \frac{H\,\Delta x}{A\,\Delta T}$.
3. Units: $[K] = \frac{\mathrm{W}\cdot\mathrm{m}}{\mathrm{m^2}\cdot\mathrm{K}} = \mathrm{W\,m^{-1}\,K^{-1}}$, which is option $4$.

**Subtopic:** Thermal Conduction and Its Formula · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q020_d60c4e0e_28102026.png?v=d60c4e0ee0de)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Thermal conductivity is defined through the RATE of heat flow, $\frac{Q}{t} = kA\frac{\Delta T}{L}$, so its unit is $\mathrm{W\,m^{-1}\,K^{-1}}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Building the unit from $Q$ instead of $\frac{Q}{t}$ leaves the joule in place of the watt, and gives $\mathrm{J\,m^{-1}\,K^{-1}}$ with the metre power otherwise right
- **Why:** This question requires a defining relation turned into a unit, demonstrated by the four options differing only in joule against watt and metre against inverse metre.
<!--/ecat-->

## Q21

Physics · Rotational Motion

A solid cylinder of mass $2\,\mathrm{kg}$ and radius $4\,\mathrm{cm}$ rotating about its axis at the rate of $3\,\mathrm{rpm}$. The torque required to stop after $2\pi$ revolutions is

- **(1)** $2 \times 10^{-6}\,\mathrm{N\,m}$
- (2) $2 \times 10^{-3}\,\mathrm{N\,m}$
- (3) $12 \times 10^{-4}\,\mathrm{N\,m}$
- (4) $2 \times 10^{6}\,\mathrm{N\,m}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\omega_0 = 3\,\mathrm{rpm} = \frac{3 \times 2\pi}{60} = \frac{\pi}{10}\,\mathrm{rad\,s^{-1}}$.
2. $\theta = 2\pi\ \text{rev} = 2\pi \times 2\pi = 4\pi^2\,\mathrm{rad}$.
3. $0 = \omega_0^2 - 2\alpha\theta \Rightarrow \alpha = \frac{\omega_0^2}{2\theta} = \frac{\pi^2/100}{8\pi^2} = \frac{1}{800}\,\mathrm{rad\,s^{-2}}$.
4. $I = \frac{1}{2}MR^2 = \frac{1}{2} \times 2 \times (0.04)^2 = 1.6 \times 10^{-3}\,\mathrm{kg\,m^2}$.
5. $\tau = I\alpha = \frac{1.6 \times 10^{-3}}{800} = 2 \times 10^{-6}\,\mathrm{N\,m}$, which is option $1$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 4)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q021_1c7d3015_28102026.png?v=1c7d30157d7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Stopping a rotating body takes $\tau = I\alpha$ with $\alpha = \frac{\omega^2}{2\theta}$, so every quantity has to be in SI units first: the radius in metre, the rate in radian per second and the turning in radian
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  $r^2 = (0.04)^2 = 1.6\times10^{-3}$, and keeping the $1.6$ while dropping the $10^{-3}$ makes $I = 1.6\,\mathrm{kg\,m^2}$ instead of $1.6\times10^{-3}$, which multiplies the torque by $10^3$ and gives exactly $2\times10^{-3}\,\mathrm{N\,m}$
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem printing a mass of $2\,\mathrm{kg}$, a radius of $4\,\mathrm{cm}$, a rate of $3\,\mathrm{rpm}$ and a turning of $2\pi$ revolutions.
- **Note:** Option 3 carries the mantissa $12$, which matches the one wrong route this problem offers other than a power slip -- the turning taken in revolutions instead of radians -- but that route ends at $12.6\times10^{-6}$, not at the printed $12\times10^{-4}$. A reviewer with the printed paper should check whether that option reads $12\times10^{-6}$; as stored, no route reaches it, which is why it is recorded as a filler rather than as the trap.
<!--/ecat-->

## Q22

Physics · Work, Energy and Power

A force $F = 20 + 10\,y$ acts on a particle in $y$-direction where $F$ is in newton and $y$ in meter. Work done by this force to move the particle from $y = 0$ to $y = 1\,\mathrm{m}$ is

- (1) $30\,\mathrm{J}$
- (2) $5\,\mathrm{J}$
- **(3)** $25\,\mathrm{J}$
- (4) $20\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Force varies with position, so $W = \int_{0}^{1} F\,dy = \int_{0}^{1} (20 + 10y)\,dy$.
2. $\int (20 + 10y)\,dy = 20y + 5y^2$.
3. $W = [20y + 5y^2]_{0}^{1} = 20 + 5 = 25\,\mathrm{J}$, which is option $3$.

**Subtopic:** Work Done by Variable Force · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q022_1c6b8095_28102026.png?v=1c6b809592be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** When the force changes along the path the work is the area under the force-displacement line, $W=\int F\,dy$, which here is $20 + 5 = 25\,\mathrm{J}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Putting $y=1$ into $F = 20+10y$ gives $30\,\mathrm{N}$, and multiplying that by the $1\,\mathrm{m}$ uses $W = Fs$, which holds only for a force that does not change along the way
- **Why:** This question requires a number computed from the stem's own expression, demonstrated by the stem printing $F = 20 + 10\,y$ and the limits "from $y = 0$ to $y = 1\,\mathrm{m}$".
<!--/ecat-->

## Q23

Physics · Current Electricity

Which of the following acts as a circuit protects device?

- (1) Conductor
- (2) Inductor
- (3) Switch
- **(4)** Fuse

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A fuse is a wire of low melting point in series; excess current $I$ produces Joule heating $H = I^2 R t$ that melts it, opening the circuit, so the protective device is the fuse, option $4$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q023_8c00f995_28102026.png?v=8c00f9957cae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A fuse is the protective element of a circuit: a thin wire of low melting point that melts and breaks the circuit when the current exceeds its rating
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A switch does break a circuit, which is the right answer to "which device opens the circuit"; what it cannot do is break it BY ITSELF when the current runs too high, which is what protecting means here
- **Why:** This question requires one stated function of one named component, demonstrated by the stem asking which of the four "acts as a circuit protects device" with four component names and no circuit printed.
- **Note:** The stem as printed reads "circuit protects device", which looks like a printing slip for "circuit protection device"; the sense is not in doubt and the tag follows the question as printed.
<!--/ecat-->

## Q24

Physics · Current Electricity

In the circuits shown below, the readings of voltmeters and the ammeters will be

![printed figure: Circuit 1: 10 ohm resistor with voltmeter V1 across it, ammeter A1 and 10 V cell; Circuit 2: same with a 10 ohm resistor in series with voltmeter V2 across it](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q024_971b1263_28102026.svg?v=971b12637bc0)

*Circuit 1: 10 ohm resistor with voltmeter V1 across it, ammeter A1 and 10 V cell; Circuit 2: same with a 10 ohm resistor in series with voltmeter V2 across it*

![drawn: Circuit 1: 10 ohm resistor with voltmeter V1 across it, ammeter A1 and 10 V cell; Circuit 2: same with a 10 ohm resistor in series with voltmeter V2 across it](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q024_question_4715d456_28102026.svg?v=4715d4565905)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $V_2 > V_1$ and $i_1 = i_2$
- (2) $V_1 = V_2$ and $i_1 > i_2$
- **(3)** $V_1 = V_2$ and $i_1 = i_2$
- (4) $V_2 > V_1$ and $i_1 > i_2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. An ideal voltmeter has infinite resistance, so no current flows through any branch containing it.
2. Circuit 1: $i_1 = \frac{10\,\text{V}}{10\,\Omega} = 1\,\text{A}$ and $V_1 = i_1 R = 10\,\text{V}$.
3. Circuit 2: the branch with $10\,\Omega$ and $V_2$ carries zero current, so $i_2 = \frac{10\,\text{V}}{10\,\Omega} = 1\,\text{A}$.
4. The drop across the $10\,\Omega$ in series with $V_2$ is $0 \times 10 = 0$, so $V_2 = 10\,\text{V}$.
5. $V_1 = V_2 = 10\,\text{V}$ and $i_1 = i_2 = 1\,\text{A}$, which is option $3$.

**Subtopic:** Ammeter and Voltmeter in Circuits · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q024_9980e95a_28102026.png?v=9980e95a3cbe)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An ideal voltmeter draws no current, so a resistor placed in series with it carries no current, drops no voltage and changes neither the reading nor the current in the main circuit
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The voltmeter half is right, $V_1 = V_2$, and the ammeter half treats the extra $10\,\Omega$ as added circuit resistance, which would cut the current; but that resistor sits in the voltmeter's own branch, where no current flows
- **Why:** This question requires a known idealisation applied to a printed circuit, demonstrated by the stem asking for "the readings of voltmeters and the ammeters" in two circuits that differ only by a resistor drawn in series with the voltmeter.
- **Note:** The figure is needed and was supplied: both circuits hold a $10\,\Omega$ resistor across a $10\,\mathrm{V}$ cell with an ammeter in the main loop, and circuit 2 adds a $10\,\Omega$ resistor in series with its voltmeter. Each option is two comparisons that must both hold, which is why qtype is two_part and the trap can be half_right.
<!--/ecat-->

## Q25

Physics · Electrostatics

A hollow metal sphere of radius $R$ is uniformly charged. The electric field due to the sphere at a distance $r$ from the centre

- (1) Increases as $r$ increases for $r < R$ and for $r > R$
- **(2)** Zero as $r$ increases for $r < R$, decreases as $r$ increases for $r > R$
- (3) Zero as $r$ increases for $r < R$, increases as $r$ increases for $r > R$
- (4) Decreases as $r$ increases for $r < R$ and for $r > R$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For a Gaussian sphere of radius $r < R$, the enclosed charge is $q_{enc} = 0$ (all charge sits on the surface), so $E \cdot 4\pi r^2 = 0 \Rightarrow E = 0$.
2. For $r > R$, $q_{enc} = Q$, so $E \cdot 4\pi r^2 = \frac{Q}{\varepsilon_0} \Rightarrow E = \frac{Q}{4\pi\varepsilon_0 r^2}$.
3. $E \propto \frac{1}{r^2}$ decreases as $r$ increases for $r > R$; zero inside and decreasing outside is option $2$.

**Subtopic:** Field Due to a Uniformly Charged Thin Spherical Shell · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q025_00cd7fc4_28102026.png?v=00cd7fc417d7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A charged conductor holds its charge on the surface, so the field is zero everywhere inside the shell and outside it falls as $1/r^2$, exactly as if the charge sat at the centre
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Treating the sphere's charge as a point at the centre gives $E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}$ at every $r$, which is right for $r>R$ and wrongly makes the field grow as $r$ falls below $R$
- **Why:** This question requires the shell result applied to both regions of the same case, demonstrated by every option pairing a claim for '$r < R$' with a separate claim for '$r > R$'.
<!--/ecat-->

## Q26

Physics · Magnetic Effect of Electric Current

At a point A on the earth’s surface the angle of dip, $\delta = +25^\circ$. At a point B on the earth’s surface the angle of dip, $\delta = -25^\circ$. We can interpret that:

- (1) A and B are both located in the northern hemisphere.
- (2) A is located in the southern hemisphere and B is located in the northern hemisphere.
- **(3)** A is located in the northern hemisphere and B is located in the southern hemisphere.
- (4) A and B are both located in the southern hemisphere.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the northern hemisphere the north pole of a dip needle dips downward, so the angle of dip is taken positive; in the southern hemisphere it points upward, so the dip is negative.
2. At A, $\delta = +25^\circ > 0$, so A is in the northern hemisphere; at B, $\delta = -25^\circ < 0$, so B is in the southern hemisphere, which is option $3$.

**Subtopic:** Earth's Magnetism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q026_eaaf3c19_28102026.png?v=eaaf3c196e6a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The sign of the angle of dip records which way the earth's field tilts out of the horizontal: it is positive where the field points into the ground, which is the northern hemisphere
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Remembering that the earth's magnetic south pole lies near the geographic north leads to reading the field as coming up out of the ground there, which inverts the sign rule and swaps both locations
- **Why:** This question requires the dip-sign convention applied to two printed readings, demonstrated by the stem supplying nothing but '$\delta = +25^\circ$' at A and '$\delta = -25^\circ$' at B.
<!--/ecat-->

## Q27

Physics · Modern Physics

The total energy of an electron in an atom in an orbit is $-3.4\,\mathrm{eV}$. Its kinetic and potential energies are, respectively:

- (1) $-3.4\,\mathrm{eV}$, $-3.4\,\mathrm{eV}$
- (2) $-3.4\,\mathrm{eV}$, $-6.8\,\mathrm{eV}$
- **(3)** $3.4\,\mathrm{eV}$, $-6.8\,\mathrm{eV}$
- (4) $3.4\,\mathrm{eV}$, $3.4\,\mathrm{eV}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a Bohr orbit, $K = \frac{1}{2}\frac{kZe^2}{r}$, $U = -\frac{kZe^2}{r}$, so $U = -2K$ and $E = K + U = -K$.
2. $K = -E = -(-3.4\,\mathrm{eV}) = 3.4\,\mathrm{eV}$.
3. $U = 2E = 2 \times (-3.4\,\mathrm{eV}) = -6.8\,\mathrm{eV}$, which is option $3$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q027_18c0895e_28102026.png?v=18c0895edd06)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a Bohr orbit the kinetic energy is minus the total energy and the potential energy is twice it, so $E=-3.4\,\mathrm{eV}$ fixes $KE=+3.4\,\mathrm{eV}$ and $PE=-6.8\,\mathrm{eV}$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Getting $PE=2E=-6.8\,\mathrm{eV}$ right and then writing the kinetic energy as $-3.4\,\mathrm{eV}$, carrying the total energy's minus sign across on the view that a bound electron's energies are all negative
- **Why:** This question requires two values computed from one printed number and reported together, demonstrated by the stem's 'kinetic and potential energies are, respectively' and by each option carrying two entries.
<!--/ecat-->

## Q28

Physics · Ray Optics

In total internal reflection when the angle of incidence is equal to the critical angle for the pair of media in contact, what will be angle of refraction?

- (1) $180^\circ$
- (2) $0^\circ$
- (3) Equal to angle of incidence
- **(4)** $90^\circ$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Snell's law at the interface: $n_1 \sin i_c = n_2 \sin r$, with $\sin i_c = \frac{n_2}{n_1}$ by definition of the critical angle.
2. Substituting: $n_1 \cdot \frac{n_2}{n_1} = n_2 \sin r \Rightarrow \sin r = 1$.
3. $r = 90^\circ$, the refracted ray grazes the surface, which is option $4$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q028_1a41e1e8_28102026.png?v=1a41e1e8f426)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The critical angle is defined as the incidence at which the refracted ray grazes the boundary, so at that incidence the angle of refraction is $90^\circ$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  'Equal to angle of incidence' is the law of reflection — true of the reflected ray at every incidence — and the stem opens with 'In total internal reflection', which points at the reflected ray rather than at the refracted one the question asks about
- **Why:** This question requires Snell's law applied at the stated incidence, demonstrated by the stem's condition 'when the angle of incidence is equal to the critical angle for the pair of media in contact'.
<!--/ecat-->

## Q29

Physics · Gravitation

The work done to raise a mass $m$ from the surface of the earth to a height $h$, which is equal to the radius of the earth, is:

- (1) $mgR$
- (2) $2\,mgR$
- **(3)** $\frac{1}{2}mgR$
- (4) $\frac{3}{2}mgR$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Potential energy at distance $r$ from the centre: $U(r) = -\frac{GMm}{r}$.
2. At the surface $r = R$: $U_1 = -\frac{GMm}{R}$; at height $h = R$, $r = 2R$: $U_2 = -\frac{GMm}{2R}$.
3. $W = U_2 - U_1 = -\frac{GMm}{2R} + \frac{GMm}{R} = \frac{GMm}{2R}$.
4. Using $GM = gR^2$: $W = \frac{gR^2 m}{2R} = \frac{1}{2}mgR$, which is option $3$.

**Subtopic:** Gravitational Potential Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q029_8427eaa3_28102026.png?v=8427eaa399e1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Over a rise as large as the earth's radius $g$ is no longer constant, so the work is the change in $-GMm/r$, which comes to $\frac{1}{2}mgR$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Using $W=mgh$ with $h=R$ returns $mgR$ exactly; that formula holds only while the rise is small enough for $g$ to stay constant, and the stem has deliberately made the rise equal to the whole radius
- **Why:** This question requires the potential-energy difference worked out where $g$ cannot be treated as constant, demonstrated by the stem's 'to a height $h$, which is equal to the radius of the earth'.
<!--/ecat-->

## Q30

Physics · Kinematics

When an object is shot from the bottom of a long smooth inclined plane kept at an angle $60^\circ$ with horizontal, it can travel a distance $x_1$ along the plane. But when the inclination is decreased to $30^\circ$ and the same object is shot with the same velocity, it can travel $x_2$ distance. Then $x_1 : x_2$ will be:

- (1) $1:\sqrt{2}$
- (2) $\sqrt{2}:1$
- **(3)** $1:\sqrt{3}$
- (4) $1:2\sqrt{3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. On a smooth incline the only retarding acceleration along the plane is $a = g\sin\theta$.
2. Using $v^2 = u^2 - 2ax$ with $v = 0$: $x = \frac{u^2}{2g\sin\theta}$.
3. $\frac{x_1}{x_2} = \frac{\sin 30^\circ}{\sin 60^\circ} = \frac{1/2}{\sqrt{3}/2} = \frac{1}{\sqrt{3}}$.
4. So $x_1 : x_2 = 1 : \sqrt{3}$, which is option $3$.

**Subtopic:** Third Equation of Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q030_e781844c_28102026.png?v=e781844c7d82)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** On a smooth incline the retardation is $g\sin\theta$, so for a fixed launch speed the distance travelled up the plane goes as $1/\sin\theta$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Setting up $x\propto 1/\sin\theta$ correctly and then writing $\sin 60^\circ=\sqrt{3}$ instead of $\frac{\sqrt{3}}{2}$ turns $\frac{\sin 30^\circ}{\sin 60^\circ}$ into $\frac{1/2}{\sqrt{3}}=\frac{1}{2\sqrt{3}}$
- **Why:** This question requires how many times the distance up the plane changes when only the inclination changes, demonstrated by the options being bare ratios of '$x_1 : x_2$' with $v$ and $g$ nowhere in them.
<!--/ecat-->

## Q31

Physics · Modern Physics

$\alpha$-particle consists of :

- **(1)** 2 protons and 2 neutrons only
- (2) 2 electrons, 2 protons and 2 neutrons
- (3) 2 electrons and 4 protons only
- (4) 2 protons only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. An $\alpha$-particle is a doubly ionised helium nucleus, ${}^{4}_{2}\mathrm{He}^{2+}$, which has $Z = 2$ protons and $A - Z = 4 - 2 = 2$ neutrons and no electrons, which is option $1$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q031_74da2d46_28102026.png?v=74da2d46a4af)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An alpha-particle is a bare helium nucleus: two protons and two neutrons, with no electrons
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  '2 electrons, 2 protons and 2 neutrons' is the correct make-up of a neutral helium ATOM, so a student who identifies the alpha-particle as 'helium' answers for the atom instead of its nucleus. The particle is emitted from the nucleus and carries charge $+2e$, which it only has because the electrons are absent.
- **Why:** This question requires the stated composition of the alpha-particle, demonstrated by the stem '$\alpha$-particle consists of :' with four options differing only in which sub-atomic particles are listed.
<!--/ecat-->

## Q32

Physics · Kinematics

The speed of a swimmer in still water is $20\,\mathrm{m/s}$. The speed of river water is $10\,\mathrm{m/s}$ and is flowing due east. If he is standing on the south bank and wishes to cross the river along the shortest path the angle at which he should make his strokes w.r.t. north is given by :

- **(1)** $30^\circ$ west
- (2) $0^\circ$
- (3) $60^\circ$ west
- (4) $45^\circ$ west

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Shortest path means the resultant velocity points due north, perpendicular to the banks.
2. The east component of the swimmer's velocity must cancel the river: $v_s \sin\theta = v_r$, with the strokes aimed west of north.
3. $\sin\theta = \frac{v_r}{v_s} = \frac{10}{20} = \frac{1}{2}$.
4. $\theta = 30^\circ$ west of north, which is option $1$.

**Subtopic:** River Problems · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q032_fdd4dc04_28102026.png?v=fdd4dc0487c0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** To cross along the shortest path the swimmer's upstream velocity component must cancel the current: $v\sin\theta = u$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Heading straight across, $0^\circ$, is the correct heading for the shortest TIME, so a student holding one river-crossing result reports it for the shortest PATH. Aiming straight across lets the current carry him downstream, so the path is longer than the river's width.
- **Why:** This question requires computing a heading from $v\sin\theta = u$, demonstrated by the stem's 'wishes to cross the river along the shortest path' with $20\,\mathrm{m/s}$ and $10\,\mathrm{m/s}$ printed.
<!--/ecat-->

## Q33

Physics · Laws of Motion

A particle moving with velocity $\vec{V}$ is acted by three forces shown by the vector triangle PQR. The velocity of the particle will :

![printed figure: Vector triangle PQR of three forces: R to P, P to Q, Q to R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q033_eb18fe57_28102026.svg?v=eb18fe571ebc)

*Vector triangle PQR of three forces: R to P, P to Q, Q to R*

![drawn: Vector triangle PQR of three forces: R to P, P to Q, Q to R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q033_question_b210d011_28102026.svg?v=b210d0113204)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) increase
- (2) decrease
- **(3)** remain constant
- (4) change according to the smallest force $\overrightarrow{\mathrm{QR}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. From the figure the arrows run $P \to Q$, $Q \to R$, $R \to P$, so the three forces are taken head to tail in order and close the triangle.
2. $\vec{F}_{net} = \overrightarrow{PQ} + \overrightarrow{QR} + \overrightarrow{RP} = \vec{0}$.
3. $\vec{a} = \frac{\vec{F}_{net}}{m} = \vec{0}$, so $\vec{V}$ remains constant, which is option $3$.

**Subtopic:** Equilibrium of Forces · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q033_b683ff3c_28102026.png?v=b683ff3ca888)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Three forces drawn head to tail round a closed triangle have zero resultant, so the velocity does not change
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  In the triangle law of addition two vectors are drawn head to tail and the closing side, drawn the OTHER way round, is the resultant; read that way, QR looks like a leftover force. All three arrows here run the same way round the loop — R to P, P to Q, Q to R — so the sum is zero and nothing is left over.
- **Why:** This question requires reading the sense of the three arrows in the printed triangle, demonstrated by the stem 'three forces shown by the vector triangle PQR' with the figure's arrows running R to P, P to Q and Q to R.
- **Note:** The supplied figure spec carries all three arrow senses and the labels P, R and Q, so the figure was readable at this step.
<!--/ecat-->

## Q34

Physics · Kinematics

Two particles A and B are moving in uniform circular motion in concentric circles of radii $r_A$ and $r_B$ with speed $v_A$ and $v_B$ respectively. Their time period of rotation is the same. The ratio of angular speed of A to that of B will be :

- (1) $r_A : r_B$
- (2) $v_A : v_B$
- (3) $r_B : r_A$
- **(4)** $1 : 1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Angular speed in uniform circular motion is $\omega = \frac{2\pi}{T}$.
2. $\frac{\omega_A}{\omega_B} = \frac{2\pi/T_A}{2\pi/T_B} = \frac{T_B}{T_A}$.
3. Since $T_A = T_B$, $\omega_A : \omega_B = 1 : 1$, which is option $4$.

**Subtopic:** Angular Velocity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q034_1734c683_28102026.png?v=1734c6839071)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Angular speed depends only on the period, $\omega = 2\pi/T$, so equal periods give equal angular speeds whatever the radii
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  With a common period $v = 2\pi r/T$, so $r_A : r_B$ is the true ratio of their LINEAR speeds — a quantity the stem prints but does not ask for. Angular speed contains no radius at all.
- **Why:** This question requires comparing two angular speeds through $\omega = 2\pi/T$, demonstrated by the stem's 'Their time period of rotation is the same' with every option printed as a ratio.
- **Note:** asks is relation rather than calculate: the answer is a factor between two angular speeds fixed by the shared period, and no number is computed from printed data.
<!--/ecat-->

## Q35

Physics · Laws of Motion

A block of mass $10\,\mathrm{kg}$ is in contact against the inner wall of a hollow cylindrical drum of radius $1\,\mathrm{m}$. The coefficient of friction between the block and the inner wall of the cylinder is $0.1$. The minimum angular velocity needed for the cylinder to keep the block stationary when the cylinder is vertical and rotating about its axis, will be : $(g = 10\,\mathrm{m/s^2})$

- (1) $\sqrt{10}\,\mathrm{rad/s}$
- (2) $\frac{10}{2\pi}\,\mathrm{rad/s}$
- **(3)** $10\,\mathrm{rad/s}$
- (4) $10\,\pi\,\mathrm{rad/s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The normal reaction of the wall provides the centripetal force: $N = m\omega^2 r$.
2. For the block to stay stationary, maximum friction must balance weight: $\mu N = mg$.
3. Substitute: $\mu m \omega^2 r = mg \Rightarrow \omega^2 = \frac{g}{\mu r}$.
4. $\omega^2 = \frac{10}{0.1 \times 1} = 100 \Rightarrow \omega_{min} = 10\,\mathrm{rad/s}$, which is option $3$.

**Subtopic:** Centripetal and Centrifugal Force, Static Friction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q035_83a2baf0_28102026.png?v=83a2baf0055c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Inside a rotating drum the wall supplies $N = m\omega^2 r$ and it is the friction $\mu N$ that must hold the weight, so $\omega_{\min} = \sqrt{g/\mu r}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Setting the wall's normal push equal to the weight, $m\omega^2 r = mg$, gives $\omega = \sqrt{g/r} = \sqrt{10}$. The normal force is horizontal and cannot hold the block up; only the friction it generates, $\mu N$, can.
- **Why:** This question requires computing a minimum angular velocity from $\mu m\omega^2 r = mg$, demonstrated by the stem's 'minimum angular velocity needed for the cylinder to keep the block stationary' with $\mu = 0.1$, $r = 1\,\mathrm{m}$ and $g = 10\,\mathrm{m/s^2}$ printed.
<!--/ecat-->

## Q36

Physics · Electrostatics

Two parallel infinite line charges with linear charge densities $+\lambda\,\mathrm{C/m}$ and $-\lambda\,\mathrm{C/m}$ are placed at a distance of $2R$ in free space. What is the electric field mid-way between the two line charges?

- (1) Zero
- (2) $\dfrac{2\lambda}{\pi\varepsilon_0 R}\,\mathrm{N/C}$
- **(3)** $\dfrac{\lambda}{\pi\varepsilon_0 R}\,\mathrm{N/C}$
- (4) $\dfrac{\lambda}{2\pi\varepsilon_0 R}\,\mathrm{N/C}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Field of an infinite line charge at distance $r$: $E = \frac{\lambda}{2\pi\varepsilon_0 r}$.
2. At the midpoint $r = R$ for each line, so each gives $E_1 = E_2 = \frac{\lambda}{2\pi\varepsilon_0 R}$.
3. The field of $+\lambda$ points away from it and the field of $-\lambda$ points towards it, so at the midpoint both point the same way (from $+\lambda$ to $-\lambda$).
4. $E_{net} = E_1 + E_2 = \frac{2\lambda}{2\pi\varepsilon_0 R} = \frac{\lambda}{\pi\varepsilon_0 R}\,\mathrm{N/C}$, which is option $3$.

**Subtopic:** Field Due to Infinitely Long Straight Uniformly Charged Wire · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q036_c9a44128_28102026.png?v=c9a44128e92c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each infinite line gives $E = \lambda/2\pi\varepsilon_0 r$; between oppositely charged lines the two fields point the same way and add
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  'Mid-way between two equal charges the field cancels' is a rule whose condition is that the charges be ALIKE. The stem prints $+\lambda$ and $-\lambda$, and for opposite charges both fields at the midpoint point from the positive line towards the negative one, so they add.
- **Why:** This question requires adding two line-charge fields at a point, demonstrated by the stem's '$+\lambda\,\mathrm{C/m}$ and $-\lambda\,\mathrm{C/m}$ are placed at a distance of $2R$'.
<!--/ecat-->

## Q37

Physics · Electrostatics

Two point charges A and B, having charges $+Q$ and $-Q$ respectively, are placed at certain distance apart and force acting between them is $F$. If $25\%$ charge of A is transferred to B, then force between the charges becomes :

- (1) $F$
- **(2)** $\frac{9F}{16}$
- (3) $\frac{16F}{9}$
- (4) $\frac{4F}{3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Initially $F = \frac{kQ^2}{r^2}$.
2. $25\%$ of A's charge is $\frac{Q}{4}$; after transfer $q_A = Q - \frac{Q}{4} = \frac{3Q}{4}$.
3. $q_B = -Q + \frac{Q}{4} = -\frac{3Q}{4}$.
4. $F' = \frac{k\left(\frac{3Q}{4}\right)\left(\frac{3Q}{4}\right)}{r^2} = \frac{9}{16}\frac{kQ^2}{r^2} = \frac{9F}{16}$, which is option $2$.

**Subtopic:** Coulomb's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q037_d13d77d7_28102026.png?v=d13d77d7484e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Coulomb force goes as the product of the two charges, so moving a quarter of A's charge to B leaves $0.75Q\times0.75Q$, i.e. $9/16$ of the original force
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The new product is $\tfrac34 Q \times \tfrac34 Q = \tfrac{9}{16}Q^2$, and $16/9$ is that ratio written upside down — the answer to 'F is how many times the new force' instead of 'the new force is how many times F'.
- **Why:** This question requires scaling the Coulomb force by the change in the product of the charges, demonstrated by the stem's 'If $25\%$ charge of A is transferred to B' with every option printed as a multiple of $F$.
<!--/ecat-->

## Q38

Physics · Mechanical Properties of Fluids

A small hole of area of cross-section $2\,\mathrm{mm^2}$ is present near the bottom of a fully filled open tank of height $2\,\mathrm{m}$. Taking $g = 10\,\mathrm{m/s^2}$, the rate of flow of water through the open hole would be nearly

- **(1)** $12.6 \times 10^{-6}\,\mathrm{m^3/s}$
- (2) $8.9 \times 10^{-6}\,\mathrm{m^3/s}$
- (3) $2.23 \times 10^{-6}\,\mathrm{m^3/s}$
- (4) $6.4 \times 10^{-6}\,\mathrm{m^3/s}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Efflux speed from Torricelli's law: $v = \sqrt{2gh}$.
2. $v = \sqrt{2 \times 10 \times 2} = \sqrt{40} \approx 6.32\,\mathrm{m/s}$.
3. Area $A = 2\,\mathrm{mm^2} = 2 \times 10^{-6}\,\mathrm{m^2}$.
4. $Q = Av = 2 \times 10^{-6} \times 6.32 \approx 12.6 \times 10^{-6}\,\mathrm{m^3/s}$, which is option $1$.

**Subtopic:** Torricelli's Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q038_de4ba545_28102026.png?v=de4ba5452f79)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Torricelli's efflux speed is $\sqrt{2gh}$, and the volume rate through the hole is $A\sqrt{2gh}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Dropping the 2 inside the root gives $\sqrt{gh} = \sqrt{20} = 4.47\,\mathrm{m/s}$, and $2\times10^{-6}\times4.47$ is exactly the printed $8.9\times10^{-6}\,\mathrm{m^3/s}$; the efflux speed is the free-fall speed from the depth, $\sqrt{2gh}$.
- **Why:** This question requires computing a volume flow rate as $A\sqrt{2gh}$, demonstrated by the stem's 'the rate of flow of water through the open hole' with the area $2\,\mathrm{mm^2}$ and the height $2\,\mathrm{m}$ printed.
<!--/ecat-->

## Q39

Physics · Semiconductor Electronics

The correct Boolean operation represented by the circuit diagram drawn is :

![printed figure: Switches A and B to ground in parallel with an LED (Y) and resistor R, fed from +6 V through R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q039_bc8a59ed_28102026.svg?v=bc8a59ed6bc4)

*Switches A and B to ground in parallel with an LED (Y) and resistor R, fed from +6 V through R*

![drawn: Switches A and B to ground in parallel with an LED (Y) and resistor R, fed from +6 V through R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q039_question_6c9df53b_28102026.svg?v=6c9df53bea84)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) AND
- (2) OR
- **(3)** NAND
- (4) NOR

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Switches $A$ and $B$ are in series, joining the node between the top $R$ and the LED to ground.
2. If either switch is open ($A=0$ or $B=0$), no path to ground exists, so current flows through the LED: $Y=1$.
3. If both are closed ($A=B=1$), the node is shorted to ground and the LED goes off: $Y=0$.
4. Truth table $Y = 1,1,1,0$ gives $Y = \overline{A \cdot B}$, which is NAND, option $3$.

**Subtopic:** Logic Gates · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 6)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q039_8525ab62_28102026.png?v=8525ab62afde)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** The two switches sit in series as a shunt across the LED branch, so the output is high unless both are closed — a NAND
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The two switches do form one series path, and 'series means AND' names that path AND. In this circuit the series path is a short across the LED, so closing both switches is what turns the output OFF, and the function is the complement, $\overline{A\cdot B}$.
- **Why:** This question requires reading the circuit's topology, demonstrated by the stem 'The correct Boolean operation represented by the circuit diagram drawn' with the switch branch wired from the LED's node to ground.
- **Note:** The figure arrived as a netlist (R1 vcc–n1, SA n1–nL, SB nL–gnd, LED n1–n2, R2 n2–gnd), so the series pairing of the switches and the shunt across the LED were both readable at this step.
<!--/ecat-->

## Q40

Physics · Thermodynamics

In which of the following processes, heat is neither absorbed nor released by a system?

- (1) Isothermal
- **(2)** Adiabatic
- (3) Isobaric
- (4) Isochoric

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. By definition an adiabatic process allows no heat transfer between the system and its surroundings, so $q = 0$ (and $\Delta U = w$), which is option $2$.

**Subtopic:** Adiabatic Process · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q040_f511905e_28102026.png?v=f511905e35c0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An adiabatic process is the one defined by zero heat exchange; an isothermal process holds temperature fixed and exchanges heat freely
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Nothing changes thermally' collapses two neighbouring definitions into one, and the isothermal process is the one printed beside the adiabatic in the same section; but holding $T$ fixed requires heat to flow in exactly as fast as work is done, so $Q\neq0$ there.
- **Why:** This question requires the definition that fixes $Q=0$, demonstrated by the stem 'heat is neither absorbed nor released by a system?' set against four named processes.
- **Note:** Swap test applied: replacing 'isothermal' and 'adiabatic' with two unlike words leaves the pull standing, because what is conflated is 'temperature unchanged' with 'no heat exchanged' — two adjacent definitions, not two similar words. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q41

Physics · Electromagnetic Induction

A 800 turn coil of effective area $0.05\,\mathrm{m^2}$ is kept perpendicular to a magnetic field $5 \times 10^{-5}\,\mathrm{T}$. When the plane of the coil is rotated by $90^\circ$ around any of its coplanar axis in $0.1\,\mathrm{s}$, the emf induced in the coil will be:

- (1) $2\,\mathrm{V}$
- (2) $0.2\,\mathrm{V}$
- (3) $2 \times 10^{-3}\,\mathrm{V}$
- **(4)** $0.02\,\mathrm{V}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Initially the field is perpendicular to the plane of the coil, so $\Phi_i = NBA\cos 0^\circ = NBA$.
2. $\Phi_i = 800 \times 5 \times 10^{-5}\,\mathrm{T} \times 0.05\,\mathrm{m^2} = 2 \times 10^{-3}\,\mathrm{Wb}$.
3. After rotating the plane by $90^\circ$ about a coplanar axis, the field lies in the plane, so $\Phi_f = NBA\cos 90^\circ = 0$.
4. $|e| = \frac{\Delta \Phi}{\Delta t} = \frac{2 \times 10^{-3}\,\mathrm{Wb}}{0.1\,\mathrm{s}} = 0.02\,\mathrm{V}$, which is option $4$.

**Subtopic:** Faraday's Law of Electromagnetic Induction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q041_2fb60d1b_28102026.png?v=2fb60d1b2002)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The induced emf is the rate of change of flux linkage, $N\Delta(BA\cos\theta)/\Delta t$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $NBA = 800\times5\times10^{-5}\times0.05 = 2\times10^{-3}$, which is the flux linkage that disappears, not the emf; stopping before the division by $0.1\,\mathrm{s}$ leaves exactly the printed $2\times10^{-3}$.
- **Why:** This question requires computing an emf from the change in flux linkage over the stated time, demonstrated by the stem's 'rotated by $90^\circ$ around any of its coplanar axis in $0.1\,\mathrm{s}$' with $N$, $A$ and $B$ all printed.
<!--/ecat-->

## Q42

Physics · Oscillations

The radius of circle, the period of revolution, initial position and sense of revolution are indicated in the fig. y-projection of the radius vector of rotating particle P is:

![printed figure: Particle P on a circle of radius 3 m, starting at the top (t = 0) and moving clockwise with period T = 4 s](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q042_4b54ea75_28102026.svg?v=4b54ea758659)

*Particle P on a circle of radius 3 m, starting at the top (t = 0) and moving clockwise with period T = 4 s*

![drawn: Particle P on a circle of radius 3 m, starting at the top (t = 0) and moving clockwise with period T = 4 s](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q042_question_57624e2e_28102026.svg?v=57624e2e40d2)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $y(t) = -3\cos 2\pi t$, where y in m
- (2) $y(t) = 4\sin\left(\frac{\pi t}{2}\right)$, where y in m
- (3) $y(t) = 3\cos\left(\frac{3\pi t}{2}\right)$, where y in m
- **(4)** $y(t) = 3\cos\left(\frac{\pi t}{2}\right)$, where y in m

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. From the figure, the radius is $A = 3\,\text{m}$ and $T = 4\,\text{s}$.
2. $\omega = \frac{2\pi}{T} = \frac{2\pi}{4} = \frac{\pi}{2}\,\text{rad s}^{-1}$.
3. At $t = 0$, P is at the top of the circle on the $+y$ axis, so $y(0) = +3\,\text{m}$ (maximum).
4. For clockwise motion from the top, the angle from the $+y$ axis is $\omega t$, so $y(t) = A\cos\omega t$.
5. $y(t) = 3\cos\left(\frac{\pi t}{2}\right)\,\text{m}$, which is option $4$.

**Subtopic:** SHM as Projection of Circular Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q042_1237f536_28102026.png?v=1237f536c263)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** The projection of uniform circular motion is SHM whose amplitude is the radius and whose $\omega$ is $2\pi/T$; where the particle starts decides sine against cosine
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Writing the projection in the habitual form $y = A\sin\omega t$ presumes the particle starts on the x-axis, while the figure starts P at the end of the y-radius, where the projection is a cosine; the option's amplitude 4 is the figure's period, not its radius.
- **Why:** This question requires reading the amplitude, period and starting point off the figure, demonstrated by the stem 'The radius of circle, the period of revolution, initial position and sense of revolution are indicated in the fig.'
- **Note:** The figure spec supplies the radius labelled '3 m', 'T = 4 s', the drawn axes, the sense arrow and the 'P(t = 0)' label, so the figure was readable. Its caption says P starts 'at the top' while the drawn y-axis runs towards the foot of the page; the key's $y(0) = +3\,\mathrm{m}$ agrees with the drawing rather than with the caption, and the question is tagged as printed.
<!--/ecat-->

## Q43

Physics · Electromagnetic Waves

A parallel plate capacitor of capacitance $20\,\mu\mathrm{F}$ is being charged by a voltage source whose potential is changing at the rate of $3\,\mathrm{V/s}$. The conduction current through the connecting wires, and the displacement current through the plates of the capacitor, would be, respectively.

- (1) Zero, $60\,\mu\mathrm{A}$
- **(2)** $60\,\mu\mathrm{A}$, $60\,\mu\mathrm{A}$
- (3) $60\,\mu\mathrm{A}$, zero
- (4) Zero, zero

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Charge on the capacitor is $q = CV$, so the conduction current in the wires is $I_c = \frac{dq}{dt} = C\frac{dV}{dt}$.
2. $I_c = 20\times10^{-6}\,\mathrm{F} \times 3\,\mathrm{V/s} = 60\times10^{-6}\,\mathrm{A} = 60\,\mu\mathrm{A}$.
3. Displacement current between the plates is $I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \varepsilon_0 \frac{d}{dt}\left(\frac{q}{\varepsilon_0}\right) = \frac{dq}{dt} = I_c$.
4. So $I_d = 60\,\mu\mathrm{A}$; both currents are $60\,\mu\mathrm{A}$, which is option $2$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q043_80535a8c_28102026.png?v=80535a8c5179)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** While a capacitor charges, the displacement current between the plates equals the conduction current in the wires, both $C\,dV/dt$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'A capacitor blocks current' sends the first entry to zero while the plates keep the computed $C\,dV/dt = 20\,\mu\mathrm{F}\times3\,\mathrm{V/s} = 60\,\mu\mathrm{A}$; the wires are exactly where the charging current flows, so the first entry is $60\,\mu\mathrm{A}$ too.
- **Why:** This question requires both currents computed from $C\,dV/dt$, demonstrated by the stem asking for 'the conduction current through the connecting wires, and the displacement current through the plates of the capacitor ... respectively'.
- **Note:** E1 called this multi_part_respectively; on the current axis a two-answer shape is two_part, and the pairs printed in the options are what makes half_right available here.
<!--/ecat-->

## Q44

Physics · Units and Measurements

In an experiment, the percentage of error occurred in the measurement of physical quantities A, B, C and D are $1\%$, $2\%$, $3\%$ and $4\%$ respectively. Then the maximum percentage of error in the measurement X, where $X = \dfrac{A^{2}B^{1/2}}{C^{1/3}D^{3}}$, will be

- (1) $\left(\dfrac{3}{13}\right)\%$
- **(2)** $16\%$
- (3) $-10\%$
- (4) $10\%$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For $X = \dfrac{A^{2}B^{1/2}}{C^{1/3}D^{3}}$, the maximum fractional error is $\dfrac{\Delta X}{X} = 2\dfrac{\Delta A}{A} + \dfrac{1}{2}\dfrac{\Delta B}{B} + \dfrac{1}{3}\dfrac{\Delta C}{C} + 3\dfrac{\Delta D}{D}$ (errors always add).
2. Substitute: $2(1\%) + \frac{1}{2}(2\%) + \frac{1}{3}(3\%) + 3(4\%)$.
3. $= 2\% + 1\% + 1\% + 12\% = 16\%$, which is option $2$.

**Subtopic:** Errors in Measurement · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q044_624d16c0_28102026.png?v=624d16c0d6aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A maximum percentage error adds every contribution, each weighted by the size of its exponent, whether the quantity sits above or below the line
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Carrying the signs of division into the error formula gives $2 + 1 - 1 - 12 = -10$, and reporting its size gives $10\%$; in a maximum-error estimate the contributions of $C$ and $D$ are added, because the worst case is the one where the errors reinforce.
- **Why:** This question requires combining weighted percentage errors, demonstrated by the stem's $X = \dfrac{A^{2}B^{1/2}}{C^{1/3}D^{3}}$ with the four errors printed as $1\%$, $2\%$, $3\%$ and $4\%$.
<!--/ecat-->

## Q45

Physics · Magnetic Effect of Electric Current

A cylindrical conductor of radius $R$ is carrying a constant current. The plot of the magnitude of the magnetic field. $B$ with the distance $d$ from the centre of the conductor, is correctly represented by the figure :

- (1) ![printed figure: B vs d: constant B up to R, then falling curve beyond R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q045_option_1_b817e468_28102026.svg?v=b817e46836f7) *B vs d: constant B up to R, then falling curve beyond R* ![drawn: B vs d: constant B up to R, then falling curve beyond R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q045_option_1_e41f0154_28102026.svg?v=e41f01544330)  
*drawn on the booklet's geometry, checked against its figure spec* — [graph: $B$ vs $d$, marked $R$]
- (2) ![printed figure: B vs d: zero inside R, jumps to a maximum at d = R, then falls off outside](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q045_option_2_481d2b4d_28102026.svg?v=481d2b4d5ad5) *B vs d: zero inside R, jumps to a maximum at d = R, then falls off outside* ![drawn: B vs d: zero inside R, jumps to a maximum at d = R, then falls off outside](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q045_option_2_782c802a_28102026.svg?v=782c802a2685)  
*drawn on the booklet's geometry, checked against its figure spec* — [graph: $B$ vs $d$, marked $R$]
- **(3)** ![printed figure: B vs d: linear rise from origin to a peak at d = R, then a decreasing curve beyond R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q045_option_3_65eb671f_28102026.svg?v=65eb671f9491) *B vs d: linear rise from origin to a peak at d = R, then a decreasing curve beyond R* ![drawn: B vs d: linear rise from origin to a peak at d = R, then a decreasing curve beyond R](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q045_option_3_9741ef0d_28102026.svg?v=9741ef0d12f1)  
*drawn on the booklet's geometry, checked against its figure spec* — [graph: $B$ vs $d$, marked $R$]
- (4) ![printed figure: B against d: rises linearly from the origin up to R, then stays constant](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q045_option_4_f6beaf62_28102026.svg?v=f6beaf620a53) *B against d: rises linearly from the origin up to R, then stays constant* ![drawn: B against d: rises linearly from the origin up to R, then stays constant](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q045_option_4_5c82db04_28102026.svg?v=5c82db04877b)  
*drawn on the booklet's geometry, checked against its figure spec* — [graph: $B$ vs $d$, marked $R$]

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Take a circular Amperian loop of radius $d$ coaxial with the conductor, assuming uniform current density.
2. Inside ($d < R$): $I_{enc} = I\frac{d^2}{R^2}$, so $B(2\pi d) = \mu_0 I \frac{d^2}{R^2}$.
3. Hence $B = \frac{\mu_0 I d}{2\pi R^2} \propto d$, a straight line from the origin.
4. Outside ($d > R$): $I_{enc} = I$, so $B = \frac{\mu_0 I}{2\pi d} \propto \frac{1}{d}$.
5. Both give $B = \frac{\mu_0 I}{2\pi R}$ at $d = R$, so the graph peaks continuously at $R$ and decays as $1/d$, which is option $3$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q045_319c8d4a_28102026.png?v=319c8d4a4670)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Ampere's law gives $B\propto d$ inside a uniformly conducting cylinder and $B\propto1/d$ outside, so the field peaks at the surface $d=R$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are the plots themselves and each reached this step as the placeholder text '[graph: $B$ vs $d$, marked $R$]', so no curve was available to compare
- **Why:** This question requires Ampere's law applied inside and outside the conductor, demonstrated by the stem's 'plot of the magnitude of the magnetic field. $B$ with the distance $d$ from the centre of the conductor'.
- **Note:** Every option is stored as the placeholder '[graph: B vs d, marked R]' and has_figure is false, so the four curves were not supplied to this step. The printed paper is intact, so this is not source damage. A reviewer holding the graphs should check the device this item usually carries: the key rises linearly to $d=R$ and then falls as $1/d$, and the distractors worth testing are a field held constant inside the conductor, a $1/d$ curve drawn through the whole range as though the conductor were a thin wire, and a curve that keeps rising beyond $R$.
<!--/ecat-->

## Q46

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The number of sigma $(\sigma)$ and pi $(\pi)$ bonds in pent-2-en-4-yne is

- **(1)** $10\sigma$ bonds and $3\pi$ bonds
- (2) $8\sigma$ bonds and $5\pi$ bonds
- (3) $11\sigma$ bonds and $2\pi$ bonds
- (4) $13\sigma$ bonds and no $\pi$ bonds

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Write the structure: $\mathrm{CH_3{-}CH{=}CH{-}C{\equiv}CH}$, formula $\mathrm{C_5H_6}$.
2. Each of the $4$ carbon-carbon links contributes one $\sigma$ bond: $4\sigma$.
3. There are $3 + 1 + 1 + 0 + 1 = 6$ C-H bonds, each a $\sigma$ bond: $6\sigma$.
4. Total $\sigma = 4 + 6 = 10$.
5. The $\mathrm{C{=}C}$ has $1\pi$ and the $\mathrm{C{\equiv}C}$ has $2\pi$: total $3\pi$.
6. $10\sigma$ and $3\pi$ bonds, which is option $1$.

**Subtopic:** Orbital Overlap Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q046_f380164f_28102026.png?v=f380164fb40f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Every linkage between two atoms holds exactly one $\sigma$ bond; the second and third bonds of a double or triple bond are the $\pi$ bonds
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The triple bond is split as $2\sigma + 1\pi$ instead of $1\sigma + 2\pi$, which moves one bond from the $\pi$ column into the $\sigma$ column and turns 10 and 3 into 11 and 2.
- **Why:** This question requires the $\sigma$ and $\pi$ counts worked out over a structure built from its name, demonstrated by the options separating '$10\sigma$ bonds and $3\pi$ bonds' from three other splits of the same 13 bonds.
- **Note:** E1 called this statement_options; nothing in it is judged as a statement, and each option supplies two counts that must both hold, so the shape is recorded as two_part.
<!--/ecat-->

## Q47

Chemistry · organic · Alcohols, Phenols and Ethers

The structure of intermediate A in the following reaction, is

![printed figure: (propan-2-yl)benzene →($\ce{O2}$) A →($\ce{H+}$ / $\ce{H2O}$) phenol + propan-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q047_f58d1bf2_28102026.svg?v=f58d1bf2a8c2)

*(propan-2-yl)benzene →[$\ce{O2}$] A →[$\ce{H+}$ / $\ce{H2O}$] phenol + propan-2-one*

![drawn: (propan-2-yl)benzene →($\ce{O2}$) A →($\ce{H+}$ / $\ce{H2O}$) phenol + propan-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_question_5d536d62_28102026.svg?v=5d536d62429e)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: (propan-2-yl)benzene `CC(C)c1ccccc1` ![(propan-2-yl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_question_s1_e63202da_28102026.svg?v=e63202dabcb8); phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_question_s2_5e648107_28102026.svg?v=5e6481073b43); propan-2-one `CC(C)=O` ![propan-2-one](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_question_s3_bc6081c8_28102026.svg?v=bc6081c85b4b)

- (1) phenoxyl `[O]c1ccccc1` ![phenoxyl](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_option_1_s1_db140182_28102026.svg?v=db140182f97a); propan-2-yl `C[CH]C` ![propan-2-yl](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_option_1_s2_4d915c62_28102026.svg?v=4d915c62afd0)
- **(2)** (2-hydroperoxypropan-2-yl)benzene `CC(C)(OO)c1ccccc1` ![(2-hydroperoxypropan-2-yl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_option_2_s1_1e3fe791_28102026.svg?v=1e3fe7913544)
- (3) (propan-2-ylperoxy)benzene `CC(C)OOc1ccccc1` ![(propan-2-ylperoxy)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_option_3_s1_16d53d54_28102026.svg?v=16d53d542672)
- (4) (1-hydroperoxypropan-2-yl)benzene `CC(COO)c1ccccc1` ![(1-hydroperoxypropan-2-yl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q047_option_4_s1_f92536a8_28102026.svg?v=f92536a8e98c)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The starting compound is cumene, $\mathrm{C_6H_5CH(CH_3)_2}$, with one tertiary benzylic $\mathrm{C-H}$.
2. Air oxidation ($\mathrm{O_2}$) inserts $\mathrm{O_2}$ into that benzylic $\mathrm{C-H}$: $\mathrm{C_6H_5CH(CH_3)_2 + O_2 \rightarrow C_6H_5C(CH_3)_2-O-O-H}$ (cumene hydroperoxide, A).
3. Acid hydrolysis: $\mathrm{C_6H_5C(CH_3)_2OOH \xrightarrow{H^+,\,H_2O} C_6H_5OH + CH_3COCH_3}$, matching the products shown.
4. Cumene hydroperoxide is drawn in option $2$.

**Subtopic:** Preparation of Phenols · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q047_c4f28ad7_28102026.png?v=c4f28ad737b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Cumene oxidised by $\ce{O2}$ gives cumene hydroperoxide, and acid hydrolysis of that intermediate splits it into phenol and acetone
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and were not supplied to this step: options_en holds four empty strings, so there is nothing to test a route against
- **Why:** This question requires the intermediate of a printed two-step scheme, demonstrated by '(propan-2-yl)benzene →[O2] A →[H+ / H2O] phenol + propan-2-one' with A left as a letter.
- **Note:** The stem and the scheme are intact - the supplied figure text gives the whole conversion - so this is our reach and not damage to the paper, and no trap is written. A reviewer holding the four option structures should check whether a distractor replaces the O-O of the hydroperoxide with a single oxygen, that is 2-phenylpropan-2-ol, since the peroxide linkage is what the acid cleavage to phenol and acetone depends on.
<!--/ecat-->

## Q48

Chemistry · inorganic · The p–Block Elements

The correct structure of tribromooctaoxide is

- **(1)** tribromine octaoxide `[O-][Br+2]([O-])([Br+3]([O-])([O-])[O-])[Br+3]([O-])([O-])[O-]`
- (2) tribromine octaoxide trianion (Br3O8 3-) `[O-][Br+]([O-])([O-])[Br+]([O-])([O-])[Br+3]([O-])([O-])[O-]`
- (3) tribromine octaoxide tetraanion (Br3O8 4-) `[O-][Br+]([O-])([O-])[Br+2]([O-])([O-])[Br+]([O-])([O-])[O-]`
- (4) tribromine octaoxide trianion (Br3O8 3-) `[O-][Br+3]([O-])([O-])[Br]([O-])([O-])[Br+2]([O-])([O-])[O-]`

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Tribromooctaoxide is $\mathrm{Br_3O_8}$, a neutral molecule, so the correct structure must carry no net charge.
2. Options 2, 3 and 4 each contain $\mathrm{O^-}$ groups (net charge $-2$ or $-3$), so they cannot represent neutral $\mathrm{Br_3O_8}$.
3. In option 1 each terminal Br has three $\mathrm{Br=O}$ bonds (oxidation state $+6$) and the central Br has two $\mathrm{Br=O}$ bonds (oxidation state $+4$); average $= \frac{6+4+6}{3} = \frac{16}{3}$, consistent with $\mathrm{Br_3O_8}$, so the answer is option $1$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q048_11d95de9_28102026.png?v=11d95de9c83b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tribromooctaoxide is the bromine oxide $\ce{Br3O8}$, whose structure is carried from the printed drawing rather than derived
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and were not supplied to this step: options_en holds four empty strings, so no option content exists to carry a route
- **Why:** This question requires the structure stored for one named oxide, demonstrated by 'The correct structure of tribromooctaoxide is' with drawn structures as the four options.
- **Note:** options_en holds four empty strings - the options are drawn structures that were not carried into this step - while the stem is intact, so this is a reach limit of the packet and not source damage. A reviewer holding the structures should check whether the distractors differ only in how the eight oxygens are shared between the three bromine atoms, since that bridging pattern is the one decision the question contains.
<!--/ecat-->

## Q49

Chemistry · physical · Structure of Atom

4d, 5p, 5f and 6p orbitals are arranged in the order of decreasing energy. The correct option is

- **(1)** $\mathrm{5f} > \mathrm{6p} > \mathrm{5p} > \mathrm{4d}$
- (2) $\mathrm{6p} > \mathrm{5f} > \mathrm{5p} > \mathrm{4d}$
- (3) $\mathrm{6p} > \mathrm{5f} > \mathrm{4d} > \mathrm{5p}$
- (4) $\mathrm{5f} > \mathrm{6p} > \mathrm{4d} > \mathrm{5p}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Apply the $(n+l)$ rule: higher $(n+l)$ means higher energy; for equal $(n+l)$, higher $n$ means higher energy.
2. $4d$: $n+l = 4+2 = 6$.
3. $5p$: $n+l = 5+1 = 6$.
4. $5f$: $n+l = 5+3 = 8$.
5. $6p$: $n+l = 6+1 = 7$.
6. $4d$ and $5p$ tie at $6$; $5p$ has larger $n$, so $E_{5p} > E_{4d}$.
7. Decreasing energy: $5f > 6p > 5p > 4d$, which is option $1$.

**Subtopic:** Atomic Orbitals: Shapes, Energies and Nodes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q049_d035db89_28102026.png?v=d035db891dec)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Orbital energy rises with $(n+l)$, and when two orbitals share the same $(n+l)$ the one with the smaller $n$ lies lower
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The four orbitals are ranked by the principal quantum number alone, which puts 6p at the top; $(n+l)$ is 7 for 6p against 8 for 5f, so 5f is the highest.
- **Why:** This question requires orbital energies ordered by the $(n+l)$ rule, demonstrated by '4d, 5p, 5f and 6p orbitals are arranged in the order of decreasing energy' putting the tied pair 4d and 5p in the same list as 5f and 6p.
<!--/ecat-->

## Q50

Chemistry · physical · Redox Reactions

Which of the following reactions are disproportionation reaction?
Select the correct option from the following

- **(a)** $\mathrm{2Cu^{+} \longrightarrow Cu^{2+} + Cu^{0}}$
- **(b)** $\mathrm{3MnO_4^{2-} + 4H^{+} \longrightarrow 2MnO_4^{-} + MnO_2 + 2H_2O}$
- **(c)** $\mathrm{2KMnO_4 \xrightarrow{\Delta} K_2MnO_4 + MnO_2 + O_2}$
- **(d)** $\mathrm{2MnO_4^{-} + 3Mn^{2+} + 2H_2O \longrightarrow 5MnO_2 + 4H^{\oplus}}$

- **(1)** (a) and (b) only
- (2) (a), (b) and (c)
- (3) (a), (c) and (d)
- (4) (a) and (d) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Disproportionation: one element in one oxidation state is oxidised and reduced at the same time.
2. (a) $\mathrm{Cu^{+}}$ ($+1$) $\to$ $\mathrm{Cu^{2+}}$ ($+2$) and $\mathrm{Cu^{0}}$ ($0$): disproportionation.
3. (b) Mn in $\mathrm{MnO_4^{2-}}$ is $+6$; it goes to $+7$ in $\mathrm{MnO_4^{-}}$ and $+4$ in $\mathrm{MnO_2}$: disproportionation.
4. (c) Mn in $\mathrm{KMnO_4}$ is $+7$; it goes to $+6$ ($\mathrm{K_2MnO_4}$) and $+4$ ($\mathrm{MnO_2}$), so Mn is only reduced; O goes from $-2$ to $0$. Different elements are oxidised and reduced, so this is not disproportionation.
5. (d) Mn at $+7$ and $+2$ both become $+4$ in $\mathrm{MnO_2}$: comproportionation, not disproportionation.
6. Only (a) and (b) qualify, which is option $1$.

**Subtopic:** Types of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q050_f085b7ba_28102026.png?v=f085b7babc69)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Disproportionation needs one element in one oxidation state to be both oxidised and reduced in the same reaction
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  In (c) the manganese ends up as $\mathrm{Mn^{+6}}$ in $\mathrm{K_2MnO_4}$ and $\mathrm{Mn^{+4}}$ in $\mathrm{MnO_2}$, so a student who tests only 'does one element come out in two oxidation states' adds (c) to the correct (a) and (b); but both manganese states are below $+7$, so manganese is only reduced and the element oxidised is oxygen, $-2 \to 0$ in $\mathrm{O_2}$
- **Why:** This question requires the disproportionation criterion applied to each printed equation, demonstrated by '$\mathrm{2KMnO_4 \longrightarrow K_2MnO_4 + MnO_2 + O_2}$', where the manganese only falls and the element oxidised is oxygen.
<!--/ecat-->

## Q51

Chemistry · physical · Thermodynamics

Under isothermal condition, a gas at $300\,\mathrm{K}$ expands from $0.1\,\mathrm{L}$ to $0.25\,\mathrm{L}$ against a constant external pressure of $2\,\mathrm{bar}$. The work done by the gas is
(Given that $1\,\mathrm{L\,bar} = 100\,\mathrm{J}$)

- **(1)** $-30\,\mathrm{J}$
- (2) $5\,\mathrm{kJ}$
- (3) $25\,\mathrm{J}$
- (4) $30\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Change in volume: $\Delta V = 0.25\,\mathrm{L} - 0.1\,\mathrm{L} = 0.15\,\mathrm{L}$.
2. Work against constant external pressure (NCERT convention): $w = -p_{ex}\,\Delta V$.
3. $w = -(2\,\mathrm{bar})(0.15\,\mathrm{L}) = -0.3\,\mathrm{L\,bar}$.
4. $-0.3\,\mathrm{L\,bar} \times 100\,\mathrm{J/(L\,bar)} = -30\,\mathrm{J}$, which is option $1$.

**Subtopic:** Pressure–Volume Work for Isothermal Irreversible Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q051_6cfa475b_28102026.png?v=6cfa475bc943)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For expansion against a constant external pressure $w = -p_{ext}\Delta V$, and the minus sign is what the convention attaches to work leaving the system
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  $2\,\mathrm{bar} \times 0.15\,\mathrm{L} = 0.3\,\mathrm{L\,bar} = 30\,\mathrm{J}$ is the right magnitude, and the stem's words 'work done by the gas' carry the sign to positive, where $w = -p_{ext}\Delta V$ puts it negative.
- **Why:** This question requires the pressure-volume work computed from the stem's numbers, demonstrated by 'expands from 0.1 L to 0.25 L against a constant external pressure of 2 bar' with '1 L bar = 100 J' supplied.
- **Note:** Recorded arguable_key: the stem asks for 'The work done by the gas' and the key prints $-30\,\mathrm{J}$, which is $w$ for the gas under the $w = -p_{ext}\Delta V$ convention, while a strict reading of 'done by the gas' would report the same magnitude positive. Tagged as printed; the key is not re-judged, and the doubt rests on the sign convention rather than on the arithmetic.
<!--/ecat-->

## Q52

Chemistry · inorganic · Environmental Chemistry

Among the following, the one that is not a green house gas is

- (1) Nitrous oxide
- (2) Methane
- (3) Ozone
- **(4)** Sulphur dioxide

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT names the greenhouse gases as $CO_2$, $CH_4$, $N_2O$, CFCs and ozone ($O_3$); nitrous oxide, methane and ozone are all on this list, while sulphur dioxide ($SO_2$) is an air pollutant and not a greenhouse gas, so the answer is option $4$.

**Subtopic:** Air Pollution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q052_3e73c4a3_28102026.png?v=3e73c4a30ee1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The greenhouse gases listed in the chapter are carbon dioxide, methane, nitrous oxide, CFCs, water vapour and ozone, while sulphur dioxide belongs to the acid-rain account
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Ozone is printed in the same chapter as the stratospheric depletion problem, so a student who files ozone under the ozone hole rather than under warming reads it as the gas that is not a greenhouse gas.
- **Why:** This question requires membership of the chapter's greenhouse-gas list, demonstrated by 'the one that is not a green house gas' against four gases of which only 'Sulphur dioxide' is absent from it.
- **Note:** nearby_fact rather than look_alike_term: swapping 'Ozone' and 'Sulphur dioxide' for two unlike words leaves the pull intact, because what carries it is ozone's position in the chapter's other section rather than any likeness of the two names.
<!--/ecat-->

## Q53

Chemistry · physical · Electrochemistry

For the cell reaction $\mathrm{2Fe^{3+}(aq) + 2I^{-}(aq) \rightarrow 2Fe^{2+}(aq) + I_2(aq)}$ $E^{\circ}_{\mathrm{Cell}} = 0.24\,\mathrm{V}$ at $298\,\mathrm{K}$. The standard Gibbs energy $(\Delta_r G^{\circ})$ of the cell reaction is :

- **(1)** $-46.32\,\mathrm{kJ\,mol^{-1}}$
- (2) $-23.16\,\mathrm{kJ\,mol^{-1}}$
- (3) $46.32\,\mathrm{kJ\,mol^{-1}}$
- (4) $23.16\,\mathrm{kJ\,mol^{-1}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Each $\mathrm{Fe^{3+}}$ gains one electron and two are reduced, while $2\mathrm{I^-} \rightarrow \mathrm{I_2}$ loses two electrons, so $n = 2$.
2. $\Delta_r G^{\circ} = -nFE^{\circ}_{\mathrm{cell}}$.
3. $\Delta_r G^{\circ} = -(2)(96500\,\mathrm{C\,mol^{-1}})(0.24\,\mathrm{V}) = -46320\,\mathrm{J\,mol^{-1}}$.
4. $-46320\,\mathrm{J\,mol^{-1}} = -46.32\,\mathrm{kJ\,mol^{-1}}$, which is option $1$.

**Subtopic:** Cell Potential · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q053_17be1f6d_28102026.png?v=17be1f6d05bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** $\Delta_r G^{\circ} = -nFE^{\circ}_{cell}$, with $n$ read off the balanced cell reaction
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The half reaction $\mathrm{Fe^{3+} + e^- \rightarrow Fe^{2+}}$ is taken as the whole change, so $n$ is put at 1 instead of 2 and $-1 \times 96500 \times 0.24 = -23.16\,\mathrm{kJ\,mol^{-1}}$ comes out, exactly half the right value.
- **Why:** This question requires the standard Gibbs energy computed from the cell potential, demonstrated by the stem printing '$\mathrm{2Fe^{3+}(aq) + 2I^{-}(aq) \rightarrow 2Fe^{2+}(aq) + I_2(aq)}$' with '$E^{\circ}_{\mathrm{Cell}} = 0.24\,\mathrm{V}$'.
- **Note:** The four options are a two-by-two grid of one magnitude against its half, each with both signs; the one trap is placed on the halved magnitude because the stem's printed coefficients are what settle $n$, and the sign and combined cases are carried in other_options.
<!--/ecat-->

## Q54

Chemistry · inorganic · The s-Block Elements

Enzymes that utilize ATP in phosphate transfer require an alkaline earth metal ($\mathrm{M}$) as the cofactor. $\mathrm{M}$ is :

- (1) $\mathrm{Be}$
- **(2)** $\mathrm{Mg}$
- (3) $\mathrm{Ca}$
- (4) $\mathrm{Sr}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Enzymes that transfer phosphate from ATP (e.g. kinases) act on the $\mathrm{Mg^{2+}}$-ATP complex, so the required alkaline earth cofactor $\mathrm{M}$ is $\mathrm{Mg}$, option $2$.

**Subtopic:** Biological Importance of Sodium, Potassium, Magnesium and Calcium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q054_ced62667_28102026.png?v=ced626671936)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Enzymes that transfer phosphate from ATP need magnesium as the cofactor, while calcium's biological roles are bone, clotting and muscle contraction
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Calcium's biological importance is printed in the same short section as magnesium's, so a student who remembers that section as 'the biologically important alkaline earth metal' reaches for calcium.
- **Why:** This question requires one stated biological role of a named metal, demonstrated by 'Enzymes that utilize ATP in phosphate transfer require an alkaline earth metal (M) as the cofactor'.
- **Note:** nearby_fact rather than look_alike_term: swapping 'Mg' and 'Ca' for two unlike symbols leaves the pull intact, because what carries it is calcium's roles being printed in the same section, not any likeness between the two names.
<!--/ecat-->

## Q55

Chemistry · organic · Hydrocarbons

The most suitable reagent for the following conversion, is :

![printed figure: but-2-yne → cis-2-butene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q055_2b399694_28102026.svg?v=2b3996947abd)

*but-2-yne → cis-2-butene*

![drawn: but-2-yne → cis-2-butene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q055_question_715244ed_28102026.svg?v=715244ed0a8d)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: but-2-yne `CC#CC` ![but-2-yne](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q055_question_s1_e5e0f53b_28102026.svg?v=e5e0f53bcbc7); (Z)-but-2-ene `C/C=C\C` ![(Z)-but-2-ene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q055_question_s2_1608ef32_28102026.svg?v=1608ef3214e9)

- (1) $\mathrm{Na}$/liquid $\mathrm{NH_3}$
- **(2)** $\mathrm{H_2}$, $\mathrm{Pd/C}$, quinoline
- (3) $\mathrm{Zn/HCl}$
- (4) $\mathrm{Hg^{2+}/H^{+}}$, $\mathrm{H_2O}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The conversion is partial reduction of but-2-yne $\mathrm{CH_3C{\equiv}CCH_3}$ to cis-but-2-ene, which needs syn addition of $\mathrm{H_2}$.
2. Lindlar-type catalyst $\mathrm{H_2,\ Pd/C}$ poisoned with quinoline stops at the alkene and adds $\mathrm{H_2}$ syn, giving the cis alkene.
3. $\mathrm{Na}$/liquid $\mathrm{NH_3}$ gives anti addition (trans-2-butene), $\mathrm{Zn/HCl}$ does not reduce the alkyne to the cis alkene, and $\mathrm{Hg^{2+}/H^{+}, H_2O}$ hydrates it to a ketone, so the answer is option $2$.

**Subtopic:** Preparation of Alkenes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q055_09d67ee2_28102026.png?v=09d67ee2e28e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Lindlar's catalyst - hydrogen over palladium poisoned with quinoline - adds the two hydrogens on the same side to give the cis-alkene, while sodium in liquid ammonia gives the trans
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Sodium in liquid ammonia does convert but-2-yne to but-2-ene, so dropping the printed 'cis' from the product leaves this reagent looking right; with the geometry kept, it delivers the trans isomer instead.
- **Why:** This question requires the reagent that effects a printed conversion, demonstrated by the scheme 'but-2-yne → cis-2-butene' with the arrow deliberately left bare.
- **Note:** The figure arrived as text, 'but-2-yne → cis-2-butene', with nothing printed over the arrow, so the conversion is readable here and a trap can be audited; the options are text and complete.
<!--/ecat-->

## Q56

Chemistry · inorganic · The p–Block Elements

Which is the correct thermal stability order for $\mathrm{H_2E}$ ($\mathrm{E} = \mathrm{O}$, $\mathrm{S}$, $\mathrm{Se}$, $\mathrm{Te}$ and $\mathrm{Po}$)?

- (1) $\mathrm{H_2S} < \mathrm{H_2O} < \mathrm{H_2Se} < \mathrm{H_2Te} < \mathrm{H_2Po}$
- (2) $\mathrm{H_2O} < \mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te} < \mathrm{H_2Po}$
- **(3)** $\mathrm{H_2Po} < \mathrm{H_2Te} < \mathrm{H_2Se} < \mathrm{H_2S} < \mathrm{H_2O}$
- (4) $\mathrm{H_2Se} < \mathrm{H_2Te} < \mathrm{H_2Po} < \mathrm{H_2O} < \mathrm{H_2S}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Down group 16 ($\mathrm{O} \to \mathrm{Po}$) the size of $\mathrm{E}$ increases, so the $\mathrm{E{-}H}$ bond becomes longer.
2. A longer bond is weaker: $\Delta_{diss}H(\mathrm{E{-}H})$ decreases from $\mathrm{O{-}H}$ to $\mathrm{Po{-}H}$.
3. Thermal stability follows bond strength, so $\mathrm{H_2Po} < \mathrm{H_2Te} < \mathrm{H_2Se} < \mathrm{H_2S} < \mathrm{H_2O}$, which is option $3$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q056_ac78ab00_28102026.png?v=ac78ab006810)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Thermal stability of the group-16 hydrides falls as the E-H bond strength falls down the group, so $\mathrm{H_2O}$ is the most stable and $\mathrm{H_2Po}$ the least
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The sequence printed here is the exact reverse of the key: the acidic-strength trend, which does rise down the group, is carried over to thermal stability, so the inequality signs end up pointing the wrong way.
- **Why:** This question requires one group trend arranged as an order, demonstrated by 'the correct thermal stability order for $\mathrm{H_2E}$' with the direction left to the printed inequality signs.
- **Note:** E1 called this statement_options; the options are inequality chains rather than statements to judge, so the shape is recorded as mcq with asks order.
<!--/ecat-->

## Q57

Chemistry · inorganic · The p–Block Elements

Which of the following is incorrect statement?

- **(1)** $\mathrm{PbF_4}$ is covalent in nature
- (2) $\mathrm{SiCl_4}$ is easily hydrolysed
- (3) $\mathrm{GeX_4}$ ($\mathrm{X} = \mathrm{F}, \mathrm{Cl}, \mathrm{B}\ , \mathrm{I}$) is more stable than $\mathrm{GeX_2}$
- (4) $\mathrm{SnF_4}$ is ionic in nature

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Group 14 tetrahalides are generally covalent, but $\mathrm{SnF_4}$ and $\mathrm{PbF_4}$ are exceptions that are ionic in nature, so option $4$ is correct and option $1$ ("$\mathrm{PbF_4}$ is covalent") is incorrect.
2. $\mathrm{SiCl_4}$ has vacant $d$ orbitals on Si that accept a lone pair from $\mathrm{H_2O}$, so it is easily hydrolysed: $\mathrm{SiCl_4 + 4H_2O \rightarrow Si(OH)_4 + 4HCl}$; option $2$ is correct.
3. For Ge the inert pair effect is weak, so the $+4$ state is more stable and $\mathrm{GeX_4}$ is more stable than $\mathrm{GeX_2}$; option $3$ is correct.
4. Hence the incorrect statement is option $1$.

**Subtopic:** General Properties & Trends of Group 14 (Carbon Family) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q057_e86028e8_28102026.png?v=e86028e86c9b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Among the group-14 tetrahalides the heavier fluorides $\mathrm{SnF_4}$ and $\mathrm{PbF_4}$ are ionic, while the other tetrahalides are covalent
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The general rule that group-14 tetrahalides are covalent, held without the fluoride exception, makes the true statement '$\mathrm{SnF_4}$ is ionic' read as the incorrect one and leaves the genuinely false $\mathrm{PbF_4}$ line standing.
- **Why:** This question requires the stated bonding character of named group-14 halides, demonstrated by '$\mathrm{PbF_4}$ is covalent in nature' standing against '$\mathrm{SnF_4}$ is ionic in nature' in the same option set.
- **Note:** Option 3 prints the halogen list as 'X = F, Cl, B , I', where B appears to stand for Br; the slip does not change which statement is incorrect, and the question is tagged as printed.
<!--/ecat-->

## Q58

Chemistry · inorganic · The p–Block Elements

Match the following :
Which of the following is the correct option?

| List-I | | List-II | |
|---|---|---|---|
| a | Pure nitrogen | i | Chlorine |
| b | Haber process | ii | Sulphuric acid |
| c | Contact process | iii | Ammonia |
| d | Deacon’s process | iv | Sodium azide or Barium azide |

- (1) (i) (ii) (iii) (iv)
- (2) (ii) (iv) (i) (iii)
- (3) (iii) (iv) (ii) (i)
- **(4)** (iv) (iii) (ii) (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Very pure nitrogen is obtained by thermal decomposition of azide: $\mathrm{Ba(N_3)_2 \rightarrow Ba + 3N_2}$, so (a)-(iv).
2. Haber process: $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$, so (b)-(iii).
3. Contact process: $\mathrm{2SO_2 + O_2 \rightarrow 2SO_3}$, then $\mathrm{H_2SO_4}$, so (c)-(ii).
4. Deacon's process: $\mathrm{4HCl + O_2 \xrightarrow{CuCl_2} 2Cl_2 + 2H_2O}$, so (d)-(i).
5. The order (iv) (iii) (ii) (i) is option $4$.

**Subtopic:** Dinitrogen - Preparation, Properties and Uses, Ammonia – Preparation, Properties and Test with Cu · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q058_f7070142_28102026.png?v=f707014287ba)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named industrial process has one printed product - Haber gives ammonia, contact gives sulphuric acid, Deacon's gives chlorine - and pure dinitrogen comes from a decomposing azide
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Ammonia is the nitrogen compound printed beside dinitrogen in the same section, so 'Pure nitrogen' takes (iii) Ammonia and the azide is left over for the Haber process by elimination, while the contact and Deacon rows stay right.
- **Why:** This question requires the product the source states for each named process, demonstrated by 'Haber process' and 'Contact process' in Column I standing against 'Ammonia' and 'Sulphuric acid' in Column II.
- **Note:** asks is fact_line, not compare: three of the four rows ask only which product belongs to a named process, which is a stated fact, and row (a) asks which reagent is decomposed for pure dinitrogen - also printed rather than worked out. compare was ruled out because nothing here asks for two similar things to be told apart; the pairing itself is already recorded by qtype match_columns.
<!--/ecat-->

## Q59

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following diatomic molecular species has only $\pi$ bonds according to Molecular Orbital Theory?

- (1) $\mathrm{O_2}$
- (2) $\mathrm{N_2}$
- **(3)** $\mathrm{C_2}$
- (4) $\mathrm{Be_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{C_2}$ has 12 electrons: $KK\,\sigma 2s^2\,\sigma^* 2s^2\,(\pi 2p_x^2 = \pi 2p_y^2)$.
2. The $\sigma 2s$ and $\sigma^* 2s$ contributions cancel, and $\sigma 2p_z$ is empty, so bond order $= \frac{8-4}{2} = 2$ arises entirely from the two $\pi$ bonds.
3. $\mathrm{N_2}$ and $\mathrm{O_2}$ both fill $\sigma 2p_z$ (they contain a $\sigma$ bond), and $\mathrm{Be_2}$ has bond order $0$, so the answer is $\mathrm{C_2}$, option $3$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q059_a9e2b76d_28102026.png?v=a9e2b76d2cba)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In $\mathrm{C_2}$ the $\sigma 2s$ and $\sigma^* 2s$ contributions cancel, so the bond order of 2 comes entirely from the two filled $\pi 2p$ orbitals
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  $\mathrm{N_2}$ is the molecule the molecular orbital diagram is worked through, and it does carry two $\pi$ bonds, so a student counting $\pi$ bonds stops at the familiar neighbour and overlooks the $\sigma 2p$ bond it also has.
- **Why:** This question requires each species' molecular orbital filling read for bond type, demonstrated by 'has only $\pi$ bonds according to Molecular Orbital Theory' with four diatomic species as options.
- **Note:** nearby_fact rather than look_alike_term: the two formulas resemble each other in no way, and the swap test confirms it - replacing $\mathrm{C_2}$ and $\mathrm{N_2}$ with unlike names leaves the pull intact, since it rests on $\mathrm{N_2}$ being the species the diagram is demonstrated on.
<!--/ecat-->

## Q60

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

For the second period elements the correct increasing order of first ionisation enthalpy is:

- (1) $\mathrm{Li < Be < B < C < N < O < F < Ne}$
- **(2)** $\mathrm{Li < B < Be < C < O < N < F < Ne}$
- (3) $\mathrm{Li < B < Be < C < N < O < F < Ne}$
- (4) $\mathrm{Li < Be < B < C < O < N < F < Ne}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Across period 2 the nuclear charge rises and atomic size falls, so first ionisation enthalpy generally increases from $\mathrm{Li}$ to $\mathrm{Ne}$.
2. $\mathrm{Be}$ ($2s^2$) loses a penetrating $2s$ electron while $\mathrm{B}$ ($2s^2 2p^1$) loses a less penetrating, better shielded $2p$ electron, so $\Delta_i H(\mathrm{B}) < \Delta_i H(\mathrm{Be})$.
3. $\mathrm{N}$ has a stable half-filled $2p^3$ configuration while $\mathrm{O}$ ($2p^4$) loses a paired electron with extra repulsion, so $\Delta_i H(\mathrm{O}) < \Delta_i H(\mathrm{N})$.
4. Hence $\mathrm{Li < B < Be < C < O < N < F < Ne}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q060_fe0620d0_28102026.png?v=fe0620d022e7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** First ionisation enthalpy rises across period 2 but breaks twice: Be is above B because a 2s electron is harder to pull than a 2p, and N is above O because O must lose a paired 2p electron
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who knows the Be-above-B break and applies it correctly then runs the rest of the period straight, so N and O are left in plain atomic-number order and only one of the two breaks survives.
- **Why:** This question requires an ordering, demonstrated by the stem asking for 'the correct increasing order of first ionisation enthalpy' and by the four options differing only at the Be-B and N-O positions.
- **Note:** qtype is recorded as mcq because the codebook's arrange_in_order maps there; the ordering demand sits in asks: order.
<!--/ecat-->

## Q61

Chemistry · organic · Polymers

The biodegradable polymer is:

- (1) Nylon-6,6
- **(2)** Nylon 2-Nylon 6
- (3) Nylon-6
- (4) Buna-S

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Nylon 2-nylon 6 is an alternating polyamide copolymer of glycine and $\epsilon$-aminocaproic acid and is biodegradable, while nylon-6,6, nylon-6 and Buna-S are non-biodegradable, so the answer is option $2$.

**Subtopic:** Biodegradable Polymers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q061_255f6698_28102026.png?v=255f66987cd6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nylon 2-nylon 6 is the biodegradable polyamide copolymer of glycine and amino caproic acid; the ordinary nylons and Buna-S are not biodegradable
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  A student who remembers the answer as a nylon with a 6 in its name takes the shorter name that the key's own name contains, Nylon-6, which is an ordinary non-biodegradable polyamide.
- **Why:** This question requires the stated membership of a named list, demonstrated by the stem 'The biodegradable polymer is:' with three non-biodegradable polymers beside the one printed in that section.
- **Note:** Applied the 5.1 test on the trap: replacing Nylon-6 with an unlike polymer name kills the pull, because what carries the student is that the distractor's name is contained inside the key's name, so this is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q62

Chemistry · physical · Ionic Equilibrium

pH of a saturated solution of $\mathrm{Ca(OH)_2}$ is 9. The solubility product $(K_{sp})$ of $\mathrm{Ca(OH)_2}$ is:

- **(1)** $0.5 \times 10^{-15}$
- (2) $0.25 \times 10^{-10}$
- (3) $0.125 \times 10^{-15}$
- (4) $0.5 \times 10^{-10}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{pOH} = 14 - \mathrm{pH} = 14 - 9 = 5$.
2. $[\mathrm{OH^-}] = 10^{-5}\,\mathrm{M}$.
3. $\mathrm{Ca(OH)_2} \rightleftharpoons \mathrm{Ca^{2+}} + 2\mathrm{OH^-}$, so $[\mathrm{Ca^{2+}}] = \frac{[\mathrm{OH^-}]}{2} = 0.5 \times 10^{-5}\,\mathrm{M}$.
4. $K_{sp} = [\mathrm{Ca^{2+}}][\mathrm{OH^-}]^2 = (0.5 \times 10^{-5})(10^{-5})^2 = 0.5 \times 10^{-15}$, which is option $1$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q062_62b240eb_28102026.png?v=62b240eb014d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For $\mathrm{Ca(OH)_2}$, $K_{sp} = [\mathrm{Ca^{2+}}][\mathrm{OH^-}]^2 = 4s^3$, so the hydroxide concentration read from the pH has to be both halved for the cation and squared for the anion
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  A student who gets $s = 0.5 \times 10^{-5}$ and writes $K_{sp} = s^3$ drops the factor 4 that the stoichiometry puts in front, giving $0.125 \times 10^{-15}$ instead of $0.5 \times 10^{-15}$.
- **Why:** This question requires a number computed from the stem, demonstrated by it supplying 'pH of a saturated solution of Ca(OH)2 is 9' and asking for the solubility product.
<!--/ecat-->

## Q63

Chemistry · physical · Chemical Kinetics

If the rate constant for a first order reaction is $k$, the time $(t)$ required for the completion of $99\%$ of the reaction is given by:

- (1) $t = 0.693/k$
- (2) $t = 6.909/k$
- **(3)** $t = 4.606/k$
- (4) $t = 2.303/k$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a first order reaction, $t = \frac{2.303}{k}\log\frac{[A]_0}{[A]}$.
2. After $99\%$ completion, $[A] = 0.01[A]_0$, so $\frac{[A]_0}{[A]} = 100$.
3. $\log 100 = 2$, so $t = \frac{2.303 \times 2}{k} = \frac{4.606}{k}$, which is option $3$.

**Subtopic:** First Order Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q063_3b062c37_28102026.png?v=3b062c37314c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a first order reaction $t = \frac{2.303}{k}\log\frac{[A]_0}{[A]}$, and 99% completion means the ratio is 100, so the logarithm is 2
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  A student reaches for the one first-order time they hold as a formula, the half-life $0.693/k$, which is the true time for 50% completion and not for 99%.
- **Why:** This question requires an expression obtained from the integrated rate law, demonstrated by the stem asking for 'the time (t) required for the completion of 99% of the reaction' in terms of k.
<!--/ecat-->

## Q64

Chemistry · organic · Biomolecules

The non-essential amino acid among the following is:

- (1) valine
- (2) leucine
- **(3)** alanine
- (4) lysine

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Valine, leucine and lysine are essential amino acids (they must come from the diet), while alanine is synthesised in the body, so the non-essential one is alanine, option $3$.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q064_f288ab8c_28102026.png?v=f288ab8c1410)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Non-essential amino acids are those the body can synthesise, and alanine is one of them; valine, leucine and lysine have to come from the diet
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead  
  All three wrong options are members of the essential list printed beside the non-essential one, so a student who holds the two lists as lists but not which name sits in which is carried to whichever of the three they half-recall as home-made.
- **Why:** This question requires the stated membership of the non-essential list, demonstrated by the stem 'The non-essential amino acid among the following is:' with four names from the same table as options.
- **Note:** No single option dominates here: all three wrong options are drawn from the essential list and no printed word in the stem or in any option favours one of them, so the trap is recorded at set level with no option named, as the schema allows, and each wrong option carries its own route in other_options.
<!--/ecat-->

## Q65

Chemistry · organic · Haloalkanes and Haloarenes

Among the following, the reaction that proceeds through an electrophilic substitution, is:

- (1) benzenediazonium chloride `N#[N+]c1ccccc1.[Cl-]` ![benzenediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_1_s1_4e4b99bb_28102026.svg?v=4e4b99bb5d11); chlorobenzene `Clc1ccccc1` ![chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_1_s2_56d22037_28102026.svg?v=56d220370f56); dinitrogen `N#N` ![dinitrogen](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_1_s3_954b7428_28102026.svg?v=954b7428b3ff); dicopper dichloride `[Cl-].[Cl-].[Cu+].[Cu+]` ![dicopper dichloride](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_1_s4_d9ad1238_28102026.svg?v=d9ad1238cb83) — [benzene ring]$-\overset{+}{\mathrm{N}}_2\mathrm{Cl}^{-} \xrightarrow{\mathrm{Cu_2Cl_2}}$ [benzene ring]$-\mathrm{Cl} + \mathrm{N_2}$
- **(2)** benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_2_s1_8ef0b79c_28102026.svg?v=8ef0b79c19c9); dichlorine `ClCl` ![dichlorine](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_2_s2_5e64a175_28102026.svg?v=5e64a17500b3); chlorobenzene `Clc1ccccc1` ![chlorobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_2_s3_1d0b4a0c_28102026.svg?v=1d0b4a0c6070); hydrogen chloride `Cl` ![hydrogen chloride](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_2_s4_50337fd9_28102026.svg?v=50337fd9cb46) — [benzene ring]$+ \mathrm{Cl_2} \xrightarrow{\mathrm{AlCl_3}}$ [benzene ring]$-\mathrm{Cl} + \mathrm{HCl}$
- (3) benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_3_s1_e5ed400d_28102026.svg?v=e5ed400d326f); dichlorine `ClCl` ![dichlorine](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_3_s2_5e64a175_28102026.svg?v=5e64a17500b3); 1,2,3,4,5,6-hexachlorocyclohexane `ClC1C(Cl)C(Cl)C(Cl)C(Cl)C1Cl` ![1,2,3,4,5,6-hexachlorocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_3_s3_033716c6_28102026.svg?v=033716c64846) — [benzene ring]$+ \mathrm{Cl_2} \xrightarrow{\text{UV light}}$ [cyclohexane ring with six $-\mathrm{Cl}$]
- (4) phenylmethanol `OCc1ccccc1` ![phenylmethanol](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_4_s1_3b4d40fc_28102026.svg?v=3b4d40fce4be); hydrogen chloride `Cl` ![hydrogen chloride](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_4_s2_50337fd9_28102026.svg?v=50337fd9cb46); (chloromethyl)benzene `ClCc1ccccc1` ![(chloromethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_4_s3_d517a95e_28102026.svg?v=d517a95e575a); water `O` ![water](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q065_option_4_s4_cbac8b2a_28102026.svg?v=cbac8b2a939f) — [benzene ring]$-\mathrm{CH_2OH} + \mathrm{HCl} \xrightarrow{\text{heat}}$ [benzene ring]$-\mathrm{CH_2Cl} + \mathrm{H_2O}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Option $1$: $\mathrm{C_6H_5N_2^+Cl^-} \xrightarrow{\mathrm{Cu_2Cl_2}} \mathrm{C_6H_5Cl}$ is the Sandmeyer reaction, a radical (nucleophilic-type) replacement of $\mathrm{N_2}$, not electrophilic substitution.
2. Option $2$: $\mathrm{Cl_2} + \mathrm{AlCl_3} \rightarrow \mathrm{Cl^+} + \mathrm{AlCl_4^-}$ generates the electrophile.
3. $\mathrm{Cl^+}$ attacks the benzene ring to form the arenium ion, which loses $\mathrm{H^+}$ to give $\mathrm{C_6H_5Cl} + \mathrm{HCl}$: electrophilic aromatic substitution.
4. Option $3$: $\mathrm{C_6H_6} + 3\mathrm{Cl_2} \xrightarrow{h\nu} \mathrm{C_6H_6Cl_6}$ is free-radical addition.
5. Option $4$: $\mathrm{C_6H_5CH_2OH} + \mathrm{HCl} \rightarrow \mathrm{C_6H_5CH_2Cl}$ is nucleophilic substitution at the benzylic carbon.
6. Only option $2$ proceeds by electrophilic substitution.

**Subtopic:** Preparation of Haloarenes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q065_b68468e9_28102026.png?v=b68468e9af30)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Electrophilic substitution is an electrophile replacing a hydrogen on the aromatic ring, which is what the Lewis-acid-catalysed chlorination does and what free-radical and side-chain reactions do not
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  A student who matches the reagents -- benzene plus chlorine -- without reading what sits over the arrow takes the UV-light reaction, where chlorine behaves as a radical and adds to the ring instead of substituting on it.
- **Why:** This question requires the mechanism a printed reaction goes by, demonstrated by the stem 'the reaction that proceeds through an electrophilic substitution, is:' with four written reactions as the options.
- **Note:** E1_question_type is null because no pattern covers options that are reactions; the printed shape is the codebook's reaction_options, which maps to qtype mcq. asks is recorded as reaction, following the codebook's reaction_mechanism mapping onto that value; the alternative reading, apply_rule, was set aside because the material being judged is four printed reactions rather than a rule applied to a fresh case.
<!--/ecat-->

## Q66

Chemistry · physical · Solutions

The mixture that forms maximum boiling azeotrope is:

- **(1)** Water + Nitric acid
- (2) Ethanol + Water
- (3) Acetone + Carbon disulphide
- (4) Heptane + Octane

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A maximum boiling azeotrope forms when a solution shows large negative deviation from Raoult's law ($p_{total} < x_A p_A^0 + x_B p_B^0$).
2. Water + nitric acid shows strong negative deviation (stronger $A\text{--}B$ attractions) and forms a maximum boiling azeotrope at about $68\%$ $\mathrm{HNO_3}$ by mass.
3. Ethanol + water and acetone + $\mathrm{CS_2}$ show positive deviation, so they give minimum boiling azeotropes.
4. Heptane + octane forms a nearly ideal solution with no azeotrope, so the answer is option $1$.

**Subtopic:** Azeotropes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q066_cca2f753_28102026.png?v=cca2f753b202)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A maximum boiling azeotrope comes from negative deviation from Raoult's law, where the two components attract each other more strongly than themselves, as in nitric acid and water
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  A student recalls the one azeotrope everybody meets, 95% ethanol with water, which is a true azeotrope but the MINIMUM boiling one, since ethanol and water deviate positively.
- **Why:** This question requires the stated example of a named behaviour, demonstrated by the stem 'The mixture that forms maximum boiling azeotrope is:' with four named mixtures as options.
<!--/ecat-->

## Q67

Chemistry · physical · Chemical Kinetics

For the chemical reaction
$\mathrm{N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)}$
the correct option is:

- (1) $-\frac{1}{3}\frac{d[\mathrm{H_2}]}{dt} = -\frac{1}{2}\frac{d[\mathrm{NH_3}]}{dt}$
- (2) $-\frac{d[\mathrm{N_2}]}{dt} = 2\frac{d[\mathrm{NH_3}]}{dt}$
- **(3)** $-\frac{d[\mathrm{N_2}]}{dt} = \frac{1}{2}\frac{d[\mathrm{NH_3}]}{dt}$
- (4) $3\frac{d[\mathrm{H_2}]}{dt} = 2\frac{d[\mathrm{NH_3}]}{dt}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$, divide each rate of change by its stoichiometric coefficient, with a minus sign for reactants.
2. $\text{rate} = -\frac{d[\mathrm{N_2}]}{dt} = -\frac{1}{3}\frac{d[\mathrm{H_2}]}{dt} = +\frac{1}{2}\frac{d[\mathrm{NH_3}]}{dt}$.
3. Option 1 puts a minus sign on $\frac{d[\mathrm{NH_3}]}{dt}$ (product), so it is wrong.
4. Option 2 uses factor $2$ instead of $\frac{1}{2}$, so it is wrong.
5. Option 4: the correct relation is $-2\frac{d[\mathrm{H_2}]}{dt} = 3\frac{d[\mathrm{NH_3}]}{dt}$, so it is wrong.
6. $-\frac{d[\mathrm{N_2}]}{dt} = \frac{1}{2}\frac{d[\mathrm{NH_3}]}{dt}$ matches option $3$.

**Subtopic:** Rate of a Chemical Reaction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q067_8f91e27c_28102026.png?v=8f91e27c5aa3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** One rate of reaction is got by dividing each species' rate of change by its stoichiometric coefficient, with a minus sign for reactants and a plus for products
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who reasons that ammonia appears twice as fast as nitrogen disappears puts the 2 on the wrong side, writing $-d[\mathrm{N_2}]/dt = 2\,d[\mathrm{NH_3}]/dt$ when the coefficient divides rather than multiplies.
- **Why:** This question requires a convention applied to a printed equation, demonstrated by the stem giving 'N2(g) + 3H2(g) to 2NH3(g)' and asking for 'the correct option' among four rate relations.
- **Note:** The stem is only an instruction and each option is a complete relation to be judged, which is the codebook's statement_options, so qtype is statements.
<!--/ecat-->

## Q68

Chemistry · physical · Basic Concepts of Chemistry

The number of moles of hydrogen molecules required to produce 20 moles of ammonia through Haber's process is :

- (1) 10
- (2) 20
- **(3)** 30
- (4) 40

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Haber's process: $\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}$.
2. Mole ratio $\frac{n(\mathrm{H_2})}{n(\mathrm{NH_3})} = \frac{3}{2}$.
3. $n(\mathrm{H_2}) = 20 \times \frac{3}{2} = 30$ mol, which is option $3$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q068_79c6f619_28102026.png?v=79c6f6191105)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Haber's process runs $\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}$, so each mole of ammonia needs one and a half moles of hydrogen
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  A student who works the stoichiometry from the nitrogen side gets 10, which is the moles of NITROGEN needed for 20 moles of ammonia, not the moles of hydrogen the stem asks for.
- **Why:** This question requires a number computed from the stem, demonstrated by it asking for 'the number of moles of hydrogen molecules required to produce 20 moles of ammonia'.
<!--/ecat-->

## Q69

Chemistry · organic · Alcohols, Phenols and Ethers

The compound that is most difficult to protonate is :

- (1) water `O` ![water](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q069_option_1_s1_d5978eab_28102026.svg?v=d5978eabd7d2)
- (2) methanol `CO` ![methanol](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q069_option_2_s1_33303b1d_28102026.svg?v=33303b1d65df)
- (3) methoxymethane `COC` ![methoxymethane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q069_option_3_s1_4ef3a042_28102026.svg?v=4ef3a0420065)
- **(4)** phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q069_option_4_s1_c923df7d_28102026.svg?v=c923df7d9f96)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Ease of protonation depends on the availability of the oxygen lone pair (basicity).
2. Electron-donating $\mathrm{CH_3}$ groups (+I) raise electron density on O, so $\mathrm{CH_3OCH_3} > \mathrm{CH_3OH} > \mathrm{H_2O}$ in basicity.
3. In $\mathrm{Ph{-}O{-}H}$ the O lone pair is delocalised into the benzene ring by resonance, so it is least available for $\mathrm{H^+}$.
4. Hence phenol is the most difficult to protonate, which is option $4$.

**Subtopic:** Acidity of Phenols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q069_43ad3992_28102026.png?v=43ad39921c76)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** How hard a compound is to protonate depends on how available the lone pair on its oxygen is, which substituents and conjugation with a ring take away
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings in this record, so there is nothing printed to find a route to; the stem alone does not say which four compounds were set against each other.
- **Why:** This question requires four compounds to be told apart on one property, demonstrated by the stem 'The compound that is most difficult to protonate is :' -- but the options our record holds are blank, so no further reading is possible.
- **Note:** options_en carries four empty strings and figure_image is null, while the printed paper for an 'Acidity of Phenols' item of this kind sets out drawn structures. The option set as we hold it is unusable, so this is a repair task, not a finding about the question: the four structures need re-extracting before any trap can be written. qtype and asks are recorded from the stem alone -- a superlative over four similar compounds, hence compare rather than order, since the answer is one compound and not a sequence -- and both should be re-checked once the options are restored. A reviewer holding the printed options should look for the compound whose lone pair is tied up in conjugation, which is the mechanism this stem is built on.
<!--/ecat-->

## Q70

Chemistry · physical · Solutions

For an ideal solution, the correct option is :

- (1) $\Delta_{\mathrm{mix}} S = 0$ at constant $T$ and $P$
- (2) $\Delta_{\mathrm{mix}} V \neq 0$ at constant $T$ and $P$
- **(3)** $\Delta_{\mathrm{mix}} H = 0$ at constant $T$ and $P$
- (4) $\Delta_{\mathrm{mix}} G = 0$ at constant $T$ and $P$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In an ideal solution solute-solvent interactions equal solute-solute and solvent-solvent interactions, so $\Delta_{\mathrm{mix}} H = 0$ and $\Delta_{\mathrm{mix}} V = 0$ at constant $T$ and $P$.
2. Mixing increases randomness, so $\Delta_{\mathrm{mix}} S > 0$, ruling out option $1$; $\Delta_{\mathrm{mix}} V = 0$ rules out option $2$.
3. $\Delta_{\mathrm{mix}} G = \Delta_{\mathrm{mix}} H - T\Delta_{\mathrm{mix}} S = -T\Delta_{\mathrm{mix}} S < 0$, ruling out option $4$.
4. Hence $\Delta_{\mathrm{mix}} H = 0$ is the correct statement, which is option $3$.

**Subtopic:** Ideal and Nonideal Solutions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q070_5f6f73ce_28102026.png?v=5f6f73cea2e7)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An ideal solution obeys Raoult's law over the whole range, and what vanishes on mixing is the enthalpy and the volume change -- not the entropy, and not the free energy
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who holds 'nothing changes on mixing an ideal solution' carries the zero across to entropy as well, when mixing always increases the disorder and so $\Delta_{\mathrm{mix}}S > 0$.
- **Why:** This question requires the stated conditions defining an ideal solution, demonstrated by four rival claims about mixing quantities 'at constant T and P', of which only the enthalpy one holds.
- **Note:** The stem is only an instruction and each option is a complete claim to be judged, which is the codebook's statement_options, so qtype is statements.
<!--/ecat-->

## Q71

Chemistry · physical · Ionic Equilibrium

Conjugate base for Brönsted acids $\mathrm{H_2O}$ and $\mathrm{HF}$ are :

- (1) $\mathrm{OH^-}$ and $\mathrm{H_2F^+}$, respectively
- (2) $\mathrm{H_3O^+}$ and $\mathrm{F^-}$, respectively
- **(3)** $\mathrm{OH^-}$ and $\mathrm{F^-}$, respectively
- (4) $\mathrm{H_3O^+}$ and $\mathrm{H_2F^+}$, respectively

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A conjugate base is what remains after a Brönsted acid gives away one proton: $\mathrm{HA} \rightarrow \mathrm{A^-} + \mathrm{H^+}$.
2. $\mathrm{H_2O} \rightarrow \mathrm{OH^-} + \mathrm{H^+}$, so the conjugate base of $\mathrm{H_2O}$ is $\mathrm{OH^-}$.
3. $\mathrm{HF} \rightarrow \mathrm{F^-} + \mathrm{H^+}$, so the conjugate base of $\mathrm{HF}$ is $\mathrm{F^-}$, which is option $3$.

**Subtopic:** Brønsted–Lowry Acids and Bases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q071_ac755067_28102026.png?v=ac755067381c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A Bronsted acid's conjugate base is what is left after it donates one proton, so water gives OH- and HF gives F-
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student handles HF correctly to give F- and then gives water the species it is most often printed with, $\mathrm{H_3O^+}$, which is what water becomes when it ACCEPTS a proton.
- **Why:** This question requires one rule applied to two cases at once, demonstrated by the stem asking for the conjugate base of 'H2O and HF' with every option naming two species 'respectively'.
- **Note:** E1_question_type says statement_options; the stem asks for two answers together and every option is a pair joined by 'respectively', which is the codebook's multi_part_respectively and maps to qtype two_part.
<!--/ecat-->

## Q72

Chemistry · physical · Surface Chemistry

Which mixture of the solutions will lead to the formation of negatively charged colloidal $[\mathrm{AgI}]\mathrm{I^{-}}$ sol. ?

- **(1)** $50\,\mathrm{mL}$ of $1\,\mathrm{M}$ $\mathrm{AgNO_3}$ + $50\,\mathrm{mL}$ of $1.5\,\mathrm{M}$ $\mathrm{KI}$
- **(2)** $50\,\mathrm{mL}$ of $1\,\mathrm{M}$ $\mathrm{AgNO_3}$ + $50\,\mathrm{mL}$ of $2\,\mathrm{M}$ $\mathrm{KI}$
- (3) $50\,\mathrm{mL}$ of $2\,\mathrm{M}$ $\mathrm{AgNO_3}$ + $50\,\mathrm{mL}$ of $1.5\,\mathrm{M}$ $\mathrm{KI}$
- (4) $50\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{AgNO_3}$ + $50\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{KI}$

**Answer** — booklet: (1, 2) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A negative $[\mathrm{AgI}]\mathrm{I^{-}}$ sol forms when $\mathrm{AgNO_3}$ is added to excess $\mathrm{KI}$, so $\mathrm{I^{-}}$ is adsorbed on $\mathrm{AgI}$.
2. Option 1: $n(\mathrm{Ag^+}) = 0.05 \times 1 = 0.05\,\mathrm{mol}$, $n(\mathrm{I^-}) = 0.05 \times 1.5 = 0.075\,\mathrm{mol}$, so $\mathrm{I^-}$ is in excess by $0.025\,\mathrm{mol}$.
3. Option 2: $n(\mathrm{Ag^+}) = 0.05\,\mathrm{mol}$, $n(\mathrm{I^-}) = 0.05 \times 2 = 0.10\,\mathrm{mol}$, so $\mathrm{I^-}$ is in excess by $0.05\,\mathrm{mol}$.
4. Option 3: $n(\mathrm{Ag^+}) = 0.10\,\mathrm{mol} > n(\mathrm{I^-}) = 0.075\,\mathrm{mol}$, so $\mathrm{Ag^+}$ is in excess and the sol would be positive $[\mathrm{AgI}]\mathrm{Ag^+}$.
5. Option 4: $n(\mathrm{Ag^+}) = n(\mathrm{I^-}) = 0.005\,\mathrm{mol}$, no excess ion, so no charged sol is stabilised.
6. Options 1 and 2 both give excess $\mathrm{I^-}$; option 1 has the smaller excess, which favours a stable sol over coagulation by excess electrolyte, so choose option $1$.

**Subtopic:** Charge on Colloidal Particles · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q072_247cc5ca_28102026.png?v=247cc5ca2868)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A colloidal AgI sol takes the charge of whichever ion is left in excess after precipitation, because that ion is preferentially adsorbed on the AgI surface
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Counting millimoles gives $100$ of $\mathrm{AgNO_3}$ against $75$ of $\mathrm{KI}$, so the excess ion here is $\mathrm{Ag^+}$ and the sol is $[\mathrm{AgI}]\mathrm{Ag^+}$; reading the excess the other way round turns a positive sol into the negative one asked for
- **Why:** This question requires the preferential-adsorption rule applied to the millimoles each mixture supplies, demonstrated by the stem asking for a "negatively charged colloidal $[\mathrm{AgI}]\mathrm{I^-}$ sol" while every option prints a volume and a molarity.
- **Note:** The answer line prints two options and `accepted_answers` holds both; options 1 and 2 each leave KI in excess ($75$ against $50$ mmol, and $100$ against $50$ mmol), so both do give the negative sol and neither carries a trap here. The E1 pattern called this `statement_options` on option length, but the options are reagent mixtures, not statements to judge, so the printed shape is a plain MCQ.
<!--/ecat-->

## Q73

Chemistry · organic · Chemistry in Everyday Life

Among the following, the narrow spectrum antibiotic is :

- **(1)** Penicillin G
- (2) Ampicillin
- (3) Amoxycillin
- (4) Chloramphenicol

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A narrow spectrum antibiotic acts mainly against either Gram-positive or Gram-negative bacteria; Penicillin G acts mainly against Gram-positive bacteria, while Ampicillin, Amoxycillin and Chloramphenicol are broad spectrum, so the answer is option $1$.

**Subtopic:** Antibiotics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q073_a8a6d184_28102026.png?v=a8a6d18451ef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Penicillin G is narrow spectrum because it acts mainly on Gram-positive bacteria, while its semi-synthetic relatives ampicillin and amoxycillin were made broad spectrum
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Ampicillin is printed in the same sentence as penicillin G as a penicillin, so a student holding "the penicillins are the narrow ones" takes the neighbour on the page instead of the parent drug
- **Why:** This question requires the stated classification of one named drug, demonstrated by the stem asking only for "the narrow spectrum antibiotic" with four drug names and no criterion printed to apply.
<!--/ecat-->

## Q74

Chemistry · organic · Hydrocarbons

An alkene "A" on reaction with $\mathrm{O_3}$ and $\mathrm{Zn{-}H_2O}$ gives propanone and ethanal in equimolar ratio. Addition of $\mathrm{HCl}$ to alkene "A" gives "B" as the major product. The structure of product "B" is:

- (1) 1-chloro-3-methylbutane `CC(C)CCCl` ![1-chloro-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q074_option_1_s1_c7603229_28102026.svg?v=c7603229fd4c) — $\mathrm{Cl{-}CH_2{-}CH_2{-}CH(CH_3)_2}$
- (2) 1-chloro-2-methylbutane `CCC(C)CCl` ![1-chloro-2-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q074_option_2_s1_5481264b_28102026.svg?v=5481264b618a) — $\mathrm{H_3C{-}CH_2{-}CH(CH_2Cl){-}CH_3}$
- **(3)** 2-chloro-2-methylbutane `CCC(C)(C)Cl` ![2-chloro-2-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q074_option_3_s1_08eb86e9_28102026.svg?v=08eb86e9d23a) — $\mathrm{H_3C{-}CH_2{-}C(CH_3)(Cl){-}CH_3}$
- (4) 2-chloro-3-methylbutane `CC(C)C(C)Cl` ![2-chloro-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q074_option_4_s1_29f764dd_28102026.svg?v=29f764ddaed6) — $\mathrm{H_3C{-}CH(Cl){-}CH(CH_3){-}CH_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Join the two carbonyl carbons of $\mathrm{(CH_3)_2C{=}O}$ and $\mathrm{CH_3CHO}$ by a double bond: $A = \mathrm{(CH_3)_2C{=}CH{-}CH_3}$ (2-methylbut-2-ene).
2. Protonation by $\mathrm{HCl}$ gives the more stable tertiary carbocation $\mathrm{(CH_3)_2\overset{+}{C}{-}CH_2CH_3}$ (Markovnikov).
3. $\mathrm{Cl^-}$ attacks it: $B = \mathrm{H_3C{-}CH_2{-}C(CH_3)(Cl){-}CH_3}$ (2-chloro-2-methylbutane), which is option $3$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q074_d2b78e87_28102026.png?v=d2b78e87e583)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Reductive ozonolysis cuts the double bond into its two carbonyl fragments, so the alkene can be rebuilt by joining the two carbonyl carbons, and HCl then adds by Markovnikov's rule
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  HCl does add across the double bond of $\mathrm{(CH_3)_2C{=}CHCH_3}$, but putting the chlorine on the $\mathrm{CH}$ carbon instead of the fully substituted one gives 2-chloro-3-methylbutane, the anti-Markovnikov product
- **Why:** This question requires the product of a named addition on an alkene first rebuilt from its ozonolysis fragments, demonstrated by the stem printing "gives propanone and ethanal in equimolar ratio" and then "Addition of $\mathrm{HCl}$ to alkene A gives B as the major product".
<!--/ecat-->

## Q75

Chemistry · inorganic · Coordination Compounds – Practice

What is the correct electronic configuration of the central atom in $\mathrm{K_4[Fe(CN)_6]}$ based on crystal field theory?

- (1) $t_{2g}^{4}\,e_{g}^{2}$
- **(2)** $t_{2g}^{6}\,e_{g}^{0}$
- (3) $e^{3}\,t_{2}^{3}$
- (4) $e^{4}\,t_{2}^{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Charge balance on $[\mathrm{Fe(CN)_6}]^{4-}$: $x + 6(-1) = -4 \Rightarrow x = +2$.
2. $\mathrm{Fe^{2+}}$ has configuration $[\mathrm{Ar}]\,3d^{6}$.
3. Six $\mathrm{CN^-}$ ligands give an octahedral field, so the split levels are $t_{2g}$ and $e_g$ (this rules out options $3$ and $4$, which are tetrahedral labels).
4. $\mathrm{CN^-}$ is a strong-field ligand, so $\Delta_o > P$ and the electrons pair in $t_{2g}$.
5. Low spin $d^{6}$: $t_{2g}^{6}\,e_g^{0}$, which is option $2$.

**Subtopic:** Crystal Field Theory and Its Limitations · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q075_8ba03956_28102026.png?v=8ba039563fe5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Crystal field filling for an octahedral complex: $\mathrm{Fe^{2+}}$ is $d^6$, and the strong field of six cyanide ligands puts all six electrons in the lower $t_{2g}$ set
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  $t_{2g}^{4}e_{g}^{2}$ is the right octahedral filling for $d^6$ when the splitting is small, so a student who gets $\mathrm{Fe^{2+}} = d^6$ and then applies Hund's rule without asking what $\mathrm{CN^-}$ does to $\Delta_o$ lands here
- **Why:** This question requires the crystal field filling rule applied to one named complex, demonstrated by the stem asking for the configuration "based on crystal field theory" of the central atom in $\mathrm{K_4[Fe(CN)_6]}$.
<!--/ecat-->

## Q76

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the incorrect statement related to $\mathrm{PCl_5}$ from the following:

- (1) Three equatorial $\mathrm{P{-}Cl}$ bonds make an angle of $120^\circ$ with each other
- (2) Two axial $\mathrm{P{-}Cl}$ bonds make an angle of $180^\circ$ with each other
- (3) Axial $\mathrm{P{-}Cl}$ bonds are longer than equatorial $\mathrm{P{-}Cl}$ bonds
- **(4)** $\mathrm{PCl_5}$ molecule is non-reactive

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{PCl_5}$ is $sp^3d$ hybridised with a trigonal bipyramidal shape: three equatorial $\mathrm{P{-}Cl}$ bonds at $120^\circ$ and two axial bonds at $180^\circ$, so options $1$ and $2$ are correct.
2. Each axial bond pair feels more repulsion from the equatorial bond pairs, so axial bonds are longer and weaker than equatorial bonds, so option $3$ is correct.
3. Because the axial bonds are longer and weaker, $\mathrm{PCl_5}$ is very reactive, so the statement that it is non-reactive (option $4$) is the incorrect one.

**Subtopic:** Hybridisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q076_97b95b42_28102026.png?v=97b95b424f62)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** $\mathrm{PCl_5}$ is trigonal bipyramidal with equatorial bonds $120^\circ$ apart and axial bonds collinear, and the longer, weaker axial bonds are what make it reactive
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The axial bonds really are longer than the equatorial ones, so a student holding the plain $sp^3d$ picture in which all five bonds are alike reads this true line as the false one and marks it
- **Why:** This question requires stated facts about one named molecule graded one by one against a negated task, demonstrated by the stem "Identify the incorrect statement related to $\mathrm{PCl_5}$" with three true geometry claims printed beside one false reactivity claim.
- **Note:** The three wrong options are all true statements, so each is reached by reading the task as "pick the correct statement"; I put the trap on option 3 because it is the one a specific chemistry belief, the five bonds being equivalent, marks as false.
<!--/ecat-->

## Q77

Chemistry · physical · Ionic Equilibrium

Which will make basic buffer?

- (1) $50\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{NaOH}$ + $25\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{CH_3COOH}$
- (2) $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{CH_3COOH}$ + $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{NaOH}$
- **(3)** $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{HCl}$ + $200\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{NH_4OH}$
- (4) $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{HCl}$ + $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ $\mathrm{NaOH}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A basic buffer needs a weak base together with its salt of a strong acid, e.g. $\mathrm{NH_4OH} + \mathrm{NH_4Cl}$.
2. Option 3: $n(\mathrm{HCl}) = 100 \times 0.1 = 10\,\mathrm{mmol}$ and $n(\mathrm{NH_4OH}) = 200 \times 0.1 = 20\,\mathrm{mmol}$.
3. $\mathrm{HCl} + \mathrm{NH_4OH} \rightarrow \mathrm{NH_4Cl} + \mathrm{H_2O}$ consumes $10\,\mathrm{mmol}$ of $\mathrm{NH_4OH}$, leaving $10\,\mathrm{mmol}\ \mathrm{NH_4OH} + 10\,\mathrm{mmol}\ \mathrm{NH_4Cl}$, a basic buffer.
4. Option 1: $n(\mathrm{NaOH}) = 5\,\mathrm{mmol} > n(\mathrm{CH_3COOH}) = 2.5\,\mathrm{mmol}$, so excess strong base remains with $\mathrm{CH_3COONa}$; not a buffer.
5. Option 2 gives only $\mathrm{CH_3COONa}$ (exact neutralisation) and option 4 gives only $\mathrm{NaCl}$; neither is a buffer, so the answer is option $3$.

**Subtopic:** Buffer Solutions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q077_1915e383_28102026.png?v=1915e3837be8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A basic buffer needs a weak base together with its salt left over in the mixture, which means the weak base must be supplied in excess of the strong acid
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  A weak acid with a strong base is the buffer recipe and the resulting acetate solution is above pH 7, but $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ against $100\,\mathrm{mL}$ of $0.1\,\mathrm{M}$ is $10$ mmol against $10$ mmol, which leaves no acetic acid at all
- **Why:** This question requires the basic-buffer criterion applied to the millimoles each printed mixture supplies, demonstrated by the stem "Which will make basic buffer?" above four options that each print two volumes and two molarities.
- **Note:** The E1 pattern called this `statement_options` on option length, but the options are reagent mixtures rather than statements to judge, so the printed shape is a plain MCQ, the same shape as q072.
<!--/ecat-->

## Q78

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The major product of the following reaction is:

![printed figure: phthalic acid + ammonia ($\ce{NH3}$) →(strong heating)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_agent/q078_0b773946_28102026.svg?v=0b7739462303)

*phthalic acid + ammonia ($\ce{NH3}$) →[strong heating]*

![drawn: phthalic acid + ammonia ($\ce{NH3}$) →(strong heating)](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_question_8a7c49ce_28102026.svg?v=8a7c49cecf4f)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: phthalic acid `O=C(O)c1ccccc1C(=O)O` ![phthalic acid](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_question_s1_77f81faa_28102026.svg?v=77f81faadb17); ammonia `N` ![ammonia](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_question_s2_f296ea5a_28102026.svg?v=f296ea5af8a6)

- (1) 2-carbamoylbenzoic acid `NC(=O)c1ccccc1C(=O)O` ![2-carbamoylbenzoic acid](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_option_1_s1_a2283f76_28102026.svg?v=a2283f769630)
- **(2)** isoindoline-1,3-dione `O=C1NC(=O)c2ccccc21` ![isoindoline-1,3-dione](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_option_2_s1_02878c46_28102026.svg?v=02878c46a5a3)
- (3) 2-aminobenzoic acid `Nc1ccccc1C(=O)O` ![2-aminobenzoic acid](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_option_3_s1_3e7c7d2a_28102026.svg?v=3e7c7d2a513f)
- (4) benzene-1,2-diamine `Nc1ccccc1N` ![benzene-1,2-diamine](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/figures_drawn/q078_option_4_s1_07f24cbd_28102026.svg?v=07f24cbd9a74)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Phthalic acid reacts with $\mathrm{NH_3}$ to give the ammonium salt $\mathrm{C_6H_4(COO^-NH_4^+)(COOH)}$.
2. Heating removes $\mathrm{H_2O}$ to give phthalamic acid $\mathrm{C_6H_4(CONH_2)(COOH)}$.
3. Strong heating removes a second $\mathrm{H_2O}$ through intramolecular cyclisation, giving phthalimide $\mathrm{C_6H_4(CO)_2NH}$, which is option $2$.

**Subtopic:** Reactions with Ammonia and Decarboxylation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q078_4b6ffbcc_28102026.png?v=4b6ffbcc0682)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Phthalic acid with ammonia gives the ammonium salt, and strong heating drives off water to close the ring as phthalimide
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings, so there is nothing to read a route onto; I checked `options_en` for 1, 2, 3 and 4 and each is "", while the stem's own reaction survives in the figure record as phthalic acid + ammonia under strong heating
- **Why:** This question requires the product of a named reaction under a stated condition, demonstrated by the stem "The major product of the following reaction is:" above a scheme printing phthalic acid, ammonia and "strong heating" over the arrow.
- **Note:** The four options are empty in our record, so the key (2) cannot be matched to any printed structure and no trap or filler can be written; the stem and the reactant figure are intact, so the repair needed is the option set only. A reviewer holding the printed options should expect the pull to be on the un-cyclised intermediate, either the diamide (phthalamide) or the ammonium phthalate salt, since those are what a student reaches by stopping before the ring closes.
<!--/ecat-->

## Q79

Chemistry · inorganic · The p–Block Elements

Match the Xenon compounds in Column-I with its structure in Column-II and assign the correct code:

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{XeF_4}$ | (i) | pyramidal |
| (b) | $\mathrm{XeF_6}$ | (ii) | square planar |
| (c) | $\mathrm{XeOF_4}$ | (iii) | distorted octahedral |
| (d) | $\mathrm{XeO_3}$ | (iv) | square pyramidal |

- (1) (a) (i), (b) (ii), (c) (iii), (d) (iv)
- **(2)** (a) (ii), (b) (iii), (c) (iv), (d) (i)
- (3) (a) (ii), (b) (iii), (c) (i), (d) (iv)
- (4) (a) (iii), (b) (iv), (c) (i), (d) (ii)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\mathrm{XeF_4}$: 4 bond pairs + 2 lone pairs ($sp^3d^2$) gives square planar, so (a) $\to$ (ii).
2. $\mathrm{XeF_6}$: 6 bond pairs + 1 lone pair ($sp^3d^3$) gives distorted octahedral, so (b) $\to$ (iii).
3. $\mathrm{XeOF_4}$: 5 bond pairs + 1 lone pair ($sp^3d^2$) gives square pyramidal, so (c) $\to$ (iv).
4. $\mathrm{XeO_3}$: 3 bond pairs + 1 lone pair ($sp^3$) gives pyramidal, so (d) $\to$ (i).
5. The match (a)(ii), (b)(iii), (c)(iv), (d)(i) is option $2$.

**Subtopic:** Important Compounds of Xenon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q079_16611bfe_28102026.png?v=16611bfe59bf)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The shape of each xenon compound follows from counting its bond pairs and lone pairs: XeF4 square planar, XeF6 distorted octahedral, XeOF4 square pyramidal, XeO3 pyramidal
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The two shape names that share the word 'pyramidal' are exchanged - XeOF4 is given (i) pyramidal and XeO3 (iv) square pyramidal - while the XeF4 and XeF6 rows are kept right.
- **Why:** This question requires each formula's bond and lone pairs turned into a shape, demonstrated by Column I printing 'XeF4', 'XeF6', 'XeOF4' and 'XeO3' against four shape names in Column II.
- **Note:** look_alike_term rather than nearby_fact: I applied the swap test by replacing 'pyramidal' and 'square pyramidal' with two unlike names, and the swap in option 3 has nothing left to run on, so the likeness of the two names is what carries it.
<!--/ecat-->

## Q80

Chemistry · inorganic · The D- and F-Block Elements – Practice

The manganate and permanganate ions are tetrahedral, due to :

- **(1)** The $\pi$-bonding involves overlap of p-orbitals of oxygen with d-orbitals of manganese
- (2) There is no $\pi$-bonding
- (3) The $\pi$-bonding involves overlap of p-orbitals of oxygen with p-orbitals of manganese
- (4) The $\pi$-bonding involves overlap of d-orbitals of oxygen with d-orbitals of manganese

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In $\mathrm{MnO_4^{2-}}$ and $\mathrm{MnO_4^{-}}$ the $\sigma$ framework around Mn is tetrahedral, and the $\pi$-bonds arise from overlap of filled oxygen $2p$ orbitals with empty manganese $3d$ orbitals ($p\pi$-$d\pi$ bonding), which is option $1$.

**Subtopic:** Potassium Permanganate (KMnO4) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q080_1f2950df_28102026.png?v=1f2950df470f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In $\mathrm{MnO_4^{2-}}$ and $\mathrm{MnO_4^{-}}$ the $\pi$ bonding is $p\pi$–$d\pi$: filled oxygen $p$ orbitals overlap sideways with vacant manganese $d$ orbitals
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  $p$–$p$ sideways overlap is the $\pi$ bond carried over from $\mathrm{C{=}C}$ and $\mathrm{C{=}O}$, so a student who knows "$\pi$ bonds are made by $p$ orbitals" keeps both partners $p$ and changes only the atom names
- **Why:** This question requires the stated reason behind a granted structural fact, demonstrated by the stem reading "are tetrahedral, due to :" with the shape given and only the cause left to pick.
<!--/ecat-->

## Q81

Chemistry · inorganic · The p–Block Elements

Which of the following species is not stable?

- (1) $\mathrm{[SiF_6]^{2-}}$
- (2) $\mathrm{[GeCl_6]^{2-}}$
- (3) $\mathrm{[Sn(OH)_6]^{2-}}$
- **(4)** $\mathrm{[SiCl_6]^{2-}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Group 14 elements beyond carbon can expand coordination to six using $d$ orbitals, forming $\mathrm{[MX_6]^{2-}}$ species.
2. $\mathrm{Si}$ is small and $\mathrm{F}$ is small, so six $\mathrm{F}$ fit around $\mathrm{Si}$: $\mathrm{[SiF_6]^{2-}}$ is stable.
3. $\mathrm{Ge}$ and $\mathrm{Sn}$ are larger, so $\mathrm{[GeCl_6]^{2-}}$ and $\mathrm{[Sn(OH)_6]^{2-}}$ are stable.
4. Six large $\mathrm{Cl}$ atoms cannot be accommodated around small $\mathrm{Si}$ (steric repulsion, weak lone-pair interaction), so $\mathrm{[SiCl_6]^{2-}}$ is not stable, which is option $4$.

**Subtopic:** Hydrides, Halides, Oxides, Silicones of Group 14 · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q081_8e826798_28102026.png?v=8e82679860ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A group-14 centre can hold six ligands only if it is large enough for them: silicon takes six small fluorides but not six chlorides, while the bigger germanium and tin can
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who remembers that one hexachloro species of group 14 is unknown but not which element it belongs to takes germanium, the neighbour printed beside silicon in the same group
- **Why:** This question requires the stated fact about which group-14 complex ion is not known, demonstrated by the stem "Which of the following species is not stable?" with four ions and no size data printed to work from.
- **Note:** On the §5.1 swap test: replacing germanium with an unlike element name leaves the trap standing, because what carries the student is germanium's position beside silicon in group 14 and the shared hexachloro formula, not any likeness between the words. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q82

Chemistry · physical · Electrochemistry

For a cell involving one electron $E^{\circ}_{\mathrm{cell}} = 0.59\,\mathrm{V}$ at $298\,\mathrm{K}$, the equilibrium constant for the cell reaction is : $\left[\text{Given that } \dfrac{2.303\,RT}{F} = 0.059\,\mathrm{V} \text{ at } T = 298\,\mathrm{K}\right]$

- (1) $1.0 \times 10^{2}$
- (2) $1.0 \times 10^{5}$
- **(3)** $1.0 \times 10^{10}$
- (4) $1.0 \times 10^{30}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. At equilibrium, $E^{\circ}_{\mathrm{cell}} = \frac{2.303\,RT}{nF}\log K = \frac{0.059}{n}\log K$.
2. $\log K = \frac{n E^{\circ}_{\mathrm{cell}}}{0.059} = \frac{1 \times 0.59}{0.059} = 10$.
3. $K = 10^{10} = 1.0 \times 10^{10}$, which is option $3$.

**Subtopic:** Nernst Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q082_9cc6066e_28102026.png?v=9cc6066ec74e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At equilibrium the cell does no work, so $E^\circ_{\mathrm{cell}} = \frac{0.059}{n}\log K$, and with $n=1$ the equilibrium constant follows from one division
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem prints both numbers the division needs, $n=1$ and $\frac{2.303RT}{F}=0.059$, so $\log K = 0.59/0.059 = 10$ is forced in one step; I tested the misuses that usually produce a printed option and none lands on $10^{2}$, $10^{5}$ or $10^{30}$ -- putting $n$ in the denominator still gives $10$, taking the slope as $0.0295$ gives $10^{20}$, and swapping $\log$ for $\ln$ gives $2.2\times10^{4}$, which is not printed
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by the stem supplying $E^\circ_{\mathrm{cell}} = 0.59\,\mathrm{V}$, "one electron" and the bracketed $\frac{2.303RT}{F} = 0.059\,\mathrm{V}$.
- **Note:** The three wrong options are a spread of exponents, 2, 5 and 30, rather than the results of named wrong operations. $10^{30}$ is what $n=3$ would give, but the stem states "a cell involving one electron" and nothing printed points at three, so that is arithmetic that reaches the option rather than a route a prepared student has a reason to walk.
<!--/ecat-->

## Q83

Chemistry · inorganic · The s-Block Elements

Which of the following is an amphoteric hydroxide?

- (1) $\mathrm{Sr(OH)_2}$
- (2) $\mathrm{Ca(OH)_2}$
- (3) $\mathrm{Mg(OH)_2}$
- **(4)** $\mathrm{Be(OH)_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Group 2 hydroxides become more basic down the group; $\mathrm{Mg(OH)_2}$, $\mathrm{Ca(OH)_2}$ and $\mathrm{Sr(OH)_2}$ are basic, while $\mathrm{Be(OH)_2}$ dissolves in both acid and alkali ($\mathrm{Be(OH)_2 + 2OH^- \rightarrow [Be(OH)_4]^{2-}}$), so it is amphoteric, which is option $4$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q083_4674ba5a_28102026.png?v=4674ba5a889c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Beryllium is the anomalous first member of group 2: its oxide and hydroxide dissolve in both acid and alkali, while the hydroxides below it are purely basic and get more basic down the group
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  $\mathrm{Mg(OH)_2}$ is printed next to beryllium as the weakly basic, sparingly soluble hydroxide, so a student who remembers "the top of group 2 is the odd one" and reads weak basicity as half-acidic stops one place too low
- **Why:** This question requires one stated property of one named compound, demonstrated by the stem "Which of the following is an amphoteric hydroxide?" with four group-2 hydroxides and no criterion printed to apply.
<!--/ecat-->

## Q84

Chemistry · physical · States of Matter

A gas at $350\,\mathrm{K}$ and $15\,\mathrm{bar}$ has molar volume 20 percent smaller than that for an ideal gas under the same conditions. The correct option about the gas and its compressibility factor $(Z)$ is :

- (1) $Z > 1$ and attractive forces are dominant
- (2) $Z > 1$ and repulsive forces are dominant
- **(3)** $Z < 1$ and attractive forces are dominant
- (4) $Z < 1$ and repulsive forces are dominant

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $Z = \frac{pV_m}{RT} = \frac{V_{m,\text{real}}}{V_{m,\text{ideal}}}$.
2. Molar volume is 20% smaller, so $V_{m,\text{real}} = 0.8\,V_{m,\text{ideal}}$ and $Z = 0.8 < 1$.
3. $Z < 1$ means the gas is more compressible than an ideal gas, so attractive forces are dominant, which is option $3$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q084_a7e23a7d_28102026.png?v=a7e23a7d6f7d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $Z = V_{\mathrm{real}}/V_{\mathrm{ideal}}$, so a molar volume smaller than ideal means $Z<1$, and $Z<1$ is the signature of attractions pulling the molecules closer than an ideal gas would sit
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Taking the molar volume as 20 percent smaller gives $Z = 0.8 < 1$, which this option has right, and then reading "closer together" as "pushing on each other" attaches repulsion to it
- **Why:** This question requires a definition and its sign convention applied to a stated comparison, demonstrated by the stem printing "molar volume 20 percent smaller than that for an ideal gas" and asking for "the correct option about the gas and its compressibility factor $(Z)$".
- **Note:** Each option is two claims joined by "and", a $Z$ inequality plus a dominant force, and half right scores nothing, so the answer has two halves even though "respectively" is not printed; that is why qtype is two_part and not the pattern's `statement_options`.
<!--/ecat-->

## Q85

Chemistry · physical · The Solid State

A compound is formed by cation C and anion A. The anions form hexagonal close packed (hcp) lattice and the cations occupy $75\%$ of octahedral voids. The formula of the compound is :

- (1) $\mathrm{C_2A_3}$
- (2) $\mathrm{C_3A_2}$
- **(3)** $\mathrm{C_3A_4}$
- (4) $\mathrm{C_4A_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In an hcp lattice of $N$ anions there are $N$ octahedral voids.
2. Cations occupy $75\%$ of them: number of C $= 0.75N = \frac{3}{4}N$.
3. $\mathrm{C:A} = \frac{3}{4}N : N = 3:4$.
4. The formula is $\mathrm{C_3A_4}$, which is option $3$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q085_009f4d62_28102026.png?v=009f4d621081)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A close-packed lattice of N spheres has N octahedral voids and 2N tetrahedral ones, so the formula follows from the fraction of the named void type that is filled
- **Trap:** **old ncert answer** (`old_ncert_answer`) — the paper altered one value in an NCERT example or line, and NCERT's own answer is printed as a distractor — option 4  
  $\mathrm{C_4A_3}$ is the answer to NCERT's own exercise, where the cations fill $2/3$ of the TETRAHEDRAL voids: $\tfrac{2}{3}\times 2N = \tfrac{4}{3}N$ gives $4:3$, while this paper has changed both values to $75\%$ of the OCTAHEDRAL voids, which gives $0.75N$ and so $3:4$
- **Why:** This question requires a formula computed from the stem's own figures, demonstrated by the stem printing "hexagonal close packed (hcp) lattice" and "the cations occupy $75\%$ of octahedral voids".
- **Note:** The four options form a complete grid of the two values that were changed: fraction $3/4$ or $2/3$, crossed with octahedral ($N$) or tetrahedral ($2N$) voids. $3/4$ with octahedral is the key, $3/4$ with tetrahedral is option 2, $2/3$ with octahedral is option 1, and $2/3$ with tetrahedral is option 4, which is the published answer to the NCERT exercise.
<!--/ecat-->

## Q86

Chemistry · physical · Thermodynamics

In which case change in entropy is negative?

- (1) Evaporation of water
- (2) Expansion of a gas at constant temperature
- (3) Sublimation of solid to gas
- **(4)** $\mathrm{2H(g) \rightarrow H_2(g)}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Evaporation (liquid $\rightarrow$ gas) increases disorder, so $\Delta S > 0$.
2. Isothermal expansion of a gas increases volume: $\Delta S = nR\ln\frac{V_2}{V_1} > 0$.
3. Sublimation (solid $\rightarrow$ gas) increases disorder, so $\Delta S > 0$.
4. For $\mathrm{2H(g) \rightarrow H_2(g)}$, $\Delta n_g = 1 - 2 = -1$, so the system becomes more ordered and $\Delta S < 0$, which is option $4$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q086_d73c4342_28102026.png?v=d73c43427b0e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Entropy falls only when the freedom of the particles falls, which among these cases happens where two moles of gaseous atoms combine into one mole of molecules
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Evaporation takes heat in, and a student who turns that into a falling entropy has computed the sign for the SURROUNDINGS, where $\Delta S = -\Delta H/T$ is indeed negative, and read it as the answer
- **Why:** This question requires one rule about disorder applied case by case, demonstrated by the stem "In which case change in entropy is negative?" above three expansions or phase changes and one combination, $\mathrm{2H(g)\rightarrow H_2(g)}$.
<!--/ecat-->

## Q87

Chemistry · physical · Structure of Atom

Which of the following series of transitions in the spectrum of hydrogen atom falls in visible region?

- (1) Lyman series
- **(2)** Balmer series
- (3) Paschen series
- (4) Brackett series

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Lyman series ends at $n_f = 1$: ultraviolet; Paschen ($n_f = 3$) and Brackett ($n_f = 4$) are infrared.
2. Balmer series ends at $n_f = 2$: $\frac{1}{\lambda} = R\left(\frac{1}{2^2} - \frac{1}{n^2}\right)$ gives $\lambda \approx 365$ to $656\,\text{nm}$, the visible region, which is option $2$.

**Subtopic:** Hydrogen Spectrum and Spectral Series · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q087_77c07a0b_28102026.png?v=77c07a0bccc6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only the hydrogen transitions ending at $n=2$, the Balmer series, have photon energies that fall in the $400$–$700\,\mathrm{nm}$ visible window; $n=1$ lands in the ultraviolet and $n\ge 3$ in the infrared
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Lyman is the first row of the printed table of series, so a student who remembers that one named series is the visible one and reaches for the first entry lands here instead of on the second row
- **Why:** This question requires one stated fact pairing a named series with a spectral region, demonstrated by the stem "falls in visible region?" above four series names with no wavelengths or $n$ values printed.
<!--/ecat-->

## Q88

Chemistry · inorganic · Hydrogen

The method used to remove temporary hardness of water is :

- (1) Calgon's method
- **(2)** Clark's method
- (3) Ion-exchange method
- (4) Synthetic resins method

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Temporary hardness comes from the soluble bicarbonates $\mathrm{Ca(HCO_3)_2}$ and $\mathrm{Mg(HCO_3)_2}$.
2. In Clark's method slaked lime is added: $\mathrm{Ca(HCO_3)_2 + Ca(OH)_2 \rightarrow 2CaCO_3\downarrow + 2H_2O}$ and $\mathrm{Mg(HCO_3)_2 + 2Ca(OH)_2 \rightarrow 2CaCO_3\downarrow + Mg(OH)_2\downarrow + 2H_2O}$, so the bicarbonate hardness is removed.
3. Calgon's method, ion-exchange (zeolite) and synthetic resins are the methods NCERT gives for removing permanent hardness, so the answer is option $2$.

**Subtopic:** Hardness of Water · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q088_5f26493c_28102026.png?v=5f26493c9c8a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Temporary hardness is bicarbonate hardness, so it is removed by boiling or by Clark's method, in which a calculated amount of lime precipitates the bicarbonates as carbonate
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Calgon's method is the other person-named softening method printed in the same section, so a student who recalls two named methods but not which hardness each is filed under takes the neighbour in the list
- **Why:** This question requires one stated pairing of a named method with a named kind of hardness, demonstrated by the stem "The method used to remove temporary hardness of water is :" above four method names with no chemistry printed to work from.
- **Note:** On the §5.1 swap test: replacing "Calgon's method" with "sodium hexametaphosphate treatment", an unlike name for the same thing, leaves the trap standing, because the pull is that it is the other named method in the same printed list. So nearby_fact rather than look_alike_term, even though the two names both begin with C. The verdict records a real doubt: resin and ion-exchange methods do in practice soften water carrying bicarbonate hardness, so options 3 and 4 are defensible on the chemistry; the key rests on the textbook's split of the methods between permanent and temporary, and the tag follows the printed key.
<!--/ecat-->

## Q89

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Which one is malachite from the following?

- (1) $\mathrm{CuFeS_2}$
- (2) $\mathrm{Cu(OH)_2}$
- (3) $\mathrm{Fe_3O_4}$
- **(4)** $\mathrm{CuCO_3.Cu(OH)_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Malachite is the green copper ore basic copper carbonate, $\mathrm{CuCO_3 \cdot Cu(OH)_2}$, while $\mathrm{CuFeS_2}$ is copper pyrites, $\mathrm{Fe_3O_4}$ is magnetite and $\mathrm{Cu(OH)_2}$ is not an ore, so the answer is option $4$.

**Subtopic:** Occurrence of Metals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q089_81a3a93e_28102026.png?v=81a3a93ed055)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Malachite is the basic carbonate ore of copper, $\mathrm{CuCO_3\cdot Cu(OH)_2}$, so its formula carries both a carbonate and a hydroxide on copper
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Malachite and magnetite differ by two letters, and $\mathrm{Fe_3O_4}$ is magnetite, so a student who has the ore names stored by sound answers the question the name sounds like
- **Why:** This question requires one stated pairing of an ore name with its formula, demonstrated by the stem "Which one is malachite from the following?" above four formulae with no property printed to reason from.
- **Note:** The §5.1 swap test decides this one the opposite way to q088: replace "magnetite" with an unlike mineral name and nothing pulls a copper question toward an iron oxide, so here the resemblance between the two words is what carries the student, which is look_alike_term.
<!--/ecat-->

## Q90

Chemistry · organic · Amines

The correct order of the basic strength of methyl substituted amines in aqueous solution is :

- **(1)** $\mathrm{(CH_3)_2NH > CH_3NH_2 > (CH_3)_3N}$
- (2) $\mathrm{(CH_3)_3N > CH_3NH_2 > (CH_3)_2NH}$
- (3) $\mathrm{(CH_3)_3N > (CH_3)_2NH > CH_3NH_2}$
- (4) $\mathrm{CH_3NH_2 > (CH_3)_2NH > (CH_3)_3N}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Inductive (+I) effect alone would give $\mathrm{(CH_3)_3N > (CH_3)_2NH > CH_3NH_2}$, as seen in the gas phase.
2. In aqueous solution the protonated amine is stabilised by H-bonding with water, which is greatest for $\mathrm{CH_3NH_3^+}$ (three N-H) and least for $\mathrm{(CH_3)_3NH^+}$ (one N-H); steric hindrance to solvation also rises with substitution.
3. Combining these effects for methyl groups gives $\mathrm{(CH_3)_2NH > CH_3NH_2 > (CH_3)_3N}$, which is option $1$.

**Subtopic:** Chemical Reactions of Amines (Basicity, Alkylation and Acylation) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q090_ff58be9e_28102026.png?v=ff58be9ef066)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** In water the basic strength of the methylamines is set by two opposing effects, the electron-releasing methyls and the loss of hydration and room around nitrogen, which leaves the secondary amine strongest and the tertiary weakest
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  $\mathrm{(CH_3)_3N > (CH_3)_2NH > CH_3NH_2}$ is the order the inductive effect alone gives, and it is the right answer once the stem's "in aqueous solution" is dropped, because in the gas phase basicity does rise steadily with each methyl added
- **Why:** This question requires a trend arranged over three named compounds under a printed condition, demonstrated by the stem asking for "the correct order of the basic strength of methyl substituted amines in aqueous solution".
<!--/ecat-->

## Q91

Biology · botany · Biodiversity and Conservation

The Earth Summit held in Rio de Janeiro in 1992 was called

- (1) to reduce $\mathrm{CO_2}$ emissions and global warming
- **(2)** for conservation of biodiversity and sustainable utilization of its benefits
- (3) to assess threat posed to native species by invasive weed species
- (4) for immediate steps to discontinue use of CFCs that were damaging the ozone layer

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The historic Convention on Biological Diversity (the Earth Summit, Rio de Janeiro, 1992) called on all nations to conserve biodiversity and use its benefits sustainably, which is option $2$.

**Subtopic:** How Do We Conserve Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q091_78a9f8a2_28102026.png?v=78a9f8a2f623)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The 1992 Rio Earth Summit is the convention on biological diversity: conserving biodiversity and sharing the benefits of its sustainable use
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Cutting $\mathrm{CO_2}$ emissions is the aim of the climate agreement printed a few pages away in the same environmental run, and a student who has the Rio summit filed as the big climate meeting of 1992 takes that aim for this one
- **Why:** This question requires the stated purpose of a dated event, demonstrated by "The Earth Summit held in Rio de Janeiro in 1992 was called" with "for conservation of biodiversity and sustainable utilization of its benefits" as the printed aim.
- **Note:** No filler here, and that is a finding about the option set: all four options are real environmental aims drawn from the same two chapters, so nothing is struck out by a securely known fact and each has its own route. nearby_fact was preferred to answers_other_question because what carries the student is the run of agreements printed together, and the option as printed is not a true statement about THIS summit. E1 called the shape statement_options; the stem is a sentence completion rather than statements to be judged, so mcq is recorded.
<!--/ecat-->

## Q92

Biology · zoology · Human Health and Disease

Colostrum the yellowish fluid, secreted by mother during the initial days of lactation is very essential to impart immunity to the new born infants because it contains :

- (1) Natural killer cells
- (2) Monocytes
- (3) Macrophages
- **(4)** Immunoglobulin A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Colostrum secreted in the first days of lactation contains a lot of antibodies, mainly $\mathrm{IgA}$, which give the newborn passive immunity, so the answer is option $4$.

**Subtopic:** Active and Passive Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q092_fd215be9_28102026.png?v=fd215be97201)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Colostrum gives the newborn passive immunity because it is rich in the antibody IgA
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option for a route: all three are co-ordinate cells of the immune chapter, and the colostrum line names antibodies alone, so nothing printed brings a macrophage, a monocyte or a natural killer cell nearer to colostrum than the other two, and no one of the three can be named as the option a route lands on
- **Why:** This question requires the stated reason colostrum protects an infant, demonstrated by "is very essential to impart immunity to the new born infants because it contains :".
- **Note:** Recorded as no_trap rather than forcing a pick: the three wrong options form an undifferentiated set of immune cells and choosing one of them would assert a preference the printed question does not create. The device the question does carry is at the level of the set — the answer is a molecule while every distractor is a cell — which is a property of the option set rather than a route to any single option. asks is reason_line because the stem's own "because" asks for the cause of a granted fact.
<!--/ecat-->

## Q93

Biology · botany · Anatomy of Flowering Plants

Grass leaves curl inwards during very dry weather. Select the most appropriate reason from the following :

- (1) Closure of stomata
- **(2)** Flaccidity of bulliform cells
- (3) Shrinkage of air spaces in spongy mesophyll
- (4) Tyloses in vessels

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In grass (monocot) leaves, large empty colourless bulliform cells in the adaxial epidermis lose water and become flaccid during water stress, so the leaf curls inwards, which is option $2$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q093_ae496cf0_28102026.png?v=ae496cf006fc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Bulliform cells in a grass leaf go flaccid when water is short, and that is what rolls the leaf inwards
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Stomatal closure is the response to dry weather the chapter states, so a student who reads the stem as asking what happens in drought answers with it; it conserves water but moves no part of the leaf, so it cannot curl the blade
- **Why:** This question requires the stated cause of a described observation, demonstrated by "Grass leaves curl inwards during very dry weather. Select the most appropriate reason from the following".
<!--/ecat-->

## Q94

Biology · both · Cell: The Unit of Life

The shorter and longer arms of a submetacentric chromosome are referred to as

- (1) s-arm and l-arm respectively
- **(2)** p-arm and q-arm respectively
- (3) q-arm and p-arm respectively
- (4) m-arm and n-arm respectively

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. By standard chromosome nomenclature the shorter arm is the $p$-arm and the longer arm is the $q$-arm, so the answer is option $2$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q094_af37dec7_28102026.png?v=af37dec76e31)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A chromosome's short arm is called p and its long arm q, measured from the centromere
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A student who recalls that the two arms are called p and q, but not which letter is the short one, reads the pair onto the stem's "shorter and longer" the other way round and gives q to the short arm
- **Why:** This question requires the agreed names of the two chromosome arms in the stated order, demonstrated by "The shorter and longer arms of a submetacentric chromosome are referred to as".
- **Note:** E1 called the shape statement_options; the options are notation pairs completing the stem, not statements to be judged, so mcq is recorded. The "respectively" is what makes the reversed pair a separate option rather than the same answer.
<!--/ecat-->

## Q95

Biology · botany · Respiration in Plants

Respiratory Quotient (RQ) value of tripalmitin is

- (1) 0.9
- **(2)** 0.7
- (3) 0.07
- (4) 0.09

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $RQ = \frac{\text{volume of } CO_2 \text{ evolved}}{\text{volume of } O_2 \text{ consumed}}$.
2. Oxidation of tripalmitin: $2(C_{51}H_{98}O_6) + 145\,O_2 \rightarrow 102\,CO_2 + 98\,H_2O + \text{energy}$.
3. $RQ = \frac{102\,CO_2}{145\,O_2} \approx 0.7$, which is option $2$.

**Subtopic:** The Respiratory Balance Sheet, Amphibolic Pathway and Respiratory Quotient · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q095_11cdb0a6_28102026.png?v=11cdb0a68428)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** RQ is the ratio of $\mathrm{CO_2}$ given out to $\mathrm{O_2}$ used, and for a fat such as tripalmitin it is about 0.7
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  0.9 is the RQ the same passage gives for proteins, printed beside the figure for fats, and a student who remembers that the list holds a 0.7 and a 0.9 but not which substrate owns which takes the neighbouring value
- **Why:** This question requires a stated value for a named substrate, demonstrated by "Respiratory Quotient (RQ) value of tripalmitin is".
- **Note:** The value is also derivable from the printed oxidation equation for tripalmitin ($102\,\mathrm{CO_2}$ released against $145\,\mathrm{O_2}$ used), but the options are the remembered figures of the RQ list rather than arithmetic near-misses, which is why the pull is the protein value and not a slip. Two of the three wrong options are fillers because they are the same two figures with the decimal shifted; this is recorded rather than dressed up as two routes.
<!--/ecat-->

## Q96

Biology · botany · Microbes in Human Welfare

Which of the following is a commercial blood cholesterol lowering agent?

- (1) Cyclosporin A
- **(2)** Statin
- (3) Streptokinase
- (4) Lipases

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statins, from the yeast $Monascus\ purpureus$, competitively inhibit the enzyme of cholesterol synthesis, so they lower blood cholesterol; Cyclosporin A is an immunosuppressant, Streptokinase a clot buster and Lipases are used in detergents, so the answer is option $2$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q096_24fec181_28102026.png?v=24fec18163c4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Statins, from the yeast Monascus purpureus, are the microbial product commercialised as a blood-cholesterol lowering agent
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Cyclosporin A is named in the sentence immediately before statins in the same list of commercialised microbial products, and a student who remembers the list but not which product has which use takes the neighbour
- **Why:** This question requires which named microbial product has a stated use, demonstrated by "Which of the following is a commercial blood cholesterol lowering agent?".
- **Note:** No filler, and that is a property of the option set: all four options are bioactive molecules from the same passage, so no securely known fact strikes any of them out and each carries its own route — adjacency in the passage, the fat-splitting name, and the circulatory use.
<!--/ecat-->

## Q97

Biology · zoology · Digestion and Absorption

Match the following structures with their respective location in organs

| List-I | | List-II | |
|---|---|---|---|
| (a) | Crypts of Lieberkuhn | (i) | Pancreas |
| (b) | Glisson's Capsule | (ii) | Duodenum |
| (c) | Islets of Langerhans | (iii) | Small intestine |
| (d) | Brunner's Glands | (iv) | Liver |

- (1) (iii) (i) (ii) (iv)
- (2) (ii) (iv) (i) (iii)
- **(3)** (iii) (iv) (i) (ii)
- (4) (iii) (ii) (i) (iv)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Crypts of Lieberkuhn are intestinal glands lying between the villi of the small intestine, so $(a) \rightarrow (iii)$.
2. Glisson's capsule is the connective tissue sheath covering the hepatic lobules of the liver, so $(b) \rightarrow (iv)$.
3. Islets of Langerhans are the endocrine part of the pancreas, so $(c) \rightarrow (i)$.
4. Brunner's glands are submucosal glands of the duodenum, so $(d) \rightarrow (ii)$.
5. The sequence $(iii)\,(iv)\,(i)\,(ii)$ matches option $3$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q097_4ae81394_28102026.png?v=4ae813943c33)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named gut or gland structure has one organ it is described in: crypts of Lieberkuhn in the small intestine, Glisson's capsule in the liver, islets of Langerhans in the pancreas, Brunner's glands in the duodenum
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The duodenum is the first stretch of the small intestine, so a student holding the two labels as one region lets Brunner's glands take "Small intestine" and the crypts take "Duodenum"; with each location used once, NCERT's crypts go with the small intestine and Brunner's glands with the duodenum
- **Why:** This question requires each named structure placed in the organ the text states for it, demonstrated by "Match the following structures with their respective location in organs".
- **Note:** Option 2's two pairings are each true at a coarser anatomical grain, which is exactly what makes it the trap; the key is not arguable because the four locations are used once each, so giving Brunner's glands the whole small intestine forces the crypts into the duodenum, which contradicts the text's own placement.
<!--/ecat-->

## Q98

Biology · botany · Biodiversity and Conservation

Which of the following is the most important cause for animals and plants being driven to extinction?

- **(1)** Habitat loss and fragmentation
- (2) Drought and floods
- (3) Economic exploitation
- (4) Alien species invasion

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Among the causes of biodiversity loss (habitat loss and fragmentation, over-exploitation, alien species invasions, co-extinctions), habitat loss and fragmentation is the most important cause of extinction, which is option $1$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q098_72abcd38_28102026.png?v=72abcd381e6a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Habitat loss and fragmentation is the first and largest of the four printed causes of extinction; alien invasion and over-exploitation stand beside it as smaller ones
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Alien species invasion is one of the four causes the chapter names, and it is the one carried by its examples, the Nile perch and the water hyacinth, so a student who checks only whether the option is a cause stops before the stem's 'most important'
- **Why:** This question requires the ranking the chapter prints among its causes, demonstrated by the stem's 'the most important cause' with three other true causes standing in the options.
- **Note:** answers_other_question rather than nearby_fact: option 4 is itself one of the printed causes and fails only the stem's superlative, which is the case the retired trap list maps under not_the_superlative. Option 1 reads as two items, but 'habitat loss and fragmentation' is the single cause as the chapter names it and the other options are single causes, so this is not a pair question.
<!--/ecat-->

## Q99

Biology · zoology · Neural Control and Coordination

Which part of the brain is responsible for thermoregulation?

- (1) Cerebrum
- **(2)** Hypothalamus
- (3) Corpus callosum
- (4) Medulla oblongata

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The hypothalamus holds the centres that regulate body temperature (along with hunger and thirst), so the answer is option $2$.

**Subtopic:** Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q099_8c9dd526_28102026.png?v=8c9dd526e203)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Body temperature, hunger and thirst are controlled by hypothalamic centres; the medulla holds the respiratory and cardiovascular ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The medulla is carried as the seat of the involuntary housekeeping functions -- breathing, heart rate, gastric secretion -- and temperature control is filed under the same heading
- **Why:** This question requires one named brain part matched to a printed function, demonstrated by the stem's 'responsible for thermoregulation' set against four parts of the brain.
<!--/ecat-->

## Q100

Biology · zoology · Animal Kingdom

Consider following features

Select the correct option of animal groups which possess all the above characteristics

- **((a))** Organ system level of organisation
- **((b))** Bilateral symmetry
- **((c))** True coelomates with segmentation of body

- **(1)** Annelida, Arthropoda and Chordata
- (2) Annelida, Arthropoda and Mollusca
- (3) Arthropoda, Mollusca and Chordata
- (4) Annelida, Mollusca and Chordata

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. All three features (organ system level, bilateral symmetry, true coelom with segmentation) must hold for each group named in the option.
2. Annelida: organ system level, bilateral, coelomate, metamerically segmented, so it qualifies.
3. Arthropoda: organ system level, bilateral, coelomate, segmented body, so it qualifies.
4. Chordata: organ system level, bilateral, coelomate, segmented (e.g. myotomes, vertebral column), so it qualifies.
5. Mollusca: organ system level, bilateral, coelomate but unsegmented, so it fails feature (c).
6. Options $2$, $3$ and $4$ each include Mollusca, so the answer is option $1$ (Annelida, Arthropoda and Chordata).

**Subtopic:** Basis of Classification · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q100_e8f29538_28102026.png?v=e8f29538700f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Segmentation of the body is what separates Annelida, Arthropoda and Chordata from the other organ-system-level, bilaterally symmetrical coelomates
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Annelida and Arthropoda are the two segmented phyla named first, and Mollusca passes the organ-system and bilateral-symmetry lines, so the third place goes to Mollusca and its unsegmented body is never tested.
- **Why:** This question requires the stated features of each named phylum, demonstrated by '(c) True coelomates with segmentation of body' being the one printed line that Mollusca fails.
- **Note:** compare was ruled out for asks: the four options are sets of phyla, but one printed fact - whether the phylum is segmented - settles the question, so nothing here asks for two similar concepts to be held apart.
<!--/ecat-->

## Q101

Biology · zoology · Structural Organisation in Animals

Select the correct sequence of organs in the alimentary canal of cockroach starting from mouth

- **(1)** Pharynx $\rightarrow$ Oesophagus $\rightarrow$ Crop $\rightarrow$ Gizzard $\rightarrow$ Ileum $\rightarrow$ Colon $\rightarrow$ Rectum
- (2) Pharynx $\rightarrow$ Oesophagus $\rightarrow$ Gizzard $\rightarrow$ Crop $\rightarrow$ Ileum $\rightarrow$ Colon $\rightarrow$ Rectum
- (3) Pharynx $\rightarrow$ Oesophagus $\rightarrow$ Gizzard $\rightarrow$ Ileum $\rightarrow$ Crop $\rightarrow$ Colon $\rightarrow$ Rectum
- (4) Pharynx $\rightarrow$ Oesophagus $\rightarrow$ Ileum $\rightarrow$ Crop $\rightarrow$ Gizzard $\rightarrow$ Colon $\rightarrow$ Rectum

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The mouth opens into the pharynx, which leads to the oesophagus; the oesophagus widens into the sac-like crop, which is followed by the gizzard (proventriculus), then the midgut, and the hindgut runs ileum $\rightarrow$ colon $\rightarrow$ rectum. This is option $1$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q101_a40e8ac9_28102026.png?v=a40e8ac9df4e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The cockroach gut runs pharynx, oesophagus, crop for storage, gizzard for grinding, then the ileum, colon and rectum
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Grinding comes to mind as the first thing done to food, so the gizzard is placed ahead of the crop while the rest of the printed order is left untouched
- **Why:** This question requires the printed sequence of the canal, demonstrated by the stem's 'correct sequence of organs in the alimentary canal of cockroach starting from mouth' and by option 2 differing from the key at one adjacency only.
- **Note:** half_right, not reversed: rule 5.1 excludes one swapped pair inside a longer order from reversed, and this option has six of its seven places right with the crop and gizzard exchanged.
<!--/ecat-->

## Q102

Biology · botany · Environmental Issues

Which of the following pairs of gases is mainly responsible for green house effect?

- (1) Ozone and Ammonia
- (2) Oxygen and Nitrogen
- (3) Nitrogen and Sulphur dioxide
- **(4)** Carbon dioxide and Methane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The main greenhouse gases are $\mathrm{CO_2}$ and $\mathrm{CH_4}$ (with CFCs and $\mathrm{N_2O}$), so the pair is Carbon dioxide and Methane, option $4$.

**Subtopic:** Greenhouse Effect and Global Warming · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q102_9bb5c38f_28102026.png?v=9bb5c38fb77e)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Carbon dioxide and methane are the two largest contributors to the greenhouse effect; ozone belongs to the depletion story, not to this one
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Ozone depletion is the section printed beside global warming, so a student who holds the two atmospheric problems as one reaches for the gas the other problem is told through
- **Why:** This question requires the two gases named as the main contributors, demonstrated by the stem asking which of the 'pairs of gases is mainly responsible for green house effect'.
- **Note:** Recorded as two_part because the stem asks for a pair and each option is a pair of gases accepted or rejected whole.
<!--/ecat-->

## Q103

Biology · zoology · Locomotion and Movement

Which of the following muscular disorders is inherited?

- (1) Tetany
- **(2)** Muscular dystrophy
- (3) Myasthenia gravis
- (4) Botulism

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT lists muscular dystrophy as progressive degeneration of skeletal muscle, mostly due to a genetic disorder, so it is inherited; tetany is due to low $\mathrm{Ca^{2+}}$, myasthenia gravis is autoimmune and botulism is caused by a bacterial toxin, which gives option $2$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q103_61c367ed_28102026.png?v=61c367eddc6a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Muscular dystrophy is the inherited one among the muscular disorders; myasthenia gravis is auto-immune and tetany is a calcium problem
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Myasthenia gravis is the entry printed beside muscular dystrophy in the same short list of muscular disorders, and its progressive weakening reads like something carried from birth
- **Why:** This question requires the cause printed against each disorder, demonstrated by the stem's 'which of the following muscular disorders is inherited' with three non-genetic disorders from the same list among the options.
<!--/ecat-->

## Q104

Biology · zoology · Structural Organisation in Animals

The ciliated epithelial cells are required to move particles or mucus in a specific direction. In humans, these cells are mainly present in

- (1) Bile duct and Bronchioles
- (2) Fallopian tubes and Pancreatic duct
- (3) Eustachian tube and Salivary duct
- **(4)** Bronchioles and Fallopian tubes

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT states ciliated epithelium is mainly present in the inner surface of hollow organs like bronchioles and fallopian tubes, which is option $4$.

**Subtopic:** Epithelial Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q104_ce673e12_28102026.png?v=ce673e128c12)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ciliated epithelium lines the bronchioles and the fallopian tubes, where something has to be kept moving in one direction; gland ducts are lined without cilia
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Bronchioles is the site fixed first, from the mucus an airway has to clear, and a duct is then accepted as the second site because a duct also carries something along
- **Why:** This question requires the two sites printed for ciliated epithelium, demonstrated by the stem's 'these cells are mainly present in' and by options 1 and 2 each keeping one of the two.
- **Note:** Recorded as two_part: each option is a pair of sites scored whole, which is also why two of the options can keep one correct half.
<!--/ecat-->

## Q105

Biology · zoology · Body Fluids and Circulation

Match the Column-I with Column-II
Select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| a | P - wave | i | Depolarisation of ventricles |
| b | QRS complex | ii | Repolarisation of ventricles |
| c | T - wave | iii | Coronary ischemia |
| d | Reduction in the size of T-wave | iv | Depolarisation of atira |
|  |  | v | Repolarisation of atria |

- **(1)** (a) (iv), (b) (i), (c) (ii), (d) (iii)
- (2) (a) (iv), (b) (i), (c) (ii), (d) (v)
- (3) (a) (ii), (b) (i), (c) (v), (d) (iii)
- (4) (a) (ii), (b) (iii), (c) (v), (d) (iv)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The P-wave represents electrical excitation (depolarisation) of the atria, so $a \rightarrow iv$.
2. The QRS complex represents depolarisation of the ventricles, so $b \rightarrow i$.
3. The T-wave represents the return of the ventricles from excited to normal state (repolarisation), so $c \rightarrow ii$.
4. A reduction in the size of the T-wave indicates insufficient oxygen supply to heart muscle, i.e. coronary ischemia, so $d \rightarrow iii$.
5. The match $a-iv,\ b-i,\ c-ii,\ d-iii$ is option $1$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q105_988f6854_28102026.png?v=988f68540804)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each ECG wave records one electrical event of the cardiac cycle, and a reduction in the T-wave's size is read as coronary ischemia
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Column II holds five events for four rows, so a student who has P, QRS and T right but has not met the shrunken T-wave as a diagnostic sign gives (d) the one physiological event left unused, "Repolarisation of atria"
- **Why:** This question requires each wave of the ECG tied to the stated electrical event, demonstrated by Column I's "Reduction in the size of T-wave" against Column II's "Coronary ischemia".
- **Note:** Column II holds five entries for four rows, and the leftover entry is what the trap runs on. Our record prints entry (iv) as "Depolarisation of atira"; the typo does not change the pairing.
<!--/ecat-->

## Q106

Biology · botany · Biodiversity and Conservation

Which one of the following is not a method in situ conservation of biodiversity?

- (1) Biosphere Reserve
- (2) Wildlife Sanctuary
- **(3)** Botanical Garden
- (4) Sacred Grove

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In situ conservation protects species in their natural habitat (biosphere reserves, wildlife sanctuaries, sacred groves), whereas a botanical garden keeps plants outside their natural habitat, which is ex situ conservation, so the answer is option $3$.

**Subtopic:** In Situ Conservation, Ex Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q106_834ef605_28102026.png?v=834ef6057b18)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In situ conservation keeps a species in its own habitat -- biosphere reserves, sanctuaries, sacred groves -- while a botanical garden holds it away from home
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The in situ list carried in the head is the notified protected areas, national parks and sanctuaries and biosphere reserves, and sacred groves are not on it, so with 'not' in the stem the entry missing from the remembered list is the one marked
- **Why:** This question requires the membership of the in situ list, demonstrated by the stem's 'not a method in situ conservation of biodiversity' set against three of its entries and one ex situ method.
- **Note:** condition_missed was considered for the NOT polarity and ruled out: the route here keeps the 'not' and fails on an incomplete in situ list rather than dropping the stem's condition. Within this packet q110 and q111 are also negated and come out no_trap, because their wrong options are the chapter's core printed lines; the sacred grove is the one entry a protected-area list leaves out, which is what separates this question from those two.
<!--/ecat-->

## Q107

Biology · zoology · Evolution

In a species, the weight of newborn ranges from $2$ to $5\,\mathrm{kg}$. $97\%$ of the newborn with an average weight between $3$ to $3.3\,\mathrm{kg}$ survive whereas $99\%$ of the infants born with weight from $2$ to $2.5\,\mathrm{kg}$ or $4.5$ to $5\,\mathrm{kg}$ die. Which type of selection process is taking place?

- (1) Directional Selection
- **(2)** Stabilizing Selection
- (3) Disruptive Selection
- (4) Cyclical Selection

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Newborns of intermediate weight ($3$ to $3.3\,\mathrm{kg}$) survive at $97\%$ while both extremes ($2$ to $2.5\,\mathrm{kg}$ and $4.5$ to $5\,\mathrm{kg}$) die at $99\%$; selection against both tails favouring the mean is stabilizing selection, option $2$.

**Subtopic:** Types of Natural Selection · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q107_32b18f4c_28102026.png?v=32b18f4c0d0c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Stabilizing selection removes both extremes and holds the population at its existing mean; disruptive favours the extremes and directional moves the mean one way
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The stem names two groups at the two ends of the range, and two groups at the ends is the picture carried for disruptive selection, so the extremes are read as the favoured bands instead of the dying ones
- **Why:** This question requires a known selection type carried to a described population, demonstrated by the stem's figures: 97 per cent of the middle band surviving while 99 per cent of both end bands die.
<!--/ecat-->

## Q108

Biology · both · Cell Cycle and Cell Division

The correct sequence of phases of cell cycle is :

- (1) $\mathrm{M} \rightarrow \mathrm{G_1} \rightarrow \mathrm{G_2} \rightarrow \mathrm{S}$
- (2) $\mathrm{G_1} \rightarrow \mathrm{G_2} \rightarrow \mathrm{S} \rightarrow \mathrm{M}$
- (3) $\mathrm{S} \rightarrow \mathrm{G_1} \rightarrow \mathrm{G_2} \rightarrow \mathrm{M}$
- **(4)** $\mathrm{G_1} \rightarrow \mathrm{S} \rightarrow \mathrm{G_2} \rightarrow \mathrm{M}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Interphase comes first and is $\mathrm{G_1} \rightarrow \mathrm{S} \rightarrow \mathrm{G_2}$; the M phase follows, so the order is $\mathrm{G_1} \rightarrow \mathrm{S} \rightarrow \mathrm{G_2} \rightarrow \mathrm{M}$, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q108_67af2942_28102026.png?v=67af294271dd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Interphase runs G1, then S where the DNA is replicated, then G2, and mitosis follows
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The two gap phases are numbered one and two, so they are put in that order and the S phase is pushed into the space that is left before mitosis
- **Why:** This question requires the printed order of the cycle's phases, demonstrated by the stem's 'correct sequence of phases of cell cycle' and by option 2 holding the right four phases with S and G2 exchanged.
- **Note:** half_right, not reversed: rule 5.1 excludes one swapped pair inside a longer order from reversed, and option 2 keeps G1 first and M last with only the middle pair exchanged.
<!--/ecat-->

## Q109

Biology · zoology · Chemical Coordination and Integration

How does steroid hormone influence the cellular activities?

- (1) Changing the permeability of the cell membrane
- **(2)** Binding to DNA and forming a gene-hormone complex
- (3) Activating cyclic AMP located on the cell membrane
- (4) Using aquaporin channels as second messenger

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Steroid hormones are lipid-soluble, cross the plasma membrane and bind intracellular (nuclear) receptors; the hormone-receptor complex interacts with the genome to alter gene expression, which matches option $2$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q109_df275184_28102026.png?v=df275184498a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A steroid hormone enters the cell and acts on the genome through an intracellular receptor; peptide hormones stay outside and work through a second messenger
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The second-messenger route is printed as the other half of the same account, for the hormones that cannot get into the cell, so a student who holds cyclic AMP as the way hormones act applies it to the steroid as well
- **Why:** This question requires the mechanism the chapter gives for hormones with intracellular receptors, demonstrated by the stem's 'How does steroid hormone influence the cellular activities?'
- **Note:** The pattern called this statement_options; the four options are rival mechanisms answering a how-question rather than claims to be graded, so the shape recorded is mcq and the demand is reason_line.
<!--/ecat-->

## Q110

Biology · both · Cell: The Unit of Life

Which of the following statements is **not** correct?

- (1) Lysosomes have numerous hydrolytic enzymes
- (2) The hydrolytic enzymes of lysosomes are active under acidic pH
- (3) Lysosomes are membrane bound structures
- **(4)** Lysosomes are formed by the process of packaging in the endoplasmic reticulum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Lysosomes are membrane-bound vesicles rich in hydrolytic enzymes (lipases, proteases, carbohydrases) that are active at acidic pH, so options $1$, $2$ and $3$ are correct; they are formed by packaging in the Golgi apparatus, not the endoplasmic reticulum, so option $4$ is the incorrect statement.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q110_66b15e0a_28102026.png?v=66b15e0af4d0)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lysosomes are vesicles budded off the Golgi apparatus, filled with hydrolytic enzymes that work at acid pH
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each remaining option against the lysosome paragraph: numerous hydrolytic enzymes, activity at acidic pH and a bounding membrane are all printed there as they stand, so none of the three can be read as the incorrect statement. The whole work of the question sits in the keyed option, where the Golgi apparatus has been replaced by the endoplasmic reticulum, and a trap cannot sit on the key.
- **Why:** This question requires the organelle a lysosome is budded from, demonstrated by the keyed option's 'formed by the process of packaging in the endoplasmic reticulum' where the Golgi apparatus is what the chapter prints.
- **Note:** No wrong option carries a route: all three are the lysosome paragraph's own lines, printed as true, and the single altered element sits in the keyed option, which cannot hold the trap. Three fillers is the finding here, not unfinished work.
<!--/ecat-->

## Q111

Biology · botany · Sexual Reproduction in Flowering Plants

Which one of the following statements regarding post-fertilization development in flowering plants is incorrect?

- (1) Ovary develops into fruit
- (2) Zygote develops into embryo
- (3) Central cell develops into endosperm
- **(4)** Ovules develop into embryo sac

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Post-fertilization: ovary $\rightarrow$ fruit, zygote $\rightarrow$ embryo, central cell (primary endosperm nucleus) $\rightarrow$ endosperm, ovules $\rightarrow$ seeds; so 'ovules develop into embryo sac' is incorrect, which is option $4$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q111_30698b39_28102026.png?v=30698b39ee0e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** After fertilisation the ovary becomes the fruit, the zygote the embryo, the central cell the endosperm and the ovule the seed -- the embryo sac was already there before fertilisation
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each remaining option against the post-fertilisation sequence: ovary to fruit, zygote to embryo and central cell to endosperm are printed as the events of exactly this stage, so none of the three can be read as incorrect. What the question turns on is the keyed option moving the embryo sac, whose formation is complete before fertilisation, into the events that follow it.
- **Why:** This question requires which of four developments belongs to the post-fertilisation stage, demonstrated by the keyed option's 'Ovules develop into embryo sac', a change that is finished before fertilisation.
- **Note:** Like q110 in this packet, the three wrong options are the chapter's own printed lines and the single altered element sits in the keyed option, so no wrong option has a route. The one snag worth checking, the naming of the central cell against the secondary nucleus, was checked and does not make option 3 false.
<!--/ecat-->

## Q112

Biology · both · Biomolecules

Concanavalin A is

- (1) an alkaloid
- (2) an essential oil
- **(3)** a lectin
- (4) a pigment

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT's table of secondary metabolites lists Concanavalin A under lectins, so the answer is option $3$.

**Subtopic:** Primary And Secondary Metabolites · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q112_31287d0c_28102026.png?v=31287d0cbae9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Concanavalin A is the named example of a lectin in the plant secondary-metabolite table, where lectins sit alongside alkaloids, essential oils, toxins and pigments
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who remembers only that Concanavalin A is one of the named plant secondary metabolites reaches for the class that collects such names, the alkaloids, which is printed in the row above lectins in the same table.
- **Why:** This question requires the stated class a named compound belongs to, demonstrated by the stem 'Concanavalin A is' and four options that are the class headings of one printed table.
<!--/ecat-->

## Q113

Biology · both · Biotechnology: Principles and Processes

Which one of the following equipments is essentially required for growing microbes on a large scale, for industrial production of enzymes?

- (1) BOD incubator
- (2) Sludge digester
- (3) Industrial oven
- **(4)** Bioreactor

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Growing microbes on a large scale for industrial production of enzymes needs large vessels with controlled temperature, pH, aeration and agitation, i.e. a bioreactor, which is option $4$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q113_c4c52a6e_28102026.png?v=c4c52a6ee60a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A bioreactor is the vessel that holds large volumes of culture under controlled conditions, which is what industrial production of a microbial product needs
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  A student who pictures a large tank of microbes picks the sludge digester, which really is large-scale microbial growth -- but it is the answer to how sewage is treated, not to how a product is manufactured.
- **Why:** This question requires the stated fact of which vessel industrial microbial production needs, demonstrated by the stem asking what is 'essentially required for growing microbes on a large scale, for industrial production of enzymes'.
<!--/ecat-->

## Q114

Biology · both · Biomolecules

> ⚠ The independent solve chose (2); the booklet prints (3).

Consider the following statement : Select the correct option.

- **(A)** Coenzyme or metal ion that is tightly bound to enzyme protein is called prosthetic group.
- **(B)** A complete catalytic active enzyme with its bound prosthetic group is called apoenzyme.

- (1) Both (A) and (B) are true.
- (2) (A) is true but (B) is false.
- **(3)** Both (A) and (B) are false.
- (4) (A) is false but (B) is true.

**Answer** — booklet: (3) · independent solve: (2) · differs

**Solved independently** (answer withheld)

1. Statement A: a cofactor that is tightly bound to the enzyme protein is called a prosthetic group, so A is true.
2. Statement B: the protein part alone is the $\text{apoenzyme}$; $\text{apoenzyme} + \text{cofactor} = \text{holoenzyme}$, the complete catalytically active enzyme, so B is false.
3. A true and B false matches option $2$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q114_fde37069_28102026.png?v=fde37069ac66)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Cofactors come as prosthetic groups, coenzymes and metal ions; the protein with its prosthetic group bound is the holoenzyme and the protein alone is the apoenzyme
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Statement (B) swaps apoenzyme for holoenzyme, which is the conspicuous error; statement (A) keeps the source's 'tightly bound' wording and puts coenzyme and metal ion where the organic prosthetic group belongs, so catching (B) and passing (A) lands here.
- **Why:** This question requires two neighbouring definitions held apart, demonstrated by statement (B) calling 'A complete catalytic active enzyme with its bound prosthetic group' the apoenzyme.
- **Note:** E1 recorded plain_mcq by default, but the question prints two labelled statements with four truth verdicts as options, so the shape is recorded as statements. The primary trap is nearby_fact, carried by the three cofactor kinds printed together in one list; the apoenzyme/holoenzyme likeness that would make it look_alike_term is what option 4 runs on, not the trap option.
<!--/ecat-->

## Q115

Biology · both · Molecular Basis of Inheritance

Purines found both in DNA and RNA are

- (1) Adenine and thymine
- **(2)** Adenine and guanine
- (3) Guanine and cytosine
- (4) Cytosine and thymine

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Purines (adenine, guanine) are found in both DNA and RNA. Cytosine and thymine are pyrimidines, so only option $2$, adenine and guanine, fits.

**Subtopic:** Structure of Polynucleotide Chain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q115_31a58223_28102026.png?v=31a58223de6d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Adenine and guanine are the two purines and both occur in DNA and in RNA; thymine and uracil are the pyrimidines that differ between the two nucleic acids
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student reads off the remembered base pair A-T, which gets adenine right and then adds thymine, a pyrimidine that RNA does not even carry.
- **Why:** This question requires the stated fact of which bases are purines, demonstrated by the key option 'Adenine and guanine' and by every option bundling two bases that stand or fall together.
- **Note:** E1_question_type is plain_mcq, but each option is a pair of bases accepted or rejected whole, which is the codebook's pair_options; pair_options maps to qtype statements in category_retired.qtype, so that is what is recorded.
<!--/ecat-->

## Q116

Biology · zoology · Human Reproduction

Select the correct sequence for transport of sperm cells in male reproductive system.

- (1) Testis $\rightarrow$ Epididymis $\rightarrow$ Vasa efferentia $\rightarrow$ Rete testis $\rightarrow$ Inguinal canal $\rightarrow$ Urethra
- **(2)** Seminiferous tubules $\rightarrow$ Rete testis $\rightarrow$ Vasa efferentia $\rightarrow$ Epididymis $\rightarrow$ Vas deferens $\rightarrow$ Ejaculatory duct $\rightarrow$ Urethra $\rightarrow$ Urethral meatus
- (3) Seminiferous tubules $\rightarrow$ Vasa efferentia $\rightarrow$ Epididymis $\rightarrow$ Inguinal canal $\rightarrow$ Urethra
- (4) Testis $\rightarrow$ Epididymis $\rightarrow$ Vasa efferentia $\rightarrow$ Vas deferens $\rightarrow$ Ejaculatory duct $\rightarrow$ Inguinal canal $\rightarrow$ Urethra $\rightarrow$ Urethral meatus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The male accessory ducts carry sperms in the order seminiferous tubules $\rightarrow$ rete testis $\rightarrow$ vasa efferentia $\rightarrow$ epididymis $\rightarrow$ vas deferens $\rightarrow$ ejaculatory duct $\rightarrow$ urethra $\rightarrow$ urethral meatus. Options $1$, $3$ and $4$ get the order wrong or put the inguinal canal in the sperm path, so option $2$ is correct.

**Subtopic:** The Male Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q116_0687411d_28102026.png?v=0687411db5ec)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Sperm leave the seminiferous tubules through the rete testis and vasa efferentia into the epididymis, and only then into the vas deferens, ejaculatory duct and urethra
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who knows the duct names and that the tract ends at the urethral meatus accepts the option of matching length, but it puts the epididymis before the vasa efferentia and routes sperm through the inguinal canal.
- **Why:** This question requires the order of a staged path, demonstrated by the stem 'Select the correct sequence for transport of sperm cells' and by options that differ only in which duct follows which.
- **Note:** qtype is recorded as mcq because the codebook's arrange_in_order maps there; the sequencing demand is carried by asks: order.
<!--/ecat-->

## Q117

Biology · zoology · Evolution

Match the hominids with their correct brain size :
Select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| a | <i>Homo habilis</i> | i | $900\,\mathrm{cc}$ |
| b | <i>Homo neanderthalensis</i> | ii | $1350\,\mathrm{cc}$ |
| c | <i>Homo erectus</i> | iii | $650\text{-}800\,\mathrm{cc}$ |
| d | <i>Homo sapiens</i> | iv | $1400\,\mathrm{cc}$ |

- (1) (iii) (i) (iv) (ii)
- (2) (iii) (ii) (i) (iv)
- **(3)** (iii) (iv) (i) (ii)
- (4) (iv) (iii) (i) (ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Brain sizes as NCERT gives them: \textit{Homo habilis} $650\text{-}800\,\mathrm{cc}$, so (a)-(iii); Neanderthal man $1400\,\mathrm{cc}$, so (b)-(iv); \textit{Homo erectus} about $900\,\mathrm{cc}$, so (c)-(i); which leaves \textit{Homo sapiens} at $1350\,\mathrm{cc}$, so (d)-(ii).
2. The match (iii), (iv), (i), (ii) is option $3$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q117_b4e1b95b_28102026.png?v=b4e1b95b90d4)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cranial capacity through the human fossil series, where the Neanderthal's 1400 cc is larger than modern Homo sapiens' 1350 cc
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The 1400 cc and 1350 cc figures are printed a few lines apart in the same passage, and a student carrying the general picture of brain size rising towards the present hands the larger one to Homo sapiens and the smaller to the Neanderthal
- **Why:** This question requires each hominid matched to the brain size stated for it, demonstrated by "Match the hominids with their correct brain size" with "$1350\,\mathrm{cc}$" and "$1400\,\mathrm{cc}$" both on offer.
- **Note:** Test applied for nearby_fact against look_alike_term: replace 1350 cc and 1400 cc with two unlike values and the pull survives, because what carries it is the two figures standing side by side in the passage together with the expectation of a rising series, not any resemblance between them.
<!--/ecat-->

## Q118

Biology · both · Evolution

Variations caused by mutation, as proposed by Hugo de Vries are

- (1) random and directional
- **(2)** random and directionless
- (3) small and directional
- (4) small and directionless

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Hugo de Vries proposed that variations caused by mutation are random and directionless (Darwinian variations are small and directional), which is option $2$.

**Subtopic:** Mechanism of Evolution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q118_36c446f8_28102026.png?v=36c446f8c562)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** De Vries held that the mutations driving saltation are random and directionless, in deliberate contrast with Darwin's variations, which are small and directional
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A student recalls the sentence that sets the two men against each other and takes the half describing Darwinian variation -- small and directional -- which is true of Darwin's variations and not of de Vries's mutations.
- **Why:** This question requires the stated description de Vries gave of mutation, demonstrated by the four options being the two attribute pairs of one printed contrast crossed with each other.
- **Note:** The four options are a two-by-two grid -- random or small, crossed with directional or directionless -- so each wrong option keeps one correct word.
<!--/ecat-->

## Q119

Biology · both · Cell: The Unit of Life

Which of the following pair of organelles does not contain DNA?

- (1) Mitochondria and Lysosomes
- (2) Chloroplast and Vacuoles
- **(3)** Lysosomes and Vacuoles
- (4) Nuclear envelope and Mitochondria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts contain their own circular DNA (semi-autonomous organelles), so any pair containing either of them is wrong: options $1$, $2$ and $4$ are excluded.
2. Lysosomes and vacuoles are single-membrane bound organelles of the endomembrane system and carry no DNA, so the answer is option $3$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q119_4449745d_28102026.png?v=4449745dd9f1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mitochondria and chloroplasts carry their own circular DNA and so are semi-autonomous; lysosomes and vacuoles carry none
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student who files DNA under the nucleus and the chloroplast only counts mitochondria as DNA-free, and pairs them with lysosomes, which really do lack DNA.
- **Why:** This question requires the stated fact of which organelles hold their own DNA, demonstrated by the stem asking for the 'pair of organelles' that 'does not contain DNA' with each option standing or falling as a pair.
- **Note:** E1_question_type is plain_mcq, but each option is a pair of organelles judged whole -- the codebook's pair_options, which maps to qtype statements. Every wrong option pairs one DNA-free organelle with one DNA-bearing one, so half_right is the device of the whole set and the trap is placed on the pair whose failing half is the mitochondrion.
<!--/ecat-->

## Q120

Biology · zoology · Breathing and Exchange of Gases

Due to increasing air-borne allergens and pollutants, many people in urban areas are suffering from respiratory disorder causing wheezing due to

- (1) benign growth on mucous lining of nasal cavity
- **(2)** inflammation of bronchi and bronchioles
- (3) proliferation of fibrous tissues and damage of the alveolar walls
- (4) reduction in the secretion of surfactants by pneumocytes.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Wheezing caused by air-borne allergens and pollutants is $\text{asthma}$, which is due to inflammation of the bronchi and bronchioles, so the answer is option $2$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q120_fc7e9a8d_28102026.png?v=fc7e9a8dc093)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Asthma is wheezing caused by inflammation and narrowing of the bronchi and bronchioles, which allergens and pollutants trigger
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Emphysema sits in the same disorders paragraph and is the one tied to inhaled smoke and damaged alveolar walls, so a student keying on the pollutant in the stem stops there. Alveolar damage gives breathlessness, but the whistle of a wheeze is made in narrowed airways, not in the alveoli.
- **Why:** This question requires the cause the book gives for wheezing, demonstrated by the stem ending 'causing wheezing due to' and option 2 supplying 'inflammation of bronchi and bronchioles'. On the trap axis the swap test was applied: replace emphysema with any unlike disorder name and the pull survives, because it is the disorder printed beside asthma that carries the student, so nearby_fact and not look_alike_term.
<!--/ecat-->

## Q121

Biology · zoology · Principles of Inheritance and Variation

Select the incorrect statement.

- (1) Male fruit fly is heterogametic
- (2) In male grasshoppers $50\%$ of sperms have no sex-chromosome
- **(3)** In domesticated fowls, sex of progeny depends on the type of sperm rather than egg
- (4) Human males have one of their sex-chromosome much shorter than the other

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Male Drosophila is $XY$, so it is heterogametic: statement $1$ is correct.
2. Male grasshopper is $XO$, so $50\%$ of sperms carry $X$ and $50\%$ carry no sex chromosome: statement $2$ is correct.
3. In fowl the female is $ZW$ and the male $ZZ$, so every sperm carries $Z$ and the egg ($Z$ or $W$) decides the sex: statement $3$ is incorrect.
4. In human males the $Y$ chromosome is much shorter than the $X$: statement $4$ is correct.
5. The incorrect statement is option $3$.

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q121_50205027_28102026.png?v=502050277e4a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In birds the female is the heterogametic sex (ZW), so the egg and not the sperm decides the sex of the chick, unlike the XY and XO systems
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The XY picture rehearsed for humans and the fruit fly says every sperm carries either an X or a Y, and carried across to the grasshopper it makes 'no sex-chromosome' read as the planted error. Grasshopper males are XO: there is no Y at all, so half the sperm carry the single X and half carry none.
- **Why:** This question requires the stated fact that in birds the female is heterogametic, demonstrated by option 3 claiming that in domesticated fowls 'sex of progeny depends on the type of sperm rather than egg'. For the trap, the swap test was applied: the names grasshopper and human resemble each other not at all, and the pull comes from the XY case printed beside the XO case, so nearby_fact.
- **Note:** E1 called this statement_options and q124 plain_mcq, although both print the stem 'Select the incorrect statement' over four full-sentence options. Both are recorded here as qtype statements, since the stem asks for statements to be judged.
<!--/ecat-->

## Q122

Biology · both · Biotechnology: Principles and Processes

DNA precipitation out of a mixture of biomolecules can be achieved by treatment with

- (1) Isopropanol
- **(2)** Chilled ethanol
- (3) Methanol at room temperature
- (4) Chilled chloroform

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In the isolation of DNA, after treating with RNase and protease, adding chilled ethanol makes the purified DNA precipitate out as fine threads, so the answer is option $2$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q122_4c3311a8_28102026.png?v=4c3311a84112)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In DNA isolation the purified DNA is brought out of the aqueous suspension as fine threads by adding chilled ethanol
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Isopropanol is the other alcohol that drops DNA out of solution, so a student carrying the step as 'add alcohol' picks the alcohol that no temperature disqualifies. The step as the book prints it names one reagent, chilled ethanol, and that name is what the question is asking for.
- **Why:** This question requires the named reagent printed for the precipitation step of DNA isolation, demonstrated by the four options differing only in which alcohol or solvent and at what temperature ('Chilled ethanol' against 'Methanol at room temperature'). Swap test for the trap: replace isopropanol with any unlike solvent name and the pull survives, because what carries the student is membership of the same reagent step rather than any resemblance between the words, so nearby_fact.
<!--/ecat-->

## Q123

Biology · botany · Microbes in Human Welfare

Select the correct group of biocontrol agents.

- (1) Bacillus thuringiensis, Tobacco mosaic virus, Aphids
- **(2)** Trichoderma, Baculovirus, Bacillus thuringiensis
- (3) Oscillatoria, Rhizobium, Trichoderma
- (4) Nostoc, Azospirillium, Nucleopolyhedrovirus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Biocontrol agents named in NCERT are $Bacillus\ thuringiensis$, $Trichoderma$ and Baculoviruses (genus $Nucleopolyhedrovirus$); option $2$ lists only these, so it is the answer.

**Subtopic:** Microbes as Biocontrol Agents · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q123_4bbcb81b_28102026.png?v=4bbcb81b6800)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biocontrol agents are living organisms used against pests and pathogens — Trichoderma, baculoviruses and Bacillus thuringiensis — and are a different list from the biofertilisers
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Trichoderma leads this option and is the free-living fungus taught as a biocontrol agent, so a group checked by the member that is recognised is accepted whole. Rhizobium and Oscillatoria come from the biofertiliser list, and one disqualified member sinks the group.
- **Why:** This question requires membership of the named list of biocontrol agents to hold for every organism in a bundled option, demonstrated by the keyed option reading as a whole trio, 'Trichoderma, Baculovirus, Bacillus thuringiensis'.
- **Note:** The options are groups of three organisms accepted or rejected whole, which the retired E1 vocabulary called pair_options; recorded as two_part because the answer must hold for every member at once and the current qtype list carries no value for a bundled set.
<!--/ecat-->

## Q124

Biology · zoology · Strategies for Enhancement in Food Production

Select the incorrect statement.

- (1) Inbreeding increases homozygosity
- (2) Inbreeding is essential to evolve purelines in any animal.
- **(3)** Inbreeding selects harmful recessive genes that reduce fertility and productivity
- (4) Inbreeding helps in accumulation of superior genes and elimination of undesirable genes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Inbreeding (mating of closely related individuals) increases homozygosity, so option $1$ is correct.
2. Inbreeding is necessary to evolve a pureline in any animal, so option $2$ is correct.
3. Increased homozygosity exposes harmful recessive genes, which are then eliminated by selection; this helps accumulate superior genes and remove undesirable ones, so option $4$ is correct.
4. Inbreeding does not select harmful recessive genes; it exposes them for elimination. Option $3$ is the incorrect statement.

**Subtopic:** Animal Breeding · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q124_536bcaa6_28102026.png?v=536bcaa6e238)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inbreeding raises homozygosity and exposes harmful recessives so that selection can eliminate them; it does not select for them
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Inbreeding depression — reduced fertility and productivity on continued inbreeding — is printed in the same paragraph, and a student holding that caution reads 'essential to evolve purelines in any animal' as the overstatement the negated stem must be after. The line in the book is that inbreeding is necessary if a pureline is to be evolved in any animal.
- **Why:** This question requires the stated line that inbreeding exposes harmful recessive genes so that selection can eliminate them, demonstrated by option 3 reading 'Inbreeding selects harmful recessive genes that reduce fertility and productivity'. Swap test on the trap: the pull on option 2 comes from the inbreeding-depression sentence printed next to it, not from any resemblance between words, so nearby_fact.
- **Note:** E1 called this plain_mcq and q121 statement_options, although both print the stem 'Select the incorrect statement' over four full-sentence options. Both are recorded here as qtype statements.
<!--/ecat-->

## Q125

Biology · botany · Microbes in Human Welfare

Match the following organisms with the products they produce
Select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Lactobacillus | (i) | Cheese |
| (b) | Saccharomyces cerevisiae | (ii) | Curd |
| (c) | Aspergillus niger | (iii) | Citric Acid |
| (d) | Acetobacter aceti | (iv) | Bread |
|  |  | (v) | Acetic Acid |

- (1) (ii) (iv) (v) (iii)
- **(2)** (ii) (iv) (iii) (v)
- (3) (iii) (iv) (v) (i)
- (4) (ii) (i) (iii) (v)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Lactobacillus (LAB) converts milk to curd: $(a) \rightarrow (ii)$.
2. Saccharomyces cerevisiae (baker's yeast) is used to make bread: $(b) \rightarrow (iv)$.
3. Aspergillus niger produces citric acid: $(c) \rightarrow (iii)$.
4. Acetobacter aceti produces acetic acid: $(d) \rightarrow (v)$.
5. The sequence $(ii)\,(iv)\,(iii)\,(v)$ is option $2$.

**Subtopic:** Microbes in Household Products, Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q125_a10996cb_28102026.png?v=a10996cba871)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each industrial microbe is tied to one named product: Lactobacillus to curd, baker's yeast to bread, Aspergillus niger to citric acid and Acetobacter aceti to acetic acid
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  "Citric Acid" and "Acetic Acid" sit in Column II as two near-identical short acid names, and a student who has not read the "aceti" in Acetobacter aceti as the pointer to acetic acid attaches them the other way round
- **Why:** This question requires each organism matched to the product stated for it, demonstrated by "Match the following organisms with the products they produce".
- **Note:** Test applied for look_alike_term against nearby_fact: replace "Citric Acid" and "Acetic Acid" with two unlike products and the swap stops being attractive, so the resemblance of the two names is doing the work rather than their position in the column. Column II holds five entries for four rows; the unused one in the key is "Cheese".
<!--/ecat-->

## Q126

Biology · botany · Transport in Plants

What is the direction of movement of sugars in phloem?

- (1) Non-multidirectional
- (2) Upward
- (3) Downward
- **(4)** Bi-directional

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Phloem translocates sugars from a $\text{source}$ to a $\text{sink}$; because source and sink positions can reverse with season and need, the movement can go up or down, i.e. it is bi-directional, which is option $4$.

**Subtopic:** Phloem Transport: Flow from Source to Sink · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q126_dbeb669e_28102026.png?v=dbeb669e86aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Phloem carries sugar from any source to any sink, so translocation is bi-directional, unlike the one-way upward flow in xylem
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Sugar loaded in the leaf and sent down to the root is the standard picture, and it is the half of the answer paired against xylem's upward flow, so downward gets taken for the whole of it. Downward is one direction of two: a sink can be a bud, a flower or a fruit above the source, so the same tissue also carries sugar upward.
- **Why:** This question requires the stated direction of phloem translocation, demonstrated by the stem asking only for 'the direction of movement of sugars in phloem' with four bare directions as options. half_right is used on option 3 under the rulebook's 'true but incomplete set' clause — downward is one of the two directions the answer requires, not a lone wrong name.
<!--/ecat-->

## Q127

Biology · botany · Reproduction in Organisms

In some plants, the female gamete develops into embryo without fertilization. This phenomenon is known as

- (1) Autogamy
- (2) Parthenocarpy
- (3) Syngamy
- **(4)** Parthenogenesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. An embryo forming from an unfertilised female gamete is $\text{parthenogenesis}$ (parthenocarpy = seedless fruit without fertilisation; autogamy = self-pollination; syngamy = fusion of gametes), which is option $4$.

**Subtopic:** Sexual Reproduction: Events and Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q127_da1ce435_28102026.png?v=da1ce435ac4f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parthenogenesis is a female gamete developing into an embryo with no fertilisation; parthenocarpy is a fruit developing with no fertilisation
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  A student who has stored 'partheno- means without fertilisation' picks the other partheno- word, which names fruit set rather than embryo formation.
- **Why:** This question requires the term for a stated phenomenon, demonstrated by the stem 'the female gamete develops into embryo without fertilization. This phenomenon is known as'.
- **Note:** The stem says 'In some plants', while the term's standard examples are animals and the parallel plant phenomenon is apomixis; the definition the stem gives is still parthenogenesis and the key is tagged as printed.
<!--/ecat-->

## Q128

Biology · botany · Sexual Reproduction in Flowering Plants

Persistent nucellus in the seed is known as

- (1) Chalaza
- **(2)** Perisperm
- (3) Hilum
- (4) Tegmen

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In seeds such as black pepper and beet, residual nucellus persists, and this persistent nucellus is called perisperm, which is option $2$.

**Subtopic:** Embryo and Seed · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q128_12d64b8b_28102026.png?v=12d64b8b050d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In seeds such as black pepper and beet the nucellus is not fully used up, and that residual persistent nucellus is called perisperm
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who remembers that the ovule's coverings become the seed coats takes the inner coat, tegmen, as the leftover layer, when tegmen comes from the inner integument and not from the nucellus.
- **Why:** This question requires the stated name for a seed tissue, demonstrated by the stem 'Persistent nucellus in the seed is known as' with four seed and ovule parts as options.
<!--/ecat-->

## Q129

Biology · both · Principles of Inheritance and Variation

What map unit (Centimorgan) is adopted in the construction of genetic maps?

- (1) A unit of distance between two expressed genes representing $10\%$ cross over.
- (2) A unit of distance between two expressed genes representing $100\%$ cross over.
- **(3)** A unit of distance between genes on chromosomes, representing $1\%$ cross over.
- (4) A unit of distance between genes on chromosomes, representing $50\%$ cross over.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A genetic map unit (centimorgan) is defined as the distance between genes on a chromosome that yields $1\%$ crossing over (recombination frequency), which is option $3$.

**Subtopic:** Linkage & Recombination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q129_faf71e8e_28102026.png?v=faf71e8e5279)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** One map unit, the centimorgan, is defined as 1% recombination frequency between two genes on a chromosome
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  A student recalls 50% as the number that matters in linkage work and takes the option that pairs it with the right wording, but 50% recombination is the mark of genes assorting independently, not the size of one map unit.
- **Why:** This question requires the stated definition of a unit, demonstrated by the key option 'A unit of distance between genes on chromosomes, representing 1% cross over' and by the options differing only in that percentage and in the phrase before it.
<!--/ecat-->

## Q130

Biology · zoology · Body Fluids and Circulation

What would be the heart rate of a person if the cardiac output is $5\,\mathrm{L}$, blood volume in the ventricles at the end of diastole is $100\,\mathrm{mL}$ and at the end of ventricular systole is $50\,\mathrm{mL}$?

- (1) 50 beats per minute
- (2) 75 beats per minute
- **(3)** 100 beats per minute
- (4) 125 beats per minute

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Stroke volume is end-diastolic volume minus end-systolic volume: $SV = 100\,\mathrm{mL} - 50\,\mathrm{mL} = 50\,\mathrm{mL}$.
2. Cardiac output (per minute) is $5\,\mathrm{L} = 5000\,\mathrm{mL}$.
3. $CO = SV \times HR \Rightarrow HR = \frac{CO}{SV} = \frac{5000\,\mathrm{mL/min}}{50\,\mathrm{mL}} = 100$ beats per minute, which is option $3$.

**Subtopic:** Cardiac Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q130_d0bb60d5_28102026.png?v=d0bb60d54980)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Stroke volume is end-diastolic volume minus end-systolic volume, and heart rate is cardiac output divided by that stroke volume
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who divides cardiac output by the end-diastolic volume instead of by the stroke volume gets $5000/100 = 50$, because the ventricle never empties completely.
- **Why:** This question requires a number computed from the stem, demonstrated by it supplying 'cardiac output is 5 L', 100 mL at end of diastole and 50 mL at end of systole and asking for the heart rate.
- **Note:** E1_question_type says statement_options, but the four options are bare values in beats per minute, not statements to judge; recorded as mcq.
<!--/ecat-->

## Q131

Biology · botany · Mineral Nutrition

*Thiobacillus* is a group of bacteria helpful in carrying out

- (1) Nitrogen fixation
- (2) Chemoautotrophic fixation
- (3) Nitrification
- **(4)** Denitrification

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the nitrogen cycle as the textbook teaches it, soil nitrate is reduced to $N_2$ (denitrification, $NO_3^- \rightarrow N_2$) by the bacteria *Pseudomonas* and *Thiobacillus*, so the answer is option $4$.

**Subtopic:** Nitrogen Fixation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q131_32aa8bd8_28102026.png?v=32aa8bd8f620)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thiobacillus, with Pseudomonas, reduces soil nitrate back to gaseous nitrogen, which is denitrification
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who remembers that a named bacterium handles each step of the nitrogen cycle picks the step printed just before this one, nitrification, which belongs to Nitrosomonas and Nitrobacter.
- **Why:** This question requires the stated fact of which nitrogen-cycle step a named bacterium carries out, demonstrated by the stem 'Thiobacillus is a group of bacteria helpful in carrying out' with four steps of that cycle as options.
- **Note:** Option 2 is true of the organism's nutrition, and 'chemoautotrophic fixation' is not a process the chapter names; the key is tagged as printed.
<!--/ecat-->

## Q132

Biology · zoology · Excretory Products and Their Elimination

Which of the following factors is responsible for the formation of concentrated urine?

- (1) Low levels of antidiuretic hormone
- **(2)** Maintaining hyperosmolarity towards inner medullary interstitium in the kidneys.
- (3) Secretion of erythropoietin by Juxtaglomerular complex
- (4) Hydrostatic pressure during glomerular filtration

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Low ADH reduces water reabsorption in the DCT and collecting duct, so it gives dilute urine, not concentrated urine; option $1$ is out.
2. Erythropoietin from the JG cells stimulates RBC formation and has no role in concentrating urine; option $3$ is out.
3. Glomerular hydrostatic pressure drives filtration (GFR), not the concentration of the filtrate; option $4$ is out.
4. The counter-current mechanism of Henle's loop and the vasa recta keeps an increasing medullary interstitial osmolarity from $300$ to about $1200\,\mathrm{mOsmol\,L^{-1}}$.
5. This gradient draws water out of the collecting duct, so the urine becomes concentrated, which is option $2$.

**Subtopic:** Mechanism of Concentration of the Filtrate · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q132_568f7fc3_28102026.png?v=568f7fc3dd78)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Urine is concentrated because the counter-current mechanism keeps the inner medullary interstitium hyperosmotic, so water leaves the collecting duct
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who knows ADH is the hormone of urine concentration keeps the hormone and inverts its direction, where it is high ADH that concentrates urine and low ADH that gives a dilute flood.
- **Why:** This question requires the reason given for an outcome, demonstrated by the stem asking which factor 'is responsible for the formation of concentrated urine' and by the key naming the hyperosmolarity of the inner medullary interstitium.
- **Note:** E1_question_type says statement_options; the options are noun phrases naming rival causes rather than statements to be judged, so qtype is mcq and the cause-selection demand is carried by asks: reason_line.
<!--/ecat-->

## Q133

Biology · both · Cell: The Unit of Life

Which of the following statements regarding mitochondria is incorrect?

- (1) Outer membrane is permeable to monomers of carbohydrates, fats and proteins.
- **(2)** Enzymes of electron transport are embedded in outer membrane.
- (3) Inner membrane is convoluted with infoldings.
- (4) Mitochondrial matrix contains single circular DNA molecule and ribosomes.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The respiratory chain (electron transport system) enzymes lie in the inner mitochondrial membrane (cristae), so statement $2$ (outer membrane) is incorrect; options $1$, $3$ and $4$ are correct, giving option $2$.

**Subtopic:** Mitochondria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q133_d0e441aa_28102026.png?v=d0e441aac2ed)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The electron transport enzymes sit in the inner mitochondrial membrane, which is the selectively permeable one; the outer membrane is freely permeable and the matrix holds the circular DNA
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who remembers that a mitochondrial membrane is selectively permeable attaches that selectivity to the outer membrane, and so reads the freely-permeable line as the false one.
- **Why:** This question requires the stated fact of where the electron transport enzymes sit, demonstrated by option 2 'Enzymes of electron transport are embedded in outer membrane' being the only printed claim that moves them off the inner membrane.
<!--/ecat-->

## Q134

Biology · botany · Transport in Plants

Xylem translocates.

- (1) Water only
- (2) Water and mineral salts only
- (3) Water, mineral salts and some organic nitrogen only
- **(4)** Water, mineral salts, some organic nitrogen and hormones

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Xylem translocates water, mineral salts, some organic nitrogen and hormones from roots to the aerial parts, which is option $4$.

**Subtopic:** Uptake and Transport of Mineral Nutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q134_23b5502d_28102026.png?v=23b5502d84f8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The xylem carries water, mineral salts, some organic nitrogen and hormones from root to shoot -- the list is longer than the water-and-minerals summary
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student working from the standard division of labour -- xylem carries water and minerals, phloem carries food -- stops the list at mineral salts, and the word 'only' turns a partly correct list into a wrong answer.
- **Why:** This question requires the stated contents of xylem sap, demonstrated by the options being nested lists separated by the word 'only' -- 'Water only', 'Water and mineral salts only', and so on.
- **Note:** E1_question_type is plain_mcq; each option is a set of substances accepted or rejected whole, which is the codebook's pair_options and maps to qtype statements.
<!--/ecat-->

## Q135

Biology · both · Cell Cycle and Cell Division

Cell in $\mathrm{G_0}$ phase :

- **(1)** exit the cell cycle
- (2) enter the cell cycle
- (3) suspend the cell cycle
- (4) terminate the cell cycle

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. As NCERT teaches, cells that do not divide further exit the $\mathrm{G_1}$ phase and enter the inactive quiescent stage $\mathrm{G_0}$; they are said to exit the cell cycle, though they stay metabolically active and can re-enter it, so the answer is option $1$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q135_23ec2279_28102026.png?v=23ec2279b7ee)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cells that stop dividing leave G1 for the quiescent G0 stage, where they stay metabolically active but no longer proliferate
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who carries the word 'quiescent' from the same sentence rather than the word 'exit' reads G0 as a pause and picks 'suspend the cell cycle'.
- **Why:** This question requires the stated description of G0, demonstrated by four rival verbs -- exit, enter, suspend, terminate -- completing the stem 'Cell in G0 phase :'.
- **Note:** Applied the 5.1 test: exit and suspend do not resemble each other as words, so this is not look_alike_term; the pull is the neighbouring clause of the same printed sentence, which calls G0 an inactive stage of the cell cycle. That same clause makes option 3 defensible on a strict reading -- a stage 'of the cell cycle' is not outside it -- so the key is recorded as arguable, and tagged as printed.
<!--/ecat-->

## Q136

Biology · botany · Anatomy of Flowering Plants

Which of the statements given below is not true about formation of Annual Rings in trees?

- (1) Annual ring is a combination of spring wood and autumn wood produced in a year
- (2) Differential activity of cambium causes light and dark bands of tissue early and late wood respectively.
- (3) Activity of cambium depends upon variation in climate.
- **(4)** Annual rings are not prominent in trees of temperate region.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In temperate regions cambium is very active in spring (light early wood) and less active in winter (dark late wood). These alternating bands make annual rings prominent, so statement $4$ is not true, while statements $1$, $2$ and $3$ are true. The answer is option $4$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q136_d70c25a9_28102026.png?v=d70c25a9be02)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Annual rings are prominent where the seasons differ sharply, so temperate trees show them clearly and the ring is one year's early wood plus late wood
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who pictures spring growth as the dense, dark band holds the light-and-dark assignment the other way round, and so marks the statement that pairs light with early wood as the untrue one.
- **Why:** This question requires the stated fact about where annual rings are prominent, demonstrated by option 4 'Annual rings are not prominent in trees of temperate region' standing against the sharply seasonal climate the rest of the options depend on.
<!--/ecat-->

## Q137

Biology · botany · Ecosystem

Which of the following ecological pyramids is generally inverted?

- (1) Pyramid of numbers in grassland
- (2) Pyramid of energy
- (3) Pyramid of biomass in a forest
- **(4)** Pyramid of biomass in a sea

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A pyramid of energy is always upright, because only about $10\%$ of energy passes to each next trophic level. That rules out option $2$.
2. In a grassland the pyramid of numbers is upright (many grasses $>$ herbivores $>$ carnivores), and in a forest the pyramid of biomass is upright. That rules out options $1$ and $3$.
3. In the sea, the biomass of phytoplankton is smaller than the biomass of the fish that eat them, so the pyramid of biomass is inverted. The answer is option $4$.

**Subtopic:** Ecological Pyramids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q137_87b31853_28102026.png?v=87b318539c0b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The pyramid of biomass in the sea is inverted because the tiny standing crop of phytoplankton turns over fast enough to support a much larger mass of consumers
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who remembers that the forest example gives an inverted pyramid picks the forest option, but the inversion in the forest belongs to the pyramid of NUMBERS -- one tree carrying thousands of insects -- while its biomass pyramid is upright.
- **Why:** This question requires the stated fact of which pyramid is inverted, demonstrated by the options crossing the quantity plotted with the ecosystem -- numbers in grassland, biomass in a forest, biomass in a sea.
<!--/ecat-->

## Q138

Biology · botany · Morphology of Flowering Plants

Placentation in which ovules develop on the inner wall of the ovary or in peripheral part, is

- (1) Basal
- (2) Axile
- **(3)** Parietal
- (4) Free central

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Ovules borne on the inner wall of the ovary or on its peripheral part define parietal placentation (as in mustard and Argemone), which is option $3$.

**Subtopic:** Gynoecium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q138_967c032e_28102026.png?v=967c032e0d2b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parietal placentation has the ovules on the inner wall of the ovary; axile has them on a central axis in a septate ovary and free central on a central axis with no septa
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who remembers axile as the type with ovules spread around inside a chambered ovary picks it for a stem about the ovary wall, when axile attaches them to the central axis instead.
- **Why:** This question requires the name attached to a stated arrangement, demonstrated by the stem quoting the definition 'ovules develop on the inner wall of the ovary or in peripheral part' and offering the four placentation types.
<!--/ecat-->

## Q139

Biology · botany · Environmental Issues

Which of the following protocols did aim for reducing emission of chlorofluorocarbons into the atmosphere?

- **(1)** Montreal Protocol
- (2) Kyto Protocol
- (3) Gothenburg Protocol
- (4) Geneva Protocol

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The Montreal Protocol, signed in 1987 at Montreal, Canada, aimed to control the emission of ozone-depleting substances such as CFCs, so the answer is option $1$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q139_28a9bdc3_28102026.png?v=28a9bdc3e157)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Montreal Protocol is the agreement aimed at cutting the release of ozone-depleting substances such as chlorofluorocarbons; the Kyoto Protocol deals with greenhouse gases
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who holds two protocols from this chapter without fixing which gas each one is about picks the other one, Kyoto, whose business is greenhouse gas emission rather than ozone-depleting CFCs.
- **Why:** This question requires the stated fact of which protocol targets CFCs, demonstrated by the stem 'did aim for reducing emission of chlorofluorocarbons into the atmosphere' with four protocols as options.
- **Note:** Option 2 is printed 'Kyto Protocol' in the paper; copied exactly as given, and the intended name is plainly Kyoto.
<!--/ecat-->

## Q140

Biology · zoology · Reproductive Health

Which of the following contraceptive methods do involve a role of hormone?

- **(1)** Lactational amenorrhea, Pills Emergency contraceptives.
- (2) Barrier method, Lactational amenorrhea, Pills.
- (3) CuT, Pills, Emergency contraceptives.
- (4) Pills, Emergency contraceptives, Barrier methods.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Oral pills contain progestogens or progestogen-estrogen combinations, so they are hormonal.
2. Emergency contraceptives (within 72 hours) use progestogens or progestogen-estrogen combinations, so they are hormonal.
3. Barrier methods (condoms, diaphragms, cervical caps, vaults) act physically, so options $2$ and $4$ include a non-hormonal method.
4. CuT releases $\mathrm{Cu}$ ions that suppress sperm motility and fertilising capacity, not hormones, so option $3$ includes a non-hormonal method.
5. Lactational amenorrhea depends on the hormonal state of intense lactation that suppresses ovulation, so option $1$ (Lactational amenorrhea, Pills, Emergency contraceptives) is the answer.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q140_493f7cf3_28102026.png?v=493f7cf3b866)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lactational amenorrhoea, oral pills and emergency contraceptives all work through hormones; barrier methods work mechanically and the CuT is the copper-releasing, not the hormone-releasing, IUD
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who files lactational amenorrhoea under natural methods and so as hormone-free drops the key and takes the set that keeps the two certain hormonal methods, adding the CuT because hormone-releasing IUDs exist.
- **Why:** This question requires the stated fact of which methods act through hormones, demonstrated by each option bundling three named methods that stand or fall together -- 'CuT, Pills, Emergency contraceptives'.
<!--/ecat-->

## Q141

Biology · zoology · Breathing and Exchange of Gases

Tidal Volume and Expiratory Reserve Volume of an athlete is $500\,\mathrm{mL}$ and $1000\,\mathrm{mL}$, respectively. What will be his Expiratory Capacity if the Residual Volume is $1200\,\mathrm{mL}$?

- **(1)** $1500\,\mathrm{mL}$
- (2) $1700\,\mathrm{mL}$
- (3) $2200\,\mathrm{mL}$
- (4) $2700\,\mathrm{mL}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Expiratory Capacity is defined as $EC = TV + ERV$; Residual Volume is not included.
2. $EC = 500\,\mathrm{mL} + 1000\,\mathrm{mL} = 1500\,\mathrm{mL}$.
3. $1500\,\mathrm{mL}$ is option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q141_176b6289_28102026.png?v=176b6289fe01)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Expiratory capacity is tidal volume plus expiratory reserve volume; the residual volume belongs to functional residual capacity and not to this one
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who reaches for the capacity that uses the residual volume adds expiratory reserve to residual volume, $1000 + 1200 = 2200$ mL, which is the functional residual capacity and not the expiratory capacity.
- **Why:** This question requires a number computed from the stem's volumes, demonstrated by it supplying 500 mL, 1000 mL and 1200 mL and asking 'What will be his Expiratory Capacity'.
- **Note:** E1_question_type says multi_part_respectively; the stem's 'respectively' hands over two given volumes rather than asking for two answers, and the answer is one value in mL, so qtype is mcq.
<!--/ecat-->

## Q142

Biology · botany · Sexual Reproduction in Flowering Plants

What is the fate of the male gametes discharged in the synergid?

- (1) One fuses with egg other(s) degenerate (s) in the synergid.
- (2) All fuse with the egg.
- (3) One fuses with the egg, other(s) fuse(s) with synergid nucleus.
- **(4)** One fuses with the egg and other fuses with central cell nuclei.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The pollen tube releases two male gametes into the cytoplasm of a synergid; one fuses with the egg (syngamy, forming the $2n$ zygote) and the other fuses with the two polar nuclei of the central cell (triple fusion, forming the $3n$ PEN), which is option $4$.

**Subtopic:** Double Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q142_20ab8a6f_28102026.png?v=20ab8a6fa55c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In double fertilisation both male gametes are used: one fuses with the egg to make the zygote and the other with the two polar nuclei of the central cell to make the primary endosperm nucleus
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  A student who remembers that the pollen tube discharges its gametes into a synergid keeps the second fusion at that same spot, so the gamete is made to fuse with the synergid nucleus instead of travelling on to the central cell.
- **Why:** This question requires the stated fate of each male gamete, demonstrated by the options differing only in what the second gamete fuses with -- 'synergid nucleus' against 'central cell nuclei'.
<!--/ecat-->

## Q143

Biology · botany · Plant Growth and Development

What is the site of perception of photoperiod necessary for induction of flowering in plants?

- (1) Lateral buds
- (2) Pulvinus
- (3) Shoot apex
- **(4)** Leaves

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The photoperiodic stimulus is perceived by the $\text{leaves}$, which pass a hormonal signal to the shoot apex where flowers form; so the site of perception is the leaves, option $4$.

**Subtopic:** Photoperiodism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q143_5adb14b3_28102026.png?v=5adb14b3b498)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The leaves perceive the photoperiod and pass a flowering stimulus to the shoot apex, which is where the flower is actually made
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  A student who knows the flower is formed at the shoot apex names that as the site of perception too, collapsing where the day length is measured into where the response appears.
- **Why:** This question requires the stated site of a process, demonstrated by the stem asking for 'the site of perception of photoperiod necessary for induction of flowering'.
<!--/ecat-->

## Q144

Biology · botany · The Living World

Select the correctly written scientific name of Mango which was first described by Carolus Linnaeus :

- (1) Mangifera indica Car. Linn.
- **(2)** Mangifera indica Linn.
- (3) Mangifera indica
- (4) Mangifera Indica

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Binomial rules: the genus begins with a capital letter, the specific epithet with a small letter, and the author who first described the species is written after the epithet in abbreviated form, so $\textit{Mangifera indica}$ described by Linnaeus is written $\textit{Mangifera indica}$ Linn., which is option $2$.

**Subtopic:** Diversity in Living World and Binomial Nomenclature · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q144_11be0e8d_28102026.png?v=11be0e8d8593)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Binomial nomenclature rules: genus capitalised, species epithet in lower case, both italicised, and the author's name added in abbreviated form after the species epithet
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  A student checks the two rules they hold firmly -- two words, genus capitalised, species lower case -- and stops there, missing the stem's clause that the name was first described by Linnaeus and so must carry his name abbreviated.
- **Why:** This question requires a naming convention applied to a printed case, demonstrated by the stem asking for 'the correctly written scientific name of Mango which was first described by Carolus Linnaeus' and by the options differing only in author citation and capitalisation.
<!--/ecat-->

## Q145

Biology · both · Biotechnology: Principles and Processes

Following statements describe the characteristics of the enzyme Restriction Endonuclease. Identify the incorrect statement.

- (1) The enzyme cuts DNA molecule at identified position within the DNA.
- **(2)** The enzyme binds DNA at specific sites and cuts only one of the two strands.
- (3) The enzyme cuts the sugar-phosphate backbone at specific sites on each strand.
- (4) The enzyme recognizes a specific palindromic nucleotide sequence in the DNA.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A restriction endonuclease recognises a specific palindromic sequence, binds the DNA there and cuts the sugar-phosphate backbone of each of the two strands, so options $1$, $3$ and $4$ are correct and option $2$ ("cuts only one of the two strands") is the incorrect statement.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q145_22b004c8_28102026.png?v=22b004c8a2bd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A restriction endonuclease cuts inside the DNA, at a palindromic recognition sequence, and it cuts the backbone of both strands
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The enzyme that works on the ends of a DNA molecule is the exonuclease, printed in the same contrast sentence; a student holding only 'one of them works at the ends' reads 'cuts at identified position within the DNA' as the false line and marks it.
- **Why:** This question requires the stated properties of restriction endonucleases, demonstrated by 'Identify the incorrect statement' set against four printed descriptions of which only 'cuts only one of the two strands' contradicts them.
- **Note:** nearby_fact rather than look_alike_term: I applied the swap test by replacing 'endonuclease' and 'exonuclease' with two unlike words, and the pull survives, because what carries it is the contrast sentence printing the end-acting enzyme beside the within-acting one, not the likeness of the two names.
<!--/ecat-->

## Q146

Biology · botany · Plant Kingdom

From evolutionary point of view, retention of the female gametophyte with developing young embryo on the parent sporophyte for some time, is first observed in :

- (1) Liverworts
- (2) Mosses
- **(3)** Pteridophytes
- (4) Gymnosperms

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In heterosporous pteridophytes such as $Selaginella$ and $Salvinia$, the female gametophyte is retained on the parent sporophyte and the zygote develops into a young embryo within it; NCERT calls this the precursor to the seed habit, first seen in Pteridophytes (option $3$).

**Subtopic:** Pteridophytes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q146_46b24b70_28102026.png?v=46b24b70037b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Retention of the female gametophyte with the young embryo on the parent sporophyte begins in some pteridophytes and is the precursor of the seed habit
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Gymnosperms do retain the female gametophyte with the embryo on the sporophyte, so a student who stores retention as 'the seed habit' answers for the group where the seed habit is complete rather than for the group where it is first seen.
- **Why:** This question requires the stated point in the plant sequence at which a feature appears, demonstrated by 'is first observed in' standing against four coordinate plant groups.
<!--/ecat-->

## Q147

Biology · botany · Principles of Inheritance and Variation

In Antirrhinum (Snapdragon), a red flower was crossed with a white flower and in $\mathrm{F_1}$ generation pink flowers were obtained. When pink flowers were selfed, the $\mathrm{F_2}$ generation showed white, red and pink flowers. Choose the incorrect statement from the following :

- (1) This experiment does not follow the Principle of Dominance.
- (2) Pink colour in $\mathrm{F_1}$ is due to incomplete dominance.
- (3) Ratio of $\mathrm{F_2}$ is $\frac{1}{4}$ (Red) : $\frac{2}{4}$ (Pink) : $\frac{1}{4}$ (White)
- **(4)** Law of Segregation does not apply in this experiment

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Red ($RR$) $\times$ white ($rr$) gives pink $Rr$ in $\mathrm{F_1}$: incomplete dominance, so the Principle of Dominance is not followed, and options $1$, $2$ are correct; alleles still segregate, giving $\mathrm{F_2}$ $\frac{1}{4}RR : \frac{2}{4}Rr : \frac{1}{4}rr$ (option $3$ correct), so option $4$, saying segregation does not apply, is the incorrect statement.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q147_d1b8a1b3_28102026.png?v=d1b8a1b3af32)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Incomplete dominance sets aside the law of dominance but leaves segregation intact, which is why the F2 recovers red and white in a 1:2:1
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The principle of dominance is carried as a law that holds in every cross, so the line saying this experiment does NOT follow it reads like the false one; the pink F1 printed in the stem is the condition that suspends dominance here.
- **Why:** This question requires Mendel's principles applied to the cross printed in the stem, demonstrated by 'Law of Segregation does not apply in this experiment' standing against an F2 that 'showed white, red and pink flowers'.
<!--/ecat-->

## Q148

Biology · botany · Respiration in Plants

Conversion of glucose to glucose-6-phosphate, the first irreversible reaction of glycolysis, is catalyzed by

- (1) Aldolase
- **(2)** Hexokinase
- (3) Enolase
- (4) Phosphofructokinase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Glycolysis begins when ATP phosphorylates glucose to glucose-6-phosphate, and the enzyme that catalyses this is $\text{hexokinase}$, which is option $2$.

**Subtopic:** Glycolysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q148_1fb5d261_28102026.png?v=1fb5d2612235)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hexokinase puts the first phosphate on glucose; the other glycolytic kinase, phosphofructokinase, acts two steps later on fructose-6-phosphate
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Phosphofructokinase is the kinase carried as the irreversible, rate-controlling step of glycolysis, so matching the stem's 'first irreversible reaction' to that memory puts the phosphorylation at the wrong step of the pathway.
- **Why:** This question requires the enzyme named for one stated glycolytic step, demonstrated by 'Conversion of glucose to glucose-6-phosphate ... is catalyzed by' printing both the substrate and the product.
<!--/ecat-->

## Q149

Biology · zoology · Human Health and Disease

Drug called ‘Heroin’ is synthesized by

- (1) methylation of morphine
- **(2)** acetylation of morphine
- (3) glycosylation of morphine
- (4) nitration of morphine

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Heroin is chemically diacetylmorphine, formed by acetylation of morphine (extracted from the latex of $Papaver\ somniferum$), which is option $2$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q149_90ed479f_28102026.png?v=90ed479f596e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Heroin is diacetylmorphine, made by acetylating morphine; the methylated derivative of morphine is codeine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Codeine, the methyl derivative, is printed in the same paragraph as heroin, so a student who remembers that morphine is chemically modified to give both reaches for methylation.
- **Why:** This question requires the stated chemistry of one named drug, demonstrated by 'Drug called ‘Heroin’ is synthesized by' with four modifications of morphine as the options.
- **Note:** nearby_fact rather than look_alike_term: swapping 'methylation' and 'acetylation' for two unlike words leaves the pull intact, because what carries it is codeine being printed beside heroin as the other morphine derivative.
<!--/ecat-->

## Q150

Biology · zoology · Reproductive Health

Select the hormone-releasing Intra-Uterine Devices.

- (1) Vaults, LNG-20
- (2) Multiload 375, Progestasert
- **(3)** Progestasert, LNG-20
- (4) Lippes Loop, Multiload 375

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT classes IUDs as non-medicated (Lippes Loop), copper-releasing (CuT, Cu7, Multiload 375) and hormone-releasing (Progestasert, LNG-20); vaults are barrier methods, so the hormone-releasing pair is Progestasert, LNG-20, which is option $3$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q150_eea0f0b1_28102026.png?v=eea0f0b194be)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT splits IUDs into non-medicated, copper releasing and hormone releasing, and only Progestasert and LNG-20 sit in the last class
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Progestasert belongs in the hormone-releasing line and Multiload 375 is the other medicated device, so a student who divides IUDs only into plain and medicated takes both names and the half-wrong pair scores nothing.
- **Why:** This question requires the membership of one named class of IUDs, demonstrated by 'Select the hormone-releasing Intra-Uterine Devices' with options that each pair two device names.
- **Note:** E1 called this plain_mcq, but each option is a pair of device names accepted or rejected whole, so the printed shape is recorded as two_part; 'statements' was ruled out because nothing in it is judged as a statement.
<!--/ecat-->

## Q151

Biology · zoology · Evolution

A gene locus has two alleles A, a. If the frequency of dominant allele A is 0.4, then what will be the frequency of homozygous dominant, heterozygous and homozygous recessive individuals in the population?

- (1) 0.36(AA); 0.48(Aa); 0.16(aa)
- (2) 0.16(AA); 0.24(Aa); 0.36(aa)
- **(3)** 0.16(AA); 0.48(Aa); 0.36(aa)
- (4) 0.16(AA); 0.36(Aa); 0.48(aa)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Allele frequencies sum to one: $q = 1 - p = 1 - 0.4 = 0.6$.
2. Homozygous dominant: $p^2 = (0.4)^2 = 0.16$.
3. Heterozygous: $2pq = 2 \times 0.4 \times 0.6 = 0.48$.
4. Homozygous recessive: $q^2 = (0.6)^2 = 0.36$.
5. $0.16(AA);\ 0.48(Aa);\ 0.36(aa)$ matches option $3$.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q151_d6f96573_28102026.png?v=d6f96573e19b)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Hardy-Weinberg: with allele frequencies $p$ and $q$, the three genotype classes come out as $p^2$, $2pq$ and $q^2$ and must add to 1
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  A student with both homozygote values right fills the middle class in as $pq = 0.4\times0.6 = 0.24$ and drops the 2 from $2pq$; the three frequencies then add to 0.76 instead of 1
- **Why:** This question requires the three genotype frequencies computed from one allele frequency, demonstrated by "If the frequency of dominant allele A is 0.4, then what will be the frequency of homozygous dominant, heterozygous and homozygous recessive individuals".
- **Note:** E1 called this plain_mcq, but each option bundles three values graded whole, which is the shape recorded here as two_part. All three wrong options carry routes and none is filler: the option set is the correct triple with one of its three numbers altered or two of them exchanged.
<!--/ecat-->

## Q152

Biology · both · Biotechnology and Its Applications

Which of the following is true for Golden rice?

- **(1)** It is Vitamin A enriched, with a gene from daffodil
- (2) It is pest resistant, with a gene from Bacillus thuringiensis
- (3) It is drought tolerant, developed using Agrobacterium vector
- (4) It has yellow grains, because of a gene introduced from a primitive variety of rice

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Golden rice is a transgenic rice engineered to produce $\beta$-carotene (provitamin A) in the endosperm, so it is Vitamin A enriched; the phytoene synthase gene came from daffodil, making option $1$ correct while pest resistance (Bt), drought tolerance and a primitive-rice gene do not describe it.

**Subtopic:** Biotechnological Applications in Agriculture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q152_075ff4b3_28102026.png?v=075ff4b3adc8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Golden rice carries a daffodil gene that makes the grain accumulate $\beta$-carotene, so it is vitamin A enriched
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The first half is true and the name of the rice says so — the grains are yellow — and a student who has only that much accepts the second half, which sources the colour from a primitive rice variety instead of from the daffodil gene
- **Why:** This question requires which stated claim holds for one named transgenic crop, demonstrated by "Which of the following is true for Golden rice?" with "It is Vitamin A enriched, with a gene from daffodil".
- **Note:** Every option pairs a trait with a source or technique, so each wrong one has a true half; the trap is placed on the option whose true half is specific to this crop rather than to transgenics in general, which is what makes half_right the mechanism here rather than a bare wrong fact.
<!--/ecat-->

## Q153

Biology · botany · Plant Kingdom

Pinus seed cannot germinate and established without fungal association. This is because :

- (1) its embryo is immature.
- **(2)** it has obligate association with mycorrhizae.
- (3) it has very hard seed coat.
- (4) its seeds contain inhibitors that present germination.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT: Pinus roots have an obligate association with mycorrhizal fungi, so without the fungus the seed cannot germinate and establish; this is option $2$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q153_73c6afe0_28102026.png?v=73c6afe08aa1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Pinus roots carry an obligate mycorrhizal fungus, so the seedling cannot establish without it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Drop the stem's "without fungal association" and the question becomes why a seed fails to germinate, whose first stock answer is a hard, impermeable seed coat; with the condition kept, the reason has to involve the fungus
- **Why:** This question requires the stated reason a named gymnosperm depends on a fungus, demonstrated by "Pinus seed cannot germinate and established without fungal association. This is because :".
- **Note:** E1 called the shape statement_options; the stem is a trailing "because" completed by four short clauses rather than statements to be judged, so mcq is recorded.
<!--/ecat-->

## Q154

Biology · both · Molecular Basis of Inheritance

Which of the following features of genetic code does allow bacteria to produce human insulin by recombinant DNA technology?

- (1) Genetic code is not ambiguous
- (2) Genetic code is redundant
- **(3)** Genetic code is nearly universal
- (4) Genetic code is specific

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The genetic code is nearly universal, so a codon such as $UUU$ codes for phenylalanine in both bacteria and humans; bacteria therefore translate the human insulin gene correctly, which is option $3$.

**Subtopic:** Genetic Code and Its Features · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q154_d15f2d70_28102026.png?v=d15f2d702fb1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The genetic code is nearly universal, so the same triplets specify the same amino acids in a bacterium as in a human cell
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  "Specific" and "universal" are two entries of the same short list of code features, and a student who reads specificity as "the code says exactly the same thing everywhere" takes it for the property that lets E. coli read a human gene; specificity means one codon specifies one amino acid, which says nothing about other organisms
- **Why:** This question requires four co-ordinate features of the genetic code held apart until one is seen to bear on the stem's case, demonstrated by "Which of the following features of genetic code does allow bacteria to produce human insulin" with all four options true of the code.
- **Note:** asks is compare rather than reason_line or fact_line: every option is a true feature of the code, so nothing is recalled or caused here — the work is telling the four look-alike features apart. This is also the one place in this run where compare sits on something that is not a match question. Test applied for look_alike_term against nearby_fact: replace "specific" with an unlike phrase and the pull dies, because what carries it is the word reading as exactness, not its place in the list.
<!--/ecat-->

## Q155

Biology · zoology · Reproductive Health

Which of the following sexually transmitted diseases is not completely curable?

- (1) Gonorrhoea
- (2) Genital warts
- **(3)** Genital herpes
- (4) Chlamydiasis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The textbook says that apart from hepatitis-B, genital herpes and HIV, STIs are completely curable if detected early, so genital herpes (option $3$) is the one that is not completely curable.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q155_fdd5f1f8_28102026.png?v=fdd5f1f82c77)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Of the sexually transmitted infections, hepatitis-B, genital herpes and HIV are the ones not completely curable; the rest respond to early treatment
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  "Genital warts" and "Genital herpes" differ only in the second word, and a student who remembers that the incurable one is a "genital" infection picks the wrong half of the pair; genital warts is printed in the curable list
- **Why:** This question requires which named infection falls outside a stated exception, demonstrated by "Which of the following sexually transmitted diseases is not completely curable?".
- **Note:** Negated task ("not"), so the three wrong options are all true members of the curable list. Test applied for look_alike_term against nearby_fact: both hold, since genital warts is printed in the same sentence as genital herpes, and by the rulebook's tie-break the resemblance wins, so look_alike_term is recorded. Two fillers rather than three forced routes, because nothing in the question separates gonorrhoea from chlamydiasis.
<!--/ecat-->

## Q156

Biology · botany · Biological Classification

Which of the following statements is incorrect?

- (1) Viroids lack a protein coat.
- (2) Viruses are obligate parasites.
- **(3)** Infective constituent in viruses is the protein coat.
- (4) Prions consist of abnormally folded proteins.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Viroids are free RNA without a protein coat, so option $1$ is correct; viruses are obligate parasites, so option $2$ is correct; prions are abnormally folded proteins, so option $4$ is correct; in viruses the nucleic acid is infectious and the protein coat is not, so option $3$ is the incorrect statement.

**Subtopic:** Viruses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q156_90bf1ff4_28102026.png?v=90bf1ff4a652)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a virus the nucleic acid is the infectious part and the protein coat only wraps it; viroids are free RNA and prions are misfolded protein
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  A student who reads "viroid" as a kind of virus gives it a protein coat and so marks this statement as the incorrect one; the viroid was defined by the absence of that coat
- **Why:** This question requires four printed claims about acellular agents graded against the stated facts, demonstrated by "Which of the following statements is incorrect?" with "Infective constituent in viruses is the protein coat" as the false one.
- **Note:** Negated task ("incorrect"), so all three wrong options are true statements. Test applied for look_alike_term against nearby_fact: replace "Viroids" with an unlike word and the pull dies, because what carries it is the viroid-virus resemblance rather than the two agents being described in neighbouring sentences.
<!--/ecat-->

## Q157

Biology · zoology · Animal Kingdom

Match the following organisms with their respective characteristics :
Select the correct option from the following :

| List-I | | List-II | |
|---|---|---|---|
| (a) | Pila | (i) | Flame cells |
| (b) | Bombyx | (ii) | Comb plates |
| (c) | Pleurobrachia | (iii) | Radula |
| (d) | Taenia | (iv) | Malpighian tubules |

- (1) (a) (iii) (b) (ii) (c) (i) (d) (iv)
- **(2)** (a) (iii) (b) (iv) (c) (ii) (d) (i)
- (3) (a) (ii) (b) (iv) (c) (iii) (d) (i)
- (4) (a) (iii) (b) (ii) (c) (iv) (d) (i)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $Pila$ is a mollusc, and molluscs have a file-like rasping feeding organ, the radula: $(a) \to (iii)$.
2. $Bombyx$ is an arthropod (insect), and its excretion is through Malpighian tubules: $(b) \to (iv)$.
3. $Pleurobrachia$ is a ctenophore, which moves using eight external rows of ciliated comb plates: $(c) \to (ii)$.
4. $Taenia$ is a platyhelminth, and its excretion and osmoregulation are done by flame cells: $(d) \to (i)$.
5. The matching $(a)(iii),\ (b)(iv),\ (c)(ii),\ (d)(i)$ is option $2$.

**Subtopic:** Phylum – Ctenophora and Platyhelminthes, Phylum – Arthropoda · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q157_976ad670_28102026.png?v=976ad6704e3c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each phylum's diagnostic organ identifies its example genus: radula for molluscs, Malpighian tubules for insects, comb plates for ctenophores, flame cells for flatworms
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Ctenophora is printed between Coelenterata and Platyhelminthes, so a student who cannot place Pleurobrachia and slides it one phylum along gives it the flame cells, which then pushes Taenia onto the Malpighian tubules and Bombyx onto the comb plates
- **Why:** This question requires each organism matched to the diagnostic feature stated for its group, demonstrated by "Match the following organisms with their respective characteristics" with "Comb plates" and "Flame cells" both on offer.
- **Note:** Test applied for nearby_fact against look_alike_term: replace "comb plates" and "flame cells" with two unlike words and the pull survives, because it rests on Ctenophora and Platyhelminthes being consecutive in the printed phylum sequence rather than on the two names resembling each other.
<!--/ecat-->

## Q158

Biology · both · Molecular Basis of Inheritance

Expressed Sequence Tags (ESTs) refers to :

- **(1)** Genes expressed as RNA
- (2) Polypeptide expression
- (3) DNA polymorphism
- (4) Novel DNA sequences

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the Human Genome Project, the Expressed Sequence Tags (ESTs) approach identifies all the genes that are expressed as RNA, so the answer is option $1$.

**Subtopic:** Human Genome Project · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q158_ab072da1_28102026.png?v=ab072da18e64)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Human Genome Project ran two approaches, and ESTs is the name of the one that went after the genes that are expressed as RNA rather than sequencing the whole genome
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who recalls that HGP had two approaches but not which name belongs to which picks the other approach, sequence annotation, whose business is the novel and non-coding stretches of DNA.
- **Why:** This question requires the stated fact of what one HGP approach is named, demonstrated by the stem 'Expressed Sequence Tags (ESTs) refers to :' and the key option 'Genes expressed as RNA'.
- **Note:** E1_question_type says arrange_in_order ('6 arrange/sequence'), but nothing is printed to sequence and the options are four single terms; the pattern fired on the word 'Sequence' inside the term being defined. Recorded as mcq, which is also where arrange_in_order maps.
<!--/ecat-->

## Q159

Biology · botany · Biological Classification

Which is of the following statements is incorrect?

- (1) Morels and truffles are edible delicacies.
- (2) *Claviceps* is a source of many alkaloids and LSD.
- (3) Conidia are produced exogenously and ascospores endogenously.
- **(4)** Yeasts have filamentous bodies with long thread-like hyphae.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Morels and truffles are edible ascomycetes, so option $1$ is correct.
2. $Claviceps$ yields ergot alkaloids and LSD, so option $2$ is correct.
3. In Ascomycetes conidia form exogenously on conidiophores and ascospores form endogenously in asci, so option $3$ is correct.
4. Yeasts are unicellular fungi without long thread-like hyphae, so option $4$ is incorrect and is the answer.

**Subtopic:** Ascomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q159_fc42bbd6_28102026.png?v=fc42bbd6f86c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Yeasts are unicellular ascomycetes, so the filamentous septate mycelium that the rest of the class shows is exactly what yeast does not have
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who cannot place which ascomycete spore is borne inside a sac and which is borne openly treats the one unfamiliar line in the set as the false one, and strikes the conidia-ascospores line instead of the yeast line.
- **Why:** This question requires the stated fact that yeast is unicellular, demonstrated by option 4 'Yeasts have filamentous bodies with long thread-like hyphae' being the only printed claim NCERT contradicts.
- **Note:** Stem as printed reads 'Which is of the following statements is incorrect?' -- a typo in the paper or in extraction; tagged as printed, task is still the negated one.
<!--/ecat-->

## Q160

Biology · botany · Biological Classification

Match Column - I Column - II
Choose the correct answer from the option given below

| List-I | | List-II | |
|---|---|---|---|
| a | Saprophyte | i | Symbiotic association of fungi with plant roots |
| b | Parasite | ii | Decomposition of dead organic materials |
| c | Lichens | iii | Living on living plants or animals |
| d | Mycorrhiza | iv | Symbiotic association of algae and fungi |

- (1) (i) (ii) (iii) (iv)
- (2) (iii) (ii) (i) (iv)
- (3) (ii) (i) (iii) (iv)
- **(4)** (ii) (iii) (iv) (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Saprophytes feed on dead organic matter, so $a \rightarrow (ii)$.
2. Parasites live on living plants or animals, so $b \rightarrow (iii)$.
3. Lichens are a symbiotic association of algae and fungi, so $c \rightarrow (iv)$.
4. Mycorrhiza is a symbiotic association of fungi with plant roots, so $d \rightarrow (i)$.
5. The sequence $(ii)\,(iii)\,(iv)\,(i)$ is option $4$.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q160_619bd0b1_28102026.png?v=619bd0b1def6)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Four modes of fungal living, with mycorrhiza the fungus-and-root partnership and a lichen the alga-and-fungus one
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Two Column-II lines both open "Symbiotic association of", and a student who takes the algae-and-fungi one for Mycorrhiza is then left to give Lichens the line about living on living plants, which matches their habit of growing on bark
- **Why:** This question requires each mode of living matched to the definition stated for it, demonstrated by the two rival lines "Symbiotic association of fungi with plant roots" and "Symbiotic association of algae and fungi".
- **Note:** Test applied for look_alike_term against nearby_fact: replace the two symbiosis lines with two unlike definitions and the pull dies, so their near-identical wording is carrying it. Checked whether the rows demand compare rather than fact_line: the two symbiosis lines do have to be told apart, but each row still asks only for the definition the book prints for that term, so fact_line holds.
<!--/ecat-->

## Q161

Biology · zoology · Chemical Coordination and Integration

Which of the following glucose transporters is insulin-dependent?

- (1) GLUT I
- (2) GLUT II
- (3) GLUT III
- **(4)** GLUT IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. GLUT IV (GLUT4) in skeletal muscle and adipose tissue moves to the plasma membrane in response to insulin, so it is the insulin-dependent transporter; GLUT I, II and III are insulin-independent, giving option $4$.

**Subtopic:** Pancreas · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q161_37474c5e_28102026.png?v=37474c5e31e3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Insulin works by recruiting GLUT 4 to the membrane of muscle and fat cells; the other glucose transporters move glucose whether insulin is present or not
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who remembers that one GLUT sits in the beta cell and the liver and is the transporter of the insulin story picks GLUT II, which belongs to insulin SECRETION rather than to insulin's action.
- **Why:** This question requires the stated fact of which transporter insulin controls, demonstrated by the stem asking which GLUT 'is insulin-dependent' with the four numbered members of one family as options.
<!--/ecat-->

## Q162

Biology · zoology · Human Health and Disease

Which of the following immune responses is responsible for rejection of kidney graft?

- (1) Auto-immune response
- (2) Humoral immune response
- (3) Inflammatory immune response
- **(4)** Cell-mediated immune response

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Rejection of a transplanted organ such as a kidney graft is due to the body recognising the graft as non-self, and this is brought about by T-lymphocytes, i.e. the cell-mediated immune response (CMI), which is option $4$.

**Subtopic:** Acquired Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q162_b17b7ae8_28102026.png?v=b17b7ae83335)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Graft rejection is the work of T-lymphocytes, so it is the cell-mediated arm of acquired immunity and not the antibody arm
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who holds that immunity against anything foreign means antibodies picks the other half of the pair NCERT prints side by side, the humoral response, because antibody is the word attached to 'foreign'.
- **Why:** This question requires the stated fact of which immune response rejects a graft, demonstrated by the key option naming the 'Cell-mediated immune response' against the 'Humoral immune response' printed beside it.
<!--/ecat-->

## Q163

Biology · zoology · Excretory Products and Their Elimination

Use of an artificial kidney during hemodialysis may result in :
Which of the following options is the most appropriate?

- **(a)** Nitrogenous waste build-up in the body
- **(b)** Non-elimination of excess potassium ions
- **(c)** Reduced absorption of calcium ions from gastro-intestinal tract
- **(d)** Reduced RBC production

- (1) (a) and (b) are correct
- (2) (b) and (c) are correct
- **(3)** (c) and (d) are correct
- (4) (a) and (d) are correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Haemodialysis filters the blood through the dialysing fluid, removing nitrogenous wastes such as urea, so (a) nitrogenous waste build-up is not expected.
2. The dialysing fluid matches plasma except for wastes, so excess $\mathrm{K^+}$ ions are also removed; (b) is not expected.
3. The artificial kidney does not make calcitriol (active vitamin D), so absorption of $\mathrm{Ca^{2+}}$ from the gastro-intestinal tract falls; (c) is correct.
4. The artificial kidney does not secrete erythropoietin, so RBC production falls; (d) is correct.
5. (c) and (d) are correct, which is option $3$.

**Subtopic:** Disorders Of The Excretory System · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 18)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q163_6e3e58f8_28102026.png?v=6e3e58f8010f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Dialysis clears the solutes a kidney excretes but replaces none of its hormone work, so erythropoietin and vitamin-D activation still fail
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Nitrogenous waste build-up and retained potassium are true of untreated kidney failure, and hemodialysis is the procedure that removes exactly those two, so this pair answers what a failing kidney causes rather than what using the machine leaves behind.
- **Why:** This question requires the causal limits of a stated procedure, demonstrated by 'Use of an artificial kidney during hemodialysis may result in' set against (c) and (d), which name kidney functions the machine does not perform.
- **Note:** The calcium-absorption and RBC consequences rest on the kidney's endocrine role rather than on the short printed line about hemodialysis; tagged as printed, with no re-judging of the key.
<!--/ecat-->

## Q164

Biology · zoology · Neural Control and Coordination

> ⚠ The independent solve chose (4); the booklet prints (1).

Which of the following statements is correct?

- **(1)** Cornea is an external, transparent and protective proteinacious covering of the eye-ball.
- (2) Cornea consists of dense connective tissue of elastin and can repair itself.
- (3) Cornea is convex, transparent layer which is highly vascularised.
- (4) Cornea consists of dense matrix of collagen and is the most sensitive portion the eye.

**Answer** — booklet: (1) · independent solve: (4) · differs

**Solved independently** (answer withheld)

1. Option $3$ is false: the cornea is transparent because it is avascular, not highly vascularised.
2. Option $2$ is false: the corneal stroma is dense connective tissue of collagen, not elastin.
3. Option $1$ is false: the cornea is the transparent front part of the outer coat, not a protective proteinaceous covering of the whole eyeball.
4. Option $4$ is true: the cornea is a dense collagen matrix with the densest nerve supply, so it is the most sensitive part of the eye. The answer is option $4$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 18)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q164_c1cd33cf_28102026.png?v=c1cd33cfdcb7)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The cornea is the transparent front of the eye's outer fibrous coat: avascular, made of dense collagenous connective tissue, and it is the eye's protective window
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who remembers that the outer coat of the eyeball is dense connective tissue reads the collagen half of this option as the textbook line and lets it vouch for the second half about sensitivity.
- **Why:** This question requires the stated description of the cornea, demonstrated by all four options describing the same structure and differing only in the clauses attached -- 'elastin', 'highly vascularised', 'most sensitive portion'.
- **Note:** Key is option 1 as printed and the tag follows it, but option 4's two clauses are both defensible outside the textbook line -- the cornea is a dense collagen matrix and is densely innervated -- so the key rests on sticking to the printed description rather than on the subject. Recorded as arguable_key, not re-judged. Option 1's wording 'proteinacious covering' is also unusual and is copied exactly as given.
<!--/ecat-->

## Q165

Biology · both · Principles of Inheritance and Variation

The frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes was explained by :

- (1) T.H. Morgan
- (2) Gregor J. Mendel
- **(3)** Alfred Sturtevant
- (4) Sutton Boveri

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Sturtevant used the recombination frequency between gene pairs on the same chromosome as a measure of the distance between genes and built genetic maps from it, so the answer is option $3$.

**Subtopic:** Linkage & Recombination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q165_f70c09ad_28102026.png?v=f70c09adb4f1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sturtevant turned recombination frequency into map distance and drew the first genetic maps; Morgan's own contribution was showing that linked genes recombine at different rates
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who remembers linkage and recombination as Morgan's chapter picks Morgan, whose name is printed inside the same sentence that introduces Sturtevant as his student.
- **Why:** This question requires the stated attribution of map distance from recombination frequency, demonstrated by the stem quoting almost verbatim 'the frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes'.
<!--/ecat-->

## Q166

Biology · both · Molecular Basis of Inheritance

Match the following genes of the Lac operon with their respective products :
Select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| a | i gene | i | $\beta$-galactosidase |
| b | z gene | ii | Permease |
| c | a gene | iii | Repressor |
| d | y gene | iv | Transacetylase |

- (1) (i) (iii) (ii) (iv)
- (2) (iii) (i) (ii) (iv)
- **(3)** (iii) (i) (iv) (ii)
- (4) (iii) (iv) (i) (ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the lac operon the $i$ gene codes for the repressor, the $z$ gene for $\beta$-galactosidase, the $y$ gene for permease and the $a$ gene for transacetylase, so $a \to iii$, $b \to i$, $c \to iv$, $d \to ii$, which is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q166_ef8bbdc3_28102026.png?v=ef8bbdc3545a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the lac operon the i gene is regulatory and codes the repressor, while z, y and a code $\beta$-galactosidase, permease and transacetylase in that order
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The operon is always written z, y, a against $\beta$-galactosidase, permease, transacetylase, but Column I prints the rows as i, z, a, y; a student reciting the product sequence down the printed rows gets the z gene right and then hands permease to the a gene and transacetylase to the y gene
- **Why:** This question requires each lac operon gene matched to the product stated for it, demonstrated by "Match the following genes of the Lac operon with their respective products".
- **Note:** Test applied for nearby_fact against look_alike_term: replace "Permease" and "Transacetylase" with two unlike words and the pull survives, because it rests on the printed row order (i, z, a, y) running against the remembered z-y-a sequence, not on any resemblance between the product names.
<!--/ecat-->

## Q167

Biology · botany · Plant Growth and Development

It takes very long time for pineapple plants to produce flowers. Which combination of hormones can be applied to artificially induce flowering in pineapple plants throughout the year to increase yield?

- **(1)** Auxin and Ethylene
- (2) Gibberellin and Cytokinin
- (3) Gibberellin and Abscisic acid
- (4) Cytokinin and Abscisic acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT notes that auxins induce flowering in pineapple and that ethylene also promotes flowering in pineapple and helps synchronise fruit set, so the pair is $\text{Auxin and Ethylene}$, which is option $1$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins, Ethylene and Abscisic Acid · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q167_ef0f561b_28102026.png?v=ef0f561bca57)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Auxin and ethylene are the two regulators used on pineapple to force flowering and fruiting out of season; gibberellin, cytokinin and abscisic acid are listed for other jobs
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Gibberellin's own flowering effect, the bolting of a flowering stalk in rosette plants, sits in the same printed list of hormone effects, so a student holding 'gibberellin makes plants flower' takes it and reads cytokinin as the growth partner that goes with it
- **Why:** This question requires the regulator-to-effect pairing the chapter prints, demonstrated by the stem asking which 'combination of hormones can be applied to artificially induce flowering in pineapple plants'.
- **Note:** The options are hormone pairs accepted or rejected whole, so the answer has two halves that must both hold; recorded as two_part, where the pattern's plain_mcq sees only four answers.
<!--/ecat-->

## Q168

Biology · zoology · Digestion and Absorption

Identify the cells whose secretion protects the lining of gastro-intestinal tract from various enzymes.

- (1) Chief Cells
- **(2)** Goblet Cells
- (3) Oxyntic Cells
- (4) Duodenal Cells

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Goblet cells secrete $\text{mucus}$, which lubricates the lining of the gastro-intestinal tract and protects it from enzymes and acid, so the answer is option $2$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q168_d85486f9_28102026.png?v=d85486f984df)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mucus from goblet cells is the coat that keeps the gut's own enzymes and acid off its lining
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The chief cell's secretion is remembered as the inactive proenzyme pepsinogen, and 'secreted inactive so it cannot digest anything yet' reads as protection from enzymes, which is the phrase the stem uses
- **Why:** This question requires the stated secretion of one named cell type, demonstrated by the stem's 'Identify the cells whose secretion protects the lining' set against four cell names with no criterion printed to apply.
<!--/ecat-->

## Q169

Biology · botany · Microbes in Human Welfare

Which of the following can be used as a biocontrol agent in the treatment of plant disease?

- **(1)** Trichoderma
- (2) Chlorella
- (3) Anabaena
- (4) Lactobacillus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\textit{Trichoderma}$ is a free-living fungus in root ecosystems that acts against many plant pathogens, so it is a biocontrol agent (option $1$); $\textit{Chlorella}$, $\textit{Anabaena}$ and $\textit{Lactobacillus}$ are not used for plant disease control.

**Subtopic:** Microbes as Biocontrol Agents · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q169_3bdd2b43_28102026.png?v=3bdd2b43146b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Trichoderma is the free-living fungus named as a biocontrol agent against plant pathogens; the chapter's other microbes are biofertilisers or food microbes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Anabaena is the agriculture microbe printed in the neighbouring section of the same chapter, as a nitrogen-fixing biofertiliser in paddy fields, so a student holding 'microbes put to work in the field' takes the one they can place in a field
- **Why:** This question requires the membership of the printed biocontrol list, demonstrated by the stem's 'can be used as a biocontrol agent in the treatment of plant disease' set against four microbe names.
<!--/ecat-->

## Q170

Biology · botany · Anatomy of Flowering Plants

Phloem in gymnosperms lacks :

- (1) Albuminous cells and sieve cells
- (2) Sieve tubes only
- (3) Companion cells only
- **(4)** Both sieve tubes and companion cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, gymnosperms have albuminous cells and sieve cells in their phloem and lack both sieve tubes and companion cells, which is option $4$.

**Subtopic:** Complex Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q170_c3e50f47_28102026.png?v=c3e50f47a613)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperm phloem conducts through sieve cells with albuminous cells beside them; the sieve tube and its companion cell are angiosperm structures
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The taught contrast is that gymnosperms have sieve cells in place of sieve tubes, so a student who can quote that one substitution marks sieve tubes as the missing element and stops before the second one
- **Why:** This question requires both phloem elements that gymnosperms lack, demonstrated by options 2 and 3 each naming one of them with 'only' while option 4 names both.
- **Note:** half_right rather than nearby_fact because option 2 is a correct but incomplete set, which is rule 5.1's own wording for an option that is true as far as it goes. The options are not uniform pairs, so the shape stays mcq.
<!--/ecat-->

## Q171

Biology · zoology · Human Reproduction

Extrusion of second polar body from egg nucleus occurs :

- **(1)** after entry of sperm but before fertilization
- (2) after fertilization
- (3) before entry of sperm into ovum
- (4) simultaneously with first cleavage

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Sperm entry into the secondary oocyte triggers completion of meiosis II, which releases the second polar body and forms the haploid ootid; only after this do the haploid sperm and ovum nuclei fuse to form the zygote, so the extrusion comes after sperm entry but before fertilization, which is option $1$.

**Subtopic:** Fertilisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q171_ed1fde7c_28102026.png?v=ed1fde7c3513)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The secondary oocyte finishes its second meiotic division only once a sperm is inside it, casting off the second polar body before the two nuclei fuse
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The sentence carried from the chapter is that the fusion of sperm and ovum induces the completion of the secondary oocyte's meiotic division, which places the polar body after fertilisation rather than between sperm entry and fusion
- **Why:** This question requires the stated moment at which the second meiotic division completes, demonstrated by the keyed option's wording 'after entry of sperm but before fertilization', which turns on where sperm entry ends and fertilisation begins.
- **Note:** Tagged as printed. Option 2 is defensible on the chapter's own sentence that the fusion of the gametes induces completion of the meiotic division, so the key rests on reading fertilisation strictly as nuclear fusion; recorded as arguable_key rather than re-judged.
<!--/ecat-->

## Q172

Biology · both · Molecular Basis of Inheritance

Under which of the following conditions will there be no change in the reading frame of following mRNA? $5'\mathrm{AACAGCGGUGCUAUU}3'$

- (1) Insertion of G at $5^{\text{th}}$ position
- (2) Deletion of G from $5^{\text{th}}$ position
- (3) Insertion of A and G at $4^{\text{th}}$ and $5^{\text{th}}$ positions respectively
- **(4)** Deletion of GGU from $7^{\text{th}}$, $8^{\text{th}}$ and $9^{\text{th}}$ positions

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Split the mRNA into triplets from the 5' end: $\mathrm{AAC\,|\,AGC\,|\,GGU\,|\,GCU\,|\,AUU}$.
2. Positions $7,8,9$ are $\mathrm{G,G,U}$, which is exactly the third codon $\mathrm{GGU}$.
3. Deleting $\mathrm{GGU}$ removes $3$ bases (one whole codon): $\mathrm{AAC\,|\,AGC\,|\,GCU\,|\,AUU}$, so the reading frame of the rest is unchanged.
4. Inserting or deleting $1$ base (options $1$, $2$) or inserting $2$ bases (option $3$) changes the number of bases by a non-multiple of $3$, causing a frameshift.
5. Hence the reading frame is unchanged only in option $4$.

**Subtopic:** Effect of Mutation on Genetic Code · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q172_93eccd8a_28102026.png?v=93eccd8a7af3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A reading frame survives an insertion or deletion only when the number of bases added or removed is a multiple of three
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The rule is held as 'one base in or out shifts the frame', so a change involving two bases reads as the exception to it, and this is the only option that is not a single-base change
- **Why:** This question requires the multiple-of-three rule carried to a printed sequence, demonstrated by option 4 removing exactly three bases, 'GGU from 7th, 8th and 9th positions', while every other option changes one or two.
<!--/ecat-->

## Q173

Biology · both · Cell: The Unit of Life

The concept of “Omnis cellula-e cellula” regarding cell division was first proposed by

- **(1)** Rudolf Virchow
- (2) Theodor Schwann
- (3) Schleiden
- (4) Aristotle

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Rudolf Virchow (1855) first explained that new cells arise from pre-existing cells, $\textit{Omnis cellula-e cellula}$, which is option $1$.

**Subtopic:** Cell And Its Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q173_d48a0a44_28102026.png?v=d48a0a44fd3d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Virchow's 'omnis cellula e cellula' added cell division to the cell theory that Schleiden and Schwann had left unexplained
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The Latin dictum is filed under 'the cell theory', and the cell theory is carried as Schleiden and Schwann's, so a student who places the phrase inside the theory hands it to one of its two authors
- **Why:** This question requires the attribution of one printed line, demonstrated by the stem's 'was first proposed by' set against four names with no subject reasoning available to decide between them.
<!--/ecat-->

## Q174

Biology · both · Biotechnology and Its Applications

What triggers activation of protoxin to active Bt toxin of Bacillus thuringiensis in boll worm?

- (1) Body temperature
- (2) Moist surface of midgut
- **(3)** Alkaline pH of gut
- (4) Acidic pH of stomach

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Bt toxin exists as inactive protoxin; once ingested by the insect, the alkaline pH of the gut solubilises the crystals and activates the toxin, which is option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q174_6fafedee_28102026.png?v=6fafedee5d24)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The Bt protoxin is an inactive crystal that the alkaline pH of the insect gut dissolves into the active toxin
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The pH is remembered as what dissolves the crystal, and the only digestive pH a student can quote is the stomach's, so the sense of the scale is flipped to acidic to match it
- **Why:** This question requires the reason printed for the conversion, demonstrated by the stem asking what 'triggers activation of protoxin to active Bt toxin', which the account answers with the alkaline pH of the gut.
- **Note:** nearby_fact was considered for option 4, since it also moves the site from the insect midgut to the stomach, and ruled out: what the question turns on is the sense of the pH, and this option keeps the variable and inverts it.
<!--/ecat-->

## Q175

Biology · zoology · Human Health and Disease

Identify the correct pair representing the causative agent of typhoid fever and the confirmatory test for typhoid.

- (1) Plasmodium vivax / UTI test
- (2) Streptococcus pneumoniae / Widal test
- (3) Salmonella typhi / Anthrone test
- **(4)** Salmonella typhi / Widal test

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Typhoid fever is caused by the bacterium $\textit{Salmonella typhi}$, and the Widal test confirms it, so the correct pair is option $4$.

**Subtopic:** Bacterial Diseases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q175_3500712a_28102026.png?v=3500712a7684)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Typhoid is caused by Salmonella typhi and is confirmed by the Widal test
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The agent is the half that can be quoted, so the two pairs beginning with Salmonella typhi survive and the choice between them is then made on which test name sounds clinical
- **Why:** This question requires both halves of one printed pairing, demonstrated by the stem's 'Identify the correct pair representing the causative agent of typhoid fever and the confirmatory test' and by options 2 and 3 each keeping one half.
- **Note:** The pattern read the four options as full statements; they are agent/test pairs scored whole, so the shape recorded is two_part.
<!--/ecat-->

## Q176

Biology · zoology · Principles of Inheritance and Variation

What is the genetic disorder in which an individual has an overall masculine development gynaecomastia, and is sterile ?

- (1) Turner's syndrome
- **(2)** Klinefelter's syndrome
- (3) Edward syndrome
- (4) Down's syndrome

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. An extra X in a male ($47,\,XXY$, i.e. $44 + XXY$) is Klinefelter's syndrome, which shows overall masculine development, gynaecomastia and sterility, so the answer is option $2$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q176_8b67b252_28102026.png?v=8b67b25220e4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Klinefelter's syndrome is the 47,XXY male, masculine in build but with breast development and sterile; Turner's is the 45,X female
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Turner's and Klinefelter's are learnt as the pair of sex-chromosome disorders and sterility is printed for both, so a student holding the pair but not the signs that separate them takes the other member
- **Why:** This question requires a printed sign list matched to its named disorder, demonstrated by the stem's 'overall masculine development gynaecomastia, and is sterile'.
- **Note:** The likeness test decides the label: Turner and Klinefelter do not resemble each other as words, so what offers option 1 is its position as the other half of the printed pair, which is nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q177

Biology · botany · Environmental Issues

Polyblend, a fine powder of recycled modified plastic, has proved to be a good material for

- (1) Making plastic sacks
- (2) Use as a fertilizer
- **(3)** Construction of roads
- (4) Making tubes and pipes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Polyblend, the fine powder of recycled modified plastic developed by Ahmed Khan, is blended with bitumen and used to lay roads, which is option $3$.

**Subtopic:** Solid Wastes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q177_9b7866d9_28102026.png?v=9b7866d9177d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Polyblend is blended with bitumen to lay roads that stand up to water better than tar alone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The polyblend passage opens by naming its maker as a plastic sack manufacturer, so the phrase 'plastic sack' sits in the same sentence as the material and is carried across to the material's use
- **Why:** This question requires the one printed use of a named material, demonstrated by the stem's 'has proved to be a good material for' set against four unrelated uses.
- **Note:** Two of the three wrong options are fillers because the passage names only one plastic article at all, the manufacturer's sack, and that is where the single route lands.
<!--/ecat-->

## Q178

Biology · botany · Environmental Issues

Which of these following methods is the most suitable for disposal of nuclear waste?

- (1) Shoot the waste into space
- (2) Bury the waste under Antarctic ice-cover
- (3) Dump the waste within rocks under deep ocean
- **(4)** Bury the waste within rocks deep below the Earth's surface

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The NCERT method for disposing of nuclear waste is to pre-treat it, store it in suitable shielded containers and bury it within rocks about $500\,\text{m}$ deep below the Earth's surface, which is option $4$; disposal into space, under Antarctic ice or under the deep ocean is not the method taught.

**Subtopic:** Radioactive Wastes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q178_5c3e5db6_28102026.png?v=5c3e5db632d0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nuclear waste, after pre-treatment, is buried in rock some hundreds of metres below the land surface, because nothing shallower contains the radiation
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The containment half, burial within rocks, is the phrase the recommendation is remembered by, and the sea bed is the remote place disposal stories attach to, so an option carrying both reads as the same recommendation
- **Why:** This question requires the stated disposal recommendation, demonstrated by the stem's 'most suitable for disposal of nuclear waste' and by option 4's 'within rocks deep below the Earth's surface'.
- **Note:** The pattern called this statement_options; the stem asks which method is most suitable rather than which statement is correct, and no lettered block is printed, so the shape recorded is mcq.
<!--/ecat-->

## Q179

Biology · zoology · Chemical Coordination and Integration

Match the following hormones with the respective disease
Select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Insulin | (i) | Addison's disease |
| (b) | Thyroxin | (ii) | Diabetes insipidus |
| (c) | Corticoids | (iii) | Acromegaly |
| (d) | Growth Hormone | (iv) | Goitre |
|  |  | (v) | Diabetes mellitus |

- (1) (a)-(v), (b)-(i), (c)-(ii), (d)-(iii)
- (2) (a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)
- **(3)** (a)-(v), (b)-(iv), (c)-(i), (d)-(iii)
- (4) (a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Insulin deficiency or resistance gives hyperglycaemia, i.e. diabetes mellitus: $(a) \to (v)$.
2. Thyroxin synthesis falls in iodine deficiency, enlarging the thyroid as goitre: $(b) \to (iv)$.
3. Deficient secretion of adrenal corticoids causes Addison's disease: $(c) \to (i)$.
4. Excess growth hormone in adults causes acromegaly: $(d) \to (iii)$.
5. The match $(a)-(v), (b)-(iv), (c)-(i), (d)-(iii)$ is option $3$.

**Subtopic:** Endocrine Disorders · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q179_ff00a96c_28102026.png?v=ff00a96c24fb)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each of these disorders traces to one hormone: insulin to diabetes mellitus, thyroxin to goitre, corticoids to Addison's disease and growth hormone to acromegaly
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Column II prints two diseases whose names both begin "Diabetes", with insipidus at (ii) ahead of mellitus at (v), and a student pairing insulin with the first "Diabetes" they reach takes insipidus; the other three rows of this code are the key's own
- **Why:** This question requires each hormone matched to the disorder the text names for it, demonstrated by Column II printing both "Diabetes insipidus" and "Diabetes mellitus" for four hormones.
- **Note:** Test applied for look_alike_term against nearby_fact: replace "Diabetes insipidus" with an unlike disease name and the pull dies, because nothing else would attach it to insulin, so the shared word is doing the work. Column II holds five entries for four rows, and in the key the unused entry is precisely the look-alike one.
<!--/ecat-->

## Q180

Biology · zoology · Locomotion and Movement

Select the correct option.

- (1) $8^{\mathrm{th}}$, $9^{\mathrm{th}}$ and $10^{\mathrm{th}}$ pairs of ribs articulate directly with the sternum.
- (2) $11^{\mathrm{th}}$ and $12^{\mathrm{th}}$ pairs of ribs are connected to the sternum with the help of hyaline cartilage.
- (3) Each rib is a flat thin bone and all the ribs are connected dorsally to the thoracic vertebrae and ventrally to the sternum.
- **(4)** There are seven pairs of vertebrosternal, three pairs of vertebrochondral and two pairs of vertebral ribs.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The first $7$ pairs of ribs attach ventrally to the sternum through hyaline cartilage, so they are true (vertebrosternal) ribs.
2. Pairs $8$, $9$ and $10$ do not reach the sternum directly; they join the hyaline cartilage of the $7^{\mathrm{th}}$ rib, so they are vertebrochondral (false) ribs, and option $1$ is false.
3. Pairs $11$ and $12$ are not connected ventrally at all; they are floating (vertebral) ribs, so options $2$ and $3$ are false.
4. $7 + 3 + 2 = 12$ pairs: $7$ vertebrosternal, $3$ vertebrochondral, $2$ vertebral, which is option $4$.

**Subtopic:** Axial Skeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/28102026/neet_papers/2019/2019_P1/crops/q180_9ef2d938_28102026.png?v=9ef2d9386d24)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Of the twelve rib pairs the first seven join the sternum directly, the next three join it through the seventh rib's cartilage, and the last two do not reach it at all
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first half of the option is the textbook's own description of a rib -- a thin flat bone joined to the thoracic vertebrae behind and the sternum in front -- and the word 'all' rides in with it, pulling the two floating pairs into a sentence they stand outside
- **Why:** This question requires the counts and the names of the three rib groups, demonstrated by option 4's 'seven pairs of vertebrosternal, three pairs of vertebrochondral and two pairs of vertebral ribs' set against three rival claims about the same ribs.
- **Note:** `statements` rather than mcq: the stem is the bare instruction 'Select the correct option.' and each option is a full claim about the ribs to be graded true or false, which is the printed shape the pattern also read.
<!--/ecat-->

