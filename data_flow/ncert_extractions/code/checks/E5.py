"""Step-specific check for E5 (spec Section 13/E5 + codebook/E5.md).

E5'S ITEM IS ONE WRONG OPTION OF ONE QUESTION -- three per question in the normal case, each
tagged by two runs plus an adjudicator on disagreement. Every rule below is about THAT one option.
schemas/E5.json constrains `option` to a single '1'-'4' and `trap` to config/allowed_values.yaml
v0.2's 20 values; this file adds the rules a schema cannot express:

  (1) `option` IS THE OPTION THIS ITEM IS FOR. The runner addresses one wrong option per item
      (proposed item id `<QID>#opt<N>`, config/_pending_E_entries.yaml), and an output that tags a
      different option silently attributes a trap to the wrong distractor. Checked against
      context["input_data"]["wrong_option"]["number"] when the plugin supplies it, else against
      the item id's own suffix.

  (2) `option` IS NOT THE CORRECT ANSWER. "Never tag the correct option. There is no trap on the
      answer" (codebook/E5.md §1). The answer to judge against is the one students are taught --
      spec 12's rule, in this order: D7's `latest_answer`, then B8's `corrected_answer`, then
      `official_answer`. This is the single most consequential check in E5: a trap tagged on the
      right answer is not a small error, it is feedback that teaches the wrong thing.

  (3) `old_ncert_fact` HAS A HARD PRECONDITION. codebook/E5.md §4: tag it "only when a change-log
      entry on an evidence passage shows this option was right by the older book", and never from
      an option "sounding dated". The agent is given those entries precisely so this can be
      checked. `ncert/change_log.csv` holds ONLY ITS HEADER ROW today -- A9 has never written a
      real entry, because A6-A9 have only run against two Biology chapters -- so this trap is
      effectively untaggable right now and "should essentially never appear. If an agent produces
      it anyway, that is a signal the agent guessed -- the check should treat it as such."
      This check treats it as such.

  (4) `calculation_slip` MUST NAME THE SLIP. The agent prompt requires it and codebook/E5.md §3
      says "an unnamed slip is not a tag, it is a shrug". Mechanically: `why` must contain
      arithmetic substance -- a number, or an explicit named operation (squared, inverted,
      doubled, factor, power, ...). "Forgot to square the length ratio: 4 x 2 = 8" passes;
      "arithmetic error" does not.

  (5) `partial_combination` NEEDS COMBINATION OPTIONS. The value means "the combination names only
      a SUBSET of the correct set" (codebook/E5.md §3), which is meaningless when the options are
      not combinations at all. Decided with E6's real, already-tested `describe_tags.answer_form()`
      rather than a second copy of option-shape detection.

  (6) `new_trap` REQUIRES a non-empty `new_description` (that string is E_NEW_CATEGORY's content).

WHAT IS DELIBERATELY NOT CHECKED. Which trap is the RIGHT trap. codebook/E5.md §5 expects genuine
disagreement to cluster on exactly three boundaries -- calculation_slip/number_near_miss,
wrong_pairing/swapped_positions, opposite_answer/sign_or_direction -- and routing those to the
adjudicator (E5_ADJUDICATED, normal) is the designed mechanism. A script preferring one side would
pre-empt it. Also not checked: codebook/E5.md §3's `partial_combination` DECISION RULE (whether an
option that both omits a true item and includes a false one gets the false item's trap). That rule
is the codebook author's own reading, explicitly flagged as the owner's call in §6.1, and it
affects the largest number of real tags of anything in that file -- a script must not harden it
before the owner has ruled.

Convention: def check(data, context) -> (bool, str), ';'-joined segments.
"""
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import describe_tags  # noqa: E402
from lib import records as lib_records  # noqa: E402

#: Arithmetic substance for a `calculation_slip`'s `why` -- a digit, or a named operation.
_SLIP_NAMED = re.compile(
    r"\d|\bsquar|\bcube|\broot\b|\binvert|\breciprocal\b|\bdoubl|\bhalv|\bfactor\b|\bpower\b|"
    r"\bexponent\b|\bsign\b|\bconvert|\bmultipl|\bdivid|\bsubtract|\badd(?:ed|s|ition)?\b",
    re.IGNORECASE)

#: `partial_combination` only means anything when the options really are combinations/match codes.
_COMBINATION_FORMS = ("combination_code", "match_code")


def question_record(context):
    """The real question record. Prefers context["input_data"]["record"]; falls back to
    papers/records/<QID>.json (the item id's part before '#') so this check is testable against
    real data before the E plugins exist. {} when neither is available."""
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


