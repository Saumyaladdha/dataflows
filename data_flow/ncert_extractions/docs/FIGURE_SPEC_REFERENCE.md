# Writing a figure spec, or a reaction card

Two renderers, two formats. **Physics** figures are a spec of primitives drawn by
`scripts/render_figure.py`. **Organic** reactions are a card of SMILES drawn by
`scripts/render_reaction.py` through RDKit. Both are JSON, and in both the rule is the same:

> **You describe WHAT is there. The renderer decides how it looks.**
> Never give a colour, a size or a position that the renderer can work out for itself.

---

## Part 1 — a physics spec (`figures/specs/<id>.json`)

### Coordinates

**y increases UPWARD**, origin bottom-left, units arbitrary. Write what you mean — "the vector
leaves the origin at 60°" — and compute the endpoint. Never guess pixel positions.

```json
{"figure_id": "PHY12L_CH03_P143", "title": "What the figure shows, as a sentence",
 "width": 340, "height": 335, "pad": 20,
 "draw": [ ... ], "angles_claimed": [ ... ], "note": "..." }
```

### The primitives

| kind | required | options |
|---|---|---|
| `line` | `from`, `to` | `dashed`, `arrow` (`end`/`start`/`both`), `colour`, `width` |
| `circle` | `centre`, `r` | `colour`, `width`, `fill` |
| `dot` | `centre` | `r`, `colour` |
| `polygon` | `points` (≥3) | `colour`, `width`, `fill` |
| `angle` | `vertex`, `r`, `from_deg`, `to_deg` | `colour`, `width` |
| `right_angle` | `vertex` | `size`, `towards` (e.g. `[1,-1]`) |
| `label` | `text` + (`at` **or** `beside`) | `sub`, `sup`, `size`, `colour`, `italic`, `anchor`, `style` (`serif`/`sans`) |
| `resistor` | `from`, `to` | `zigs`, `amp`, `lead`, `colour` |
| `cell` | `centre` | `plates`, `horizontal`, `long`, `short`, `gap` |
| `meter` | `centre`, `r`, `text` | — (a circle with its letter: G, A, V) |
| `diode` | `from`, `to` | `size` |
| `gate` | `at` | `gate` (`and`/`or`), `w`, `h` |
| `terminal` | `centre` | `r` (the small open circle on a lead) |
| `block` | `centre`, `w`, `h` | `deg`, `hatch` (a hatched box, for mechanics) |

Colours: `ink` (the drawing), `accent` (what the question turns on), `muted` (annotation), and
`blue` `green` `red` `violet` `orange` `yellow` **only when the figure is ABOUT colour** — a ray
diagram naming its rays, a spectrum. Never decorative.

### Three rules that have each already caught a real error

**1. Compute a position, never estimate it.** A vector at 60° from `(10,20)` with length 150 ends
at `(10 + 150·cos 60°, 20 + 150·sin 60°)` = `(85, 150)`. A 45° right triangle has **equal legs**.
The first draft of this pilot drew a vector at 40.7° under a label reading 60°, and a "45°"
triangle whose legs were 150 and 160 — giving 43.2°. Both looked fine and both were wrong.

**2. Claim every angle the figure labels**, including right angles, in `angles_claimed`:

```json
{"degrees": 60, "vertex": [10, 20], "ray_to": [85, 150], "measured_from": [240, 20]}
```

The checker recomputes each one from your coordinates and reports a mismatch beneath the figure.
A right-angle *mark* with nothing claiming it is decoration — the lines may not be perpendicular
at all.

**3. Label a component with `beside`, not `at`.**

```json
{"kind": "label", "text": "R", "sub": "2", "italic": true,
 "beside": {"from": [30,200], "to": [170,320], "offset": 46, "side": -1}}
```

The renderer puts it `offset` away from the midpoint, perpendicular to the component, on `side`
(+1 or −1). Hand-computed positions land on the drawing — `R₂` and `R₄` did exactly that, twice.
Use `sub` / `sup` for subscripts; a separately positioned "2" drifts.

### What not to attempt — and how to decide

**A redraw replaces a scan only when it can replace it COMPLETELY.** Where the figure IS the
illustration, a partial redraw is worse than the scan: it looks authoritative and is missing the
thing the figure is about. An oscillating table fan drawn as two crossed axes is not that figure.

The test is not "does it contain a picture". It is: **is there a diagram left once the picture is
removed?**

**Rule 1, categorical and absolute. A PERSON, a hand, or a rendered real object as the SUBJECT puts
a figure out of scope — however much geometry surrounds it.** No redraw replaces a drawing of a
girl swinging a stone, and the caption under that one says "we can FEEL this": the demonstration IS
the figure.

This rule replaced a primitive-count threshold, because the count was the wrong test. Figure 4.4
reached **26 primitives** — a clean ellipse, the string, the stone, two motion arrows — and still
had to be dropped. Counting geometry measures how much is left, not whether what is left is the
figure.

**Rule 2, for everything else: is there a diagram left once the picture is removed?**

