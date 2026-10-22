# NCERT Extraction — specification and runbook

**Read this file first.** It is written so a new Claude session can run the whole flow without
asking anyone anything. Every number in it was measured off the real PDFs; where something has
*not* been measured, it says so.

```bash
cd data_flow/ncert_extractions
../.venv/bin/python code/build_chapter_json.py BIO11L-ch01     # one chapter, end to end
```

---

## 0 · The one rule

> **Geometry is measured. Words are read by an agent. Structure is judged by an agent.
> Everything else is derived from those three.**

Nothing is trusted outside what it is provably good at. The measurements behind that split are
in §3.

---

## 1 · What this produces

Per chapter, under `data/<old|new>_ncert/class_<11|12>/<subject>/ch<NN>_<slug>/`:

| file | what it is |
|---|---|
| `chapter.json` | **the truth** — the nested tree, ids, marks, sentences, boxes |
| `chapter.html` | the book page by page, opens in any browser, no server |
| `chapter.md` | the same text as CommonMark — GitHub, VS Code, Obsidian |
| `figures/` | one PNG per real figure and table, named by printed folio |
| `README.md` | what the chapter is, counts, provenance |

Plus, once per run:

| | |
|---|---|
| `data/dynamodb/` | the rows, one file per chapter, ready for the loader |
| `assets/furniture/<DESIGN>/` | header art cut **once per book** |
| `assets/fonts/` | Bookman + Century Gothic metric clones, embedded into the HTML |

`chapter.json` is the master. The HTML, the Markdown, the DynamoDB rows and the search index are
all **views built from it**. If the table is ever wrong, refill it from here.

---

## 2 · The six book designs

There are **six**, keyed by `(subject, class)` — not three keyed by subject.

| design | applies to | header | folio | foot |
|---|---|---|---|---|
| **BIO11** | `BIO11L` + `BIO11O` | pale-green band `#e1ecb6` → y63pt, grey strip `#d1d3d4` → y73.1 | white rounded tab 35×36pt on the strip | green bar `#cbdf7f` from y751.5 |
| **BIO12** | `BIO12L` + `BIO12O` | dark-green rule `#4b7336` → y31.8, brown block `#745a21` 146pt on the outer end, leaf motif | orange `#f7941d` tab bleeding off the outer edge at y613 | none, imprint only |
| CHE11 · CHE12 · PHY11 · PHY12 | — | **registered, NOT measured** | | |

**Old and new share a design.** Measured: `BIO11O ch3` and `BIO11L ch3` are identical to four
decimal places on every rectangle; so are `BIO12O ch7` and `BIO12L ch6`. The editions differ in
**content** and in the **imprint line** — never in typography.

That is why there is one `STYLE#BIO11` row for both editions, and why a renderer never branches
on old-vs-new for layout.

### The canonical sheet

Every NCERT Biology book sets the **same** text block in absolute points on a **612 × 784 pt**
(215.9 × 276.6 mm) sheet:

```
recto (odd folio)    body x  60.0 → 420.0        inner margin  60pt
verso (even folio)   body x 192.0 → 552.0        outer rail   192pt
measure                      360.0pt             identical on both
Class 11 text top y ~104pt, foot ~714pt
Class 12 text top y  ~88pt, foot ~715pt
```

The scans do **not** all carry that sheet. `source_pdfs/new/class_12/biology/*.pdf` are
568.8 × 777.6 pt — the same page with 21.6pt trimmed off each side (`60.0 − 38.4 = 21.6`, and
`612 − 568.8 = 43.2 = 2 × 21.6`). `normalise_page` measures that crop off the page's own text
block and puts every page back on the canonical sheet. Without it the new Class 12 book renders
7% narrower than Class 11 *and* narrower than its own older edition — three page sizes for one
physical book.

---

## 3 · Why the text layer is not the source of text

The PDF text layer is **excellent for geometry and for running prose** and **quietly wrong for
notation**. Both halves are measured.

**Prose — identical to the agent.** Compared block for block across 23 pages of `BIO11L` ch01
and ch03: the agent found **zero** words the text layer had missed.

**Notation — corrupts silently:**

```
'C6H12O6 (Glucose)'    subscripts of C₆H₁₂O₆ flattened to inline digits
'(CH )'                subscript digits dropped ENTIRELY
'CH OH'                the same
'OCH2' 'HOCH2' 'HO'    a structural formula shattered into fragments
```

Across the whole of `BIO11L` ch09 — Biomolecules, a chapter of H₂O and CO₂ — PyMuPDF's *flags*
reported **9 superscripts and 0 subscripts**, because it does not flag subscripts at all.

**But the information is there one level down.** Character geometry recovers it exactly:

```
'C' size 9.5  origin_y 201.6        'H' size 9.5  origin_y 201.6
'6' size 5.5  origin_y 204.8        '1' size 5.5  origin_y 204.8
```

Subscripts are 58% of the body size on a baseline 3.2pt lower. Reading characters instead of
span flags yields **53 subscripts** in that chapter and **227 superscripts** in Class 11 Physics
ch01. `char_script()` in `extract_page_layout.py` does this.

**So the agent still owns the words.** `a2-page-reader` is given the page **image** *and* the
text layer, and its brief says: copy the layer's characters where they match what it sees, read
the **image** where they do not, and **always** read the image for superscripts, subscripts, °,
′ ″ and radicals. It supervises the layer rather than competing with it. 12% of pages have no
text layer at all and are image-only.

---

## 4 · The flow

