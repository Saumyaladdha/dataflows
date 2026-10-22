"""Step-specific check for D2 (spec Section 12/D2 'Checks' + d2-subtopic-picker.md's own rules).

Mirrors scripts/checks/D1.py exactly, one level down: subtopic_ids instead of chapter_ids,
cross-referenced against context["input_data"]["all_subtopic_ids"] -- the subtopic id list(s)
(one chapter, or two for a two-chapter D1 question) the agent was actually shown, per the step's
own Input line ("that chapter's subtopic list (id, name, one-line description). For two chapters,
both lists."). "Runs agree" lives in step_plugins.D2Plugin.check(), same split as D1.

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "D2 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    ids = data.get("subtopic_ids")
    if not isinstance(ids, list) or not ids:
        return False, "subtopic_ids must be a non-empty list"

    if ids == ["unsure"]:
        pass
    else:
        if "unsure" in ids:
            return False, "subtopic_ids mixes 'unsure' with real subtopic id(s)"
        if len(ids) != len(set(ids)):
            return False, f"subtopic_ids has duplicate entries: {ids}"
        allowed = set((context.get("input_data") or {}).get("all_subtopic_ids") or [])
        unknown = [i for i in ids if i not in allowed]
        if unknown:
            return False, (
                f"D2_UNKNOWN_SUBTOPIC: subtopic_ids {unknown} not among the subtopic ids the "
                f"agent was actually shown ({sorted(allowed)})"
            )

    confidence = data.get("confidence")
    if confidence not in ("high", "medium", "low"):
        return False, f"confidence {confidence!r} is not high/medium/low"

    return True, "ok"
