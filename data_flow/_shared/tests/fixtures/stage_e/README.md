# tests/fixtures/stage_e — HAND-BUILT FIXTURES, NOT REAL PIPELINE DATA

Every file in this directory is **invented test data**, written on 2026-10-12 for
`tests/test_e_checks.py`. None of it came out of a real paper, a real agent call or a real run.

**Nothing here may ever be copied into a real pipeline path** — not `papers/records/`, not
`steps/*/out/`, not `codebook/`, not `flags/`. Fixture data written into a real path was a real
mistake made once already in this project (`docs/OPEN_QUESTIONS.md`, 2026-10-10) and cost real
cleanup. Every `question_id` here is deliberately outside the real `Q-%06d` series so a stray file
could never be mistaken for a bank record, and every fixture carries a `_fixture` key saying so.

## Why each fixture exists — i.e. what real data could NOT cover

The 10 real canonical records in `papers/records/` cover most of Stage E's checks, and
`tests/test_e_checks.py` uses them wherever they reach. These fixtures exist only for the cases
the real bank cannot currently produce:

| File | The case real data cannot reach |
|---|---|
| `record_negative_with_combination_options.json` | A question with a negative word **and** combination options — the second row of spec 13/E2's negative-word guard. Real `Q-000005` has `NOT` but its options are reactions (single items); real `Q-000015` has combination options but no negative word. No real record has both, so the guard's combination branch is otherwise untested. |
| `record_negative_with_match_code_options.json` | The same guard row for match-code options. No real record is a match-the-lists question at all. |
| `e0_grouper_output.json` | An `e0-category-grouper` output. E0 has never run: it needs ~300 questions and the bank holds 10. Needed to test that `scripts/e0_category_sheet.py` lays out spec 13/E0's eleven columns correctly. |
