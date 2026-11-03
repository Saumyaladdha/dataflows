# NCERT mapping — the job, and the design behind it

Two halves. **Part A is the work**: what to produce, where to put it, how to check it. **Part B is
the background** — what the data is, what was measured, and the table the files end up in. Part A
is enough to do the job; Part B is there when a decision needs explaining.

Everything is measured against the data as of 2026-10-30. Where a number appears, it was counted,
not estimated.

---

# PART A · What to produce

Your job is the mapping between the older NCERT and the current one. You produce JSON files; we
run a script that turns them into database rows. Nothing you write has to know anything about the
database.

Everything happens inside `data_flow/ncert_extractions/`.

---

## The three folders

```
data/
├── new_ncert/    the current NCERT        ← already here, 34 chapters
├── old_ncert/    the previous NCERT       ← you put the chapters here
└── mapping/      what changed             ← you produce this
```

**The path is identical in all three.** Only the first word changes:

```
new_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
old_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
mapping/  class_12/biology/ch01_sexual-reproduction-in-flowering-plants/pair.json
```

All 34 chapter folders are already created in `old_ncert/` and `mapping/`. They are empty.

---

## What it looks like when you are done

```
data/
│
├── new_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/
│       chapter.json                    already here, 97 nodes
│
├── old_ncert/class_12/biology/
│   ├── ch01_sexual-reproduction-in-flowering-plants/
│   │       chapter.json                you add this — the older chapter 2, 92 nodes
│   ├── ch02_human-reproduction/
│   │       chapter.json                the older chapter 3
│   └── _dropped/
│       ├── ch01_reproduction-in-organisms/chapter.json
│       ├── ch09_strategies-for-enhancement-in-food-production/chapter.json
│       └── ch16_environmental-issues/chapter.json
│
└── mapping/class_12/biology/
    ├── ch01_sexual-reproduction-in-flowering-plants/
    │       pair.json                   new ch1 = old ch2
    │       change.json                 the changes in this chapter
    ├── ch02_human-reproduction/
    │       pair.json
    │       change.json
    └── _dropped/
        └── ch01_reproduction-in-organisms/
                pair.json               "chapter_removed"
```

**Two files per chapter in `mapping/`.** `pair.json` is three lines. `change.json` is a list, one
entry per change — most paragraphs do not change, so it is shorter than the chapter.

You are only placing files in folders. There is no script for you to run.

---

## Step 1 · Put the older chapters in `old_ncert/`

The older biology chapters are in `~/Downloads/DATA_NCERT/`:

```
OLD_ncert_class11_bio/    22 chapters
OLD_ncert_class12_bio/    16 chapters
```

Copy each `chapter.json` into `old_ncert/`, into the folder **named after the current edition's
chapter**:

```
OLD_ncert_class12_bio/ch02_sexual-reproduction-in-flowering-plants/chapter.json
   →  data/old_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
```

The old chapter number is already inside the file at `chapter.number`. The folder name comes from
the current edition, because that is the edition students read today.

### Chapters that no longer exist

Three class-12 chapters were removed from the current NCERT. They have no folder in `new_ncert/`,
so put them under `_dropped/` with their **own** old name:

```
old_ncert/class_12/biology/_dropped/ch01_reproduction-in-organisms/chapter.json
old_ncert/class_12/biology/_dropped/ch09_strategies-for-enhancement-in-food-production/chapter.json
old_ncert/class_12/biology/_dropped/ch16_environmental-issues/chapter.json
```

Class 11 went from 22 chapters to 19, so it has its own removals. Working those out is part of
step 2.

---

## Step 2 · `pair.json` — which old chapter is which

**Do this before step 3.** The diff has to know which two chapters to compare. Comparing chapter 1
against chapter 1 is wrong wherever the numbering shifted, and in class 12 it shifted for twelve
of the thirteen chapters.

One file per chapter: `mapping/class_12/biology/ch01_…/pair.json`

```json
{
  "latest": { "chapter_no": 1, "reprint": "2026-27",
              "title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS" },
  "older":  { "chapter_no": 2, "reprint": "2022-23",
              "title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS" },
  "matched_on": "title"
}
```

For a removed chapter, under `mapping/class_12/biology/_dropped/ch01_…/pair.json`:

```json
{
  "latest": null,
  "older":  { "chapter_no": 1, "reprint": "2022-23",
              "title": "REPRODUCTION IN ORGANISMS" },
  "verdict": "chapter_removed",
  "affects_answers": true
}
```

`matched_on` is how you decided: `"title"` where the titles are the same, `"content"` where you had
to read the chapter to be sure.

### Class 12 is already worked out

| old | new | title |
|---|---|---|
| 2 | 1 | Sexual Reproduction in Flowering Plants |
| 3 | 2 | Human Reproduction |
| 4 | 3 | Reproductive Health |
| 5 | 4 | Principles of Inheritance and Variation |
| 6 | 5 | Molecular Basis of Inheritance |
| 7 | 6 | Evolution |
| 8 | 7 | Human Health and Disease |
| 10 | 8 | Microbes in Human Welfare |
| 11 | 9 | Biotechnology: Principles and Processes |
| 12 | 10 | Biotechnology and its Applications |
| 13 | 11 | Organisms and Populations |
| 14 | 12 | Ecosystem |
| 15 | 13 | Biodiversity and Conservation |
| **1** | — | **Reproduction in Organisms — removed** |
| **9** | — | **Strategies for Enhancement in Food Production — removed** |
| **16** | — | **Environmental Issues — removed** |

