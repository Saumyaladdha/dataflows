"""Step-specific check for A5 (spec Section 9/A5 'Checks'): exactly one subtopic id or "none";
the id exists in the chapter's real subtopic list.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
context["input_data"] is the A5 agent input: passage (id, edition, kind, full text), subtopics
(id, name, short description, for this chapter's latest edition). `valid_subtopic_ids` is derived
from `input_data["subtopics"]` when present.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "A5 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    subtopic_id = data.get("subtopic_id")
    if subtopic_id in (None, ""):
        return False, "A5_UNSURE: subtopic_id is empty"
    if subtopic_id == "unsure":
        return True, "ok (unsure is always allowed, rule 6; resolved via the fallback chain)"
    if subtopic_id == "none":
        return True, "ok"

    input_data = context.get("input_data") or {}
    valid_ids = {s.get("id") or s.get("subtopic_id") for s in (input_data.get("subtopics") or [])}
    if valid_ids and subtopic_id not in valid_ids:
        return False, f"A5_UNSURE: subtopic_id {subtopic_id!r} is not one of this chapter's subtopics {sorted(valid_ids)}"

    return True, "ok"
