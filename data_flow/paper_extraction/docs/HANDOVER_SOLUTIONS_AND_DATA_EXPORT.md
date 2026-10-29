# Handover — printed solutions, CDN images, and the `data/` export

**For:** whoever picks up the paper-extraction pipeline next, and their agents.
**Goal:** every NEET question in this corpus ends up in `paper_extraction/data/<year>/<paper_code>/`
as one JSON and one HTML, carrying the question, **the publisher's printed worked solution**, our
own independent solve, the classification, and CDN links for every image.

Read sections 0, 2 and 13 before writing any code. Everything else is per-task.

---

## 0. Read first, in this order

| file | why |
|---|---|
| `docs/PAPER_EXTRACTION_V2.md` | the corpus, the families, and every threshold with the measurement that set it. The single most important document here. |
| `../ncert_extractions/LESSONS.md` | every defect this project has shipped and the rule that stops it |
| `../_shared/code/CONVENTIONS.md` | the script/runner contract. Rules 4 and 7 are load-bearing (see §13) |
| `config/steps.yaml` | every step's declaration: agent, inputs, schema, check, fallback, flags |

**Environment.** Use `data_flow/.venv/bin/python` (3.14). The macOS system `python3` is 3.6 with an
ASCII default and silently truncates these files at the first non-ASCII byte. Required packages:
`pymupdf pillow numpy pyyaml jsonschema`.

---

## 1. What this pipeline is, in 60 seconds

A NEET question paper PDF becomes structured questions through a chain of **steps**. Each step has
a letter-number ID (`B3V`, `QCHAP`, `E7V`), one declaration in `config/steps.yaml`, a JSON Schema
in `schemas/`, a check module in `code/checks/`, and — if it is an agent step — a markdown brief in
`agents/`.

A step is either:

- **script** — runs itself: `python code/run_step.py <STEP> --auto`
- **agent** — a person or a Claude session dispatches it: `--list` prints one line per item, you
  invoke the named subagent once per line, then `--check` validates and re-lists until `DONE`
- **hybrid** — `script | agent-name`, script half resolves what it can, agent decides the rest

A script never calls an agent. That is CONVENTIONS rule 7 and it is not negotiable.

The live v2 flow:

```
extract_paper_v2.py   pick the source PDF by measured chars/page, cut question + figure crops
assign_subject.py     subject from the paper's own printed section headings
B3V   agent           read each question from its IMAGE          <- the record
cut_agent_figures.py  cut the figure boxes the agent reported
B6V   agent           solve it with the printed answer withheld
export_paper_v2.py    CSV, HTML and JSON per booklet
QSUBJ -> QCHAP -> QTOPIC -> E7V                                   the classification chain
```

---

## 2. The state today — measured, not estimated

Counts are from `papers/exports/json/questions_v2_all.json`, regenerate with
`python code/export_paper_v2.py --json`.

**10 booklets, 1,869 questions**, one booklet per year 2015–2024.

| what | filled | of 1,869 |
|---|---|---|
| question read from its own image (B3V) | **358** | 19% |
| still on the text-layer draft **and flagged unrepresentable** | **637** | the quality risk |
| publisher's printed answer | 1,506 | 81% |
| independent AI solve (B6V) | 358 | 19% |
| answers disagree | **8** | worth a human read |
| chapter assigned | 799 | 43% |
| subtopic assigned | 774 | 41% |
| difficulty banded | 353 | 19% |
| questions with a figure crop | 169 (212 crops) | 9% |
| **printed solutions available but discarded** | **1,451** | **78% — this handover** |

Per-year solution availability, which decides where to start:

| year | solutions printed | of | family |
|---|---|---|---|
| 2015 | 175 | 177 | `aakash_classic` |
| 2016 | 180 | 181 | `aakash_classic` |
| 2017 | 178 | 179 | `aakash_classic` |
| 2018 | 180 | 180 | `aakash_classic` |
| **2019** | **0** | 174 | `solution_inline` |
| **2020** | **38** | 178 | `solution_inline` |
| **2021** | **100** | 200 | `solution_inline` |
| 2022 | 200 | 200 | `aakash` |
| 2023 | 200 | 200 | `aakash` |
| 2024 | 200 | 200 | `aakash` |

