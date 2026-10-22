"""Step-specific check for S0 (spec Section 8 'Checks': every required file has exactly one
manifest row and the input tree reconciles; each missing item has a flag).

Convention used by every scripts/checks/<STEP>.py in this build:
    def check(data, context) -> (passed: bool, message: str)
`data` is the already schema-valid parsed output being checked (per S0, one record from
steps/S0/out/<item>.json, matching schemas/S0.json). `context` is a dict that always has
`item_id`/`step`/`project_root`, plus whatever that step's run_step.py plugin adds -- for S0,
`open_flags` (a list of open flags/flags.jsonl rows, loaded once by the caller, so this check can
confirm a `status: "missing"` record really did raise S0_MISSING_INPUT rather than re-reading the
whole flags file per item).

On failure, `message` is a "; "-joined list of segments, each optionally "<FLAG_CODE>: <detail>"
using a code from config/steps.yaml's S0 `flags` map -- here just S0_MISSING_INPUT.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "S0 output is not an object"

    item_type = data.get("item_type")
    status = data.get("status")
    if item_type not in ("ncert_book", "lab_manual", "paper", "key", "legacy_sheet"):
        return False, f"unknown item_type {item_type!r}"
    if status not in ("present", "missing", "out_of_scope"):
        return False, f"unknown status {status!r}"

    if status == "missing":
        open_flags = context.get("open_flags") or []
        item_id = context.get("item_id")
        has_flag = any(
            f.get("code") == "S0_MISSING_INPUT" and f.get("item_id") == item_id
            for f in open_flags
        )
        if not has_flag:
            return False, (
                f"S0_MISSING_INPUT: record {item_id!r} has status=missing but no matching "
                "S0_MISSING_INPUT flag was found in flags/flags.jsonl"
            )

    if status == "present" and item_type in ("ncert_book", "lab_manual", "legacy_sheet") and not data.get("note"):
        # present records should explain what was found (spec 8/S0 pitfalls: silent passes hide
        # real problems); not a hard requirement of the spec text, so this is advisory only.
        return True, "ok (note: 'present' record has no explanatory note)"

    return True, "ok"
