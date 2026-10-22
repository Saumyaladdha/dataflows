# What is left · measured 2026-10-13

Every number here was measured by running the pipeline, not estimated. Where a count was taken
earlier in the day and the queue has since moved, that is said. Nothing in this file is a plan;
it is a statement of position.

Totals at the time of writing: **5,414 items — 4,869 pass, 533 flagged, 7 blocked, 4 skipped,
1 stale.** 1,214 open flag rows. 242 tests passing.

---

## 1. Stage A — the NCERT index · THE BIGGEST REMAINING BODY OF WORK

| step | done | still queued | state |
|---|---|---|---|
| A1 register books | 13 | 0 | complete |
| A2 read a page | 1,116 | **~2,987** | ~27% |
| A2S transcribe a special block | 352 | **~1,709** | ~17% |
| A3 split into passages | 615 | **~491** | grows with A2 |
| A4 write subtopics | 45 | **~30** | grows with A3 |
| A5 link passages | 0 | — | **NEVER RUN** |
| A6 | 0 | — | **NEVER RUN** |
| A7 | 0 | — | **NEVER RUN** |
| A8 judge a change | 0 | — | **NEVER RUN** |
| A9 | 0 | — | **NEVER RUN** |

A2/A2S/A3/A4 queue depths were measured earlier today and move as waves land.

**A5–A9 are the entire edition change-log half of Stage A and have never produced a single
output.** They are blocked on older-edition page coverage, which is the slowest part of A2. Until
they run:

* nothing can say which NCERT lines changed between editions;
* `D5` (older-line finder) and `D6` (status note) cannot run, which gates **all of Stage E**;
* `old_ncert_fact` in the E5 trap taxonomy has 0 instances **because the change log is empty**,
  not because the trap does not exist.

This is the critical path for the whole project. Everything in section 4 below waits on it.

---

## 2. Stage B — the papers · ESSENTIALLY COMPLETE

| step | outputs | queue |
|---|---|---|
| B1 register papers | 211 | 0 |
| B2 find boundaries | 437 | 0 |
| B3 read questions | 745 | 0 |
| B4 second read | script-resolved (612 status) | 0 |
| B5 copy the key | 49 | **17** |
| B6 blind solve | 562 | 0 |
| B7 chemistry branch | 162 | 0 |
| B8 fix faulty | 5 | 0 |
| B9 recover the figure | 63 | 0 |
| B10 split the figure | 14 | 0 |
| C1 merge booklet codes | 36 | 0 |

**The only Stage B work outstanding is B5's 17 key-copier items** — 2019 and 2022 papers that
became reachable only after the B1 booklet-code repairs. One group of 5 was dispatched and is in
flight; 12 were never started.

---

## 3. Stage D — linking to NCERT · BARELY STARTED

| step | outputs | queue | state |
|---|---|---|---|
| D1 pick the chapter | 10 | **1,152** | 1% |
| D2 pick subtopics | 4 | 0 (gated) | |
| D3 draft passages | 3 | 0 (gated) | |
| D4 quote the evidence | 1 | 1 | |
| D5 older line finder | 0 | — | **NEVER RUN** — needs A5–A9 |
| D6 status note | 0 | — | **NEVER RUN** |
| D7 latest answer check | 0 | — | **NEVER RUN** |
| D8 fact line | 0 | — | **NEVER RUN** |
| D9 repeat finder | 0 | — | **NEVER RUN** |
| D10 | 0 | — | **NEVER RUN** |
| D11 group confirmer | 0 | — | **NEVER RUN** |

D1's 1,152-item queue is the largest single queue in the project. D2 and D3 read 0 only because
they are gated on D1.

---

## 4. Stage E — tagging · NEVER RUN, AND NOT FOR THE OBVIOUS REASON

E0–E6 have produced **no outputs at all**. The runner's own explanation, quoted verbatim:

> E1 needs a resolved D7. No question has one: D7 needs D6, and D6 is agent-driven and has never
> been dispatched, so nothing has reached E1 yet. Nothing is fabricated to make it look otherwise.

**This is easy to misread, so state it plainly.** `exports/discovery/` holds a complete five-axis
taxonomy — 86 categories across E1–E5, with **580 questions already tagged** and two independent
discovery passes with their disagreements recorded. That work is real and it is good. But it was
produced by a separate discovery exercise, **not** by the pipeline's E steps. The pipeline has
never tagged a question. The two must not be confused: the discovery output is a vocabulary plus a
hand-verified sample, and the pipeline's job is to apply that vocabulary to every question with a
per-question audit trail.

---

## 5. Stage F — review · WAITING ON A PERSON

F1 and F6 have a status but no outputs; F3 and F5 have one each; F4 has 197 outputs against 18
status files; F2 has never run. Stage F is where people review, and the queue below is what they
are waiting for.