```
                     source_pdfs/<old|new>/class_<11|12>/<subject>/Chapter_N.pdf
                                            │
          ┌─────────────────────────────────┴──────────────────────────────┐
          │                                                                │
  GEOMETRY  [script]                                         WORDS  [AGENT, per page]
  extract_page_layout.py                                     A2   a2-page-reader
    bbox · font · colour · size                              A2S  a2-special-transcriber
    printed line pitch                                       A2B  a2-bold-marker
    printed folio · recto/verso                              A2I  a2-italic-marker
    figure / table boxes                                     A2N  a2-notation-fixer
    furniture: ground, watermark,                            A2L  a2-layout-reader
      header art, QR                                              (image-only pages)
          │                                                                │
          └─────────────────────────────────┬──────────────────────────────┘
                                            │
                        JOIN  [script]  join_agent_text.py
                        difflib alignment · agent text → measured box
                        every node stamped  source · qa
                                            │
                        CROPS [script]  cut_figures.py
                                            │
          ┌─────────────────────────────────┴──────────────────────────────┐
     STRUCTURE [AGENT]                                         TREE [script]
     A3 a3-passage-splitter                                    build_chapter_json.py
     A4 a4-subtopic-writer                                       → chapter.json  (TRUTH)
          └─────────────────────────────────┬──────────────────────────────┘
                                            │
            ┌───────────────┬───────────────┼───────────────┬──────────────┐
      chapter.html     chapter.md      export_rows.py   upload_assets.py  search index
                                       data/dynamodb/    CDN urls
                                            │
                                   load_to_dynamodb.py
                                            │
                              REVIEW [AGENT] a2r-render-reviewer
```

---

## 5 · Run it

### One chapter
```bash
../.venv/bin/python code/build_chapter_json.py BIO11L-ch01
```
Prints how many pages used agent text. **If it says fewer than all pages, the chapter is not
finished** — dispatch A2 for the rest before trusting the output.

### Shared furniture, once per book
```bash
../.venv/bin/python code/build_furniture_assets.py BIO11 BIO12
```
Cuts the header art once per book and side. **Do not cut furniture per page**: measured, one
chapter produced 25 crops of a single header and 8 of them were broken 295-byte near-empties, so
a third of its pages carried a different header from the rest.

### CDN
```bash
export ARIVIHAN_TOKEN=…  ARIVIHAN_USER_ID=…      # from auth/verify-otp
../.venv/bin/python code/upload_assets.py --furniture BIO11
../.venv/bin/python code/upload_assets.py --chapter BIO11L-ch01 --dry-run
```
Writes `image` (CDN url) + `image_sha256` onto each figure node, keeping `image_local` as the
fallback. Re-running skips anything whose bytes have not changed.
**The token is never committed** — it is read from the environment.

### Load
```bash
../.venv/bin/python code/load_to_dynamodb.py --chapter BIO11L-ch01 --dry-run
../.venv/bin/python code/load_to_dynamodb.py --all --table ncert_content
```

---

## 6 · The agents

Under `agents/`. Dispatch one per printed line of `run_step.py <STEP> --list`.

| step | agent | item | gives |
|---|---|---|---|
| A1 | `a1-book-registrar` | a book | the register row |
| **A2** | **`a2-page-reader`** | **one page** | **the words** — image + text layer |
| A2S | `a2-special-transcriber` | a table/equation/figure | its real content |
| A2B | `a2-bold-marker` | a page | which substrings are bold |
| A2I | `a2-italic-marker` | a page | italic — *every species name* |
| A2N | `a2-notation-fixer` | a page | sub/superscripts backfilled |
| A2L | `a2-layout-reader` | a page | geometry where there is no text layer |
| A2R | `a2r-render-reviewer` | a rendered page | render vs the real book page |
| A3 | `a3-passage-splitter` | a section | blocks grouped into passages |
| **A4** | **`a4-subtopic-writer`** | **a chapter** | **named subtopics + their passages** |
| A5 | `a5-passage-linker` | a passage | links across the chapter |
| A6–A9 | pairing, diffs, change log | | old ↔ new |

**Coverage today, Biology (1,118 pages across 71 chapters):**

| | |
|---|---|
| A2 page reads | **597 pages · 42 of 71 chapters complete** |
| A3 passages | 487 |
| A2S | 376 |
| **A4 subtopics** | **48 — the biggest gap** |
| A2N · A2B | 15 each |
| A2I · A5 · A6 | **0 — never run** |

The 42 complete chapters can be built now at zero agent cost. The other 29 need A2 first.

---

## 7 · `chapter.json` — the tree

Store the chapter as its **structure**, not as boxes on a page. A product asks for
"1.2.2 Genus, paragraph 1", never "page 7, block 4".

```
CH#BIO11-01#EN
  META                chapter row
  N#001               intro paragraph
  N#002               section  1.1 Diversity in the Living World
  N#002.001             para   ¶1
  N#002.006             list   the 4 rules of nomenclature  (ONE node, pages 4→5)
  N#003               section  1.2 Taxonomic Categories
  N#003.005             section  1.2.2 Genus
  N#003.005.001           para   ¶1          ← the Genus paragraph
  N#004               summary
  N#005               exercises
  PG#007              page row
  TERM#genus          term row
```

### Four things the tree does that a page-box model cannot

1. **A paragraph broken by a page is ONE node with TWO `boxes`.** A2 reports
   `continues_from_previous`; without it, `1.1 ¶1` ends page 3 mid-sentence at "biodiversity or
   the number and" and page 4 opens with an orphan — neither quotable.
2. **A list is ONE node holding its items.** The four nomenclature rules run pages 4→5.
3. **A figure sits after the paragraph that first names it.** Figure 1.1 is *printed* beside the
   end of 1.2.6 but *belongs* to 1.2.7. The printed spot stays in `boxes`.
4. **Furniture is never content.** The running head, folio, reprint line and the opener's
   contents list live on page/chapter rows. Left in the tree, "4 Biology" and "2024-25" turn up
   in search and read-along as though NCERT wrote them.

### A node

```json
{"id":"p_7Kq2xP","kind":"para","path":"003.005.001",
 "body":"Genus comprises a group of related species …",
 "marks":[{"from":0,"to":5,"b":true},{"from":274,"to":281,"i":true}],
 "body_md":"**Genus** comprises … the genus *Solanum* …",
 "sentences":[{"n":1,"from":0,"to":120}, …],
 "terms":["Genus"],
 "pages":[7],
 "boxes":[{"page":7,"bbox":[0.098,0.2195,0.6864,0.3392]}],
 "source":"page_image","qa":"auto"}
```

**`marks` are character offsets, not nested spans** — so one sentence can be lifted out with its
italics intact by arithmetic on its own range. A mark covers **only the word**: the text layer
runs trailing punctuation into the italic, storing `Solanum.` italic *with* its full stop.

