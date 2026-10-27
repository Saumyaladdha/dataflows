# Paper extraction v2 — the new corpus, and what changes

`Saumya_NEET_work/NEW/NEET_Papers` replaces the sources Stage B was built against. This document is
the plan, the measured facts about the new files, and the list of agent changes that follow. Read it
before running any Stage B step on a v2 source.

## 1. Why the old flow does not fit any more

The first corpus took whatever source could be found per year: a chapter-topicwise coaching
compilation for 2023, an OCR pass for 2022, a booklet for 2024. Three sources meant three parsers, a
separate figure-hunting stage, and an answer key matched in from elsewhere. Measured against the
printed papers it reached 87% (2024), 87% (2023 vs coaching) / **69% vs the real NTA volume**, and
75% (2022, OCR-contaminated).

The new corpus removes the three causes at once:

| what used to be a separate stage | why it is no longer one |
|---|---|
| figure hunting across other codes and the web | the figure is **in this booklet**, in this question's own region |
| matching an official answer key in | `Answer (3)` is **printed under every question**, per code |
| per-year parser | ~92 booklets across 2015–2024 are **one publisher, one layout** |

## 2. What the corpus actually holds — measured

`python3 scripts/extract_paper_v2.py --probe`

```
211 pdf(s), 137 unique by content
   duplicate_bytes    74      the same file arrives as Download_Here.pdf and as its real name
   aakash             64      "Answers & Solutions", text layer, Answer (N) printed
   aakash_classic     16      same publisher, older wording
   solution_inline    12      2015/2016: "Solution: (4)" instead of "Answer (4)"
   scanned            41      no text layer at all
   unknown_text        4
```

Codes with a usable text source, by year:

| year | codes | | year | codes |
|---|---|---|---|---|
| 2015 | 4/4 | | 2021 | 4/5 |
| 2016 | 7/7 | | 2022 | **23/24** |
| 2017 | 5/5 | | 2023 | **22/24** |
| 2018 | 5/5 | | 2024 | **21/24** |
| 2019–20 | 3/3 | | 2025 | **0/5 — all scans** |

**Two sites, and the formats differ.** The same booklet appears both as a scan and as a text
booklet, under names that do not say which is which: 2023 Set_E1 holds a 22 MB `..._E1.pdf` (scan,
PDFium) and a 2.7 MB `..._Set_E1.pdf` (also a scan, Zan Image Printer), while the text version is
the 70-page one. **Never choose a source by filename.** `--probe` and `pick_booklets()` choose by
measured chars-per-page, which is why the extractor opens every candidate before picking.

## 2.1 Who published these — at least six, not two

Counted by brand markers in page text and PDF metadata across the 137 size-unique files:

| year | publishers found |
|---|---|
| 2015 | **vedantu 4**, motion 1 |
| 2016 | **vedantu 7**, motion 1 |
| 2017 | **vedantu 5**, motion 1 |
| 2018 | **vedantu 5**, resonance 1 |
| 2019 | motion 1 |
| 2020 | aakash 1 |
| 2021 | allen 4, motion 1, brilliant 1 |
| 2022 | **aakash 22**, motion 5, brilliant 1 |
| 2023 | **aakash 21**, resonance 8 |
| 2024 | **aakash 20**, motion 3 |

Two consequences:

1. **2022–2024 are Aakash and carry no Vedantu.** The booklets actually selected for those years are
   all `family: aakash`.
2. **Vedantu is the dominant source for 2015–2018.** `b3-question-reader` has a rule about a stem
   running into a `www.vedantu.com` footer; that rule is dormant for 2022–2024 and becomes live the
   moment the corpus is extended back. Do not delete it.

## 3. Format families, and how they are told apart

Identified from the FIRST page's text, never the filename:

| family | fingerprint | answer marker | years |
|---|---|---|---|
| `aakash` | `Corporate Office : Aakash Tower` | `Answer (3)` | 2017–2024 |
| `aakash_classic` | `Answers & Solutions` | `Answer (3)` | 2017–2018 |
| `solution_inline` | question 1 opens the file | `Solution: (3)`, `Answer Key: (3)` | 2015, 2016 |
| `scanned` | under 200 chars/page | none — needs OCR | 2025, some codes elsewhere |
| `ocr_scan` | has a text layer AND most pages are sliced scans | present but machine-read | scattered, e.g. 2022/Set_T2 |
| `unknown_text` | has text, matches no fingerprint | unknown | 4 files |

### 3.1 `ocr_scan` — the family that hides

A booklet whose pages are **sliced scans carrying an OCR text layer** looks like a text source by
every character count and is not one. Measured on `2022/Set_T2/Download_Now.pdf`: **2,123 chars per
page**, comfortably past the text test, while every page is cut into **150–400 image fragments** and
only **1 of 200** questions could be located.

An OCR layer is exactly what SPEC Rule 26 refuses. Its characters are a machine's reading of a
picture, so the digits and exponents that decide a NEET answer carry no more authority than the scan
— yet its chars-per-page makes it indistinguishable from a real text layer everywhere downstream.
Refusing it at detection is the only place that distinction is still visible.

It is detected by the fragment count, not the text: more than `MAX_IMAGES_PER_PAGE` images on at
least half the sampled pages.

A `scanned` or `ocr_scan` booklet is **skipped**, not OCR'd into the same corpus. Mixing an OCR read with a
text-layer read is exactly how the first 2022 corpus reached 75%, and a mixed corpus cannot be
audited because no row says which path produced it.

## 4. The procedure — page by page, as Stage B already defines it

Nothing new is invented here. `config/steps.yaml` B2 already says the crop step is script-side:
*"figure/option cropping are SCRIPT-side (the question-crop step after this agent returns boxes)"*.

