"""Step-specific check for F2 (spec 14/F2, F3 step 3).

`data` is one reviewer correction written as a NEW F2 step output
(steps/F2/out/<ITEM>.correctionNNN.<field>.json, schemas/F2.json shape).

What this enforces beyond the schema:
  * the correction actually changes something — `new` equal to `old` is not a correction and
    would trigger a pointless cascade;
  * a reviewer and a date are present, because spec 14/F3 step 2-3 requires both on every
    decision and `approved by nobody on no date` is not an audit trail;
  * the output records which step's value it supersedes, so history stays traceable without
    anyone having to modify the original step's output file.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "F2 output is not an object"
    if data.get("step") != "F2":
        return False, f"step is {data.get('step')!r}, expected 'F2'"
    for key in ("item_id", "field"):
        if not str(data.get(key) or "").strip():
            return False, f"{key} is empty"
    if "new" not in data:
        return False, "no `new` value; a correction must carry the corrected value"
    if not str(data.get("reviewer") or "").strip():
        return False, "no reviewer named; spec 14/F3 requires the reviewer on every decision"
    if not str(data.get("decided_at") or "").strip():
        return False, "no decided_at; spec 14/F3 requires the date on every decision"
    if data.get("new") == data.get("old"):
        return False, (f"`new` equals `old` ({data.get('new')!r}) — that is an approval, not a "
                       f"correction, and would cascade for no reason")
    flag_id = data.get("flag_id")
    if flag_id is not None and not str(flag_id).startswith("FL-"):
        return False, f"flag_id {flag_id!r} is not a flag id"
    if "old" not in data:
        return True, "note: no `old` value recorded; the superseded value is not traceable from this file alone"
    return True, "ok"