13 paired, 3 removed, all 16 accounted for. **Class 11 (22 → 19) still has to be done.**

### Check before moving on

| | |
|---|---|
| every old chapter appears exactly once | 22 old chapters → 22 `pair.json` entries |
| every `"latest": null` chapter sits under `_dropped/` | |
| no two old chapters point at the same new chapter | |
| 22 old chapters in the sheet, 22 folders on disk | a mismatch means one was missed |

---

## Step 3 · `change.json` — what changed inside the chapter

One file per chapter: `mapping/class_12/biology/ch01_…/change.json`

A JSON **list**. One entry per change. An unchanged paragraph gets no entry — there is nothing to
record, and most paragraphs are unchanged (measured: 60–90% are word-for-word identical).

```json
[
  {
    "n": 1,
    "change_type": "edited",

    "from": { "id": "p_RO3LHI", "chapter_no": 2, "reprint": "2022-23",
              "address": "Ch 2 › 2.1", "page": 6,
              "body": "The number of species that are known and described range between 1.7-1.8 million." },

    "to":   { "id": "p_yXCbmf", "chapter_no": 1, "reprint": "2026-27",
              "address": "Ch 1 › 1.1", "page": 4,
              "body": "The number of species that are known and described range between 20 million." },

    "diff": [
      { "op": "same", "text": "The number of species that are known and described range between " },
      { "op": "del",  "text": "1.7-1.8" },
      { "op": "ins",  "text": "20" },
      { "op": "same", "text": " million." }
    ],
    "similarity": 0.94,

    "verdict": "fact_changed",
    "why": "The species count changed from 1.7-1.8 million to 20 million.",
    "affects_answers": true
  }
]
```

### The four change types

| `change_type` | when | fields |
|---|---|---|
| `edited` | the text changed | `from` + `to` + `diff` |
| `moved` | same text, different place in the chapter | `from.address` + `to.address`, one `body` is enough |
| `removed` | in the older edition, gone from the current one | `from` only, `to: null` |
| `added` | new in the current edition | `to` only, `from: null` |

### `id` is how paragraphs are linked

Every node in `chapter.json` has an `id` like `p_NiISDE`. Use **those** in `from.id` and `to.id`.

Do not link on position. Position shifts whenever a chapter is re-extracted; the id does not.
Checked across all 70 chapters: **no id is missing and none is duplicated**, so this is safe.

### `diff` — put it in the file, do not leave it to the app

The `diff` array is what lets the final page show `1.7-1.8 million` struck out and `20 million`
beside it. Three operations: `same`, `del`, `ins`. Concatenating the `same` and `del` text must
reproduce `from.body` exactly; `same` plus `ins` must reproduce `to.body`.

If the app had to compute this, every app would need the same algorithm and they would drift. In
the file, it is computed once and every surface shows the same thing.

### `verdict` — the judgement, and the point of the whole exercise

`change_type` is mechanical. `verdict` is the judgement, and it is the field everything downstream
actually uses.

| `verdict` | meaning |
|---|---|
| `fact_changed` | a stated fact is different — past exam answers may now be wrong |
| `fact_removed` | the fact is gone — past questions on it are out of syllabus |
| `fact_added` | new material, no past questions exist |
| `wording_only` | rewritten, same fact, nothing to review |

Two real examples that a diff calls identical and a reader does not:

```
1.7-1.8 million  →  20 million
   fact_changed · a past question asking for this number is now wrong

"Fungi multiply and spread easily due to the millions of asexual spores they produce"
   →  "Fungi spread easily because they produce millions of asexual spores"
   wording_only · same fact, nothing to review
```

Set `affects_answers: true` on `fact_changed` and `fact_removed`, `false` on the others.

### Check before moving on

| | |
|---|---|
| **no `change.json` has `moved: 0` AND `edited: 0`** | **this is the important one** |
| every `edited` entry has both `from.body` and `to.body` | |
| every entry has a `verdict` | |
| `diff` reconstructs both bodies exactly | |
| every `from.id` / `to.id` exists in the matching `chapter.json` | |

**On the first check:** a file containing only `added` and `removed`, with nothing `moved` and
nothing `edited`, means nothing matched — which means the wrong two chapters were compared. Go back
to `pair.json`.

This has already happened once. `CHG_BIO12-ch01.json` holds 94 added and 92 removed with zero
matches, because *Reproduction in Organisms* was compared against *Sexual Reproduction in Flowering
Plants* — two unrelated chapters. All 186 of those rows are worthless. The check above catches it
in one line.

---

## Step 4 · Optional · `report.md`

A short human-readable summary per chapter. Useful for review, safe to delete, nothing reads it.

---

## What we do after you hand it over

```
your mapping/  →  export script  →  JSON rows  →  load into DynamoDB
```

You never touch the database and never need to know its shape. If your files pass the checks
above, the load works.

---

## Summary of what to produce

| file | where | how many |
|---|---|---|
| `chapter.json` | `old_ncert/class_NN/biology/chNN_…/` | 38 (22 + 16) |
| `pair.json` | `mapping/class_NN/biology/chNN_…/` | 38 |
| `change.json` | `mapping/class_NN/biology/chNN_…/` | 70 |

