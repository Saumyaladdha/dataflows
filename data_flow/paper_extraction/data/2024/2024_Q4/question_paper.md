# NEET (UG) 2024 · Code Q4

200 questions · source `NEET_Papers/2024/Set_Q4/NEET_2024_Question_Paper_Q4.pdf` · every image a CDN link (0 without one) · 47 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Electrostatics

A thin spherical shell is charged by some source. The potential difference between the two points $C$ and $P$ (in V) shown in the figure is: (Take $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$ SI units)

![printed figure: Charged thin spherical shell of radius R = 3 cm with centre C and point P on the shell](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q001_ab453eed_29102026.png?v=ab453eedbdfc)

*Charged thin spherical shell of radius R = 3 cm with centre C and point P on the shell*

- (1) $3 \times 10^{5}$
- (2) $1 \times 10^{5}$
- (3) $0.5 \times 10^{5}$
- **(4)** Zero

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For uniformly charged spherical shell,
2. $V = \frac{kq}{R}$ (For $r \le R$)
3. $\therefore\ V_C = V_P$
4. $V_C - V_P = \text{Zero}$

**Solved independently** (answer withheld)

1. For a thin charged spherical shell, $E = 0$ for $r < R$.
2. So the potential is constant inside and equals the surface value: $V_C = V_{surface} = \frac{kq}{R}$.
3. Point $P$ lies on the shell, so $V_P = \frac{kq}{R} = \frac{9 \times 10^{9} \times 10^{-6}}{0.03} = 3 \times 10^{5}\,\text{V}$.
4. $V_C - V_P = 3 \times 10^{5} - 3 \times 10^{5} = 0$, which is option $4$.

**Subtopic:** Potential Due to Linear and Surface Charge Distribution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q001_0660e712_29102026.png?v=0660e712503c)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q001_e1025bd8_29102026.png?v=e1025bd80bdd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The potential is the same everywhere inside and on a charged shell, so the centre and a point on the surface differ by zero volts
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The stem hands over $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$ and the figure hands over $R = 3$ cm and $q = 1\,\mu$C, which are exactly the three numbers $V = \frac{kq}{R}$ needs, and that computation gives $3 \times 10^{5}$ V. It is the potential at P and at C alike, so it answers what the potential is, not what the difference is.
- **Why:** This question requires the shell's interior to be recognised as an equipotential rather than any number to be computed, demonstrated by the stem asking for 'the potential difference between the two points $C$ and $P$' while the figure puts $C$ at the centre and $P$ on the shell of radius $R = 3$ cm.
- **Note:** The stem names neither the radius nor the charge; both come from the figure, which the packet supplies as a drawn spec - a circle of radius R centred on C, a dashed radius ending on the circle at P, and the labels 'R = 3 cm' and 'q = 1 uC'. That is enough to place P on the shell, so the question is tagged as complete rather than figure-blocked.
<!--/ecat-->

## Q2

Physics · Semiconductor Electronics

The output ($Y$) of the given logic gate is similar to the output of an/a

![printed figure: A NAND gate with tied inputs (A) and a NOR gate with tied inputs (B) feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q002_c18a32b2_29102026.png?v=c18a32b272a3)

*A NAND gate with tied inputs (A) and a NOR gate with tied inputs (B) feeding a NOR gate with output Y*

- (1) NAND gate
- (2) NOR gate
- (3) OR gate
- **(4)** AND gate

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: NAND gate (inputs tied to A) and NOR gate (inputs tied to B) feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q002_sol_1_5679940a_29102026.png?v=5679940aa3be)

*NAND gate (inputs tied to A) and NOR gate (inputs tied to B) feeding a NOR gate with output Y*

1. $Y_1 = \overline{A \cdot A} = \overline{A}$
2. $Y_2 = \overline{B + B} = \overline{B}$
3. $Y = \overline{Y_1 + Y_2}$
4. $= \overline{\overline{A} + \overline{B}} = \overline{\overline{A}} \cdot \overline{\overline{B}}$
5. $= A.B$ is similar to output of AND Gate

**Solved independently** (answer withheld)

1. The top NAND gate has both inputs joined to $A$, so its output is $\overline{A \cdot A} = \overline{A}$.
2. The bottom NOR gate has both inputs joined to $B$, so its output is $\overline{B + B} = \overline{B}$.
3. The final NOR gate gives $Y = \overline{\overline{A} + \overline{B}}$.
4. By De Morgan's theorem, $\overline{\overline{A} + \overline{B}} = A \cdot B$.
5. $Y = A \cdot B$ is the AND gate output, which is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q002_27118e6c_29102026.png?v=27118e6c1883)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q002_338b3eed_29102026.png?v=338b3eed2776)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A gate with both its inputs tied to one line acts as an inverter, and a NOR fed by two inverted inputs is an AND by De Morgan's theorem
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Both first-stage gates have their inputs tied, so the final NOR sees $\bar{A}$ and $\bar{B}$ and $Y = \overline{\bar{A} + \bar{B}}$; cancelling the outer bar against the two inner bars, as if inversions simply undo one another, leaves $A + B$ and that is an OR.
- **Why:** This question requires De Morgan's theorem applied to the circuit as drawn, demonstrated by both first-stage gates having their two inputs wired to a single line and the stem asking which gate the output $Y$ 'is similar to'.
- **Note:** The figure is supplied as a drawn spec: an AND body with an output bubble whose two inputs both come from A, an OR body with a bubble whose two inputs both come from B, and a third OR body with a bubble taking those two outputs. That reads as a NAND and a NOR used as inverters feeding a NOR, giving $Y = A \cdot B$, which matches the printed key.
<!--/ecat-->

## Q3

Physics · Wave Optics

If the monochromatic source in Young’s double slit experiment is replaced by white light, then

- (1) Interference pattern will disappear
- (2) There will be a central dark fringe surrounded by a few coloured fringes
- **(3)** There will be a central bright white fringe surrounded by a few coloured fringes
- (4) All bright fringes will be of equal width

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. At central point on screen, path difference is zero for all wavelength.
2. So, central bright fringe is white and other fringes depend on wavelength as $\beta = \frac{\lambda D}{d}$.
3. Therefore, other fringes will be coloured.

**Solved independently** (answer withheld)

1. At the central point the path difference is $\Delta = 0$ for every wavelength, so every colour has a maximum there and the central fringe is bright white.
2. Fringe width $\beta = \frac{\lambda D}{d}$ depends on $\lambda$, so the bright fringes of different colours do not coincide away from the centre and the nearby fringes are coloured (blue nearest, red farther).
3. After a few fringes the colours overlap so much that the pattern washes out, so there is a central bright white fringe surrounded by a few coloured fringes, which is option $3$.

**Subtopic:** Young's Double-Slit Experiment (YDSE) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q003_1d265f99_29102026.png?v=1d265f995ae0)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q003_6cd88125_29102026.png?v=6cd8812510a9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** At the centre of a double-slit pattern every wavelength has zero path difference, so the central fringe is white, while fringe width grows with wavelength on either side
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The coloured fringes on either side are correct and carry the whole sentence, so the one word that fails rides on them; but the centre is where every wavelength arrives in phase, which makes it white, not dark.
- **Why:** This question requires what the double-slit apparatus shows when one component is swapped, demonstrated by the stem's 'If the monochromatic source in Young's double slit experiment is replaced by white light, then' and options that differ over what sits at the centre and whether anything is seen at all.
- **Note:** E1 returned `statement_options`, a retired name. The stem prints no lettered block and does not ask for a statement to be graded correct, so under the current vocabulary the printed shape is a plain MCQ whose options happen to be full clauses.
<!--/ecat-->

## Q4

Physics · Units and Measurements

In a vernier callipers, $(N+1)$ divisions of vernier scale coincide with $N$ divisions of main scale. If $1$ MSD represents $0.1\,\mathrm{mm}$, the vernier constant (in $\mathrm{cm}$) is:

- (1) $\dfrac{1}{10N}$
- **(2)** $\dfrac{1}{100(N+1)}$
- (3) $100N$
- (4) $10(N+1)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $V.C = \mathrm{MSD} - \mathrm{VSD}$ ...(1)
2. given : $(N + 1)\,\mathrm{VSD} = N\,\mathrm{MSD}$
3. $\mathrm{VSD} = \left(\frac{N}{N+1}\right)\mathrm{MSD}$ ...(2)
4. From (1) and (2)
5. $V.C = (\mathrm{MSD}) - \frac{N}{N+1}(\mathrm{MSD})$
6. $= \mathrm{MSD}\left(1 - \frac{N}{N+1}\right) = \frac{\mathrm{MSD}}{N+1}$
7. $= \frac{0.01}{N+1} = \frac{1}{100(N+1)}$

**Solved independently** (answer withheld)

1. $(N+1)\,\mathrm{VSD} = N\,\mathrm{MSD}$, so $1\,\mathrm{VSD} = \frac{N}{N+1}\,\mathrm{MSD}$.
2. $\mathrm{VC} = 1\,\mathrm{MSD} - 1\,\mathrm{VSD} = \left(1 - \frac{N}{N+1}\right)\mathrm{MSD} = \frac{1}{N+1}\,\mathrm{MSD}$.
3. $1\,\mathrm{MSD} = 0.1\,\mathrm{mm} = 0.01\,\mathrm{cm} = \frac{1}{100}\,\mathrm{cm}$.
4. $\mathrm{VC} = \frac{1}{100(N+1)}\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q004_e92e36e4_29102026.png?v=e92e36e44e29)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q004_23361eee_29102026.png?v=23361eeeec10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The vernier constant is one main-scale division minus one vernier division, which equals 1 MSD divided by the number of vernier divisions
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Carrying the familiar least count $= \frac{1\,\mathrm{MSD}}{N}$ instead of building it from the printed coincidence puts $N$ under the 0.1, and leaving that 0.1 in millimetres while the answer is wanted in centimetres prints the result as $\frac{1}{10N}$.
- **Why:** This question requires the least count built from the printed coincidence and then converted to centimetres, demonstrated by the stem's '$(N+1)$ divisions of vernier scale coincide with $N$ divisions of main scale' together with its demand for 'the vernier constant (in cm)'.
<!--/ecat-->

## Q5

Physics · Mechanical Properties of Solids

The maximum elongation of a steel wire of $1\,\mathrm{m}$ length if the elastic limit of steel and its Young’s modulus, respectively, are $8 \times 10^{8}\,\mathrm{N\,m^{-2}}$ and $2 \times 10^{11}\,\mathrm{N\,m^{-2}}$, is:

- **(1)** $4\,\mathrm{mm}$
- (2) $0.4\,\mathrm{mm}$
- (3) $40\,\mathrm{mm}$
- (4) $8\,\mathrm{mm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In the case for maximum elongation,
2. Stress = Elastic limit
3. $\delta_{\mathrm{max}} = \frac{\sigma_{\mathrm{elastic}} \times L}{\text{Young's modulus}} = \frac{8 \times 10^{8} \times 1}{2 \times 10^{11}} = 4 \times 10^{-3}$
4. $= 4\,\mathrm{mm}$
5. i.e. maximum elongation is $4\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. At the elastic limit, $Y = \frac{\sigma}{\Delta L / L}$, so $\frac{\Delta L}{L} = \frac{\sigma}{Y}$.
2. $\frac{\Delta L}{L} = \frac{8 \times 10^{8}}{2 \times 10^{11}} = 4 \times 10^{-3}$.
3. $\Delta L = 4 \times 10^{-3} \times 1\,\mathrm{m} = 4 \times 10^{-3}\,\mathrm{m} = 4\,\mathrm{mm}$, which is option $1$.

**Subtopic:** Hooke's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q005_d6ffabff_29102026.png?v=d6ffabfff655)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q005_1762bcc7_29102026.png?v=1762bcc7fa25)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Maximum elongation is set by the elastic limit: strain is stress divided by Young's modulus, and elongation is that strain times the original length
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  $\frac{8 \times 10^{8}}{2 \times 10^{11}} = 4 \times 10^{-3}$, so the elongation is $4 \times 10^{-3}$ m; converted one prefix short that reads $0.4$ cm, and $0.4$ is printed with mm beside it.
- **Why:** This question requires the strain at the elastic limit multiplied by the length, demonstrated by the stem supplying '$8 \times 10^{8}$ N m$^{-2}$' as the elastic limit against '$2 \times 10^{11}$ N m$^{-2}$' for Young's modulus and asking for 'the maximum elongation'.
- **Note:** E1 returned `multi_part_respectively`. The word 'respectively' here only labels the two supplied constants; one elongation is asked for and each option is a single length, so the printed shape is a plain MCQ, not a multi-part answer.
<!--/ecat-->

## Q6

Physics · Rotational Motion

The moment of inertia of a thin rod about an axis passing through its mid point and perpendicular to the rod is $2400\,\mathrm{g\,cm^{2}}$. The length of the $400\,\mathrm{g}$ rod is nearly:

- **(1)** $8.5\,\mathrm{cm}$
- (2) $17.5\,\mathrm{cm}$
- (3) $20.7\,\mathrm{cm}$
- (4) $72.0\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Moment of inertia of rod $= I = \frac{m\ell^{2}}{12}$
2. $\Rightarrow 2400 = 400\frac{\ell^{2}}{12}$
3. $\Rightarrow 72 = \ell^{2}$
4. $\Rightarrow \ell = \sqrt{72} = 8.48\,\mathrm{cm} \simeq 8.5\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. For a thin rod about a perpendicular axis through its centre, $I = \frac{ML^2}{12}$.
2. $L^2 = \frac{12I}{M} = \frac{12 \times 2400\,\mathrm{g\,cm^2}}{400\,\mathrm{g}} = 72\,\mathrm{cm^2}$.
3. $L = \sqrt{72}\,\mathrm{cm} \approx 8.49\,\mathrm{cm} \approx 8.5\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Moment of Inertia of a Uniform Rod · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q006_b3484cbf_29102026.png?v=b3484cbf25c3)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q006_a1490a4e_29102026.png?v=a1490a4ea197)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a rod about an axis through its centre $I = \frac{mL^{2}}{12}$, so the length comes out of a square root
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  $\frac{12 \times 2400}{400} = 72$ is $L^{2}$, not $L$, and 72.0 is printed in centimetres among the options, so the root is the one operation left untaken.
- **Why:** This question requires $I = \frac{mL^{2}}{12}$ solved for $L$, demonstrated by the stem fixing the axis 'passing through its mid point and perpendicular to the rod' and supplying both $2400\,\mathrm{g\,cm^{2}}$ and the $400\,\mathrm{g}$ mass.
- **Note:** The route to option 3 computes 20.8 cm against the printed 20.7 cm; the stem's 'nearly' is what lets the two be read as the same option, and the gap is recorded rather than smoothed over.
<!--/ecat-->

## Q7

Physics · Magnetic Effect of Electric Current

A tightly wound $100$ turns coil of radius $10\,\mathrm{cm}$ carries a current of $7\,\mathrm{A}$. The magnitude of the magnetic field at the centre of the coil is (Take permeability of free space as $4\pi \times 10^{-7}$ SI units):

- (1) $44\,\mathrm{mT}$
- (2) $4.4\,\mathrm{T}$
- **(3)** $4.4\,\mathrm{mT}$
- (4) $44\,\mathrm{T}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The magnitude of magnetic field due to circular coil of $N$ turns is given by
2. $B_C = \frac{\mu_0 i N}{2R}$
3. $= \frac{4\pi \times 10^{-7} \times 7 \times 100}{2 \times 0.1}$
4. $= 4.4 \times 10^{-3}\,\mathrm{T} = 4.4\,\mathrm{mT}$

**Solved independently** (answer withheld)

1. The field at the centre of a tightly wound coil of $N$ turns is $B = \frac{\mu_0 N I}{2R}$.
2. Substitute $N = 100$, $I = 7\,\mathrm{A}$, $R = 0.1\,\mathrm{m}$: $B = \frac{4\pi \times 10^{-7} \times 100 \times 7}{2 \times 0.1}$.
3. $B = 4\pi \times 3.5 \times 10^{-4}\,\mathrm{T} = 4.398 \times 10^{-3}\,\mathrm{T}$.
4. $B \approx 4.4\,\mathrm{mT}$, which is option $3$.

**Subtopic:** Magnetic Field on the Axis of a Circular Current Loop · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q007_de31ee8b_29102026.png?v=de31ee8beb11)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q007_62ee9b0a_29102026.png?v=62ee9b0acb24)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Field at the centre of a circular coil, $B=\frac{\mu_0 N I}{2R}$, with the radius put in metres
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The radius is printed in centimetres and the formula needs metres, so a student who converts $10\,\mathrm{cm}$ to $0.01\,\mathrm{m}$ gets $B=\frac{4\pi\times10^{-7}\times100\times7}{2\times0.01}=4.4\times10^{-2}\,\mathrm{T}$, which is printed as $44\,\mathrm{mT}$.
- **Why:** This question requires computing a field from a stated relation with the length converted to SI, demonstrated by the stem printing '$100$ turns', 'radius $10\,\mathrm{cm}$', '$7\,\mathrm{A}$' and the value of $\mu_0$, and asking for 'the magnitude of the magnetic field at the centre of the coil'.
<!--/ecat-->

## Q8

Physics · Work, Energy and Power

At any instant of time $t$, the displacement of any particle is given by $2t-1$ (SI unit) under the influence of force of $5\,\mathrm{N}$. The value of instantaneous power is (in SI unit):

- **(1)** $10$
- (2) $5$
- (3) $7$
- (4) $6$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $x = 2t - 1$
2. $v = \frac{dx}{dt} = 2\,\mathrm{m\,s^{-1}}$
3. $P = F.\,v$
4. $= 2 \times 5 = 10\,\mathrm{W}$

**Solved independently** (answer withheld)

1. Velocity is the time derivative of displacement: $v = \frac{dx}{dt} = \frac{d}{dt}(2t - 1) = 2\,\mathrm{m\,s^{-1}}$.
2. Instantaneous power $P = F v = 5\,\mathrm{N} \times 2\,\mathrm{m\,s^{-1}} = 10\,\mathrm{W}$, which is option $1$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q008_dba68ee1_29102026.png?v=dba68ee19e94)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q008_a9c371da_29102026.png?v=a9c371dabe2e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Instantaneous power is force times instantaneous velocity, and velocity is the time derivative of the displacement
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The stem prints a function of $t$ but never a value of $t$, so a student who does not differentiate substitutes $t=1\,\mathrm{s}$ into $2t-1$, gets $1\,\mathrm{m}$ and multiplies the force by it, $5\times1=5$ -- which is force times displacement, not force times velocity.
- **Why:** This question requires differentiating the printed displacement and multiplying by the force, demonstrated by 'the displacement of any particle is given by $2t-1$' being paired with 'the value of instantaneous power'.
<!--/ecat-->

## Q9

Physics · Work, Energy and Power

Two bodies $A$ and $B$ of same mass undergo completely inelastic one dimensional collision. The body $A$ moves with velocity $v_1$ while body $B$ is at rest before collision. The velocity of the system after collision is $v_2$. The ratio $v_1 : v_2$ is

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $4 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Before collision $\Rightarrow$

![printed figure: Before collision: body A moving with velocity v1, body B at rest](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q009_sol_1_43fa7cb9_29102026.png?v=43fa7cb9cc6a)

*Before collision: body A moving with velocity v1, body B at rest*

2. It undergoes completely inelastic collision
3. Using conservation of linear momentum
4. Initial momentum = Final momentum
5. $\Rightarrow mv_1 = mv_2 + mv_2$
6. $\Rightarrow mv_1 = 2mv_2$
7. $\Rightarrow \frac{v_1}{v_2} = \frac{2}{1}$

**Solved independently** (answer withheld)

1. Linear momentum is conserved in the collision: $m v_1 + m(0) = (m + m) v_2$.
2. $v_2 = \frac{v_1}{2}$.
3. $v_1 : v_2 = 2 : 1$, which is option $2$.

**Subtopic:** Problems on Inelastic Collision · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q009_f6aa4423_29102026.png?v=f6aa442300e7)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q009_318df2cb_29102026.png?v=318df2cb3c93)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Momentum is conserved in a perfectly inelastic collision, so equal masses sticking together move at half the incoming speed
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Momentum conservation gives $v_2=\frac{v_1}{2}$, and a student who writes the sentence 'the velocity after the collision is half' straight into a ratio reads off $1:2$, which is the order the stem did not ask for.
- **Why:** This question requires the factor by which the speed changes when the moving body sticks to an equal resting mass, demonstrated by the answer being asked as 'The ratio $v_1 : v_2$' with no numerical data printed.
<!--/ecat-->

## Q10

Physics · Laws of Motion

A horizontal force $10\,\mathrm{N}$ is applied to a block $A$ as shown in figure. The mass of blocks $A$ and $B$ are $2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively. The blocks slide over a frictionless surface. The force exerted by block $A$ on block $B$ is :

![printed figure: Horizontal force F = 10 N pushing block A (2 kg) against block B (3 kg) on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q010_d95173d5_29102026.png?v=d95173d55fe5)

*Horizontal force F = 10 N pushing block A (2 kg) against block B (3 kg) on a frictionless floor*

- (1) Zero
- (2) $4\,\mathrm{N}$
- **(3)** $6\,\mathrm{N}$
- (4) $10\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $F = (M_1 + M_2)a$
2. $a = \frac{10}{2+3} = 2\,\mathrm{m\,s^{-2}}$
3. $F' = M_2(2) = 3 \times 2\,\mathrm{N} = 6\,\mathrm{N}$

**Solved independently** (answer withheld)

1. The surface is frictionless and $F$ pushes $A$ into $B$, so both blocks move together with a common acceleration.
2. $a = \frac{F}{m_A + m_B} = \frac{10\,\mathrm{N}}{(2+3)\,\mathrm{kg}} = 2\,\mathrm{m\,s^{-2}}$.
3. The only horizontal force on $B$ is the contact force from $A$: $N = m_B a = 3\,\mathrm{kg} \times 2\,\mathrm{m\,s^{-2}} = 6\,\mathrm{N}$, which is option $3$.

**Subtopic:** Block Problem · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q010_9b921be9_29102026.png?v=9b921be98cfb)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q010_e377ddf8_29102026.png?v=e377ddf86ab3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Contact force between two pushed blocks: get the common acceleration from the pair, then apply $F=ma$ to the block being pushed
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The common acceleration is $a=\frac{10}{2+3}=2\,\mathrm{m\,s^{-2}}$, and a student who then applies $F=ma$ to the block the hand is pushing instead of to the block being pushed gets $2\times2=4\,\mathrm{N}$ -- the right law cut at the wrong block.
- **Why:** This question requires the common acceleration of the pair followed by $F=ma$ on the rear block, demonstrated by 'The blocks slide over a frictionless surface' and the task 'The force exerted by block $A$ on block $B$'.
- **Note:** E1's pattern recorded multi_part_respectively, but the word 'respectively' sits in the premise -- 'The mass of blocks $A$ and $B$ are $2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively' -- while the task asks for one force and each option is a single value, so the printed shape is mcq. The figure spec supplied with the question matches the stem: $F=10\,\mathrm{N}$ on the $2\,\mathrm{kg}$ block, in contact with the $3\,\mathrm{kg}$ block.
<!--/ecat-->

## Q11

Physics · Gravitation

The mass of a planet is $\frac{1}{10}^{\text{th}}$ that of the earth and its diameter is half that of the earth. The acceleration due to gravity on that planet is:

- (1) $19.6\,\mathrm{m\,s^{-2}}$
- (2) $9.8\,\mathrm{m\,s^{-2}}$
- (3) $4.9\,\mathrm{m\,s^{-2}}$
- **(4)** $3.92\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $g' = \frac{GM'}{R'^{2}} = \frac{GM}{10\left(\frac{R}{2}\right)^{2}}$
2. $= \frac{4}{10}\frac{GM}{R^{2}} = 0.4 \times 9.8$
3. $= 3.92\,\mathrm{m\,s^{-2}}$

**Solved independently** (answer withheld)

1. $g = \frac{GM}{R^2}$ on any planet of mass $M$ and radius $R$.
2. Half the diameter means half the radius: $R' = \frac{R}{2}$, and $M' = \frac{M}{10}$.
3. $g' = \frac{G(M/10)}{(R/2)^2} = \frac{4}{10}\frac{GM}{R^2} = 0.4\,g$.
4. $g' = 0.4 \times 9.8 = 3.92\,\mathrm{m\,s^{-2}}$, which is option $4$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q011_a6831cac_29102026.png?v=a6831cac96b9)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q011_03efa39a_29102026.png?v=03efa39aedfa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Surface gravity $g=\frac{GM}{R^2}$ scales as mass over the square of the radius
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  'Half that of the earth' is the one comparison printed in plain words, and a student who carries that halving straight onto $g$ writes $\frac{9.8}{2}=4.9$. Size enters $g=\frac{GM}{R^2}$ squared and in the denominator, so halving the diameter multiplies $g$ by four rather than halving it.
- **Why:** This question requires scaling $g=\frac{GM}{R^2}$ by two stated factors, demonstrated by 'The mass of a planet is $\frac{1}{10}^{\text{th}}$ that of the earth and its diameter is half that of the earth'.
<!--/ecat-->

## Q12

Physics · Semiconductor Electronics

Consider the following statements A and B and identify the correct answer:

![printed figure: I-V axes with the four quadrants marked (I) to (IV)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q012_a3307c07_29102026.png?v=a3307c071997)

*I-V axes with the four quadrants marked (I) to (IV)*

- **(A)** For a solar-cell, the I-V characteristics lies in the IV quadrant of the given graph.
- **(B)** In a reverse biased $pn$ junction diode, the current measured in $(\mu\mathrm{A})$, is due to majority charge carriers.

- **(1)** A is correct but B is incorrect
- (2) A is incorrect but B is correct
- (3) Both A and B are correct
- (4) Both A and B are incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A: Solar cell characteristics

![printed figure: I-V characteristic of a solar cell in the fourth quadrant, from I_SC on the current axis to V_OC on the voltage axis](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q012_sol_1_6a8b2ffe_29102026.png?v=6a8b2ffef17e)

*I-V characteristic of a solar cell in the fourth quadrant, from I_SC on the current axis to V_OC on the voltage axis*

2. B: In reverse biased $pn$ junction diode, the current measured in $(\mu\mathrm{A})$, is due to minority charge carrier.

**Solved independently** (answer withheld)

1. A solar cell delivers power to the load, so its $I$-$V$ characteristic is drawn with $V > 0$ and $I < 0$, i.e. in quadrant $\mathrm{IV}$; statement A is correct.
2. In reverse bias the barrier blocks majority carriers, and the small current of order $\mu\mathrm{A}$ is due to drift of minority carriers across the junction; statement B is incorrect.
3. A correct and B incorrect matches option $1$.

**Subtopic:** Special Purpose PN Junction Diodes, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q012_962a6d02_29102026.png?v=962a6d028909)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q012_be35cdb2_29102026.png?v=be35cdb291fc)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A solar cell works in the quadrant where the voltage is positive and the current negative, and the microampere current in a reverse-biased diode is carried by the minority carriers.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The magnitude in statement B is right — a reverse-biased junction really does pass only a few $\mu$A — so a student who checks that part and stops lets the carrier word ride and reads both statements as correct.
- **Why:** This question requires two stated diode facts to be judged as printed, demonstrated by statement B reading 'the current measured in $(\mu\mathrm{A})$, is due to majority charge carriers.'
- **Note:** E1's pattern called this plain_mcq, but the paper prints a labelled block of two statements A and B with verdict options, so the shape recorded here is statements. The figure came through as a printed PNG plus a spec: its current axis is drawn with the arrowhead downward, so the region labelled (IV) is the one with $V$ positive and $I$ negative — the same quadrant the usual convention gives, so statement A reads as correct on either reading of the axes and the figure is confirmatory rather than decisive. That is why asks is fact_line and not read_diagram.
<!--/ecat-->

## Q13

Physics · Ray Optics

A light ray enters through a right angled prism at point $P$ with the angle of incidence $30^\circ$ as shown in figure. It travels through the prism parallel to its base $BC$ and emerges along the face $AC$. The refractive index of the prism is:

![printed figure: A ray enters a right-angled prism ABC at P with 30 degree incidence, travels parallel to base BC and emerges along face AC](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q013_d9d9371f_29102026.png?v=d9d9371f59c4)

*A ray enters a right-angled prism ABC at P with 30 degree incidence, travels parallel to base BC and emerges along face AC*

- (1) $\frac{\sqrt{5}}{4}$
- **(2)** $\frac{\sqrt{5}}{2}$
- (3) $\frac{\sqrt{3}}{4}$
- (4) $\frac{\sqrt{3}}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A ray enters a right-angled prism at 30 degrees, travels parallel to the base and emerges along the hypotenuse face](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q013_sol_1_4ecb96da_29102026.png?v=4ecb96da03d1)

*A ray enters a right-angled prism at 30 degrees, travels parallel to the base and emerges along the hypotenuse face*

1. $A = 90^\circ$
2. In prism, $r_1 + c = A$
3. $r_1 = 90^\circ - c \quad \ldots(1)$
4. $\sin c = \frac{1}{\mu} \Rightarrow \cos c = \frac{\sqrt{\mu^2 - 1}}{\mu}$
5. $\Rightarrow$ Apply Snell's law, on incidence surface
6. $1 \cdot \sin 30^\circ = \mu \sin(r_1) \Rightarrow 1 \times \frac{1}{2} = \mu \times \sin(90^\circ - c)$
7. $\frac{1}{2} = \mu \times \frac{\sqrt{\mu^2 - 1}}{\mu}$
8. On squaring $\frac{1}{4} = \mu^2 - 1$
9. $\Rightarrow \mu^2 = \frac{5}{4} \Rightarrow \mu = \frac{\sqrt{5}}{2}$

**Solved independently** (answer withheld)

1. From the figure the prism angle is $A = 90^\circ$, so the refraction angles inside satisfy $r_1 + r_2 = A = 90^\circ$.
2. Snell's law at face $AB$: $\sin 30^\circ = \mu \sin r_1 \Rightarrow \sin r_1 = \frac{1}{2\mu}$.
3. The ray emerges along face $AC$ (grazing emergence), so $\mu \sin r_2 = \sin 90^\circ = 1 \Rightarrow \sin r_2 = \frac{1}{\mu}$.
4. Since $r_2 = 90^\circ - r_1$, $\cos r_1 = \frac{1}{\mu}$.
5. $\sin^2 r_1 + \cos^2 r_1 = 1 \Rightarrow \frac{1}{4\mu^2} + \frac{1}{\mu^2} = \frac{5}{4\mu^2} = 1$.
6. $\mu = \frac{\sqrt{5}}{2}$, which is option $2$.

**Subtopic:** Prism · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q013_8fd0e051_29102026.png?v=8fd0e051b14f)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q013_75ed46a4_29102026.png?v=75ed46a47355)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Grazing emergence means the ray meets the second face at the critical angle, and in a prism the two internal angles add up to the prism angle
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The geometry gives $\mu^2=\frac{5}{4}$, and a student who takes the root over the numerator only writes $\mu=\frac{\sqrt{5}}{4}$, leaving the $4$ unrooted.
- **Why:** This question requires Snell's law at the entry face combined with the critical-angle condition at the second face, demonstrated by 'it travels through the prism parallel to its base $BC$ and emerges along the face $AC$'.
- **Note:** The figure spec supplied with the question carries the right angle at $A$ and the $30^\circ$ at $P$, which is what the geometry turns on, so the question could be tagged from the packet. Worth recording for a reviewer: all three wrong options are less than $1$, so knowing that a prism's refractive index exceeds $1$ strikes them all out without any geometry; the trap recorded is the one that catches a student who works the algebra through.
<!--/ecat-->

## Q14

Physics · Modern Physics

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below.

- **(Statement I)** Atoms are electrically neutral as they contain equal number of positive and negative charges.
- **(Statement II)** Atoms of each element are stable and emit their characteristic spectrum.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (1) · differs

**Publisher's solution**

1. Statement I is true as atoms are electrically neutral because they contain equal number of positive and negative charges.
2. Statement II is wrong as atom of most of the elements are stable and emit characteristic spectrum. But this statement is not true for every atom.

**Solved independently** (answer withheld)

1. Statement I: an atom has equal numbers of protons ($+e$ each) and electrons ($-e$ each), so $q_{net} = Z(+e) + Z(-e) = 0$. Statement I is correct.
2. Statement II: the NCERT Atoms chapter says that atoms of each element are stable and emit a characteristic spectrum, made of discrete lines unique to the element. Statement II is correct.
3. Both statements are correct, so the answer is option $1$.

**Subtopic:** Alpha-Particle Scattering and Rutherford Nuclear Model of the Atom and Thomson's Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q014_4d8a5d0e_29102026.png?v=4d8a5d0e8c26)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q014_ae8c9848_29102026.png?v=ae8c9848f33d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An atom is neutral because it carries as many protons as electrons; whether every element's atoms are stable emitters of a characteristic spectrum is a separate claim, and the one the key rejects
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Both sentences read like lines out of the Atoms chapter, so a student checking the pair by recognition grants both; Statement I does hold, but the verdict's second half carries 'atoms of each element are stable', and the key rejects that, so the two-part verdict fails on one part
- **Why:** This question requires each printed sentence about the atom to be graded against the fact the textbook states, demonstrated by the four options being only the correct/incorrect verdicts on 'Atoms are electrically neutral as they contain equal number of positive and negative charges' and 'Atoms of each element are stable and emit their characteristic spectrum', with no quantity to compute and no condition supplied to apply.
- **Note:** On a plain reading Statement II states something observed - atoms are stable and each element gives its own spectrum - yet the printed key marks it incorrect; tagged exactly as printed per rulebook section 7, and the key is not re-judged here. A reviewer holding the NTA solution should check which ground it rests on: the quantifier 'atoms of each element', since not every element has stable atoms, or the classical frame of the Rutherford/Thomson section this question is filed under. The 'INCORRECT' recorded in negative_words_seen comes from the standard verdict wording of the options, not from the task, so the task itself reads direct. qtype follows the printed shape, two labelled statements, which matches E1's statement_i_ii; half_right is taken over nearby_fact because the option that pulls is a two-part verdict whose first part, the grant of Statement I, is correct and whose failure is confined to the second.
<!--/ecat-->

## Q15

Physics · Mechanical Properties of Fluids

A thin flat circular disc of radius $4.5\,\mathrm{cm}$ is placed gently over the surface of water. If surface tension of water is $0.07\,\mathrm{N\,m^{-1}}$, then the excess force required to take it away from the surface is

- **(1)** $19.8\,\mathrm{mN}$
- (2) $198\,\mathrm{N}$
- (3) $1.98\,\mathrm{mN}$
- (4) $99\,\mathrm{N}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: A hatched flat disc on the water surface with surface-tension forces T acting upward around its rim](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q015_sol_1_e7dd42a0_29102026.png?v=e7dd42a0944d)

*A hatched flat disc on the water surface with surface-tension forces T acting upward around its rim*

1. Excess force $= T \times 2\pi R$
2. $= \frac{7}{100} \times 2 \times 3.14 \times \frac{4.5}{100}$
3. $= 197.82 \times 10^{-4}$
4. $= 19.8 \times 10^{-3}\,\mathrm{N}$
5. $= 19.8\,\mathrm{mN}$

**Solved independently** (answer withheld)

1. Surface tension acts along the contact line, which is the rim of the disc, so $F = T \times 2\pi r$.
2. $2\pi r = 2\pi \times 0.045\,\mathrm{m} = 0.2827\,\mathrm{m}$.
3. $F = 0.07\,\mathrm{N\,m^{-1}} \times 0.2827\,\mathrm{m} = 1.98 \times 10^{-2}\,\mathrm{N} = 19.8\,\mathrm{mN}$, which is option $1$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q015_ca67c1c1_29102026.png?v=ca67c1c11e18)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q015_c956dfbe_29102026.png?v=c956dfbe234c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Lifting a flat disc off a liquid surface takes a force equal to the surface tension times the contact line it is held by, $F = T \times 2\pi r$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The multiplication ends at $1.98\times10^{-2}$ N, and reading that $10^{-2}$ as the prefix milli puts the student's own digits straight onto option 3 instead of the 19.8 mN they should have written.
- **Why:** This question requires computing a force from surface tension and the wetted perimeter, demonstrated by the stem supplying 'radius $4.5$ cm' and 'surface tension of water is $0.07$ N m$^{-1}$' and asking for 'the excess force required to take it away from the surface'.
<!--/ecat-->

## Q16

Physics · Electromagnetic Induction

In the above diagram, a strong bar magnet is moving towards solenoid-2 from solenoid-1. The direction of induced current in solenoid-1 and that in solenoid-2, respectively, are through the directions:

![printed figure: A bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q016_0bc2d97e_29102026.png?v=0bc2d97e61d6)

*A bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)*

- **(1)** $AB$ and $DC$
- (2) $BA$ and $CD$
- (3) $AB$ and $CD$
- (4) $BA$ and $DC$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Bar magnet moving with velocity v from solenoid-1 (current up, leads A, B) towards solenoid-2 (current down, leads C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q016_sol_1_e5e53c5e_29102026.png?v=e5e53c5e208e)

*Bar magnet moving with velocity v from solenoid-1 (current up, leads A, B) towards solenoid-2 (current down, leads C, D)*

1. North of magnet is moving away from solenoid 1 so end $B$ of solenoid 1 is South and as south of magnet is approaching solenoid 2 so end $C$ of solenoid 2 is South.

**Solved independently** (answer withheld)

1. The magnet has $N$ on the left (facing solenoid-1) and $S$ on the right (facing solenoid-2), and it moves to the right with velocity $v$.
2. Solenoid-1: the $N$ pole moves away, so by Lenz's law the flux decrease is opposed and the near (right) face of solenoid-1 becomes an $S$ pole to attract it.
3. An $S$ face means the induced current is clockwise as seen from the magnet; with the wire rising on the front strokes from $A$, this is current from $A$ to $B$.
4. Solenoid-2: the $S$ pole approaches, so the near (left) face of solenoid-2 becomes an $S$ pole to repel it, i.e. current clockwise as seen from the magnet.
5. Solenoid-2 is viewed from the opposite side but wound the same way, so the current runs from the right lead to the left lead: $D \to C$.
6. Induced currents are $AB$ and $DC$, which is option $1$.

**Subtopic:** Direction of Induced Current · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q016_a4c92964_29102026.png?v=a4c9296464ac)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q016_efba8a0c_29102026.png?v=efba8a0cd436)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lenz's law read twice over: the coil the magnet is leaving works to keep the flux it is losing, the coil it is approaching works to oppose the flux it is gaining, so the two induced currents circulate in opposite senses
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Holding Lenz's law as the one line 'the coil pushes the magnet away', the student makes the near face of both solenoids repel; solenoid-1 is being left behind, so its face has to attract the departing N pole, and that coil alone comes out flipped.
- **Why:** This question requires Lenz's law applied separately to a coil being left and a coil being approached, demonstrated by the stem asking for 'the direction of induced current in solenoid-1 and that in solenoid-2, respectively' while the magnet moves from the one towards the other.
- **Note:** The figure arrives as a picture plus a coordinate spec. The spec places A and C at the left terminals and B and D at the right of two identically drawn solenoids, with the magnet's N pole to the left and v pointing right, which fixes the RELATIVE senses the four options are built on. The winding handedness cannot be recovered from a two-dimensional zigzag, so the absolute A-to-B sense is taken from the printed key and every route above is stated in relative terms.
<!--/ecat-->

## Q17

Physics · Kinematics

A particle moving with uniform speed in a circular path maintains:

- (1) Constant velocity
- (2) Constant acceleration
- (3) Constant velocity but varying acceleration
- **(4)** Varying velocity and varying acceleration

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A particle moving with uniform speed in a circular path maintains varying velocity and varying acceleration.
2. It is because direction of both velocity as well as acceleration will change continuously.

**Solved independently** (answer withheld)

1. Velocity $\vec{v}$ has constant magnitude $v$ but its direction is always tangent to the circle, so $\vec{v}$ changes continuously.
2. Acceleration $\vec{a}$ has constant magnitude $a = \frac{v^2}{r}$ but always points towards the centre, so its direction changes and $\vec{a}$ varies.
3. Both velocity and acceleration vary, which is option $4$.

**Subtopic:** Uniform Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q017_6b4820e8_29102026.png?v=6b4820e88b2d)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q017_1c30d46c_29102026.png?v=1c30d46c7554)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Uniform speed is not uniform velocity: on a circular path both the velocity and the centripetal acceleration keep a fixed magnitude and a direction that turns continuously
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The remembered line 'uniform circular motion has a constant centripetal acceleration $v^2/r$' is recited without its qualifier, but $v^2/r$ fixes only the magnitude while the vector turns with the particle.
- **Why:** This question requires deciding whether two vector quantities stay constant when only the speed is uniform, demonstrated by the stem's 'uniform speed in a circular path' set against options that grade 'velocity' and 'acceleration' as constant or varying.
- **Note:** Ruled out condition_missed on option 2: the stem states no condition that is then dropped, and what fails is the content of the remembered relation, so formula_misused carries it.
<!--/ecat-->

## Q18

Physics · Modern Physics

Match List I with List II.
List I (Spectral Lines of Hydrogen for transitions from)
List II (Wavelengths ($\mathrm{nm}$))
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $n_2 = 3$ to $n_1 = 2$ | I | $410.2$ |
| B | $n_2 = 4$ to $n_1 = 2$ | II | $434.1$ |
| C | $n_2 = 5$ to $n_1 = 2$ | III | $656.3$ |
| D | $n_2 = 6$ to $n_1 = 2$ | IV | $486.1$ |

- (1) A-II, B-I, C-IV, D-III
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-IV, B-III, C-I, D-II
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Energy difference $\Delta E = \frac{hc}{\lambda}$
2. $\therefore \lambda \propto \frac{1}{\Delta E}$
3. $(\Delta E)_{6-2} > (\Delta E)_{5-2} > (\Delta E)_{4-2} > (\Delta E)_{3-2}$
4. $\lambda_{6-2} < \lambda_{5-2} < \lambda_{4-2} < \lambda_{3-2}$
5. A-III, B-IV, C-II, D-I

**Solved independently** (answer withheld)

1. For the Balmer series, $\frac{1}{\lambda} = R\left(\frac{1}{2^2} - \frac{1}{n_2^2}\right)$, so $\lambda$ decreases as $n_2$ increases.
2. $n_2 = 3$: $\frac{1}{\lambda} = \frac{5R}{36}$, $\lambda = \frac{36}{5 \times 1.097\times10^{7}}\,\mathrm{m} \approx 656.3\,\mathrm{nm}$, so A-III.
3. $n_2 = 4$: $\frac{1}{\lambda} = \frac{3R}{16}$, $\lambda \approx 486.1\,\mathrm{nm}$, so B-IV.
4. $n_2 = 5$: $\frac{1}{\lambda} = \frac{21R}{100}$, $\lambda \approx 434.1\,\mathrm{nm}$, so C-II.
5. $n_2 = 6$: $\frac{1}{\lambda} = \frac{2R}{9}$, $\lambda \approx 410.2\,\mathrm{nm}$, so D-I.
6. A-III, B-IV, C-II, D-I is option $2$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q018_fb559ad1_29102026.png?v=fb559ad16e9a)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q018_0534b414_29102026.png?v=0534b41444b3)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In the Balmer series the wavelength falls as the starting level rises: the $3 \to 2$ jump is the smallest energy gap and gives the longest line at 656.3 nm, while the lines crowd down towards 410.2 nm as $n_2$ grows
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who carries the energy-wavelength link the wrong way round reads 'the $6 \to 2$ jump is the biggest' as 'so it gives the biggest wavelength' and hands 656.3 nm to D, and option 1 is the only code with D-III; $E = hc/\lambda$ makes the biggest jump the shortest line, 410.2 nm.
- **Why:** This question requires the Balmer rule that a larger drop to $n_1 = 2$ gives a shorter wavelength, applied to each listed jump so the four printed numbers can be ranked against it, demonstrated by List I carrying only quantum numbers such as "$n_2 = 3$ to $n_1 = 2$" and List II only bare wavelengths, with no value attached to any transition.
- **Note:** asks is apply_rule rather than calculate because all four wavelengths are printed: the rule is applied to rank them and no quantity is produced. A one-pair shortcut exists — 656.3 nm is the $3 \to 2$ line and A-III appears only in option 2 — which is why the distractors have to be read as anchor picks rather than as completed sorts; no distractor reproduces an exact mechanical mapping, each sitting one adjacent interchange away from one.
<!--/ecat-->

## Q19

Physics · Units and Measurements

The quantities which have the same dimensions as those of solid angle are:

- **(1)** strain and angle
- (2) stress and angle
- (3) strain and arc
- (4) angular speed and stress

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Solid angle $d\Omega = \frac{dA}{r^{2}}$ has dimensions $[\mathrm{M^{0}L^{0}T^{0}}]$
2. Strain $= \frac{\Delta l}{l}$ has dimensions $[\mathrm{M^{0}L^{0}T^{0}}]$
3. Angle measured in radians is also dimensionless $[\mathrm{M^{0}L^{0}T^{0}}]$
4. $\theta = \frac{l}{r}$

**Solved independently** (answer withheld)

1. Solid angle $\Omega = \frac{A}{r^2}$, so $[\Omega] = \frac{L^2}{L^2} = [M^0L^0T^0]$ (dimensionless).
2. Strain $= \frac{\Delta L}{L}$, so $[\text{strain}] = [M^0L^0T^0]$.
3. Plane angle $\theta = \frac{s}{r}$, so $[\theta] = [M^0L^0T^0]$.
4. Stress $= \frac{F}{A}$ has $[ML^{-1}T^{-2}]$, arc has $[L]$, angular speed has $[T^{-1}]$; none is dimensionless.
5. Only strain and angle match, which is option $1$.

**Subtopic:** Dimensional Formulae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q019_e6347b77_29102026.png?v=e6347b777174)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q019_5dc79381_29102026.png?v=5dc793811ad2)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Solid angle is an area divided by a length squared, so it is dimensionless, and matching it means naming other pure ratios: strain is a length over a length, a plane angle is an arc over a radius
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Angle is secured first, then 'stress' is accepted for 'strain' because the two words sit a letter apart and are learnt in one breath, but stress is force over area and carries $\mathrm{ML^{-1}T^{-2}}$.
- **Why:** This question requires the dimensional formula of each named quantity checked against a dimensionless solid angle, demonstrated by option 1 'strain and angle' sitting against option 2 'stress and angle'. The swap test decides the trap label: replace 'stress' with an unlike word such as 'momentum' and the option stops attracting, so the resemblance to 'strain', not any printed neighbouring position, is doing the work.
- **Note:** The pattern classifier recorded plain_mcq, but each option is a pair of quantities accepted or rejected whole, with half an option scoring nothing, so the shape recorded here is two_part.
<!--/ecat-->

## Q20

Physics · Wave Optics

An unpolarised light beam strikes a glass surface at Brewster's angle. Then

- (1) The reflected light will be partially polarised.
- (2) The refracted light will be completely polarised.
- (3) Both the reflected and refracted light will be completely polarised.
- **(4)** The reflected light will be completely polarised but the refracted light will be partially polarised.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Unpolarised light incident at Brewster's angle: reflected and refracted rays with polarisation marks](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q020_sol_1_33fdb17b_29102026.png?v=33fdb17b3030)

*Unpolarised light incident at Brewster's angle: reflected and refracted rays with polarisation marks*

1. According to Brewster's law, reflected rays are completely polarized and refracted rays are partially polarized.

**Solved independently** (answer withheld)

1. At Brewster's angle $i_B$, $\tan i_B = n$ and the reflected and refracted rays are perpendicular ($i_B + r = 90^\circ$); the reflected light is completely polarised while the refracted light, which carries the rest of both components, is only partially polarised, which is option $4$.

**Subtopic:** Brewster's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q020_44d7514b_29102026.png?v=44d7514b943a)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q020_ab0c001c_29102026.png?v=ab0c001cfdb2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Brewster's angle is the one incidence at which the reflected beam comes out completely plane-polarised, while the refracted beam keeps both components and is only partially polarised
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The general statement that light reflected off glass is partially polarised is carried straight through, but the stem has pinned the incidence at Brewster's angle, which is precisely the angle where that partial polarisation becomes complete.
- **Why:** This question requires Brewster's condition applied to the reflected and the refracted beam separately, demonstrated by the stem fixing the incidence 'at Brewster's angle' and option 4 grading the two beams one against the other.
- **Note:** The pattern classifier recorded statement_options because every option is a full sentence. The qtype rule keeps this at mcq: the stem prints no lettered block of statements and does not ask which statement is correct.
<!--/ecat-->

## Q21

Physics · Electrostatics

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- **(A)** The potential $(V)$ at any axial point, at $2\,\mathrm{m}$ distance $(r)$ from the centre of the dipole of dipole moment vector $\vec{P}$ of magnitude, $4 \times 10^{-6}\,\mathrm{C\,m}$, is $\pm 9 \times 10^{3}\,V$. (Take $\dfrac{1}{4\pi \epsilon_0} = 9 \times 10^{9}$ SI units)
- **(R)** $V = \pm \dfrac{2P}{4\pi \epsilon_0 r^2}$, where $r$ is the distance of any axial point, situated at $2\,\mathrm{m}$ from the centre of the dipole.

- (1) Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true and R is NOT the correct explanation of A.
- **(3)** A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The potential $V$ at any point, at distance $r$ from centre of dipole $= \frac{KP\cos\theta}{r^{2}}$
2. At axial point where $\theta = 0^{\circ}$, $V = \frac{KP}{r^{2}} = \frac{9 \times 10^{9} \times 4 \times 10^{-6}}{2^{2}} = 9 \times 10^{3}\ \mathrm{V}$
3. At axial point where $\theta = 180^{\circ}$, $V = \frac{-KP}{r^{2}} = -9 \times 10^{3}\ \mathrm{V}$

**Solved independently** (answer withheld)

1. For an axial point far from a short dipole, $V = \pm \dfrac{1}{4\pi\epsilon_0}\dfrac{P}{r^2}$.
2. $V = \pm \dfrac{9 \times 10^{9} \times 4 \times 10^{-6}}{(2)^2} = \pm \dfrac{36 \times 10^{3}}{4}$.
3. $V = \pm 9 \times 10^{3}\,\mathrm{V}$, so Assertion A is true.
4. Reason R states $V = \pm \dfrac{2P}{4\pi\epsilon_0 r^2}$, which has an extra factor $2$ (that factor belongs to the axial field $E = \dfrac{2P}{4\pi\epsilon_0 r^3}$), so R is false.
5. A true and R false is option $3$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q021_b80ceb7c_29102026.png?v=b80ceb7cbe5c)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q021_2bafb5e9_29102026.png?v=2bafb5e97914)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The potential on a dipole's axis is $V=\frac{1}{4\pi\epsilon_0}\frac{P}{r^{2}}$; the factor 2 belongs to the axial field, not to the potential
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  R prints the factor 2 that belongs to the axial field of a dipole, and substituting the stem's numbers into it gives $V=\frac{2\times 9\times 10^{9}\times 4\times 10^{-6}}{2^{2}}=1.8\times 10^{4}$ V, which does not match A's $\pm 9\times 10^{3}$ V, so A is read as the false half.
- **Why:** This question requires computing the axial dipole potential from the printed numbers and then checking the printed relation against that computation, demonstrated by R reading "$V = \pm \frac{2P}{4\pi \epsilon_0 r^2}$" while A's $\pm 9\times 10^{3}$ V is what the same $P$, $r$ and $\frac{1}{4\pi\epsilon_0}$ give without the 2.
- **Note:** All three wrong options carry a route, so none is recorded as filler; the finding is the single misused relation in R, and options 1 and 2 are where that same misremembering lands when the arithmetic is skipped or hedged. The "NOT" and "false" flagged in negative_words_seen are part of the standard assertion-reason option wording, not a negated task.
<!--/ecat-->

## Q22

Physics · Rotational Motion

A wheel of a bullock cart is rolling on a level road as shown in the figure below. If its linear speed is $v$ in the direction shown, which one of the following options is correct ($P$ and $Q$ are any highest and lowest points on the wheel, respectively)?

![printed figure: A spoked wheel rolling on a hatched level road, velocity v to the right, top point P and bottom point Q](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q022_61047b73_29102026.png?v=61047b73b444)

*A spoked wheel rolling on a hatched level road, velocity v to the right, top point P and bottom point Q*

- (1) Point $P$ moves slower than point $Q$
- **(2)** Point $P$ moves faster than point $Q$
- (3) Both the points $P$ and $Q$ move with equal speed
- (4) Point $P$ has zero speed

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In the case of pure rolling,

![printed figure: Rolling wheel: top point P moves at 2v, centre at v, contact point Q at rest](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q022_sol_1_ae6fe0c3_29102026.png?v=ae6fe0c3c177)

*Rolling wheel: top point P moves at 2v, centre at v, contact point Q at rest*

2. The topmost point will have velocity $2v$ while point $Q$ i.e. lowest point will have zero velocity.
3. Hence point $P$ moves faster than point $Q$.

**Solved independently** (answer withheld)

1. Rolling without slipping: $v = \omega R$.
2. Top point $P$: $v_P = v + \omega R = 2v$.
3. Lowest point $Q$ (contact): $v_Q = v - \omega R = 0$.
4. $v_P = 2v > v_Q = 0$, so $P$ moves faster than $Q$, which is option $2$.

**Subtopic:** Rolling Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q022_fd34d6c6_29102026.png?v=fd34d6c681cf)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q022_bd47a9aa_29102026.png?v=bd47a9aa97ab)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** On a wheel rolling without slipping a rim point carries the centre's $v$ plus the spin's $\omega R$, giving $2v$ at the top and zero at the point touching the road
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The stem gives the cart one linear speed $v$, and treating that as the speed of the wheel as a whole makes every point of it move alike; the rolling relation adds $\omega R = v$ on top, forward at the highest point and backward at the contact point.
- **Why:** This question requires ranking the speeds of two rim points under rolling, demonstrated by the stem defining 'P and Q are any highest and lowest points on the wheel, respectively' and the options grading which one 'moves faster'.
- **Note:** The figure is supplied, but the stem itself fixes P as the highest point and Q as the lowest and gives the direction of v in words, so nothing in the answer rests on reading the picture; asks is recorded as compare rather than read_diagram for that reason.
<!--/ecat-->

## Q23

Physics · Oscillations

If $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$ represents the motion of a particle executing simple harmonic motion, the amplitude and time period of motion, respectively, are

- (1) $5\,\mathrm{cm}$, $2\,\mathrm{s}$
- **(2)** $5\,\mathrm{m}$, $2\,\mathrm{s}$
- (3) $5\,\mathrm{cm}$, $1\,\mathrm{s}$
- (4) $5\,\mathrm{m}$, $1\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$
2. Amplitude $= 5\,\mathrm{m}$
3. $\omega = \pi = \frac{2\pi}{T}$
4. $T = \frac{2\pi}{\pi} = 2\,\mathrm{s}$

**Solved independently** (answer withheld)

1. Compare with $x = A\sin(\omega t + \phi)$: $A = 5\,\mathrm{m}$, $\omega = \pi\,\mathrm{rad\,s^{-1}}$.
2. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi} = 2\,\mathrm{s}$.
3. $5\,\mathrm{m}$, $2\,\mathrm{s}$ is option $2$.

**Subtopic:** Calculate Amplitude of SHM, Calculate Time Period of SHM · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q023_62e1791c_29102026.png?v=62e1791cda1a)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q023_c8d74a3b_29102026.png?v=c8d74a3bcaee)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Amplitude and angular frequency are read straight off $x = A\sin(\omega t + \phi)$, and the period follows as $T = 2\pi/\omega$.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Matching the printed $\pi t$ against the standard form $x = A\sin(2\pi t/T + \phi)$ but dropping the 2 gives $\pi/T = \pi$, so $T = 1$ s is printed beside the amplitude that was read correctly.
- **Why:** This question requires reading $A$ and $\omega$ off a printed SHM equation and converting $\omega$ into a period, demonstrated by the stem's '$x = 5\sin(\pi t + \pi/3)$ m' and its request for 'the amplitude and time period of motion, respectively'.
- **Note:** E1 called this multi_part_respectively, which the current qtype list carries as two_part. The failing half of option 4 comes from a dropped factor of 2, but the option has two parts and one of them holds, so half_right governs over arithmetic_slip by rule 2.
<!--/ecat-->

## Q24

Physics · Semiconductor Electronics

A logic circuit provides the output $Y$ as per the following truth table : The expression for the output $Y$ is :

![printed figure: Truth table of A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q024_61790026_29102026.svg?v=61790026efb7)

*Truth table of A, B and output Y*

![drawn: Truth table of A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_drawn/q024_question_d14113be_29102026.svg?v=d14113be8eb9)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $A.B+\overline{A}$
- (2) $A.\overline{B}+\overline{A}$
- **(3)** $\overline{B}$
- (4) $B$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Truth table of the logic circuit: inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q024_sol_1_71a5ce58_29102026.svg?v=71a5ce581f05)

*Truth table of the logic circuit: inputs A, B and output Y*

![drawn: Truth table of the logic circuit: inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_drawn/q024_solution_1_d00c5671_29102026.svg?v=d00c56710b37)  
*drawn on the booklet's geometry, checked against its figure spec*

1. According to given truth table, output is independent on value of $A$
2. $\therefore$ Output $Y = \overline{B}$

**Solved independently** (answer withheld)

1. From the table, $Y = 1$ for $(A,B) = (0,0)$ and $(1,0)$, and $Y = 0$ for $(0,1)$ and $(1,1)$.
2. $Y = \overline{A}\,\overline{B} + A\overline{B} = \overline{B}(\overline{A} + A) = \overline{B}$.
3. Option $2$ fails: at $A=0, B=1$, $A\overline{B} + \overline{A} = 0 + 1 = 1 \neq 0$; options $1$ and $4$ also fail at $(0,0)$.
4. So $Y = \overline{B}$, which is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q024_ccc558cd_29102026.png?v=ccc558cd8edf)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q024_e9020351_29102026.png?v=e9020351d31d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Turning a truth table into a Boolean expression: OR the minterms of the rows whose output is 1, then simplify — here the output follows B alone, inverted
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  A student who writes one term per output-1 row but takes the first row from the A column alone writes $\overline{A}$ where that row gives $\overline{A}.\overline{B}$, and the sum $A.\overline{B}+\overline{A}$ is sitting in the options. The dropped $\overline{B}$ makes the expression turn on at $A=0, B=1$, where the table prints 0.
- **Why:** This question requires a stated rule applied to a case with no quantity produced — the output-1 rows turned into minterms and simplified — demonstrated by the stem asking for 'The expression for the output $Y$' from a table whose only data are the 0/1 entries under A, B and Y.
- **Note:** The truth table is supplied as a figure rather than as printed text, so `table_based` / `figure_to_read` is a secondary overlay on a plain MCQ; the primary shape stays mcq because one question is asked and the four options are expressions, with no lettered block. The drawn spec's labels read, top to bottom, (A,B,Y) = (0,0,1), (0,1,0), (1,0,1), (1,1,0), which gives $Y=\overline{B}$ and matches the printed key (3); the row set is the same whichever way round the rows are read, so the key does not depend on the table's orientation. `read_diagram` was considered for `asks` because the data lives in the figure, but the answer is not read off the table — it is constructed from it by Boolean algebra, and the trap sits in that construction, not in the reading.
<!--/ecat-->

## Q25

Physics · Modern Physics

If $c$ is the velocity of light in free space, the correct statements about photon among the following are:
Choose the correct answer from the options given below:

- **(A)** The energy of a photon is $E = h\nu$.
- **(B)** The velocity of a photon is $c$.
- **(C)** The momentum of a photon, $p = \dfrac{h\nu}{c}$.
- **(D)** In a photon-electron collision, both total energy and total momentum are conserved.
- **(E)** Photon possesses positive charge.

- (1) A and B only
- **(2)** A, B, C and D only
- (3) A, C and D only
- (4) A, B, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (A) If $c$ is the velocity of light
2. so, $E = h\nu$ (Energy of photon)
3. (B) Velocity of photon is equal to velocity of light i.e. $c$.
4. (C) $\lambda = \frac{h}{p}$
5. $p = \frac{h}{\lambda}$
6. $p = \frac{h\nu}{c}$
7. (D) In photon-electron collision both total energy and total momentum are conserved.

**Solved independently** (answer withheld)

1. A photon has energy $E = h\nu$, so A is true.
2. In free space every photon travels at $c$, so B is true.
3. A photon's momentum is $p = \frac{E}{c} = \frac{h\nu}{c}$, so C is true.
4. In a photon-electron collision, total energy and total momentum are both conserved, so D is true.
5. Photons are electrically neutral and are not deflected by electric or magnetic fields, so E is false.
6. The true statements are A, B, C and D, which is option $2$.

**Subtopic:** Photon Energy and Number of Photons · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q025_5806e636_29102026.png?v=5806e63691f3)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q025_65b9088d_29102026.png?v=65b9088d303e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The standard photon properties: energy $h\nu$, speed $c$, momentum $h\nu/c$, total energy and total momentum conserved in a collision, and no charge at all.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Three of this option's four items — $E=h\nu$, the speed $c$, and conservation in a photon-electron collision — are printed photon properties, so checking the familiar ones lets E ride in with them; photons are listed as electrically neutral, which falsifies E, and the option has also dropped the true C.
- **Why:** This question requires each printed photon property to be judged as stated, demonstrated by statement E, 'Photon possesses positive charge.'
<!--/ecat-->

## Q26

Physics · Laws of Motion

A bob is whirled in a horizontal plane by means of a string with an initial speed of $\omega$ rpm. The tension in the string is $T$. If speed becomes $2\omega$ while keeping the same radius, the tension in the string becomes:

- (1) $T$
- **(2)** $4T$
- (3) $\frac{T}{4}$
- (4) $\sqrt{2}T$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Bob m on a string of length l whirled about a pivot with angular speed omega; tension T acts along the string towards the pivot](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q026_sol_1_556dbe3c_29102026.png?v=556dbe3cf4e5)

*Bob m on a string of length l whirled about a pivot with angular speed omega; tension T acts along the string towards the pivot*

1. $T = m\ell\omega^{2}$

![printed figure: Bob m on a string of length l whirled at 2ω; tension T′ acts along the string towards the centre](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q026_sol_2_3658bf5f_29102026.png?v=3658bf5f242c)

*Bob m on a string of length l whirled at 2ω; tension T′ acts along the string towards the centre*

2. $T' = m\ell(2\omega)^{2}$
3. $T' = 4T$

**Solved independently** (answer withheld)

1. The string tension supplies the centripetal force: $T = m\omega^2 r$.
2. With the angular speed doubled at the same radius: $T' = m(2\omega)^2 r = 4m\omega^2 r$.
3. $T' = 4T$, which is option $2$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q026_4c969163_29102026.png?v=4c96916347ca)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q026_d9a248ed_29102026.png?v=d9a248edbb20)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At fixed radius the string tension is the centripetal force $m\omega^2 r$, so it goes with the square of the rotation rate.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Reaching for the period form $F = 4\pi^2 m r/T^2$ and reading the doubled rpm as a doubled $T$ divides the force by $2^2$, printing $T/4$ — the exact reciprocal of the right factor.
- **Why:** This question requires knowing how the tension scales when the rotation rate doubles at fixed radius, demonstrated by 'If speed becomes $2\omega$ while keeping the same radius' and by options that are all multiples of $T$ with no number to compute.
<!--/ecat-->

## Q27

Physics · Current Electricity

The terminal voltage of the battery, whose emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$, when connected through an external resistance of $4\,\Omega$ as shown in the figure is:

![printed figure: A 10 V cell with 1 ohm internal resistance (inside a dashed box) driving current through an external 4 ohm resistor](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q027_05c64e6c_29102026.png?v=05c64e6cd463)

*A 10 V cell with 1 ohm internal resistance (inside a dashed box) driving current through an external 4 ohm resistor*

- (1) $4\,\mathrm{V}$
- (2) $6\,\mathrm{V}$
- **(3)** $8\,\mathrm{V}$
- (4) $10\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: A 10 V cell with a 4 ohm and a 1 ohm resistor in one loop, current i](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q027_sol_1_a0bff0fa_29102026.png?v=a0bff0fadfff)

*A 10 V cell with a 4 ohm and a 1 ohm resistor in one loop, current i*

1. Current in circuit $i = \frac{10}{4+1} = 2\,\mathrm{A}$
2. Terminal voltage $= E - iR$
3. $= 10 - 2 \times 1 = 8\,\mathrm{V}$

**Solved independently** (answer withheld)

1. The cell drives current around the single loop through the external $4\,\Omega$ resistor, so the battery is discharging.
2. $I = \frac{E}{R + r} = \frac{10\,\mathrm{V}}{4\,\Omega + 1\,\Omega} = 2\,\mathrm{A}$.
3. $V = E - Ir = 10\,\mathrm{V} - (2\,\mathrm{A})(1\,\Omega) = 8\,\mathrm{V}$, which is option $3$.

**Subtopic:** Terminal Potential Difference · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q027_631d2eba_29102026.png?v=631d2eba60ca)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q027_a939b35b_29102026.png?v=a939b35b17f9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Terminal voltage is the emf less the drop inside the cell, $V = \varepsilon - Ir$, which is the same as $IR$ across the external resistor.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Carrying 'the cell is a 10 V source' into a closed circuit reads the terminal voltage straight off the emf, but $V = \varepsilon$ holds only when no current flows or $r = 0$, and the stem prints $r = 1\,\Omega$ with a 4 Ω path closed across it.
- **Why:** This question requires turning an emf, an internal resistance and an external resistance into a terminal voltage, demonstrated by 'whose emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$ ... external resistance of $4\,\Omega$' against four options that are all voltages.
- **Note:** The figure repeats in a picture the circuit the stem already gives in numbers, so it decorates rather than gates this question. 10 V is also a true statement of the emf, but the pull is the ideal-cell reading used where the stem states $r = 1\,\Omega$, so condition_missed governs rather than answers_other_question.
<!--/ecat-->

## Q28

Physics · Magnetic Effect of Electric Current

In a uniform magnetic field of $0.049\,\mathrm{T}$, a magnetic needle performs 20 complete oscillations in $5$ seconds as shown. The moment of inertia of the needle is $9.8 \times 10^{-6}\,\mathrm{kg\,m^{2}}$. If the magnitude of magnetic moment of the needle is $x \times 10^{-5}\,\mathrm{Am^{2}}$, then the value of '$x$' is :

![printed figure: A magnetic needle NS hung by a thread from a fixed support in a uniform horizontal magnetic field B](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q028_dddab350_29102026.png?v=dddab3503c92)

*A magnetic needle NS hung by a thread from a fixed support in a uniform horizontal magnetic field B*

- (1) $5\pi^{2}$
- (2) $128\pi^{2}$
- (3) $50\pi^{2}$
- **(4)** $1280\pi^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Time period of Oscillation, $T = 2\pi\sqrt{\frac{I}{MB}}$
2. $\Rightarrow \frac{1}{4} = 2\pi\sqrt{\frac{9.8 \times 10^{-6}}{M \times 0.049}}$
3. $\Rightarrow \frac{1}{16} = 4\pi^{2} \times \frac{9.8 \times 10^{-6}}{M \times 49 \times 10^{-3}}$
4. $\Rightarrow M = \frac{4\pi^{2} \times 9.8 \times 10^{-6}}{49 \times 10^{-3}} \times 16$
5. $= \frac{4\pi^{2} \times 9.8 \times 16 \times 10^{-3}}{49}$
6. $= 12.8\pi^{2} \times 10^{-3} \times 10^{-2} \times 10^{2} = 1280\pi^{2} \times 10^{-5}\,\mathrm{Am^{2}}$

**Solved independently** (answer withheld)

1. Period: $T = \frac{5\,\mathrm{s}}{20} = 0.25\,\mathrm{s}$.
2. For a needle oscillating in a uniform field, $T = 2\pi\sqrt{\frac{I}{mB}}$.
3. Rearranging, $m = \frac{4\pi^{2} I}{B T^{2}}$.
4. $B T^{2} = 0.049 \times 0.0625 = 3.0625 \times 10^{-3}$.
5. $\frac{I}{B T^{2}} = \frac{9.8 \times 10^{-6}}{3.0625 \times 10^{-3}} = 3.2 \times 10^{-3}$.
6. $m = 4\pi^{2} \times 3.2 \times 10^{-3} = 1.28 \times 10^{-2}\pi^{2} = 1280\pi^{2} \times 10^{-5}\,\mathrm{A\,m^{2}}$.
7. So $x = 1280\pi^{2}$, which is option $4$.

**Subtopic:** The Dipole in a Uniform Magnetic Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q028_dd24a4c4_29102026.png?v=dd24a4c44a9c)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q028_7fa6aa22_29102026.png?v=7fa6aa220d84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A magnetic needle swinging in a uniform field is a dipole oscillator, $T = 2\pi\sqrt{I/mB}$, so the magnetic moment follows from the measured period.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Forming the period as oscillations over seconds gives $T = 20/5 = 4$ s instead of $5/20 = 0.25$ s, and feeding 4 s into $m = 4\pi^2 I/(T^2 B)$ returns exactly $5\pi^2 \times 10^{-5}$.
- **Why:** This question requires a period extracted from a count of oscillations and fed into the dipole-oscillation formula to return a magnetic moment, demonstrated by '20 complete oscillations in $5$ seconds' and 'the magnitude of magnetic moment of the needle is $x \times 10^{-5}$'.
- **Note:** The figure shows the needle hung in the field and carries no quantity the stem does not already print, so it decorates rather than gates the question.
<!--/ecat-->

## Q29

Physics · Current Electricity

A wire of length '$l$' and resistance $100\,\Omega$ is divided into 10 equal parts. The first 5 parts are connected in series while the next 5 parts are connected in parallel. The two combinations are again connected in series. The resistance of this final combination is:

- (1) $26\,\Omega$
- **(2)** $52\,\Omega$
- (3) $55\,\Omega$
- (4) $60\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A wire of length l shown as a thick bar with a double-headed dimension arrow above it](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q029_sol_1_6f160677_29102026.png?v=6f1606773ccd)

*A wire of length l shown as a thick bar with a double-headed dimension arrow above it*

1. Divided into 10 parts
2. $R = \frac{\rho l}{A}$
3. $R' = \frac{\rho l}{10A} = \frac{R}{10}$
4. $R_S = 5 \times \frac{R}{10}$ [series]
5. $R_S = 50$
6. $R_P = \frac{R}{50}$ [parallel]
7. $R_{\mathrm{eq}} = R_S + R_P$
8. $= 52\,\Omega$

**Solved independently** (answer withheld)

1. Each of the 10 equal parts has resistance $r = \frac{100\,\Omega}{10} = 10\,\Omega$.
2. Five parts in series: $R_s = 5r = 50\,\Omega$.
3. Five parts in parallel: $R_p = \frac{r}{5} = 2\,\Omega$.
4. The two combinations in series: $R = R_s + R_p = 50 + 2 = 52\,\Omega$, which is option $2$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q029_2afab118_29102026.png?v=2afab1187e79)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q029_68f7ca65_29102026.png?v=68f7ca6516ef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Equal resistors give $nR$ in series and $R/n$ in parallel, and each of ten equal parts of a wire carries a tenth of its resistance.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The stored rule 'equal resistors in parallel halve' is the two-resistor result, and applied to five parts it makes the parallel block 5 Ω instead of 2 Ω, which added to the series block's 50 Ω prints 55 Ω.
- **Why:** This question requires equal sub-resistances combined in series and then in parallel and the two blocks added, demonstrated by 'The first 5 parts are connected in series while the next 5 parts are connected in parallel' and 'The two combinations are again connected in series'.
- **Note:** The length $l$ is printed but never used; the 100 Ω alone decides the answer.
<!--/ecat-->

## Q30

Physics · Magnetic Effect of Electric Current

Match List-I with List-II.
List-I (Material) | List-II (Susceptibility ($\chi$))
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| A | Diamagnetic | I | $\chi = 0$ |
| B | Ferromagnetic | II | $0 > \chi \geq -1$ |
| C | Paramagnetic | III | $\chi >> 1$ |
| D | Non-magnetic | IV | $0 < \chi < \varepsilon$ (a small positive number) |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-II, B-I, C-III, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (Material) | (Susceptibility ($\chi$))
2. Diamagnetic | (II) | $0 > \chi \geq -1$
3. Ferromagnetic | (III) | $\chi >> 1$
4. Paramagnetic | (IV) | $0 < \chi < \varepsilon$
5. Non-magnetic | (I) | $\chi = 0$

**Solved independently** (answer withheld)

1. Diamagnetic materials have small negative susceptibility, $-1 \leq \chi < 0$, so A-II.
2. Ferromagnetic materials have very large positive susceptibility, $\chi \gg 1$, so B-III.
3. Paramagnetic materials have small positive susceptibility, $0 < \chi < \varepsilon$, so C-IV.
4. Non-magnetic materials have $\chi = 0$, so D-I.
5. A-II, B-III, C-IV, D-I is option $1$.

**Subtopic:** Magnetism and Matter · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q030_d262a206_29102026.png?v=d262a206f51a)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q030_4f52016d_29102026.png?v=4f52016db07c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Susceptibility sorts materials by sign and size: diamagnetic is weakly negative, paramagnetic weakly positive, ferromagnetic $\chi >> 1$, and $\chi = 0$ is the non-magnetic case
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Fixing ferromagnetic at $\chi >> 1$ and non-magnetic at $\chi = 0$ leaves the two weak classes, and a student who remembers only that diamagnetic and paramagnetic susceptibilities are both tiny attaches the minus sign to the wrong one; the minus sign records that a diamagnet is pushed out of the field, not pulled in.
- **Why:** This question requires the susceptibility range NCERT states for each class of material, demonstrated by List II printing those ranges as the fixed lines "$0 > \chi \geq -1$", "$\chi >> 1$" and "$0 < \chi < \varepsilon$ (a small positive number)" with no sample, field or measurement given to work from.
- **Note:** Tie-break on the trap: half_right could be claimed because option 4 holds two correct rows and two wrong ones, but that is true of almost every match-code distractor and names nothing. What option 4 inverts is the sign relation itself — which of the two weakly magnetic classes carries the negative $\chi$ — so reversed is the informative label. The "not" clause under reversed concerns one swapped pair inside an ordering, and this is a pairing, not an order. The non-magnetic row ($\chi = 0$) is not in NCERT's three-row table, so that pairing is reached by the definition rather than off the table.
<!--/ecat-->

## Q31

Physics · Modern Physics

$\mathrm{{}^{290}_{82}X \xrightarrow{\alpha} Y \xrightarrow{e^{+}} Z \xrightarrow{\beta^{-}} P \xrightarrow{e^{-}} Q}$
In the nuclear emission stated above, the mass number and atomic number of the product $Q$ respectively, are

- (1) $280, 81$
- (2) $286, 80$
- (3) $288, 82$
- **(4)** $286, 81$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{{}^{290}_{82}X \xrightarrow{\alpha} {}^{286}_{80}Y \xrightarrow{e^{+}} {}^{286}_{79}Z \xrightarrow{\beta^{-}} {}^{286}_{80}P \xrightarrow{e^{-}} {}^{286}_{81}Q}$
2. $A \rightarrow 286$
3. $Z = 81$

**Solved independently** (answer withheld)

1. Alpha emission lowers $A$ by 4 and $Z$ by 2: ${}^{290}_{82}X \to {}^{286}_{80}Y$.
2. Positron ($e^{+}$) emission keeps $A$ and lowers $Z$ by 1: ${}^{286}_{80}Y \to {}^{286}_{79}Z$.
3. $\beta^{-}$ emission keeps $A$ and raises $Z$ by 1: ${}^{286}_{79}Z \to {}^{286}_{80}P$.
4. Electron ($e^{-}$) emission keeps $A$ and raises $Z$ by 1: ${}^{286}_{80}P \to {}^{286}_{81}Q$.
5. So $Q$ has $A = 286$, $Z = 81$, which is option $4$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q031_af2668cf_29102026.png?v=af2668cfe68a)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q031_38397119_29102026.png?v=38397119ac59)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Mass number and charge are conserved along a decay chain: an alpha takes away $(4, 2)$, an emitted electron raises the atomic number by one and an emitted positron lowers it by one.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  286 and 80 is a true pair on this chain, reached at Y and again at P, so netting the positron against the beta or losing count of the arrows prints a stage the stem did not ask for.
- **Why:** This question requires mass number and charge carried through four printed emissions and both reported for the final product, demonstrated by the scheme's four arrows and by 'the mass number and atomic number of the product $Q$ respectively, are'.
- **Note:** E1 read this as reaction_scheme, which the current qtype list does not carry; the printed shape is a decay scheme whose answer is two numbers given together, so two_part is recorded. The final $e^-$ arrow is treated by the printed key as an emitted electron, raising the atomic number to 81; read instead as electron capture it would give 286, 79, which is not among the options. Tagged as printed.
<!--/ecat-->

## Q32

Physics · Modern Physics

The graph which shows the variation of $\left(\frac{1}{\lambda^{2}}\right)$ and its kinetic energy, $E$ is (where $\lambda$ is de Broglie wavelength of a free particle):

- (1) ![printed figure: Graph of 1/lambda^2 against E: a curve rising from O, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q032_option_1_9dcd8352_29102026.png?v=9dcd83524b4a) *Graph of 1/lambda^2 against E: a curve rising from O, concave upward*
- (2) ![printed figure: Graph of 1/lambda^2 against kinetic energy E: a curve falling steeply then flattening (hyperbola-like)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q032_option_2_9235cf85_29102026.png?v=9235cf85888c) *Graph of 1/lambda^2 against kinetic energy E: a curve falling steeply then flattening (hyperbola-like)*
- (3) ![printed figure: Graph of 1/lambda^2 against kinetic energy E: a curve rising from the origin O, steep at first and then flattening](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q032_option_3_66f57221_29102026.png?v=66f5722157ff) *Graph of 1/lambda^2 against kinetic energy E: a curve rising from the origin O, steep at first and then flattening*
- **(4)** ![printed figure: Graph of 1/lambda^2 against E: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q032_option_4_6cd042c5_29102026.png?v=6cd042c58e3c) *Graph of 1/lambda^2 against E: a straight line rising from the origin O*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. de-Broglie wavelength $\lambda = \frac{h}{P} = \frac{h}{mv} = \frac{h}{\sqrt{2\,mE}}$ where $E = \frac{1}{2}mv^{2}$
2. Squaring both sides,
3. $\lambda^{2} = \frac{h^{2}}{4m^{2}E}$
4. $\Rightarrow \frac{1}{\lambda^{2}} = (\text{constant})\,E$
5. Graph passes through origin with constant slope.

**Solved independently** (answer withheld)

1. For a free particle, $E = \frac{p^2}{2m}$, so $p = \sqrt{2mE}$.
2. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mE}}$.
3. $\frac{1}{\lambda^2} = \frac{2mE}{h^2} = \left(\frac{2m}{h^2}\right)E$, so $\frac{1}{\lambda^2} \propto E$.
4. The graph is a straight line through the origin, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q032_b06c055b_29102026.png?v=b06c055b5fe1)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q032_4417d73c_29102026.png?v=4417d73c15bb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** For a free particle $\lambda = h/\sqrt{2mE}$, so $1/\lambda^{2}$ is proportional to the kinetic energy and plots as a straight line through the origin
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are graphs and they reached this step as empty strings, so no wrong curve can be named or checked.
- **Why:** This question requires the de Broglie relation applied to decide the shape of a plot, demonstrated by the stem asking for 'the graph which shows the variation of $\left(\frac{1}{\lambda^{2}}\right)$ and its kinetic energy, $E$'.
- **Note:** The options arrived empty; the stem shows they are graphs, so the printed shape is graph-options, which the qtype axis has no value for and is recorded here as mcq. The paper itself is intact, so this is not source damage, only a reach limit on this step. A reviewer holding the printed options should check whether a curve that rises with falling slope is offered: that is what a student who carries only $\lambda \propto 1/\sqrt{E}$ draws, plotting $1/\lambda$ against $E$ instead of $1/\lambda^{2}$, whereas $1/\lambda^{2} = 2mE/h^{2}$ is a straight line through the origin.
<!--/ecat-->

## Q33

Physics · Alternating Current

In an ideal transformer, the turns ratio is $\frac{N_P}{N_S} = \frac{1}{2}$. The ratio $V_S : V_P$ is equal to (the symbols carry their usual meaning) :

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $1 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to transformer ratio,
2. $\frac{V_S}{V_P} = \frac{N_S}{N_P} = 2 : 1$

**Solved independently** (answer withheld)

1. For an ideal transformer, $\frac{V_S}{V_P} = \frac{N_S}{N_P}$.
2. Given $\frac{N_P}{N_S} = \frac{1}{2}$, so $\frac{N_S}{N_P} = 2$.
3. $\frac{V_S}{V_P} = 2$, i.e. $V_S : V_P = 2 : 1$, which is option $2$.

**Subtopic:** Transformer · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q033_bffe2604_29102026.png?v=bffe2604282a)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q033_0f21cfda_29102026.png?v=0f21cfda9f63)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** In an ideal transformer the voltage across a coil is proportional to its number of turns, so $V_S/V_P = N_S/N_P$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The stem prints the turns ratio the other way up, $N_P/N_S = 1/2$, so carrying '1 : 2' straight across to the voltages answers for $V_P : V_S$ and leaves the asked order inverted.
- **Why:** This question requires the turns ratio converted into the voltage ratio in the order asked, demonstrated by the stem printing '$\frac{N_P}{N_S} = \frac{1}{2}$' and then asking for 'The ratio $V_S : V_P$'.
<!--/ecat-->

## Q34

Physics · Thermodynamics

A thermodynamic system is taken through the cycle $abcda$. The work done by the gas along the path $bc$ is:

![printed figure: P-V cycle abcda: rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q034_90722763_29102026.png?v=90722763327b)

*P-V cycle abcda: rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3*

- **(1)** Zero
- (2) $30\,\mathrm{J}$
- (3) $-90\,\mathrm{J}$
- (4) $-60\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Path $bc$ is an isochoric process.
2. $\therefore$ Work done by gas along path $bc$ is zero.

**Solved independently** (answer withheld)

1. From the figure, $b$ and $c$ both lie at $V = 400\,\mathrm{cm^3}$, so path $bc$ is isochoric.
2. $W_{bc} = \int_b^c P\,dV = 0$ because $dV = 0$, which is option $1$.

**Subtopic:** Isochoric Process · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q034_f12bc54f_29102026.png?v=f12bc54fa0e7)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q034_35cb75fe_29102026.png?v=35cb75fe7da6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A vertical path on a $P$–$V$ diagram is isochoric, and a gas whose volume does not change does no work
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The first sentence names the whole cycle $abcda$, and the enclosed rectangle is $200\,\mathrm{kPa} \times 300\,\mathrm{cm}^{3} = 60\,\mathrm{J}$, negative because the loop runs anticlockwise; that is a true value for the cycle, not for the leg the stem names.
- **Why:** This question requires reading which leg of the printed cycle $bc$ is, demonstrated by the figure placing both $b$ and $c$ at $400\,\mathrm{cm}^{3}$, so that the path is isochoric and the answer is 'Zero'.
- **Note:** The supplied figure spec draws pressure increasing downwards, with the $300\,\mathrm{kPa}$ line below the $100\,\mathrm{kPa}$ line. That orientation does not change which edge is vertical, so the printed key stands; the coordinates used above are $a(100\,\mathrm{cm}^{3},100\,\mathrm{kPa})$, $b(400,100)$, $c(400,300)$, $d(100,300)$.
<!--/ecat-->

## Q35

Physics · Capacitance

In the following circuit, the equivalent capacitance between terminal $A$ and terminal $B$ is :

![printed figure: Five 2 μF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q035_22f54644_29102026.png?v=22f546449df0)

*Five 2 μF capacitors in a bridge between terminals A and B*

- **(1)** $2\,\mu\mathrm{F}$
- (2) $1\,\mu\mathrm{F}$
- (3) $0.5\,\mu\mathrm{F}$
- (4) $4\,\mu\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Five 2 μF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q035_sol_1_2c9eb2c1_29102026.png?v=2c9eb2c152bf)

*Five 2 μF capacitors in a bridge between terminals A and B*

1. Given circuit is balanced Wheatstone bridge

![printed figure: Two branches between A and B, each with two 2 μF capacitors in series](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q035_sol_2_edf92103_29102026.png?v=edf921031d18)

*Two branches between A and B, each with two 2 μF capacitors in series*

2. $C_{AB} = 1 + 1 = 2\,\mu\mathrm{F}$

**Solved independently** (answer withheld)

1. The circuit is a Wheatstone bridge: top arm $2\,\mu\mathrm{F}$ and $2\,\mu\mathrm{F}$, bottom arm $2\,\mu\mathrm{F}$ and $2\,\mu\mathrm{F}$, with the middle $2\,\mu\mathrm{F}$ across the junctions.
2. Balance check: $\frac{C_1}{C_2} = \frac{2}{2} = \frac{C_3}{C_4} = \frac{2}{2}$, so the two middle nodes are at equal potential and the middle capacitor holds no charge; remove it.
3. Each branch is two capacitors in series: $C_s = \frac{2 \times 2}{2 + 2} = 1\,\mu\mathrm{F}$.
4. The two branches are in parallel: $C_{AB} = 1 + 1 = 2\,\mu\mathrm{F}$, which is option $1$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q035_6a0685f0_29102026.png?v=6a0685f005fb)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q035_4ca09036_29102026.png?v=4ca09036f189)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A capacitor bridge whose two arms carry equal ratios is balanced, so the bridge capacitor stays uncharged and the network is two series pairs in parallel
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $1\,\mu\mathrm{F}$ is one arm, $2\,\mu\mathrm{F}$ in series with $2\,\mu\mathrm{F}$ — the first number the reduction produces, and it answers for the path $A$–$P$–$B$ rather than for $A$ to $B$.
- **Why:** This question requires the series–parallel reduction of a balanced capacitor bridge, demonstrated by the figure's five equal $2\,\mu\mathrm{F}$ capacitors with the fifth joining the midpoints $P$ and $Q$ of two identical arms.
- **Note:** The topology was taken from the supplied netlist: $C_1$ A–P, $C_2$ P–B, $C_3$ A–Q, $C_4$ Q–B, $C_5$ P–Q, all $2\,\mu\mathrm{F}$. All three wrong options carry a route, so none is recorded as filler.
<!--/ecat-->

## Q36

Physics · Capacitance

If the plates of a parallel plate capacitor connected to a battery are moved close to each other, then
Choose the most appropriate answer from the options given below:

- **(A)** the charge stored in it, increases.
- **(B)** the energy stored in it, decreases.
- **(C)** its capacitance increases.
- **(D)** the ratio of charge to its potential remains the same.
- **(E)** the product of charge and voltage increases.

- (1) A, B and E only
- **(2)** A, C and E only
- (3) B, D and E only
- (4) A, B and C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Given $V' = V = \text{Constant}$
2. (i) $C' = \frac{\varepsilon_0 A}{d'}, C = \frac{\varepsilon_0 A}{d}$
3. $d' < d$
4. $C' > C$
5. Hence, final capacitance greater than initial capacitance,
6. (ii) $U' = \frac{1}{2}C'V^{2}$
7. $U = \frac{1}{2}CV^{2}$
8. $U' > U$
9. Hence final energy is greater than initial energy
10. (iii) $\frac{Q'}{V'} = C'$ and $\frac{Q}{V} = C$
11. $\frac{Q'}{V'} \neq \frac{Q}{V}$
12. (iv) Product of charge and voltage
13. $X' = Q'V = C'V^{2}$
14. $X = QV = CV^{2}$
15. $X' > X$

**Solved independently** (answer withheld)

1. The capacitor stays connected to the battery, so the potential difference $V$ is constant.
2. $C = \frac{\varepsilon_0 A}{d}$; moving the plates closer decreases $d$, so $C$ increases (C true).
3. $Q = CV$ with $V$ fixed and $C$ larger, so $Q$ increases (A true).
4. $U = \frac{1}{2}CV^2$ increases, so B (energy decreases) is false.
5. $\frac{Q}{V} = C$ increases, so D (ratio remains the same) is false.
6. $QV = CV^2$ increases, so E is true.
7. True statements are A, C and E, which is option $2$.

**Subtopic:** The Parallel Plate Capacitor, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q036_2d0dc803_29102026.png?v=2d0dc8032c48)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q036_7216e6da_29102026.png?v=7216e6da32f9)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** While the battery stays connected the voltage is fixed, so closing the gap raises $C$, raises $Q = CV$, and raises the stored energy $\tfrac{1}{2}CV^2$.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Reaching for $U = Q^2/2C$ and seeing $C$ rise gives a falling energy, which is the result for a capacitor whose battery has been taken away; with the battery still across the plates $V$ is the fixed quantity, so $U = \tfrac{1}{2}CV^2$ rises instead.
- **Why:** This question requires the capacitor relations run under the condition the stem prints, demonstrated by 'connected to a battery' holding $V$ fixed while statement B claims 'the energy stored in it, decreases.'
<!--/ecat-->

## Q37

Physics · Alternating Current

A $10\,\mu\mathrm{F}$ capacitor is connected to a $210\,\mathrm{V}$, $50\,\mathrm{Hz}$ source as shown in figure. The peak current in the circuit is nearly ($\pi = 3.14$):

![printed figure: A 10 μF capacitor C connected across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q037_0e403b59_29102026.png?v=0e403b595f89)

*A 10 μF capacitor C connected across a 210 V, 50 Hz AC source in one loop*

- (1) $0.58\,\mathrm{A}$
- **(2)** $0.93\,\mathrm{A}$
- (3) $1.20\,\mathrm{A}$
- (4) $0.35\,\mathrm{A}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Capacitive Reactance $X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}}$
2. $= \frac{1000}{3.14}$
3. $V_{\mathrm{rms}} = 210\,\mathrm{V}$
4. $i_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{X_C} = \frac{210}{X_C}$
5. Peak current $= \sqrt{2}\, i_{\mathrm{rms}} = \sqrt{2} \times \frac{210}{1000} \times 3.14 = 0.932$
6. $\simeq 0.93\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Capacitive reactance: $X_C = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}} = \frac{1}{3.14 \times 10^{-3}} \approx 318.5\,\Omega$.
2. The source value $210\,\mathrm{V}$ is the rms voltage, so $I_{rms} = \frac{V_{rms}}{X_C} = \frac{210}{318.5} \approx 0.659\,\mathrm{A}$.
3. Peak current: $I_0 = \sqrt{2}\, I_{rms} = 1.414 \times 0.659 \approx 0.93\,\mathrm{A}$, which is option $2$.

**Subtopic:** AC Voltage Applied to a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q037_24b43d5a_29102026.png?v=24b43d5a199b)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q037_6642d332_29102026.png?v=6642d3326bfd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The current in a purely capacitive AC circuit is set by the reactance $X_C = 1/\omega C$, and the peak current is $\sqrt{2}$ times the rms current
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each named slip on these numbers was worked out and none lands on a printed option: reporting the rms current gives $0.66\,\mathrm{A}$, taking $\sqrt{2}$ the wrong way gives $0.47\,\mathrm{A}$, dropping the $2$ from $2\pi f$ gives $0.47\,\mathrm{A}$, using $\omega = f$ gives $0.15\,\mathrm{A}$ and reading $10\,\mu\mathrm{F}$ as $10^{-6}\,\mathrm{F}$ gives $0.093\,\mathrm{A}$, while the wrong options read $0.58$, $1.20$ and $0.35\,\mathrm{A}$.
- **Why:** This question requires the peak current computed from the capacitive reactance, demonstrated by the stem supplying '$10\,\mu\mathrm{F}$', '$210\,\mathrm{V}$, $50\,\mathrm{Hz}$' and $\pi = 3.14$ and asking for 'the peak current in the circuit'.
- **Note:** Three fillers is unusual, so the arithmetic was worked twice. $X_C = 318\,\Omega$, $I_{rms} = 0.66\,\mathrm{A}$, $I_0 = 0.93\,\mathrm{A}$. The slip this stem most invites, handing in the rms current for the peak, is not printed among the options, and each printed value sits between the outputs of the named slips rather than on one of them. The figure repeats what the stem already states and adds no further quantity.
<!--/ecat-->

## Q38

Physics · Units and Measurements

A force defined by $F = \alpha t^{2} + \beta t$ acts on a particle at a given time $t$. The factor which is dimensionless, if $\alpha$ and $\beta$ are constants, is:

- (1) $\beta t/\alpha$
- **(2)** $\alpha t/\beta$
- (3) $\alpha\beta t$
- (4) $\alpha\beta/t$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. From principle of homogeneity
2. $[F] = [\alpha t^{2}] = [\beta t]$
3. $[\alpha] = \frac{[F]}{[t^{2}]}$ and $[\beta] = \frac{[F]}{[t]}$
4. $\therefore\ [\alpha]\,[t] = [\beta]$
5. $\therefore\ \frac{\alpha t}{\beta} =$ dimensionless

**Solved independently** (answer withheld)

1. By the principle of homogeneity, $\alpha t^{2}$ and $\beta t$ have the same dimensions: $[\alpha]T^{2} = [\beta]T$.
2. Dividing both sides by $[\beta]T$: $\frac{[\alpha]T}{[\beta]} = 1$.
3. So $\frac{\alpha t}{\beta}$ is dimensionless, which is option $2$.

**Subtopic:** Homogeneity of Dimensions in an Equation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q038_441d4ae4_29102026.png?v=441d4ae4f6fc)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q038_0b57cafc_29102026.png?v=0b57cafc5334)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Every term added to a force must itself have the dimensions of force, which fixes $[\alpha] = [F]T^{-2}$ and $[\beta] = [F]T^{-1}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Pairing $\alpha$ with the first power of $t$ and $\beta$ with the square gives $[\alpha] = [F]T^{-1}$ and $[\beta] = [F]T^{-2}$, and with the two constants exchanged it is $\beta t/\alpha$ that comes out dimensionless.
- **Why:** This question requires the rule of dimensional homogeneity applied to each term of the printed sum, demonstrated by the stem's '$F = \alpha t^{2} + \beta t$' and its request for 'the factor which is dimensionless'.
<!--/ecat-->

## Q39

Physics · Thermodynamics

The following graph represents the $T$-$V$ curves of an ideal gas (where $T$ is the temperature and $V$ the volume) at three pressures $P_1$, $P_2$ and $P_3$ compared with those of Charles’s law represented as dotted lines. Then the correct relation is:

![printed figure: T-V curves of an ideal gas at pressures P1, P2, P3 with Charles's law dotted lines](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q039_2b146617_29102026.png?v=2b1466174218)

*T-V curves of an ideal gas at pressures P1, P2, P3 with Charles's law dotted lines*

- (1) $P_3 > P_2 > P_1$
- (2) $P_1 > P_3 > P_2$
- (3) $P_2 > P_1 > P_3$
- **(4)** $P_1 > P_2 > P_3$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. At same temperature, curve with higher volume corresponds to lower pressure.
2. $V_3 > V_2 > V_1$
3. $\Rightarrow P_1 > P_2 > P_3$
4. (We draw a straight line parallel to volume axis to get this)

**Solved independently** (answer withheld)

1. For an ideal gas $PV = nRT$, so $T = \frac{P}{nR}V$.
2. At constant pressure the $T$-$V$ (Charles's law) line has slope $\frac{dT}{dV} = \frac{P}{nR} \propto P$.
3. In the graph the line for $P_1$ is steepest, then $P_2$, and $P_3$ is the least steep.
4. Hence $P_1 > P_2 > P_3$, which is option $4$.

**Subtopic:** Gas Laws · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q039_137893dd_29102026.png?v=137893dd73e5)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q039_a3e5281b_29102026.png?v=a3e5281b8b15)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On a $T$-$V$ plot an ideal gas gives a line of slope $P/nR$, so the steeper the line the higher the pressure
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Carrying the gas law as $V \propto 1/P$ puts the inverse straight onto the drawn slope, so the steepest curve is taken for the lowest pressure and the order comes out exactly inverted
- **Why:** This question requires the slope of each drawn line read as $P/nR$, demonstrated by the stem printing only 'the $T$-$V$ curves of an ideal gas ... at three pressures $P_1$, $P_2$ and $P_3$' and asking for 'the correct relation', with no pressure value anywhere in words.
- **Note:** Slopes read off the carried figure spec confirm the printed key: the $P_1$ curve is steepest and the $P_3$ curve shallowest. Tagged `reversed` rather than `formula_misused` because the option printed is the exact inversion of the key and the mechanism inverts a relation rather than fetching a different one. Observation for a reviewer, not a key challenge: the stem calls the gas ideal, yet the solid curves are drawn departing from the dotted Charles's-law straight lines, which an ideal gas would lie on; the slope ordering that decides the answer is unaffected.
<!--/ecat-->

## Q40

Physics · Magnetic Effect of Electric Current

An iron bar of length $L$ has magnetic moment $M$. It is bent at the middle of its length such that the two arms make an angle $60^\circ$ with each other. The magnetic moment of this new magnet is :

- (1) $M$
- **(2)** $\frac{M}{2}$
- (3) $2M$
- (4) $\frac{M}{\sqrt{3}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A straight bar magnet of length l, with a double-headed arrow above it marking its length](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q040_sol_1_417052b7_29102026.png?v=417052b738a8)

*A straight bar magnet of length l, with a double-headed arrow above it marking its length*

1. $M = ml$.

![printed figure: Bar bent at its middle: two arms of length l/2 at 60 degrees, with the separation of the free ends marked](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q040_sol_2_0c57539d_29102026.png?v=0c57539d464f)

*Bar bent at its middle: two arms of length l/2 at 60 degrees, with the separation of the free ends marked*

2. $\Delta l = 2\frac{l}{2}\sin 30^\circ$
3. $= \frac{l}{2}$
4. $M' = ml/2$
5. $= M/2$

**Solved independently** (answer withheld)

1. Pole strength $m$ is unchanged, and $M = mL$.
2. Each arm has length $\frac{L}{2}$, and with $60^\circ$ between them the two arms and the line joining the ends form an equilateral triangle.
3. So the new separation of the poles is $\frac{L}{2}$.
4. $M' = m \cdot \frac{L}{2} = \frac{M}{2}$, which is option $2$.

**Subtopic:** Permanent Magnet and the Bar Magnet · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q040_7da18181_29102026.png?v=7da18181f19b)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q040_b8f06db3_29102026.png?v=b8f06db3da2c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A magnet's moment is pole strength times the straight-line separation of its poles, so bending at the middle gives the vector sum of two $M/2$ arms whose moments meet at $180^\circ$ minus the bend angle
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Bending cuts nothing off the bar, so the moment is taken to be untouched; but $M = m\ell$ counts the straight-line separation of the poles, and a $60^\circ$ bend brings the two ends from $L$ apart to $L/2$ apart
- **Why:** This question requires the bent magnet's moment built as the vector sum of two $M/2$ arms, demonstrated by the stem 'bent at the middle of its length such that the two arms make an angle $60^\circ$ with each other'.
- **Note:** Tagged `formula_misused` rather than `arithmetic_slip`: the relation itself is misremembered — the moment is treated as a property of the material rather than $m$ times the pole separation — and no operation is botched. Worth recording about this option set: the natural angle misreading, taking the printed $60^\circ$ as the angle between the two arm moments, yields $\frac{\sqrt{3}}{2}M \approx 0.87M$, which is not printed, so that route has no landing option here.
<!--/ecat-->

## Q41

Physics · Electromagnetic Waves

A parallel plate capacitor is charged by connecting it to a battery through a resistor. If $I$ is the current in the circuit, then in the gap between the plates:

- (1) There is no current
- **(2)** Displacement current of magnitude equal to $I$ flows in the same direction as $I$
- (3) Displacement current of magnitude equal to $I$ flows in a direction opposite to that of $I$
- (4) Displacement current of magnitude greater than $I$ flows but can be in any direction

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Capacitor plates with wire loop L1 around the lead and loop L2 in the gap](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q041_sol_1_32c9dc36_29102026.png?v=32c9dc367ad3)

*Capacitor plates with wire loop L1 around the lead and loop L2 in the gap*

1. According to modified Ampere’s law
2. $\oint B.\,dl = \mu_0(I_C + I_D)$
3. For Loop $L_1$ $\quad I_C \neq 0$ and $I_D = 0$
4. For Loop $L_2$ $\quad I_C = 0$ and $I_D \neq 0$
5. Due to KCL $\quad I_C = I_D$

**Solved independently** (answer withheld)

1. In the gap $E = \frac{q}{\varepsilon_0 A}$, so $\Phi_E = EA = \frac{q}{\varepsilon_0}$.
2. $I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \frac{dq}{dt} = I$, directed along the growing field, i.e. the same direction as $I$, which is option $2$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q041_a1ad8c9f_29102026.png?v=a1ad8c9f6474)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q041_427aced4_29102026.png?v=427aced4115b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** While a capacitor charges, the changing electric flux between the plates carries a displacement current equal in size and sense to the conduction current in the wires
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The rule that an induced effect opposes its cause is carried over to the displacement current, so the size is taken as $I$ and the direction flipped, but $i_d = \varepsilon_0 \frac{d\Phi_E}{dt}$ continues the conduction current across the gap in the same sense
- **Why:** This question requires Maxwell's displacement current applied to the gap of a charging capacitor, demonstrated by options 2 and 3 being identical except for 'flows in the same direction as $I$' against 'flows in a direction opposite to that of $I$'.
- **Note:** The E1 pattern classifier recorded `statement_options` on the length of the options. Under the three-value qtype this is `mcq` by rule 1: no lettered statement block is printed and the stem is a sentence the options complete, not an instruction to judge statements. `apply_rule` rather than `calculate` because the rule is applied with no quantity computed — $I$ is handed over by the stem.
<!--/ecat-->

## Q42

Physics · Mechanical Properties of Solids

A metallic bar of Young’s modulus, $0.5 \times 10^{11}\,\mathrm{N\,m^{-2}}$ and coefficient of linear thermal expansion $10^{-5}\,^{\circ}\mathrm{C}^{-1}$, length $1\,\mathrm{m}$ and area of cross-section $10^{-3}\,\mathrm{m^{2}}$ is heated from $0^{\circ}\mathrm{C}$ to $100^{\circ}\mathrm{C}$ without expansion or bending. The compressive force developed in it is :

- (1) $5 \times 10^{3}\,\mathrm{N}$
- **(2)** $50 \times 10^{3}\,\mathrm{N}$
- (3) $100 \times 10^{3}\,\mathrm{N}$
- (4) $2 \times 10^{3}\,\mathrm{N}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Thermal strain = Longitudinal strain = $\alpha\,\Delta T$
2. $\Rightarrow$ Longitudinal strain, $\delta = 10^{-5} \times 10^{2} = 10^{-3}$
3. $\Rightarrow$ Compressive stress = $\delta \times$ Young's Modulus
4. $= 10^{-3} \times 0.5 \times 10^{11}$
5. $= 0.5 \times 10^{8}$
6. $\Rightarrow$ Compressive force = $0.5 \times 10^{8} \times 10^{-3} = 0.5 \times 10^{5}$
7. $= 5 \times 10^{4} \times \frac{10}{10} = 50 \times 10^{3}\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Expansion is prevented, so the thermal strain $\alpha\,\Delta T$ is cancelled by a compressive strain of the same size.
2. Stress $= Y\alpha\,\Delta T$, so force $F = Y A \alpha\,\Delta T$.
3. $F = (0.5\times10^{11})(10^{-3})(10^{-5})(100) = 0.5\times10^{11}\times10^{-6} = 5\times10^{4}\,\mathrm{N}$.
4. $5\times10^{4}\,\mathrm{N} = 50\times10^{3}\,\mathrm{N}$, which is option $2$.

**Subtopic:** Thermal Stress and Strain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q042_296c4d2e_29102026.png?v=296c4d2e8953)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q042_2d70119e_29102026.png?v=2d70119e7464)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A bar held at fixed length while heated turns the thermal strain $\alpha\Delta T$ into an elastic stress $Y\alpha\Delta T$, so the force is $YA\alpha\Delta T$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Stacking only the powers of ten gives $10^{11-5-3+2} = 10^{5}$, and the $0.5$ standing in front of $Y$ is never multiplied in, so $100 \times 10^{3}$ N is printed instead of half of it
- **Why:** This question requires $F = YA\alpha\Delta T$ evaluated from four printed quantities, demonstrated by the stem 'heated from $0^{\circ}$C to $100^{\circ}$C without expansion or bending. The compressive force developed in it is'.
- **Note:** `arithmetic_slip` rather than `formula_misused`: the relation used on the trap route is the right one, and what fails is a factor left out of the multiplication, which is the line §5.1 draws between the two.
<!--/ecat-->

## Q43

Physics · Current Electricity

> ⚠ The independent solve chose (unsure); the booklet prints (1).

Choose the correct circuit which can achieve the bridge balance.

- **(1)** ![printed figure: Wheatstone bridge: 10 Ω, 10 Ω, 15 Ω and 5 Ω arms, diode D in series with 5 Ω, galvanometer G across, cell E and plug key K](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q043_option_1_85e1460b_29102026.png?v=85e1460bd54a) *Wheatstone bridge: 10 Ω, 10 Ω, 15 Ω and 5 Ω arms, diode D in series with 5 Ω, galvanometer G across, cell E and plug key K*
- (2) ![printed figure: Wheatstone bridge 10 ohm, 10 ohm, 15 ohm, 5 ohm with a diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q043_option_2_770ba65c_29102026.png?v=770ba65ca293) *Wheatstone bridge 10 ohm, 10 ohm, 15 ohm, 5 ohm with a diode D in the 5 ohm arm, galvanometer G, cell E and key K*
- (3) ![printed figure: Bridge with 10 Ω, 10 Ω, 15 Ω arms, galvanometer G, and a diode D in parallel with 5 Ω in the fourth arm; cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q043_option_3_beca6818_29102026.png?v=beca68181f2a) *Bridge with 10 Ω, 10 Ω, 15 Ω arms, galvanometer G, and a diode D in parallel with 5 Ω in the fourth arm; cell E and key K*
- (4) ![printed figure: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and 5 ohm arms, galvanometer G across the middle, diode D in series with the 5 ohm arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q043_option_4_da2c21b2_29102026.png?v=da2c21b201f5) *Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and 5 ohm arms, galvanometer G across the middle, diode D in series with the 5 ohm arm, cell E and key K*

**Answer** — booklet: (1) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. In option (1),
2. $\frac{10}{15} = \frac{10}{5 + R_D}$
3. The diode can conduct and have resistance $R_D = 10\,\Omega$ because diode have dynamic resistance.
4. In that case bridge will be balanced.

**Solved independently** (answer withheld)

1. The galvanometer joins the top node $B$ and the bottom node $C$; the cell joins the left node $A$ and the right node $D$, with $A$ at the higher potential (long plate on the left).
2. Balance condition: $\frac{R_{AB}}{R_{BD}} = \frac{R_{AC}}{R_{CD}}$.
3. $\frac{10}{10} = \frac{15}{R_{CD}} \Rightarrow R_{CD} = 15\,\Omega$.
4. Options 1, 2, 4: ideal diode in series with $5\,\Omega$, so $R_{CD} = 5\,\Omega$ (forward bias) or $R_{CD} \to \infty$ (reverse bias).
5. Option 3: ideal diode in parallel with $5\,\Omega$, so $R_{CD} = 0$ (forward bias) or $R_{CD} = 5\,\Omega$ (reverse bias).
6. No case gives $R_{CD} = 15\,\Omega$, so no option balances with the values as read; no option can be chosen.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 19)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q043_0c285010_29102026.png?v=0c285010e5e1)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q043_ce0ce833_29102026.png?v=ce0ce833342d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A Wheatstone bridge balances only when the two ratio arms are equal, $P/Q = R/S$, so that the galvanometer branch carries no current
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options are circuit diagrams and no option artwork or stem figure was carried into this step, so there is nothing in the record to read a route off
- **Why:** This question requires the bridge-balance condition read off a drawn network, demonstrated by the stem 'Choose the correct circuit which can achieve the bridge balance' with no resistance, cell or meter named in words.
- **Note:** The packet carries `options_en` as four empty strings and `has_figure: false`; the option content of this question is pictorial and the export does not carry option artwork into this step. The printed paper is intact, so under §5.0 this is our reading limit and not `source_damage_artifact`, and no trap is asserted. A reviewer holding the four circuits should check two mechanisms: whether a distractor transposes the ratio arms, which would make the trap `reversed`, and whether one merely interchanges the cell and the galvanometer across the bridge — that circuit still balances, so if it is among the options the flag to raise is `arguable_key`, not a trap.
<!--/ecat-->

## Q44

Physics · Kinematics

The velocity $(v)$ – time $(t)$ plot of the motion of a body is shown below: The acceleration $(a)$ – time $(t)$ graph that best suits this motion is :

![printed figure: Velocity-time graph: zero, uniform rise, constant velocity, uniform fall to zero (trapezium)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_b3b8eae7_29102026.png?v=b3b8eae7cbd9)

*Velocity-time graph: zero, uniform rise, constant velocity, uniform fall to zero (trapezium)*

- (1) ![printed figure: Option (1): a-t graph, a trapezoid pulse of positive acceleration above the t-axis](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_option_1_32ba784d_29102026.png?v=32ba784def65) *Option (1): a-t graph, a trapezoid pulse of positive acceleration above the t-axis*
- (2) ![printed figure: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_option_2_8d179d86_29102026.png?v=8d179d868d3f) *Acceleration-time graph: zero, then rising linearly, then constant*
- **(3)** ![printed figure: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_option_3_2389a68c_29102026.png?v=2389a68c7b0e) *Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse*
- (4) ![printed figure: Option (4): a-t graph with a negative constant step then a rising straight line](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_option_4_4473982c_29102026.png?v=4473982c2006) *Option (4): a-t graph with a negative constant step then a rising straight line*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Initially, the body has zero velocity and zero slope.
2. Hence the acceleration would be zero initially.
3. After that, the slope of $v$-$t$ curve is constant and positive.
4. After some time, velocity becomes constant and acceleration is zero.
5. After that, the slope of $v$-$t$ curve is constant and negative.

![printed figure: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q044_sol_1_dc7d5ee5_29102026.png?v=dc7d5ee5e6be)

*Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse*


**Solved independently** (answer withheld)

1. Acceleration is the slope of the velocity-time graph: $a = \frac{dv}{dt}$.
2. Initially $v = 0$ and constant, so $a = 0$.
3. Next, $v$ rises linearly with $t$, so the slope is a positive constant: $a = +a_0$.
4. Then $v$ stays constant (flat top), so $a = 0$.
5. Then $v$ falls linearly to zero, so the slope is a negative constant: $a = -a_0'$.
6. After that $v = 0$, so $a = 0$; the a-t graph is a positive rectangle, a zero gap, then a negative rectangle, which is option $3$.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q044_b2c26aff_29102026.png?v=b2c26affc243)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q044_327f9c26_29102026.png?v=327f9c261a05)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Acceleration is the slope of the velocity-time graph, so each straight segment of the $v$-$t$ plot becomes a flat step in the $a$-$t$ plot
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and no option artwork was carried into this step, so no distractor can be inspected and no route named
- **Why:** This question requires each straight segment of the printed plot converted into its slope, demonstrated by the stem 'The acceleration $(a)$ - time $(t)$ graph that best suits this motion is'.
- **Note:** The stem figure was carried as a drawn spec and reads as five straight segments: $v = 0$, a uniform rise, a constant stretch, a uniform fall back to zero, then zero again, with the rise and the fall of nearly equal steepness. The four option graphs arrive as empty strings, since the export does not carry option artwork into this step; the printed paper is intact, so under §5.0 this is a reading limit rather than `source_damage_artifact`. A reviewer holding the options should check for an $a$-$t$ graph with both pulses drawn positive, the sign of the deceleration dropped, and for one carrying a non-zero step across the constant-velocity stretch.
<!--/ecat-->

## Q45

Physics · Ray Optics

A small telescope has an objective of focal length $140\,\mathrm{cm}$ and an eye piece of focal length $5.0\,\mathrm{cm}$. The magnifying power of telescope for viewing a distant object is:

- (1) 34
- **(2)** 28
- (3) 17
- (4) 32

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $f_0 = 140\,\mathrm{cm}$ and $f_e = 5\,\mathrm{cm}$
2. For distant object,
3. $m = \frac{f_0}{f_e} = \frac{140}{5} = 28$

**Solved independently** (answer withheld)

1. For a distant object in normal adjustment, the magnifying power is $m = \frac{f_o}{f_e}$.
2. $m = \frac{140\,\mathrm{cm}}{5.0\,\mathrm{cm}} = 28$, which is option $2$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q045_5d8f3714_29102026.png?v=5d8f3714c222)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q045_418d3a19_29102026.png?v=418d3a19408b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A telescope in normal adjustment magnifies by the objective's focal length divided by the eyepiece's
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  A student who has learnt both eyepiece adjustments reaches for the fuller-looking formula $m=\frac{f_o}{f_e}\left(1+\frac{f_e}{D}\right)$ and gets $28\times1.2=33.6$, which is the printed 34. That bracket holds only while the final image is kept at the near point, which this stem never asks for.
- **Why:** This question requires the magnifying power computed from the two printed focal lengths, demonstrated by the stem giving an objective of '140 cm' and an eye piece of '5.0 cm' and asking for the magnifying power 'for viewing a distant object'.
- **Note:** The stem does not state the eyepiece adjustment. The key follows the normal-adjustment convention for a distant object, $f_o/f_e=28$, and option 1 is exactly the near-point value 33.6 rounded; tagged as printed. Checked the old_ncert_answer route and ruled it out: the textbook telescope exercise runs on 144 cm and 6.0 cm with answer 24, and 24 is not among these options, so no altered value leaves an older answer sitting in the option list.
<!--/ecat-->

## Q46

Physics · Gravitation

The minimum energy required to launch a satellite of mass $m$ from the surface of earth of mass $M$ and radius $R$ in a circular orbit at an altitude of $2R$ from the surface of the earth is:

- **(1)** $\frac{5GmM}{6R}$
- (2) $\frac{2GmM}{3R}$
- (3) $\frac{GmM}{2R}$
- (4) $\frac{GmM}{3R}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Apply energy conservation,
2. $U_i + K_i = U_f + K_f$
3. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2}mv^{2}$
4. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2} \times m \times \frac{GM}{3R}$
5. $\Rightarrow K_i = -\frac{1}{6}\frac{GMm}{R} + \frac{GMm}{R}$
6. $K_i = \frac{5}{6}\frac{GMm}{R}$

**Solved independently** (answer withheld)

1. Orbit radius from the centre: $r = R + 2R = 3R$.
2. Total energy in a circular orbit: $E_{orbit} = -\frac{GMm}{2r} = -\frac{GMm}{6R}$.
3. Energy on the surface (at rest): $E_{surface} = -\frac{GMm}{R}$.
4. $E_{min} = E_{orbit} - E_{surface} = \frac{GMm}{R} - \frac{GMm}{6R} = \frac{5GMm}{6R}$, which is option $1$.

**Subtopic:** Motion of a Satellite · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q046_67561f50_29102026.png?v=67561f504acf)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q046_11993ee6_29102026.png?v=11993ee6a7c6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Launching into a circular orbit costs the rise in gravitational potential energy plus the orbital kinetic energy, since a satellite at radius $r$ has total energy $-\frac{GMm}{2r}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $\frac{2GmM}{3R}$ is exactly the rise in potential energy from $R$ to $3R$, so a student who reads 'launch' as lifting the satellite to that height computes $\Delta U$ and finds it printed. That number answers how much it costs to get the mass up there, not how much it costs to have it circling.
- **Why:** This question requires the energy difference between rest on the surface and a circular orbit of radius $3R$, demonstrated by the stem asking for 'the minimum energy required to launch' the satellite into 'a circular orbit at an altitude of $2R$ from the surface'.
<!--/ecat-->

## Q47

Physics · Oscillations

If the mass of the bob in a simple pendulum is increased to thrice its original mass and its length is made half its original length, then the new time period of oscillation is $\frac{x}{2}$ times its original time period. Then the value of $x$ is:

- (1) $\sqrt{3}$
- **(2)** $\sqrt{2}$
- (3) $2\sqrt{3}$
- (4) $4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $T' = 2\pi\sqrt{\frac{\ell'}{g}}$ where $\ell' = \frac{\ell}{2}$
2. $T = 2\pi\sqrt{\frac{\ell}{g}}$
3. $T' = \frac{x}{2}T$
4. $2\pi\sqrt{\frac{\ell}{2g}} = \frac{x}{2}2\pi\sqrt{\frac{\ell}{g}}$
5. $\frac{1}{\sqrt{2}} = \frac{x}{2} \Rightarrow x = \sqrt{2}$

**Solved independently** (answer withheld)

1. The period of a simple pendulum is $T = 2\pi\sqrt{\frac{l}{g}}$, which does not depend on the bob's mass, so tripling the mass has no effect.
2. With $l' = \frac{l}{2}$: $T' = 2\pi\sqrt{\frac{l/2}{g}} = \frac{T}{\sqrt{2}}$.
3. $\frac{T}{\sqrt{2}} = \frac{\sqrt{2}}{2}T$, so $\frac{x}{2} = \frac{\sqrt{2}}{2}$ and $x = \sqrt{2}$, which is option $2$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q047_7aaf372a_29102026.png?v=7aaf372a976e)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q047_c88b8e35_29102026.png?v=c88b8e352f86)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** A simple pendulum's period is set by length and $g$ alone, $T=2\pi\sqrt{L/g}$, so the bob's mass cancels out
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who carries the spring oscillator's $T=2\pi\sqrt{m/k}$ over to the pendulum multiplies the period by $\sqrt{3}$ for the trebled mass and leaves the length out, because that formula has no length in it; $T'=\sqrt{3}\,T=\frac{2\sqrt{3}}{2}T$ gives $x=2\sqrt{3}$.
- **Why:** This question requires the factor by which the period changes when the stated changes are made, demonstrated by the stem asking only that 'the new time period of oscillation is $\frac{x}{2}$ times its original time period' while 'increased to thrice its original mass' sits beside a relation in which mass does not appear.
<!--/ecat-->

## Q48

Physics · Electromagnetic Induction

A sheet is placed on a horizontal surface in front of a strong magnetic pole. A force is needed to:
Choose the correct statement(s) from the options given below:

- **(A)** hold the sheet there if it is magnetic.
- **(B)** hold the sheet there if it is non-magnetic.
- **(C)** move the sheet away from the pole with uniform velocity if it is conducting.
- **(D)** move the sheet away from the pole with uniform velocity if it is both, non-conducting and non-polar.

- (1) B and D only
- **(2)** A and C only
- (3) A, C and D only
- (4) C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A. A magnetic pole will repel or attract magnetic sheet so force is need.
2. B. If sheet is non-magnetic, no force needed.
3. C. If it is conducting, then there will be addy current in sheet, which opposes the motion. So forces is needed move sheet with uniform speed.
4. D. The non-conducting and non-polar sheet do not interact with magnetic field of magnet.

**Solved independently** (answer withheld)

1. A magnetic sheet is attracted towards the strong pole, so a force is needed to hold it in place: $A$ is true.
2. A non-magnetic sheet at rest feels no magnetic force, so no force is needed to hold it: $B$ is false.
3. When a conducting sheet moves away from the pole, the flux through it changes, inducing eddy currents that by Lenz's law oppose the motion; a force $F = F_{\text{eddy}}$ is needed to keep $v$ uniform: $C$ is true.
4. A non-conducting, non-polar sheet has no induced currents and no magnetic interaction, so with uniform velocity $\sum F = 0$ needs no applied force: $D$ is false.
5. Correct statements are $A$ and $C$ only, which is option $2$.

**Subtopic:** Eddy Currents · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q048_5b791cd4_29102026.png?v=5b791cd4c26e)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q048_ef7c5804_29102026.png?v=ef7c58047235)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A magnetic sheet is pulled toward the pole and has to be held, a conductor dragged away from the pole is opposed by its own eddy currents, and a non-conducting non-polar sheet feels neither.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Having got C right through eddy-current drag, a student carries that drag on to D and reads past the words that switch it off; a non-conducting, non-polar sheet has nothing in it for the changing flux to drive, so no force opposes its uniform motion.
- **Why:** This question requires magnetic attraction and the eddy-current rule applied to the material condition each statement prints, demonstrated by C's 'if it is conducting' set against D's 'if it is both, non-conducting and non-polar.'
<!--/ecat-->

## Q49

Physics · Current Electricity

Two heaters A and B have power rating of $1\,\mathrm{kW}$ and $2\,\mathrm{kW}$, respectively. Those two are first connected in series and then in parallel to a fixed power source. The ratio of power outputs for these two cases is:

- (1) $1:1$
- **(2)** $2:9$
- (3) $1:2$
- (4) $2:3$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Power Consumed $= P = \frac{V^{2}}{R}$
2. $\frac{P_A}{P_B} = \frac{R_B}{R_A}$
3. $R_A = 2R_B$
4. For Series Combination
5. $P_S = \frac{V^{2}}{3R_B}$
6. For Parallel Combination
7. $P_P = \frac{3V^{2}}{2R_B}$
8. $\frac{P_S}{P_P} = \frac{2}{9}$

**Solved independently** (answer withheld)

1. For a fixed source voltage $V$, $R = \frac{V^2}{P}$, so $R_A = \frac{V^2}{1\,\mathrm{kW}}$ and $R_B = \frac{V^2}{2\,\mathrm{kW}}$.
2. Series: $P_s = \frac{V^2}{R_A + R_B} = \frac{1}{\frac{1}{1} + \frac{1}{2}}\,\mathrm{kW} = \frac{2}{3}\,\mathrm{kW}$.
3. Parallel: $P_p = P_A + P_B = 1 + 2 = 3\,\mathrm{kW}$.
4. $\frac{P_s}{P_p} = \frac{2/3}{3} = \frac{2}{9}$, i.e. $2:9$, which is option $2$.

**Subtopic:** Electrical Energy and Power, Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q049_1aa66468_29102026.png?v=1aa664684705)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q049_b0bb3476_29102026.png?v=b0bb34766928)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A heater's power rating is its output at full rated voltage; in parallel each keeps that output, while in series the shared voltage drops both
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Reading '1 kW' and '2 kW' as what each heater always draws, a student totals 3 kW in the series case and 3 kW in the parallel case and answers 1:1. The rating holds only with the full source voltage across the heater, which is true in parallel and false in series, where the pair gives $\frac{2}{3}$ kW.
- **Why:** This question requires the combined output of the pair worked out in each connection from the two rated powers, demonstrated by the stem asking for 'the ratio of power outputs for these two cases' after they are 'first connected in series and then in parallel to a fixed power source'.
- **Note:** The stem says 'a fixed power source'; the printed key, 2:9, follows from a fixed VOLTAGE source, which is how a heater rating is defined. Tagged as printed, with the loose wording recorded here rather than treated as a trap.
<!--/ecat-->

## Q50

Physics · Electromagnetic Waves

The property which is not of an electromagnetic wave travelling in free space is that:

- (1) They are transverse in nature
- (2) The energy density in electric field is equal to energy density in magnetic field
- (3) They travel with a speed equal to $\frac{1}{\sqrt{\mu_0 \varepsilon_0}}$
- **(4)** They originate from charges moving with uniform speed

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The EM waves originate from an accelerating charge.
2. The charge moving with uniform velocity produces steady state magnetic field.

**Solved independently** (answer withheld)

1. EM waves in free space are transverse, with $\vec{E} \perp \vec{B} \perp \vec{v}$, so option $1$ is a true property.
2. In free space $\frac{1}{2}\varepsilon_0 E^2 = \frac{B^2}{2\mu_0}$ since $E = cB$, so option $2$ is a true property.
3. Their speed is $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, so option $3$ is a true property.
4. EM waves originate from accelerated charges; a charge moving with uniform speed (no acceleration) does not radiate, so option $4$ is not a property, which is the answer.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q050_f718c22a_29102026.png?v=f718c22a95e7)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q050_b1b53724_29102026.png?v=b1b53724b6e4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Electromagnetic waves are radiated by accelerating charges; a charge moving with uniform velocity radiates nothing
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  In a free-space wave $E=cB$, so the electric field is some $10^8$ times the magnetic one in SI units, and a student who compares the fields instead of the energy densities concludes the electric share must be far the larger and marks the stated equality as the property that fails. The constants in $\frac{1}{2}\varepsilon_0E^2$ and $\frac{B^2}{2\mu_0}$ are what make the two equal.
- **Why:** This question requires the stated origin of electromagnetic waves, demonstrated by option 4's claim that they 'originate from charges moving with uniform speed' standing against the chapter's line that it is accelerated charges which radiate.
- **Note:** E1 classed this as statement_options because the four options are full property claims with no lettered block printed. On the current axis the nearest value is `statements`, since the stem asks each option to be judged as a claim about electromagnetic waves rather than offering four names; recorded here because the shape sits between `mcq` and `statements`. The task is negated ('is not of an electromagnetic wave'), so all three wrong options are true statements.
<!--/ecat-->

## Q51

Chemistry · inorganic · The p–Block Elements

Among Group 16 elements, which one does NOT show $-2$ oxidation state?

- (1) $\mathrm{O}$
- (2) $\mathrm{Se}$
- (3) $\mathrm{Te}$
- **(4)** $\mathrm{Po}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Oxygen shows $-2$, $-1$, $+1$ and $+2$ oxidation states
2. Selenium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
3. Tellurium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
4. Polonium shows $+2$ and $+4$ oxidation states

**Solved independently** (answer withheld)

1. Down Group 16 the electronegativity falls, so the stability of the $-2$ oxidation state decreases: $\mathrm{O} > \mathrm{S} > \mathrm{Se} > \mathrm{Te} > \mathrm{Po}$; $\mathrm{Po}$ is metallic and hardly shows the $-2$ state, which is option $4$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q051_25cb9fef_29102026.png?v=25cb9fef05b9)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q051_d8ce2566_29102026.png?v=d8ce2566e143)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The stability of the $-2$ state falls down Group 16, and polonium is the member the text says hardly shows it
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Oxygen is the member of Group 16 the oxidation-state paragraph singles out as behaving unlike the rest, so a student carrying 'oxygen is the exception' puts it against the NOT in the stem. The exception they hold is that oxygen shows no $+4$ or $+6$ state for want of d orbitals, which answers a different question from the $-2$ one asked here.
- **Why:** This question requires the stated fact about where the $-2$ oxidation state stops in Group 16, demonstrated by the stem 'which one does NOT show $-2$ oxidation state' standing over four members of one group with no criterion printed to apply.
- **Note:** Chose answers_other_question over nearby_fact: option 1 is not merely printed beside the right fact, it is the correct answer to the neighbouring question 'which Group 16 element does not show $+4$ and $+6$ oxidation states', so what carries the student is a remembered answer to a question the stem resembles.
<!--/ecat-->

## Q52

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
List I (Molecule)
List II (Number and types of bond/s between two carbon atoms)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | ethane | I | one $\sigma$-bond and two $\pi$-bonds |
| B | ethene | II | two $\pi$-bonds |
| C | carbon molecule, $\mathrm{C_2}$ | III | one $\sigma$-bond |
| D | ethyne | IV | one $\sigma$-bond and one $\pi$-bond |

- (1) A-I, B-IV, C-II, D-III
- (2) A-IV, B-III, C-II, D-I
- **(3)** A-III, B-IV, C-II, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Ethane: one $(\mathrm{C-C})$ $\sigma$ bond

![printed figure: ethane ($\ce{H3C-CH3}$), drawn with all hydrogens shown and a single bond between the two carbon atoms](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q052_sol_1_76f9facd_29102026.png?v=76f9facdecb6)

*ethane ($\ce{H3C-CH3}$), drawn with all hydrogens shown and a single bond between the two carbon atoms*

![drawn: ethane ($\ce{H3C-CH3}$), drawn with all hydrogens shown and a single bond between the two carbon atoms](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q052_solution_1_5f96e6e1_30102026.svg?v=5f96e6e1cf49)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

2. (B) Ethene: one $(\mathrm{C-C})$ $\sigma$ and one $(\mathrm{C-C})$ $\pi$ bond

![printed figure: ethene ($\ce{H2C=CH2}$), drawn with all hydrogens shown and a double bond between the two carbon atoms](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q052_sol_2_bce65d3b_29102026.png?v=bce65d3b9de1)

*ethene ($\ce{H2C=CH2}$), drawn with all hydrogens shown and a double bond between the two carbon atoms*

![drawn: ethene ($\ce{H2C=CH2}$), drawn with all hydrogens shown and a double bond between the two carbon atoms](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q052_solution_2_fba951d1_30102026.svg?v=fba951d1a57c)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

3. (C) $\mathrm{C_2}$: two $(\mathrm{C-C})$ $\pi$ bonds
4. (D) Ethyne $\mathrm{H-C\equiv C-H}$: two $(\mathrm{C-C})$ $\pi$ bonds and one $(\mathrm{C-C})$ $\sigma$ bond

**Solved independently** (answer withheld)

1. Ethane has a $\mathrm{C-C}$ single bond: one $\sigma$-bond, so A-III.
2. Ethene has a $\mathrm{C=C}$ double bond: one $\sigma$-bond and one $\pi$-bond, so B-IV.
3. For $\mathrm{C_2}$, the MO configuration is $KK\,\sigma 2s^2\,\sigma^* 2s^2\,(\pi 2p_x^2 = \pi 2p_y^2)$, bond order $2$ with both bonds $\pi$: two $\pi$-bonds, so C-II.
4. Ethyne has a $\mathrm{C\equiv C}$ triple bond: one $\sigma$-bond and two $\pi$-bonds, so D-I.
5. A-III, B-IV, C-II, D-I is option $3$.

**Subtopic:** Orbital Overlap Concept, Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q052_2383e10b_29102026.png?v=2383e10b6fe2)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q052_07444619_29102026.png?v=074446196ed6)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A single C–C bond is one σ, a double adds one π and a triple two; the bare C₂ molecule breaks that pattern because MO filling gives it two π bonds and no net σ bond
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Carbon is tetravalent and C₂ carries no hydrogens, so the two atoms are given the biggest multiple bond printed, one σ and two π. The Lewis counting rule holds for hydrocarbons but not for C₂, where the π orbitals fill below σ2p and a bond order of 2 means two π bonds with no net σ bond.
- **Why:** This question requires the σ and π count of a carbon–carbon bond to be derived from each molecule's bonding, demonstrated by List II printing counts such as 'one σ-bond and two π-bonds' against named species including the bare 'carbon molecule, C₂', whose entry cannot be read off a Lewis structure.
- **Note:** The three hydrocarbon rows alone decide the code: A-III with B-IV and D-I occur together only in option 3, so the C₂ row can be reached by elimination rather than from molecular orbital theory. Printed shape and the E1 pattern agree.
<!--/ecat-->

## Q53

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Fehling’s solution ‘A’ is

- **(1)** aqueous copper sulphate
- (2) alkaline copper sulphate
- (3) alkaline solution of sodium potassium tartrate (Rochelle’s salt)
- (4) aqueous sodium citrate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fehling solution ‘A’ = Aqueous copper sulphate
2. Fehling solution ‘B’ = Alkaline sodium potassium tartrate (Rochelle salt)

**Solved independently** (answer withheld)

1. Fehling's reagent is made of two solutions: Fehling's A is aqueous $\mathrm{CuSO_4}$ and Fehling's B is alkaline sodium potassium tartrate (Rochelle salt), which is option $1$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q053_b2a26d86_29102026.png?v=b2a26d8602a8)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q053_66fcb3a8_29102026.png?v=66fcb3a8ca24)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fehling's reagent is stored as two solutions, A the copper sulphate and B the alkaline tartrate, mixed only at the time of the test
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A and B are learnt together as one reagent and the tartrate is the half with the memorable name, so a student who holds both compositions but not which bottle carries which letter writes Rochelle's salt against A. Rochelle's salt is solution B; A is the plain copper sulphate.
- **Why:** This question requires the stated composition of one named bench solution, demonstrated by the stem 'Fehling's solution A is' set over four options that are each a real reagent composition.
- **Note:** Applied the swap test for nearby_fact against look_alike_term: 'aqueous copper sulphate' and 'alkaline solution of sodium potassium tartrate' resemble each other in no part, so the likeness is doing no work and what carries the student is the two solutions being printed side by side as A and B. Considered asks: experiment, since Fehling's is a bench test, but nothing here is set up or observed and the answer is a stated composition, so fact_line.
<!--/ecat-->

## Q54

Chemistry · physical · Electrochemistry

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $1$ mol of $\mathrm{H_2O}$ to $\mathrm{O_2}$ | I | $3\,\mathrm{F}$ |
| B | $1$ mol of $\mathrm{MnO_4^-}$ to $\mathrm{Mn^{2+}}$ | II | $2\,\mathrm{F}$ |
| C | $1.5$ mol of Ca from molten $\mathrm{CaCl_2}$ | III | $1\,\mathrm{F}$ |
| D | $1$ mol of FeO to $\mathrm{Fe_2O_3}$ | IV | $5\,\mathrm{F}$ |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-I, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{4OH^- \rightarrow 2H_2O + O_2 + 4e^-}$
2. for $2$ mole of $\mathrm{H_2O}$ = $4\mathrm{F}$ charge is required
3. for $1$ mole of $\mathrm{H_2O}$ = $\frac{4\mathrm{F}}{2} = 2\mathrm{F}$ required
4. $\mathrm{\overset{+7}{Mn}O_4^- \rightarrow \overset{+2}{Mn}{}^{2+}}$
5. for $1$ mole $\mathrm{MnO_4^-}$ $5\mathrm{F}$ charge is required
6. $\mathrm{Ca^{2+} \xrightarrow{+2e^-} Ca}$
7. For $1$ mole $\mathrm{Ca^{2+}}$ ion required = $2\mathrm{F}$
8. $1.5$ mole $\mathrm{Ca^{2+}}$ ion required = $\frac{2}{1} \times 1.5 = 3\mathrm{F}$
9. $\mathrm{\overset{+2}{Fe}O \rightarrow \overset{+3}{Fe}{}_2O_3}$
10. for $1$ mole FeO, $1\mathrm{F}$ charge is required.

**Solved independently** (answer withheld)

1. A: $2\mathrm{H_2O} \rightarrow \mathrm{O_2} + 4\mathrm{H^+} + 4e^-$, so $1$ mol $\mathrm{H_2O}$ releases $2$ mol $e^-$, i.e. $2\,\mathrm{F}$ (II).
2. B: Mn goes from $+7$ in $\mathrm{MnO_4^-}$ to $+2$, so $1$ mol needs $5$ mol $e^-$, i.e. $5\,\mathrm{F}$ (IV).
3. C: $\mathrm{Ca^{2+}} + 2e^- \rightarrow \mathrm{Ca}$, so $1.5 \times 2 = 3$ mol $e^-$, i.e. $3\,\mathrm{F}$ (I).
4. D: Fe goes from $+2$ in FeO to $+3$ in $\mathrm{Fe_2O_3}$, so $1$ mol needs $1$ mol $e^-$, i.e. $1\,\mathrm{F}$ (III).
5. A-II, B-IV, C-I, D-III matches option $1$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q054_584e6b0e_29102026.png?v=584e6b0ee7df)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q054_12d88937_29102026.png?v=12d88937b3fe)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Charge in faradays = moles of the named species × electrons transferred per mole, the electrons coming from the oxidation-state change
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Ca²⁺ + 2e⁻ → Ca is worth 2 F per mole, and the '1.5 mol' printed in row C is left out of the multiplication, so C is read as 2 F instead of 1.5 × 2 = 3 F. Option 4 is the only code pairing C with II, so that one dropped factor settles the whole answer.
- **Why:** This question requires the charge in faradays to be computed for each change, demonstrated by row C reading '1.5 mol of Ca from molten CaCl₂' against entries of 3 F, 2 F, 1 F and 5 F, so the stated amount must be multiplied by the electrons per mole.
<!--/ecat-->

## Q55

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the correct reagents that would bring about the following transformation.

![printed figure: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q055_c7604f0a_29102026.png?v=c7604f0aa7a4)

*allylcyclohexane → 3-cyclohexylpropanal*

![drawn: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_22b87b16_30102026.svg?v=22b87b160f5d)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

Structures: allylcyclohexane `C=CCC1CCCCC1` ![allylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_s1_f36180db_30102026.svg?v=f36180db6e8a); 3-cyclohexylpropanal `O=CCCC1CCCCC1` ![3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_s2_f25b29a6_30102026.svg?v=f25b29a6896c)

- (1) (i) $\mathrm{H_2O/H^+}$ (ii) $\mathrm{CrO_3}$
- **(2)** (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) PCC
- (3) (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) alk.$\mathrm{KMnO_4}$ (iv) $\mathrm{H_3O^{\oplus}}$
- (4) (i) $\mathrm{H_2O/H^+}$ (ii) PCC

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: allylcyclohexane →((i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q055_sol_1_057623fc_29102026.png?v=057623fce4fa)

*allylcyclohexane →[(i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC] 3-cyclohexylpropanal*

![drawn: allylcyclohexane →((i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q055_solution_1_428d3637_30102026.svg?v=428d3637c567)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

1. Mechanism :

![printed figure: allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H drawn on the middle CH, BH₂ on the end carbon); (3-cyclohexylpropyl)borane + allylcyclohexane → bis(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₂BH; bis(3-cyclohexylpropyl)borane + allylcyclohexane → tris(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₃B; tris(3-cyclohexylpropyl)borane →(H₂O / 3H₂O₂, OH⁻) 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →(PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q055_sol_2_c733e5ba_29102026.png?v=c733e5ba1352)

*allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H drawn on the middle CH, BH₂ on the end carbon); (3-cyclohexylpropyl)borane + allylcyclohexane → bis(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₂BH; bis(3-cyclohexylpropyl)borane + allylcyclohexane → tris(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₃B; tris(3-cyclohexylpropyl)borane →[H₂O / 3H₂O₂, OH⁻] 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →[PCC] 3-cyclohexylpropanal*

![drawn: allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H drawn on the middle CH, BH₂ on the end carbon); (3-cyclohexylpropyl)borane + allylcyclohexane → bis(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₂BH; bis(3-cyclohexylpropyl)borane + allylcyclohexane → tris(3-cyclohexylpropyl)borane, (cyclohexyl-CH₂-CH₂-CH₂)₃B; tris(3-cyclohexylpropyl)borane →(H₂O / 3H₂O₂, OH⁻) 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →(PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q055_solution_2_95583f8a_30102026.svg?v=95583f8accf5)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*


**Solved independently** (answer withheld)

1. The product has $\mathrm{-CHO}$ on the terminal carbon, so the terminal alkene carbon must get the oxygen (anti-Markovnikov).
2. $\mathrm{BH_3}$ then $\mathrm{H_2O_2/OH^-}$ converts $\mathrm{R{-}CH_2{-}CH{=}CH_2}$ to the primary alcohol $\mathrm{R{-}CH_2{-}CH_2{-}CH_2OH}$.
3. PCC oxidises a primary alcohol only to the aldehyde: $\mathrm{R{-}CH_2CH_2CH_2OH \xrightarrow{PCC} R{-}CH_2CH_2CHO}$, which is option $2$.
4. Options $1$ and $4$ use $\mathrm{H_2O/H^+}$ (Markovnikov, secondary alcohol, giving a ketone); option $3$ uses alk. $\mathrm{KMnO_4}$, which gives the carboxylic acid.

**Subtopic:** Preparation of Aldehydes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q055_0357c134_29102026.png?v=0357c1341552)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q055_031f4a08_29102026.png?v=031f4a084808)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hydroboration-oxidation puts the OH on the terminal carbon, and only a mild oxidant such as PCC stops a primary alcohol at the aldehyde
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first two reagents are exactly the anti-Markovnikov route the printed target needs, and a student who has reached 3-cyclohexylpropan-1-ol then reaches for the oxidant they use most. Alkaline $\mathrm{KMnO_4}$ followed by $\mathrm{H_3O^+}$ carries the primary alcohol past the aldehyde to 3-cyclohexylpropanoic acid.
- **Why:** This question requires naming the reagent set that effects a printed conversion, demonstrated by the stem 'Identify the correct reagents that would bring about the following transformation' with four reagent sequences as options.
- **Note:** The figure was supplied to this step as a drawn reaction, allylcyclohexane to 3-cyclohexylpropanal with nothing written over the arrow, so the transformation could be read and the routes checked against it.
<!--/ecat-->

## Q56

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Intramolecular hydrogen bonding is present in

- **(1)** 2-nitrophenol `O=[N+]([O-])c1ccccc1O` ![2-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_1_s1_41d9f699_30102026.svg?v=41d9f6994db3)
- (2) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_2_s1_b3de126e_30102026.svg?v=b3de126edb17)
- (3) 3-nitrophenol `O=[N+]([O-])c1cccc(O)c1` ![3-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_3_s1_c8ec89cf_30102026.svg?v=c8ec89cf3e3a)
- (4) $\mathrm{HF}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In o-nitrophenol intramolecular H-bonding is present.

![printed figure: 2-nitrophenol with a dotted O···H bond between the nitro oxygen and the phenolic H, labelled ← H-bonding](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q056_sol_1_c6ee0160_29102026.png?v=c6ee01606202)

*2-nitrophenol with a dotted O···H bond between the nitro oxygen and the phenolic H, labelled ← H-bonding*

![drawn: 2-nitrophenol with a dotted O···H bond between the nitro oxygen and the phenolic H, labelled ← H-bonding](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q056_solution_1_072d22b1_30102026.svg?v=072d22b1f889)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*


**Solved independently** (answer withheld)

1. Option $1$ is o-nitrophenol: the $-\mathrm{OH}$ and $-\mathrm{NO_2}$ groups are on adjacent ring carbons, so the $\mathrm{O-H}$ hydrogen bonds to an oxygen of $\mathrm{NO_2}$ within the same molecule (six-membered ring).
2. In p-nitrophenol (option $2$) and m-nitrophenol (option $3$) the groups are too far apart, so they form only intermolecular hydrogen bonds.
3. $\mathrm{HF}$ (option $4$) forms intermolecular $\mathrm{H-F\cdots H-F}$ chains, not intramolecular bonds.
4. So intramolecular hydrogen bonding is present in option $1$.

**Subtopic:** Hydrogen Bonding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q056_d587afb3_29102026.png?v=d587afb38d63)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q056_65a713aa_29102026.png?v=65a713aa4fab)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A hydrogen bond counts as intramolecular only when donor and acceptor sit on the same molecule, close enough to close a ring
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  options 1, 2 and 3 are stored in this record as empty strings, so three of the four species the question turns on cannot be read and no route to any of them can be checked against the printed page
- **Why:** This question requires applying the intramolecular hydrogen-bonding criterion to each species offered, demonstrated by the stem 'Intramolecular hydrogen bonding is present in' standing with no further condition and the one readable option being the single molecule $\mathrm{HF}$.
- **Note:** Three of the four options are blank in our record while the paper printed species there, so this is damage to what we stored and not a figure this step was never given; no trap is written for it. A reviewer holding the printed options should check whether option 4, $\mathrm{HF}$, is reached by a student who knows HF as the textbook hydrogen-bonded species and does not separate bonding between molecules from bonding within one.
<!--/ecat-->

## Q57

Chemistry · physical · Chemical Kinetics

Activation energy of any chemical reaction can be calculated if one knows the value of

- (1) rate constant at standard temperature
- (2) probability of collision
- (3) orientation of reactant molecules during collision
- **(4)** rate constant at two different temperatures

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. To calculate value of $E_a$
2. Equation used is
3. $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$
4. Hence $E_a$ can be calculated if value of rate constant $k$ is known at two different temperatures $T_1$ and $T_2$.

**Solved independently** (answer withheld)

1. Arrhenius equation at two temperatures: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
2. Rearranging, $E_a = 2.303R\,\log\frac{k_2}{k_1}\,\frac{T_1 T_2}{T_2 - T_1}$, so the rate constants at two different temperatures are needed, which is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q057_f06eedd1_29102026.png?v=f06eedd1dc5d)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q057_0a79789e_29102026.png?v=0a79789e1cca)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The Arrhenius equation yields the activation energy only once the frequency factor is cancelled, which takes rate constants at two temperatures
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student holding $k = A e^{-E_a/RT}$ sees one rate constant and one temperature as enough to solve for $E_a$, and 'standard temperature' seems to supply the $T$. But $A$ is unknown as well, so a single $k$ fixes nothing until the two-temperature form $\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1}-\frac{1}{T_2}\right)$ cancels it.
- **Why:** This question requires knowing what data the Arrhenius relation needs before an activation energy follows from it, demonstrated by the stem 'can be calculated if one knows the value of' set against 'rate constant at standard temperature' and 'rate constant at two different temperatures'.
- **Note:** Nothing is computed here and no quantity is produced, so apply_rule rather than calculate: the student applies the Arrhenius relation to decide which data determine $E_a$.
<!--/ecat-->

## Q58

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ | I | Solvate isomerism |
| B | $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ | II | Linkage isomerism |
| C | $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ | III | Ionization isomerism |
| D | $\mathrm{[Co(H_2O)_6]Cl_3}$ | IV | Coordination isomerism |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-I, B-III, C-IV, D-II
- (3) A-I, B-IV, C-III, D-II
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A. $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ — II. Linkage isomerism due to ‘N’ and ‘O’ linkage by $\mathrm{NO_2}$
2. B. $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ — III. Ionization isomerism
3. C. $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ — IV. Coordination isomerism
4. D. $\mathrm{[Co(H_2O)_6]Cl_3}$ — I. Solvate isomerism

**Solved independently** (answer withheld)

1. A: $\mathrm{NO_2^-}$ is ambidentate (binds through N or O), so $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ shows linkage isomerism: A–II.
2. B: $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ and $\mathrm{[Co(NH_3)_5Br]SO_4}$ give different ions in solution, so ionization isomerism: B–III.
3. C: In $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ both cation and anion are complexes and ligands can interchange between metals, so coordination isomerism: C–IV.
4. D: In $\mathrm{[Co(H_2O)_6]Cl_3}$ water can be a ligand or lattice water, so solvate (hydrate) isomerism: D–I.
5. A–II, B–III, C–IV, D–I matches option $1$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q058_4f166d24_29102026.png?v=4f166d242f27)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q058_65a48864_29102026.png?v=65a48864ab39)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Which isomerism a coordination compound can show is decided by what its formula holds: an ambidentate ligand, a counter-ion that can trade with a ligand, two complex ions, or solvent inside the sphere
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Ionization and coordination isomerism are both taught as 'something swaps between inside and outside the coordination sphere', so the compound printed as two ions is called the ionization case and the sulphate/bromide compound is left with coordination. What decides it is what swaps with what: a counter-ion for a ligand in row B, whole ligand sets between two metals in row C.
- **Why:** This question requires the criterion for each isomerism to be applied to a printed formula, demonstrated by row A carrying the ambidentate NO₂ in [Co(NH₃)₅(NO₂)]Cl₂ and row C carrying two complex ions in [Co(NH₃)₆][Cr(CN)₆], which decide 'Linkage isomerism' and 'Coordination isomerism'.
- **Note:** Trap label decided by the rulebook's swap test: 'ionization' and 'coordination' read nothing alike, so the pull is that the source prints the two in one list of isomerism types — position, not likeness, hence nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q59

Chemistry · physical · Basic Concepts of Chemistry

1 gram of sodium hydroxide was treated with $25\,\mathrm{mL}$ of $0.75\,\mathrm{M}$ $\mathrm{HCl}$ solution, the mass of sodium hydroxide left unreacted is equal to

- (1) $750\,\mathrm{mg}$
- **(2)** $250\,\mathrm{mg}$
- (3) Zero mg
- (4) $200\,\mathrm{mg}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{M} = \frac{\mathrm{W} \times 1000}{\mathrm{M_2} \times \mathrm{V\ (in\ mL)}}$
2. $\mathrm{W} = \frac{\mathrm{M} \times \mathrm{M_2} \times \mathrm{V\ (in\ mL)}}{1000} = \frac{0.75 \times 36.5 \times 25}{1000}$
3. $= 0.684\,\mathrm{g}$ (Mass of $\mathrm{HCl}$)
4. $\underset{36.5\,\mathrm{g}}{\mathrm{HCl}} + \underset{40\,\mathrm{g}}{\mathrm{NaOH}} \longrightarrow \mathrm{HCl} + \mathrm{NaOH}$
5. $36.5\,\mathrm{g}$ $\mathrm{HCl}$ reacts with $\mathrm{NaOH} = 40\,\mathrm{g}$
6. $0.684\,\mathrm{g}$ $\mathrm{HCl}$ reacts with $\mathrm{NaOH} = \frac{40}{36.5} \times 0.684 \simeq 0.750\,\mathrm{g}$
7. Amount of $\mathrm{NaOH}$ left $= 1\,\mathrm{g} - 0.750\,\mathrm{g} = 0.250\,\mathrm{g} = 250\,\mathrm{mg}$

**Solved independently** (answer withheld)

1. Moles of NaOH: $n_{\mathrm{NaOH}} = \frac{1\,\mathrm{g}}{40\,\mathrm{g\,mol^{-1}}} = 0.025\,\mathrm{mol}$.
2. Moles of HCl: $n_{\mathrm{HCl}} = 0.025\,\mathrm{L} \times 0.75\,\mathrm{mol\,L^{-1}} = 0.01875\,\mathrm{mol}$.
3. $\mathrm{NaOH + HCl \rightarrow NaCl + H_2O}$ is 1:1, so $0.01875\,\mathrm{mol}$ NaOH reacts.
4. Unreacted NaOH: $0.025 - 0.01875 = 0.00625\,\mathrm{mol}$.
5. Mass left: $0.00625 \times 40 = 0.25\,\mathrm{g} = 250\,\mathrm{mg}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q059_cd711509_29102026.png?v=cd71150998f2)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q059_11e3a7dc_29102026.png?v=11e3a7dc5bff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Limiting-reagent stoichiometry: the reagent in deficit fixes how much of the other is consumed, and the remainder is what is left unreacted
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  750 mg is the mass of NaOH the acid does consume: $0.025 \times 0.75 = 0.01875$ mol of HCl, which neutralises $0.01875 \times 40 = 0.75\,\mathrm{g}$ of NaOH. A student who finishes that multiplication finds the number already printed as an option, before the subtraction the stem actually asks for.
- **Why:** This question requires a limiting-reagent calculation and the subtraction that follows it, demonstrated by the stem asking for 'the mass of sodium hydroxide left unreacted' after 1 gram of NaOH meets 25 mL of 0.75 M HCl.
<!--/ecat-->

## Q60

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of electronegativity:
$\mathrm{N}$, $\mathrm{O}$, $\mathrm{F}$, $\mathrm{C}$, $\mathrm{Si}$
Choose the correct answer from the options given below:

- **(1)** $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$
- (2) $\mathrm{Si} < \mathrm{C} < \mathrm{O} < \mathrm{N} < \mathrm{F}$
- (3) $\mathrm{O} < \mathrm{F} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$
- (4) $\mathrm{F} < \mathrm{O} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Electronegativity increases across the period on moving left to right.
2. It decreases on moving down the group.
3. The correct option is $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$

**Solved independently** (answer withheld)

1. Across period 2, electronegativity increases left to right: $\mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$.
2. Down group 14, electronegativity decreases, so $\mathrm{Si} < \mathrm{C}$.
3. Combined order: $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$, which is option $1$.

**Subtopic:** Trends in Chemical Properties – Electronegativity and Electron Affinity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q060_5815e09a_29102026.png?v=5815e09a4506)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q060_66d853d8_29102026.png?v=66d853d87239)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Electronegativity rises across a period and falls down a group, so fluorine tops the scale and silicon is the lowest of these five
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The series is carried in memory as the descending run F, O, N, C, Si, and option 4 prints those five symbols in exactly that left-to-right order, so matching the symbols without reading the sign gives the reverse of the increasing order the stem asks for.
- **Why:** This question requires ranking five elements on the periodic electronegativity trend and printing that ranking in the stated direction, demonstrated by "increasing order of electronegativity" with the exact reverse sequence standing as option 4.
- **Note:** E1_question_type is arrange_in_order, which has no counterpart among the six qtype values; the shape on the page is a stem with four answer options, so qtype is mcq and the ordering demand is carried on asks: order.
<!--/ecat-->

## Q61

Chemistry · physical · Thermodynamics

Match List I with List II.

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Isothermal process | I | No heat exchange |
| B | Isochoric process | II | Carried out at constant temperature |
| C | Isobaric process | III | Carried out at constant volume |
| D | Adiabatic process | IV | Carried out at constant pressure |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-I, B-II, C-III, D-IV
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (A) Isothermal process $\Rightarrow$ Temperature is constant throughout the process
2. (B) Isochoric process $\Rightarrow$ Volume is constant throughout the process
3. (C) Isobaric process $\Rightarrow$ Pressure is constant throughout the process
4. (D) Adiabatic process $\Rightarrow$ No exchange of heat ($q$) between system and surrounding

**Solved independently** (answer withheld)

1. Isothermal: $T$ constant, so A-II; isochoric: $V$ constant, so B-III; isobaric: $P$ constant, so C-IV; adiabatic: $\Delta Q = 0$, so D-I. This is option $4$.

**Subtopic:** Thermodynamic Processes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q061_c0fa4e3b_29102026.png?v=c0fa4e3bf365)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q061_b7dd74a5_29102026.png?v=b7dd74a56970)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each 'iso-' process names the quantity held constant, while adiabatic is defined by no heat crossing the boundary
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Isothermal' carries 'therm', and therm calls up heat, so the process is paired with 'No heat exchange'. Isothermal fixes the temperature and lets heat flow freely; the process with no heat crossing the boundary is the adiabatic one.
- **Why:** This question requires the stated definition of each named process, demonstrated by List II printing them verbatim as 'Carried out at constant temperature', 'Carried out at constant volume', 'Carried out at constant pressure' and 'No heat exchange'.
- **Note:** Trap label decided by the swap test: replace 'isothermal' with a word carrying no heat root and the pull to 'No heat exchange' dies, so likeness is doing the work rather than the two processes being printed in one section.
<!--/ecat-->

## Q62

Chemistry · organic · Alcohols, Phenols and Ethers

Which one of the following alcohols reacts instantaneously with Lucas reagent?

- (1) $\mathrm{CH_3-CH_2-CH_2-CH_2OH}$
- (2) butan-2-ol `CCC(C)O` ![butan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_2_s1_c4a3c85d_30102026.svg?v=c4a3c85dc59b) — $\mathrm{CH_3-CH_2-CH(CH_3)-OH}$
- (3) 2-methylpropan-1-ol `CC(C)CO` ![2-methylpropan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_3_s1_8c9a66f5_30102026.svg?v=8c9a66f5ca6a) — $\mathrm{CH_3-CH(CH_3)-CH_2OH}$
- **(4)** 2-methylpropan-2-ol `CC(C)(C)O` ![2-methylpropan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_4_s1_8ebdae72_30102026.svg?v=8ebdae72a312) — $\mathrm{CH_3-C(CH_3)_2-OH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Tertiary alcohols react instantaneously with Lucas reagent and gives immediate turbidity.
2. In case of tertiary alcohols, they form halides easily with Lucas reagent (conc. $\mathrm{HCl}$ and $\mathrm{ZnCl_2}$)

**Solved independently** (answer withheld)

1. Lucas reagent ($\mathrm{ZnCl_2}$ + conc. $\mathrm{HCl}$) converts alcohols to alkyl chlorides via carbocations; the rate follows $3^\circ > 2^\circ > 1^\circ$.
2. Option 1 $\mathrm{CH_3CH_2CH_2CH_2OH}$ and option 3 $\mathrm{(CH_3)_2CHCH_2OH}$ are primary alcohols: no turbidity at room temperature.
3. Option 2 $\mathrm{CH_3CH_2CH(CH_3)OH}$ is a secondary alcohol: turbidity appears only after about 5 minutes.
4. Option 4 $\mathrm{(CH_3)_3C-OH}$ is a tertiary alcohol: it forms the stable $3^\circ$ carbocation and gives turbidity immediately, so the answer is option $4$.

**Subtopic:** Test of Alcohol · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q062_a440c60e_29102026.png?v=a440c60ef716)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q062_6080d114_29102026.png?v=6080d1144a32)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The Lucas test runs by $\mathrm{S_N1}$, so turbidity appears in the order set by carbocation stability: tertiary at once, secondary in minutes, primary only on heating
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Butan-2-ol does cloud the Lucas reagent, so a student holding "Lucas reagent reacts with secondary and tertiary alcohols" stops at the secondary structure; the word "instantaneously" is the part of the test that separates the two, and the secondary alcohol takes about five minutes.
- **Why:** This question requires applying the Lucas-test reactivity order to four printed structures, demonstrated by "reacts instantaneously with Lucas reagent" with the four options differing only in where the chain branches.
<!--/ecat-->

## Q63

Chemistry · physical · Structure of Atom

The energy of an electron in the ground state ($n = 1$) for $\mathrm{He^{+}}$ ion is $-x\,\mathrm{J}$, then that for an electron in $n = 2$ state for $\mathrm{Be^{3+}}$ ion in J is

- **(1)** $-x$
- (2) $-\dfrac{x}{9}$
- (3) $-4x$
- (4) $-\dfrac{4}{9}x$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
2. For $\mathrm{He^{+}}$ $(n = 1)$,
3. $E_n = -x = -R_H\left(\frac{2^2}{1^2}\right) = -4R_H$
4. $\therefore\ R_H = \frac{x}{4}$
5. For $\mathrm{Be^{3+}}$ $(n = 2)$,
6. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
7. $= -\frac{x}{4} \times \left(\frac{4 \times 4}{2 \times 2}\right) = -x\,\mathrm{J}$

**Solved independently** (answer withheld)

1. For a hydrogen-like ion, $E_n = -k\frac{Z^2}{n^2}$.
2. For $\mathrm{He^{+}}$, $Z = 2$, $n = 1$: $E = -k\frac{2^2}{1^2} = -4k = -x$.
3. For $\mathrm{Be^{3+}}$, $Z = 4$, $n = 2$: $E = -k\frac{4^2}{2^2} = -4k$.
4. So $E_{\mathrm{Be^{3+}},\,n=2} = -x\,\mathrm{J}$, which is option $1$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q063_75b30fbd_29102026.png?v=75b30fbd5327)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q063_3cfef9bd_29102026.png?v=3cfef9bdbe44)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a one-electron ion the Bohr energy goes as $-13.6\,Z^2/n^2$ eV, so doubling the nuclear charge and the level together leaves the energy unchanged
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Beryllium's $Z = 4$ is twice helium's $Z = 2$ and the energy carries $Z^2$, so comparing the two ions on charge alone gives four times deeper, $-4x$, with the $1/n^2$ that the stem's $n = 2$ supplies left out of the comparison.
- **Why:** This question requires comparing $-13.6\,Z^2/n^2$ for two one-electron ions and reporting the factor by which the energy changes, demonstrated by the options being $-x$, $-x/9$, $-4x$ and $-\frac{4}{9}x$, every one a multiple of the given energy.
- **Note:** formula_misused rather than arithmetic_slip on option 3: the $1/n^2$ is not lost in the arithmetic, it is absent from the relation being compared, which §5.1 calls the right relation misremembered.
<!--/ecat-->

## Q64

Chemistry · organic · Haloalkanes and Haloarenes

The compound that will undergo $\mathrm{S_N1}$ reaction with the fastest rate is

- (1) (bromomethyl)cyclohexane `BrCC1CCCCC1` ![(bromomethyl)cyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_1_s1_757d45db_30102026.svg?v=757d45db512a)
- (2) bromocyclohexane `BrC1CCCCC1` ![bromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_2_s1_e13bf846_30102026.svg?v=e13bf8460aa7)
- (3) bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_3_s1_2d0c8cae_30102026.svg?v=2d0c8caedcd4)
- **(4)** (1-bromoethyl)benzene `CC(Br)c1ccccc1` ![(1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_4_s1_4d3516dc_30102026.svg?v=4d3516dc2b4d)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Reactivity towards $\mathrm{S_N1}$ depends upon stability of carbocation.
2. Order of stability is

![printed figure: 1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q064_sol_1_36ca61a0_29102026.png?v=36ca61a01c87)

*1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation*

![drawn: 1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_solution_1_58363708_30102026.svg?v=58363708d6a4)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

3. Hence

![printed figure: (1-bromoethyl)benzene is](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q064_sol_2_dbc33ac1_29102026.png?v=dbc33ac125ec)

*(1-bromoethyl)benzene is*

![drawn: (1-bromoethyl)benzene is](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q064_solution_2_9e6cdce8_30102026.svg?v=9e6cdce857cf)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

4. is most reactive

**Solved independently** (answer withheld)

1. $\mathrm{S_N1}$ rate depends on the stability of the carbocation formed in the slow ionisation step.
2. Option 1, $\mathrm{C_6H_{11}CH_2Br}$, would give a primary carbocation, which is very unstable.
3. Option 2, $\mathrm{C_6H_{11}Br}$, gives a secondary carbocation with no resonance stabilisation.
4. Option 3, $\mathrm{C_6H_5Br}$, has a C-Br bond with partial double-bond character and would give an unstable phenyl cation, so it does not undergo $\mathrm{S_N1}$.
5. Option 4, $\mathrm{C_6H_5CH(Br)CH_3}$, gives $\mathrm{C_6H_5\overset{+}{C}HCH_3}$, a secondary benzylic carbocation stabilised by resonance with the ring.
6. The benzylic cation is the most stable, so option $4$ reacts fastest.

**Subtopic:** Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q064_96b1b97b_29102026.png?v=96b1b97b2ed3)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q064_2b45b9c1_29102026.png?v=2b45b9c1df53)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\mathrm{S_N1}$ rate follows carbocation stability, so the fastest substrate is the one whose departing halide leaves the best-stabilised cation
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options are stored in this record as empty strings, so no structure can be examined and no route to a wrong option can be shown
- **Why:** This question requires applying the carbocation-stability ranking to decide a relative rate, demonstrated by "will undergo $\mathrm{S_N1}$ reaction with the fastest rate".
- **Note:** options_en carries four empty strings: the paper prints four drawn structures that did not survive extraction, has_figure is false and figure_image is null, so nothing was supplied to inspect and no trap is written. qtype and asks are taken from the stem, which is intact. A reviewer holding the structures should check whether an allylic or benzylic halide is printed beside the tertiary one, and whether a secondary halide sits next to it, since the ranking turns on which cation is better stabilised.
<!--/ecat-->

## Q65

Chemistry · physical · Solutions

The Henry’s law constant ($K_\mathrm{H}$) values of three gases (A, B, C) in water are 145, $2 \times 10^{-5}$ and $35\,\mathrm{kbar}$, respectively. The solubility of these gases in water follow the order:

- (1) B > A > C
- **(2)** B > C > A
- (3) A > C > B
- (4) A > B > C

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Value of Henry’s law constant $\propto \frac{1}{\text{Solubility of gas}}$
2. Higher the value of $K_{\mathrm{H}}$ at a given pressure, lower is the solubility of the gas in the liquid.
3. $K_{\mathrm{H}}$ value of gases (given) : $\mathrm{A} > \mathrm{C} > \mathrm{B}$
4. $\therefore$ Order of solubility of gases in water : $\mathrm{B} > \mathrm{C} > \mathrm{A}$

**Solved independently** (answer withheld)

1. Henry's law: $p = K_\mathrm{H}\,x$, so at a given pressure $x = \frac{p}{K_\mathrm{H}}$; a larger $K_\mathrm{H}$ means lower solubility.
2. Order the constants: $K_\mathrm{H}(B) = 2 \times 10^{-5} < K_\mathrm{H}(C) = 35 < K_\mathrm{H}(A) = 145\,\mathrm{kbar}$.
3. Reverse the order for solubility: $B > C > A$, which is option $2$.

**Subtopic:** Solubility of a Gas in a Liquid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q065_076e4b56_29102026.png?v=076e4b566b3e)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q065_f4d472c1_29102026.png?v=f4d472c1943e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Henry's law constant is inversely related to solubility: in $p = K_\mathrm{H}x$ the larger the constant, the less of the gas dissolves at a given pressure
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Sorting the three printed numbers straight down, 145 then 35 then $2 \times 10^{-5}$, gives A > C > B, which reads $K_\mathrm{H}$ as if it measured how much dissolves; the constant sits on the other side of $p = K_\mathrm{H}x$, so the biggest constant belongs to the least soluble gas.
- **Why:** This question requires inverting Henry's constant into a solubility ranking, demonstrated by "the solubility of these gases in water follow the order" set against constants of 145, $2 \times 10^{-5}$ and 35 kbar, with the straight ranking of those three numbers printed as option 3.
- **Note:** E1_question_type is statement_options, which contradicts the printed shape: the options are bare orderings such as "B > A > C", not full statements, so qtype is recorded as mcq.
<!--/ecat-->

## Q66

Chemistry · physical · Chemical Kinetics

Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?

- (1) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope starting slightly below the origin (negative intercept) and rising to the right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q066_option_1_618089d2_29102026.png?v=618089d21a0e) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope starting slightly below the origin (negative intercept) and rising to the right*
- (2) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope with a positive intercept on the ln k axis, rising to the right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q066_option_2_8bef8d02_29102026.png?v=8bef8d029756) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope with a positive intercept on the ln k axis, rising to the right*
- (3) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope passing through the origin, rising to the right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q066_option_3_6f507c08_29102026.png?v=6f507c088ae4) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line of positive slope passing through the origin, rising to the right*
- **(4)** ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line of negative slope starting at a positive intercept on the ln k axis and falling to meet the 1/T axis](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q066_option_4_9e5cb998_29102026.png?v=9e5cb99845a5) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line of negative slope starting at a positive intercept on the ln k axis and falling to meet the 1/T axis*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The Arrhenius equation is given as
2. $k = Ae^{-\frac{E_a}{RT}}$
3. $\therefore\ \ln k = \ln A - \frac{E_a}{RT}$
4. $\ln k$ v/s $\frac{1}{T}$ gives a straight line graph with slope $= -\frac{E_a}{R}$ and intercept $= \ln A$

![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line of negative slope; labels: Intercept = ln A (at the ln k axis), Slope = $-\frac{E_a}{R}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q066_sol_1_eefdebe8_29102026.png?v=eefdebe8cd90)

*graph of ln k (y-axis) vs 1/T (x-axis): a straight line of negative slope; labels: Intercept = ln A (at the ln k axis), Slope = $-\frac{E_a}{R}$*


**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$.
2. Taking logarithms: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$.
3. This is a straight line in $\frac{1}{T}$ with slope $-\frac{E_a}{R} < 0$ and intercept $\ln A$ on the $\ln k$ axis.
4. Options 1, 2 and 3 all show a positive slope; only option $4$ shows a falling straight line with a positive intercept, so the answer is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q066_5c833951_29102026.png?v=5c833951381e)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q066_39153234_29102026.png?v=391532340935)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Written as $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$, the Arrhenius equation is a straight line in $\ln k$ against $1/T$ with slope $-E_a/R$ and intercept $\ln A$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are plots and this record stores them as empty strings, so no curve can be inspected and no wrong option can be shown to pull
- **Why:** This question requires matching the Arrhenius equation to the plot that carries it, demonstrated by "Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?".
- **Note:** options_en holds four empty strings where the paper prints four graphs; has_figure is false and figure_image is null, so nothing graphical reached this step and no trap is written. qtype and asks come from the stem, which is intact. A reviewer holding the plots should check the option drawn with a positive slope, which is what dropping the minus sign in $-E_a/R$ yields, and any curved plot, since linearity is exactly what the logarithmic form fixes.
<!--/ecat-->

## Q67

Chemistry · physical · Chemical Equilibrium

In which of the following equilibria, $K_p$ and $K_c$ are NOT equal?

- **(1)** $\mathrm{PCl_{5(g)} \rightleftharpoons PCl_{3(g)} + Cl_{2(g)}}$
- (2) $\mathrm{H_{2(g)} + I_{2(g)} \rightleftharpoons 2HI_{(g)}}$
- (3) $\mathrm{CO_{(g)} + H_2O_{(g)} \rightleftharpoons CO_{2(g)} + H_{2(g)}}$
- (4) $\mathrm{2BrCl_{(g)} \rightleftharpoons Br_{2(g)} + Cl_{2(g)}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $K_p = K_c\,(RT)^{\Delta n_g}$
2. for $K_p \neq K_c$,
3. $\Delta n_g \neq 0$
4. $\Delta n_g = n_p - n_r$
5. (1) $\Delta n_g = 2 - 1 = 1$
6. (2) $\Delta n_g = 2 - 2 = 0$
7. (3) $\Delta n_g = 2 - 2 = 0$
8. (4) $\Delta n_g = 2 - 2 = 0$

**Solved independently** (answer withheld)

1. $K_p = K_c (RT)^{\Delta n_g}$, so $K_p \neq K_c$ only when $\Delta n_g \neq 0$.
2. Option 1: $\Delta n_g = (1+1) - 1 = 1$, so $K_p = K_c RT \neq K_c$.
3. Option 2: $\Delta n_g = 2 - (1+1) = 0$, so $K_p = K_c$.
4. Option 3: $\Delta n_g = (1+1) - (1+1) = 0$, so $K_p = K_c$.
5. Option 4: $\Delta n_g = (1+1) - 2 = 0$, so $K_p = K_c$; hence the answer is option $1$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q067_b56a0dc2_29102026.png?v=b56a0dc250d7)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q067_b44c788d_29102026.png?v=b44c788d253a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $K_p = K_c(RT)^{\Delta n}$, so the two constants differ only when the balanced equation changes the number of moles of gas
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Counting gaseous species instead of moles makes $\mathrm{2BrCl \rightleftharpoons Br_2 + Cl_2}$ read as one gas becoming two, so $\Delta n$ comes out $+1$ and the option looks like the odd one out; the coefficient 2 puts two moles on each side, so $\Delta n = 0$.
- **Why:** This question requires $\Delta n$ for the gases read off each balanced equation and put into $K_p = K_c(RT)^{\Delta n}$, demonstrated by the stem 'In which of the following equilibria, $K_p$ and $K_c$ are NOT equal?' with every species printed as (g) so that only the coefficients decide.
- **Note:** The negation is carried by the capitalised NOT. Three options share $\Delta n = 0$, so reading past the negation names no single option and it is therefore not recorded as the trap.
<!--/ecat-->

## Q68

Chemistry · organic · Hydrocarbons

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- **(Statement I)** The boiling point of three isomeric pentanes follows the order
n-pentane $>$ isopentane $>$ neopentane
- **(Statement II)** When branching increases, the molecule attains a shape of sphere. This results in smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Both statement I and statement II are correct.
2. Boiling point of n-pentane $= 309\,\mathrm{K}$
3. isopentane $= 301\,\mathrm{K}$
4. neopentane $= 282.5$
5. As branching increases molecules attain the shape of a sphere results in smaller area of contact thus weak intermolecular forces between spherical molecules, which are overcome at relatively lower temperature.
6. Leading to decrease in boiling point.

**Solved independently** (answer withheld)

1. Statement I: boiling points are n-pentane ($309\,\text{K}$) $>$ isopentane ($301\,\text{K}$) $>$ neopentane ($282.5\,\text{K}$), so Statement I is correct.
2. Statement II: more branching makes the molecule closer to a sphere, which gives less surface area for contact, weaker van der Waals forces and a lower boiling point, so Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Physical Properties of Alkanes, Alkenes and Alkynes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q068_42018e51_29102026.png?v=42018e514dcc)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q068_969a63ea_29102026.png?v=969a63ea13e2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Branching lowers the boiling point of isomeric alkanes because a more spherical molecule offers less surface for van der Waals contact
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The melting-point trend sits beside the boiling points in the same physical-properties paragraph, and compact neopentane tops that one, so reaching for it makes the order in Statement I look inverted. Packing in the crystal sets melting points; boiling turns on surface contact in the liquid, which is the mechanism Statement II describes.
- **Why:** This question requires deciding whether a printed explanation accounts for a printed order, demonstrated by Statement II's 'smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point', which is the reason NCERT gives rather than a second separate fact. The swap test puts the trap at nearby_fact: renaming the rival trend to any unlike words leaves the pull intact, because it is the melting-point order printed beside the boiling points that carries it, not a resemblance between names.
<!--/ecat-->

## Q69

Chemistry · organic · Biomolecules

The reagents with which glucose does **not** react to give the corresponding tests/products are
Choose the correct options from the given below:

- **(A)** Tollen’s reagent
- **(B)** Schiff’s reagent
- **(C)** $\mathrm{HCN}$
- **(D)** $\mathrm{NH_2OH}$
- **(E)** $\mathrm{NaHSO_3}$

- (1) B and C
- (2) A and D
- **(3)** B and E
- (4) E and D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Despite having the aldehyde group glucose does not give Schiff’s test and it does not form the hydrogen sulphite addition product with $\mathrm{NaHSO_3}$.

**Solved independently** (answer withheld)

1. Glucose reduces Tollens' reagent to give a silver mirror, so $\mathrm{A}$ reacts.
2. Glucose adds $\mathrm{HCN}$ to form a cyanohydrin, so $\mathrm{C}$ reacts.
3. Glucose reacts with $\mathrm{NH_2OH}$ to form an oxime, so $\mathrm{D}$ reacts.
4. Glucose gives no Schiff's test and forms no hydrogensulphite addition product with $\mathrm{NaHSO_3}$, because it exists mainly in the cyclic hemiacetal form, so $\mathrm{B}$ and $\mathrm{E}$ do not react.
5. The reagents that do not react are $\mathrm{B}$ and $\mathrm{E}$, which is option $3$.

**Subtopic:** Structure and Reactions of Glucose · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q069_88dc1cb6_29102026.png?v=88dc1cb64e78)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q069_42419128_29102026.png?v=424191282cd1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Glucose sits mainly in its cyclic hemiacetal form, so it still gives the carbonyl reactions with HCN and $\mathrm{NH_2OH}$ and still reduces Tollen's reagent, yet refuses Schiff's test and the $\mathrm{NaHSO_3}$ addition
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  NCERT prints the reagents glucose does react with - Tollen's, HCN, $\mathrm{NH_2OH}$ - in the sentences next to the two it refuses, so a student holding 'glucose fails Schiff's test' fills the second slot from the adjacent list and marks HCN. Glucose does add HCN to give the cyanohydrin, which is cited as evidence that the carbonyl group is present.
- **Why:** This question requires the reagent-by-reagent record of what glucose does and does not react with, demonstrated by the stem asking for 'the reagents with which glucose does **not** react to give the corresponding tests/products' across five named reagents.
- **Note:** half_right was considered, since option 1 holds one correct member and one wrong one, but the swap test in the rulebook decides it: 'Schiff's reagent' and 'HCN' resemble each other not at all, and replacing either with an unlike reagent name leaves the trap intact, because what carries the student is which of the two adjacent NCERT lists the reagent sits in. Options 1 and 4 carry the same device on opposite halves of the key pair; option 1 is recorded as the trap because the Schiff's-test line is the one the stem's own wording ('tests/products') echoes first.
<!--/ecat-->

## Q70

Chemistry · physical · Thermodynamics

In which of the following processes entropy increases?
Choose the correct answer from the options given below:

- **(A)** A liquid evaporates to vapour.
- **(B)** Temperature of a crystalline solid lowered from $130\,\mathrm{K}$ to $0\,\mathrm{K}$.
- **(C)** $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
- **(D)** $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$

- (1) A and C
- (2) A, B and D
- **(3)** A, C and D
- (4) C and D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When a liquid evaporates to vapour entropy increases.
2. $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
3. Number of gaseous product molecules increases so entropy increases.
4. $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$
5. $1$ mole $\mathrm{Cl_{2(g)}}$ form $2$ mol $\mathrm{Cl_{(g)}}$. So entropy increases.

**Solved independently** (answer withheld)

1. A: $\mathrm{liquid \rightarrow vapour}$ increases molecular disorder, so $\Delta S > 0$.
2. B: cooling a crystalline solid from $130\,\mathrm{K}$ to $0\,\mathrm{K}$ reduces disorder, so $\Delta S < 0$.
3. C: $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$ has $\Delta n_g = +2$, so $\Delta S > 0$.
4. D: $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$ has $\Delta n_g = +1$, so $\Delta S > 0$.
5. Entropy increases in A, C and D, which is option $3$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q070_3c8fd1ff_29102026.png?v=3c8fd1ffd07d)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q070_278fd8c4_29102026.png?v=278fd8c42000)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Entropy rises when the number of freely moving particles rises - a liquid becoming vapour, a solid giving off gases, or one mole of gas splitting into two
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Counting an entropy rise only where the state of matter becomes less ordered picks up A and C and leaves D unmarked, because $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$ is gas on both sides. Splitting one mole of gas into two moles of atoms doubles the number of independent particles, so D is an increase as well.
- **Why:** This question requires the disorder rule applied to each printed change, demonstrated by 'In which of the following processes entropy increases?' set over items as unlike as 'A liquid evaporates to vapour' and '$\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$'.
- **Note:** B is the only false item in the printed list, so the two wrong options split cleanly: option 2 is the one that admits B, and options 1 and 4 are true but short of the full set.
<!--/ecat-->

## Q71

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List I with List II.
Choose the correct answer from the options given below:

![printed figure: cyclohexylidenecyclohexane → 2 cyclohexanone; benzene → diphenylmethanone; cyclohexanol → cyclohexanone; ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q071_6d593cfa_29102026.png?v=6d593cfaf449)

*cyclohexylidenecyclohexane → 2 cyclohexanone; benzene → diphenylmethanone; cyclohexanol → cyclohexanone; ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$*

Structures: cyclohexylidenecyclohexane `C1CCC(=C2CCCCC2)CC1`; cyclohexanone `O=C1CCCCC1`; benzene `c1ccccc1`; diphenylmethanone `O=C(c1ccccc1)c1ccccc1`; cyclohexanol `OC1CCCCC1`; cyclohexanone `O=C1CCCCC1`; ethylbenzene `CCc1ccccc1`; potassium benzoate `O=C([O-])c1ccccc1.[K+]`; benzoyl chloride `O=C(Cl)c1ccccc1`

| List-I | | List-II | |
|---|---|---|---|
| A | Cyclohexylidenecyclohexane $\rightarrow$ 2 Cyclohexanone | I | $\mathrm{C_6H_5COCl}$/Anhyd. $\mathrm{AlCl_3}$ |
| B | Benzene $\rightarrow$ Benzophenone ($\mathrm{C_6H_5COC_6H_5}$) | II | $\mathrm{CrO_3}$ |
| C | Cyclohexanol $\rightarrow$ Cyclohexanone | III | $\mathrm{KMnO_4/KOH}$, $\Delta$ |
| D | Ethylbenzene ($\mathrm{C_6H_5CH_2CH_3}$) $\rightarrow$ Potassium benzoate ($\mathrm{C_6H_5COOK}$) | IV | (i) $\mathrm{O_3}$ (ii) $\mathrm{Zn\text{-}H_2O}$ |

- (1) A-IV, B-I, C-III, D-II
- (2) A-III, B-I, C-II, D-IV
- **(3)** A-IV, B-I, C-II, D-III
- (4) A-I, B-IV, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: (A) cyclohexylidenecyclohexane →((i) $\ce{O3}$, (ii) $\ce{Zn-H2O}$) 2 cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q071_sol_1_5c168b1a_29102026.png?v=5c168b1a89dc)

*(A) cyclohexylidenecyclohexane →[(i) $\ce{O3}$, (ii) $\ce{Zn-H2O}$] 2 cyclohexanone*

1. It is reductive ozonolysis

![printed figure: (B) benzene →(benzoyl chloride/Anhyd. $\ce{AlCl3}$) diphenylmethanone](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q071_sol_2_f5051a39_29102026.png?v=f5051a3925e5)

*(B) benzene →[benzoyl chloride/Anhyd. $\ce{AlCl3}$] diphenylmethanone*

2. It is Friedel-Crafts acylation reaction.

![printed figure: (C) cyclohexanol →($\ce{CrO3}$) cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q071_sol_3_82c6db8f_29102026.png?v=82c6db8f7712)

*(C) cyclohexanol →[$\ce{CrO3}$] cyclohexanone*

3. Secondary alcohols are oxidised to ketones by $\mathrm{CrO_3}$

![printed figure: (D) ethylbenzene →($\ce{KMnO4}$, KOH, Δ) potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q071_sol_4_02f46360_29102026.png?v=02f463607928)

*(D) ethylbenzene →[$\ce{KMnO4}$, KOH, Δ] potassium benzoate*


**Solved independently** (answer withheld)

1. A: reductive ozonolysis of the $\mathrm{C=C}$ in cyclohexylidenecyclohexane gives $2$ cyclohexanone, so $\mathrm{A \to IV}$ ((i) $\mathrm{O_3}$ (ii) $\mathrm{Zn\text{-}H_2O}$).
2. B: Friedel-Crafts acylation $\mathrm{C_6H_6 + C_6H_5COCl \xrightarrow{AlCl_3} C_6H_5COC_6H_5}$, so $\mathrm{B \to I}$.
3. C: $\mathrm{CrO_3}$ oxidises the secondary alcohol cyclohexanol to cyclohexanone, so $\mathrm{C \to II}$.
4. D: hot alkaline $\mathrm{KMnO_4}$ oxidises the whole alkyl side chain to $\mathrm{-COOK}$, giving $\mathrm{C_6H_5COOK}$, so $\mathrm{D \to III}$.
5. $\mathrm{A\text{-}IV, B\text{-}I, C\text{-}II, D\text{-}III}$ is option $3$.

**Subtopic:** Preparation of Ketones, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q071_6c4f29c0_29102026.png?v=6c4f29c0d9dd)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q071_9b87d11c_29102026.png?v=9b87d11c6f26)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Matching a reagent to the conversion it performs: ozonolysis cleaves C=C, benzoyl chloride with AlCl₃ acylates an arene, CrO₃ takes a secondary alcohol to a ketone, and hot alkaline KMnO₄ cuts a benzylic side chain back to the carboxylate salt
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  KMnO₄ is the oxidant that comes first to hand for taking a secondary alcohol to a ketone, so entry III is placed on cyclohexanol and CrO₃ is pushed onto the ethylbenzene row. The product printed for that row is potassium benzoate, and the potassium can only come from the KOH in entry III.
- **Why:** This question requires the reagent that effects each printed conversion, demonstrated by row D reading 'Ethylbenzene → Potassium benzoate' against reagent entries that include 'KMnO₄/KOH, Δ'.
- **Note:** The record's RDKit render carries status failed_check, but List I and List II are printed in full as text, including entry IV's '(i) O₃ (ii) Zn-H₂O', so the question is complete for tagging and no source damage is claimed.
<!--/ecat-->

## Q72

Chemistry · inorganic · The p–Block Elements

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** The boiling point of hydrides of Group 16 elements follow the order $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
- **(Statement II)** On the basis of molecular mass, $\mathrm{H_2O}$ is expected to have lower boiling point than the other members of the group but due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Statement I is correct, because boiling point of hydrides of group $16$ follows the order
2. $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
3. Statement II due to intermolecular H-bonding $\mathrm{H_2O}$ shows higher boiling point than respective hydrides of group $16$.
4. (Both Statement are true)
5. Order from $\mathrm{H_2Te}$ to $\mathrm{H_2S}$ is due to decreasing molar mass.

**Solved independently** (answer withheld)

1. Among $\mathrm{H_2S}$, $\mathrm{H_2Se}$, $\mathrm{H_2Te}$ boiling point rises with molar mass (van der Waals forces): $\mathrm{H_2Te\,(271\,K) > H_2Se\,(232\,K) > H_2S\,(213\,K)}$.
2. $\mathrm{H_2O}$ boils at $373\,\mathrm{K}$, the highest, so $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$ and Statement I is true.
3. By molar mass alone $\mathrm{H_2O}$ ($18$) should boil lowest; extensive intermolecular H-bonding makes it highest, so Statement II is true.
4. Both statements are true, which is option $1$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q072_e870f259_29102026.png?v=e870f259cdf7)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q072_3a895638_29102026.png?v=3a89563887a8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Hydrogen bonding lifts water out of the molecular-mass boiling-point order of the Group 16 hydrides, while the other three rise with size
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The hydride order printed beside boiling point in the Group 16 table is thermal stability, $H_2O > H_2S > H_2Se > H_2Te$, falling steadily down the group, so reaching for it makes Statement I's tail $H_2Te > H_2Se > H_2S$ read backwards. Stability falls down the group because the bond weakens; boiling point rises because van der Waals forces grow with size once H-bonding is out of the picture.
- **Why:** This question requires deciding whether hydrogen bonding accounts for water breaking the mass order, demonstrated by Statement II's 'due to the presence of extensive H-bonding in H2O, it has higher boiling point', with Statement I supplying the order that reason has to explain. The swap test puts the trap at nearby_fact: the rival order that makes Statement I look inverted is thermal stability, printed in the same hydride table, and renaming it to unlike words does not kill the pull, so position rather than likeness is doing the work.
<!--/ecat-->

## Q73

Chemistry · physical · Chemical Equilibrium

For the reaction $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$. At a given time, the composition of reaction mixture is: $[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$. Then, which of the following is correct?

- (1) Reaction is at equilibrium.
- (2) Reaction has a tendency to go in forward direction.
- **(3)** Reaction has a tendency to go in backward direction.
- (4) Reaction has gone to completion in forward direction.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$
2. At a given time $t$, $Q_C$ is to be calculated and been compared with $K_C$.
3. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^{2}} = \frac{(2 \times 10^{-3})(2 \times 10^{-3})}{(2 \times 10^{-3})^{2}}$
4. $Q_C = 1$
5. As $Q_C > K_C$, so reaction has a tendency to move backward.

**Solved independently** (answer withheld)

1. Write the reaction quotient: $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2}$.
2. $Q_C = \frac{(2 \times 10^{-3})(2 \times 10^{-3})}{(2 \times 10^{-3})^2} = 1$.
3. Compare: $Q_C = 1 > K_C = 4 \times 10^{-3}$.
4. When $Q_C > K_C$, the reaction tends to go in the backward direction, which is option $3$.

**Subtopic:** Predicting the Extent and Direction of a Reaction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q073_54cb4d33_29102026.png?v=54cb4d33a374)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q073_e46ff8fd_29102026.png?v=e46ff8fd8443)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Reaction quotient against equilibrium constant: $Q > K_C$ means the mixture must shift to the left
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Writing $Q$ as $\frac{[B][C]}{[A]}$ without the exponent from the coefficient 2 gives $2\times10^{-3}$, which sits below $K_C = 4\times10^{-3}$ and so points forward; with the square in place, $Q = 1$ and the comparison turns the other way.
- **Why:** This question requires the reaction quotient computed from the printed mixture and set against the equilibrium constant, demonstrated by '$K_C = 4 \times 10^{-3}$' being supplied beside '$[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$'.
- **Note:** E1's pattern read the four full-sentence options as statement_options. No statement block is printed and the stem asks which single outcome holds for one mixture rather than asking for a verdict on statements, so the shape recorded here is mcq.
<!--/ecat-->

## Q74

Chemistry · physical · Structure of Atom

Match List I with List II
List I (Quantum Number) | List II (Information provided)
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | $m_l$ | I | Shape of orbital |
| B | $m_s$ | II | Size of orbital |
| C | $l$ | III | Orientation of orbital |
| D | $n$ | IV | Orientation of spin of electron |

- (1) A-I, B-III, C-II, D-IV
- **(2)** A-III, B-IV, C-I, D-II
- (3) A-III, B-IV, C-II, D-I
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Magnetic quantum number $m_l$ informs about orientation of orbital.
2. Spin quantum number $m_s$ informs about orientation of spin of electron.
3. Azimuthal quantum number $(l)$ informs about shape of orbital
4. Principal quantum number $(n)$ informs about size of orbital

**Solved independently** (answer withheld)

1. $m_l$ (magnetic quantum number) gives the orientation of the orbital, so A-III; $m_s$ gives the orientation of the electron's spin, so B-IV; $l$ (azimuthal) gives the shape of the orbital, so C-I; $n$ (principal) gives the size of the orbital, so D-II, which is option $2$.

**Subtopic:** Quantum Numbers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q074_779a5aec_29102026.png?v=779a5aec0ffe)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q074_d8b87974_29102026.png?v=d8b879741ac5)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each quantum number carries one piece of information: n the size of the orbital, l its shape, m_l its orientation and m_s the orientation of the electron's spin
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Shape of orbital' and 'Size of orbital' are the same phrase with one short word changed, so a student who holds n and l apart only as 'the first two quantum numbers' takes whichever reads right and gives n the shape. The letter in 2p and 3d is the l value and it is l that fixes the shape, while n fixes how far the orbital extends.
- **Why:** This question requires the one piece of information each quantum number carries, demonstrated by List II printing 'Shape of orbital', 'Size of orbital', 'Orientation of orbital' and 'Orientation of spin of electron' against the bare symbols m_l, m_s, l and n.
- **Note:** Trap label decided by the swap test: rewrite entry II as 'radial extent of the electron cloud' and the two entries no longer read as one phrase with a word changed, and the pull dies — likeness wins over the fact that the n and l rows are printed together.
<!--/ecat-->

## Q75

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

A compound with a molecular formula of $\mathrm{C_6H_{14}}$ has two tertiary carbons. Its IUPAC name is :

- (1) n-hexane
- (2) 2-methylpentane
- **(3)** 2,3-dimethylbutane
- (4) 2,2-dimethylbutane

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{CH_3 - CH_2 - CH_2 - CH_2 - CH_2 - CH_3}$ has no tertiary carbon (n-Hexane)

![printed figure: 2-methylpentane, $\ce{H3C-CH2-CH2-CH(CH3)-CH3}$, main-chain carbons numbered 5, 4, 3, 2, 1 from left to right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q075_sol_1_3c4c978f_29102026.png?v=3c4c978f2699)

*2-methylpentane, $\ce{H3C-CH2-CH2-CH(CH3)-CH3}$, main-chain carbons numbered 5, 4, 3, 2, 1 from left to right*

![drawn: 2-methylpentane, $\ce{H3C-CH2-CH2-CH(CH3)-CH3}$, main-chain carbons numbered 5, 4, 3, 2, 1 from left to right](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q075_solution_1_585d705a_30102026.svg?v=585d705ac38b)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

2. has only one tertiary carbon (2-Methylpentane)

![printed figure: 2,3-dimethylbutane, $\ce{H3C-CH(CH3)-CH(CH3)-CH3}$, main-chain carbons numbered 1, 2, 3, 4 from left to right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q075_sol_2_305b8652_29102026.png?v=305b8652f9a8)

*2,3-dimethylbutane, $\ce{H3C-CH(CH3)-CH(CH3)-CH3}$, main-chain carbons numbered 1, 2, 3, 4 from left to right*

![drawn: 2,3-dimethylbutane, $\ce{H3C-CH(CH3)-CH(CH3)-CH3}$, main-chain carbons numbered 1, 2, 3, 4 from left to right](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q075_solution_2_d5e089fd_30102026.svg?v=d5e089fd210c)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

3. has two tertiary carbon. (2, 3-Dimethylbutane)

![printed figure: 2,2-dimethylbutane, $\ce{H3C-C(CH3)2-CH2-CH3}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q075_sol_3_0d123dfe_29102026.png?v=0d123dfe940c)

*2,2-dimethylbutane, $\ce{H3C-C(CH3)2-CH2-CH3}$*

![drawn: 2,2-dimethylbutane, $\ce{H3C-C(CH3)2-CH2-CH3}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q075_solution_3_d9ab31ad_30102026.svg?v=d9ab31ad2380)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

4. has no tertiary carbon (2, 2-Dimethylbutane)

**Solved independently** (answer withheld)

1. A tertiary carbon is bonded to three other carbons, i.e. a $\mathrm{CH}$ carbon in an alkane.
2. n-hexane $\mathrm{CH_3(CH_2)_4CH_3}$ has no tertiary carbon.
3. 2-methylpentane $\mathrm{(CH_3)_2CHCH_2CH_2CH_3}$ has one tertiary carbon (C-2).
4. 2,2-dimethylbutane $\mathrm{(CH_3)_3CCH_2CH_3}$ has a quaternary C-2 and no tertiary carbon.
5. 2,3-dimethylbutane $\mathrm{(CH_3)_2CH{-}CH(CH_3)_2}$ has two tertiary carbons (C-2 and C-3), which is option $3$.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q075_1eb686d6_29102026.png?v=1eb686d644c6)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q075_19a583ed_29102026.png?v=19a583ed4502)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Degree of a carbon atom: a tertiary carbon is joined to three other carbons, and among the $\mathrm{C_6H_{14}}$ isomers only 2,3-dimethylbutane carries two of them
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Reading 'two tertiary carbons' as 'the most branched skeleton' sends the student to 2,2-dimethylbutane, whose C2 carries two methyls plus C1 and C3 — four carbons, which makes it quaternary, the class printed next to tertiary, and leaves the isomer with no tertiary carbon at all.
- **Why:** This question requires the definition of a tertiary carbon applied to each $\mathrm{C_6H_{14}}$ isomer, demonstrated by 'has two tertiary carbons' being the only criterion the stem prints.
- **Note:** Test applied on the trap axis: swap 2,2-dimethylbutane and 2,3-dimethylbutane for two unlike names for the same skeletons and the route still lands on the 2,2 isomer, because it is reached by grading the branched carbon one class along the primary-to-quaternary series rather than by the likeness of the two printed names. Position does the work, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q76

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

On heating, some solid substances change from solid to vapour state without passing through liquid state. The technique used for the purification of such solid substances based on the above principle is known as

- (1) Crystallization
- **(2)** Sublimation
- (3) Distillation
- (4) Chromatography

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (1) Crystallization : It is based on difference in the solubilities of the compound and impurities in a suitable solvent.
2. (2) Sublimation : It is the purification technique based on principle that on heating, some solid substances change from solid to vapour state without passing through liquid state.
3. (3) Distillation : It is used to separate volatile liquids from non-volatile impurities and the liquids having sufficient difference in their boiling point.
4. (4) Chromatography : It is based on separation by using stationary and mobile phase.

**Solved independently** (answer withheld)

1. A solid passing directly to vapour on heating, skipping the liquid state, is sublimation; purifying sublimable solids from non-sublimable impurities this way is the sublimation technique, option $2$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q076_08ebde81_29102026.png?v=08ebde81fc64)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q076_6c0aaaeb_29102026.png?v=6c0aaaeb1b55)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sublimation purifies solids that pass straight from solid to vapour on heating, with no liquid stage in between
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The stem's words 'change from solid to vapour state' pick out the one other method in the same purification list that works through a vapour, and answering on 'vapour' alone reaches distillation; distillation boils a liquid, which is the stage the stem rules out.
- **Why:** This question requires the name the source gives to a stated purification principle, demonstrated by 'change from solid to vapour state without passing through liquid state' being the definition itself and the four options being the methods the chapter lists together.
- **Note:** Test applied on the trap axis: sublimation and distillation share no resemblance as words, and replacing them with two unlike names leaves the route intact, because what carries the student is their sitting together in one printed list of purification methods. Hence nearby_fact.
<!--/ecat-->

## Q77

Chemistry · organic · General Organic Chemistry

The most stable carbocation among the following is :

- (1) 2-methylpentan-3-ylium `CC[CH+]C(C)C` ![2-methylpentan-3-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_1_s1_b3402e87_30102026.svg?v=b3402e87400a)
- (2) 4-methylpentan-2-ylium `C[CH+]CC(C)C` ![4-methylpentan-2-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_2_s1_faebab24_30102026.svg?v=faebab248a5a)
- (3) cyclopentylmethylium `[CH2+]C1CCCC1` ![cyclopentylmethylium](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_3_s1_d417ac45_30102026.svg?v=d417ac453e11)
- **(4)** 1-methylcyclohexan-1-ylium `C[C+]1CCCCC1` ![1-methylcyclohexan-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_4_s1_f39bac72_30102026.svg?v=f39bac72ddb7)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The stability of carbocation can be described by the hyperconjugation. Greater the extent of hyperconjugation, more is the stability of carbocation.
2. (1) $\rightarrow 3\ \alpha\text{-H}$

![printed figure: (1) 2-methylpentan-3-ylium cation](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q077_sol_1_636bd302_29102026.png?v=636bd302b419)

*(1) 2-methylpentan-3-ylium cation*

![drawn: (1) 2-methylpentan-3-ylium cation](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_solution_1_5a7373ba_30102026.svg?v=5a7373ba90e0)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

3. (2) $\rightarrow 5\ \alpha\text{-H}$

![printed figure: (2) 4-methylpentan-2-ylium cation ($\ce{H3C-CH^+-CH2-CH(CH3)2}$)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q077_sol_2_861587f0_29102026.png?v=861587f0617e)

*(2) 4-methylpentan-2-ylium cation ($\ce{H3C-CH^+-CH2-CH(CH3)2}$)*

![drawn: (2) 4-methylpentan-2-ylium cation ($\ce{H3C-CH^+-CH2-CH(CH3)2}$)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_solution_2_f87da1ce_30102026.svg?v=f87da1cef850)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

4. (3) $\rightarrow 1\ \alpha\text{-H}$

![printed figure: (3) cyclopentylmethylium cation (cyclopentyl-$\ce{CH2^+}$)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q077_sol_3_ad05c286_29102026.png?v=ad05c2862340)

*(3) cyclopentylmethylium cation (cyclopentyl-$\ce{CH2^+}$)*

![drawn: (3) cyclopentylmethylium cation (cyclopentyl-$\ce{CH2^+}$)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_solution_3_44fbfd14_30102026.svg?v=44fbfd141a04)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

5. (4) $\rightarrow 7\ \alpha\text{-H}$

![printed figure: (4) 1-methylcyclohexylium cation](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q077_sol_4_9a2788d9_29102026.png?v=9a2788d91226)

*(4) 1-methylcyclohexylium cation*

![drawn: (4) 1-methylcyclohexylium cation](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q077_solution_4_04e27e21_30102026.svg?v=04e27e21e89c)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

6. Stability order of carbocations = (4) > (2) > (1) > (3)

**Solved independently** (answer withheld)

1. Option $1$: $\mathrm{CH_3CH_2\overset{+}{C}HCH(CH_3)_2}$ is a $2^\circ$ carbocation.
2. Option $2$: $\mathrm{CH_3\overset{+}{C}HCH_2CH(CH_3)_2}$ is a $2^\circ$ carbocation.
3. Option $3$: cyclopentyl$-\overset{+}{C}\mathrm{H_2}$ is a $1^\circ$ carbocation.
4. Option $4$: the positive carbon of the ring also bears $\mathrm{CH_3}$, so 1-methylcyclohexyl cation is a $3^\circ$ carbocation.
5. Carbocation stability order is $3^\circ > 2^\circ > 1^\circ$ (hyperconjugation and $+I$ effect), so the most stable is option $4$.

**Subtopic:** Hyperconjugation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q077_ac63b578_29102026.png?v=ac63b5788b5f)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q077_0caf18a4_29102026.png?v=0caf18a4caf6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Carbocation stability: the positive carbon is steadied by the alkyl groups around it and by any conjugation it can reach
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four option fields arrived at this step as empty strings, so there is no option text to examine and no route can be read from it
- **Why:** This question requires four carbocations ranked against one another on stability, demonstrated by the stem 'The most stable carbocation among the following is :', though the options that would be ranked did not reach this step.
- **Note:** The printed options are drawn structures and all four option fields are stored empty; has_figure is false and figure_image is null, so the structures were lost on extraction rather than withheld. No trap is written for an option set we do not hold. A reviewer working from the printed paper should check whether the distractors differ only in alkyl substitution around the cationic carbon, in which case the mechanism to confirm is a count of hyperconjugating alpha C-H bonds made at the wrong carbon; the subtopic recorded is Hyperconjugation.
<!--/ecat-->

## Q78

Chemistry · organic · Amines

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** Aniline does not undergo Friedel-Crafts alkylation reaction.
- **(Statement II)** Aniline cannot be prepared through Gabriel synthesis.

- **(1)** Both statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is correct but Statement II is false
- (4) Statement I is incorrect but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Aniline does not undergo Friedel-Crafts alkylation reaction due to salt formation with aluminium chloride, the Lewis acid, which is used as a catalyst.
2. Aniline (aromatic primary amine) cannot be prepared by Gabriel phthalimide synthesis because aryl halides do not undergo nucleophilic substitution with anion formed by phthalimide.

**Solved independently** (answer withheld)

1. Aniline is a Lewis base: $\mathrm{C_6H_5NH_2 + AlCl_3 \rightarrow C_6H_5NH_2^{+}\!-\!AlCl_3^{-}}$, and the positive N deactivates the ring, so no Friedel-Crafts reaction; Statement I is true.
2. Gabriel synthesis needs $\mathrm{S_N2}$ attack of the phthalimide anion on an alkyl halide; aryl halides do not undergo this substitution, so aniline (a primary aromatic amine) cannot be made this way; Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q078_ee731f47_29102026.png?v=ee731f47224f)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q078_90a14ed0_29102026.png?v=90a14ed0e8e1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aniline falls outside two general rules: AlCl3 ties up its lone pair so Friedel-Crafts fails, and an aryl halide will not react with phthalimide anion so Gabriel synthesis fails
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Gabriel phthalimide synthesis is carried as the clean route to primary amines and aniline is a primary amine, so the headline rule applied straight to it makes Statement II read false. The method's first step is nucleophilic substitution on a halide, and chlorobenzene will not give its halide up to the phthalimide anion, so aromatic primary amines sit outside the rule's reach.
- **Why:** This question requires knowing whether a named substrate undergoes two named transformations, demonstrated by 'Aniline does not undergo Friedel-Crafts alkylation reaction' and 'Aniline cannot be prepared through Gabriel synthesis', neither of which asks why and neither of which explains the other. The trap is condition_missed because the Gabriel rule is applied where its own requirement, a halide that undergoes nucleophilic substitution, does not hold.
- **Note:** Option wording is inconsistent as printed: options 1 and 2 use 'true/false' while option 3 reads 'correct but ... false' and option 4 'incorrect but ... true'. Tagged as printed; the four verdicts are the standard set.
<!--/ecat-->

## Q79

Chemistry · physical · Redox Reactions

Which reaction is NOT a redox reaction?

- (1) $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$
- (2) $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$
- (3) $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$
- **(4)** $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Oxidation-state annotated equation: $\ce{Zn^0 + CuSO4 -> ZnSO4 + Cu^0}$ (Cu in CuSO4 marked +2, Zn in ZnSO4 marked +2), Redox reaction; a bracket arrow labelled Reduction runs from Cu (+2) in CuSO4 to Cu (0), and a bracket arrow labelled Oxidation runs from Zn (0) to Zn (+2) in ZnSO4](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q079_sol_1_cad97766_29102026.png?v=cad97766e6a9)

*Oxidation-state annotated equation: $\ce{Zn^0 + CuSO4 -> ZnSO4 + Cu^0}$ (Cu in CuSO4 marked +2, Zn in ZnSO4 marked +2), Redox reaction; a bracket arrow labelled Reduction runs from Cu (+2) in CuSO4 to Cu (0), and a bracket arrow labelled Oxidation runs from Zn (0) to Zn (+2) in ZnSO4*

1. (1) $\mathrm{\overset{0}{Zn} + \overset{+2}{Cu}SO_4 \longrightarrow \overset{+2}{Zn}SO_4 + \overset{0}{Cu}}$, Redox reaction

![printed figure: Oxidation-state annotated equation: $\ce{KClO3 + I2^0 -> 2KIO3 + Cl2^0}$ (Cl in KClO3 marked +5, I in KIO3 marked +5), Redox reaction; a bracket arrow labelled Reduction runs from Cl (+5) in KClO3 to Cl2 (0), and a bracket arrow labelled Oxidation runs from I2 (0) to I (+5) in KIO3](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q079_sol_2_4020d406_29102026.png?v=4020d4066ee4)

*Oxidation-state annotated equation: $\ce{KClO3 + I2^0 -> 2KIO3 + Cl2^0}$ (Cl in KClO3 marked +5, I in KIO3 marked +5), Redox reaction; a bracket arrow labelled Reduction runs from Cl (+5) in KClO3 to Cl2 (0), and a bracket arrow labelled Oxidation runs from I2 (0) to I (+5) in KIO3*

2. (2) $\mathrm{K\overset{+5}{Cl}O_3 + \overset{0}{I_2} \longrightarrow 2K\overset{+5}{I}O_3 + \overset{0}{Cl_2}}$, Redox reaction

![printed figure: Oxidation-state annotated equation: $\ce{H2^0 + Cl2^0 -> 2HCl}$ (H in HCl marked +1, Cl in HCl marked −1), Redox reaction; a bracket arrow labelled Reduction runs from Cl2 (0) to Cl (−1) in HCl, and a bracket arrow labelled Oxidation runs from H2 (0) to H (+1) in HCl](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q079_sol_3_7ad39740_29102026.png?v=7ad3974031ae)

*Oxidation-state annotated equation: $\ce{H2^0 + Cl2^0 -> 2HCl}$ (H in HCl marked +1, Cl in HCl marked −1), Redox reaction; a bracket arrow labelled Reduction runs from Cl2 (0) to Cl (−1) in HCl, and a bracket arrow labelled Oxidation runs from H2 (0) to H (+1) in HCl*

3. (3) $\mathrm{\overset{0}{H_2} + \overset{0}{Cl_2} \longrightarrow 2\overset{+1}{H}Cl^{-1}}$, Redox reaction
4. (4) $\mathrm{\overset{+2}{Ba}Cl_2^{-1} + \overset{+1}{Na_2}SO_4^{-2} \longrightarrow \overset{+2}{Ba}SO_4 + 2\overset{+1}{Na}Cl^{-1}}$
5. This is not a redox reaction as there is no change in oxidation state.

**Solved independently** (answer withheld)

1. In option $1$, $\mathrm{Zn}$ goes $0 \rightarrow +2$ and $\mathrm{Cu}$ goes $+2 \rightarrow 0$, so it is redox.
2. In option $2$, $\mathrm{Cl}$ goes $+5 \rightarrow 0$ and $\mathrm{I}$ goes $0 \rightarrow +5$, so it is redox.
3. In option $3$, $\mathrm{H}$ goes $0 \rightarrow +1$ and $\mathrm{Cl}$ goes $0 \rightarrow -1$, so it is redox.
4. In option $4$, $\mathrm{Ba}\,(+2)$, $\mathrm{Cl}\,(-1)$, $\mathrm{Na}\,(+1)$, $\mathrm{S}\,(+6)$ and $\mathrm{O}\,(-2)$ keep their oxidation states; it is a double displacement (precipitation) reaction.
5. So the reaction that is not redox is option $4$.

**Subtopic:** Oxidation Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q079_85303a7d_29102026.png?v=85303a7d25a1)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q079_e3e2bd3a_29102026.png?v=e3e2bd3a938d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A reaction is redox only if at least one oxidation number changes; an exchange of partners that leaves every oxidation number untouched is not redox
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Holding chlorine at $-1$ wherever it appears makes $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$ read as iodine simply taking chlorine's place with nothing oxidised; the $-1$ rule holds only while the halogen is not bonded to oxygen, and in the chlorate chlorine is $+5$ and leaves as $\mathrm{Cl_2}$ at $0$.
- **Why:** This question requires oxidation numbers assigned on both sides of each printed equation, demonstrated by 'Which reaction is NOT a redox reaction?' set over four balanced equations rather than over any named reaction type.
- **Note:** E1's pattern returned null here because the options are whole reactions, while q067 of this same group carries equation options under plain_mcq; the pattern treated the two shapes inconsistently. The printed shape in both cases is a question with four answers, so both are recorded as mcq.
<!--/ecat-->

## Q80

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
List I (Compound) | List II (Shape/geometry)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{NH_3}$ | I | Trigonal Pyramidal |
| B | $\mathrm{BrF_5}$ | II | Square Planar |
| C | $\mathrm{XeF_4}$ | III | Octahedral |
| D | $\mathrm{SF_6}$ | IV | Square Pyramidal |

- **(1)** A-I, B-IV, C-II, D-III
- (2) A-II, B-IV, C-III, D-I
- (3) A-III, B-IV, C-I, D-II
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{NH_3} \Rightarrow$ $sp^{3}$ hybridised with $1$ lone pair.
2. Structure will be Trigonal Pyramidal.
3. $\mathrm{BrF_5} \Rightarrow$ $sp^{3}d^{2}$ hybridised with $1$ lone pair.
4. Structure will be Square Pyramidal.
5. $\mathrm{XeF_4} \Rightarrow$ $sp^{3}d^{2}$ with two lone pairs.
6. Structure will be Square Planar.
7. $\mathrm{SF_6} \Rightarrow$ $sp^{3}d^{2}$ with no lone pair.
8. Structure will be Octahedral.
9. A-I, B-IV, C-II, D-III

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: 3 bond pairs + 1 lone pair on N, so the shape is trigonal pyramidal: A-I.
2. $\mathrm{BrF_5}$: 5 bond pairs + 1 lone pair on Br (octahedral electron geometry), so the shape is square pyramidal: B-IV.
3. $\mathrm{XeF_4}$: 4 bond pairs + 2 lone pairs on Xe (opposite each other), so the shape is square planar: C-II.
4. $\mathrm{SF_6}$: 6 bond pairs, no lone pair on S, so the shape is octahedral: D-III.
5. A-I, B-IV, C-II, D-III matches option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q080_8fff7e31_29102026.png?v=8fff7e319671)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q080_db6e8408_29102026.png?v=db6e840821d0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR: the molecular shape is the arrangement of the bonded atoms left after every lone pair is taken out of the parent electron-pair geometry
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Counting six electron pairs round the central atom and naming that parent polyhedron gives BrF5 'octahedral', and dropping only the first lone pair out of XeF4 gives it 'square pyramidal'; option 4 is the only code carrying both, so the two rows treated as the hard ones appear to settle it.
- **Why:** This question requires VSEPR applied row by row, working each shape from the bonded atoms and the lone pairs on the named central atom, demonstrated by List II printing 'Square Pyramidal', 'Square Planar' and 'Octahedral' together, the three names one six-electron-pair parent yields at lone-pair counts of one, two and zero.
- **Note:** Key confirmed as printed against the shapes themselves: NH3 trigonal pyramidal, BrF5 square pyramidal, XeF4 square planar, SF6 octahedral, which is option 1. Worth recording for a reviewer that all three wrong codes assign NH3 a six-pair name, so the single row NH3 to Trigonal Pyramidal strikes out every distractor at once; that is why the trap had to be located in the BrF5/XeF4 rows a student checks first rather than in the code as a whole.
<!--/ecat-->

## Q81

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of first ionization enthalpy: $\mathrm{Li}$, $\mathrm{Be}$, $\mathrm{B}$, $\mathrm{C}$, $\mathrm{N}$ Choose the correct answer from the options given below:

- (1) $\mathrm{Li} < \mathrm{Be} < \mathrm{B} < \mathrm{C} < \mathrm{N}$
- **(2)** $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$
- (3) $\mathrm{Li} < \mathrm{Be} < \mathrm{C} < \mathrm{B} < \mathrm{N}$
- (4) $\mathrm{Li} < \mathrm{Be} < \mathrm{N} < \mathrm{B} < \mathrm{C}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Increasing order of first ionization enthalpy is $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$

![printed figure: table of first ionization enthalpy (Δ_iH/kJ mol⁻¹) by element: Li 520; Be 899; B 801; C 1086; N 1402](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q081_sol_1_5f6ccb86_29102026.svg?v=5f6ccb8636b3)

*table of first ionization enthalpy (Δ_iH/kJ mol⁻¹) by element: Li 520; Be 899; B 801; C 1086; N 1402*


**Solved independently** (answer withheld)

1. Across period 2, $\Delta_i H_1$ generally increases with nuclear charge, so $\mathrm{Li}$ is lowest and $\mathrm{N}$ is highest.
2. $\mathrm{B}$ ($2s^2 2p^1$) loses a $2p$ electron that is shielded by $2s$ and less penetrating, while $\mathrm{Be}$ ($2s^2$) loses a $2s$ electron, so $\Delta_i H_1(\mathrm{B}) < \Delta_i H_1(\mathrm{Be})$.
3. $\mathrm{C}$ has higher nuclear charge than $\mathrm{Be}$ and $\mathrm{B}$, so $\Delta_i H_1(\mathrm{Be}) < \Delta_i H_1(\mathrm{C}) < \Delta_i H_1(\mathrm{N})$.
4. Order: $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 37)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q081_a0c382d9_29102026.png?v=a0c382d9294a)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q081_a13cc273_29102026.png?v=a13cc2734805)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** First ionisation enthalpy rises across period 2, but beryllium exceeds boron because boron's outgoing electron leaves a higher-energy 2p orbital while beryllium's leaves a filled 2s
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The trend 'ionisation enthalpy increases left to right' is run straight across Li, Be, B, C, N and reproduces the elements in the order the stem prints them; the trend's own basis fails at Be to B, where the electron removed switches from 2s to 2p and the value drops from 899 to 801 kJ mol$^{-1}$.
- **Why:** This question requires the across-period ionisation-enthalpy trend together with the point where it breaks, demonstrated by 'increasing order of first ionization enthalpy' asked over a list containing both Be and B.
- **Note:** E1's arrange_in_order has no counterpart in this axis's qtype list, so the printed shape is recorded as mcq and the ordering is carried by asks: order.
<!--/ecat-->

## Q82

Chemistry · inorganic · The D- and F-Block Elements – Practice

‘Spin only’ magnetic moment is same for which of the following ions?
Choose the most appropriate answer from the options given below.

- **(A)** $\mathrm{Ti^{3+}}$
- **(B)** $\mathrm{Cr^{2+}}$
- **(C)** $\mathrm{Mn^{2+}}$
- **(D)** $\mathrm{Fe^{2+}}$
- **(E)** $\mathrm{Sc^{3+}}$

- **(1)** B and D only
- (2) A and E only
- (3) B and C only
- (4) A and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ions | No. of unpaired electrons | Configuration
2. $\mathrm{Ti^{3+}}$ | $1$ | $3d^{1}$
3. $\mathrm{Cr^{2+}}$ | $4$ | $3d^{4}$
4. $\mathrm{Mn^{2+}}$ | $5$ | $3d^{5}$
5. $\mathrm{Fe^{2+}}$ | $4$ | $3d^{6}$
6. $\mathrm{Sc^{3+}}$ | $0$ | $3d^{0}$
7. Spin only magnetic moment is given by $\sqrt{n(n+2)}\,\mathrm{BM}$
8. $\therefore$ $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ will have same spin only magnetic moment.

**Solved independently** (answer withheld)

1. Configurations: $\mathrm{Ti^{3+}}: 3d^1$, $\mathrm{Cr^{2+}}: 3d^4$, $\mathrm{Mn^{2+}}: 3d^5$, $\mathrm{Fe^{2+}}: 3d^6$, $\mathrm{Sc^{3+}}: 3d^0$.
2. Unpaired electrons (high spin): $n = 1, 4, 5, 4, 0$ respectively.
3. $\mu = \sqrt{n(n+2)}$ BM, so $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ both give $\mu = \sqrt{24} \approx 4.90$ BM.
4. Only B and D share the same value, which is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q082_a42b6575_29102026.png?v=a42b6575b7e3)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q082_5beb9df8_29102026.png?v=5beb9df81018)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only moment $\mu = \sqrt{n(n+2)}$ depends only on the number of unpaired d electrons, so $d^4$ and $d^6$ both carry four and both read 4.90 BM
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Chromium's half-filled $[\mathrm{Ar}]3d^5 4s^1$ is a fact about the neutral atom, and carried across to $\mathrm{Cr^{2+}}$ it leaves five unpaired electrons, matching $\mathrm{Mn^{2+}}$ at 5.92 BM. Taking away both electrons - the lone 4s and one 3d - leaves $3d^4$, four unpaired, 4.90 BM.
- **Why:** This question requires the spin-only moment worked out for each ion from its own unpaired-electron count, demonstrated by "'Spin only' magnetic moment is same for which of the following ions?" asked over five ions of five different d counts.
- **Note:** A second route also lands on option 3 and a reviewer may wish to check it: reading $\mathrm{Mn^{2+}}$ as $d^4$, which is $\mathrm{Mn^{3+}}$'s count, makes B and C agree at 4.90 BM. The recorded route is the chromium one because the half-filled exception is the explicit rule the chapter teaches.
<!--/ecat-->

## Q83

Chemistry · inorganic · The D- and F-Block Elements – Practice

The $E^\circ$ value for the $\mathrm{Mn^{3+}/Mn^{2+}}$ couple is more positive than that of $\mathrm{Cr^{3+}/Cr^{2+}}$ or $\mathrm{Fe^{3+}/Fe^{2+}}$ due to change of

- (1) $d^{5}$ to $d^{4}$ configuration
- (2) $d^{5}$ to $d^{2}$ configuration
- **(3)** $d^{4}$ to $d^{5}$ configuration
- (4) $d^{3}$ to $d^{5}$ configuration

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $E^{\circ}_{\mathrm{Mn^{3+}/Mn^{2+}}} > E^{\circ}_{\mathrm{Cr^{3+}/Cr^{2+}}}$ or $E^{\circ}_{\mathrm{Fe^{3+}/Fe^{2+}}}$
2. Electronic configuration of $\mathrm{Mn^{3+}} = [\mathrm{Ar}]3d^{4}$
3. Electronic configuration of $\mathrm{Mn^{2+}} = [\mathrm{Ar}]3d^{5}$
4. Electronic configuration of $\mathrm{Cr^{3+}} = [\mathrm{Ar}]3d^{3}$
5. Electronic configuration of $\mathrm{Cr^{2+}} = [\mathrm{Ar}]3d^{4}$
6. As $\mathrm{Mn^{3+}}$ from $d^{4}$ configuration goes to more stable $d^{5}$ configuration (Half filled), due to more exchange energy in $d^{5}$ configuration.

**Solved independently** (answer withheld)

1. $\mathrm{Mn^{3+}}$ is $[\mathrm{Ar}]\,3d^{4}$ and $\mathrm{Mn^{2+}}$ is $[\mathrm{Ar}]\,3d^{5}$.
2. Reduction $\mathrm{Mn^{3+}} + e^- \rightarrow \mathrm{Mn^{2+}}$ reaches the extra-stable half-filled $d^{5}$ configuration, so $E^\circ$ is highly positive.
3. The change is $d^{4} \rightarrow d^{5}$, which is option $3$.

**Subtopic:** Trends of Electrode Potentials · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q083_555687f9_29102026.png?v=555687f973b3)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q083_41559e34_29102026.png?v=41559e34575b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Reduction of Mn$^{3+}$ gives the half-filled d$^5$ Mn$^{2+}$, and that extra stability is what makes the couple's E$^\circ$ unusually positive
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The half-filled shell is read as the configuration being destroyed rather than the one being formed, so the change is written d$^5$ to d$^4$; reduction of the couple runs the other way, Mn$^{3+}$ (d$^4$) to Mn$^{2+}$ (d$^5$), which is why its potential is the positive one.
- **Why:** This question requires the reason the textbook gives for the unusually positive Mn$^{3+}$/Mn$^{2+}$ potential, demonstrated by the stem closing on 'due to change of' with every option naming a d-configuration change.
<!--/ecat-->

## Q84

Chemistry · physical · Basic Concepts of Chemistry

The highest number of helium atoms is in

- **(1)** $4\,\mathrm{mol}$ of helium
- (2) $4\,\mathrm{u}$ of helium
- (3) $4\,\mathrm{g}$ of helium
- (4) $2.271098\,\mathrm{L}$ of helium at STP

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (1) $4\,\mathrm{mol}$ of $\mathrm{He} = 4\,N_{A}$ $\mathrm{He}$ atoms
2. (2) $4\,\mathrm{u}$ of $\mathrm{He} = \frac{4\,\mathrm{u}}{4\,\mathrm{u}} = 1$ $\mathrm{He}$ atom
3. (3) $4\,\mathrm{g}$ of Helium $= \frac{4\,\mathrm{g}}{4\,\mathrm{g}}$ mole $= 1$ mole $= N_{A}$ $\mathrm{He}$ atom
4. (4) $2.2710982$ of $\mathrm{He}$ at STP $= \frac{2.271}{22.710982}$ mole
5. $= 0.1$ mole
6. $= 0.1\,N_{A}$ $\mathrm{He}$ atom

**Solved independently** (answer withheld)

1. Option 1: $4\,\mathrm{mol}$ He contains $4N_A$ atoms.
2. Option 2: one He atom has mass $4\,\mathrm{u}$, so $4\,\mathrm{u}$ is $1$ atom.
3. Option 3: $n = \frac{4\,\mathrm{g}}{4\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$, i.e. $N_A$ atoms.
4. Option 4: at STP the molar volume is $22.71098\,\mathrm{L\,mol^{-1}}$, so $n = \frac{2.271098}{22.71098} = 0.1\,\mathrm{mol}$, i.e. $0.1N_A$ atoms.
5. $4N_A > N_A > 0.1N_A > 1$, so the highest number is in $4\,\mathrm{mol}$ of helium, option $1$.

**Subtopic:** Mole Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q084_c29192e0_29102026.png?v=c29192e0e435)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q084_6241cd50_29102026.png?v=6241cd50e4fc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A mole is a fixed number of particles, so an amount given in grams, in u, or as a gas volume at STP must each be converted to moles before the particle counts can be compared
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  '4 g of helium is one mole, 6.022$\times$10$^{23}$ atoms' is the worked line of the mole chapter and the option prints that quantity exactly; it answers how much helium makes a mole, while the stem asks which amount holds the most atoms, and 4 mol holds four times as many.
- **Why:** This question requires each printed amount to be converted into a number of atoms before they are compared, demonstrated by the same element being offered in mol, in u, in g and as '2.271098 L of helium at STP'.
- **Note:** asks is calculate rather than compare: the four options are not neighbouring concepts to tell apart but the same substance in four units, and the decision is made by converting each to a particle count.
<!--/ecat-->

## Q85

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** Both $\mathrm{[Co(NH_3)_6]^{3+}}$ and $\mathrm{[CoF_6]^{3-}}$ complexes are octahedral but differ in their magnetic behaviour.
- **(Statement II)** $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic whereas $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{Co^{3+}}$ ion is having $3d^{6}$ configuration.
2. Electronic configuration of $\mathrm{Co^{3+}}$ :

![printed figure: orbital-box diagram: 3d (⇅ ↑ ↑ ↑ ↑), 4s ( ), 4p ( )( )( ) (3d⁶ with one paired and four unpaired electrons; 4s and 4p empty)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q085_sol_1_8d680faa_29102026.png?v=8d680faa7536)

*orbital-box diagram: 3d [⇅ ↑ ↑ ↑ ↑], 4s [ ], 4p [ ][ ][ ] (3d⁶ with one paired and four unpaired electrons; 4s and 4p empty)*

3. In presence of $\mathrm{NH_3}$ ligand, pairing of electrons takes place and it becomes diamagnetic complex ion.
4. In presence of $\mathrm{NH_3}$ ligand :

![printed figure: orbital-box diagram: 3d (⇅ ⇅ ⇅ _ _), 4s ( ), 4p ( )( )( ) (3d⁶ with three paired electrons and two empty 3d orbitals; 4s and 4p empty)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q085_sol_2_71d24d72_29102026.png?v=71d24d72444a)

*orbital-box diagram: 3d [⇅ ⇅ ⇅ _ _], 4s [ ], 4p [ ][ ][ ] (3d⁶ with three paired electrons and two empty 3d orbitals; 4s and 4p empty)*

5. $\therefore$ $\mathrm{[Co(NH_3)_6]^{3+}}$ is octahedral with $d^{2}sp^{3}$ hybridisation and it is diamagnetic in nature.
6. In case of $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co}$ is in $+3$ oxidation state and it is having $3d^{6}$ configuration.
7. In presence of weak field $\mathrm{F^{-}}$ ligand, pairing does not take place.
8. In presence of $\mathrm{F^{-}}$ ligands :

![printed figure: orbital-box diagram: 3d (⇅ ↑ ↑ ↑ ↑), then 4s ( ), 4p ( )( )( ) and the first two 4d orbitals enclosed together in one outer box, remaining 4d ( )( )( ) (3d⁶ with four unpaired electrons; 4s, 4p and two 4d orbitals grouped as empty orbitals for hybridisation)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q085_sol_3_d002b3fd_29102026.png?v=d002b3fdb671)

*orbital-box diagram: 3d [⇅ ↑ ↑ ↑ ↑], then 4s [ ], 4p [ ][ ][ ] and the first two 4d orbitals enclosed together in one outer box, remaining 4d [ ][ ][ ] (3d⁶ with four unpaired electrons; 4s, 4p and two 4d orbitals grouped as empty orbitals for hybridisation)*

9. $\therefore$ In $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co^{3+}}$ is $sp^{3}d^{2}$ hybridised with four unpaired electrons, so it is paramagnetic in nature.

**Solved independently** (answer withheld)

1. In both complexes cobalt is $\mathrm{Co^{3+}}$, configuration $[\mathrm{Ar}]\,3d^6$, with coordination number $6$, so both are octahedral.
2. $\mathrm{NH_3}$ is a strong-field ligand: electrons pair as $t_{2g}^6 e_g^0$ ($d^2sp^3$), $n = 0$, so $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic.
3. $\mathrm{F^-}$ is a weak-field ligand: $t_{2g}^4 e_g^2$ ($sp^3d^2$), $n = 4$, so $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.
4. Statement I (differ in magnetic behaviour) and Statement II are both true, which is option $1$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q085_ffe69f3d_29102026.png?v=ffe69f3dfe94)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q085_71a09ee1_29102026.png?v=71a09ee1ebaa)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Ligand field strength, not the metal, decides spin pairing: NH3 forces d6 Co(III) low-spin and diamagnetic while F- leaves it high-spin and paramagnetic
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Put F- above NH3 in the spectrochemical series and the two labels in Statement II change places: $[CoF_6]^{3-}$ comes out paired and diamagnetic, $[Co(NH_3)_6]^{3+}$ paramagnetic, so Statement II reads false while Statement I's 'they differ' survives untouched. The series runs the other way, with F- near the weak-field end, which is what leaves four unpaired electrons on the fluoro complex.
- **Why:** This question requires applying the spectrochemical series to two octahedral d6 complexes, demonstrated by Statement II's '[Co(NH3)6]3+ is diamagnetic whereas [CoF6]3- is paramagnetic', which follows only once NH3 is placed above F- in field strength. The trap is reversed because the printed assignment is exactly inverted by putting F- above NH3, with no other change to the working.
<!--/ecat-->

## Q86

Chemistry · inorganic · The D- and F-Block Elements – Practice

The pair of lanthanoid ions which are diamagnetic is

- **(1)** $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$
- (2) $\mathrm{Ce^{3+}}$ and $\mathrm{Eu^{2+}}$
- (3) $\mathrm{Gd^{3+}}$ and $\mathrm{Eu^{3+}}$
- (4) $\mathrm{Pm^{3+}}$ and $\mathrm{Sm^{3+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Magnetic moment $\mu = \sqrt{n(n+2)}$
2. $n \rightarrow$ number of unpaired electron
3. $\mathrm{Ce^{4+}} \Rightarrow (\mathrm{Xe})\,4f^{0}$
4. $\mu = 0$ Diamagnetic
5. $\mathrm{Yb^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{14}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, each with a paired electron (↑↓ in all 7 boxes, 14 electrons)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_1_5e85ac48_29102026.png?v=5e85ac48eb6f)

*orbital-box diagram of the f subshell: seven boxes, each with a paired electron (↑↓ in all 7 boxes, 14 electrons)*

6. $\mu = 0$ Diamagnetic
7. $\mathrm{Ce^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{1}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, one unpaired electron in the first box, the other six empty](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_2_538dc93b_29102026.png?v=538dc93b4f0d)

*orbital-box diagram of the f subshell: seven boxes, one unpaired electron in the first box, the other six empty*

8. $\mu = \sqrt{3}$ Paramagnetic
9. $\mathrm{Eu^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, each with one unpaired electron (↑ in all 7 boxes)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_3_35245747_29102026.png?v=352457471d3a)

*orbital-box diagram of the f subshell: seven boxes, each with one unpaired electron (↑ in all 7 boxes)*

10. $\mu = \sqrt{63}$ Paramagnetic
11. $\mathrm{Gd^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, each with one unpaired electron (↑ in all 7 boxes)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_4_f53d297f_29102026.png?v=f53d297f41b3)

*orbital-box diagram of the f subshell: seven boxes, each with one unpaired electron (↑ in all 7 boxes)*

12. $\mu = \sqrt{63}$ Paramagnetic
13. $\mathrm{Eu^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{6}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, six with one unpaired electron each (↑) and the last box empty](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_5_49b76ec3_29102026.png?v=49b76ec3cfaa)

*orbital-box diagram of the f subshell: seven boxes, six with one unpaired electron each (↑) and the last box empty*

14. $\mu = \sqrt{48}$ Paramagnetic
15. $\mathrm{Pm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{4}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, four with one unpaired electron each (↑) and the last three empty](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_6_24417872_29102026.png?v=244178721089)

*orbital-box diagram of the f subshell: seven boxes, four with one unpaired electron each (↑) and the last three empty*

16. $\mu = \sqrt{24}$ Paramagnetic
17. $\mathrm{Sm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{5}$

![printed figure: orbital-box diagram of the f subshell: seven boxes, five with one unpaired electron each (↑) and the last two empty](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q086_sol_7_8a5b193e_29102026.png?v=8a5b193e3d5f)

*orbital-box diagram of the f subshell: seven boxes, five with one unpaired electron each (↑) and the last two empty*

18. $\mu = \sqrt{35}$ Paramagnetic
19. Hence $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ are only diamagnetic.

**Solved independently** (answer withheld)

1. $\mathrm{Ce}$ is $[\mathrm{Xe}]4f^1 5d^1 6s^2$, so $\mathrm{Ce^{4+}}$ is $[\mathrm{Xe}]4f^0$: no unpaired electrons.
2. $\mathrm{Yb}$ is $[\mathrm{Xe}]4f^{14} 6s^2$, so $\mathrm{Yb^{2+}}$ is $[\mathrm{Xe}]4f^{14}$: no unpaired electrons.
3. The other pairs contain $\mathrm{Ce^{3+}}\,(4f^1)$, $\mathrm{Eu^{2+}}\,(4f^7)$, $\mathrm{Gd^{3+}}\,(4f^7)$, $\mathrm{Eu^{3+}}\,(4f^6)$, $\mathrm{Pm^{3+}}\,(4f^4)$ and $\mathrm{Sm^{3+}}\,(4f^5)$, all of which have unpaired electrons and are paramagnetic.
4. So the diamagnetic pair is $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$, which is option $1$.

**Subtopic:** Magnetic Properties, General Characteristics of Lanthanoids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q086_5b3ba9ee_29102026.png?v=5b3ba9ee4b5e)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q086_ab042c4f_29102026.png?v=ab042c4fbc1f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A lanthanoid ion is diamagnetic only when its 4f subshell is empty or completely full, so the f-electron count must be worked out from each ion's oxidation state
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Eu$^{2+}$ is printed alongside Yb$^{2+}$ wherever the chapter lists the lanthanoids holding a +2 state, so picking from that remembered roster instead of counting f electrons lands on Eu$^{2+}$, which is 4f$^7$ with seven unpaired electrons.
- **Why:** This question requires each ion's f-electron count to be derived from its charge and tested against 'no unpaired electrons', demonstrated by 'The pair of lanthanoid ions which are diamagnetic' over options that pair a +4 ion with a +2 ion.
- **Note:** E1 returned plain_mcq, but each option is a pair of ions accepted or rejected whole, so the shape recorded is two_part. On the trap axis the rulebook's swap test was applied: replacing 'Eu' with an unlike name leaves the pull intact, because what carries the student is the +2 lanthanoids being printed together and not any resemblance between the names, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q87

Chemistry · inorganic · Principles Related to Practical Chemistry

Given below are certain cations. Using inorganic qualitative analysis, arrange them in increasing group number from 0 to VI. Choose the correct answer from the options given below.

- **(A)** $\mathrm{Al^{3+}}$
- **(B)** $\mathrm{Cu^{2+}}$
- **(C)** $\mathrm{Ba^{2+}}$
- **(D)** $\mathrm{Co^{2+}}$
- **(E)** $\mathrm{Mg^{2+}}$

- **(1)** B, A, D, C, E
- (2) B, C, A, D, E
- (3) E, C, D, B, A
- (4) E, A, B, C, D

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: table of Group and Cations: Group-II $\ce{Cu^2+}$; Group-III $\ce{Al^3+}$; Group-IV $\ce{Co^2+}$; Group-V $\ce{Ba^2+}$; Group-VI $\ce{Mg^2+}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q087_sol_1_8ca7a0c0_29102026.svg?v=8ca7a0c0ccac)

*table of Group and Cations: Group-II $\ce{Cu^2+}$; Group-III $\ce{Al^3+}$; Group-IV $\ce{Co^2+}$; Group-V $\ce{Ba^2+}$; Group-VI $\ce{Mg^2+}$*

1. The correct order of group number of ions is $\underset{(\mathrm{B})}{\mathrm{Cu^{2+}}} < \underset{(\mathrm{A})}{\mathrm{Al^{3+}}} < \underset{(\mathrm{D})}{\mathrm{Co^{2+}}} < \underset{(\mathrm{C})}{\mathrm{Ba^{2+}}} < \underset{(\mathrm{E})}{\mathrm{Mg^{2+}}}$
2. $\therefore$ The correct order is B, A, D, C, E

**Solved independently** (answer withheld)

1. $\mathrm{Cu^{2+}}$ (B) is precipitated as $\mathrm{CuS}$ by $\mathrm{H_2S}$ in dilute HCl: group II.
2. $\mathrm{Al^{3+}}$ (A) is precipitated as $\mathrm{Al(OH)_3}$ by $\mathrm{NH_4OH}/\mathrm{NH_4Cl}$: group III.
3. $\mathrm{Co^{2+}}$ (D) is precipitated as $\mathrm{CoS}$ by $\mathrm{H_2S}$ in ammoniacal medium: group IV.
4. $\mathrm{Ba^{2+}}$ (C) is precipitated as $\mathrm{BaCO_3}$ by $(\mathrm{NH_4})_2\mathrm{CO_3}$: group V.
5. $\mathrm{Mg^{2+}}$ (E) remains for group VI.
6. Increasing group order: B, A, D, C, E, which is option $1$.

**Subtopic:** Group Analysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 40)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q087_979324d4_29102026.png?v=979324d4a26b)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q087_24fee33b_29102026.png?v=24fee33b8661)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Qualitative analysis files cations by which group reagent precipitates them: $\mathrm{Cu^{2+}}$ in II, $\mathrm{Al^{3+}}$ in III, $\mathrm{Co^{2+}}$ in IV, $\mathrm{Ba^{2+}}$ in V and $\mathrm{Mg^{2+}}$ in VI
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Reading 'increasing group number' off the periodic table instead of off the analysis scheme gives Mg 2, Ba 2, Co 9, Cu 11, Al 13, which sorts to E, C, D, B, A exactly. The stem fixes the scale with 'Using inorganic qualitative analysis' and 'from 0 to VI', so the periodic-table groups are the wrong ruler.
- **Why:** This question requires each cation placed on the qualitative-analysis group scale and then sequenced, demonstrated by 'arrange them in increasing group number from 0 to VI' with four options that are orderings of the five lettered cations.
- **Note:** Option 3 is also close to the exact reverse of the key (which would be E, C, D, A, B) and could be read as a decreasing-order slip, but it differs in the last two places. The periodic-table group route accounts for all five positions exactly, including that difference, so it is the route recorded.
<!--/ecat-->

## Q88

Chemistry · organic · Haloalkanes and Haloarenes

Major products A and B formed in the following reaction sequence, are

![printed figure: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q088_b6aeb829_29102026.png?v=b6aeb829127e)

*2-methylcyclohexan-1-ol →[$\ce{PBr3}$] A (major) →[alc. KOH, Δ] B (major)*

![drawn: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_question_2d0aeb6c_30102026.svg?v=2d0aeb6c9715)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

Structures: 2-methylcyclohexan-1-ol `CC1CCCCC1O` ![2-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_question_s1_d1520427_30102026.svg?v=d1520427ffb6)

- **(1)** 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_1_s1_a2e0c472_30102026.svg?v=a2e0c472fe36); 1-methylcyclohexene `CC1=CCCCC1` ![1-methylcyclohexene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_1_s2_daf611a5_30102026.svg?v=daf611a53ea1) — A =, B =
- (2) 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_2_s1_a2e0c472_30102026.svg?v=a2e0c472fe36); 4-methylcyclohexene `CC1CC=CCC1` ![4-methylcyclohexene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_2_s2_389bd25f_30102026.svg?v=389bd25f3ebf) — A =, B =
- (3) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_3_s1_948eb8c3_30102026.svg?v=948eb8c30e51); 6-methylcyclohex-2-en-1-ol `CC1CCC=CC1O` ![6-methylcyclohex-2-en-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_3_s2_84119fb9_30102026.svg?v=84119fb9e0a2) — A =, B =
- (4) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_4_s1_948eb8c3_30102026.svg?v=948eb8c30e51); 2-methylcyclohexan-1-one `CC1CCCCC1=O` ![2-methylcyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_4_s2_957f65c8_30102026.svg?v=957f65c86888) — A =, B =

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) 1-bromo-2-methylcyclohexane (A) major (curved arrows: Base takes the H on the methyl-bearing carbon, Br leaves); (A) → 1-methylcyclohexene (B) major](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q088_sol_1_0e80a862_29102026.png?v=0e80a862c071)

*2-methylcyclohexan-1-ol →[$\ce{PBr3}$] 1-bromo-2-methylcyclohexane (A) major (curved arrows: Base takes the H on the methyl-bearing carbon, Br leaves); (A) → 1-methylcyclohexene (B) major*

![drawn: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) 1-bromo-2-methylcyclohexane (A) major (curved arrows: Base takes the H on the methyl-bearing carbon, Br leaves); (A) → 1-methylcyclohexene (B) major](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q088_solution_1_d200f5fa_30102026.svg?v=d200f5fa534a)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*


**Solved independently** (answer withheld)

1. $\mathrm{PBr_3}$ converts an alcohol to an alkyl bromide: $3\,\mathrm{R{-}OH} + \mathrm{PBr_3} \rightarrow 3\,\mathrm{R{-}Br} + \mathrm{H_3PO_3}$, so the ring $-\mathrm{OH}$ is replaced by $-\mathrm{Br}$ at the same carbon.
2. Hence $A$ = 1-bromo-2-methylcyclohexane (no new Br on another carbon, OH not retained), which rules out options $3$ and $4$.
3. Alcoholic $\mathrm{KOH}$ with heat causes $\beta$-elimination of $\mathrm{HBr}$ from $A$.
4. Two $\beta$-carbons are available; by Saytzeff's rule the H is lost from the more substituted $\beta$-carbon (the one carrying $\mathrm{CH_3}$), giving the more substituted (trisubstituted) alkene.
5. So $B$ = 1-methylcyclohexene, with the double bond at the methyl-bearing carbon, which is option $1$.

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions, Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q088_592ee5c1_29102026.png?v=592ee5c10da7)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q088_4d4e315f_29102026.png?v=4d4e315fd450)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** PBr$_3$ replaces an alcohol's OH by Br without rearrangement, and alcoholic KOH with heat then eliminates HBr to give the more substituted alkene
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each option is printed as two drawn structures and the packet carries only the text 'A =, B =', so the structures that decide between the options were not supplied to this step.
- **Why:** This question requires the product of PBr$_3$ on a secondary alcohol followed by elimination with alcoholic KOH, demonstrated by the printed scheme '2-methylcyclohexan-1-ol, PBr$_3$, A (major), alc. KOH and heat, B (major)'.
- **Note:** The stem scheme came through in full but the four option structures did not, every option reading only 'A =, B ='. Rulebook section 5.0, third case: the printed paper is intact and the images were simply not supplied to this step, so this is a reach limit and not source_damage_artifact, and no trap is tagged. A reviewer holding the printed options should check two things: whether B is offered as the Hofmann alkene 3-methylcyclohexene instead of the Saytzeff product 1-methylcyclohexene, and whether A is offered as a ring-rearranged or 2-substituted bromide, since PBr$_3$ substitutes without rearrangement.
<!--/ecat-->

## Q89

Chemistry · physical · Thermodynamics

The work done during reversible isothermal expansion of one mole of hydrogen gas at $25^{\circ}\mathrm{C}$ from pressure of $20$ atmosphere to $10$ atmosphere is (Given $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$)

- (1) $0$ calorie
- **(2)** $-413.14$ calories
- (3) $413.14$ calories
- (4) $100$ calories

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $W_{\mathrm{rev},\ \mathrm{iso}} = -2.303\,nRT\log\frac{P_i}{P_f}$
2. $= -2.303 \times 1 \times 2 \times 298 \times \log 2$
3. $= -2.303 \times 1 \times 2 \times 298 \times 0.3$
4. $= -413.14$ calories

**Solved independently** (answer withheld)

1. For reversible isothermal expansion of an ideal gas, $w = -2.303\,nRT\log\frac{p_1}{p_2}$.
2. $T = 25 + 273 = 298\,\mathrm{K}$, $n = 1$, $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$, $\frac{p_1}{p_2} = \frac{20}{10} = 2$.
3. $w = -2.303 \times 1 \times 2.0 \times 298 \times \log 2 = -2.303 \times 596 \times 0.3010$.
4. $w \approx -413.14\,\mathrm{cal}$, which is option $2$.

**Subtopic:** Pressure–Volume Work for Isothermal Reversible Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q089_1a35b918_29102026.png?v=1a35b918682c)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q089_e5fec772_29102026.png?v=e5fec772fa10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Reversible isothermal work is $w = -2.303\,nRT\log(p_1/p_2)$, and with work measured on the system an expansion comes out negative
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Working $2.303\,nRT\log(p_1/p_2) = 2.303 \times 1 \times 2.0 \times 298 \times \log 2$ gives 413.14 and the option prints it unsigned; that figure is the work done by the gas, and in the convention the chapter uses an expansion must carry a minus sign.
- **Why:** This question requires the reversible isothermal work expression evaluated on the printed data, demonstrated by 'from pressure of 20 atmosphere to 10 atmosphere' with 'Given R = 2.0 cal K$^{-1}$ mol$^{-1}$'.
<!--/ecat-->

## Q90

Chemistry · organic · Amines

Identify the major product C formed in the following reaction sequence: $\mathrm{CH_3-CH_2-CH_2-I}\xrightarrow{\mathrm{NaCN}}\mathrm{A}\xrightarrow[\text{Partial hydrolysis}]{\mathrm{OH^-}}\mathrm{B}\xrightarrow[\mathrm{Br_2}]{\mathrm{NaOH}}\underset{\text{(major)}}{\mathrm{C}}$

- **(1)** propylamine
- (2) butylamine
- (3) butanamide
- (4) $\alpha$–bromobutanoic acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: 1-iodopropane →(NaCN) butanenitrile (A) →(Partial hydrolysis) butanamide (B); (B) →(NaOH/Br₂) propan-1-amine (C) (Propyl amine)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q090_sol_1_44202c31_29102026.png?v=44202c3160b5)

*1-iodopropane →[NaCN] butanenitrile (A) →[Partial hydrolysis] butanamide (B); (B) →[NaOH/Br₂] propan-1-amine (C) (Propyl amine)*

![drawn: 1-iodopropane →(NaCN) butanenitrile (A) →(Partial hydrolysis) butanamide (B); (B) →(NaOH/Br₂) propan-1-amine (C) (Propyl amine)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q090_solution_1_1b241360_30102026.svg?v=1b2413602a0e)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

1. Step-I is $\mathrm{S_N}$ reaction with $\overset{\ominus}{\mathrm{C}}\mathrm{N}$ nucleophile.
2. Step-II will give amide.
3. Step-III is Hoffmann bromamide degradation reaction.

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2I + NaCN \rightarrow CH_3CH_2CH_2CN}$ (A, butanenitrile), by $S_N2$ substitution.
2. Partial hydrolysis with $\mathrm{OH^-}$: $\mathrm{CH_3CH_2CH_2CN \rightarrow CH_3CH_2CH_2CONH_2}$ (B, butanamide).
3. Hoffmann bromamide degradation with $\mathrm{Br_2/NaOH}$: $\mathrm{RCONH_2 \rightarrow RNH_2}$ with one carbon fewer.
4. $\mathrm{CH_3CH_2CH_2CONH_2 \rightarrow CH_3CH_2CH_2NH_2}$ (C, propylamine), which is option $1$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q090_177094f5_29102026.png?v=177094f59bf9)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q090_2bdc80c6_29102026.png?v=2bdc80c6c48d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hofmann bromamide degradation: $\mathrm{Br_2/NaOH}$ turns a primary amide into a primary amine with one carbon fewer
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The amide-to-amine step is held without its defining feature, that the carbonyl carbon leaves, so the four-carbon amide is written out as the four-carbon butylamine instead of the three-carbon propylamine.
- **Why:** This question requires the product of the Hofmann bromamide degradation, demonstrated by the last arrow reading $\mathrm{NaOH}$ over $\mathrm{Br_2}$ on the amide that the arrow marked "Partial hydrolysis" has just produced.
- **Note:** E1 returned arrange_in_order, which the pattern took from the words "reaction sequence"; the printed shape is a single scheme with four named compounds as options and one product asked for, so the shape recorded here is mcq.
<!--/ecat-->

## Q91

Chemistry · organic · Haloalkanes and Haloarenes

The products A and B obtained in the following reactions, respectively, are
$\mathrm{3ROH + PCl_3 \rightarrow 3RCl + A}$
$\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + B}$

- (1) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_3}$
- (2) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_4}$
- (3) $\mathrm{H_3PO_4}$ and $\mathrm{POCl_3}$
- **(4)** $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. These reactions are preparation of haloalkanes from alcohols.
2. $\mathrm{3ROH + PCl_3 \longrightarrow 3RCl + \underset{(A)}{H_3PO_3}}$
3. $\mathrm{ROH + PCl_5 \longrightarrow RCl + HCl + \underset{(B)}{POCl_3}}$
4. A and B are $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$ respectively.

**Solved independently** (answer withheld)

1. With $\mathrm{PCl_3}$, the three $\mathrm{-OH}$ groups' H and O go to P: $\mathrm{3ROH + PCl_3 \rightarrow 3RCl + H_3PO_3}$, so $A = \mathrm{H_3PO_3}$.
2. With $\mathrm{PCl_5}$: $\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + POCl_3}$, so $B = \mathrm{POCl_3}$.
3. $A = \mathrm{H_3PO_3}$ and $B = \mathrm{POCl_3}$, which is option $4$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q091_fde42249_29102026.png?v=fde422495d37)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q091_8c24653e_29102026.png?v=8c24653e85c7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** $\mathrm{PCl_3}$ gives up all three chlorines to the alcohol and leaves phosphorous acid $\mathrm{H_3PO_3}$, while $\mathrm{PCl_5}$ gives up one and leaves phosphoryl chloride $\mathrm{POCl_3}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Both by-products are known and the only live decision is which reagent leaves which; handing $\mathrm{POCl_3}$ to the $\mathrm{PCl_3}$ line and $\mathrm{H_3PO_3}$ to the $\mathrm{PCl_5}$ line gives option 1, the key with its two halves exchanged.
- **Why:** This question requires the phosphorus by-product each chlorinating agent leaves behind, demonstrated by the two printed equations "$\mathrm{3ROH + PCl_3 \rightarrow 3RCl + A}$" and "$\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + B}$", whose stoichiometry fixes which species is which.
<!--/ecat-->

## Q92

Chemistry · physical · Electrochemistry

Mass in grams of copper deposited by passing $9.6487\,\mathrm{A}$ current through a voltmeter containing copper sulphate solution for $100$ seconds is (Given : Molar mass of $\mathrm{Cu}$ : $63\,\mathrm{g\,mol^{-1}}$, $1\,\mathrm{F} = 96487\,\mathrm{C}$)

- (1) $3.15\,\mathrm{g}$
- **(2)** $0.315\,\mathrm{g}$
- (3) $31.5\,\mathrm{g}$
- (4) $0.0315\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Cu^{2+}(aq) + 2e^{-} \rightarrow Cu(s)}$
2. Mass of $\mathrm{Cu}$ deposited $(w) = \frac{M \times i \times t}{nF}$
3. $= \frac{63 \times 9.6487 \times 100}{2 \times 96487}$
4. $= 0.315\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $Q = It = 9.6487\,\mathrm{A} \times 100\,\mathrm{s} = 964.87\,\mathrm{C}$.
2. $Q = \frac{964.87}{96487}\,\mathrm{F} = 0.01\,\mathrm{F}$.
3. $\mathrm{Cu^{2+}} + 2e^- \rightarrow \mathrm{Cu}$, so $2\,\mathrm{F}$ deposit $1\,\mathrm{mol}$ Cu.
4. $n_{\mathrm{Cu}} = \frac{0.01}{2} = 0.005\,\mathrm{mol}$.
5. $m = 0.005 \times 63 = 0.315\,\mathrm{g}$, which is option $2$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q092_17cc2705_29102026.png?v=17cc2705fc6d)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q092_7db5bbca_29102026.png?v=7db5bbca093b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Faraday's first law: mass deposited equals the equivalent mass times the number of faradays passed, and $\mathrm{Cu^{2+}}$ takes two faradays per mole
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $31.5$ is $63/2$, the equivalent mass of copper and so the mass one faraday deposits, but the charge actually passed is $9.6487\times100 = 964.87\,\mathrm{C}$, which is one hundredth of a faraday.
- **Why:** This question requires Faraday's first law carried through to a number, demonstrated by the stem supplying "$9.6487\,\mathrm{A}$", "$100$ seconds", "$63\,\mathrm{g\,mol^{-1}}$" and "$1\,\mathrm{F} = 96487\,\mathrm{C}$" and asking for a mass in grams.
<!--/ecat-->

## Q93

Chemistry · physical · Basic Concepts of Chemistry

A compound X contains $32\%$ of A, $20\%$ of B and remaining percentage of C. Then, the empirical formula of X is :
(Given atomic masses of $\mathrm{A} = 64$; $\mathrm{B} = 40$; $\mathrm{C} = 32\,\mathrm{u}$)

- (1) $\mathrm{A_2BC_2}$
- **(2)** $\mathrm{ABC_3}$
- (3) $\mathrm{AB_2C_2}$
- (4) $\mathrm{ABC_4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Element | Mass percentage $\%$ | No. of moles | No. of moles/Smallest number | Simplest whole number
2. A | $32\%$ | $\frac{32}{64} = \frac{1}{2}$ | $\frac{1}{2} \times 2$ | $= 1$
3. B | $20\%$ | $\frac{20}{40} = \frac{1}{2}$ | $\frac{1}{2} \times 2$ | $= 1$
4. C | $48\%$ | $\frac{48}{32} = \frac{3}{2}$ | $\frac{3}{2} \times 2$ | $= 3$
5. So, empirical formula of $X = \begin{matrix} \mathrm{A} & : & \mathrm{B} & : & \mathrm{C} \\ 1 & : & 1 & : & 3 \end{matrix}$
6. $\therefore$ The correct empirical formula of compound X is $\mathrm{ABC_3}$

**Solved independently** (answer withheld)

1. Percentage of C: $100 - 32 - 20 = 48\%$.
2. Moles of A in 100 g: $n_A = \frac{32}{64} = 0.5$.
3. Moles of B: $n_B = \frac{20}{40} = 0.5$.
4. Moles of C: $n_C = \frac{48}{32} = 1.5$.
5. Divide by the smallest, $0.5$: $A : B : C = 1 : 1 : 3$.
6. Empirical formula is $\mathrm{ABC_3}$, which is option $2$.

**Subtopic:** Empirical and Molecular Formula · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q093_dd72db6b_29102026.png?v=dd72db6bdefc)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q093_1b46afc0_29102026.png?v=1b46afc0408f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Empirical formula: divide each element's mass percentage by its atomic mass, then scale the whole set of mole ratios up to the smallest whole numbers
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The mole numbers come out $0.5 : 0.5 : 1.5$, and rounding the odd $1.5$ up to $2$ before dividing through by $0.5$ turns the ratio $1:1:3$ into $1:1:4$.
- **Why:** This question requires mass percentages converted into a whole-number mole ratio, demonstrated by "remaining percentage of C" and the given atomic masses "$\mathrm{A} = 64$; $\mathrm{B} = 40$; $\mathrm{C} = 32\,\mathrm{u}$".
<!--/ecat-->

## Q94

Chemistry · inorganic · Principles Related to Practical Chemistry

During the preparation of Mohr’s salt solution (Ferrous ammonium sulphate), which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion?

- (1) dilute hydrochloric acid
- (2) concentrated sulphuric acid
- (3) dilute nitric acid
- **(4)** dilute sulphuric acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During the preparation of Mohr’s salt, dilute sulphuric acid is added to prevent the hydrolysis of $\mathrm{Fe^{2+}}$ ion.

**Solved independently** (answer withheld)

1. Mohr's salt is $\mathrm{FeSO_4\cdot(NH_4)_2SO_4\cdot 6H_2O}$, and $\mathrm{Fe^{2+}}$ hydrolyses: $\mathrm{Fe^{2+} + 2H_2O \rightleftharpoons Fe(OH)_2 + 2H^+}$.
2. Adding $\mathrm{H^+}$ shifts this equilibrium left, so an acid is needed; dilute $\mathrm{HNO_3}$ and concentrated $\mathrm{H_2SO_4}$ are oxidising and would convert $\mathrm{Fe^{2+}}$ to $\mathrm{Fe^{3+}}$, and $\mathrm{HCl}$ adds foreign $\mathrm{Cl^-}$ ions.
3. Dilute $\mathrm{H_2SO_4}$ supplies $\mathrm{H^+}$ with the common $\mathrm{SO_4^{2-}}$ ion and does not oxidise $\mathrm{Fe^{2+}}$, which is option $4$.

**Subtopic:** Titration · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q094_efb1cb05_29102026.png?v=efb1cb0598dd)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q094_1984f2c4_29102026.png?v=1984f2c4a9d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Mohr's salt is acidified with dilute sulphuric acid: it suppresses hydrolysis of $\mathrm{Fe^{2+}}$ without bringing in a foreign anion or oxidising the iron
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Dilute HCl is the acid the bench work adds to stop hydrolysis in the cases printed alongside this one, $\mathrm{SnCl_2}$, $\mathrm{BiCl_3}$ and $\mathrm{SbCl_3}$, so the rule "add a little dilute acid to suppress hydrolysis" arrives carrying the acid it is usually printed with.
- **Why:** This question requires the reagent a named bench preparation specifies, demonstrated by "During the preparation of Mohr's salt solution (Ferrous ammonium sulphate), which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion?".
<!--/ecat-->

## Q95

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the **correct** answer.

- (1) Three resonance structures can be drawn for ozone
- (2) $\mathrm{BF_3}$ has non-zero dipole moment
- (3) Dipole moment of $\mathrm{NF_3}$ is greater than that of $\mathrm{NH_3}$
- **(4)** Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (1) In ozone; there are two resonating structures.
2. (2) $\mathrm{BF_3}$ i.e., ; Dipole moment $= 0$

![printed figure: boron trifluoride ($\ce{BF3}$, trigonal planar) with partial charges δ⁺ on B and δ⁻ on each F, and B–F bond dipole arrows that cancel](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q095_sol_1_b3c5aa2e_29102026.png?v=b3c5aa2e9562)

*boron trifluoride ($\ce{BF3}$, trigonal planar) with partial charges δ⁺ on B and δ⁻ on each F, and B–F bond dipole arrows that cancel*

![drawn: boron trifluoride ($\ce{BF3}$, trigonal planar) with partial charges δ⁺ on B and δ⁻ on each F, and B–F bond dipole arrows that cancel](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q095_solution_1_945bc48b_30102026.svg?v=945bc48b69ec)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

3. (3) $(0.80 \times 10^{-30}\ \mathrm{Cm}) < (4.90 \times 10^{-30}\ \mathrm{Cm})$

![printed figure: nitrogen trifluoride ($\ce{NF3}$, lone pair on N, bond dipoles pointing to F) < ammonia ($\ce{NH3}$, lone pair on N, bond dipoles pointing to N)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q095_sol_2_c8cf5d97_29102026.png?v=c8cf5d97af1f)

*nitrogen trifluoride ($\ce{NF3}$, lone pair on N, bond dipoles pointing to F) < ammonia ($\ce{NH3}$, lone pair on N, bond dipoles pointing to N)*

![drawn: nitrogen trifluoride ($\ce{NF3}$, lone pair on N, bond dipoles pointing to F) < ammonia ($\ce{NH3}$, lone pair on N, bond dipoles pointing to N)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q095_solution_2_cf1447ee_30102026.svg?v=cf1447ee087f)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

4. (4) (3 canonical forms)

![printed figure: three resonance (canonical) structures of carbonate ion ($\ce{CO3^2-}$): carbonate (C=O up) ↔ carbonate (C=O lower left) ↔ carbonate (C=O lower right)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q095_sol_3_210241a9_29102026.png?v=210241a9d960)

*three resonance (canonical) structures of carbonate ion ($\ce{CO3^2-}$): carbonate (C=O up) ↔ carbonate (C=O lower left) ↔ carbonate (C=O lower right)*

![drawn: three resonance (canonical) structures of carbonate ion ($\ce{CO3^2-}$): carbonate (C=O up) ↔ carbonate (C=O lower left) ↔ carbonate (C=O lower right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q095_solution_3_d8a2a791_30102026.svg?v=d8a2a791f614)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*


**Solved independently** (answer withheld)

1. Ozone $\mathrm{O_3}$ has only two resonance structures, so option $1$ is incorrect.
2. $\mathrm{BF_3}$ is trigonal planar and its bond dipoles cancel, so $\mu = 0$; option $2$ is incorrect.
3. In $\mathrm{NH_3}$ the lone-pair moment adds to the N–H bond moments, while in $\mathrm{NF_3}$ it opposes the N–F bond moments, so $\mu(\mathrm{NH_3}) = 1.47\,\mathrm{D} > \mu(\mathrm{NF_3}) = 0.23\,\mathrm{D}$; option $3$ is incorrect.
4. $\mathrm{CO_3^{2-}}$ has three equivalent canonical forms (the C=O double bond on each of the three O atoms), so option $4$ is correct.

**Subtopic:** Bond Parameters · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q095_69427e7b_29102026.png?v=69427e7b8b38)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q095_f25e1023_29102026.png?v=f25e102335b8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A molecular dipole moment is the vector sum of the bond moments and the lone-pair moment, and the number of canonical forms equals the number of equivalent positions the multiple bond can take
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Fluorine is far more electronegative than hydrogen, so the N-F bond moment is the larger, and carrying that trend straight to the molecule ignores that the lone pair's moment adds to the bond moments in $\mathrm{NH_3}$ and opposes them in $\mathrm{NF_3}$.
- **Why:** This question requires four printed claims about bonding graded one by one against what the book states, demonstrated by option 4's "Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion" standing while option 1 makes the same count for ozone.
- **Note:** E1 returned statement_options, which matches the printed shape: no lettered block is given, the stem is the bare instruction "Identify the correct answer", and each option is a full claim judged on its own truth. Mapped to qtype statements on that basis rather than to mcq.
<!--/ecat-->

## Q96

Chemistry · physical · Chemical Kinetics

The rate of a reaction quadruples when temperature changes from $27^\circ\mathrm{C}$ to $57^\circ\mathrm{C}$. Calculate the energy of activation.
Given $R = 8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$, $\log 4 = 0.6021$

- **(1)** $38.04\,\mathrm{kJ/mol}$
- (2) $380.4\,\mathrm{kJ/mol}$
- (3) $3.80\,\mathrm{kJ/mol}$
- (4) $3804\,\mathrm{kJ/mol}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$
2. $\log\left(\frac{4}{1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{300} - \frac{1}{330}\right)$
3. $E_a = \frac{(\log(4)) \times 2.303 \times 8.314 \times 300 \times 330}{30}$
4. $= 3.804 \times 10^{4}\,\mathrm{J/mol}$
5. $= 38.04\,\mathrm{kJ/mol}$

**Solved independently** (answer withheld)

1. Convert temperatures: $T_1 = 27 + 273 = 300\,\mathrm{K}$, $T_2 = 57 + 273 = 330\,\mathrm{K}$.
2. Arrhenius equation: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. $\frac{T_2 - T_1}{T_1 T_2} = \frac{30}{300 \times 330} = \frac{1}{3300}\,\mathrm{K^{-1}}$.
4. $\log 4 = 0.6021 = \frac{E_a}{2.303 \times 8.314 \times 3300}$.
5. $E_a = 0.6021 \times 2.303 \times 8.314 \times 3300 \approx 38044\,\mathrm{J\,mol^{-1}} = 38.04\,\mathrm{kJ\,mol^{-1}}$, which is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q096_2bd1e61e_29102026.png?v=2bd1e61e5957)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q096_92b0c0b0_29102026.png?v=92b0c0b0e78c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Activation energy from a rate ratio at two temperatures, using the two-point Arrhenius equation with both temperatures in kelvin.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Writing $300 \times 330 = 9900$ instead of $99000$ turns the temperature factor into $330$ in place of $3300$, and $11.53 \times 330 = 3804$ J mol$^{-1}$, which is the printed $3.80$ kJ/mol.
- **Why:** This question requires the two-temperature Arrhenius equation worked on the stem's own numbers, demonstrated by 'Calculate the energy of activation' with $R$ and $\log 4 = 0.6021$ handed over in the stem.
- **Note:** All three distractors are the key times a power of ten, so the paper tests the arithmetic rather than the setup: the setup errors give unprinted values - Celsius temperatures give $0.59$ kJ/mol and dropping the $2.303$ gives $16.5$ kJ/mol. Option 3 carries the primary trap because the slip that reaches it happens inside the stem's own multiplication.
<!--/ecat-->

## Q97

Chemistry · organic · Hydrocarbons

For the given reaction:

'P' is

![printed figure: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q097_d213c314_29102026.png?v=d213c314af50)

*1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 'P' (major product)*

![drawn: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_question_eac6cb7e_30102026.svg?v=eac6cb7e6891)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*

Structures: 1,2-dicyclohexylethene `C(=CC1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_question_s1_a6764621_30102026.svg?v=a6764621264a)

- (1) cyclohexanecarbaldehyde `O=CC1CCCCC1` ![cyclohexanecarbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_1_s1_6c5034d9_30102026.svg?v=6c5034d97ec0)
- **(2)** cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_2_s1_de3f7ae0_30102026.svg?v=de3f7ae04444)
- (3) 1,2-dicyclohexylethane-1,2-diol `OC(C1CCCCC1)C(O)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_3_s1_832d6d32_30102026.svg?v=832d6d32fdb7)
- (4) 1,2-dicyclohexylethane-1,2-dione `O=C(C(=O)C1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-dione](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_4_s1_66d17a93_30102026.svg?v=66d17a937658)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. (E)-1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 2 cyclohexanecarboxylic acid (Major product)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q097_sol_1_19b538fd_29102026.png?v=19b538fd31e2)

*I. (E)-1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 2 cyclohexanecarboxylic acid (Major product)*

![drawn: I. (E)-1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 2 cyclohexanecarboxylic acid (Major product)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2024/2024_Q4/figures_drawn/q097_solution_1_9582f2ea_30102026.svg?v=9582f2ea761a)  
*drawn from its SMILES, turned to match the printed picture, checked against its SMILES*


**Solved independently** (answer withheld)

1. The substrate is $\mathrm{C_6H_{11}{-}CH{=}CH{-}C_6H_{11}}$, a symmetrical 1,2-disubstituted alkene.
2. Hot acidic $\mathrm{KMnO_4}$ cleaves the $\mathrm{C{=}C}$ bond oxidatively.
3. Each $\mathrm{{=}CH{-}R}$ fragment becomes $\mathrm{R{-}COOH}$ (the aldehyde does not survive acidic permanganate).
4. So $\mathrm{C_6H_{11}{-}CH{=}CH{-}C_6H_{11}} \xrightarrow{\mathrm{KMnO_4/H^+}} 2\,\mathrm{C_6H_{11}{-}COOH}$, cyclohexanecarboxylic acid, which is option $2$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q097_f8b86994_29102026.png?v=f8b8699484b2)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q097_67c3c703_29102026.png?v=67c3c7035d49)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hot acidic KMnO4 cleaves the C=C of an alkene, and a doubly bonded carbon carrying one hydrogen ends up as a carboxylic acid group.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options_en arrived as empty strings, so the structures the options print were not supplied to this step and no option can be named or a route to it traced; the stem scheme was supplied and was read.
- **Why:** This question requires knowing what a named oxidant does to a disubstituted alkene, demonstrated by 'KMnO4/H+' written over the arrow and the stem asking what 'P' is.
- **Note:** The packet carries the stem scheme in full (1,2-dicyclohexylethene, KMnO4/H+ over the arrow, 'P' as the major product) but every option is an empty string, so the option structures were not carried into this step. Nothing shows the paper itself to be damaged, so per the rulebook's third case this is not source_damage_artifact. A reviewer holding the printed options should check for condition_missed: the hot acidic permanganate condition pushes the cleavage all the way to two molecules of cyclohexanecarboxylic acid, and an option stopping at the 1,2-diol (cold dilute alkaline KMnO4) or at cyclohexanecarbaldehyde (reductive ozonolysis) would be the route to confirm. The key is tagged as printed, Answer (2).
<!--/ecat-->

## Q98

Chemistry · physical · Solutions

The plot of osmotic pressure $(\Pi)$ vs concentration $(\mathrm{mol\,L^{-1}})$ for a solution gives a straight line with slope $25.73\,\mathrm{L\,bar\,mol^{-1}}$. The temperature at which the osmotic pressure measurement is done is (Use $R = 0.083\,\mathrm{L\,bar\,mol^{-1}\,K^{-1}}$)

- **(1)** $37\,^{\circ}\mathrm{C}$
- (2) $310\,^{\circ}\mathrm{C}$
- (3) $25.73\,^{\circ}\mathrm{C}$
- (4) $12.05\,^{\circ}\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\Pi = CRT$
2. $\text{Slope} = RT$
3. $25.73 = 0.083 \times T$
4. $T = \frac{25.73}{0.083} = 309.47 \approx 310\,\mathrm{K}$
5. $\therefore$ Temperature in $^{\circ}\mathrm{C} = 310 - 273$
6. $= 37\,^{\circ}\mathrm{C}$

**Solved independently** (answer withheld)

1. Van 't Hoff equation: $\Pi = CRT$, so a plot of $\Pi$ vs $C$ is a straight line with slope $RT$.
2. $RT = 25.73\,\mathrm{L\,bar\,mol^{-1}}$, so $T = \frac{25.73}{0.083} = 310\,\mathrm{K}$.
3. $T = 310 - 273 = 37\,^{\circ}\mathrm{C}$, which is option $1$.

**Subtopic:** Osmosis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q098_201edaaf_29102026.png?v=201edaafe896)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q098_20879416_29102026.png?v=2087941645ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** van 't Hoff relation $\Pi = cRT$: the slope of osmotic pressure against concentration is $RT$, so the slope divided by $R$ is the absolute temperature.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Dividing $25.73$ by $0.083$ gives $310$, and $310$ is sitting in the options - but with $^{\circ}$C printed after it, so stopping at the kelvin value hands in a temperature $273$ degrees too high.
- **Why:** This question requires a temperature computed from $\Pi = cRT$, demonstrated by 'a straight line with slope $25.73$ L bar mol$^{-1}$' and four options that are temperatures in $^{\circ}$C.
<!--/ecat-->

## Q99

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below.

- **(Statement I)** $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex whereas $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex.
- **(Statement II)** Complex $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligands but $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has more than one kind of ligands.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex as only one type of ligands ($\mathrm{NH_3}$) is coordinated with $\mathrm{Co^{3+}}$ ion.
2. While $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex in which $\mathrm{Co^{3+}}$ ion is ligated with more than one type of ligands, *i.e.*, $\mathrm{NH_3}$ and $\mathrm{Cl^{-}}$.

**Solved independently** (answer withheld)

1. A homoleptic complex has the metal bound to only one kind of ligand; a heteroleptic complex has more than one kind.
2. $\mathrm{[Co(NH_3)_6]^{3+}}$ has only $\mathrm{NH_3}$ ligands, so it is homoleptic.
3. $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has both $\mathrm{NH_3}$ and $\mathrm{Cl^-}$ ligands, so it is heteroleptic.
4. Statement I and Statement II are both true, which is option $1$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q099_44f4e1d2_29102026.png?v=44f4e1d27a88)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q099_b026728e_29102026.png?v=b026728ea870)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Homoleptic means one kind of ligand throughout; heteroleptic means more than one kind in the same coordination sphere
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Homoleptic and heteroleptic differ only by their prefix, and holding the pair crossed puts the labels in Statement I on the wrong complexes, so Statement I reads false. Statement II carries no jargon at all, only one kind of ligand against more than one, so it still reads true and the two verdicts land on option 4.
- **Why:** This question requires applying the homoleptic and heteroleptic criterion to two printed formulas, demonstrated by Statement II's 'has only one kind of ligands but [Co(NH3)4Cl2]+ has more than one kind of ligands', which is the criterion Statement I's labels have to match. The swap test puts the trap at look_alike_term: replace the two names with unlike words and there is nothing left to cross, so the resemblance of the prefixes is what carries the pull.
<!--/ecat-->

## Q100

Chemistry · physical · Chemical Equilibrium

Consider the following reaction in a sealed vessel at equilibrium with concentrations of $\mathrm{N_2} = 3.0 \times 10^{-3}\,\mathrm{M}$, $\mathrm{O_2} = 4.2 \times 10^{-3}\,\mathrm{M}$ and $\mathrm{NO} = 2.8 \times 10^{-3}\,\mathrm{M}$.
$\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
If $0.1\,\mathrm{mol\,L^{-1}}$ of $\mathrm{NO_{(g)}}$ is taken in a closed vessel, what will be degree of dissociation $(\alpha)$ of $\mathrm{NO_{(g)}}$ at equilibrium?

- (1) $0.00889$
- (2) $0.0889$
- (3) $0.8889$
- **(4)** $0.717$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
2. $K_c = \frac{[\mathrm{N_2}][\mathrm{O_2}]}{[\mathrm{NO}]^2}$
3. $= \frac{3 \times 10^{-3} \times 4.2 \times 10^{-3}}{2.8 \times 10^{-3} \times 2.8 \times 10^{-3}}$
4. $= 1.607$
5. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
6. $t = 0$: $0.1$, $0$, $0$
7. $0.1 - 0.1\alpha$, $0.05\alpha$, $0.05\alpha$
8. $K_c = \frac{0.05\alpha \times 0.05\alpha}{(0.1 - 0.1\alpha)^2}$
9. $K_c = \frac{0.05\alpha \times 0.05\alpha}{0.01(1 - \alpha)^2}$
10. $1.607 = \frac{(0.05)^2 \alpha^2}{0.01(1 - \alpha)^2}$
11. $\frac{\alpha^2}{(1 - \alpha)^2} = \frac{1.607 \times (0.1)^2}{(0.05)^2}$
12. $\frac{\alpha}{1 - \alpha} = \frac{1.27 \times 0.1}{0.05}$
13. $\frac{\alpha}{1 - \alpha} = 2.54$
14. $\alpha = 2.54 - 2.54\alpha$
15. $3.54\alpha = 2.54$
16. $\alpha = \frac{2.54}{3.54} = 0.717$

**Solved independently** (answer withheld)

1. $K_c = \frac{[\mathrm{N_2}][\mathrm{O_2}]}{[\mathrm{NO}]^2} = \frac{(3.0\times10^{-3})(4.2\times10^{-3})}{(2.8\times10^{-3})^2}$.
2. $K_c = \frac{12.6\times10^{-6}}{7.84\times10^{-6}} = 1.607$.
3. Starting with $0.1\,\mathrm{M}$ NO: at equilibrium $[\mathrm{NO}] = 0.1(1-\alpha)$, $[\mathrm{N_2}] = [\mathrm{O_2}] = 0.05\alpha$.
4. $K_c = \frac{(0.05\alpha)^2}{(0.1(1-\alpha))^2} = \left(\frac{\alpha}{2(1-\alpha)}\right)^2 = 1.607$.
5. $\frac{\alpha}{2(1-\alpha)} = \sqrt{1.607} = 1.268$.
6. $\alpha = 2.536(1-\alpha) \Rightarrow \alpha = \frac{2.536}{3.536} = 0.717$, which is option $4$.

**Subtopic:** Degree of Dissociation and Vapour Density, Calculating Equilibrium Concentrations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 46)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q100_cc5e7e53_29102026.png?v=cc5e7e531a84)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q100_ae546b71_29102026.png?v=ae546b71a267)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** One set of equilibrium concentrations fixes $K_c$, and the same $K_c$ with the $2\mathrm{NO} \rightleftharpoons \mathrm{N_2} + \mathrm{O_2}$ stoichiometry fixes the degree of dissociation from any starting amount.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Squaring $2.8 \times 10^{-3}$ as $7.84 \times 10^{-7}$ instead of $7.84 \times 10^{-6}$ makes $K_c = 16.1$ in place of $1.61$, and $\alpha = \frac{2\sqrt{K_c}}{1+2\sqrt{K_c}}$ then comes out as $0.889$.
- **Why:** This question requires $K_c$ computed from the printed equilibrium concentrations and then re-used with the stoichiometry of $\mathrm{2NO \rightleftharpoons N_2 + O_2}$, demonstrated by 'If $0.1$ mol L$^{-1}$ of NO is taken in a closed vessel, what will be degree of dissociation $(\alpha)$ of NO at equilibrium?'.
- **Note:** Three of the four options are the digits 8.89 at different powers of ten; only the largest has a derivation, so the other two are recorded as fillers with the routes that were checked. The printed key, $0.717$, is reproduced by the clean calculation.
<!--/ecat-->

## Q101

Biology · botany · Plant Growth and Development

Auxin is used by gardeners to prepare weed-free lawns. But no damage is caused to grass as auxin

- (1) promotes apical dominance.
- (2) promotes abscission of mature leaves only.
- **(3)** does not affect mature monocotyledonous plants.
- (4) can help in cell division in grasses, to produce growth.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Auxin does not affect mature monocot plants.
2. In monocots, especially grasses show limited translocation and cause rapid degradation of external auxin.

**Solved independently** (answer withheld)

1. Synthetic auxins (e.g. 2,4-D) are used as weedicides: they kill dicotyledonous weeds but do not affect mature monocotyledonous plants, so lawn grass (a monocot) is unharmed, which is option $3$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q101_21eb749a_29102026.png?v=21eb749ac333)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q101_a5c7a9f2_29102026.png?v=a5c7a9f2eff8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Auxin herbicides are selective: broad-leaved dicot weeds are killed while mature monocot grasses are insensitive
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Apical dominance is auxin's best-known effect and NCERT prints it in the same auxin block as the weed-free-lawn line, so a student reaching for a true auxin function supplies it here, but it says nothing about why a monocot grass survives
- **Why:** This question requires the reason NCERT gives for grass surviving an auxin weedkiller, demonstrated by the stem breaking off at 'no damage is caused to grass as auxin' so that each option is a rival explanation rather than a fact to name.
- **Note:** Option 1 is also printed beside the key's line in the same auxin block, so nearby_fact was considered; answers_other_question was taken because the option's failure is relevance, not substitution. It is true of auxin and simply does not address monocots against dicots, which is §5.1's 'TRUE but answers something the stem did not ask'.
<!--/ecat-->

## Q102

Biology · botany · Photosynthesis in Higher Plants

How many molecules of ATP and NADPH are required for every molecule of $\mathrm{CO_2}$ fixed in the Calvin cycle?

- (1) 2 molecules of ATP and 3 molecules of NADPH
- (2) 2 molecules of ATP and 2 molecules of NADPH
- (3) 3 molecules of ATP and 3 molecules of NADPH
- **(4)** 3 molecules of ATP and 2 molecules of NADPH

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For fixation of $1$ molecule of $\mathrm{CO_2}$ in Calvin cycle $3$ $\mathrm{ATP}$ molecules and $2$ $\mathrm{NADPH}$ molecules are required.

**Solved independently** (answer withheld)

1. Fixing one $\mathrm{CO_2}$ in the Calvin cycle uses 2 ATP and 2 NADPH in reduction and 1 ATP in regenerating RuBP, so $3$ ATP and $2$ NADPH per $\mathrm{CO_2}$; this is option $4$.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q102_d73527e0_29102026.png?v=d73527e01cd3)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q102_ca13c5e4_29102026.png?v=ca13c5e4325f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fixing one CO2 in the Calvin cycle costs 3 ATP and 2 NADPH: two ATP and both NADPH in the reduction step, the third ATP in regenerating RuBP
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who holds the pair of numbers 3 and 2 but not which cofactor owns which gives the larger number to NADPH, because NADPH is the one doing the reducing, and the printed option is exactly that swap
- **Why:** This question requires the stored stoichiometry of the Calvin cycle, demonstrated by 'How many molecules of ATP and NADPH are required for every molecule of CO2 fixed' supplying no quantity to compute from, and by each option printing both counts together.
- **Note:** type_patterns called this statement_options on 'full-statement options', which contradicts the printed shape: the options are numeric pairs, not statements to judge. Recorded as two_part, since both counts must be right together. The counts in the key match NCERT's own line for one CO2 fixed.
<!--/ecat-->

## Q103

Biology · botany · Anatomy of Flowering Plants

In the given figure, which component has thin outer walls and highly thickened inner walls?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q103_ae4d1033_29102026.png?v=ae4d1033d0f0)

- **(1)** C
- (2) D
- (3) A
- (4) B

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Guard cells of stomata have thin outer wall and highly thickened inner walls.

**Solved independently** (answer withheld)

1. The figure is a stomatal apparatus: A = epidermal cell, B = subsidiary cell, C = bean-shaped guard cell, D = stomatal pore.
2. Guard cells have thin, elastic outer walls and highly thickened inner walls (facing the pore), so the answer is C, which is option $1$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 47)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q103_3a894d82_29102026.png?v=3a894d82ab97)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q103_67ae6025_29102026.png?v=67ae6025dc8e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Uneven wall thickening, thin on the outer side and heavily thickened on the inner side, is the wall pattern that marks out one cell among the epidermal cells in the figure
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the options are bare letters and the figure was not supplied to this step
- **Why:** This question requires reading a named component off the supplied figure, demonstrated by 'In the given figure, which component' and by options that are only the bare letters 'C', 'D', 'A', 'B'.
- **Note:** The paper is intact, so this is not source_damage_artifact; the figure (figures_agent/2024_Q4/q103.png) simply was not readable at this step and the options carry no content a trap could be read from. For a reviewer holding the figure: the chapter is Epidermal Tissue System and the stem's thin-outer, thick-inner wall is the guard-cell pattern, so check whether a wrong letter points at a cell drawn next to the guard cell, such as a subsidiary or ordinary epidermal cell. That would be a nearby_fact carried by position in the drawing, and it cannot be confirmed without the image.
<!--/ecat-->

## Q104

Biology · botany · Cell: The Unit of Life

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Nucleolus | I | Site of formation of glycolipid |
| B | Centriole | II | Organization like the cartwheel |
| C | Leucoplasts | III | Site for active ribosomal RNA synthesis |
| D | Golgi apparatus | IV | For storing nutrients |

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-II, B-III, C-I, D-IV
- (3) A-III, B-IV, C-II, D-I
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Nucleolus is a site for active ribosomal RNA synthesis
2. Both the centrioles in a centrosome lie perpendicular to each other in which each has an organisation like the cartwheel.
3. Leucoplasts are the colourless plastids of varied shapes and sizes with stored nutrients.
4. Golgi apparatus is the important site for formation of glycoproteins and glycolipids.

**Solved independently** (answer withheld)

1. Nucleolus is the site for active ribosomal RNA synthesis, so $A \rightarrow III$.
2. Centriole has peripheral triplet microtubules arranged like a cartwheel, so $B \rightarrow II$.
3. Leucoplasts are colourless plastids that store nutrients (starch, oils, proteins), so $C \rightarrow IV$.
4. Golgi apparatus is the important site of formation of glycoproteins and glycolipids, so $D \rightarrow I$.
5. $A$-$III$, $B$-$II$, $C$-$IV$, $D$-$I$ matches option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q104_287d1917_29102026.png?v=287d1917b3cf)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q104_74ecc94c_29102026.png?v=74ecc94c7554)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each organelle has one signature job: the nucleolus makes rRNA, the centriole's triplet fibrils sit in a cartwheel, leucoplasts store food, and the Golgi builds glycolipids
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who has secured nucleolus-rRNA and Golgi-glycolipid finds both of those pairings already inside this code, so the two pairings they cannot check ride along on the two they can.
- **Why:** This question requires the function NCERT states for each named organelle, demonstrated by List II printing 'Site for active ribosomal RNA synthesis' and 'Organization like the cartwheel' as properties to be returned to their owners.
<!--/ecat-->

## Q105

Biology · botany · Morphology of Flowering Plants

Identify the type of flowers based on the position of calyx, corolla and androecium with respect to the ovary from the given figures (a) and (b)

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q105_e8e8572b_29102026.png?v=e8e8572bacf7)

- (1) (a) Epigynous; (b) Hypogynous
- (2) (a) Hypogynous; (b) Epigynous
- (3) (a) Perigynous; (b) Epigynous
- **(4)** (a) Perigynous; (b) Perigynous

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. If gynoecium is situated in the centre and other parts of the flower are located on the rim of the thalamus almost at the same level, it is called perigynous.
2. Both diagram shows perigynous condition.

**Solved independently** (answer withheld)

1. In figure (a) the thalamus forms a deep cup; the ovary sits free inside it and the sepals, petals and stamens arise from the cup's rim, roughly level with the ovary, so (a) is perigynous.
2. In figure (b) the thalamus forms a shallower cup; the ovary is again free (not fused with the thalamus), with the other whorls on the rim at about the ovary's level, so (b) is perigynous.
3. Neither ovary is fused with the thalamus with whorls above it (epigynous), and neither has whorls inserted below a superior ovary on a flat or convex thalamus (hypogynous), so the answer is option $4$.

**Subtopic:** Position of the Ovary · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q105_82334355_29102026.png?v=82334355fb1f)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q105_b47d593b_29102026.png?v=b47d593b6263)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Hypogynous, perigynous and epigynous name where calyx, corolla and androecium sit relative to the ovary: above a superior ovary, level with a half-sunken ovary, or above an ovary the thalamus has grown over and fused with
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student reads the first figure as perigynous and then, because the thalamus has climbed around the ovary in the second, promotes it to epigynous, so the option keeps the key's label for (a) and loses (b)
- **Why:** This question requires reading the two figures and naming the ovary position in each, demonstrated by 'from the given figures (a) and (b)' and by options that label both (a) and (b) and are graded whole.
- **Note:** type_patterns called this statement_options; the options are paired terms for (a) and (b), so it is recorded as two_part, matching q102. The figure (figures_agent/2024_Q4/q105.png) was not readable at this step, so the trap rests on the printed option terms and the printed key, not on the drawings: option 3 is the only option that agrees with the key on (a) and departs on (b), and the routes name the perigynous-epigynous boundary rather than any specific drawing. A reviewer holding the figure should confirm that boundary is what separates the key from option 3.
<!--/ecat-->

## Q106

Biology · botany · Biological Classification

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Rhizopus | I | Mushroom |
| B | Ustilago | II | Smut fungus |
| C | Puccinia | III | Bread mould |
| D | Agaricus | IV | Rust fungus |

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Rhizopus is a bread mould fungus.
2. Ustilago is a smut fungi.
3. Puccinia is known as rust fungi.
4. Agaricus is commonly called mushroom.
5. A-III
6. B-II
7. C-IV
8. D-I

**Solved independently** (answer withheld)

1. Rhizopus is the bread mould (A-III); Ustilago is the smut fungus (B-II); Puccinia is the rust fungus (C-IV); Agaricus is the mushroom (D-I), so the match is option $1$.

**Subtopic:** Basidiomycetes, Phycomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q106_38ea22d4_29102026.png?v=38ea22d45814)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q106_f70d9db4_29102026.png?v=f70d9db435bb)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The textbook fungi by their common names: Rhizopus the bread mould, Ustilago the smut, Puccinia the rust and Agaricus the mushroom
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who has Rhizopus as the bread mould and Ustilago as the smut sees both of those pairings in this code and takes the remaining two names, printed in one NCERT line together, either way round.
- **Why:** This question requires the common name NCERT prints for each named fungus, demonstrated by List II offering 'Mushroom', 'Smut fungus', 'Bread mould' and 'Rust fungus' as the names to be returned to Agaricus, Ustilago, Rhizopus and Puccinia.
- **Note:** nearby_fact was considered for option 3, since Puccinia and Agaricus are printed in the same NCERT line, and the position test was applied: swapping them for two unlike names leaves the pull intact, so position is doing the work. But the option is a four-part code with two of the key's pairings kept and the failing part is what decides it, so half_right is the label that names the option; the position effect is recorded in the route.
<!--/ecat-->

## Q107

Biology · botany · Morphology of Flowering Plants

Which of the following is an example of actinomorphic flower?

- **(1)** Datura
- (2) Cassia
- (3) Pisum
- (4) Sesbania

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Datura shows actinomorphic flower.
2. In Cassia, Pisum and Sesbania, zygomorphic flowers are seen.

**Solved independently** (answer withheld)

1. NCERT lists Datura as having actinomorphic flowers and Cassia, Pisum, Sesbania (pea, gulmohur-type) as having zygomorphic flowers, so the answer is option $1$.

**Subtopic:** The Flower · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q107_fda10a45_29102026.png?v=fda10a45b17a)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q107_3a5a0cfb_29102026.png?v=3a5a0cfb8661)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Actinomorphic flowers divide into equal halves through any radial plane; the legume flowers divide in one plane only and are zygomorphic
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  NCERT's single sentence on floral symmetry prints mustard, datura and chilli on the actinomorphic side and pea, gulmohur, bean and Cassia on the zygomorphic side, so a student who recalls that Cassia is one of the symmetry examples but not which side it sits on takes it, helped by its five spreading, nearly equal petals
- **Why:** This question requires the named example NCERT prints for radial floral symmetry, demonstrated by 'Which of the following is an example of actinomorphic flower?' offering four plant names with no criterion printed to apply; the trap was settled by the swap test, since replacing Cassia with a plant outside NCERT's symmetry sentence kills the pull, so position carries it and not likeness of names.
<!--/ecat-->

## Q108

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the set of **correct** statements:
Choose the correct answer from the options given below.

- **(A)** The flowers of *Vallisneria* are colourful and produce nectar.
- **(B)** The flowers of water lily are not pollinated by water.
- **(C)** In most of water-pollinated species, the pollen grains are protected from wetting.
- **(D)** Pollen grains of some hydrophytes are long and ribbon like.
- **(E)** In some hydrophytes, the pollen grains are carried passively inside water.

- (1) C, D and E only
- (2) A, B, C and D only
- (3) A, C, D and E only
- **(4)** B, C, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Flowers of *Vallisneria* are not colourful and do not produce nectar.
2. Waterlily is pollinated by insect or wind.
3. In water-pollinated species, pollen grains are protected from wetting by a mucilaginous covering.
4. In some hydrophytes such as *Vallisneria* pollen grains are carried passively by water current.

**Solved independently** (answer withheld)

1. Statement A is false: water-pollinated flowers such as those of *Vallisneria* are not colourful and do not produce nectar.
2. Statement B is true: water lily and water hyacinth flowers emerge above water and are pollinated by insects or wind, not by water.
3. Statement C is true: in most water-pollinated species the pollen grains are protected from wetting by a mucilaginous covering.
4. Statement D is true: in some hydrophytes (e.g. seagrasses) the pollen grains are long and ribbon like.
5. Statement E is true: in seagrasses the pollen grains are carried passively inside the water.
6. Correct set is B, C, D and E only, which is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 49)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q108_ea6833f1_29102026.png?v=ea6833f18674)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q108_806bf268_29102026.png?v=806bf2685760)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Water-pollinated flowers trade colour and nectar for mucilage-protected, ribbon-like pollen, while aquatics whose flowers emerge above the water, like water lily, are still insect- or wind-pollinated
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Water lily is a name printed inside the water-pollination paragraph itself, so it is read as an example of hydrophily rather than as the counter-example, statement B is struck out, and the three statements that can be confirmed word for word are left standing alone
- **Why:** This question requires the printed description of water-pollinated flowers and pollen to be checked statement by statement, demonstrated by 'In most of water-pollinated species, the pollen grains are protected from wetting' standing in the same list as 'The flowers of water lily are not pollinated by water'.
- **Note:** nearby_fact rather than look_alike_term: Vallisneria and water lily do not resemble each other as words, and the pull survives if either name is swapped for an unlike one, because what carries the student is that both names are printed inside the water-pollination paragraph.
<!--/ecat-->

## Q109

Biology · botany · Principles of Inheritance and Variation

A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant. What type of phenotype/s is/are expected in the progeny?

- (1) Only red flowered plants
- **(2)** Red flowered as well as pink flowered plants
- (3) Only pink flowered plants
- (4) Red, Pink as well as white flowered plants

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Pink colour flower in snapdragon have genotype Rr
2. Red flowered snapdragon have genotype RR when they both are crossed

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q109_sol_1_c94426c1_29102026.svg?v=c94426c108cc)

3. So the progeny that we get are red and pink flowered plants only

**Solved independently** (answer withheld)

1. In Snapdragon, flower colour shows incomplete dominance: $RR$ = red, $Rr$ = pink, $rr$ = white.
2. Pink $\times$ red is $Rr \times RR$; gametes are $R, r$ and $R$.
3. Progeny: $\frac{1}{2} RR$ (red) $: \frac{1}{2} Rr$ (pink), so red and pink flowered plants appear, which is option $2$.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q109_db68e303_29102026.png?v=db68e3030d46)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q109_d936def9_29102026.png?v=d936def9a6aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Under incomplete dominance the heterozygote shows the intermediate colour, so pink is Rr and a pink x red (RR) cross gives half red and half pink with no white possible
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The three colours red, pink and white are the answer to the snapdragon cross the book prints, the self of the pink F1, so a student who matches the organism to that figure recites its phenotypes instead of running the cross in the stem
- **Why:** This question requires applying the incomplete-dominance rule to a cross the book does not print, demonstrated by 'A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant' rather than the printed self of the pink F1.
- **Note:** type_patterns called this statement_options; each option is a single outcome phrase rather than a statement block to judge, so it is recorded as mcq under the rule that long options do not by themselves make a question statements.
<!--/ecat-->

## Q110

Biology · botany · Plant Growth and Development

Formation of interfascicular cambium from fully developed parenchyma cells is an example for

- (1) Differentiation
- (2) Redifferentiation
- **(3)** Dedifferentiation
- (4) Maturation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The phenomenon of formation of interfascicular cambium from fully differentiated parenchyma cells is called dedifferentiation.

**Solved independently** (answer withheld)

1. Fully differentiated parenchyma cells that regain the ability to divide and form a meristem (interfascicular cambium) undergo dedifferentiation, which is option $3$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q110_922cf332_29102026.png?v=922cf332e04a)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q110_3143984c_29102026.png?v=3143984ce6c3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Dedifferentiation: cells that are already fully mature regain the power to divide and become meristematic again
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Redifferentiation is the next sentence of the same paragraph and differs from the right name by one prefix, so a student who remembers that the interfascicular cambium goes on to make secondary xylem and phloem reads the example as the re- step. The cells named in the stem are the mature parenchyma that regain division, which is the de- step; redifferentiation is what their products do afterwards.
- **Why:** This question requires the name NCERT gives to mature cells regaining the power to divide, demonstrated by the stem's 'from fully developed parenchyma cells', which fixes the starting point of the change.
- **Note:** Swap test applied on the trap axis: replace the two names with unlike words and the pull dies, so the resemblance of the prefixed pair is doing the work and the label is look_alike_term even though NCERT prints the two beside each other.
<!--/ecat-->

## Q111

Biology · botany · Principles of Inheritance and Variation

Match List I with List II
Choose the **correct** answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Two or more alternative forms of a gene | I | Back cross |
| B | Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent | II | Ploidy |
| C | Cross of $\mathrm{F_1}$ progeny with any of the parents | III | Allele |
| D | Number of chromosome sets in plant | IV | Test cross |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Two or more alternative forms of gene are called alleles.
2. B. Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent is a test cross.
3. C. Cross of $\mathrm{F_1}$ progeny with any of the parents is a back cross.
4. D. Number of chromosome sets in plant is called ploidy.

**Solved independently** (answer withheld)

1. Two or more alternative forms of a gene are alleles, so $A \rightarrow III$.
2. Crossing the $\mathrm{F_1}$ with the homozygous recessive parent is a test cross, so $B \rightarrow IV$.
3. Crossing the $\mathrm{F_1}$ with either parent is a back cross, so $C \rightarrow I$.
4. The number of chromosome sets in a plant is its ploidy, so $D \rightarrow II$.
5. $A-III, B-IV, C-I, D-II$ is option $3$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q111_407b4798_29102026.png?v=407b4798d438)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q111_41628e94_29102026.png?v=41628e940b3c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** A test cross crosses the F1 to the homozygous recessive parent; a back cross crosses the F1 to either parent, so the test cross is the special case of the back cross
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Not one of the three wrong codes repeats a single pairing from the key, so either of the two rows whose wording names the term outright - alternative forms of a gene, number of chromosome sets - settles the answer alone; and the one pair of look-alike definitions the lists do print, 'with homozygous recessive parent' against 'with any of the parents', is nowhere offered swapped on its own.
- **Why:** This question requires telling two neighbouring crosses apart from their definitions, demonstrated by List I printing 'Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent' and 'Cross of $\mathrm{F_1}$ progeny with any of the parents' as separate rows while List II prints both 'Back cross' and 'Test cross'.
- **Note:** no_trap here rests on an inspectable property of the option set, not on any claim about what is picked: no wrong code repeats a pairing from the key, so one secured pair decides the question. compare was chosen over fact_line because rows B and C differ by a single phrase and List II prints both terms of that pair; fact_line would have been right had the rows been four unrelated definitions.
<!--/ecat-->

## Q112

Biology · botany · Photosynthesis in Higher Plants

Which of the following are required for the dark reaction of photosynthesis? Choose the correct answer from the options given below:

- **(A)** Light
- **(B)** Chlorophyll
- **(C)** $\mathrm{CO_2}$
- **(D)** ATP
- **(E)** NADPH

- (1) A, B and C only
- (2) B, C and D only
- **(3)** C, D and E only
- (4) D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For dark reaction of photosynthesis there are the requirement of
2. $\mathrm{CO_2}$
3. ATP
4. NADPH

**Solved independently** (answer withheld)

1. The dark reaction (Calvin cycle) does not directly use light or chlorophyll, so A and B are not required.
2. It fixes $\mathrm{CO_2}$ (C) and uses ATP (D) and NADPH (E) from the light reaction, so the answer is C, D and E only, option $3$.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q112_9f149c3e_29102026.png?v=9f149c3ed440)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q112_974aecda_29102026.png?v=974aecda4bd5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Calvin cycle runs without light but spends the light reaction's ATP and NADPH to fix CO2
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Light and chlorophyll are the requirements photosynthesis is introduced with, so the requirement list of the light reaction is supplied for the stage that follows it
- **Why:** This question requires the stated inputs of the light-independent reaction, demonstrated by the five items being 'Light', 'Chlorophyll', 'CO2', 'ATP' and 'NADPH' with no condition or quantity printed to work out.
- **Note:** wrong_site_attacked is used in its stage sense: the option supplies the requirements of the other stage of the same pathway.
<!--/ecat-->

## Q113

Biology · botany · Cell Cycle and Cell Division

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** Chromosomes become gradually visible under light microscope during leptotene stage.
- **(Statement II)** The beginning of diplotene stage is recognized by dissolution of synaptonemal complex.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. During leptotene stage the chromosomes become gradually visible under the light microscope.
2. The beginning of diplotene is recognised by the dissolution of the synaptonemal complex and the tendency of the recombined homologous chromosomes of the bivalents to separate from each other except at the site of crossover.
3. Thus both statement I and II are correct.

**Solved independently** (answer withheld)

1. In leptotene of prophase I, chromosomes become gradually visible under the light microscope, so Statement I is true.
2. The beginning of diplotene is recognised by dissolution of the synaptonemal complex, so Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q113_85536f1e_29102026.png?v=85536f1eeaf1)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q113_605a8ef4_29102026.png?v=605a8ef4f9ea)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each sub-stage of prophase I is recognised by one landmark: chromosomes first become visible in leptotene, and the synaptonemal complex formed in zygotene dissolves at the start of diplotene
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The synaptonemal complex is learnt as the zygotene structure, so a student who has filed it there reads a sentence attaching it to diplotene as a moved fact and marks Statement II false. NCERT prints both ends of the complex's life, and the dissolution is what it names as diplotene's opening landmark.
- **Why:** This question requires the landmark NCERT assigns to each named sub-stage of prophase I, demonstrated by 'The beginning of diplotene stage is recognized by dissolution of synaptonemal complex', whose verdict turns on where that structure's life begins and ends. Applied the likeness test to the trap: the -tene names share a suffix, but replacing them with unlike words leaves the pull intact, because what carries the student is the adjacent printed fact that the complex forms in the stage before.
<!--/ecat-->

## Q114

Biology · botany · Cell Cycle and Cell Division

Spindle fibers attach to kinetochores of chromosomes during

- (1) Prophase
- **(2)** Metaphase
- (3) Anaphase
- (4) Telophase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spindle fibers attach to kinetochores of chromosome in metaphase stage.

**Solved independently** (answer withheld)

1. In NCERT, the start of metaphase is marked by spindle fibres attaching to the kinetochores of chromosomes, which then line up at the equatorial (metaphase) plate, so the answer is option $2$.

**Subtopic:** Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q114_f963303a_29102026.png?v=f963303a0a24)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q114_c6c1de14_29102026.png?v=c6c1de140db5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Metaphase: the chromosomes line up on the equator and the spindle fibres bind the kinetochore on each chromatid
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Prophase is stored by its headline event, the assembly of the mitotic spindle, so a student who holds spindle and prophase as one item puts the attachment there too. The fibres do exist by then, but while the nuclear envelope is intact they cannot reach the chromosomes, and NCERT places the binding to kinetochores in metaphase.
- **Why:** This question requires the mitotic stage NCERT states the spindle fibres bind the kinetochores in, demonstrated by the four options being the four phases with no criterion printed to apply.
- **Note:** The option names the right event one stage early rather than a different fact printed beside it, so wrong_site_attacked is used in preference to nearby_fact.
<!--/ecat-->

## Q115

Biology · botany · Biotechnology: Principles and Processes

What is the fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism? Choose the correct answer from the options given below:

- **(A)** The piece of DNA would be able to multiply itself independently in the progeny cells of the organism.
- **(B)** It may get integrated into the genome of the recipient.
- **(C)** It may multiply and be inherited along with the host DNA.
- **(D)** The alien piece of DNA is not an integral part of chromosome.
- **(E)** It shows ability to replicate.

- (1) A and B only
- (2) D and E only
- **(3)** B and C only
- (4) A and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because
2. The fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism are:
3. (B) It may get integrated into the genome of the recipient
4. (C) It may multiply and be inherited along with the host DNA
5. $\Rightarrow$ This piece of DNA would not be able to multiply itself in the progeny cells of the organism but when gets integrated into the genome of the recipient, it may multiply and be inherited along with the host DNA.

**Solved independently** (answer withheld)

1. A piece of DNA carrying only the gene of interest has no origin of replication, so it cannot multiply independently in the progeny cells: A is false and E is false.
2. Such DNA may get integrated into the genome of the recipient: B is true.
3. Once integrated, it may multiply and be inherited along with the host DNA: C is true.
4. Hence B and C only, which is option $3$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 51)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q115_3b51fa10_29102026.png?v=3b51fa10c91c)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q115_20625f10_29102026.png?v=20625f100c4f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A DNA fragment with no origin of replication cannot multiply on its own; it is propagated only by integrating into the host chromosome and being copied with it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A transferred gene is understood to be there in order to multiply, so the fragment is granted replication - but the stem's 'only gene of interest' means no origin of replication came with it, and the origin is the condition that licenses replication
- **Why:** This question requires the replication requirement to be carried into each proposed fate, demonstrated by the stem's 'a piece of DNA carrying only gene of interest', which is what separates 'It may get integrated into the genome of the recipient' from 'would be able to multiply itself independently in the progeny cells'.
- **Note:** The NOT recorded in negative_words_seen comes from statement D, 'is not an integral part of chromosome', not from the task, so the task reads straight.
<!--/ecat-->

## Q116

Biology · botany · Molecular Basis of Inheritance

The lactose present in the growth medium of bacteria is transported to the cell by the action of

- (1) Beta-galactosidase
- (2) Acetylase
- **(3)** Permease
- (4) Polymerase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The y gene lac operon codes for permease enzyme, which increase the permeability of cell to $\beta$-galactosides.
2. So, the lactose present in the growth medium of bacteria is transported into the cell by the action of permease.

**Solved independently** (answer withheld)

1. In the lac operon, the $y$ gene codes for permease, which increases the permeability of the cell to $\beta$-galactosides, so lactose is transported into the cell by permease, which is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q116_bd03659f_29102026.png?v=bd03659f9596)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q116_d314e589_29102026.png?v=d314e5899f50)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the lac operon the y gene makes permease, which carries lactose across the bacterial membrane; the z gene's beta-galactosidase only splits it once it is inside
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Beta-galactosidase is the enzyme carried in memory as the lactose enzyme and is the first of the three lac genes printed. It is true that it acts on lactose, but it hydrolyses it into galactose and glucose inside the cell, which answers the breakdown question and not the transport one the stem asks.
- **Why:** This question requires the lac-operon enzyme NCERT states increases the cell's permeability to lactose, demonstrated by the stem's 'transported to the cell by the action of'.
<!--/ecat-->

## Q117

Biology · botany · Anatomy of Flowering Plants

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** Parenchyma is living but collenchyma is dead tissue.
- **(Statement II)** Gymnosperms lack xylem vessels but presence of xylem vessels is the characteristic of angiosperms.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- **(4)** Statement I is false but Statement II is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Collenchyma is also living tissue.
2. Gymnosperm lack xylem vessels but presence of xylem vessels is the characteristic of angiosperm.

**Solved independently** (answer withheld)

1. Parenchyma and collenchyma are both living simple tissues; only sclerenchyma is dead, so Statement I is false.
2. Gymnosperms lack xylem vessels, and vessels are a characteristic feature of angiosperms, so Statement II is true.
3. Statement I false and Statement II true is option $4$.

**Subtopic:** Permanent Tissue, Complex Tissue · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 52)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q117_7cbc171d_29102026.png?v=7cbc171d73c4)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q117_1a6ed69a_29102026.png?v=1a6ed69a90e8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Among the simple tissues only sclerenchyma is dead, parenchyma and collenchyma both being living, and xylem vessels are the angiosperm feature gymnosperms lack
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Dead at maturity' belongs to sclerenchyma, the third member of the -enchyma trio, and a student who holds the three names as one block attaches it to collenchyma and passes Statement I as true. Statement II is true as printed, so both-true follows from that one misattachment.
- **Why:** This question requires the stored property NCERT attaches to each named tissue and group, demonstrated by 'Parenchyma is living but collenchyma is dead tissue', which is settled by one recalled property of one named tissue. Applied the likeness test: replace sclerenchyma with a word from outside the -enchyma trio and the pull on Statement I dies, so the resemblance between the three names is what carries it rather than their order on the page.
- **Note:** compare was considered because both statements print a contrast, and rejected: the contrast is asserted by the statement, and what the student must supply is one stored property of collenchyma.
<!--/ecat-->

## Q118

Biology · botany · Biological Classification

Which one of the following is not a criterion for classification of fungi?

- (1) Morphology of mycelium
- **(2)** Mode of nutrition
- (3) Mode of spore formation
- (4) Fruiting body

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The morphology of the mycelium, mode of spore formation and fruiting bodies form the basis for the division of the kingdom fungi into various classes.

**Solved independently** (answer withheld)

1. Fungi are divided into classes on the basis of the morphology of the mycelium, the mode of spore formation and the fruiting bodies, so mode of nutrition is not a criterion, which is option $2$.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q118_0a98d288_29102026.png?v=0a98d288c542)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q118_72e28d46_29102026.png?v=72e28d46e07c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fungal classification rests on the morphology of the mycelium, the mode of spore formation and the fruiting body; nutrition is described for fungi but is not one of those criteria
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Fungal nutrition fills the opening of the same section - saprophytic, parasitic, symbiotic - so a student who takes that as the basis of classification must discard one of the three real criteria, and the fruiting body is the one missing from Phycomycetes and Deuteromycetes. The option is true, since NCERT does list the fruiting body as a criterion, so it answers which feature IS a criterion rather than the negated question printed.
- **Why:** This question requires the three criteria NCERT states fungal classification rests on, demonstrated by the stem's 'not a criterion for classification of fungi' set over four options that are all true statements about fungi.
<!--/ecat-->

## Q119

Biology · botany · Principles of Inheritance and Variation

In a plant, black seed color (BB/Bb) is dominant over white seed color (bb). In order to find out the genotype of the black seed plant, with which of the following genotype will you cross it?

- (1) BB
- **(2)** bb
- (3) Bb
- (4) BB/Bb

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. To determine the genotype of a black seed colour at $F_2$, the black seed from $F_2$ is crossed with the white seed colour.
2. This is called a test cross.
3. $\therefore$ To determine the genotype of (BB/Bb) black seed we need to cross them with white seed i.e. bb.

**Solved independently** (answer withheld)

1. The genotype of a dominant-phenotype plant is found by a test cross with the homozygous recessive parent, $bb$.
2. $BB \times bb \rightarrow$ all $Bb$ (black); $Bb \times bb \rightarrow 1\,Bb : 1\,bb$ (black : white), so the cross with $bb$ (option $2$) distinguishes them.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q119_f8812208_29102026.png?v=f88122080e49)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q119_76046386_29102026.png?v=760463867b71)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Test cross: cross the unknown dominant with the homozygous recessive, so that each offspring's colour reports the unknown's second allele
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The cross printed beside the test cross is the heterozygote selfing Bb x Bb with its 3:1 ratio, so a student reaching for the remembered monohybrid cross pairs the black plant with Bb. White then appears in a quarter of the offspring if the unknown is Bb and in none if it is BB, which reads a ratio instead of reading the unknown's second allele straight off each offspring.
- **Why:** This question requires the test-cross rule applied to an unknown dominant, demonstrated by the stem's 'in order to find out the genotype of the black seed plant, with which of the following genotype will you cross it'.
- **Note:** Option 3 would also let white seeds appear, at a quarter instead of a half, but the printed key follows the test cross as it is defined; tagged as printed, not re-judged. Swap test on the trap axis: replace the symbols with unlike ones and the pull survives, because what carries the student is the adjacent remembered cross rather than the likeness of bb and Bb, so nearby_fact and not look_alike_term.
<!--/ecat-->

## Q120

Biology · botany · Biodiversity and Conservation

Tropical regions show greatest level of species richness because
Choose the correct answer from the options given below.

- **(A)** Tropical latitudes have remained relatively undisturbed for millions of years, hence more time was available for species diversification.
- **(B)** Tropical environments are more seasonal.
- **(C)** More solar energy is available in tropics.
- **(D)** Constant environments promote niche specialization.
- **(E)** Tropical environments are constant and predictable.

- **(1)** A, C, D and E only
- (2) A and B only
- (3) A, B and E only
- (4) A, B and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Only statement B is incorrect because tropical environments unlike temperate ones, are less seasonal, relatively more constant and predictable.
2. Thus statements A, C, D and E are correct.

**Solved independently** (answer withheld)

1. Statement A is true: tropical latitudes remained relatively undisturbed for millions of years, giving long evolutionary time for species diversification.
2. Statement B is false: tropical environments are less seasonal, not more seasonal.
3. Statement C is true: more solar energy is available in the tropics, contributing to higher productivity.
4. Statements D and E are true: tropical environments are relatively constant and predictable, and such constant environments promote niche specialization.
5. True statements are A, C, D and E, which is option $1$.

**Subtopic:** Latitudinal Gradients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q120_a5ddc9a1_29102026.png?v=a5ddc9a14d69)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q120_0275bdef_29102026.png?v=0275bdefeeb0)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Tropical richness is explained by undisturbed evolutionary time, a constant and predictable environment that allows niche specialisation, and more available solar energy
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The printed line reads that tropical environments, unlike temperate ones, are less seasonal; B prints that comparison the other way round, and the two halves of the one sentence are ticked together
- **Why:** This question requires the reasons given for the latitudinal gradient to be judged as explanations, demonstrated by the stem ending 'show greatest level of species richness because' with 'More solar energy is available in tropics' among the statements to be weighed.
<!--/ecat-->

## Q121

Biology · botany · Biodiversity and Conservation

These are regarded as major causes of biodiversity loss:
Choose the correct option:

- **(A)** Over exploitation
- **(B)** Co-extinction
- **(C)** Mutation
- **(D)** Habitat loss and fragmentation
- **(E)** Migration

- (1) A, C and D only
- (2) A, B, C and D only
- (3) A, B and E only
- **(4)** A, B and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Major causes of biodiversity losses are
2. (1) Habitat loss and fragmentation
3. (2) Over-exploitation
4. (3) Alien species invasions
5. (4) Co-extinctions
6. Hence correct option is A, B and D only.

**Solved independently** (answer withheld)

1. NCERT lists the four major causes of biodiversity loss (the 'Evil Quartet') as habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions, so A, B and D are causes while mutation (C) and migration (E) are not; the set A, B and D only is option $4$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q121_e6b64d19_29102026.png?v=e6b64d196c54)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q121_acf0ea25_29102026.png?v=acf0ea25a09d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The named major causes of biodiversity loss are habitat loss and fragmentation, over-exploitation, alien species invasion and co-extinction
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The causes are remembered as a set of four, only three of them are printed among these five items, and mutation is taken in to fill the fourth slot, so the correct trio is ticked plus one item that is not a cause at all
- **Why:** This question requires membership of the named set of major causes, demonstrated by the five items being 'Over exploitation', 'Co-extinction', 'Mutation', 'Habitat loss and fragmentation' and 'Migration', with no criterion printed to apply to them.
<!--/ecat-->

## Q122

Biology · botany · Molecular Basis of Inheritance

A transcription unit in DNA is defined primarily by the three regions in DNA and these are with respect to upstream and down stream end;

- (1) Repressor, Operator gene, Structural gene
- (2) Structural gene, Transposons, Operator gene
- (3) Inducer, Repressor, Structural gene
- **(4)** Promotor, Structural gene, Terminator

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A transcription unit of DNA is defined primarily by the three regions in the DNA:
2. (i) A promoter
3. (ii) The structural gene
4. (iii) A terminator
5. The promoter is said to be located towards $5'$-end (upstream) of the structural gene (the reference is made with respect to the polarity of coding strand)
6. The terminator is located towards $3'$-end (downstream) of the coding strand.

**Solved independently** (answer withheld)

1. A transcription unit in DNA consists of a promoter at the upstream end, the structural gene in the middle, and a terminator at the downstream end, which is option $4$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q122_077dc480_29102026.png?v=077dc4806363)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q122_1fb1c05c_29102026.png?v=1fb1c05c45b3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A transcription unit is three stretches of DNA in order - promoter upstream, structural gene, terminator downstream
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Repressor, operator and structural gene are the parts of the lac operon, the model drawn a few pages away in the same chapter as a line of DNA with boxes on it, so a student holding that diagram supplies its labels when asked for three regions. Only the structural gene belongs to both; what defines the transcription unit at its two ends is the promoter and the terminator.
- **Why:** This question requires the three DNA regions NCERT says a transcription unit is defined by, demonstrated by the stem's 'defined primarily by the three regions in DNA and these are with respect to upstream and down stream end'.
- **Note:** The pattern classifier recorded statement_options on 15 full-statement options, but the printed options are not statements: each is an ordered triple of named DNA regions accepted or rejected whole, half an option scoring nothing. The shape is therefore recorded as two_part, the nearest current value for an answer whose parts must all hold, since pair_options is retired. Swap test on the trap axis: replace operator and repressor with two unlike words and the pull is intact, because the neighbouring operon diagram carries it rather than any resemblance to promoter, so nearby_fact.
<!--/ecat-->

## Q123

Biology · botany · Biotechnology: Principles and Processes

Hind II always cuts DNA molecules at a particular point called recognition sequence and it consists of:

- (1) $8\,\mathrm{bp}$
- **(2)** $6\,\mathrm{bp}$
- (3) $4\,\mathrm{bp}$
- (4) $10\,\mathrm{bp}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2).
2. The first restriction endonuclease – Hind II, whose functioning depends on a specific DNA nucleotide sequence was isolated.
3. It was found that Hind II always cut DNA molecules at a particular point by recognising sequence of six base pairs.
4. Option (1), (3) and (4) are incorrect because they have either more than $6$ or less than $6\,\mathrm{bp}$.

**Solved independently** (answer withheld)

1. NCERT says Hind II always cuts DNA at a particular point by recognising a specific sequence of $6\,\mathrm{bp}$, which is option $2$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q123_b895a9b9_29102026.png?v=b895a9b972b9)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q123_0f294a78_29102026.png?v=0f294a788ff6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A restriction endonuclease binds a fixed palindromic recognition site, and the site NCERT gives for Hind II is six base pairs long
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The chapter's worked cutting example is EcoRI, whose figure leaves a four-base AATT overhang, so a student recalling that figure instead of the Hind II sentence reads the count off the overhang and answers 4 bp.
- **Why:** This question requires the stored length NCERT gives for Hind II's recognition site, demonstrated by the stem ending 'it consists of:' above four bare base-pair counts with no sequence printed to count.
- **Note:** E1_question_type arrived as arrange_in_order, which contradicts the printed shape - nothing is sequenced and the four options are single values; the word 'recognition sequence' in the stem is the likely pattern hit. Recorded as mcq. nearby_fact rather than look_alike_term: '4 bp' and '6 bp' do not resemble each other as terms, and swapping the counts for two unlike numbers leaves the pull intact, because what carries it is the other count printed on the same page.
<!--/ecat-->

## Q124

Biology · botany · Biomolecules

The cofactor of the enzyme carboxypeptidase is:

- **(1)** Zinc
- (2) Niacin
- (3) Flavin
- (4) Haem

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as the cofactor of the enzyme carboxypeptidase is zinc.
2. Niacin is associated with coenzyme NAD and NADP.
3. Option (4) is incorrect as haem is the prosthetic group in peroxidase and catalase.

**Solved independently** (answer withheld)

1. NCERT lists zinc as the metal-ion cofactor of the proteolytic enzyme carboxypeptidase, so the answer is option $1$ (Zinc).

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q124_fe8ff8bf_29102026.png?v=fe8ff8bffca4)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q124_df05a201_29102026.png?v=df05a201d48c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Enzyme cofactors come in three kinds - metal ions, prosthetic groups and coenzymes - and carboxypeptidase's is a tightly bound zinc ion
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  NCERT's cofactor paragraph names haem as the prosthetic group of peroxidase and catalase one sentence from the line giving carboxypeptidase its zinc, so a student who kept the paragraph's examples without their enzymes picks the other bound, metal-carrying group.
- **Why:** This question requires the one cofactor NCERT attaches to a named enzyme, demonstrated by 'The cofactor of the enzyme carboxypeptidase is:' with four options that are each a cofactor from the same chapter.
- **Note:** nearby_fact rather than look_alike_term: zinc, haem, niacin and flavin resemble each other in no way as words, and swapping them for unlike terms would leave the pull intact, because it is the shared paragraph that carries it.
<!--/ecat-->

## Q125

Biology · botany · Microbes in Human Welfare

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Clostridium butylicum | I | Ethanol |
| B | Saccharomyces cerevisiae | II | Streptokinase |
| C | Trichoderma polysporum | III | Butyric acid |
| D | Streptococcus sp. | IV | Cyclosporin-A |

- (1) A-III, B-I, C-II, D-IV
- (2) A-II, B-IV, C-III, D-I
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-IV, B-I, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Clostridium butylicum — Butyric acid
2. B. Saccharomyces cerevisiae — Ethanol
3. C. Trichoderma polysporum — Cyclosporin-A
4. D. Streptococcus sp. — Streptokinase

**Solved independently** (answer withheld)

1. $A$: Clostridium butylicum produces butyric acid, so $A \to III$.
2. $B$: Saccharomyces cerevisiae (brewer's yeast) produces ethanol, so $B \to I$.
3. $C$: Trichoderma polysporum produces cyclosporin-A, an immunosuppressant, so $C \to IV$.
4. $D$: Streptococcus produces streptokinase, a clot buster, so $D \to II$.
5. $A-III,\ B-I,\ C-IV,\ D-II$ is option $3$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q125_8a8dbd1c_29102026.png?v=8a8dbd1cd534)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q125_fd4cc15a_29102026.png?v=fd4cc15a276d)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each industrial microbe is tied to one product: Clostridium butylicum to butyric acid, baker's yeast to ethanol, Trichoderma polysporum to cyclosporin-A and Streptococcus to streptokinase
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student who has the two fermentation pairs right finds both of them in this code and then drops the two bioactive drugs, which NCERT prints side by side, onto the two remaining microbes in the order the lists run.
- **Why:** This question requires the product NCERT names for each industrial microbe, demonstrated by List II printing 'Butyric acid', 'Ethanol', 'Cyclosporin-A' and 'Streptokinase' as the products to be returned to their producers.
- **Note:** Options 1 and 4 each keep two of the key's pairings, so the primary trap was decided on which single confusion reaches the code. Option 1 needs one: which of the two bioactive drugs comes from which of the two remaining organisms. Option 4 needs that plus accepting a fungal metabolite from a bacterium, so it is carried in other_options.
<!--/ecat-->

## Q126

Biology · botany · Biodiversity and Conservation

List of endangered species was released by

- (1) GEAC
- (2) WWF
- (3) FOAM
- **(4)** IUCN

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. List of endangered species was released by – IUCN.

**Solved independently** (answer withheld)

1. The list of threatened and endangered species (the Red List / Red Data Book) is released by the IUCN (International Union for Conservation of Nature), which is option $4$.

**Subtopic:** Loss of Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q126_70200157_29102026.png?v=702001576eff)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q126_d56cb53f_29102026.png?v=d56cb53f8b71)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The IUCN publishes the Red List, the international inventory recording which species are threatened
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  WWF is the conservation body whose visible work is saving threatened animals, so a student holding only 'the organisation that deals with endangered species' reaches for it; the inventory asked for is the Red List, which WWF does not issue.
- **Why:** This question requires the body NCERT names as releasing the list of threatened species, demonstrated by 'List of endangered species was released by' above four organisation acronyms.
- **Note:** nearby_fact rather than look_alike_term: IUCN and WWF share no letters or shape, and replacing them with two unlike acronyms would leave the pull intact, because it rests on both being conservation bodies rather than on resemblance. Option 3 prints 'FOAM', which names no organisation and may be a garbled FAO; tagged as printed, and flagged here for a source check.
<!--/ecat-->

## Q127

Biology · botany · Biodiversity and Conservation

The type of conservation in which the threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called

- (1) in-situ conservation
- **(2)** Biodiversity conservation
- (3) Semi-conservative method
- (4) Sustainable development

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The type of conservation in which threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called ex-situ conservation which is a type of biodiversity conservation.

**Solved independently** (answer withheld)

1. Taking threatened species out of their natural habitat and protecting them in a special setting is $\text{ex-situ}$ conservation, as NCERT defines it.
2. Option $1$, in-situ conservation, means protection inside the natural habitat, which is the opposite, so it is wrong.
3. Option $3$, semi-conservative, is a mode of DNA replication and option $4$, sustainable development, is a resource-use concept, so both are wrong.
4. Ex-situ conservation is one kind of biodiversity conservation, so option $2$ is the only option that still fits.

**Subtopic:** Ex Situ Conservation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q127_cea07c8c_29102026.png?v=cea07c8cf4d4)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q127_dc5384f2_29102026.png?v=dc5384f24616)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation moves a threatened species out of its habitat into protected care, while in situ conservation protects it where it lives
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem reproduces NCERT's definition of ex situ conservation almost word for word, and no option reads 'ex situ'; the printed key points at the umbrella term 'Biodiversity conservation', so the option set as stored cannot be read for the route a student would take.
- **Why:** This question requires the term NCERT gives for taking a threatened species out of its habitat into special care, demonstrated by the stem's 'taken out from their natural habitat and placed in special setting where they can be protected and given special care' while option 1 prints the opposite term and no option prints the defined one.
- **Note:** The record is internally inconsistent: the stem is NCERT's ex situ sentence, option 1 is its opposite, and the key is (2) 'Biodiversity conservation', a generic umbrella that does not name the defined practice. That pattern fits an option whose text did not carry across rather than a trap the paper built, so no trap is written and a source check is requested. The key is not re-judged here; the tag follows the printed key.
<!--/ecat-->

## Q128

Biology · botany · Strategies for Enhancement in Food Production

The capacity to generate a whole plant from any cell of the plant is called:

- **(1)** Totipotency
- (2) Micropropagation
- (3) Differentiation
- (4) Somatic hybridization

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Totipotency is defined as the capacity to generate a whole plant from any cell of the plant.

**Solved independently** (answer withheld)

1. The ability of a single plant cell (explant) to give rise to a whole plant is called totipotency, which is option $1$.

**Subtopic:** Plant Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q128_7c35151b_29102026.png?v=7c35151b4a14)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q128_a5ae034c_29102026.png?v=a5ae034c7b06)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Totipotency is the capacity of any plant cell to regenerate a whole plant; micropropagation is the technique that exploits it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Micropropagation is defined in the next lines of the same tissue-culture passage, so a student who holds the passage as one block but not which sentence defined which word hands the technique's name to the capacity.
- **Why:** This question requires the term NCERT defines for a cell's ability to regenerate an entire plant, demonstrated by 'The capacity to generate a whole plant from any cell of the plant is called:'.
- **Note:** nearby_fact rather than look_alike_term: totipotency and micropropagation share no stem or sound, and swapping them for two unlike words leaves the pull intact, because what carries it is their sitting in the same passage.
<!--/ecat-->

## Q129

Biology · botany · Organisms and Populations

The equation of Verhulst-Pearl logistic growth is $\frac{dN}{dt} = rN\left[\frac{K-N}{K}\right]$. From this equation, K indicates:

- (1) Intrinsic rate of natural increase
- (2) Biotic potential
- **(3)** Carrying capacity
- (4) Population density

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In the equation $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$, $K$ represents carrying capacity.

**Solved independently** (answer withheld)

1. In $\frac{dN}{dt} = rN\left[\frac{K-N}{K}\right]$, $r$ is the intrinsic rate of natural increase, $N$ is the population density and $K$ is the carrying capacity, which is option $3$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q129_1a8586cf_29102026.png?v=1a8586cf071a)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q129_f52b9f58_29102026.png?v=f52b9f58aa12)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the logistic equation $K$ is the carrying capacity, the number the habitat can sustain, while $r$ is the intrinsic rate of natural increase
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  'Intrinsic rate of natural increase' is the gloss NCERT prints for $r$ in this same equation, so a student who kept the equation's names without their symbols answers for $r$ when the stem asked for $K$.
- **Why:** This question requires the meaning NCERT attaches to one symbol of the printed logistic equation, demonstrated by 'From this equation, K indicates:' with $r$, $N$ and $K$ all standing in the stem.
- **Note:** answers_other_question rather than nearby_fact: option 1 is not merely printed beside the answer, it is the correct and complete answer to a different question the same stem could have asked - what $r$ denotes.
<!--/ecat-->

## Q130

Biology · botany · Anatomy of Flowering Plants

Bulliform cells are responsible for

- **(1)** Inward curling of leaves in monocots.
- (2) Protecting the plant from salt stress.
- (3) Increased photosynthesis in monocots.
- (4) Providing large spaces for storage of sugars.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In grasses, certain adaxial epidermal cells along the veins modify themselves into large, empty, colourless cells.
2. These are called bulliform cells.
3. When the bulliform cells in the leaves have absorbed water and are turgid, the leaf surface is exposed.
4. When they are flaccid due to water stress, they make the leaves curl inwards to minimise water loss.

**Solved independently** (answer withheld)

1. Bulliform cells are large, empty, colourless cells in the upper epidermis of grass (monocot) leaves; when they lose turgor under water stress the leaf curls inward to cut water loss, so the answer is option $1$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q130_e6a764f5_29102026.png?v=e6a764f5a726)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q130_bf69a226_29102026.png?v=bf69a22692c0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bulliform cells are the large empty epidermal cells of a grass leaf; when they go flaccid the leaf rolls inwards and cuts water loss
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Water stress is the condition named in the bulliform-cell line, and the option offers the same phrase with one word changed, so a student who kept the protective role but not the stressor settles on salt stress.
- **Why:** This question requires the function NCERT states for one named cell type, demonstrated by the stem 'Bulliform cells are responsible for' followed by four rival functions with no criterion printed to apply. Rule-5 test: swap 'salt stress' for an unlike phrase and the pull on option 2 dies, so the likeness to the printed 'water stress' is doing the work, not position.
- **Note:** E1 called this statement_options, which the printed shape does not support: the stem is a sentence completion and the options are noun phrases, not statements put up to be judged. Recorded as mcq, with the rest of the group.
<!--/ecat-->

## Q131

Biology · botany · Biomolecules

Lecithin, a small molecular weight organic compound found in living tissues, is an example of:

- (1) Amino acids
- **(2)** Phospholipids
- (3) Glycerides
- (4) Carbohydrates

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2).
2. Some lipids have phosphorous and a phosphorylated organic compound in them. These are phospholipids.
3. They are found in cell membrane. Lecithin is one example.
4. Option (3) is incorrect as glycerides are another group of lipids in which both glycerol and fatty acids are present.
5. Option (1) and (2) are incorrect as amino acids and carbohydrates are separate groups of biomolecules.

**Solved independently** (answer withheld)

1. Lecithin is glycerol esterified with fatty acids and a phosphate group carrying choline, so it is a phospholipid (option $2$).

**Subtopic:** Lipids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q131_f7c96d40_29102026.png?v=f7c96d4018f4)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q131_7b9fab4a_29102026.png?v=7b9fab4a5738)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Phospholipids are lipids carrying a phosphate head in place of one fatty acid, and lecithin is the named membrane example
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The lipid names printed just before the phospholipid line are mono-, di- and triglycerides, so a student who gets as far as 'lecithin is a fat' stops on the neighbouring name.
- **Why:** This question requires the class NCERT files one named compound under, demonstrated by 'Lecithin ... is an example of:' with four biomolecule classes as options. Rule-5 test: 'glycerides' and 'phospholipids' are not alike as words and the pull survives swapping them for unlike words, so position in the lipid paragraph carries it.
<!--/ecat-->

## Q132

Biology · botany · Biomolecules

Inhibition of Succinic dehydrogenase enzyme by malonate is a classical example of:

- (1) Cofactor inhibition
- (2) Feedback inhibition
- **(3)** Competitive inhibition
- (4) Enzyme activation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because malonate shows close structural similarity with the substrate and it competes with the substrate for the substrate binding site of the enzyme succinic dehydrogenase.
2. Option (1), (2) and (4) are incorrect as enzyme activation, co-factor inhibition are not showing structural similarity with substrate.

**Solved independently** (answer withheld)

1. Malonate closely resembles the substrate succinate in structure, so it competes with succinate for the active site of succinic dehydrogenase, which is competitive inhibition (option $3$).

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q132_b9192be1_29102026.png?v=b9192be1c36b)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q132_7ae6314b_29102026.png?v=7ae6314be285)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A competitive inhibitor resembles the substrate and occupies the active site, as malonate does against succinate on succinic dehydrogenase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Succinic dehydrogenase sits in the Krebs cycle, and feedback inhibition is the inhibition pathways are taught with, so a student who places the enzyme in a pathway reaches for the pathway's own control name.
- **Why:** This question requires the named inhibition type NCERT attaches to the malonate example, demonstrated by 'is a classical example of' with four mechanism names as options. Rule-5 test: 'feedback' and 'competitive' are unlike words and the pull survives swapping them, so it is the inhibition types being taught side by side that carries it.
<!--/ecat-->

## Q133

Biology · botany · Biotechnology and Its Applications

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** Bt toxins are insect group specific and coded by a gene cry IAc.
- **(Statement II)** Bt toxin exists as inactive protoxin in B. thuringiensis. However, after ingestion by the insect the inactive protoxin gets converted into active form due to acidic pH of the insect gut.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as specific Bt toxin genes were isolated from Bacillus thuringiensis and incorporated into the several crop plants such as cotton.
2. The choice of genes depends upon the crop and the targeted pest as most Bt toxins are insect-group specific.
3. The toxin is coded by a gene named cry.
4. There are a number of them, for example, the proteins encoded by the genes cry IAc and cry IIAb control the cotton bollworms, that of cry IAb controls corn borer.

**Solved independently** (answer withheld)

1. Bt toxin proteins are insect-group specific and are coded by cry genes, e.g. $cryIAc$ (with $cryIIAb$) against cotton bollworms, so Statement I is taken as true.
2. The protoxin is activated in the insect gut by its alkaline pH, not acidic pH, so Statement II is false.
3. Statement I true and Statement II false is option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 57)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q133_36377f4d_29102026.png?v=36377f4d8ee2)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q133_50bb1ef3_29102026.png?v=50bb1ef3ac3d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Bt crystals are eaten as inactive protoxin and are solubilised into active toxin by the alkaline pH of the insect gut, and each cry gene codes a toxin for one insect group
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Guts are carried as acidic from human digestion, so a sentence giving an acidic gut as the cause of activation reads like the mechanism as taught and Statement II passes. NCERT gives the opposite condition: the alkaline pH of the insect gut is what solubilises the crystals.
- **Why:** This question requires the cause NCERT gives for protoxin activation, demonstrated by 'the inactive protoxin gets converted into active form due to acidic pH of the insect gut', where the verdict turns on whether the stated cause is the one the book prints.
- **Note:** asks is reason_line rather than fact_line because the statement that decides the verdict is the one asserting a cause ('due to ...'); Statement I is a plain fact line and is true as printed.
<!--/ecat-->

## Q134

Biology · botany · Morphology of Flowering Plants

> ⚠ The independent solve chose (4); the booklet prints (3).

Identify the part of the seed from the given figure which is destined to form root when the seed germinates.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q134_f87231cf_29102026.png?v=f87231cf8fd4)

- (1) A
- (2) B
- **(3)** C
- (4) D

**Answer** — booklet: (3) · independent solve: (4) · differs

**Publisher's solution**

1. Radicle is destined to form root.
2. In the given diagram ‘C’ represent radicle

**Solved independently** (answer withheld)

1. The figure is the L.S. of a monocot (maize) grain: endosperm above, embryo in the lower side.
2. At the upper end of the embryo axis, $A$ is the coleoptile and $B$ is the plumule (shoot apex with leaf primordia), which form the shoot.
3. $C$ marks the scutellum/embryo region beside the axis, which does not form the root.
4. $D$ is the radicle covered by the coleorhiza at the lower end of the axis; the radicle forms the root, so the answer is option $4$.

**Subtopic:** The Seed · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 57)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q134_feb9ee20_29102026.png?v=feb9ee2092be)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q134_daf867a7_29102026.png?v=daf867a76f32)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** The radicle is the end of the embryo axis that grows into the root, while the plumule at the other end gives the shoot
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the options are bare letters and the figure was not supplied to this step
- **Why:** This question requires reading one labelled part off a printed seed figure, demonstrated by 'Identify the part of the seed from the given figure' and options that are the bare letters A, B, C and D.
- **Note:** The seed figure (figures_agent/2024_Q4/q134.png) was not supplied to this step and the options carry no words, so no letter can be tied to a part and no route can be named. The paper itself is intact, so this is not source damage. A reviewer holding the figure should check the label at the other end of the embryo axis, the plumule, and the cotyledon beside it; a pull onto either would be nearby_fact, with the radicle and plumule sitting one above the other on the same axis.
<!--/ecat-->

## Q135

Biology · botany · Principles of Inheritance and Variation

Which one of the following can be explained on the basis of Mendel's Law of Dominance? Choose the correct answer from the options given below:

- **(A)** Out of one pair of factors one is dominant and the other is recessive.
- **(B)** Alleles do not show any expression and both the characters appear as such in $\mathrm{F_2}$ generation.
- **(C)** Factors occur in pairs in normal diploid plants.
- **(D)** The discrete unit controlling a particular character is called factor.
- **(E)** The expression of only one of the parental characters is found in a monohybrid cross.

- (1) A, B and C only
- **(2)** A, C, D and E only
- (3) B, C and D only
- (4) A, B, C, D and E

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to Law of Dominance
2. (1) Characters are controlled by discrete units called factors
3. (2) Factors occur in pairs
4. (3) In a dissimilar pair of factors one member of the pair dominates (dominant) the other recessive
5. The law of dominance is used to explain the expression of only one of the parental characters in a monohybrid cross.
6. Law of segregation is based on the fact that the alleles do not show any expression and both the characters are recovered as such in $\mathrm{F_2}$ generation

**Solved independently** (answer withheld)

1. NCERT states the Law of Dominance as: characters are controlled by discrete units called factors; factors occur in pairs; in a dissimilar pair one factor dominates the other.
2. So D (discrete unit called factor) and C (factors occur in pairs) are part of the law.
3. A (one factor of a pair is dominant, the other recessive) is the core of the law.
4. E: the law explains why only one of the parental characters is expressed in the $\mathrm{F_1}$ of a monohybrid cross, so E is explained.
5. B is wrong: alleles do show expression, and the statement does not follow from dominance.
6. Correct set is A, C, D and E only, which is option $2$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 58)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q135_91433f3c_29102026.png?v=91433f3ccb82)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q135_8e2989ba_29102026.png?v=8e2989ba2e86)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel's Law of Dominance - factors occur in pairs and one member of a dissimilar pair dominates the other - is what accounts for only one parental character showing in a monohybrid cross
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Statement B ends on the F2 line the law is genuinely used to explain, and that familiar ending vouches for its opening claim that the alleles show no expression, so every statement is accepted and the all-five option is taken
- **Why:** This question requires each statement to be checked against the printed postulates of the Law of Dominance, demonstrated by 'Factors occur in pairs in normal diploid plants' and 'The expression of only one of the parental characters is found in a monohybrid cross' both standing as items to accept or reject.
<!--/ecat-->

## Q136

Biology · botany · Respiration in Plants

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Citric acid cycle | I | Cytoplasm |
| B | Glycolysis | II | Mitochondrial matrix |
| C | Electron transport system | III | Intermembrane space of mitochondria |
| D | Proton gradient | IV | Inner mitochondrial membrane |

- (1) A-I, B-II, C-III, D-IV
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Citric acid cycle occurs in mitochondrial matrix.
2. Glycolysis occurs in cytosol in most of the organism.
3. Electron transport system is present in the inner mitochondrial membrane.
4. Proton gradient is formed across the intermembrane space of mitochondria.

**Solved independently** (answer withheld)

1. The citric acid (Krebs) cycle takes place in the mitochondrial matrix, so $A \rightarrow II$.
2. Glycolysis takes place in the cytoplasm, so $B \rightarrow I$.
3. The electron transport system is located in the inner mitochondrial membrane, so $C \rightarrow IV$.
4. Protons are pumped into the intermembrane space of mitochondria, building the proton gradient there, so $D \rightarrow III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $2$.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation, Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q136_87b2d87b_29102026.png?v=87b2d87b7919)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q136_0d1ddff4_29102026.png?v=0d1ddff4d663)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Respiration is split by compartment: glycolysis in the cytoplasm, the citric acid cycle in the matrix, the electron transport system in the inner membrane and the pumped protons in the intermembrane space
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No wrong code repeats a single pairing from the key, so one secured site - glycolysis in the cytoplasm - strikes out all three; and the one single mis-storage that could be made here, the electron transport system against the proton gradient, appears only inside a code that at the same time moves glycolysis into the mitochondrial matrix.
- **Why:** This question requires the compartment NCERT assigns to each stage of respiration, demonstrated by List II printing 'Cytoplasm', 'Mitochondrial matrix', 'Intermembrane space of mitochondria' and 'Inner mitochondrial membrane' as the sites to be returned to their stages.
- **Note:** no_trap rests on the structure of the printed codes, not on any claim about picking: every correct pairing appears in the key alone. A reviewer should look again at option 1 if the mechanism is re-examined with response data, because it is the only code carrying the electron transport system and the proton gradient on each other's compartments, but it also places glycolysis in the matrix.
<!--/ecat-->

## Q137

Biology · botany · Biodiversity and Conservation

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Robert May | I | Species-Area relationship |
| B | Alexander von Humboldt | II | Long term ecosystem experiment using out door plots |
| C | Paul Ehrlich | III | Global species diversity at about 7 million |
| D | David Tilman | IV | Rivet popper hypothesis |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-I, B-III, C-II, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Robert May places the global species diversity at about $7$ million.
2. Alexander von Humboldt gave species-area relationship.
3. Paul Ehrlich used an analogy “Rivet popper hypothesis” to explain the role of species in the ecosystem.
4. David Tilman performed long term ecosystem experiments using out door plots.

**Solved independently** (answer withheld)

1. Robert May estimated global species diversity at about $7$ million, so $A \rightarrow III$.
2. Alexander von Humboldt described the species-area relationship, so $B \rightarrow I$.
3. Paul Ehrlich proposed the rivet popper hypothesis, so $C \rightarrow IV$.
4. David Tilman carried out long-term ecosystem experiments using outdoor plots, so $D \rightarrow II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ matches option $2$.

**Subtopic:** The Importance of Species Diversity to the Ecosystem, Species–Area Relationships · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q137_34d30049_29102026.png?v=34d300498411)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q137_c8761d02_29102026.png?v=c8761d0262b5)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Who contributed what to biodiversity: May's estimate of about 7 million species, Humboldt's species-area relationship, Ehrlich's rivet popper analogy and Tilman's long-term outdoor plots
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who has fixed Robert May to the 7 million figure finds that pairing kept here and arranges the other three names, all drawn from the same two sections of the chapter, around it.
- **Why:** This question requires the attribution NCERT prints for each named ecologist, demonstrated by List II offering 'Global species diversity at about 7 million' and 'Rivet popper hypothesis' as the contributions to be returned to their authors.
<!--/ecat-->

## Q138

Biology · botany · Ecosystem

> ⚠ The independent solve chose (2); the booklet prints (3).

In an ecosystem if the Net Primary Productivity (NPP) of first trophic level is $100x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, what would be the GPP (Gross Primary Productivity) of the third trophic level of the same ecosystem?

- (1) $\dfrac{x}{10}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (2) $x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- **(3)** $10x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (4) $\dfrac{100x}{3x}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. NPP at first trophic level would be the GPP for second trophic level.
2. NPP at second trophic level would be GPP for third trophic level.
3. Therefore, $100x\,(\mathrm{kcal/m^{2}/yr})$ would be GPP at second trophic level and $100x \times 10\%\,(\mathrm{kcal/m^{2}/yr})$ i.e., $10x\,(\mathrm{kcal/m^{2}/yr})$ energy would be GPP at third trophic level.

**Solved independently** (answer withheld)

1. By the $10\%$ law, only $10\%$ of the energy available at one trophic level is transferred to the next.
2. Energy reaching the second trophic level $= 0.1 \times 100x = 10x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$.
3. Energy reaching the third trophic level $= 0.1 \times 10x = x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, which is option $2$.

**Subtopic:** Energy Flow · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 59)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q138_d546ee63_29102026.png?v=d546ee63d2bd)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q138_e8cbf711_29102026.png?v=e8cbf7113aa9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Ten per cent law: only a tenth of the energy held at one trophic level passes on to the next
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the stem's $100x$ and the printed key differ by one ten-per-cent step, and option 4 prints as a ratio of $x$ terms, so which option any route lands on cannot be fixed from this record
- **Why:** This question requires the ten per cent law carried from one trophic level to the next, demonstrated by 'if the Net Primary Productivity (NPP) of first trophic level is $100x$' with options that are multiples of $x$.
- **Note:** Tagged as printed and no trap written. The stem as stored gives the first level $100x$; one transfer leaves $10x$ at the second level and a second transfer leaves $x$ at the third, which is option 2, while the printed key is option 3, $10x$. The key follows if the stem read $1000x$. Option 4 reads $\frac{100x}{3x}$, a ratio of $x$ terms that carries the kcal units of a productivity, which looks like debris rather than a printed distractor. Two characters of this record are therefore in doubt, and a route built on either number would be a guess; needs checking against the printed paper before any trap is written.
<!--/ecat-->

## Q139

Biology · botany · Plant Kingdom

Read the following statements and choose the set of correct statements:
In the members of Phaeophyceae,
Choose the correct answer from the options given below:

- **(A)** Asexual reproduction occurs usually by biflagellate zoospores.
- **(B)** Sexual reproduction is by oogamous method only.
- **(C)** Stored food is in the form of carbohydrates which is either mannitol or laminarin.
- **(D)** The major pigments found are chlorophyll a, c and carotenoids and xanthophyll.
- **(E)** Vegetative cells have a cellulosic wall, usually covered on the outside by gelatinous coating of algin.

- (1) A, B, C and D only
- (2) B, C, D and E only
- **(3)** A, C, D and E only
- (4) A, B, C and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In members of Phaeophyceae sexual reproduction is by oogamous, isogamous or anisogamous methods.
2. Therefore correct set of statements are A, C, D and E.

**Solved independently** (answer withheld)

1. A is true: asexual reproduction in brown algae is usually by biflagellate zoospores.
2. B is false: sexual reproduction may be isogamous, anisogamous or oogamous, not oogamous only.
3. C is true: stored food is complex carbohydrates as laminarin or mannitol.
4. D is true: pigments are chlorophyll $a$, $c$, carotenoids and xanthophylls.
5. E is true: the cellulosic wall is usually covered outside by a gelatinous coating of algin.
6. True set is A, C, D and E, which is option $3$.

**Subtopic:** Phaeophyceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q139_3f84f373_29102026.png?v=3f84f373cce7)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q139_d47160dd_29102026.png?v=d47160ddfdd7)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Brown algae: chlorophyll a and c with carotenoids and xanthophylls, food stored as mannitol or laminarin, a cellulose wall coated with algin, and sexual reproduction that is not restricted to oogamy
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Statements A, C and D are NCERT's own sentences on Phaeophyceae, so a set carrying all three reads as verified, and B rides in on their back: the book lists isogamous, anisogamous and oogamous reproduction for brown algae, and B keeps only the third with 'only' attached.
- **Why:** This question requires each printed line of NCERT's Phaeophyceae description to be graded true or false, demonstrated by 'Sexual reproduction is by oogamous method only' standing among statements C, D and E, which reproduce the book's wording.
- **Note:** Every wrong option is the same shape: statement B plus three true statements. B is the single failing part in all three, so the landing option was chosen by the route that needs no extra belief — checking in printed order and stopping at four letters.
<!--/ecat-->

## Q140

Biology · botany · Plant Growth and Development

Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem, thus, increasing the yield?

- (1) Auxin
- **(2)** Gibberellin
- (3) Cytokinin
- (4) Abscisic acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sugarcanes store carbohydrate as sugar in their stems.
2. Spraying sugarcane crop with gibberellins increases the length of the stem, thus increasing the yield.

**Solved independently** (answer withheld)

1. Gibberellins promote internode elongation, so spraying sugarcane with gibberellin lengthens the stem and increases sugar yield, which is option $2$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q140_2941c0fe_29102026.png?v=2941c0fe0376)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q140_f1379cf0_29102026.png?v=f1379cf09534)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gibberellin lengthens internodes, which is why spraying it on sugarcane raises the stem length and the yield
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Elongation is the word auxins are taught with, so a student matching 'increases the length of stem' to a hormone takes the elongation hormone from the section printed just before gibberellin's.
- **Why:** This question requires the crop use NCERT gives to one growth regulator, demonstrated by 'Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem'. Rule-5 test: 'auxin' and 'gibberellin' are unlike words and the pull survives swapping them for unlike words, so it is the elongation fact's position in the neighbouring hormone's section that carries it.
<!--/ecat-->

## Q141

Biology · botany · Morphology of Flowering Plants

Match List I with List II
List I (Types of Stamens) List II (Example)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Monoadelphous | I | Citrus |
| B | Diadelphous | II | Pea |
| C | Polyadelphous | III | Lily |
| D | Epiphyllous | IV | China-rose |

- **(1)** A-IV, B-II, C-I, D-III
- (2) A-IV, B-I, C-II, D-III
- (3) A-I, B-II, C-IV, D-III
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In China rose monoadelphous androecium is present.
2. Diadelphous androecium is found in pea plant.
3. Polyadelphous androecium is found in citrus.
4. Epiphyllous androecium is found in lily.

**Solved independently** (answer withheld)

1. Monoadelphous stamens (filaments fused into one bundle) occur in China-rose, so $A \to IV$.
2. Diadelphous stamens (two bundles) occur in pea, so $B \to II$.
3. Polyadelphous stamens (more than two bundles) occur in citrus, so $C \to I$.
4. Epiphyllous stamens (attached to perianth) occur in lily, so $D \to III$.
5. $A$-IV, $B$-II, $C$-I, $D$-III matches option $1$.

**Subtopic:** Androecium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q141_012f9b9b_29102026.png?v=012f9b9ba747)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q141_fa33945f_29102026.png?v=fa33945f9c83)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stamen cohesion counts bundles, not stamens: one bundle in China rose, two in pea, many in Citrus, while epiphyllous stamens ride on the petals
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  A student who hears the mono-/poly- prefix as a count of stamens sees China rose's crowd of stamens and reads it as polyadelphous. The prefix counts the bundles the filaments fuse into, and China rose's many stamens fuse into a single tube.
- **Why:** This question requires the plant NCERT prints as the example of each stamen-fusion type, demonstrated by List I reading 'Types of Stamens' against List II 'Example' with no bundle count supplied to work from. Replacing 'Monoadelphous' and 'Polyadelphous' with two unlike words that name bundle counts outright kills the pull, so the likeness of the prefixed terms is doing the work - look_alike_term, not nearby_fact.
- **Note:** Options 2 and 3 are the two codes that keep A-IV and D-III and swap the remaining pair, and both are reached by the same mechanism - counting stamens instead of bundles. Option 3 is carried as the trap because the miscount is strongest on China rose's numerous stamens; option 2 is the same mechanism applied to pea's nine united filaments.
<!--/ecat-->

## Q142

Biology · botany · Molecular Basis of Inheritance

Which of the following statement is correct regarding the process of replication in E.coli?

- (1) The DNA dependent DNA polymerase catalyses polymerization in one direction that is $3' \rightarrow 5'$
- (2) The DNA dependent RNA polymerase catalyses polymerization in one direction, that is $5' \rightarrow 3'$
- (3) The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ as well as $3' \rightarrow 5'$ direction
- **(4)** The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ direction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In Prokaryotes, like E.coli during replication, the DNA dependent DNA polymerase catalyse polymerization only in one direction, that is $5' \rightarrow 3'$

**Solved independently** (answer withheld)

1. As NCERT teaches, the DNA-dependent DNA polymerase catalyses polymerisation in one direction only, $5' \rightarrow 3'$, so options $1$ and $3$ are wrong and option $4$ is correct for replication.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q142_1c9c9a32_29102026.png?v=1c9c9a3220b7)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q142_2ee4c4ff_29102026.png?v=2ee4c4ff9d88)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA polymerase can only add a nucleotide to a free 3'-OH, so the new strand is always built 5'→3' and the lagging strand has to be made in pieces
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The direction printed in option 2 is the right one and the sentence is true as written, so a student who checks the arrow in each option before checking the enzyme stops there; the stem asked about replication, and this option is about the RNA polymerase of transcription.
- **Why:** This question requires the direction NCERT states for the replication enzyme, demonstrated by four options that differ only in which polymerase is named and whether it works '5' → 3'' or '3' → 5''.
- **Note:** E1 left the type null with the comment that the options are reactions; the options are four full claims about polymerase direction and the stem's own word is 'statement', so the printed shape is recorded as statements. Option 2 is true as written of DNA dependent RNA polymerase, and the primase acting during E. coli replication is one, so the option is defensible on a literal reading of 'regarding the process of replication'; tagged as printed, with the key left as it stands.
<!--/ecat-->

## Q143

Biology · botany · Respiration in Plants

Identify the step in tricarboxylic acid cycle, which does not involve oxidation of substrate.

- (1) Malic acid $\rightarrow$ Oxaloacetic acid
- (2) Succinic acid $\rightarrow$ Malic acid
- **(3)** Succinyl-CoA $\rightarrow$ Succinic acid
- (4) Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Oxidation involves the loss of electrons (often as part of hydrogen) from a molecule, leaving to an increase in its oxidation state.
2. This process is typically associated with the transfer of electrons to an electron acceptor which is reduced in the process.
3. The conversion of succinyl CoA to succinic acid does not involve oxidation of substrate.

**Solved independently** (answer withheld)

1. Malic acid $\rightarrow$ oxaloacetic acid is a dehydrogenation: $\text{NAD}^+ \rightarrow \text{NADH} + \text{H}^+$, so the substrate is oxidised.
2. Succinic acid $\rightarrow$ malic acid passes through fumarate; succinate $\rightarrow$ fumarate reduces $\text{FAD} \rightarrow \text{FADH}_2$, so it involves oxidation.
3. Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid is oxidative decarboxylation: $\text{NAD}^+ \rightarrow \text{NADH} + \text{H}^+$ and $\text{CO}_2$ released.
4. Succinyl-CoA $\rightarrow$ succinic acid releases CoA and forms $\text{GTP}$ (or $\text{ATP}$) by substrate-level phosphorylation, with no electron carrier reduced.
5. So the step without substrate oxidation is option $3$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 61)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q143_5bc45ef9_29102026.png?v=5bc45ef93c8d)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q143_1b33c9fa_29102026.png?v=1b33c9fa831e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An oxidation step in the Krebs cycle is one that hands hydrogens to NAD+ or FAD; succinyl-CoA → succinate is the substrate-level phosphorylation step and oxidises nothing
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The test carried out of the cycle is 'an oxidation step makes NADH', and no NADH is printed on succinic acid → malic acid, so the rule is applied at the one step it does not cover — succinate dehydrogenase passes its hydrogens to FAD instead.
- **Why:** This question requires the criterion 'oxidation of substrate' to be applied to each printed conversion, demonstrated by a stem that asks for the step 'which does not involve oxidation of substrate' while the options print bare substrate → product arrows with no enzyme or coenzyme beside them.
- **Note:** E1 left the type null with the comment that the options are reactions; they are substrate-to-product arrows from one pathway with no reagent or condition printed, so the printed shape is recorded as a plain mcq.
<!--/ecat-->

## Q144

Biology · botany · Molecular Basis of Inheritance

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Frederick Griffith | I | Genetic code |
| B | Francois Jacob & Jacque Monod | II | Semi-conservative mode of DNA replication |
| C | Har Gobind Khorana | III | Transformation |
| D | Meselson & Stahl | IV | Lac operon |

- (1) A-III, B-II, C-I, D-IV
- **(2)** A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-IV, D-I
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Frederick Griffith series of experiment witness miraculous transformation in the bacteria.
2. The elucidation of Lac operon was a result of a close association between geneticist, Francois Jacob and a biochemist, Jacques Monod.
3. Meselson and Stahl gave semi-conservative mode of DNA replication.
4. Har Gobind Khorana developed chemical method to define combination of bases in genetic code.

**Solved independently** (answer withheld)

1. Griffith's experiments with Streptococcus pneumoniae showed transformation, so $A \rightarrow III$; Jacob and Monod proposed the lac operon, so $B \rightarrow IV$; Khorana helped decipher the genetic code, so $C \rightarrow I$; Meselson and Stahl proved semi-conservative DNA replication, so $D \rightarrow II$; A-III, B-IV, C-I, D-II is option $2$.

**Subtopic:** The Lac Operon, Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q144_a3ab13a6_29102026.png?v=a3ab13a6e6aa)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q144_b0468b11_29102026.png?v=b0468b114075)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Who established what in molecular genetics: Griffith on transformation, Jacob and Monod on the lac operon, Khorana on the genetic code, Meselson and Stahl on semi-conservative replication
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  With Griffith and Khorana fixed, the two leftover entries are both E. coli work from the same chapter, so a student holding only the organism hands the replication experiment to the two-name team he met first. The lac operon's regulator model is printed under Jacob and Monod's names, and the heavy-isotope culture experiment under Meselson and Stahl's.
- **Why:** This question requires the attribution NCERT prints for each named worker, demonstrated by List II holding 'Transformation', 'Lac operon', 'Genetic code' and 'Semi-conservative mode of DNA replication' with no experiment described to reason from. Swapping the two team names for unlike words leaves the pull intact, because what carries the student is the two attributions sitting in the same chapter on the same organism - nearby_fact, not look_alike_term.
- **Note:** Option 2 is the only code that pairs Meselson and Stahl with semi-conservative replication, so that one pairing fixes the key on its own; the trap on option 1 requires a student who does not hold it and anchors instead on Griffith and Khorana.
<!--/ecat-->

## Q145

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the correct description about the given figure:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q145_153facce_29102026.png?v=153facce4b50)

- **(1)** Wind pollinated plant inflorescence showing flowers with well exposed stamens.
- (2) Water pollinated flowers showing stamens with mucilaginous covering.
- (3) Cleistogamous flowers showing autogamy.
- (4) Compact inflorescence showing complete autogamy

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The given diagram shows a wind pollinated plant showing compact inflorescence and well exposed stamens.
2. Stamens are exposed so complete autogamy does not occur.

**Solved independently** (answer withheld)

1. The figure shows a compact inflorescence from which many long filaments with anthers hang out on all sides, i.e. well-exposed stamens.
2. Well-exposed stamens let wind carry the pollen away easily, an adaptation of wind pollination (anemophily) as NCERT describes it.
3. Cleistogamous flowers never open, so their stamens could not be exposed; water-pollinated flowers do not have exposed stamens like these. So options $2$, $3$ and $4$ are out and the answer is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q145_2abf3f94_29102026.png?v=2abf3f947647)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q145_453b7a4f_29102026.png?v=453b7a4f1c8f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Wind-pollinated flowers advertise nothing and hang their stamens out into the air, while water-pollinated ones keep their pollen under a mucilaginous coat
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Which description is correct is fixed by the printed figure, and the figure was not supplied to this step, so no wrong option can be shown to pull
- **Why:** This question requires the printed figure to be read before any option can be graded, demonstrated by the stem 'Identify the correct description about the given figure' and four options that are rival descriptions of one picture.
- **Note:** The packet carries only a file path and a CDN link for the figure, not its content, so no trap is asserted. The paper itself is intact, so this is a limit of this step's reach and not source damage. A reviewer holding the figure should check option 2 first: water pollination is the other abiotic agent printed in the same NCERT section, so a figure showing an aquatic or ribbon-leaved plant would pull there. Option 3 should be checked if the flowers in the figure are drawn closed. E1's pattern read the four full descriptions as statement_options and that is carried over as qtype statements; the live decision is still reading the picture, which is what asks records.
<!--/ecat-->

## Q146

Biology · botany · Cell: The Unit of Life

The DNA present in chloroplast is:

- (1) Linear, double stranded
- **(2)** Circular, double stranded
- (3) Linear, single stranded
- (4) Circular, single stranded

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The DNA present in chloroplast is circular double stranded.

**Solved independently** (answer withheld)

1. Chloroplasts contain their own small DNA, which is circular and double stranded (like prokaryotic DNA), which is option $2$.

**Subtopic:** Plastids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q146_88586d53_29102026.png?v=88586d5349d2)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q146_3fe10eba_29102026.png?v=3fe10ebaf6ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plastid and mitochondrial genomes are prokaryote-like — naked, circular and double stranded — unlike the linear nuclear chromosome
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Double stranded is the half a student is sure of, and 'linear' is imported from the nuclear chromosome drawn in the same chapter, so the option keeps the right strandedness and swaps the shape.
- **Why:** This question requires the two stated properties of plastid DNA, demonstrated by four options that cross 'Linear' against 'Circular' with 'single stranded' against 'double stranded'.
<!--/ecat-->

## Q147

Biology · botany · Photosynthesis in Higher Plants

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- **(Statement I)** In $\mathrm{C_3}$ plants, some $\mathrm{O_2}$ binds to RuBisCO, hence $\mathrm{CO_2}$ fixation is decreased.
- **(Statement II)** In $\mathrm{C_4}$ plants, mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In $\mathrm{C_3}$ plant, some $\mathrm{O_2}$ bind to RuBisCO, and hence $\mathrm{CO_2}$ fixation is decreased.
2. Statement II is incorrect, photorespiration does not occur in $\mathrm{C_4}$ plants as they lack RuBisCO in mesophyll.
3. Hence statement I is the only correct option.

**Solved independently** (answer withheld)

1. In $\mathrm{C_3}$ plants RuBisCO also binds $\mathrm{O_2}$ (photorespiration), so less $\mathrm{CO_2}$ is fixed: Statement I is true.
2. In $\mathrm{C_4}$ plants the mesophyll cells lack RuBisCO, so they cannot photorespire; the bundle sheath has a high $\mathrm{CO_2}$ concentration, so photorespiration is avoided. NCERT says photorespiration does not occur in $\mathrm{C_4}$ plants, so 'very little photorespiration in mesophyll' is wrong and Statement II is false.
3. Statement I true, Statement II false, which is option $3$.

**Subtopic:** Photorespiration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 62)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q147_8f8a5bc3_29102026.png?v=8f8a5bc3ac3f)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q147_4eefebe7_29102026.png?v=4eefebe7a224)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Photorespiration occurs wherever RuBisCO meets $\mathrm{O_2}$, so in a C4 leaf it can only be sited in the CO2-rich bundle sheath, the mesophyll carrying PEP carboxylase instead
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  'C4 plants show little or no photorespiration' is the line a student carries, and Statement II says that in other words, so it goes through without the cell types being checked against the enzyme each holds. The statement has the two cells the wrong way round, since a C4 mesophyll cell has no RuBisCO at all and the bundle sheath is the only place the process could sit.
- **Why:** This question requires which cell of a C4 leaf photorespiration can be sited in, demonstrated by 'mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration', which is decided by where RuBisCO is held.
- **Note:** wrong_site_attacked was taken over reversed because nothing ordered or directional is inverted here; a process is placed in the wrong cell type of the same leaf.
<!--/ecat-->

## Q148

Biology · botany · Biomolecules

Match List-I with List-II
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | GLUT-4 | I | Hormone |
| B | Insulin | II | Enzyme |
| C | Trypsin | III | Intercellular ground substance |
| D | Collagen | IV | Enables glucose transport into cells |

- **(1)** A-IV, B-I, C-II, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-II, B-III, C-IV, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1)
2. A. GLUT-4 — IV. Enables glucose transport into cells
3. B. Insulin — I. Hormone
4. C. Trypsin — II. Enzyme
5. D. Collagen — III. Intercellular ground substance

**Solved independently** (answer withheld)

1. GLUT-4 is a glucose transporter, so $A \rightarrow IV$; insulin is a hormone, so $B \rightarrow I$; trypsin is an enzyme, so $C \rightarrow II$; collagen is intercellular ground substance, so $D \rightarrow III$. This is option $1$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q148_4feb18a5_29102026.png?v=4feb18a55ff2)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q148_8ed830d9_29102026.png?v=8ed830d901b0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sorting named proteins by the job they do - hormone, enzyme, structural ground substance, or the membrane carrier that moves glucose
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Insulin's taught job is getting glucose into cells, so the one List II entry written as a function reads as insulin's, and that pairing appears in this option alone. The entry names the protein that does the carrying, GLUT-4, while insulin's slot in this list is 'Hormone'.
- **Why:** This question requires the job NCERT names for each of the four molecules, demonstrated by List II offering 'Hormone', 'Enzyme', 'Intercellular ground substance' and 'Enables glucose transport into cells' as the only four slots.
- **Note:** The trap sits on one pair inside the code, B-IV, which is true of insulin but is not the pairing the one-to-one list asks for; answers_other_question is the §5.1 value for a true option that is not what was asked. The four codes are the four cyclic rotations of one mapping, so any single securely held pair - insulin as a hormone, trypsin as an enzyme - fixes the key.
<!--/ecat-->

## Q149

Biology · botany · Morphology of Flowering Plants

Match List I with List II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Rose | I | Twisted aestivation |
| B | Pea | II | Perigynous flower |
| C | Cotton | III | Drupe |
| D | Mango | IV | Marginal placentation |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Rose have half-inferior ovary, thus it is known as Perigynous flower.
2. In Pea, the placenta form a ridge along the ventral suture of the ovary and ovules are borne on this ridge forming two rows.
3. In Cotton, twisted aestivation is present.
4. In Mango, fruit is drupe.

**Solved independently** (answer withheld)

1. Rose has a perigynous flower, so $A \rightarrow II$.
2. Pea (legume) has marginal placentation, so $B \rightarrow IV$.
3. Cotton (China rose family) shows twisted aestivation, so $C \rightarrow I$.
4. Mango fruit is a drupe, so $D \rightarrow III$.
5. $A\text{-}II,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}III$ is option $1$.

**Subtopic:** The Flower, The Fruit · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q149_ee6a5dca_29102026.png?v=ee6a5dca3c44)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q149_c17612eb_29102026.png?v=c17612eb79e0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The stock plant examples of floral and fruit characters: perigynous rose, marginal placentation in pea, twisted aestivation in cotton, the mango drupe
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  NCERT's example of twisted aestivation is China rose, and the item printed here is 'Rose', so a student carrying the remembered example matches the two names - and only this option holds A-I. Rose in this list is the perigynous example, and cotton is the twisted-aestivation plant.
- **Why:** This question requires the plant NCERT names as the example of each floral or fruit character, demonstrated by List II reading 'Twisted aestivation', 'Perigynous flower', 'Drupe' and 'Marginal placentation' against four bare plant names. Replacing 'Rose' with an unlike plant name kills the pull, so the resemblance between 'Rose' and the printed example 'China rose' is doing the work - look_alike_term, not nearby_fact.
- **Note:** Option 2 is also the straight positional code A-I, B-II, C-III, D-IV, but the route carried here is the China-rose resemblance, because anchoring on A-I selects this option uniquely.
<!--/ecat-->

## Q150

Biology · botany · Strategies for Enhancement in Food Production

Which of the following are fused in somatic hybridization involving two varieties of plants?

- (1) Callus
- (2) Somatic embryos
- **(3)** Protoplasts
- (4) Pollens

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Protoplast of two varieties of plants are fused in somatic hybridization.

**Solved independently** (answer withheld)

1. In somatic hybridization the cell walls of the two varieties are digested away and the naked $\text{protoplasts}$ are fused to give a hybrid protoplast, which is option $3$.

**Subtopic:** Tissue Culture and Somatic Hybridisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q150_1fc0e4c9_29102026.png?v=1fc0e4c9eb75)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q150_d0816d6b_29102026.png?v=d0816d6be347)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Somatic hybridisation fuses two wall-less protoplasts, so one plant ends up with both varieties' characters without any gamete taking part
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  The stem's word 'somatic' is printed again inside 'somatic embryos', so a student who has not held on to the protoplast step picks the option that echoes the name of the process; somatic embryos are what cultured cells grow into, and nothing is fused to make them.
- **Why:** This question requires the cell stage NCERT states is fused, demonstrated by the stem asking what 'are fused in somatic hybridization' while all four options name tissue-culture or reproductive material. The swap test decides the trap label: replace 'Somatic embryos' with 'embryoids' and the pull disappears, so the likeness to the stem's word is doing the work rather than position.
<!--/ecat-->

## Q151

Biology · zoology · Animal Kingdom

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Pleurobrachia | I | Mollusca |
| B | Radula | II | Ctenophora |
| C | Stomochord | III | Osteichthyes |
| D | Air bladder | IV | Hemichordata |

- (1) A-IV, B-II, C-III, D-I
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. A. Pleurobrachia – is a member of phylum Ctenophora.
3. B. Radula – is a rasping feeding organ present in phylum Mollusca.
4. C. Stomochord – Rudimentary structure similar to notochord found in the collar region of members of phylum Hemichordata.
5. D. Air bladder – is found in Osteichthyes which provides them buoyancy.

**Solved independently** (answer withheld)

1. $A$: Pleurobrachia is a comb jelly, so it belongs to Ctenophora ($II$).
2. $B$: The radula is the rasping feeding organ of Mollusca ($I$).
3. $C$: The stomochord is the rudimentary notochord-like structure of Hemichordata ($IV$).
4. $D$: The air bladder (swim bladder) is characteristic of bony fishes, Osteichthyes ($III$).
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $2$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q151_9176ff30_29102026.png?v=9176ff3036a1)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q151_f1d66d9b_29102026.png?v=f1d66d9b3dcb)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each phylum's diagnostic organ or genus: the ctenophore Pleurobrachia, the molluscan radula, the hemichordate stomochord, the air bladder of bony fishes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Balanoglossus is printed as the tongue worm and the radula is a rasping tongue, so a student placing two organ words he has read once reaches for the phylum whose own account mentions a tongue. The chapter prints 'stomochord' inside the Hemichordata description itself, and the radula in the molluscan mouth.
- **Why:** This question requires the phylum NCERT attaches to each named organ or genus, demonstrated by List I setting 'Radula', 'Stomochord' and 'Air bladder' against four phylum names with no diagnostic criterion printed. Swapping 'radula' and 'stomochord' for two unlike words leaves the pull intact, because the two terms bear no resemblance to each other and what carries the student is their lying a few lines apart in the same phylum account - nearby_fact.
<!--/ecat-->

## Q152

Biology · zoology · Cell Cycle and Cell Division

Following are the stages of cell division :
Choose the correct sequence of stages from the options given below :

- **(A)** Gap 2 phase
- **(B)** Cytokinesis
- **(C)** Synthesis phase
- **(D)** Karyokinesis
- **(E)** Gap 1 phase

- (1) C-E-D-A-B
- (2) E-B-D-A-C
- (3) B-D-E-A-C
- **(4)** E-C-A-D-B

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct sequence of stages of cell division is
2. Gap 1 phase (E) $\rightarrow$ Synthesis phase (C) $\rightarrow$ Gap 2 phase (A)
3. $\rightarrow$ Karyokinesis (D) $\rightarrow$ Cytokinesis (B)
4. The correct sequence will be $\rightarrow$ E $\rightarrow$ C $\rightarrow$ A $\rightarrow$ D $\rightarrow$ B

**Solved independently** (answer withheld)

1. Interphase runs $G_1$ (E) $\rightarrow$ S (C) $\rightarrow$ $G_2$ (A), then the M phase follows.
2. In the M phase, karyokinesis (D) comes before cytokinesis (B), so the order is $E \rightarrow C \rightarrow A \rightarrow D \rightarrow B$, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q152_ef320418_29102026.png?v=ef320418e9ea)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q152_bc3ea216_29102026.png?v=bc3ea21661b8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** One turn of the cell cycle: G1, S and G2 make up interphase, and M phase runs karyokinesis then cytokinesis
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each wrong order was tested against every single-displacement reading of the cycle — entering the loop at a stage other than G1, running it backwards end to end, reciting the two gap phases together before S, and swapping karyokinesis with cytokinesis. Every wrong option needs at least two of those at once, and the orders a single one of them produces (E-A-C-D-B for the gaps recited together, B-D-A-C-E for a clean backward traversal) are not printed.
- **Why:** This question requires the stages of one cell cycle to be put in time order, demonstrated by 'Choose the correct sequence of stages' printed over the unordered labels Gap 2 phase, Cytokinesis, Synthesis phase, Karyokinesis and Gap 1 phase.
- **Note:** The pattern classifier called this arrange_in_order; the printed shape is a lettered block A-E, so qtype is statements and the sequencing is carried by asks: order.
<!--/ecat-->

## Q153

Biology · zoology · Human Health and Disease

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Common cold | I | Plasmodium |
| B | Haemozoin | II | Typhoid |
| C | Widal test | III | Rhinoviruses |
| D | Allergy | IV | Dust mites |

- (1) A-II, B-IV, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because
2. Common cold is caused by Rhinoviruses
3. Haemozoin is released in blood due to ruptured RBCs after Plasmodium infection.
4. Widal test is used to confirm the typhoid fever.
5. Allergy is caused due to dust mites.

**Solved independently** (answer withheld)

1. Common cold is caused by $\text{Rhinoviruses}$, so A-III.
2. Haemozoin is the toxin released by $\text{Plasmodium}$ when RBCs rupture, so B-I.
3. The Widal test confirms typhoid fever, so C-II.
4. Dust mites are a common allergen, so D-IV.
5. A-III, B-I, C-II, D-IV is option $3$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q153_74b9a82f_29102026.png?v=74b9a82ff8d6)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q153_80792168_29102026.png?v=807921684e50)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pairing each disease marker with its agent: rhinoviruses behind the common cold, haemozoin from ruptured RBCs in malaria, the Widal test for typhoid, dust mites as the allergen
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The allergy paragraph names mites in dust and lists sneezing, watery eyes and a running nose - the common cold's own presentation - so a student matching the cold by its symptoms pairs it with dust mites, and only this option carries A-IV. The cold's cause is printed in its own paragraph as rhino viruses, and dust mites stay with allergy.
- **Why:** This question requires the agent or disease NCERT links to each named item, demonstrated by List I setting 'Haemozoin' and 'Widal test' against 'Plasmodium' and 'Typhoid' in List II. The names 'dust mites' and 'rhino viruses' bear no resemblance to each other, so swapping them for unlike words leaves the pull alive - what carries the student is the symptom line printed beside, which is nearby_fact.
- **Note:** Option 2 is the near-correct code, keeping Widal-Typhoid and Allergy-Dust mites and swapping only the cold and haemozoin, but no printed line reaches either of its differing pairs, so the trap is carried on option 4 where a nameable pull exists. Option 3 is also the only code pairing the common cold with rhinoviruses, so that one line fixes the key.
<!--/ecat-->

## Q154

Biology · zoology · Human Health and Disease

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Typhoid | I | Fungus |
| B | Leishmaniasis | II | Nematode |
| C | Ringworm | III | Protozoa |
| D | Filariasis | IV | Bacteria |

- (1) A-I, B-III, C-II, D-IV
- **(2)** A-IV, B-III, C-I, D-II
- (3) A-III, B-I, C-IV, D-II
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Typhoid – Caused by Salmonella typhimurium (Bacteria)
3. Leishmaniasis – Caused by protozoan i.e., Leishmania donovani
4. Ringworm – Caused by fungi belonging to the genera Microsporum, Trichophyton and Epidermophyton
5. Filariasis – Caused by Wuchereria bancrofti and Wuchereria malayi (Nematode)

**Solved independently** (answer withheld)

1. Typhoid is caused by the bacterium $Salmonella\ typhi$ (A-IV), leishmaniasis by the protozoan $Leishmania$ (B-III), ringworm by fungi (C-I) and filariasis by the nematode $Wuchereria$ (D-II), so the match A-IV, B-III, C-I, D-II is option $2$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q154_90163656_29102026.png?v=90163656bdcc)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q154_b3985250_29102026.png?v=b39852506481)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each human disease in the taught list is tied to one class of causal agent: bacterium, protozoan, fungus or helminth
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The name Ringworm carries the word worm in it, so the disease is read as a worm infection and takes 'Nematode'; the nematode entry is then spent and Filariasis is left with 'Bacteria'.
- **Why:** This question requires the class of causal agent the source states for each named disease, demonstrated by List II holding only the four agent kinds 'Fungus', 'Nematode', 'Protozoa', 'Bacteria' with no criterion printed to apply. Applying the swap test, replacing 'Ringworm' with 'Dermatophytosis' kills the pull entirely, so the likeness inside the name is doing the work rather than the entry's position in the list.
<!--/ecat-->

## Q155

Biology · zoology · Evolution

The flippers of the Penguins and Dolphins are the example of the

- (1) Adaptive radiation
- (2) Natural selection
- **(3)** Convergent evolution
- (4) Divergent evolution

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3), because the flippers of the Penguins and Dolphins perform similar function but they are not anatomically similar structures.
2. This is example of analogous structures.
3. Option (1) is incorrect as adaptive radiation is the process of evolution of different species in a given geographical area starting from a point and literally radiating to the other areas of geography.
4. Option (2) is incorrect as natural selection is a key mechanism of evolution.
5. Option (4) is incorrect as divergent evolution results in the formation of homologous structures.

**Solved independently** (answer withheld)

1. Penguin and dolphin flippers do the same job (swimming) but come from unrelated lineages, so they are analogous organs, which NCERT gives as the result of convergent evolution (option $3$).

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q155_cc3b435d_29102026.png?v=cc3b435d706a)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q155_947014d9_29102026.png?v=947014d977e4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Analogous organs look and work alike but grow out of different ancestry; convergent evolution is unrelated stock pushed into the same form by the same habitat
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A dolphin's flipper is a forelimb, and the forelimb of whale, bat, cheetah and human is the picture printed for homology on the facing part of the same section, so a student who recognises the limb answers with the divergent example printed beside this one.
- **Why:** This question requires the example NCERT itself prints for analogy, demonstrated by the stem naming 'flippers of the Penguins and Dolphins' and by options that set 'Convergent evolution' against 'Divergent evolution'. The swap test decides the trap label: rename the two options 'analogy' and 'homology', words that do not resemble each other, and the pull survives, because the printed forelimb figure is what carries the student there.
<!--/ecat-->

## Q156

Biology · zoology · Body Fluids and Circulation

Following are the stages of pathway for conduction of an action potential through the heart
Choose the correct sequence of pathway from the options given below

- **(A)** AV bundle
- **(B)** Purkinje fibres
- **(C)** AV node
- **(D)** Bundle branches
- **(E)** SA node

- **(1)** E-C-A-D-B
- (2) A-E-C-B-D
- (3) B-D-E-C-A
- (4) E-A-D-B-C

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1) because the correct pathway of conduction of action potential is
2. SA $\rightarrow$ AV node $\rightarrow$ AV bundle $\rightarrow$ Bundle branches $\rightarrow$ Purkinje fibres

**Solved independently** (answer withheld)

1. The action potential starts at the pacemaker, the SA node ($E$), passes to the AV node ($C$), then the AV bundle ($A$), the right and left bundle branches ($D$) and finally the Purkinje fibres ($B$): $E \to C \to A \to D \to B$, which is option $1$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q156_56bec159_29102026.png?v=56bec159259d)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q156_15946d99_29102026.png?v=15946d99422b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The heart's conducting system carries the impulse from the SA node to the AV node, then the AV bundle, the bundle branches and finally the Purkinje fibres
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'AV node' and 'AV bundle' are the same two letters followed by a different noun, so a student holding one 'AV' stage in the chain runs the SA node straight into the AV bundle and parks the leftover AV node at the end, which is exactly E-A-D-B-C.
- **Why:** This question requires the conducting pathway of the heart to be ordered from its pacemaker outward, demonstrated by 'Choose the correct sequence of pathway' over AV bundle, Purkinje fibres, AV node, Bundle branches and SA node. Swap test applied: replace 'AV bundle' with an unlike name and the merging of the two stages dies, so the resemblance and not the list position is doing the work.
<!--/ecat-->

## Q157

Biology · zoology · Biotechnology: Principles and Processes

Which of the following statements is incorrect?

- (1) A bio-reactor provides optimal growth conditions for achieving the desired product
- (2) Most commonly used bio-reactors are of stirring type
- **(3)** Bio-reactors are used to produce small scale bacterial cultures
- (4) Bio-reactors have an agitator system, an oxygen delivery system and foam control system

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3)
2. The statement (3) is incorrect because bioreactors are used for processing of large volumes ($100 - 1000\,\text{litres}$) of culture.
3. Small volume cultures cannot yield appreciable quantities of products.
4. To produce in large quantities the development of bioreactors is required.

**Solved independently** (answer withheld)

1. Bio-reactors are large vessels (100-1000 L) used to process large volumes of culture under optimal conditions; so the statement that they produce small scale bacterial cultures is incorrect, which is option $3$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q157_41266856_29102026.png?v=412668565caa)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q157_378e2223_29102026.png?v=378e2223923f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A bioreactor is the large-volume vessel, of the order of 100 to 1000 litres, in which cultures are processed into product; small cultures are raised in flasks
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student holding the chapter's five bioreactor systems - agitator, oxygen delivery, foam control, temperature control and pH control - counts only three here and reads the two missing ones as the planted error. Naming three systems does not deny the other two, so the sentence stays true.
- **Why:** This question requires judging four printed claims about bioreactors against the chapter's own description and naming the false one, demonstrated by the stem's 'Which of the following statements is incorrect?' together with option 3's 'small scale bacterial cultures', the only clause that description contradicts.
- **Note:** E1 read this as statement_options; the printed shape agrees with qtype statements, since the stem itself asks which statement is incorrect.
<!--/ecat-->

## Q158

Biology · zoology · Human Reproduction

Which of the following is not a component of Fallopian tube?

- **(1)** Uterine fundus
- (2) Isthmus
- (3) Infundibulum
- (4) Ampulla

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as uterine fundus is the upper, dome-shaped part of the uterus, above the opening of fallopian tubes.
2. Option (2) is incorrect as isthmus is the last and narrow part of the oviduct that links to the uterus.
3. Option (3) is incorrect as infundibulum is the part of oviduct which is closer to the ovary.
4. Option (4) is incorrect as ampulla is the wider part of the oviduct.

**Solved independently** (answer withheld)

1. The Fallopian tube (oviduct) has three parts: infundibulum, ampulla and isthmus, so the uterine fundus is not one of them, which is option $1$.

**Subtopic:** The Female Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q158_45dbbe6f_29102026.png?v=45dbbe6f50d9)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q158_8fc6e763_29102026.png?v=8fc6e7631891)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The oviduct runs infundibulum to ampulla to isthmus; the fundus is the domed upper part of the uterus, not a part of the tube
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The description of the oviduct ends with the isthmus, the narrow part that joins the uterus, so a student who files each part by the organ it opens into puts the isthmus on the uterine side and ticks it as the part that is not of the tube. The isthmus is named as the last segment of the oviduct itself.
- **Why:** This question requires the parts the chapter names for the oviduct, demonstrated by the stem's 'not a component of Fallopian tube' set against 'Uterine fundus', which names a part of a different organ. The test applied to the trap was the swap test: replace 'Isthmus' with an unlike word and the pull survives, because what carries the student is where the part is printed, at the uterine junction, rather than any likeness between names.
<!--/ecat-->

## Q159

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements : In the light of the above statements, choose the correct answer from the option given below :

- **(Statement I)** In the nephron, the descending limb of loop of Henle is impermeable to water and permeable to electrolytes.
- **(Statement II)** The proximal convoluted tubule is lined by simple columnar brush border epithelium and increases the surface area for reabsorption.

- (1) Both Statement I and Statement II are true
- **(2)** Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2) because
2. Statement I is false as the descending limb of loop of Henle is permeable to water and almost impermeable to electrolytes.
3. Statement II is false as proximal convoluted tubule is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption.

**Solved independently** (answer withheld)

1. Statement I: the descending limb of the loop of Henle is permeable to water but almost impermeable to electrolytes, so Statement I (impermeable to water, permeable to electrolytes) is false.
2. Statement II: NCERT describes the PCT as lined by simple cuboidal brush border epithelium that increases the surface area for reabsorption; the stem says columnar, so Statement II is false.
3. Both statements false, which is option $2$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q159_25e712d7_29102026.png?v=25e712d7ec41)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q159_9f248789_29102026.png?v=9f248789cc49)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The two limbs of the loop of Henle have opposite permeabilities, the descending passing water and the ascending passing salts, and the PCT's simple cuboidal brush border epithelium is what enlarges the reabsorbing surface
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The PCT sentence runs as NCERT's own down to the brush border and what it is for, with cuboidal replaced by columnar, so a student who checks the clause they remember passes Statement II while correctly rejecting Statement I's limb claim.
- **Why:** This question requires two stored anatomical facts, which limb of the loop passes water and which epithelium lines the PCT, demonstrated by 'The proximal convoluted tubule is lined by simple columnar brush border epithelium', where one adjective decides the verdict. Applied the likeness test: replace columnar with a word from outside the epithelium list and the swap is caught at once, so the resemblance between cuboidal and columnar is carrying the trap.
<!--/ecat-->

## Q160

Biology · zoology · Evolution

Which one of the following factors will not affect the Hardy-Weinberg equilibrium?

- (1) Genetic recombination
- (2) Genetic drift
- (3) Gene migration
- **(4)** Constant gene pool

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as a constant gene pool will not disturb the Hardy-Weinberg equilibrium.
2. Option (1), (2) & (3) will affect the equilibrium leading to evolution.

**Solved independently** (answer withheld)

1. NCERT names five factors that affect Hardy-Weinberg equilibrium: gene migration, genetic drift, mutation, genetic recombination and natural selection, so options $1$, $2$ and $3$ affect it, while a constant gene pool (stable allele frequencies) is the equilibrium state itself, which is option $4$.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q160_fc50e54a_29102026.png?v=fc50e54ae629)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q160_99d145ee_29102026.png?v=99d145ee2ded)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hardy-Weinberg equilibrium is disturbed by five named factors - gene migration, genetic drift, mutation, genetic recombination and natural selection - while a gene pool that stays constant is the equilibrium itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Recombination is taught in the inheritance chapter as the shuffling of alleles already present into new combinations, so a student carries that adjacent fact here and concludes it creates no new allele and therefore moves no frequency. The evolution chapter nonetheless lists genetic recombination among the factors that disturb the equilibrium.
- **Why:** This question requires the chapter's own list of factors that disturb Hardy-Weinberg equilibrium, demonstrated by the stem's 'will not affect the Hardy-Weinberg equilibrium' set against 'Constant gene pool', which restates the equilibrium rather than naming a disturbing factor. Swap test on the trap: replace 'Genetic recombination' with any unlike phrase from the inheritance chapter and the pull survives, so the adjacency of the remembered fact and not a likeness of names is doing the work.
<!--/ecat-->

## Q161

Biology · zoology · Chemical Coordination and Integration

Which of the following is not a steroid hormone?

- (1) Cortisol
- (2) Testosterone
- (3) Progesterone
- **(4)** Glucagon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as glucagon is a proteinaceous hormone secreted from pancreas.
2. Options (1), (2) and (3) are not correct as they are steroid in nature.

**Solved independently** (answer withheld)

1. Cortisol, testosterone and progesterone are steroid hormones, while glucagon is a peptide hormone secreted by the $\alpha$-cells of the islets of Langerhans, so the answer is option $4$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q161_f94ae096_29102026.png?v=f94ae096d154)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q161_ab93f990_29102026.png?v=ab93f990edc3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chemical nature of hormones: the adrenal cortex and the gonads build steroids from cholesterol, while the pancreas secretes peptide hormones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Cortisol is printed in this chapter as the hormone that pushes blood glucose up under stress, which is the job the same chapter gives glucagon, so a student sorting the four by what they do rather than by what they are made of groups cortisol with glucagon and ticks it. Cortisol is filed under the glucocorticoids of the adrenal cortex, which are steroids.
- **Why:** This question requires the stated chemical nature of four named hormones, demonstrated by the stem's 'not a steroid hormone' set against 'Glucagon', the pancreatic peptide among three cholesterol-derived hormones. Swap test on the trap: replace 'Cortisol' with another adrenal-cortex hormone and the pull survives, because the adjacency of the glucose role carries it rather than any likeness between the words.
<!--/ecat-->

## Q162

Biology · zoology · Reproductive Health

Match List I with List II
Choose the correct answer from the option given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Non-medicated IUD | I | Multiload 375 |
| B | Copper releasing IUD | II | Progestogens |
| C | Hormone releasing IUD | III | Lippes loop |
| D | Implants | IV | LNG-20 |

- (1) A-III, B-I, C-II, D-IV
- (2) A-I, B-III, C-IV, D-II
- (3) A-IV, B-I, C-II, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because
2. Lippes loop is a non-medicated IUD.
3. Multiload 375 is a copper releasing IUD.
4. LNG -20 is a hormone releasing IUD.
5. Progestogens are used as implants.

**Solved independently** (answer withheld)

1. Lippes loop is a non-medicated IUD, so $A \rightarrow III$.
2. Multiload 375 is a copper-releasing IUD, so $B \rightarrow I$.
3. LNG-20 is a hormone-releasing IUD, so $C \rightarrow IV$.
4. Implants contain progestogens (or progestogen-estrogen) placed under the skin, so $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q162_1c2400c8_29102026.png?v=1c2400c832d0)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q162_71e0e3d3_29102026.png?v=71e0e3d3280a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Intrauterine devices are grouped by what they release -- nothing, copper or a hormone -- and each group carries its own named devices, with implants a separate progestogen route
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The hormone-releasing IUDs and the implants are both progestogen based and are printed one after the other, so a student holding 'hormone releasing means progestogen' puts 'Progestogens' on the IUD and hands 'LNG-20' to the implants.
- **Why:** This question requires the device names the source prints under each kind of IUD, demonstrated by List II holding trade names -- 'Multiload 375', 'Lippes loop', 'LNG-20' -- that nothing in the stem lets a student derive. On the swap test the two hormonal entries resemble each other not at all, so position in the printed list is what carries the student, which is nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q163

Biology · zoology · Structural Organisation in Animals

In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on

- (1) $5^{\text{th}}$ segment
- **(2)** $10^{\text{th}}$ segment
- (3) $8^{\text{th}}$ and $9^{\text{th}}$ segment
- (4) $11^{\text{th}}$ segment

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2), because in both sexes of cockroach, $10^{\text{th}}$ segment bears a pair of jointed filamentous structures called anal cerci.
2. Options (1), (3) and (4) are incorrect because $5^{\text{th}}$, $8^{\text{th}}$ and $9^{\text{th}}$ segments do not bear such structures.
3. In adult cockroaches only $10^{\text{th}}$ segments are present in abdomen.
4. $11^{\text{th}}$ abdominal segment is absent.

**Solved independently** (answer withheld)

1. In both sexes of cockroach, the $10^{\text{th}}$ abdominal segment bears a pair of jointed filamentous anal cerci, which is option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q163_aa315242_29102026.png?v=aa315242340f)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q163_c6953c42_29102026.png?v=c6953c421153)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cockroach abdomen: the 10th segment bears the anal cerci in both sexes, while the 9th sternum bears the anal styles in males only
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The anal styles sit on the 9th sternum and are the other pair of thread-like hind appendages, so a student who recalls the appendage but not its segment slides the cerci back to the 9th. The stem's 'In both sexes' is the phrase that separates the two, since the styles are in males only.
- **Why:** This question requires the segment the chapter assigns to the anal cerci, demonstrated by the stem's 'In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on' with all four options being segment numbers.
<!--/ecat-->

## Q164

Biology · zoology · Breathing and Exchange of Gases

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Expiratory capacity | I | Expiratory reserve volume + Tidal volume + Inspiratory reserve volume |
| B | Functional residual capacity | II | Tidal volume + Expiratory reserve volume |
| C | Vital capacity | III | Tidal volume + Inspiratory reserve volume |
| D | Inspiratory capacity | IV | Expiratory reserve volume + Residual volume |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-III, B-II, C-IV, D-I
- (3) A-II, B-I, C-IV, D-III
- (4) A-I, B-III, C-II, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Expiratory capacity = Tidal volume + Expiratory reserve volume
2. Functional residual capacity = Expiratory reserve volume + Residual volume
3. Vital capacity = Expiratory reserve volume + Tidal volume + Inspiratory reserve volume
4. Inspiratory capacity = Tidal volume + Inspiratory reserve volume

**Solved independently** (answer withheld)

1. Expiratory capacity $= TV + ERV$, so A matches II.
2. Functional residual capacity $= ERV + RV$, so B matches IV.
3. Vital capacity $= ERV + TV + IRV$, so C matches I.
4. Inspiratory capacity $= TV + IRV$, so D matches III.
5. A-II, B-IV, C-I, D-III is option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q164_0e2b592e_29102026.png?v=0e2b592e8c56)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q164_49993932_29102026.png?v=49993932622e)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each lung capacity is a stated sum of named respiratory volumes, and residual volume belongs only to the functional residual capacity because it can never be breathed out
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Vital capacity stored as 'all the air the lungs hold' sends the student scanning List II for the only sum containing residual volume, so 'Expiratory reserve volume + Residual volume' goes to the vital capacity and the three-volume sum is pushed onto the functional residual capacity.
- **Why:** This question requires the stated composition of each lung capacity, demonstrated by List II printing each capacity as a sum of volumes, 'Expiratory reserve volume + Tidal volume + Inspiratory reserve volume'.
- **Note:** Weighed formula_misused against nearby_fact: List II here prints compositions rather than names, so the pull on option 3 is a wrong sum carried in memory, not an entry reachable by its position. That is why this member's trap label differs from the rest of the group. apply_rule was considered for asks and rejected because the sums are printed in the source rather than derived from any criterion the stem supplies.
<!--/ecat-->

## Q165

Biology · zoology · Neural Control and Coordination

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pons | I | Provides additional space for Neurons, regulates posture and balance. |
| B | Hypothalamus | II | Controls respiration and gastric secretions. |
| C | Medulla | III | Connects different regions of the brain. |
| D | Cerebellum | IV | Neuro secretory cells |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-I, B-III, C-II, D-IV
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. A. Pons – Part of hindbrain, it connects different regions of the brain.
3. B. Hypothalamus – Also have neuro secretory cells which secrete hormones.
4. C. Medulla oblongata – Part of hindbrain which controls respiration and gastric secretions.
5. D. Cerebellum – Part of hindbrain with convoluted surface which provides additional space for neurons, also regulates posture and balance.

**Solved independently** (answer withheld)

1. Pons consists of fibre tracts that interconnect different regions of the brain, so $A \to III$.
2. Hypothalamus contains groups of neurosecretory cells that secrete hypothalamic hormones, so $B \to IV$.
3. Medulla contains centres that control respiration, cardiovascular reflexes and gastric secretions, so $C \to II$.
4. Cerebellum has a very convoluted surface to provide additional space for neurons and maintains posture and balance, so $D \to I$.
5. $A$-$III$, $B$-$IV$, $C$-$II$, $D$-$I$ matches option $2$.

**Subtopic:** Hindbrain, Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q165_8064d1ef_29102026.png?v=8064d1efff8d)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q165_a8e5c724_29102026.png?v=a8e5c7245d02)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What each brain part does: pons relays fibre tracts, medulla runs the vital reflexes, cerebellum holds posture and balance, hypothalamus secretes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Entry II prints two functions joined by 'and', and the pons owns one of them through its pneumotaxic centre, so a student who stops at 'Controls respiration' pairs A with II and never tests the gastric half.
- **Why:** This question requires the function the source gives for each named brain part, demonstrated by List II entries such as 'Controls respiration and gastric secretions.'
- **Note:** half_right is applied to a List II entry that prints two functions joined by 'and', and the failing part is the gastric-secretion half. The judged unit therefore has two parts, which is what rule 2 requires; it is not a lone name.
<!--/ecat-->

## Q166

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below :

- **(Statement I)** The presence or absence of hymen is not a reliable indicator of virginity.
- **(Statement II)** The hymen is torn during the first coitus only.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) because the presence or absence of hymen is not a reliable indicator of virginity because hymen can also be broken by a sudden jolt, insertion of a vaginal tampon, active participation in some sports and in some women the hymen persists even after coitus.

**Solved independently** (answer withheld)

1. Per NCERT, the presence or absence of the hymen is not a reliable indicator of virginity or sexual experience, so Statement I is true.
2. The hymen can be torn by a sudden fall or jolt, insertion of a vaginal tampon, or active participation in sports such as horseback riding or cycling, and in some women it persists even after coitus, so Statement II is false.
3. Statement I is true and Statement II is false, which is option $3$.

**Subtopic:** Female External Genitalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q166_79c4d700_29102026.png?v=79c4d700ac0c)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q166_474fe23c_29102026.png?v=474fe23c9f9f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The hymen can be torn by events other than first coitus and may survive it, which is why its presence or absence says nothing about virginity
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  NCERT prints the first coitus among the causes of the hymen tearing, so a student who checks that clause finds it supported and passes Statement II as true. The failing part is the word 'only', because the same paragraph also gives a sudden fall or jolt, vigorous physical activity and a vaginal tampon as causes.
- **Why:** This question requires the set of causes NCERT gives for the hymen tearing, demonstrated by 'The hymen is torn during the first coitus only', which keeps one printed cause and excludes the rest.
- **Note:** half_right is used here on the 'true but incomplete set' clause of its definition: Statement II keeps one real cause and excludes the others, which is what fails. The NOT recorded in negative_words_seen sits inside Statement I's premise, 'not a reliable indicator', and not in the task instruction.
<!--/ecat-->

## Q167

Biology · zoology · Biotechnology: Principles and Processes

The following diagram showing restriction sites in E. coli cloning vector pBR322. Find the role of ‘X’ and ‘Y’ genes :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q167_6940a325_29102026.png?v=6940a325888c)

- (1) The gene ‘X’ is responsible for resistance to antibiotics and ‘Y’ for protein involved in the replication of Plasmid.
- **(2)** The gene ‘X’ is responsible for controlling the copy number of the linked DNA and ‘Y’ for protein involved in the replication of Plasmid.
- (3) The gene ‘X’ is for protein involved in replication of Plasmid and ‘Y’ for resistance to antibiotics.
- (4) Gene ’X’ is responsible for recognitions sites and ‘Y’ is responsible for antibiotic resistance.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2), because
2. ‘X’ in the given diagram is ori while ‘Y’ is rop.
3. ‘X’ which is ori is responsible for controlling the copy number of the linked DNA and ‘Y’ which is rop codes for protein involved in the replication of plasmid.
4. Options (1), (3) and (4) are incorrect as ‘X’ and ‘Y’ are not related to these functions.

**Solved independently** (answer withheld)

1. In the textbook map of pBR322, $ori$ lies in the lower-left arc and $rop$ lies at the bottom next to the $Pvu\,II$ site, so $X = ori$ and $Y = rop$.
2. $ori$ is where replication starts and it controls the copy number of the linked DNA.
3. $rop$ codes for proteins involved in the replication of the plasmid.
4. So $X$ controls copy number and $Y$ codes for the replication protein, which is option $2$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q167_db9cd512_29102026.png?v=db9cd51251e9)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q167_c7bf8a44_29102026.png?v=c7bf8a44aa03)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On pBR322 the ori controls the copy number of the linked DNA and rop codes for the protein involved in replicating the plasmid, while ampR and tetR are the selectable markers
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The two genes named first about pBR322 are the resistance genes ampR and tetR, printed on the same circle as ori and rop, so a student who cannot place the label X reaches for the feature of this plasmid they can name. The role the key assigns X is control of the copy number of the linked DNA, which is the ori.
- **Why:** This question requires reading which labelled positions on the printed pBR322 map carry X and Y and then giving what each gene does, demonstrated by the stem's 'The following diagram showing restriction sites in E. coli cloning vector pBR322. Find the role of X and Y genes'.
- **Note:** E1 read this as statement_options; the printed shape is two roles answered together, each option fixing both X and Y and scoring nothing if only one is right, so qtype is two_part. The figure itself was not viewable at this step, so the assignment X = ori and Y = rop was taken from the printed key as required, and the routes above rest on the option text plus that key; a reviewer holding the figure should confirm that the map labels X at the origin of replication and Y at rop.
<!--/ecat-->

## Q168

Biology · zoology · Molecular Basis of Inheritance

Which one is the correct product of DNA dependent RNA polymerase to the given template?
3’TACATGGCAAATATCCATTCA5’

- **(1)** 5’AUGUACCGUUUAUAGGUAAGU3’
- (2) 5’AUGUAAAGUUUAUAGGUAAGU3’
- (3) 5’AUGUACCGUUUAUAGGGAAGU3’
- (4) 5’ATGTACCGTTTATAGGTAAGT3’

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Template DNA is :
2. 3’TACATGGCAAATATCCATTCA5’
3. 5’AUGUACCGUUUAUAGGUAAGU3’ m-RNA

**Solved independently** (answer withheld)

1. DNA-dependent RNA polymerase builds RNA in the $5' \to 3'$ direction, complementary and antiparallel to the $3' \to 5'$ template, using U in place of T.
2. Pair each template base: $T \to A$, $A \to U$, $C \to G$, $G \to C$, giving $5'$-AUGUACCGUUUAUAGGUAAGU-$3'$.
3. Option 2 has AAAG where CCGU is expected, option 3 has GGGAAGU where GGUAAGU is expected, and option 4 contains T (DNA), so the match is option $1$.

**Subtopic:** Transcription · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 70)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q168_8b055c03_29102026.png?v=8b055c03fa53)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q168_b201689c_29102026.png?v=b201689c2255)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Transcription reads the template strand 3' to 5' and builds an antiparallel complementary strand in which uracil replaces thymine
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Pairing the template base by base gives A-T-G-T-A-C-C-G and onward, and option 4 prints exactly that, so a student who stops at 'the complementary strand' hands it in. That sequence is the coding DNA strand of this gene; the polymerase puts U wherever DNA puts T, which is option 1.
- **Why:** This question requires the base-pairing rule applied to a printed sequence, demonstrated by the stem supplying 3'TACATGGCAAATATCCATTCA5' and asking for 'the correct product of DNA dependent RNA polymerase' rather than for any stored fact.
- **Note:** Option 4 is the correct coding strand of this gene, so it is true subject matter answering a question the stem did not ask; old_ncert_answer was ruled out because no NCERT value has been altered here.
<!--/ecat-->

## Q169

Biology · zoology · Human Health and Disease

Which of the following are Autoimmune disorders? Choose the most appropriate answer from the options given below:

- **(A)** Myasthenia gravis
- **(B)** Rheumatoid arthritis
- **(C)** Gout
- **(D)** Muscular dystrophy
- **(E)** Systemic Lupus Erythematosus (SLE)

- (1) A, B & D only
- **(2)** A, B & E only
- (3) B, C & E only
- (4) C, D & E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as Myasthenia gravis, Rheumatoid arthritis and Systemic Lupus Erythematosus (SLE) are autoimmune disorders.
2. Muscular dystrophy is a genetic disorder which progressively affects the skeletal muscles.
3. Gout is the inflammation of joints due to deposition of uric acid crystals.
4. Option (1), (3) and (4) are not the correct answer because all of them are not autoimmune disorders.

**Solved independently** (answer withheld)

1. Myasthenia gravis (A) is autoimmune: antibodies act against acetylcholine receptors at the neuromuscular junction.
2. Rheumatoid arthritis (B) is autoimmune: the immune system attacks the synovial joints.
3. Gout (C) is not autoimmune: it is joint inflammation from deposition of uric acid crystals.
4. Muscular dystrophy (D) is not autoimmune: it is a genetic, progressive degeneration of skeletal muscle.
5. SLE (E) is autoimmune: autoantibodies act against the body's own tissues.
6. So the autoimmune set is $\{A, B, E\}$, which is option $2$.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 70)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q169_49925b63_29102026.png?v=49925b634637)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q169_7cbbcce2_29102026.png?v=7cbbcce225d4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An autoimmune disorder is the body's own antibodies attacking its own tissue, which is what separates myasthenia gravis, rheumatoid arthritis and SLE from a metabolic or an inherited muscle disease
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Myasthenia gravis and muscular dystrophy are printed one entry after the other in NCERT's list of muscular disorders, so a student who recognises myasthenia gravis from that list carries its neighbour across and files muscular dystrophy as autoimmune too.
- **Why:** This question requires each named disorder to be assigned to the autoimmune class or kept out of it, demonstrated by 'Which of the following are Autoimmune disorders?' over a list that mixes Gout and Muscular dystrophy with Myasthenia gravis, Rheumatoid arthritis and SLE. Swap test applied: 'muscular dystrophy' and 'myasthenia gravis' are not alike as words, and replacing either with an unlike name leaves the pull intact because the shared list position carries it, so this is nearby_fact and not look_alike_term.
<!--/ecat-->

## Q170

Biology · zoology · Animal Kingdom

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Pterophyllum | I | Hag fish |
| B | Myxine | II | Saw fish |
| C | Pristis | III | Angel fish |
| D | Exocoetus | IV | Flying fish |

- (1) A-II, B-I, C-III, D-IV
- **(2)** A-III, B-I, C-II, D-IV
- (3) A-IV, B-I, C-II, D-III
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct option is option no. (2) as
2. Pterophyllum is the scientific name for Angel fish.
3. Myxine is the scientific name for Hag fish.
4. Pristis is the scientific name for Saw fish.
5. Exocoetus is the scientific name for Flying fish.

**Solved independently** (answer withheld)

1. $\text{Pterophyllum}$ is the angel fish, so $A \rightarrow III$.
2. $\text{Myxine}$ is the hag fish, so $B \rightarrow I$.
3. $\text{Pristis}$ is the saw fish, so $C \rightarrow II$.
4. $\text{Exocoetus}$ is the flying fish, so $D \rightarrow IV$.
5. $A-III, B-I, C-II, D-IV$ matches option $2$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q170_8ea76acf_29102026.png?v=8ea76acfc40c)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q170_f685c09c_29102026.png?v=f685c09cfe2d)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named fish genus in the chordate examples carries a fixed common name, and the genus name is not a safe guide to it
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Pterophyllum' opens with ptero-, the root a student meets in wing words, so the genus is read as the flying fish and takes 'Flying fish', leaving Exocoetus with 'Angel fish'.
- **Why:** This question requires the common name recorded for each named genus, demonstrated by List II holding only common names -- 'Hag fish', 'Saw fish', 'Angel fish', 'Flying fish'. On the swap test, renaming the genus to Scalare kills the pull of option 3 completely, so the likeness of the name is doing the work rather than its place in the list.
<!--/ecat-->

## Q171

Biology · zoology · Human Reproduction

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- **(Assertion A)** FSH acts upon ovarian follicles in female and Leydig cells in male.
- **(Reason R)** Growing ovarian follicles secrete estrogen in female while interstitial cells secrete androgen in male human being.

- (1) Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- (3) A is true but R is false
- **(4)** A is false but R is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as FSH is a gonadotropin affects ovarian follicles in females and causes their growth but in males LH affects Leydig cells leading to secretion of androgens.
2. Growing ovarian follicles secrete estrogen in females while interstitial cells secrete androgen in male human being.
3. Hence, Assertion is false and Reason is true.

**Solved independently** (answer withheld)

1. In males, $\text{FSH}$ acts on Sertoli cells, while $\text{LH}$ acts on the Leydig (interstitial) cells, so Assertion A is false.
2. Growing ovarian follicles secrete estrogen and the interstitial (Leydig) cells secrete androgens, so Reason R is true.
3. A is false and R is true, which is option $4$.

**Subtopic:** Hormonal Regulation of Reproduction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 71)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q171_6239a1c6_29102026.png?v=6239a1c6ec93)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q171_6dc72487_29102026.png?v=6dc7248731df)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** FSH acts on the ovarian follicle in the female and on the Sertoli cells in the male; the Leydig (interstitial) cells are LH's target and the source of androgen
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The Leydig cells are the testicular target NCERT prints beside FSH's own target, and the Reason names those same cells again as the androgen source, so the cell name in the Assertion arrives already vouched for and A is graded true.
- **Why:** This question requires the stated fact about which cell FSH acts on in the male, demonstrated by the Assertion's clause 'Leydig cells in male' being the only thing in either statement that can fail.
- **Note:** Swap test applied for nearby_fact against look_alike_term: 'Leydig' and 'Sertoli' are unlike words, so replacing the pair with two unlike names leaves the trap standing because NCERT prints the two gonadotropin targets side by side and the Reason prints the interstitial-cell line again. Position carries it, not resemblance. The negative words recorded for this question are the standard Assertion-Reason option wording, not a negated task.
<!--/ecat-->

## Q172

Biology · zoology · Biomolecules

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Lipase | I | Peptide bond |
| B | Nuclease | II | Ester bond |
| C | Protease | III | Glycosidic bond |
| D | Amylase | IV | Phosphodiester bond |

- (1) A-IV, B-II, C-III, D-I
- (2) A-III, B-II, C-I, D-IV
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-I, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. A. Lipase – Digests ester bond found in lipids.
3. B. Nuclease – Helps in digestion of phosphodiester bonds found in nucleic acids.
4. C. Protease – Helps in digestion of peptide bond found in proteins.
5. D. Amylase – Digests/breaks the glycosidic bonds found in carbohydrates i.e., digest starch into smaller molecules, ultimately yielding maltose, which in turn is cleaved into two glucose molecules by maltase.

**Solved independently** (answer withheld)

1. Lipase hydrolyses the ester bonds of lipids, so $A \rightarrow II$; nuclease hydrolyses the phosphodiester bonds of nucleic acids, so $B \rightarrow IV$; protease hydrolyses peptide bonds, so $C \rightarrow I$; amylase hydrolyses glycosidic bonds of starch, so $D \rightarrow III$. This matches option $3$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 71)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q172_5ff622bf_29102026.png?v=5ff622bf163f)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q172_a40ea29c_29102026.png?v=a40ea29c8858)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each hydrolytic enzyme class is named for the substrate whose bond it breaks: ester in fats, phosphodiester in nucleic acids, peptide in proteins, glycosidic in starch
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Phosphodiester bond' has ester inside it, so a student who knows a fat is an ester reaches for the longer, more chemical-sounding name for lipase and leaves the plain 'Ester bond' to the nuclease.
- **Why:** This question requires the bond each enzyme class hydrolyses, demonstrated by List II holding four bond names, 'Peptide bond', 'Ester bond', 'Glycosidic bond', 'Phosphodiester bond'. On the swap test, 'Ester bond' and 'Phosphodiester bond' share the very word that decides the pairing and replacing either with an unlike name kills the pull, so the resemblance carries the student rather than the list position.
<!--/ecat-->

## Q173

Biology · zoology · Cell: The Unit of Life

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Axoneme | I | Centriole |
| B | Cartwheel pattern | II | Cilia and flagella |
| C | Crista | III | Chromosome |
| D | Satellite | IV | Mitochondria |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-II, B-IV, C-I, D-III
- **(4)** A-II, B-I, C-IV, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Axoneme is seen in cilia and flagella
2. Centriole shows cartwheel appearance
3. Crista is found in mitochondria
4. Satellite is present in chromosomes

**Solved independently** (answer withheld)

1. The axoneme is the 9+2 microtubule core of cilia and flagella, so $A \rightarrow II$.
2. The cartwheel pattern (9 peripheral triplet fibrils with a central hub) is seen in the centriole, so $B \rightarrow I$.
3. Cristae are infoldings of the inner mitochondrial membrane, so $C \rightarrow IV$.
4. A satellite is a small fragment beyond the secondary constriction of some chromosomes, so $D \rightarrow III$.
5. $A\text{-}II,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}III$ matches option $4$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 71)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q173_745b5a68_29102026.png?v=745b5a68d810)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q173_32d6b7d4_29102026.png?v=32d6b7d4eb7e)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each organelle owns a signature ultrastructure: the centriole's cartwheel, the mitochondrion's cristae, the chromosome's satellite, the axoneme of cilia and flagella
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  With axoneme fixed to cilia and satellite to the chromosome, only centriole and mitochondrion are left, and a student picturing the mitochondrion's inner folds radiating inward reads Cartwheel pattern as that picture, which pushes Crista onto the centriole
- **Why:** This question requires the stated owner of each named ultrastructure, demonstrated by List II holding four coordinate organelles, Centriole, Cilia and flagella, Chromosome and Mitochondria, with no criterion printed to apply.
- **Note:** wrong_site_attacked was considered for option 3 and rejected: the cartwheel is a structure, not an event relocated along a stage or site the stem prints, and what carries the student is the two organelle paragraphs sitting together. Distractor construction is paired here: options 1 and 2 differ only in the B and C rows, as do options 3 and 4.
<!--/ecat-->

## Q174

Biology · zoology · Cell Cycle and Cell Division

Match List I with List II :
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| A | Diakinesis | I | Synaptonemal complex formation |
| B | Pachytene | II | Completion of terminalisation of chiasmata |
| C | Zygotene | III | Chromosomes look like thin threads |
| D | Leptotene | IV | Appearance of recombination nodules |

- (1) A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-IV, D-III
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Diakinesis – Completion of terminalisation of chiasmata
2. (B) Pachytene – Appearance of recombination nodules
3. (C) Zygotene – Synaptonemal complex formation
4. (D) Leptotene – Chromosomes look like thin threads
5. A-II, B-IV, C-I, D-III

**Solved independently** (answer withheld)

1. Diakinesis (A) is marked by completion of terminalisation of chiasmata, so $A \rightarrow II$.
2. Pachytene (B) shows the appearance of recombination nodules, so $B \rightarrow IV$.
3. Zygotene (C) is when synapsis is accompanied by synaptonemal complex formation, so $C \rightarrow I$.
4. Leptotene (D) is when chromosomes become visible as thin threads, so $D \rightarrow III$.
5. $A$-II, $B$-IV, $C$-I, $D$-III matches option $3$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q174_76d6133b_29102026.png?v=76d6133b9602)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q174_1ce2d4b4_29102026.png?v=1ce2d4b497ed)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each sub-stage of prophase I is named by one event: thin threads at leptotene, synapsis and the synaptonemal complex at zygotene, recombination nodules at pachytene, terminalisation of chiasmata completed at diakinesis
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The keyword chiasmata carries the student to pachytene, where crossing over happens, so row II is handed to pachytene although it reads Completion of terminalisation of chiasmata, which belongs to diakinesis; holding leptotene to the thin threads then leaves option 2 as the only code with both rows
- **Why:** This question requires the event NCERT states for each named sub-stage, demonstrated by rows such as Chromosomes look like thin threads standing against four stage names.
- **Note:** asks was tested against order and rejected: the stem asks for a pairing code, and no option is a sequence. The one-error completion a student with the zygotene and pachytene events swapped would want, A-II, B-I, C-IV, D-III, is not printed.
<!--/ecat-->

## Q175

Biology · zoology · Animal Kingdom

Consider the following statements :
Choose the correct answer from the options given below :

- **(A)** Annelids are true coelomates
- **(B)** Poriferans are pseudocoelomates
- **(C)** Aschelminthes are acoelomates
- **(D)** Platyhelminthes are pseudocoelomates

- (1) B only
- **(2)** A only
- (3) C only
- (4) D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2), because annelids are true coelomate animals.
2. Options (1), (3) and (4) are incorrect because poriferans are acoelomates, aschelminths are pseudocoelomates and platyhelminthes are acoelomates.

**Solved independently** (answer withheld)

1. A: Annelids have a true coelom (schizocoelom), so A is true.
2. B: Poriferans have no body cavity (cellular level of organisation), so they are not pseudocoelomates; B is false.
3. C: Aschelminthes are the standard example of pseudocoelomates, not acoelomates; C is false.
4. D: Platyhelminthes are acoelomates, not pseudocoelomates; D is false.
5. Only A is true, which is option $2$ (A only).

**Subtopic:** Basis of Classification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q175_6c567781_29102026.png?v=6c567781d25c)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q175_4a947beb_29102026.png?v=4a947bebc9a5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Body-cavity grades: a coelom lined by mesoderm in annelids, a pseudocoelom with mesoderm in scattered pouches in Aschelminthes, and no cavity at all in Platyhelminthes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Acoelomate and pseudocoelomate differ only in their prefix on a shared root, and NCERT introduces the two in consecutive sentences with Platyhelminthes against one and Aschelminthes against the other, so a student holding 'these worms fall short of a true coelom' but not which prefix goes where reads D as the correct statement.
- **Why:** This question requires each phylum to be matched with its body-cavity grade, demonstrated by 'Annelids are true coelomates' standing against 'Platyhelminthes are pseudocoelomates' and 'Aschelminthes are acoelomates'. Swap test applied: the two grades differ only in the prefix on one root, the same shape as monocondylic against dicondylic, and although NCERT also prints them in consecutive sentences, the rulebook gives the resemblance the win when both hold.
- **Note:** Two wrong statements, C and D, carry the same crossed pair in mirror; D was named as the landing option because 'pseudocoelomate' is the grade taught alongside the worms as a block, and Platyhelminthes is the first worm phylum printed in that sequence.
<!--/ecat-->

## Q176

Biology · zoology · Biotechnology and Its Applications

Match List I with List II :

Choose the correct answer form the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\alpha$ –I antitrypsin | I | Cotton bollworm |
| B | Cry IAb | II | ADA deficiency |
| C | Cry IAc | III | Emphysema |
| D | Enzyme replacement therapy | IV | Corn borer |

- (1) A-II, B-I, C-IV, D-III
- (2) A-III, B-I, C-II, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. $\alpha$– I antitrypsin $\rightarrow$ Is used for treatment of Emphysema
3. $\mathit{Cry}$ I Ab gene $\rightarrow$ Controls corn borer
4. $\mathit{Cry}$ I Ac gene $\rightarrow$ Controls cotton bollworms
5. Enzyme replacement therapy $\rightarrow$ Can be used as treatment option in ADA deficiency.

**Solved independently** (answer withheld)

1. $\alpha$-1 antitrypsin is used to treat emphysema: A-III.
2. The gene $cry\,IAb$ controls corn borer: B-IV.
3. The gene $cry\,IAc$ (with $cry\,IIAb$) controls cotton bollworm: C-I.
4. Enzyme replacement therapy (giving functional ADA) is used for ADA deficiency: D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton, Gene Therapy and Molecular Diagnosis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q176_0c0f1368_29102026.png?v=0c0f1368db86)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q176_a7f9d734_29102026.png?v=a7f9d7346cbc)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which product serves which target: cry IAb against corn borer, cry IAc against cotton bollworm, alpha-1 antitrypsin for emphysema, enzyme replacement for ADA deficiency
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  NCERT names the cotton bollworm first in the single sentence that lists the cry genes, so a student holding antitrypsin to emphysema attaches the bollworm to the first cry gene in List I and reaches the only code carrying A-III with B-I
- **Why:** This question requires the target NCERT states for each named gene or therapy, demonstrated by List II being four bare targets, Cotton bollworm, ADA deficiency, Emphysema and Corn borer, with nothing printed about how any of them works. Test applied for the trap label: replacing cry IAb and cry IAc with two unlike labels leaves the pest pairing just as arbitrary and leaves both pests in one printed sentence, so the trap survives and position is the carrier, which makes it nearby_fact rather than look_alike_term.
- **Note:** No code offers the single-error completion A-III, B-I, C-IV, D-II, so a student who swaps only the two pests has to give up another row to answer. The stem as extracted reads Choose the correct answer form the options given below, with form for from; tagged as printed.
<!--/ecat-->

## Q177

Biology · zoology · Locomotion and Movement

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Fibrous joints | I | Adjacent vertebrae, limited movement |
| B | Cartilaginous joints | II | Humerus and Pectoral girdle, rotational movement |
| C | Hinge joints | III | Skull, don’t allow any movement |
| D | Ball and socket joints | IV | Knee, help in locomotion |

- (1) A-IV, B-II, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-III, C-I, D-IV
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as
2. Fibrous joints do not allow any movement. This type of joint is shown by the flat skull bones which fuse end-to-end with the help of dense fibrous connective tissues in the form of sutures.
3. Cartilaginous joint is present between the adjacent vertebrae in the vertebral column and this permits limited movements.
4. Hinge joint is a type of synovial joint present in knee, help in locomotion
5. Ball and socket joint is also a type of synovial joint present between humerus and pectoral girdle and allows rotational movement.

**Solved independently** (answer withheld)

1. Fibrous joints (A) do not allow any movement, as in the flat skull bones, so $A \to III$.
2. Cartilaginous joints (B) join adjacent vertebrae and allow limited movement, so $B \to I$.
3. Hinge joints (C) occur at the knee, so $C \to IV$.
4. Ball and socket joints (D) are between the humerus and pectoral girdle, allowing rotational movement, so $D \to II$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ is option $4$.

**Subtopic:** Joints · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q177_a7974885_29102026.png?v=a7974885f837)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q177_a5b64826_29102026.png?v=a5b648268830)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Joint type goes with the site and the amount of movement: fibrous in the skull with none, cartilaginous between vertebrae with limited movement, hinge at the knee, ball and socket at the shoulder with rotation
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all three wrong codes row by row: not one of them contains a single correct pairing, so no partial knowledge selects one. Each List II row also prints its own site and its own degree of movement, and all four pairings are the chapter's own sentences, so a wrong code can only be reached by contradicting the words printed inside the row it moves.
- **Why:** This question requires the joint type NCERT names for each site, demonstrated by List II printing the site together with the movement, Humerus and Pectoral girdle, rotational movement, so each row carries its own answer.
- **Note:** Three fillers is the finding here, not a gap: I looked again because of the count, and the structural reason is that every List II row prints both site and degree of movement, which over-determines the pairing, and no wrong code holds even one correct row. asks was tested against compare and against apply_rule: the movement phrases are not a criterion applied to a new case, they are the chapter's own sentences, so fact_line stands.
<!--/ecat-->

## Q178

Biology · zoology · Structural Organisation in Animals

Three types of muscles are given as a, b and c. Identify the correct matching pair along with their location in human body:
Name of muscle/location

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q178_5455386e_29102026.png?v=5455386e1801)

- (1) (a) Smooth - Toes
(b) Skeletal – Legs
(c) Cardiac – Heart
- **(2)** (a) Skeletal - Triceps
(b) Smooth – Stomach
(c) Cardiac – Heart
- (3) (a) Skeletal - Biceps
(b) Involuntary – Intestine
(c) Smooth – Heart
- (4) (a) Involuntary – Nose tip
(b) Skeletal – Bone
(c) Cardiac – Heart

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Figure (a) represents skeletal muscle fibres which are closely attached to skeletal bones. In a typical muscle such as triceps and biceps, striated muscle fibres are bundled together in a parallel fashion.
3. Figure (b) represents smooth muscle fibres which are present in the wall of internal organs such as the blood vessels, stomach and intestine.
4. Figure (c) represents cardiac muscle fibres which are exclusively present in the heart.

**Solved independently** (answer withheld)

1. Figure $(a)$ shows long cylindrical, unbranched, striated fibres: skeletal muscle, found in limbs such as the triceps.
2. Figure $(b)$ shows spindle-shaped fibres without striations, each with one central nucleus: smooth muscle, found in the wall of the stomach.
3. Figure $(c)$ shows striated, branched fibres joined together: cardiac muscle, found only in the heart.
4. Option $1$ fails (smooth muscle is not in toes), option $3$ fails ($(c)$ is cardiac, not smooth), option $4$ fails ($(a)$ is skeletal, not involuntary); option $2$ matches all three.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q178_ae7f8455_29102026.png?v=ae7f8455489d)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q178_b198be15_29102026.png?v=b198be15654c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Skeletal muscle moves the limb bones, smooth muscle lines the walls of hollow visceral organs, and cardiac muscle is found only in the heart
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Both smooth and cardiac muscle are involuntary, so a student sorting the rows on that single criterion passes (a) Skeletal - Biceps and (b) Involuntary - Intestine and then lets 'Smooth - Heart' through on the same reasoning. The heart's muscle is indeed involuntary, but it is cardiac and not smooth, so the third row fails and the whole set falls with it.
- **Why:** This question requires the stated location of each muscle type, demonstrated by the stem asking for 'the correct matching pair along with their location in human body' and by each option standing or falling as a whole set of three name and location rows.
- **Note:** E1's pattern returned statement_options, but no statement block and no standalone claim is printed: each option is a set of three muscle/location rows accepted or rejected whole, so the shape recorded here is two_part. match_columns was ruled out because no second list is printed and the answer is not a pairing code. has_figure is set and the stored image is tagged shows: question; all four options arrived as text, so nothing was missing from the record.
<!--/ecat-->

## Q179

Biology · zoology · Principles of Inheritance and Variation

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Down’s syndrome | I | $11^{\text{th}}$ chromosome |
| B | $\alpha$-Thalassemia | II | ‘X’ chromosome |
| C | $\beta$-Thalassemia | III | $21^{\text{st}}$ chromosome |
| D | Klinefelter’s syndrome | IV | $16^{\text{th}}$ chromosome |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Down’s syndrome is due to presence of an additional copy of chromosome number $21$.
2. Klinefelter’s syndrome is caused due to presence of an additional copy of $\mathrm{X}$-chromosome.
3. $\alpha$-Thalassemia is controlled by two closely linked genes on chromosome $16$ of each parent.
4. $\beta$-Thalassemia is controlled by a single gene $\mathrm{HBB}$ on chromosome $11$ of each parent.

**Solved independently** (answer withheld)

1. Down's syndrome is caused by trisomy of chromosome $21$, so $A \to III$.
2. $\alpha$-Thalassemia is controlled by the HBA1 and HBA2 genes on chromosome $16$, so $B \to IV$.
3. $\beta$-Thalassemia is controlled by the HBB gene on chromosome $11$, so $C \to I$.
4. Klinefelter's syndrome has karyotype $47,\,XXY$ (an extra $X$ chromosome), so $D \to II$.
5. $A$-$III$, $B$-$IV$, $C$-$I$, $D$-$II$ is option $3$.

**Subtopic:** Chromosomal Disorders, Thalassemia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q179_fb41132e_29102026.png?v=fb41132ed895)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q179_2dee2004_29102026.png?v=2dee20043ed9)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which chromosome each disorder sits on: trisomy of 21 in Down's syndrome, an extra X in Klinefelter's, the alpha-globin genes on 16 and the single beta-globin gene on 11
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The two thalassemia chromosomes are carried in memory as a pair, 11 and 16, without which letter owns which, and taking alpha with the smaller number gives B-I, a row only option 4 prints
- **Why:** This question requires the chromosome NCERT assigns to each named disorder, demonstrated by List II being four bare chromosome labels, the 11th, the X, the 21st and the 16th, with no symptom or mechanism printed to reason from. Test applied for the trap label: 11th chromosome and 16th chromosome bear no resemblance to each other, and the pull is that both numbers are printed together in the thalassemia paragraph, so position is the carrier and the label is nearby_fact.
- **Note:** All four codes are cyclic rotations of A-I, B-II, C-III, D-IV, so no code can hold one or two correct rows: each is either wholly right or wholly wrong. A student anchored on Down's syndrome and the 21st chromosome therefore reaches the key in one step.
<!--/ecat-->

## Q180

Biology · zoology · Breathing and Exchange of Gases

Which of the following factors are favourable for the formation of oxyhaemoglobin in alveoli?

- (1) High $\mathrm{pO_2}$ and High $\mathrm{pCO_2}$
- **(2)** High $\mathrm{pO_2}$ and Lesser $\mathrm{H^+}$ concentration
- (3) Low $\mathrm{pCO_2}$ and High $\mathrm{H^+}$ concentration
- (4) Low $\mathrm{pCO_2}$ and High temperature

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Conditions favourable for formation of oxyhaemoglobin in alveoli are high $\mathrm{pO_2}$, less $\mathrm{H^+}$ concentration low $\mathrm{pCO_2}$ and low temperature.
3. Option (1), (3) and (4) are not correct as they do not favour the formation of oxyhaemoglobin.

**Solved independently** (answer withheld)

1. In the alveoli, high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, lesser $\mathrm{H^+}$ concentration and lower temperature favour formation of oxyhaemoglobin.
2. Option $1$ includes high $\mathrm{pCO_2}$, option $3$ includes high $\mathrm{H^+}$ and option $4$ includes high temperature, each unfavourable.
3. Only option $2$ (high $\mathrm{pO_2}$ and lesser $\mathrm{H^+}$ concentration) lists two favourable factors, so the answer is option $2$.

**Subtopic:** Transport of Gases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q180_8a74470e_29102026.png?v=8a74470eedad)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q180_72100dd8_29102026.png?v=72100dd88ebe)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the alveoli high pO2, low pCO2, fewer H+ ions and lower temperature make haemoglobin bind oxygen, while the opposite set at the tissues makes it let go
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'High pO2' is the alveolar condition held first and option 1 opens with it, so the pairing is accepted on the strength of its first half. The second half is the tissue condition: carbon dioxide is being unloaded at the alveoli, so alveolar pCO2 is low, not high.
- **Why:** This question requires the printed list of alveolar conditions, demonstrated by the stem asking which 'factors are favourable for the formation of oxyhaemoglobin in alveoli' and by every option pairing two such factors that must both hold.
- **Note:** Every wrong option is built the same way: one true alveolar factor joined to one factor from the tissue side. condition_missed was considered, since the failing half is a tissue condition imported into the alveoli, but the device here is the two-part option whose true half vouches for the false one, which is what half_right names.
<!--/ecat-->

## Q181

Biology · zoology · Evolution

Given below are some stages of human evolution. Arrange them in correct sequence. (Past to Recent) Choose the correct sequence of human evolution from the options given below:

- **(A)** Homo habilis
- **(B)** Homo sapiens
- **(C)** Homo neanderthalensis
- **(D)** Homo erectus

- (1) D-A-C-B
- (2) B-A-D-C
- (3) C-B-D-A
- **(4)** A-D-C-B

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because the correct sequence of stages of human evolution from past to recent is
2. Homo habilis $\rightarrow$ Homo erectus $\rightarrow$ Homo neanderthalensis $\rightarrow$ Homo sapiens

**Solved independently** (answer withheld)

1. As NCERT teaches, the order from past to recent is $Homo\ habilis$ (A) $\rightarrow$ $Homo\ erectus$ (D) $\rightarrow$ $Homo\ neanderthalensis$ (C) $\rightarrow$ $Homo\ sapiens$ (B), which gives A-D-C-B, option $4$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 75)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q181_2ab4ea3a_29102026.png?v=2ab4ea3a4b70)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q181_8c6d1f72_29102026.png?v=8c6d1f72ba28)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The hominid line in time order: Homo habilis, then Homo erectus, then Homo neanderthalensis, with Homo sapiens most recent
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Only one adjacency is disturbed here — the two oldest species change places while the recent end still reads neanderthalensis then sapiens — and a student with Homo erectus fixed as the first named Homo, the upright one, puts it at the head and habilis second.
- **Why:** This question requires four hominids to be placed in time order, demonstrated by the instruction 'Arrange them in correct sequence. (Past to Recent)' over Homo habilis, Homo sapiens, Homo neanderthalensis and Homo erectus.
- **Note:** Label chosen under rulebook section 5.0: the printed option moves one species to the wrong stage of the sequence, which is what the retired wrong_site_or_stage named, and its live family is wrong_site_attacked. 'reversed' is excluded by its own wording, since this is one swapped pair inside a longer order.
<!--/ecat-->

## Q182

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cocaine | I | Effective sedative in surgery |
| B | Heroin | II | Cannabis sativa |
| C | Morphine | III | Erythroxylum |
| D | Marijuana | IV | Papaver somniferum |

- (1) A-IV, B-III, C-I, D-II
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-I, C-III, D-IV
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct option is (4) as
2. A. Cocaine – Obtained from plant Erythroxylum coca, stimulating action on CNS.
3. B. Heroin – Formed by the acetylation of morphine which is obtained from plant Papaver somniferum.
4. C. Morphine – Obtained from Papaver somniferum, is an effective sedative in surgery.
5. D. Marijuana – Obtained from Cannabis sativa, produces hallucinogenic effect and affects cardiovascular system of the body.

**Solved independently** (answer withheld)

1. Cocaine is obtained from the coca plant $Erythroxylum\ coca$, so $A \rightarrow III$.
2. Heroin (diacetylmorphine) is made from morphine, which comes from the latex of the poppy $Papaver\ somniferum$, so $B \rightarrow IV$.
3. Morphine is a very effective sedative and painkiller, useful for patients who have had surgery, so $C \rightarrow I$.
4. Marijuana is obtained from the inflorescences of $Cannabis\ sativa$, so $D \rightarrow II$.
5. $A-III, B-IV, C-I, D-II$ is option $4$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 75)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q182_9896e975_29102026.png?v=9896e975e01c)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q182_92c1621e_29102026.png?v=92c1621e2d8f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each drug's printed source or use: cocaine from Erythroxylum coca, heroin from the poppy Papaver somniferum, morphine as the sedative used after surgery, marijuana from Cannabis sativa
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Papaver somniferum is the plant a student ties to morphine, and row C has already spent morphine on the sedative line, so the poppy is handed to cocaine and Erythroxylum is left for heroin, which is the only code that keeps C-I and D-II while exchanging A and B
- **Why:** This question requires the source or use NCERT prints for each named drug, demonstrated by List II being three plant names and one use, Erythroxylum, Papaver somniferum, Cannabis sativa and Effective sedative in surgery. Test applied for the trap label: Erythroxylum and Papaver somniferum resemble each other in no way, and the pull is that both are printed in the same passage on drugs, so position carries the student and the label is nearby_fact.
<!--/ecat-->

## Q183

Biology · zoology · Human Reproduction

Given below are two statements: One is labelled as Assertion A and the other is labelled as Reason R: In the light of the above statements, choose the most appropriate answer from the options given below:

- **(Assertion A)** Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby.
- **(Reason R)** Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

- **(1)** Both A and R are correct and R is the correct explanation of A
- (2) Both A and R are correct but R is NOT the correct explanation of A
- (3) A is correct but R is not correct
- (4) A is not correct but R is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1)
2. Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby as colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

**Solved independently** (answer withheld)

1. Assertion A is true: doctors recommend breast-feeding in the initial period for a healthy baby.
2. Reason R is true: colostrum carries several antibodies (IgA) that build resistance in the newborn (passive immunity).
3. R explains why A is recommended, so both are correct and R is the correct explanation of A, which is option $1$.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 75)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q183_9a0eac55_29102026.png?v=9a0eac55b91e)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q183_b10941a6_29102026.png?v=b10941a6c279)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Colostrum, the first milk, carries maternal antibodies that give the newborn its early passive immunity, and that is the reason early breast-feeding is advised
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Colostrum is only the milk of the first few days while the Assertion says 'initial period of infant growth', so a student who measures the two windows against each other keeps both statements true and denies the link.
- **Why:** This question requires the reason given for early breast-feeding, demonstrated by the Reason printing 'Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby' as the candidate ground for the recommendation.
- **Note:** The retired per-option name for the hedge option here was format_reflex_option; mapped into the live axis as half_right, because option 2 is a compound verdict whose truth half holds and whose link half fails, and the route is a scope comparison rather than a reflex. No live value names an explanatory link wrongly denied, so if this recurs it is worth proposing one.
<!--/ecat-->

## Q184

Biology · zoology · Reproductive Health

Which of the following is not a natural/traditional contraceptive method?

- (1) Coitus interruptus
- (2) Periodic abstinence
- (3) Lactational amenorrhea
- **(4)** Vaults

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as
2. Vault is a barrier method of contraception which is made of rubber that is inserted into the female reproductive tract to cover the cervix during the coitus.
3. Option (1) is incorrect as coitus interruptus is a natural method of contraception in which male partner withdraws his penis from the vagina just before ejaculation so as to avoid insemination.
4. Option (2) is incorrect as periodic abstinence is also a natural method of contraception in which couples avoid coitus during the fertile period.
5. Option (3) is incorrect as lactational amenorrhea is also a natural method of contraception which is based on the fact that ovulation and therefore the cycle do not occur during the period of intense lactational following parturition.

**Solved independently** (answer withheld)

1. NCERT lists periodic abstinence, coitus interruptus and lactational amenorrhea as natural/traditional methods, while vaults (like diaphragms and cervical caps) are barrier methods, so the answer is option $4$.

**Subtopic:** Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q184_f2a6479f_29102026.png?v=f2a6479f4dba)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q184_243b6ffc_29102026.png?v=243b6ffce6fe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's natural or traditional methods are periodic abstinence, withdrawal and lactational amenorrhoea; the vault is a barrier device
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Lactational amenorrhoea is on the chapter's natural-methods list, so it is a true answer to 'which IS a natural method', and a student who reads the task without its 'not' hands that true answer in. A second route also lands here: taking 'natural' to exclude anything hormonal, since this method works by suppressing ovulation.
- **Why:** This question requires the membership of the natural-methods list, demonstrated by the stem asking which is 'not a natural/traditional contraceptive method' while 'Vaults' stands among three methods the chapter files as natural.
- **Note:** The task is negated, so the same polarity route reaches all three true options; the headline trap is placed on option 3 because a second, independent route, the reading of natural as hormone-free, also lands there.
<!--/ecat-->

## Q185

Biology · zoology · Biotechnology: Principles and Processes

The “Ti plasmid” of Agrobacterium tumefaciens stands for

- (1) Tumour inhibiting plasmid
- (2) Tumor independent plasmid
- **(3)** Tumor inducing plasmid
- (4) Temperature independent plasmid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as Ti plasmid of *Agrobacterium tumefaciens* is tumor inducing plasmid, containing T-DNA which causes tumor in several dicot plants.
2. Options (1), (2) and (4) are not correct.

**Solved independently** (answer withheld)

1. The Ti plasmid of $Agrobacterium\ tumefaciens$ transforms plant cells into tumour cells (crown gall), so Ti means Tumour inducing plasmid, which is option $3$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q185_8f0a5364_29102026.png?v=8f0a53641ba1)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q185_a2ed8a1f_29102026.png?v=a2ed8a1fb86c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Agrobacterium tumefaciens causes crown gall by delivering T-DNA from its tumour-inducing (Ti) plasmid, which biotechnology disarms and uses as a vector
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Inhibiting' and 'inducing' both expand the i of Ti and both begin 'in-', so a student holding only 'Ti has to do with tumours' picks by the wrong verb. The name comes from the wild bacterium, whose plasmid gives the plant its crown gall tumour; it is the laboratory that later disarms it.
- **Why:** This question requires the stated expansion of an abbreviation, demonstrated by the stem 'The Ti plasmid of Agrobacterium tumefaciens stands for' and by three options offering rival expansions of the same two letters.
- **Note:** Test applied for the look_alike_term against nearby_fact split: replace 'inhibiting' with an unlike word such as 'destroying' and the option no longer fits the i of Ti at all, so the resemblance between inhibiting and inducing is doing the work rather than anything printed beside it.
<!--/ecat-->

## Q186

Biology · zoology · Chemical Coordination and Integration

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Exophthalmic goiter | I | Excess secretion of cortisol, moon face & hypergylcemia. |
| B | Acromegaly | II | Hypo-secretion of thyroid hormone and stunted growth. |
| C | Cushing’s syndrome | III | Hyper secretion of thyroid hormone & protruding eye balls. |
| D | Cretinism | IV | Excessive secretion of growth hormone. |

- (1) A-I, B-III, C-II, D-IV
- (2) A-IV, B-II, C-I, D-III
- (3) A-III, B-IV, C-II, D-I
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as
2. (A) Exophthalmic goiter (III) Hyper secretion of thyroid hormone and characterized by protruding eye balls
3. (B) Acromegaly (IV) Excessive secretion of growth hormone
4. (C) Cushing’s syndrome (I) Excess secretion of cortisol, moon face and hyperglycaemia
5. (D) Cretinism (II) Hypo-secretion of thyroid hormone and characterized by stunted growth

**Solved independently** (answer withheld)

1. Exophthalmic goiter (Graves' disease) is hypersecretion of thyroid hormone with protruding eyeballs, so $A \rightarrow III$.
2. Acromegaly is caused by excessive secretion of growth hormone in adults, so $B \rightarrow IV$.
3. Cushing's syndrome is excess cortisol secretion with moon face and hyperglycaemia, so $C \rightarrow I$.
4. Cretinism is hyposecretion of thyroid hormone in infancy with stunted growth, so $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}II$ matches option $4$.

**Subtopic:** Endocrine Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q186_13fc8115_29102026.png?v=13fc8115aaa7)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q186_fb22199c_29102026.png?v=fb22199c0259)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each endocrine disorder is fixed by its gland and the direction of secretion: thyroid excess gives exophthalmic goitre, infant thyroid deficiency gives cretinism, growth-hormone excess gives acromegaly, cortisol excess gives Cushing's syndrome
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Two List II rows name their own hormone, so those pairs are settled first; option 3 agrees with both and the two leftover rows are then accepted without the gland being recalled, giving Cushing's the stunted growth and cretinism the cortisol.
- **Why:** This question requires the gland and the direction of secretion that the source states for each named disorder, demonstrated by List II offering 'Excess secretion of cortisol, moon face & hypergylcemia.' as a whole description to be attached to a row printed only as 'Cushing's syndrome'.
- **Note:** List II is printed with 'hypergylcemia' and 'goiter' in the source; tagged as printed.
<!--/ecat-->

## Q187

Biology · zoology · Cell: The Unit of Life

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements:
Statement I: Mitochondria and chloroplasts both double membranes bound organelles.
Statement II: Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.
In the light of the above statements, choose the mis appropriate answer from the options given below:

- **(Statement I)** Mitochondria and chloroplasts both double membranes bound organelles.
- **(Statement II)** Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (1) · differs

**Publisher's solution**

1. Both mitochondria and chloroplasts are double membrane bound cell organelles.
2. Transport of ions occurs across the inner membrane of mitochondria.
3. The inner membrane of chloroplast is impermeable to ions and metabolites.
4. Therefore, it is said that inner membrane of mitochondria is relatively more permeable to that of chloroplast.

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts each have an outer and an inner membrane, so Statement I is correct.
2. The mitochondrial inner membrane is highly impermeable (cristae, ETC, specific carriers needed), so it is less permeable than the chloroplast membrane system; Statement II is correct.
3. Both statements correct $\Rightarrow$ option $1$.

**Subtopic:** Plastids, Mitochondria · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 77)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q187_5b3a34af_29102026.png?v=5b3a34af80c0)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q187_6cddf3b8_29102026.png?v=6cddf3b82fc9)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Mitochondria and chloroplasts are both double membrane bound, and the textbook's 'relatively less permeable' inner membrane belongs to the chloroplast, compared against its own outer membrane
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Relatively less permeable' is the book's own phrase, so Statement II reads like a printed line; the book hangs that phrase on the inner chloroplast membrane, and the paper hangs it on the mitochondrion instead.
- **Why:** This question requires telling the two double-membrane organelles apart on a stated membrane property, demonstrated by Statement II's 'Inner membrane of mitochondria is relatively less permeable, as compared chloroplast', which places the book's chloroplast descriptor on the mitochondrion.
- **Note:** Trap axis decided by the position test rather than the likeness test: 'mitochondria' and 'chloroplast' do not resemble each other as words, so swapping them for two unlike names keeps the pull, which comes from the two organelles being described in adjacent paragraphs of the same section; hence nearby_fact, not look_alike_term. Stem carries OCR damage - 'choose the mis appropriate answer' for 'most appropriate', 'both double membranes bound organelles' for 'are both double membrane bound organelles', and 'as compared chloroplast' for 'as compared to chloroplast'. The sense is recoverable and the printed key (3) is consistent with the 'most appropriate' reading, so the question is tagged as printed. A reviewer may want to flag Statement II as arguable, since the inner mitochondrial membrane is elsewhere taught as the tightest of these membranes; the key is followed, not re-judged.
<!--/ecat-->

## Q188

Biology · zoology · Biomolecules

Regarding catalytic cycle of an enzyme action, select the correct sequential steps : Choose the correct answer from the options given below :

- **(A)** Substrate enzyme complex formation.
- **(B)** Free enzyme ready to bind with another substrate.
- **(C)** Release of products.
- **(D)** Chemical bonds of the substrate broken.
- **(E)** Substrate binding to active site.

- **(1)** E, A, D, C, B
- (2) A, E, B, D, C
- (3) B, A, C, D, E
- (4) E, D, C, B, A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) which is E, A, D, C, B.
2. The catalytic cycle of an enzyme action can be described in the following steps.
3. (1) First, the substrate binds to the active site of the enzyme, fitting into the active site.
4. (2) The binding of the substrate induces the enzyme to alter its shape, fitting more tightly around the substrate.
5. (3) The active site of the enzyme, now in close proximity of the substrate breaks the chemical bonds of the substrate and the new enzyme-product complex is formed.
6. (4) The enzyme releases the products of the reaction and the free enzyme is ready to bind to another molecule of the substrate and run through the catalytic cycle once again.
7. Options (2), (3) and (4) are incorrect as the steps mentioned are in the wrong sequence.

**Solved independently** (answer withheld)

1. The substrate first binds to the active site of the enzyme: step $E$.
2. Binding induces the enzyme to alter its shape, forming the enzyme-substrate complex: step $A$.
3. The active site, now close to the substrate, breaks the chemical bonds of the substrate, forming the enzyme-product complex: step $D$.
4. The enzyme releases the products of the reaction: step $C$.
5. The free enzyme is ready to bind another substrate and run the cycle again: step $B$.
6. Sequence $E, A, D, C, B$ matches option $1$.

**Subtopic:** Enzymes and Chemical Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 77)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q188_9f378121_29102026.png?v=9f378121eb1f)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q188_83cc94e8_29102026.png?v=83cc94e8307f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The catalytic cycle runs substrate binding, enzyme-substrate complex, bond breaking, product release, free enzyme regenerated
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  E, D, C, B keeps the four events of the cycle in the order they are taught and A is parked at the end, because 'substrate binding to active site' and 'substrate enzyme complex formation' read as one event named twice
- **Why:** This question requires the steps of one process to be put in sequence, demonstrated by the stem asking to 'select the correct sequential steps' and every option being an ordering of the same five lettered items.
- **Note:** The stem calls it a catalytic cycle while asking for a fixed sequential start; that tension is what option 3 exploits, and the key fixes the start at substrate binding to the active site.
<!--/ecat-->

## Q189

Biology · zoology · Structural Organisation in Animals

Match List I with List II related to digestive system of cockroach.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | The structures used for storing of food | I | Gizzard |
| B | Ring of 6-8 blind tubules at junction of foregut and midgut. | II | Gastric Caeca |
| C | Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut. | III | Malpighian tubules |
| D | The structures used for grinding the food. | IV | Crop |

- **(1)** A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as
2. The structure used for griding the food particles – Gizzard
3. The structure used for storing of food – Crop
4. Ring of 6-8 blind tubules at junction of foregut and midgut which assists in secretion of digestive juices – Gastric Caeca
5. Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut which assists in elimination of nitrogenous wastes – Malpighian tubules

**Solved independently** (answer withheld)

1. In cockroach the crop is the sac-like part of the foregut that stores food, so $A \to IV$.
2. A ring of $6$-$8$ blind tubules (gastric caeca) lies at the junction of foregut and midgut, so $B \to II$.
3. A ring of $100$-$150$ yellow thin filaments (Malpighian tubules) lies at the junction of midgut and hindgut, so $C \to III$.
4. The gizzard (proventriculus) has chitinous plates that grind food, so $D \to I$.
5. $A$-$IV$, $B$-$II$, $C$-$III$, $D$-$I$ is option $1$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 78)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q189_3c3992bc_29102026.png?v=3c3992bceb19)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q189_18019b2f_29102026.png?v=18019b2f0c89)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The cockroach gut gives every structure one station: the crop stores food, the gizzard grinds it, the gastric caeca ring the foregut-midgut junction and the Malpighian tubules the midgut-hindgut junction
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  Both middle rows print a ring of tubules at a gut junction, so a student holding both structures as 'a ring of tubules' without the junction each one rings hands each structure the other's junction.
- **Why:** This question requires the structure the source names at each stated station of the cockroach gut, demonstrated by rows printed as 'Ring of 6-8 blind tubules at junction of foregut and midgut.' against bare names such as 'Gizzard'.
- **Note:** The stem frames List II as the 'digestive system of cockroach' while the Malpighian tubules are excretory; the pairing is still the one the row's site describes, so the question is tagged as printed.
<!--/ecat-->

## Q190

Biology · zoology · Animal Kingdom

The following are the statements about non-chordates:
Choose the most appropriate answer from the options given below:

- **(A)** Pharynx is perforated by gill slits.
- **(B)** Notochord is absent.
- **(C)** Central nervous system is dorsal.
- **(D)** Heart is dorsal if present.
- **(E)** Post anal tail is absent.

- (1) A & C only
- (2) A, B & D only
- **(3)** B, D & E only
- (4) B, C & D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) as the features of non-chordates among the given statements are:
2. B. Notochord is absent.
3. D. Heart is dorsal if present.
4. E. Post anal tail is absent.
5. Statements A and C are features of chordates.
6. Hence, option (3) is correct and options (1), (2) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Non-chordates lack pharyngeal gill slits, so statement A is false.
2. Non-chordates lack a notochord, so statement B is true.
3. In non-chordates the central nervous system is ventral, solid and double, so statement C is false.
4. In non-chordates the heart, if present, is dorsal, so statement D is true.
5. Non-chordates have no post-anal tail, so statement E is true.
6. The true statements are $B$, $D$ and $E$, which is option $3$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 78)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q190_5e3c2ac6_29102026.png?v=5e3c2ac6bc26)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q190_6923277d_29102026.png?v=6923277d61e0)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** NCERT's chordate against non-chordate table: non-chordates have no notochord, a ventral solid nerve cord, no post-anal tail, no pharyngeal gill slits and a dorsal heart
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who has kept 'the heart is dorsal in non-chordates' attaches dorsal to the nerve cord as well and takes C in place of E, which swaps the two organs between the sides of the table
- **Why:** This question requires five characters to be sorted onto the chordate or the non-chordate side of the same comparison, demonstrated by 'Pharynx is perforated by gill slits' and 'Notochord is absent' sitting in one list where the stem names only non-chordates.
- **Note:** Statement D, 'Heart is dorsal if present', is the non-chordate entry of the printed comparison and reads against intuition; the key at option 3 is consistent with it.
<!--/ecat-->

## Q191

Biology · zoology · Excretory Products and Their Elimination

Choose the correct statement given below regarding juxta medullary nephron.

- (1) Juxta medullary nephrons are located in the columns of Bertini.
- (2) Renal corpuscle of juxta medullary nephron lies in the outer portion of the renal medulla.
- **(3)** Loop of Henle of juxta medullary nephron runs deep into medulla.
- (4) Juxta medullary nephrons outnumber the cortical nephrons.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no, (3) because the length of loop of Henle of juxta medullary nephron is longer than the length of loop of Henle of cortical nephron and runs deep into medulla.
2. Option (1) is incorrect as juxta medullary nephron are not present in columns of Bertini.
3. Option (2) is incorrect because renal corpuscle of juxta medullary nephron lies in inner cortical region.
4. Option (4) is incorrect as juxta medullary nephrons are lesser in number than cortical nephrons.

**Solved independently** (answer withheld)

1. Juxtamedullary nephrons have their renal corpuscles in the inner cortex next to the medulla (not in the columns of Bertini or the medulla), are fewer than cortical nephrons, and have very long loops of Henle that run deep into the medulla, so only option $3$ is correct.

**Subtopic:** Human Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 78)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q191_57a2cd27_29102026.png?v=57a2cd276ec0)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q191_0bb576e0_29102026.png?v=0bb576e0aef6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A juxtamedullary nephron keeps its renal corpuscle in the cortex next to the medulla and sends a long loop of Henle deep into the medulla; cortical nephrons, the majority, have short loops
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  This nephron really does reach deep into the medulla, so a student carrying 'the juxtamedullary nephron lives in the medulla' moves the whole nephron there, corpuscle included. Every renal corpuscle, in both kinds of nephron, lies in the cortex; only the loop descends.
- **Why:** This question requires the stated position of the juxtamedullary nephron's parts, demonstrated by the stem 'Choose the correct statement given below regarding juxta medullary nephron' and by the key reading 'Loop of Henle of juxta medullary nephron runs deep into medulla'.
- **Note:** asks: compare was considered, since options 2 and 4 turn on the cortical against juxtamedullary distinction, but the key is verified against one printed line about a single named nephron, so the discrimination lives in the distractors rather than in the task.
<!--/ecat-->

## Q192

Biology · zoology · Neural Control and Coordination

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- **(Statement I)** The cerebral hemispheres are connected by nerve tract known as corpus callosum.
- **(Statement II)** The brain stem consists of the medulla oblongata, pons and cerebrum.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as statement I is correct but statement II is incorrect.
2. In human brain, a deep cleft divides the cerebrum longitudinally into two halves, which are termed as the left and right cerebral hemispheres.
3. The cerebral hemispheres are connected by a tract of nerve fibres called corpus callosum.
4. Three major regions make up the brain stem i.e. mid brain, pons and medulla oblongata.
5. Cerebrum is a part of forebrain which does not form brain stem.
6. Options (1), (2) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: the two cerebral hemispheres are connected by a tract of nerve fibres called the corpus callosum, so Statement I is correct.
2. Statement II: the brain stem is formed by the midbrain, pons and medulla oblongata; the cerebrum is part of the forebrain, not the brain stem, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect is option $3$.

**Subtopic:** Forebrain, Hindbrain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 79)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q192_f5f6c3ca_29102026.png?v=f5f6c3ca5bae)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q192_0499df2d_29102026.png?v=0499df2d6091)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The brain stem is midbrain, pons and medulla oblongata; the cerebrum is forebrain and sits above the stem, and the corpus callosum is the fibre tract joining the two cerebral hemispheres
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Medulla oblongata and pons are two of the brain stem's three parts, and the third name printed is the cerebrum, a region described in the same account of the brain, so the list reads like the remembered one.
- **Why:** This question requires the stated membership of the brain stem, demonstrated by Statement II's list 'the medulla oblongata, pons and cerebrum'.
- **Note:** Trap axis decided by the position test: 'cerebrum' and 'midbrain' share no resemblance as words, so the pull survives swapping them for unlike names and comes from the cerebrum being a region named in the same description of the brain - nearby_fact, not look_alike_term. half_right was ruled out under the rule that a lone swapped name is not that label; the thing with parts here is the statement, not the option. The stem line does not reprint the two statements inline, but both are supplied in the statements block, so nothing is missing.
<!--/ecat-->

## Q193

Biology · zoology · Body Fluids and Circulation

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P wave | I | Heart muscles are electrically silent. |
| B | QRS complex | II | Depolarisation of ventricles. |
| C | T wave | III | Depolarisation of atria. |
| D | T-P gap | IV | Repolarisation of ventricles. |

- (1) A-I, B-III, C-IV, D-II
- **(2)** A-III, B-II, C-IV, D-I
- (3) A-II, B-III, C-I, D-IV
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2) as
2. A. P wave - III. Depolarisation of atria.
3. B. QRS complex - II. Depolarisation of ventricles.
4. C. T wave - IV. Repolarisation of ventricles.
5. D. T-P gap - I. Heart muscles are electrically silent.

**Solved independently** (answer withheld)

1. P wave represents depolarisation of the atria: $A \rightarrow III$.
2. QRS complex represents depolarisation of the ventricles: $B \rightarrow II$.
3. T wave represents repolarisation of the ventricles: $C \rightarrow IV$.
4. T-P gap is the period when heart muscles are electrically silent: $D \rightarrow I$.
5. $A$-$III$, $B$-$II$, $C$-$IV$, $D$-$I$ matches option $2$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 79)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q193_e89b3cc7_29102026.png?v=e89b3cc76372)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q193_f3b74452_29102026.png?v=f3b7445231ba)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each part of the ECG trace is one electrical event: P is atrial depolarisation, QRS ventricular depolarisation, T ventricular repolarisation, and the T-P gap is the silent interval between beats
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  The trace flattens once the T wave is over, so 'Heart muscles are electrically silent' is read as a description of the T wave itself, which leaves repolarisation of the ventricles to be parked on the P wave.
- **Why:** This question requires the event the source attaches to each part of the ECG trace, demonstrated by List II offering 'Heart muscles are electrically silent.' as one of the four items to be placed against bare labels such as 'T-P gap'.
- **Note:** All three wrong options are reachable by misaligning the four events with the four segments, so none of them is filler; option 4 is recorded as the trap because it keeps QRS with depolarisation of ventricles while moving the silent stretch onto the T wave.
<!--/ecat-->

## Q194

Biology · zoology · Evolution

Match List I with List II:
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Mesozoic Era | I | Lower invertebrates |
| B | Proterozoic Era | II | Fish & Amphibia |
| C | Cenozoic Era | III | Birds & Reptiles |
| D | Paleozoic Era | IV | Mammals |

- (1) A-II, B-I, C-III, D-IV
- (2) A-III, B-I, C-II, D-IV
- (3) A-I, B-II, C-IV, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4)
2. (A) Mesozoic Era – (III) Birds & Reptiles
3. (B) Proterozoic Era – (I) Lower invertebrates
4. (C) Cenozoic Era – (IV) Mammals
5. (D) Paleozoic Era – (II) Fish & Amphibia

**Solved independently** (answer withheld)

1. Mesozoic Era is the age of reptiles, with birds arising in it: $A \rightarrow III$; Proterozoic Era had lower invertebrates: $B \rightarrow I$; Cenozoic Era is the age of mammals: $C \rightarrow IV$; Paleozoic Era saw fish and amphibia: $D \rightarrow II$. So $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$, which is option $4$.

**Subtopic:** Brief Account of Evolution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 80)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q194_516021ae_29102026.png?v=516021aeb70d)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q194_ea414658_29102026.png?v=ea414658bda5)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The eras run Proterozoic, Paleozoic, Mesozoic, Cenozoic, and each is remembered by the animals that dominated it: lower invertebrates, fishes and amphibians, reptiles and birds, mammals
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The Mesozoic as the age of reptiles and the Proterozoic as the oldest era are the two pairs settled first; option 2 agrees with both and then hands the mammals to the Paleozoic, which only the prefixes Paleo- and Ceno- can rule out.
- **Why:** This question requires the dominant animal group the source assigns to each named era, demonstrated by List I printing bare era names, 'Mesozoic Era' and 'Proterozoic Era', against fauna such as 'Birds & Reptiles'.
- **Note:** The chronology of the eras gives a cross-check, but each row still asks for the era-and-fauna pairing as stated and the answer form is a pairing code, so asks is fact_line and not order.
<!--/ecat-->

## Q195

Biology · zoology · Principles of Inheritance and Variation

As per ABO blood grouping system, the blood group of father is $\mathrm{B^{+}}$, mother is $\mathrm{A^{+}}$ and child is $\mathrm{O^{+}}$. Their respective genotype can be
Choose the most appropriate answer from the options given below :

- **(A)** $\mathrm{I^{B}i/I^{A}i/ii}$
- **(B)** $\mathrm{I^{B}I^{B}/I^{A}I^{A}/ii}$
- **(C)** $\mathrm{I^{A}I^{B}/iI^{A}/I^{B}i}$
- **(D)** $\mathrm{I^{A}i/I^{B}i/I^{A}i}$
- **(E)** $\mathrm{iI^{B}/iI^{A}/I^{A}I^{B}}$

- **(1)** A only
- (2) B only
- (3) C & B only
- (4) D & E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Genotype of father with blood group $\mathrm{B^{+}}$ = $\mathrm{I^{B}i/iI^{B}}$
2. Genotype of mother with blood group $\mathrm{A^{+}}$ = $\mathrm{I^{A}i/iI^{A}}$
3. Genotype of child with blood group $\mathrm{O^{+}}$ = $\mathrm{ii}$
4. Hence only ‘A’ is correct.

**Solved independently** (answer withheld)

1. Child is blood group O, so the child's genotype is $ii$, with one $i$ allele from each parent.
2. Father is group B and carries $i$, so the father is $I^{B}i$; mother is group A and carries $i$, so the mother is $I^{A}i$.
3. A: $I^{B}i / I^{A}i / ii$ matches father, mother and child.
4. B: $I^{B}I^{B} \times I^{A}I^{A}$ can only give $I^{A}I^{B}$ children, never $ii$, so B is wrong.
5. C: father $I^{A}I^{B}$ is group AB, not B, so C is wrong; D: father $I^{A}i$ is group A, so D is wrong; E: child $I^{A}I^{B}$ is group AB, not O, so E is wrong.
6. Only A is correct, which is option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 80)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q195_4e1332e9_29102026.png?v=4e1332e9db70)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q195_fa0c9cd3_29102026.png?v=fa0c9cd3f5c5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An O child carries $\mathrm{ii}$, so each parent must hand over an $\mathrm{i}$, forcing the B father to $\mathrm{I^{B}i}$ and the A mother to $\mathrm{I^{A}i}$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Each phenotype is given its textbook genotype, $\mathrm{B}$ as $\mathrm{I^{B}I^{B}}$, $\mathrm{A}$ as $\mathrm{I^{A}I^{A}}$ and $\mathrm{O}$ as $\mathrm{ii}$, and the set is accepted because every genotype matches the blood group printed beside it, with the child's O group never used as a condition on the parents
- **Why:** This question requires the ABO inheritance rule to be applied to a stated family, demonstrated by the stem fixing father $\mathrm{B^{+}}$, mother $\mathrm{A^{+}}$ and child $\mathrm{O^{+}}$ and asking which genotype triples 'can be' theirs.
- **Note:** The lettered items are genotype triples rather than claims, but each is judged true or false of the printed family and the options select a subset, so the printed shape is a statement list.
<!--/ecat-->

## Q196

Biology · zoology · Organisms and Populations

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below :

- **(Statement I)** Gause's competitive exclusion principle states that two closely related species competing for different resources cannot exist indefinitely.
- **(Statement II)** According to Gause's principle, during competition, the inferior will be eliminated. This may be true if resources are limiting.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is true but Statement II is false.
- **(4)** Statement I is false but Statement II is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Gause's competitive exclusion principle states that two closely related species competing for the same resources cannot exist indefinitely and the competitively inferior one will be eliminated eventually.
2. This may be true if resources are limiting.

**Solved independently** (answer withheld)

1. Gause's competitive exclusion principle: two closely related species competing for the same resources cannot co-exist indefinitely and the competitively inferior one is eventually eliminated, which may be true if resources are limiting. Statement I says 'different resources', so it is false; Statement II is true, giving option $4$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 80)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q196_429d149a_29102026.png?v=429d149a4ac4)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q196_30728b5c_29102026.png?v=30728b5ce8ab)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gause's competitive exclusion principle: two closely related species competing for the same resource cannot coexist indefinitely, and the inferior competitor goes only where resources are limiting
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Statement I runs as the remembered sentence until one word, where 'different resources' stands in place of 'the same resources', inverting the very condition the principle rests on.
- **Why:** This question requires the printed wording of Gause's principle, demonstrated by Statement I's 'competing for different resources', where the principle holds of species competing for the same resources.
- **Note:** reversed was chosen over condition_missed because no rule is being applied past its condition here: the condition clause itself has been flipped to its opposite inside a quoted principle, which is an inverted relation. half_right was ruled out because the flip is a single word inside a statement, not a failing part of a multi-part option.
<!--/ecat-->

## Q197

Biology · zoology · Human Health and Disease

Given below are two statements : In the light of above statements, choose the most appropriate answer from the options given below :

- **(Statement I)** Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
- **(Statement II)** Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.

- **(1)** Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as both statements I and II are correct.
2. In humans, the bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
3. Both bone-marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes.
4. Options (2), (3) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: bone marrow is the main lymphoid organ in which all blood cells, including lymphocytes, are produced, so Statement I is correct.
2. Statement II: the textbook states that bone marrow and thymus both provide micro-environments for the development and maturation of T-lymphocytes, so Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 81)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q197_0e15663d_29102026.png?v=0e15663d6cb3)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q197_73e3543e_29102026.png?v=73e3543e5dd2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bone marrow and thymus are the primary lymphoid organs: the marrow produces all blood cells including lymphocytes, and both organs supply the micro-environment in which T-lymphocytes develop and mature
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The sharper fact printed alongside - T-lymphocytes mature in the thymus, B-lymphocytes in the bone marrow - is reached for, and it makes a true statement about both organs look like a misattribution.
- **Why:** This question requires the stated roles of the two primary lymphoid organs, demonstrated by Statement II's 'Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes'.
- **Note:** Trap axis decided by the position test: 'bone marrow' and 'thymus' are unlike words, so the pull is not resemblance but the adjacent printed fact about where T cells mature - nearby_fact, not look_alike_term. half_right was ruled out because no part of Statement II fails; the question works the other way round, with a correct two-part statement made to look part-wrong.
<!--/ecat-->

## Q198

Biology · zoology · Structural Organisation in Animals

Match List I with List II: Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Unicellular glandular epithelium | I | Salivary glands |
| B | Compound epithelium | II | Pancreas |
| C | Multicellular glandular epithelium | III | Goblet cells of alimentary canal |
| D | Endocrine glandular epithelium | IV | Moist surface of buccal cavity |

- (1) A-II, B-I, C-III, D-IV
- (2) A-IV, B-III, C-I, D-II
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) as
2. A. Unicellular glandular epithelium — (III) Goblet cells of alimentary canal
3. B. Compound epithelium — (IV) Lines moist surface of buccal cavity
4. C. Multicellular glandular epithelium — (I) Salivary glands
5. D. Endocrine glandular epithelium — (II) Pancreas

**Solved independently** (answer withheld)

1. Unicellular glandular epithelium is the isolated goblet cells of the alimentary canal, so $A \rightarrow III$.
2. Compound epithelium covers the moist surface of the buccal cavity, so $B \rightarrow IV$.
3. Multicellular glandular epithelium forms clusters of cells such as the salivary glands, so $C \rightarrow I$.
4. Endocrine glandular epithelium releases hormones; the pancreas (islets) is the endocrine match, so $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}II$ is option $3$.

**Subtopic:** Animal Tissues: Epithelial Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 81)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q198_5fd217c8_29102026.png?v=5fd217c86e5e)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q198_71cec7a6_29102026.png?v=71cec7a6a3ba)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An epithelium's name carries its own criterion: compound counts layers and is protective, unicellular glandular is a single secreting cell, multicellular glandular is a ducted gland, endocrine glandular has no duct
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Compound' is read as compounded of many cells, which is what 'Multicellular' two rows below actually means, so the goblet cells scattered through the canal lining go to the compound row and the unicellular row is left with the buccal surface.
- **Why:** This question requires the criterion printed in each List I entry applied to a named example, demonstrated by rows reading 'Unicellular glandular epithelium' and 'Multicellular glandular epithelium', whose own words decide which of 'Goblet cells of alimentary canal' and 'Salivary glands' belongs where. On the trap axis the resemblance test was applied: replace 'Compound epithelium' with 'stratified protective epithelium' and the pull dies, so the likeness of 'compound' to 'multicellular' is doing the work and the label is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q199

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II:
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | RNA polymerase III | I | snRNPs |
| B | Termination of transcription | II | Promotor |
| C | Splicing of Exons | III | Rho factor |
| D | TATA box | IV | SnRNAs, tRNA |

- (1) A-II, B-IV, C-I, D-III
- (2) A-III, B-II, C-IV, D-I
- (3) A-III, B-IV, C-I, D-II
- **(4)** A-IV, B-III, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In eukaryotes, RNA polymerase III codes for snRNAs, tRNA and 5s rRNA.
2. Splicing of exons is performed by snRNPs.
3. TATA box is present in promoter region of transcription unit.
4. Rho factor is responsible for termination of transcription.

**Solved independently** (answer withheld)

1. RNA polymerase III transcribes tRNA, 5S rRNA and snRNAs, so $A \rightarrow IV$.
2. In prokaryotes the Rho factor ends transcription, so $B \rightarrow III$.
3. snRNPs in the spliceosome remove introns and join the exons, so $C \rightarrow I$.
4. The TATA box is part of the promoter, so $D \rightarrow II$.
5. $A$-IV, $B$-III, $C$-I, $D$-II matches option $4$.

**Subtopic:** Transcription · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 82)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q199_2a5cc33d_29102026.png?v=2a5cc33dda25)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q199_e0c019a1_29102026.png?v=e0c019a1812f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Transcription divides its labour: RNA polymerase III makes tRNA and snRNA, the TATA box lies inside the promoter, rho factor terminates transcription, and snRNPs splice out the introns
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  'RNA polymerase binds the promoter' is a true sentence about any polymerase, so a student who has not fixed which RNAs polymerase III makes attaches it to 'Promotor', and the TATA box is then left with the rho factor.
- **Why:** This question requires the partner the source states for each item of the transcription machinery, demonstrated by List I printing bare names, 'RNA polymerase III' and 'TATA box', to be joined to items such as 'Rho factor'.
- **Note:** Printed as 'Promotor' and 'SnRNAs' in the source; the near-identical printing of 'snRNPs' and 'SnRNAs' in List II is what the option-2 proof turns on. Tagged as printed.
<!--/ecat-->

## Q200

Biology · zoology · Human Reproduction

Identify the correct option (A), (B), (C), (D) with respect to spermatogenesis.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q200_86f8ab27_29102026.png?v=86f8ab278953)

- **(1)** FSH, Leydig cells, Sertoli cells, spermiogenesis.
- (2) ICSH, Interstitial cells, Leydig cells, spermiogenesis.
- (3) FSH, Sertoli cells, Leydig cells, spermatogenesis.
- (4) ICSH, Leydig cells, Sertoli cells, spermatogenesis.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/figures_agent/q200_sol_1_7f556532_29102026.png?v=7f5565325a7b)

2. (A) is $\mathrm{FSH}$ which is a pituitary hormone.
3. (B) is Leydig cells which are found in the interstitial space outside of the seminiferous tubules.
4. (C) is Sertoli cells are found inside the seminiferous tubules.
5. (D) is Spermiogenesis which is a process that helps in transformation of spermatids into spermatozoa.

**Solved independently** (answer withheld)

1. GnRH from the hypothalamus stimulates the pituitary to release two gonadotropins, $\text{LH}$ and $\text{FSH}$, so the right-hand branch $(A) = \text{FSH}$.
2. $\text{LH}$ acts on the Leydig (interstitial) cells, which secrete androgens, so $(B) = $ Leydig cells.
3. $\text{FSH}$ acts on the Sertoli cells, which secrete factors that help spermatogenesis, so $(C) = $ Sertoli cells.
4. Androgens drive the formation of spermatids; the Sertoli-cell factors then aid the conversion of spermatids to sperms, so $(D) = $ spermiogenesis.
5. The sequence FSH, Leydig cells, Sertoli cells, spermiogenesis is option $1$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Hormonal Regulation of Reproduction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 82)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/crops/q200_8fa6873e_29102026.png?v=8fa6873e54bf)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2024/2024_Q4/solutions/q200_8e78d187_29102026.png?v=8e78d1876af5)

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** LH acts on the Leydig cells and FSH on the Sertoli cells, and the Sertoli factors assist spermiogenesis, the shaping of spermatids into spermatozoa, not the whole of spermatogenesis
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Spermiogenesis and spermatogenesis differ by three letters and the stem itself prints the second one, so a student who has both cell types in the right slots still closes the set with 'spermatogenesis' and names the testis gonadotropin ICSH. ICSH is LH's own male name rather than the second gonadotropin, and spermiogenesis is only the spermatid-to-spermatozoa step, so the set fails at its first and last terms while looking right in the middle.
- **Why:** This question requires the hormone, cell and stage names the textbook states for spermatogenesis to be supplied in every slot of one bundled set, demonstrated by the four options differing only in 'FSH' against 'ICSH', 'Leydig cells' against 'Sertoli cells' and 'spermatogenesis' against 'spermiogenesis'; swapping those twin terms for two unlike words kills the pull, so likeness rather than printed position is doing the work and the label is look_alike_term, not nearby_fact.
- **Note:** The lettered items (A) to (D) are not in the text we hold: the record carries a question image with shows='question', which this step cannot open, so slot order was not inspected and every route is written from the four printed term sets and the printed key, which are complete. A reviewer holding the image should confirm which blank each term fills. E1 called this statement_options on '15 full-statement options', which does not match the printed shape here: the options are four-term sets accepted or rejected whole, not full statements, so qtype is recorded as two_part, with the remark that the bundle has four members rather than two. The look-alike discrimination between Leydig and Sertoli and between spermiogenesis and spermatogenesis is carried by the trap field; asks stays fact_line because each slot wants a name the textbook states.
<!--/ecat-->

