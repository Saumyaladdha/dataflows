# Stage 0 · Intake report

Generated: 2026-10-12T13:45:34+05:30  
Source: `inputs/manifest.csv` (420 rows) vs `inputs/` tree (420 files, excluding `inputs/_reference/`)

## Summary

- Manifest rows by kind: key=30, lab_manual=1, legacy_sheet=22, ncert=186, paper=181

- Required/checked items: **50 present**, **18 missing**, 6 out-of-scope-informational

- `S0_MISSING_INPUT` (blocker) flags raised this run: **18**

- File <-> manifest reconciliation: OK, exact match

- Legacy sheet classification check: OK, no misclassified files


## 1. NCERT books (Physics / Chemistry / Biology x Class 11 / 12 x latest / older)

| Subject | Class | Edition | Status | Note |
|---|---|---|---|---|
| Physics | 11 | latest | **present** | 14 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Physics | 11 | older | **present** | 18 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Physics | 12 | latest | **present** | 14 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Physics | 12 | older | **present** | 15 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Chemistry | 11 | latest | **present** | 9 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Chemistry | 11 | older | **present** | 19 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Chemistry | 12 | latest | **present** | 10 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Chemistry | 12 | older | **present** | 16 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Biology | 11 | latest | **present** | 19 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Biology | 11 | older | **present** | 23 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Biology | 12 | latest | **present** | 13 latest-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |
| Biology | 12 | older | **present** | 16 older-edition chapter PDF(s) found (one-PDF-per-chapter layout; treated as one logical book per docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry) |

## 2. Lab manuals

| Subject | Status | Note |
|---|---|---|
| Physics | **missing** | Physics NCERT lab manual not collected (none in this drop; confirmed missing per Codebook Section 1) |
| Chemistry | **present** | 1 lab manual PDF(s) found |

## 3. Papers & keys, 2016–2026 (in scope)

One row per (year, sitting). A `missing` paper/key with a note mentioning "could not be confirmed" means file(s) exist but couldn't be safely attributed to this sitting — not that nothing exists at all.