---

## 3. What you are building

| # | task | kind | blocks on |
|---|---|---|---|
| 1 | stop discarding the printed solution lines | script | — |
| 2 | cut a solution crop per question | script | 1 |
| 3 | **B3S · solution-reader** — read the solution from its image | **new agent** | 2 |
| 4 | `ai_solution_stepwise` — split B6V's prose into steps | schema + brief | — |
| 5 | CDN upload for paper images | script | — |
| 6 | the `data/<year>/<paper_code>/` JSON + HTML export | script | 1–5 |

Do them in that order. 1, 4 and 5 are independent and can run in parallel.

---

## 4. Target output layout

Everything lands here, mirroring how the NCERT side files its built chapters:

```
paper_extraction/data/
  2015/
    2015_A/
      question_paper.html          the whole booklet, one page, offline-openable
      questions.json               every question, the schema in §11
      q002.html                    optional: one question per page
  2016/
    2016_X/
      ...
  2024/
    2024_Q2/
      ...
```

Rules for this folder:

- `data/` is **committed**. It is the deliverable.
- One folder per `paper_code`, which is `<year>_<booklet_code>` — `2015_A`, `2024_Q2`.
- The HTML must open from disk with **no network**: no CDN stylesheet, no CDN script, no web
  font. See §12.
- Images are referenced by **CDN URL first**, with the local path as a fallback attribute, so the
  page works both online and from a clean clone.
- Writing this folder must be **idempotent**: running the exporter twice produces byte-identical
  files. No timestamps in the output.

---

## 5. Task 1 — keep the solution lines

**File:** `code/extract_paper_v2.py`, function `read_text_draft()`, around line 752.

Today every line of the worked solution is thrown away:

```python
if solution_at is not None:
    continue          # <- the solution dies here
```

Only the index survives (`solution_at`, `answer_at`). The lines are already in hand at this point,
so this is a small change.

**Do:** collect the lines from `solution_at` to the end of the question's line list into
`solution_lines: [str]` and return it on the draft dict, beside `solution_at` / `answer_at`.

**Watch out — the `solution_inline` family.** In 2019/2020/2021 the booklet prints
`Solution: (4)` as a single line that is **both** the answer marker and the solution marker:
`SOLUTION_START` and `ANSWER` both match it, and `solution_at == answer_at`. So the solution text
starts **on** that line, not after it. Handle both cases.

**Before writing the regex work, do this 10-minute check.** 2019 reports 0 solutions out of 174,
2020 reports 38 of 178, 2021 reports 100 of 200. Either those booklets genuinely print no working,
or `SOLUTION_START` misses their wording. **The two look identical in the counts and need opposite
fixes.** Open one page of each and look. Record what you find in this file.

The current pattern, for reference:

```python
SOLUTION_START = re.compile(r"^\s*(?:Sol\s*[.:]|Solution\s*[.:]|Hide\s+solution)", re.I)
```

**Done when:** `papers/papers/<paper_id>.json` carries `text_layer_draft.solution_lines` for 1,451+
questions, and re-running the extractor changes nothing else.

---

## 6. Task 2 — cut the solution crop

**File:** `code/extract_paper_v2.py`, the same geometry pass that cuts the question crop.

The question crop is deliberately clipped at the `Answer (N)` line, so the solution is in neither
the crop nor (after task 1 alone) a trustworthy text form. Cut it as its own image.

- **from:** the `answer_at` line's top
- **to:** the next question's first line, or the page's text-bottom if the solution runs to the
  page end
- **write to:** `papers/solutions/<paper_id>/q###.png`
- **record on the question:** `solution_image`, and the bbox used

A solution that spans a page break produces **more than one crop**, in order. Do not drop the
continuation — a half-solution read as whole is the exact failure mode this project keeps catching.

Reuse the existing furniture/watermark exclusion. The watermark rule is document-level and by
xref; do not reinvent it.

**Done when:** `papers/solutions/` holds one or more crops for each of the 1,451 questions that
have a solution, and a sample of 10 opened by eye show the working and nothing of the next
question.

