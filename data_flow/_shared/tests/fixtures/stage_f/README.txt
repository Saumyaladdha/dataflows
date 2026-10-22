tests/fixtures/stage_f/ — FIXTURE DATA ONLY. NOT REAL PIPELINE DATA.

Hand-built input for tests/test_stage_f.py (Stage F: F1 review pack, F3 apply + cascade, F4
counts, F5 release gate, F6 gold scoring). Every question, flag, subtopic, change-log row, gold
row and sign-off in this folder is invented so the Stage F code paths that have no real data yet
can be exercised end to end.

NOTHING HERE MAY BE COPIED INTO THE REAL ncert/, papers/, steps/, flags/, review/, data/ OR gold/
PATHS. The test copies this tree into a temporary directory and points the scripts' PROJECT_ROOT
at the copy; the real project is never written to. (See docs/OPEN_QUESTIONS.md 2026-10-10 for
what happened the one time fixtures were written into real paths.)

Ids use the REAL grammar of spec 6.1 — otherwise Stage F's id parsing would not be exercised at
all — but sit in deliberately impossible ranges so they can never be confused with real data:
  * questions  Q-990001 .. Q-990006   (the real counter is in the Q-0000xx range)
  * chapters   BIO12-CH91, BIO12-CH92 (NCERT Biology class 12 has 16 chapters)
  * passages   BIO12L-CH91-P01, ...
  * flags      FL-990001 ..           (the real counter is in the FL-0001xx range)
  * changes    CL-9901, CL-9902

Deliberate properties:
  * 6 questions across 2 chapters, 3 subjects and 4 years, so the audit sample has more than one
    (subject, year) stratum and the "recent" mixes have both recent (>= 2021) and older rows.
  * Q-990002 and Q-990003 share repeat group RG-9901, so unique_questions < questions_total.
  * Q-990005 is already released, so the released-only counts are a strict, non-empty subset.
  * Q-990006 is merged into Q-990005, so canonical-only counting is exercised.
  * One flag per F1 priority band, including the codes the ordering special-cases.
  * BIO12-CH91 can be driven to a clean release; BIO12-CH92 fails the gate on purpose.