**`id` is hashed from `(book-without-edition, chapter, tree path)`** — not from the content — so
the Hindi paragraph gets the **same** id, and the id survives a re-extraction (block numbers
shift; tree positions do not).

---

## 8 · DynamoDB

Two tables. `ncert_content` has **7 row kinds**, one partition per chapter per language:

```
BOOK#BIO11#EN      META                 book
BOOK#BIO11#EN      UNIT#1               unit   (+ UNIT#1#N#002 the Ernst Mayr box)
CH#BIO11-01#EN     META                 chapter
CH#BIO11-01#EN     N#003.005.001        node   ← almost all rows
CH#BIO11-01#EN     PG#007               page
CH#BIO11-01#EN     TERM#genus           term
CH#BIO11-01#EN     CHG#2027-28#…        change
STYLE#BIO11        V1                   the design, shared by both editions
PAIR#BIO11         LATEST#01            old ↔ new, matched on TITLE
```

Every node carries `chapter_no/title`, `topic_no/title/id`, `subtopic_no/title/id`,
`sub_subtopic_*` where the book goes that deep, and `address` — denormalised, because DynamoDB
cannot join and a product uses one row at a time.

**`grade`, not `class`. `body`, not `text`.** Both are DynamoDB reserved words.

**The pair row matches on TITLE, never chapter number.** The editions renumber: *Principles of
Inheritance and Variation* is ch4 of the latest Class XII and ch5 of the older. Looking up the
same *number* fetches *Reproductive Health* and presents it as the older edition of a genetics
page — worse than showing nothing, because it looks authoritative.

---

## 9 · Rendering — and never overflowing

A renderer fetches **three** things:

```
content   Query   PK = "CH#BIO11-01#EN", begins_with(SK, "N#")
pages     Query   PK = "CH#BIO11-01#EN", begins_with(SK, "PG#")
style     GetItem PK = "STYLE#BIO11",    SK = "V1"
```

The **style row** carries the page grid in mm, the furniture geometry and fills, the CDN urls
for the header art and fonts, and a `kinds` map giving every block kind its size, colour and
alignment. A row says `"kind":"section"`; the style row says what a section looks like **in this
book**. Same renderer, six style rows.

**Folio and page number are never content.** The page row has `printed_page_number` and
`page_side`; the style row says where the tab goes on each side. The renderer draws it.

### Content must never run off the page

1. **Measured line pitch** on every node — the pitch the book actually prints (e.g. 14.10pt),
   not a stylesheet guess. Removes most drift.
2. **A per-page `fit` factor** on the page row, computed at build time from measured line counts
   × pitch against the available column height. The renderer applies
   `font-size: calc(var(--body) * var(--fit))`. Deterministic, no JS.
3. **`overflow: "continue"`** — if content still exceeds, the page grows onto a continuation
   sheet. Losing a sentence to save a page count is never the right trade.

Hard guards: the body column is `max-width: measure`; figures are `max-width:100%`; a table
scrolls inside its own box. **Diagram width** = `min(bbox_width, measure)` — a figure can never
be wider than the measure, and a marginal figure keeps its rail width.

---

## 10 · What is NOT done

Honest list. Do not assume any of these.

| | state |
|---|---|
| **29 Biology chapters** | no A2 agent read — not built |
| **A4 subtopics** | 48 of 71 chapters |
| **A2I italic** | never run — species names rely on the text layer |
| **A5, A6** | never run — no old↔new passage pairing |
| **Chemistry, Physics** | designs registered, **not measured**; `render_chapter_html.py` refuses them without `--allow-unmeasured` |
| **Hindi** | no Hindi PDFs in `source_pdfs/`; the `#EN` key is ready for it |
| **`ncert_file`** (`kebo101`) | null — no mapping from our `Chapter_1.pdf` names |
| **`reprint` for Class 11** | our PDFs print `2024-25`, not the `2026-27` the schema targets |
| **S3 upload** | not wired; `chapter.json` is written to disk only |
| **`a2r-render-reviewer`** | never run on these renders |

---

## 11 · Rules that cost something when broken

- **Never join the two editions on chapter number.** Join on title, or on A6 once it runs.
- **Never cut furniture per page.** Once per book, or pages disagree with each other.
- **Never let the text layer supply notation.** It drops subscripts silently.
- **Never put furniture in the tree.** It reaches search and read-along as NCERT's own words.
- **Never commit the CDN token.** `ARIVIHAN_TOKEN` at run time only.
- **Never claim agent provenance a page does not have.** `source` is on every node for this.
- **Use `../.venv/bin/python`.** The system `python3` is 3.6 and truncates every file at its
  first non-ASCII character.

---

# 12 · RUNBOOK — what an agent must do, in order

Hand this section to whoever runs the next chapter. Follow it exactly; do not improvise an
order.

## 12.1 · One chapter, start to finish

```bash
cd data_flow/ncert_extractions

# plain-words form — "chapter 2, biology, old NCERT"
../.venv/bin/python code/run_chapter.py --old --class 11 --subject biology --chapter 2

# or the book-id form
../.venv/bin/python code/run_chapter.py BIO11O-ch02
```

That single command runs all eight steps and prints what each did. **Read the `agent` line.**

```
  agent     13/13 pages read by a2-page-reader, 69 blocks replaced
```

If it says fewer than all pages, the chapter is **not finished**. Go to §12.2.

## 12.2 · When pages have no agent read

`run_chapter.py` prints the page numbers. Those pages carry PDF text-layer text — good prose,
**unreliable notation**. Dispatch the reader:

```bash
../.venv/bin/python code/run_step.py A2 --list        # one line per page needing a read
```

Then, once per printed line, invoke the agent with exactly:

```
Use the a2-page-reader subagent. Input: <input path>. Output: <output path>. Do nothing else.
```

Then `run_step.py A2 --check` until it prints `DONE`, and re-run `run_chapter.py`.

**Never run two waves of the same step at once.** `--list` → one agent per line → `--check` is
not a style; it is what keeps two agents off the same file.

## 12.3 · The order, and why it cannot be reordered

