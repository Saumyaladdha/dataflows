"""Step-specific check for B7 (spec Section 10/B7 + b7-chem-branch-sorter.md's own rules). Only
ever called for a Chemistry question's AGENT output (Physics/Biology/undetected-subject resolve
SCRIPT-only inside step_plugins.B7Plugin.check(), never through this file) -- validates the one
thing a single agent output can check on its own: well-formed per schemas/B7.json. The "unsure ->
adjudicator -> keyword-rank fallback" chain (spec 10/B7 "On failure") is a cross-run/SCRIPT
decision, so it lives in step_plugins.B7Plugin.check() itself, same precedent as B4's own
field-by-field comparison living in its plugin rather than here.

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B7 output is not an object"

    required = ["branch", "confidence", "why"]
    missing = [f for f in required if f not in data]
    if missing:
        return False, f"missing required field(s): {missing}"

    if data.get("branch") == "unsure":
        return False, f"B7_BRANCH_GUESS: agent returned unsure -- {data.get('why', '')}"

    return True, "ok"