---

## 7. Task 3 — the `B3S · solution-reader` agent

This is the step that makes the solution text trustworthy. **It mirrors `b3-question-reader`
(B3V) exactly** — read `agents/b3-question-reader.md` first and follow its shape.

### Why an agent and not a text parse

The same reason B3V exists. The text layer cannot represent a stacked fraction — numerator, drawn
bar and denominator are three unrelated objects on three rows. Measured on 2015 Code-A: question
170 prints options `4/9, 9/4, 121/49, 49/121` and the text layer yields `"9 9", "4 121", "49 49",
"121"`. A worked solution is *nothing but* fractions, radicals and exponents, so it is the worst
case for a text parse, not the best.

So `solution_lines` from task 1 is a **draft and a cross-check, never the record** — exactly as
`text_layer_draft` is for the stem.

### Files to create

| file | content |
|---|---|
| `agents/b3s-solution-reader.md` | the brief — copy the structure of `b3-question-reader.md` |
| `schemas/B3S.json` | the output schema |
| `code/checks/B3S.py` | the check |
| `config/steps.yaml` → `B3S:` entry | `stage: B`, `item: question`, `needs: B3V`, `fallback: [retry]` |
| `code/step_plugins.py` → `B3SPlugin` | registered in `get_plugins()` |

### Input the agent receives

```json
{
  "paper_id": "2015_A",
  "qno": 2,
  "solution_image": "solutions/2015_A/q002.png",
  "solution_lines_draft": ["...", "..."],
  "question_text": "...",
  "options": {"1": "...", "2": "...", "3": "...", "4": "..."}
}
```

The question and options are given **so the agent can say which option the working lands on**. It
is not asked to solve anything.

### Output

```json
{
  "solution_stepwise": [
    "$\\mathrm{Gd}$ has atomic number $Z = 64$, so $64$ electrons must be placed.",
    "The $[\\mathrm{Xe}]$ core accounts for $54$, leaving $64 - 54 = 10$ beyond it.",
    "A half-filled $4f$ subshell is extra-stable, so the ten are placed $4f^{7}5d^{1}6s^{2}$.",
    "Hence the configuration is $[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$."
  ],
  "concludes": "1",
  "has_figure": false,
  "figure_bbox": null,
  "complete": true,
  "note": ""
}
```

### Rules the brief must state

1. **Copy, never solve.** The agent transcribes the publisher's reasoning. If the publisher's
   working is wrong, it is copied as printed and said so in `note`. This step is not a solver.
2. **LaTeX for everything** — every number with a unit, every formula, every chemical formula,
   every Greek letter, every exponent and subscript. Same rule as B3V.
3. **One step per printed step.** Do not merge the publisher's steps into a paragraph and do not
   invent steps it did not write.
4. **`concludes` is what the WORKING arrives at**, which may differ from the printed `Answer (N)`.
   That disagreement is the point of the field — see §11 `verdict_self`. If the working does not
   clearly land on an option, `"unclear"`.
5. **`complete: false`** when the crop is cut off at an edge. A clipped solution transcribed as
   whole is worse than one reported clipped, because nothing downstream can then tell.
6. **A solution figure is not transcribed here.** Set `has_figure` and `figure_bbox` and let the
   figure transcriber handle it, exactly as B3V does.
7. Never reconstruct scrambled notation into what it "should" say. Copy what is legible, mark the
   span, flag it in `note`.

### Flags

```yaml
B3S_SOLUTION_CLIPPED: normal
B3S_CONCLUDES_UNCLEAR: low
B3S_CONTRADICTS_PRINTED_ANSWER: high    # concludes != publisher_answer
```

That last flag is a new defect class nothing currently catches: a booklet printing `Answer (3)`
above a solution that works out to 1. Today you would only find it by reading 1,451 solutions.

### Running it

```bash
python code/run_step.py B3S --list          # one line per unread solution
# invoke b3s-solution-reader once per line
python code/run_step.py B3S --check         # repeat until DONE
```

---

## 8. Task 4 — `ai_solution_stepwise`