| # | step | who | must come after |
|---|---|---|---|
| 1 | `extract_page_layout` | script | — |
| 2 | `a2-page-reader` | **agent** | 1 (it is given the rendered page) |
| 3 | `join_agent_text` | script | 2 — nothing to join before |
| 4 | `cut_figures` | script | 1 — needs the measured boxes |
| 5 | `build_chapter_json` | script | 3 and 4 |
| 6 | `a3-passage-splitter` | **agent** | 2 — groups A2's blocks |
| 7 | `a4-subtopic-writer` | **agent** | 6 — names A3's passages |
| 8 | `export_rows` | script | 5 |
| 9 | `upload_assets` | script | 4 |
| 10 | `load_to_dynamodb` | script | 8 |
| 11 | `a2r-render-reviewer` | **agent** | 5 |

`A4` **cannot** run before `A3`: it is handed passages, not blocks. `A3` cannot run before `A2`:
it groups block numbers that only exist once a page has been read.

## 12.4 · CDN

```bash
curl .../auth/send-otp   -d '{"phoneNumber":"…"}'
curl .../auth/verify-otp -d '{"phoneNumber":"…","otp":"…"}'
export ARIVIHAN_TOKEN=…  ARIVIHAN_USER_ID=…

../.venv/bin/python code/upload_assets.py --furniture BIO11        # once per book
../.venv/bin/python code/run_chapter.py BIO11O-ch02 --upload       # crops for this chapter
```

Writes `image` (the CDN url) and `image_sha256` onto each figure node; `image_local` stays as
the fallback. Re-running skips anything whose bytes have not changed. **The token is read from
the environment and is never written to a file.**

## 12.5 · Load

```bash
../.venv/bin/python code/load_to_dynamodb.py --chapter BIO11O-ch02 --dry-run
../.venv/bin/python code/load_to_dynamodb.py --all --table ncert_content
```

It **refuses** nodes whose `source` is `text_layer` and says how many. That is deliberate: see
§3. `--allow-unverified` overrides it knowingly.

---

# 13 · Defects found, and what each one cost

Every item here was a real bug in this code, found by measurement. They are recorded so the
same mistake is not made twice — and because several of them are invisible unless you look.

| # | defect | how it showed | fix |
|---|---|---|---|
| 1 | **Folio and running head swapped on every page** | `4`'s box bottom was 76.49 and `BIOLOGY`'s 76.43 — 0.06pt apart. Rounded to 1dp they sorted in the wrong order, so the head line read `Biology 4`. That flipped recto/verso, which drives margin mirroring and tab placement. | bucket the baseline to 3pt, then order left-to-right |
| 2 | **Summary and Exercises came out empty** | reading order was column-first, so `Summary` at y 0.134 sorted *after* a paragraph at y 0.168; the summary text was filed under *1.2.7 Kingdom* | order the tree by y, not by column |
| 3 | **Whole paragraphs rendered bold** | the agent join gave the agent's text the *first run's* flags; the first run is the bold term `Genus`, so all 479 characters became bold — 1 mark where the book prints 7, and `terms` empty | re-locate the layer's formatted substrings into the agent's text |
| 4 | **`P. tigris` split into two italic marks** | the abbreviating full stop sat in its own unformatted run | close a mark gap of ≤2 chars when it contains only punctuation/space |
| 5 | **Figure artwork and caption were separate nodes** | 6 of 13 figures had a caption with no picture and a picture with no caption | merge on page + proximity — **after** crops are attached, not before |
| 6 | **`Table 1.1 indicates…` cropped as a table** | the caption regex was case-insensitive, so a sentence *mentioning* the table matched and a block of prose was cut out as an image | match `TABLE n.m` case-sensitively — the printed caption is caps |
| 7 | **The chapter's title came out as `Unit 1`** | the title scan ran over the whole PDF, and the unit opener carries `Unit 1` at 4× body size | scan the chapter's own pages only |
| 8 | **The opener's contents rail became content** | `1.1 Diversity in the Living World` appeared twice — once as a heading, once as a stray line — and reached search | match the rail against the real headings and re-label it furniture |
| 9 | **Page-break paragraphs never stitched** | A2 reports `continues_from_previous`; the join was dropping it, so `1.1 ¶1` stayed two half-sentences | carry the flag onto the element |
| 10 | **The green chapter-opening header never rendered** | the gradient `<div>` had no `left`/`right`, so it computed to zero width — every Class 11 opener was blank white | use the page's own cut artwork; keep a `left:0;right:0` fallback |
| 11 | **The chapter title printed twice on the opener** | furniture was *rendered* from the page region, baking the title in as pixels under the live text | extract the embedded image by xref, comparing against the page-**clipped** rect |
| 12 | **8 of 25 header crops were broken 295-byte near-empties** | furniture was cut per page, so one chapter held 25 crops of one header and a third of its pages looked different | cut furniture **once per book**, choosing the crop with the most ink |
| 13 | **Content ran off the bottom of the sheet** | a fixed height with `overflow:hidden` does not "fit" — it deletes | the sheet is a **minimum**; the footer is flow content at the end |
| 14 | **Text blocks printed on top of each other** | absolute positioning plus reflow: one extra wrapped line pushes a block past the next block's top, and the error accumulates | flow the body column; keep only the rail absolute, with collision push-down |
| 15 | **9,683 "figures" in a 14-page chapter** | scanned figures arrive as thousands of zero-height scan-line strips | merge by grid occupancy, drop sub-10pt dust |
| 16 | **The watermark was emitted as artwork** | `© NCERT / not to be republished` is an image at a fixed bbox on every page | detect it, and never draw it |
| 17 | **Every older Class 11 chapter raised "no PDF"** | those files are named `4 3. Plant Kingdom.pdf` — ordinal first, chapter number second | ask `runner_core.extract_chapter_num`, the same rule the register uses |
| 18 | **0 subscripts across a chapter of H₂O and CO₂** | PyMuPDF's span flags do not mark subscripts at all | read **character** size and baseline: recovers 53 subscripts there, 227 superscripts in Physics ch01 |

## 13.1 · Still open

