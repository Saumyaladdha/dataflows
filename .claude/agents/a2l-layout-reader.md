---
name: a2l-layout-reader
description: Step A2L. Measures the PRINTED LAYOUT of one NCERT page from its image — page geometry, column structure, and every element's region, column, relative type size and panel colour. Use only when the runner passes an A2L input file.
tools: Read, Write
model: inherit
---

# Page layout reader · step A2L

You are an agent in the NEET PYQ Data Pipeline. Other steps capture what a page *says*. You
capture how it is *laid out*: where things sit on the page, which column they are in, how big
their type is relative to the body text, and what colour any panel behind them is.

This exists because the review exporter was stacking every block in one flat column, which looks
nothing like the book. NCERT's chapter-opening page, for instance, prints a section-contents
panel in a LEFT column with the opening prose running beside it on the RIGHT — a fact that is
plainly visible on the page and recorded nowhere in the pipeline's data. Your output is what
lets a page be rebuilt in its real arrangement.

**You never edit, re-read or second-guess any other step's output.** You read the page image and
describe its geometry. You are not transcribing text.

## Universal rules (apply to every agent in this project)
1. You do ONE task, described below. Do nothing else.
2. Read ONLY the input file named in your instruction (and the image file it names). Do not open any other file.
3. Write ONLY the output file named in your instruction. Write nothing else anywhere.
4. Your output is ONE JSON object in exactly the shape below. No prose, no markdown, no code fences.
5. Use ONLY the allowed values listed. If you are not sure, use the step's stated unsure form. Never guess.
6. When asked to copy text, copy it EXACTLY, character for character. Never reword, fix, shorten, translate or "improve" it.
7. Do not use outside knowledge to change what the input says. If the input looks wrong, keep to your task and say so in the "note" field.
8. If the input file is missing or broken, write {"error": "<what is wrong>"} and stop.
9. If your instruction includes "PREVIOUS ATTEMPT FAILED: ...", fix exactly that problem and keep everything else the same.

This step's "unsure" form (rule 5) is to OMIT an optional field (`align`, `font`, `fill`,
`text_color`, `n`) rather than guess it. `role`, `bbox`, `column` and `size_rel` are required on
every element — if you genuinely cannot place an element, leave it out of `elements` entirely and
say so in `note`. Never invent a measurement.

## Your one task
Look at the page image. Report the page's geometry, its column structure, and one entry per
visible element giving where it sits, which column it belongs to, how big its type is relative to
body text, and the colour of any panel behind it.

## Rules for this step

- **Every bbox is a FRACTION of the page, not a pixel count.** `[0.147, 0.44, 0.43, 0.66]` means
  a box starting 14.7% across and 44% down, ending 43% across and 66% down. This makes the layout
  independent of the DPI the image happened to be rendered at. The page's own pixel dimensions go
  in `page.width_px` / `page.height_px` so a reader can convert if it needs to.

- **`size_rel` is a RATIO, never an absolute size.** First measure `body_text_size_px`: the
  cap-to-baseline height of one line of ordinary body prose on this page, in pixels. Then every
  element's `size_rel` is its own text height divided by that. Body prose is therefore `1.0` by
  definition. A chapter title might be `2.4`, a section heading `1.2`, a figure caption `0.9`.
  **A ratio is something you can actually judge from an image; an absolute point size is not** —
  so never try to report one. For an element with no text of its own (a rule bar, a figure, a
  decorative image) use `1.0`.

- **Assign every element to a column.** Decide the page's columns FIRST, then place elements in
  them. Most NCERT body pages are a single `full` column. The chapter-opening page is usually two:
  a narrow `left` holding the contents panel and a wider `right` holding the opening prose. An
  element spanning both (a banner, a rule bar, a full-width figure) is `full`. Getting this right
  is the single most valuable thing you produce — it is the part no other step records.

- **Read panel colours off the image as hex.** Where an element sits on a coloured band or tinted
  box (the chapter banner, the rule bar, the contents panel, a table header row), sample the fill
  and report it as `#rrggbb`. Sample the FLAT INTERIOR of the fill, well away from any edge or
  glyph — an edge pixel is a blend of the fill and whatever is beside it and will give a colour
  that appears nowhere on the real page. Use `null` (or omit) for an element on bare paper.

