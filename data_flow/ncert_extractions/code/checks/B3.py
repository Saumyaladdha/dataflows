"""Step-specific check for B3 (spec Section 10/B3 'Checks' + b3-question-reader.md's own rules).

Implements the HARD-failure half of B3's checks only (retry-then-block chain):
  - "exactly four options; each option has text or an image (never both empty)"
    -> option_parser.validate_options (no option_images passed from this agent, per the
    schemas/B3.json DISCREPANCY note -- B3's four options must each carry real/placeholder TEXT).
  - a real, checkable proof point for the Master Plan risk #1 fix (the whole reason this task
    exists): if a transcribed field still contains a known overlay marker ("CORRECT ANSWER",
    "Hide solution") despite B2's box supposedly ending before that card, that is treated as a
    hard transcription-integrity failure, not a soft note -- no catalogue flag code names this
    specific failure (B2/B3's own "Never invent a category" rule applies to AGENT-emitted
    category VALUES, not this script's own internal check-failure labels), so it resolves to the
    generic "<STEP>_CHECK_FAILED" segment per runner_core.parse_check_message, the same way any
    other unrecognised check message does.

Deliberately NOT implemented here: "no two options identical" (B3_DUPLICATE_OPTIONS) and
"statements labelled consecutively" -- spec 10/B3's own "On failure" text says duplicates
CONTINUE (B4 decides), i.e. they are a soft flag-and-keep-going outcome, not a check failure that
blocks or retries; step_plugins.B3Plugin.check() handles that half directly (calling
option_parser.find_duplicate_options itself, raising B3_DUPLICATE_OPTIONS without failing this
check), precisely so this file's one return value doesn't have to conflate two different
severities. "statements labelled consecutively" is left as a future check (not yet seen in real
output at the time of this build pass; see report).

Convention: def check(data, context) -> (bool, str).
"""
from lib import option_parser

_OVERLAY_MARKERS = ("CORRECT ANSWER", "Hide solution", "hide solution")


def check(data, context):
    if not isinstance(data, dict):
        return False, "B3 output is not an object"

    options = data.get("options_en") or {}
    invalid = option_parser.validate_options(options, {})
    if invalid:
        return False, f"B3_OPTION_COUNT: option(s) {invalid} have neither text nor an image crop"

    haystacks = [data.get("stem_en") or ""]
    haystacks += [s.get("text", "") for s in (data.get("statements") or [])]
    haystacks += [s.get("text", "") for s in (data.get("list_i") or [])]
    haystacks += [s.get("text", "") for s in (data.get("list_ii") or [])]
    haystacks += list(options.values())
    blob = "\n".join(haystacks)
    for marker in _OVERLAY_MARKERS:
        if marker in blob:
            return False, (
                f"overlay leakage: transcribed output still contains {marker!r} -- the B2 crop "
                "boundary failed to exclude the answer/solution card (Master Plan risk #1)"
            )

    return True, "ok"
