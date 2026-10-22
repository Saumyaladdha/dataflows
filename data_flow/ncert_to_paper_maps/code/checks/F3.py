"""Step-specific check for F3 (spec 14/F3).

`data` is one apply_review.py report (schemas/F3.json shape).

What this enforces beyond the schema:
  * no applied decision is missing its reviewer or date;
  * every correct/edit wrote its new value to a NEW steps/F2/out/ file — the one mechanism that
    keeps "never edit an agent's output" true;
  * a report with errors is a failing check, so a malformed decisions.csv row cannot be mistaken
    for a clean apply;
  * a correct/edit that cascaded to nothing is surfaced as a note, not hidden: it is legitimate
    (not every field is read by a step) but it is also how a missing cascade.yaml entry looks.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "F3 output is not an object"
    errors = data.get("errors") or []
    if errors:
        first = errors[0]
        detail = first.get("why") if isinstance(first, dict) else str(first)
        return False, f"{len(errors)} decision row(s) were rejected; first: {detail}"

    notes = []
    for entry in data.get("applied") or []:
        if not isinstance(entry, dict):
            return False, f"applied entry is not an object: {entry!r}"
        target = entry.get("target")
        if not str(entry.get("reviewer") or "").strip():
            return False, f"{target}: applied with no reviewer"
        if not str(entry.get("decided_at") or "").strip():
            return False, f"{target}: applied with no decided_at"
        decision = entry.get("decision")
        if decision in ("correct", "edit"):
            out = entry.get("f2_output") or ""
            if not out.startswith("steps/F2/out/"):
                return False, (f"{target}: a {decision} did not write a new steps/F2/out/ file "
                               f"(got {out!r}); the original agent output must never be edited "
                               f"in place")
            if not entry.get("cascade_steps"):
                notes.append(f"{target}: field {entry.get('field')!r} cascaded to no step")

    cascade = data.get("cascade") or {}
    pairs = cascade.get("pairs")
    marked = cascade.get("marked_stale")
    if not data.get("dry_run") and isinstance(pairs, int) and isinstance(marked, int) \
            and pairs != marked:
        return False, f"cascade planned {pairs} pair(s) but marked {marked} stale"

    if notes:
        return True, "note: " + "; ".join(notes)
    return True, "ok"