Class 12's pairing is in step 2 and can be copied. Class 11's pairing, and every `change.json`, is
the work.

---

## The order is not optional

```
old_ncert/ files  →  pair.json  →  change.json  →  verdicts
```

Each step reads the one before it. Running the diff before the pairing produces a change log that
**looks finished and is wrong**, which is far harder to spot than a missing file.

---
---

# PART B · The data, and the table it loads into

Background for whoever runs the export and the load. Not needed to produce the files in Part A.

Handoff note. Written 2026-10-30 against the data in `~/Downloads/DATA_NCERT` and the pipeline in
`data_flow/ncert_extractions`. Every count in this document was measured, not estimated; the
command that produced it is given so you can re-run it.

---

### 1. What is on disk right now

```
~/Downloads/DATA_NCERT/
  new_ncert_class11_bio/    ch1 … ch19        19 chapters   latest, reprint 2024-25
  new_ncert_class12_bio/    ch1 … ch13        13 chapters   latest, reprint 2026-27
  OLD_ncert_class11_bio/    ch01 … ch22       22 chapters   older,  reprint 2022-23
  OLD_ncert_class12_bio/    ch01 … ch16       16 chapters   older,  reprint 2022-23
  papers_extracted/         8 NEET papers
```

**70 NCERT chapters, both editions, 6,709 content nodes, 1,402 files.**

Validated: all 70 `chapter.json` parse, none broken, none missing a required top-level field.

```
Biology only. There is NO physics and NO chemistry NCERT in this set.
```

Note two things about editions before you design anything around them:

| book | edition | reprint |
|---|---|---|
| BIO11L | latest | **2024-25** |
| BIO12L | latest | **2026-27** |
| BIO11O | older | 2022-23 |
| BIO12O | older | 2022-23 |

"Latest" is **not one edition**. Class 11's latest is 2024-25 and class 12's is 2026-27. When
NCERT reprints class 11 again, a third version appears and the word "latest" moves. **Key on the
reprint year, never on the word "latest".** See §6.

---

### 2. What one `chapter.json` holds

### Top level

| key | what it is |
|---|---|
| `book`, `book_id` | `BIO12`, `BIO12L` — the trailing `L`/`O` is the edition |
| `grade`, `subject`, `lang` | `12`, `biology`, `EN` |
| `edition` | `latest` or `older` |
| `reprint` | `2026-27` — **this is the real edition identifier** |
| `reprint_inferred` | whether the reprint was read off the page or guessed |
| `chapter` | `{ number, title }` |
| `pages`, `unit_pages`, `unit_page_records` | which PDF pages this chapter covers |
| `design_key`, `sheet_pt` | which measured book design renders it |
| `source_pdf` | the file it came from |
| **`tree`** | **the content — a nested array of nodes** |
| `passages` | passage groupings (step A3) |
| `text_join`, `layout_join`, `special_join`, `structure_join`, `consumer_finalise` | per-step join reports; audit trail, not content |

### A node inside `tree`

Nodes nest through `children`. Measured on one chapter (125 nodes):

| key | on how many | what it is |
|---|---|---|
| `kind` | all | `para` · `section` · `question` · `figure` · `list` · `summary` · `exercises` · `chapter_title` |
| `id` | all | **stable id, e.g. `p_NiISDE`** — use this to link, never the position |
| `pages`, `page_file` | all | which printed page |
| `boxes` | all | where on the page it sits |
| `source`, `qa` | all | which step produced it, and its check result |
| `body`, `body_md` | 97 | the text |
| `sentences` | 95 | the text split into sentences |
| `passage_id` | 87 | which passage it belongs to |
| `marks` | 71 | bold / italic spans |
| `print_font`, `print_size_pt`, `ink` | 109 | measured typography |
| `caption`, `caption_*` | 16 | figure captions |
| `image`, `image_sha256` | 10 | figure image |
| `children` | 12 | nested nodes |

Node kinds across all 70 chapters:

```
para 3,663 · section 960 · question 891 · figure 670 · list 171
chapter_title 153 · exercises 70 · summary 69
```

**The 891 `question` nodes are NCERT's own end-of-chapter exercises.** They are already
extracted and already attached to their chapter. Nobody has used them yet; they are a product in
themselves.

---

### 2.1 Is the JSON sound? — validated

Every one of the 70 `chapter.json` files was checked field by field:

| check | result |
|---|---|
| files that parse | **70 of 70** |
| nodes | **6,709** |
| missing `book_id` / `grade` / `subject` / `edition` / `reprint` / `lang` / `chapter` / `tree` | **none** |
| missing `chapter.number` or `chapter.title` | **none** |
| nodes with no `id` | **0** |
| duplicate `id` within a chapter | **0** |
| reprints found | 2026-27 (13) · 2024-25 (19) · 2022-23 (38) |

**No `id` is missing and none is duplicated.** That is the property the whole mapping rests on:
`from_id` → `to_id` only works if every node has a stable, unique id.

One thing the check surfaced and then cleared: 1,027 `section` and `summary` nodes carry no
`body`. **1,018 of them have `children`** — they are containers wrapping other nodes, which is
correct. Only **9 of 6,709** (0.13%) have neither body nor children; each carries a `fill`
attribute, so they are tinted panels picked up as empty sections. Harmless, and not worth fixing.

**The extraction is sound. What is missing is the mapping, not the data.**

---

### 3. The agents, and which have run

