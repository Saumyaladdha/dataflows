"""Step-specific check for F5 (spec 14/F5, CLAUDE.md rule 12).

`data` is one chapter's release-gate verdict (schemas/F5.json shape — what
export_tables.gate() returns and what data/_release_log.jsonl records).

This check exists to make the gate's own integrity checkable after the fact: a release log row
that says `ok: true` while one of its conditions says `ok: false`, or while it carries no
sign-off, would mean something was released that should not have been. The five conditions it
insists on by name are the five the spec names, so a future edit that quietly drops one is
caught here rather than discovered in `data/`.
"""

REQUIRED_CONDITIONS = {
    "queue_empty",
    "subtopic_list_approved",
    "change_log_rows_approved",
    "audit_sample_meets_target",
    "signoff_row",
    "nothing_blocked",
}


def check(data, context):
    if not isinstance(data, dict):
        return False, "F5 output is not an object"
    if not str(data.get("chapter_id") or "").strip():
        return False, "chapter_id is empty"

    conditions = data.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return False, "no gate conditions recorded; a release must record why it was allowed"
    ids = {c.get("id") for c in conditions if isinstance(c, dict)}
    missing = REQUIRED_CONDITIONS - ids
    if missing:
        return False, (f"the gate did not evaluate every condition spec 14/F5 names; missing: "
                       f"{sorted(missing)}")

    failed = sorted(c["id"] for c in conditions if isinstance(c, dict) and not c.get("ok"))
    ok = data.get("ok")
    if not isinstance(ok, bool):
        return False, "`ok` is missing or not a boolean"
    if ok and failed:
        return False, (f"ok=true but these conditions failed: {failed}. A chapter must not be "
                       f"released with any condition unmet, and there is no override.")
    if not ok and not failed:
        return False, "ok=false but every condition passed; the verdict and the conditions disagree"

    signoff = data.get("signoff")
    if ok:
        if not isinstance(signoff, dict):
            return False, ("ok=true with no sign-off row. CLAUDE.md: never release a chapter; "
                           "only export_tables.py does, after a sign-off row in "
                           "review/releases.csv.")
        if not str(signoff.get("signed_by") or "").strip():
            return False, "ok=true but the sign-off row has an empty signed_by"
        if not str(signoff.get("released_at") or "").strip():
            return False, "ok=true but the sign-off row has an empty released_at"

    target = data.get("audit_target")
    if target is not None and not (0 < float(target) <= 1):
        return False, f"audit_target {target!r} is not in (0, 1]"

    if not ok:
        return True, f"note: release refused; unmet conditions: {failed}"
    return True, "ok"
