"""Step-specific check for D3 (spec Section 12/D3 'Writes' + its own Procedure rules).

D3 is a pure SCRIPT step (fetch_passages.py, no agent) -- schemas/D3.json already constrains the
three-list shape (each item {passage_id, text}, latest capped at 15). This file adds what a single
D3 output can check beyond pure shape:
  - no passage_id repeated within one list (a script bug, not a real-world possibility given how
    fetch_passages.py builds each list from a dict keyed by passage_id).
  - no passage_id repeated ACROSS lists (latest/older/lab_manual are meant to be disjoint --
    the same real NCERT passage should never be offered to D4 twice under two different roles).
  - every item's text is non-empty (an empty-text passage slipping through would silently break
    D4's quote verification downstream; worth catching here where the cause is still local).

Whether "zero latest passages" should re-run D2 (spec 12/D3 On failure) is a per-item RUNNER
decision across two different pipeline steps (needs D2's own re-dispatch), not something one D3
output's own check() can decide alone -- that state machine lives in step_plugins.D3Plugin.check(),
the same split as every other bespoke multi-stage chain in this build (C1, A4, A6).

Convention: def check(data, context) -> (bool, str).
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "D3 output is not an object"

    seen_anywhere = {}
    for key in ("latest", "older", "lab_manual"):
        items = data.get(key)
        if not isinstance(items, list):
            return False, f"{key} is not a list"
        seen_here = set()
        for item in items:
            if not isinstance(item, dict):
                return False, f"{key} contains a non-object item"
            pid = item.get("passage_id")
            text = item.get("text")
            if not pid:
                return False, f"{key} has an item with no passage_id"
            if not text or not text.strip():
                return False, f"{key} passage {pid!r} has empty text"
            if pid in seen_here:
                return False, f"{key} repeats passage_id {pid!r}"
            seen_here.add(pid)
            if pid in seen_anywhere:
                return False, (
                    f"passage_id {pid!r} appears in both {seen_anywhere[pid]!r} and {key!r} "
                    f"-- latest/older/lab_manual are meant to be disjoint"
                )
            seen_anywhere[pid] = key

    return True, "ok"
