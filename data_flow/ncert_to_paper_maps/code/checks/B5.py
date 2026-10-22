"""Step-specific check for B5 (spec Section 10/B5 'Checks' + b5-key-copier.md's own rules).

'every question exactly one row' and 'key text layer agrees' are cross-referenced against a real
paper's full question set (needs B2/B3 fully run for the paper) and are therefore enforced at the
register/join level in step_plugins.B5Plugin, not purely from one output in isolation here (same
precedent as B1's register-level checks). This file validates what a single B5 output can check
on its own: the row shape itself (answer pattern is already schema-enforced by schemas/B5.json;
this adds the "no duplicate qno in one key page" sanity check, a real, cheap cross-row check
within the one output).

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B5 output is not an object"
    rows = data.get("rows") or []
    if not rows:
        return False, "B5_KEY_ROW_MISSING: no rows at all in this key page's output"
    seen = set()
    for row in rows:
        qno = row.get("qno")
        if qno is None:
            return False, "a key row is missing qno"
        if qno in seen:
            return False, f"duplicate qno {qno} within one key page's rows"
        seen.add(qno)
    return True, "ok"
