# Drawing our own figures — organic, and the physics equivalent

**Status:** the organic half exists and is proven (the Chemistry Renderer package, v4.1, 21 Oct 2026,
127 Haloalkanes cards — 118 identical to NCERT, 9 nearly, 0 different). The physics half is a
working pilot in this repo: `scripts/render_figure.py`, four figures in `figures/`, and a geometry
checker that has already caught two of my own errors. This document says how the organic renderer
joins this pipeline, and what the physics equivalent has to be.

**The package is not on this machine.** It was shared as a zip and never landed here, so everything
below about the chemistry side is read off the team guide, not off the code. Step 0 of any work is
to get the zip and run `tests/test_golden.py`.

---

## 1. Why this is the right architecture, in one line

> The AI never draws. It writes a card, code checks the card, and the renderer draws it.

That split is what makes a generated figure trustworthy, and the guide states the reason better than
any argument for it: **a wrong atom in a SMILES still draws a valid-looking picture, so nobody
notices.** The same is true of physics. A velocity vector drawn at 40.7° under a label reading 60°
looks entirely authoritative — I drew exactly that in the first pass of this pilot, and only a
script comparing the label against the coordinates caught it.

So a figure is a RECORD, not a picture, exactly as a quoted NCERT line is a record. The judgement
(what does this drawing show?) belongs to an agent. The drawing is mechanical and belongs to a
renderer that makes no judgements. And between them sits a check that is **not** the same kind of
thing as the generator — which is the part most pipelines skip.

---

## 2. Organic: joining the Chemistry Renderer to this pipeline

### 2.1 What it replaces

`2016_X q005` is a reaction scheme — `(CH3)2CHBr + KOH → (CH3)2CHOH + KBr`, and cyclohexene + Br2 —
and our copy of it is a watermarked photocopy with a pink wash across two thirds of it. There are
more: every organic question with a mechanism or a scheme currently shows a crop of a reprint.

A reaction card replaces it exactly, and the guide's own example is the shape:

```json
{"id": "C06", "title": "Halogenation of chlorobenzene",
 "rows": [[{"mol": "[Cl:1]c1ccccc1", "orient": {"atom": 1, "deg": 90}},
           {"plus": true}, {"ce": "Cl2", "plain": true},
           {"arrow": {"dir": "right", "above": "Anhyd. FeCl3", "len": 4.4}},
           {"mol": "[Cl:1]c1ccc(Cl)cc1", "name": "1, 4-Dichlorobenzene", "tag": "Major",
            "check": {"name": "1,4-dichlorobenzene", "smiles": "Clc1ccc(Cl)cc1"}}]]}
```

### 2.2 Where it plugs in

A new step, **FIGC** (figure, chemistry), scoped the way every other step here is scoped — by the
CONFIRMED subject and, for chemistry, by QCHAP's branch:

| | |
|---|---|
| **Item** | one organic-chemistry question whose B3V read reports `has_figure` |
| **Agent** | writes the reaction card from the question image, using the package's own `AI_CARD_WRITER_PROMPT.md` |
| **Check** | `check_cards()` — RDKit parses every SMILES, **OPSIN rebuilds every structure from its name** |
| **Render** | `render_card()` → HTML fragment, inline SVG, no JavaScript |
| **Stored** | the card JSON on the question record; the HTML regenerated from it on every export |

Three things make this fit without friction:

1. **The output is inline SVG with no JavaScript.** Our pages must be self-contained — the
   shareable file inlines every asset and the artifact viewer blocks external hosts — and an HTML
   fragment with inline SVG embeds in both with nothing to install. This was luck, not planning.
2. **`page_css()` once in the head, `render_card()` per figure** is exactly how `export_paper_v2`
   already composes a page.
3. **The card JSON is the stored artefact** and the picture is derived. That is the same rule as
   everywhere else here: the agent's output is the record, the rendering is a view of it.

### 2.3 What it does NOT fix, stated plainly

The guide is honest about the limits and they carry straight over. `check_cards()` catches a SMILES
that will not parse, a missing atom handle, an unknown part type, and a structure that contradicts
its name. It does **not** catch a well-formed but wrong reaction, Major and Minor swapped, or wrong
conditions on the arrow. OPSIN cannot read ions, carbocations or resonance forms at all — 25 of the
chapter's species — so those get the RDKit parse check only.

For this pipeline that means: **a rendered figure never becomes evidence.** It is a view of the
question, like the booklet crop. The answer still rests on a quoted NCERT line (D4V) or on a
concept and approach (QCA), both of which are checked by their own means.

### 2.4 Cost, and what to do first

- `brew install cairo`, Python 3.12, `rdkit==2026.9.1` pinned, Java for OPSIN, Playwright only if
  PNGs are wanted. We already have RDKit installed.
- **Run `tests/test_golden.py` before anything else.** 127 cards must come out identical. The guide
  names the two usual causes of failure — a different RDKit version, or cairo not loading — and both
  are silent.
- Pin RDKit in CI. It changes its drawings between releases.

---

## 3. Physics: the plan, and the one hard problem

### 3.1 What already works in this repo