`b6-blind-solver` already returns `working` as one prose string. Add a `steps: [str]` field to its
output so the AI's reasoning is step-by-step like the publisher's, and renders the same way.

- edit `agents/b6-blind-solver.md` — add `steps` to the output shape and one rule: *one step per
  move, LaTeX throughout, do not merge*
- edit `schemas/B6.json` — add `steps`, array of strings, not required (the 358 existing outputs
  must stay valid)
- the exporter falls back to splitting `working` on sentence boundaries where `steps` is absent

**Do not re-run the 358 existing solves to backfill this.** They are valid; a split of their
`working` is good enough, and a re-run costs agent calls for cosmetics.

---

## 9. Task 5 — CDN upload for paper images

Copy the working implementation from the NCERT side — do not write a new one.

| from | to |
|---|---|
| `../ncert_extractions/code/cdn_login.py` | `code/cdn_login.py` (unchanged) |
| `../ncert_extractions/code/upload_assets.py` | `code/upload_paper_assets.py` |

Point it at three sources and write back three pairs:

| image | local field | CDN field |
|---|---|---|
| question crop `papers/crops/<paper_id>/q###.png` | `question_image` | `question_image_cdn` |
| figure crops `papers/figures/<paper_id>/*.png` | `figures[].local` | `figures[].cdn_url` |
| solution crops `papers/solutions/<paper_id>/q###.png` | `solution_image` | `solution_image_cdn` |

Keep `sha256` on every uploaded image. That is what makes a re-run free: a crop whose bytes have
not changed is not uploaded again.

```bash
python code/cdn_login.py --phone <number>              # sends an OTP
python code/cdn_login.py --phone <number> --otp 1234   # prints the export lines
export ARIVIHAN_TOKEN=...  ARIVIHAN_USER_ID=...
python code/upload_paper_assets.py --paper-id 2015_A --dry-run
python code/upload_paper_assets.py --paper-id 2015_A
```

**The credential is never written to disk.** It is read from `ARIVIHAN_TOKEN` /
`ARIVIHAN_USER_ID` at run time. `.gitignore` already blocks `.env`, `*.pem`, `*.key` and
`cdn.json`. Do not add a config file for it, do not print it, do not commit it.

**Order matters: build → upload → re-export.** Re-running the extractor after an upload used to
discard every URL. Always upload after the crops are final, then export.

---

## 10. Task 6 — the `data/<year>/<paper_code>/` export

**File:** `code/export_paper_v2.py`. It already writes CSV, HTML and JSON into
`papers/exports/`. Add a `--data` mode that writes the layout in §4.

Reuse this file's existing merge helpers — **do not write a second assembler.** They are:

```
reading()            the agent's read where there is one, else the draft
agent_read()         B3V output
solved_answer()      B6V output
confirmed_subject()  QSUBJ, or the printed heading
chapter_topic()      QCHAP + QTOPIC
stream_and_branch()  derived per chapter
difficulty_of()      E7V
taxonomy_gap()       the chapter/topic the agent wanted and could not find
verdict()            publisher vs AI
is_key_grid()        a "question" that is really a row of the printed answer key
```

Two new helpers to add alongside them: `publisher_solution(paper_id, qno)` reading `steps/B3S/out/`,
and `verdict_self(publisher_answer, concludes)`.

A note on paths: the tree was re-filed into `data_flow/` after these scripts were written, so what
the code calls `papers_v2/` is now `papers/` and `inputs/` is now `source_pdfs/`. A `_dir()`
resolver at the top of `export_paper_v2.py` handles both. Use it; do not hard-code either name.

---

## 11. The JSON schema

One file per booklet at `data/<year>/<paper_code>/questions.json`:

```json
{
  "schema": "neet-pyq/question-record/v2",
  "paper_code": "2015_A",
  "meta": { "...": "the booklet: family, layout, pages, option_style, source_pdf, sha256_16" },
  "counts": { "...": "roll-ups" },
  "questions": [ "... one record per question, below ..." ]
}
```

One question record, every field:

```json
{
  "question_id": "2015_A__q002",
  "paper_code": "2015_A",
  "year": 2015,
  "booklet_code": "A",
  "qno": 2,

  "question_text": "Gadolinium belongs of $4f$ series. Its atomic number is $64$. Which of the following is the correct electronic configuration of gadolinium?",
  "options": {
    "1": "$[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$",
    "2": "$[\\mathrm{Xe}]4f^{6}5d^{2}6s^{2}$",
    "3": "$[\\mathrm{Xe}]4f^{8}6d^{2}$",
    "4": "$[\\mathrm{Xe}]4f^{9}5s^{1}$"
  },
  "statements": [],
  "list_i": [],
  "list_ii": [],
  "structure": "plain",
  "negative_words_seen": [],

  "publisher_answer": "1",
  "publisher_answer_text": "$[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$",
  "publisher_answer_starred": false,
  "publisher_solution_stepwise": [
    "$\\mathrm{Gd}$ has atomic number $Z = 64$, so $64$ electrons must be placed.",
    "The $[\\mathrm{Xe}]$ core accounts for $54$, leaving $64 - 54 = 10$ electrons beyond it.",
    "A half-filled $4f$ subshell is extra-stable, so the ten are placed $4f^{7}5d^{1}6s^{2}$ rather than $4f^{8}6s^{2}$.",
    "Hence the configuration is $[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$."
  ],
  "publisher_concludes": "1",
  "solution_image": "solutions/2015_A/q002.png",
  "solution_image_cdn": "https://cdn.arivihan.com/pyq/2015_A/sol_q002.png",

  "ai_answer": "1",
  "ai_answer_text": "$[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$",
  "ai_solution_stepwise": [
    "$[\\mathrm{Xe}]$ core $= 54$ electrons; $64 - 54 = 10$ electrons remain.",
    "Place them as $4f^{7} + 5d^{1} + 6s^{2} = 7 + 1 + 2 = 10$, the half-filled-$f$ exception.",
    "This matches option $1$."
  ],
  "ai_why": "$\\mathrm{Gd}$ ($Z = 64$) is a half-filled-$f$ exception: $[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$, which option $1$ states.",
  "ai_confidence": "high",

  "verdict_answer": "agree",
  "verdict_self": "agree",

  "subject": "Chemistry",
  "subject_from": "confirmed by q-subject-confirmer (position had guessed Physics)",
  "subject_why": "Tests the $4f$-block electronic configuration of gadolinium, which is inorganic atomic structure.",
  "subject_confidence": "high",
  "agrees_with_position": false,
  "stream": "inorganic",
  "branch": null,

  "chapter_code": "CHENEETENGDFB",
  "chapter_name": "The D- and F-Block Elements",
  "chapter_why": "The answer turns on the lanthanoid electronic configuration of $\\mathrm{Gd}$, the $4f^{7}5d^{1}6s^{2}$ half-filled-$f$ exception taught with the $f$-block series.",
  "chapter_confidence": "high",

  "subtopic_1_id": "neet_chemistry_the_d_and_fblock_elements_practice_electronic_configurations_of_the_dblock_fblock_practice",
  "subtopic_1_name": "Electronic Configurations of the d-Block & f-Block",
  "subtopic_1_why": "The answer depends on knowing the $f$-block filling order and the half-filled-$4f$ exception that makes $\\mathrm{Gd}$ $[\\mathrm{Xe}]4f^{7}5d^{1}6s^{2}$.",
  "subtopic_2_id": null,
  "subtopic_2_name": null,
  "subtopic_2_why": null,
  "taxonomy_gap": "",

  "difficulty_level": "easy",
  "difficulty_steps": 1,
  "difficulty_step_list": ["recall the configuration of $\\mathrm{Gd}$ ($Z = 64$) as the half-filled-$4f$ exception"],
  "difficulty_why": "A single recall of a configuration the $f$-block chapter states explicitly as an exception.",
  "what_makes_it_hard": "Options $1$ and $2$ both account for the ten electrons beyond $[\\mathrm{Xe}]$, so counting alone cannot choose between them.",

  "figures": [
    {
      "role": "stem_figure",
      "kinds": ["image"],
      "page": 9,
      "crop_bbox": [36.1, 1600.4, 932.9, 1872.6],
      "target_box_in_crop": [38.9, 38.9, 857.9, 233.2],
      "local": "figures/2015_A/q030_stem_figure_1.png",
      "cdn_url": "https://cdn.arivihan.com/pyq/2015_A/q030_stem_figure_1.png",
      "sha256": "4f1c9ab3…",
      "caption": "",
      "labels": []
    }
  ],

  "source_pdf": "NEET_Papers/2015/NEET_2015_Code_A_official.pdf",
  "page": 1,
  "question_image": "crops/2015_A/q002.png",
  "question_image_cdn": "https://cdn.arivihan.com/pyq/2015_A/q002.png",
  "read_from": "agent",
  "read_note": "Excluded the publisher's printed working block below the options.",
  "text_layer_reliable": true,
  "needs_image_read": false,

  "status": {
    "question": "done",
    "publisher_solution": "done",
    "ai_solution": "done",
    "subject": "done",
    "chapter": "done",
    "subtopic": "done",
    "difficulty": "done",
    "figures": "done",
    "categories": "excluded"
  },
  "pending": []
}
```