| Year | Sitting | Paper | Key | Note |
|---|---|---|---|---|
| 2016 | MAIN | **missing** | **present** | paper: 4 paper file(s) exist for 2016 but which sitting each belongs to (MAIN/PH2) could not be confirmed from the filename alone: inputs/papers/neet_2016_code-A_P_W.pdf, inputs/papers/neet_2016_code-B_Q_X.pdf, inputs/papers/neet_2016_code-C_R_Y.pdf, inputs/papers/neet_2016_code-D_S_Z.pdf |
| 2016 | PH2 | **missing** | **present** | paper: 4 paper file(s) exist for 2016 but which sitting each belongs to (MAIN/PH2) could not be confirmed from the filename alone: inputs/papers/neet_2016_code-A_P_W.pdf, inputs/papers/neet_2016_code-B_Q_X.pdf, inputs/papers/neet_2016_code-C_R_Y.pdf, inputs/papers/neet_2016_code-D_S_Z.pdf |
| 2017 | MAIN | **present** | **present** | — |
| 2018 | MAIN | **present** | **present** | — |
| 2019 | MAIN | **missing** | **missing** | paper: 6 paper file(s) exist for 2019 but which sitting each belongs to (MAIN/REEXAM) could not be confirmed from the filename alone: inputs/papers/2019.pdf, inputs/papers/neet_2019_code-P1.pdf, inputs/papers/neet_2019_code-P2.pdf, inputs/papers/neet_2019_code-Q2.pdf, inputs/papers/neet_2019_code-R3.pdf, inputs/papers/neet_2019_code-S2.pdf; key: 1 key file(s) exist for 2019 but cover the whole year without splitting by sitting — cannot confirm MAIN is covered: inputs/keys/NEET_answers-key_2019-neet.pdf |
| 2019 | REEXAM | **missing** | **missing** | paper: 6 paper file(s) exist for 2019 but which sitting each belongs to (MAIN/REEXAM) could not be confirmed from the filename alone: inputs/papers/2019.pdf, inputs/papers/neet_2019_code-P1.pdf, inputs/papers/neet_2019_code-P2.pdf, inputs/papers/neet_2019_code-Q2.pdf, inputs/papers/neet_2019_code-R3.pdf, inputs/papers/neet_2019_code-S2.pdf; key: 1 key file(s) exist for 2019 but cover the whole year without splitting by sitting — cannot confirm REEXAM is covered: inputs/keys/NEET_answers-key_2019-neet.pdf |
| 2020 | MAIN | **missing** | **missing** | paper: 24 paper file(s) exist for 2020 but which sitting each belongs to (MAIN/REEXAM) could not be confirmed from the filename alone: inputs/papers/neet_2020_code-AKANH-E5.pdf, inputs/papers/neet_2020_code-AKANH-F5.pdf, inputs/papers/neet_2020_code-AKANH-G5.pdf, inputs/papers/neet_2020_code-AKANH-H5.pdf, inputs/papers/neet_2020_code-ANKHA-E2.pdf, inputs/papers/neet_2020_code-ANKHA-F2.pdf, inputs/papers/neet_2020_code-ANKHA-G2.pdf, inputs/papers/neet_2020_code-ANKHA-H2.pdf, inputs/papers/neet_2020_code-HAKAN-E4.pdf, inputs/papers/neet_2020_code-HAKAN-F4.pdf, inputs/papers/neet_2020_code-HAKAN-G4.pdf, inputs/papers/neet_2020_code-HAKAN-H4.pdf, inputs/papers/neet_2020_code-KANHA-E1.pdf, inputs/papers/neet_2020_code-KANHA-F1.pdf, inputs/papers/neet_2020_code-KANHA-G1.pdf, inputs/papers/neet_2020_code-KANHA-H1.pdf, inputs/papers/neet_2020_code-KHANA-E6.pdf, inputs/papers/neet_2020_code-KHANA-F6.pdf, inputs/papers/neet_2020_code-KHANA-G6.pdf, inputs/papers/neet_2020_code-KHANA-H6.pdf, inputs/papers/neet_2020_code-NAKHA-E3.pdf, inputs/papers/neet_2020_code-NAKHA-F3.pdf, inputs/papers/neet_2020_code-NAKHA-G3.pdf, inputs/papers/neet_2020_code-NAKHA-H3.pdf; key: 1 key file(s) exist for 2020 but cover the whole year without splitting by sitting — cannot confirm MAIN is covered: inputs/keys/NEET_answers-key_2020-neet.pdf |
| 2020 | REEXAM | **missing** | **missing** | paper: 24 paper file(s) exist for 2020 but which sitting each belongs to (MAIN/REEXAM) could not be confirmed from the filename alone: inputs/papers/neet_2020_code-AKANH-E5.pdf, inputs/papers/neet_2020_code-AKANH-F5.pdf, inputs/papers/neet_2020_code-AKANH-G5.pdf, inputs/papers/neet_2020_code-AKANH-H5.pdf, inputs/papers/neet_2020_code-ANKHA-E2.pdf, inputs/papers/neet_2020_code-ANKHA-F2.pdf, inputs/papers/neet_2020_code-ANKHA-G2.pdf, inputs/papers/neet_2020_code-ANKHA-H2.pdf, inputs/papers/neet_2020_code-HAKAN-E4.pdf, inputs/papers/neet_2020_code-HAKAN-F4.pdf, inputs/papers/neet_2020_code-HAKAN-G4.pdf, inputs/papers/neet_2020_code-HAKAN-H4.pdf, inputs/papers/neet_2020_code-KANHA-E1.pdf, inputs/papers/neet_2020_code-KANHA-F1.pdf, inputs/papers/neet_2020_code-KANHA-G1.pdf, inputs/papers/neet_2020_code-KANHA-H1.pdf, inputs/papers/neet_2020_code-KHANA-E6.pdf, inputs/papers/neet_2020_code-KHANA-F6.pdf, inputs/papers/neet_2020_code-KHANA-G6.pdf, inputs/papers/neet_2020_code-KHANA-H6.pdf, inputs/papers/neet_2020_code-NAKHA-E3.pdf, inputs/papers/neet_2020_code-NAKHA-F3.pdf, inputs/papers/neet_2020_code-NAKHA-G3.pdf, inputs/papers/neet_2020_code-NAKHA-H3.pdf; key: 1 key file(s) exist for 2020 but cover the whole year without splitting by sitting — cannot confirm REEXAM is covered: inputs/keys/NEET_answers-key_2020-neet.pdf |
| 2021 | MAIN | **present** | **present** | — |
| 2022 | MAIN | **present** | **present** | — |
| 2023 | MAIN | **present** | **present** | — |
| 2024 | MAIN | **missing** | **missing** | paper: 25 paper file(s) exist for 2024 but which sitting each belongs to (MAIN/RETEST) could not be confirmed from the filename alone: inputs/papers/2024.pdf, inputs/papers/neet_2024_code-Q1.pdf, inputs/papers/neet_2024_code-Q2.pdf, inputs/papers/neet_2024_code-Q3.pdf, inputs/papers/neet_2024_code-Q4.pdf, inputs/papers/neet_2024_code-Q5.pdf, inputs/papers/neet_2024_code-Q6.pdf, inputs/papers/neet_2024_code-R1.pdf, inputs/papers/neet_2024_code-R2.pdf, inputs/papers/neet_2024_code-R3.pdf, inputs/papers/neet_2024_code-R4.pdf, inputs/papers/neet_2024_code-R5.pdf, inputs/papers/neet_2024_code-R6.pdf, inputs/papers/neet_2024_code-S1.pdf, inputs/papers/neet_2024_code-S2.pdf, inputs/papers/neet_2024_code-S3.pdf, inputs/papers/neet_2024_code-S4.pdf, inputs/papers/neet_2024_code-S5.pdf, inputs/papers/neet_2024_code-S6.pdf, inputs/papers/neet_2024_code-T1.pdf, inputs/papers/neet_2024_code-T2.pdf, inputs/papers/neet_2024_code-T3.pdf, inputs/papers/neet_2024_code-T4.pdf, inputs/papers/neet_2024_code-T5.pdf, inputs/papers/neet_2024_code-T6.pdf; key: 1 key file(s) exist for 2024 but cover the whole year without splitting by sitting — cannot confirm MAIN is covered: inputs/keys/NEET_answers-key_2024-neet.pdf |
| 2024 | RETEST | **missing** | **missing** | paper: 25 paper file(s) exist for 2024 but which sitting each belongs to (MAIN/RETEST) could not be confirmed from the filename alone: inputs/papers/2024.pdf, inputs/papers/neet_2024_code-Q1.pdf, inputs/papers/neet_2024_code-Q2.pdf, inputs/papers/neet_2024_code-Q3.pdf, inputs/papers/neet_2024_code-Q4.pdf, inputs/papers/neet_2024_code-Q5.pdf, inputs/papers/neet_2024_code-Q6.pdf, inputs/papers/neet_2024_code-R1.pdf, inputs/papers/neet_2024_code-R2.pdf, inputs/papers/neet_2024_code-R3.pdf, inputs/papers/neet_2024_code-R4.pdf, inputs/papers/neet_2024_code-R5.pdf, inputs/papers/neet_2024_code-R6.pdf, inputs/papers/neet_2024_code-S1.pdf, inputs/papers/neet_2024_code-S2.pdf, inputs/papers/neet_2024_code-S3.pdf, inputs/papers/neet_2024_code-S4.pdf, inputs/papers/neet_2024_code-S5.pdf, inputs/papers/neet_2024_code-S6.pdf, inputs/papers/neet_2024_code-T1.pdf, inputs/papers/neet_2024_code-T2.pdf, inputs/papers/neet_2024_code-T3.pdf, inputs/papers/neet_2024_code-T4.pdf, inputs/papers/neet_2024_code-T5.pdf, inputs/papers/neet_2024_code-T6.pdf; key: 1 key file(s) exist for 2024 but cover the whole year without splitting by sitting — cannot confirm RETEST is covered: inputs/keys/NEET_answers-key_2024-neet.pdf |
| 2025 | MAIN | **present** | **present** | — |
| 2026 | CANCELLED | **missing** | not required (cancelled) | paper: no paper file found for 2026 CANCELLED |
| 2026 | REEXAM | **missing** | **present** | paper: no paper file found for 2026 REEXAM |

