# Which corpus is which

Two question corpora exist side by side. This file says what each is for, because the directory
names alone do not, and reading the wrong one is how a measurement gets quoted against the wrong
population.

| directory | status | what it is |
|---|---|---|
| `papers/` | **v1 — reference, frozen** | 698 records, 280 figures, built from three different per-year sources. Measured 87% / 87% (69% vs the real NTA volume) / 75% against the printed papers. Keep it: it is what the new numbers are compared against, and 58 scripts, tests and configs read it. |
| `papers_v2/` | **v2 — live** | Built by `scripts/extract_paper_v2.py` from `Saumya_NEET_work/NEW`, one publisher, one layout, text layer, figures in place, answer printed per question per code. See `docs/PAPER_EXTRACTION_V2.md`. |

## Why `papers/` was not renamed or deleted

It was going to be moved to `papers_v1_reference/`. It is not, and the reason is worth recording
rather than quietly skipping:

**58 files** under `scripts/`, `tests/` and `config/` resolve paths through `"papers"` —
`run_step.py`, `runner_core`, `lib/records`, every Stage B and D plugin, the category sheet builder,
the census checks. Renaming the directory is a 58-file refactor whose only benefit is a tidier name,
and whose failure mode is a path that resolves to nothing and a step that reports zero items as
though there were no work to do. That is a silent failure, which is the worst kind.

So: `papers/` keeps its name and this file records that it is the v1 reference. If it should
actually be moved, the safe order is (1) add a single `CORPUS_ROOT` constant to `runner_core`, (2)
route all 58 call sites through it, (3) run the full test suite, (4) then rename. Ask for that
explicitly; it is not a side effect of extraction work.

## What is NOT duplicated between them

`papers_v2/` is not a superset. It holds, per booklet:

```
papers_v2/papers/<year>_<code>.json     meta, questions, b2_boundaries
papers_v2/crops/<year>_<code>/q###.png  one question image per question   (B3 reads these)
papers_v2/figures/<year>_<code>/        one crop per figure                (B3F reads these)
papers_v2/exports/questions_v2.csv      flat, one row per question
papers_v2/exports/html/                 one paper-like page per booklet, plus an index
```

It does **not** hold the NCERT links, the category tags, the repeat groups or the review decisions
that `papers/records/` carries from Stages C–F. Those were produced against v1 question text and
have to be re-derived, not copied, once v2 question text is confirmed by B3.

## 2026-10-21 — v1 question crops removed

`papers/questions/` held 200 PNG crops across four v1 booklets (NEET-2022-MAIN-Q1, 2023-E1, 2023-E2,
2024-Q1), 46 MB. Deleted, with `papers/pages/` which was empty.

Checked before removing: **zero** of the 698 records in `papers/records/`, and zero step outputs,
referenced any file in it. `scripts/question_assets.py` still names the directory as a lookup path
and will now find nothing there, which is correct behaviour -- but it is why a v1 sheet that
expected a crop would come back blank rather than erroring.

**`papers/figures/` was NOT deleted.** 64 of the 698 records point into it, including the evidence
that settled `b9s-source-figure-confirmer`'s cross-source figure matches. 10 MB is not worth
breaking 64 finished, checked records.

Note that three of those four booklets -- 2023-E1, 2023-E2 and 2024-Q1 -- are NOT in `papers_v2`,
which holds 2023_E3 and 2024_Q2. Their extracted data survives in `papers/records/`; only the
pictures are gone, and recovering them would mean re-cutting from the source PDFs.


## 2026-10-21 · 20 D4V outputs superseded, not deleted

`legacy/d4v_superseded_20261021/` holds the 20 evidence packets that came back `not_at_all` or
`partly` in the first wave and were re-run after the input gained `chapter_index`,
`search_this_file`, `older_edition_passages` and `other_books_you_may_search`. They are kept rather
than deleted because they are the measurement that justified the change: three of them name a
passage that was proved to exist in the book and to have been absent from that run's shortlist
(`BIO12L-CH04-P39`, `BIO12L-CH04-P87`, `PHY12L-CH03-P66`). Deleting them would leave the fix in the
code with no record of what it fixed.

Seven further weak outputs were NOT re-run and NOT moved: `2019_P1` and `2020_F1` print no answer
under any question, so `answer_to_support` is empty for all 352 of their questions and the step has
nothing to find evidence FOR. Those need the answer extraction fixed, or `b6-blind-solver` run over
both papers, before a re-run can do anything but reproduce the same error object.