| | |
|---|---|
| **Vector-drawn figures are not cut** | 3 of 11 figures in BIO11O ch02 are caption-only — their artwork is vector, not an image block, so nothing was cropped. Figures 2.1, 2.3 and 2.5 are affected. |
| **~30% of nodes still carry `text_layer` text** | the difflib alignment leaves unmatched blocks on the layer's text. They are labelled, and the loader refuses them by default. |
| **`chapter.html` is a reading view, not a facsimile** | one flowing column, not one sheet per printed page. The printed position of every node is in `boxes` for anyone who wants the facsimile. |

---

# 14 · THE AGENTS WE WERE IGNORING — audit of 2026-10-22

This section exists because a large mistake was made and must not be repeated: **the pipeline
was consuming one agent out of eleven.** Everything else had already been run, at real cost,
and was sitting on disk unread while the code re-derived worse answers from the PDF.

## 14.1 · What was on disk vs what was read

| step | agent | outputs | Biology | was it read? |
|---|---|---|---|---|
| A1 | `a1-book-registrar` | 13 | 0 | no |
| **A2** | `a2-page-reader` | **1,432** | **597** | **yes** — the only one |
| **A2S** | `a2-special-transcriber` | **1,014** | **376** | **NO** |
| **A3** | `a3-passage-splitter` | **815** | **487** | **NO** |
| A2N | `a2n-notation-fixer` | 112 | 15 | **NO** |
| A2B | `a2b-bold-marker` | 111 | 15 | **NO** |
| **A2L** | `a2l-layout-reader` | **144** | **15** | **NO** |
| A2C | `a2c-structure-transcriber` | 22 | 0 | no |
| A2R | `a2r-render-reviewer` | 22 | 0 | **NO** |
| **A4** | `a4-subtopic-writer` | **75** | **48** | **NO** |
| A2I · A5–A9 | — | 0 | 0 | never run |

Three of those are now wired (`A2` text, `A2L` layout, `A2S` special). **A3, A4, A2B and A2N
are still unread.**

## 14.2 · What each one gives that nothing else can

**`a2l-layout-reader` (A2L) — the arrangement.** Per element it measures `column`
(`full`/`left`/`right`), `align`, `font`, `text_color` and `fill`, plus the page's real column
ranges. The extractor can only *cluster x-positions*, which is a guess at the judgement A2L is
asked to make directly — decide the page's columns first, then place elements in them.

> Measured cost of not having it: on BIO11L ch02 the bbox heuristic placed figures **9 right,
> 1 left, 0 full-width** on a chapter that prints several across the full measure. And the
> fills — a caption band `#fef2e2`, a rule bar `#4c7435`, a contents panel `#ffe5ca` — are
> VECTOR drawings that never appear in the text layer at all, so the renderer had them only
> from a hard-coded per-book table, correct for the one book it was sampled from.

**`a2-special-transcriber` (A2S) — tables, equations, figures.** Returns a table's `header[]`
and `rows[][]`, an equation's `latex`, a figure's labels.

> Measured: a cell grid *can* be rebuilt from span x-positions, and `_cell_grid` does — 6×7 on
> Table 1.1, the right shape. But the text layer had already cut a word at a column boundary:
> geometry gives `Monocotyledona` and `Phylum/` + `Division` as two header rows; A2S gives
> `Monocotyledonae` and `Phylum/ Division`. No amount of geometry recovers a character that is
> not in the file.

**`a3-passage-splitter` (A3)** — which blocks form one coherent passage. 487 Biology outputs,
**unread**. A passage is what an exam-question citation points at.

**`a4-subtopic-writer` (A4)** — the named subtopics and their passages. 48 Biology outputs,
**unread**. This is the answer to "where do subtopics come from".

**`a2n-notation-fixer` (A2N)** — sub/superscripts backfilled from the page image.
**`a2b-bold-marker` (A2B)** — which substrings are bold, read off the image.
**`a2r-render-reviewer` (A2R)** — the render checked against the real page. Never run here.

## 14.3 · Why it was missed, so the shape of the mistake is visible

The deterministic extractor was written first and worked well enough to produce something that
*looked* finished — pages, figures, HTML. Each later question ("why is the green missing?",
"why do figures stack?", "why is the table prose?") was answered by improving the **heuristic**,
because the heuristic was the thing in front of me. Nobody asked the one question that would
have short-circuited all of it: *is there already an agent whose job this is?*

There was, for every single one of them.

**The rule that follows:** before deriving any fact from the PDF, check `steps/<STEP>/out/` for
an agent that was asked for exactly that fact. The agent output is the answer; the derivation
is the fallback for pages the agent has not covered.

## 14.4 · The joiners

| module | brings | falls back to |
|---|---|---|
| `join_agent_text.py` | the words, `source` per node | the text layer |
| `join_agent_layout.py` | column, align, font, fills, colours | clustered geometry |
| `join_agent_special.py` | table grids, equation LaTeX, figure labels | `_cell_grid` from span x |

Each stamps its own provenance (`source`, `layout_source`, `special_source`) and reports counts
rather than a claim. A page can never say it had an agent it did not have.

**Order matters:** text → layout → special. A2L and A2S both match on `a2_block_n`, which the
text join is what writes.

## 14.5 · Still unwired — do these next

1. **A3 → passages** (487 Biology outputs ready). Needed for `PS#` rows and for evidence
   citation.
2. **A4 → subtopics** (48 ready). Needed for `topic_*` / `subtopic_*` on every node where the
   book's numbered headings do not already supply them.
3. **A2B / A2N** — bold and notation, where A2's own text did not already carry them.
4. **A2R** — run it on the rendered pages and act on what it reports.

---

# 15 · Making sure a fix reaches every chapter, not just the one in front of us

Each defect in §13 was found on one page and could have been patched there. None were. Every
fix is in the extractor or the joiners, so it applies to all 71 Biology chapters and to
Chemistry and Physics when they are measured. Two habits enforce that:

**Fix the rule, never the page.** No chapter id appears in any `if` in `code/`. If a fix needs
one, the rule has not been understood yet.

**Re-run the built chapters after every extractor change.**

```bash
for ch in $(ls data/*_ncert/class_*/*/*/chapter.json | sed 's#.*/##'); do … ; done
# or simply, for the ones built so far:
for ch in BIO11L-ch01 BIO11O-ch01 BIO11L-ch02 BIO11O-ch02; do
  ../.venv/bin/python code/run_chapter.py $ch
done
```