## 4. Extra check: 2018 booklet-code-level paper <-> key matching

2018 is the one year with genuinely per-booklet-code keys (every other year is one file for the whole year, or split only by phase/sitting). This checks every paper code has a matching key code, beyond the year x sitting grain above.

| Booklet code | Status | Note |
|---|---|---|
| QQ | **missing** | paper booklet code QQ (2018) has no matching final-key file (key set has 19 codes, paper set has 20) |

## 5. Out of scope (years outside 2016–2026)

Registered for completeness; Stage B does not run on these pending Section 20 decision #1.

| Year | Paper file(s) | Note |
|---|---|---|
| 2010 | inputs/papers/AIPMT-2010-Preliminary ..pdf; inputs/papers/aipmt-2010-main.pdf | 2 paper file(s), 0 key file(s); out of scope pending Section 20 decision #1 (years outside 2016-2026) |
| 2011 | inputs/papers/AIPMT-2011-Main-Original-Solved-Question-Paper.pdf; inputs/papers/AIPMT-2011-Preliminary.pdf | 2 paper file(s), 0 key file(s); out of scope pending Section 20 decision #1 (years outside 2016-2026) |
| 2012 | — | no paper PDF at all for 2012 (only legacy spreadsheets exist); out of scope regardless pending Section 20 decision #1, but a real collection gap worth surfacing (Codebook Section 2) |
| 2013 | inputs/papers/AIPMT_2013_NEET_UG_By_ALLEN.pdf | 1 paper file(s), 0 key file(s); out of scope pending Section 20 decision #1 (years outside 2016-2026) |
| 2014 | inputs/papers/AIPMT 2014.pdf; inputs/papers/neet_2014_code-P.pdf; inputs/papers/neet_2014_code-Q.pdf; inputs/papers/neet_2014_code-R.pdf; inputs/papers/neet_2014_code-S.pdf | 5 paper file(s), 0 key file(s); out of scope pending Section 20 decision #1 (years outside 2016-2026) |
| 2015 | inputs/papers/AIPMT 2015.pdf; inputs/papers/neet_2015_code-A.pdf; inputs/papers/neet_2015_code-B.pdf; inputs/papers/neet_2015_code-C.pdf; inputs/papers/neet_2015_code-D.pdf | 5 paper file(s), 0 key file(s); out of scope pending Section 20 decision #1 (years outside 2016-2026) |