### Allowed values

| field | values |
|---|---|
| `structure` | `plain` · `statements` · `list` · `match` · `table` · `assertion_reason` · `statement_i_ii` |
| `negative_words_seen` | `NOT` · `EXCEPT` · `INCORRECT` · `FALSE` · `WRONG` |
| `publisher_answer` · `publisher_concludes` · `ai_answer` | `"1"`–`"4"` · `"unsure"` · `"unclear"` · `null` |
| `verdict_answer` | `agree` · `differs` · `ai_unsure` · `unchecked` |
| `verdict_self` | `agree` · `publisher_contradicts_itself` · `unclear` · `unchecked` |
| `subject` | `Physics` · `Chemistry` · `Biology` |
| `stream` | `physical` · `inorganic` · `organic` · `null` |
| `branch` | `botany` · `zoology` · `both` · `null` |
| `difficulty_level` | `easy` · `medium` · `hard` · `unsure` |
| `*_confidence` | `high` · `medium` · `low` |
| `figures[].role` | `stem_figure` · `option_panels` |
| every `status.*` | `done` · `unsure` · `not_run` · `excluded` · `none` |

### `status` and `pending` are not decoration

Four values, and they mean different things:

- `done` — a step ran and answered
- `unsure` — a step ran and judged that the vocabulary did not fit. **This is a real answer**, and
  for a chapter it must be accompanied by `taxonomy_gap` naming what was wanted
- `not_run` — the work is still owed. `pending` lists it by step
- `excluded` — deliberately out of scope (E1–E5 categories)

**A blank with a reason and a field nobody has judged must never look the same.** That is SPEC
Rule 19 and the most frequently violated rule in this project's history. An exporter that simply
omits what is missing collapses the distinction and the gap stops getting fixed.

### LaTeX everywhere

Every text field carries LaTeX, not just the stem and options:
`publisher_solution_stepwise`, `ai_solution_stepwise`, `ai_why`, `subject_why`, `chapter_why`,
`subtopic_*_why`, `difficulty_why`, `difficulty_step_list`, `what_makes_it_hard`.

Backslashes are doubled in JSON — `$[\\mathrm{Xe}]$` on disk is `$[\mathrm{Xe}]$` in the data. Do
not hand-edit these files.

---

## 12. The HTML requirements

`data/<year>/<paper_code>/question_paper.html` — one page per booklet, reproducing the paper so a
person can check the extraction against the printed original by eye.

The existing `write_html()` / `question_card()` in `export_paper_v2.py` already renders the
question, options, classification, difficulty and figures. **What is missing is the solutions
block.** Verified: the current HTML contains no publisher solution anywhere.

### Add to each question card

