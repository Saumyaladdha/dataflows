# LESSONS — every defect this pipeline has shipped, and the rule that stops it

**Read this before changing anything in `code/` or `agents/`.** It is not a style guide. Every
entry below is a real defect that reached a finished-looking file and was caught by a person
reading it, not by a test. The rule under each one is what the code now enforces, and
`code/check_chapter.py` fails the build on most of them.

If you are an agent or an engineer picking this up: the fastest way to do harm here is to make
a page *look* finished. Everything in this file was, at the time, output that looked fine.

---

## 0 · The three rules that generate all the others

**0.1 — NEVER LET A GUESS LOOK LIKE A MEASUREMENT.**
The single most damaging defect in this project's history was not a wrong number. It was 127
invented bounding boxes, all `0.10–0.90` wide and evenly subdivided down the page, that reached
`chapter.json` carrying no indication they were invented. A consumer cannot tell them from
measurements, so it trusts them. Every box now carries `src`: `measured` (PDF text layer),
`agent` (a2l-layout-reader measured the page image), or `estimated` (invented — a reading-order
guess that describes no printed layout). `BOX_NO_PROVENANCE` and `ESTIMATED_GEOMETRY` fail the
build.

**0.2 — A PIPELINE THAT CANNOT DO THE JOB MUST SAY SO, NOT PRODUCE SOMETHING.**
`BIO12L-ch01` is a pure A4 scan: 595.32 × 841.92 pt, **zero** extractable characters, 6,794
image fragments. Everything downstream of the text layer — boxes, marks, folios, running heads,
figure captions, the chapter title, table grids — had no source at all. The pipeline built it
anyway and reported `23 pages, 26 figures, 137 nodes`. Not one measured box. Not one mark. An
empty chapter title. It looked like success. `SCAN_WITHOUT_LAYOUT_AGENT` now fails that build.

**0.3 — CONTENT THAT DOES NOT FIT MUST BE REPORTED, NEVER HIDDEN.**
The sheet is a fixed height with `overflow:hidden`. A `--fit` floor of 0.72 did not make
content fit; it made the overflow invisible — text ran under the footer bar and stopped
mid-sentence. The floor is gone, the factor now says what the page actually needs, and
`PAGE_OVERFLOW` fails the build below 0.72 because at that point the content is on the wrong
page and shrinking is not the fix.

---

## 1 · Input classes — know what you are reading before you read it

| | born-digital | **pure scan** |
|---|---|---|
| count in corpus | most | **8 files** |
| page size | 612 × 784 pt and kin | **595.32 × 841.92 pt (A4)** |
| aspect | 0.781 | **0.707 — a different SHAPE, not a crop** |
| text layer | yes | **zero characters** |
| geometry from | PyMuPDF spans | **a2l-layout-reader ONLY** |

The eight scans: `new/class_12/biology/Chapter_{1,4,7,9,11}.pdf`,
`old/class_12/biology/Old_ncert_Bio_Chapter_{2,3}.pdf`,
`old/class_11/chemistry/P2/6 5. Organic Chemistry….pdf`.

**Rule.** Read the page's own `mediabox`; never assume the design's canonical trim. Forcing
612 × 784 on an A4 scan makes every sheet wider and shorter than the book, and then *no*
coordinate can line up however good the stylesheet is. `sheet_pt`, `sheet_aspect` and
`geometry_source` are on every page record. `SHEET_NOT_CANONICAL` warns.

---

## 2 · Defects in reading the page

| what shipped | why | rule now |
|---|---|---|
| Folio and running head swapped on **every** page — `Biology 4` read as a heading | `4`.bbox[3]=76.49 vs `BIOLOGY`.bbox[3]=76.43; rounding to 1dp sorted them wrongly, flipping recto/verso | sort lines on a **3pt baseline bucket**, never on raw y |
| `Summary` and `Exercises` rendered **empty** | column-first reading order put the heading (y=0.134) after the paragraph (y=0.168) | order blocks by y before column |
| A whole 479-char paragraph bold | the join gave agent text the **first run's** flags | re-locate each formatted substring inside the agent's text |
| `andtypes`, `Linnaeusused`, `andmelongena`, `Allthese`, `undera`, `triploidendosperm`, `Mangovarieties`, `isthe` | page-break stitching joined `text` with a space and `runs` **without** one — and `body` is built from the runs | insert a separator run when stitching; **verified 0 remaining** |
| Exercises flattened into one block | the agent returned them `\n`-separated and `re.sub(r"\s+", " ")` destroyed it | collapse **spaces and tabs only**, never newlines |
| 11 figures on a 1-figure chapter | vector drawing paths clustered into "figures" | only claim a figure on a page that prints `Figure N.M` |
| A header band rendered mid-page under a caption | bands are vector art too | exclude furniture zones from vector clustering |
| `Monocotyledona` (truncated) in a table cell | geometry split the cell | A2S reads table cells; geometry only grids them |

**The agent is usually right and the join is usually wrong.** Twice I "fixed" an agent that had
returned correct output which my own post-processing then destroyed. Check the agent's raw
output before changing its brief.

---

## 3 · Defects in the tree

- **Orphan nodes put 23 pages on one sheet.** 12 `section` nodes were built inline and never
  given a page key; the renderer buckets by page, so they all landed together, every section
  overlapping the next. → every node carries `pages` **or** `page_file`. `ORPHAN_NODES` fails.
- **Nodes created by a late pass escape tagging.** The question-split runs after the tree is
  assembled, so its nodes reached the file with no `belongs`. → tag **after every pass that can
  create a node**, as the last thing before serialisation.
- **Unit pages were dropped, costing 95 words** including the whole Ernst Mayr biography. They
  belong to the book rather than the chapter — which is a reason to *route* them to `UNIT#`
  rows, never a reason to drop or stop printing them. → one tree over the whole file, every
  node tagged `belongs: unit|chapter`.
- **`pages` must list every page of the source file.** Listing only the chapter's made the
  render 2 sheets short and renumbered every folio after them.

---

## 4 · Defects in the render

- **The page template was inferred from whether a crop existed.** `is_opener = any(a["kind"]
  == "header art" …)` is a fact about our pipeline, not about the book. The Unit opener has no
  such crop, so it was drawn as an ordinary page — header band, running head, single measure —
  none of which that page prints; and on the Class 12 scan art was detected everywhere, so
  **all 22 sheets** were drawn as chapter openers. → `page_kind` is **data** on the page
  record: `unit_opener` | `unit_page` | `chapter_opener` | `ordinary`. `ALL_OPENERS` fails.
- **One sheet per source page, always.** 23 PDF pages → 22 sheets means every folio after the
  gap is one short of the book. `SHEET_COUNT` fails.
- **One crop attached to five different figures** (`i019_fig01.png` on pages 5, 8, 12, 17, 19 —
  pages printing different illustrations). `IMAGE_REUSED` fails.
- **Figure boxes outside the page** (`bbox[3] = 1.0739`). `BOX_OUT_OF_PAGE` fails.
- **26 figures, not one caption** — the captions were in the tree as ordinary paragraphs, which
  also corrupts the prose: `False fruits of apple and strawberryin which fruits develop without
  fertilisation` welds a caption onto the next paragraph and changes the biology.
  `FIGURE_NO_CAPTION` fails.
- **Multi-panel figures lose their grouping.** The four Zoological Parks photos are one
  `Figure 1.3` in a 2×2 grid with one caption; floated individually they stack down the page
  and the last is cut off at the footer.
- **Running head printed the chapter title on every page.** The measured string was on the page
  record; the renderer was passed the chapter title instead. Verso prints `Biology`, recto the
  chapter name.
- **No print pagination.** Without `break-after:page` + `@page size`, Cmd-P repaginates and a
  784pt sheet lands across two A4 leaves.

---

## 4b · The page-break defect — now fixed, and why it mattered most

A paragraph printed across two pages is **one node** in the tree (right: a product asking for
"1.2.1 Species, paragraph 2" wants all of it) but **two fragments** on paper. The renderer
emitted the whole node on the first of its pages. Consequences, all of which were reported as
separate defects by separate reviewers:

- the continuation appeared on the wrong page, and the next page began mid-thought
- the first page overfilled, which is what drove `--fit` down and then clipped it
- an external reviewer named every break point in Class 11 ch01 and all four were wrong

`char_ranges` records which characters printed on which page. The renderer now slices the body
and its marks per range and emits each fragment on its own sheet, so the node stays whole in
the data while the render breaks where the book breaks:

| page | ends | next page begins |
|---|---|---|
| 3 | `…biodiversity or the number and` | `types of organisms present on earth` |
| 5 | `…arrangement of organisms. Linnaeus` | `used Systema Naturae as the title` |
| 6 | `…Solanum includes species like nigrum and` | `melongena. Human beings belong…` |
| 7 | `…the next higher category called Phylum. All` | `these, based on the common features` |