```
B1   register the paper                      page_images + text_layer
B2   find question boundaries   ITEM = PAGE   boxes in IMAGE PIXELS
     ^ when a text layer exists, scripts/extract_paper_v2.py MEASURES these instead of
       dispatching the agent. The agent remains the path for scanned booklets.
(script) crop one image per question          scripts/extract_paper_v2.py
(script) crop one image per figure            same pass, same geometry
B3   read one question          ITEM = QUESTION  reads the QUESTION IMAGE
B3F  transcribe one figure      ITEM = FIGURE    caption + labels, exactly as printed   [NEW]
B10  split option panels        ITEM = FIGURE    when one crop holds four pictures
```

**The text layer is a draft, never the record.** `codebook/A2`'s rule applies verbatim to these
booklets:

> This rule does NOT apply to superscripts, subscripts, radicals, absolute-value bars, inequalities,
> hat symbols or the degree symbol — the text_layer regularly LOSES these even when its plain prose
> is exact.

A NEET paper is made of exactly those characters: `10^-7`, `CO2`, `√2`, `≥`, `37°`. So
`text_layer_draft` in the extractor output is a cross-check for B3 and a way to measure agreement —
it is not the answer. A pure text parse of 2024 Code-Q2 scored 100% on answers and 99.8% on
four-option questions **and was still unsafe**, for this reason alone.

## 5. How figures are extracted, and why one mechanism covers all of them

**Not** by pulling embedded images. Measured on one page of 2024 Code-Q2: **2 embedded images
against 212 vector paths.** A chemical structure, a circuit, a ray diagram, a graph and a match-list
table are vector art plus text labels — there is no image object to pull, and `get_images` returns
the publisher's logo.

Instead the question's **region is rendered**. That captures raster, vector, composite and tabular
figures identically, which is what "no separate figure flow" means in practice: the figure crop falls
out of the same geometry pass that cuts the question crop.

Two conventions are taken from Stage A because they are proven there:

- the crop is **grown outward** toward its neighbours, and `target_box_in_crop` says which part
  inside it is the subject — `a2-special-transcriber` needs this because a tight crop loses the
  caption and a loose one imports the next figure;
- a figure is **never described**. It goes to a transcriber for its caption and labels, copied
  exactly. Nothing in this pipeline writes prose about a drawing.

### 5.1 The four tests that decide "figure or not"

Set from the measured distribution over one booklet's ink bands, not guessed. Each test exists
because the version without it was wrong:

| test | threshold | the error it fixes |
|---|---|---|
| repeated-image furniture | an image on ≥25% of pages | **the watermark**. See 5.2 |
| size | ≥40pt tall AND wide | a fraction bar, a radical overbar, a table rule |
| substance | ≥8 vector paths | a single stroked line is a rule, not a drawing |
| text coverage | <80% of the band's height covered by text lines, measured as a **union** | a band that is just the underline of its own text. Summing per-line overlaps double-counts and gave coverage above 1.0 |

An embedded image above the logo threshold is a figure whatever its path count.

### 5.2 The watermark — the single biggest error, and how it is caught

These booklets carry a large diagonal *Aakash Medical|IIT-JEE|Foundations* watermark. Measured in
2024 Code-Q2: image **xref 818, on 81 of 82 pages, at the identical rect (172,272)-(435,514)**,
263×242pt — bigger than most real diagrams and sitting over the middle of the text column.

With no watermark rule, **65.5% of questions appeared to carry a figure** and the crops were
solution prose with branding across it. With it, the figure rate is **16%**, which is the plausible
rate for a NEET paper.

The rule is **document-level and by xref**, not geometric:

- *document-level*, because "this mark is on every page" is only visible across pages. Per page, a
  watermark and a diagram look the same — both large, both mid-page.
- *by xref, not by rect*, because excluding the rect would also drop any real diagram sitting behind
  the watermark, and on these pages that is most of them.

### 5.3 Where the question stops and the solution begins

The cut is anchored on the **`Answer (N)` line**, not on `Sol.`, and a band straddling the cut is
assigned by its **midpoint**.

Measured case: 2024 Code-Q2 question 50. Its solution's figure begins at y=515 while the `Sol.`
label sits at y=529.5 — the drawing starts *above* its own label because it is set beside it.
Anchored on `Sol.` with a top-edge test, that solution figure was emitted as the question's own
option panel. `Answer (N)` always precedes the solution, so it is the safe anchor.

## 5.4 Every format difference that had to be measured, and what it cost

Each row is a real defect found by testing one booklet per publisher instead of trusting the Aakash
result. Every one of them returned a confident wrong number rather than an error, which is why they
are listed with the measurement that exposed them.

| what differs | how it was wrong | how it is handled |
|---|---|---|
| **Option markers** `(1)-(4)` vs `(a)-(d)` vs `(A)-(D)` | Vedantu 2021 parsed **0 of 200** option sets; the questions looked *empty*, not *unparsed* | style measured per booklet, then per question |
| **Case is meaningful** | 2020 Code-F1 prints options `(A)-(D)` while `(a)-(d)` are MATCH-LIST ITEMS on the same page; folding case promoted list items to options | styles are separate patterns, never merged; a fallback style is accepted only if it yields a complete set of four |
| **Style changes mid-booklet** | 2020's Biology half is `(A)-(D)` and its Physics half is not; one style per booklet explained **90 of 178** | `best_draft()` retries the other styles per question |
| **Answer marker may be a letter** | `Answer: (c)` against a digit-only pattern found **0 of 200** answers | the answer pattern accepts `[1-4a-dA-D]` and normalises |
| **No space after the question number** | `108.The average thermal energy...` lost **46 of 200** questions — a whole block, 108 and 111-135, which read as a source defect | the space is optional; a capital or bracket must follow, so `1.5` still does not match |
| **Two columns** | 2017 Code-C parsed **78 of 179** option sets, reading options out of the neighbouring column | gutter measured by projection profile; one `parts` box per (page, column) |
| **Printed page border** | four edge rules merged into one page-covering band, so **126 of 200** questions reported option panels and every crop was a full page | long thin rules excluded; no band may cover more than 60% of a page |
| **Page-sized background image** | correctly flagged as furniture, it then vetoed every vector path drawn on top of it: 2017 and 2018 reported **0 figures** while their pages held 208 and 893 drawings | only a furniture mark under 25% of the page may veto content |
| **Sliced scan with an OCR text layer** | 2,123 chars/page passed every text test; **1 of 200** questions found | its own refused family, `ocr_scan`, detected by fragment count |
| **Shredded maths** | 2020's Physics half sets each glyph on its own line, so option markers do not survive as line starts | the question CROP is still cut; B3 reads it from the image, which is what the draft/record split is for |