A fix that improves one chapter and breaks another is not a fix. The counts printed by
`run_chapter.py` — pages, figures, agent pages, rows per kind — are the cheap regression test:
they should move in the direction the change intended and nowhere else.

---

# 16 · Final state — every agent wired (2026-10-22)

All agent output that exists on disk is now consumed. Four joiners, each owning one thing, each
stamping its own provenance and reporting counts rather than claims.

| joiner | agent | brings | falls back to | provenance field |
|---|---|---|---|---|
| `join_agent_text.py` | **A2** | the words | PDF text layer | `source` |
| `join_agent_layout.py` | **A2L** | column, align, font, fills, colours | clustered geometry | `layout_source` |
| `join_agent_special.py` | **A2S** | table grids, equation LaTeX, figure labels | `_cell_grid` from span x | `special_source` |
| `join_agent_structure.py` | **A3 + A4** | passages, subtopics | nothing — agent-only | `source` on the row |

**Order is fixed and cannot be changed:** text → layout → special → structure. A2L and A2S both
match on `a2_block_n`, which the text join writes; A3 groups those same block numbers; A4 names
A3's passages.

## 16.1 · Row kinds now emitted

```
para 196 · passage 138 · term 78 · section 59 · subtopic 58 · box 44 · page 44
figure 27 · list 12 · table 4 · summary 4 · exercises 4 · chapter 4 · book 4
pair 2 · unit 2 · style 1
```

A node row carries **25/25** of the schema's specified fields — `PK SK id kind chapter_no
chapter_title topic_no topic_title topic_id subtopic_no subtopic_title subtopic_id address
para_no body marks body_md sentences terms pages boxes lang reprint source qa` — plus
`line_pitch_pt`, which the renderer needs and the schema does not forbid.

**Only `change` rows are absent**, and they cannot exist yet: a change row is the diff between
two reprints of the same book, and we hold one reprint per edition. It is a real gap, not an
oversight.

## 16.2 · Tables are TEXT, not pictures

Verified on `BIO11L-ch01`: the HTML contains `<table class="grid">` with
`<td>Man</td><td>Homo sapiens</td>…` and **zero** table images. The crop is still cut and kept
as a fallback for a renderer that wants the book's own ruled, tinted grid.

The grid comes from A2S where it has run and from `_cell_grid` where it has not. Where both
exist the agent wins and the measured one is kept beside it as `table_grid_measured`, so a
later check can flag a disagreement instead of silently preferring one.

## 16.3 · The honest gaps

| | |
|---|---|
| A2L coverage | **15 of ~1,118** Biology pages. Everything else uses clustered geometry. |
| A4 ↔ old edition | A4's passage ids are the *latest* edition's, so older-edition subtopic links come back **0**. Reported, not faked. |
| `change` rows | impossible with one reprint per edition |
| A2I (italic) | never run |
| A5–A9 | never run — no old↔new passage pairing, no change log |
| vector figures | 3 of 11 in BIO11O-ch02 are caption-only; their artwork is vector, not an image block |
| Chemistry, Physics | designs registered, **not measured** |

---

# 17 · `change` rows cover BOTH kinds of change

The schema's example is reprint-to-reprint (`CHG#2027-28#…`). That is one case of two, and the
smaller one.

**The bigger case is rationalisation: old edition → new edition.** Measured on Class 11 Biology
Chapter 1, `build_change_rows.py` produces **62 change rows**:

| change_type | n | what it is |
|---|---|---|
| `removed` | 28 | all of `1.1 WHAT IS 'LIVING'?` — deleted outright |
| `moved` | 24 | `1.2 Diversity` was `1.1`; `Genus` was `1.3.2`, now `1.2.2` |
| `edited` | 10 | small rewrites |
| `added` | 0 | nothing new — rationalisation only deletes and renumbers |

Both kinds are the same shape of fact — *this text was added / removed / moved / edited, here
is where it was, here is where it is now* — so they are one row kind separated by
`change_type`, with `from_edition`/`to_edition` and `from_reprint`/`to_reprint` saying which two
books were compared.

**This is not the `PAIR#` row's job.** A pair row says "new chapter 4 is old chapter 5" — the
CHAPTER level. A change row is the PARAGRAPH level, and it is what lets a product answer *"has
the line my question was built from survived?"*, which is the whole reason `ncert_links` exists.

**Matched by TEXT, never by position** — position is the thing that changed. Exact normalised
match first, then similarity ≥ 0.82 for an edit; what is left is a genuine add or delete. Where
the text is identical and only the address differs the row is `moved` and **the node keeps its
id**, which is exactly what makes a stable id worth having.

```bash
../.venv/bin/python code/build_change_rows.py --book BIO11 --chapter 1
# -> data/dynamodb/_changes/CHG_BIO11-ch01.json
```

Requires **both editions built**. It says so and skips rather than guessing.

---

# 18 · A2V — the verifier that stops this recurring

`agents/a2v-extraction-verifier.md`. Every other check in this pipeline looks at an INPUT;
defects in the OUTPUT were found only when a person read the finished file. Several reached
that point — §13 lists eighteen.

A2V is handed a built chapter and its page images and reports discrepancies it can SEE:
presence, placement, heading level, formatting, notation, table shape, figure/caption pairing.
It fixes nothing. Every finding names the page, what the page shows and what the data has, so
it can be acted on without re-reading the book.

Run it after every chapter build, before loading:

```bash
../.venv/bin/python code/run_step.py A2V --list
# per line: Use the a2v-extraction-verifier subagent. Input: <in>. Output: <out>. Do nothing else.
../.venv/bin/python code/run_step.py A2V --check
```

---

# 19 · The runner after the workflow split

The 2026-10-22 split gave each workflow only its own stage scripts. Two things broke and are
now fixed, because they will break again the same way if anyone re-splits:

1. **`from scripts.lib import …`** — the package was renamed `scripts/` → `code/`, so every
   module addressing it by the old name failed the moment the folder moved. Rewritten to
   `from lib import …` in 5 files.