| | |
|---|---|
| **Out of scope** | the figure's content is a shaded 3-D solid, an apparatus photograph, a freeform surface, or a tonal wash that carries the meaning. Measured: these leave 1–12 primitives. |
| **In scope** — draw it, list the picture in `unreadable` | the pictorial element is incidental and the physics survives without it. A car on a banked road becomes a rectangle and the force diagram is untouched: 68 primitives, four verified angles. |

When you declare a figure out of scope, still write the spec file, with `"out_of_scope": true` and
the reason in `unreadable`. The decision then stays on record and nobody re-attempts it.

Examples already decided, in `legacy/figures_not_targeted/`: a ceiling fan and potter's wheel, an
oscillating table fan, a girl on a swivel chair, an arbitrary closed surface drawn as a blob.

**Tables are the opposite case and redraw very well.** NCERT's data tables become clean selectable
vector text instead of a watermarked raster. Where a table has a "Figure" column of 3-D pictograms,
drop that column and keep the rest — the "Axis" column states the same thing in words.

---

## Part 2 — an organic reaction card (`figures/cards/<id>.json`)

```json
{"title": "Aniline + benzoyl chloride, NaOH → N-phenylbenzamide",
 "row": [
   {"mol": "Nc1ccccc1", "name": "Aniline", "w": 200, "h": 160},
   {"plus": true},
   {"mol": "O=C(Cl)c1ccccc1", "name": "Benzoyl chloride", "w": 220, "h": 170},
   {"arrow": {"above": "NaOH", "len": 110}},
   {"mol": "O=C(Nc1ccccc1)c1ccccc1", "name": "N-Phenylbenzamide", "w": 300, "h": 180}
 ]}
```

| part | keys |
|---|---|
| `mol` | a **SMILES**, plus `name`, optional `tag` (`Major`/`Minor`), `w`, `h` |
| `plus` | `true` |
| `arrow` | `{"above": "...", "below": "...", "len": 110}` — reagent above, conditions below |
| `text` | plain text for anything that is not a structure |

**The SMILES is the molecule.** A wrong atom still draws a valid-looking picture, so write the
SMILES from the structure you can see and give the `name` as NCERT prints it — the two are checked
against each other. The renderer reports each molecule's formula; if it does not match what you
intended, the SMILES is wrong.

Canvas sizes: roughly 150 px per ring plus 60 px per substituent label. Too small and RDKit
crushes the structure; too large and it floats in space.

**Draw a structure only where NCERT DRAWS a structure.** Where the book writes a condensed formula
— `(C₂H₅)₂CHNH₂`, `CH₃–NH–CH₃`, `R–NH₂` — carry it as a `text` part, written exactly as printed.
Converting it to a skeleton changes what the figure shows, and on an exercise it can hand over the
answer: Intext Question 9.1 asks the reader to classify four amines, two of which NCERT prints as
formulas; drawing their skeletons shows the nitrogen's substitution directly.

The same rule kills a whole class of card. **A data table is not a reaction card.** Table 9.3 lists
ten amine names and their pKb values and draws nothing at all; a card built from those names put ten
structures beside a scan that has none. If the crop draws no structures, there is no card to write.

**Keep NCERT's order.** The parts of a `row` are drawn in the order you list them and the row never
rewraps, so list them exactly as the book prints them left to right. NCERT's sequences usually mean
something — its four example amines run one, two, then all three hydrogens replaced — and a reader
comparing the redraw with the scan matches them by position.

### Structure options

| key | what it does |
|---|---|
| `orient` | `{"atom": 1, "deg": 90}` — rotate so the atom carrying map number 1 points at 90° from the ring centre. NCERT hangs a substituent ABOVE its ring; drawn to the side it reads as a different arrangement. Map numbers are handles (`[N+:1]`) and are never drawn. |
| `abbreviate` | `true` — condense NO₂, SO₃H, COOH, CHO, OCH₃ into text on the ring, as NCERT prints them. An expanded nitro group is a different notation from the book's. |
| `overlay` | a list of marks placed from RDKit's own atom positions: `{"kind": "lone_pair", "atom": 0, "push": 16}`, or `"plus"` / `"minus"` for a circled charge. |

`overlay` positions are computed, never guessed: the renderer asks the drawer where it actually put
the atom and pushes the mark OUTWARD from the molecule's centre, so it lands outside the ring. A
pixel offset cannot work, because RDKit chooses both the layout and the scale.

**Lone pairs are content, not decoration.** NCERT prints `:NH₂` on aniline because that pair is why
aniline is a base, and on several figures it is the whole point.

**Reagents and counter-ions are WRITTEN, not drawn.** NCERT prints `HBF₄`, `Cl⁻`, `N₂BF₄⁻` as
formulas; expanding tetrafluoroborate into a boron with four fluorines is a different figure. Use a
`text` part. The same goes for anything with no bonds — ammonia, HCl — which the renderer refuses
outright, because a single-atom drawing has no bond length to scale by and fills the canvas.

**Still out of scope for this pilot:** curved electron-pushing arrows, resonance brackets, 2-D grid
schemes, and NCERT's exact Bookman-matched type. Those are what the Arivihan Chemistry Renderer
handles; if a figure needs them, say so in `unreadable` and leave it its scan.