### 5.4.1 Hybrid booklets — the fault that looks exactly like a parser bug

A booklet can be **part real text and part sliced scan**. 2023 Code-E3 is the measured case: pages
1-20 carry a genuine text layer and pages 21 onward are sliced scans with a partial OCR layer. Family
detection samples the first 8 pages, so the whole booklet is called `aakash`, correctly for the part
it looked at.

What that produced: question 94 came back with options `(1)` and `(3)` only. Options `(2)` and `(4)`
are **not in the text layer at all** — OCR dropped them silently. Across the booklet 51 of 200
questions were short, which reads as a parser that cannot find options rather than as a source that
does not contain them.

So reliability is tracked **per page, and reported per question**. `text_layer_reliable: false` means
every statement in that question's `text_layer_draft` is a second guess rather than a cross-check,
and B3 must read the crop. The crop itself is cut normally — the geometry is sound, only the text is
not — so nothing is lost, but nothing is silently trusted either. The flag is carried into the CSV
and shown on the HTML page.

This is the same principle as refusing `ocr_scan` whole booklets, applied at page granularity: the
distinction between "read from text" and "read from a machine's reading of a picture" has to survive
into the output, because no later step can reconstruct it.

### 5.5 Two-column layout, and why the first two detectors were thrown away

The gutter is found from a **vertical projection profile** -- how many text lines CROSS each x
position. Two earlier attempts used where lines START and both failed:

- *widest gap between consecutive starts*: a few indented lines start mid-page and bridge the gutter,
  so on 2017 Code-C the largest gap was 94pt and sat in the wrong place;
- *histogram of starts with a valley test*: found **3 of 16** real two-column pages and produced a
  **false positive on 2024 Code-Q2**, which is single-column.

A crossing profile is robust because an indented line still does not cross the gutter. Measured on
page 9 of each booklet, `#` dense, `+` sparse, `.` empty:

```
2017 Code-C  ....++#######################+.++##########++++++++++++++.....   two columns
2018 Code-AA .......##########+###+++++++++.++.#############++++++#+++.....   two columns
2019 Code-P1 ......##+#########+++.++++++..+++###############++++++++....     two columns
2024 Code-Q2 .......++##########++++++++....++++++.........................   one column
2021 Code-O1 .......#########+++++++.....................................     one column
2015 Code-A  ..#################++++++++++++++++++.........................   one column
```

Verified across one booklet per year: 15/16 pages on each of 2017, 2018 and 2019; **0 false
positives** on 2015, 2016, 2020, 2021, 2022, 2023 and 2024.

A false split is worse than no support, because it invents a gutter and reads a question's options
out of its neighbour -- returning a plausible number instead of an error. That is why the detector is
strict, and why reading order is *the whole left column, then the whole right*, never interleaved by
y: a question can start at the foot of the left column and end at the top of the right, where its
last line has a SMALLER y than its first. Comparing y alone drops those lines, so a two-column
question loses its options. Positions are compared as `(page, column, y)`.

## 6. Agent changes this corpus requires

| agent | change | why |
|---|---|---|
| `b5-key-copier` | **not used for v2 text sources** | the answer is printed under every question, per code. Still the path for a year whose booklet prints none |
| `b9-figure-matcher` | **retired for v2 sources** | it chose among candidate images downloaded from the web. The figure is now in the booklet, so there is nothing to choose between |
| `b9s-source-figure-confirmer` | **promoted from rescue to the standard check** | it already confirms "a figure cropped out of the official booklet belongs to our question and is complete". That is now the normal path, not a fallback |
| `b2-boundary-finder` | **fallback for scans only** | boundaries are measured from the text layer when one exists |
| `b3-question-reader` | updated | the question image now always contains the figure; the placeholder rules ("Image option — will be added soon") describe the OLD scrape and are kept only as legacy |
| `b3f-figure-transcriber` | **NEW** | nothing transcribed a paper figure's caption and labels. B3 only records `has_figure`/`figure_bbox`. Mirrors `a2-special-transcriber` |
| `b10-figure-splitter` | unchanged, still needed | one crop still holds four option graphs, and its printed-label trap still applies |
| `a2c-structure-transcriber` | **reused for papers** | a drawn structure in a Chemistry option is the same problem as one in NCERT. `not_a_structure` stays a real answer |

## 6.1 Running it — the whole flow, in order

```bash
python3 scripts/run_paper_pipeline.py --year 2024      # steps 1-6
```

The pipeline script covers extraction through export. The CLASSIFICATION chain after it is run the
same way every other stage is — `run_step.py <STEP> --list`, one agent per printed line, then
`--check` — and **its order is not optional**, because each step's input is built from the one before.