2. **`step_plugins.py` imports every stage's modules.** It holds a plugin for every step A–F,
   but `fetch_passages` and `build_groups` are Stage D and now live in `ncert_to_paper_maps`,
   `qmap_plugins`/`ecat_plugin`/`b3v_plugin`/… are paper-side. Importing them unconditionally
   meant a Stage A command died on a Stage D import. They are now optional: a plugin whose
   module is absent is not registered, which is correct — that step does not run in this
   workflow — and `step_plugins.available_steps()` says what this workflow can run.

```
ncert_extractions can run:  A1 A2 A2B A2C A2I A2L A2N A2R A2S A3 A4 A5 A6 A7 A8 A9 …
modules absent (other workflows): fetch_passages build_groups qmap_plugins ecat_plugin …
```

---

# 20 · The same mistake, four more times (2026-10-22, later)

§14 recorded that the pipeline was deriving with heuristics what agents had already been asked
to judge. It happened four more times in one sitting. The pattern is identical each time, so it
is written out once here:

> **A heuristic was built to recover something the agent had already provided, and the join was
> destroying the agent's answer on the way in.**

| # | symptom | what I built | what was already there |
|---|---|---|---|
| 1 | Table read as a run-on sentence | `_cell_grid`, clustering span x-positions into columns | **A2S** had the table: `header[]` + `rows[][]`, with `Monocotyledonae` complete where geometry truncated it to `Monocotyledona` |
| 2 | Figures stacked down the middle | a bbox heuristic guessing left/right/full | **A2L** reports `column: full\|left\|right` as a judgement, plus `align`, `font`, `fill`, `text_color` |
| 3 | Exercises as one 1,026-char blob | a regex splitting on `N.` at sentence boundaries | **A2** returned the questions `\n`-separated — and `join_agent_text` was flattening them with `re.sub(r"\s+", " ")` |
| 4 | Page-break paragraphs in halves | — | **A2** reports `continues_from_previous`; the join dropped the field |

Number 3 is the sharpest: the agent gave the right answer, the join deleted it, and a regex was
then written to reconstruct what had just been thrown away. It recovered 7 of 10 questions,
because question 5 carries two italic sub-lines, 7 carries options `(a)(b)(c)` and 9 carries
`(i)`–`(v)`, and no rule about digits and full stops separates a question number from a
sub-part number.

## 20.1 · The three rules that follow

1. **Before deriving a fact, grep `steps/*/out/` for an agent that was asked for it.**
2. **Never normalise an agent's output on the way in.** Whitespace, line breaks and block
   boundaries are the agent's answer, not noise. `join_agent_text` now collapses spaces and
   tabs only, never newlines.
3. **A derivation that cannot verify itself must refuse.** The exercise split now checks the
   numbers run `1..N` with no gaps and, when they do not, leaves the block whole and sets
   `needs_agent_split` with the attempt recorded. Seven questions with three silently missing
   looks complete; one unsplit block is visibly unfinished.

## 20.2 · Agent briefs improved rather than worked around

`agents/a2-page-reader.md` now states that **an exercises question is its own block**
(`kind: "question"`), with its sub-parts kept inside it, and that a non-exercises numbered list
stays ONE block because it is one passage. The brief explains why a script cannot do it: *you
can see the boundaries; a script cannot.*

That is the correct shape of fix. The regex was a workaround for a brief that had not been
written.

## 20.3 · More defects fixed in the same pass

| defect | cause | fix |
|---|---|---|
| Chapter title page missing entirely | `chapter_title` was listed as furniture | it is printed ONCE, on its own page — not furniture |
| Opener had no green panel or QR | the page prints **no folio**, so it was absent from the page map | pages keyed by file when there is no folio |
| A header band rendered **mid-page** under a figure caption | vector-figure clustering picked the page's own band — bands are vector too | head 13% / foot 8% / full-bleed bars excluded from clustering |
| 11 figures on a 1-figure chapter | every ruled box and tint panel clustered as artwork | a vector figure is claimed only where the page prints a `Figure N.M` caption no image figure accounts for |
| Table had no colour and overflowed the trim | fill never read; `width:100%` with auto layout | fill sampled from the page's drawings; `table-layout:fixed` |
| `art: null` on every page | `cut_figures` runs AFTER `doc` is built | artwork attached after cutting — the same ordering mistake as the figure captions |
| Runner dead after the workflow split | `from scripts.lib import …`, and cross-workflow plugin imports | imports rewritten; plugins made optional per workflow |


---

# 21 · THE REVIEW GATE — run it every time, on every chapter

**No chapter is finished until a reviewer agent has compared it against the page images.**

Everything in §13 and §20 — thirty-odd defects — reached a finished-looking file because the
only check was a person noticing. Scripts check inputs; nothing checked the output. Two agents
exist for exactly this and both must run before a chapter is called done:

| step | agent | compares | catches |
|---|---|---|---|
| **A2V** | `a2v-extraction-verifier` | `chapter.json` ↔ the page images | missing/duplicated/misplaced pieces, wrong heading level, bad marks, flattened notation, wrong table shape, caption/figure mismatch |
| **A2R** | `a2r-render-reviewer` | the rendered page ↔ the real book page | a cropped diagram, a band in the middle of the text, half a page blank, content off the sheet |

## 21.1 · The gate

```bash
# 1 build
../.venv/bin/python code/run_chapter.py BIO11L-ch01

# 2 VERIFY THE DATA against the pages        <- not optional
../.venv/bin/python code/run_step.py A2V --list
#   per line: Use the a2v-extraction-verifier subagent. Input: <in>. Output: <out>. Do nothing else.
../.venv/bin/python code/run_step.py A2V --check

# 3 VERIFY THE RENDER against the pages      <- not optional
../.venv/bin/python code/run_step.py A2R --list
#   per line: Use the a2r-render-reviewer subagent. Input: <in>. Output: <out>. Do nothing else.
../.venv/bin/python code/run_step.py A2R --check

# 4 only now: load
../.venv/bin/python code/load_to_dynamodb.py --chapter BIO11L-ch01
```

**A chapter with an unresolved `high` finding does not get loaded.** `load_to_dynamodb.py`
already refuses `source: text_layer` nodes; a `high` A2V finding is the same class of problem
and should be treated the same way.

