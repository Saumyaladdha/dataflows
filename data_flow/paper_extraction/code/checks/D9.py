"""Step-specific check for D9 (spec Section 12/D9 'Checks' + d9-repeat-finder.md's own rules).

spec 12/D9 Checks, verbatim and complete: "ids exist, same subtopic, other year." All three need
the per-item candidate table step_plugins.D9Plugin passes as
`context["input_data"]["others"]` = {qid: {"year": int, "sitting": str, "subtopics": [...]}},
alongside this question's own id/year/subtopics.

  (1) ids exist -- every id in possible_repeats is a key of that table. The table IS the agent's
      allowed-values list (d9-repeat-finder.md Allowed values: "IDs from `others` only"), so an id
      outside it was invented or hallucinated, not merely over-included.
  (2) same subtopic -- the id shares at least one subtopic with this question. (The plugin only
      ever builds the table from same-subtopic questions, so this check is a guard on the
      PLUGIN as much as on the agent; it is cheap and it catches a table-building bug that would
      otherwise surface as a wrong repeat group three steps later.)
  (3) other year -- the id's year differs from this question's year.

      *** SPEC QUESTION RAISED, IMPLEMENTED AS WRITTEN ANYWAY. *** This rule makes a repeat
      between two SITTINGS OF THE SAME YEAR structurally unfindable: 2016 MAIN/PH2, 2019
      MAIN/REEXAM, 2020 MAIN/REEXAM, 2024 MAIN/RETEST, and above all 2026 CANCELLED (3 May) /
      REEXAM (21 Jun) -- a cancelled paper and its re-exam being the single most likely place in
      the corpus for one fact to be asked twice inside one year. Spec says "other years" and this
      file enforces exactly that, because silently widening a spec rule is worse than reporting
      it. codebook/D11.md §6 raises the same question independently. Owner's call; if the answer
      is "widen it", the change is one line here plus one in D9Plugin._others_table (swap the
      year comparison for a (year, sitting) comparison), and nothing else in D9/D10/D11 needs to
      move.
  (4) shape consistency: `none` is true exactly when possible_repeats is empty; no duplicates;
      never this question's own id (the agent file's own Never rule).

What is DELIBERATELY NOT checked here: whether a candidate is a REAL repeat. D9 is a wide net by
design ("inclusive. If unsure, include"), and D11 is the strict verdict. A long possible_repeats
list is not a defect and must never fail this check.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined, each optionally
prefixed "<FLAG_CODE>: ..." using one of this step's own config/steps.yaml flag codes.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "D9 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    repeats = data.get("possible_repeats")
    none_flag = data.get("none")
    if not isinstance(repeats, list):
        return False, "possible_repeats is not a list"
    if not isinstance(none_flag, bool):
        return False, "none is not a boolean"

    input_data = context.get("input_data") or {}
    this_id = input_data.get("this_id")
    this_year = input_data.get("this_year")
    this_subtopics = set(input_data.get("this_subtopics") or [])
    others = input_data.get("others") or {}

    segments = []

    if none_flag and repeats:
        segments.append(f"none is true but possible_repeats lists {len(repeats)} id(s)")
    if not none_flag and not repeats:
        segments.append("possible_repeats is empty but none is false")

    if len(repeats) != len(set(repeats)):
        dupes = sorted({r for r in repeats if repeats.count(r) > 1})
        segments.append(f"possible_repeats has duplicate id(s): {dupes}")

    for qid in dict.fromkeys(repeats):  # dedup, preserve order, report each problem once
        if this_id and qid == this_id:
            segments.append(f"D9_BAD_CANDIDATE: possible_repeats lists this question's own id {qid!r}")
            continue
        other = others.get(qid)
        if other is None:
            segments.append(
                f"D9_BAD_CANDIDATE: {qid!r} is not one of the candidate questions given "
                f"({len(others)} were)"
            )
            continue
        shared = this_subtopics & set(other.get("subtopics") or [])
        if this_subtopics and not shared:
            segments.append(
                f"D9_BAD_CANDIDATE: {qid!r} shares no subtopic with this question "
                f"(this: {sorted(this_subtopics)}, that: {sorted(other.get('subtopics') or [])})"
            )
        if this_year is not None and other.get("year") == this_year:
            segments.append(
                f"D9_BAD_CANDIDATE: {qid!r} is from the SAME year ({this_year}); spec 12/D9 scopes "
                f"repeat candidates to other years (see this file's docstring -- a real spec "
                f"question, not a bug)"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
