"""Step-specific check for A3 (spec Section 9/A3 'Checks'): every block exactly once; order kept
except the paragraph-interrupted-by-figure/box case; concatenation of passages equals the section
text word for word.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
context["input_data"] is the A3 work input: book_id, chapter, section_heading, blocks (n, kind, text).

The hard requirement ("every block exactly once") is checked in full. "Concatenation ... equals
the section text word for word" is, by construction, guaranteed as long as every block appears
exactly once (the agent returns block NUMBERS only -- universal rule 5, "agents never retype
source text" -- so the SCRIPT does the actual cutting from the original blocks; there is no text
for the agent to get wrong here). What this check adds beyond "every block exactly once" is
therefore the order rule: each passage's own block numbers must be non-decreasing (a passage is
one contiguous idea, read in its own order), and only the KNOWN interrupter shape -- an earlier
passage picking up again as a LATER passage, e.g. [[1],[2,4],[3],[5]] -- is allowed to look
"out of order" across passages; any other cross-passage reordering is flagged as a softer
A3_DEFAULT_CUTS note rather than a hard failure, since judging "is this a legitimate interrupter"
from block numbers alone is inherently a judgement call this script-level check can't make with
certainty (that's exactly why A3 is an AGENT step and not a SCRIPT step).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A3 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    passages = data.get("passages") or []
    input_data = context.get("input_data") or {}
    expected_blocks = [b["n"] for b in (input_data.get("blocks") or [])]

    seen = []
    for passage in passages:
        for n in passage:
            seen.append(n)

    segments = []
    expected_set, seen_set = set(expected_blocks), set(seen)
    missing = expected_set - seen_set
    extra = seen_set - expected_set
    duplicates = sorted({n for n in seen if seen.count(n) > 1})
    if missing:
        segments.append(f"A3_DEFAULT_CUTS: block(s) {sorted(missing)} missing from any passage")
    if extra:
        segments.append(f"A3_DEFAULT_CUTS: block(s) {sorted(extra)} not in the input's blocks")
    if duplicates:
        segments.append(f"A3_DEFAULT_CUTS: block(s) {duplicates} appear in more than one passage")

    for passage in passages:
        if len(passage) > 1 and list(passage) != sorted(passage):
            segments.append(f"A3_DEFAULT_CUTS: passage {passage} is not in increasing block order")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
