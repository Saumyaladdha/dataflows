# Physics layout: measured comparison against the reference build

Measured 2026-10-15 by the main session. Every number here came from rendering a PDF and
measuring pixels, or from counting markup in the generated HTML — not from the PDF text layer.

## The reference build

`exports/review/html/PHY12O-ch01_READER_1.html` is an older physics build whose CONTENT is
unreliable (many transcription errors) but whose LAYOUT paginates markedly better. It is a
reference for layout only.

## Pagination, printed and measured

| build | sheets | blank | sparse | mean ink |
|---|---|---|---|---|
| READER_1 (reference) | 54 | 3 | 2 | 8.3% |
| current | 65 | 6 | 7 | 10.1% |
| **the book** | **50** | **0** | **0** | **~20%** |

## What is NOT the cause

These were checked and found **identical** between the reference and the current build, so none
of them explains the 11-sheet difference:

- **Design tokens**: all 46 `--*` custom properties match exactly — same fonts
  (`Bookman Old Style`/`TeX Gyre Bonum` body, `Century Gothic`/`TeX Gyre Adventor` display),
  same palette (`--accent: #00adef`, `--banner: #c6eafb`, `--box-fill: #dbdcde`,
  `--folio-fill: #c6eafb`), same measured `--size-*` scale.
- **Print CSS**: all 16 rules inside `@media print` are byte-identical.
- **Page geometry**: both 215.9mm × 276.6mm (612×784pt), both `line-height: 1.21`.
- **Sheet structure**: both have 50 `<section class="page-row">`, 50 `band-tab`s.

## What IS different — the likely cause

| marker | reference | current | note |
|---|---|---|---|
| `fig-float` | 12 | **21** | the current build floats 9 MORE elements |
| `box-group` | 27 | **22** | the current build merges 5 FEWER worked-example fragments |
| `folio-tab` | 53 | 51 | minor |

Both differences push the sheet count up:

1. **Too many floats.** The main session changed `_column_map_for_page` to derive an element's
   column from its measured bbox instead of A2L's `column` label (the label was wrong — 621
   physics elements claimed `full` while their own bboxes showed two columns). That fix is
   correct in principle and is what finally let prose wrap beside FIGURE 1.4 on p006. But it is
   evidently over-firing: 21 floats against the reference's 12. A float carries
   `break-inside: avoid`, so a wrongly-floated paragraph becomes an unbreakable block that jumps
   whole to the next sheet. **Suspect first: paragraphs being floated as if they were figures.**
   Check what roles are receiving a side column — only `figure`, `box`, `marginal_note` and
   `table` should float; a `paragraph` or `list` in a side column is the OTHER column and should
   stay in flow so it wraps around the float.

2. **Less box merging.** `_merge_box_runs` is producing 22 groups where the reference produced
   27. Fewer groups means example fragments are rendering as separate panels with their own
   padding and margins, which both wastes vertical space and creates more break opportunities.

## Also reported by the user, unverified by me

- Heading colours and box colours differ from the book. Physics measures FOUR box fills in A2L
  (`#dbdcde` worked examples, `#c6eafb` feature boxes, `#9cdcf8` scientist panel,
  `#d1d2d4` Points to Ponder) and TWO heading inks (grey `#6d6e71` for x.y headings, cyan
  `#00adef` for captions, sub-headings and box bars). Verify each renders its own measured
  value rather than one collapsed per-role colour.

## Page furniture — measured, book vs ours

Measured by colour-masking `#c6eafb` (the folio fill) and the glyph ink in the foot margin.
Book figures from `Old_ncert_Physics_Chapter_1.pdf` p2; ours from the current build, sheets 2 and 4.

| | book | ours | note |
|---|---|---|---|
| folio tab x | 0.127–0.185 | **0.000–0.072** | ours BLEEDS to the trim; the book INSETS it 12.7% |
| folio tab y | 0.916–0.937 | **0.648–0.680** | ours sits two-thirds down; the book puts it at the foot |
| folio width | 0.058 | 0.072 | ours ~24% too wide |
| folio height | 0.021 | 0.032 | ours ~50% too tall |
| year imprint | centre x 0.499, y 0.956 | present, roughly centred | the book centres it on EVERY page |

The folio was deliberately drawn from CSS at the sheet edge rather than cropped, because absolute
positioning could not paginate — but the position it was given is wrong on both axes. It belongs
at the FOOT of the page, inset from the trim, not bled off the side at 65% height.

Note the book alternates the folio to the OUTER corner: left on a verso, right on a recto, as the
chapter-opening reference pages show. Whatever fix is applied should mirror with the spread the
same way the header band already does.