Fifteen agents exist in `data_flow/ncert_extractions/agents/`:

| agent | step | what it does | run on this data? |
|---|---|---|---|
| `a1-book-registrar` | A1 | registers a book from its first pages | yes |
| `a2-page-reader` | A2 | reads ONE page image into ordered blocks | yes |
| `a2-special-transcriber` | A2S | transcribes a table, figure caption or equation | yes |
| `a2b-bold-marker` | A2B | backfills bold spans | yes |
| `a2i-italic-marker` | A2I | backfills italic spans | yes |
| `a2l-layout-reader` | A2L | measures the printed layout of a page | partial |
| `a2n-notation-fixer` | A2N | restores exponents, subscripts, radicals | partial |
| `a2c-structure-transcriber` | A2C | reads a drawn chemical structure to SMILES | n/a (biology) |
| `a2r-render-reviewer` | A2R | reviews the render against the PDF, page by page | yes |
| `a2v-extraction-verifier` | A2V | verifies nothing was invented or dropped | yes |
| `a3-passage-splitter` | A3 | splits a section into one-idea passages | yes (`passage_id` present) |
| `a4-subtopic-writer` | A4 | drafts the NEET-testable subtopic list | yes |
| `a5-passage-linker` | A5 | links a passage to a subtopic where the heading does not settle it | **NO** (but `ST#` rows exist from headings) |
| `figp-figure-redrawer` | FIGP | redraws a figure as a checked spec | partial |
| **`a8-change-judge`** | **A8** | **judges an old↔new passage pair** | **NO — 0 outputs, never run** |

Two gaps matter:

- **A5 never ran as an agent**, but subtopics are NOT missing. The exported rows already carry
  `ST#` items holding `subtopic_key`, `name`, `passages` and `node_ids`, derived from the printed
  headings (`from_heading`). So "every NCERT passage for this subtopic" IS answerable. What A5
  would add is linking a passage to a subtopic where the heading does not settle it.
- **A8 never ran.** This is the edition-change judge. See §4.

---

### 4. Mapping — what it is, and what is actually done

Mapping has **two levels**. Neither is finished.

### Level 1 · Chapter ↔ chapter

Which old chapter became which new chapter. Worked out from the printed titles:

**Class 12 — 16 old chapters, 13 new.**

| old | new | title |
|---|---|---|
| ch02 | ch1 | Sexual Reproduction in Flowering Plants |
| ch03 | ch2 | Human Reproduction |
| ch04 | ch3 | Reproductive Health |
| ch05 | ch4 | Principles of Inheritance and Variation |
| ch06 | ch5 | Molecular Basis of Inheritance |
| ch07 | ch6 | Evolution |
| ch08 | ch7 | Human Health and Disease |
| ch10 | ch8 | Microbes in Human Welfare |
| ch11 | ch9 | Biotechnology: Principles and Processes |
| ch12 | ch10 | Biotechnology and its Applications |
| ch13 | ch11 | Organisms and Populations |
| ch14 | ch12 | Ecosystem |
| ch15 | ch13 | Biodiversity and Conservation |
| **ch01** | — | **Reproduction in Organisms — REMOVED** |
| **ch09** | — | **Strategies for Enhancement in Food Production — REMOVED** |
| **ch16** | — | **Environmental Issues — REMOVED** |

13 paired by title, 3 removed, 16 of 16 accounted for. Class 11 (22 → 19) has not been worked
out yet and will have its own removals.

**Those three removed chapters are why 23 of 90 biology questions in NEET 2017 could not be
traced to any current NCERT line.** A removed chapter is the single most valuable fact in this
whole dataset: it tells you which past questions are now out of syllabus.

### Level 2 · Node ↔ node

Which paragraph became which paragraph. This is what a `change` row carries:

```
from_id  p_lVIhjG   ← the old paragraph
to_id    p_5iZTGX   ← the new paragraph
```

Only **changed** nodes get a row. An unchanged paragraph gets none — there is nothing to record.

**Done so far: 2 chapters of 70.** `CHG_BIO11-ch01` (62 rows) and `CHG_BIO12-ch01`.

Change types measured on BIO11 ch01: `moved` 25 · `removed` 27 · `edited` 10.

### The defect to fix before running the other 68

The current `edited` row stores **one** body and a similarity score:

```json
{ "change_type": "edited", "from_id": "p_RO3LHI", "to_id": "p_yXCbmf",
  "body": "If you look around you will see...", "note": "similarity 1.00" }
```

So you learn **that** a paragraph changed, never **what** changed. A reader cannot see
`1.7-1.8 million` become `20 million`.

Also: that row says `similarity 1.00`, meaning identical, while being typed `edited`. Either the
similarity is computed wrongly or the type is wrong. **Check those 10 rows before generating
~2,000 more**, or a share of the change log will be false.

Fix the row shape first — see §6.5.

### What A8 adds that a script cannot

A script can say *what* changed, exactly, character by character. It cannot say whether it
**matters**:

| | |
|---|---|
| `1.7-1.8 million` → `20 million` | **fact changed** — a past answer may now be wrong |
| "Fungi multiply and spread easily due to the millions of asexual spores they produce" → "Fungi spread easily because they produce millions of asexual spores" | **wording only** — nothing changes |

A diff calls both "edited". Only a reader can tell them apart, which is exactly what
`a8-change-judge` was written for and why its brief says:

> *The change log must separate real fact changes from rewording, because changed facts can
> change past answers.*

This same pattern — script proposes, agent judges — was used on the NEET 2017 NCERT lines and
caught real errors: one question's "best" retrieved line was about AIDS prevention, another was a
generic sentence about the digestive system that said nothing about the cells being asked for.
Both would have shipped as evidence if the script had been trusted.

---

### 5. What is missing, in priority order

| | state |
|---|---|
| Biology extraction, both editions | **done** — 70 chapters, JSON clean |
| Chapter pairing (level 1) | **not stored** — class 12 worked out in §4, class 11 not started |
| Node changes (level 2) | **2 of 70 chapters** |
| A8 judgement on changes | **never run** |
| Subtopic linking (A5) | **never run** |
| Physics / Chemistry NCERT | **does not exist** |
| Load into DynamoDB | partial, and **blocked by a key collision** — see §6.1 |

---

### 6. The table

One table. Reprint year in the key. Version in the sort key.

```
Table   ncert_content
PK      String
SK      String
GSI1    GSI1PK / GSI1SK
Billing on-demand
```

### 6.1 Two bugs in the current rows — fix before loading

**A · Primary key collision.** Rows on disk today:

```
BIO11L ch01   PK = CH#BIO11-01#EN   SK = N#001   edition = latest
BIO11O ch01   PK = CH#BIO11-01#EN   SK = N#001   edition = older
```

Identical `PK` + `SK`. In DynamoDB that is the primary key, so **loading one silently overwrites
the other**. Only one old chapter is loaded today; loading more would have destroyed the latest
data with no error. For class 12 it is worse — old ch01 is *Reproduction in Organisms* and new
ch01 is *Sexual Reproduction in Flowering Plants*, two unrelated chapters sharing one key.

Fix: put the reprint in the partition key.

**B · Stale rows on re-extract.** DynamoDB has no "replace this partition" operation. A chapter
with 97 nodes re-extracted down to 90 leaves rows `N#091`–`N#097` alive as orphans, and the
chapter then reads with seven phantom paragraphs and no error anywhere.

Fix: version the sort key (`V2#N#001`) and point `active_version` at it from the chapter row.

### 6.2 Book

```
PK  BOOK#BIO12
SK  REPRINT#2026-27
```
```json
{ "kind": "book", "book": "BIO12", "grade": 12, "subject": "biology", "lang": "EN",
  "reprint": "2026-27", "edition_label": "latest", "chapters": 13, "source_pdf": "..." }
```

### 6.3 Chapter

```
PK  CH#BIO12#2026-27#01#EN
SK  META
```
```json
{ "kind": "chapter",
  "GSI1PK": "SUB#biology#12#2026-27", "GSI1SK": "CH#01",
  "chapter_no": 1, "chapter_title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS",
  "nodes": 97, "active_version": 2,
  "maps_to": { "reprint": "2022-23", "chapter_no": 2 } }
```

### 6.4 Content node — one per paragraph, figure, question

```
PK  CH#BIO12#2026-27#01#EN
SK  V2#N#002
```
```json
{ "kind": "para",
  "GSI1PK": "SUB#biology#12#2026-27", "GSI1SK": "CH#01#N#002",
  "id": "p_NiISDE", "chapter_no": 1,
  "body": "Biology in essence is the story of life on earth...",
  "body_md": "...", "sentences": [ ... ], "boxes": [ ... ], "pages": [4],
  "passage_id": "BIO12L-CH01-P03",

  "was_id": "p_lVIhjG",
  "change": "edited" }
```

The older edition's row is the same shape under its own key, carrying `now_id` instead of
`was_id`:

```
PK  CH#BIO12#2022-23#02#EN
SK  V1#N#005
```

`was_id` / `now_id` sit **on the node** so a reader gets the counterpart while reading the
chapter — no second query, no index. The `change` rows in §6.5 keep the detail.

A figure node is the same row with `kind: "figure"` plus `caption`, `image` (CDN url),
`image_drawn` (our own SVG) and `image_local` (the crop).

### 6.5 Change — both lines, and the diff

```
PK  CH#BIO12#2026-27#01#EN
SK  CHG#003
```
```json
{ "kind": "change",
  "change_type": "edited",

  "from": { "id": "p_RO3LHI", "reprint": "2022-23", "chapter_no": 2,
            "address": "Ch 2 › 2.1", "page": 6,
            "body": "The number of species that are known and described range between 1.7-1.8 million." },

  "to":   { "id": "p_yXCbmf", "reprint": "2026-27", "chapter_no": 1,
            "address": "Ch 1 › 1.1", "page": 4,
            "body": "The number of species that are known and described range between 20 million." },

  "diff": [ { "op": "same", "text": "The number of species that are known and described range between " },
            { "op": "del",  "text": "1.7-1.8" },
            { "op": "ins",  "text": "20" },
            { "op": "same", "text": " million." } ],
  "similarity": 0.94,

  "verdict": "fact_changed",
  "why": "The species count changed from 1.7-1.8 million to 20 million.",
  "affects_answers": true }
```

| `change_type` (script) | meaning | fields |
|---|---|---|
| `edited` | the text changed | `from` + `to` + `diff` |
| `moved` | same text, different place | `from.address` + `to.address` |
| `removed` | in the older edition, deleted from the new | `from` only, `to: null` |
| `added` | new in the latest edition | `to` only, `from: null` |

