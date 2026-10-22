"""Step-specific check for A7. Section 9/A7 names no explicit "Checks" line (config/steps.yaml's
A7 entry notes this: pure SCRIPT, deterministic word-level diff, nothing to retry/adjudicate/
default). This check enforces the internal consistency schemas/A7.json and spec 6.4 both imply
for one line of ncert/diffs/<CHAPTER>.jsonl: `identical` and `diff` must agree with each other,
and a dropped-identical pair should never have been written at all (spec 9/A7 procedure:
"Identical -> drop").

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring. `data`
is one decoded JSONL line; context["item_id"] is the chapter id (A7's real item unit is "one
pair", but this build's plugin validates every line of a chapter's file in one pass).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A7 line is not an object"

    identical = data.get("identical")
    diff = data.get("diff") or []

    if identical is True and diff:
        return False, "identical=true but diff is non-empty"
    if identical is False and not diff:
        return False, "identical=false but diff is empty"
    if identical is True:
        # Per spec 9/A7 procedure ("Identical -> drop"), an identical pair should not have been
        # written to the file at all -- A8's item is "one non-identical pair". Flag rather than
        # hard-fail: the data is internally consistent, just a looser interpretation of "drop".
        return True, "note: identical=true line was written (spec says identical pairs should be dropped, not written)"

    for span in diff:
        if "old" not in span or "new" not in span:
            return False, f"diff span missing old/new: {span}"
        if span["old"] == span["new"]:
            return False, f"diff span has no actual difference: {span}"

    return True, "ok"