```
┌─ Q2 ────────────────────────────── Chemistry · inorganic · easy ─┐
│  [question text, LaTeX rendered]                                  │
│  (1) …   (2) …   (3) …   (4) …          ← correct option marked   │
│                                                                   │
│  ── The publisher's solution ──────────  Answer (1)  ───────────  │
│   1. Gd has atomic number Z = 64 …                                │
│   2. The [Xe] core accounts for 54 …                              │
│   3. A half-filled 4f subshell …                                  │
│   → concludes: option 1                                           │
│   [solution crop image]                                           │
│                                                                   │
│  ── Solved independently (answer withheld) ──  AI: 1 · high ────  │
│   1. [Xe] core = 54 electrons …                                   │
│   2. Place them 4f7 + 5d1 + 6s2 …                                 │
│                                                                   │
│  verdict: agree                                                   │
│                                                                   │
│  chapter   The D- and F-Block Elements                            │
│            why: the answer turns on …                             │
│  subtopic 1  Electronic Configurations of the d-Block & f-Block   │
│            why: …                                                 │
│  difficulty  easy · 1 step · why: …                               │
└───────────────────────────────────────────────────────────────────┘
```

### Non-negotiables for the HTML

1. **No network.** No CDN stylesheet, no CDN script, no web font. KaTeX and MathJax from a CDN
   were both tried and both fail where this page is actually read — a local file in an editor
   preview, where external scripts are blocked, so every formula shows as literal `$\frac{4}{9}$`
   source. LaTeX is rendered **at export time** by `code/lib/texhtml.py`, which needs nothing but
   itself.
2. **Unrenderable LaTeX shows in red, never guessed.** `texhtml.py` already does this. An
   unrendered `\overbrace` is a gap someone can fix; a silently mangled one is a wrong answer that
   looks right. Expect the first export after the solution work to surface a few new red commands —
   that is the renderer working. Add them to the symbol table from a **census** of what the corpus
   actually contains, never from guesswork.
3. **Newlines become `<br>`.** In these stems a line break is content, not formatting — two
   thermochemical equations on two lines, "Statement I / Statement II", lettered part lists.
4. **Images use the CDN URL with the local path as fallback**, so the page works online and from a
   clean clone.
5. **Every classification is labelled, and says so when absent.** A row that was not assigned reads
   `not mapped yet` or `blocked: needs a chapter first` — never a blank. An absent row and an empty
   row look identical and mean opposite things.
6. **Nothing is tidied for presentation.** A question with fewer than four options, no printed
   answer, a clipped solution, or `text_layer_reliable: false` is **marked on the page**. The
   export exists to find those, not to hide them.
7. **Tables are rebuilt as tables, never shown as pictures.** A picture of a match-list cannot be
   searched, reflowed, or checked against the options.

---

## 13. Rules you must not break

These are each here because breaking them already cost this project a corpus.

1. **`b6-blind-solver` must never see an answer.** Not the printed `Answer (N)`, not a key, not
   the publisher's solution text, not a question crop that includes the marked option. Its entire
   value is that it has seen none. `publisher_solution_stepwise` must not appear anywhere in B6's
   input — separate row, separate build path. The checkmark on a correct option is a *shape*, not a
   colour, and survives greyscaling, so a naive crop leaks the answer silently.
2. **The text layer is a draft, never the record.** This applies to the solution exactly as it
   applies to the stem. A pure text parse of 2024 Code-Q2 scored 100% on answers and 99.8% on
   four-option questions **and was still unsafe**, because it cannot represent a stacked fraction.
3. **A script never calls an agent and never makes a network call** (CONVENTIONS rule 7). The one
   documented exception is the CDN upload, which is an ingest, not a judgement, and is cached.
4. **Every script is idempotent** (CONVENTIONS rule 4). Running the same command twice produces
   the same bytes and does no new work. No timestamps in output files.
5. **Never invent a taxonomy value.** An agent that cannot find the right chapter answers `unsure`
   and fills `proposed_chapter`. A question forced into the nearest chapter is wrong forever and
   looks right.
6. **Refuse rather than approximate.** A scanned booklet is skipped, not OCR'd into the same
   corpus. An unrecognised layout is `unknown_text`, not a guess.
7. **Carry provenance that cannot be reconstructed later.** `read_from`, `text_layer_reliable`,
   `subject_from`, `figure source` — once these are dropped, no later step can recover them.