**Rule.** Keep the tree semantic and the render page-faithful. Never resolve the tension by
discarding one of them. Marks are character offsets into the whole body, so a fragment must
clip and re-base them; a mark spanning the break survives on both sides.

### Three more fixed in the same pass

- **A heading prints once, where the book prints it.** Every open heading was re-emitted at the
  top of each new page so a page never opened with orphaned prose. NCERT runs section 1.1 across
  pages 3–5 and prints its heading on page 3 only. The re-emit also pushed real content down and
  fed the overflow. The running head is what orients a reader mid-section.
- **A short formatted fragment must land on a word boundary.** The one superscript run on the
  Ernst Mayr page is the `th` of `20th`; scanning forward for `th` found `the` 76 characters
  earlier and rendered `<sup>th</sup>e Harvard University`. Fragments of ≤3 characters now
  require a non-letter after them.
- **Exercises are numbered consecutively — scan for the NEXT EXPECTED number.** Both regexes
  needed a sentence boundary before the numeral, and three of ten exercises have none (`6.`
  follows `Mangifera indica`, `8.` follows `(c) Species Genus Order Phylum`, `10.` follows
  `(v) Genus`). They were dropped, the split `[1,2,3,4,5,7,9]` had gaps, so the whole block was
  left unsplit and rendered as one run-on paragraph with no numbers. Looking for `6.` only once
  `5.` is found removes the ambiguity entirely — `1.7-1.8 million` cannot match, because by
  then the scan wants a different number. Both editions now yield complete runs (1–11, 1–10).

### And the measurement that explained "the content does not fit"

`fit_factor` computes a page's height from the **book's own** measured line counts and pitch.
When it says a page needs 142%, it is not saying the type is too big — it is saying the text
block we give it is smaller than the book's. The design declared 610pt; measured across 81
pages, NCERT sets 643pt typical and 662pt at the deepest. We were 2.5–4 lines short **per
page**, then shrinking the type to hide it. `code/measure_text_block.py` reports this for every
book design; four of twelve were short.

**Rule.** When a derived number looks wrong, check its inputs before adjusting its output.

---

## 5 · The architectural fact

Two external reviews, on two different chapters, reached the same conclusion independently, and
it is correct:

> Keep **two linked representations** — a semantic chapter tree for reading and search, and a
> page-layout representation for PDF-faithful rendering. The pipeline currently tries to
> recover the second from the first *after* the layout information has been discarded.

`char_ranges` is the prerequisite and now exists, and §4b is the first half of the fix: the
render breaks paragraphs where the book breaks them. Figures and marginal content are now
**placed from their measured boxes** rather than floated, which reproduces multi-panel grids
(Figure 1.3's four photographs are two measured crops side by side, and floating them stacked
the columns and cut the last photograph in half) and puts rail content in the rail.

What remains is the opener templates — the unit opener's curved panel, display type and
seahorse, and the chapter opener's large blue title — which need the measured artwork and A2L
on those pages. **Only a MEASURED box may be used for placement**: an estimated one is a
reading-order guess and would place content confidently in the wrong place, so those still
flow.

---

## 6 · Working rules

- **`../.venv/bin/python`, never `python3`.** System python is 3.6 with an ASCII default and
  truncates these files at the first non-ASCII character.
- **Verify a claim against the data before acting on it** — including a claim in this file, and
  including your own earlier analysis. Both external reviews were ~95% accurate; the parts that
  were wrong would have sent me to rewrite working code.
- **`code/check_chapter.py` runs at the end of every build.** Adding a defect without adding
  its check means the next person ships it again. The reason an external reviewer found 60
  things while the build reported 0 is that the build only checked what I had thought to check.
- **Deterministic checks are half the gate.** `a2v-extraction-verifier` (data vs page images)
  and `a2r-render-reviewer` (render vs page images) catch what no rule can: a cropped diagram,
  a heading at the wrong level, a mark on the wrong word. Both halves are required.

---

## 7 · The two renderers — how layout gets to "exact"

The question "how do we make the layout 100% accurate" has a known answer, and both external
reviews pointed at it. Industry practice splits PDF→HTML into two incompatible goals:

> Visual/pixel-perfect approaches output one absolutely-positioned div per text run and look
> nearly identical to the PDF. Semantic/reflow approaches output headings, paragraphs, lists
> and tables, but only approximately match the original layout.

We had been trying to get the first out of the second. Now there are two renderers over **one**
`chapter.json`:

| | `render_from_tree.py` → `chapter.html` | `render_exact.py` → `chapter-exact.html` |
|---|---|---|
| lays out by | reflowing the semantic tree | placing every measured box |
| good for | reading, search, translation, PYQ citation, reflow | looking exactly like the book, print |
| can drift? | yes — reflow depends on the reader's font metrics | no — nothing is laid out, only placed |
| needs | the tree | a **measured** box for every node |

They stay in step because both read the same boxes and the same `char_ranges`.

**`render_exact.py` refuses to place an `estimated` box.** Placing a reading-order guess at
precise coordinates is worse than not placing it: it is confidently wrong. A chapter built from
a scan with no A2L read therefore renders nothing there, and the page says so.

### What actually makes placement exact

Not font matching — **measured line metrics**. `extract_page_layout.py` measures every block's
`line_count` and `line_pitch_pt`, and `build_chapter_json.py` was carrying the pitch and
dropping the count. Everything downstream then fell back to guessing "about 62 characters to a
line" from the character count — and that guess drives `fit_factor`, which decides whether a
page overflows and how far the type is scaled. So **every page's type size was being set from
an estimate when the real number had been measured two steps earlier and discarded.**

The guess was not close: a 26-character paragraph that the book sets on 2 lines was guessed at
0; a 1321-character block set on 19 lines was guessed at 21. With the real numbers a block's
printed height is `line_count × line_pitch_pt` exactly, the exact renderer sets `line-height`
to the measured pitch, and Class 11 ch01's last `PAGE_TIGHT` warning disappeared on its own.

**Rule.** Before improving a heuristic, check whether the thing it estimates is already
measured somewhere upstream and being thrown away. Twice now it was.

---

## 8 · Markdown is a deliverable, not a by-product

`chapter.md` is what a person is handed. It has no CSS to hide behind, so every content defect
is visible in it — and several defects that *looked* like HTML styling problems were content
defects all along. A reviewer's standard, which is the right one:

1. every source paragraph present **once**, no repetition
2. every sentence continuous — **a figure or caption must never interrupt one**
3. headings, lists, questions and sub-questions keep their structure
4. captions separate from lesson text, linked to the right figure
5. scientific names, symbols, numbers and meaningful emphasis preserved
6. tables keep every cell and its row/column relationship
7. every diagram present as a verified asset or a faithful equivalent
8. source wording preserved; source typos handled explicitly, never silently "corrected"

### What was wrong, and the rule

- **A numbered list held one item containing rules 1–3, and then rules 2 and 3 again.** The
  extractor had both the run-on block and the split blocks and kept both, so a reader saw rule
  2 twice. Fixed by the same consecutive-number scan the exercises use, plus a dedup.
  → *When two representations of the same content arrive, pick one. Keeping both is a defect,
  not redundancy.*
- **`- 1.` is not an ordered list.** It prints a bullet in front of a numeral. The number is
  the list marker; `ordered` is now a property of the node.
- **Splitting a node must re-base its marks, not rebuild its text.** `body_md` is *derived*
  from `(body, marks)`. Cutting `"4. "` off the front shifts every offset by three characters,
  and rebuilding `body_md` from the plain body silently dropped every italic in the list —
  `*Mangifera indica*` came out upright. → *Never regenerate a derived field from a stale one.*
- **Letter-spaced captions reach the text layer as `c a t e g o r i e s`** — not a word in any
  search index. Collapsed.
- **`-196⁰C` uses a superscript zero, not a degree sign.** It is not a temperature.
- **`pollinators.You'll`** — a missing sentence space welds two sentences together.
- **`reprint Reprint 2026-27`** — the header added a word the imprint already carried.

### The ordering bug worth remembering

Two passes — the `belongs` tag and the sub-part split — were placed **before**
`_split_exercise_questions`, the pass that *creates* the question nodes they read. Both
silently did nothing for days: walking a tree that does not yet contain the nodes you are
looking for is not an error, it is a no-op. The `belongs` tag left five questions untagged and
the sub-part split found zero questions.

→ **A pass that reads a node kind must run after every pass that can create one.** When a
transformation appears to have no effect, check its position in the sequence before checking
its logic.

---

## 9 · Absolute positioning does not forgive duplication