---

## 6. Data corrections needed · SPECIFIC ITEMS

### 6.1 Questions whose content is wrong or contradictory

| item | what is wrong | found by |
|---|---|---|
| `Q-000678` | B3's bracketed description says "diphenyl ether"; the matched figure is **benzyl phenyl ether**. Diphenyl ether cannot give any of the four options' benzyl products, so the description contradicts the options. Likely a B3 misreading. | B9 agent, unprompted |
| `Q-000695` | Stem names **o-phthalaldehyde** (two CHO); the near-match figure shows **2-acetylbenzaldehyde**. Possibly B3 misread an acetyl group as a second CHO. Figure deliberately left unattached. | B9 agent |
| `Q-000672` | Candidate figure is unmistakably the same question but its battery reads **40 V** where our stem says 10 V (40 V ⇒ R ≈ 21 Ω, not among our options; 10 V ⇒ 100 Ω). Likely the old bank's misprint. No figure attached. | B9 agent |
| `NEET-2024-MAIN-Q1 q0001` / `q0014` | Same question content at two numbers **in one booklet**, which cannot happen in a real paper. Both carry a collapsed truth table and scrambled Boolean options; q0014 also has a booklet-instruction preamble glued to its stem. | content-key dedup |
| `NEET-2024-MAIN-Q1 q0010`, `q0011` | **BLOCKED.** B3 reports the crop is a run-on prose/solution fragment, not a question card. The 2024 Q1 scrape is disturbed around these pages. | B3 |

### 6.2 Nine questions with genuinely duplicate options — unusable as recorded

Re-read at 6–8× magnification; **all nine confirmed as genuine defects in our source**, not lost
notation. Each was checked specifically for a lost radical, exponent, decimal point, leading digit
and unit prefix.

* `NEET-2023-MAIN-E1-q0055` / `E2-q0060` — options 1 and 4 both `34 cm^-1`
* `NEET-2023-MAIN-E1-q0008` / `E2-q0011` — options 2 and 3 both `7 A`
* `NEET-2022-MAIN-Q1-q0011` — option 3 `1: 2`, option 4 `1 : 2`, differing only in spacing
* `NEET-2024-MAIN-Q1-q0001`, `-q0014` — options 3 and 4 both a bare `B`
* `NEET-2022-MAIN-Q1-q0047` — **two** identical pairs, and the stem's two figures are absent
* `NEET-2022-MAIN-Q1-q0083` — options 2, 3 **and** 4 all a bare `57`

These are unanswerable as they stand. The fix is better source material, not another transcription
pass: no re-read can recover a character the image does not contain.

### 6.3 Pictures still missing

| item | slots | state |
|---|---|---|
| `Q-000500`, `Q-000502` | 6 | placeholder options, **no figure recovered at all** |
| `Q-000385`, `Q-000492`, `Q-000509`, `Q-000520` | 16 | B9 recovered the **stem** figure, not the option pictures. `figure_path` is set, so these look handled while the actual missing thing is still missing |
| 36 option slots across 8 questions | 36 | panels cut, but **which panel is which option number is unverified** — see 7.4 |
| 23 questions | — | stem names a figure (`"in the figure"`, `"the following circuit"`) while `has_figure` is **false**, so B9 never considered them |

**A data-model gap behind this:** nothing on a record distinguishes a *stem* figure from an
*option* panel. `figure_path` says only that some picture exists.

### 6.4 Known limitation, recorded and not fixed

A2's coverage denominator counts text sitting inside `needs_special` bounding boxes, so a page
whose content is mostly a table reads as under-covered (`BIO12O-ch10-p002` at 0.0%,
`BIO11O-ch12-p010` at 39.8%). A proper fix needs per-line coordinates.

---

## 7. Decisions only the owner can make · THESE BLOCK WORK

### 7.1 The source strategy — the biggest one
**189 of 201 registered question papers are Chromium print-to-PDF of the scraped website**
(`Creator: Chromium`, `Producer: Skia/PDF`, `Title: … | neet.training`), including every paper the
580 analysed questions come from. For those papers, anything the website did not render — reaction
structures, graphs, circuits, image options — is absent from the file we are calling the source.

12 papers are from real publishing toolchains, and `NEET_PYQ/Paper/` holds genuine-layout books
with real embedded images (2025: 133, AIPMT 2014: 232, 2024: 86, 2017: 75 … but **2023: 0**, and
2016/2020/2012/2026 absent entirely).

**Open:** should `NEET_PYQ/Paper/` become the primary extraction source for B1–B6? It would fix
the missing figures and the unreadable-glyph defect in one move, and let B6 stop refusing every
`has_figure` question. It also means re-extracting every B-stage record already built.

