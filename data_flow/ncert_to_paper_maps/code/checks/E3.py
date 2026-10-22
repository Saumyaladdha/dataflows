"""Step-specific check for E3 (spec Section 13/E3 + codebook/E3.md).

schemas/E3.json already constrains `content_shape` to config/allowed_values.yaml v0.2's 29 values
and requires a non-empty `why`. This file adds:

  (1) `new_shape` REQUIRES a non-empty `new_description` (that string is E_NEW_CATEGORY's content).
  (2) `why` must have SUBSTANCE. Spec 13/E3 says E3 judges the NCERT material through D4's
      evidence lines, and codebook/E3.md §2 says to write `why` naming the evidence -- "Evidence
      is the ordered stages of mitosis" is checkable, "Tests process understanding" is not. The
      mechanical floor: a real sentence (>= 4 words), and it must not be a bare restatement of
      the tag name. A script cannot judge whether a sentence names the evidence; it can refuse
      a sentence too short to name anything.
  (3) `current_affairs` against D6. codebook/E3.md §3: "if you tag `current_affairs` and D6 says
      `latest_ncert`, one of the two is wrong." `current_affairs` is defined as a time-bound fact
      in NO edition, so it is always outside NCERT -- a contradiction with the record's own
      `syllabus_status` is a real, mechanically detectable error, not a judgement.
  (4) `current_affairs` must not be a stand-in for MISSING evidence. codebook/E3.md §4 is explicit:
      "Do NOT tag `current_affairs` merely because no evidence was found. Missing evidence is a
      pipeline gap; `current_affairs` is a claim about the textbook." So `current_affairs` with
      zero evidence lines in the input is failed. This matters today more than it will later:
      Stage A has indexed 2 of 13 Biology chapters and zero Physics/Chemistry chapters, so D4
      structurally cannot cite supporting text for most real questions, and "no evidence" is the
      NORMAL state, not a signal about the textbook.

WHAT IS DELIBERATELY NOT A FAILURE HERE: `confidence: medium`. Spec 13/E3's "On failure" line
makes medium confidence a FLAG -- E3_MEDIUM (low) -- raised by the plugin, never a check failure.
codebook/E3.md §4 tells the agent to use medium whenever no evidence was available, which is most
real questions right now, so failing it would retry every honest tag in the bank and then blame
the agent for the pipeline's own gap. `confidence: low` is likewise not failed: E3 has one run,
spec names no low-confidence rule for it, and a low-confidence honest tag is more useful than a
retried confident guess. Both are reported in the PASSING message instead, so the plugin can raise
E3_MEDIUM from the check result without a second pass over the data.

Also deliberately not checked: whether the shape is the RIGHT one, and the "practical_procedure
normally co-occurs with syllabus_status lab_manual" relationship -- codebook/E3.md §3 calls that
one "normally", and the real Laboratory Manual books are not in inputs/ at all (confirmed missing
twice), so a question that genuinely is practical_procedure has no lab-manual evidence to co-occur
with. Failing on it would punish a correct tag for a missing source.

Convention: def check(data, context) -> (bool, str), ';'-joined segments.
"""
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import records as lib_records  # noqa: E402

#: `why` must be at least a short real sentence. Spec gives no number; this is the floor below
#: which a sentence cannot name an evidence line at all ("Evidence is the ordered stages of
#: mitosis" is 7 words; "tests recall" is 2).
MIN_WHY_WORDS = 4

#: Spec 17.4 / codebook/E3.md §3: current_affairs is a fact in NO edition, hence always outside
#: NCERT. These syllabus_status values therefore contradict it outright.
_IN_NCERT_STATUSES = ("latest_ncert", "deleted_content", "lab_manual")


def question_record(context):
    """The real question record. Prefers context["input_data"]["record"]; falls back to
    papers/records/<QID>.json so this check is testable against real data before the E plugins
    exist. {} when neither is available -- rules needing it degrade to a reported skip."""
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
        return False, "E3 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    shape = data.get("content_shape")
    why = (data.get("why") or "").strip()
    new_description = (data.get("new_description") or "").strip()
    confidence = data.get("confidence")
    input_data = context.get("input_data") or {}
    segments = []

    if shape == "new_shape" and not new_description:
        segments.append(
            "E_NEW_CATEGORY: content_shape is new_shape but new_description is empty; the "
            "description is the whole content of the E_NEW_CATEGORY flag Stage F reviews")

    # (2) `why` substance.
    words = why.split()
    if len(words) < MIN_WHY_WORDS:
        segments.append(
            f"why is {len(words)} word(s) ({why!r}); it must name the evidence the shape was read "
            f"from, in a sentence a reviewer can check in seconds")
    elif why.strip().strip(".").lower() == str(shape).replace("_", " ").lower():
        segments.append(
            f"why just restates the tag ({why!r}); it must name the NCERT evidence behind it")

    # (3) and (4) current_affairs.
    if shape == "current_affairs":
        record = question_record(context)
        status = record.get("syllabus_status")
        if status in _IN_NCERT_STATUSES:
            segments.append(
                f"content_shape is current_affairs (a time-bound fact in NO edition, so always "
                f"outside NCERT) but D6 recorded syllabus_status {status!r}; one of the two is "
                f"wrong (codebook/E3.md §3)")
        evidence = input_data.get("evidence")
        if isinstance(evidence, list) and not evidence:
            segments.append(
                "content_shape is current_affairs but the input carried no evidence lines at all; "
                "missing evidence is a pipeline gap, not a claim about the textbook "
                "(codebook/E3.md §4) -- Stage A has indexed 2 of 13 Biology chapters and zero "
                "Physics/Chemistry chapters, so no evidence is the normal state today")

    if segments:
        return False, "; ".join(segments)

    # Not failures -- reported so the plugin can raise E3_MEDIUM (low) straight from this message.
    if confidence == "medium":
        return True, "ok (medium confidence -> E3_MEDIUM)"
    if confidence == "low":
        return True, "ok (low confidence; E3 has one run and spec names no low-confidence rule)"
    return True, "ok"