| # | step | kind | what it does |
|---|---|---|---|
| 1 | `extract_paper_v2.py` | script | picks the source by measured chars-per-page, cuts question and figure crops |
| 2 | `assign_subject.py` | script | subject + branch from the paper's own printed section headings |
| 3 | **`b3-question-reader`** (B3V) | AGENT | reads each question from its IMAGE — the record |
| 4 | `cut_agent_figures.py` | script | cuts the figure boxes the agent reported |
| 5 | **`b6-blind-solver`** (B6V) | AGENT | answers with the printed answer withheld |
| 6 | `export_paper_v2.py` | script | CSV and paper-like HTML per booklet |
| 7 | **`q-subject-confirmer`** (QSUBJ) | AGENT | the subject of any question whose paper printed NO heading |
| 8 | **`q-chapter-picker`** (QCHAP) | AGENT | the chapter, from a CLOSED list chosen by subject |
| 9 | **`q-subtopic-picker`** (QTOPIC) | AGENT | the subtopic, from THAT CHAPTER'S list only |
| 10 | `extend_taxonomy.py` | script | mints the chapters/topics the agents asked for and could not find |
| 11 | **`e7-difficulty-rater`** (E7V) | AGENT | easy / medium / hard, by counted work, answer withheld |
| 12 | **`e-category-rater`** (ECAT) | AGENT | E1–E5: type, format, shape, thinking, traps |

**Why 7 comes before 8, and what happens if it does not.** The chapter list handed to QCHAP is
chosen BY SUBJECT. A wrong subject is a wrong closed list, and the agent can then only answer
`unsure` — which is exactly what happened to 108 questions before the guard existed. QCHAP now
**refuses** a question whose subject is only a positional guess: it requires a printed heading or a
QSUBJ confirmation. This is not a nicety. In 2017 Code-C, **179 of 179** positional guesses were
wrong (the booklet runs Biology → Physics → Chemistry), and in 2015 Code-A, 43 of 43.

Every script skips what is already done, so an interrupted run resumes by repeating the command.

## 6.1.1 Subject, stream, chapter, subtopic — what each one is

These are four separate claims and the HTML labels them separately, because a reviewer cannot
confirm an assignment they cannot name:

| field | where it comes from |
|---|---|
| `subject` | the paper's printed section heading, else QSUBJ reading the question |
| `stream` (Chemistry) | `physical` / `inorganic` / `organic`, derived from the CHAPTER |
| `branch` (Biology) | `botany` / `zoology` / `both` — printed heading wins, else derived from the chapter |
| `chapter` | QCHAP, from the closed list |
| `subtopic 1`, `subtopic 2` | QTOPIC, from that chapter's list. Two are allowed and the ORDER matters: the first is what the answer turns on, the second a genuine second home, never a synonym |

**Neither stream nor branch is in the source table.** A full scan of `ExamChapterTopicMappings`
(1,606 rows, `Count == ScannedCount`, no pagination key) carries `subject` as
physics/chemistry/biology and nothing finer. Both are therefore derived **at chapter level, not per
question** — "Alcohols, Phenols and Ethers" is organic for every question in it — so the judgement
is made 59 times instead of 1,869 and lives in one reviewable file,
`papers_v2/mappings/chapter_streams.json`. `both` is preserved rather than forced: cell biology,
genetics and biotechnology genuinely are examined in both NEET sections.

## 6.1.2 When the taxonomy has no home for a question

The scan holds **26 Chemistry, 32 Biology and 31 Physics chapters** against roughly 97 in the NEET
syllabus. Whole chapters are absent — Transport in Plants, Digestion and Absorption, Environmental
Issues, The s-Block Elements, The Solid State, Hydrogen, Surface Chemistry — and so are obvious
topics inside present chapters (Current Electricity has no Potentiometer; Waves has no Doppler
Effect; Semiconductor Electronics stops at diodes).

The agents are forbidden to invent a code, and forbidden to quietly file a question in the nearest
chapter. Instead they answer `unsure` **and fill `proposed_chapter` / `proposed_topic`** with the
name as it should appear. Then:

```bash
python3 scripts/collect_taxonomy_gaps.py --apply    # the evidence: what was wanted, by how many
python3 scripts/extend_taxonomy.py --apply          # mints them into taxonomy_additions.json
```

`extend_taxonomy.py` writes `papers_v2/mappings/taxonomy_additions.json`, which `chapter_index()`
merges ON TOP of the scan. It never edits the scan: that file is a copy of a table owned elsewhere,
and rewriting a copy is how two systems quietly stop agreeing. Every added row carries
`added_locally: true`, so nothing downstream can mistake a chapter this project minted for one the
product owns. Titles are matched on an aggressively canonical form — dashes folded, a leading "The"
dropped, the source's own " - Practice" suffix stripped — because the cost is asymmetric: a missed
match adds a DUPLICATE chapter, while an over-eager one merely merges two spellings of the same one.

A question that is `unsure` shows its gap on the page by name — *"chapter missing from the taxonomy:
The s-Block Elements"* — never as a blank. An unmapped question and a carefully-mapped one that
found the vocabulary wanting look identical when both render empty, and they are opposites.

## 6.2 Subject, and why the question number is not enough

Assigned from the printed section heading where there is one; `subject_from` on every question says
which. Where no heading exists the positional guess is recorded but **is not trusted by anything
downstream** — QCHAP refuses it outright until `q-subject-confirmer` has read the question.

**Three of ten booklets print their sections in a NON-standard order:**

```
2015 Code-A    Chemistry 1-45    Biology 46-135    Physics 136-192
2017 Code-C    Biology 1-90      Physics 91-135    Chemistry 136-180
2020 Code-F1   Biology 1-90      Physics 91-135    Chemistry 136-180
```

