"""Step-specific check for B4 (spec Section 10/B4). B4's own real work is a field-by-field
COMPARISON between two independent readings (SCRIPT text-layer extraction vs B3, or
b4-second-reader vs B3) after latex_normalise -- that comparison is inherently a two-reading,
cross-item operation, so it lives in step_plugins.B4Plugin.check() itself (same shape as A8's
run-A/run-B agreement check, which is also implemented directly in its plugin rather than through
this per-output schema-check file). This file still exists, per config/steps.yaml's
`check: scripts/checks/B4.py` pointer, to do the one thing a SINGLE B4 output can validate in
isolation: that it is well-formed per schemas/B4.json's two branches.

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "B4 output is not an object"
    options = data.get("options_en") or {}
    for key in ("1", "2", "3", "4"):
        if key not in options:
            return False, f"B4 output missing option {key!r}"
    return True, "ok"
