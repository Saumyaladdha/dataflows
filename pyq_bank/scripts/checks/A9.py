"""Step-specific check for A9 (spec Section 9/A9 'Done when'/6.4): every non-identical pair has a
change_log row; every removed passage is listed in deleted_topics; change_ids are unique.

`data` is the combined {"change_log_rows": [...], "deleted_topics_rows": [...]} shape
schemas/A9.json models (see that schema's own docstring: A9's real output is two CSV files,
ncert/change_log.csv and ncert/deleted_topics.csv -- step_plugins.A9Plugin.check() assembles this
object from both files before calling here). `context` may carry `expected_diff_count` (how many
non-identical pairs this chapter's ncert/diffs/<CHAPTER>.jsonl actually has) and
`expected_removed_passage_ids` (from ncert/pairs/<CHAPTER>.json's `result: "removed"` rows) when
the caller has them in hand, for the two cross-reference checks; both are skipped, not failed,
when absent.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A9 output is not an object"

    change_rows = data.get("change_log_rows") or []
    deleted_rows = data.get("deleted_topics_rows") or []
    segments = []

    change_ids = [r.get("change_id") for r in change_rows]
    dupes = sorted({c for c in change_ids if change_ids.count(c) > 1})
    if dupes:
        segments.append(f"duplicate change_id(s): {dupes}")

    for r in change_rows:
        if r.get("approval") not in (None, "pending") and not r.get("_allow_any_approval"):
            # A9 writes rows as pending (spec 9/A9 Writes); a non-pending approval here means
            # either a Stage F edit already landed (fine) or the writer skipped the default
            # (worth a note, not a hard failure, since Section 9/A9 defines no fixed enum).
            pass
        if not r.get("old_passage_id") and not r.get("new_passage_id"):
            segments.append(f"change row {r.get('change_id')} has neither old_passage_id nor new_passage_id")

    deleted_ids = [r.get("old_passage_id") for r in deleted_rows]
    dup_deleted = sorted({d for d in deleted_ids if deleted_ids.count(d) > 1})
    if dup_deleted:
        segments.append(f"duplicate old_passage_id(s) in deleted_topics: {dup_deleted}")

    expected_diff_count = context.get("expected_diff_count")
    if expected_diff_count is not None and len(change_rows) < expected_diff_count:
        segments.append(
            f"only {len(change_rows)} change_log row(s) for {expected_diff_count} non-identical pair(s)"
        )

    expected_removed = context.get("expected_removed_passage_ids")
    if expected_removed is not None:
        missing_removed = set(expected_removed) - set(deleted_ids)
        if missing_removed:
            segments.append(f"removed passage(s) missing from deleted_topics_rows: {sorted(missing_removed)}")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