## 21.2 · What the reviewer is checking the JSON for

Every one of these was a real defect that shipped:

- every printed paragraph, heading, list, figure, table and question appears **exactly once**
- a figure sits with **its own caption**, and under the section that discusses it
- `marks` cover the words the page prints bold/italic and **only** those words
- subscripts and superscripts are real (`C₆H₁₂O₆`, not `C6H12O6`)
- a table's `table_grid` has the row and column count the page prints
- heading depth matches the printed number (`1.2` topic, `1.2.2` subtopic)
- exercise questions are separate and **numbered 1..N with no gaps**
- furniture — running head, folio, reprint line, opener contents rail — is **absent** from the
  content, and present on the page/chapter rows

## 21.3 · The self-check the build already does

`run_chapter.py` prints these every run, and they are the cheap regression test. They should
move in the direction a change intended and nowhere else:

```
tree    <pages> pages, <figures> figures
agent   <n>/<n> pages read by a2-page-reader, <n> blocks replaced
rows    <n> rows {kind: count, ...}
```

And the build refuses to pretend: a page with no agent read is named in a WARNING;
`--require-agent` makes it fatal; a split that cannot verify itself sets `needs_agent_split`
and leaves the block whole rather than emitting a partial answer.

---

# 22 · The 60-point external review — triage

An external page-by-page review of `BIO11L-ch01` against its PDF listed 60 defects. Its central
conclusion is correct and is now the architecture this section plans toward:

> *Keep two linked representations: a semantic chapter tree for reading and search, and a
> page-layout representation for PDF-faithful rendering. The current HTML tries to recover the
> second from the first after the layout information has already been lost.*

Every concrete claim was checked against the data before being accepted. The ones that were
verifiable all verified.

## 22.1 · Fixed

| # | defect | fix |
|---|---|---|
| 51 | Words fused at page joins — `andtypes`, `Linnaeusused`, `andmelongena`, `Allthese` | the stitch joined `text` with a space and `runs` **without** one, and `body` is built from the runs. A separator run is now inserted. **4 corruptions → 0** |
| 55 | Multi-box paragraphs carried no character ranges | each box now records `{page, page_file, from, to}` — which characters the book printed on which page |
| 32 | Every page's running head said the chapter title | the page record already held the measured string; the renderer was passed the chapter title. Now alternates `Biology` / `The Living World` as the book does |
| 8 | Two PDF pages omitted — the Unit opener and the Ernst Mayr box | kept as `unit_tree` + `unit_page_records`, stored under `BOOK#…/UNIT#n` per the schema. **Coverage 87% → pass** |
| 54 | Page references inconsistent; opener boxes had `page: null` and no `page_file` | every box carries `page_file`; section nodes were the one kind missing it |
| 45 | Numbered rules rendered as a bulleted `<ul>` | *open — see 22.2* |

## 22.2 · Open, and why each is blocked

| # | defect | blocked on |
|---|---|---|
| 1–6 | Page fragments not placed on their original pages | **the two-representation fix.** `char_ranges` is now recorded, which is the prerequisite; the renderer must learn to place a fragment rather than a whole node |
| 7 | Section headings repeated on continuation pages | the re-emit was deliberate (so a page never opens with orphaned prose) and is wrong. Needs the fragment model to know whether the section *started* on this page |
| 9–16 | Opener uses an ordinary-page layout; block positions discarded; wrong column on p8; table confined to the measure; side content in the main column; Summary/Exercises not centred; no first-line indent | **A2L.** `column`, `indent`, `align`, `text_block` and `space_before` are exactly these fields. Six agents are running |
| 17–28 | Typography: substitute fonts, no explicit base size, one shrink factor, wrong pitch, titles as body text, heading sizes, small-caps misapplied, colours off, lost italics | partly A2L (`size_pt`, `text_color`), partly a real stylesheet pass once A2L lands |
| 29–30 | HTML not self-contained; opener depends on a missing image | the crops exist on disk; they must be inlined as data URIs or served from the CDN |
| 31 | Watermark not reproduced | **deliberate** — the owner asked for it to be removed. Not a defect |
| 33–34 | Furniture geometry approximate; crop marks absent | A2L for geometry; crop marks are out of scope |
| 35–37 | Figure 1.1 missing; its box is caption-sized; caption split in two | the flowchart is **vector**; nothing was cropped because no image block exists. A2L's measured `figure` box is the fix |
| 38–43 | Table column widths, text size, borders, caption styling, cell italics, word-breaking | A2S gives cells as plain strings — italics are lost at source. Column widths need A2L's `col_x` |
| 44 | Nomenclature rules duplicated in JSON | **re-check: the list now holds 4 distinct items**, so this is resolved by the newline-preservation fix |
| 46–50 | Exercises flattened; sub-parts, arrows and alignment lost | **A2's brief now requires one block per question**, sub-parts kept inside. Needs A2 re-run on p009 |
| 52–53 | `layout_join` reports 0 enriched; `needs_agent_split` reaches the renderer | 52 is A2L not having run. 53 is now surfaced by `check_chapter.py` as a WARN rather than shipping silently |
| 56 | No complete font/style/baseline spec on nodes | A2L `size_pt` + a stylesheet pass |
| 57 | Fixed-height pages hide overflow | **real.** `overflow:hidden` plus a `--fit` floor of 0.72 can clip. Needs a measured-overflow check |
| 58 | Footer absolutely positioned, text can run under it | same |
| 59 | No `break-after:page` for print | one-line CSS fix |
| 60 | "agent text 9/9" overstates completeness | `check_chapter.py` now prints fails and warns beside it |

## 22.3 · What this changed about how we work

`code/check_chapter.py` runs at the end of every build and fails on any defect already shipped
once: orphan nodes, text coverage below 90%, duplicate content, figure over-detection, gapped
exercise numbers, furniture as content, missing title. **Class 11 ch01 both editions: 0 fails.**

The reason the external review found 60 things and the build found 0 is that the build was only
checking what I had thought to check. That is why §21's agent review gate is not optional.


See **[LESSONS.md](../LESSONS.md)** — every defect this pipeline has shipped and the rule that prevents it. Read it before changing `code/` or `agents/`.