8. **Never add a threshold without the measurement that set it**, in a comment beside it. Every
   constant in `extract_paper_v2.py` has one. Match that.

---

## 14. How to run and verify

```bash
cd data_flow/paper_extraction
PY=../.venv/bin/python

# 1 extraction (scripts only)
$PY code/extract_paper_v2.py --year 2015 --apply
$PY code/assign_subject.py --apply

# 2 agents — dispatched, not automatic
$PY code/run_step.py B3V --list      # read each question from its image
$PY code/run_step.py B3V --check
$PY code/run_step.py B3S --list      # read each printed solution   <- new
$PY code/run_step.py B3S --check
$PY code/run_step.py B6V --list      # solve with the answer withheld
$PY code/run_step.py B6V --check

# 3 classification — order is NOT optional
$PY code/run_step.py QSUBJ  --list && $PY code/run_step.py QSUBJ  --check
$PY code/run_step.py QCHAP  --list && $PY code/run_step.py QCHAP  --check
$PY code/run_step.py QTOPIC --list && $PY code/run_step.py QTOPIC --check
$PY code/run_step.py E7V    --list && $PY code/run_step.py E7V    --check

# 4 images
$PY code/upload_paper_assets.py --paper-id 2015_A

# 5 export
$PY code/export_paper_v2.py --data
```

**QSUBJ must run before QCHAP.** The chapter list handed to QCHAP is chosen *by subject*, so a
wrong subject means a wrong closed list and the agent can only answer `unsure`. QCHAP refuses a
question whose subject is only a positional guess. This is not a nicety: in 2017 Code-C, **179 of
179** positional guesses were wrong, and in 2015 Code-A, 43 of 43.

### Verify

```bash
$PY code/pipeline_status.py                 # what is done, what is next
$PY code/export_paper_v2.py --data          # run twice; `git status` must be clean the 2nd time
$PY code/run_step.py B3S --check            # must print DONE
```

Then read ten random questions in the HTML against the printed PDF. That is the only check that
catches a lost digit, and it is the check that found the defects this project exists to prevent.

---

## 15. Definition of done

- [ ] `solution_lines` present for 1,451+ questions; the 2019/2020/2021 gap investigated and the
      finding written into §5 of this file
- [ ] `papers/solutions/<paper_id>/q###.png` cut for every question with a solution, page-break
      continuations included
- [ ] `b3s-solution-reader` brief, `schemas/B3S.json`, `code/checks/B3S.py`, the `steps.yaml`
      entry and `B3SPlugin` all exist; `run_step.py B3S --list` prints work
- [ ] `ai_solution_stepwise` emitted for new solves; existing 358 split from `working`
- [ ] every image carries a `*_cdn` URL and a `sha256`; the local path still works offline
- [ ] `data/<year>/<paper_code>/questions.json` validates against §11 for all 10 booklets
- [ ] `data/<year>/<paper_code>/question_paper.html` opens from disk with no network, shows both
      solution blocks, renders LaTeX, and marks every problem instead of hiding it
- [ ] re-running the export twice leaves `git status` clean
- [ ] `verdict_self` computed; every `publisher_contradicts_itself` raised as a flag

### Known gaps that are not your fault

- **Only 358 of 1,869 questions have been read from their image.** B3S inherits that: a solution
  read for a question whose stem is still a mangled draft is of limited use. Prioritise the 637
  questions flagged `draft_cannot_represent_this_question`.
- **No Vedantu booklet is in this checkout.** `source_pdfs/papers_v2_sources/NEET_Papers/` holds
  exactly 10 PDFs, all `aakash` / `aakash_classic` / `solution_inline`. The docs describe a
  211-file corpus where Vedantu dominates 2015–2018; those files come from the Drive link in the
  root README. The code is ready for them — `FAMILIES` takes one new row, the `lower` option style
  and the letter-form answer marker are already implemented and documented as Vedantu-specific —
  but nothing can be measured until the files are local.
- **No v2 step has ever raised a flag.** All 1,298 rows in `flags/flags.jsonl` come from v1 steps
  keyed on v1 ids. If you add flag-raising to B3S, you are the first; follow `lib/flags.py`.
