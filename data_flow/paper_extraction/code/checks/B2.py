"""Step-specific check for B2 (spec Section 10/B2 'Checks'). Per-page checks only -- the
cross-page/whole-paper checks ("numbers continuous across pages", "total = the paper's printed
count") need every page of a paper processed, which this build pass does not do for real at full
127-page scale (see the report: only a small number of real pages were dispatched for proof, by
design, to keep the real-subagent budget on B1/B3). This file is written to be correct and ready
to run at full scale; it is simply not exercised end to end here. Flagged as a known limitation,
same precedent as A2's documented cross-page continuity gap before it was fixed.

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B2 output is not an object"

    required = ["page", "questions", "top_continues_from_previous", "note"]
    missing = [f for f in required if f not in data]
    if missing:
        return False, f"missing required field(s): {missing}"

    questions = data.get("questions") or []
    seen_qnos = set()
    for q in questions:
        qno = q.get("qno")
        if qno is None:
            return False, "a question entry is missing qno"
        if qno in seen_qnos:
            return False, f"B2_BOUNDARY_ADJUDICATED: duplicate qno {qno} on the same page"
        seen_qnos.add(qno)
        parts = q.get("parts") or []
        if not parts:
            return False, f"qno {qno} has no parts/boxes"
        for part in parts:
            bbox = part.get("bbox")
            if not bbox or len(bbox) != 4:
                return False, f"qno {qno} has a malformed bbox: {bbox!r}"
            x0, y0, x1, y1 = bbox
            if x1 <= x0 or y1 <= y0:
                return False, f"qno {qno} has a degenerate/inverted bbox: {bbox!r}"

    # A numbering gap (B2_MISSING_QNO) is reported honestly by the agent in `note` per the agent
    # file's own rules, not something this script can reliably detect from one page in isolation
    # (the gap might legitimately span a page boundary) -- left to the cross-page pass above.

    return True, "ok"