## 6. Legacy sheets

22 spreadsheet(s) registered under `inputs/legacy_sheets/`, all `kind=legacy_sheet`. Per spec Section 2.2/13, these are never passed to any agent and never set any field directly — comparison-only in Stage F.

Classification check: every legacy sheet is `kind=legacy_sheet` and sits under `inputs/legacy_sheets/`; no paper/key file is misclassified as a legacy sheet. OK.


## 7. Notices & coaching material

| Category | Status |
|---|---|
| Official notices (`inputs/notices/`) | **missing** — none received yet |
| Coaching solutions (`inputs/coaching/`) | **missing** — none received yet (Section 20 decision #4: not licensed even if received) |

## 8. File <-> manifest reconciliation detail (procedure step 1)

Every file under `inputs/` (excluding `inputs/_reference/`) has exactly one manifest row, and every manifest row points to a file that exists. OK.


## 9. Files with ambiguous/unresolved metadata

These files are registered (`kind` is reliable — it comes from folder location) but `sitting` (and in a few cases `year`) was deliberately left blank rather than guessed. This is exactly why some `missing` rows above exist even though a file is physically present: presence of an unsplit/ambiguous file does not confirm presence of a specific required sitting.

- `inputs/keys/NEET_answers-key_2019-neet.pdf` — year 2019: sitting could not be determined from filename
- `inputs/keys/NEET_answers-key_2020-neet.pdf` — year 2020: sitting could not be determined from filename
- `inputs/keys/NEET_answers-key_2024-neet.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/2019.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/2024.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/AIPMT-2010-Preliminary ..pdf` — year 2010: sitting could not be determined from filename
- `inputs/papers/AIPMT-2011-Preliminary.pdf` — year 2011: sitting could not be determined from filename
- `inputs/papers/neet_2016_code-A_P_W.pdf` — year 2016: sitting could not be determined from filename
- `inputs/papers/neet_2016_code-B_Q_X.pdf` — year 2016: sitting could not be determined from filename
- `inputs/papers/neet_2016_code-C_R_Y.pdf` — year 2016: sitting could not be determined from filename
- `inputs/papers/neet_2016_code-D_S_Z.pdf` — year 2016: sitting could not be determined from filename
- `inputs/papers/neet_2019_code-P1.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/neet_2019_code-P2.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/neet_2019_code-Q2.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/neet_2019_code-R3.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/neet_2019_code-S2.pdf` — year 2019: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-AKANH-E5.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-AKANH-F5.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-AKANH-G5.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-AKANH-H5.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-ANKHA-E2.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-ANKHA-F2.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-ANKHA-G2.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-ANKHA-H2.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-HAKAN-E4.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-HAKAN-F4.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-HAKAN-G4.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-HAKAN-H4.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KANHA-E1.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KANHA-F1.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KANHA-G1.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KANHA-H1.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KHANA-E6.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KHANA-F6.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KHANA-G6.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-KHANA-H6.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-NAKHA-E3.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-NAKHA-F3.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-NAKHA-G3.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2020_code-NAKHA-H3.pdf` — year 2020: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q1.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q2.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q3.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q4.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q5.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-Q6.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R1.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R2.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R3.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R4.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R5.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-R6.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S1.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S2.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S3.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S4.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S5.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-S6.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T1.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T2.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T3.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T4.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T5.pdf` — year 2024: sitting could not be determined from filename
- `inputs/papers/neet_2024_code-T6.pdf` — year 2024: sitting could not be determined from filename

## 10. Judgment calls made for this run

See `docs/OPEN_QUESTIONS.md`, entries dated 2026-10-09 under Section 8 (S0), in full. Summary:

- A CANCELLED sitting requires a paper but not a key (a cancelled exam has no official final key by definition).
- An ambiguous sitting split (file exists but can't be attributed to MAIN vs. PH2/REEXAM/RETEST) counts as `missing` for both candidate sittings, not `present` for either.
- `inputs/_reference/` is excluded from the file<->manifest reconciliation (Codebook Section 7: reference-only, not a formal intake source).
- 2018's paper<->key booklet-code matching was checked individually since it's the one year where that's actually possible from real per-code key files.
- S0's own step status is `flagged` (never `blocked`) even with missing items, since the spec's own "On failure" line for S0 says the rest of the run continues.
