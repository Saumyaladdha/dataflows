# NEET PYQ — Input Collection Codebook

**Status as of 2026-10-09:** a large real data drop (`Saumya_NEET_work`, 1.3 GB — NCERT books, NEET papers by booklet code, official answer keys, legacy spreadsheets) has been copied into `pyq_bank/inputs/`. Coaching solutions and official notices are still not received.

**Important distinction kept throughout this file:** `PRESENT (unverified)` means the file exists in `pyq_bank/inputs/` under the row's expected name/location, confirmed only by filename and folder path. `RECEIVED (verified)` is reserved for a row where the file has actually been **opened** and its content checked against what the row claims (reprint year on the imprint page, sitting/date on the cover, booklet code inside the PDF, final-vs-provisional key wording). Today's pass copied and filename-matched 363 PDFs, 44 xlsx and 4 reference files — opening and verifying every one individually has **not** happened yet. Do not treat `PRESENT (unverified)` as equivalent to passing Stage 0 intake.

**Purpose:** track every input the active spec (`NEET_PYQ_Pipeline_v2.1_ACTIVE_SPEC.md`, Section 8 / S0 intake) requires. Columns match `inputs/manifest.csv` (`file, kind, subject, class, edition, year, sitting, booklet_code, source, downloaded_on`).

---

## 1 · NCERT books (both editions, English, Class 11 & 12)