### 7.2 Should the register record that a "paper" is a website print?
Nothing in `register/papers.csv` distinguishes a real paper from a print of a scrape. A reader
cannot currently tell. These files are faithful for text and systematically blind to drawn content.

### 7.3 Legacy-sheet figures — the rule question
`CLAUDE.md` forbids passing legacy-sheet columns and coaching material to agents that must not see
them. B9 **has already used** the sheets' Mathpix figure URLs to recover 57 figures. My reading,
offered as a proposal and not a decision: a figure image is the original exam's own content, not a
coaching judgement, so the defensible split is **use the `![](mathpix-url)` image only, never the
sheet's `Chapter Name`/`Chapter No`/`Topic`/`Question Type`/`Answer` columns.** This needs
ratifying or reversing. Related: `2024.pdf` carries a **Physics Wallah watermark**, so it is
coaching material too.

### 7.4 The unverified option-panel mapping — 36 slots
A printed panel label is the **source paper's** option order, and booklet codes shuffle option
order. `Q-000343` is the proof: the official key for our booklet says the answer is **4**, while
the physically correct Arrhenius plot in the recovered picture is printed **(2)**. So B10 cuts the
panels and keeps them under their printed labels, and the sheet states the mapping is unverified.
Only a person can confirm which panel is which option — or decide to re-point such questions at
the booklet code whose paper we actually hold with images.

### 7.5 Smaller decisions, each blocking something
* **4 AIPMT papers rejected** for `year < 2012` against the schema floor — scope question.
* **`list_of_reactions`** — E1 has no value for "each of the four options is a whole reaction"
  (real case `Q-000005`). `config/allowed_values.yaml` is unchanged pending the decision.
* **2019/2020/2024 re-exam sittings** — real sittings, genuinely missing papers, currently expected
  and flagged. Are limited re-tests in scope at all?
* **23 stale flags** sit in `review/decisions.DRAFT.csv` with `reviewer` deliberately empty so they
  cannot be applied without a name.
* **`B6_IMAGE_INPUT_UNSAFE` (55)** — B6's input for figure questions is a raw crop that may contain
  the scrape's "CORRECT ANSWER" panel, so those blind solves are **not reliably blind**. A design
  limitation, not a bug.
* **`trust: memory_based` vs `official`** on neet.training papers — the owner's instruction
  "trust neet training, add as official" was read as intent rather than literally, because `trust`
  records whether the page confirmed its own booklet code. Flagged for confirmation.

---

## 8. Open flags · 1,214 rows

| code | n | needs |
|---|---|---|
| `B1_REGISTER_DRAFT` | 211 | reviewer approval (working as designed) |
| `B4_MISMATCH_ADJUDICATED` | 179 | reviewer sight of the adjudication |
| `B1_CHECK_FAILED` | 167 | investigation |
| `B1_MANIFEST_MISMATCH` | 136 | owner decision on the reshuffled sets |
| `B5_KEY_ROW_MISSING` | 128 | 61 papers genuinely have no booklet code |
| `A2_JOIN_ADJUDICATED` | 68 | reviewer |
| `B9_FIGURE_RECOVERED` | 58 | permanent provenance marker, by design |
| `B6_IMAGE_INPUT_UNSAFE` | 55 | see 7.5 |
| `B6_DISAGREES_WITH_KEY` | 54 | this **is** the blind solve's output, by design |
| `S0_MISSING_INPUT` | 18 | the genuinely absent papers |

An earlier audit re-tested every open flag's premise: **23 are stale** (their condition is no
longer true), **79 still true**, the rest need a person. `scripts/audit_flags.py` re-runs that.

---

## 9. Still to build

1. **The figure flow's step 1 — not built.** The owner's instruction is: check
   `NEET_PYQ/Paper/<year>.pdf` **first**, screenshot the figure, and only fall back to the Excel.
   `recover_figures.py` currently draws candidates **only** from the Excel. Building this needs the
   `b9-figure-matcher` brief extended for paper-crop variations: a crop comes from a different
   booklet code, question numbers differ between codes, `2023.pdf` has zero images, and
   2016/2020 have no paper at all.
2. **Nothing distinguishes a stem figure from an option panel** on a record (see 6.3).
3. **`docs/question_categories/` is superseded** — a parallel 15-category taxonomy I built before
   finding `exports/discovery/CATEGORIES.xlsx`. Kept only so the note explaining the mistake has
   something to point at. Nothing should be built on it.

### Stale notes in this repo, to correct
* `docs/OPEN_QUESTIONS.md` says `legacy_match.py` is "not built yet". **It is built** — 454 lines,
  with `match_one`, `canonical_records`, `assert_no_legacy` and a self-test.