The exact renderer's first version was *worse* than the reflowed one, and every fault was the
same fault: **one box, one fragment.**

| defect | cause |
|---|---|
| the nomenclature list printed 4× per page | the node's whole body drawn into each of its 4 boxes |
| page continuations appeared on both pages | same — the fragment was never cut to the box |
| all ten exercises stacked at one position | children inheriting the parent `exercises` node's single box |
| seven black rectangles over the text | `fill` is the measured **ink**, painted as a background |
| the table became a run-on sentence | `table_grid` ignored; in a taxonomy table the row/column relationship *is* the content |
| headings lost `1.2.1` | section nodes keep `number` and `title` separately |

In a flow, drawing something twice looks like a repeat. In absolute positioning it stacks in
place, often invisibly. So the rules are:

- a **list** prints one item per box (4 boxes + 4 items is the extractor having measured each)
- a **paragraph split across pages** prints its own `char_ranges` slice in each box
- anything else prints **once**, at its first box — an unattributable box is better left empty
- nodes **sharing** a box are given successive slices of it, weighted by their length
- a `fill` may only be painted if it is a **light** tint; dark means it is ink

---

## 10 · Only an agent that reads the page image can recover artwork

Two of Class 11 ch01's most important images existed nowhere in the pipeline's output, for two
different reasons, and **neither was recoverable without `a2l-layout-reader`**.

**Figure 1.1, the taxonomic hierarchy flowchart.** `cut_figures.py` crops EMBEDDED IMAGE
BLOCKS. A diagram drawn as vector paths is not an image block, so there was nothing to cut, and
NCERT draws most of its flowcharts and labelled cross-sections that way. The figure node
reached `chapter.json` with a caption, a number, and no artwork — and worse, carrying the
CAPTION's box, which is one line tall. Cropping that box gives a 7mm sliver, which an earlier
build shipped. A2L measured the real artwork at `[0.128, 0.19, 0.362, 0.496]` on its
pale-yellow panel; `crop_vector_figures.py` renders that region out of the PDF.

**The Ernst Mayr portrait.** The only crop containing it was a scan of the WHOLE page —
portrait, caption and every word of the biography. Drawing that would print the biography
twice: once as live text, once baked into pixels underneath. Dropping it is correct, and it
takes the photograph with it. There was no figure node at all, because a photograph on a page
whose text layer describes only the prose produces no block. A2L measured the portrait at
`[0.127, 0.383, 0.394, 0.636]` with its caption as a separate box, and that measurement is the
only record that the photograph exists.

**Rules.**
- A figure node's box is frequently its CAPTION's box. Prefer A2L's measured artwork box, and
  write it back onto the node — cropping the right region while leaving the node pointing at
  the caption makes the renderer place the full diagram into a one-line slot.
- A box shorter than ~24pt is a caption line, not artwork. Never crop it.
- When A2L measures a figure the tree has no node for, CREATE the node. The measurement is
  evidence the artwork exists; discarding it loses the artwork permanently.

## 11 · Two more renderer traps

**`height:auto` ignores the box.** `.fig.placed img{width:100%;height:auto}` keeps the file's
own aspect, so a 289×725 crop placed in a 41×53mm box rendered 104mm tall — double its box —
and every figure on the Class 12 pages overlapped the next and ran off the sheet. Use
`object-fit:contain` inside an `overflow:hidden` box: the artwork fits its measured rectangle
undistorted, and a crop whose aspect disagrees with its measurement can never spill again.

**One page, one bucket key.** A page that prints a folio is keyed by the folio; one that does
not is keyed by its file. Mixing them splits a page in two: Figure 1.1 carried `page_file: 008`
and no folio, so it opened a second sheet `f008` beside page 8's own `p8`, and a 9-page chapter
rendered 10 sheets. Resolve the file to its folio before bucketing.

**And the type must fit the box it was measured in.** A title given a flat 24pt inside a box
measured for the book's own setting wraps to three lines and spills over whatever is positioned
beneath it — absolute positioning gives a block no room to push its neighbours away, so it
simply overlaps them. Box height and printed line count are both measured, so the size that
fits is arithmetic: `(box_height / line_count) / leading`.

## 12 · The exact render, compared page by page with the book (BIO11L ch01-03)

Every item below was found by setting `chapter-exact.html` beside the PDF page and was fixed in
the code, so it applies to every chapter built after it. `run_chapter.py` now writes
`chapter-exact.html` on every build; it used to be a separate command, so a rebuilt chapter
could carry a stale exact page or none.

| what shipped | why | rule now |
|---|---|---|
| Every title blue serif; the unit opener is near-black AvantGarde | colour and face were chosen by node KIND in the stylesheet | `ink`, `print_font`, `print_size_pt` are measured per node and win (`_typography`) |
| `UNIT 1` wrapped, its `1` printed on the subtitle; chapter titles over the first paragraph | the size was fitted from box height; a substitute font wraps a one-line title | measured size; one printed line stays one line; book's own line breaks (`line_starts`, matched on letters so small caps work) |
| Paragraphs a line long, last line over the next block | Georgia fallback is wider; the clone font's space is 3.36pt, the book's justified gap 2.64pt | embed TeX Gyre Bonum/Adventor (glyph widths measured equal to Bookman Light); `word-spacing:-0.7pt`; `_FIT_JS` tightens a block to its measured `lines x pitch` |
| Unit opener page bare white | every full-page ground image was excluded | a ground is cut when it is not a flat tone, by xref, at its unclipped bleed rect, de-duplicated |
| Figure and table captions missing from the page | only the artwork box was placed | `caption_box` kept on the node and drawn; table caption set above its grid |
| Exercises ran over the imprint | question nodes lost the block's size and pitch | questions inherit `_TYPO_KEYS`; inline sub-parts stay on one line (`parts_inline`) |
| Table 2.1 printed twice, cells over the grid | the extractor's table region stopped early; 23 cells stayed loose nodes | with an A2S grid, loose cells inside the table area are absorbed (`_absorb_table_cells`) |
| Numbered list run together, rule 4 missing from the next page | 4 items, 2 boxes: all drawn in the first | items distributed over the boxes by measured lines, one hanging-numbered row each |
| Prions and Lichens paragraphs dropped | one text-layer block, three A2 paragraphs; the join kept the first | split on measured line boxes (`_claim_followers`); the reverse case merges (`_claim_absorbed`) |
| Figures 2.1, 2.3, 2.6 printed as bare labels, no artwork | one black path at the watermark's rect touches every drawing; clustering fused the page into one blob, then dropped it | skip watermark-sized paths; only prose (>42 chars) can veto a cluster; one caption takes its whole row/grid of clusters |
| Figure 3.2's vector thalli lost beside its scanned mosses | the caption was already 'used' by the image | a drawing touching an image figure grows it -- unless that would overlap another panel, then it is its own panel |
| A label spanning two panels (`(d) (c)`) merged three figures | label absorption grew one box across its neighbours | a label may not make its figure overlap another |
| Caption and paragraph text printed twice, once inside the crop | crops are renders of a region and reached into neighbouring text | `_trim_figures_from_text` pulls the box clear of any remaining text by the crop pad |
| Paragraph set around a figure ran over its caption | a block was flowed as one rectangle | every printed line placed at its measured box (`line_geom`); flow only where a line cannot be matched |
| Exercise 7 lost its arrows (`Species -> Order -> ...`); the Summary kept text-layer text | the layer lists the Summary paragraph before its heading; in-order alignment left both blocks unmatched, and the book DRAWS the arrows | unmatched blocks are re-paired by content, any order (`_pair_out_of_order`) |
| The line holding `20<sup>th</sup>` printed over the next line | a browser grows a line box to fit a superscript | `sup,sub{line-height:0}` |
| `categories/` printed as `categories` + `/ranks` | the line-start rule pulled any punctuation onto the next line | only opening brackets and quotes move to the next line |
| **Text cut off**: a line stretched with half its words, the next run off the sheet | a line's start matched a repeated word (`pteridophytes`) earlier in the paragraph | the occurrence nearest the expected position wins, and every placed line must hold the letters the book printed there, else the block flows; a line that still overflows is tightened, never clipped |
| Exercises run off the right edge | a node with no measured `line_count` was treated as one line and forbidden to wrap | `nowrap` only for a MEASURED single line |
| Figure 3.1 caption read `(a) ... Figure 3.1 Algae :` | lines grouped by a 3pt baseline bucket, and a row straddled its edge | rows grouped by vertical overlap (`_line_rows`) |
| Figure 3.5 caption began `(b) (a)` | panel labels share the caption's text block | leading label-only rows are split off and join their panels |
| Figure 3.3 panel (a) had no label | the `(a)` is drawn as vector outlines, not text | small drawn marks next to a figure join it (`_absorb_drawn_marks`) |
| Caption and table-cell genus names upright | only caption text kept; A2S cells are plain strings | `caption_marks`, `cell_italics` |
| Match table run-on, then printed twice | A2S had the table but no element was matched to it; then the merged cells became its caption | `_table_from_cells`; merged cell text is cleared |
| `N2-fixing` without its subscript | the `2` is its own line object, measured against itself | sub/superscripts judged against their printed ROW |
| Figure 2.5's three pictures shipped as ONE crop and one CDN link | a figure was one image whatever it printed | lettered panels measured from the PDF (`_find_panels`): one crop, one JSON entry, one HTML image, one MD line and one CDN link each; split only when >=2 letters, each claims a picture, labels included and no overlap -- otherwise the figure stays whole |
| (i)/(ii)/(iii) steps printed as one run-on paragraph | a list with ONE measured box was drawn as one joined body | every list item is its own row with a hanging marker (`1.`, `(i)`, `(a)`) |
| Agent steps found no PDF, every check failed | the runner still read `inputs/ncert/` and `scripts/checks/` after the split | `iter_ncert_files` also walks `source_pdfs/`; checks load from `code/checks/` |
| `Class -- Cyclostomata` printed five times | fake bold: the PDF draws the text 5x, offset <0.4pt | overprinted copies collapse to one bold line (`_drop_overprint`) |
| `...Urochordata or Tunicata...` swallowed into Table 4.1 | the table grew down to any block within 26pt | a block reaching past the table's column band, not starting at its left edge, is not a row |