**Three print no heading at all** — 2017_C, 2018_AA and 2019_P1, 533 questions — so for those the
agent is the only source. The measurements that settle how much the guess is worth:

| booklet | positional guesses the agent overturned |
|---|---|
| 2015 Code-A | 43 of 43 |
| 2017 Code-C | **179 of 179** |
| 2018 Code-AA | 0 of 180 |
| 2019 Code-P1 | 2 of 174 |

So the guess is not uniformly bad — it is bad *unpredictably*, which is worse, because nothing on
the page distinguishes a booklet it got right from one it got wrong. That asymmetry is why the
confirmation is a gate rather than an audit. (2019_P1's two overturns are not even subject errors:
both are rows of the printed answer-key grid segmented as questions — see below.)

**Not every "question" is a question.** 2019_P1 q031 and q050 are rows of the booklet's final-page
answer-key table, picked up by the boundary finder running past the end of the paper. Both have an
empty options object and a stem of nothing but `31. (1) 32. (1) ...`. The whole mapping chain now
skips any stem carrying three or more such pairs, and the export flags it — not because it is a hard
question or a badly read one, but because **it is not a question**, and because it means the answer
key is sitting inside the question stream, which matters to every step that must not see the key.

## 6.3 Two answers, and the key that was removed

| column | source | how it fails |
|---|---|---|
| `answer_official` | the booklet's own printed `Solution: (3)` | publishers get questions wrong |
| `answer_solved` | `b6-blind-solver`, printed answer withheld | catches the case where the publisher is wrong |

**The separately published NTA key PDFs were removed from the flow on 2026-10-21**, by the owner's
decision and on measured evidence. `scripts/read_official_key.py` and the 176 parsed per-code keys
are in `legacy/retired_2026-10-21/` with the measurement that retired them.

NEET prints the same questions in ~24 booklet codes with the options reordered, so a key only means
anything against the code it was published for — and the 2016, 2017 and 2022 PDFs carry no `BOOK :
<code>` heading to split on. Joined anyway, those keys contradicted the booklet's own printed answer
on **71%, 74% and 78%** of questions. That is not a finding; it is one wrong join repeated, arriving
labelled "official". **Do not re-introduce the step** without first proving, per booklet, that a key
PDF was published for the exact code in hand.

The booklet's printed answer is now THE official answer, and the independent check is no longer a
document join but an agent that solves the question having seen no answer at all.

## 6.4 The export, and why the page renders rather than links

`export_paper_v2.py` writes one CSV and one paper-like HTML per booklet. Three parts of it are
load-bearing enough to name, because each replaced something that looked fine and was not:

**`scripts/lib/texhtml.py` — LaTeX rendered at export time, with no network and no library.**
KaTeX and MathJax were both tried from a CDN, and both fail in the one place the output is actually
read: a local file opened in an editor preview, where external scripts are blocked. The page then
shows `$\frac{4}{9}$` as literal source, which is harder to read than either the rendered maths or
the plain text — the worst of the three outcomes. So the maths is rendered here into `<sup>`,
`<sub>` and a small CSS fraction, and the page needs nothing but itself.

It is deliberately NOT a LaTeX engine. It covers what `b3-question-reader` is instructed to emit and
leaves anything else VISIBLE IN RED rather than guessing: an unrendered `\overbrace` is a gap
someone can fix, a silently mangled one is a wrong answer that looks right. The symbol table was
built from a CENSUS of every `\command` the corpus actually contains, not from guesswork — which is
how `\,` was found, the most common thing in these stems after `\frac` (128 occurrences), printing
as a literal comma and turning `141\,kJ\,mol^{-1}` into "141,kJ,mol-1".

Two more things the renderer must do, because in these stems they are CONTENT and not formatting:

- **Newlines become `<br>`.** The booklet prints two thermochemical equations on two lines and the
  agent reads them as two lines; HTML collapses them into one unreadable sentence. Same damage for
  "Statement I / Statement II" and for any lettered part list.
- **Scripts render in PROSE too, not only inside `$...$`.** The text-layer draft writes `HNO_{3}`
  with no delimiters at all, because it is rebuilt from PDF span positions and never passes through
  a LaTeX writer. Rendering only inside `$` left every drafted formula showing its own braces.

**Tables are rebuilt, never shown as pictures.** `b3-question-reader` reads match-the-column items
into `list_i` / `list_ii` with each cell's own LaTeX, and statement lists into `statements`. Where
there is no image read yet, `parse_match_lists()` recovers the table from the FLATTENED stem — the
printed table interleaves its columns row by row, so the flattened text alternates letter-marker,
text, roman-marker, text, and that alternation is the signal. A stem that does not alternate is not
a match list and is left alone. A picture of a table cannot be searched, re-flowed on a narrow
screen, or checked against the options, so the crop is suppressed once the table is rebuilt.

**Every classification is LABELLED on the page, and says so when it is absent.** The header was a
row of bare chips, which is useless to the person checking the work: `Aldehydes, Ketones and
Carboxylic Acids` beside `Nucleophilic Addition Reactions` gives no way to tell which is the chapter
and which the subtopic. Now each row names itself — subject, stream, chapter, subtopic 1, subtopic 2
— and a field that was not assigned says `not mapped yet` or `blocked: needs a chapter first`
rather than vanishing. An absent row and an empty row look identical on a page and mean opposite
things. Subtopics are numbered because two are allowed and the ORDER is meaningful: the first is
what the answer turns on, the second a genuine second home, never a synonym.

Each assignment also carries the agent's own one-line `why` — the fact the CORRECT ANSWER depends
on. A reader who doubts a chapter needs the reason to disagree with; without it the only options are
to accept the label or re-derive the mapping from scratch.

## 6.5 Labels have to be readable, or they are codes

