"""Step-specific check for E1 (spec Section 13/E1 + codebook/E1.md + scripts/type_patterns.py).

schemas/E1.json already constrains `question_type` to config/allowed_values.yaml v0.2's 19 values
and `confidence` to high/medium/low. This file adds the rules a schema cannot express:

  (1) `new_type` REQUIRES a non-empty `new_description` -- that string is what E_NEW_CATEGORY
      (normal) carries to Stage F, and spec 13/E1's "On failure: new_type -> E_NEW_CATEGORY
      (normal) with the description" is empty-handed without it.
  (2) THE AGENT MUST NOT BE ANSWERING A QUESTION THE SCRIPT ALREADY DECIDED. Spec 13/E1 is
      explicit: "SCRIPT patterns first (type_patterns.py); AGENT e1-type-tagger ONLY when no
      pattern decides." So this check re-runs scripts/type_patterns.classify() on the real record
      and fails if it returns a value -- the item should never have been dispatched, and letting
      it through would silently replace a deterministic, self-tested classification with a
      judgement. 9 of the 10 real canonical questions are decided by pattern, so this is the
      common case, not a corner.
  (3) When the script DID hand over (classify() -> None), the one real reason it does so today is
      rule 9b: the four OPTIONS are each a chemical reaction (real Q-000005), a shape no spec
      pattern covers. codebook/E1.md §4 says what the agent should do until the owner rules:
      `new_type` with the description. Anything else is allowed but is reported as a segment so
      the gap stays countable in Stage F instead of being absorbed into a near value -- and
      `statement_options` specifically is FAILED, because that is the exact mis-tag already found
      and fixed on this real question ("a reaction equation is not a statement to judge").
  (4) `confidence: low` on a value other than `new_type` is reported. E1 has one run and no
      adjudicator, so a low-confidence agent tag has nothing downstream to catch it; spec 13/E1
      names no flag for it, so this is a plain check failure that triggers E1's retry.

What is DELIBERATELY NOT checked here: whether the chosen type is the RIGHT one. Every mechanical
boundary spec names by question id (2026-May#25, 2015#161, 2014#27, 2015#130) is already encoded
as a passing self-test in scripts/type_patterns.py, which is where it belongs -- re-implementing
those patterns here would create a second, drifting copy of the classifier. A second E1 tag on a
legitimately two-tag question (codebook/E1.md §2, e.g. fill_in_blank + figure_to_read) is recorded
in `new_description`, which is why a non-empty `new_description` on a normal value is NOT an error.

Convention: def check(data, context) -> (bool, str). A failing check returns a ';'-joined set of
segments (runner_core.parse_check_message), each optionally prefixed "<FLAG_CODE>: ..." with one
of this step's own config/steps.yaml flag codes.
"""
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import type_patterns  # noqa: E402
from lib import records as lib_records  # noqa: E402


def question_record(context):
    """The real question record this item is about.

    Prefers context["input_data"]["record"] (what the plugin passes, and what a fixture supplies),
    and falls back to reading papers/records/<QID>.json so the check is testable against real data
    before the E plugins exist. Returns {} when neither is available, and every rule that needs
    the record then degrades to a reported skip rather than a false pass or a crash."""
    rec = (context.get("input_data") or {}).get("record")
    if isinstance(rec, dict) and rec:
        return rec
    qid = str(context.get("item_id") or "").split("#")[0]
    if not qid:
        return {}
    # lib_records.read_record() returns a SKELETON {"question_id", "field_sources"} when the
    # record does not exist, which would read here as a real-but-empty record and SILENTLY skip
    # every rule that needs real fields. Test the file itself instead. (Real gotcha found by
    # tests/test_e_checks.py, 2026-10-12.)
    if not os.path.exists(lib_records.record_path(qid)):
        return {}
    try:
        return lib_records.read_record(qid) or {}
    except Exception:  # noqa: BLE001 -- an unreadable record is a reported skip, never a crash
        return {}


def check(data, context):
    if not isinstance(data, dict):
        return False, "E1 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    question_type = data.get("question_type")
    new_description = (data.get("new_description") or "").strip()
    segments = []

    # (1) new_type needs its one-line description.
    if question_type == "new_type" and not new_description:
        segments.append(
            "E_NEW_CATEGORY: question_type is new_type but new_description is empty; the "
            "description is the whole content of the E_NEW_CATEGORY flag Stage F reviews")

    # (4) low confidence on a real value has nothing downstream to catch it.
    if data.get("confidence") == "low" and question_type != "new_type":
        segments.append(
            f"confidence is low on question_type {question_type!r}; E1 has one run and no "
            f"adjudicator, so use new_type with a description if no listed value really fits")

    record = question_record(context)
    if not record:
        segments.append(
            "no question record available (neither context['input_data']['record'] nor "
            "papers/records/<QID>.json), so the script-decided cross-check could not run")
        return (False, "; ".join(segments)) if segments else (True, "ok")

    script_value, rule = type_patterns.classify(record)

    # (2) the agent must only run when no pattern decided.
    if script_value is not None:
        segments.append(
            f"scripts/type_patterns.py already decides this question as {script_value!r} "
            f"(pattern {rule}), so spec 13/E1 says the agent must not run for it at all; the "
            f"agent answered {question_type!r}")
    else:
        # (3) the script handed over -- today that means the options-are-reactions gap.
        if question_type == "statement_options":
            segments.append(
                f"the patterns handed this question over because {rule}, and `statement_options` "
                f"is the exact mis-tag already found and fixed on real Q-000005: four reaction "
                f"equations are not four statements to judge (codebook/E1.md §4)")
        elif question_type != "new_type":
            segments.append(
                f"the patterns handed this question over because {rule}; codebook/E1.md §4 says "
                f"to answer `new_type` with a description until the owner rules on adding "
                f"`list_of_reactions`, so that the shape stays countable in Stage F rather than "
                f"being absorbed into {question_type!r}")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
