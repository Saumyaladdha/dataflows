tests/fixtures/stage_e_plugins/ - FIXTURE DATA ONLY. NOT REAL PIPELINE DATA.

Hand-built input for tests/test_e_plugins.py, which unit-tests the SEVEN Stage E runner plugins
in scripts/step_plugins.py (E0Plugin .. E6Plugin): which items they dispatch, what they put in an
agent's input, how the retry / second-run / adjudicator / safe-default chains resolve, and that
each step's codebook reaches its agent with its hash recorded.

WHY FIXTURES AT ALL. Stage E cannot run end to end on real data: E1 needs a resolved D7, D7 needs
D6, and D6 is agent-driven (d6-status-note-writer) and has never been dispatched in this project,
so NO real question has reached any E step. Every agent output in the tests is invented too - no
E agent has ever run here, so there is no real E output to test against. A test showing a plugin
dispatches, merges and falls back correctly proves the wiring; it does not prove any tag is right.

NOTHING HERE MAY BE COPIED INTO THE REAL papers/, steps/, ncert/, flags/ OR review/ PATHS. The
test copies this tree into a temporary directory and repoints PROJECT_ROOT at the copy; the real
project is never written to. (docs/OPEN_QUESTIONS.md 2026-10-10 records what happened the one
time fixture data was written into real paths.)

Ids use spec 6.1's real grammar - otherwise the plugins' id handling would not be exercised - but
sit in deliberately impossible ranges:
  * questions  Q-991001 .. Q-991007   (the real counter is in the Q-0000xx range; stage_f's
                                       fixtures own Q-9900xx)
  * chapters   PHY11-CH99, CHE12-CH99
  * passages   PHY11L-CH99-P01 ...

THE SEVEN QUESTIONS, and the branch of Stage E each one exists to exercise:

  Q-991001  Physics, normal, answer 1. scripts/type_patterns.py decides it by pattern 16
            (single_statement) and scripts/describe_tags.py decides stem_context by pattern
            (`plain`, no context fired) -> E1 and E6 both resolve SCRIPT-only, no agent line.
            Also the happy path for E2/E3/E4 and for E5's normal 3-wrong-option case.
  Q-991002  Chemistry/organic, normal, answer 3, four options that are each a REACTION and no
            figure - the real Q-000005 shape, the one shape no spec E1 pattern covers, so
            type_patterns.classify returns None and E1 must dispatch e1-type-tagger.
  Q-991003  Chemistry/organic, normal, answer 1, reaction wording AND a figure, so TWO
            describe_tags context patterns fire (`reaction_given` + `figure_given`), spec 13/E6's
            tie-break needs judgement, and E6 must dispatch e6-context-tagger.
  Q-991004  multiple_accepted, official_answer "1,3" (B5 writes a multiple-accepted key
            comma-joined) -> E5 must create exactly TWO items, not three.
  Q-991005  dropped with an empty official key and a B8 corrected_answer of "1" - the live branch
            config/steps.yaml's E5 safe_default names - -> E5 treats the correction as the answer
            and creates items for the remaining three options.
  Q-991006  dropped with an empty official key and NO corrected_answer -> E5 creates NO item at
            all and records the question `skipped`. It must never invent a wrong option.
  Q-991007  Chemistry with branch `unsure` - the real state of every Biology record too - for
            E4's branch rule (the input must carry `branch` even when its value is useless).

UPSTREAM STATUSES. steps/D7/, steps/D8/, steps/E1/ .. steps/E4/ hold hand-written `pass` status
files only so each E step's `needs` gate opens; nothing was run to produce them.
