"""Step-specific check for E2 (spec Section 13/E2 + codebook/E2.md §2) -- including THE
NEGATIVE-WORD GUARD, the one check in Stage E that can force an adjudication.

schemas/E2.json already constrains `format` to config/allowed_values.yaml v0.2's 26 values. This
file is mostly one thing: spec 13/E2's guard, verbatim ---

    "if B3's `negative_words_seen` is non-empty (NOT, EXCEPT, INCORRECT, FALSE, WRONG, MISMATCH)
     and the options are single items or statements, the format must be `pick_incorrect` or
     `odd_one_out`; if the options are combinations or match codes, the format stays
     `pick_correct_combination` / `pick_match_code` and the negative is recorded in E6. If the
     stem has no negative word, the format must not be `pick_incorrect`."

and spec 13/E2's "On failure: guard fails -> retry with 'The stem contains <word>'; then
adjudicator -> E2_NEGATIVE_GUARD (high)."

HOW THE THREE RULES ARE IMPLEMENTED, AND THE ONE ASYMMETRY THAT MATTERS

The guard reads the negative words two different ways on purpose, because the two directions fail
in opposite ways and a known real defect sits between them:

  * `b3-question-reader.md`'s own allowed set lists only FIVE negative words -- it omits
    **MISMATCH** -- while this guard checks six (a real 5-vs-6 discrepancy already logged in
    docs/OPEN_QUESTIONS.md, 2026-10-11). So a real "mismatched"/"wrongly matched" question can
    arrive with an EMPTY `negative_words_seen`, and codebook/E2.md §2 tells the agent to read the
    stem itself and tag by the stem in that case.

  * **Rule 1 and 2 (a negative is present) therefore trigger on B3's FIELD only** -- spec's own
    literal wording. Using the stem here would make the guard fire on an incidental "does not"
    buried in an option-statement, and a false guard failure costs a retry, an adjudication and a
    `high` flag on a correctly-tagged question.

  * **Rule 3 (no negative is present) uses the FIELD OR THE STEM.** If it used the field alone, an
    agent that correctly followed codebook/E2.md §2 -- saw "wrongly matched" in a real stem,
    tagged `pick_incorrect`, with B3's field empty because of the MISMATCH gap -- would be failed
    for doing the right thing. Reading the stem as well makes rule 3 permissive in exactly the
    case the known defect creates, and no more.

"The options are combinations or match codes" is decided by reusing `describe_tags.answer_form()`
-- E6's real, already-tested option-shape classifier, whose three real distinctions were each
found by a real mis-tag (a LaTeX fraction is an expression not a ratio; a LaTeX-encoded unit is
number_with_unit not expression; one arrow is a reaction, two are an ordering). Writing a third
copy of option-shape detection here would guarantee the two drift. `combination_code` and
`match_code` are the exempt family; EVERY other answer_form is in the constrained family,
including `order` and the two image forms -- "which order is NOT correct" and "which graph is NOT"
are both legitimately `pick_incorrect`, so putting them in the constrained family is right.

THE RETRY MESSAGE IS CARRIED IN THE SEGMENT. Each `E2_NEGATIVE_GUARD` segment's detail begins with
the literal sentence spec 13/E2 names -- "The stem contains <word>." -- so the plugin can forward
the segment detail to the retry unchanged instead of reconstructing it and risking a different
wording. See config/_pending_E_entries.yaml.

Also checked (not part of the guard):
  * `new_format` REQUIRES a non-empty `new_description` (that string is E_NEW_CATEGORY's content).
  * `confidence: low`: E2 is one run, so a low-confidence tag has nothing downstream to catch it.
  * a code-shaped format (`pick_match_code`, `pick_correct_combination`) against unambiguously
    non-code options (a number, a ratio, an expression). Deliberately narrow: the ambiguous
    term/statement cases are left alone, because a false failure here costs an adjudication.

What is DELIBERATELY NOT checked: which of two near formats is right. Every boundary spec 13/E2
names (2013#50 calculate_value not count_correct; 2016-P1#121 odd_one_out not pick_incorrect;
2013#22 calculate_value not pick_proportionality; 2017#111 name_or_identify not
pick_scientist_or_date) is a judgement about meaning, not shape -- those live in codebook/E2.md §3
where the agent reads them. A script asserting them would be guessing.

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

#: Spec 13/E2's own six. B3's prompt lists only five (MISMATCH missing) -- see module docstring.
NEGATIVE_WORDS = ("NOT", "EXCEPT", "INCORRECT", "FALSE", "WRONG", "MISMATCH")

#: The only format allowed when a negative word meets single-item/statement options.
#:
#: WAS ("pick_incorrect", "odd_one_out"). v1 merged both into `pick_correct_statement`, which grades
#: every option and picks one -- the correct one, or the incorrect one when the stem is negated. So
#: the FORMAT no longer encodes negation, and this check can no longer infer from the format that
#: the stem must contain a negative word. The negation moved to `task_polarity` (rulebook section 6),
#: which is derived in scripts/build_category_sheet_v2.py and is not an E2 agent output.
#:
#: What survives is the useful half, and it is the half that caught real errors: a negated stem over
#: single-item options must be `pick_correct_statement` and NOT a letter-code format. What is gone is
#: the converse -- "this format implies a negative word somewhere" -- and `_NEGATION_MOVED` below
#: says so out loud rather than letting a weakened check look like the original.
NEGATIVE_FORMATS = ("pick_correct_statement",)

#: Reported, not enforced: E2 cannot check this any more and should not pretend to.
_NEGATION_MOVED = (
    "note: E2 can no longer verify that a negated stem is reflected in the FORMAT, because "
    "pick_correct/pick_incorrect merged into pick_correct_statement in allowed_values v0.3. The "
    "negation is recorded in `task_polarity`; whether it matches the stem is checked there.")

#: The answer_form family that keeps its format and records the negative in E6 instead.
CODE_ANSWER_FORMS = ("combination_code", "match_code")

#: answer_form -> the format a code-shaped answer must carry.
CODE_FORMAT_FOR = {"combination_code": "pick_correct_combination", "match_code": "pick_match_code"}

#: answer_forms that are unambiguously NOT a letter code, used only by the narrow extra check.
NON_CODE_ANSWER_FORMS = ("number_with_unit", "ratio", "expression")


def question_record(context):
    """The real question record. Prefers context["input_data"]["record"]; falls back to
    papers/records/<QID>.json so this check is testable against real data before the E plugins
    exist. {} when neither is available -- every rule then degrades to a reported skip."""
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


def field_negatives(record):
    """The DISTINCT negative words B3 actually recorded, upper-cased. B3 writes the field as
    `negative_words`; spec 13/E2 calls it `negative_words_seen`; both names are read, the same
    way scripts/describe_tags.py already does."""
    seen = record.get("negative_words")
    if seen is None:
        seen = record.get("negative_words_seen")
    if not seen:
        return set()
    return {str(w).strip().upper() for w in seen if str(w).strip()}


def stem_negatives(record):
    """Negative words visible in the stem and its lettered statements, read directly. Used ONLY
    to make rule 3 permissive where B3's missing MISMATCH would otherwise fail a correct tag."""
    parts = [record.get("stem_en") or ""]
    for s in record.get("statements") or []:
        parts.append(f"{s.get('label', '')} {s.get('text', '')}" if isinstance(s, dict) else str(s))
    text = "\n".join(parts).upper()
    return {w for w in NEGATIVE_WORDS if re.search(rf"\b{w}\b", text)}