| `verdict` (A8) | meaning |
|---|---|
| `fact_changed` | a stated fact is different — review past questions |
| `fact_removed` | the fact is gone — past questions are out of syllabus |
| `fact_added` | new material |
| `wording_only` | rewritten, same fact, nothing to review |

**Store the `diff` in the row, do not compute it in the app.** Computed client-side, every app
needs the same algorithm and they will drift. Stored, the pipeline computes it once, every
surface renders identically, and the claim is auditable. The cost is bytes, and there are none to
spare worry about: the largest node in the whole corpus is 16 KB against a 400 KB item limit.

### 6.6 Chapter mapping

```
PK  PAIR#BIO12#2022-23_to_2026-27
SK  LATEST#01
```
```json
{ "kind": "pair", "latest_chapter_no": 1, "older_chapter_no": 2,
  "chapter_title": "SEXUAL REPRODUCTION IN FLOWERING PLANTS", "matched_on": "title" }
```

A chapter deleted outright:

```
PK  PAIR#BIO12#2022-23_to_2026-27
SK  DROPPED#01
```
```json
{ "kind": "pair", "latest_chapter_no": null, "older_chapter_no": 1,
  "chapter_title": "REPRODUCTION IN ORGANISMS",
  "verdict": "chapter_removed", "affects_answers": true }
```

**A dropped chapter can live nowhere else.** It has no row in the latest edition, because it has
no chapter in the latest edition. This item type is the only place that fact can be recorded.

### 6.7 Compare run — the tracking row

```
PK  DIFF#BIO12#2022-23_to_2026-27
SK  CH#01
```
```json
{ "kind": "diff_run", "status": "done", "compared_at": "2026-10-30",
  "changes": 62,
  "counts": { "edited": 10, "moved": 25, "removed": 27, "added": 0 },
  "judged": 62, "fact_changed": 4, "wording_only": 6 }
```

One query answers "which chapters have been compared, and which have not". Today that question
cannot be answered at all, which is why it took a file listing to discover only 2 of 70 are done.

### 6.8 Book design

```
PK  STYLE#BIO12
SK  V1
```
```json
{ "kind": "style",
  "page": { "trim_mm": [215.9, 276.58], "measure_mm": 127.0 },
  "type": { "body_pt": 10.5, "leading": 1.27 } }
```

---

### 6.9 What one chapter actually looks like in the table

Real rows for Class 12 Biology chapter 1, both editions:

| PK | SK | kind | what it holds |
|---|---|---|---|
| `CH#BIO12#2026-27#01#EN` | `META` | chapter | SEXUAL REPRODUCTION IN FLOWERING PLANTS |
| `CH#BIO12#2026-27#01#EN` | `V1#N#001` | para | Chapter 1 Sexual Reproduction in flowering Plants |
| `CH#BIO12#2026-27#01#EN` | `V1#N#002` | para | Biology in essence is the story of life on earth… |
| `CH#BIO12#2026-27#01#EN` | … | | **97 nodes in total** |
| `CH#BIO12#2026-27#01#EN` | `V1#N#045` | figure | PANCHANAN MAHESHWARI (1904-1966) |
| `CH#BIO12#2026-27#01#EN` | `ST#01` | subtopic | from the printed heading |
| `CH#BIO12#2026-27#01#EN` | `CHG#001` | change | edited — both bodies plus the diff |
| `CH#BIO12#2022-23#02#EN` | `META` | chapter | the older chapter 2, same title |
| `CH#BIO12#2022-23#02#EN` | `V1#N#001` | chapter_title | CHAPTER 2 |
| `CH#BIO12#2022-23#02#EN` | … | | **92 nodes in total** |
| `PAIR#BIO12#2022-23_to_2026-27` | `LATEST#01` | pair | new ch1 = old ch2 |
| `PAIR#BIO12#2022-23_to_2026-27` | `DROPPED#01` | pair | Reproduction in Organisms |
| `DIFF#BIO12#2022-23_to_2026-27` | `CH#01` | diff_run | status: done |
| `BOOK#BIO12` | `REPRINT#2026-27` | book | 13 chapters |
| `STYLE#BIO12` | `V1` | style | measured page design |

**The first word of `SK` says what a row is.** Nobody has to read documentation to tell a
paragraph from a change from a chapter pairing.

### A figure row

Figures are ordinary nodes with `kind: "figure"`. Real example from that chapter:

```json
{ "PK": "CH#BIO12#2026-27#01#EN",
  "SK": "V1#N#045",
  "kind": "figure",
  "id": "f_OExVn8",
  "caption": "PANCHANAN MAHESHWARI (1904-1966)",
  "image": "https://d30lmobgrc5gb8.cloudfront.net/general/23102026/ncert/2026-27/BIO12L/ch01/i002_fig01-78720802_23102026.png",
  "image_sha256": "787208028ffcd41d…" }
```

The CDN url is already on the node — the figures have been uploaded. `image_sha256` is what lets
a re-upload be skipped when the picture has not changed. Where the pipeline has drawn its own
version of a figure, the node also carries `image_drawn` (an SVG) and `image_local` (the crop);
`image` is the CDN url and stays the reference copy.

This chapter has 16 figures.

---

### 6.10 Most of the content is identical between editions

Measured on Class 12, comparing each paired chapter paragraph by paragraph:

| pair | old nodes | new nodes | **identical** | only in old | only in new |
|---|---|---|---|---|---|
| old 2 → new 1 | 92 | 97 | **58** | 34 | 39 |
| old 3 → new 2 | 57 | 57 | **34** | 23 | 23 |
| old 5 → new 4 | 117 | 115 | **63** | 54 | 52 |
| old 7 → new 6 | 47 | 46 | **33** | 14 | 13 |
| old 14 → new 12 | 78 | 50 | **41** | **37** | 9 |
| old 15 → new 13 | 50 | 51 | **46** | 4 | 5 |

**60% to 90% of paragraphs are word-for-word identical.** Two extremes are worth naming:

- **ch13 Biodiversity** — 46 of 50 unchanged. Almost nothing moved.
- **ch12 Ecosystem** — 37 paragraphs deleted against only 9 added. Heavily cut.

Three consequences:

**An identical paragraph produces no change row.** There is nothing to record. Those 58 identical
paragraphs in chapter 1 cost nothing in the change log.

**An identical chapter produces `change.json: []`** and `pair.json` carrying `"identical": true`.

**Both editions' nodes are still stored.** Rendering the older chapter needs its own text in its
own order, and deduplicating would put a join on every paragraph read.

### Why the identical paragraphs are the valuable half

A past question resting on a paragraph that is identical in both editions is **safe**. One resting
on a paragraph that is `removed` or `fact_changed` needs review.

The `only in old` column is a syllabus-coverage number in its own right: Ecosystem lost 37
paragraphs and Biodiversity lost 4, so the old Ecosystem questions are far more exposed than the
old Biodiversity ones. **That comparison cannot be made today** — it needs the mapping.

---

### 7. Queries

| question | query |
|---|---|
| a chapter, in printed order | `PK = CH#BIO12#2026-27#01#EN`, `SK begins_with V2#N#` |
| a chapter and all its changes | `PK = CH#BIO12#2026-27#01#EN` |
| the whole chapter mapping | `PK = PAIR#BIO12#2022-23_to_2026-27` |
| which chapters were removed | same PK, `SK begins_with DROPPED#` |
| which facts changed | `PK = CH#…`, `SK begins_with CHG#`, filter `verdict = fact_changed` |
| every chapter of a book | GSI1 `GSI1PK = SUB#biology#12#2026-27` |
| how much has been compared | `PK = DIFF#BIO12#2022-23_to_2026-27` |
| where a paragraph used to be | read the chapter; the node carries `was_id` |

---

### 8. Row counts

| | rows |
|---|---|
| content nodes, 70 chapters, both editions | 6,709 |
| chapter rows | 70 |
| book rows | 4 |
| chapter pairs | ~38 |
| compare-run rows | ~70 |
| style rows | 4 |
| change rows (still to generate) | ~2,000 |
| **total** | **~8,900** |

Largest item 16 KB. Nothing here is a scale problem.

---

### 8.1 Production readiness

**The structure is production grade.** Single table with composite PK/SK, prefixes that make each
row self-describing, keys derived from the access patterns rather than from the data's shape, item
sizes 25× under the limit, and linking on stable `id` rather than on position. A chapter is one
query. Nothing here needs rethinking.

Three operational items are open. One is fixed in this document; two are deliberately deferred.

### Fixed here · no arrow in a primary key

```
PAIR#BIO12#2022-23→2026-27        wrong — a non-ASCII character in a primary key
PAIR#BIO12#2022-23_to_2026-27     correct
```

It works in DynamoDB, but a primary key travels through URLs, logs, the CLI, CSV exports and
support tickets. Keep every key plain ASCII. This document now uses `_to_` throughout.

### Deferred · old versions are never deleted

`SK` carries the extraction version (`V1#N#001`, `V2#N#001`) so that re-extracting a chapter
cannot leave orphan rows behind — the real bug it exists to prevent. The cost is that superseded
versions live forever: ten re-extractions leave ten copies of a chapter.

**Not a problem at this scale and not worth solving yet.** 8,900 rows with a handful of versions is
nothing. It becomes real when a book is re-extracted repeatedly, so the decision is recorded now
rather than discovered later:

- **Option A — TTL.** Stamp superseded rows with an expiry and let DynamoDB delete them. Free, but
  the rows vanish on DynamoDB's schedule, not yours.
- **Option B — cleanup job.** When `active_version` advances, delete the rows of the version two
  behind. Keeps exactly two versions, so a rollback is always possible.

Option B is the better fit — a rollback target is worth more here than saved storage. Build it when
a book has been re-extracted more than twice, not before.

### Deferred · concurrent loaders overwrite each other

Two loaders running at once will silently overwrite one another's rows, last write winning with no
error. Only matters once more than one loader exists; add a `ConditionExpression` then.

---

### 9. Order of work

1. **Check the 10 `edited` rows that say `similarity 1.00`.** Identical text typed as edited is
   either a bad similarity or a bad type. Settle it before generating ~2,000 more rows.
2. **Fix the exporter's key** — reprint in `PK`, version in `SK`. Loading old chapters today
   overwrites latest chapters silently.
3. **Add `from.body`, `to.body` and `diff` to the change row**, and `was_id` / `now_id` to nodes.
4. **Work out the class 11 chapter pairing** (22 → 19) the way class 12 was done in §4, and
   write `PAIR` rows for both classes.