**Rule.** A render is checked against the page image, not against its own data. Every row
here passed `check_chapter.py`.

## 13 · BIO11L ch02 audited against the PDF, all three deliverables (2026-10-23)

An external audit of `chapter.md` found two defects; comparing the PDF, the JSON, the Markdown
and the printed exact render page by page found sixteen. Text was word-for-word right and
italics were complete -- every defect was structure, typing or placement.

| what shipped | why | rule now |
|---|---|---|
| Table 2.1's Animalia column printed again under the table (MD) and over the grid (HTML) | `_absorb_table_cells` ran once; the column sat past the table box's FIRST right edge | absorb to a fixpoint -- each pass widens the box |
| The QR code a captionless "figure": drawn twice, top of the MD, filed under viruses | the embedded image became a figure as well as `qr code` furniture | a captionless figure on a furniture box is dropped (`_drop_furniture_figures`) |
| `Figure 2.5 Fungi: (a) Mucor`, then `- (b) Aspergillus (c) Agaricus` inside 2.3.2's paragraph | the caption's 2nd line opens with `(b)`, so it was typed a list | a label-led block on the caption's last line is caption (`_absorb_caption_tails`); the stitcher steps over it |
| Sentences cut by Figures 2.3 and 2.6 (`legume` / figure / `roots, etc.`) | the figure sat between the halves in reading order | stitching steps over figures and captions |
| `The three-domain system...` a side `box` | side-note test was left edge + smaller size; a recto's measure starts at x 0.10 | a rail note is also narrow (< 0.40 of the sheet) |
| `2.6 VIRUSES, VIROIDS, PRIONS AND LICHENS` in capitals | the small-caps detector rejected the comma in `IRUSES,` | punctuation allowed inside small-caps spans |
| `CHAPTER 2` missing, title in capitals | A2's title block replaced the layer's true-case two-line element | `_restore_title_lines`: one node per measured line, layer's case |
| Figure 2.4 one combined crop and CDN link | images (b) and (c) overlap by 2pt; clustering fused them | one embedded image per printed letter seeds its own panel |
| Lettered figures linked twice (combined `image` + panels) | the whole-figure crop stayed on the node | a figure with >= 2 panels is carried by its panels only |
| Half-letters down Figure 2.4's left edge | crops are page renders; the pad reached the justified prose edge | crops are pulled clear of prose lines outside the figure |
| Panel (b) carried the top of panel (c) | sibling-stop only fired for non-overlapping panels | overlapping neighbours part at the middle of the overlap |
| `karyogamy` plain in list item (ii) | layer runs covered item (i) only, A2 listed no bold terms | list items take bold/italic from PDF spans inside the list's box |
| Page 12 continuation reflowed one line long, over the next paragraph | only single-page paragraphs got `line_geom` | `frag_line_geom`: each page-break fragment placed at its own measured lines |
| Table 2.1 drawn 50mm short of the book | rows at minimum height | a tinted grid takes its measured depth |
| `(Figure 2.5a)*, Rhizopus*` | the italic run began with `, ` | comma and semicolon stripped from an emphasis run's start |
| 48 passages all holding the same text, node ids that do not exist | ch02's A3/A4 used the block-number join | A3/A4 re-run on the finished tree (`structure_inputs.py`) |
| Figure 2.1's four bacteria (Cocci, Bacilli, Spirilla, Vibrio) one crop and one link | no `(a)` letters, so the lettered panel search gave up | `_named_panels_from_pdf`: drawings named beneath on one baseline become panels (`key` a,b,c names the file) |
| The green foot strip missing on all 13 sheets | design key is `footer_bar`; the renderer read `footer_band`/`foot_band`, ordinary pages only | `footer_bar` drawn on ordinary and chapter-opener pages |

**CDN.** The upload API names a file `<stem>_<ddmmyyyy>.png`, so a same-day re-upload of a
changed crop reuses its URL, and CloudFront keeps serving the copy it cached first (query
strings are ignored). Verify each URL's bytes against `image_sha256` after a re-upload.
A changed crop the map already knows now goes up as `<stem>-<sha8>.png` (`cdn_publish.link`),
so it gets a URL that has never been cached.

## 14 · BIO11L ch03: every lettered figure split into its own CDN links (2026-10-23)

Figures 3.1-3.3 shipped as one combined image each; 3.4 and 3.5 were already split. Each
failed a different way, and each fix is general:

| what shipped | why | rule now |
|---|---|---|
| Figure 3.2's crop printed two lines of body text above it | `apply_agent_figures` took the WATERMARK image into the figure's box | the watermark is never one of a figure's pictures |
| Figure 3.2 whole (4 letters, 4 pictures) | the label `Antheridial branch` joined the nearest LETTER, (b), so (b) reached into (d) | a leftover piece joins the picture it lies against, or a letter if one is nearer |
| Figure 3.3 whole | `(d)` 224pt below the Equisetum was scored "beneath" it and took (b)'s picture | "just beneath" means within 40pt (also splits ch04 Figure 4.19) |
| Figure 3.3 whole | its `(a)` is drawn as paths: 3 text letters, 4 pictures | one absent letter of a..last + one unclaimed picture-sized piece = that panel |
| Figure 3.3 (a) cut without its letter | the drawn `(a)` is 9pt; clusters under 12pt were dropped | panel clustering keeps clusters down to 6pt |
| Figure 3.1 whole | ONE scanned picture, letters painted into the pixels | `_panels_from_raster`: split the picture's ink, take it only if the drawings fall into exactly the caption's rows (2,3,2); each panel is cut from the picture with only its own pixels (RGBA), since neighbouring boxes overlap |
| `reach *a* height`, chlorophyll's `a` plain | a short fragment matched the first free-standing `a` | a fragment of <= 3 chars is placed by the two words printed before it |
| `gemma cell in Marchantia` plain | A2's block of exercises 1-4 kept only exercise 1's layer runs | absorbed layer blocks bring their runs |
| `*Chara (*Figure 3.1a)` in the MD | the book sets the `(` italic; `*` cannot close after `(` | MD emphasis is trimmed off spaces and brackets; JSON marks unchanged |

## 15 · BIO12L ch01: built from a printed copy, rebuilt from the official PDF (2026-10-23)

The first build used `Chapter_1 (2).pdf`, a **"Microsoft: Print To PDF" re-print**: A4, every
page flattened to pictures, **0 characters of text** on all 23 pages. Everything the pipeline
measures came back empty, so it guessed: a near-full-page picture of each printed page was
filed as "header art" and drawn under the live text (every line printed twice), one page-19
crop was pasted on five pages, 46 of 55 figures were page slices, title and folios were blank.
**Rule: a chapter is built only from the official NCERT file** (`ncert.nic.in/textbook/pdf/
lebo1NN.pdf`; PageMaker -> Ghostscript, real fonts, text on every page). Check `get_text()` is
non-empty before running anything.

The existing A2/A2S reads were kept: the print had placed each book page 1:1 at the sheet's
top-left (registration 0.82-0.97 on all 23 pages, offset 0), so their boxes hold, and only the
page numbers shift by 2 (the official file opens with the Unit VI opener and the Panchanan
Maheshwari page). Originals are in `steps/_archive/BIO12L-ch01-a4print/`; A2L was not carried
over (it existed only to supply guessed geometry for a text-less PDF).

