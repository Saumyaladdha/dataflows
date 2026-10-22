"""Step-specific check for A4 (spec Section 9/A4 'Checks'): every passage covered by >= 1
subtopic; names unique; 4-15 subtopics (SOFT -- outside the range flags only, doesn't fail this
check); run A/run B match rate >= 70% (SOFT, and a cross-run comparison besides -- computed by
step_plugins.A4Plugin.check() across both runs, not here).

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring. This
file checks ONE run's output in isolation (the per-run hard requirements); the soft count check is
folded into the return message as a "note:" even when the check otherwise passes, so the caller
can see it without the whole run being treated as failed (spec: "soft: outside -> flag only").

context["input_data"] may include `all_passage_ids` (every passage id the chapter actually has) --
when absent (no real upstream passage data yet), the coverage check is skipped rather than failed,
since there is nothing to compare "covered" against.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A4 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    subtopics = data.get("subtopics") or []
    segments = []
    notes = []

    names = [s.get("name") for s in subtopics]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        segments.append(f"A4_SUBTOPICS_DRAFT: duplicate subtopic name(s): {dupes}")

    input_data = context.get("input_data") or {}
    all_passage_ids = input_data.get("all_passage_ids")
    if all_passage_ids:
        covered = set()
        for s in subtopics:
            covered.update(s.get("passages") or [])
        uncovered = set(all_passage_ids) - covered
        if uncovered:
            segments.append(f"A4_SUBTOPICS_DRAFT: passage(s) not covered by any subtopic: {sorted(uncovered)}")

    n = len(subtopics)
    if not (4 <= n <= 15):
        notes.append(f"note: {n} subtopics is outside the usual 4-15 range (soft check only)")

    if segments:
        return False, "; ".join(segments)
    return True, "; ".join(notes) if notes else "ok"
