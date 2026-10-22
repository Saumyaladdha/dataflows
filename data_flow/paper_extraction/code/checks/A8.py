"""Step-specific check for A8 (spec Section 9/A8 'Checks'): runs A and B agree on change_type.
That comparison is inherently cross-run, so it lives in step_plugins.A8Plugin.check() (which has
both runs in hand), not here -- this file checks ONE run's internal validity, which is what's left
once schema validation (already enum-restricted by schemas/A8.json) is done: the fields that
support a change_type actually make sense together.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A8 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    change_type = data.get("change_type")
    segments = []

    if change_type == "unsure":
        return True, "ok (unsure is always allowed, rule 6)"

    if change_type in ("fact_changed",) and data.get("old_fact") == data.get("new_fact"):
        segments.append(f"A8_ADJUDICATED: change_type=fact_changed but old_fact == new_fact ({data.get('old_fact')!r})")

    if change_type == "fact_removed" and (data.get("new_fact") or "").strip():
        segments.append("A8_ADJUDICATED: change_type=fact_removed but new_fact is non-empty")

    if change_type == "fact_added" and (data.get("old_fact") or "").strip():
        segments.append("A8_ADJUDICATED: change_type=fact_added but old_fact is non-empty")

    if not (data.get("why") or "").strip():
        segments.append("A8_ADJUDICATED: why is empty")

    if change_type == "wording_only" and data.get("could_flip_an_answer") not in (True, False):
        segments.append("A8_ADJUDICATED: could_flip_an_answer must be a boolean")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
