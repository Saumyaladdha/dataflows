"""Step-specific check for D1 (spec Section 12/D1 'Checks' + d1-chapter-picker.md's own rules).

Shape/internal-consistency checks only (same scope boundary as scripts/checks/C1.py/B8.py's own
docstrings): schemas/D1.json already constrains chapter_ids to a 1-2 item array of strings and
confidence to high/medium/low. What this file adds, using the per-item `context["input_data"]`
the step_plugins.D1Plugin run passes alongside the agent output (same pattern as A4Plugin._run_check
passing {"all_passage_ids": ...}):
  - chapter_ids is exactly ["unsure"], OR every id in it is a real id from the chapter list the
    agent was actually shown (context["input_data"]["all_chapter_ids"]) -- "ids exist" (spec 12/D1
    Checks). An id outside that list is flagged D1_UNKNOWN_CHAPTER (a genuine schema-valid but
    content-wrong output, same spirit as C1's own content checks beyond pure shape).
  - "unsure" is never mixed with a real id (the agent file's own allowed_values: chapter_ids is
    EITHER one/two real ids OR exactly ["unsure"], never both).
  - no duplicate id.
"Runs agree" (the other half of spec 12/D1's Checks line) needs BOTH runs' outputs at once, so it
is cross-run logic living in step_plugins.D1Plugin.check(), not here (same split as A4's own
match-rate/merge logic living in A4Plugin, not scripts/checks/A4.py).

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "D1 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    ids = data.get("chapter_ids")
    if not isinstance(ids, list) or not ids:
        return False, "chapter_ids must be a non-empty list"

    if ids == ["unsure"]:
        pass
    else:
        if "unsure" in ids:
            return False, "chapter_ids mixes 'unsure' with real chapter id(s)"
        if len(ids) != len(set(ids)):
            return False, f"chapter_ids has duplicate entries: {ids}"
        allowed = set((context.get("input_data") or {}).get("all_chapter_ids") or [])
        unknown = [i for i in ids if i not in allowed]
        if unknown:
            return False, (
                f"D1_UNKNOWN_CHAPTER: chapter_ids {unknown} not among the chapter ids the agent "
                f"was actually shown ({sorted(allowed)})"
            )

    confidence = data.get("confidence")
    if confidence not in ("high", "medium", "low"):
        return False, f"confidence {confidence!r} is not high/medium/low"

    return True, "ok"
