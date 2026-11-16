# NEET (UG) 2023 · Code F1

200 questions · source `NEET_Papers/2023/Set_F1/NEET_2023_Question_Paper_F1.pdf` · every image a CDN link (0 without one) · 47 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Rotational Motion

> ⚠ The independent solve found no printed option exactly right ("which no option shows"); its pick (4) is the closest fit, so treat this question as possibly misprinted.

The ratio of radius of gyration of a solid sphere of mass $M$ and radius $R$ about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is

- (1) $5 : 3$
- (2) $2 : 5$
- (3) $5 : 2$
- **(4)** $3 : 5$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For a solid sphere, $I_1 = \frac{2}{5}MR^2$, so $k_1 = R\sqrt{\frac{2}{5}}$.
2. For a thin hollow sphere, $I_2 = \frac{2}{3}MR^2$, so $k_2 = R\sqrt{\frac{2}{3}}$.
3. $\frac{k_1}{k_2} = \sqrt{\frac{2/5}{2/3}} = \sqrt{\frac{3}{5}} = \sqrt{3} : \sqrt{5}$.
4. No option shows $\sqrt{3} : \sqrt{5}$; option $4$ ($3 : 5$) has the right numbers and is the intended answer if the square roots were lost.

**Subtopic:** Radius of Gyration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q001_de7233f6_02112026.png?v=de7233f66872)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Radius of gyration is $k=\sqrt{I/M}$, so comparing a solid sphere ($I=\frac{2}{5}MR^2$) with a thin shell ($I=\frac{2}{3}MR^2$) means comparing square roots, not the coefficients themselves
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The two coefficients $\frac{2}{5}$ and $\frac{2}{3}$ divided in the order they were written down, shell over sphere, give $\frac{2/3}{2/5}=\frac{5}{3}$, which is the printed ratio turned the other way up.
- **Why:** This question requires two stored moments of inertia turned into radii of gyration and divided in the stem's order, demonstrated by the stem asking for "the ratio of radius of gyration of a solid sphere ... to the radius of gyration of the thin hollow sphere of same mass and radius".
- **Note:** The key is tagged as printed, and a doubt is recorded rather than acted on: $k=\sqrt{I/M}$, so the ratio of the two radii of gyration is $\sqrt{3}:\sqrt{5}$, while the printed option 4, $3:5$, is the ratio of $k^2$ (equivalently of the two moments of inertia). No option carries $\sqrt{3}:\sqrt{5}$, so the key is the only available choice and the labels follow it; a reviewer should log this as a square root dropped in the question rather than in the key.
<!--/ecat-->

## Q2

Physics · Modern Physics

The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are $2.14\,\mathrm{eV}$, $2.30\,\mathrm{eV}$ and $2.75\,\mathrm{eV}$ respectively. If incident electromagnetic radiation has an incident energy of $2.20\,\mathrm{eV}$, which of these photosensitive surfaces may emit photoelectrons?

- (1) Both Na and K
- (2) K only
- (3) Na only
- **(4)** Cs only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Photoelectrons are emitted only if $E_{photon} \geq \phi$.
2. Cs: $\phi = 2.14\,\mathrm{eV} < 2.20\,\mathrm{eV}$, so Cs emits.
3. K: $\phi = 2.30\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so K does not emit.
4. Na: $\phi = 2.75\,\mathrm{eV} > 2.20\,\mathrm{eV}$, so Na does not emit.
5. Only Cs emits, which is option $4$.

**Subtopic:** Photoelectric Effect · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q002_d4d17274_02112026.png?v=d4d1727446a7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Photoemission needs the photon energy to reach or exceed the work function, so only the surface whose work function lies below the incident energy emits
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Reading the threshold as "the work function must exceed the photon energy" admits exactly the two surfaces whose printed values sit above $2.20\,\mathrm{eV}$, K at $2.30$ and Na at $2.75$, which is option 1 complete.
- **Why:** This question requires the threshold condition applied to three supplied work functions with no quantity produced, demonstrated by the stem "If incident electromagnetic radiation has an incident energy of $2.20\,\mathrm{eV}$, which of these photosensitive surfaces may emit photoelectrons?" against the printed $2.14$, $2.30$ and $2.75\,\mathrm{eV}$.
<!--/ecat-->

## Q3

Physics · Mechanical Properties of Fluids

The amount of energy required to form a soap bubble of radius $2\,\mathrm{cm}$ from a soap solution is nearly (surface tension of soap solution $= 0.03\,\mathrm{N\,m^{-1}}$)

- (1) $5.06 \times 10^{-4}\,\mathrm{J}$
- **(2)** $3.01 \times 10^{-4}\,\mathrm{J}$
- (3) $50.1 \times 10^{-4}\,\mathrm{J}$
- (4) $30.16 \times 10^{-4}\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A soap bubble has two free surfaces, so the area created is $A = 2 \times 4\pi r^2 = 8\pi r^2$.
2. $r = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$, so $r^2 = 4 \times 10^{-4}\,\mathrm{m^2}$.
3. $A = 8\pi \times 4 \times 10^{-4} = 32\pi \times 10^{-4}\,\mathrm{m^2} \approx 1.005 \times 10^{-2}\,\mathrm{m^2}$.
4. $W = T A = 0.03 \times 1.005 \times 10^{-2} \approx 3.016 \times 10^{-4}\,\mathrm{J}$.
5. $3.01 \times 10^{-4}\,\mathrm{J}$ is option $2$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q003_943459b7_02112026.png?v=943459b7270e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Making a bubble creates two liquid surfaces, so the energy needed is $W = T\,\Delta A = 2T(4\pi r^2)$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Squaring the converted radius as $0.02^2 = 0.004$ instead of $0.0004$ loses one power of ten, and $2 \times 0.03 \times 4\pi \times 0.004 = 30.16 \times 10^{-4}\,\mathrm{J}$ is printed.
- **Why:** This question requires surface energy computed over two surfaces from the stem's numbers, demonstrated by "The amount of energy required to form a soap bubble of radius $2\,\mathrm{cm}$" with the surface tension supplied as $0.03\,\mathrm{N\,m^{-1}}$.
<!--/ecat-->

## Q4

Physics · Current Electricity

Resistance of a carbon resistor determined from colour codes is $(22000 \pm 5\%)\,\Omega$. The colour of third band must be

- (1) Green
- **(2)** Orange
- (3) Yellow
- (4) Red

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Write the value as two significant digits times a power of ten: $22000\,\Omega = 22 \times 10^{3}\,\Omega$.
2. The first two bands give the digits $2, 2$, and the third band gives the multiplier $10^{3}$.
3. In the colour code, multiplier $3$ is orange, so the third band is orange, option $2$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q004_1c03e9fc_02112026.png?v=1c03e9fcde1c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In the carbon resistor code the first two bands are the two significant figures and the third is the power of ten, so $22000\,\Omega = 22 \times 10^{3}$ needs the colour for 3
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Writing $22000$ in the usual one-digit form $2.2 \times 10^{4}$ and reading that exponent as the third band gives the colour for 4, yellow, instead of the colour for 3.
- **Why:** This question requires the colour code convention applied to a given resistance, demonstrated by the stem "Resistance of a carbon resistor determined from colour codes is $(22000 \pm 5\%)\,\Omega$. The colour of third band must be" with four colours as options.
- **Note:** All four options are multiplier colours - green 5, orange 3, yellow 4, red 2 - so the whole spread is a choice of exponent. Our stored stem reads $22000\,\Omega$, which gives $22 \times 10^{3}$ and the printed key, orange; no digit is missing here.
<!--/ecat-->

## Q5

Physics · Alternating Current

In a series $LCR$ circuit, the inductance $L$ is $10\,\mathrm{mH}$, capacitance $C$ is $1\,\mu\mathrm{F}$ and resistance $R$ is $100\,\Omega$. The frequency at which resonance occurs is

- (1) $15.9\,\mathrm{kHz}$
- (2) $1.59\,\mathrm{rad/s}$
- **(3)** $1.59\,\mathrm{kHz}$
- (4) $15.9\,\mathrm{rad/s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Resonance in a series $LCR$ circuit occurs at $\omega_0 = \frac{1}{\sqrt{LC}}$, independent of $R$.
2. $LC = (10 \times 10^{-3}\,\mathrm{H})(1 \times 10^{-6}\,\mathrm{F}) = 10^{-8}\,\mathrm{s^2}$.
3. $\sqrt{LC} = 10^{-4}\,\mathrm{s}$, so $\omega_0 = 10^{4}\,\mathrm{rad/s}$.
4. $f_0 = \frac{\omega_0}{2\pi} = \frac{10^4}{2\pi} \approx 1591.5\,\mathrm{Hz} = 1.59\,\mathrm{kHz}$, which is option $3$.

**Subtopic:** Resonance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q005_73c8a300_02112026.png?v=73c8a3005eca)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Series resonance sits at $f = \frac{1}{2\pi\sqrt{LC}}$, and the resistance has no part in it
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  With $\sqrt{LC} = 10^{-4}$, the division $\frac{1}{2\pi \times 10^{-4}}$ comes out as $0.159 \times 10^{4}$, and writing that as $1.59 \times 10^{4}$ instead of $1.59 \times 10^{3}$ leaves the decimal one place out, giving $15.9\,\mathrm{kHz}$.
- **Why:** This question requires a number computed from the resonance relation and the stem's component values, demonstrated by "the inductance $L$ is $10\,\mathrm{mH}$, capacitance $C$ is $1\,\mu\mathrm{F}$" and the question "The frequency at which resonance occurs is".
- **Note:** The resistance $R = 100\,\Omega$ is supplied and enters no step of the resonant frequency; it affects the sharpness, not the position, of resonance.
<!--/ecat-->

## Q6

Physics · Electromagnetic Waves

In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of $2.0 \times 10^{10}\,\mathrm{Hz}$ and amplitude $48\,\mathrm{V\,m^{-1}}$. Then the amplitude of oscillating magnetic field is (Speed of light in free space $= 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$)

- (1) $1.6 \times 10^{-8}\,\mathrm{T}$
- **(2)** $1.6 \times 10^{-7}\,\mathrm{T}$
- (3) $1.6 \times 10^{-6}\,\mathrm{T}$
- (4) $1.6 \times 10^{-9}\,\mathrm{T}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For a plane EM wave in free space the field amplitudes are related by $B_0 = \frac{E_0}{c}$.
2. $B_0 = \frac{48\,\mathrm{V\,m^{-1}}}{3 \times 10^{8}\,\mathrm{m\,s^{-1}}} = 16 \times 10^{-8}\,\mathrm{T}$.
3. $16 \times 10^{-8}\,\mathrm{T} = 1.6 \times 10^{-7}\,\mathrm{T}$, which is option $2$.

**Subtopic:** Relation Between E, B, and Speed of Light · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q006_91eb6d50_02112026.png?v=91eb6d50dc96)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a plane electromagnetic wave the two field amplitudes are tied by $B_0 = E_0/c$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $\frac{48}{3 \times 10^{8}}$ is worked as $16 \times 10^{-8}$, and rewriting that as $1.6 \times 10^{-8}$ moves the digit without paying for it with the exponent.
- **Why:** This question requires a number computed from the field-amplitude relation and the supplied constants, demonstrated by "amplitude $48\,\mathrm{V\,m^{-1}}$" with "Speed of light in free space $= 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$" given in the stem.
- **Note:** The stated frequency $2.0 \times 10^{10}\,\mathrm{Hz}$ is surplus to the computation; all four options share the digits $1.6$ and differ only in the power of ten.
<!--/ecat-->

## Q7

Physics · Semiconductor Electronics

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Photovoltaic devices can convert optical radiation into electricity.
- (Statement II) Zener diode is designed to operate under reverse bias in breakdown region.

- (1) Both Statement I and Statement II are incorrect
- (2) Statement I is correct but Statement II is incorrect
- (3) Statement I is incorrect but Statement II is correct
- **(4)** Both Statement I and Statement II are correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: a photovoltaic device such as a solar cell generates an emf when optical radiation falls on it, so it converts light into electricity; Statement I is correct.
2. Statement II: a Zener diode is heavily doped and is designed to operate under reverse bias in the breakdown region (used as a voltage regulator); Statement II is correct.
3. Both statements are correct, which is option $4$.

**Subtopic:** Special Purpose PN Junction Diodes · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 2)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q007_0aec1e77_02112026.png?v=0aec1e778ce3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A photovoltaic cell turns incident light into electrical energy, while a Zener diode is built so that reverse breakdown is its normal working region.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The ordinary p-n junction's reverse characteristic, where breakdown current rises sharply and can damage the diode, is carried onto the Zener, so Statement II reads as describing a forbidden operating region and is marked incorrect.
- **Why:** This question requires two stored facts about named semiconductor devices to be judged one at a time, demonstrated by Statement I naming 'Photovoltaic devices' and Statement II naming 'Zener diode', two devices that share no quantity or relation.
<!--/ecat-->

## Q8

Physics · Units and Measurements

The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are

- (1) Personal errors
- (2) Least count errors
- **(3)** Random errors
- (4) Instrumental errors

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT defines random errors as those that occur irregularly and arise from unpredictable fluctuations in experimental conditions such as temperature and voltage supply, so the answer is option $3$.

**Subtopic:** Errors in Measurement · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q008_e7f72853_02112026.png?v=e7f7285345b3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Random errors are the ones that come from irregular, unpredictable changes in the experimental conditions, as against systematic errors, which have a fixed cause and a fixed sign
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The voltage supply is a piece of the apparatus, so a student who files an error by the object named in its cause puts it with the instrument and picks the class printed beside random errors in the same list.
- **Why:** This question requires the printed definition of one error class recognised from its own stated cause, demonstrated by the stem "errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply", which reproduces the chapter's example of random errors.
<!--/ecat-->

## Q9

Physics · Electrostatics

If $\oint_{s} \vec{E} \cdot \overrightarrow{dS} = 0$ over a surface, then

- (1) The magnitude of electric field on the surface is constant
- (2) All the charges must necessarily be inside the surface
- (3) The electric field inside the surface is necessarily uniform
- **(4)** The number of flux lines entering the surface must be equal to the number of flux lines leaving it

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. By Gauss's law, $\oint_s \vec{E}\cdot d\vec{S} = \frac{q_{enc}}{\varepsilon_0}$.
2. Given the flux is $0$, so $q_{enc} = 0$; charges may be outside, so option $2$ is wrong.
3. Zero net flux does not require $|\vec{E}|$ constant on the surface or $\vec{E}$ uniform inside, so options $1$ and $3$ are wrong.
4. Net flux $= \Phi_{out} - \Phi_{in} = 0 \Rightarrow \Phi_{in} = \Phi_{out}$: lines entering equal lines leaving, which is option $4$.

**Subtopic:** Electric Flux · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q009_6101ec67_02112026.png?v=6101ec6781c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A closed-surface integral of $\vec{E}$ is the NET flux, so its vanishing says the inward and outward flux cancel and the enclosed net charge is zero - it says nothing about the field at any one point
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  In every worked Gauss problem the surface is chosen so that $|\vec{E}|$ is constant on it and $\oint \vec{E}\cdot d\vec{S}$ becomes $EA$, so a student reading the printed integral recalls that assumption and takes it to be what the equation states.
- **Why:** This question requires Gauss's law applied to a stated condition with no quantity produced, demonstrated by the stem "If $\oint_{s} \vec{E} \cdot \overrightarrow{dS} = 0$ over a surface, then" and four rival consequences as options.
- **Note:** E1 called this statement_options because each option is a full sentence; under the rule that long sentences as options do not make a question a statements item - no lettered block is printed and the stem does not ask for statements to be judged - it is recorded as mcq.
<!--/ecat-->

## Q10

Physics · Current Electricity

If the galvanometer $G$ does not show any deflection in the circuit shown, the value of $R$ is given by

![printed figure: Two cells 10 V and 2 V with 400 ohm, R and galvanometer G](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q010_02781c8c_02112026.png?v=02781c8c7041)

*Two cells 10 V and 2 V with 400 ohm, R and galvanometer G*

![drawn: Two cells 10 V and 2 V with 400 ohm, R and galvanometer G](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_drawn/q010_question_d07b944a_03112026.svg?v=d07b944a8c51)  
*drawn by code/lib/physics_figure.py*

- (1) $50\,\Omega$
- **(2)** $100\,\Omega$
- (3) $400\,\Omega$
- (4) $200\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. With no deflection in $G$, no current flows through the $2\,\text{V}$ branch, so the potential difference across $R$ equals $2\,\text{V}$.
2. The $10\,\text{V}$ cell then drives current only through $400\,\Omega$ and $R$ in series: $I = \frac{10}{400 + R}$.
3. $V_R = IR = \frac{10R}{400 + R} = 2$.
4. $10R = 800 + 2R \Rightarrow 8R = 800 \Rightarrow R = 100\,\Omega$, which is option $2$.

**Subtopic:** Kirchhoff's Laws of Current Distribution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q010_062fca47_02112026.png?v=062fca473c81)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A galvanometer branch with no deflection carries no current, so the $2\,\mathrm{V}$ cell's emf equals the drop the $10\,\mathrm{V}$ cell produces across $R$: $\frac{10R}{400+R} = 2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  No deflection is the balance phrase from the Wheatstone bridge, and a student who applies the bridge condition concludes the two resistances must match, which reads the printed $400\,\Omega$ straight off the figure.
- **Why:** This question requires a resistance computed from a loop in the supplied circuit, demonstrated by the stem "If the galvanometer $G$ does not show any deflection in the circuit shown, the value of $R$ is given by" with the figure supplying $10\,\mathrm{V}$, $2\,\mathrm{V}$ and $400\,\Omega$.
- **Note:** The figure was supplied to this step as a drawn spec with a netlist, so the circuit could be read: the $10\,\mathrm{V}$ cell drives $400\,\Omega$ and $R$ in series, and the $2\,\mathrm{V}$ cell sits in the galvanometer branch across $R$.
<!--/ecat-->

## Q11

Physics · Alternating Current

An ac source is connected to a capacitor $C$. Due to decrease in its operating frequency

- (1) Displacement current increases
- **(2)** Displacement current decreases
- (3) Capacitive reactance remains constant
- (4) Capacitive reactance decreases

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Capacitive reactance is $X_C = \frac{1}{2\pi f C}$.
2. As $f$ decreases, $X_C$ increases, ruling out options $3$ and $4$.
3. Conduction current $I = \frac{V}{X_C}$ therefore decreases.
4. The displacement current between the plates equals the conduction current, $I_d = I$, so $I_d$ decreases, which is option $2$.

**Subtopic:** Variation of Reactance with Frequency · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q011_b08da5b0_02112026.png?v=b08da5b0db06)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Capacitive reactance is $X_C = \frac{1}{2\pi f C}$, so lowering the frequency raises the reactance and the displacement current, which equals the conduction current, falls
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Carrying "reactance grows with frequency" across from the inductor makes a drop in frequency look like a drop in reactance, and the current then has to rise.
- **Why:** This question requires the frequency dependence of capacitive reactance applied to a stated change with no quantity produced, demonstrated by the stem "An ac source is connected to a capacitor $C$. Due to decrease in its operating frequency" and options that name only a direction of change.
<!--/ecat-->

## Q12

Physics · Modern Physics

The minimum wavelength of $X$-rays produced by an electron accelerated through a potential difference of $V$ volts is proportional to

- **(1)** $\frac{1}{V}$
- (2) $\frac{1}{\sqrt{V}}$
- (3) $V^{2}$
- (4) $\sqrt{V}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The shortest wavelength comes from an electron that gives all of its kinetic energy $eV$ to a single photon: $eV = \frac{hc}{\lambda_{min}}$.
2. $\lambda_{min} = \frac{hc}{eV}$, so $\lambda_{min} \propto \frac{1}{V}$, which is option $1$.

**Subtopic:** Continuous and Characteristic X-Ray Spectra · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q012_83ba8ac0_02112026.png?v=83ba8ac07517)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The cut-off wavelength of the continuous X-ray spectrum comes from the whole electron energy going to one photon, $eV = \frac{hc}{\lambda_{\min}}$, so $\lambda_{\min} \propto \frac{1}{V}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $\lambda \propto \frac{1}{\sqrt{V}}$ is a real and much-practised result - the de Broglie wavelength of an electron accelerated through $V$ volts - and the stem's wording, a wavelength and an accelerating potential, matches that problem almost word for word.
- **Why:** This question requires how one quantity moves with another rather than any number, demonstrated by the stem "The minimum wavelength of $X$-rays produced by an electron accelerated through a potential difference of $V$ volts is proportional to" with four powers of $V$ as options.
<!--/ecat-->

## Q13

Physics · Mechanical Properties of Fluids

The venturi-meter works on

- **(1)** Bernoulli’s principle
- (2) The principle of parallel axes
- (3) The principle of perpendicular axes
- (4) Huygens’s principle

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A venturi-meter measures flow speed from the pressure difference between its wide section and its throat; by continuity $A_1 v_1 = A_2 v_2$ and Bernoulli's principle $P_1 - P_2 = \frac{1}{2}\rho (v_2^2 - v_1^2)$, so it works on Bernoulli's principle, which is option $1$.

**Subtopic:** Venturi Tube and Aspirator Pump Problems · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q013_4b0e0cea_02112026.png?v=4b0e0cea4cb7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The venturi-meter measures flow speed from a pressure difference between a wide and a narrow section, which is Bernoulli's principle used as a device
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the stem's single noun: two of them are the moment-of-inertia theorems from rotational motion and the third is the wavefront construction from wave optics. None of the three mentions pressure, speed or flow, and the venturi-meter is defined in the fluids chapter with no reference to any of them, so no remembered fact about the instrument reaches them.
- **Why:** This question requires the principle named as a stored fact about a named instrument, demonstrated by the whole stem being "The venturi-meter works on" with no quantity supplied to apply anything to.
- **Note:** Three fillers on one question is unusual, so the options were re-examined: the wrong three come from two chapters the venturi-meter appears in neither of, and the only likeness among them is between options 2 and 3, which resemble each other rather than the answer. The finding stands as no_trap.
<!--/ecat-->

## Q14

Physics · Semiconductor Electronics

A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?

- (1) p-n junction diodes
- **(2)** Capacitor
- (3) Load resistance
- (4) A centre-tapped transformer

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The capacitor placed across the load acts as a filter: it charges to the peak voltage and discharges slowly through the load between peaks, removing the ac ripple, so the answer is option $2$.

**Subtopic:** Use of PN Junction Diode as Rectifier · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q014_70352b6f_02112026.png?v=70352b6f0754)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a rectifier the diodes turn the ac into a one-way output and the capacitor across the load is the filter, charging at the peaks and discharging between them to flatten the ripple
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The diodes are what get rid of the reversed half of the ac, so a student who reads "remove the ac" as the rectifying job names them, where the stem asks what cleans the already rectified output.
- **Why:** This question requires the stated function of one named part of a named circuit, demonstrated by the stem listing the parts and asking "Which of these components remove the ac ripple from the rectified output?"
<!--/ecat-->

## Q15

Physics · Units and Measurements

A metal wire has mass $(0.4 \pm 0.002)\,\mathrm{g}$, radius $(0.3 \pm 0.001)\,\mathrm{mm}$ and length $(5 \pm 0.02)\,\mathrm{cm}$. The maximum possible percentage error in the measurement of density will nearly be

- (1) $1.3\%$
- **(2)** $1.6\%$
- (3) $1.4\%$
- (4) $1.2\%$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Density of a wire: $\rho = \frac{m}{\pi r^2 l}$.
2. Maximum fractional error: $\frac{\Delta \rho}{\rho} = \frac{\Delta m}{m} + 2\frac{\Delta r}{r} + \frac{\Delta l}{l}$.
3. $\frac{\Delta m}{m} = \frac{0.002}{0.4} = 0.005 = 0.5\%$.
4. $2\frac{\Delta r}{r} = 2 \times \frac{0.001}{0.3} = 0.00667 = 0.667\%$.
5. $\frac{\Delta l}{l} = \frac{0.02}{5} = 0.004 = 0.4\%$.
6. $\frac{\Delta \rho}{\rho} = 0.5\% + 0.667\% + 0.4\% = 1.567\% \approx 1.6\%$, which is option $2$.

**Subtopic:** Errors in Measurement · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q015_60e64b04_02112026.png?v=60e64b04633c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Fractional errors add, and a quantity raised to a power carries its power as a multiplier: for $\rho = \frac{m}{\pi r^2 l}$ the percentage error is $\frac{\Delta m}{m} + 2\frac{\Delta r}{r} + \frac{\Delta l}{l}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Adding the three fractional errors without doubling the radius term gives $0.5\% + 0.33\% + 0.4\% = 1.23\%$, which is the printed $1.2\%$.
- **Why:** This question requires a percentage error computed from the stem's measurements, demonstrated by "mass $(0.4 \pm 0.002)\,\mathrm{g}$, radius $(0.3 \pm 0.001)\,\mathrm{mm}$ and length $(5 \pm 0.02)\,\mathrm{cm}$" with the density asked for.
- **Note:** Two of the three wrong options are fillers here, which is unusual; the four options form a tight comb ($1.2$, $1.3$, $1.4$, $1.6$) and only $1.2\%$ and the key fall out of the stem's numbers, so the finding is recorded rather than smoothed over.
<!--/ecat-->

## Q16

Physics · Wave Optics

For Young’s double slit experiment, two statements are given below: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) If screen is moved away from the plane of slits, angular separation of the fringes remains constant.
- (Statement II) If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases.

- (1) Both Statement I and Statement II are false.
- **(2)** Statement I is true but Statement II is false.
- (3) Statement I is false but Statement II is true.
- (4) Both Statement I and Statement II are true.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Angular separation of fringes in YDSE is $\theta = \frac{\beta}{D} = \frac{\lambda}{d}$.
2. $\theta$ does not depend on $D$, so moving the screen away leaves it constant: Statement I is true.
3. $\theta \propto \lambda$, so a larger wavelength increases the angular separation: Statement II is false.
4. Statement I true, Statement II false is option $2$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q016_8fdd7649_02112026.png?v=8fdd7649f8c5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Angular fringe separation in Young's experiment is $\lambda/d$: the screen distance does not appear in it, and the separation grows with wavelength.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The linear fringe width $\beta = \lambda D/d$ is used where the stem says angular separation, so moving the screen away appears to widen the fringes and Statement I reads false, while the same relation correctly makes Statement II false.
- **Why:** This question requires the angular separation's dependence on each of two quantities in turn, demonstrated by Statement I moving only the screen and Statement II changing only the wavelength, each asking which way the separation moves.
- **Note:** `asks` is `relation` rather than `fact_line` because each statement changes one quantity and asks which way a second one moves; the other member of this group is two stored device facts and is tagged `fact_line`.
<!--/ecat-->

## Q17

Physics · Work, Energy and Power

The potential energy of a long spring when stretched by $2\,\mathrm{cm}$ is $U$. If the spring is stretched by $8\,\mathrm{cm}$, potential energy stored in it will be

- (1) $4\,U$
- (2) $8\,U$
- **(3)** $16\,U$
- (4) $2\,U$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Spring potential energy is $U = \frac{1}{2}kx^2$, so $U \propto x^2$.
2. $\frac{U'}{U} = \left(\frac{8\,\mathrm{cm}}{2\,\mathrm{cm}}\right)^2 = 4^2 = 16$.
3. $U' = 16\,U$, which is option $3$.

**Subtopic:** Potential Energy of Spring · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q017_227dbbd6_02112026.png?v=227dbbd6fff3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Spring potential energy goes as the square of the extension, $U = \frac{1}{2}kx^2$, so quadrupling the stretch multiplies the energy by sixteen
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The extension goes from $2\,\mathrm{cm}$ to $8\,\mathrm{cm}$, a factor of 4, and stopping at that factor instead of squaring it gives $4U$.
- **Why:** This question requires how many times one quantity changes when another does, demonstrated by "The potential energy of a long spring when stretched by $2\,\mathrm{cm}$ is $U$" with the options given as multiples of $U$ rather than as energies.
<!--/ecat-->

## Q18

Physics · Ray Optics

Light travels a distance $x$ in time $t_1$ in air and $10x$ in time $t_2$ in another denser medium. What is the critical angle for this medium?

- (1) $\sin^{-1}\left(\frac{10t_2}{t_1}\right)$
- (2) $\sin^{-1}\left(\frac{t_1}{10\,t_2}\right)$
- **(3)** $\sin^{-1}\left(\frac{10\,t_1}{t_2}\right)$
- (4) $\sin^{-1}\left(\frac{t_2}{t_1}\right)$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Speed of light in air: $c = \frac{x}{t_1}$.
2. Speed of light in the medium: $v = \frac{10x}{t_2}$.
3. Refractive index: $n = \frac{c}{v} = \frac{x/t_1}{10x/t_2} = \frac{t_2}{10\,t_1}$.
4. Critical angle: $\sin C = \frac{1}{n} = \frac{10\,t_1}{t_2}$, so $C = \sin^{-1}\left(\frac{10\,t_1}{t_2}\right)$, which is option $3$.

**Subtopic:** Total Internal Reflection (TIR) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q018_591cd377_02112026.png?v=591cd37752ff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The refractive index is the ratio of the two speeds, each got from its own distance and time, and the critical angle follows from $\sin C = \frac{1}{n}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Reading "$10x$ in time $t_2$" as $x$ in time $10t_2$ puts the factor 10 on the time instead of the distance, so $n = \frac{10t_2}{t_1}$ and $\sin C$ comes out as $\frac{t_1}{10t_2}$ - the key with the 10 moved across the line.
- **Why:** This question requires an expression built from the stem's symbols through two relations, demonstrated by "Light travels a distance $x$ in time $t_1$ in air and $10x$ in time $t_2$ in another denser medium" with the answer wanted as a critical angle.
<!--/ecat-->

## Q19

Physics · Alternating Current

A $12\,\mathrm{V}$, $60\,\mathrm{W}$ lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of $220\,\mathrm{V}$. Assuming the transformer to be ideal, what is the current in the primary winding?

- (1) $2.7\,\mathrm{A}$
- (2) $3.7\,\mathrm{A}$
- (3) $0.37\,\mathrm{A}$
- **(4)** $0.27\,\mathrm{A}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For an ideal transformer, power in the primary equals power in the secondary: $P_p = P_s = 60\,\mathrm{W}$.
2. $I_p = \frac{P_p}{V_p} = \frac{60\,\mathrm{W}}{220\,\mathrm{V}}$.
3. $I_p \approx 0.27\,\mathrm{A}$, which is option $4$.

**Subtopic:** Transformer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q019_545e25cb_02112026.png?v=545e25cba7c9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An ideal transformer passes the power through unchanged, so the primary current is the lamp's power divided by the primary voltage
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Dividing the two printed numbers the other way up, $\frac{220}{60}$, gives $3.7\,\mathrm{A}$ instead of $\frac{60}{220} = 0.27\,\mathrm{A}$.
- **Why:** This question requires a current computed from the stem's power and voltage, demonstrated by "A $12\,\mathrm{V}$, $60\,\mathrm{W}$ lamp ... primary is connected to ac mains of $220\,\mathrm{V}$" with the primary current asked for.
<!--/ecat-->

## Q20

Physics · Laws of Motion

A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is

- (1) Along northward
- **(2)** Along north-east
- (3) Along south-west
- (4) Along eastward

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Take east as $\hat{i}$ and north as $\hat{j}$; initial velocity $\vec{v}_1 = -v\hat{j}$ (southward).
2. Final velocity $\vec{v}_2 = v\hat{i}$ (eastward, same speed).
3. $\Delta\vec{v} = \vec{v}_2 - \vec{v}_1 = v\hat{i} + v\hat{j}$.
4. $\vec{F} \propto \Delta\vec{p} = m\Delta\vec{v}$, which is directed at $45^\circ$ between east and north, i.e. north-east, option $2$.

**Subtopic:** Newton's Second Law as Change in Momentum · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q020_db72f4e4_02112026.png?v=db72f4e43f67)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Force points along the CHANGE in velocity, so turning from southward to eastward at the same speed needs a force along east plus north, i.e. north-east
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  East is where the player ends up going, so a student who takes the force to lie along the motion rather than along the change in motion reads the new direction of travel off the stem.
- **Why:** This question requires Newton's second law in its change-of-momentum form applied to a described turn, with a sense rather than a magnitude as the answer, demonstrated by "turns eastward with the same speed" and four compass directions as options.
- **Note:** The speed is unchanged, so no quantity is produced and the whole answer is a direction; that is why this is apply_rule and not calculate, even though a vector subtraction is carried out.
<!--/ecat-->

## Q21

Physics · Current Electricity

The magnitude and direction of the current in the following circuit is

![printed figure: Loop ABCD with 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm on top and 7 ohm on the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q021_bc3db65f_02112026.png?v=bc3db65fc6b3)

*Loop ABCD with 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm on top and 7 ohm on the bottom*

![drawn: Loop ABCD with 2 ohm, 10 V cell, junction E, 5 V cell, 1 ohm on top and 7 ohm on the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q021_question_8ca7c8b7_02112026.svg?v=8ca7c8b706f7)  
*drawn by code/lib/physics_figure.py*

- **(1)** $0.5\,\mathrm{A}$ from $A$ to $B$ through $E$
- (2) $\frac{5}{9}\,\mathrm{A}$ from $A$ to $B$ through $E$
- (3) $1.5\,\mathrm{A}$ from $B$ to $A$ through $E$
- (4) $0.2\,\mathrm{A}$ from $B$ to $A$ through $E$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The two cells are in series but opposing (like terminals meet at $E$), so $E_{net} = 10\,\mathrm{V} - 5\,\mathrm{V} = 5\,\mathrm{V}$.
2. All resistors are in one loop: $R_{total} = 2\,\Omega + 1\,\Omega + 7\,\Omega = 10\,\Omega$.
3. $I = \frac{E_{net}}{R_{total}} = \frac{5}{10} = 0.5\,\mathrm{A}$.
4. The current direction is set by the larger $10\,\mathrm{V}$ cell, flowing from $A$ to $B$ through $E$; only option $1$ has $0.5\,\mathrm{A}$.

**Subtopic:** Combination of Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q021_41c4eb62_02112026.png?v=41c4eb62b03c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a single loop the two cells that face each other subtract, and the current is the net emf divided by the sum of every resistance in the loop
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Leaving one resistor out of the series sum turns $2+1+7 = 10\,\Omega$ into $9\,\Omega$, and the option prints the result of that unreduced, $\frac{5}{9}\,\mathrm{A}$, with the key's own direction attached.
- **Why:** This question requires a current computed from the supplied loop, demonstrated by the figure's $10\,\mathrm{V}$ and $5\,\mathrm{V}$ cells with $2\,\Omega$, $1\,\Omega$ and $7\,\Omega$ in one loop and the stem asking for "The magnitude and direction of the current".
- **Note:** Each option bundles a magnitude with a direction, so half_right was weighed for option 2; the direction it prints is the key's own, so what catches a student is the resistor missing from the sum rather than a part-right compound claim, and arithmetic_slip names that. E1 called this statement_options because the options are phrases; the printed shape is one question with four options, so it is recorded as mcq. The figure was supplied as a drawn spec with a netlist and could be read.
<!--/ecat-->

## Q22

Physics · Rotational Motion

The angular acceleration of a body, moving along the circumference of a circle, is

- (1) Along the radius towards the centre
- (2) Along the tangent to its position
- **(3)** Along the axis of rotation
- (4) Along the radius, away from centre

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$, and for motion on a fixed circle $\vec{\omega}$ lies along the axis of rotation, so $\vec{\alpha}$ is along the axis of rotation, which is option $3$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q022_67df9975_02112026.png?v=67df99759d20)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Angular velocity and angular acceleration are axial vectors: they lie along the axis of rotation, not in the plane the body moves in
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Inward along the radius is the direction of the centripetal acceleration, so a student who answers for the acceleration they associate with circular motion gives a true direction for the wrong quantity.
- **Why:** This question requires the stored direction convention for an axial vector, demonstrated by the stem "The angular acceleration of a body, moving along the circumference of a circle, is" with no magnitude, radius or rate supplied to work with.
<!--/ecat-->

## Q23

Physics · Kinematics

A bullet is fired from a gun at the speed of $280\,\mathrm{m\,s^{-1}}$ in the direction $30^\circ$ above the horizontal. The maximum height attained by the bullet is ($g = 9.8\,\mathrm{m\,s^{-2}}$, $\sin 30^\circ = 0.5$)

- (1) $2000\,\mathrm{m}$
- **(2)** $1000\,\mathrm{m}$
- (3) $3000\,\mathrm{m}$
- (4) $2800\,\mathrm{m}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Maximum height of a projectile: $H = \frac{u^2 \sin^2\theta}{2g}$.
2. Vertical component: $u\sin\theta = 280 \times 0.5 = 140\,\mathrm{m\,s^{-1}}$.
3. $H = \frac{(140)^2}{2 \times 9.8} = \frac{19600}{19.6} = 1000\,\mathrm{m}$, which is option $2$.

**Subtopic:** Maximum Height Reached · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q023_3ae8b56c_02112026.png?v=3ae8b56c5ef2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Maximum height in projectile motion uses the vertical component squared: $H = \frac{u^2\sin^2\theta}{2g}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Two separate single-step slips both land on $2000\,\mathrm{m}$: using the supplied $\sin 30^\circ = 0.5$ without squaring it, or dividing by $g$ instead of $2g$.
- **Why:** This question requires a height computed from the stem's speed, angle and constants, demonstrated by "fired ... at the speed of $280\,\mathrm{m\,s^{-1}}$ in the direction $30^\circ$ above the horizontal" with $g$ and $\sin 30^\circ$ supplied.
<!--/ecat-->

## Q24

Physics · Magnetic Effect of Electric Current

The net magnetic flux through any closed surface is

- (1) Positive
- (2) Infinity
- (3) Negative
- **(4)** Zero

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Gauss's law for magnetism (no isolated magnetic poles) gives $\oint \vec{B} \cdot d\vec{A} = 0$, so the net flux is zero, which is option $4$.

**Subtopic:** Magnetism and Gauss's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q024_86633ac6_02112026.png?v=86633ac61217)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** There are no magnetic monopoles, so every field line that enters a closed surface leaves it and the net magnetic flux through any closed surface is zero
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Treating a magnetic pole as a magnetic charge and carrying $\oint \vec{E}\cdot d\vec{S} = \frac{q}{\varepsilon_0}$ across to magnetism makes a surface drawn round a north pole look like a surface round a positive charge, with a net outward flux.
- **Why:** This question requires a stated law recalled as it stands, demonstrated by the whole stem being "The net magnetic flux through any closed surface is" with no field, surface or current supplied.
<!--/ecat-->

## Q25

Physics · Capacitance

The equivalent capacitance of the system shown in the following circuit is

![printed figure: A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q025_4824645c_02112026.png?v=4824645cde32)

*A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B*

![drawn: A 3 uF capacitor in series with two 3 uF capacitors in parallel between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q025_question_07892dab_02112026.svg?v=07892dab19a2)  
*drawn by code/lib/physics_figure.py*

- (1) $3\,\mu\mathrm{F}$
- (2) $6\,\mu\mathrm{F}$
- (3) $9\,\mu\mathrm{F}$
- **(4)** $2\,\mu\mathrm{F}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The two $3\,\mu\mathrm{F}$ capacitors between the junction and $B$ are in parallel: $C_p = 3 + 3 = 6\,\mu\mathrm{F}$.
2. This combination is in series with the $3\,\mu\mathrm{F}$ capacitor from $A$: $C_{eq} = \frac{3 \times 6}{3 + 6}$.
3. $C_{eq} = \frac{18}{9} = 2\,\mu\mathrm{F}$, which is option $4$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q025_49b0014a_02112026.png?v=49b0014a3717)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Capacitors in parallel add, capacitors in series add as reciprocals, and a network has to be reduced inwards to outwards: $3\,\mu\mathrm{F}$ in series with $3+3 = 6\,\mu\mathrm{F}$ gives $2\,\mu\mathrm{F}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $6\,\mu\mathrm{F}$ is the true capacitance of the parallel pair, so stopping at the first reduction answers for part of the network instead of for $A$ to $B$.
- **Why:** This question requires a capacitance computed by reducing the supplied network, demonstrated by the figure's three $3\,\mu\mathrm{F}$ capacitors with two sharing the nodes $M$ and $B$, and the stem asking for "The equivalent capacitance of the system shown".
- **Note:** The figure was supplied as a drawn spec with a netlist, so the series-parallel arrangement could be read directly.
<!--/ecat-->

## Q26

Physics · Kinematics

A vehicle travels half the distance with speed $v$ and the remaining distance with speed $2v$. Its average speed is

- (1) $\frac{2v}{3}$
- **(2)** $\frac{4v}{3}$
- (3) $\frac{3v}{4}$
- (4) $\frac{v}{3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Let total distance be $d$; each half is $\frac{d}{2}$.
2. $t_1 = \frac{d/2}{v} = \frac{d}{2v}$.
3. $t_2 = \frac{d/2}{2v} = \frac{d}{4v}$.
4. $t = t_1 + t_2 = \frac{3d}{4v}$.
5. $v_{avg} = \frac{d}{t} = \frac{4v}{3}$, which is option $2$.

**Subtopic:** Average Speed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q026_368ef8a4_02112026.png?v=368ef8a434dc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average speed is total distance over total time, so equal distances at two speeds give the harmonic mean $\frac{2v_1v_2}{v_1+v_2}$, never the arithmetic one
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Averaging the reciprocals gives $\frac{1}{v_{av}} = \frac{1}{2}\left(\frac{1}{v}+\frac{1}{2v}\right) = \frac{3}{4v}$, and reading that line off as $\frac{3v}{4}$ reports the reciprocal of the answer as the answer.
- **Why:** This question requires an expression computed from distance and time rather than a factor of change, demonstrated by "travels half the distance with speed $v$ and the remaining distance with speed $2v$" and options that are fractions of $v$.
<!--/ecat-->

## Q27

Physics · Modern Physics

The half life of a radioactive substance is $20$ minutes. In how much time, the activity of substance drops to $\left(\frac{1}{16}\right)^{\mathrm{th}}$ of its initial value?

- (1) $40$ minutes
- (2) $60$ minutes
- **(3)** $80$ minutes
- (4) $20$ minutes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Activity after $n$ half-lives: $\frac{A}{A_0} = \left(\frac{1}{2}\right)^n$.
2. $\frac{1}{16} = \left(\frac{1}{2}\right)^4 \Rightarrow n = 4$.
3. $t = n\,T_{1/2} = 4 \times 20\,\text{min} = 80\,\text{min}$, which is option $3$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q027_770705dc_02112026.png?v=770705dc4011)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each half-life multiplies the activity by $\frac{1}{2}$, so $\frac{1}{16} = \left(\frac{1}{2}\right)^4$ takes four of them
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Writing the chain as $\frac{1}{2} \to \frac{1}{4} \to \frac{1}{8} \to \frac{1}{16}$ and counting the steps between the fractions on the page gives three half-lives, because the first halving from the full activity is not on the list.
- **Why:** This question requires a time computed from the decay law and the given half-life, demonstrated by "The half life of a radioactive substance is $20$ minutes" with the activity asked to fall to $\left(\frac{1}{16}\right)^{\mathrm{th}}$.
<!--/ecat-->

## Q28

Physics · Kinetic Theory of Gases

The temperature of a gas is $-50^\circ\mathrm{C}$. To what temperature the gas should be heated so that the rms speed is increased by 3 times?

- **(1)** $3295^\circ\mathrm{C}$
- (2) $3097\,\mathrm{K}$
- (3) $223\,\mathrm{K}$
- (4) $669^\circ\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $T = -50 + 273 = 223\,\mathrm{K}$.
2. $v_{rms} = \sqrt{\frac{3RT}{M}} \propto \sqrt{T}$.
3. Increased by 3 times: $v' = v + 3v = 4v$.
4. $\frac{T'}{T} = \left(\frac{v'}{v}\right)^2 = 16$.
5. $T' = 16 \times 223\,\mathrm{K} = 3568\,\mathrm{K}$.
6. $T' = 3568 - 273 = 3295^\circ\mathrm{C}$, which is option $1$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q028_8f6a46b5_02112026.png?v=8f6a46b5aef1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The rms speed goes as $\sqrt{T}$ in kelvin, so multiplying the speed by a factor multiplies the absolute temperature by the square of it
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Taking the temperature to follow the speed directly instead of its square multiplies $223\,\mathrm{K}$ by 3 to give $669$, and the option prints that number with a Celsius sign on it.
- **Why:** This question requires a temperature computed from the square dependence of rms speed, demonstrated by "The temperature of a gas is $-50^\circ\mathrm{C}$" with the rms speed to be "increased by 3 times".
- **Note:** The key follows the paper's reading of "increased by 3 times" as a fourfold rms speed: $16 \times 223\,\mathrm{K} = 3568\,\mathrm{K} = 3295^\circ\mathrm{C}$, which is option 1 exactly. The other reading, $v_2 = 3v_1$, gives $2007\,\mathrm{K} = 1734^\circ\mathrm{C}$, which is not printed in any form, so the stem's wording is loose but the key is the only option the arithmetic reaches. Recorded, not re-judged.
<!--/ecat-->

## Q29

Physics · Thermodynamics

A Carnot engine has an efficiency of $50\%$ when its source is at a temperature $327^{\circ}\mathrm{C}$. The temperature of the sink is

- (1) $15^{\circ}\mathrm{C}$
- (2) $100^{\circ}\mathrm{C}$
- (3) $200^{\circ}\mathrm{C}$
- **(4)** $27^{\circ}\mathrm{C}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Convert the source temperature to kelvin: $T_1 = 327 + 273 = 600\,\mathrm{K}$.
2. Carnot efficiency: $\eta = 1 - \frac{T_2}{T_1}$.
3. $0.5 = 1 - \frac{T_2}{600} \Rightarrow T_2 = 300\,\mathrm{K}$.
4. $T_2 = 300 - 273 = 27^{\circ}\mathrm{C}$, which is option $4$.

**Subtopic:** Carnot Engine · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q029_310b339d_02112026.png?v=310b339d85ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Carnot efficiency is $1 - \frac{T_{\text{sink}}}{T_{\text{source}}}$ with both temperatures in kelvin, so a 50% engine has a sink at half the source's absolute temperature
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked every value the stem's numbers reach: the source is $600\,\mathrm{K}$, the sink $300\,\mathrm{K} = 27^\circ\mathrm{C}$ (the key), and the same problem worked wrongly in Celsius gives $\frac{327}{2} = 163.5^\circ\mathrm{C}$, which is not printed. Because the efficiency is exactly 50%, even inverting the ratio to $\eta = \frac{T_2}{T_1}$ returns the same $300\,\mathrm{K}$, so that error produces no option either. The three wrong options are everyday temperatures that no step of the formula yields.
- **Why:** This question requires a temperature computed from the Carnot efficiency relation, demonstrated by "an efficiency of $50\%$ when its source is at a temperature $327^{\circ}\mathrm{C}$" with the sink asked for.
- **Note:** Three fillers, so the options were re-examined: the one classic error here - leaving the temperatures in Celsius - gives $163.5^\circ\mathrm{C}$, which the paper does not print, and the 50% figure makes the inverted-ratio error invisible. That is why this question carries no trap.
<!--/ecat-->

## Q30

Physics · Electromagnetic Induction

The magnetic energy stored in an inductor of inductance $4\,\mu\mathrm{H}$ carrying a current of $2\,\mathrm{A}$ is

- (1) $4\,\mathrm{mJ}$
- (2) $8\,\mathrm{mJ}$
- **(3)** $8\,\mu\mathrm{J}$
- (4) $4\,\mu\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$.
2. $U = \frac{1}{2} \times (4 \times 10^{-6}\,\mathrm{H}) \times (2\,\mathrm{A})^2$.
3. $U = \frac{1}{2} \times 4 \times 10^{-6} \times 4 = 8 \times 10^{-6}\,\mathrm{J}$.
4. $8 \times 10^{-6}\,\mathrm{J} = 8\,\mu\mathrm{J}$, which is option $3$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q030_0be8aef3_02112026.png?v=0be8aef33e6e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The energy stored in an inductor is $\frac{1}{2}LI^2$, with the current squared
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Using $\frac{1}{2}LI$ in place of $\frac{1}{2}LI^2$ gives $\frac{1}{2}(4\,\mu\mathrm{H})(2\,\mathrm{A}) = 4\,\mu\mathrm{J}$, with the prefix handled correctly.
- **Why:** This question requires an energy computed from the stored-energy relation and the given values, demonstrated by "an inductor of inductance $4\,\mu\mathrm{H}$ carrying a current of $2\,\mathrm{A}$".
<!--/ecat-->

## Q31

Physics · Mechanical Properties of Solids

Let a wire be suspended from the ceiling (rigid support) and stretched by a weight $W$ attached at its free end. The longitudinal stress at any point of cross-sectional area $A$ of the wire is

- **(1)** $W/A$
- (2) $W/2A$
- (3) Zero
- (4) $2W/A$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Neglecting the wire's own mass, equilibrium of the hanging weight gives tension $T = W$ at every cross-section of the wire.
2. Longitudinal stress $= \frac{T}{A} = \frac{W}{A}$, which is option $1$.

**Subtopic:** Stress and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q031_952645eb_02112026.png?v=952645ebeb03)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Longitudinal stress is the tension across a section divided by its area, and in a wire loaded at one end the tension at every section is the load itself
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Counting both the hanging weight and the ceiling's equal reaction as forces that stretch the wire doubles the numerator and gives $\frac{2W}{A}$.
- **Why:** This question requires the definition of stress applied to a described loading with no numbers supplied, demonstrated by "stretched by a weight $W$" and "The longitudinal stress at any point of cross-sectional area $A$", where the phrase "at any point" is what has to be acted on.
<!--/ecat-->

## Q32

Physics · Electrostatics

An electric dipole is placed at an angle of $30^{\circ}$ with an electric field of intensity $2 \times 10^{5}\,\mathrm{N\,C^{-1}}$. It experiences a torque equal to $4\,\mathrm{N\,m}$. Calculate the magnitude of charge on the dipole, if the dipole length is $2\,\mathrm{cm}$.

- (1) $6\,\mathrm{mC}$
- (2) $4\,\mathrm{mC}$
- **(3)** $2\,\mathrm{mC}$
- (4) $8\,\mathrm{mC}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Torque on a dipole: $\tau = pE\sin\theta = qlE\sin\theta$.
2. Rearrange: $q = \frac{\tau}{lE\sin\theta}$.
3. $q = \frac{4}{(0.02)(2\times10^{5})(0.5)} = \frac{4}{2000}$.
4. $q = 2\times10^{-3}\,\mathrm{C} = 2\,\mathrm{mC}$, which is option $3$.

**Subtopic:** Torque and Work Done in Rotating Dipole in Uniform Electric Field · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q032_057699f9_02112026.png?v=057699f96379)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Torque on a dipole is $pE\sin\theta$, and the dipole moment is the charge times the FULL separation, so $q = \frac{\tau}{E\sin\theta \cdot l}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Taking the printed $2\,\mathrm{cm}$ as twice the charge separation and dividing the dipole moment by $0.01\,\mathrm{m}$ instead of $0.02\,\mathrm{m}$ doubles the charge to $4\,\mathrm{mC}$.
- **Why:** This question requires a charge computed from the torque relation and the stem's values, demonstrated by "It experiences a torque equal to $4\,\mathrm{N\,m}$" with the field, the angle and "the dipole length is $2\,\mathrm{cm}$" all supplied.
<!--/ecat-->

## Q33

Physics · Modern Physics

In hydrogen spectrum, the shortest wavelength in the Balmer series is $\lambda$. The shortest wavelength in the Bracket series is

- **(1)** $4\lambda$
- (2) $9\lambda$
- (3) $16\lambda$
- (4) $2\lambda$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The shortest wavelength of a series is its series limit, $n_2 \to \infty$, so $\frac{1}{\lambda_{min}} = \frac{R}{n_1^2}$.
2. Balmer ($n_1 = 2$): $\frac{1}{\lambda} = \frac{R}{4}$, so $\lambda = \frac{4}{R}$.
3. Brackett ($n_1 = 4$): $\frac{1}{\lambda'} = \frac{R}{16}$, so $\lambda' = \frac{16}{R}$.
4. $\frac{\lambda'}{\lambda} = \frac{16}{4} = 4$, so $\lambda' = 4\lambda$, which is option $1$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q033_09b97f20_02112026.png?v=09b97f205ba2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The shortest wavelength of a hydrogen series is its limit, $\lambda_{min} = n_1^2/R$, so it grows as the square of the lower level
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The series limit is $\lambda = n_1^2/R$ and Brackett's lower level is $n_1 = 4$, so the factor is read straight off as $4^2 = 16$. The $\lambda$ the stem supplies is itself $4/R$, so the honest ratio is $16/4 = 4$.
- **Why:** This question requires the $n_1^2$ dependence of a series limit turned into a factor, demonstrated by the options being bare multiples of $\lambda$ -- "$4\lambda$", "$16\lambda$" -- with no wavelength in metres anywhere in the stem.
- **Note:** The stem spells the series "Bracket"; the Brackett series ($n_1 = 4$) is plainly meant and the key is consistent with that reading.
<!--/ecat-->

## Q34

Physics · Waves

The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is

- **(1)** $2:1$
- (2) $1:3$
- (3) $3:1$
- (4) $1:2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Fundamental of an open pipe: $f_o = \frac{v}{2L}$.
2. Fundamental of a closed pipe: $f_c = \frac{v}{4L}$.
3. $\frac{f_o}{f_c} = \frac{v/2L}{v/4L} = 2$, so the ratio is $2:1$, which is option $1$.

**Subtopic:** Organ Pipe · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q034_513ba636_02112026.png?v=513ba636347b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** An open pipe's fundamental is $v/2L$ and a closed pipe's is $v/4L$, so at equal length the open pipe sounds at twice the frequency
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Both fundamentals are recalled correctly, $v/2L$ and $v/4L$, and the ratio is then read off the denominators 2 and 4 as $1:2$. Dividing instead of reading gives $(v/2L) \div (v/4L) = 2$, and the stem asks open first.
- **Why:** This question requires the open and closed pipe fundamentals compared as a factor, demonstrated by the stem asking for "the ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length" while supplying neither a length nor a speed of sound.
<!--/ecat-->

## Q35

Physics · Gravitation

Two bodies of mass $m$ and $9m$ are placed at a distance $R$. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be ($G$ = gravitational constant)

- (1) $-\dfrac{12Gm}{R}$
- **(2)** $-\dfrac{16Gm}{R}$
- (3) $-\dfrac{20Gm}{R}$
- (4) $-\dfrac{8Gm}{R}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At the null point a distance $x$ from $m$: $\frac{Gm}{x^2} = \frac{G(9m)}{(R-x)^2}$.
2. Taking square roots: $R - x = 3x$, so $x = \frac{R}{4}$.
3. Distance from $9m$ is $R - \frac{R}{4} = \frac{3R}{4}$.
4. $V = -\frac{Gm}{R/4} - \frac{G(9m)}{3R/4} = -\frac{4Gm}{R} - \frac{12Gm}{R}$.
5. $V = -\frac{16Gm}{R}$, which is option $2$.

**Subtopic:** Calculation of Gravitational Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q035_4a4a28a1_02112026.png?v=4a4a28a13e7a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field-free point between two masses sits nearer the lighter one ($R/4$ from $m$), and potential there is a scalar sum of two negative terms, not zero
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $-20Gm/R$ is the true potential at the midpoint of the joining line, $-2Gm/R - 18Gm/R$, taken by a student who picks the obvious point on that line instead of solving for the one where the field cancels. That point is at $R/4$ from $m$, where the sum is $-16Gm/R$.
- **Why:** This question requires the field-null point located and the two potentials then added as scalars, demonstrated by the stem embedding "where the gravitational field equals zero" inside a question that asks for the potential.
<!--/ecat-->

## Q36

Physics · Kinematics

A bullet from a gun is fired on a rectangular wooden block with velocity $u$. When bullet travels $24\,\mathrm{cm}$ through the block along its length horizontally, velocity of bullet becomes $\frac{u}{3}$. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is

- (1) $24\,\mathrm{cm}$
- (2) $28\,\mathrm{cm}$
- (3) $30\,\mathrm{cm}$
- **(4)** $27\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Assume uniform retardation $a$ inside the block and apply $v^2 = u^2 - 2as$ to the first $24\,\mathrm{cm}$.
2. $u^2 - \left(\frac{u}{3}\right)^2 = 2a(24) \Rightarrow \frac{8u^2}{9} = 48a$.
3. $2a = \frac{8u^2}{9 \times 24} = \frac{u^2}{27}$.
4. For the remaining distance $x$ the bullet goes from $\frac{u}{3}$ to rest: $\left(\frac{u}{3}\right)^2 = 2a x$.
5. $\frac{u^2}{9} = \frac{u^2}{27} x \Rightarrow x = 3\,\mathrm{cm}$.
6. Total length $L = 24 + 3 = 27\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Third Equation of Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q036_04fb529c_02112026.png?v=04fb529cf071)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Under constant retardation the distance travelled goes with the square of the speed lost, so dropping from $u$ to $u/3$ uses $8/9$ of the stopping distance
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  24 cm is the distance the stem has already measured -- the run over which the speed fell to $u/3$ -- and the closing words put the bullet at the far end of the block, so the two get read as the same length. The last $u/3$ still costs 3 cm, making the block 27 cm.
- **Why:** This question requires $v^2 = u^2 - 2as$ applied twice under one retardation, demonstrated by "then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block".
<!--/ecat-->

## Q37

Physics · Modern Physics

The radius of inner most orbit of hydrogen atom is $5.3 \times 10^{-11}\,\mathrm{m}$. What is the radius of third allowed orbit of hydrogen atom?

- (1) $1.06\,\mathrm{\AA}$
- (2) $1.59\,\mathrm{\AA}$
- **(3)** $4.77\,\mathrm{\AA}$
- (4) $0.53\,\mathrm{\AA}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the Bohr model $r_n = n^2 r_1$.
2. $r_3 = 3^2 \times 5.3 \times 10^{-11}\,\mathrm{m} = 4.77 \times 10^{-10}\,\mathrm{m}$.
3. $4.77 \times 10^{-10}\,\mathrm{m} = 4.77\,\mathrm{\AA}$, which is option $3$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q037_8dfa5b48_02112026.png?v=8dfa5b48bfef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bohr orbit radii grow as the square of the quantum number, $r_n = n^2 r_1$, so the third orbit is nine times the innermost
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  $r_n = n^2 r_1$ carried as "the radius grows with the orbit number" turns the third orbit into $3 \times 0.53 = 1.59$ Å. The square is what the Bohr model demands, giving $9 \times 0.53 = 4.77$ Å.
- **Why:** This question requires $r_n = n^2 r_1$ evaluated at $n = 3$, demonstrated by the stem supplying "the radius of inner most orbit" and asking for "the radius of third allowed orbit".
<!--/ecat-->

## Q38

Physics · Laws of Motion

Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is $0.15$ ($g = 10\,\mathrm{m\,s^{-2}}$).

- (1) $150\,\mathrm{m\,s^{-2}}$
- **(2)** $1.5\,\mathrm{m\,s^{-2}}$
- (3) $50\,\mathrm{m\,s^{-2}}$
- (4) $1.2\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. To stay at rest relative to the car, the body must accelerate with the car, and only static friction can supply that force: $ma \le f_{s,\max} = \mu_s m g$.
2. Cancel $m$: $a_{\max} = \mu_s g$.
3. $a_{\max} = 0.15 \times 10 = 1.5\,\mathrm{m\,s^{-2}}$, which is option $2$.

**Subtopic:** Static Friction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q038_8caeaf68_02112026.png?v=8caeaf68f19a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A body rides with the car only while the force needed stays inside limiting static friction, so $a_{max} = \mu_s g$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $a_{max} = \mu_s g$ is set up correctly and then evaluated with $g$ in cm s$^{-2}$, $0.15 \times 1000 = 150$, or with the coefficient read as 15 instead of 0.15. On the stem's own $g = 10$ m s$^{-2}$ the product is $1.5$ m s$^{-2}$.
- **Why:** This question requires limiting static friction converted into a maximum acceleration, demonstrated by the stem's "so that a body lying on the floor of the car remains stationary" with only $\mu$ and $g$ supplied.
<!--/ecat-->

## Q39

Physics · Current Electricity

$10$ resistors, each of resistance $R$ are connected in series to a battery of emf $E$ and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased $n$ times. The value of $n$ is

- **(1)** $100$
- (2) $1$
- (3) $1000$
- (4) $10$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In series, $R_s = 10R$, so $I_s = \frac{E}{10R}$.
2. In parallel, $R_p = \frac{R}{10}$, so $I_p = \frac{E}{R/10} = \frac{10E}{R}$.
3. $n = \frac{I_p}{I_s} = \frac{10E/R}{E/(10R)} = 100$, which is option $1$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q039_49737073_02112026.png?v=497370731329)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Ten equal resistors give $10R$ in series and $R/10$ in parallel, a hundredfold fall in resistance, so the same emf drives a hundred times the current
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The parallel combination is correctly seen as $R/10$ and the current is read as ten times larger, with the series resistance left as a single $R$ instead of $10R$. The factor of ten acts twice -- once on each arrangement -- so $n = (10E/R) \div (E/10R) = 100$.
- **Why:** This question requires the current compared across two arrangements of the same ten resistors, demonstrated by the stem asking for the factor by which "the current is increased $n$ times" while giving no value for $E$ or $R$.
<!--/ecat-->

## Q40

Physics · Kinematics

A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity $4\,\mathrm{m\,s^{-1}}$. The ball strikes the water surface after $4\,\mathrm{s}$. The height of bridge above water surface is (Take $g = 10\,\mathrm{m\,s^{-2}}$)

- (1) $60\,\mathrm{m}$
- **(2)** $64\,\mathrm{m}$
- (3) $68\,\mathrm{m}$
- (4) $56\,\mathrm{m}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Take upward as positive: $u = +4\,\mathrm{m\,s^{-1}}$, $a = -g = -10\,\mathrm{m\,s^{-2}}$, $t = 4\,\mathrm{s}$.
2. $s = ut - \frac{1}{2}gt^2$.
3. $s = 4 \times 4 - \frac{1}{2} \times 10 \times 4^2 = 16 - 80 = -64\,\mathrm{m}$.
4. The ball ends $64\,\mathrm{m}$ below the launch point, so the bridge height is $64\,\mathrm{m}$, which is option $2$.

**Subtopic:** Freely Falling Bodies · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q040_fcb51f71_02112026.png?v=fcb51f715b5a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a body thrown up that lands below its start, one signed equation covers the whole flight: taking down as positive, $h = -ut + \tfrac{1}{2}gt^2$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Worked the standard slips for a thrown-up-then-falls-past-the-start problem and none lands on a printed option: dropping the initial velocity gives $\tfrac{1}{2}(10)(16) = 80$ m, signing the throw downwards gives $16 + 80 = 96$ m, restarting the clock at the top without the $0.8$ m rise gives $64.8$ m, and using $g = 9.8$ gives $62.4$ m. The three wrong options are 56, 60 and 68, which with the key 64 form a ladder in steps of 4.
- **Why:** This question requires one signed kinematic equation carried across a flight that starts upwards and ends below the start, demonstrated by "throws a small ball vertically upwards with a velocity $4\,\mathrm{m\,s^{-1}}$" and "strikes the water surface after $4\,\mathrm{s}$".
- **Note:** The option set is the key in a four-metre ladder (56, 60, 64, 68) and the two values the standard slips produce -- 80 m from dropping the initial velocity, 96 m from signing it downwards -- are both absent, so no printed option catches a nameable mistake. Hence no_trap rather than a forced label.
<!--/ecat-->

## Q41

Physics · Alternating Current

The net impedance of circuit (as shown in figure) will be

![printed figure: Series LCR circuit with an AC source 220 V, 50 Hz](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q041_3eadb352_02112026.png?v=3eadb352a4cf)

*Series LCR circuit with an AC source 220 V, 50 Hz*

![drawn: Series LCR circuit with an AC source 220 V, 50 Hz](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q041_question_0fb7fefa_02112026.svg?v=0fb7fefa2e2c)  
*drawn by code/lib/physics_figure.py*

- (1) $15\,\Omega$
- **(2)** $5\sqrt{5}\,\Omega$
- (3) $25\,\Omega$
- (4) $10\sqrt{2}\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Series LCR circuit with $R = 10\,\Omega$, $L = \frac{50}{\pi}\,\text{mH}$, $C = \frac{10^3}{\pi}\,\mu\text{F}$, $f = 50\,\text{Hz}$.
2. $X_L = 2\pi f L = 2\pi (50) \frac{50}{\pi}\times 10^{-3} = 5\,\Omega$.
3. $X_C = \frac{1}{2\pi f C} = \frac{1}{2\pi (50) \frac{10^3}{\pi}\times 10^{-6}} = \frac{1}{0.1} = 10\,\Omega$.
4. $Z = \sqrt{R^2 + (X_C - X_L)^2} = \sqrt{10^2 + 5^2} = \sqrt{125}$.
5. $\sqrt{125} = 5\sqrt{5}\,\Omega$, which is option $2$.

**Subtopic:** Impedance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q041_72871be7_02112026.png?v=72871be79123)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a series LCR circuit the resistance and the NET reactance add in quadrature: $Z = \sqrt{R^2 + (X_L - X_C)^2}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $X_L = 5\,\Omega$ and $X_C = 10\,\Omega$ come out correctly and the net reactance $5\,\Omega$ is then added straight onto $R = 10\,\Omega$ to give $15\,\Omega$. Resistance and reactance stand at right angles in the phasor diagram, so they combine as $\sqrt{10^2 + 5^2} = 5\sqrt{5}$.
- **Why:** This question requires the two reactances evaluated and then combined with the resistance in quadrature, demonstrated by the figure printing $L = 50/\pi$ mH, $C = 10^3/\pi\,\mu$F and $R = 10\,\Omega$ in one series loop at 50 Hz while the options offer both the surd $5\sqrt{5}$ and the plain sums 15 and 25.
- **Note:** The figure arrived as a drawn spec in this packet, so the component values could be read; the stem alone does not carry them.
<!--/ecat-->

## Q42

Physics · Gravitation

A satellite is orbiting just above the surface of the earth with period $T$. If $d$ is the density of the earth and $G$ is the universal constant of gravitation, the quantity $\dfrac{3\pi}{Gd}$ represents

- **(1)** $T^{2}$
- (2) $T^{3}$
- (3) $\sqrt{T}$
- (4) $T$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For an orbit just above the surface, $r \approx R$, so $T = 2\pi\sqrt{\frac{R^{3}}{GM}}$.
2. Squaring: $T^{2} = \frac{4\pi^{2}R^{3}}{GM}$.
3. Mass of the earth in terms of density: $M = \frac{4}{3}\pi R^{3} d$.
4. Substitute: $T^{2} = \frac{4\pi^{2}R^{3}}{G \cdot \frac{4}{3}\pi R^{3} d} = \frac{3\pi}{Gd}$.
5. So $\frac{3\pi}{Gd} = T^{2}$, which is option $1$.

**Subtopic:** Motion of a Satellite · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q042_b6c62aa1_02112026.png?v=b6c62aa19931)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a satellite skimming the surface $T^2 = 4\pi^2 R^3/GM$, and putting $M = \frac{4}{3}\pi R^3 d$ cancels the radius to leave $T^2 = 3\pi/Gd$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The derivation ends as $T = \sqrt{3\pi/Gd}$ and the root is then carried to the other side, so the printed expression gets read as $\sqrt{T}$. Squaring the correct line instead gives $3\pi/Gd = T^2$.
- **Why:** This question requires the orbital-period relation with the earth's mass replaced by its density, demonstrated by the stem supplying "$d$ is the density of the earth" and "$G$ is the universal constant of gravitation" and then printing $\dfrac{3\pi}{Gd}$ for identification.
<!--/ecat-->

## Q43

Physics · Ray Optics

Two thin lenses are of same focal lengths ($f$), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be

- (1) $\frac{f}{4}$
- (2) $\frac{f}{2}$
- **(3)** Infinite
- (4) Zero

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For thin lenses in contact, $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}$.
2. Convex lens $f_1 = +f$, concave lens $f_2 = -f$, so $\frac{1}{F} = \frac{1}{f} - \frac{1}{f} = 0$.
3. $\frac{1}{F} = 0 \Rightarrow F = \infty$, which is option $3$ (Infinite).

**Subtopic:** Combination of Thin Lenses in Contact · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q043_5b3719df_02112026.png?v=5b3719df65a3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Powers add for thin lenses in contact, so equal convex and concave powers cancel and the pair has zero power and infinite focal length
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $1/F = 1/f + 1/(-f) = 0$ is reached correctly and the zero is written down as the answer. Zero is the combination's POWER; the focal length is its reciprocal, which is infinite.
- **Why:** This question requires the thin-lens addition rule applied with the sign convention, demonstrated by "same focal lengths ($f$), but one is convex and the other one is concave" and by the answer being the verdict "Infinite" rather than a computed number.
<!--/ecat-->

## Q44

Physics · Semiconductor Electronics

For the following logic circuit, the truth table is

![printed figure: Inputs A and B each pass through a NOT gate into a NAND gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q044_3ea79dba_02112026.png?v=3ea79dbab03c)

*Inputs A and B each pass through a NOT gate into a NAND gate giving output Y*

![drawn: Inputs A and B each pass through a NOT gate into a NAND gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q044_question_d58ac12a_02112026.svg?v=d58ac12afb0a)  
*drawn by code/lib/physics_figure.py*

- **(1)** $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 1 \end{array}$
- (2) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$
- (3) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{array}$
- (4) $\begin{array}{ccc} A & B & Y \\ 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{array}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The figure shows $A$ and $B$ each inverted, then fed to a NAND gate, so $Y = \overline{\bar{A}\cdot\bar{B}}$.
2. By De Morgan's theorem, $\overline{\bar{A}\cdot\bar{B}} = \bar{\bar{A}} + \bar{\bar{B}} = A + B$.
3. So the circuit is an OR gate: $Y = 0, 1, 1, 1$ for $AB = 00, 01, 10, 11$, which is option $1$.

**Subtopic:** Logic Gates · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q044_4bb87823_02112026.png?v=4bb87823ab17)

---

<!--ecat-->
#### Categories

- **Type:** **New type (proposed)** (`new_type`) — a printed shape none of the above describes
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Inverting both inputs of a NAND gate gives an OR gate: $\overline{\bar{A}\cdot\bar{B}} = A + B$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The output gate in the figure is an AND with a bubble, i.e. a NAND, so its own table $1,1,1,0$ is written straight down against the raw inputs $A$ and $B$. The NAND is fed by $\bar{A}$ and $\bar{B}$, not by $A$ and $B$, and $\overline{\bar{A}\cdot\bar{B}} = A + B$ gives $0,1,1,1$.
- **Why:** This question requires the gate rules applied to the drawn chain rather than to the gate names, demonstrated by the figure placing a NOT gate on each of $A$ and $B$ before the bubbled AND, so that the printed NAND table and the printed AND table are both available as options.
- **Note:** The E1 pattern returned plain_mcq on its 16-option default, but the printed options are four truth tables judged whole, which is the shape recorded here and the reason for new_type. The figure arrived as a drawn spec in this packet (two NOT gates feeding an AND gate with an output bubble), so the network could be read; the stem names no gates at all.
<!--/ecat-->

## Q45

Physics · Magnetic Effect of Electric Current

A very long conducting wire is bent in a semi-circular shape from $A$ to $B$ as shown in figure. The magnetic field at point $P$ for steady current configuration is given by

![printed figure: Long wire with a semicircular bend from A to B, point P at the centre of the semicircle](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q045_380d4d08_02112026.png?v=380d4d0866be)

*Long wire with a semicircular bend from A to B, point P at the centre of the semicircle*

![drawn: Long wire with a semicircular bend from A to B, point P at the centre of the semicircle](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q045_question_f021b128_02112026.svg?v=f021b128b55a)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{\mu_0 i}{4R}$ pointed away from the page
- **(2)** $\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$ pointed away from page
- (3) $\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$ pointed into the page
- (4) $\frac{\mu_0 i}{4R}$ pointed into the page

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $P$ is the centre of the semicircle, and $A$, $B$ are the feet of the perpendiculars from $P$ to the two semi-infinite straight wires, each at distance $R$.
2. Semicircular arc (current from $A$ down the left side to $B$): $B_{arc} = \frac{\mu_0 i}{4R}$, directed out of the page by the right-hand rule.
3. Upper semi-infinite wire (current rightward, $P$ below it, ending at $A$): $B_1 = \frac{\mu_0 i}{4\pi R}$, into the page.
4. Lower semi-infinite wire (current leftward, $P$ above it, starting at $B$): $B_2 = \frac{\mu_0 i}{4\pi R}$, into the page.
5. Net: $B = \frac{\mu_0 i}{4R} - \frac{2\mu_0 i}{4\pi R} = \frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$, out of the page, which is option $2$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q045_9c5a21b1_02112026.png?v=9c5a21b1a747)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At the centre of a semicircular arc the field is $\mu_0 i/4R$, and each semi-infinite straight wire ending on the perpendicular foot adds $\mu_0 i/4\pi R$, the straight pair opposing the arc here
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Both contributions are found and subtracted correctly to give the magnitude $\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$, and the right-hand rule is then turned the other way for the surviving term. Against the printed key the resultant is away from the page, so only the sense fails.
- **Why:** This question requires the arc's field and the two semi-infinite straight fields summed with their senses, demonstrated by each option pairing a magnitude with a direction -- "$\frac{\mu_0 i}{4R}\left[1-\frac{2}{\pi}\right]$ pointed into the page" -- so both parts must hold at once.
- **Note:** The E1 pattern called this statement_options from a count of sentence-shaped options; the printed shape is a magnitude plus a direction that must both be right, which is two_part. Tagged as printed. Working the figure exactly as transcribed in this packet -- current in along the lower wire, round the left of the arc, out along the upper wire -- puts the arc's contribution into the page and the straight pair's out of it, making the resultant into the page, i.e. option 3, while the printed key is option 2; the magnitude $\frac{\mu_0 i}{4R}[1-\frac{2}{\pi}]$ is the same either way. A reviewer holding the printed figure should check the arrow senses on the two straight portions: if they are as transcribed, the trap and option 1 exchange directions and the labels stay as they are.
<!--/ecat-->

## Q46

Physics · Current Electricity

The resistance of platinum wire at $0^{\circ}\mathrm{C}$ is $2\,\Omega$ and $6.8\,\Omega$ at $80^{\circ}\mathrm{C}$. The temperature coefficient of resistance of the wire is

- (1) $3 \times 10^{-3}\,^{\circ}\mathrm{C}^{-1}$
- **(2)** $3 \times 10^{-2}\,^{\circ}\mathrm{C}^{-1}$
- (3) $3 \times 10^{-1}\,^{\circ}\mathrm{C}^{-1}$
- (4) $3 \times 10^{-4}\,^{\circ}\mathrm{C}^{-1}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Use $R_T = R_0(1 + \alpha T)$, so $\alpha = \frac{R_T - R_0}{R_0 T}$.
2. $R_T - R_0 = 6.8\,\Omega - 2\,\Omega = 4.8\,\Omega$.
3. $R_0 T = 2\,\Omega \times 80^{\circ}\mathrm{C} = 160\,\Omega\,^{\circ}\mathrm{C}$.
4. $\alpha = \frac{4.8}{160} = 0.03 = 3 \times 10^{-2}\,^{\circ}\mathrm{C}^{-1}$, which is option $2$.

**Subtopic:** Temperature Coefficient of Resistance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q046_e9e2e5ea_02112026.png?v=e9e2e5eabd77)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The temperature coefficient is the fractional change of resistance per degree referred to the resistance at $0^{\circ}$C: $\alpha = (R - R_0)/(R_0\,\Delta t)$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $\alpha = 4.8/(2 \times 80)$ is set up correctly and the division is finished one decimal place out, giving $0.003$ instead of $0.03$. All four options print the same mantissa 3, so the whole question rests on where that decimal lands: $4.8/160 = 0.03 = 3 \times 10^{-2}$.
- **Why:** This question requires the temperature coefficient computed from two resistances and the interval between them, demonstrated by the stem supplying "$2\,\Omega$" at $0^{\circ}$C and "$6.8\,\Omega$ at $80^{\circ}$C" while all four options differ only in the power of ten.
<!--/ecat-->

## Q47

Physics · Electrostatics

An electric dipole is placed as shown in the figure. The electric potential (in $10^{2}\,\mathrm{V}$) at point $P$ due to the dipole is ($\epsilon_0$ = permittivity of free space and $\dfrac{1}{4\pi\epsilon_0} = K$)

![printed figure: Electric dipole -q and +q, 3 cm each side of origin 0, with point P on the axis 5 cm from 0](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q047_88938fdb_02112026.png?v=88938fdb235d)

*Electric dipole -q and +q, 3 cm each side of origin 0, with point P on the axis 5 cm from 0*

![drawn: Electric dipole -q and +q, 3 cm each side of origin 0, with point P on the axis 5 cm from 0](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_drawn/q047_question_c84c001c_03112026.svg?v=c84c001c34e2)  
*drawn by code/lib/physics_figure.py*

- (1) $\left(\dfrac{5}{8}\right)qK$
- (2) $\left(\dfrac{8}{5}\right)qK$
- (3) $\left(\dfrac{8}{3}\right)qK$
- **(4)** $\left(\dfrac{3}{8}\right)qK$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. From the figure, $P$ is $5\,\mathrm{cm}$ from the centre $O$ on the axis, on the side of $+q$.
2. Distance from $+q$: $r_+ = 5 - 3 = 2\,\mathrm{cm} = 0.02\,\mathrm{m}$.
3. Distance from $-q$: $r_- = 5 + 3 = 8\,\mathrm{cm} = 0.08\,\mathrm{m}$.
4. $V = Kq\left(\frac{1}{0.02} - \frac{1}{0.08}\right) = Kq(50 - 12.5) = 37.5\,Kq$.
5. $37.5\,Kq = \frac{3}{8}qK \times 10^{2}\,\mathrm{V}$, which is option $4$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q047_f6033f59_02112026.png?v=f6033f5970ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Potential is a signed scalar sum, so on the dipole axis the near charge gives $+Kq/r_+$ and the far charge $-Kq/r_-$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The two distances are read correctly as 2 cm and 8 cm and the two potentials are then added as magnitudes, $Kq(50 + 12.5)$, giving $\frac{5}{8}qK$. The left charge is $-q$, so its term is subtracted: $Kq(50 - 12.5) = \frac{3}{8}qK$ in units of $10^2$ V.
- **Why:** This question requires the two axial distances taken from the figure and the two potentials added with their signs, demonstrated by the figure placing $-q$ and $+q$ "3 cm" either side of O with P at "5 cm", which fixes $r_+ = 2$ cm and $r_- = 8$ cm.
- **Note:** The distances live only in the figure, which arrived as a drawn spec in this packet; the stem's "(in $10^2$ V)" is what makes $\frac{3}{8}qK$ the printed form of $37.5\,Kq$ volts.
<!--/ecat-->

## Q48

Physics · Ray Optics

In the figure shown here, what is the equivalent focal length of the combination of lenses (Assume that all layers are thin)?

![printed figure: Thin biconvex lens of index n1 = 1.5 embedded in a medium of index n2 = 1.6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q048_0e5f2d45_02112026.png?v=0e5f2d457f02)

*Thin biconvex lens of index n1 = 1.5 embedded in a medium of index n2 = 1.6*

![drawn: Thin biconvex lens of index n1 = 1.5 embedded in a medium of index n2 = 1.6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_drawn/q048_question_c409cd3c_03112026.svg?v=c409cd3c6231)  
*drawn by code/lib/physics_figure.py*

- (1) $-40\,\mathrm{cm}$
- **(2)** $-100\,\mathrm{cm}$
- (3) $-50\,\mathrm{cm}$
- (4) $40\,\mathrm{cm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The slab of $n_2 = 1.6$ with the lens of $n_1 = 1.5$ inside acts as three thin lenses in contact in air: plano-concave ($n_2$), biconvex ($n_1$), plano-concave ($n_2$).
2. Biconvex lens: $\frac{1}{f_1} = (1.5-1)\left(\frac{1}{20}+\frac{1}{20}\right) = \frac{1}{20}\,\mathrm{cm^{-1}}$.
3. Each plano-concave lens: $\frac{1}{f_2} = (1.6-1)\left(\frac{1}{\infty}-\frac{1}{20}\right) = -\frac{3}{100}\,\mathrm{cm^{-1}}$.
4. Lenses in contact: $\frac{1}{F} = \frac{1}{20} - 2\times\frac{3}{100} = \frac{5}{100}-\frac{6}{100} = -\frac{1}{100}\,\mathrm{cm^{-1}}$.
5. $F = -100\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Combination of Thin Lenses in Contact, Lens Maker Formula · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q048_2d55787c_02112026.png?v=2d55787c8fd5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A convex lens surrounded by a denser medium diverges; with thin layers, add the powers of the three layers -- medium, lens, medium -- in air
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  "A biconvex lens converges, so the focal length is positive" is applied although the figure puts the lens ($n_1 = 1.5$) inside a denser medium ($n_2 = 1.6$), and $+40$ cm is the only positive option on offer. Denser outside means the surfaces bend light the other way, so the combination diverges and $f = -100$ cm.
- **Why:** This question requires the powers of three thin layers added with the indices the figure prints, demonstrated by "Assume that all layers are thin" together with the figure's $n_1 = 1.5$ inside, $n_2 = 1.6$ outside and $R_1 = R_2 = 20$ cm.
- **Note:** The indices and radii live only in the figure, which arrived as a drawn spec in this packet. Checked the key: adding the three thin layers in air gives $1/f = -0.03 + 0.05 - 0.03 = -0.01$ cm$^{-1}$, i.e. $-100$ cm, and the surface-by-surface refraction calculation (including the shift at the flat exit face) gives the same $-100$ cm, so the printed key stands.
<!--/ecat-->

## Q49

Physics · Magnetic Effect of Electric Current

A wire carrying a current $I$ along the positive $x$-axis has length $L$. It is kept in a magnetic field $\vec{B} = (2\hat{i} + 3\hat{j} - 4\hat{k})\,\mathrm{T}$. The magnitude of the magnetic force acting on the wire is

- (1) $\sqrt{5}\,IL$
- **(2)** $5\,IL$
- (3) $\sqrt{3}\,IL$
- (4) $3\,IL$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The force on a straight current-carrying wire is $\vec{F} = I\vec{L} \times \vec{B}$ with $\vec{L} = L\hat{i}$.
2. $\hat{i} \times (2\hat{i} + 3\hat{j} - 4\hat{k}) = 0 + 3\hat{k} + 4\hat{j}$, so $\vec{F} = IL(4\hat{j} + 3\hat{k})$.
3. $|\vec{F}| = IL\sqrt{4^2 + 3^2} = 5\,IL$, which is option $2$.

**Subtopic:** Magnetic Force · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q049_55cd8a7a_02112026.png?v=55cd8a7a32ea)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Only the field perpendicular to the current produces force, so $|F| = IL\sqrt{B_y^2 + B_z^2}$ and the component along the wire contributes nothing
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The component along the wire is correctly thrown away, and then only one of the two surviving components is kept: $F = ILB_y = 3IL$. Both survive, so they combine as $IL\sqrt{3^2 + 4^2} = 5IL$.
- **Why:** This question requires the cross product of the current direction with the field and then the magnitude of what survives, demonstrated by "a current $I$ along the positive $x$-axis" set against "$\vec{B} = (2\hat{i} + 3\hat{j} - 4\hat{k})$ T".
<!--/ecat-->

## Q50

Physics · Oscillations

The $x$-$t$ graph of a particle performing simple harmonic motion is shown in the figure. The acceleration of the particle at $t = 2\,\mathrm{s}$ is

![printed figure: x-t graph of SHM: x = sin(pi t/4), amplitude 1 m, period 8 s](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q050_ec3d0ab8_02112026.png?v=ec3d0ab8bc69)

*x-t graph of SHM: x = sin(pi t/4), amplitude 1 m, period 8 s*

![drawn: x-t graph of SHM: x = sin(pi t/4), amplitude 1 m, period 8 s](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_drawn/q050_question_29670de0_03112026.svg?v=29670de081d6)  
*drawn by code/lib/physics_figure.py*

- (1) $-\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$
- (2) $\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$
- **(3)** $-\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$
- (4) $\frac{\pi^2}{8}\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. From the graph, amplitude $A = 1\,\mathrm{m}$ and period $T = 8\,\mathrm{s}$.
2. $\omega = \frac{2\pi}{T} = \frac{2\pi}{8} = \frac{\pi}{4}\,\mathrm{rad\,s^{-1}}$.
3. At $t = 2\,\mathrm{s}$ the graph shows $x = +1\,\mathrm{m}$ (maximum displacement).
4. $a = -\omega^2 x = -\left(\frac{\pi}{4}\right)^2 (1) = -\frac{\pi^2}{16}\,\mathrm{m\,s^{-2}}$, which is option $3$.

**Subtopic:** Acceleration in SHM · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q050_49419b4c_02112026.png?v=49419b4c8ac0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In SHM the acceleration is $-\omega^2 x$, so it is largest at the extreme position and always points back towards the centre
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  $\omega = 2\pi/8 = \pi/4$ and $x = 1$ m at $t = 2$ s are read off the graph correctly and the magnitude $\pi^2/16$ comes out right, with the minus sign of $a = -\omega^2 x$ left off. At $t = 2$ s the particle is at the positive extreme, so the acceleration points back towards the origin and is negative.
- **Why:** This question requires $\omega$ and the displacement read off the plot and then substituted in $a = -\omega^2 x$, demonstrated by the graph showing a 1 m amplitude with zeros at $t = 0, 4, 8$ s -- an 8 s period -- and the crest standing at $t = 2$ s.
- **Note:** The amplitude and period live only in the figure, which arrived as a drawn spec in this packet.
<!--/ecat-->

## Q51

Chemistry · inorganic · The D- and F-Block Elements – Practice

The stability of $\mathrm{Cu^{2+}}$ is more than $\mathrm{Cu^{2+}}$ salts in aqueous solution due to

- (1) Enthalpy of atomization
- **(2)** Hydration energy
- (3) Second ionisation enthalpy
- (4) First ionisation enthalpy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The greater stability of $\mathrm{Cu^{2+}}(aq)$ over $\mathrm{Cu^{+}}(aq)$ comes from the much more negative $\Delta_{hyd}H$ of $\mathrm{Cu^{2+}}$, which more than compensates for the second ionisation enthalpy of Cu, so the answer is option $2$.

**Subtopic:** Oxidation State · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q051_489a47a9_02112026.png?v=489a47a9d9a9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In water the much larger hydration enthalpy of the smaller, doubly charged copper ion outweighs the second ionisation enthalpy, so the +2 state is the stable one in aqueous solution
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the stem as stored reads "The stability of $\mathrm{Cu^{2+}}$ is more than $\mathrm{Cu^{2+}}$ salts", naming the same ion on both sides of the comparison, so which two species the question contrasts is not in the record and no route to a wrong option can be audited
- **Why:** This question requires the reason NCERT gives for one oxidation state being favoured in water, demonstrated by the stem's "due to" followed by four thermodynamic quantities as options.
- **Note:** Stem damage: the comparison has lost one species -- it compares $\mathrm{Cu^{2+}}$ with $\mathrm{Cu^{2+}}$. A reviewer with the printed paper should check whether the first species is $\mathrm{Cu^{+}}$; if it is, the mechanism to confirm is option 3, second ionisation enthalpy, the quantity that works against the +2 state and so the one reached for when the question asks which quantity decides the comparison. Tagged as printed; the key (hydration energy) is consistent with either reading and is not re-judged here.
<!--/ecat-->

## Q52

Chemistry · physical · Surface Chemistry

Which one is an example of heterogenous catalysis?

- (1) Hydrolysis of sugar catalysed by $\mathrm{H^{+}}$ ions
- (2) Decomposition of ozone in presence of nitrogen monoxide
- **(3)** Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron
- (4) Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Heterogeneous catalysis means the catalyst is in a different phase from the reactants.
2. Option 1: sugar solution and $\mathrm{H^{+}}$ ions are both in the aqueous phase, so homogeneous.
3. Option 2: $\mathrm{O_3(g)}$ with $\mathrm{NO(g)}$ are both gases, so homogeneous.
4. Option 4: $\mathrm{2SO_2(g) + O_2(g) \xrightarrow{NO(g)} 2SO_3(g)}$ is all gas phase, so homogeneous (lead chamber process).
5. Option 3: $\mathrm{N_2(g) + 3H_2(g) \xrightarrow{Fe(s)} 2NH_3(g)}$ has a solid catalyst with gaseous reactants, so heterogeneous, which is option $3$.

**Subtopic:** Homogeneous and Heterogeneous Catalysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q052_40b8a2cf_02112026.png?v=40b8a2cf3c6f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A catalysis is heterogeneous when the catalyst is in a different phase from the reactants, as finely divided solid iron is to nitrogen and hydrogen gas
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The $\mathrm{SO_2 \rightarrow SO_3}$ conversion is carried in memory as the contact process over solid $\mathrm{V_2O_5}$, so the option is read as that reaction and the catalyst actually printed in it -- oxides of nitrogen -- is passed over
- **Why:** This question requires the defining criterion of heterogeneous catalysis applied to four printed cases, demonstrated by the key naming the catalyst's physical state inside the option -- "in the presence of finely divided iron".
- **Note:** type_patterns returned statement_options, but the stem is a single question ("Which one is an example of heterogenous catalysis?") and the options are reaction descriptions rather than claims to be graded, so the printed shape is recorded as mcq on the rulebook's statement_options test.
<!--/ecat-->

## Q53

Chemistry · physical · States of Matter

Which amongst the following options are correct graphical representation of Boyle’s Law?

- **(1)** ![printed figure: graph of P (y-axis) against 1/V (x-axis): three straight lines through the origin labelled T3, T2, T1 from steepest to least steep; T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_agent/q053_option_1_f7ac3bdd_03112026.png?v=f7ac3bdde957) *graph of P (y-axis) against 1/V (x-axis): three straight lines through the origin labelled T3, T2, T1 from steepest to least steep; T3 > T2 > T1*
- (2) ![printed figure: graph of P (y-axis) against 1/V (x-axis): three hyperbola-like curves labelled T1 (lowest), T2, T3 (highest); T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q053_option_2_97972a73_02112026.png?v=97972a736961) *graph of P (y-axis) against 1/V (x-axis): three hyperbola-like curves labelled T1 (lowest), T2, T3 (highest); T3 > T2 > T1*
- (3) ![printed figure: graph of P (y-axis) against T (x-axis): three straight lines through the origin labelled V1, V2, V3 from steepest to least steep; V1 < V2 < V3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_agent/q053_option_3_fa8dce8b_03112026.png?v=fa8dce8b61f6) *graph of P (y-axis) against T (x-axis): three straight lines through the origin labelled V1, V2, V3 from steepest to least steep; V1 < V2 < V3*
- (4) ![printed figure: graph of P (y-axis) against V (x-axis): three hyperbola-like curves labelled T1 (highest), T2, T3 (lowest); T3 > T2 > T1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q053_option_4_4cb758d3_02112026.png?v=4cb758d32619) *graph of P (y-axis) against V (x-axis): three hyperbola-like curves labelled T1 (highest), T2, T3 (lowest); T3 > T2 > T1*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Boyle's law at constant $n$ and $T$: $PV = nRT$, so $P = nRT\cdot\frac{1}{V}$.
2. A plot of $P$ against $\frac{1}{V}$ is a straight line through the origin with slope $nRT$.
3. Higher $T$ gives a larger slope, so with $T_3 > T_2 > T_1$ the $T_3$ line is steepest; option $1$ shows exactly this.
4. Option $2$ draws $P$ vs $\frac{1}{V}$ as hyperbolas, which is wrong.
5. Option $3$ is $P$ vs $T$ at constant $V$ (Gay-Lussac's law), not Boyle's law.
6. Option $4$ is $P$ vs $V$ hyperbolas, but the outermost curve is labelled $T_1$ although $T_3 > T_2 > T_1$; the outermost isotherm should be $T_3$, so the labelling is wrong.
7. Only option $1$ is a correct Boyle's law graph.

**Subtopic:** Gas Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q053_1c55d5e3_02112026.png?v=1c55d5e3812a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Boyle's law plotted: p against V is a hyperbola, p against 1/V is a straight line through the origin, and pV against p is a horizontal line
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and the packet carries all four as empty strings, so no plot was supplied to this step and no route to a wrong curve can be named
- **Why:** This question requires a plotted form of a gas law to be read, demonstrated by the stem asking for the "correct graphical representation of Boyle's Law".
- **Note:** Options 1-4 are empty in the record because they are graphs; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the plots should check the standard pull here: a straight line drawn for p against V, which is the shape belonging to the p against 1/V plot carried over to the wrong axes.
<!--/ecat-->

## Q54

Chemistry · physical · Chemical Kinetics

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A reaction can have zero activation energy.
- (Reasons R) The minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value, is called activation energy.

- **(1)** Both A and R are true and R is NOT the correct explanation of A
- (2) A is true but R is false
- (3) A is false but R is true
- (4) Both A and R are true and R is the correct explanation of A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Activation energy is $E_a = E_{threshold} - E_{reactants}$; if reactant molecules already possess the threshold energy, $E_a = 0$, so A is true.
2. R states the standard definition of activation energy as the extra energy needed to reach the threshold value, so R is true.
3. The definition in R does not account for why $E_a$ can be zero, so R is not the correct explanation of A, which is option $1$.

**Subtopic:** Activation Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q054_1cb8acea_02112026.png?v=1cb8acea9503)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Activation energy is the gap between the reactants' energy and the threshold energy, so a reaction whose reactants already hold threshold energy needs none
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The Reason prints the textbook definition of activation energy and the Assertion is about activation energy, so the shared term is read as the link; a definition says what the quantity is and never says why one reaction's value can fall to zero.
- **Why:** This question requires the definition of activation energy applied to the limiting case, demonstrated by R printing 'the minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value' while A asks whether that amount can be zero.
<!--/ecat-->

## Q55

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with $\mathrm{Fe^{3+}}$ due to the formation of

- (1) $\mathrm{NaSCN}$
- (2) $\mathrm{[Fe(CN)_5NOS]^{4-}}$
- **(3)** $\mathrm{[Fe(SCN)]^{2+}}$
- (4) $\mathrm{Fe_4[Fe(CN)_6]_3\cdot xH_2O}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. When N and S are both present, sodium fusion gives $\mathrm{NaSCN}$; with $\mathrm{Fe^{3+}}$ this forms $\mathrm{[Fe(SCN)]^{2+}}$, which is blood red, so the answer is option $3$.

**Subtopic:** Detection of Elements · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q055_a07ef300_02112026.png?v=a07ef300e8bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** When nitrogen and sulphur are both present, Lassaigne's fusion gives thiocyanate, and it is the iron(III) thiocyanate complex, not the sodium salt, that shows the blood red colour
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Sodium thiocyanate is the true product of the fusion when N and S are both present, and that remembered sentence is answered instead of the stem's question, which is which species carries the colour
- **Why:** This question requires a bench observation from a named test to be read back to the species responsible, demonstrated by the stem supplying the test, the reagent and the colour -- "gives blood red colour with $\mathrm{Fe^{3+}}$".
<!--/ecat-->

## Q56

Chemistry · organic · Haloalkanes and Haloarenes

Consider the following reaction and identify the product (P).

![printed figure: 3-Methylbutan-2-ol ($\ce{CH3-CH(CH3)-CH(OH)-CH3}$) →(HBr) P](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q056_e286a9d4_02112026.png?v=e286a9d44c16)

*3-Methylbutan-2-ol ($\ce{CH3-CH(CH3)-CH(OH)-CH3}$) →[HBr] P*

![drawn: 3-Methylbutan-2-ol ($\ce{CH3-CH(CH3)-CH(OH)-CH3}$) →(HBr) P](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q056_question_958aaa11_02112026.svg?v=958aaa1168c6)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 3-methylbutan-2-ol `CC(C)C(C)O` ![3-methylbutan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q056_question_s1_ca11da3c_02112026.svg?v=ca11da3c56c5)

- (1) $\mathrm{CH_3CH=CH-CH_3}$
- (2) 2-bromo-3-methylbutane `CC(C)C(C)Br` ![2-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q056_option_2_s1_18faa9fe_02112026.svg?v=18faa9fe6ac0) — $\mathrm{CH_3-CH(CH_3)-CH(Br)-CH_3}$
- (3) 1-bromo-2,2-dimethylpropane `CC(C)(C)CBr` ![1-bromo-2,2-dimethylpropane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q056_option_3_s1_7ca1318b_02112026.svg?v=7ca1318b3106) — $\mathrm{CH_3-C(CH_3)_2-CH_2Br}$
- **(4)** 2-bromo-2-methylbutane `CCC(C)(C)Br` ![2-bromo-2-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q056_option_4_s1_c5380da6_02112026.svg?v=c5380da663c8) — $\mathrm{CH_3-C(Br)(CH_3)-CH_2-CH_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Protonation of the $-OH$ by $\mathrm{HBr}$ gives $\mathrm{(CH_3)_2CH-CH(OH_2^+)CH_3}$.
2. Loss of $\mathrm{H_2O}$ gives the secondary carbocation $\mathrm{(CH_3)_2CH-\overset{+}{C}H-CH_3}$.
3. A 1,2-hydride shift from C3 gives the more stable tertiary carbocation $\mathrm{(CH_3)_2\overset{+}{C}-CH_2-CH_3}$.
4. Attack of $\mathrm{Br^-}$ gives $\mathrm{(CH_3)_2C(Br)-CH_2-CH_3}$ (2-bromo-2-methylbutane), which is option $4$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 12)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q056_44e596b6_02112026.png?v=44e596b6fc6c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A secondary alcohol treated with HBr goes through a carbocation, and a hydride shift to the adjacent branch point turns it into the more stable tertiary cation before bromide arrives
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The substitution is carried out where the hydroxyl stood, giving 2-bromo-3-methylbutane, because the hydride shift that moves the positive centre to the tertiary carbon is never looked for
- **Why:** This question requires the product a named reagent gives on a named substrate, demonstrated by the scheme printing 3-methylbutan-2-ol over an HBr arrow to P and the options differing in where the bromine sits.
- **Note:** Option 1 as stored is $\mathrm{CH_3CH=CH-CH_3}$, a four-carbon alkene, which cannot come from a five-carbon alcohol; the printed paper may carry a five-carbon alkene here. It is tagged as stored and treated as filler on the carbon count. The key and the other three options are internally consistent, so the question is rated rather than set aside.
<!--/ecat-->

## Q57

Chemistry · physical · Chemical Kinetics

For a certain reaction, the rate $= k[\mathrm{A}]^{2}[\mathrm{B}]$, when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would

- (1) Increase by a factor of six
- **(2)** Increase by a factor of nine
- (3) Increase by a factor of three
- (4) Decrease by a factor of nine

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Initial rate: $r = k[\mathrm{A}]^2[\mathrm{B}]$.
2. With $[\mathrm{A}]$ tripled and $[\mathrm{B}]$ constant: $r' = k(3[\mathrm{A}])^2[\mathrm{B}]$.
3. $r' = 9k[\mathrm{A}]^2[\mathrm{B}] = 9r$, so the rate increases by a factor of nine, which is option $2$.

**Subtopic:** Rate Expression · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q057_bb7944ef_02112026.png?v=bb7944efb806)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** In a rate law the order is a power, not a multiplier: tripling a species that appears squared multiplies the rate by $3^2$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The order 2 is multiplied by the factor 3 instead of 3 being raised to the power 2, so $2 \times 3 = 6$ is read off where $3^2 = 9$ belongs
- **Why:** This question requires how many times one quantity changes when another is changed, demonstrated by the stem holding B constant and asking what "the initial rate would" do when A is tripled.
- **Note:** type_patterns returned statement_options; the options are short consequences ("Increase by a factor of nine") and not claims to be graded, so the printed shape is recorded as mcq.
<!--/ecat-->

## Q58

Chemistry · inorganic · The p–Block Elements

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Coke | I | Carbon atoms are $\mathrm{sp^{3}}$ hybridised |
| B | Diamond | II | Used as a dry lubricant |
| C | Fullerene | III | Used as a reducing agent |
| D | Graphite | IV | Cage like molecules |

- (1) A-IV, B-I, C-II, D-III
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-III, B-IV, C-I, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Coke is used as a reducing agent in metallurgy, so $A \to III$.
2. In diamond each carbon is $\mathrm{sp^{3}}$ hybridised, tetrahedrally bonded, so $B \to I$.
3. Fullerenes such as $\mathrm{C_{60}}$ are cage-like molecules, so $C \to IV$.
4. Graphite's layers slide over each other, so it is used as a dry lubricant: $D \to II$.
5. $A$-III, $B$-I, $C$-IV, $D$-II matches option $2$.

**Subtopic:** Catenation & Allotropy Group 14 · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q058_642a7ae2_02112026.png?v=642a7ae26178)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each allotrope of carbon carries one printed identity: diamond's sp$^3$ network, graphite's sliding layers that lubricate, fullerene's closed cage molecule, and coke's job as the reducing agent in metallurgy
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Diamond's lattice is pictured as a rigid three-dimensional framework of linked carbon rings, so "Cage like molecules" reads as diamond. That leaves sp$^3$ for fullerene, whose curved surface already looks as though its carbons cannot be flat.
- **Why:** This question requires the property printed against each named carbon allotrope — a hybridisation for two of them and a use for the other two — demonstrated by List-II setting "Carbon atoms are sp$^3$ hybridised" beside "Used as a reducing agent", so each row is answered by a stated fact and not by any criterion the stem supplies.
<!--/ecat-->

## Q59

Chemistry · inorganic · The s-Block Elements

Which one of the following statements is correct?

- (1) All enzymes that utilise ATP in phosphate transfer require $\mathrm{Ca}$ as the cofactor
- (2) The bone in human body is an inert and unchanging substance
- (3) $\mathrm{Mg}$ plays roles in neuromuscular function and interneuronal transmission
- **(4)** The daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ in the human body is estimated to be $0.2\text{-}0.3\,\mathrm{g}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option $1$: enzymes that use ATP in phosphate transfer need $\mathrm{Mg}$ as cofactor, not $\mathrm{Ca}$, so it is false.
2. Option $2$: bone is not inert; it is constantly being solubilised and redeposited, so it is false.
3. Option $3$: the role in neuromuscular function and interneuronal transmission is that of $\mathrm{Ca}$, not $\mathrm{Mg}$, so it is false.
4. Option $4$: the daily requirement of $\mathrm{Mg}$ and $\mathrm{Ca}$ is $200\text{-}300\,\mathrm{mg} = 0.2\text{-}0.3\,\mathrm{g}$, so it is correct, which is option $4$.

**Subtopic:** Biological Importance of Sodium, Potassium, Magnesium and Calcium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q059_decc677a_02112026.png?v=decc677ae068)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The biological roles NCERT assigns to magnesium and to calcium are separate: magnesium is the cofactor for ATP phosphate transfer, calcium carries neuromuscular function and interneuronal transmission, and bone is continuously remodelled
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The neuromuscular and interneuronal sentence is remembered from the paragraph where magnesium and calcium are discussed together, and it is handed to magnesium because both metals are treated in the same two paragraphs
- **Why:** This question requires one stated fact from the section on the biological importance of these metals, demonstrated by the stem being only "Which one of the following statements is correct?" with each option a textbook sentence carrying one altered word.
- **Note:** Key doubt recorded, not re-judged: option 4 gives one range, $0.2$-$0.3$ g, for the daily requirement of magnesium AND calcium, whereas the source prints that figure for magnesium and a larger one for calcium, so the key is loose as worded. Option 3 is also true of magnesium in general physiology even though the textbook assigns those roles to calcium. Tagged as printed.
<!--/ecat-->

## Q60

Chemistry · physical · The Solid State

A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy $1/3$ of tetrahedral voids. If the formula of the compound is $\mathrm{A_xB_y}$, then the value of $x + y$ is in option

- (1) $4$
- (2) $3$
- (3) $2$
- **(4)** $5$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Let the number of B atoms in the ccp lattice be $N$.
2. A ccp lattice has $2N$ tetrahedral voids.
3. A occupies $\frac{1}{3}$ of them: $n_A = \frac{1}{3}(2N) = \frac{2N}{3}$.
4. $A : B = \frac{2N}{3} : N = 2 : 3$, so the formula is $\mathrm{A_2B_3}$.
5. $x + y = 2 + 3 = 5$, which is option $4$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q060_a3a9b82c_02112026.png?v=a3a9b82c5c9a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ccp lattice has four atoms and eight tetrahedral voids per unit cell, so filling one third of those voids gives $\mathrm{A_{8/3}B_4}$, which reduces to $\mathrm{A_2B_3}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The void count is taken as one per lattice atom instead of two, so one third of four voids gives $\mathrm{AB_3}$ and $x+y=4$
- **Why:** This question requires a number computed from the stem's numbers, demonstrated by "atoms of A occupy $1/3$ of tetrahedral voids" and the options being values of $x+y$.
<!--/ecat-->

## Q61

Chemistry · inorganic · Coordination Compounds – Practice

Homoleptic complex from the following complexes is

- (1) Diamminechloridonitrito-N-platinum (II)
- (2) Pentaamminecarbonatocobalt (III) chloride
- (3) Triamminetriaquachromium (III) chloride
- **(4)** Potassium trioxalatoaluminate (III)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A homoleptic complex has the metal bound to only one kind of ligand.
2. Option 1 is $[\mathrm{Pt(NH_3)_2Cl(NO_2)}]$ with $\mathrm{NH_3}$, $\mathrm{Cl^-}$ and $\mathrm{NO_2^-}$: heteroleptic.
3. Option 2 is $[\mathrm{Co(NH_3)_5(CO_3)}]\mathrm{Cl}$ with $\mathrm{NH_3}$ and $\mathrm{CO_3^{2-}}$: heteroleptic.
4. Option 3 is $[\mathrm{Cr(NH_3)_3(H_2O)_3}]\mathrm{Cl_3}$ with $\mathrm{NH_3}$ and $\mathrm{H_2O}$: heteroleptic.
5. Option 4 is $\mathrm{K_3[Al(C_2O_4)_3]}$ with only $\mathrm{C_2O_4^{2-}}$ ligands: homoleptic, so the answer is option $4$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q061_89719979_02112026.png?v=8971997954bb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A homoleptic complex is bound to only one kind of ligand, which the trisoxalato aluminate ion is and any name printing two different ligand words is not
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Homoleptic is read as "ligands of the same kind" in the loose sense of same charge and same denticity, and ammine and aqua being both neutral and monodentate lets the three-and-three name pass
- **Why:** This question requires a definition applied to four printed names, demonstrated by the stem naming only the class -- "Homoleptic complex from the following complexes is" -- and leaving the test to be carried out on each name.
- **Note:** I considered no_trap here, since each wrong name prints two or more ligand words. Option 3 is kept as the trap because it is the one name whose two ligands match in charge and denticity, which is the loosened test that reaches it.
<!--/ecat-->

## Q62

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The correct order of energies of molecular orbitals of $\mathrm{N_2}$ molecule, is

- (1) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$
- (2) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < \sigma 2p_z < \sigma^{*}2p_z < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y)$
- (3) $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma 2p_z < \sigma^{*}2p_z$
- **(4)** $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For molecules up to $\mathrm{N_2}$ (total electrons $\le 14$), $2s$-$2p$ mixing raises the energy of $\sigma 2p_z$ above the degenerate $\pi 2p_x = \pi 2p_y$ pair.
2. So the order is $\sigma 1s < \sigma^{*}1s < \sigma 2s < \sigma^{*}2s < (\pi 2p_x = \pi 2p_y) < \sigma 2p_z < (\pi^{*}2p_x = \pi^{*}2p_y) < \sigma^{*}2p_z$, which is option $4$.

**Subtopic:** Energy Level Diagram for Molecular Orbitals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q062_4e05387c_02112026.png?v=4e05387c1e2f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** For $\mathrm{N_2}$ the two $\pi 2p$ orbitals lie below $\sigma 2p_z$, the reverse of the general second-row sequence that holds from $\mathrm{O_2}$ onwards
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The general second-row sequence, in which $\sigma 2p_z$ comes before the $\pi 2p$ pair, is applied to nitrogen because that is the order the energy-level list is printed in
- **Why:** This question requires an ordering of items, demonstrated by the stem asking for "The correct order of energies of molecular orbitals" and each option printing a full sequence.
- **Note:** type_patterns returned arrange_in_order; the printed shape is four options from which one is picked, so qtype is mcq and the ordering is carried on the asks axis.
<!--/ecat-->

## Q63

Chemistry · inorganic · The p–Block Elements

Taking stability as the factor, which one of the following represents correct relationship?

- (1) $\mathrm{InI_3} > \mathrm{InI}$
- (2) $\mathrm{AlCl} > \mathrm{AlCl_3}$
- **(3)** $\mathrm{TlI} > \mathrm{TlI_3}$
- (4) $\mathrm{TlCl_3} > \mathrm{TlCl}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Down group 13 the inert pair effect makes the $+1$ oxidation state increasingly stable relative to $+3$.
2. For Al, $+3$ is the stable state, so $\mathrm{AlCl_3} > \mathrm{AlCl}$; option $2$ is wrong.
3. For Tl, $+1$ is more stable than $+3$, so $\mathrm{TlCl} > \mathrm{TlCl_3}$ (option $4$ wrong) and $\mathrm{TlI} > \mathrm{TlI_3}$, which is option $3$.
4. Option $1$ ($\mathrm{InI_3} > \mathrm{InI}$) is not the intended relationship; the clear inert-pair case is Tl, so the answer is option $3$.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q063_bee0ff91_02112026.png?v=bee0ff913317)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Down group 13 the inert pair effect makes the lower oxidation state the stable one, so thallium(I) is more stable than thallium(III) while the lighter members favour the +3 state
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The group oxidation state is taken to be the stable one throughout group 13, which turns the thallium comparison the wrong way round and puts $\mathrm{TlCl_3}$ above $\mathrm{TlCl}$
- **Why:** This question requires two similar cases to be told apart on which way a property runs, demonstrated by the stem's "Taking stability as the factor" with four options each asserting one halide more stable than another.
- **Note:** Key doubt recorded, not re-judged: option 1, $\mathrm{InI_3} > \mathrm{InI}$, is also defensible on the standard group-13 trend, since indium's +3 state is the more stable one, so two options read as true while the paper prints only option 3. Tagged as printed.
<!--/ecat-->

## Q64

Chemistry · inorganic · The p–Block Elements

> ⚠ The independent solve chose (2); the booklet prints (1).

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R

In the light of the above statements, choose the correct answer from the options given below

- (Assertion A) Helium is used to dilute oxygen in diving apparatus.
- (Reason R) Helium has high solubility in $\mathrm{O_2}$.

- **(1)** Both A and R are true and R is NOT the correct explanation of A
- (2) A is true but R is false
- (3) A is false but R is true
- (4) Both A and R are true and R correct explanation of A

**Answer** — booklet: (1) · independent solve: (2) · differs

**Solved independently** (answer withheld)

1. Assertion A is true: helium is mixed with oxygen in diving apparatus to dilute it.
2. It is used because helium has very low solubility in blood, unlike $\mathrm{N_2}$, so it does not cause bends; Reason R ('high solubility in $\mathrm{O_2}$') is false, so the answer is option $2$.

**Subtopic:** Applications & Special Features of Group 18 · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q064_d700d9b4_02112026.png?v=d700d9b43493)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Divers breathe a helium–oxygen mixture because helium is very sparingly soluble in blood, so it does not come out as bubbles on decompression
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Helium's very low solubility in blood is the reason the book gives for the diving mixture, so a solubility sentence sitting under this Assertion reads as that reason; R names solubility in $\mathrm{O_2}$, a different medium, and so leaves the diving use unexplained.
- **Why:** This question requires the reason the source gives for the helium–oxygen diving mixture, demonstrated by R offering 'Helium has high solubility in $\mathrm{O_2}$' as that reason while the stated ground is solubility in blood.
<!--/ecat-->

## Q65

Chemistry · physical · Structure of Atom

Select the correct statements from the following
Choose the correct answer from the options given below

- (A) Atoms of all elements are composed of two fundamental particles.
- (B) The mass of the electron is $9.10939 \times 10^{-31}\,\mathrm{kg}$.
- (C) All the isotopes of a given element show same chemical properties:
- (D) Protons and electrons are collectively known as nucleons.
- (E) Dalton’s atomic theory, regarded the atom as an ultimate particles of matter

- (1) C, D and E only
- (2) A and E only
- **(3)** B, C and E only
- (4) A, B and C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A is false: atoms are made of three fundamental particles (electron, proton, neutron), not two.
2. B is true: $m_e = 9.10939 \times 10^{-31}\,\mathrm{kg}$.
3. C is true: isotopes have the same atomic number and electronic configuration, so they show the same chemical properties.
4. D is false: nucleons are protons and neutrons, not protons and electrons.
5. E is true: Dalton's atomic theory regarded the atom as the ultimate, indivisible particle of matter.
6. The correct statements are B, C and E, which is option $3$.

**Subtopic:** Discovery of Sub-Atomic Particles, Isobars and Isotopes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q065_f2d33dff_02112026.png?v=f2d33dffafbc)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Atoms hold three fundamental particles, nucleons are protons and neutrons, and isotopes of one element share chemical properties - the opening lines of the Structure of Atom chapter
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Statement A reads as the chapter's own opening claim once a student counts only the electron and the proton, so A joins the two statements they are sure of, B and C, and the neutron is left out of the count.
- **Why:** This question requires each of five printed claims checked against the chapter's own sentences, demonstrated by the stem "Select the correct statements from the following" and by B quoting a stored value, "The mass of the electron is $9.10939 \times 10^{-31}\,\mathrm{kg}$".
<!--/ecat-->

## Q66

Chemistry · inorganic · Hydrogen

Which of the following statements are NOT correct? Choose the most appropriate answer from the options given below:

- (A) Hydrogen is used to reduce heavy metal oxides to metals.
- (B) Heavy water is used to study reaction mechanism.
- (C) Hydrogen is used to make saturated fats from oils.
- (D) The $\mathrm{H-H}$ bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements.
- (E) Hydrogen reduces oxides of metals that are more active than iron.

- (1) B, D only
- **(2)** D, E only
- (3) A, B, C only
- (4) B, C, D, E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A is correct: hydrogen reduces heavy metal oxides to metals.
2. B is correct: heavy water ($\mathrm{D_2O}$) is used to study reaction mechanisms.
3. C is correct: hydrogenation of vegetable oils with $\mathrm{H_2}$ gives saturated fats.
4. D is NOT correct: the $\mathrm{H-H}$ bond dissociation enthalpy ($435.88\,\mathrm{kJ\,mol^{-1}}$) is the highest for a single bond between two atoms of any element, not the lowest.
5. E is NOT correct: hydrogen reduces oxides of metals less active than iron, not more active.
6. The incorrect statements are D and E, which is option $2$.

**Subtopic:** Isotopes of Hydrogen and Properties of Dihydrogen · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q066_72a50e54_02112026.png?v=72a50e540cbf)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Uses of dihydrogen and heavy water, and the two NCERT lines this question inverts: the H-H bond enthalpy is the highest of any single bond, and hydrogen reduces oxides of metals less active than iron
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A, B and C are the three statements that are true, so a student who grades all five correctly and then looks for the option naming the ones that hold ticks option 3, which answers "which are correct" instead of the printed "which are NOT correct".
- **Why:** This question requires five printed claims graded against the hydrogen chapter's sentences under a negated task, demonstrated by the stem "Which of the following statements are NOT correct?" set against statement D, "The $\mathrm{H-H}$ bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements".
- **Note:** The content device inside D and E is a reversal, but the one trap the question lands on a printed option is option 3, which is exactly the set of true statements; the reversal is what the student has to catch rather than what an option offers.
<!--/ecat-->

## Q67

Chemistry · organic · Haloalkanes and Haloarenes

The given compound is an example of ______.

![printed figure: $\ce{C6H5-CH=CH-CH(X)-CH2CH3}$ (benzene ring bearing CH=CH-CH(X)-CH2CH3, i.e. 3-X-1-phenylpent-1-ene)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q067_1ec1c4bf_02112026.png?v=1ec1c4bfe060)

*$\ce{C6H5-CH=CH-CH(X)-CH2CH3}$ (benzene ring bearing CH=CH-CH(X)-CH2CH3, i.e. 3-X-1-phenylpent-1-ene)*

![drawn: $\ce{C6H5-CH=CH-CH(X)-CH2CH3}$ (benzene ring bearing CH=CH-CH(X)-CH2CH3, i.e. 3-X-1-phenylpent-1-ene)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q067_question_17881878_02112026.svg?v=17881878856f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 3-X-1-phenylpent-1-ene `*C(C=Cc1ccccc1)CC` ![3-X-1-phenylpent-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q067_question_s1_06161d9a_02112026.svg?v=06161d9a9fd8)

- (1) Aryl halide
- **(2)** Allylic halide
- (3) Vinylic halide
- (4) Benzylic halide

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The structure is $\mathrm{C_6H_5{-}CH{=}CH{-}CH(X){-}CH_2CH_3}$.
2. The carbon bearing $X$ is $sp^3$ and is bonded directly to a $\mathrm{C{=}C}$ carbon, so it is an allylic position (not on the ring, not on the vinylic carbon, not next to the ring).
3. Hence the compound is an allylic halide, which is option $2$.

**Subtopic:** Classification, Nomenclature, and Physical Properties of Haloalkanes and Haloarenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q067_c9a458a8_02112026.png?v=c9a458a81822)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A halide is allylic when the halogen sits on the saturated carbon next to a carbon-carbon double bond, and vinylic when it sits on the doubly bonded carbon itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The halogen is seen to be at the double bond and the adjacent class is taken, because allylic and vinylic are both defined off the same C=C in the same place in the text
- **Why:** This question requires a classification rule applied to a printed structure, demonstrated by the blank in "The given compound is an example of ______" with four halide classes as options.
- **Note:** type_patterns returned fill_in_blank, which the rulebook treats as an overlay rather than a shape, so qtype is recorded as mcq. The structure arrived as figure text with the halogen written as X, which still fixes its position relative to the double bond and the ring, so the question is rateable.
<!--/ecat-->

## Q68

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify product (A) in the following reaction:

![printed figure: 1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one →(Zn–Hg / conc. HCl) (A) + 2$\ce{H2O}$](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q068_55bd2b9d_02112026.png?v=55bd2b9d91eb)

*1-[3-(3-acetylcyclohexyl)phenyl]ethan-1-one →[Zn–Hg / conc. HCl] (A) + 2$\ce{H2O}$*

![drawn: 1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one →(Zn–Hg / conc. HCl) (A) + 2$\ce{H2O}$](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_question_5a86a14d_02112026.svg?v=5a86a14d5c1b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-[3-(3-acetylcyclohexyl)phenyl]ethan-1-one `CC(=O)c1cccc(C2CCCC(C(C)=O)C2)c1` ![1-(3-(3-acetylcyclohexyl)phenyl)ethan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_question_s1_b0bcb60f_02112026.svg?v=b0bcb60f4403); water `O` ![water](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_question_s2_795507b0_02112026.svg?v=795507b0c355)

- (1) 1-{3-[3-(1-hydroxyethyl)cyclohexyl]phenyl}ethan-1-ol `CC(O)c1cccc(C2CCCC(C(C)O)C2)c1` ![1-{3-(3-(1-hydroxyethyl)cyclohexyl)phenyl}ethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_option_1_s1_c64f9ecf_02112026.svg?v=c64f9ecf1ada)
- (2) {3-[3-(hydroxymethyl)cyclohexyl]phenyl}methanol `OCc1cccc(C2CCCC(CO)C2)c1` ![{3-(3-(hydroxymethyl)cyclohexyl)phenyl}methanol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_option_2_s1_2c5d719a_02112026.svg?v=2c5d719a19e2)
- (3) 1-methyl-3-(3-methylcyclohexyl)benzene `Cc1cccc(C2CCCC(C)C2)c1` ![1-methyl-3-(3-methylcyclohexyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_option_3_s1_1c1a93da_02112026.svg?v=1c1a93da0fd1)
- **(4)** 1-ethyl-3-(3-ethylcyclohexyl)benzene `CCc1cccc(C2CCCC(CC)C2)c1` ![1-ethyl-3-(3-ethylcyclohexyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q068_option_4_s1_04d2848e_02112026.svg?v=04d2848ee871)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Zn-Hg with conc. HCl is the Clemmensen reduction, which reduces a carbonyl $\mathrm{C{=}O}$ to $\mathrm{CH_2}$.
2. Each acetyl group $-\mathrm{COCH_3}$ (on the cyclohexane ring and on the benzene ring) becomes an ethyl group $-\mathrm{CH_2CH_3}$, releasing one $\mathrm{H_2O}$ each, matching $2\mathrm{H_2O}$.
3. The product has ethyl groups at both positions with the skeleton unchanged, which is option $4$.

**Subtopic:** Reduction of Aldehydes and Ketones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q068_a4d56b75_02112026.png?v=a4d56b750979)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Zinc amalgam with concentrated HCl, the Clemmensen reduction, takes a carbonyl all the way to $\mathrm{CH_2}$, and it does so at every carbonyl in the molecule
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and the packet carries all four as empty strings, so no product structure was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the product a named reagent pair gives, demonstrated by the scheme printing the diketone over a "Zn-Hg / conc. HCl" arrow to (A) with "+ 2$\mathrm{H_2O}$" alongside.
- **Note:** Options 1-4 are empty in the record because they are structures; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the structures should check two mechanisms: a product in which the carbonyls have been taken only as far as alcohols, which is the borohydride outcome rather than the Clemmensen one, and a product in which only one of the two carbonyls has been reduced -- the stem's own "2$\mathrm{H_2O}$" says both are.
<!--/ecat-->

## Q69

Chemistry · physical · Electrochemistry

> ⚠ The independent solve found no printed option exactly right ("No option equals $12"); its pick (2) is the closest fit, so treat this question as possibly misprinted.

The conductivity of centimolar solution of $\mathrm{KCl}$ at $25^{\circ}\mathrm{C}$ is $0.210\,\mathrm{ohm^{-1}\,cm^{-1}}$ and the resistance of the cell containing the solution at $25^{\circ}\mathrm{C}$ is $60\,\mathrm{ohm}$. The value of cell constant is

- (1) $3.28\,\mathrm{cm^{-1}}$
- **(2)** $1.26\,\mathrm{cm^{-1}}$
- (3) $3.34\,\mathrm{cm^{-1}}$
- (4) $1.34\,\mathrm{cm^{-1}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Conductivity $\kappa = \frac{G^*}{R}$, so cell constant $G^* = \kappa R$.
2. $G^* = 0.210\,\Omega^{-1}\mathrm{cm^{-1}} \times 60\,\Omega = 12.6\,\mathrm{cm^{-1}}$.
3. No option equals $12.6\,\mathrm{cm^{-1}}$; the digits match $1.26\,\mathrm{cm^{-1}}$, which corresponds to $\kappa = 0.0210\,\Omega^{-1}\mathrm{cm^{-1}}$, so option $2$.

**Subtopic:** Some Important Terms Related to Conductance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q069_8c915f1a_02112026.png?v=8c915f1a0d22)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The cell constant is the conductivity multiplied by the measured resistance, $G^{*} = \kappa R$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the stem as stored gives $\kappa = 0.210\,\mathrm{ohm^{-1}cm^{-1}}$ with $R = 60\,\mathrm{ohm}$, whose product is $12.6\,\mathrm{cm^{-1}}$ and is not among the four options, so the number the question was built on is not in the record and no route to a wrong option can be audited
- **Why:** This question requires a number computed from the stem's numbers, demonstrated by the stem supplying a conductivity and a resistance and the options being values of the cell constant.
- **Note:** Stem damage, almost certainly a lost zero of the kind the rulebook's own worked example describes: the printed key, $1.26\,\mathrm{cm^{-1}}$, is $\kappa R$ for $\kappa = 0.0210\,\mathrm{ohm^{-1}cm^{-1}}$, while our stem reads $0.210$. The key is consistent with the corrected stem and is not re-judged. Even on the corrected number I could find no derivation for $3.28$, $3.34$ or $1.34$ -- multiplying or dividing the two printed quantities gives only $1.26$ and $3.5\times10^{-4}$ -- so a reviewer with the printed paper should expect no_trap here on the arithmetic as well.
<!--/ecat-->

## Q70

Chemistry · physical · Ionic Equilibrium

Amongst the given options which of the following molecules/ ion acts as a Lewis acid?

- (1) $\mathrm{H_2O}$
- **(2)** $\mathrm{BF_3}$
- (3) $\mathrm{OH^-}$
- (4) $\mathrm{NH_3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A Lewis acid is an electron-pair acceptor.
2. In $\mathrm{BF_3}$, boron has only $6$ valence electrons (incomplete octet), so it can accept a lone pair: Lewis acid.
3. $\mathrm{H_2O}$, $\mathrm{OH^-}$ and $\mathrm{NH_3}$ all carry lone pairs and donate them: Lewis bases.
4. Hence the answer is $\mathrm{BF_3}$, option $2$.

**Subtopic:** Lewis Acids and Bases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q070_5d3f22c0_02112026.png?v=5d3f22c0de2c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A Lewis acid accepts a lone pair, which needs a vacant orbital -- boron in $\mathrm{BF_3}$ has one, while water, hydroxide and ammonia all carry lone pairs to give away
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Water is true as an answer to which of these can act as an acid in the proton sense, and that is the acid definition carried over to a stem that asks for a Lewis acid
- **Why:** This question requires a definition applied to four printed species, demonstrated by the stem naming only the class -- "acts as a Lewis acid" -- and the options being bare formulae.
<!--/ecat-->

## Q71

Chemistry · organic · Biomolecules

Given below are two statements :
Statement I : A unit formed by the attachment of a base to $1'$ position of sugar is known as nucleoside.
Statement II : When nucleoside is linked to phosphorous acid at $5'$-position of sugar moiety, we get nucleotide.
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) A unit formed by the attachment of a base to $1'$ position of sugar is known as nucleoside.
- (Statement II) When nucleoside is linked to phosphorous acid at $5'$-position of sugar moiety, we get nucleotide.

- (1) Both Statement I and Statement II are false
- **(2)** Statement I is true but Statement II is false
- (3) Statement I is false but Statement II is true
- (4) Both Statement I and Statement II are true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A nitrogenous base attached at the $1'$ position of the pentose sugar forms a nucleoside, so Statement I is true.
2. NCERT: a nucleotide forms when a nucleoside is linked to phosphoric acid ($\mathrm{H_3PO_4}$) at the $5'$ position; Statement II says phosphorous acid ($\mathrm{H_3PO_3}$), so as worded it is false.
3. Statement I true, Statement II false, which is option $2$.

**Subtopic:** Structure and Function of Nucleic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q071_7d37e7a2_02112026.png?v=7d37e7a2a790)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A nucleoside is base plus sugar; it becomes a nucleotide only when phosphoric acid esterifies the sugar's $5'$ hydroxyl
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Statement II is the book's nucleotide sentence with one word changed, phosphorous acid for phosphoric acid, so a student who checks that the linkage is at $5'$ and that the product is a nucleotide finds every structural detail familiar and grades both statements true.
- **Why:** This question requires two stated NCERT definitions to be graded separately, demonstrated by Statement II reading 'linked to phosphorous acid at $5'$-position of sugar moiety' where the book's acid is phosphoric.
<!--/ecat-->

## Q72

Chemistry · physical · Structure of Atom

The relation between $n_m$, ($n_m$ = the number of permissible values of magnetic quantum number ($m$)) for a given value of azimuthal quantum number ($l$), is

- (1) $l = 2n_m + 1$
- (2) $n_m = 2l^2 + 1$
- (3) $n_m = l + 2$
- **(4)** $l = \frac{n_m - 1}{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For a given $l$, $m$ takes the values $-l, \ldots, 0, \ldots, +l$.
2. So $n_m = 2l + 1$.
3. Rearranging, $l = \frac{n_m - 1}{2}$, which is option $4$.

**Subtopic:** Quantum Numbers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q072_bb3762b4_02112026.png?v=bb3762b4b039)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a given $l$ the magnetic quantum number runs from $-l$ to $+l$, giving $2l+1$ permitted values, so $l = (n_m-1)/2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The count is remembered as $2l+1$ with the $l$ squared, and $n_m = 2l^2+1$ survives the two cases a student is most likely to test, since it gives 1 for an s orbital and 3 for a p orbital
- **Why:** This question requires a relation derived and then rearranged, demonstrated by the options being four algebraic forms linking $n_m$ and $l$, one of them solved for $l$.
<!--/ecat-->

## Q73

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Amongst the following the total number of species NOT having eight electrons around central atom in its outer most shell, is $\mathrm{NH_3}$, $\mathrm{AlCl_3}$, $\mathrm{BeCl_2}$, $\mathrm{CCl_4}$, $\mathrm{PCl_5}$ :

- (1) 2
- (2) 4
- (3) 1
- **(4)** 3

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: N has 3 bond pairs + 1 lone pair $= 8$ electrons (octet).
2. $\mathrm{AlCl_3}$: Al has 3 bond pairs $= 6$ electrons (incomplete octet).
3. $\mathrm{BeCl_2}$: Be has 2 bond pairs $= 4$ electrons (incomplete octet).
4. $\mathrm{CCl_4}$: C has 4 bond pairs $= 8$ electrons (octet).
5. $\mathrm{PCl_5}$: P has 5 bond pairs $= 10$ electrons (expanded octet).
6. Species not having 8 electrons: $\mathrm{AlCl_3}, \mathrm{BeCl_2}, \mathrm{PCl_5}$ $= 3$, which is option $4$.

**Subtopic:** Octet Rule · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q073_5e5d44c9_02112026.png?v=5e5d44c90db2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The octet rule is broken in two directions: aluminium and beryllium halides leave the central atom short of eight electrons, while $\mathrm{PCl_5}$ puts ten around phosphorus
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The octet test is applied in one direction only -- which central atoms are short of eight -- so $\mathrm{AlCl_3}$ and $\mathrm{BeCl_2}$ are counted and the expanded octet of $\mathrm{PCl_5}$ is passed over, giving 2
- **Why:** This question requires the octet rule applied to five printed species, demonstrated by the stem listing $\mathrm{NH_3}$, $\mathrm{AlCl_3}$, $\mathrm{BeCl_2}$, $\mathrm{CCl_4}$ and $\mathrm{PCl_5}$ and asking for "the total number of species NOT having eight electrons around central atom".
- **Note:** Vocabulary gap recorded rather than forced: what the answer WANTS here is a tally, and no asks value says that. apply_rule is used because the work is the octet criterion applied to five new cases, but its definition adds "with no quantity produced", which a count of 3 breaks; calculate does not fit either, since nothing is computed from the stem's numbers. The value this axis is missing is count_qualifying_items, which the codebook's E2 axis already carries for exactly this reason, and q094 of this same paper (how many species obey Huckel's rule) is a second instance.
<!--/ecat-->

## Q74

Chemistry · physical · States of Matter

Intermolecular forces are forces of attraction and repulsion between interacting particles that will include
Choose the most appropriate answer from the options given below :

- (A) dipole - dipole forces
- (B) dipole - induced dipole forces
- (C) hydrogen bonding
- (D) covalent bonding
- (E) dispersion forces

- (1) A, B, C, D are correct
- **(2)** A, B, C, E are correct
- (3) A, C, D, E are correct
- (4) B, C, D, E are correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Dipole-dipole, dipole-induced dipole, hydrogen bonding and dispersion (London) forces act between molecules, so A, B, C and E are intermolecular forces.
2. Covalent bonding (D) holds atoms together within a molecule, so it is intramolecular and is excluded.
3. The correct set is A, B, C, E, which is option $2$.

**Subtopic:** Intermolecular Forces · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q074_27ebd495_02112026.png?v=27ebd495edfd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Intermolecular forces act between molecules - dipole-dipole, dipole-induced dipole, dispersion and hydrogen bonding - while a covalent bond holds atoms inside one molecule and is excluded by definition
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Three of its members are genuine intermolecular forces, and covalent bonding joins them once a student reads "forces of attraction and repulsion between interacting particles" as covering the bond itself, with dispersion forces left out as the unfamiliar name.
- **Why:** This question requires the membership boundary the chapter draws around intermolecular forces, demonstrated by the stem "Intermolecular forces are forces of attraction and repulsion between interacting particles that will include" with "covalent bonding" planted as item D.
<!--/ecat-->

## Q75

Chemistry · inorganic · The s-Block Elements

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Metallic sodium dissolves in liquid ammonia giving a deep blue solution, which is paramagnetic.
- (Reason R) The deep blue solution is due to the formation of amide.

- (1) Both A and R are true but R is NOT the correct explanation of A
- **(2)** A is true but R is false
- (3) A is false but R is true
- (4) Both A and R are true and R is the correct explanation of A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\mathrm{Na + (x+y)NH_3 \rightarrow [Na(NH_3)_x]^+ + [e(NH_3)_y]^-}$; the ammoniated electron gives the deep blue colour and makes the solution paramagnetic, so A is true.
2. The blue colour is due to ammoniated electrons, not amide; amide ($\mathrm{NaNH_2}$) forms only on standing ($\mathrm{Na^+ + e^- + NH_3 \rightarrow NaNH_2 + \tfrac{1}{2}H_2}$) and the blue colour is lost, so R is false: option $2$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q075_f51bc643_02112026.png?v=f51bc643dee5)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Sodium in liquid ammonia releases ammoniated electrons, and those free electrons make the dilute solution deep blue and paramagnetic; the amide appears only later, with hydrogen
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The amide is printed in the same passage as the blue solution — the solution liberates hydrogen on standing and forms the amide — so a student who has read that passage accepts the amide sentence and then lets it account for the colour it is printed beside.
- **Why:** This question requires the cause the source gives for the deep blue colour, demonstrated by R asserting 'The deep blue solution is due to the formation of amide' against A's description of a blue paramagnetic solution.
- **Note:** nearby_fact rather than look_alike_term: 'amide' and 'ammoniated electron' do not resemble each other, and replacing the amide with any other unlike species printed in the same passage would keep the pull, so position in the text is doing the work.
<!--/ecat-->

## Q76

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The element expected to form largest ion to achieve the nearest noble gas configuration is

- (1) $\mathrm{F}$
- **(2)** $\mathrm{N}$
- (3) $\mathrm{Na}$
- (4) $\mathrm{O}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. To reach the nearest noble gas configuration (Ne) the elements form $\mathrm{N^{3-}}$, $\mathrm{O^{2-}}$, $\mathrm{F^{-}}$ and $\mathrm{Na^{+}}$, which all have $10$ electrons.
2. For isoelectronic ions, radius falls as nuclear charge rises: $Z = 7 < 8 < 9 < 11$.
3. So $\mathrm{N^{3-}} > \mathrm{O^{2-}} > \mathrm{F^{-}} > \mathrm{Na^{+}}$; the largest ion comes from $\mathrm{N}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Atomic and Ionic Radius · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q076_809a56f3_02112026.png?v=809a56f310fd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Across an isoelectronic series the radius grows as the nuclear charge falls, so of the ions that reach the neon configuration the nitride ion is the largest and the sodium ion, having emptied its outer shell, is the smallest
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Sodium is true as the answer to which of these elements has the largest atom, and that ranking is handed over to a stem that asks about the ion
- **Why:** This question requires four similar cases ranked on size, demonstrated by the stem asking which element is "expected to form largest ion to achieve the nearest noble gas configuration".
<!--/ecat-->

## Q77

Chemistry · organic · Chemistry in Everyday Life

Some tranquilizers are listed below. Which one from the following belongs to barbiturates?

- (1) Meprobamate
- (2) Valium
- **(3)** Veronal
- (4) Chlordiazepoxide

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Barbiturates are derivatives of barbituric acid; NCERT lists veronal, amytal, nembutal, luminal and seconal as barbiturate tranquilizers, so Veronal (option $3$) is the barbiturate while meprobamate, Valium and chlordiazepoxide are non-barbiturate tranquilizers.

**Subtopic:** Tranquilizers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q077_dc1eac70_02112026.png?v=dc1eac70a762)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Barbiturates are the derivatives of barbituric acid -- veronal, amytal, nembutal, luminal, seconal -- and are a separate class from the benzodiazepine and carbamate tranquilizers printed in the same section
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Meprobamate is the tranquilizer the text names immediately before the barbiturate sentence, as one of the first to be designed, so a student who files the barbiturates as the earliest class reaches for the name printed next to them
- **Why:** This question requires one stated fact, which named drug belongs to a named class, demonstrated by the stem conceding that all four are tranquilizers and asking only "Which one from the following belongs to barbiturates?".
- **Note:** Swap test applied: meprobamate, valium, chlordiazepoxide and veronal do not resemble one another, so likeness is not the pull here; replacing any pair with two unlike words leaves the trap standing because it is the printed position of the names in the same section that carries the student. Hence nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q78

Chemistry · physical · Electrochemistry

> ⚠ The independent solve chose (4); the booklet prints (1).

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R
In the light of the above statements, choose the correct answer from the options given below

- (Assertion A) In equation $\Delta_{r}G = -nFE_{\mathrm{cell}}$, value of $\Delta_{r}G$ depends on n.
- (Reasons R) $E_{\mathrm{cell}}$ is an intensive property and $\Delta_{r}G$ is an extensive property.

- **(1)** Both A and R are true and R is NOT the correct explanation of A
- (2) A is true but R is false
- (3) A is false but R is true
- (4) Both A and R are true and R is the correct explanation of A

**Answer** — booklet: (1) · independent solve: (4) · differs

**Solved independently** (answer withheld)

1. $\Delta_r G = -nFE_{\mathrm{cell}}$, where $n$ is the number of moles of electrons transferred in the reaction as written, so $\Delta_r G$ changes with $n$: A is true.
2. $E_{\mathrm{cell}}$ does not depend on the amount of reactants (intensive), while $\Delta_r G$ scales with the amount of reaction (extensive): R is true.
3. Because $E_{\mathrm{cell}}$ is fixed but $\Delta_r G$ must scale with amount, the factor $n$ carries that dependence, so R correctly explains A, which is option $4$.

**Subtopic:** Nernst Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q078_42a7aeed_02112026.png?v=42a7aeeda22a)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In $\Delta_{r}G = -nFE_{\mathrm{cell}}$ the factor $n$ makes $\Delta_{r}G$ scale with the electrons transferred, while $E_{\mathrm{cell}}$, being intensive, does not change with $n$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Intensive against extensive is the pair usually quoted when a cell reaction is multiplied through, so a true R built from that pair reads as the account of A; R sorts the two quantities into classes and never names $n$, which is the factor A's claim rests on.
- **Why:** This question requires the intensive/extensive criterion applied to the two quantities in the printed equation, demonstrated by R reading '$E_{\mathrm{cell}}$ is an intensive property and $\Delta_{r}G$ is an extensive property' against A's claim about the $n$ in $\Delta_{r}G = -nFE_{\mathrm{cell}}$.
- **Note:** The key is defensible but arguable: the extensive/intensive contrast in R is often taught as exactly the reason $\Delta_{r}G$ scales with $n$ while $E_{\mathrm{cell}}$ does not, which would make option 4 correct. Tagged as printed, with option 4 carried as the trap.
<!--/ecat-->

## Q79

Chemistry · organic · Polymers

Which amongst the following molecules on polymerization produces neoprene?

- **(1)** $\mathrm{H_2C=\overset{\overset{\large Cl}{|}}{C}-CH=CH_2}$
- (2) $\mathrm{H_2C=CH-C\equiv CH}$
- (3) $\mathrm{H_2C=\overset{\overset{\large CH_3}{|}}{C}-CH=CH_2}$
- (4) $\mathrm{H_2C=CH-CH=CH_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Neoprene is formed by free-radical polymerization of chloroprene, $\mathrm{H_2C=C(Cl)-CH=CH_2}$ (2-chloro-1,3-butadiene), which is option $1$.

**Subtopic:** Natural Rubber (cis-1,4-Polyisoprene) and Vulcanisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q079_92c7d401_02112026.png?v=92c7d40100b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Neoprene is polychloroprene, so its monomer is 2-chlorobuta-1,3-diene; the methyl analogue isoprene gives natural rubber instead
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Neoprene and isoprene differ only in their first syllable, and this option is isoprene, so the monomer whose name sounds like the polymer's is taken
- **Why:** This question requires the monomer the source prints against a named polymer, demonstrated by the stem naming the product -- "on polymerization produces neoprene" -- with no condition or mechanism supplied to be reasoned from.
- **Note:** Swap test applied, and the likeness wins: neoprene against isoprene is a one-syllable difference, and if the two were renamed to unlike words the pull of option 3 would go, leaving only the general fact that a rubber monomer is a substituted diene.
<!--/ecat-->

## Q80

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Complete the following reaction [C] is ________

![printed figure: (A) cyclohexanone →(HCN) (B) 1-hydroxycyclohexane-1-carbonitrile →(conc. $\ce{H2SO4}$, Δ) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q080_3b3bfb07_02112026.png?v=3b3bfb07d071)

*[A] cyclohexanone →[HCN] [B] 1-hydroxycyclohexane-1-carbonitrile →[conc. $\ce{H2SO4}$, Δ] [C]*

![drawn: (A) cyclohexanone →(HCN) (B) 1-hydroxycyclohexane-1-carbonitrile →(conc. $\ce{H2SO4}$, Δ) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_question_9799ed66_02112026.svg?v=9799ed66a4ee)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_question_s1_ecae2398_02112026.svg?v=ecae2398c700); 1-hydroxycyclohexane-1-carbonitrile `N#CC1(O)CCCCC1` ![1-hydroxycyclohexane-1-carbonitrile](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_question_s2_21d03bff_02112026.svg?v=21d03bffc4d3)

- (1) cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_option_1_s1_5fc26872_02112026.svg?v=5fc268722cd9)
- (2) cyclohex-1-ene-1-carbaldehyde `O=CC1=CCCCC1` ![cyclohex-1-ene-1-carbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_option_2_s1_47f14bf7_02112026.svg?v=47f14bf77a4c)
- **(3)** cyclohex-1-ene-1-carboxylic acid `O=C(O)C1=CCCCC1` ![cyclohex-1-ene-1-carboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_option_3_s1_9e69062a_02112026.svg?v=9e69062a7631)
- (4) cyclohexanol `OC1CCCCC1` ![cyclohexanol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q080_option_4_s1_b130dcca_02112026.svg?v=b130dccaeb49)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cyclohexanone [A] adds HCN to give the cyanohydrin [B], 1-hydroxycyclohexane-1-carbonitrile.
2. Hot conc. $\mathrm{H_2SO_4}$ hydrolyses the nitrile: $-\mathrm{C{\equiv}N} \rightarrow -\mathrm{COOH}$.
3. Hot conc. $\mathrm{H_2SO_4}$ also dehydrates the tertiary alcohol, putting a $\mathrm{C{=}C}$ in the ring next to the carboxyl carbon.
4. So [C] is cyclohex-1-ene-1-carboxylic acid, which is option $3$.

**Subtopic:** Nucleophilic Addition Reactions, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q080_2baf85b7_02112026.png?v=2baf85b7e52e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A ketone plus HCN gives the cyanohydrin, and concentrated sulphuric acid with heat both hydrolyses the nitrile and takes out the hydroxyl, giving an unsaturated carboxylic acid
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and the packet carries all four as empty strings, so no product structure was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the product of a printed two-step scheme, demonstrated by the figure running cyclohexanone over an HCN arrow to [B] and then over a "conc. $\mathrm{H_2SO_4}$, $\Delta$" arrow to the blank [C].
- **Note:** Options 1-4 are empty in the record because they are structures; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the structures should check two mechanisms: the hydroxy acid, which is what the nitrile hydrolysis alone gives with the hydroxyl left in place, and the amide, which is the product of stopping the hydrolysis one step early.
<!--/ecat-->

## Q81

Chemistry · organic · Hydrocarbons

Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is :

- **(1)** $32$
- (2) $30$
- (3) $18$
- (4) $16$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Heating sodium ethanoate with NaOH and CaO (soda lime) is decarboxylation: $\mathrm{CH_3COONa + NaOH \xrightarrow{CaO,\,\Delta} CH_4 + Na_2CO_3}$.
2. Molar mass of $\mathrm{CH_4} = 12 + 4(1) = 16\,\mathrm{g\,mol^{-1}}$.
3. Mass of 2 mol $= 2 \times 16 = 32\,\mathrm{g}$, which is option $1$.

**Subtopic:** Preparation of Alkane · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q081_aae58f44_02112026.png?v=aae58f441e0e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Sodium ethanoate heated with sodium hydroxide and calcium oxide loses carbon dioxide and keeps a hydrogen, giving methane, whose molar mass is 16
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The product is identified correctly as methane and its molar mass, 16, is read off as the answer, with the factor of two the stem asks for left out
- **Why:** This question requires a number computed from the stem, demonstrated by "Weight (g) of two moles of the organic compound" following the named reaction conditions.
<!--/ecat-->

## Q82

Chemistry · organic · Amines

Which of the following reactions will NOT give primary amine as the product?

- (1) $\mathrm{CH_3CN} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$
- **(2)** $\mathrm{CH_3NC} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$
- (3) $\mathrm{CH_3CONH_2} \xrightarrow[\text{(ii) } \mathrm{H_3O^{\oplus}}]{\text{(i) } \mathrm{LiAlH_4}} \text{Product}$
- (4) $\mathrm{CH_3CONH_2} \xrightarrow{\mathrm{Br_2/KOH}} \text{Product}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{CH_3C{\equiv}N \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
2. Option 2: $\mathrm{CH_3N{\equiv}C \xrightarrow{LiAlH_4} CH_3NHCH_3}$, a secondary amine.
3. Option 3: $\mathrm{CH_3CONH_2 \xrightarrow{LiAlH_4} CH_3CH_2NH_2}$, a primary amine.
4. Option 4: Hofmann bromamide degradation, $\mathrm{CH_3CONH_2 \xrightarrow{Br_2/KOH} CH_3NH_2}$, a primary amine.
5. Only option $2$ does not give a primary amine.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q082_2c8a105f_02112026.png?v=2c8a105f060b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Lithium aluminium hydride reduces a nitrile and an amide to a primary amine, but an isocyanide to a secondary amine, because the carbon of $\mathrm{R{-}NC}$ is attached to nitrogen on one side and gains the new carbon-hydrogen bonds on the other
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  $\mathrm{CH_3CN}$ and $\mathrm{CH_3NC}$ differ only in the order of the two letters, so the nitrile is read as the isocyanide and ticked as the reaction that fails to give a primary amine
- **Why:** This question requires the product each printed reagent set gives, demonstrated by the four options being complete reactions and the task being to find the one that "will NOT give primary amine as the product".
- **Note:** type_patterns fired no pattern here because the options are reactions; the current qtype vocabulary has no value for that, and the printed shape is still one question with four options from which one is picked, so qtype is mcq. The retired E1 list carried reaction_options for this printing.
<!--/ecat-->

## Q83

Chemistry · physical · Basic Concepts of Chemistry

The right option for the mass of $\mathrm{CO_2}$ produced by heating $20\,\mathrm{g}$ of $20\%$ pure limestone is (Atomic mass of Ca = $40$) $\left[\mathrm{CaCO_3} \xrightarrow{1200\,\mathrm{K}} \mathrm{CaO} + \mathrm{CO_2}\right]$

- **(1)** $1.76\,\mathrm{g}$
- (2) $2.64\,\mathrm{g}$
- (3) $1.32\,\mathrm{g}$
- (4) $1.12\,\mathrm{g}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Mass of pure $\mathrm{CaCO_3} = 0.20 \times 20\,\mathrm{g} = 4\,\mathrm{g}$.
2. Molar mass of $\mathrm{CaCO_3} = 40 + 12 + 3(16) = 100\,\mathrm{g\,mol^{-1}}$.
3. $n(\mathrm{CaCO_3}) = \frac{4}{100} = 0.04\,\mathrm{mol}$.
4. From $\mathrm{CaCO_3} \rightarrow \mathrm{CaO} + \mathrm{CO_2}$ (1:1), $n(\mathrm{CO_2}) = 0.04\,\mathrm{mol}$.
5. $m(\mathrm{CO_2}) = 0.04 \times 44 = 1.76\,\mathrm{g}$, which is option $1$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q083_d5e1c6b1_02112026.png?v=d5e1c6b15f55)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Only the pure limestone reacts: 20 percent of 20 g is 4 g of $\mathrm{CaCO_3}$, which is 0.04 mol and gives 0.04 mol of $\mathrm{CO_2}$, or 1.76 g
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I worked the named slips this stem offers and none of them lands on a printed option: ignoring the purity gives $8.8$ g, weighing the $\mathrm{CaO}$ instead of the $\mathrm{CO_2}$ gives $2.24$ g, and treating the 20 percent as impurity rather than purity gives $7.04$ g, none of which is printed, while the three distractors correspond to purities of 30 and 15 percent and to a mole count that no step of this calculation produces
- **Why:** This question requires a number computed from the stem's numbers, demonstrated by "20 g of 20% pure limestone" with the balanced equation and the atomic mass of calcium supplied.
- **Note:** no_trap is a finding here, not a gap: the three distractors are spread around the key at purities the stem does not print, and I could demonstrate no single named slip -- dropped purity, wrong product weighed, purity read as impurity -- that lands on any of them.
<!--/ecat-->

## Q84

Chemistry · organic · Amines

Identify the product in the following reaction:

![printed figure: benzenediazonium chloride →((i) $\ce{Cu2Br2}$/HBr (ii) Mg/dry ether (iii) $\ce{H2O}$) Product](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q084_e1ebe722_02112026.png?v=e1ebe722ad9a)

*benzenediazonium chloride →[(i) $\ce{Cu2Br2}$/HBr (ii) Mg/dry ether (iii) $\ce{H2O}$] Product*

![drawn: benzenediazonium chloride →((i) $\ce{Cu2Br2}$/HBr (ii) Mg/dry ether (iii) $\ce{H2O}$) Product](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2023/2023_F1/figures_drawn/q084_question_5d05bc4c_03112026.svg?v=5d05bc4cf415)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzenediazonium chloride `N#[N+]c1ccccc1.[Cl-]` ![benzenediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q084_question_s1_7589eab3_02112026.svg?v=7589eab3c8e1)

- **(1)** benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q084_option_1_s1_dbf27a87_02112026.svg?v=dbf27a872e50)
- (2) phenylmagnesium bromide `[Br][Mg][c]1ccccc1` ![phenylmagnesium bromide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q084_option_2_s1_c9815f06_02112026.svg?v=c9815f069863)
- (3) 4-bromophenol `Oc1ccc(Br)cc1` ![4-bromophenol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q084_option_3_s1_fbd34b5b_02112026.svg?v=fbd34b5b0836)
- (4) phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q084_option_4_s1_b51d9a3a_02112026.svg?v=b51d9a3a6eec)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Sandmeyer reaction: $\mathrm{C_6H_5N_2^+Cl^-} \xrightarrow{\mathrm{Cu_2Br_2/HBr}} \mathrm{C_6H_5Br} + \mathrm{N_2}$.
2. Grignard formation: $\mathrm{C_6H_5Br} \xrightarrow{\mathrm{Mg/dry\ ether}} \mathrm{C_6H_5MgBr}$.
3. Hydrolysis: $\mathrm{C_6H_5MgBr} + \mathrm{H_2O} \rightarrow \mathrm{C_6H_6} + \mathrm{Mg(OH)Br}$, so the product is benzene, option $1$.

**Subtopic:** Chemical Reactions of Diazonium Salts and Coupling Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q084_00d2269a_02112026.png?v=00d2269a8282)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A diazonium salt gives the aryl bromide with $\mathrm{Cu_2Br_2/HBr}$, that bromide gives the Grignard reagent with magnesium in dry ether, and water then replaces the metal by hydrogen, so the ring ends up bare
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and the packet carries all four as empty strings, so no product structure was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the product of a printed three-step sequence, demonstrated by the scheme running benzenediazonium chloride over an arrow labelled "(i) $\mathrm{Cu_2Br_2}$/HBr (ii) Mg/dry ether (iii) $\mathrm{H_2O}$" to the word Product.
- **Note:** Options 1-4 are empty in the record because they are structures; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the structures should check two mechanisms: bromobenzene, which is the sequence stopped after step (i), and phenol, which is what the last step gives if water is read as attacking the ring rather than the carbon-magnesium bond.
<!--/ecat-->

## Q85

Chemistry · organic · General Organic Chemistry

The number of $\sigma$ bonds, $\pi$ bonds and lone pair of electrons in pyridine, respectively are:

- (1) 12, 3, 0
- **(2)** 11, 3, 1
- (3) 12, 2, 1
- (4) 11, 2, 0

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Pyridine is $\mathrm{C_5H_5N}$: a six-membered aromatic ring with one N and five C–H units.
2. Ring $\sigma$ bonds: $6$; C–H $\sigma$ bonds: $5$; total $\sigma = 6 + 5 = 11$.
3. The aromatic ring has $3$ alternating double bonds, so $\pi = 3$.
4. The $sp^2$ N carries $1$ lone pair (in the ring plane, not part of the aromatic sextet).
5. $(11, 3, 1)$ is option $2$.

**Subtopic:** Aromaticity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q085_8a756b93_02112026.png?v=8a756b938ac7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Pyridine is benzene with one CH replaced by N, so it loses a C-H sigma bond and gains a lone pair: eleven sigma bonds, three pi bonds, one lone pair
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The ring is counted as though it were benzene, with six C-H bonds and no lone pair, so twelve, three and zero is read off -- the correct triple for benzene, not for pyridine
- **Why:** This question requires three counts worked out from a structure that is not drawn, demonstrated by the stem asking for "The number of $\sigma$ bonds, $\pi$ bonds and lone pair of electrons in pyridine, respectively" with each option a triple of integers.
- **Note:** qtype is two_part because the answer is three numbers judged whole -- half an option scores nothing -- which is what type_patterns recorded as multi_part_respectively.
<!--/ecat-->

## Q86

Chemistry · physical · Thermodynamics

Which amongst the following options is the correct relation between change in enthalpy and change in internal energy?

- **(1)** $\Delta H = \Delta U + \Delta n_{g}RT$
- (2) $\Delta H - \Delta U = -\Delta nRT$
- (3) $\Delta H + \Delta U = \Delta nR$
- (4) $\Delta H = \Delta U - \Delta n_{g}RT$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. By definition $H = U + PV$, so $\Delta H = \Delta U + \Delta (PV)$.
2. For gases at constant $T$, $PV = nRT$ gives $\Delta (PV) = \Delta n_{g} RT$.
3. Hence $\Delta H = \Delta U + \Delta n_{g} RT$, which is option $1$.

**Subtopic:** Enthalpy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q086_644b4001_02112026.png?v=644b40019356)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** From $H = U + pV$ with $pV = nRT$ for the gaseous species, the enthalpy change exceeds the internal energy change by $\Delta n_g RT$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The correct rearrangement $\Delta U = \Delta H - \Delta n_g RT$ is remembered and then written with $\Delta H$ and $\Delta U$ exchanged, so the $RT$ term is subtracted from the wrong side
- **Why:** This question requires a relation derived from a definition, demonstrated by the four options being four algebraic forms linking $\Delta H$ and $\Delta U$.
- **Note:** asks is calculate on the same reading used for q072 of this paper: the answer is a symbolic expression derived from a stated definition, which the brief assigns to calculate rather than to relation, since relation is reserved for how many times one quantity changes when another does.
<!--/ecat-->

## Q87

Chemistry · organic · Alcohols, Phenols and Ethers

Consider the following reaction : [reaction scheme figure] Identify products A and B.

![printed figure: (benzyloxy)benzene →(Δ / HI) A + B](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q087_3b546dfb_02112026.png?v=3b546dfbf70b)

*(benzyloxy)benzene →[Δ / HI] A + B*

![drawn: (benzyloxy)benzene →(Δ / HI) A + B](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_question_e8dd9493_02112026.svg?v=e8dd94934709)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: (benzyloxy)benzene `c1ccc(COc2ccccc2)cc1` ![(benzyloxy)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_question_s1_f059e8f0_02112026.svg?v=f059e8f02f11)

- (1) phenylmethanol `OCc1ccccc1` ![phenylmethanol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_1_s1_76b1501e_02112026.svg?v=76b1501e4315); iodobenzene `Ic1ccccc1` ![iodobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_1_s2_1d87e391_02112026.svg?v=1d87e3910938) — A =, $\mathrm{-CH_2OH}$ and B =, $\mathrm{-I}$
- **(2)** (iodomethyl)benzene `ICc1ccccc1` ![(iodomethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_2_s1_c8defd7a_02112026.svg?v=c8defd7a0f2d); phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_2_s2_26093786_02112026.svg?v=26093786dda8) — A =, $\mathrm{-CH_2I}$ and B =, $\mathrm{-OH}$
- (3) toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_3_s1_b4bc3ebf_02112026.svg?v=b4bc3ebff656); iodobenzene `Ic1ccccc1` ![iodobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_3_s2_1d87e391_02112026.svg?v=1d87e3910938) — A =, $\mathrm{-CH_3}$ and B =, $\mathrm{-I}$
- (4) toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_4_s1_b4bc3ebf_02112026.svg?v=b4bc3ebff656); phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q087_option_4_s2_26093786_02112026.svg?v=26093786dda8) — A =, $\mathrm{-CH_3}$ and B =, $\mathrm{-OH}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Protonation of the ether oxygen by HI gives $\mathrm{C_6H_5CH_2-\overset{+}{O}H-C_6H_5}$.
2. The aryl $\mathrm{C-O}$ bond has partial double-bond character and phenyl cations do not form, so cleavage occurs at the benzyl $\mathrm{CH_2-O}$ bond, which gives a stable benzyl carbocation.
3. $\mathrm{I^-}$ attacks the benzyl carbon: $\mathrm{C_6H_5CH_2I}$ (A), and phenol $\mathrm{C_6H_5OH}$ (B) is released.
4. A $= \mathrm{C_6H_5CH_2I}$, B $= \mathrm{C_6H_5OH}$, which is option $2$.

**Subtopic:** Reactions of Ethers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q087_bb8e8851_02112026.png?v=bb8e8851480b)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hot HI cleaves an ether at the carbon that can take a nucleophile, and in benzyl phenyl ether that is the benzylic $\mathrm{CH_2}$, so the iodide goes to the side chain and the ring keeps the oxygen as phenol
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  The iodide is sent to the ring carbon instead of the benzylic carbon, which turns the products round into iodobenzene and benzyl alcohol
- **Why:** This question requires the products of a printed reaction, demonstrated by the scheme sending benzyl phenyl ether over a "$\Delta$ / HI" arrow to "A + B" and each option fixing both A and B together.
- **Note:** type_patterns returned plain_mcq, but each option fixes two products at once ("A = ... and B = ...") and half an option scores nothing, so the printed shape is recorded as two_part. The figure note records that some glyphs in the crop are inverted, which does not affect the structure read here.
<!--/ecat-->

## Q88

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which of the following statements are INCORRECT? Choose the correct answer from the options given below:

- (A) All the transition metals except scandium form $\mathrm{MO}$ oxides which are ionic.
- (B) The highest oxidation number corresponding to the group number in transition metal oxides is attained in $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$.
- (C) Basic character increases from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_4}$ to $\mathrm{V_2O_5}$.
- (D) $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO_4^{3-}}$ salts.
- (E) $\mathrm{CrO}$ is basic but $\mathrm{Cr_2O_3}$ is amphoteric.

- (1) B and D only
- **(2)** C and D only
- (3) B and C only
- (4) A and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A: all transition metals except Sc form ionic $\mathrm{MO}$ oxides, so A is correct.
2. B: oxides from $\mathrm{Sc_2O_3}$ to $\mathrm{Mn_2O_7}$ show the highest oxidation state equal to the group number, so B is correct.
3. C: as oxidation state of V rises, $\mathrm{V_2O_3}$ (basic) $\to$ $\mathrm{V_2O_4}$ (less basic) $\to$ $\mathrm{V_2O_5}$ (amphoteric), so basic character decreases and C is incorrect.
4. D: $\mathrm{V_2O_4}$ dissolves in acids to give $\mathrm{VO^{2+}}$ salts, not $\mathrm{VO_4^{3-}}$, so D is incorrect.
5. E: $\mathrm{CrO}$ is basic and $\mathrm{Cr_2O_3}$ is amphoteric, so E is correct.
6. Incorrect statements are C and D, which is option $2$.

**Subtopic:** Transition Elements (d-Block) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q088_ae810d35_02112026.png?v=ae810d350ae3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxides of the first transition series: basic character falls as the oxidation state rises from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_5}$, and $\mathrm{V_2O_4}$ dissolves in acid as the vanadyl $\mathrm{VO^{2+}}$ ion, not as a vanadate
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  C is genuinely one of the incorrect statements, and B joins it once a student who knows the oxidation-number-equals-group-number coincidence breaks after manganese reads B as making that claim across the whole series.
- **Why:** This question requires printed statements about transition metal oxides checked against the chapter's own lines under a negated task, demonstrated by the stem "Which of the following statements are INCORRECT?" set against statement C, "Basic character increases from $\mathrm{V_2O_3}$ to $\mathrm{V_2O_4}$ to $\mathrm{V_2O_5}$".
<!--/ecat-->

## Q89

Chemistry · organic · Alcohols, Phenols and Ethers

> ⚠ The independent solve chose (2); the booklet prints (3).

Which amongst the following be most readily dehydrated under acidic conditions?

- (1) pentane-2,4-diol `CC(O)CC(C)O` ![pentane-2,4-diol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q089_option_1_s1_c43e7c26_02112026.svg?v=c43e7c26414c)
- (2) 3-nitrobutane-1,2-diol `CC(C(O)CO)[N+](=O)[O-]` ![3-nitrobutane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q089_option_2_s1_0c486a98_02112026.svg?v=0c486a9853f8)
- **(3)** 5-nitrohexan-2-ol `CC(O)CCC(C)[N+](=O)[O-]` ![5-nitrohexan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q089_option_3_s1_01d96399_02112026.svg?v=01d96399b884)
- (4) 4-nitropentan-2-ol `CC(O)CC(C)[N+](=O)[O-]` ![4-nitropentan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q089_option_4_s1_9ee8793c_02112026.svg?v=9ee8793c8aab)

**Answer** — booklet: (3) · independent solve: (2) · differs

**Solved independently** (answer withheld)

1. Read the options: (1) $\mathrm{CH_3CH(OH)CH_2CH(OH)CH_3}$; (2) $\mathrm{CH_3CH(NO_2)CH(OH)CH_2OH}$; (3) $\mathrm{CH_3CH(NO_2)CH_2CH_2CH(OH)CH_3}$; (4) $\mathrm{CH_3CH(NO_2)CH_2CH(OH)CH_3}$.
2. In (2) the $\alpha$-H on the $\mathrm{C{-}NO_2}$ carbon is acidic and lies on the carbon adjacent to $\mathrm{C{-}OH}$.
3. Loss of $\mathrm{H_2O}$ across these two carbons gives $\mathrm{CH_3C(NO_2){=}CH{-}CH_2OH}$, a $\mathrm{C{=}C}$ conjugated with $\mathrm{NO_2}$, which is stabilised.
4. In (3) and (4) the $\mathrm{NO_2}$ carbon is not adjacent to $\mathrm{C{-}OH}$, and (1) has no activating group, so no conjugated alkene forms; hence option $2$.

**Subtopic:** Reactions of Alcohols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q089_9c7c437f_02112026.png?v=9c7c437f7428)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Acid-catalysed dehydration of an alcohol goes through a carbocation, so the alcohol that gives the most stable cation loses water most readily
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and the packet carries all four as empty strings, so the four alcohols being compared were not supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires four similar cases ranked on how readily they react, demonstrated by the stem's superlative -- "most readily dehydrated under acidic conditions".
- **Note:** Options 1-4 are empty in the record because they are structures; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the structures should check the usual mechanism on this item: the least substituted alcohol picked because it looks least hindered, where the ranking actually follows carbocation stability, tertiary before secondary before primary.
<!--/ecat-->

## Q90

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

The reaction that does NOT take place in a blast furnace between $900\,\mathrm{K}$ to $1500\,\mathrm{K}$ temperature range during extraction of iron is :

- (1) $\mathrm{FeO + CO \rightarrow Fe + CO_2}$
- (2) $\mathrm{C + CO_2 \rightarrow 2CO}$
- (3) $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$
- **(4)** $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the blast furnace, the $500$-$800\,\mathrm{K}$ zone has $\mathrm{3Fe_2O_3 + CO \rightarrow 2Fe_3O_4 + CO_2}$, $\mathrm{Fe_3O_4 + 4CO \rightarrow 3Fe + 4CO_2}$ and $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$.
2. The $900$-$1500\,\mathrm{K}$ zone has $\mathrm{C + CO_2 \rightarrow 2CO}$ and $\mathrm{FeO + CO \rightarrow Fe + CO_2}$; limestone decomposes and $\mathrm{CaO + SiO_2 \rightarrow CaSiO_3}$ forms slag in the hotter region.
3. So $\mathrm{Fe_2O_3 + CO \rightarrow 2FeO + CO_2}$ does not take place at $900$-$1500\,\mathrm{K}$, which is option $4$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q090_a0b7d357_02112026.png?v=a0b7d357c53b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The blast furnace is printed as two temperature bands: $\mathrm{Fe_2O_3}$ is reduced to FeO by CO in the cooler 500-800 K zone, while 900-1500 K holds the reduction of FeO to iron, the regeneration of CO from coke, and slag formation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The two carbon monoxide reductions of iron oxide are held the wrong way round, so the FeO step is filed in the cooler zone and read as the reaction that does not take place in the printed range
- **Why:** This question requires a stated fact about which reaction the source prints in which temperature band, demonstrated by the stem fixing the band -- "between $900\,\mathrm{K}$ to $1500\,\mathrm{K}$" -- while all four equations are real furnace reactions.
- **Note:** Swap test applied on the nearby_fact / look_alike_term boundary: option 1 and the key are two equations rather than two names, and what carries the student is that the furnace scheme prints the two CO reductions in adjacent temperature bands, so position does the work and the label is nearby_fact.
<!--/ecat-->

## Q91

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the major product obtained in the following reaction: [figure] $+\,2\left[\mathrm{Ag(NH_3)_2}\right]^{+} +$ $3\,^{-}\mathrm{OH} \xrightarrow{\Delta}$ major product

![printed figure: 2-acetylbenzaldehyde + 2$\ce{(Ag(NH3)2)+}$ +](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q091_a3298ec0_02112026.png?v=a3298ec0bdac)

*2-acetylbenzaldehyde + 2$\ce{[Ag(NH3)2]+}$ +*

![drawn: 2-acetylbenzaldehyde + 2$\ce{(Ag(NH3)2)+}$ +](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_question_32a537b6_02112026.svg?v=32a537b6f2c4)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2-acetylbenzaldehyde `CC(=O)c1ccccc1C=O` ![2-acetylbenzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_question_s1_a0144de1_02112026.svg?v=a0144de11df3); diamminesilver(I) `[NH3]->[Ag+]<-[NH3]` ![diamminesilver(I)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_question_s2_919f617f_02112026.svg?v=919f617f4899)

- (1) 1-[2-(hydroxymethyl)phenyl]ethan-1-one `CC(=O)c1ccccc1CO` ![1-(2-(hydroxymethyl)phenyl)ethan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_option_1_s1_7d7073d0_02112026.svg?v=7d7073d0e417)
- **(2)** 2-acetylbenzoate `CC(=O)c1ccccc1C(=O)[O-]` ![2-acetylbenzoate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_option_2_s1_b2b6129c_02112026.svg?v=b2b6129c94a6)
- (3) 2-(1-hydroxyethyl)benzoate `CC(O)c1ccccc1C(=O)[O-]` ![2-(1-hydroxyethyl)benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_option_3_s1_ad108def_02112026.svg?v=ad108def0c1a)
- (4) 1-[2-(hydroxymethyl)phenyl]ethan-1-ol `CC(O)c1ccccc1CO` ![1-(2-(hydroxymethyl)phenyl)ethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q091_option_4_s1_94ca89a2_02112026.svg?v=94ca89a2ada8)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Tollens' reagent $[\mathrm{Ag(NH_3)_2}]^{+}$ in $^{-}\mathrm{OH}$ is a mild oxidant that oxidises aldehydes but not ketones.
2. The $-\mathrm{CHO}$ group is oxidised to $-\mathrm{COO^-}$: $\mathrm{RCHO} + 2[\mathrm{Ag(NH_3)_2}]^{+} + 3\,\mathrm{OH^-} \rightarrow \mathrm{RCOO^-} + 2\mathrm{Ag} + 4\mathrm{NH_3} + 2\mathrm{H_2O}$.
3. The $-\mathrm{COCH_3}$ group is not reduced or oxidised, so the product is 2-acetylbenzoate, which is option $2$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q091_a51795a2_02112026.png?v=a51795a2f4e4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Tollens' reagent oxidises an aldehyde and leaves a ketone untouched, so in a molecule carrying both only the CHO becomes a carboxylate
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and the packet carries all four as empty strings, so no product structure was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the product of a printed reaction, demonstrated by the equation setting the substrate against "2$\mathrm{[Ag(NH_3)_2]^{+}}$" and "3 $\mathrm{^{-}OH}$" over a heated arrow to the major product.
- **Note:** Options 1-4 are empty in the record because they are structures; the printed paper carries them. This is a limit of what reached this step and not damage to the paper, so no trap is written. A reviewer holding the structures should check two mechanisms: a product in which the acetyl group has been oxidised as well, which Tollens' reagent cannot do, and the free acid rather than the carboxylate, when the stem supplies three hydroxide ions.
<!--/ecat-->

## Q92

Chemistry · physical · The Solid State

What fraction of one edge centred octahedral void lies in one unit cell of fcc?

- (1) $\frac{1}{3}$
- **(2)** $\frac{1}{4}$
- (3) $\frac{1}{12}$
- (4) $\frac{1}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. An octahedral void at an edge centre of the fcc cell lies on an edge shared by $4$ unit cells.
2. Fraction belonging to one unit cell $= \frac{1}{4}$, which is option $2$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q092_4a6f4e51_02112026.png?v=4a6f4e516266)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A position at the centre of an edge is shared by four unit cells, so one quarter of an edge-centred octahedral void belongs to any one cell
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The sharing fractions are recalled as a list -- corner one eighth, edge one quarter, face one half, body centre one -- and the entry next to the right one is taken, so the face value of one half is read for an edge
- **Why:** This question requires a sharing convention applied to a named position, demonstrated by the stem asking what fraction of "one edge centred octahedral void lies in one unit cell".
<!--/ecat-->

## Q93

Chemistry · physical · Chemical Equilibrium

The equilibrium concentrations of the species in the reaction $\mathrm{A + B \rightleftharpoons C + D}$ are 2, 3, 10 and $6\,\mathrm{mol\,L^{-1}}$, respectively at $300\,\mathrm{K}$. $\Delta G^{\circ}$ for the reaction is ($R = 2\,\mathrm{cal/mol\,K}$)

- (1) $-137.26\,\mathrm{cal}$
- **(2)** $-1381.80\,\mathrm{cal}$
- (3) $-13.73\,\mathrm{cal}$
- (4) $-1372.60\,\mathrm{cal}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $K = \frac{[\mathrm{C}][\mathrm{D}]}{[\mathrm{A}][\mathrm{B}]} = \frac{10 \times 6}{2 \times 3} = 10$.
2. $\Delta G^{\circ} = -2.303\,RT \log K$.
3. $\Delta G^{\circ} = -2.303 \times 2 \times 300 \times \log 10 = -2.303 \times 600 \times 1$.
4. $\Delta G^{\circ} = -1381.8\,\mathrm{cal}$, which is option $2$.

**Subtopic:** Relationship Between K, Q and G · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q093_c60e5d7b_02112026.png?v=c60e5d7b9dd6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The equilibrium constant comes from the product concentrations over the reactant concentrations, and $\Delta G^{\circ} = -RT\ln K$ turns it into a free energy
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The remembered gas constant $1.987\,\mathrm{cal/mol\,K}$ is used in place of the $R = 2$ the stem supplies, which gives $1.987 \times 300 \times 2.303 = 1372.6$ instead of $1381.8$
- **Why:** This question requires a number computed from the stem's numbers, demonstrated by the four concentrations, the temperature and "($R = 2\,\mathrm{cal/mol\,K}$)" all being supplied and the options being values of $\Delta G^{\circ}$.
- **Note:** type_patterns returned multi_part_respectively, which the word "respectively" in the stem triggered, but there it describes the four concentrations going in, not the answer: the answer is a single value, so qtype is mcq.
<!--/ecat-->

## Q94

Chemistry · organic · General Organic Chemistry

Consider the following compounds/species: [figure: structures i.–vii.] The number of compounds/species which obey Huckel’s rule is ______.

![printed figure: i. naphthalene; ii. cyclopentadienide anion; iii. cyclobutadiene; iv. cyclopropenide anion; v. cyclopropenylium cation; vi. cyclooctatetraene; vii. anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q094_218467bd_02112026.png?v=218467bdc9f5)

*i. naphthalene; ii. cyclopentadienide anion; iii. cyclobutadiene; iv. cyclopropenide anion; v. cyclopropenylium cation; vi. cyclooctatetraene; vii. anthracene*

![drawn: i. naphthalene; ii. cyclopentadienide anion; iii. cyclobutadiene; iv. cyclopropenide anion; v. cyclopropenylium cation; vi. cyclooctatetraene; vii. anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_486ac994_02112026.svg?v=486ac99419f4)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: naphthalene `c1ccc2ccccc2c1` ![naphthalene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s1_1c4ddda0_02112026.svg?v=1c4ddda09622); cyclopenta-2,4-dien-1-ide `c1cc[cH-]c1` ![cyclopenta-2,4-dien-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s2_3e03e8a7_02112026.svg?v=3e03e8a741d1); cyclobuta-1,3-diene `C1=CC=C1` ![cyclobuta-1,3-diene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s3_68eaa57e_02112026.svg?v=68eaa57ee7c4); cycloprop-2-en-1-ide `C1=C[CH-]1` ![cycloprop-2-en-1-ide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s4_743bf84c_02112026.svg?v=743bf84c231a); cycloprop-2-en-1-ylium `c1c[cH+]1` ![cycloprop-2-en-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s5_afa2b3f9_02112026.svg?v=afa2b3f913ea); cycloocta-1,3,5,7-tetraene `C1=CC=CC=CC=C1` ![cycloocta-1,3,5,7-tetraene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s6_05a705c0_02112026.svg?v=05a705c03822); anthracene `c1ccc2cc3ccccc3cc2c1` ![anthracene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q094_question_s7_d63f99db_02112026.svg?v=d63f99db8ebd)

- (1) 6
- (2) 2
- (3) 5
- **(4)** 4

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. i. Naphthalene: planar, cyclic, conjugated with $10\,\pi$ electrons $= 4(2)+2$, so it obeys Huckel's rule.
2. ii. Cyclopentadienyl anion: $4\,\pi$ electrons from two C=C plus the lone pair gives $6\,\pi$ electrons $= 4(1)+2$, so it obeys.
3. iii. Cyclobutadiene: $4\,\pi$ electrons $= 4n$ with $n=1$, antiaromatic, does not obey.
4. iv. Cyclopropenyl anion: $2\,\pi$ from C=C plus the lone pair gives $4\,\pi$ electrons $= 4n$, does not obey.
5. v. Cyclopropenyl cation: $2\,\pi$ electrons $= 4(0)+2$, so it obeys.
6. vi. Cyclooctatetraene: $8\,\pi$ electrons $= 4n$ and tub-shaped (non-planar), does not obey.
7. vii. Anthracene: $14\,\pi$ electrons $= 4(3)+2$, so it obeys.
8. Species obeying: i, ii, v, vii, so the count is $4$, which is option $4$.

**Subtopic:** Aromaticity · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 22)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q094_7e637279_02112026.png?v=7e63727934d4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Huckel's rule needs a planar ring with $4n+2$ delocalised pi electrons: naphthalene, anthracene, the cyclopentadienide anion and the cyclopropenylium cation qualify; cyclobutadiene, the cyclopropenide anion and tub-shaped cyclooctatetraene do not
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The rule is replaced by a remembered example -- that a cyclic anion like the cyclopentadienide ion is aromatic -- so the cyclopropenide anion is counted in as well and the tally comes to 5
- **Why:** This question requires Huckel's rule applied to seven printed species, demonstrated by the stem asking for "The number of compounds/species which obey Huckel's rule" over the lettered list i to vii.
- **Note:** Same vocabulary gap as q073 of this paper: what the answer wants is a tally, and no asks value states counting. apply_rule is used because the work is one rule adjudicated over seven printed cases, and the value this axis is missing, count_qualifying_items, is recorded here rather than forced in. The figure note reports a stray printed dot beside species v, which does not change its charge or its electron count.
<!--/ecat-->

## Q95

Chemistry · inorganic · Coordination Compounds – Practice

Which complex compound is most stable?

- (1) $\mathrm{[Co(NH_3)_3(NO_3)_3]}$
- **(2)** $\mathrm{[CoCl_2(en)_2]NO_3}$
- (3) $\mathrm{[Co(NH_3)_6]_2(SO_4)_3}$
- (4) $\mathrm{[Co(NH_3)_4(H_2O)Br](NO_3)_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Options $1$, $3$ and $4$ contain only monodentate ligands ($\mathrm{NH_3}$, $\mathrm{NO_3^-}$, $\mathrm{H_2O}$, $\mathrm{Br^-}$).
2. Option $2$, $\mathrm{[CoCl_2(en)_2]NO_3}$, contains two bidentate $\mathrm{en}$ ligands that form chelate rings with $\mathrm{Co^{3+}}$.
3. Chelation (chelate effect) greatly increases complex stability, so option $2$ is the most stable.

**Subtopic:** Ligands · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q095_47bcfaba_02112026.png?v=47bcfaba3b7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** A chelating ligand makes a complex more stable than the same metal with the equivalent number of separate ligands, which is why the bis(ethylenediamine) complex is picked out here
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The hexaammine cobalt(III) complex is the stable complex the chapter builds its examples on, so it is reached for whenever stability is asked about, without the chelate ring being weighed against it
- **Why:** This question requires four similar complexes ranked on one property, demonstrated by the stem's superlative -- "Which complex compound is most stable?" -- with four formulae and no criterion stated.
- **Note:** The key rests on the chelate effect taught in the chapter. Option 3 is itself a famously stable complex, which is what gives it its pull; recorded here as the pull rather than as a challenge to the key.
<!--/ecat-->

## Q96

Chemistry · physical · Redox Reactions

On balancing the given redox reaction, $\mathrm{aCr_2O_7^{2-} + bSO_3^{2-}(aq) + cH^{+}(aq) \rightarrow 2aCr^{3+}(aq) + bSO_4^{2-}(aq) + \frac{c}{2}H_2O(l)}$ the coefficients a, b and c are found to be, respectively-

- (1) 3, 8, 1
- (2) 1, 8, 3
- (3) 8, 1, 3
- **(4)** 1, 3, 8

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Oxidation states: Cr in $\mathrm{Cr_2O_7^{2-}}$ is $+6$, in $\mathrm{Cr^{3+}}$ is $+3$; S in $\mathrm{SO_3^{2-}}$ is $+4$, in $\mathrm{SO_4^{2-}}$ is $+6$.
2. Electrons gained per $\mathrm{Cr_2O_7^{2-}}$: $2 \times 3 = 6$; electrons lost per $\mathrm{SO_3^{2-}}$: $2$.
3. Equate electrons: $6a = 2b \Rightarrow b = 3a$; take $a = 1$, $b = 3$.
4. Charge balance: left $-2 - 6 + c$, right $2(+3) + 3(-2) = 0$, so $c - 8 = 0 \Rightarrow c = 8$.
5. Check oxygen: left $7 + 9 = 16$, right $12 + \frac{c}{2} = 12 + 4 = 16$. Balanced.
6. $a, b, c = 1, 3, 8$, which is option $4$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q096_cb0ae73b_02112026.png?v=cb0ae73b33a3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Balancing this redox equation fixes the coefficients from the electron count -- six electrons taken by each dichromate, two given by each sulphite -- and then from the charge, giving $a=1$, $b=3$, $c=8$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The three coefficients 1, 3 and 8 are worked out correctly and then the larger two are put on the wrong letters, so the sulphite takes 8 and the hydrogen ion 3
- **Why:** This question requires three coefficients worked out from the printed equation, demonstrated by the stem asking for "the coefficients a, b and c" of the half-balanced equation "respectively".
- **Note:** qtype is two_part because the answer is three coefficients judged whole, which is what type_patterns recorded as multi_part_respectively.
<!--/ecat-->

## Q97

Chemistry · inorganic · Environmental Chemistry

Given below are two statements :
Statement I : The nutrient deficient water bodies lead to eutrophication
Statement II : Eutrophication leads to decrease in the level of oxygen in the water bodies.
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The nutrient deficient water bodies lead to eutrophication
- (Statement II) Eutrophication leads to decrease in the level of oxygen in the water bodies.

- (1) Both Statement I and Statement II are false
- (2) Statement I is correct but Statement II is false.
- **(3)** Statement I is incorrect but Statement II is true.
- (4) Both Statement I and Statement II are true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I is false: eutrophication results from nutrient enrichment (e.g. nitrates, phosphates) of water bodies, not nutrient deficiency.
2. Statement II is true: algal blooms and their decomposition by microbes reduce the dissolved oxygen in the water.
3. Statement I incorrect and Statement II true, which is option $3$.

**Subtopic:** Water Pollution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q097_dabd66bf_02112026.png?v=dabd66bf7ce2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Eutrophication is nutrient enrichment of a water body, and the decay of the bloom it produces is what strips the water of dissolved oxygen
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Statement I carries the right vocabulary with its direction inverted, nutrient deficient where the book says nutrient enriched, and Statement II is true as printed, so a student who verifies the oxygen claim reads the pair as a matched cause and effect and grades both true.
- **Why:** This question requires one stated fact about what starts eutrophication and one about what it does to be graded separately, demonstrated by Statement I reading 'The nutrient deficient water bodies lead to eutrophication'.
<!--/ecat-->

## Q98

Chemistry · organic · Haloalkanes and Haloarenes

Identify the final product [D] obtained in the following sequence of reactions. $\mathrm{CH_3CHO} \xrightarrow[\text{ii) } \mathrm{H_3O^+}]{\text{i) } \mathrm{LiAlH_4}} [A] \xrightarrow[\Delta]{\mathrm{H_2SO_4}} [B]$ [figure]

![printed figure: →(HBr) (C) →(bromobenzene, Na/dry ether) (D)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q098_c9444b16_02112026.png?v=c9444b16decd)

*→[HBr] [C] →[bromobenzene, Na/dry ether] [D]*

![drawn: →(HBr) (C) →(bromobenzene, Na/dry ether) (D)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q098_question_19a8cda2_02112026.svg?v=19a8cda260cf)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q098_question_s1_61d2ed9e_02112026.svg?v=61d2ed9ebe04)

- (1) biphenyl `c1ccc(-c2ccccc2)cc1` ![biphenyl](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q098_option_1_s1_96946bcf_02112026.svg?v=96946bcfe353)
- (2) $\mathrm{C_4H_{10}}$
- (3) $\mathrm{HC \equiv C^{\ominus}Na^{+}}$
- **(4)** ethylbenzene `CCc1ccccc1` ![ethylbenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_drawn/q098_option_4_s1_c3cd0ee9_02112026.svg?v=c3cd0ee97328)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CHO} \xrightarrow{\text{LiAlH}_4,\ \mathrm{H_3O^+}} \mathrm{CH_3CH_2OH}$ = [A].
2. $\mathrm{CH_3CH_2OH} \xrightarrow{\text{conc. } \mathrm{H_2SO_4},\ \Delta} \mathrm{CH_2{=}CH_2}$ = [B].
3. $\mathrm{CH_2{=}CH_2} + \mathrm{HBr} \rightarrow \mathrm{CH_3CH_2Br}$ = [C].
4. Wurtz-Fittig: $\mathrm{CH_3CH_2Br} + \mathrm{C_6H_5Br} \xrightarrow{\text{Na, dry ether}} \mathrm{C_6H_5CH_2CH_3}$ = [D], ethylbenzene, which is the drawing in option $4$.

**Subtopic:** Reactions of Haloarenes · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 24)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q098_9792b78e_02112026.png?v=9792b78ebee1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Wurtz-Fittig coupling: an alkyl halide and an aryl halide with sodium in dry ether join to give an alkyl-substituted benzene
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  options 1 and 4 are stored as empty strings and the printed key is option 4, so the option set cannot be read to find what pulls; only options 2 and 3 carry text
- **Why:** This question requires carrying a four-step scheme to its product and naming what Na in dry ether does to an alkyl halide plus an aryl halide, demonstrated by the stem "Identify the final product [D] obtained in the following sequence of reactions" with the figure reading "→[HBr] [C] →[bromobenzene, Na/dry ether] [D]".
- **Note:** Options 1 and 4 are empty in our record and the key points at option 4, so the option set is incomplete and no auditable trap can be written. E1 called this arrange_in_order; the printed shape is a multi-arrow reaction scheme with compound options, so it is recorded as mcq because the current qtype list has no scheme value. A reviewer holding the full option set should check whether $\mathrm{C_4H_{10}}$ (option 2) is placed as the Wurtz self-coupling of two bromoethane molecules offered in place of the Wurtz-Fittig product ethylbenzene, and whether option 3, sodium acetylide, is reachable at all once the full options are restored.
<!--/ecat-->

## Q99

Chemistry · physical · Surface Chemistry

Pumice stone is an example of

- (1) Gel
- **(2)** Solid sol
- (3) Foam
- (4) Sol

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Pumice stone has gas as the dispersed phase in a solid dispersion medium; per the NCERT colloid table, gas-in-solid is a solid sol, which is option $2$.

**Subtopic:** Classification of Colloids by Dispersed Phase and Dispersion Medium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q099_513b58bd_02112026.png?v=513b58bdfa81)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A colloid is named from its dispersed phase and its dispersion medium; gas dispersed in a solid is a solid sol, and pumice stone is NCERT's own example of it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Pumice stone is a frozen froth, so a student who fixes the dispersed phase as gas and then takes the medium from the next row of the colloid table lands on foam, which is gas in a liquid.
- **Why:** This question requires the colloid type that NCERT's table prints against a named example, demonstrated by the stem "Pumice stone is an example of" and four options that are type names rather than phase descriptions, so nothing in the stem supplies a criterion to apply.
- **Note:** On the nearby_fact against look_alike_term test: option 4 Sol does resemble the key Solid sol, but the pull that the question is built on sits on option 3 Foam, where the two names do not resemble each other at all and the adjacent table row is doing the work. Swap Foam for an unlike word and that trap survives, because position carries it. The look-alike route on Sol is recorded in other_options rather than as the question's one trap.
<!--/ecat-->

## Q100

Chemistry · inorganic · The p–Block Elements

Match List-I with List – II : List-I (Oxoacids of Sulphur) List-II (Bonds) Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | Peroxodisulphuric acid | I | Two $\mathrm{S{-}OH}$, Four $\mathrm{S{=}O}$, One $\mathrm{S{-}O{-}S}$ |
| B | Sulphuric acid | II | Two $\mathrm{S{-}OH}$, One $\mathrm{S{=}O}$ |
| C | Pyrosulphuric acid | III | Two $\mathrm{S{-}OH}$, Four $\mathrm{S{=}O}$, One $\mathrm{S{-}O{-}O{-}S}$ |
| D | Sulphurous acid | IV | Two $\mathrm{S{-}OH}$, Two $\mathrm{S{=}O}$ |

- **(1)** A–III, B–IV, C–I, D–II
- (2) A–I, B–III, C–IV, D–II
- (3) A–III, B–IV, C–II, D–I
- (4) A–I, B–III, C–II, D–IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Peroxodisulphuric acid $\mathrm{H_2S_2O_8}$: $\mathrm{HO{-}S(O_2){-}O{-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}O{-}S}$, so $A \to III$.
2. Sulphuric acid $\mathrm{H_2SO_4}$: $\mathrm{(HO)_2S(=O)_2}$ has two $\mathrm{S{-}OH}$ and two $\mathrm{S{=}O}$, so $B \to IV$.
3. Pyrosulphuric acid $\mathrm{H_2S_2O_7}$: $\mathrm{HO{-}S(O_2){-}O{-}S(O_2){-}OH}$ has two $\mathrm{S{-}OH}$, four $\mathrm{S{=}O}$ and one $\mathrm{S{-}O{-}S}$, so $C \to I$.
4. Sulphurous acid $\mathrm{H_2SO_3}$: $\mathrm{(HO)_2S{=}O}$ has two $\mathrm{S{-}OH}$ and one $\mathrm{S{=}O}$, so $D \to II$.
5. $A{-}III,\ B{-}IV,\ C{-}I,\ D{-}II$ is option $1$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q100_d171b9b8_02112026.png?v=d171b9b81e5a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The oxoacids of sulphur are told apart by their bonds: sulphuric has two S-OH and two S=O, sulphurous one S=O, pyrosulphuric a single S-O-S bridge between two sulphurs, and peroxodisulphuric a peroxide S-O-O-S bridge
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Nothing in the name "pyrosulphuric" announces two sulphur atoms the way "peroxodisulphuric" does, so read as a one-sulphur acid it cannot carry "Four S=O" and takes the one-S=O entry instead. That leaves "Two S-OH, Four S=O, One S-O-S" for sulphurous acid, $\mathrm{H_2SO_3}$, which has a single sulphur and nothing for a bridge to join.
- **Why:** This question requires the bond count printed for each named oxoacid of sulphur, demonstrated by List-II separating "One $\mathrm{S{-}O{-}S}$" from "One $\mathrm{S{-}O{-}O{-}S}$" with every other word in the two entries identical, so each row is answered by the structure the source gives for that acid.
- **Note:** What starts the slip on option 3 is that "pyrosulphuric" looks like "sulphuric" and so reads as a one-sulphur acid, but the two items actually exchanged — pyrosulphuric and sulphurous — are not alike, and the entry handed to each is the true bond count of an acid printed in the same set, so the swap test puts this in the nearby_fact family rather than look_alike_term; the live axis also folds the retired `wrong_pairing` into nearby_fact. The peroxo/pyro likeness is the route carried on option 2, and it is not the question's one trap because walking it also forces a peroxide bridge onto sulphuric acid. The stored stem has swallowed the two column headers into the instruction line ("List-I (Oxoacids of Sulphur) List-II (Bonds)"); nothing is missing, so this is not damage.
<!--/ecat-->

## Q101

Biology · botany · Plant Growth and Development

Which hormone promotes internode/petiole elongation in deep water rice?

- (1) Kinetin
- **(2)** Ethylene
- (3) 2, 4-D
- (4) $\mathrm{GA_3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT Class 11 (Plant Growth) states that ethylene promotes rapid internode/petiole elongation in deep water rice plants, so the answer is option $2$ (Ethylene).

**Subtopic:** Ethylene and Abscisic Acid · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q101_8cd03f0c_02112026.png?v=8cd03f0c28e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ethylene is the hormone printed for rapid internode and petiole elongation in deep water rice, letting the shoot keep above rising water
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Elongation of internodes is the headline job of the gibberellins, so a student holding 'GA elongates stems' answers from the general line instead of the specific one; deep water rice is the case the chapter prints against ethylene.
- **Why:** This question requires the one line the chapter prints about deep water rice, demonstrated by the stem naming that case specifically — 'internode/petiole elongation in deep water rice' — rather than elongation in general.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: 'ethylene' and 'GA$_3$' resemble each other in no way, and replacing them with two unlike names leaves the pull intact, because what carries it is the elongation line printed for the other hormone in the same chapter.
<!--/ecat-->

## Q102

Biology · botany · Transport in Plants

Movement and accumulation of ions across a membrane against their concentration gradient can be explained by

- (1) Facilitated Diffusion
- (2) Passive Transport
- **(3)** Active Transport
- (4) Osmosis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Movement against a concentration gradient needs energy (ATP) and carrier proteins, which is active transport, so the answer is option $3$; facilitated diffusion, passive transport and osmosis all go down the gradient.

**Subtopic:** Uptake and Transport of Mineral Nutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q102_4fac8f3b_02112026.png?v=4fac8f3b7926)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only active transport moves ions against a concentration gradient, because only it spends ATP through a pump
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Facilitated diffusion also moves ions through membrane proteins, so the carrier picture fits; the stem's condition 'against their concentration gradient' is what rules it out, since facilitated diffusion only runs down a gradient.
- **Why:** This question requires naming the transport that can work against a gradient, demonstrated by the stem's own condition, 'against their concentration gradient', which is the phrase that separates the four named mechanisms.
- **Note:** condition_missed rather than nearby_fact: facilitated diffusion is printed beside active transport, but the option becomes CORRECT the moment the stem's printed condition is struck out, which is what condition_missed names.
<!--/ecat-->

## Q103

Biology · botany · Sexual Reproduction in Flowering Plants

Large, colourful, fragrant flowers with nectar are seen in

- (1) Bird pollinated plants
- (2) Bat pollinated plants
- (3) Wind pollinated plants
- **(4)** Insect pollinated plants

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT describes insect-pollinated flowers as large, colourful, fragrant and rich in nectar, so the answer is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q103_12d61e53_02112026.png?v=12d61e5357ab)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Insect-pollinated flowers are the ones printed as large, colourful, fragrant and rich in nectar
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Bird-pollinated flowers are the neighbouring agent in the same section and are also large, brightly coloured and nectar-bearing, so three of the stem's four features fit; fragrance is the feature that belongs to the insect line.
- **Why:** This question requires the printed set of features for one pollinating agent, demonstrated by the stem listing all four at once — 'Large, colourful, fragrant flowers with nectar'.
- **Note:** nearby_fact rather than look_alike_term: the agents' names carry no resemblance, and what carries the pull is that bird pollination is described a few lines away with overlapping features.
<!--/ecat-->

## Q104

Biology · botany · Plant Growth and Development

In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as

- **(1)** Dedifferentiation
- (2) Development
- (3) Senescence
- (4) Differentiation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Mature, differentiated mesophyll cells regain the ability to divide and form an undifferentiated mass (callus); NCERT calls this dedifferentiation, which is option $1$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q104_fd5e1edc_02112026.png?v=fd5e1edc8b0f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mature cells that regain the power to divide are said to dedifferentiate, which is what mesophyll cells do when they form a callus
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'Differentiation' is the same word with the prefix dropped, and it is the term a student reaches for when the question is about cells changing in culture; the mesophyll cells are going the other way, losing their mature state to divide again.
- **Why:** This question requires the term the chapter prints for a mature cell regaining the power to divide, demonstrated by the stem describing 'leaf mesophyll cells ... put in a culture medium to form callus' and asking what the phenomenon 'may be called'.
- **Note:** look_alike_term rather than nearby_fact, by the swap test: differentiation and dedifferentiation share their root, and replacing the pair with two unlike words kills the pull, so the resemblance is doing the work.
<!--/ecat-->

## Q105

Biology · botany · Biodiversity and Conservation

The historic Convention on Biological Diversity, ‘The Earth Summit’ was held in Rio de Janeiro in the year

- **(1)** 1992
- (2) 1986
- (3) 2002
- (4) 1985

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The historic Convention on Biological Diversity, the Earth Summit, was held in Rio de Janeiro in $1992$, which is option $1$.

**Subtopic:** How Do We Conserve Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q105_91159b03_02112026.png?v=91159b03163f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Convention on Biological Diversity was signed at the Rio de Janeiro Earth Summit in 1992
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  2002 is the year of the other summit printed in the same paragraph, the World Summit on Sustainable Development at Johannesburg, so a student who holds the paragraph as 'two summits and two dates' can take the second date for the first event.
- **Why:** This question requires one printed date, demonstrated by the stem naming the event in full — 'the historic Convention on Biological Diversity, "The Earth Summit" was held in Rio de Janeiro in the year' — and leaving only the year to supply.
- **Note:** nearby_fact rather than old_ncert_answer: no value in the stem has been altered, and the distractor is a second date printed in the same paragraph rather than a superseded one.
<!--/ecat-->

## Q106

Biology · botany · Biotechnology: Principles and Processes

During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out

- **(1)** DNA
- (2) Histones
- (3) Polysaccharides
- (4) RNA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. After treating with lysozyme/cellulase, RNase and protease to remove other macromolecules, adding chilled ethanol makes the purified DNA precipitate out as fine threads, so the answer is option $1$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q106_6c83ace0_02112026.png?v=6c83ace0ddda)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** In DNA isolation the other molecules are stripped away by enzymes first, and chilled ethanol is the step that brings the purified DNA out of solution as fine threads
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  RNA is the molecule named in the step printed immediately before the ethanol line, where ribonuclease removes it, and it is a nucleic acid too, so the precipitation gets attached to the neighbouring step's molecule.
- **Why:** This question requires what one step of a named bench procedure yields, demonstrated by the stem placing itself inside it — 'during the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out'.
- **Note:** asks is experiment rather than fact_line because the stem is located inside a protocol and asks what a named step produces, not what a structure or term is. A reviewer who reads the axis more narrowly would record fact_line; the choice is noted here so it can be overturned cleanly.
<!--/ecat-->

## Q107

Biology · botany · Photosynthesis in Higher Plants

How many ATP and $\mathrm{NADPH_2}$ are required for the synthesis of one molecule of Glucose during Calvin cycle?

- **(1)** 18 ATP and 12 $\mathrm{NADPH_2}$
- (2) 12 ATP and 16 $\mathrm{NADPH_2}$
- (3) 18 ATP and 16 $\mathrm{NADPH_2}$
- (4) 12 ATP and 12 $\mathrm{NADPH_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Fixing one $\mathrm{CO_2}$ in the Calvin cycle uses $3$ ATP and $2$ $\mathrm{NADPH}$.
2. One glucose ($\mathrm{C_6}$) needs $6$ turns of the cycle.
3. ATP: $6 \times 3 = 18$; $\mathrm{NADPH}$: $6 \times 2 = 12$, which is option $1$.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q107_cabaa279_02112026.png?v=cabaa27999e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Six turns of the Calvin cycle build one glucose, and each turn spends 3 ATP and 2 NADPH — 18 ATP and 12 NADPH in all
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The NADPH half is right at 12, and the ATP half comes out 12 as well if the extra ATP spent in regenerating RuBP is left out — 2 ATP per turn instead of 3 — so the option looks internally tidy with both figures matching.
- **Why:** This question requires the printed cofactor count for one glucose, demonstrated by the stem supplying no numbers of its own — 'How many ATP and NADPH$_2$ are required for the synthesis of one molecule of Glucose during Calvin cycle?'
<!--/ecat-->

## Q108

Biology · botany · Ecosystem

In the equation $\boxed{\mathrm{GPP} - \mathrm{R} = \mathrm{NPP}}$
GPP is Gross Primary Productivity
NPP is Net Primary Productivity
R here is ________.

- (1) Respiratory quotient
- **(2)** Respiratory loss
- (3) Reproductive allocation
- (4) Photosynthetically active radiation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\mathrm{NPP} = \mathrm{GPP} - \mathrm{R}$, where $\mathrm{R}$ is the respiration losses of producers, i.e. respiratory loss (option $2$).

**Subtopic:** Productivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q108_2313863c_02112026.png?v=2313863cf8d2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Net primary productivity is gross primary productivity minus what the plants themselves respire away, so R is the respiratory loss
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Respiratory quotient' carries the right first word and is a real term from the respiration chapter, so the recall of 'R is something respiratory' stops at the nearest respiratory phrase; a quotient is a ratio and cannot be subtracted from a productivity.
- **Why:** This question requires what one symbol in a printed relation stands for, demonstrated by the stem supplying the equation and both other expansions — 'GPP is Gross Primary Productivity, NPP is Net Primary Productivity, R here is ________'.
- **Note:** E1 called this fill_in_blank, which the rulebook treats as an overlay rather than a shape; the printed shape under it is a plain MCQ, so qtype is mcq. look_alike_term rather than nearby_fact, by the swap test: replace 'respiratory loss' and 'respiratory quotient' with two unlike phrases and the pull dies, so the shared word is doing the work.
<!--/ecat-->

## Q109

Biology · botany · Biotechnology: Principles and Processes

In gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used.

- (1) Zinc
- **(2)** Tungsten or gold
- (3) Silver
- (4) Copper

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In the biolistic (gene gun) method, high-velocity microparticles of gold or tungsten coated with DNA are fired into host cells, so the answer is option $2$.

**Subtopic:** Competent Host & Insertion of rDNA into Host Cell · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q109_b028474e_02112026.png?v=b028474e5e75)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In biolistics the alien DNA is shot into cells on high-velocity microparticles of gold or tungsten
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each of the other three metals against the biotechnology chapter: zinc, silver and copper appear in no step of the gene gun, in no vector or enzyme, and in no other part of the chapter, so none of them is a printed fact a prepared student could reach for. The only named metals in the method are the two in the key.
- **Why:** This question requires one named material from a printed technique, demonstrated by the stem quoting the technique and leaving only the metal blank — 'in gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used'.
- **Note:** E1 called this fill_in_blank, an overlay on a plain MCQ, so qtype is mcq. no_trap is recorded as a finding: the option set is three metals with no printed role in the chapter, and the only distinguishing feature of the key is that it names two metals rather than one.
<!--/ecat-->

## Q110

Biology · botany · Principles of Inheritance and Variation

The phenomenon of pleiotropism refers to

- (1) Presence of two alleles, each of the two genes controlling a single trait
- **(2)** A single gene affecting multiple phenotypic expression
- (3) More than two genes affecting a single character
- (4) Presence of several alleles of a single gene controlling a single crossover

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Pleiotropy is defined as a single gene affecting multiple phenotypic traits, so the answer is option $2$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q110_7f8ae1d9_02112026.png?v=7f8ae1d9fe80)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pleiotropy is one gene showing several phenotypic effects, the mirror image of several genes acting on one trait
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The relation is stated the other way round: many genes acting on one character instead of one gene acting on many characters, which is polygenic inheritance, printed in the same section as pleiotropy.
- **Why:** This question requires the printed definition of one term, demonstrated by the stem being only 'the phenomenon of pleiotropism refers to' with four rival definitions below it.
- **Note:** E1 called this statement_options because each option is a full clause; the stem prints no statement block and asks for no verdict on statements, so by the qtype rule it is recorded as mcq.
<!--/ecat-->

## Q111

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) Late wood has fewer xylary elements with narrow vessels.
- (Reason R) Cambium is less active in winters.

- (1) Both A and R are true but R is NOT the correct explanation of A
- (2) A is true but R is false
- (3) A is false but R is true
- **(4)** Both A and R are true and R is the correct explanation of A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In winter the cambium is less active, so it forms fewer xylary elements with narrow vessels (late wood); both A and R are true and R explains A, which is option $4$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q111_5dfc7426_02112026.png?v=5dfc7426765b)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Spring wood and autumn wood differ because cambial activity follows the season: a less active cambium in winter lays down fewer xylem elements with narrow vessels
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Wide vessels and many xylary elements belong to spring wood, and a student carrying that pair the other way round reads A's 'fewer xylary elements with narrow vessels' as a description of early wood, so A looks false while R stays true
- **Why:** This question requires the causal line between cambial activity and vessel width, demonstrated by A stating only the outcome, 'fewer xylary elements with narrow vessels', while R supplies the cause, 'Cambium is less active in winters'.
<!--/ecat-->

## Q112

Biology · botany · Cell Cycle and Cell Division

Among eukaryotes, replication of DNA takes place in :

- **(1)** S phase
- (2) $\mathrm{G_1}$ phase
- (3) $\mathrm{G_2}$ phase
- (4) M phase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the eukaryotic cell cycle, DNA synthesis (replication) happens in the $\mathrm{S}$ phase of interphase, which is option $1$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q112_9a92fd56_02112026.png?v=9a92fd56f1eb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA is copied in the S phase of interphase, so the chromosome number is unchanged while the DNA content doubles
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The G$_2$ line prints synthesis in preparation for mitosis, and that word 'synthesis' is read as DNA synthesis, which places replication one stage later than it happens.
- **Why:** This question requires which phase of the cycle carries replication, demonstrated by the stem — 'among eukaryotes, replication of DNA takes place in' — and four phases of the one printed cycle as options.
- **Note:** wrong_site_attacked rather than nearby_fact: the event asked about is the right one and only its stage has moved, which is what this label names; the names G$_1$, G$_2$, S and M carry no resemblance to trade on.
<!--/ecat-->

## Q113

Biology · botany · Morphology of Flowering Plants

Family Fabaceae differs from Solanaceae and Liliaceae. With respect to the stamens, pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae.

- (1) Polyadelphous and epipetalous stamens
- (2) Monoadelphous and Monothecous anthers
- (3) Epiphyllous and Dithecous anthers
- **(4)** Diadelphous and Dithecous anthers

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Fabaceae androecium: ten stamens, diadelphous $(9)+1$, anthers dithecous; Solanaceae has epipetalous stamens and Liliaceae has epiphyllous (epitepalous) stamens, so the Fabaceae-specific feature is diadelphous with dithecous anthers, option $4$.

**Subtopic:** Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q113_e8be325b_02112026.png?v=e8be325b0ed9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Fabaceae stamens are diadelphous with dithecous anthers, against the epipetalous stamens of Solanaceae and the epiphyllous stamens of Liliaceae
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  'Dithecous anthers' is right for Fabaceae and is the half a student can confirm, but 'epiphyllous' is the Liliaceae condition — the very family the stem excludes — so the option fails on the half that was not checked.
- **Why:** This question requires separating one family's stamen characters from two others', demonstrated by the stem itself setting the contrast — 'pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae'.
- **Note:** asks is compare rather than fact_line because the stem names three families and asks which character belongs to one and not the others; a single printed line about Fabaceae does not settle it, since the option that carries a true Fabaceae feature, option 3, is still wrong on the contrast.
<!--/ecat-->

## Q114

Biology · botany · Morphology of Flowering Plants

Axile placentation is observed in

- (1) China rose, Beans and Lupin
- (2) Tomato, Dianthus and Pea
- **(3)** China rose, Petunia and Lemon
- (4) Mustard, Cucumber and Primrose

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In NCERT, axile placentation is shown by China rose, tomato and lemon, and Petunia (Solanaceae) also has axile placentation. Beans, lupin and pea are marginal, mustard and cucumber are parietal, and Dianthus and Primrose are free central, so only option $3$ lists all axile examples.

**Subtopic:** Gynoecium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q114_1eaff07d_02112026.png?v=1eaff07d5661)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Placentation is named from where the ovules sit in the ovary, and NCERT fixes one set of example plants to each type, with china rose, tomato, lemon and petunia under axile
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  China rose is NCERT's first-named axile example and it heads this option too, so a student who recognises the one name they are sure of takes the set whole; beans and lupin are legumes with marginal placentation, so the set fails on its last two names
- **Why:** This question requires the taught list of example plants under one placentation type, demonstrated by options that bundle three named plants to be taken whole - 'China rose, Petunia and Lemon' - with no criterion printed to apply.
- **Note:** E1 called this statement_options; the printed options are not statements but sets of plant names judged whole, which is the codebook's pair_options. Both retire forward to qtype statements, so the recorded label is unaffected.
<!--/ecat-->

## Q115

Biology · botany · Plant Kingdom

Identify the pair of heterosporous pteridophytes among the following :

- **(1)** Selaginella and Salvinia
- (2) Psilotum and Salvinia
- (3) Equisetum and Salvinia
- (4) Lycopodium and Selaginella

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT names Selaginella and Salvinia as heterosporous pteridophytes (they produce microspores and megaspores), while Psilotum, Equisetum and Lycopodium are homosporous, so only option $1$ has two heterosporous genera.

**Subtopic:** Pteridophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q115_8d879c65_02112026.png?v=8d879c65d0c2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nearly all pteridophytes make one kind of spore; heterosporous means two kinds, macrospores and microspores, and NCERT names only Selaginella and Salvinia
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Selaginella and Lycopodium are the two Lycopsida genera NCERT prints together, so a student holding 'Selaginella is heterosporous' extends the trait to its class-mate; Lycopodium makes one kind of spore, so only half the pair qualifies
- **Why:** This question requires the stated membership of a named group, demonstrated by the stem asking to 'Identify the pair of heterosporous pteridophytes' with each option a pair taken whole.
- **Note:** E1 defaulted this to plain_mcq, but each option is a pair of genera accepted or rejected whole, which is the codebook's pair_options; that carries forward to qtype statements, so the shape is recorded as what is printed rather than as the pattern's default.
<!--/ecat-->

## Q116

Biology · botany · Environmental Issues

The thickness of ozone in a column of air in the atmosphere is measured in terms of :

- (1) Decibels
- (2) Decameter
- (3) Kilobase
- **(4)** Dobson units

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The thickness of ozone in a column of air from the ground to the top of the atmosphere is measured in Dobson units (DU), which is option $4$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q116_ef7037ac_02112026.png?v=ef7037ac5959)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ozone in an air column is reported in its own unit, the Dobson unit, and not in a unit of length or of sound
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The decibel is the unit this same chapter prints for noise pollution, so a student revising Environmental Issues answers with the unit that chapter taught them; the ozone column is reported in Dobson units instead
- **Why:** This question requires one stated unit, demonstrated by the stem 'is measured in terms of :' with four unrelated units as options and no quantity given to convert.
<!--/ecat-->

## Q117

Biology · botany · Sexual Reproduction in Flowering Plants

What is the function of tassels in the corn cob?

- **(1)** To trap pollen grains
- (2) To disperse pollen grains
- (3) To protect seeds
- (4) To attract insects

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Corn tassels (silks on the cob) are the feathery stigma and style of the wind-pollinated female flowers, which wave in the wind to trap airborne pollen grains, so the answer is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q117_aa31ec8a_02112026.png?v=aa31ec8aaa84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The tassels of a corn cob are the stigma and style, held out in the wind to catch air-borne pollen, which is why maize is the wind-pollination example
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who has filed maize, tassels and wind together takes the direction of pollen travel from the wind rather than from the structure, and has the tassel shed pollen; NCERT identifies the tassel of the cob as stigma and style, so pollen arrives at it and does not leave from it
- **Why:** This question requires the stated function of one named structure, demonstrated by the stem 'What is the function of tassels in the corn cob?' with four rival functions and no figure or criterion supplied.
<!--/ecat-->

## Q118

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R: In the light of the above statements, choose the most appropriate answer from options given below:

- (Assertion A) The first stage of gametophyte in the life cycle of moss is protonema stage.
- (Reason R) Protonema develops directly from spores produced in capsule.

- (1) Both A and R are correct but R is not the correct explanation of A
- (2) A is correct but R is not correct
- (3) A is not correct but R is correct
- **(4)** Both A and R are correct and R is correct explanation of A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Assertion A: in moss the gametophyte begins as the creeping, green, filamentous protonema, so A is correct.
2. Reason R: the protonema develops directly from a haploid spore released from the capsule, so R is correct.
3. Since the spore germinates directly into the protonema, R explains why protonema is the first gametophyte stage, which is option $4$.

**Subtopic:** Mosses · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q118_77f07327_02112026.png?v=77f073276548)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The moss gametophyte begins as the protonema because the protonema is what grows straight out of the germinating spore; the leafy stage comes after it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  R is read as a separate fact about where moss spores come from, so the student accepts both statements and then denies that the origin of the protonema has anything to do with its being the FIRST gametophyte stage
- **Why:** This question requires deciding whether one granted fact accounts for another, demonstrated by R, 'Protonema develops directly from spores produced in capsule', being the ground on which A can call the protonema 'the first stage of gametophyte'.
<!--/ecat-->

## Q119

Biology · botany · Transport in Plants

Given below are two statements :
Statement I : The forces generated transpiration can lift a xylem-sized column of water over $130$ meters height.
Statement II : Transpiration cools leaf surfaces sometimes $10$ to $15$ degree evaporative cooling.
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The forces generated transpiration can lift a xylem-sized column of water over $130$ meters height.
- (Statement II) Transpiration cools leaf surfaces sometimes $10$ to $15$ degree evaporative cooling.

- (1) Both Statement I and Statement II are incorrect
- (2) Statement I is correct but Statement II is incorrect
- (3) Statement I is incorrect but Statement II is correct
- **(4)** Both Statement I and Statement II are correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: the forces generated by transpiration can create enough pressure to lift a xylem-sized column of water over $130\,\text{m}$ high, so it is correct.
2. Statement II: transpiration cools leaf surfaces, sometimes by $10$ to $15$ degrees, through evaporative cooling, so it is correct.
3. Both statements are correct, which is option $4$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q119_30f7bda2_02112026.png?v=30f7bda2ecf6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Transpiration pull can generate enough force to raise a xylem-sized water column over 130 m, and evaporation from the leaf cools its surface by 10 to 15 degrees
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The tallest trees stand around 100 m, so "over $130$ meters" reads as an overstatement and Statement I gets marked incorrect; the printed line is about the force transpiration can generate, not about the height of any existing tree.
- **Why:** This question requires two stated facts about transpiration to be checked as printed, demonstrated by Statement I's "over $130$ meters height" and Statement II's "$10$ to $15$ degree evaporative cooling".
- **Note:** Label chosen on which fact carries the student: the rejection of Statement I rests on a remembered neighbouring figure, the height of the tallest trees, rather than on any resemblance between terms, so nearby_fact and not look_alike_term.
<!--/ecat-->

## Q120

Biology · botany · Plant Growth and Development

Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period, the leads early seed production?

- **(1)** Gibberellic Acid
- (2) Zeatin
- (3) Abscisic Acid
- (4) Indole-3-butyric Acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT states that spraying juvenile conifers with gibberellins ($GA_3$) hastens maturity and leads to early seed production, so the answer is option $1$, Gibberellic Acid.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q120_1c64a46f_02112026.png?v=1c64a46f2bc7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gibberellins shorten the juvenile phase: sprayed on young conifers they hasten maturity and bring seed production forward
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Abscisic acid is the hormone whose own NCERT line carries the words seed development, maturation and dormancy, so a student matching the stem's 'maturity' and 'seed production' to a remembered sentence lands on it; that sentence is about seeds maturing, not about a juvenile plant reaching maturity
- **Why:** This question requires one stated application of a named hormone, demonstrated by the stem 'Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period' naming the plant and the effect and asking only for the hormone.
- **Note:** The stem as stored reads 'hastening the maturity period, the leads early seed production', where 'the' appears to stand for 'that'; the garble does not change what is asked, and I have tagged the question as printed.
<!--/ecat-->

## Q121

Biology · botany · Principles of Inheritance and Variation

Frequency of recombination between gene pairs on same chromosome as a measure of the distance between genes to map their position on chromosome, was used for the first time by

- (1) Sutton and Boveri
- **(2)** Alfred Sturtevant
- (3) Henking
- (4) Thomas Hunt Morgan

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT: Sturtevant used the frequency of recombination between gene pairs on the same chromosome as a measure of the distance between genes and mapped their position on the chromosome, which is option $2$.

**Subtopic:** Linkage & Recombination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q121_84296ed7_02112026.png?v=84296ed798c6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Recombination frequency between two genes on one chromosome measures the distance between them, and Sturtevant used it to make the first genetic map
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Morgan is the name the chapter attaches to linkage and recombination, and Sturtevant appears only as the student working in his group, so a student holding 'linkage equals Morgan' answers with the headline name; the mapping step is credited to Sturtevant in the sentence that follows
- **Why:** This question requires one stated attribution, demonstrated by the stem ending 'was used for the first time by' with four names and no reasoning offered to decide between them.
<!--/ecat-->

## Q122

Biology · botany · Molecular Basis of Inheritance

Expressed Sequence Tags (ESTs) refers to

- (1) All genes that are expressed as proteins.
- (2) All genes whether expressed or unexpressed.
- (3) Certain important expressed genes.
- **(4)** All genes that are expressed as RNA.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT (Human Genome Project) defines Expressed Sequence Tags as the approach that identifies all genes expressed as RNA, which is option $4$.

**Subtopic:** Human Genome Project · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q122_611d32dd_02112026.png?v=611d32dd8dc3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Expressed Sequence Tags were the Human Genome Project approach of identifying only those genes that are expressed as RNA, as against sequencing the whole genome blind
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Gene expression is taught as ending in a protein, so a student who reads the word 'Expressed' in the term supplies the end-product from the central dogma instead of from the printed sentence, which defines ESTs as the genes expressed as RNA
- **Why:** This question requires one stated definition, demonstrated by the stem 'Expressed Sequence Tags (ESTs) refers to' with four rival completions and no data to work from.
- **Note:** E1 returned arrange_in_order, which looks to have fired on the word 'Sequence' inside the term's name; nothing in the question is to be put in order, so the shape is recorded as the plain four-option question that is printed.
<!--/ecat-->

## Q123

Biology · botany · Biotechnology: Principles and Processes

Upon exposure to UV radiation, DNA stained with ethidium bromide will show

- (1) Bright blue colour
- (2) Bright yellow colour
- **(3)** Bright orange colour
- (4) Bright red colour

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In gel electrophoresis, separated DNA fragments stained with ethidium bromide are viewed under UV radiation and appear as bright orange coloured bands, which is option $3$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q123_1d25c1ab_02112026.png?v=1d25c1abbad2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** DNA fragments separated on a gel are made visible by staining with ethidium bromide and shining UV on the gel, which makes the bands glow bright orange
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  A student who has stored the band colour as a warm reddish glow rather than as the printed word reaches for red, the colour sitting next to orange; the observation line reads bright orange coloured bands
- **Why:** This question requires what is observed at the end of a stated procedure, demonstrated by the stem supplying both steps - 'stained with ethidium bromide' and 'exposure to UV radiation' - and asking only what the gel will show.
<!--/ecat-->

## Q124

Biology · botany · Respiration in Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) ATP is used at two steps in glycolysis.
- (Reason R) First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1-6-diphosphate.

- (1) Both A and R are true but R is NOT the correct explanation of A.
- (2) A is true but R is false.
- (3) A is false but R is true.
- **(4)** Both A and R are true and R is the correct explanation of A.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Glycolysis consumes ATP at exactly two steps, so $A$ is true.
2. Step 1: glucose $\xrightarrow{ATP}$ glucose-6-phosphate; step 2: fructose-6-phosphate $\xrightarrow{ATP}$ fructose-1,6-bisphosphate, so $R$ is true.
3. $R$ names the two ATP-using steps that $A$ refers to, so $R$ correctly explains $A$: option $4$.

**Subtopic:** Glycolysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q124_799ff092_02112026.png?v=799ff09238b6)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Glycolysis spends ATP twice in its first half: glucose to glucose-6-phosphate, and fructose-6-phosphate to fructose-1,6-bisphosphate
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  A student who places the second ATP expenditure one step earlier, at the glucose-6-phosphate to fructose-6-phosphate change, reads R's second conversion as the wrong step and so marks R false while keeping A true
- **Why:** This question requires the identity of the two ATP-consuming steps of glycolysis, demonstrated by R naming them as 'converting glucose into glucose-6-phosphate' and 'conversion of fructose-6-phosphate into fructose-1-6-diphosphate'.
- **Note:** R prints 'fructose-1-6-diphosphate' where current NCERT prints fructose 1,6-bisphosphate; the key treats R as true, and the question is tagged as printed.
<!--/ecat-->

## Q125

Biology · botany · Molecular Basis of Inheritance

Unequivocal proof that DNA is the genetic material was first proposed by

- **(1)** Alfred Hershey and Martha Chase
- (2) Avery, Macleoid and McCarthy
- (3) Wilkins and Franklin
- (4) Frederick Griffith

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Hershey and Chase (1952) grew bacteriophages with $^{32}P$ (labels DNA) and $^{35}S$ (labels protein); only $^{32}P$ entered the bacteria, giving the unequivocal proof that DNA is the genetic material, which is option $1$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q125_c27760fb_02112026.png?v=c27760fb9220)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The transformation work and the Avery team's biochemistry pointed at DNA, but the unequivocal proof that DNA is the genetic material is the Hershey and Chase bacteriophage experiment
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Drop the stem's word 'Unequivocal' and this option becomes right, because the Avery, MacLeod and McCarty work did identify DNA as the transforming principle; the text then records that this did not convince all biologists, and reserves the unequivocal proof for Hershey and Chase
- **Why:** This question requires one stated attribution, demonstrated by the stem 'Unequivocal proof that DNA is the genetic material was first proposed by' with four named investigators and no evidence supplied to weigh.
- **Note:** The options print 'Macleoid and McCarthy' for MacLeod and McCarty; the misspelling is in the paper as stored and does not change which team is meant.
<!--/ecat-->

## Q126

Biology · botany · Ecosystem

Identify the correct statements:
Choose the correct answer from the options given below:

- (A) Detrivores perform fragmentation.
- (B) The humus is further degraded by some microbes during mineralization.
- (C) Water soluble inorganic nutrients go down into the soil and get precipitated by a process called leaching.
- (D) The detritus food chain begins with living organisms.
- (E) Earthworms break down detritus into smaller particles by a process called catabolism.

- (1) B, C, D only
- (2) C, D, E only
- (3) D, E, A only
- **(4)** A, B, C only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A: detritivores such as earthworms break detritus into smaller particles (fragmentation), so A is true.
2. B: humus is degraded very slowly by some microbes and releases inorganic nutrients by mineralization, so B is true.
3. C: water-soluble inorganic nutrients go down into the soil horizon and get precipitated as unavailable salts by leaching, so C is true.
4. D: the detritus food chain begins with dead organic matter (detritus), not living organisms, so D is false.
5. E: earthworms breaking detritus into smaller particles is fragmentation; catabolism is enzymatic degradation by bacteria and fungi, so E is false.
6. True set is $\{A, B, C\}$, which is option $4$.

**Subtopic:** Decomposition · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q126_3241d8c8_02112026.png?v=3241d8c8c4e6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Decomposition runs as fragmentation, leaching, catabolism, humification and mineralisation, and the detritus food chain starts from dead organic matter
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Statements B and C are printed lines on mineralisation and leaching, so the option reads as two certainties plus one more, and D is accepted because the chain that begins with living organisms is the grazing chain described beside the detritus one.
- **Why:** This question requires the stated steps of decomposition and the stated start of the detritus food chain, demonstrated by statement D's "The detritus food chain begins with living organisms" and statement E's "a process called catabolism".
- **Note:** Swap test applied: the false statements are built by moving a name or a starting point in from an adjacent item of the same printed passage, and the words involved — catabolism against fragmentation, grazing against detritus — do not resemble each other, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q127

Biology · botany · Photosynthesis in Higher Plants

The reaction centre PS II has an absorption maxima at

- (1) $700\,\mathrm{nm}$
- (2) $660\,\mathrm{nm}$
- (3) $780\,\mathrm{nm}$
- **(4)** $680\,\mathrm{nm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In NCERT, the reaction centre of PS II is chlorophyll $a$ with absorption peak at $680\,\mathrm{nm}$ (P680), while PS I is P700, so the answer is option $4$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q127_64b8f810_02112026.png?v=64b8f810fe1f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The two photosystems are named from their reaction-centre absorption peaks: PS II peaks at 680 nm and PS I at 700 nm
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  700 nm is the number printed one sentence away, for the reaction centre of PS I, so a student who stores the two photosystems as one pair of facts and loses which number goes with which gives the other photosystem's peak
- **Why:** This question requires one stored value, demonstrated by the stem 'The reaction centre PS II has an absorption maxima at' with four wavelengths and nothing given to compute from.
<!--/ecat-->

## Q128

Biology · botany · Sexual Reproduction in Flowering Plants

In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :

- (1) Antipodals, synergids, and primary endosperm nucleus
- **(2)** Synergids, Zygote and Primary endosperm nucleus
- (3) Synergids, antipodals and Polar nuclei
- (4) Synergids, Primary endosperm nucleus and zygote

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Synergids are cells of the egg apparatus, formed from the haploid megaspore, so they are haploid ($n$).
2. Syngamy fuses the egg ($n$) with one male gamete ($n$): zygote $= n + n = 2n$ (diploid).
3. Triple fusion joins two polar nuclei ($n + n$) with the second male gamete ($n$): PEN $= 3n$ (triploid).
4. The order haploid, diploid, triploid is synergids, zygote, primary endosperm nucleus, which is option $2$.

**Subtopic:** Double Fertilisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q128_7061810f_02112026.png?v=7061810f4c4d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In a fertilised embryo sac everything left over from the female gametophyte stays haploid, syngamy makes the diploid zygote, and triple fusion makes the triploid primary endosperm nucleus
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who has the three right names but keeps the two fertilisation events as one block puts the endosperm nucleus in the diploid slot and the zygote in the triploid one; it is triple fusion, three haploid nuclei, that gives 3n, and syngamy of two that gives 2n
- **Why:** This question requires the ploidy of named embryo-sac structures to be worked out from which fusion produced them, demonstrated by the stem asking for 'the haploid, diploid and triploid structures of a fertilized embryo sac sequentially' with each option a three-name set taken whole.
- **Note:** E1 called this statement_options from its long options; the printed stem asks for three structures to be given 'sequentially' against three ploidy slots, which is the codebook's multi_part_respectively, so the recorded qtype is two_part.
<!--/ecat-->

## Q129

Biology · botany · Mineral Nutrition

Which micronutrient is required for splitting of water molecule during photosynthesis?

- (1) Molybdenum
- (2) Magnesium
- (3) Copper
- **(4)** Manganese

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Photolysis of water in photosystem II requires $\mathrm{Mn}^{2+}$ (with $\mathrm{Ca}^{2+}$ and $\mathrm{Cl}^{-}$); manganese is a micronutrient, so the answer is option $4$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q129_06e245f6_02112026.png?v=06e245f6532b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Manganese is the micronutrient whose named function is the splitting of water to liberate oxygen in photosynthesis
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Manganese and magnesium are near-homophones and both are printed in the photosynthesis context, so a student reaching for the element tied to photosynthesis produces the one whose name comes first to mind; magnesium is a macronutrient and its printed role is as the chlorophyll atom, not as the splitter of water
- **Why:** This question requires one stated function of a named element, demonstrated by the stem 'Which micronutrient is required for splitting of water molecule during photosynthesis?' with four elements and no criterion given to derive the answer.
<!--/ecat-->

## Q130

Biology · botany · Cell Cycle and Cell Division

Which of the following stages of meiosis involves division of centromere?

- (1) Metaphase II
- **(2)** Anaphase II
- (3) Telophase
- (4) Metaphase I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At anaphase II the centromere of each chromosome splits, letting sister chromatids move to opposite poles, so the answer is option $2$.

**Subtopic:** Anaphase II and Telophase II · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q130_be34218e_02112026.png?v=be34218eb8b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sister chromatids stay joined at their centromere right through the first meiotic division; the centromere splits in anaphase II, which is what lets the chromatids move to opposite poles
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Metaphase II is where the kinetochores of the sister chromatids are described as attaching to spindle fibres from opposite poles, so a student who reads that attachment as the moment of separation puts the centromere's splitting one stage early; the splitting itself is printed under anaphase II
- **Why:** This question requires one stated event to be matched to the stage it is printed under, demonstrated by the stem 'Which of the following stages of meiosis involves division of centromere?' with four stage names and nothing to work out.
<!--/ecat-->

## Q131

Biology · botany · Biomolecules

Cellulose does not form blue colour with Iodine because

- (1) It is a helical molecule
- **(2)** It does not contain complex helices and hence cannot hold iodine molecules
- (3) It breakes down when iodine reacts with it
- (4) It is a disaccharide

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Starch forms helical secondary structures that hold $I_2$ molecules, giving blue colour; cellulose has no complex helices, so it cannot hold iodine, which is option $2$.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q131_a6acbccb_02112026.png?v=a6acbccb4dcd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Starch turns blue with iodine because its helices physically hold iodine molecules; cellulose has no such complex helices, so there is nowhere for the iodine to sit
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who retrieves 'helix' as the word tied to the iodine test states it as the property of the molecule in front of them, which inverts the printed explanation; the reason runs the other way, cellulose having no complex helices and therefore holding no iodine
- **Why:** This question requires the printed reason for an absent result, demonstrated by the stem 'Cellulose does not form blue colour with Iodine because' with each option a rival explanation.
- **Note:** Option 3 is printed 'breakes'; the misspelling is in the paper as stored and does not change the claim.
<!--/ecat-->

## Q132

Biology · botany · Biodiversity and Conservation

Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?

- (1) Over exploitation for economic gain
- (2) Alien species invasions
- (3) Co-extinctions
- **(4)** Habitat loss and fragmentation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Of the four causes in the Evil Quartet, NCERT names habitat loss and fragmentation as the most important cause of extinction, which is option $4$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q132_c4da8740_02112026.png?v=c4da874062b8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Evil Quartet names four causes of extinction, and habitat loss and fragmentation is the one the text ranks as the most important
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Over-exploitation is a genuine member of the Evil Quartet, printed next to the right answer, so recognising it as one of the four reads as having answered the question; the stem asks which the text calls the most important, and that ranking is given to habitat loss and fragmentation
- **Why:** This question requires one printed ranking, demonstrated by the stem asking which of 'The Evil Quartet' is 'considered the most important cause' while all four options are members of that quartet.
<!--/ecat-->

## Q133

Biology · botany · Molecular Basis of Inheritance

What is the role of RNA polymerase III in the process of transcription in Eukaryotes?

- **(1)** Transcription of tRNA, 5 srRNA and snRNA
- (2) Transcription of precursor of mRNA
- (3) Transcription of only snRNAs
- (4) Transcription of rRNAs (28S, 18S and 5.8S)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In eukaryotes, RNA polymerase III transcribes tRNA, $5\,S$ rRNA and snRNAs (NCERT), which is option $1$.

**Subtopic:** Transcription · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q133_b9223fe1_02112026.png?v=b9223fe1598f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each eukaryotic RNA polymerase has its own set of transcripts: I makes the large rRNAs, II the precursor of mRNA, and III the tRNAs, 5S rRNA and snRNAs
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  snRNA really is transcribed by polymerase III, so a student who has stored that one pairing and meets an option naming it stops there; the printed assignment gives polymerase III three classes of transcript, and the word 'only' in the option excludes the other two
- **Why:** This question requires the printed assignment of transcripts to one named enzyme, demonstrated by the stem 'What is the role of RNA polymerase III in the process of transcription in Eukaryotes?' with each option a rival set of transcripts.
- **Note:** E1 called this statement_options; the stem is a full question and the options are answer phrases rather than claims to be judged, so the shape is recorded as a plain four-answer question. Option 1 prints '5 srRNA' for 5S rRNA, a typographic slip in the paper as stored that does not change the referent.
<!--/ecat-->

## Q134

Biology · botany · Anatomy of Flowering Plants

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body.
- (Statement II) Exarch condition is the most common feature of the root system.

- (1) Both Statement I and Statement II are false
- (2) Statement I is correct but Statement II is false
- **(3)** Statement I is incorrect but Statement II is true
- (4) Both Statement I and Statement II are true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Endarch/exarch refer to the position of protoxylem relative to metaxylem in primary xylem, not secondary xylem, so Statement I is incorrect.
2. In roots the protoxylem lies towards the periphery (exarch), so Statement II is true; this matches option $3$.

**Subtopic:** Complex Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q134_35f9061e_02112026.png?v=35f9061e477c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Endarch and exarch describe where the PRIMARY xylem sits, and the root is the exarch case while the stem is endarch
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Endarch and exarch really are the terms for xylem position, so Statement I reads as familiar and correct until the word "secondary" is noticed — the terms describe primary xylem, and Statement II is independently true, so the whole option passes.
- **Why:** This question requires the stated referent of two anatomy terms, demonstrated by Statement I putting endarch and exarch on "secondary xylem" while Statement II's exarch root claim stands as printed.
- **Note:** Label chosen as wrong_site_attacked because the correct descriptor is attached to the wrong tissue stage — primary xylem replaced by secondary — rather than to a resembling term or to a neighbouring name.
<!--/ecat-->

## Q135

Biology · botany · Cell Cycle and Cell Division

The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?

- **(1)** Pachytene
- (2) Diplotene
- (3) Diakinesis
- (4) Zygoten

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Per NCERT, during pachytene bivalents become tetrads and recombination nodules appear at the sites where crossing over occurs between non-sister chromatids of homologous chromosomes, so the answer is option $1$ (Pachytene).

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q135_8db3251f_02112026.png?v=8db3251fa668)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Crossing over happens at pachytene, where recombination nodules appear on the bivalents at the sites of exchange
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  Diplotene is the sub-stage where the chapter's other crossing-over landmark, the chiasma, becomes visible, so a student who holds one slot for 'the stage where the crossing-over structures show up' puts the recombination nodules there; the nodules are printed one sub-stage earlier, at pachytene
- **Why:** This question requires one printed event to be matched to the sub-stage it is listed under, demonstrated by the stem 'appearance of recombination nodules occurs at which sub stage of prophase I' with four sub-stage names as options.
- **Note:** Option 4 is printed 'Zygoten' for zygotene; the spelling is as stored in the paper and does not change which sub-stage is meant.
<!--/ecat-->

## Q136

Biology · botany · Plant Kingdom

Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) In gymnosperms the pollen grains are released from the microsporangium and carried by air currents.
- (Reason R) Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed.

- (1) Both A and R are true but R is NOT the current explanation of A
- **(2)** A is true but R is false
- (3) A is false but R is true
- (4) Both A and R are true and R is the correct explanation of A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A: in gymnosperms pollen grains are released from the microsporangium and carried by air currents, so A is true.
2. Reason R: pollen grains reach the micropyle of the ovule and form a pollen tube that carries the male gametes towards the archegonia, so the claim that no pollen tube is formed is false.
3. A true and R false matches option $2$.

**Subtopic:** Gymnosperms · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q136_4119402c_02112026.png?v=4119402cf913)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperm pollen is wind-borne, but the male gametes still reach the mouth of the archegonium through a pollen tube
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The gymnosperm pages are also where the motile male gametes of Cycas and Ginkgo are printed, so a student who has filed 'gymnosperm gametes get there on their own' from that neighbouring line grants R's closing clause, 'pollen tube is not formed', and marks both statements true with R explaining A
- **Why:** This question requires the stated fact that a pollen tube is formed in gymnosperms, demonstrated by R closing with 'and pollen tube is not formed' while the rest of it repeats the chapter's account of discharge at the mouth of the archegonia.
- **Note:** nearby_fact rather than look_alike_term: the pull is the motile-gamete line printed in the same gymnosperm section, not any resemblance between two names — replace Cycas and Ginkgo with unlike words and the pull survives, because position is doing the work. Option 1 as extracted reads 'the current explanation of A' where the paper's other assertion-reason items read 'the correct explanation'; tagged as printed.
<!--/ecat-->

## Q137

Biology · botany · Environmental Issues

Which one of the following statements is NOT correct?

- **(1)** Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries
- (2) Water hyacinth grows abundantly in eutrophic water bodies and leads to an imbalance in the ecosystem dynamics of the water body
- (3) The amount of some toxic substances of industrial waste water increases the organisms at successive trophic levels
- (4) The micro-organisms involved in biodegradation of organic matter in a sewage polluted water body consume a lot of oxygen causing the death of aquatic organisms

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Algal blooms from nutrient enrichment deteriorate water quality, deplete dissolved oxygen and cause fish mortality, so statement $1$ is NOT correct.
2. Water hyacinth thriving in eutrophic water and upsetting ecosystem balance (statement $2$), biomagnification of toxic industrial substances along trophic levels (statement $3$), and high oxygen use by sewage-degrading microbes killing aquatic life (statement $4$) are all correct, so the answer is option $1$.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q137_96534354_02112026.png?v=96534354f1ca)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nutrient and organic enrichment degrades a water body: blooms and weeds spoil water quality, microbial breakdown of organic matter strips the dissolved oxygen, and some industrial toxins build up along the food chain
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Drop the stem's 'NOT' and this option becomes the pick, because it states the oxygen-depletion mechanism exactly as the chapter does; the task is to find the statement that fails, and this one holds
- **Why:** This question requires four printed claims about water pollution to be graded against the text, demonstrated by the stem 'Which one of the following statements is NOT correct?' with each option a standalone claim.
- **Note:** Option 3 as stored reads 'increases the organisms at successive trophic levels', which appears to be missing 'in'; the claim it makes is biomagnification either way and the key is unaffected. Tagged as printed.
<!--/ecat-->

## Q138

Biology · botany · Photosynthesis in Higher Plants

Which of the following combinations is required for chemiosmosis?

- (1) Membrane, proton pump, proton gradient, NADP synthase
- (2) Proton pump, electron gradient, ATP synthase
- (3) Proton pump, electron gradient, NADP synthase
- **(4)** Membrane, proton pump, proton gradient, ATP synthase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Chemiosmosis requires a membrane, a proton pump, a proton gradient across the membrane and ATP synthase through which protons flow to make ATP, which is option $4$.

**Subtopic:** Chemiosmotic Hypothesis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q138_849482ee_02112026.png?v=849482ee0c6f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chemiosmosis needs four things together: a membrane, a proton pump, a proton gradient across that membrane, and ATP synthase to spend the gradient
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Three of this option's four items are the printed requirements and only the enzyme is changed, so a student who checks the beginning of the set and recognises membrane, pump and proton gradient takes it whole; the gradient is spent by ATP synthase, and the reductase that handles NADP sits elsewhere in the light reaction
- **Why:** This question requires the printed list of components for a named mechanism, demonstrated by the stem 'Which of the following combinations is required for chemiosmosis?' with each option a set taken whole.
<!--/ecat-->

## Q139

Biology · botany · Cell Cycle and Cell Division

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | M Phase | I | Proteins are synthesized |
| B | $\mathrm{G_2}$ Phase | II | Inactive phase |
| C | Quiescent stage | III | Interval between mitosis and initiation of DNA replication |
| D | $\mathrm{G_1}$ Phase | IV | Equational division |

- (1) A-IV, B-II, C-I, D-III
- **(2)** A-IV, B-I, C-II, D-III
- (3) A-II, B-IV, C-I, D-III
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. M phase (mitosis) is the equational division, so A-IV.
2. In $\mathrm{G_2}$ phase proteins are synthesised in preparation for mitosis, so B-I.
3. The quiescent stage ($\mathrm{G_0}$) is an inactive phase, so C-II.
4. $\mathrm{G_1}$ phase is the interval between mitosis and the initiation of DNA replication, so D-III.
5. A-IV, B-I, C-II, D-III matches option $2$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q139_35bb7b44_02112026.png?v=35bb7b44c05d)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each phase of the cell cycle has its own job: G1 is the gap before DNA replication, G2 is where proteins are made for mitosis, M is the equational division, and G0 is the inactive stage cells park in
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Reading the G phases as gaps in which nothing happens puts 'Inactive phase' on G2, and 'Proteins are synthesized' is then left for the only slot still open, the quiescent stage
- **Why:** This question requires the job NCERT assigns to each phase of the cell cycle, demonstrated by row D pairing 'G1 Phase' with 'Interval between mitosis and initiation of DNA replication'.
<!--/ecat-->

## Q140

Biology · botany · Organisms and Populations

Match List I with List II : Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Mutualism | I | +(A), O(B) |
| B | Commensalism | II | –(A), O(B) |
| C | Amensalism | III | +(A), –(B) |
| D | Parasitism | IV | +(A), +(B) |

- **(1)** A-IV, B-I, C-II, D-III
- (2) A-IV, B-III, C-I, D-II
- (3) A-III, B-I, C-IV, D-II
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Mutualism benefits both species: $+(A), +(B)$, so $A \rightarrow IV$.
2. Commensalism benefits one species and leaves the other unaffected: $+(A), 0(B)$, so $B \rightarrow I$.
3. Amensalism harms one species and leaves the other unaffected: $-(A), 0(B)$, so $C \rightarrow II$.
4. Parasitism benefits the parasite and harms the host: $+(A), -(B)$, so $D \rightarrow III$.
5. $A$-IV, $B$-I, $C$-II, $D$-III matches option $1$.

**Subtopic:** Commensalism and Ammensalism, Mutualism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q140_4a5b6547_02112026.png?v=4a5b65476844)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Every interspecific interaction is written as a pair of signs for its two partners: mutualism +/+, commensalism +/0, amensalism -/0, parasitism +/-
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Amensalism and commensalism differ by two letters and both carry an O for the second partner, so a student who has not separated the names hands '+(A), O(B)' to amensalism and '–(A), O(B)' to commensalism
- **Why:** This question requires the +/0/- convention applied to each named interaction, demonstrated by List II printing sign pairs such as '–(A), O(B)' in place of any description of the organisms.
- **Note:** List II writes its two partners as (A) and (B), the same letters that label List I's rows A and B; the sense is NCERT's species A and species B, and the question is tagged as printed.
<!--/ecat-->

## Q141

Biology · botany · Organisms and Populations

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Gause’s ‘Competitive Exclusion Principle’ states that two closely related species competing for the same resources cannot co-exist indefinitely and competitively inferior one will be eliminated eventually.
- (Statement II) In general, carnivores are more adversely affected by competition than herbivores.

- (1) Both Statement I and Statement II are false.
- **(2)** Statement I is correct Statement II is false.
- (3) Statement I is incorrec but Statement II is true.
- (4) Both Statement I and Statement II are true.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement I: Gause's Competitive Exclusion Principle says two closely related species competing for the same resources cannot co-exist indefinitely and the competitively inferior one is eliminated, so Statement I is correct.
2. Statement II: in general, herbivores are more adversely affected by competition than carnivores, so Statement II is false.
3. Statement I correct and Statement II false matches option $2$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q141_0eae2528_02112026.png?v=0eae25287c03)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gause's competitive exclusion principle, and the textbook's comparison that herbivores and plants are hit harder by competition than carnivores
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Statement II has the printed comparison the wrong way round — the textbook says herbivores and plants are more adversely affected than carnivores — and a student who has the fact without its direction reads the sentence as a plausible claim about fierce competition among predators.
- **Why:** This question requires two stated ecology lines to be checked as printed, demonstrated by Statement II's "carnivores are more adversely affected by competition than herbivores" standing against the printed comparison.
<!--/ecat-->

## Q142

Biology · botany · Mineral Nutrition

Match List I with List II: Choos the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Iron | I | Synthesis of auxin |
| B | Zinc | II | Component of nitrate reductase |
| C | Boron | III | Activator of catalase |
| D | Molybdenum | IV | Cell elongation and differentiation |

- (1) A-II, B-III, C-IV, D-I
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-II, B-IV, C-I, D-III
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Iron (A) is an activator of catalase, so $A \rightarrow III$.
2. Zinc (B) is needed for the synthesis of auxin, so $B \rightarrow I$.
3. Boron (C) is required for cell elongation and differentiation, so $C \rightarrow IV$.
4. Molybdenum (D) is a component of nitrate reductase, so $D \rightarrow II$.
5. $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ matches option $2$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q142_24968016_02112026.png?v=249680163563)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each micronutrient has its own named job: iron activates catalase, zinc is needed to make auxin, boron drives cell elongation and differentiation, and molybdenum is a component of nitrate reductase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Iron is the metal carried for redox enzymes — cytochromes, ferredoxin — and nitrate reductase is a redox enzyme, so iron takes that line; 'activator of several enzymes' is zinc's other printed phrase, so zinc takes catalase, and molybdenum is left with auxin
- **Why:** This question requires the role NCERT states for each micronutrient, demonstrated by row D pairing 'Molybdenum' with 'Component of nitrate reductase'.
- **Note:** nearby_fact rather than look_alike_term: iron, zinc and molybdenum do not resemble one another at all, and the wrong roles are reachable because the chapter prints them in one run-on list of micronutrients — swap the element names for unlike words and the pull survives, so position is doing the work. The stem as extracted reads 'Choos the correct answer'; tagged as printed.
<!--/ecat-->

## Q143

Biology · botany · Principles of Inheritance and Variation

Which of the following statements are correct about Klinefelter’s Syndrome? Choose the correct answer from the options given below:

- (A) This disorder was first described by Langdon Down (1866).
- (B) Such an individual has overall masculine development. However, the feminine developement is also expressed.
- (C) The affected individual is short statured.
- (D) Physical, psychomotor and metal development is retarded.
- (E) Such individuals are sterile.

- (1) C and D only
- **(2)** B and E only
- (3) A and E only
- (4) A and B only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A is false: Langdon Down (1866) described Down's syndrome, not Klinefelter's syndrome.
2. B is true: a $47,XXY$ individual has overall masculine development, but feminine traits such as gynaecomastia are also expressed.
3. C is false: short stature is a feature of Down's syndrome (and Turner's), not Klinefelter's.
4. D is false: retarded physical, psychomotor and mental development is a feature of Down's syndrome.
5. E is true: Klinefelter individuals are sterile.
6. So only B and E are correct, which is option $2$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q143_b46333e7_02112026.png?v=b46333e764df)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Klinefelter's syndrome (47, XXY): masculine build with some feminine development, and sterility — the short stature belongs to Turner's and the retardation and 1866 description to Down's
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Statement B is the description of Klinefelter's almost word for word, so the option feels anchored, and the Langdon Down attribution in A is a name printed a page earlier in the same chromosomal-disorders section.
- **Why:** This question requires the stated features of one named chromosomal disorder, demonstrated by statement A's "first described by Langdon Down (1866)" and statement C's "short statured" belonging to the neighbouring disorders.
<!--/ecat-->

## Q144

Biology · botany · Anatomy of Flowering Plants

Identify the correct statements:
Choose the correct answer from the options given below:

- (A) Lenticels are the lens-shaped openings permitting the exchange of gases.
- (B) Bark formed early in the season is called hard bark.
- (C) Bark is a technical term that refers to all tissues exterior to vascular cambium.
- (D) Bark refers to periderm and secondary phloem.
- (E) Phellogen is single-layered in thickness.

- **(1)** A and D only
- (2) A, B and D only
- (3) B and C only
- (4) B, C and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A: lenticels are lens-shaped openings in the periderm that permit gas exchange, so $A$ is true.
2. B: bark formed early in the season is soft (early) bark, not hard bark, so $B$ is false.
3. C: bark is a non-technical term for all tissues exterior to the vascular cambium, so calling it a technical term makes $C$ false.
4. D: bark includes the periderm and the secondary phloem, so $D$ is true.
5. E: phellogen is a couple of layers thick, not single-layered, so $E$ is false.
6. True statements are $A$ and $D$ only, which is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q144_6adc8d1f_02112026.png?v=6adc8d1f53a8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bark is the non-technical term for everything outside the vascular cambium — periderm plus secondary phloem — and the bark formed early in the season is the soft bark
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A and D are both correct, so the option looks like the right set with one more fact added, and B is accepted because the early-season and late-season bark names have been exchanged: the printed pair is early or soft bark against late or hard bark.
- **Why:** This question requires the stated definitions in the secondary-growth passage, demonstrated by statement B's "early in the season is called hard bark" and statement C's "Bark is a technical term".
<!--/ecat-->

## Q145

Biology · botany · Molecular Basis of Inheritance

How many different proteins does the ribosome consist of?

- (1) 60
- (2) 40
- (3) 20
- **(4)** 80

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT teaches that the ribosome consists of structural RNAs and about $80$ different proteins, which is option $4$.

**Subtopic:** Translation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q145_e6ee6468_02112026.png?v=e6ee6468880f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A ribosome is built of structural RNAs together with about 80 different proteins
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  20 is the number this part of the chapter drills, the twenty amino acids that translation strings together, so a student holding one number for the translation section offers it; the figure printed for the ribosome's different proteins is about 80
- **Why:** This question requires one stored count, demonstrated by the stem 'How many different proteins does the ribosome consist of?' with four bare numbers and nothing given to compute from.
<!--/ecat-->

## Q146

Biology · botany · Biomolecules

Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of

- (1) Amylase
- (2) Lipase
- (3) Dinitrogenase
- **(4)** Succinic dehydrogenase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Malonate resembles succinate in structure, so it binds the active site of succinic dehydrogenase as a competitive inhibitor; this is option $4$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q146_9ff2705e_02112026.png?v=9ff2705ef853)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Malonate resembles succinate closely enough to sit in the active site of succinic dehydrogenase, which is the textbook case of competitive inhibition
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The stem names pathogenic bacteria, and this is the one option that is an exclusively bacterial enzyme, so a student reasoning that an inhibitor which kills bacteria must hit something only bacteria have picks it; the printed target of malonate is succinic dehydrogenase, an enzyme of respiration that bacteria share with us
- **Why:** This question requires one printed inhibitor-enzyme pairing, demonstrated by the stem 'Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of' with four enzymes and no structure or data given.
- **Note:** The stem prints 'Melonate' for malonate; the spelling is as stored in the paper and the compound meant is unambiguous from the key.
<!--/ecat-->

## Q147

Biology · botany · Transport in Plants

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Cohesion | I | More attraction in liquid phase |
| B | Adhesion | II | Mutual attraction among water molecules |
| C | Surface tension | III | Water loss in liquid phase |
| D | Guttation | IV | Attraction towards polar surfaces |

- (1) A – IV, B – III, C – II, D – I
- (2) A – III, B – I, C – IV, D – II
- (3) A – II, B – I, C – IV, D – III
- **(4)** A – II, B – IV, C – I, D – III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Cohesion is the mutual attraction among water molecules, so $A \rightarrow II$.
2. Adhesion is the attraction of water molecules to polar surfaces, so $B \rightarrow IV$.
3. Surface tension arises because water molecules are more attracted to each other in the liquid phase than in the gas phase, so $C \rightarrow I$.
4. Guttation is the loss of water in liquid form (from hydathodes), so $D \rightarrow III$.
5. $A-II,\ B-IV,\ C-I,\ D-III$ matches option $4$.

**Subtopic:** Transpiration and Stomatal Opening and Closing, Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q147_aa7b8626_02112026.png?v=aa7b86266f4f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Cohesion is water pulling on water, adhesion is water pulling on polar surfaces, surface tension is that pull being stronger inside the liquid than at the gas boundary, and guttation is water lost as liquid
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The word 'surface' sits in both 'Surface tension' and 'Attraction towards polar surfaces', and once surface tension is pulled onto that entry the only line left for adhesion is 'More attraction in liquid phase'
- **Why:** This question requires telling three near-identical statements of water's attractive forces apart, demonstrated by List II carrying both 'Mutual attraction among water molecules' and 'More attraction in liquid phase'.
- **Note:** look_alike_term rather than nearby_fact: replace 'polar surfaces' with 'polar walls' and the pull of entry IV on 'Surface tension' dies, so the resemblance of the words, not the printed position of the entries, carries it. compare is used here, against fact_line on the other match items in this packet, because two List II entries state the same attraction in nearly the same words and the row demand is separating them.
<!--/ecat-->

## Q148

Biology · botany · Respiration in Plants

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Oxidative decarboxylation | I | Citrate synthase |
| B | Glycolysis | II | Pyruvate dehydrogenase |
| C | Oxidative phosphorylation | III | Electron transport system |
| D | Tricarboxylic acid cycle | IV | EMP pathway |

- (1) A – II, B – IV, C – I, D – III
- (2) A – III, B – I, C – II, D – IV
- **(3)** A – II, B – IV, C – III, D – I
- (4) A – III, B – IV, C – II, D – I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Oxidative decarboxylation of pyruvate to acetyl CoA is catalysed by pyruvate dehydrogenase, so $A \to II$.
2. Glycolysis is also called the EMP (Embden-Meyerhof-Parnas) pathway, so $B \to IV$.
3. Oxidative phosphorylation is coupled to the electron transport system, so $C \to III$.
4. The TCA cycle begins with acetyl CoA + OAA forming citrate via citrate synthase, so $D \to I$.
5. $A-II, B-IV, C-III, D-I$ matches option $3$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q148_750a8d43_02112026.png?v=750a8d433520)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each stage of respiration has its own catalyst or system: pyruvate dehydrogenase for the oxidative decarboxylation of pyruvate, the EMP pathway for glycolysis, the electron transport system for oxidative phosphorylation, and citrate synthase inside the TCA cycle
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The two List I entries that begin 'Oxidative' are exchanged: hearing 'oxidative' as the oxidation that happens on the respiratory chain gives the electron transport system to oxidative decarboxylation, and pyruvate dehydrogenase is then left for oxidative phosphorylation
- **Why:** This question requires which catalyst or system serves which stage of respiration, demonstrated by row C pairing 'Oxidative phosphorylation' with 'Electron transport system'.
- **Note:** look_alike_term rather than nearby_fact: the exchange is held up by the shared word 'oxidative' in two List I entries, and renaming either one kills it, so the resemblance rather than the printed order is doing the work.
<!--/ecat-->

## Q149

Biology · botany · Morphology of Flowering Plants

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem.
- (Reason R) Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves.

- (1) Both A and R are true but R is NOT the correct explanation of A
- (2) A is true but R is false
- (3) A is false but R is true
- **(4)** Both A and R are true and R correct explanation of A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Assertion A matches the NCERT definition: the flower is a modified shoot in which the shoot apical meristem changes to a floral meristem, so A is true.
2. Reason R is true: internodes do not elongate, the axis condenses, and floral appendages form laterally at successive nodes instead of leaves.
3. R describes how the shoot is modified into a flower, so R explains A, which is option $4$.

**Subtopic:** The Flower · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q149_a061b400_02112026.png?v=a061b4001264)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A flower is a modified shoot: the apical meristem turns floral, the axis stops elongating, and floral appendages replace leaves at successive nodes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A is printed as a definition, so a student treats it as needing no cause and reads R's condensed internodes and lateral appendages as a further description of a flower rather than as the account of how the shoot is modified
- **Why:** This question requires the explanation of why a flower counts as a modified shoot, demonstrated by R, 'Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves', standing behind A's definition.
- **Note:** Option 4 as extracted reads 'R correct explanation of A', missing 'is the'; the sense is the standard fourth verdict and the question is tagged as printed.
<!--/ecat-->

## Q150

Biology · botany · Biotechnology: Principles and Processes

Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence. Choose the correct answer from the options given below :

- (A) Insertion of recombinant DNA into the host cell
- (B) Cutting of DNA at specific location by restriction enzyme
- (C) Isolation of desired DNA fragment
- (D) Amplification of gene of interest using PCR

- (1) C, A, B, D
- (2) C, B, D, A
- (3) B, D, A, C
- **(4)** B, C, D, A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Genomic DNA is first cut at specific locations by a restriction enzyme: step $B$.
2. The desired DNA fragment is then separated and isolated (e.g. by gel electrophoresis): step $C$.
3. The gene of interest is amplified using PCR: step $D$.
4. The recombinant DNA is finally inserted into the host cell: step $A$.
5. Sequence $B \to C \to D \to A$ matches option $4$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q150_1ad2c18f_02112026.png?v=1ad2c18f3b0b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Recombinant DNA is made by cutting the DNA with a restriction enzyme, isolating the desired fragment, amplifying it by PCR and only then putting it into the host
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  Isolation is read as the first move — you get the DNA before you cut it — so C is placed ahead of B; the isolation this list names is of the DESIRED FRAGMENT, which cannot exist until the restriction enzyme has cut.
- **Why:** This question requires the stated sequence of recombinant DNA formation, demonstrated by the stem's "Arrange these steps in a correct sequence" over the four lettered steps.
- **Note:** Label chosen as wrong_site_attacked because the right step is placed at the wrong stage; reversed was ruled out by its own exclusion — one swapped pair inside a longer order is not an inverted order, and only B and C change places.
<!--/ecat-->

## Q151

Biology · zoology · Human Reproduction

Which of the following statements are correct regarding female reproductive cycle? Choose the most appropriate answer from the options given below.

- (A) In non-primate mammals cyclical changes during reproduction are called oestrus cycle.
- (B) First menstrual cycle begins at puberty and is called menopause.
- (C) Lack of menstruation may be indicative of pregnancy.
- (D) Cyclic menstruation extends between menarche and menopause.

- (1) A and B only
- (2) A, B and C only
- **(3)** A, C and D only
- (4) A and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement A: in non-primate mammals the reproductive cyclical changes are called the oestrus cycle, so $A$ is true.
2. Statement B: the first menstruation at puberty is called menarche, not menopause, so $B$ is false.
3. Statement C: lack of menstruation may indicate pregnancy, so $C$ is true.
4. Statement D: cyclic menstruation extends between menarche and menopause, so $D$ is true.
5. True set is $\{A, C, D\}$, which matches option $3$ (A, C and D only).

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q151_2aedfbe9_02112026.png?v=2aedfbe90319)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Menarche is the first menstrual cycle and menopause the last; cyclic menstruation runs between them, and non-primate mammals show an oestrus cycle instead
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  A and C are both correct, and B is accepted because menarche and menopause are taken as one word for the start of menstruation — the two names differ only after their shared opening.
- **Why:** This question requires the stated vocabulary of the menstrual cycle, demonstrated by statement B's "First menstrual cycle begins at puberty and is called menopause".
- **Note:** Swap test applied: replace menarche and menopause with two unlike words and the trap dies, because what carries the student is the near-identity of the two names, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q152

Biology · zoology · Reproductive Health

Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below.

- (Assertion A) Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme.
- (Reason R) Ban on amniocentesis checks increasing menace of female foeticide.

- (1) Both A and R are true and R is NOT the correct explanation of A.
- (2) A is true but R is false.
- **(3)** A is false but R is true.
- (4) Both A and R are true and R is the correct explanation of A.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Under the RCH programme, one strategy is the statutory ban on amniocentesis for sex determination, so using amniocentesis for sex determination is not a strategy: Assertion $A$ is false.
2. The ban on amniocentesis for sex determination is meant to check the rising menace of female foeticide, so Reason $R$ is true.
3. $A$ false and $R$ true matches option $3$.

**Subtopic:** Reproductive Health – Problems and Strategies, MTP and Amniocentesis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q152_f7911d2b_02112026.png?v=f7911d2b364a)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What the Reproductive and Child Health Care Programme adopts is the statutory ban on amniocentesis for sex determination, because the test was being used for female foeticide
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The programme's strategy is the BAN on amniocentesis for sex determination, and A prints the practice itself as the strategy; a student who recalls only that amniocentesis sits among the programme's measures grants A, and R, which does state the ban, then reads as confirming it
- **Why:** This question requires what the programme actually prescribes about amniocentesis, demonstrated by A calling 'Amniocentesis for sex determination' one of its strategies while R names the 'Ban on amniocentesis'.
<!--/ecat-->

## Q153

Biology · zoology · Organisms and Populations

Match List I with List II. Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | A Leopard and a Lion in a forest/grassland | I | Competition |
| B | A Cuckoo laying egg in a Crow’s nest | II | Brood parasitism |
| C | Fungi and root of a higher plant in Mycorrhizae | III | Mutualism |
| D | A cattle egret and a Cattle in a field | IV | Commensalism |

- (1) A-I, B-II, C-IV, D-III
- (2) A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-I, D-IV
- **(4)** A-I, B-II, C-III, D-IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A leopard and a lion share prey in the same habitat, so A is competition: $A \to I$.
2. A cuckoo lays its eggs in a crow's nest for the host to incubate, so B is brood parasitism: $B \to II$.
3. In mycorrhizae the fungus and the plant root both benefit, so C is mutualism: $C \to III$.
4. The cattle egret feeds on insects stirred up by grazing cattle and the cattle are unaffected, so D is commensalism: $D \to IV$.
5. $A-I, B-II, C-III, D-IV$ matches option $4$.

**Subtopic:** Mutualism, Commensalism and Ammensalism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q153_8f168463_02112026.png?v=8f1684632280)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Interactions are named from who gains and who loses: two big cats after the same prey compete, a cuckoo in a crow's nest is a brood parasite, fungus and root in a mycorrhiza both gain, and the egret gains while the cattle are unaffected
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The cattle egret is moved one box over into mutualism by crediting the cattle with a benefit from the insects the egret takes, and commensalism is then the only label left for the mycorrhiza
- **Why:** This question requires the interaction each printed example illustrates, demonstrated by row D, 'A cattle egret and a Cattle in a field', set against 'Commensalism'.
- **Note:** nearby_fact rather than look_alike_term: mutualism and commensalism do not resemble each other as words, and the pull is that they are adjacent boxes in the same list of interactions with the egret printed under one of them — rename the categories and the pull survives, so position is doing the work. The key here is also the straight positional code A-I, B-II, C-III, D-IV, so no option can be struck out for being the parallel mapping.
<!--/ecat-->

## Q154

Biology · zoology · Breathing and Exchange of Gases

Vital capacity of lung is _________.

- (1) $\mathrm{IRV + ERV + TV + RV}$
- (2) $\mathrm{IRV + ERV + TV - RV}$
- **(3)** $\mathrm{IRV + ERV + TV}$
- (4) $\mathrm{IRV + ERV}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Vital capacity is the maximum volume of air a person can breathe out after a forced inspiration, so $VC = \mathrm{IRV + TV + ERV}$, which excludes $\mathrm{RV}$; this is option $3$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q154_ccdbfcf5_02112026.png?v=ccdbfcf5f2b3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Vital capacity is all the air a person can actually move - IRV plus TV plus ERV - and it leaves out the residual volume, which cannot be breathed out
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  This is the printed sum for total lung capacity, which the same section defines as RV, ERV, TV and IRV together, so a student who has learnt one four-term sum for the lungs writes it here; vital capacity is the same sum with the residual volume taken out, because that volume can never be exhaled
- **Why:** This question requires one printed definition, demonstrated by the blank in 'Vital capacity of lung is _________.' with four rival sums of the respiratory volumes as options.
- **Note:** E1 returned fill_in_blank, which the codebook treats as an overlay rather than a shape; the primary printed shape is a plain four-answer question, so qtype is recorded as mcq.
<!--/ecat-->

## Q155

Biology · zoology · Reproductive Health

Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?

- **(1)** Gonorrhoea
- (2) Hepatitis-B
- (3) HIV Infection
- (4) Genital herpes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT states that, except for hepatitis-B, genital herpes and HIV infection, the other STDs are completely curable if detected early and treated properly, so gonorrhoea (option $1$) is the answer.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q155_82094084_02112026.png?v=82094084f12b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sexually transmitted infections are completely curable if caught early, except for the three the text names: hepatitis-B, genital herpes and HIV infection
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The three wrong options are exactly the three names in the printed 'except for' clause, so a student who has stored those names as the ones that sentence is about, without its polarity, reads them as the curable ones; hepatitis-B is the one that independently reads as manageable, because the course teaches that a vaccine for it exists
- **Why:** This question requires one printed clause about curability, demonstrated by the stem asking which infection is 'completely curable when detected early and treated properly' with the other three options being the text's named exceptions.
<!--/ecat-->

## Q156

Biology · zoology · Chemical Coordination and Integration

Math List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | CCK | I | Kidney |
| B | GIP | II | Heart |
| C | ANF | III | Gastric gland |
| D | ADH | IV | Pancreas |

- (1) A-III, B-II, C-IV, D-I
- (2) A-II, B-IV, C-I, D-III
- (3) A-IV, B-II, C-III, D-I
- **(4)** A-IV, B-III, C-II, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. CCK acts on the pancreas (pancreatic enzyme secretion) and gall bladder, so $A \to IV$.
2. GIP inhibits gastric secretion and motility, so it relates to the gastric gland: $B \to III$.
3. ANF is secreted by the atrial wall of the heart: $C \to II$.
4. ADH acts on the distal tubules of the kidney: $D \to I$.
5. $A-IV, B-III, C-II, D-I$ is option $4$.

**Subtopic:** Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q156_1ac8d9f0_02112026.png?v=1ac8d9f00e1c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each of CCK, GIP, ANF and ADH is learnt with one organ: the pancreas, the gastric gland, the heart and the kidney
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  CCK acting on the pancreas and ADH acting on the kidney are the two pairs a reader of the hormone list can state outright, and option 3 is the only other code that carries both, so it survives the elimination those two facts perform while the untested GIP and ANF pairs ride along inside it.
- **Why:** This question requires the organ the source ties to each named hormone, demonstrated by List II holding four organs — 'Kidney', 'Heart', 'Gastric gland', 'Pancreas' — with no criterion printed to work from.
- **Note:** Stem reads 'Math List I with List II'; the c has been lost from 'Match' in our record. Lists, options and key are intact, so the rating stands.
<!--/ecat-->

## Q157

Biology · zoology · Human Health and Disease

Math List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Ringworm | I | Haemophilus influenzae |
| B | Filariasis | II | Trichophyton |
| C | Malaria | III | Wuchereria bancrofti |
| D | Pneumonia | IV | Plasmodium vivax |

- (1) A-II, B-III, C-I, D-IV
- (2) A-III, B-II, C-I, D-IV
- (3) A-III, B-II, C-IV, D-I
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Ringworm is a fungal disease caused by $Trichophyton$ (A-II); filariasis is caused by $Wuchereria\ bancrofti$ (B-III); malaria is caused by $Plasmodium\ vivax$ (C-IV); pneumonia is caused by $Haemophilus\ influenzae$ (D-I), so A-II, B-III, C-IV, D-I is option $4$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q157_d38483c7_02112026.png?v=d38483c772d4)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ringworm is a fungal disease despite its name, and each common human disease is learnt with the one agent NCERT names for it
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The word 'worm' sits inside 'Ringworm' and Wuchereria bancrofti is the only worm in List II, so the disease name itself hands over the wrong agent and pushes Trichophyton across onto filariasis.
- **Why:** This question requires the agent the source names for each disease, demonstrated by List II holding four organisms — 'Trichophyton', 'Wuchereria bancrofti', 'Plasmodium vivax', 'Haemophilus influenzae' — each printed against one named disease.
- **Note:** Swap test applied for look_alike_term against nearby_fact: replace Wuchereria bancrofti with an agent that is not a worm and the pull dies, so the likeness between 'ringworm' and a worm is doing the work, not the two agents' position in the disease table. Stem reads 'Math List I with List II'; 'Match' has lost its c in our record.
<!--/ecat-->

## Q158

Biology · zoology · Body Fluids and Circulation

Math List I with List II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P-wave | I | Beginning of systole |
| B | Q-wave | II | Repolarisation of ventricles |
| C | QRS complex | III | Depolarisation of atria |
| D | T-wave | IV | Depolarisation of ventricles |

- (1) A-IV, B-III, C-II, D-I
- (2) A-II, B-IV, C-I, D-III
- (3) A-I, B-II, C-III, D-IV
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the NCERT ECG, the P-wave is depolarisation of the atria ($A \to III$), the QRS complex is depolarisation of the ventricles ($C \to IV$), the T-wave is repolarisation of the ventricles ($D \to II$), and the Q-wave marks the beginning of systole ($B \to I$), so the match is option $4$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q158_0f730e76_02112026.png?v=0f730e7695bd)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each ECG deflection marks one electrical event: P the atrial depolarisation, QRS the ventricular depolarisation, Q the start of systole, T the ventricular repolarisation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  'Beginning of systole' is printed in the sentence straight after the QRS sentence and names only the bare letter Q, so the phrase is carried onto the whole QRS complex, and option 2 is the only code that offers C-I.
- **Why:** This question requires the electrical event the source assigns to each named deflection, demonstrated by List II holding 'Depolarisation of atria', 'Depolarisation of ventricles', 'Repolarisation of ventricles' and 'Beginning of systole' against the P, Q, QRS and T labels.
- **Note:** Every distractor pairs the P-wave with something other than atrial depolarisation, so the single line 'the P-wave represents the depolarisation of the atria' settles the question on its own. Option 3 is the straight positional mapping A-I, B-II, C-III, D-IV, recorded in its proof. Stem reads 'Math List I with List II'.
<!--/ecat-->

## Q159

Biology · zoology · Human Health and Disease

In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?

- (1) B-lymphocytes
- (2) Basophils
- (3) Eosinophils
- **(4)** $\mathrm{T_H}$ cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, HIV enters macrophages, its RNA is reverse-transcribed into DNA, and the virus then enters helper T-lymphocytes ($\mathrm{T_H}$ cells), where it replicates and produces progeny viruses, so the answer is option $4$.

**Subtopic:** AIDS · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q159_77f79442_02112026.png?v=77f79442eda5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** HIV enters macrophages and helper T-lymphocytes, and it is inside the TH cells that it replicates and turns out progeny viruses
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The option differs from the key by one letter in the cell's name, B-lymphocyte against T-lymphocyte, so a student who has stored 'HIV attacks lymphocytes' without the letter produces the other one; the AIDS account names the helper T-lymphocytes as the site of replication
- **Why:** This question requires one printed cell type, demonstrated by the stem 'In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?' with four named corpuscles and nothing to deduce from.
- **Note:** The swap test was applied for the trap axis: replacing B-lymphocytes with an unlike cell name would largely kill the pull, since what carries the student is that the two names differ by a single letter, so likeness rather than position decides it.
<!--/ecat-->

## Q160

Biology · zoology · Biomolecules

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.
- (Statement II) When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor.

- (1) Both Statement I and Statement II are false.
- (2) Statement I is true but Statement II is flase.
- (3) Statement I is false but Statement II is true.
- **(4)** Both Statement I and Statement II are true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: low temperature keeps an enzyme temporarily inactive, while high temperature denatures the protein and destroys its activity, so Statement I is true.
2. Statement II: an inhibitor that closely resembles the substrate in molecular structure and inhibits the enzyme is a competitive inhibitor, so Statement II is true.
3. Both statements are true, which is option $4$.

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q160_d07829ab_02112026.png?v=d07829ab4f03)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Low temperature inactivates an enzyme only temporarily while heat denatures it, and a competitive inhibitor is one whose structure resembles the substrate
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  "Closely resembles the substrate" gets attached to non-competitive inhibition by a student who holds the two inhibitor names as one pair, so Statement II is marked false while Statement I is accepted.
- **Why:** This question requires two stated enzyme facts to be checked as printed, demonstrated by Statement II's "closely resembles the substrate … known as competitive inhibitor".
- **Note:** Swap test applied: replace 'competitive' with an unlike word and the trap dies, because what carries the student is the near-identity of the names competitive and non-competitive, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q161

Biology · zoology · Structural Organisation in Animals

Given below are two statements:
Statement I: Ligaments are dense irregular tissue.
Statement II: Cartilage is dense regular tissue.
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Ligaments are dense irregular tissue.
- (Statement II) Cartilage is dense regular tissue.

- **(1)** Both Statement I and Statement II are false
- (2) Statement I is true but Statement II is false
- (3) Statement I is false but Statement II is true
- (4) Both Statement I and Statement II are true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: ligaments (bone to bone) are dense regular connective tissue with parallel collagen fibres, so calling them dense irregular is false.
2. Statement II: cartilage is a specialised connective tissue, not dense regular tissue, so Statement II is false.
3. Both statements false, which is option $1$.

**Subtopic:** Connective Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q161_3ba5a557_02112026.png?v=3ba5a5570dcd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Dense regular connective tissue is the tendon and ligament class and dense irregular is the fibre network of the skin; cartilage belongs to neither, being a specialised skeletal tissue
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who knows ligaments are dense REGULAR tissue rejects Statement I and then has to put that term somewhere, and cartilage is the class printed next in the connective-tissue sequence, so Statement II looks like the term's proper home.
- **Why:** This question requires two neighbouring connective-tissue classes to be held apart, demonstrated by the statements printing "dense irregular tissue" against "dense regular tissue" on two different tissues.
- **Note:** asks is compare rather than fact_line because the two printed statements set the same property axis — regular against irregular packing — on two tissues, so the work is separating the classes, not retrieving one line.
<!--/ecat-->

## Q162

Biology · zoology · Cell: The Unit of Life

Which of the following are NOT considered as the part of endomembrane system? Choose the most appropriate answer from the options given below:

- (A) Mitochondria
- (B) Endoplasmic reticulum
- (C) Chloroplasts
- (D) Golgi complex
- (E) Peroxisomes

- **(1)** A, C and E only
- (2) A and D only
- (3) A, D and E only
- (4) B and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the endomembrane system comprises the endoplasmic reticulum, Golgi complex, lysosomes and vacuoles, whose functions are coordinated; mitochondria, chloroplasts and peroxisomes are not included, so the answer is A, C and E only, option $1$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q162_ad4feab3_02112026.png?v=ad4feab36968)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The endomembrane system is the ER, Golgi complex, lysosomes and vacuoles; mitochondria, chloroplasts and peroxisomes are kept out of it
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Endoplasmic reticulum and Golgi complex are the first two members the printed definition of the system lists, so the pair is true of the system and answers "which ARE part of it" — the stem asked which are NOT.
- **Why:** This question requires the stated membership of the endomembrane system, demonstrated by the stem's "NOT considered as the part of endomembrane system" against the option "B and D only".
<!--/ecat-->

## Q163

Biology · zoology · Biomolecules

Given below are two statements:

In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal).
- (Statement II) Adult human haemoglobin, consists of 4 subunits (two subunits of $\alpha$ type and two subunits of $\beta$ type.)

- (1) Both Statement I and Statement II are false.
- (2) Statement I is true but Statement II is false.
- **(3)** Statement I is false but Statement II is true.
- (4) Both Statement I and Statement II are true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: by convention the first amino acid at the left end is the N-terminal and the last at the right end is the C-terminal; the statement swaps them, so it is false.
2. Statement II: adult human haemoglobin is a tetramer of two $\alpha$ and two $\beta$ subunits, so it is true.
3. I false, II true, which is option $3$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q163_ea1c2f28_02112026.png?v=ea1c2f289f9c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A polypeptide is written with the first amino acid as the N-terminal and the last as the C-terminal; adult haemoglobin is a four-subunit protein of two alpha and two beta chains
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Statement I is the textbook's own picture of a protein as a line with a first and a last amino acid, with only the two terminal names exchanged, so a student who recognises the sentence accepts it and, Statement II being true, marks both correct.
- **Why:** This question requires two stated biomolecule facts to be checked as printed, demonstrated by Statement I naming "first amino acid (C-terminal)" and "last amino acid (N-terminal)".
<!--/ecat-->

## Q164

Biology · zoology · Principles of Inheritance and Variation

Broad palm with single palm crease is visible in a person suffering from-

- (1) Turner’s syndrome
- (2) Klinefelter’s syndrome
- (3) Thalassemia
- **(4)** Down’s syndrome

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, Down's syndrome (trisomy of chromosome $21$) shows a broad palm with a characteristic single palm crease, so the answer is option $4$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q164_0ce661f4_02112026.png?v=0ce661f4975e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Down's syndrome is the trisomy whose printed description includes a broad palm with a single characteristic crease
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Klinefelter's syndrome is the paragraph printed immediately after Down's in the same chromosomal-disorders section, so a student holding the three syndromes as one block without their separate feature lists takes the neighbouring one.
- **Why:** This question requires one feature from one syndrome's printed description, demonstrated by the stem quoting that feature and nothing else — 'broad palm with single palm crease is visible in a person suffering from'.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: 'Down's' and 'Klinefelter's' resemble each other in no way, and replacing them with two unlike names leaves the pull intact, because what carries it is the three syndromes being printed as one block.
<!--/ecat-->

## Q165

Biology · zoology · Environmental Issues

Which of the follwoing statements is correct?

- **(1)** Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.
- (2) Presence of large amount of nutrients in water restricts ‘Algal Bloom’
- (3) Algal Bloom decreases fish mortality
- (4) Eutrophication refers to increase in domestic sewage and waste water in lakes.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Option 1 is the NCERT definition of biomagnification (increase in toxicant concentration at successive trophic levels), so it is correct; options 2, 3 and 4 are false because nutrients cause algal blooms, algal blooms increase fish mortality, and eutrophication is the natural ageing of a lake by nutrient enrichment.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q165_18e84d83_02112026.png?v=18e84d83fe53)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biomagnification is the rise in a toxicant's concentration at each higher trophic level, while eutrophication is nutrient enrichment ageing a lake and algal blooms worsen water quality and kill fish
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Domestic sewage is printed beside the eutrophication definition as what accelerates the process, so the cause is read back as the definition; eutrophication is the nutrient enrichment and ageing of the lake, not the inflow of sewage itself.
- **Why:** This question requires each printed definition to be checked against a claim, demonstrated by the stem being only 'Which of the follwoing statements is correct?' with four rival claims about biomagnification, algal bloom and eutrophication below it.
- **Note:** qtype is statements, not mcq: the stem asks for the correct STATEMENT, which is the case the qtype rule names, even though no lettered block is printed. The stem's spelling 'follwoing' is as printed in the source.
<!--/ecat-->

## Q166

Biology · zoology · Excretory Products and Their Elimination

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Taenia | I | Nephridia |
| B | Paramoecium | II | Contractile vacuole |
| C | Periplaneta | III | Flame cells |
| D | Pheretima | IV | Urecose gland |

- (1) A-I, B-II, C-IV, D-III
- **(2)** A-III, B-II, C-IV, D-I
- (3) A-II, B-I, C-IV, D-III
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Taenia (Platyhelminthes) excretes through flame cells: $A \rightarrow III$.
2. Paramoecium (protist) uses a contractile vacuole for osmoregulation and excretion: $B \rightarrow II$.
3. Periplaneta (cockroach) has urecose glands that help in excretion: $C \rightarrow IV$.
4. Pheretima (earthworm) excretes through nephridia: $D \rightarrow I$.
5. $A-III, B-II, C-IV, D-I$ is option $2$.

**Subtopic:** Excretory Waste and Structure of Excretory System in Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q166_3f299be8_02112026.png?v=3f299be8a1a6)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each animal group has its own excretory organ: flame cells in flatworms, contractile vacuole in protozoans, uricose glands in insects, nephridia in annelids
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Flame cells and nephridia are printed a sentence apart as the excretory structures of the two worms on this list, and option 1 keeps the two pairs a reader can state outright — Paramoecium's contractile vacuole and the cockroach's uricose gland — while handing the tapeworm the earthworm's organ.
- **Why:** This question requires the excretory structure the source names for each animal, demonstrated by List II holding 'Nephridia', 'Contractile vacuole', 'Flame cells' and 'Urecose gland' against four named animals.
- **Note:** Swap test applied: 'flame cells' and 'nephridia' do not resemble each other as words, and replacing them with two unlike terms leaves the pull intact, because what carries the reader is that the source prints the two worm structures side by side. Hence nearby_fact, not look_alike_term. List II prints 'Urecose gland'; the standard spelling is uricose gland. The misspelling does not change which animal it belongs to.
<!--/ecat-->

## Q167

Biology · zoology · Environmental Issues

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Electrostatic precipitator is most widely used in thermal power plant .
- (Statement II) Electrostatic precipitator in thermal power plant removes ionising radiations.

- (1) Both Statement I and Statement II are incorrect.
- **(2)** Statement I is correct but Statement II is incorrect.
- (3) Statement I is incorrect but Statement II is correct.
- (4) Both Statement I and Statement II are correct.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement I: the electrostatic precipitator is the most widely used method to remove particulate matter from thermal power plant exhaust, so Statement I is correct.
2. Statement II: an electrostatic precipitator charges and collects particulate matter (dust) using electrodes; it does not remove ionising radiation, so Statement II is incorrect.
3. Statement I correct, Statement II incorrect, which is option $2$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q167_b9b984b8_02112026.png?v=b9b984b883ba)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The electrostatic precipitator is the thermal-power-plant device that removes particulate matter from the exhaust, not radiation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The device-and-plant pairing in Statement I is right, so Statement II reads as the same sentence continued, and "ionising radiations" is a pollutant term the chapter supplies a few pages away in the radioactive-waste passage.
- **Why:** This question requires the stated function of a named pollution-control device, demonstrated by Statement II's "removes ionising radiations".
- **Note:** Swap test applied: 'ionising radiations' and 'particulate matter' do not resemble each other as names, and replacing the term with another unlike pollutant from the same chapter keeps the trap alive, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q168

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct.
- (Statement II) The cavity of the cervix is called cervical canal which along with vagina forms birth canal.

- (1) Both Statement I and Statement II are false.
- (2) Statement I is correct but Statement II is false.
- (3) Statement I is incorrect but Statement II is true.
- **(4)** Both Statement I and Statement II are true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: the vas deferens receives a duct from the seminal vesicle and opens into the urethra as the ejaculatory duct, so Statement I is true.
2. Statement II: the cavity of the cervix is the cervical canal, which together with the vagina forms the birth canal, so Statement II is true.
3. Both statements are true, which is option $4$.

**Subtopic:** The Male Reproductive System, The Female Reproductive System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q168_ecd0e0b7_02112026.png?v=ecd0e0b76524)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The vas deferens joins the seminal vesicle duct to continue as the ejaculatory duct into the urethra, and the cervical canal together with the vagina makes the birth canal
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The line carried away from the female-system description is that the vagina is the birth canal, so the printed sentence adding the cervical canal to it looks like an overstatement and Statement II gets marked false while the male sentence is accepted.
- **Why:** This question requires two stated anatomical lines to be checked as printed, demonstrated by Statement II's "cervical canal which along with vagina forms birth canal".
<!--/ecat-->

## Q169

Biology · zoology · Animal Kingdom

Radial symmetry is NOT found in adults of phylum ______.

- **(1)** Hemichordata
- (2) Coelenterata
- (3) Echinodermata
- (4) Ctenophora

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Coelenterata, Ctenophora and adult Echinodermata are radially symmetrical, while Hemichordata are bilaterally symmetrical, so the answer is option $1$.

**Subtopic:** Phylum – Echinodermata and Hemichordata · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q169_a1bd48fe_02112026.png?v=a1bd48fe0a35)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Echinoderms, coelenterates and ctenophores are radially symmetrical as adults; hemichordates are bilaterally symmetrical, which is why they are the odd phylum here
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The echinoderm line reads 'adults are radially symmetrical while larvae are bilaterally symmetrical', and read the other way round it says radial symmetry is absent in the adults — which is exactly what this stem asks for.
- **Why:** This question requires which phylum's adults are not radial, demonstrated by the stem's own restriction to one stage — 'radial symmetry is NOT found in adults of phylum ______'.
- **Note:** E1 called this fill_in_blank, an overlay on a shape rather than a shape, so the printed shape underneath is a plain MCQ and qtype is mcq. reversed rather than nearby_fact: the option is reached by inverting a printed two-stage statement, not by taking a fact printed beside it.
<!--/ecat-->

## Q170

Biology · zoology · Digestion and Absorption

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Peptic cells | I | Mucus |
| B | Goblet cells | II | Bile juice |
| C | Oxyntic cells | III | Proenzyme pepsinogen |
| D | Hepatic cells | IV | $\mathrm{HCl}$ and intrinsic factor for absorption of vitamin $\mathrm{B_{12}}$ |

- (1) A-II, B-I, C-III, D-IV
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Peptic (chief) cells secrete the proenzyme pepsinogen: $A \rightarrow III$.
2. Goblet cells secrete mucus: $B \rightarrow I$.
3. Oxyntic (parietal) cells secrete HCl and intrinsic factor for vitamin $B_{12}$ absorption: $C \rightarrow IV$.
4. Hepatic cells secrete bile juice: $D \rightarrow II$.
5. The match $A$-$III$, $B$-$I$, $C$-$IV$, $D$-$II$ is option $2$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q170_4ab8c044_02112026.png?v=4ab8c04485e0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each gastric gland cell type has one secretion — peptic cells pepsinogen, oxyntic cells HCl with intrinsic factor, goblet cells mucus — while bile comes from hepatic cells
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The peptic cells and the oxyntic cells are two clauses of a single sentence listing the gastric gland's cell types, so a reader who holds the list but not which clause carried pepsinogen reads it onto the oxyntic cell, and option 1 is the only other code that keeps goblet cells with mucus.
- **Why:** This question requires the secretion the source assigns to each named cell, demonstrated by List II holding 'Mucus', 'Bile juice', 'Proenzyme pepsinogen' and 'HCl and intrinsic factor for absorption of vitamin B12'.
<!--/ecat-->

## Q171

Biology · zoology · Neural Control and Coordination

Match List I with List II with respect in human eye.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Fovea | I | Visible coloured portion of eye that regulates diameter of pupil. |
| B | Iris | II | External layer of eye formed of dense connective tissue. |
| C | Blind spot | III | Point of greatest visual acuity or resolution. |
| D | Sclera | IV | Point where optic nerve leaves the eyeball and photoreceptor cells are absent. |

- (1) A-IV, B-III, C-II, D-I
- (2) A-I, B-IV, C-III, D-II
- (3) A-II, B-I, C-III, D-IV
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Fovea is the point of greatest visual acuity: $A \to III$.
2. Iris is the visible coloured portion that regulates pupil diameter: $B \to I$.
3. Blind spot is where the optic nerve leaves the eyeball and photoreceptors are absent: $C \to IV$.
4. Sclera is the external layer of dense connective tissue: $D \to II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $4$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q171_a5d048a5_02112026.png?v=a5d048a55e4a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The retina's two named points are opposites: the fovea gives greatest visual acuity, the blind spot has no photoreceptors because the optic nerve leaves there
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The fovea and the blind spot are the two points the eye chapter names one after the other on the retina, and option 3 is the code that keeps the self-identifying iris pair while handing the acuity line to the blind spot.
- **Why:** This question requires which named part of the eye each printed description belongs to, demonstrated by List II spelling out 'Point where optic nerve leaves the eyeball and photoreceptor cells are absent' and 'Point of greatest visual acuity or resolution'.
- **Note:** The fovea / blind spot confusion is offered on two codes, options 2 and 3; option 3 is named as the trap because it is the one that also keeps the iris pair the description states outright.
<!--/ecat-->

## Q172

Biology · zoology · Cell: The Unit of Life

Which of the following functions is carried out by cytoskeleton in a cell?

- (1) Protein synthesis
- **(2)** Motility
- (3) Transportation
- (4) Nuclear division

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT lists the cytoskeleton's functions as mechanical support, motility and maintenance of cell shape, so the answer is option $2$ (Motility).

**Subtopic:** Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q172_5b459be0_02112026.png?v=5b459be04d02)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The cytoskeleton's printed jobs are mechanical support, motility and maintenance of cell shape
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Microtubules are the cytoskeletal element a student can name, and the spindle of a dividing cell is made of microtubules, so the division function printed in another chapter is carried across to the cytoskeleton's own line.
- **Why:** This question requires the function printed against one cell structure, demonstrated by the stem asking 'which of the following functions is carried out by cytoskeleton in a cell' with four functions of four different components as options.
- **Note:** A reviewer should see that option 4 is defensible on a wider reading, since spindle microtubules are cytoskeletal; the key follows the chapter's own cytoskeleton line, which names mechanical support, motility and maintenance of shape, and the tag follows the printed key.
<!--/ecat-->

## Q173

Biology · zoology · Digestion and Absorption

Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by

- **(1)** Ileo-caecal valve
- (2) Gastro-oesophageal sphincter
- (3) Pyloric sphincter
- (4) Sphincter of Oddi

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The ileo-caecal valve guards the opening of the ileum into the caecum and prevents backflow of undigested matter, so the answer is option $1$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q173_fae1eef2_02112026.png?v=fae1eef2bc7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The ileo-caecal valve guards the ileum's opening into the caecum and stops material returning to the small intestine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The gastro-oesophageal sphincter is the one printed as stopping stomach contents returning up the oesophagus, so the stem's word 'backflow' pulls the answer to that junction instead of the ileum–caecum one.
- **Why:** This question requires the name of the valve at one named junction, demonstrated by the stem fixing that junction — 'once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by'.
- **Note:** nearby_fact rather than wrong_site_attacked: the student is naming a different structure from the same printed description, not moving the right structure to another site; and the names carry no resemblance, so look_alike_term does not apply either.
<!--/ecat-->

## Q174

Biology · zoology · Reproductive Health

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Vasectomy | I | Oral method |
| B | Coitus interruptus | II | Barrier method |
| C | Cervical caps | III | Surgical method |
| D | Saheli | IV | Natural method |

- **(1)** A-III, B-IV, C-II, D-I
- (2) A-II, B-III, C-I, D-IV
- (3) A-IV, B-II, C-I, D-III
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Vasectomy (A) is a surgical sterilisation method, so $A \rightarrow III$.
2. Coitus interruptus (B) is a natural method, so $B \rightarrow IV$.
3. Cervical caps (C) are a barrier method, so $C \rightarrow II$.
4. Saheli (D) is a once-a-week oral contraceptive pill, so $D \rightarrow I$.
5. $A$-III, $B$-IV, $C$-II, $D$-I matches option $1$.

**Subtopic:** Artificial Contraceptive Methods, Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q174_07093de7_02112026.png?v=07093de7fd78)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Contraceptives are grouped by how they work: vasectomy is surgical, coitus interruptus natural, cervical caps a barrier, and Saheli an oral pill
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Vasectomy–surgical is the pair held most firmly, and this code carries it, so the option looks confirmed by the one check made; its other three pairs are all wrong, including Saheli as a barrier method when Saheli is the oral pill.
- **Why:** This question requires the printed class of each named contraceptive method, demonstrated by List II being the four method classes themselves — 'Oral method', 'Barrier method', 'Surgical method', 'Natural method' — one for each named practice.
<!--/ecat-->

## Q175

Biology · zoology · Locomotion and Movement

Match List I with List II.
List I (Type of Joint) | List II (Found between)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cartilaginous Joint | I | Between flat skull bones |
| B | Ball and Socket Joint | II | Between adjacent vertebrae in vertebral column |
| C | Fibrous Joint | III | Between carpal and metacarpal of thumb |
| D | Saddle Joint | IV | Between Humerus and Pectoral girdle |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-I, B-IV, C-III, D-II
- (3) A-II, B-IV, C-III, D-I
- (4) A-III, B-I, C-II, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Cartilaginous joint: adjacent vertebrae of the vertebral column are joined by cartilage, so $A \rightarrow II$.
2. Ball and socket joint: between the humerus and the pectoral girdle, so $B \rightarrow IV$.
3. Fibrous joint: sutures between the flat skull bones, so $C \rightarrow I$.
4. Saddle joint: between the carpal and metacarpal of the thumb, so $D \rightarrow III$.
5. $A$-$II$, $B$-$IV$, $C$-$I$, $D$-$III$ matches option $1$.

**Subtopic:** Joints · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q175_a4447671_02112026.png?v=a4447671ab3e)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each joint type has one printed example: fibrous at the skull sutures, cartilaginous between vertebrae, ball and socket at the shoulder, saddle at the base of the thumb
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  This code carries the two pairs a student can check — vertebrae as cartilaginous, humerus and girdle as ball and socket — and then hands the skull to the saddle joint and the thumb to the fibrous joint, which are the two examples printed next to each other in the same list of joint types.
- **Why:** This question requires the site NCERT prints for each type of joint, demonstrated by List II being four printed locations — 'Between flat skull bones', 'Between adjacent vertebrae in vertebral column', 'Between carpal and metacarpal of thumb', 'Between Humerus and Pectoral girdle'.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: 'fibrous' and 'saddle' resemble each other in no way, and replacing them with two unlike words leaves the exchange just as available, because what carries it is which example is printed beside which joint name in the same list.
<!--/ecat-->

## Q176

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) RNA mutates at a faster rate.
- (Statement II) Viruses having RNA genome and shorter life span mutate and evolve faster.

- (1) Both Statement I and Statement II are false.
- (2) Statement I is true but Statement II is false.
- (3) Statement I is false but Statement II is true.
- **(4)** Both Statement I and Statement II are true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: RNA is chemically less stable (reactive 2'-OH) and mutates at a faster rate than DNA, so it is true.
2. Statement II: because RNA mutates fast, viruses with an RNA genome and a short life span mutate and evolve faster, so it is true; both true is option $4$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q176_4652c50c_02112026.png?v=4652c50c8ad5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** RNA is the labile molecule and mutates faster, which is why RNA viruses with short life spans evolve quickly
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all three wrong verdicts against the DNA-versus-RNA passage: the two statements are consecutive printed lines, the second drawn from the first, and no line anywhere in the chapter assigns a faster mutation rate to DNA or detaches short viral life spans from fast evolution, so no wrong verdict has a route out of the source.
- **Why:** This question requires two stated lines about RNA's mutation rate to be checked as printed, demonstrated by Statement II's "RNA genome and shorter life span mutate and evolve faster" following directly from Statement I.
- **Note:** Three fillers was reached by looking rather than by giving up: each wrong verdict was tested for a competing printed fact and none was found, which is why the trap is recorded as no_trap. If a reviewer can name a taught line that puts a faster mutation rate on DNA, option 3 would become the trap.
<!--/ecat-->

## Q177

Biology · zoology · Molecular Basis of Inheritance

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid.
- (Statement II) In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome.

- (1) Both Statement I and Statement II are false.
- (2) Statement I is correct but Statement II is false.
- **(3)** Statement I is incorrect but Statement II is true.
- (4) Both Statement I and Statement II are true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. DNA is negatively charged because of its phosphate groups, so the phrase 'positively charged DNA' in Statement I is wrong; in prokaryotes the DNA is held by positively charged proteins in the nucleoid. Statement I is incorrect.
2. In eukaryotes, the negatively charged DNA wraps around a positively charged histone octamer to form the nucleosome. Statement II is true.
3. Statement I incorrect and Statement II true is option $3$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q177_734a09d9_02112026.png?v=734a09d9dacb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA is the negatively charged partner and the histones are the positively charged ones, in the prokaryotic nucleoid as much as in the eukaryotic nucleosome
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Statement I is the printed nucleoid sentence with the two charges exchanged — the DNA called positive and the proteins negative — and a student who recognises the sentence shape accepts it, then finds Statement II correct and marks both true.
- **Why:** This question requires the stated charges on DNA and on its associated proteins, demonstrated by Statement I's "positively charged DNA … with some negatively charged proteins" against Statement II's opposite assignment.
<!--/ecat-->

## Q178

Biology · zoology · Principles of Inheritance and Variation

Which one of the following symbols represents mating between relatives in human pedigree analysis?

- **(1)** ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q178_option_1_70a7f5db_02112026.png?v=70a7f5db6b96)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q178_option_2_373e706e_02112026.png?v=373e706eddcb)
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q178_option_3_33f15e87_02112026.png?v=33f15e873c79)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/figures_agent/q178_option_4_364c7fcf_02112026.png?v=364c7fcf46a3)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the NCERT pedigree symbols, a square joined to a circle by a double horizontal line means consanguineous mating (mating between relatives); option $1$ shows this double line, while option $4$ has a single line (ordinary mating), option $2$ shows parents with an affected son, and option $3$ shows affected individuals.

**Subtopic:** Pedigree Analysis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q178_6bffad5e_02112026.png?v=6bffad5e5850)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** In a pedigree, a mating between relatives is drawn as a double horizontal line joining the two parents
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four option slots are empty in this record: the options are drawn pedigree symbols and no image for them was supplied to this step, so which symbol each option shows cannot be read and no route to a wrong option can be named or audited.
- **Why:** This question requires one drawn symbol of a printed notation to be recognised, demonstrated by the stem asking 'which one of the following symbols represents mating between relatives in human pedigree analysis'.
- **Note:** The four options are empty strings in this record, so an option is missing and no trap is written. A reviewer holding the printed symbols should check the mechanism I would expect but cannot confirm: the consanguineous mating symbol is a DOUBLE horizontal line between two parents, and the single horizontal line that marks an ordinary mating would be the look-alike offered against it; the vertical line of descent to offspring and the diagonal slash for a deceased individual are the other symbols from the same printed key. A repair task is needed to re-extract the four option images. Separately, the current qtype list has no value for a question whose four options are drawings — the retired vocabulary carried structure_options for that — so mcq is recorded with this gap noted rather than stretching a label.
<!--/ecat-->

## Q179

Biology · zoology · Evolution

Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.

- **(1)** Numbat, Spotted cuscus, Flying phalanger
- (2) Mole, Flying squirrel, Tasmanian tiger cat
- (3) Lemur, Anteater, Wolf
- (4) Tasmanian wolf, Bobcat, Marsupial mole

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Numbat, spotted cuscus and flying phalanger are all Australian marsupials from the adaptive radiation; options 2, 3 and 4 each include placental mammals (mole, flying squirrel, lemur, anteater, wolf, bobcat), so the answer is option $1$.

**Subtopic:** What is Adaptive Radiation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q179_3892859e_02112026.png?v=3892859e0ce7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Adaptive radiation in Australian marsupials: every animal on that plate is a marsupial, and the placental look-alikes beside it belong to the convergent-evolution comparison
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Tasmanian wolf and marsupial mole both sit on NCERT's Australian marsupial plate, so an option opening with two of those names reads as the marsupial set, and the bobcat placed third is a placental cat that voids the whole set.
- **Why:** This question requires the stated membership of the Australian marsupial radiation, demonstrated by the stem asking for the correct "group/set" and each option bundling three animal names that stand or fall together.
- **Note:** The options are sets of three names accepted or rejected whole, which the retired E1 vocabulary would call pair_options; the current qtype list offers no bundled-set value, so it is recorded as mcq.
<!--/ecat-->

## Q180

Biology · zoology · Biotechnology: Principles and Processes

Which of the following is not a cloning vector?

- (1) YAC
- (2) pBR322
- **(3)** Probe
- (4) BAC

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. YAC, pBR322 and BAC are vectors used to carry foreign DNA, while a probe is a labelled DNA/RNA used for detection, so the answer is option $3$.

**Subtopic:** Cloning Vectors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q180_74c912fe_02112026.png?v=74c912fed8b1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cloning vectors carry foreign DNA into a host — plasmids, BAC and YAC; a probe is a labelled sequence used to find DNA, not to carry it
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  pBR322 is the vector NCERT names first and draws in full, so reading the stem as 'which is a cloning vector' lands on it; the claim is true of pBR322 and the stem asked for the item that is not one.
- **Why:** This question requires the stated list of cloning vectors, demonstrated by three options being named vectors (YAC, pBR322, BAC) and the fourth being "Probe", with no criterion printed to apply.
<!--/ecat-->

## Q181

Biology · zoology · Human Health and Disease

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Heroin | I | Effect on cardiovascular system |
| B | Marijuana | II | Slow down body function |
| C | Cocaine | III | Painkiller |
| D | Morphine | IV | Interfere with transport of dopamine |

- (1) A-I, B-II, C-III, D-IV
- (2) A-IV, B-III, C-II, D-I
- (3) A-III, B-IV, C-I, D-II
- **(4)** A-II, B-I, C-IV, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Heroin (smack) is a depressant and slows down body functions: $A \rightarrow II$.
2. Cannabinoids such as marijuana mainly affect the cardiovascular system: $B \rightarrow I$.
3. Cocaine interferes with the transport of the neurotransmitter dopamine: $C \rightarrow IV$.
4. Morphine is a very effective sedative and painkiller: $D \rightarrow III$.
5. The match $A-II, B-I, C-IV, D-III$ is option $4$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q181_b354133c_02112026.png?v=b354133c619d)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each drug group has one effect printed against it: heroin depresses body functions, cannabinoids act on the cardiovascular system, cocaine blocks dopamine transport, morphine kills pain
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Heroin and morphine are the two opioids printed in the same paragraph, so their lines change hands — heroin takes 'Painkiller' and morphine takes 'Slow down body function' — and cocaine takes the cardiovascular line that belongs to the cannabinoids.
- **Why:** This question requires the effect NCERT attributes to each named drug, demonstrated by List II being four printed effects, including 'Interfere with transport of dopamine' and 'Painkiller'.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: 'heroin' and 'morphine' do not resemble each other as words, and swapping them for two unlike names leaves the exchange intact, because what carries it is their adjacency in the same printed paragraph.
<!--/ecat-->

## Q182

Biology · zoology · Biotechnology and Its Applications

Which one of the following techniques does not serve the purpose of early diagnosis of a disease for its early treatment?

- **(1)** Serum and Urine analysis
- (2) Polymerase Chain Reaction (PCR) technique
- (3) Enzyme Linked Immuno-Sorbent Assay (ELISA) technique
- (4) Recombinant DNA Technology

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Conventional methods of diagnosis (serum and urine analysis) detect a pathogen only after symptoms appear, when its concentration is already high, so they do not give early detection; Recombinant DNA technology, PCR and ELISA do give early diagnosis, so the answer is option $1$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q182_750082e3_02112026.png?v=750082e344f7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Early diagnosis rests on recombinant DNA technology, PCR and ELISA; conventional serum and urine analysis detects a disease only after symptoms appear
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Recombinant DNA technology is taught in the same chapter as human insulin and Bt cotton, so its remembered role is making a product rather than spotting a disease, and a student scanning for the technique that is not diagnostic stops there.
- **Why:** This question requires the stated distinction between conventional and molecular diagnosis, demonstrated by the stem's "does not serve the purpose of early diagnosis" set against the option "Serum and Urine analysis".
<!--/ecat-->

## Q183

Biology · zoology · Human Reproduction

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Endometrium is necessary for implantation of blastocyst.
- (Reason R) In the absence of fertilization, the corpus luteum degenerates that causes disintegration of endometrium.

- **(1)** Both A and R are true but R is NOT the correct explanation of A.
- (2) A is true but R is false.
- (3) A is false but R is true.
- (4) Both A and R are true and R is the correct expiation of A.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Assertion A is true: the blastocyst becomes embedded in the endometrium of the uterus (implantation), so the endometrium is necessary.
2. Reason R is true: without fertilization the corpus luteum degenerates, progesterone falls and the endometrium disintegrates (menstruation).
3. R describes what happens to the endometrium without fertilization; it does not explain why the endometrium is required for implantation, so R is not the correct explanation of A: option $1$.

**Subtopic:** Implantation and Embryonic Development, Menstrual Cycle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q183_4f049252_02112026.png?v=4f0492526634)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The endometrium is the tissue the blastocyst embeds in; its monthly breakdown when the corpus luteum degenerates is a separate event from the role it plays at implantation
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Both statements are true and both are about the endometrium, so a student lets the shared topic stand in for an explanatory link and reads R's loss of the endometrium as showing why the endometrium is needed
- **Why:** This question requires deciding whether one true statement accounts for another, demonstrated by R describing what happens 'In the absence of fertilization' while A states what implantation of a blastocyst needs.
- **Note:** Option 4 as extracted reads 'the correct expiation of A', a typo for 'explanation'; the verdict it carries is unambiguous in the four-option format and the question is tagged as printed.
<!--/ecat-->

## Q184

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Gene ‘a’ | I | $\beta$-galactosidase |
| B | Gene ‘y’ | II | Transacetylase |
| C | Gene ‘i’ | III | Permease |
| D | Gene ‘z’ | IV | Repressor protein |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-III, B-IV, C-I, D-II
- (3) A-III, B-I, C-IV, D-II
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the lac operon, gene $a$ codes for transacetylase, so A-II; gene $y$ codes for permease, so B-III; gene $i$ codes for the repressor protein, so C-IV; gene $z$ codes for $\beta$-galactosidase, so D-I. This is option $1$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q184_248e5770_02112026.png?v=248e577077af)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the lac operon $i$ codes the repressor and the structural genes run $z$, $y$, $a$ for β-galactosidase, permease and transacetylase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  This code and the key differ in one thing only — which of the two adjacent structural genes owns β-galactosidase — and it gives β-galactosidase to $y$ and permease to $z$, taking each gene's product from its neighbour.
- **Why:** This question requires which protein each lac operon gene codes for, demonstrated by List I being the bare gene letters 'a', 'y', 'i', 'z' against List II's four gene products, 'β-galactosidase', 'Transacetylase', 'Permease', 'Repressor protein'.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: the letters $y$ and $z$ carry no resemblance to trade on, and replacing them with unlike names leaves the exchange available, so position — which product is printed beside which gene — is doing the work.
<!--/ecat-->

## Q185

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) Nephrons are of two types: Cortical & Juxta medullary, based on their relative position in cortex and medulla.
- (Reason R) Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle.

- (1) Both A and R are true but R is NOT the correct explanation of A.
- **(2)** A is true but R is false.
- (3) A is false but R is true.
- (4) Both A and R are true and R is the correct explanation of A.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A: nephrons are classed as cortical or juxtamedullary by their position in cortex and medulla, so $A$ is true.
2. Reason R: cortical nephrons have a short loop of Henle reaching only a little into the medulla, while juxtamedullary nephrons have a very long loop running deep into the medulla; R reverses this, so $R$ is false.
3. $A$ true, $R$ false gives option $2$.

**Subtopic:** Human Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q185_a8c29a6e_02112026.png?v=a8c29a6e11ca)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cortical nephrons have short loops of Henle that barely enter the medulla; juxtamedullary nephrons have the long loops that run deep into it
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  R prints a contrast that genuinely exists — one nephron type has a short loop and the other a long one — with the two types exchanged, and a student who recognises the contrast without rechecking its direction grants R and takes it as the explanation of A
- **Why:** This question requires which nephron type carries the long loop of Henle, demonstrated by R printing 'Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle'.
<!--/ecat-->

## Q186

Biology · zoology · Structural Organisation in Animals

Which of the following is characteristic feature of cockroach regarding sexual dimorphism?

- **(1)** Presence of anal styles
- (2) Presence of sclerites
- (3) Presence of anal cerci
- (4) Dark brown body colour and anal cerci

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In cockroach, anal cerci, sclerites and the dark brown body colour are found in both sexes, whereas a pair of short, thread-like anal styles is present only in males, so anal styles show sexual dimorphism: option $1$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q186_0cd226b2_02112026.png?v=0cd226b2a4ee)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sexual dimorphism in the cockroach: anal styles occur only in the male, while anal cerci occur in both sexes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The anal cerci are described in the sentence beside the anal styles and both are paired appendages at the hind end, so a student reaching for 'the appendage at the tip of the cockroach abdomen' takes the one that sits next to the right answer.
- **Why:** This question requires the stated male-only structure of the cockroach, demonstrated by the stem's "regarding sexual dimorphism" set against options that each name a real cockroach structure.
- **Note:** Swap test applied between anal styles and anal cerci: replacing 'cerci' with an unlike structure name keeps the trap alive, because what carries the student is the two appendages being described side by side at the hind end, so nearby_fact rather than look_alike_term — the shared word 'anal' adds to it but is not doing the work.
<!--/ecat-->

## Q187

Biology · zoology · Cell Cycle and Cell Division

Select the correct statements.
Choose the correct answer from the options given below:

- (A) Tetrad formation is seen during Leptotene.
- (B) During Anaphase, the centromeres split and chromatids separate.
- (C) Terminalization takes place during Pachytene.
- (D) Nucleolus, Golgi complex and ER are reformed during Telophase.
- (E) Crossing over takes place between sister chromatids of homologous chromosome.

- **(1)** B and D only
- (2) A, C and E only
- (3) B and E only
- (4) A and C only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A: tetrads are seen in pachytene after synapsis in zygotene, not leptotene, so A is false.
2. B: in (mitotic) anaphase the centromeres split and sister chromatids separate, so B is true.
3. C: terminalisation of chiasmata occurs in diakinesis, not pachytene, so C is false.
4. D: in telophase the nucleolus, Golgi complex and ER reform, so D is true.
5. E: crossing over occurs between non-sister chromatids of homologous chromosomes, so E is false.
6. True statements are B and D only, which is option $1$.

**Subtopic:** Phases of Cell Cycle, Prophase I and Its Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 46)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q187_a6b3521a_02112026.png?v=a6b3521a346f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Crossing over occurs between non-sister chromatids of homologous chromosomes, tetrads become visible in pachytene and terminalisation comes at diakinesis
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  B is certainly right, and E is accepted because "sister chromatids" is taken for "non-sister chromatids" — the two names differ only by the prefix, and the rest of the sentence is the printed one.
- **Why:** This question requires the stated placing of division events, demonstrated by statement E's "between sister chromatids of homologous chromosome" and statement A's "Tetrad formation is seen during Leptotene".
- **Note:** Swap test applied on the trap: replace sister and non-sister with two unlike words and the pull disappears, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q188

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements are correct? Choose the correct answer from the options given below:

- (A) An excessive loss of body fluid from the body switches off osmoreceptors.
- (B) ADH facilitates water reabsorption to prevent diuresis.
- (C) ANF causes vasodilation.
- (D) ADH causes increase in blood pressure.
- (E) ADH is responsible for decrease in GFR.

- **(1)** B, C and D only
- (2) A, B and E only
- (3) C, D and E only
- (4) A and B only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A: excessive loss of body fluid activates osmoreceptors, which trigger ADH release, so A is false.
2. B: ADH facilitates water reabsorption in the distal tubule and collecting duct, preventing diuresis, so B is true.
3. C: ANF causes vasodilation and lowers blood pressure, so C is true.
4. D: ADH constricts blood vessels, raising blood pressure, so D is true.
5. E: by raising blood pressure, ADH can increase glomerular blood flow and GFR, not decrease it, so E is false.
6. True set $= \{B, C, D\}$, which is option $1$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 46)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q188_5e3106a7_02112026.png?v=5e3106a7c423)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fluid loss activates the osmoreceptors and ADH release; ADH reabsorbs water and raises blood pressure, and the higher glomerular blood flow raises GFR
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Both false statements here are printed lines turned round, and both read as water conservation: a fall in body fluid is taken to switch the osmoreceptors off, and ADH is taken to cut filtration, so with B true the set of three looks consistent.
- **Why:** This question requires the stated direction of each kidney-regulation effect, demonstrated by statement A's "switches off osmoreceptors" and statement E's "decrease in GFR".
<!--/ecat-->

## Q189

Biology · zoology · Cell Cycle and Cell Division

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) During $\mathrm{G_0}$ phase of cell cycle, the cell is metabolically inactive.
- (Statement II) The centrosome undergoes duplication during S phase of interphase.

- (1) Both Statement I and Statement II are incorrect.
- (2) Statement I is correct but Statement II is incorrect.
- **(3)** Statement I is incorrect but Statement II is correct.
- (4) Both Statement I and Statement II are correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cells in the $\mathrm{G_0}$ (quiescent) phase remain metabolically active but no longer proliferate, so Statement I is incorrect.
2. During S phase of interphase the centriole (centrosome) duplicates in the cytoplasm, so Statement II is correct.
3. Statement I incorrect and Statement II correct is option $3$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 46)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q189_1fadbf0c_02112026.png?v=1fadbf0c7e19)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A cell in G0 stops dividing but stays metabolically active, and the centrosome duplicates in S phase along with the DNA
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The fact printed beside the one asked for is that G0 cells no longer proliferate, and a student who carries that takes the next step to "inactive", so Statement I passes and, Statement II being right, both come out correct.
- **Why:** This question requires two stated facts about the cell cycle to be checked as printed, demonstrated by Statement I's "the cell is metabolically inactive" and Statement II's placing of centrosome duplication in "S phase of interphase".
- **Note:** Swap test applied on this trap: the pull is not a resemblance between words but the neighbouring property printed in the same sentence — not proliferating taken for not metabolising — so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q190

Biology · zoology · Strategies for Enhancement in Food Production

Which one of the following is NOT an advantage of inbreeding?

- (1) It exposes harmful recessive genes but are eliminated by selection.
- (2) Elimination of less desirable genes and accumulation of superior genes takes place due to it.
- **(3)** It decreases the productivity of inbred population, after continuous inbreeding.
- (4) It decreases homozygosity.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Inbreeding is mating of closely related individuals for $4$-$6$ generations, so it $\textit{increases}$ homozygosity.
2. Exposing harmful recessive genes so selection removes them (option $1$) is an advantage.
3. Eliminating less desirable genes and accumulating superior genes (option $2$) is an advantage.
4. Continued inbreeding reduces fertility and productivity, i.e. inbreeding depression (option $3$), which is a disadvantage.
5. Option $4$ is factually false (inbreeding increases homozygosity), so it is also not an advantage; the intended disadvantage is option $3$.

**Subtopic:** Animal Breeding · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 46)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q190_8b86f092_02112026.png?v=8b86f092bce6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inbreeding increases homozygosity: it exposes and removes harmful recessives and fixes superior genes, but continued inbreeding brings inbreeding depression
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Inbreeding raises homozygosity, so the printed claim that it decreases homozygosity is the relation turned round, and a student reading the task as 'find the false statement' stops here instead of at the statement that is true but a cost.
- **Why:** This question requires the stated advantages and the stated cost of inbreeding, demonstrated by the stem's "NOT an advantage" set against the option "It decreases the productivity of inbred population, after continuous inbreeding".
- **Note:** Key doubt recorded, not re-judged: option 4 is also not an advantage, since inbreeding increases homozygosity and so the claim is simply untrue, which makes two options answer the stem on a reasonable reading. The printed key is (3) and the tags follow it.
<!--/ecat-->

## Q191

Biology · zoology · Organisms and Populations

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Logistic growth | I | Unlimited resource availability condition |
| B | Exponential growth | II | Limited resource availability condition |
| C | Expanding age pyramid | III | The percent individuals of pre-reproductive age is largest followed by reproductive and post reproductive age groups |
| D | Stable age pyramid | IV | The percent individuals of pre-reproductives and reproductive age group are same |

- (1) A-II, B-III, C-I, D-IV
- (2) A-II, B-IV, C-I, D-III
- (3) A-II, B-IV, C-III, D-I
- **(4)** A-II, B-I, C-III, D-IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Logistic growth: resources are limited, so $A \to II$.
2. Exponential growth: resources are unlimited, so $B \to I$.
3. Expanding age pyramid: pre-reproductive individuals are largest, then reproductive, then post-reproductive, so $C \to III$.
4. Stable age pyramid: pre-reproductive and reproductive groups are about equal, so $D \to IV$.
5. $A\text{-}II, B\text{-}I, C\text{-}III, D\text{-}IV$ is option $4$.

**Subtopic:** Life History Variation and Population Attributes, Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q191_b87a6a29_02112026.png?v=b87a6a293b1c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Resources define the growth form — unlimited gives exponential, limited gives logistic — while the age pyramid's name is set by the size of its pre-reproductive group
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Exponential' and 'expanding' both say growing, so their partners change hands: the expanding pyramid takes the unlimited-resource condition and exponential growth is left with the young-heavy age structure.
- **Why:** This question requires the condition or age-structure description printed against each named growth form, demonstrated by List II setting 'Unlimited resource availability condition' against 'Limited resource availability condition' for the two growth types.
- **Note:** look_alike_term rather than nearby_fact, by the swap test: 'Exponential growth' and 'Expanding age pyramid' resemble each other in the one word that matters, and replacing them with two unlike words kills the exchange, so the likeness rather than position is carrying it. Also recorded: A-II is present in all four options, so the logistic–limited pair cannot discriminate between them and the question turns entirely on rows B, C and D.
<!--/ecat-->

## Q192

Biology · zoology · Chemical Coordination and Integration

Which of the following are NOT under the control of thyroid hormone? Choose the correct answer from the options given below:

- (A) Maintenance of water and electrolyte balance
- (B) Regulation of basal metabolic rate
- (C) Normal rhythm of sleep-wake cycle
- (D) Development of immune system
- (E) Support the process of RBCs formation

- (1) B and C only
- **(2)** C and D only
- (3) D and E only
- (4) A and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Per NCERT, thyroid hormones regulate $\text{BMR}$ (B), support the process of RBC formation (E) and maintain water and electrolyte balance (A).
2. Normal rhythm of the sleep-wake cycle (C) is regulated by melatonin from the pineal gland, not thyroid hormone.
3. Development of the immune system (D) is promoted by thymosins from the thymus, not thyroid hormone.
4. So the items NOT under thyroid control are C and D, which is option $2$.

**Subtopic:** Thyroid Gland and Parathyroid Gland · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q192_7c448a87_02112026.png?v=7c448a872e54)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thyroid hormones regulate basal metabolic rate, support red blood cell formation and influence water and electrolyte balance; sleep rhythm is the pineal's and immune development the thymus's
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Water and electrolyte balance is printed under ADH and aldosterone, so a student who has it filed there reads it as outside thyroid control and pairs it with the immune statement, which really is outside.
- **Why:** This question requires the stated list of thyroid functions, demonstrated by the stem's "NOT under the control of thyroid hormone" against statement A's "Maintenance of water and electrolyte balance".
- **Note:** Swap test applied: water and electrolyte balance and sleep-wake rhythm are not alike as phrases, and the pull survives any rewording because it comes from where the function is printed — under the other hormones — so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q193

Biology · zoology · Animal Kingdom

The unique mammalian characteristics are:

- **(1)** hairs, pinna and mammary glands
- (2) hairs, pinna and indirect development
- (3) pinna, monocondylic skull and mammary glands
- (4) hairs, tympanic membrane and mammary glands

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT: the most unique mammalian characteristics are mammary glands, hair on the skin and external ears (pinnae), so option $1$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q193_568cb660_02112026.png?v=568cb6603503)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The features unique to Mammalia are hair, external pinnae and mammary glands; a tympanum, a condylar count and a development mode are shared with other classes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Hair and mammary glands are the two features carried for Mammalia, so an option holding both reads as correct, and the tympanic membrane placed between them is a real mammalian structure that is not unique to mammals.
- **Why:** This question requires the stated diagnostic features of Mammalia, demonstrated by the stem's "unique mammalian characteristics" and by each option bundling three features that are accepted together.
- **Note:** Option 3 carries the monocondylic / dicondylic likeness, which would be look_alike_term if it were the question's one trap; option 4 is the stronger route because two of its three items are correct and the failing item is a true mammalian structure, so the question's single trap is recorded as half_right.
<!--/ecat-->

## Q194

Biology · zoology · Locomotion and Movement

Which of the following statements are correct regarding skeletal muscle? Choose the most appropriate answer from the options given below:

- (A) Muscle bundles are held together by collagenous connective tissue layer called fascicle.
- (B) Sarcoplasmic reticulum of muscle fibre is a store house of calcium ions.
- (C) Striated appearance of skeletal muscle fibre is due to distribution pattern of actin and myosin proteins.
- (D) M line is considered as functional unit of contraction called sarcomere.

- **(1)** B and C only
- (2) A, C and D only
- (3) C and D only
- (4) A, B and C only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement A: muscle bundles (fascicles) are held together by a collagenous connective tissue layer called fascia, not fascicle, so $A$ is false.
2. Statement B: the sarcoplasmic reticulum stores $\mathrm{Ca^{2+}}$ ions, so $B$ is true.
3. Statement C: the striations come from the distribution pattern of actin and myosin, so $C$ is true.
4. Statement D: the sarcomere is the part of the myofibril between two successive Z lines, not the M line, so $D$ is false.
5. Correct set is $\{B, C\}$, which is option $1$.

**Subtopic:** Structure of Skeletal Muscle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q194_c0ecf5a0_02112026.png?v=c0ecf5a045b8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Muscle fascicles are held together by a collagenous layer called fascia, and the sarcomere is the stretch of myofibril between two successive Z lines
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  B and C are both correct, so the option looks like the right set with one more fact, and A is accepted because fascia and fascicle differ by two letters — the statement names the bundle's wrapping with the bundle's own name.
- **Why:** This question requires the stated vocabulary of skeletal muscle structure, demonstrated by statement A's "collagenous connective tissue layer called fascicle" and statement D's "M line is considered as functional unit of contraction".
- **Note:** Swap test applied: replace fascia and fascicle with two unlike words and the trap dies, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q195

Biology · zoology · Body Fluids and Circulation

Which of the following statements are correct? Choose the correct answer from the options given below:

- (A) Basophils are most abundant cells of the total WBCs
- (B) Basophils secrete histamine, serotonin and heparin
- (C) Basophils are involved in inflammatory response
- (D) Basophils have kidney shaped nucleus
- (E) Basophils are agranulocytes

- (1) C and E only
- **(2)** B and C only
- (3) A and B only
- (4) D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A is false: neutrophils are the most abundant WBCs ($60$-$65\%$); basophils are the least ($0.5$-$1\%$).
2. B is true: basophils secrete histamine, serotonin and heparin.
3. C is true: basophils are involved in inflammatory reactions.
4. D is false: a kidney-shaped nucleus is a feature of monocytes, not basophils.
5. E is false: basophils are granulocytes, not agranulocytes.
6. Only B and C are correct, which is option $2$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 48)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q195_7c4154f8_02112026.png?v=7c4154f8f567)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Basophils are the rarest granulocytes and secrete histamine, serotonin and heparin in the inflammatory response; the most abundant WBC is the neutrophil
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  B is certainly right, and A is accepted because the abundance line printed in the same list of white cells belongs to the neutrophil — the sentence is that line with the cell name changed.
- **Why:** This question requires the stated properties of one named white cell, demonstrated by statement A's "most abundant cells of the total WBCs" and statement E's "Basophils are agranulocytes".
- **Note:** Swap test applied: the statements all name the basophil, so no name is being confused with a look-alike — what carries the student is the abundance figure printed beside it for another white cell in the same list, so nearby_fact.
<!--/ecat-->

## Q196

Biology · zoology · Molecular Basis of Inheritance

Which one of the following is the sequence on corresponding coding strand, if the sequence on mRNA formed is as follows 5’AUCGAUCGAUCGAUCGAUCGAUCG AUCG 3’?

- (1) 3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’
- **(2)** 5’ ATCGATCGATCGATCGATCGATCGATCG 3’
- (3) 3’ ATCGATCGATCGATCGATCGATCGATCG 5’
- (4) 5’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 3’

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The coding strand has the same sequence and the same $5' \rightarrow 3'$ polarity as the mRNA, except that DNA has $T$ where RNA has $U$.
2. Replacing $U$ with $T$ in $5'\,AUCG\ldots AUCG\,3'$ gives $5'\,ATCG\ldots ATCG\,3'$, which is option $2$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q196_d6de3127_02112026.png?v=d6de31277a7b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The coding strand carries the same base order and the same 5'→3' polarity as the mRNA with T in place of U; the complement of the mRNA is the template strand
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The base string is built correctly — ATCGATCG… for AUCGAUCG… — and then the ends are labelled 3' to 5' because the DNA strand is remembered as running antiparallel to the RNA, which is true of the template and not of the coding strand.
- **Why:** This question requires the base-pairing and polarity convention applied to a supplied sequence, demonstrated by the stem giving the mRNA as "5'AUCGAUCG…3'" and asking for "the sequence on corresponding coding strand".
- **Note:** E1's pattern classifier returned arrange_in_order on '6 arrange/sequence'; nothing here is to be put in order — the options are four nucleotide strings differing in bases and in end labels — so the printed shape is recorded as mcq.
<!--/ecat-->

## Q197

Biology · zoology · Neural Control and Coordination

The parts of human brain that helps in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:

- (1) Corpora quadrigemina and hippocampus
- (2) Brain stem and epithalamus
- (3) Corpus callosum and thalamus
- **(4)** Limbic system and hypothalamus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT states that the inner parts of the cerebral hemispheres and associated deep structures (amygdala, hippocampus) form the limbic system, which along with the hypothalamus regulates sexual behaviour and emotional expression (excitement, pleasure, rage, fear), so the answer is option $4$.

**Subtopic:** Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q197_d6020d64_02112026.png?v=d6020d64c142)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The limbic system together with the hypothalamus governs sexual behaviour and the expression of emotions such as excitement, pleasure, rage and fear
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The hippocampus is named as one of the deep structures making up the limbic system, so an option carrying it looks like the emotion answer; the corpora quadrigemina paired with it are midbrain lobes for visual and auditory reflexes, and the option is accepted only if both parts hold.
- **Why:** This question requires the stated functions of two named forebrain regions, demonstrated by the stem listing "regulation of sexual behaviour, expression of excitement, pleasure, rage, fear" against options that pair brain parts.
- **Note:** E1's pattern classifier returned statement_options on '15 full-statement options'; the options are two-item name pairs, not standalone claims to be judged, so the shape is recorded as mcq.
<!--/ecat-->

## Q198

Biology · zoology · Structural Organisation in Animals

Match List I with List II. Choose the correct answer from the options give below:

| List-I | | List-II | |
|---|---|---|---|
| A | Mast cells | I | Ciliated epithelium |
| B | Inner surface Of bronchiole | II | Areolar connective tissue |
| C | Blood | III | Cuboidal epithelium |
| D | Tubular parts of nephron | IV | Specialised connective tissue |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-III, B-IV, C-II, D-I
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Mast cells are a cell type found in areolar connective tissue, so $A \to II$.
2. The inner surface of bronchioles is lined by ciliated epithelium, so $B \to I$.
3. Blood is a specialised (fluid) connective tissue, so $C \to IV$.
4. The tubular parts of the nephron are lined by cuboidal epithelium, so $D \to III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $2$.

**Subtopic:** Connective Tissue, Animal Tissues: Epithelial Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q198_b430f745_02112026.png?v=b430f745bacf)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each site has its own tissue: mast cells live in areolar tissue, a bronchiole is lined by ciliated epithelium, blood is a specialised connective tissue, and the nephron's tubules are cuboidal epithelium
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Areolar tissue is printed as the support framework lying beneath an epithelium, including in the wall of a bronchiole, so this code gives the bronchiole its areolar tissue and leaves the ciliated epithelium on the mast-cell row.
- **Why:** This question requires the tissue NCERT names for each site or cell type, demonstrated by List I mixing one cell type and three locations — 'Mast cells', 'Inner surface Of bronchiole', 'Blood', 'Tubular parts of nephron' — against List II's four tissue names.
- **Note:** nearby_fact rather than look_alike_term, by the swap test: 'Areolar connective tissue' and 'Ciliated epithelium' resemble each other in no way, and what carries the exchange is that areolar tissue is printed as the framework lying beside an epithelium.
<!--/ecat-->

## Q199

Biology · zoology · Structural Organisation in Animals

In cockroach, excretion is brought about by-

- (A) Phallic gland
- (B) Uricose gland
- (C) Nephrocytes
- (D) Fat body
- (E) Collaterial glands

- (1) A, B and E only
- **(2)** B, C and D only
- (3) B and D only
- (4) A and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In cockroach, excretion is by Malpighian tubules, aided by the fat body, nephrocytes and uricose glands (NCERT Class 11).
2. Phallic gland (A) is a male accessory reproductive gland and collaterial glands (E) are female accessory reproductive glands, so neither is excretory.
3. Excretory structures listed are $B$, $C$ and $D$, which is option $2$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 49)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q199_8408aa9c_02112026.png?v=8408aa9cd9b4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Besides the Malpighian tubules, excretion in the cockroach is helped by the uricose glands, the nephrocytes and the fat body; the phallic and collaterial glands are reproductive
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The uricose glands and the fat body are both genuine excretory helpers, so the pair is true as far as it goes and the nephrocytes — the third helper in the printed line — are left out.
- **Why:** This question requires the stated excretory structures of the cockroach, demonstrated by the option "B and D only" omitting the nephrocytes that the printed line names with them.
- **Note:** half_right is used here in its second sense — a true but incomplete set — which is a finding about this option and not the generic fact that combination options are part-correct: both items in it are true and exactly one true item is missing.
<!--/ecat-->

## Q200

Biology · zoology · Animal Kingdom

Select the correct statements with reference to chordates. Choose the correct answer from the options given below:

- (A) Presence of a mid-dorsal, solid and double nerve cord.
- (B) Presence of closed circulatory system.
- (C) Presence of paired pharyngeal gill slits.
- (D) Presence of dorsal heart
- (E) Triploblastic pseudocoelomate animals.

- **(1)** B and C only
- (2) B, D and E only
- (3) C, D and E only
- (4) A, C and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A is false: the chordate nerve cord is dorsal, hollow and single, not solid and double.
2. B is true: chordates have a closed circulatory system.
3. C is true: chordates have paired pharyngeal gill slits.
4. D is false: the chordate heart is ventral.
5. E is false: chordates are triploblastic coelomates, not pseudocoelomates.
6. Only B and C are correct, which is option $1$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 49)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2023/2023_F1/crops/q200_072bc9a0_02112026.png?v=072bc9a00d2f)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chordates have a dorsal, hollow, single nerve cord, paired pharyngeal gill slits, a ventral heart, a closed circulation and a true coelom; the solid double nerve cord and the dorsal heart belong to the non-chordates
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The gill slits in C are the chordate character the chapter states most plainly, and the other two items are imported from what is printed beside: the dorsal heart from the non-chordate column of the comparison, and the pseudocoelom from the body cavity of the phyla taught just before Chordata.
- **Why:** This question requires the stated chordate characters, demonstrated by statement A's "solid and double nerve cord" and statement D's "Presence of dorsal heart" being the non-chordate entries of the same comparison.
- **Note:** reversed was considered, since a dorsal heart is the inversion of a ventral one, and ruled out because one label has to cover the whole option: statement E's pseudocoelom is not an inversion of anything but the body-cavity term of the phyla printed just before Chordata, so what the option is built on throughout is importing from what sits beside the right fact. Swap test agrees — none of the wrong items resembles the right one as a word.
<!--/ecat-->

