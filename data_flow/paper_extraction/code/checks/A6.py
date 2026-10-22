"""Step-specific check for A6 (spec Section 9/A6 'Checks'): every passage exactly one of
pair/removed/added.

Unlike every other check in this build, A6's real output (ncert/pairs/<CHAPTER>.json, spec 6.4) is
ONE FILE PER CHAPTER holding every passage's row, not one file per agent run -- there is no
dedicated A6 agent (config/steps.yaml: "script + x-adjudicator"). So `data` here is the WHOLE
parsed array for one chapter (matching schemas/A6.json's top-level `array` shape), and `context`
only needs `item_id` (the chapter id) -- there is no single work input file to look at.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
"""


def check(data, context):
    if not isinstance(data, list):
        return False, "A6 output is not an array"

    segments = []
    old_ids = [row.get("old_passage_id") for row in data if row.get("old_passage_id")]
    new_ids = [row.get("new_passage_id") for row in data if row.get("new_passage_id")]

    dup_old = sorted({pid for pid in old_ids if old_ids.count(pid) > 1})
    dup_new = sorted({pid for pid in new_ids if new_ids.count(pid) > 1})
    if dup_old:
        segments.append(f"old_passage_id(s) appear more than once: {dup_old}")
    if dup_new:
        segments.append(f"new_passage_id(s) appear more than once: {dup_new}")

    for row in data:
        result = row.get("result")
        if result == "pair" and not (row.get("old_passage_id") and row.get("new_passage_id")):
            segments.append(f"result=pair row missing one side: {row}")
        elif result == "removed" and row.get("new_passage_id") is not None:
            segments.append(f"result=removed row has a new_passage_id: {row}")
        elif result == "added" and row.get("old_passage_id") is not None:
            segments.append(f"result=added row has an old_passage_id: {row}")
        elif result not in ("pair", "removed", "added"):
            segments.append(f"unknown result {result!r}: {row}")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