| book_id | subject | class | edition | status | location | notes |
|---|---|---|---|---|---|---|
| PHY11L | Physics | 11 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_11th/Physics/` | reprint year not yet confirmed from imprint page |
| PHY11O | Physics | 11 | older | PRESENT (unverified) | `inputs/ncert/older/Class_11th/Physics/` | which print year counts as "the" older edition not yet confirmed |
| PHY12L | Physics | 12 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_12th/Physics/` | |
| PHY12O | Physics | 12 | older | PRESENT (unverified) | `inputs/ncert/older/Class_12th/Physics/` | |
| CHE11L | Chemistry | 11 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_11th/Chemistry/` | |
| CHE11O | Chemistry | 11 | older | PRESENT (unverified) | `inputs/ncert/older/Class_11th/Chemistry/` | |
| CHE12L | Chemistry | 12 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_12th/Chemistry/` | |
| CHE12O | Chemistry | 12 | older | PRESENT (unverified) | `inputs/ncert/older/Class_12th/Chemistry/` | |
| BIO11L | Biology | 11 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_11th/Biology/` | |
| BIO11O | Biology | 11 | older | PRESENT (unverified) | `inputs/ncert/older/Class_11th/Biology/` | |
| BIO12L | Biology | 12 | latest | PRESENT (unverified) | `inputs/ncert/latest/Class_12th/Biology/` | |
| BIO12O | Biology | 12 | older | PRESENT (unverified) | `inputs/ncert/older/Class_12th/Biology/` | |
| PHY-LAB-M | Physics | 11–12 | lab manual | **MISSING** | — | not in this drop |
| CHE-LAB-M | Chemistry | 11–12 | lab manual | **MISSING** | — | not in this drop |

**Bonus, out of original scope:** both editions also include **Class 11/12 Maths** (`.../Class_11th/Maths/`, `.../Class_12th/Maths/`). Not required by the spec (NEET is Physics/Chemistry/Biology only) — left in place, not wired into the pipeline.

**Still open:** exact reprint year per book (A1's job), and confirmation of how many PDF parts each book splits into (spec expects Physics/Chemistry to have Part 1/Part 2).

---

## 2 · NEET question papers (2016–2026, every sitting)

Source gave papers two ways: whole-year PDFs (`NEET_PYQ/Paper/`) and **per-booklet-code** PDFs (`all_neet_sets_and_ans_key/<year>/code-*/`). Both landed in `inputs/papers/`. Booklet codes are real (e.g. 2018 has 17 codes, 2021–2024 have ~24 each) — far more than the spec's "one master code, second only to fill gaps" assumption anticipated; worth noting but not a problem, more codes just means more cross-checking material for Stage C.

| paper_id | year | sitting | status | booklet_codes_seen | notes |
|---|---|---|---|---|---|
| NEET-2016-MAIN | 2016 | MAIN | PRESENT (unverified) | A_P_W, B_Q_X, C_R_Y, D_S_Z | **MAIN vs PH2 split not yet confirmed** — all four codes sit in one `2016/` folder; legacy Excel separately has distinct "Phase I" and "Phase II" sheets, so the PDFs likely split the same way, but this hasn't been opened and checked |
| NEET-2016-PH2 | 2016 | PH2 | PRESENT (unverified), same caveat | (see above) | |
| NEET-2017-MAIN | 2017 | MAIN | PRESENT (unverified) | A, B, C, D, S | |
| NEET-2018-MAIN | 2018 | MAIN | PRESENT (unverified) | AA, BB, CC, DD, EE, FF, GG, HH, KK, LL, MM, NN, PP, RR, SS, WW, XX, YY, ZZ (17 codes — some letters e.g. II/JJ/OO/QQ/TT/UU/VV skipped, consistent with how NTA avoids visually ambiguous letters) | |
| NEET-2019-MAIN | 2019 | MAIN | PRESENT (unverified) | P1, P2, Q2, R3, S2 | **MAIN vs REEXAM split not yet confirmed** from these 5 codes |
| NEET-2019-REEXAM | 2019 | REEXAM | PRESENT (unverified), same caveat | (see above) | |
| NEET-2020-MAIN | 2020 | MAIN | PRESENT (unverified) | 24 codes, pattern `<4-letter>-<L><digit>` e.g. AKANH-E5, ANKHA-F2 | **MAIN vs REEXAM split not yet confirmed**; this closes the "2020 main paper missing" gap the spec itself flagged (Section 2.7) |
| NEET-2020-REEXAM | 2020 | REEXAM | PRESENT (unverified), same caveat | (see above) | |
| NEET-2021-MAIN | 2021 | MAIN | PRESENT (unverified) | 24 codes, pattern `<6-letter>-<L><digit>` e.g. AGAJHA-M4 | spec notes 2021–2024 printed 200 questions (180 attempted) — not yet checked whether these PDFs show 200 or 180 |
| NEET-2022-MAIN | 2022 | MAIN | PRESENT (unverified) | Q1–Q6, R1–R6, S1–S6, T1–T6 (24 codes) | **bonus asset**: this year also has Mathpix OCR output (`inputs/_reference/mathpix/2022/`) — a third-party transcription + an `answer_key_comparison.csv/.md`, not an official source, kept separate and flagged, not fed into B1 as-is |
| NEET-2023-MAIN | 2023 | MAIN | PRESENT (unverified) | E1–E6, F1–F6, G1–G6, H1–H6 (24 codes) | |
| NEET-2024-MAIN | 2024 | MAIN | PRESENT (unverified) | Q1–Q6, R1–R6, S1–S6, T1–T6 (24 codes) | **MAIN vs RETEST split not yet confirmed** |
| NEET-2024-RETEST | 2024 | RETEST | PRESENT (unverified), same caveat | (see above) | |
| NEET-2025-MAIN | 2025 | MAIN | PRESENT (unverified) | 45, 46, 47, 48 (4 codes) | |
| NEET-2026-CANCELLED | 2026 | CANCELLED (3 May) | **MISSING as PDF** | — | only exists as a legacy Excel sheet (`NEET Exam 2026_(03-05-2026).xlsx`); no official key either, which is expected since it was cancelled |
| NEET-2026-REEXAM | 2026 | REEXAM (21 June) | **MISSING as PDF** | — | only exists as a legacy Excel sheet; the **official key PDF is present** (see Section 3) even though the paper PDF itself is not |

**Not in scope by default (owner decision pending, Section 20):**

| paper_id | year | status | notes |
|---|---|---|---|
| NEET-2013-MAIN | 2013 | PRESENT (unverified) | register only, don't run Stage B per the open decision |
| AIPMT-2014-MAIN | 2014 | PRESENT (unverified) | same |
| AIPMT-2015-MAIN | 2015 | PRESENT (unverified) | same |
| AIPMT-2010/2011 (Main + Preliminary) | 2010–2011 | PRESENT (unverified) | pre-2013, not mentioned anywhere in the spec's scope — flag for the owner, new open question |
| AIPMT-2012 | 2012 | **MISSING as PDF** | legacy Excel sheets for 2012 (Main and Pre) exist, but **no paper PDF was in this drop** — a real gap, not a spec assumption |

---

## 3 · Official final answer keys

| year | sitting coverage | status | file(s) | notes |
|---|---|---|---|---|
| 2016 | Phase I & II | PRESENT (unverified) | `NEET_answers-key_2016-phase-1.pdf`, `...-phase-2.pdf` | split by phase, good — matches sitting granularity directly |
| 2017 | MAIN | PRESENT (unverified) | `NEET_answers-key_2017.pdf` | one file — not yet confirmed whether it covers all 5 codes or just one |
| 2018 | MAIN | PRESENT (unverified) | 17 separate files, one per code (AA–ZZ) | best-case granularity, matches codes 1:1 |
| 2019 | MAIN + REEXAM (not yet split) | PRESENT (unverified) | `NEET_answers-key_2019-neet.pdf` | single file for the year — MAIN/REEXAM coverage unconfirmed |
| 2020 | MAIN + REEXAM (not yet split) | PRESENT (unverified) | `NEET_answers-key_2020-neet.pdf` | single file for the year |
| 2021 | MAIN | PRESENT (unverified) | `NEET_answers-key_2021-neet.pdf` | single file |
| 2022 | MAIN | PRESENT (unverified) | `NEET_answers-key_2022-neet.pdf` | single file; Mathpix `answer_key_comparison.csv/.md` also present as unofficial cross-check material |
| 2023 | MAIN | PRESENT (unverified) | `NEET_answers-key_2023-neet.pdf` | single file |
| 2024 | MAIN + RETEST (not yet split) | PRESENT (unverified) | `NEET_answers-key_2024-neet.pdf` | single file |
| 2025 | MAIN | PRESENT (unverified) | `NEET_answers-key_2025-neet.pdf` | single file |
| 2026 | CANCELLED | **MISSING** | — | expected: a cancelled sitting has no final key |
| 2026 | REEXAM | PRESENT (unverified) | `NEET_answers-key_2026-Re_neet.pdf` | |
| pre-2016 (AIPMT/older NEET) | — | **MISSING** | — | no official key PDFs for 2010–2015 in this drop |

**Open question this raises for the spec (Section 20):** several years have only **one key file covering the whole year**, not one per booklet code as Section 6.2/S0 implicitly expects. Before B5 can do its `(paper_id, qno)` join, need to confirm whether these single-file keys actually list results **per code** inside, or use one fixed question order that all codes map back to. This should go into `docs/OPEN_QUESTIONS.md` once verified, not assumed either way.

---

## 4 · Coaching detailed solutions (Allen, Aakash, etc.)

**Still MISSING — none in this drop.** `inputs/coaching/` was created and is empty. No change from before.

---

## 5 · Official notices

**Still MISSING — none in this drop.** Both the bonus/dropped notices (5a) and the official sitting calendar (5b) remain unreceived. `inputs/notices/` was created and is empty.

One partial substitute: the **existence pattern** of the papers/keys we do have (e.g. a 2026 CANCELLED sitting with no key at all, a 2024 RETEST implied by the spec but not yet confirmed as a separate code range) is circumstantial evidence toward what Section 5b would confirm officially — but it is not a substitute for the real notices, and shouldn't be treated as one.

---

## 6 · Legacy spreadsheets (not one of the 5 required categories, but part of this drop)

22 `.xlsx` files landed in `inputs/legacy_sheets/` — AIPMT Main/Pre 2010–2012, NEET-UG 2013–2025, both 2016 phases, and both 2026 sittings. Per the spec's own hard rule (Section 2.2 / `CLAUDE.md`'s "Never" list): **these are never passed to any agent and never set any field directly** — they exist only as `legacy_chapter`/`legacy_topic`/`legacy_question_type` comparison fields in Stage F. Flagging here only so they don't get mistaken for primary source material later.

---

## 7 · Reference-only material (not a spec input category)

`inputs/_reference/mathpix/2022/` — Mathpix OCR transcriptions of the 2022 codes plus a hand-built `answer_key_comparison.csv`/`.md`. Third-party, not official. Potentially useful as a cross-check or starting point for B3/B4 prompt-tuning, but not wired into intake as a formal source — flag for the owner whether it should count as anything beyond a convenience reference.

---

## What's next (not done yet)

1. **Open and verify**, don't just filename-match: confirm NCERT reprint years (A1), confirm which booklet codes belong to which sitting for 2016/2019/2020/2024 (the "not yet confirmed" rows above), confirm whether single-year key files cover all codes.
2. **Build `inputs/manifest.csv`** once the above is verified — not before, since the manifest is supposed to be a checked record, not a filename guess.
3. **Flag real gaps to the owner**: no lab manuals, no coaching solutions, no official notices, no 2012 paper PDF, no 2026 paper PDFs (either sitting), nothing pre-2010.
4. Only after that: Stage 0 intake can actually run for real (once `scripts/intake_check.py` exists — M1–M3, not built yet).