```bash
python3 scripts/build_label_glossary.py --apply
```

`config/allowed_values.yaml` carries the E1–E5 labels; `docs/question_categories/RULEBOOK.md`
carries what each one MEANS. Until this script existed only the labels reached the output, so a page
showed a question tagged `format_reflex_option` and gave the reader no way to know what that is, or
why this question has it.

It parses **133 definitions** out of the rulebook's own tables — 20 E1, 19 E2, 23 E3, 22 E4, 49 E5 —
plus each axis's name and the phrase that says what it decides ("E1 · Question type — the shape on
the page"). Parsed, never retyped: a gloss that has drifted from the rule is worse than none,
because the reader then checks the work against the wrong rule.

On the page each label shows three things: the label, what the rulebook says it means, and the
agent's own `trap_routes` entry for why THIS question has it. The rulebook requires specific
evidence per trap — `wrong_pairing` requires "which pair, which option" — so that last line is
exactly what a reviewer checks against the rule sitting above it.

**A gap it found:** all five `strategy_available` values (`elimination`, `estimation`, `symmetry`,
`dimensional_check`, `unit_sanity`) appear in the rulebook only as a bare list, with no definition
table. The page says "no definition in the rulebook" in red rather than inventing text. The other
128 are defined.

## 6.6 Chemistry stream and Biology branch — decided once, per chapter

```bash
# steps/QSTREAM/work/all.runA.input.json -> an agent -> steps/QSTREAM/out/all.runA.json
python3 -c "…"   # then fold into papers_v2/mappings/chapter_streams.json
```

Not a per-question step, and deliberately so. 59 chapters are classified once — 27 Chemistry into
`physical` / `inorganic` / `organic`, 32 Biology into `botany` / `zoology` / `both` — and every
question inherits from its chapter. That is 59 judgements instead of 1,869, and it lives in one file
a person can review in a minute.

`both` is preserved rather than forced: cell biology, cell cycle, biomolecules, molecular basis of
inheritance, both biotechnology chapters, evolution and principles of inheritance genuinely are
examined in both NEET sections. Each records which section it is USUALLY printed under, so a
consumer that cannot take `both` has a single-branch fallback.


## 6.7 The NCERT evidence map is MARKDOWN first; HTML on request

Owner's decision, 2026-10-21. `ncert_book_mapping/` carries `.md` per book plus the structured JSON
the mapping is generated from. HTML is NOT ruled out -- it is simply not built by default, because
building it costs a full export pass and the deliverable's value is the evidence rather than the
layout. Markdown renders well enough in an editor and in any review tool, and it diffs, which an
HTML page does not.

Because the `.md` is generated from the structured JSON rather than hand-written, an HTML view can
be added later from the same data without re-running a single agent. Build it when asked for.

The evidence agents already exist and do not need writing -- `d1-chapter-picker`, `d2-subtopic-picker`,
`d4-evidence-quoter`, `d6-status-note-writer`, `d7-latest-answer-checker` for the latest edition and
`d5-older-line-finder` for the older one. What they need is v2 input builders, because they read
`papers/records/` and this corpus lives in `papers_v2/`.

Two properties of D4 are worth knowing before relying on it: the agent is handed only 5-15 passages
from the chapter D1/D2 already chose, so it searches inside the assigned chapter rather than the
whole book; and **a script re-finds every quoted line in the book word for word and rejects anything
that is not there**. A paraphrased or invented line cannot survive, which is what makes "verified"
mean something. Its `supports_answer` field is `fully` / `partly` / `not_at_all`, with every
unsupported part listed in `missing`.

## 6.8 Evidence is routed by subject, and what each subject's evidence IS

A question's evidence is not the same KIND of thing in every subject, and treating it as one is what
the first wave of Stage D got wrong. Twelve evidence agents on physics and physical chemistry
returned `partly supported` over and over. Reading their reports together, the cause was never that
NCERT lacked the physics:

- the formula the solution needed is a DISPLAY EQUATION, carried as a separate image block, so the
  extracted passage text breaks off exactly where it sits -- `"Then Ohm's law states that  where the
  constant of proportionality R..."`, `"its kinetic energy K  is"`;