def expected_option(context):
    """The option number this item is for, or None.

    Prefers the plugin's own context["input_data"]["wrong_option"]["number"]; falls back to the
    item id's suffix, accepting `Q-000015#opt2` and `Q-000015#2` so the check does not depend on
    which spelling the plugin ends up using (the proposal is `#opt<N>`)."""
    wrong_option = (context.get("input_data") or {}).get("wrong_option") or {}
    number = wrong_option.get("number")
    if number is not None and str(number).strip():
        return str(number).strip()
    item_id = str(context.get("item_id") or "")
    if "#" in item_id:
        m = re.search(r"(?:opt)?([1-4])\s*$", item_id.split("#", 1)[1])
        if m:
            return m.group(1)
    return None


#: The answer students are taught, in spec 12's own order (the same order
#: step_plugins._d_answer_taught uses): D7's latest_answer when D7 set a real one, else B8's
#: corrected_answer, else the official key. "unsure" is D7's no-verdict value, not an answer.
_ANSWER_FIELDS = ("latest_answer", "corrected_answer", "official_answer")


def answer_taught(record):
    """(set of accepted option numbers, which field they came from), or (None, None).

    A SET, not a single string, because a `multiple_accepted` question has more than one correct
    option and `B5Plugin` records them comma-joined (e.g. "1,3"). The earlier version returned
    the raw value, so the comparison below -- `option == answer` with `option` a single digit --
    could never be true for exactly those questions, silently disabling E5's most consequential
    rule ("never tag the correct option") on the only questions that have two correct options.
    `scripts/checks/B6.py` already splits on "," for the same field; this matches it rather than
    inventing a second convention."""
    for field in _ANSWER_FIELDS:
        value = record.get(field)
        if value is None:
            continue
        accepted = {a.strip() for a in str(value).split(",") if a.strip() and a.strip() != "unsure"}
        if accepted:
            return accepted, field
    return None, None


def check(data, context):
    if not isinstance(data, dict):
        return False, "E5 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    option = str(data.get("option") or "").strip()
    trap = data.get("trap")
    why = (data.get("why") or "").strip()
    new_description = (data.get("new_description") or "").strip()
    input_data = context.get("input_data") or {}
    segments = []

    if trap == "new_trap" and not new_description:
        segments.append(
            "E_NEW_CATEGORY: trap is new_trap but new_description is empty; the description is "
            "the whole content of the E_NEW_CATEGORY flag Stage F reviews")

    # (1) the option this item is actually for.
    wanted = expected_option(context)
    if wanted is None:
        segments.append(
            "cannot tell which wrong option this item is for: the input carried no "
            "wrong_option.number and the item id has no option suffix -- E5's item is ONE wrong "
            "option, so an unaddressed output cannot be stored against the right distractor")
    elif option != wanted:
        segments.append(
            f"option is {option!r} but this item is for option {wanted!r}; E5 tags exactly the "
            f"one wrong option the runner gave it -- tagging another silently attributes this "
            f"trap to the wrong distractor")

    record = question_record(context)

    # (2) never the correct option.
    if record:
        answer, source = answer_taught(record)
        if answer and option and option in answer:
            shown = ",".join(sorted(answer))
            segments.append(
                f"option {option!r} IS an answer students are taught ({source} = {shown!r}); "
                f"there is no trap on a correct option and E5 must never tag it")
        elif not answer:
            segments.append(
                f"the record has no answer at all (no latest_answer / corrected_answer / "
                f"official_answer), so 'never tag the correct option' cannot be verified; a "
                f"question with no answer has no identifiable wrong options either "
                f"(official_status {record.get('status')!r})")
    else:
        segments.append(
            "no question record available (neither context['input_data']['record'] nor "
            "papers/records/<QID>.json), so 'never tag the correct option' could not be checked "
            "-- the one rule in E5 that must never be skipped silently")

    # (3) old_ncert_fact needs a real change-log entry.
    if trap == "old_ncert_fact":
        entries = input_data.get("change_log_entries")
        if not entries:
            segments.append(
                "trap is old_ncert_fact but the input carried no change-log entry on any evidence "
                "passage; the value is only taggable when an entry shows this option was right by "
                "the OLDER book, never from an option sounding dated (codebook/E5.md §4). "
                "ncert/change_log.csv holds only its header row today, so this trap should "
                "essentially never appear yet")

    # (4) calculation_slip must name the slip.
    if trap == "calculation_slip" and not _SLIP_NAMED.search(why):
        segments.append(
            f"trap is calculation_slip but `why` names no actual slip ({why!r}); say which wrong "
            f"operation produces this option -- a number or a named operation (squared, inverted, "
            f"dropped factor of 2, wrong power). An unnamed slip is not a tag")

    # (5) partial_combination needs combination options.
    if trap == "partial_combination" and record:
        form = describe_tags.answer_form(record)
        if form not in _COMBINATION_FORMS:
            segments.append(
                f"trap is partial_combination but the options are {form!r}, not combinations or "
                f"match codes; the value means the combination names only a SUBSET of the correct "
                f"set, which says nothing about a non-combination option")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