`scripts/render_figure.py` takes a spec of primitives in **mathematical coordinates** (y up, origin
bottom left, because a person describing a diagram thinks "the vector leaves at 60 degrees", not
"y is 143 pixels down") and emits one self-contained SVG. `schemas/FIGS.json` is the vocabulary.
`scripts/build_figure_compare.py` puts each redraw beside the scan it came from.

Primitives today: `line` (dashed, arrowed), `circle`, `dot`, `polygon`, `angle`, `right_angle`,
`label` (with real subscripts), and three circuit symbols — `resistor`, `cell`, `meter`.

Four figures are drawn: a coil beside an electron path, a source velocity at 60°, a prism with
three **coloured** rays, and NCERT Figure 3.18, the Wheatstone bridge.

### 3.2 The hard problem: what is physics's OPSIN?

Chemistry's safety net works because there are **two independent routes to the same object** — the
AI writes a SMILES, and a rule-based converter rebuilds the structure from the name. Disagreement
means something is wrong, and neither route is the other's author.

Physics has no OPSIN. What it has instead is that **a figure asserts quantities, and a quantity is
recomputable from the coordinates that were drawn.** That is the equivalent, and it is strong,
because the assertion and the geometry are written by the agent independently — it has to get both
right and get them to agree.

Four levels, in order of what they catch:

**Level 1 — claimed angles (built, working).** Every angle the figure labels goes in
`angles_claimed`, and the checker recomputes it from the drawn points. This has already caught two
real errors in this pilot: a velocity vector drawn at 40.7° and labelled 60°, and a "45°" triangle
whose legs were 150 and 160, giving 43.2°. Neither was visible in the spec; both were obvious in a
number.

**Level 2 — lengths, ratios and relations (next).** A figure that labels one segment `L` and
another `2L` must draw them in that ratio. Likewise `parallel`, `perpendicular`, `collinear`,
`equal` — each a claim, each one line of arithmetic to verify.

**Level 3 — circuit topology.** A circuit card declares its netlist (`A-B: R2`, `B-C: R4`,
`B-D: G`, …). The checker derives the graph from the drawn coordinates — two components sharing an
endpoint are connected — and compares. This catches the error that matters most in a schematic: a
wire drawn to the wrong node, which looks perfectly fine.

**Level 4 — solve it.** The real analogue of OPSIN: an independent solver re-derives what the
figure asserts. A balanced Wheatstone bridge must satisfy `R1/R2 = R3/R4`. A ray at a stated angle
of incidence must satisfy Snell's law at the stated refractive index. A labelled resultant must be
the actual vector sum. Where a question's own answer is a number, the figure's geometry and that
number must agree — and when they do not, one of them is wrong and we have learned something either
way. This is where a physics renderer stops being a drawing tool and starts being a check on the
question bank.

### 3.3 The step

**FIGP** (figure, physics), mirroring FIGC:

| | |
|---|---|
| **Item** | one physics question (or NCERT figure) with a drawing |
| **Agent** | `figure-redrawer` — reads the image, writes a FIGS spec **and** its claims |
| **Check** | spec renders; every claimed angle, ratio and relation recomputes; netlist matches |
| **Render** | `render_figure.py` → inline SVG |
| **Review** | `build_figure_compare.py` — the scan above, the redraw below, claims reported |

The agent brief must carry one rule above all others, learned from my own first pass:

> **Compute the coordinates from the stated quantity. Never eyeball them.**
> A vector at 60° ends at `(x + L·cos 60°, y + L·sin 60°)`. A 45° right triangle has equal legs.
> A drawing that contradicts its own label is worse than the photocopy it replaced, because it
> looks authoritative.

### 3.4 Where to stop hand-rolling

The research says this plainly: `schemdraw` 0.23 is the right tool for a real circuit —
component libraries, transistors, logic gates — and `drawsvg` 2.4.2 for general vector work
(`svgwrite` is archived; don't start there). Our three hand-rolled symbols cover a resistor, a cell
and a meter, which is enough for the Current Electricity figures in this corpus and **not** enough
for anything with a transistor. The rule: when a figure needs a component symbol we do not have,
hand over to schemdraw rather than grow a second component library.

### 3.5 Order of work

1. **Golden set first.** Twenty NCERT physics figures, hand-authored and reviewed beside their
   scans, before any agent runs. That is what the chemistry package did with 127 cards, and it is
   why its regression test means anything.
2. **Levels 2 and 3 of the checker**, which are arithmetic and a graph comparison.
3. **The agent brief and the FIGP step**, run against the golden set as the answer key — the same
   measurement the chemistry guide lists as its own next step ("how often a real model writes a
   correct card on its first try: unknown").
4. **Level 4 solvers**, per topic, starting with circuits and ray optics.

### 3.6 Limits to state now, before anyone over-trusts this

- A redraw is a **claim about a scan**, and the scan stays beside it on every page for that reason.
- The checker verifies **internal consistency**, not fidelity. A figure can be self-consistent and
  still not be the figure that was printed. Only the side-by-side review catches that.
- Curved field lines, ball-and-stick art and anything genuinely pictorial are out of scope —
  the chemistry package reached the same conclusion for raster art and kept NCERT's images.
- Nothing here changes what counts as evidence. A figure is a view of a question, never its proof.