| what shipped / blocked | why | rule now |
|---|---|---|
| Build never finished | p014 is 1.83 M vector paths (281 MB stream), 4 min per `get_drawings`, read 6x | `visible_drawings` reads each page once; a page over 8 MB of compressed content is read as a 4pt ink grid from `get_bboxlog` |
| Figure 1.8 unnumbered | caption is 197 chars ending in `.`, typed prose | a caption is also what is SET as one: bold label run, below body size |
| Figure 1.2's caption cut after line 1 | line 2 is wider than line 1, refused, absorbed as a figure label | a continuation starts under the caption; its width is free |
| Figures 1.14, 1.15 each three overlapping crops, labels printed twice | A2 boxed each panel; the caption followed the run | a figure-block run + one caption naming as many letters = one figure, A2's boxes kept as panel hints |
| Figure 1.14 (a) missing | the fragment holding it ran off the page and was dropped as loose; the rebuild took images only | a dropped loose fragment's vector ink inside A2's box is kept |
| Figure 1.15 one group | the watermark there is 0.8400x wide; the limit was 0.84 | watermark width up to 0.86 |
| Figure 1.9 (b) held (b) and (c) | `(c)` 4pt under the box; a clipped prose line `(ii)` joined a panel | letters looked for 14pt below; label lines read unclipped, >= 60% inside |
| Any short split | -- | a split giving fewer panels than the caption names is refused |
| Summary/exercise ornament shipped as figures | narrow strip A2 never boxed | an unboxed figure < 0.12 of the page wide is `ornament` furniture, drawn as page art |
| `CAPTION_IN_PROSE` on `Figure 1.2a shows ...` | the check took a sentence for a caption | a caption label followed by a verb is prose |

The relaxed caption join also completed five truncated Class 11 captions (Figures 2.5, 4.8,
4.10, 4.14, 5.12); ch04 and ch05 were rebuilt and re-published. ch03 rebuilt identical.
Still one image each (no safe split found): 1.2, 1.7, 1.8, 1.11, 1.13.

## 16 · BIO12L ch01 against the book, page by page: colour, decoration, type (2026-10-23)

The owner compared the exact render with the PDF and asked for it to match exactly -- colours
included -- and for every fix to reach the JSON and Markdown too. What differed, and why:

| what shipped | why | rule now |
|---|---|---|
| Whole page 21.6pt right, 3.2pt down; edge art at x +0.038 | a crop offset onto the 612x784 Class 11 sheet, while the sheet drawn is the PDF page's own size | a page of another size is its own sheet: offset 0 |
| Opener: title lines on green boxes, no full green panel, no orange band, no peach contents box; no summary box or caption tints anywhere | the book's panels are VECTOR shapes; only images were cut as art and the design drew Class 11 bands | `pages[].decor`: measured panels/bands/boxes/rules (fill, stroke, width, radius) with the PDF's paint order `z`; art carries `z` too; the render draws both in that order and skips the design's bands, tab and foot bar on a measured page |
| Leaf motif showing on the opener | the green panel is painted OVER the header picture; order was lost | decor and art drawn in `z` order |
| Contents rail one run of blue 8.6pt text | Class 11's CSS | `contents_rail[].items` (number, title), `indent_pt`, `style` (face, size, colour) measured; MD one bullet per entry |
| Running head large serif | fixed CSS | `pages[].header_style` and `folio` measured; drawn in that face, size and colour |
| `1.2.1 Stamen, ...` missing | it opens its page at y 0.108, read as the running head | a numbered bold line at the top is a heading |
| `1.1 FLOWER - A FASCINATING ...` lost its small caps | the en dash in a span failed the small-caps test | dashes allowed in small-caps spans |
| Figure 1.8 / 1.5 captions printed twice | A2's box takes in the caption; the crop is a render of the box | a figure is cut back at a caption it sits on (overlapping > half the caption's width) |
| Figure 1.5 labels cut to `les`, `cus` | the labels are outlined glyphs left of A2's box | a figure grows over small drawn shapes within 6pt, repeatedly (a leader line brings its label); never a shape inside another figure |
| Bold on the wrong `Autogamy` | fake bold drawn as 4 copies of the word plus the whole line; one copy survived | a copy of a line's START at its origin is the same ink: dropped, the line's first characters bold |
| Italic activity prompts upright | multi-line italic runs over 120 chars were never placed | formatted runs up to 800 chars are placed |
| Opener contents box missing from decor | its rounded corners are 8 curve segments | a rounded box (<= 8 curves, <= 16 segments) is decor |

Class 11 ch03-ch05 were rebuilt after each change: figures, boxes, panels and italics unchanged.

## 17 · BIO12L ch03 (Reproductive Health): first build, checked against the book (2026-10-24)

Built from the official PDF (10 pages, PageMaker -> Ghostscript, 568.8 x 777.6 pt). The October
A2 reads matched the file page for page (99-100% word coverage) and passed today's A2 check. The
five pages whose reads predate today's brief (opener, figure pages, summary, exercises) were
re-read; the replaced reads are in `steps/_archive/BIO12L-ch03-old/`.

| what shipped | why | rule now |
|---|---|---|
| The IUD paragraph (p044, runs on to p045) missing from JSON, MD and page | one layer block held two A2 paragraphs; Figure 3.2 and its caption sat between them in A2's order, so `_claim_followers`' chain broke | an unclaimed paragraph goes to the nearest EARLIER matched block holding its opening words |
| `BIOLOGY` a content box on the Exercises page | the layer filed the running head and the 30pt `EXERCISES` as one block | `_split_head_from_title`: a small first row in the head zone is its own block |
| `CHAPTER 3\nREPRODUCTIVE HEALTH` one node | layer has two title elements; A2 one heading; the join merged them | `_restore_title_lines` also restores several title elements, in the printed case |
| Figure 3.4 (b) before (a) | the tubectomy drawing starts higher; reading order is top-then-left | `_order_lettered_siblings`: adjacent same-numbered figures in caption-letter order |
| `**Figure 3.1(a**)`, `**(IUDs**)` | trailing `)` trimmed off every mark | a bracket the mark itself opens is kept (`runs_to_body_marks`) |
| PAGE_OVERFLOW on p046 (needed 65%) | the 45-line side note in the rail was summed into the text column | a measured side-rail node is out of the flow (`fit_factor`) |
| 12 exercises stacked into the top of p050 | every question carried all 16 boxes of the list | `_distribute_question_boxes`; the questions group spreads over its measured depth; sub-part labels hang |
| `4 45` folio tab on p045 | Figure 3.4 (b)'s rectangle covers the tab corner; the tab decor was dropped and the crop drawn over it | decor touching the trim is never "inside a figure" (d0); edge decor over a figure draws above it |
| A figure growing over the folio tab | -- | shapes touching the padded page-number box are never grown over |

Still open: the contents box's grey under-bar and the orange double rule under the exercises
are not in `decor`; the 3.1 heading's second line is not hung; trailing `?` of an italic
question is set upright (by the trim rule).

## 17 · Build speed and the built-in page check (2026-10-24)

| what was slow / manual | why | now |
|---|---|---|
| BIO12L ch01 build ran 45 min | the drawing cache was keyed by the path as WRITTEN; the figure join opened `source_pdfs/...`, the extractor `source_pdfs\...`, so p014's 1.8 M paths were re-read in a Python loop | cache key is the normalised absolute path; the coarse grid is vectorised (p014: 51s once) |
| every rebuild re-walked every page's drawings | no persistence | `cache/drawings/<pdf sha256>/pNNNN.vK.pkl.z` -- slim, compressed, keyed by file CONTENT; extract 177s -> 75s on a rebuild. Bump `_DRAW_CACHE_VERSION` when the reader changes |
| nobody could see where a build's time went | no timings | `run_chapter.py` prints `time  build Ns, rows, exact.html, cdn, check, compare; total` |
| page-by-page review was a hand-made script after every build | -- | `code/compare_render.py <ID>` (run by `run_chapter.py`; `--no-compare` skips): book page beside render, `qa/compare/<ID>/pNN.png` + `contact.png`, pages listed worst first by blurred grey difference and colliding lines |
| chapter.html built every time | not a deliverable | dropped (owner, 2026-10-24); deliverables are chapter-exact.html, chapter.json, chapter.md |

`apply_agent_figures` spent ~95s of 157s with PyMuPDF rebuilding a page's text page for every
figure and panel; words, text dict and image list are now read once per page (`_page_read`).
BIO12L ch01 end to end: 832s -> 423s (build 711s -> 334s), output identical.

## 19 · BIO12L ch02 (Human Reproduction) against the book, all three deliverables (2026-10-24)