def check(data, context):
    if not isinstance(data, dict):
        return False, "E2 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    fmt = data.get("format")
    new_description = (data.get("new_description") or "").strip()
    segments, notes = [], []

    if fmt == "new_format" and not new_description:
        segments.append(
            "E_NEW_CATEGORY: format is new_format but new_description is empty; the description "
            "is the whole content of the E_NEW_CATEGORY flag Stage F reviews")

    if data.get("confidence") == "low" and fmt != "new_format":
        segments.append(
            f"confidence is low on format {fmt!r}; E2 has one run and no adjudicator of its own, "
            f"so use new_format with a description if no listed value really fits")

    record = question_record(context)
    if not record:
        segments.append(
            "E2_NEGATIVE_GUARD: no question record available (neither "
            "context['input_data']['record'] nor papers/records/<QID>.json), so the negative-word "
            "guard could not run at all -- it must never be skipped silently")
        return False, "; ".join(segments)

    from_field = field_negatives(record)
    from_stem = stem_negatives(record)
    form = describe_tags.answer_form(record)
    options_are_codes = form in CODE_ANSWER_FORMS

    if from_field:
        # The retry wording spec 13/E2 names, verbatim, at the head of the detail.
        word = sorted(from_field)[0]
        contains = f"The stem contains {word}."

        if not options_are_codes:
            # Rule 1: negative + single items/statements -> pick_correct_statement.
            if fmt not in NEGATIVE_FORMATS:
                segments.append(
                    f"E2_NEGATIVE_GUARD: {contains} The options are single items or statements "
                    f"(answer_form {form!r}), so the format must be "
                    f"{' or '.join(NEGATIVE_FORMATS)}, not {fmt!r} -- each option is a whole claim "
                    f"to be graded. Record the negation itself in `task_polarity`, not in the "
                    f"format.")
        else:
            # Rule 2: negative + combination/match-code options -> the format STAYS, and the
            # negative is recorded in E6's `negation` instead of in the format.
            expected = CODE_FORMAT_FOR[form]
            if fmt in NEGATIVE_FORMATS:
                segments.append(
                    f"E2_NEGATIVE_GUARD: {contains} But the options are {form}, so the format "
                    f"stays {expected!r} and the negative belongs in E6's `negation` field, not "
                    f"in the format; {fmt!r} is wrong here")
            elif fmt != expected:
                segments.append(
                    f"E2_NEGATIVE_GUARD: {contains} The options are {form}, so spec 13/E2 says "
                    f"the format stays {expected!r} (the negative is recorded in E6); the agent "
                    f"answered {fmt!r}")
    else:
        # Rule 3: no negative word at all -> the format must not be pick_incorrect. Deliberately
        # reads the stem too, so a real MISMATCH question B3 could not record is not failed.
        # `from_stem` being non-empty here means B3's field missed a negative the stem really
        # carries (the known MISMATCH gap), and codebook/E2.md §2 tells the agent to tag by the
        # stem in exactly that case -- so pick_incorrect is correct and must not be failed.
        # The former converse check lived here: "format is pick_incorrect but the stem carries no
        # negative word". It is GONE, not relaxed -- pick_correct_statement is correct for a
        # positive stem too, so the same condition now proves nothing. Deleting it rather than
        # loosening it keeps the check honest; `task_polarity` is where the negation is verified.
        if fmt in NEGATIVE_FORMATS and not from_stem:
            notes.append(_NEGATION_MOVED)

    # Narrow extra: a letter-code format against options that are plainly not letter codes.
    if fmt in CODE_FORMAT_FOR.values() and form in NON_CODE_ANSWER_FORMS:
        segments.append(
            f"format is {fmt!r} but the options are {form!r} -- not letter codes at all; a "
            f"combination/match-code format needs options that are codes")

    if segments:
        return False, "; ".join(segments)
    return True, ("ok" if not notes else "ok -- " + "; ".join(notes))