5. **Generate change rows for the remaining 68 chapters.**
6. **Run `a8-change-judge` over every change** — this is what turns a diff into a usable
   statement about the syllabus.
7. **Write `DIFF#` tracking rows** as each chapter completes.
8. Then: A5 subtopic linking, and physics / chemistry extraction.

Steps 1–3 are small and must come before 5, or the work has to be redone.

---

### 9.1 How to run it

Everything below already exists in `data_flow/ncert_extractions/code/`. Nothing has to be written
from scratch — the gap is that these have not been run on the full corpus, not that they are
missing.

Run from the repo root: `cd data_flow/ncert_extractions`

### Step 0 · Bring the older edition into `data/`

`data/old_ncert/` exists with all 34 chapter folders mirrored, but it is **empty**. The older
biology chapters are in `~/Downloads/DATA_NCERT/OLD_ncert_class11_bio/` (22) and
`OLD_ncert_class12_bio/` (16).

Copy each `chapter.json` into the folder **named after the new edition's chapter**:

```
~/Downloads/DATA_NCERT/OLD_ncert_class12_bio/ch02_sexual-reproduction-in-flowering-plants/chapter.json
  →  data/old_ncert/class_12/biology/ch01_sexual-reproduction-in-flowering-plants/chapter.json
```

The old chapter number stays inside the file at `chapter.number`; the folder name comes from the
new edition. Chapters with no new counterpart go under `_dropped/` with their own old name.

**Nothing downstream can run until this is done** — there is nothing to compare against.

### Step 1 · Extract a chapter (only if it is not already extracted)

```bash
python code/run_chapter.py BIO11O-ch02
python code/run_chapter.py --old --class 11 --subject biology --chapter 2
python code/run_chapter.py BIO11O-ch02 --upload      # also push figures to the CDN
```

The `O` / `L` in the id is the edition. All 70 chapters in `DATA_NCERT` are already extracted, so
this is only for new material.

### Step 2 · Chapter pairing — **before any diff**

The pairing must exist before the change rows, or the wrong chapters get compared. This is not a
theoretical risk: it is exactly how `CHG_BIO12-ch01.json` ended up with 94 added, 92 removed and
zero matches.

Class 12's pairing is worked out in §4 of this document. Class 11 (22 → 19) still has to be done
the same way — match on printed title, and record every old chapter with no counterpart as
`DROPPED`.

### Step 3 · Build the change rows

```bash
python code/build_change_rows.py --book BIO11 --chapter 1     # one chapter
python code/build_change_rows.py --all                        # everything
```

Two fixes are needed in this script before running it across the corpus:

1. **Read the pairing** instead of comparing chapter number to chapter number.
2. **Write `from.body`, `to.body` and `diff`** — today it writes one body and a similarity score,
   so a reader cannot see what changed.

### Step 4 · Judge each change

```bash
python code/run_step.py A8 --list     # what needs judging
python code/run_step.py A8 --check    # validate the answers
```

`a8-change-judge` decides `fact_changed` / `fact_removed` / `fact_added` / `wording_only`. A diff
cannot make that call; see §4.

### Step 5 · Build the rows

```bash
python code/export_rows.py BIO11O-ch02
python code/export_rows.py --all
```

Writes the flat JSON row lists under `data/dynamodb/`.

### Step 6 · Load

```bash
python code/load_to_dynamodb.py --all --dry-run
python code/load_to_dynamodb.py --chapter BIO11O-ch02 --table ncert_content
python code/load_to_dynamodb.py --all --region ap-south-1
```

The table name in the loader already defaults to **`ncert_content`**, which is the name used
throughout this document.

**Always run `--dry-run` first.** Until the key fix in §6.1 lands, loading an older chapter will
silently overwrite the corresponding latest chapter, with no error.

### Checks to run after each step

| after | check | a failure means |
|---|---|---|
| step 2 | every old chapter appears exactly once, as `LATEST#` or `DROPPED#` | a chapter is unaccounted for |
| step 3 | no `change.json` has `moved: 0` **and** `edited: 0` | the wrong chapters were compared |
| step 3 | every `edited` row has both `from.body` and `to.body` | the diff is unreadable |
| step 4 | every change row carries a `verdict` | A8 did not finish |
| step 5 | no two rows share a `PK` + `SK` | the key collision of §6.1 |
| step 6 | row count loaded matches row count exported | a partial load |

### The order is not optional

```
old_ncert/ files  →  pairing  →  change rows  →  A8 judgement  →  export  →  load
```

Each step consumes the one before it. Running the diff before the pairing produces a change log
that looks complete and is wrong, which is harder to notice than a missing file.

---

### 10. Things to carry forward

- **Link on `id`, never on position.** `SK` ordering shifts whenever a chapter is re-extracted;
  `id` (`p_NiISDE`) does not. The existing change rows already use `from_id`/`to_id` — that part
  is right and should stay.
- **Key on the reprint year, not on the word "latest".** Class 11's latest is 2024-25 and class
  12's is 2026-27; the word moves and the year does not.
- **Unchanged paragraphs are stored twice**, once per edition. That is deliberate: rendering an
  old chapter needs its own text in its own order, and deduplicating would put a join on every
  paragraph read. The cost is storage, which is negligible here.
- **`reprint_inferred`** marks chapters whose reprint year was guessed rather than read off the
  page. Check it before trusting a year in a key.