The October A2/A2S reads were kept: every read matched its own page of the official file
(reprint 2026-27), recall 0.92-0.99 against the text layer, the misses being figure labels.
A3/A4 were re-run on the finished tree (10 sections, 13 subtopics).

| what shipped | why | rule now |
|---|---|---|
| Exercises 2-21 inside question 1's part (k); no Exercises section at all (also BIO12L ch01) | Class 12 sets `EXERCISES` in the title face, so it was a `chapter_title` and questions were only split under `exercises`; and an item run `(f)..(k)` could only continue with `(l)` | a `chapter_title` naming an unnumbered section, once a section has opened, is that heading; list items split on two levels -- a number continues the numbers, `(a)`/`(i)` opens parts |
| p040's `(f)-(k)` loose paragraphs; q1's `(a)-(e)` left in its body | the next page's list opened on a part with no question open; `_split_parts` skips a question that has parts | leading parts join the last question (its own body split first); each carries `page_file` + `region`, and the render draws them on that page |
| Question 1 wrapped a word a line, off the sheet | printed at its first box, `1. Fill in the blanks:` (0.18 wide) | a question prints in the union of its boxes on its page |
| Contents rail: 18 bullets, run together in the render | each number is on its own line (`2.1\nThe Male ...`) | `_rail_items` takes a bare number line; MD writes one bullet per entry from `items` |
| Tree and MD opened on a captionless picture, `CHAPTER 2` after it | A2 listed the opener art first; it was a figure node | chapter titles go before opener art; a captionless unnumbered opener figure with a crop is `pages[].art` (`opener art`, its own `z`) |
| `SUMMARY` printed twice; its three paragraphs one | A2 reads the boxed summary as one block, heading included; the join absorbed the layer's three paragraph blocks | the heading word is cut from the first child; absorbed layer blocks that each open on an 8-30pt indent are split back (`_split_absorbed_paragraphs`) |
| `Bo<sup>th</sup>` for `14<sup>th</sup>` | the `th` run follows `14` with no space, so no context words; the boundary search took `Both` | a short fragment glued to a word is placed after that word |
| `Immediately after implantation ... differentiates` lost from all three files | three short body-type lines beside Figure 2.12 were absorbed as its labels | body-size text continuing a paragraph's measure (same left edge, <= 20pt below) is never a label |
| Two peach shapes and their keylines over Figure 2.10 | painted, then covered by the picture; clip-aware reading cannot see that | `_fill_shows`: a filled panel whose colour shows on < 1/50 of its box at 36 dpi is dropped, with any outline of the same rect |
| Rounded Class 11 folio tab, no caption tint on p034/p036 | 29/26 MB pages are read coarse, so `page_decor` returns nothing | trim-touching decor borrowed from the nearest measured page of the same side; caption tint from the measured tint/caption padding |
| Running head bold on versos (BIO11L ch02, reported by e0) | style taken from the first run -- the folio | `header_style` from the first run with a letter |

Figure 2.9's crop (p034) started 0.022 of the page low: on a coarse page `vector_figures` drops
every 4pt strip inside the head zone, which took the graph's top rows. Fixed in
`apply_agent_figures` (`coarse_tops_extended`): on a coarse page only, a figure box stopping
> 10pt under A2's top extends to the coarse ink inside A2's box, never above it.

## 20 · BIO12L ch04 (Principles of Inheritance and Variation): first build, checked against the book (2026-10-24)

Official `lebo104.pdf` (28 pages: Unit VII opener, the Watson/Crick page, then the chapter at
p003). The October A2/A2S reads were made from a chapter-only file: every read matched the
official page two later (word precision 1.00) and its figure boxes registered exactly (p003 opener
art at [287,58,533,210] pt, read [287,59,536,211]), so they were renumbered +2 and kept; all 26
pass today's A2 check, misses being running heads only. Originals: `steps/_archive/BIO12L-ch04-old/`.
p001/p002 stay on the text layer, as in ch01. A3 was re-run on the finished tree.

