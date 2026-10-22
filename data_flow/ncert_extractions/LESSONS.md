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