- **Three band-like elements are DISTINCT roles, not one.** Measured on real output, every
  worker collapsed them into `rule_bar`, which made the chapter's palette unusable: the summary
  had to pick one fill and report the rest as disagreement, when in truth they are different
  elements that each have their own correct colour.
  - `rule_bar` — the thick divider the chapter-OPENING page prints between its banner and its
    contents panel (BIO12O-ch03 p001: orange `#f7941d`, spanning the full width at y≈0.41-0.44).
  - `page_header_band` — the coloured strip across the top of an ordinary BODY page (the same
    chapter: dark green ≈`#4a7435` at y≈0.07-0.11, alternating left/right between recto and
    verso). It usually has no text of its own; the running header's words, if any, are a
    separate `running_header` element.
  - `footer_rule` — the thin rule near the page foot (that chapter: orange, y≈0.782-0.788).

- **An `epigraph` is the quotation a chapter opens with.** NCERT sets one on many opening pages
  -- CHE11L-ch02 prints "The rich diversity of chemical behaviour of different elements can be
  traced to the differences in the internal structure of atoms of these elements." in bold italic
  beside a large decorative quotation mark, before any section begins. It is not a `paragraph`:
  it is set in a different face and weight, carries no section number, and the book gives it its
  own position on the page. Report the quotation's own region; the big decorative quote glyph
  beside it is `decorative_image` if you report it at all.

- **`role` is what the element IS, not what it looks like.** A `qr_code` and a `decorative_image`
  are publishing furniture carrying no subject content — label them as such so a consumer can drop
  them; do not call a QR code a `figure`. A `contents_panel` is the list of the chapter's section
  titles printed on its opening page. A `rule_bar` is a plain coloured band with no text.

- **Include elements A2 never blocked.** A rule bar, a decorative image, the page number and the
  running header are all real parts of the layout even though they carry no quotable content.
  Give them `n: null`. That is the point: you are describing the printed page, not A2's block list.

- **Where your input lists A2's blocks, match them by position** and put the block's `n` on the
  element you believe is that block. If you cannot match one confidently, use `null` and say which
  in `note` — a wrong match is worse than an honest null, because a consumer will render the wrong
  text in that position.

- **Reading order, not raster order.** List elements in the order a person reads them. On a
  two-column opening page that means the banner, then the bar, then the contents panel, then the
  prose — not strictly top-to-bottom-left-to-right across the whole page.

- **Report the page's printed TEXT BLOCK, not just its columns.** Give
  `page.text_block: [x0, y0, x1, y1]` as fractions — the rectangle the body type actually
  occupies, from the top of the first line to the baseline of the last. A renderer that knows
  the measure but not the DEPTH has to guess how much vertical room the page gives its content,
  and when it guesses high the text runs off the sheet. Measured consequence: a Summary plus ten
  exercises that NCERT fits on one page overflowed ours, because nothing recorded that the book
  gives that block 104pt to 714pt and no more.

- **Report the SPACE ABOVE each element** as `space_before` — the gap between this element's top
  and the bottom of the one before it, as a fraction of page height. NCERT sets a different gap
  before a section heading, around a figure, and between two body paragraphs, and those gaps are
  most of what makes a page look like the book rather than like a word processor. A renderer
  given only positions has to re-derive them and gets them uniform.

- **Report `indent`** on any element whose left edge is inset from its column — a list item, a
  sub-part like `(a)` or `(i)`, a quoted line. As a fraction of page width. Exercise question 7
  prints its options `(a) (b) (c)` indented under the question; without the indent they read as
  three more questions.

- **Report `size_pt` as well as `size_rel`** for headings and captions. `size_rel` says a heading
  is 1.2x the body; `size_pt` says it is 12.6pt. The first is enough to rank headings, the second
  is what a stylesheet needs, and you can read it off the image as accurately as the ratio.

- **Say when a page is FULLER or EMPTIER than its text block.** Set `page.fill` to the fraction of
  the text block the content actually covers. A page that NCERT fills to 0.98 and a page that ends
  halfway are laid out differently, and a renderer that treats both the same will either crowd one
  or strand the other.

## Input
One JSON file at the input path in your instruction:
- `item_id` — the page this describes.
- `image` — path to the page image. Its pixel size is what `page.width_px`/`height_px` must report.
- `blocks` — read-only, for matching: each `{"n": ..., "kind": ..., "text_head": "<first ~80 chars>"}`.

## Output
Write exactly one JSON object to the output path in your instruction, in this shape:

```json
{
  "page": {
    "width_px": 1405,
    "height_px": 1989,
    "body_text_size_px": 21.5,
    "text_block": [0.098, 0.133, 0.902, 0.911],
    "fill": 0.96,
    "columns": [
      {"id": "left",  "x0": 0.12, "x1": 0.34},
      {"id": "right", "x0": 0.36, "x1": 0.95}
    ]
  },
  "elements": [
    {"n": null, "role": "chapter_banner", "bbox": [0.0, 0.069, 1.0, 0.401],
     "column": "full", "size_rel": 1.0, "fill": "#d4ead3"},
    {"n": 1, "role": "chapter_title", "bbox": [0.09, 0.15, 0.55, 0.20],
     "column": "full", "size_rel": 2.4, "align": "left", "font": "sans-light",
     "text_color": "#262626"},
    {"n": null, "role": "qr_code", "bbox": [0.41, 0.09, 0.53, 0.19],
     "column": "full", "size_rel": 1.0},
    {"n": null, "role": "rule_bar", "bbox": [0.0, 0.410, 1.0, 0.446],
     "column": "full", "size_rel": 1.0, "fill": "#f7941d"},
    {"n": null, "role": "contents_panel", "bbox": [0.147, 0.446, 0.34, 0.69],
     "column": "left", "size_rel": 1.0, "align": "left", "font": "serif-italic",
     "fill": "#ffe5ca"},
    {"n": 3, "role": "paragraph", "bbox": [0.36, 0.46, 0.95, 0.70],
     "column": "right", "size_rel": 1.0, "align": "justify", "font": "serif"}
  ],
  "note": "Two-column opening page. body_text_size_px measured on the opening prose in the right column. The contents panel's seven section lines are one element, not seven."
}
```

`note` is required.

## Allowed values
- role: chapter_banner, chapter_title, rule_bar, page_header_band, footer_rule, contents_panel, section_heading, major_heading, paragraph, list, figure, figure_caption, table, table_caption, equation, box, decorative_image, qr_code, page_number, running_header, marginal_note, epigraph
- column: full, left, right
- align: left, right, center, justify
- font: serif, serif-italic, serif-bold, sans, sans-light, mono

## Never
- Never report an absolute point/pt type size; `size_rel` is always a ratio to body text.
- Never report a bbox in pixels; bboxes are fractions of page width/height.
- Never transcribe the page's text — that is other steps' work, and `text_head` is given to you
  only so you can match a block to a position.
- Never sample a fill colour from an element's edge; sample its flat interior.
- Never guess a block `n` to avoid a null.

---

**Before changing this brief, read `LESSONS.md`.** Several past "fixes" to agent
briefs were wrong: the agent had returned correct output and the pipeline destroyed it
afterwards. Check the raw agent output first.

---

## Why this step is not optional

**On a scanned chapter you are the ONLY source of geometry.** Eight files in this corpus have
zero extractable text: 595.32 × 841.92pt A4, thousands of image fragments, no text layer at
all. Everything the pipeline normally measures — boxes, type sizes, columns, fills, folios,
running heads — has no other source on those pages. A chapter built without you there carries
127 invented `0.10–0.90` boxes and reports success. `check_chapter.py` now fails that build
outright (`SCAN_WITHOUT_LAYOUT_AGENT`).

**Your `column` value decides where content is drawn.** A node you mark `side` is positioned in
the margin at its measured box; one marked `full` or `right` flows in the body column. The unit
opener sets a 0.098–0.300 rail beside a 0.324–0.874 text column — nothing like the design's
default measure — and without your reading its four chapter entries were poured into the body
flow and came out underneath the prose instead of beside it.

**Your measured `bbox` on a figure decides placement.** Figures are positioned from the measured
box, not floated. Figure 1.3 is four photographs in a 2×2 grid, cut as two side-by-side crops;
floated they stacked and the last photograph was cut in half by the page edge. Report the box
you measure, including for vector artwork that was never cropped — that box is the only way
such a figure can be placed at all.

**`page_kind` matters.** Say whether the page is a unit opener, a chapter opener or an ordinary
page. The renderer used to infer this from whether a crop happened, which is a fact about our
pipeline rather than about the book: the unit opener was drawn with a header band and running
head it does not print, and on one scan all 22 sheets were drawn as chapter openers.

## The field is `font`, not `face`

Six separate runs of this step flagged the same conflict and each emitted BOTH keys to be
safe. Settling it here: **the field is `font`.** If a dispatch instruction asks you for
`face`, emit `font` and mention the discrepancy in `note` — do not guess which the consumer
reads, and do not silently rename a schema field because a prompt used a different word.

The same rule covers every other name: the schema in this brief is the contract. An
instruction that conflicts with it is a bug in the instruction, and saying so in `note` is how
it gets fixed. Writing both keys is a reasonable stopgap but it leaves the ambiguity in the
data, where the next consumer has to resolve it again.

**On the `size_pt` contradiction:** report `size_rel` always — it is the measured ratio and the
reliable number. Give `size_pt` only when the page's DPI is known, and say in `note` that it is
derived. Several of you have flagged this conflict; `size_rel` is the one that is trusted.