| what shipped | why | rule now |
|---|---|---|
| Table 4.1 an empty peach box: no caption, no rows (JSON, MD, page) | its caption opens p005 at y 0.108 and was typed the running head; then Figure 4.2, 14pt away, took the rows as labels | a Table/Figure caption is never the running head; `_TABLE_RE` also takes Class 12's `Table 4.1:`; `_mark_tables` runs BEFORE `_absorb_figure_labels` |
| Tables 4.2 and 4.3 cut after two rows, the rest loose text over the grid | the watermark (furniture) and the margin folio `61` sort among the rows and ended the table | furniture, and a folio/running head outside the table's column band, are stepped over; the table stops at a LONG (> 60 chars) block whose MAIN size is larger than its rows' (Table 4.3's 10.5pt prose under 9.5pt rows; BIO11L Table 9.2's 10.5pt `PO4 3-` row stays), judged inside the column band only, and at a `*` footnote |
| Every table caption lost its 2nd line (`Mendel in Pea`, `in Human Population`, `and Genes`) | `_join_caption_lines` knew only `Figure` captions | Table captions too -- continued by a BOLD line only, so a header row never joins |
| Table 4.2's cells `I^A` printed literally everywhere | A2S writes scripts with `^`/`_` | `join_agent_special.cell_scripts`: plain cell text + `table_grid.cell_marks`; MD writes `I<sup>A</sup>`, the render sets it, italic when the layer's italic fragments hold the letters |
| `4.2.2.1 Incomplete Dominance` missing | italic, 12pt, at y 0.107: the top-of-page rule wanted bold | a numbered top line set bold OR italic, larger than body, is a heading; any 4+-level numbered line set italic/bold/larger is a heading (also BIO11L ch04 `4.2.11.3 Class -- Osteichthyes`, swallowed by Figure 4.20) |
| Both Figure 4.13s (honey bee p021, pedigree symbols p022) a third of their artwork | vector drawings with OUTLINED labels, inside a paragraph that wraps round them: the paragraph's block box vetoed the clusters | a figure measured at < 60% of A2's box is re-measured from its own ink inside A2's box (`own_ink`: paths, never one crossing a text line, never furniture or another figure's), held inside A2's box |
| Figure 4.1's column heads and Figure 4.3's parental tier cut off | drawings wholly in the head zone (top 13%) are skipped; the extension existed for coarse pages only | every page: a box stopping > 10pt under A2's top extends up to its own ink inside A2's box |
| Figures 4.1 / 4.11 boxes from x 0 | the Class 12 folio tab (trim-touching) clustered with them | `vector_figures` drops trim-touching paths -- not on a coarse page, whose grid strips run to the trim (BIO12L ch01 Figure 1.11) |
| The binomial and 9:3:3:1 lines printed twice (DUPLICATE_CONTENT) | equation gathering took only blocks <= 42 chars; longer ones were rebuilt from spans beside the original | a block >= 95% inside A2's figure/equation box whose words A2 never read as text is that box's (also Figure 4.9's `Possibility I ...` column heads) |
| `<sup>A</sup> daughter`; `both A and B types` superscript; `HbSHb<sup>S</sup>` | a glued script fragment (`Hb`+`A`, `I`+`A`) not found on its word fell through to any free-standing letter | a glued fragment is placed on its word or not at all; the search looks back over the word when the previous formatted run ended on it (`quiescent stage (G`+`0`); a run ending in its own space (`1 ` of `F1 plants`) has nothing glued after it; never on a range already placed (`G11`) |
| `Note: The strength of linkage ...` a loose paragraph under Figure 4.11 | 4.7pt under the caption; the join allowed 4pt | a caption's `Note:` line joins up to 8pt below |
| (i)/(ii)/(iii) lists set at ~8pt | `.li` rows carry a 1.2mm gap, so 3 rows overran their box and the fit script shrank them | rows at the measured pitch (box depth / printed lines) |
| beta printed like `6` | Bonum's beta is a curled form; NCERT sets Greek in a Times face | a Greek-only `@font-face` (local Times) ahead of Bonum |
| No Summary section; its six paragraphs one 3,300-character paragraph over two pages | A2 reads the box as one block, `SUMMARY` included; the join absorbed the layer's heading with the paragraphs, and the centred heading failed the indent test that splits them back | a section heading the agent block opens with keeps its own element (read before the block); its words leave the agent text |
| `Here can you tell ... yellow/green ...?` upright | the layer's italic run breaks the line after `yellow/`; the agent writes `yellow/green` | `_find_flex`: the space after a word ending `/` or `-` is optional |
| Table 4.3's note row squeezed into column A, the grid running onto the next paragraph | A2S gives it as `[text, ""]` | render: a row with text in its first cell only spans the table (centred when sentence-long) |

**Class 11 regression (built into a scratch folder OUTSIDE `data/` -- a `data/regress_*` copy
was picked up by `export_rows`' `data/*_ncert` glob and briefly overwrote live rows; peer -36
fixed `load_docs`).** BIO11L ch01-10 and BIO12L ch01-03 rebuilt into scratch and diffed against
the live JSON. Changes from these rules: BIO11L Figure 5.8 (cyme) was shipped HALF-cropped and is
now whole; Figure 5.15's top restored; ch10 G0/G1/G2 subscripts unchanged; BIO12L ch01 `3<sup>0</sup>
minutes` (a wrong superscript) now `30`; BIO12L Figure 2.10's sperm tails restored. Class 11
deliverables were NOT republished.

## 21 · BIO12L ch05 (Molecular Basis of Inheritance): first build, checked against the book (2026-10-25)

Built from the official file (`Chapter_5.pdf`, 31 pages, PageMaker -> Ghostscript, 568.8 x 777.6 pt,
the chapter at p001 -- no unit opener). The October A2/A2S reads matched it page for page (word
precision 1.00 on all 31); four pages were re-read under today's brief (p004 figure boxes, p019
continuation flag, p029 caption read as a figure, p031 exercises typed `list`) and A2S re-run for
their special blocks. Originals: `steps/_archive/BIO12L-ch05-old/`. A3 re-run on the finished tree.

| what shipped | why | rule now |
|---|---|---|
| Table 5.1 (the genetic code) a one-line box: 17-row A2S grid squeezed over the list below | the grid is vector art with OUTLINED glyphs -- no text layer -- so only the caption was measured | `apply_agent_figures`: a table covering < 40% of A2's box with no layer text under its caption takes the drawn ink in and touching A2's box (`grid_drawn`); the render prints the crop under the live caption (`caption_box`); JSON/MD keep A2S's grid |
| Griffith's `S strain -> Inject into mice` diagram at 0.8 of the book's size | the crop is the box + ~4pt pad, fitted INTO the box with `object-fit:contain` | `cut_figures` records `crop_bbox_pt`; the node carries `image_bbox`; the render places the picture at the crop's own rect |
| Central dogma diagram cut to `DNA` and its loop; `Central dogma` missing from JSON/MD | A2's box 35pt low (re-read); the label was filed in another cluster's `absorbed_labels` | printed words inside A2's box that no text block holds join the figure; an unnumbered A2S caption printed inside the art becomes the caption (`caption_in_art`, no caption box) |
| `capping`/`tailing` bold at `called as capping and tailing` as well as `In capping` | `_list_marks_from_pdf` marked the first unmarked occurrence however many the book bolds; the join placed long runs at the first copy after the cursor | list marks only while the box prints more styled copies than the items carry, placed by the preceding word; `_take_runs` places any run by its context words, and drops it if no copy is even preceded by the right word |
| `the process of splicing` bold (plain in the book) | a layer block carried another block's runs | same context rule |
| `initiator` (codon) plain; list's last two lines outside its box | the layer block ran the list's tail into the next prompt (`also act as initiator codon. (vi) ... If following ...`), the margin folio having ended the list's own blocks | `_split_leading_tails`: a layer block is cut at a measured line opening with an agent block's first words, before alignment |
| `Compare the structure of purines ...` (italic prompt, p082) missing from all three files | same: item (v)'s end and the prompt in one layer block, absorbed whole by the list | same rule |
| HGP goals (iii)-(vi) inside item (ii) | the book misprints `(iiii)`; it was no successor of `(ii)` | `_ROMAN_MISPRINT`: `iiii` sequences as iii; label kept as printed |
| Exercises one unsplit run, off the sheet | old read typed questions `list`; `1 Group ...` has no full stop | re-read (`question` blocks); the next expected number may lack its stop |
| Rail: `The Search for Genetic` (no number) + `5.2 Material`; `5.4` + `Replication` | the number's layer block took the title's turnover line | `_merge_split_rail`: an unnumbered entry on a numbered entry's row opens its title |
| `15NH4Cl`, `15N`, `14N`, `4.6 x 10^6` flat | a digit fragment had to end its word (meant for `th` in `the`); the glued word `x10` did not match the agent's `x 10`; absorbed blocks' runs were joined with no space (`normal14NH`) | digits may touch a letter (never another digit); glued words match symbol spacing and super/subscript digits; a space run between absorbed blocks |
| Red `B`/`BI`/`BIG` (RAM HAS BRE DCA P) black and partly not bold | a run glued to letters after it was refused; marks had no colour | a run may be glued AFTER (`B` + `RE`); marks carry `color` when a run's ink is neither the block's nor near-black; the render sets it; MD keeps plain bold (colour-only splits rejoined) |
| `... 3 x 10^6 base pairs. DNA fingerprinting ...` printed twice (p105) | `_norm` dropped `6` from `10^6`, so the next layer block's opening `6 base pairs` was never claimed | `_norm` folds super/subscript digits to ASCII |
| Three paragraphs shrunk by the fit script (p090, p095, p105) | `_line_geom` counted the layer's Symbol-font arrow `a-grave` and A2's `10^6` digits as letters | those are not letters to the line match; a row that is only a script's digits is dropped |
| `5.8.1 The Lac operon` upright | headings carried no marks | `title_marks` (italic only); render and MD set them |
| List item (ii) on p095 not hung | a one-item list fragment was set as plain text | a list body opening on a marker is set as hanging rows |

Still open: exercise sub-lines (Q1's second line, Q3/Q4's sequences) run inline -- the question
body is joined; Q1 prints `1.` where the book prints `1`; the `RAM  HAS  RED  CAP` letter-spacing
is single spaces.

## 22 · BIO11L ch14 (Breathing) and ch15 (Body Fluids): first build (2026-10-26)

Built from the official files (`Chapter_14.pdf`, `Chapter_15.pdf`, 12 pages each, PageMaker ->
Ghostscript; ch14 opens with the Unit 5 opener and the Corti biography). The October A2 reads
matched the text layer word for word (precision 1.00 on all 24 pages) and were kept; five pages
were re-read under today's brief as `retry1`: the unit opener (ch14 p001, chapter list not listed
as furniture), both chapter openers (title listed as the running head) and both Exercises pages
(`list` -> one `question` per exercise). The old A2S read of ch15's exercise "table" was archived
(`steps/_archive/BIO11L-ch14-15-old/`). A2L run fresh on all 24 pages; A3 run on the tree (46 and
54 passages, none dangling).

| what shipped | why | rule now |
|---|---|---|
| A lone `–` paragraph after the HCO3 paragraph (ch14 p190), in all three files | the layer set the minus of `forms HCO3- and H+` on its own line; the agent's paragraph already holds it, and the leftover became a `box` node | `_drop_layer_duplicates`: a text-layer para/box with no letter or digit is dropped (no other chapter had one) |
| A2L reported the `2024-25` foot stamp as a second `page_number` (ch14 p001-p004) | the brief has no role for it; `pages[].folio` takes the FIRST page_number element | stripped from those outputs (raw copies archived); tell A2L agents the stamp is not the folio |

Still open: Table 14.1 and Table 15.1 render as a plain, shallow grid with the caption inside the
peach box (each chapter's only table, so `_inherit_table_fill` has nothing to inherit, though the
node's own `fill` is the peach); Figure 14.2 ships whole -- its `(a)`/`(b)` are vector paths with
no layer letters, so no panel split; the colon after a bold run-in term (`Residual Volume (RV):`)
is plain where the book sets it bold.

## 23 · BIO11L ch16-19: first build (2026-10-26)

Official files (12, 13, 9, 14 pages). October A2/A2S reads kept where they matched the text layer
(precision 1.00 everywhere); openers and Exercises pages re-read as `retry1` (ch17 p012, ch18 p008
and ch16 p001 hit the content filter once and passed on retry, built from the text layer by a
script). ch19 p014, the blank NOTE page, re-read with no blocks. A2L fresh on 48 pages; A3 on the
tree. ch15 rebuilt and republished with the same fixes.

| what shipped | why | rule now |
|---|---|---|
| ch19 p251 exercise sub-rows printed over the questions; ch16/ch17 blank-line rows twice | a question whose stem is short keyed its 60-letter alignment key into `(a) ...`, matching no layer block; a `_______.` line stopped `_claim_absorbed`; `T₄` (agent) vs `T4` (layer) never matched | `_align` keys a numbered multi-line block by its first line when its full key matches nothing; claims probe without spaces and step over blank lines |
| Match tables: empty header row, `**Column I Column II**` under the table (MD), loose line (HTML) | the agent reads the header as ONE line; renderers wanted two parts | a single `Column I Column II` part splits into the two header cells (MD and exact HTML) |
| `Match **Column I** with **Column II**` bold in the stem (ch15, ch17) | agent `bold_terms` filled their first plain occurrence; the layer's bold run `Column I Column II` held both | a term inside a run the layer carried in that style is not filled |
| ch16 `(d) Uricotelism` and `(d) ADH` one row | the book prints `(d)` twice; `(d)` is no successor of `(d)` | a letter label repeated at a line start opens a new row |
| `Note` chapter-title inside Exercises (ch19) | the layer's `NOTE` survived on a page the agent found empty | on an empty agent page, layer text the agent listed as furniture is dropped |
| `**in nature**`, `**animals**` bold (ch16 p205); also ch12 p160 `(ETS) (Figure 12.4) and it is` | `_drop_overlap_copies` flagged the whole trimmed line bold | the remainder is bold only in the copy's own face (ch12 not rebuilt) |

Still open: Fig 16.4 crop cuts `Proximal convoluted tubule`; Figs 17.2, 19.3, 19.4 ship unsplit;
exercise sub-parts run inline where the book sets columns (ch19 Q3/Q5); the ch14/15 table tint.

## 24 · PHY11L ch01 (Units and Measurement): first physics chapter, and the step driver (2026-10-28)

The user supplied the official PDF (Bullzip print of the PageMaker file, full text layer) and a
build made elsewhere (zip, `__MACOSX`) that had run **A2 only**: layout 0/12 pages, A2S 2 tables /
0 equations, no A3/A4. Every display equation on pp. 5-11 came out as text-layer fragments. The
cause was not the renderer: the agent steps after A2 could not be listed for a new chapter.

| what was wrong | why | rule now |
|---|---|---|
| `run_step.py A2/A2S/A3 --list` print "none", A2L crashes | they need A2 work inputs, `ncert/blocks/<BOOK>.jsonl` and A2 statuses that nothing rebuilds | `code/chapter_steps.py prepare/list/check/status <STEP> <CID>` -- chapter-scoped, rebuilds what each step needs from the PDF, reuses the plugins and checks |
| every good A2L read "blocked" | `schemas/A2L.json` forbade `text_block`, `fill`, `page_kind`, `space_before`, `indent`, `size_pt`, all required by the brief | schema matches the brief (457/460 stored reads now pass; the 3 left use the forbidden `face`) |
| A2L's block-number test never ran under the runner | the runner passes `input_data`, the check read `blocks` | checks/A2L.py reads `input_data.blocks` too |
| A2 p007 heading matched 0% | declaring the running head `UNITS AND MEASUREMENT` dropped the layer's lone `AND` line | only a folio number or a part of a two-part stamp is a stamp variant; stopwords never (one stored read changed verdict: BIO11L-ch11-p003, already resolved) |
| every PHY11L line printed twice | the page picture (x 0.04-0.96, full height) failed `is_page_ground`'s width test, became `header art`, was cut by RENDERING the region and drawn under the live text | as tall as the sheet and > 0.85 wide is ground; a page picture inked where the prose lines are is a page raster and is never cut (`cut_figures._is_page_raster`; 46 biology page pictures unaffected) |
| physics working (`l b = ... ± 1.6%` / `= ...`) printed from the text layer | `_TEX_NEEDED` typesets only fractions/roots/arrows | physics typesets every display equation, keeps italics, aligns `\` rows on `=` (`_physics_display`); biology/chemistry unchanged |
| our drawn figures had no NCERT path | FIGP lived only in paper_extraction | NCERT FIGP: `agents/figp-figure-redrawer.md` (NCERT copy), `code/figp_bridge.py` runs paper_extraction's `physics_figure`/`figure_text`/`print_trace`/`spec_trace` in its own process (both packages are `lib`); a passing drawing is `image_drawn` (+ `image_drawn_spec`, `image_drawn_layout`), shown in exact HTML and MD, CDN-published as SVG |

Agents writing JSON through a Bash heredoc lose `\` (LaTeX becomes tab/form-feed and the A2S
check still passes) -- every dispatch now says "Write tool, never a heredoc".

Saved workflow `.claude/workflows/ncert-chapter-pipeline.js` (args `{chapter_id, pdf?}`) runs the
whole chain with one retry per step. Not yet run end to end itself -- PHY11L ch01 was dispatched by
hand through the same `chapter_steps.py` lines.

Second pass, after the user's review (page 1 rail, Table 1.1 overprint, Table 1.2 empty):

| what was wrong | why | rule now |
|---|---|---|
| A2L made physics worse (page-wide boxes, Table 1.1 over its own text, no head rule, two stray table crops) | the text layer is exact; A2L's estimates replaced it | `book_design.a2l_join()` is False for PHY: no A2L join, no A2L-box crops, no A2L agents |
| contents rail one section titled "Introduction 1.2 The ... 1.3 ..." | rails were recognised only as `side_note` (design geometry) | a left block of `n.m` entries on page 1 is the rail; numbers in their own column are paired by height; `Summary`/`Exercises` own entries; titles light, number bold (`num_b`) |
| `In earlier time scientists ...` missing (p001) | the layer filed heading + paragraph as one block | `_split_heading_from_body`: bold/coloured `n.m` rows split from plain rows below |
| Table 1.1 rows loose paragraphs, Table 1.2 empty | captions without a colon (`Table 1.1 SI ...`) never matched; a drawn table had no node | `_is_table_caption_nocolon`; a caption-only physics table stays `table` and the join grows it over the drawn ink even when A2's box starts below the caption; physics tables print from their crop, grid kept in JSON/MD |
| columns interleaved; a paragraph's other-column half joined the wrong paragraph; `As discussed above` before its heading | `collect_blocks` sorted down the page | `_two_column_order`: a page with 2+ narrow text blocks in each half is read left column then right, band by band; an absorbed block in the other column keeps its own box (`_column_continuation_cut`, `continues_from_previous`) |
| exercises 1.3-1.7, 1.9 missing, 1.8+1.10 one block, numbers black `1.3.` | `C.k` numbers typed as headings; `collapse_lists` merged the questions | past `EXERCISES`, blocks split at every `C.k` row and typed paragraphs; `C.k` items become questions with their own boxes and marks; number bold in the accent, no stop (HTML and MD) |
| no cyan rule under the running head; folio 13pt black | the rule is a 4pt FILLED bar; the split-off folio had no runs | a long thin filled bar at the head is a rule; the folio takes the head's run (unmeasured books only) |

**Every rule above applies only to books not in MEASURED_KEYS** (`new_rules` in
`extract_page_layout.extract`, `apply_agent_text`; `a2l_join`; physics-subject checks in the
render). Run over all 32 biology chapters (old vs new extraction, `bio_regress.py` pattern) the
ungated rules changed 19 approved Class 11 pages: no-colon table captions (`Table 1.1 Organisms
...`), full-height opener art typed ground, two-column order. Gated, biology content is identical.

Third pass, inline maths (PHY11L ch01 p004-p006):

| what was wrong | why | rule now |
|---|---|---|
| p005's first line across both columns; `= 2π , have a lare (infinite) number g` glued to p006's paragraph | layer scraps of inline maths stayed text-layer paragraphs and page-break stitching joined the next page to the scrap | `_rescue_inline_math_pairs`: an unpaired short layer block whose words are in an adjacent A2 paragraph (inside its box: 60%, within 40pt: 80%) is dropped; never one in an equation's box |
| a paragraph's lines set wrongly when A2 text holds words the rows lack | `_line_geom` offsets slide | physics: `_rows_hold` -- measured lines only when the rows print the fragment's words, else it flows in its box |
| both relative-error equations lost (p006) | the safeguards read `blocks`, which drops A2's text-less equation blocks; equations then fell back onto prose | equation boxes come from A2's full block list; an equation never takes A2 prose, prefers a bare line, and is set in A2's box under the sentence it overlaps |
| text-layer scraps of display equations (`-3`, `2.51 cm`, `1 v`) | MathType reaches the layer in pieces | `_drop_equation_twins` (physics): a short text-layer paragraph inside a transcribed equation's box is dropped |

Still open on PHY11L ch01 (physics render, PHY11 not in MEASURED_KEYS): `l = 16.2 ± 0.1 cm` set
below the column (A2 measured its box at y 0.96; pre-existing); inline `T = t/n` set flat; the
9.89 g equation node keeps a leftover body label beside its LaTeX.

Earlier list (first pass), for the record: Table 1.1 grid set over
its text-layer copy (p02); a paragraph crossing columns or pages laid full-width at the page top
(p08, p09 Example 1.5); A2S equations drop lead-in words ("Then,", "or,", "Actually,"); the
relative-error lines (p06) drawn beside their typeset twins; equations inside Example boxes (1.3)
never deferred to A2S; running head without the 6pt cyan rule, folio black and bold; ◀ end
marker shown as `⊳`; exercises 1.11-1.17 typed as headings; PAGE_OVERFLOW on 6 pages. Not
CDN-published.