- or the constant lives inside a TABLE ROW (K_f for benzene, Henry's constant for nitrogen);
- or the relation is taught in ANOTHER CHAPTER (`F = ma` in Laws of Motion, `p = h rho g` in
  Mechanical Properties of Fluids).

Underneath all three is one fact: **a numerical's answer is a VALUE, and NCERT prints SENTENCES.**
There is no sentence to quote, so a part-matched paragraph gets quoted instead -- and that is worse
than no evidence, because it reads as evidence.

So the routing is by subject, and it is in code rather than left to whoever dispatches the step:

| subject | the evidence | step |
|---|---|---|
| Biology, Organic, Inorganic -- stated fact | the NCERT line, quoted and highlighted in the page's extracted text | D4V |
| Biology, Organic, Inorganic -- solving question | the NCERT line carrying the **formula, ratio or constant**, quoted and highlighted, **plus** the approach in words | D4V **and** QCA |
| Physics, Physical Chemistry | the CONCEPT (the relation) and the APPROACH (one line). No NCERT quotation. | QCA |

The middle row is the owner's correction and it is the one that keeps the split honest. Biology,
Organic and Inorganic content IS in NCERT, numericals included -- NCERT states the law of
segregation, the 9:3:3:1 ratio, the 0.34 nm rise per base pair, the solubility-product relation --
so the formula can be pointed at in the book. And a quoted constant still does not tell a reader
what to do with it, so the route is recorded beside it. What those subjects do NOT get is a route
under a stated fact: "which of the following is a hormone" has no approach, and inventing one is
padding dressed as method.

Whether a question "solves something" is read off its OWN record -- ECAT's E2 `format` is
`calculate_value`, or E4 `cognitive_demand` is `calculation`, or D4 recorded `derivation_steps` for
a `rule_used` / `rules_chained` link. Never inferred from the chapter name: Heredity asks both the
probability of an affected grandson and the name of an X-linked disorder.

**Where the routing lives:** `scripts/build_evidence_inputs.py` skips physics and physical chemistry
and reports them as routed; `scripts/qca_plugin.py` offers the in-scope questions, scoped by the
CONFIRMED subject and, for chemistry, by QCHAP's branch -- never by the positional guess, which was
wrong on all 43 checked questions of 2015 Code A and all 179 of 2017 Code C.

## 6.9 What a D4V agent may search, and why the shortlist is not a boundary

The evidence input ships a 15-passage shortlist ranked by word overlap. Nine of the first twelve
agents reported the same failure and three PROVED it: the one passage that settles a question was
not in the shortlist while a sibling question in the same run was handed it. `BIO12L-CH04-P39`
states the ABO gene I alleles verbatim; `PHY12L-CH03-P66` carries the negative-temperature
coefficient sentence; the Colour Blindness paragraph of 4.8.2 gives the 50 per cent figure.

A better ranker cannot fix this, because the ranking signal is the question's words and the book
states its facts in its own. What fixes it is letting the agent look. The input therefore carries:

- `chapter_index` -- every passage of the chapter with its section heading and page, i.e. the
  chapter's table of contents, so the agent can see that 4.8.2 exists;
- `search_this_file` -- the book file itself, which this step alone is permitted to open;
- `older_edition_passages` -- the older edition of the same chapter, because the 2023
  rationalisation cut sections a 2015 paper still asks (Meter Bridge, Potentiometer);
- `other_books_you_may_search` -- the subject's other books, because a fact can simply live
  elsewhere: polysome is described in Class XI *Cell: The Unit of Life*, not in Molecular Basis.

A quote fetched that way counts exactly as much as one from the shortlist -- the verifier checks
every quote against the book, not against the shortlist. `not_at_all` is only available after that
search, and the agent must name the sections and books it looked in.

**For Biology, `not_at_all` is almost always the search and not the book.** NEET Biology is written
FROM NCERT. The brief says so in those words, and the agents that hit it first are the reason.

## 7. Surviving format drift

The next source will differ again. What makes the flow survive it:

1. **Family is detected from page text, never the filename.** A new publisher adds one row to
   `FAMILIES`, not a new parser.
2. **An unrecognised text layout is `unknown_text`, not a crash and not a guess.** It is reported by
   `--probe` and skipped by the extractor until a fingerprint is added.
3. **Furniture is measured per document.** A different watermark on a different publisher's pages is
   caught by the same repeated-xref rule with no new constant.
4. **Header and footer are measured per page** from the running header's own baseline, so a new page
   size or margin needs no change.
5. **Geometry is in points internally and emitted in pixels** at `lib.pdf.DEFAULT_DPI`, matching
   every Stage A bbox and `schemas/B2.json`. A dpi change moves one constant.
6. **Answer markers are a list**, so a new wording is one regex.
7. **Scans are refused, not approximated**, and that includes a scan wearing a text layer
   (`ocr_scan`). The corpus stays auditable because every row came from a real text layer.
8. **Every per-page cost is bounded, so one bad file cannot stall a run.** Three guards, each put
   there by a file that actually broke the run:
   - `MAX_IMAGES_PER_PAGE` — a sliced-scan page's figure geometry is meaningless and is skipped and
     reported, never silently;
   - `MAX_PATHS_PER_PAGE` — same for a page of traced vector paths;
   - `FURNITURE_SAMPLE_PAGES` — the watermark scan reads a spread of pages rather than all of them,
     which costs nothing in accuracy because a watermark is on nearly every page by definition.
9. **Image rectangles come from one `get_image_info()` call per page, never `get_image_rects()` per
   image.** The second form costs a display-list search per image; on a page carrying 150+ fragments
   it did not finish a 27-page booklet, while the first returns in milliseconds. This was the single
   worst performance bug in the first version.
10. **A long run reports which booklet it is on.** The first version printed nothing until a booklet
    finished, so a stall was indistinguishable from slow progress and cost two debugging rounds.

## 8. Printed solutions, CDN images and the `data/` export (2026-10-26)

### 8.1 Where the sources live

`source_papers/NEET_Papers/<year>/[Set_<code>/]<booklet>.pdf`, git-ignored (third-party papers).
`rc.source_dir()` also honours the two older homes, `source_pdfs/papers_v2_sources/` and
`inputs/papers_v2_sources/`; `rc.corpus()` resolves `papers/` (current) or `papers_v2/` (older
checkout). Never hard-code either name: a glob over a missing folder reports zero work, silently.

### 8.2 The 2019-2021 solution gap is the booklets, not the regex

Measured with the extractor on the booklets it picks, nothing written:

| booklet | questions | printed answer found | solution marker | lines after the answer, no marker |
|---|---|---|---|---|
| 2019 P1 | 174 | 0 | 0 | 0 |
| 2020 F1 | 178 | 0 | 38 | 0 |
| 2021 O1 | 200 | 200 | 100 | 0 |

Read on the page: **2019 P1** prints bare questions and a one-page answer-key grid at the end, no
working anywhere. **2020 F1** prints neither answer nor working in its Biology half (q1-90); only
the Physics half carries `Solution` lines. **2021 O1** q101-200 are Vedantu-formatted (`Options:`,
then `Answer: (d)`) and stop at the answer line. So `SOLUTION_START` misses nothing in the corpus
booklets, and widening it would only add risk. The one place unmarked working exists is 2021's
subject-wise "with Solutions" files (35-41 of 50 questions each), which are not corpus booklets.
`text_layer_draft.unmarked_lines_after_answer` carries this count per question so the check can be
repeated on any new source.

### 8.3 What was added

| piece | where |
|---|---|
| `solution_lines` kept, marker stripped (on `solution_inline` the `Solution: (4)` line is both markers) | `read_text_draft()` |
| question crop stops at the printed `Answer`/`Sol.` line; solution crop cut from there to the next question, page/column continuations stitched | `extract()`, `cut_point()` |
| `b3s-solution-reader` (B3S): brief, schema, check, plugin, steps.yaml; printed answer withheld from its input; flags B3S_SOLUTION_CLIPPED / B3S_CONCLUDES_UNCLEAR / B3S_CONTRADICTS_PRINTED_ANSWER | `agents/`, `schemas/B3S.json`, `code/checks/B3S.py`, `code/b3s_plugin.py` |
| B6 `steps` (optional; old outputs split from `working`, never re-run) | `agents/b6-blind-solver.md`, `schemas/B6.json` |
| CDN upload of every crop, links carried across a re-extract by sha256 | `code/upload_paper_assets.py`, `code/cdn_login.py`, `code/lib/cdn.py` |
| `--data`: `data/<year>/<paper_code>/questions.json` + `question_paper.html`, byte-identical on re-run | `export_paper_v2.py` |

### 8.4 Two behaviour changes worth knowing

- **A re-extract clears the booklet's generated files** (JSON, crops, solutions, figures, exports) so
  every run is fresh, but **keeps agent answers** unless `--clear-agent-reads` is passed.
- **A booklet with no readable code is refused.** In the full Drive tree, 2021's code-less files all
  became `2021_NA` and overwrote one another.

## 9. Exact and redrawn figures, step-wise solutions, the LaTeX gate, one-command runs (2026-10-26)

### 9.1 Every figure has an EXACT copy, lifted from the PDF

`code/vector_figures.py`. These booklets are vector PDFs, so a figure is not redrawn to look like the
print. It is lifted out of it:

- the page is copied;
- every RASTER image is stripped (the watermark and the page background are images; the drawing is not);
- the publisher's `Answer (N)`/`Sol.` marker words are removed;
- everything outside the figure's box is deleted;
- the region is written as SVG, with text as the publisher's own glyph outlines.

Measured on 2017 Code-A: 42 figures, median 18 KB, no watermark. Degenerate zero-length paths
(`M0 0V0`, round caps) are stripped, because a browser draws them as dots. The SVG is declared at the
crop's size (dpi/72), not in points. A sliced-scan page has no vector art and keeps its PNG.

### 9.2 ...and a REDRAW from a checked card, beside it

The AI never draws: it writes a card, code checks it, and a renderer draws it (ncert_extractions
`docs/FIGURE_RENDERING_PLAN.md`).

| step | item | card | check | renderer |
|---|---|---|---|---|
| FIGC | a chemistry question | SMILES + name per drawn species, `orient`, `abbreviate` | RDKit parses; **OPSIN rebuilds the name** and the InChIKey must match | `lib/chem_cards.py` (RDKit, monochrome, CH3/NO2 as printed) |
| FIGP | a physics figure | primitives in maths coordinates + `angles_claimed` + `netlist` | renders; every claimed angle recomputed (1.5 deg); a circuit's netlist matched against its drawn wires | `lib/physics_figure.py` (pilot + capacitor, battery, inductor, switch, spring) |

`code/render_figure_cards.py` draws only cards that pass. A failed card is recorded with its reason.
`tools/` holds a portable Java 21 runtime and `opsin-cli-2.8.0` (git-ignored). Without them the name
check records `not_run`, never a pass.

Three renderer defaults changed from the pilot after the 2017_A review:

- `curve` is OPEN by default (before this, all 19 curves came out as closed blobs);
- `block` is plain unless `hatch` is set;
- hatching is clipped to the block.

### 9.3 Solutions: each figure at its step

B3S now returns `figures: [{bbox, after_step, kind}]`, one entry for every drawing in the solution.

- `cut_agent_figures.py` cuts them, and now undoes the stitcher's 10 px gap and horizontal centring
  exactly (`to_page()`).
- The export shows each figure under its step, with the whole printed block as a folded reference.
- In the JSON, `publisher_solution_figures[]` holds each figure's PNG, exact SVG and drawing, with
  their CDN links.

### 9.4 LaTeX: a census that is also a gate

`code/checks/latex_census.py` renders every field the page shows. It fails on:

- any unknown command;
- raw LaTeX left visible;
- an unpaired `$`;
- unbalanced braces.

`export_paper_v2.py --data` refuses to write while the census fails (`--allow-latex-gaps` overrides).

2017_A's first census found 6 unknown commands (57 uses: `\dfrac`, `\varepsilon`, `\textit`, `\ge`,
`\substack`, `\ddot`) and 15 raw leaks. All were fixed in `lib/texhtml.py`, which now also renders
`\ce{}`, stacked `\overset`/`\underset`, `\\` line breaks, and LaTeX commands written in prose
outside `$`.

### 9.5 One command

`.claude/workflows/neet-paper-pipeline.js` runs a booklet end to end, in this order:

1. extract;
2. B3V, then B3S;
3. figures and their vector copies;
4. B6V, QSUBJ, FIGC and FIGP together;
5. QCHAP→QTOPIC, beside E7V;
6. taxonomy gaps (`requeue_taxonomy_gaps.py` re-asks exactly the questions whose topic was minted);
7. cards;
8. CDN upload;
9. export through the LaTeX gate.

Every check is run, and failing items are retried once. `run_paper_pipeline.py` prints the same order
for a run by hand.
