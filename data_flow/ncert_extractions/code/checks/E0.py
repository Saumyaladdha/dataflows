"""Step-specific check for E0 (spec Section 13/E0) -- two agents, one schema, one check module.

E0 exists to give the OWNER data for writing codebooks. It does not create codebooks and it does
not change allowed values: spec 13/E0's "Never: write codebook/E*.md. Those are the owner's."
scripts/e0_category_sheet.py enforces that by construction (it can write exactly one path), and
tests/test_e_checks.py asserts the refusal.

schemas/E0.json carries two agent branches with disjoint required keys, so this check tells the
two workers apart from the output's own keys.

=== e0-open-look (E0.1, one question, free words, NO categories shown) ===

  (1) THE FREE TEXT MUST CONTAIN NO CATEGORY NAMES. This is the single rule that makes E0 worth
      running. Spec 13/E0: the agent completes "To get this right, the student must ___" "with no
      categories shown"; the agent file's own Never is "Never mention or invent category names".
      A tagger that has been shown the list stops discovering and starts matching, and the
      grouping in E0.2 then just reproduces the list it was fed -- which would read to the owner
      as confirmation. So every value in config/allowed_values.yaml's five discovery lists
      (question_type, format, content_shape, thinking, trap) is searched for in all five free-text
      fields, as words rather than substrings.

      The search deliberately skips values whose name is ordinary English that cannot be avoided
      when describing a question plainly -- `list`, `process`, `comparison`, `exception`, `trend`,
      `graph`, `table`, `diagram`, `formula`, `recall` and the like. Flagging those would make the
      check fire on correct free text ("follow the process in the right order" is a description,
      not a category name), and a check that cries wolf gets switched off. The values that matter
      are the compound coinages -- `pick_correct_combination`, `look_alike_term`, `elimination`,
      `assertion_reason`, `number_near_miss` -- which no one writes by accident.

  (2) `wrong_options` IS KEYED BY WRONG OPTION, AND THE ANSWER IS NOT AMONG THEM. Same granularity
      rule as E5: there is no trap on the correct option. Checked against the answer the runner
      supplied in context["input_data"]["answer"], else the record's own answer.

=== e0-category-grouper (E0.2, one tag, groups the free answers) ===

  (3) EVERY ANSWER GOES INTO EXACTLY ONE GROUP, OR `unclear`. The agent file's own rule. Checked
      by reconciling the per-subject counts plus `unclear` against the answers the runner actually
      supplied -- a silently dropped answer is the failure mode that would quietly shrink a real
      category's count, and counts are the entire output of this step.
  (4) `decision` AGREES WITH THE STARTING LIST, BOTH WAYS. keep/merge/drop are only meaningful for
      a category that IS on the starting list; `new` only for one that is not. A `new` name that
      is really an existing allowed value would read to the owner as a discovery.
  (5) `subjects` AGREES WITH WHICH COUNTS ARE NON-ZERO.
  (6) `examples` ARE REAL QUESTION IDS FROM THIS TAG'S ANSWERS, and a category with a non-zero
      count must give at least one. A category legitimately kept with count 0 ("keep with count 0
      if rare by nature; say why") gives none, which is why the schema sets no minItems.
  (7) `unclear` IDS ARE REAL AND NOT ALSO IN A GROUP'S EXAMPLES.

=== SAMPLE SIZE -- stated here, not discovered later ===

Spec 13/E0 asks for ~300 questions from the most recent papers, ~100 per subject, across many
chapters. The bank holds TEN canonical questions, all from one paper (2023 MAIN, booklet E1/E2),
split 6 Physics / 2 Chemistry / 1 Biology / 1 un-subjected. E0 therefore cannot meaningfully run
yet: a category list grouped from 10 answers would hand the owner counts of 1 and 2 and invite
decisions that ~500 real sampled questions already contradict. The check does not police sample
size -- that is the runner's list phase, and spec 16 gives E0 exactly one flag
(E0_FINDINGS_READY, normal), so inventing a sample-size flag here would be inventing a flag.
scripts/e0_category_sheet.py refuses to write a sheet from a sample below its documented floor
unless explicitly overridden, and says why.

Convention: def check(data, context) -> (bool, str), ';'-joined segments.
"""
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import tag_values  # noqa: E402
from lib import records as lib_records  # noqa: E402

#: The five tags spec 13/E0 groups, and the config/allowed_values.yaml list each one draws on.
DISCOVERY_TAGS = {
    "question_type": "question_type",
    "format": "format",
    "content_shape": "content_shape",
    "thinking": "thinking",
    "trap": "trap",
}

SUBJECTS = ("Physics", "Chemistry", "Biology")

#: Category names that are also ordinary English a person must be free to use when describing a
#: question plainly. Searching for these would fail correct free text, so they are exempt from the
#: leak scan -- see the module docstring, rule (1). Everything NOT in here is a coinage.
_ORDINARY_ENGLISH_VALUES = frozenset({
    "list", "table", "graph", "diagram", "formula", "process", "comparison", "exception",
    "trend", "recall", "application", "confusion", "reasoning", "numerical", "definition_term",
    "one_line", "cycle_or_pathway", "life_cycle", "value_or_data", "half_true", "wrong_order",
    "extreme_word", "new_type", "new_format", "new_shape", "new_trap",
    # v0.3 names that are likewise ordinary English. Omitting one would fail correct free text
    # that happens to use the word; including a coinage would hide a real leak, so only words a
    # person would plainly write about a question belong here.
    "calculation", "reaction", "new_demand",
})

_OPEN_LOOK_TEXT_FIELDS = ("student_must", "built_as", "asks_to_pick", "ncert_material")


def _coined_values():
    """Every discovery-list value that is a coinage rather than ordinary English, as a lookup of
    {search phrase: (list name, value)}. Each value is searched both as written (`look_alike_term`)
    and with underscores as spaces (`look alike term`), because free text would spell it that way.
    """
    out = {}
    for list_name in DISCOVERY_TAGS.values():
        for value in tag_values.values(list_name):
            if value in _ORDINARY_ENGLISH_VALUES:
                continue
            out[value.lower()] = (list_name, value)
            spaced = value.replace("_", " ").lower()
            if spaced != value.lower():
                out[spaced] = (list_name, value)
    return out


def question_record(context):
    """The real question record, for the open-look branch's answer check."""
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


def _answer_number(context):
    """The correct option number, as a string, or None. The runner's own value wins."""
    input_data = context.get("input_data") or {}
    for key in ("answer", "answer_taught", "latest_answer"):
        value = input_data.get(key)
        if isinstance(value, dict):
            value = value.get("number")
        if value is not None and str(value).strip() and str(value).strip() != "unsure":
            return str(value).strip()
    record = question_record(context)
    for field in ("latest_answer", "corrected_answer", "official_answer"):
        value = record.get(field)
        if value is not None and str(value).strip() and str(value).strip() != "unsure":
            return str(value).strip()
    return None


def _check_open_look(data, context):
    segments = []
    coined = _coined_values()

    texts = {f: str(data.get(f) or "") for f in _OPEN_LOOK_TEXT_FIELDS}
    for number, phrase in (data.get("wrong_options") or {}).items():
        texts[f"wrong_options[{number}]"] = str(phrase or "")

    for field, text in texts.items():
        low = text.lower()
        for phrase, (list_name, value) in coined.items():
            if re.search(rf"(?<![a-z0-9_]){re.escape(phrase)}(?![a-z0-9_])", low):
                segments.append(
                    f"{field} names the category {value!r} from the {list_name} list; E0.1 is run "
                    f"with NO categories shown precisely so the free answers are a discovery and "
                    f"not a re-statement of the existing list -- describe the action in plain "
                    f"words instead")
                break  # one report per field is enough to send it back

    wrong_options = data.get("wrong_options") or {}
    answer = _answer_number(context)
    if answer is None:
        segments.append(
            "no correct answer available (neither the input's own `answer` nor the record's "
            "latest/corrected/official answer), so 'the answer is not one of the wrong options' "
            "could not be checked")
    elif answer in {str(k) for k in wrong_options}:
        segments.append(
            f"wrong_options has an entry for option {answer!r}, which is the correct answer; "
            f"there is no reason a student would wrongly pick the right option")

    return segments


def _check_grouper(data, context):
    segments = []
    tag = data.get("tag")
    categories = data.get("categories") or []
    unclear = data.get("unclear") or []
    input_data = context.get("input_data") or {}

    starting_list = input_data.get("starting_list")
    if starting_list is None and tag in DISCOVERY_TAGS:
        # The runner is meant to pass it; fall back to the real list so the check still has teeth.
        starting_list = tag_values.values(DISCOVERY_TAGS[tag])
    if isinstance(starting_list, dict):
        starting_list = list(starting_list.keys())
    starting = {str(n) for n in (starting_list or [])}

    answers = input_data.get("answers")
    answer_ids = []
    if isinstance(answers, list):
        for a in answers:
            if isinstance(a, dict) and a.get("question_id"):
                answer_ids.append(str(a["question_id"]))
            elif isinstance(a, str):
                answer_ids.append(a)
    answer_id_set = set(answer_ids)

    total_counted = 0
    for i, cat in enumerate(categories):
        if not isinstance(cat, dict):
            segments.append(f"categories[{i}] is not an object")
            continue
        name = str(cat.get("name") or "")
        decision = cat.get("decision")
        counts = cat.get("count") or {}
        subjects = cat.get("subjects") or []
        examples = cat.get("examples") or []
        total = sum(int(counts.get(s) or 0) for s in SUBJECTS)
        total_counted += total

        # (4) decision vs the starting list, both ways.
        if starting:
            if decision == "new" and name in starting:
                segments.append(
                    f"categories[{i}] {name!r} is marked `new` but it is already on the starting "
                    f"list; a `new` row reads to the owner as a discovery, so use keep/merge/drop")
            elif decision in ("keep", "merge", "drop") and name not in starting:
                segments.append(
                    f"categories[{i}] {name!r} is marked {decision!r}, which only applies to a "
                    f"category that is ON the starting list; it is not -- use `new`")

        # (5) subjects vs non-zero counts.
        non_zero = [s for s in SUBJECTS if int(counts.get(s) or 0) > 0]
        if sorted(str(s) for s in subjects) != sorted(non_zero):
            segments.append(
                f"categories[{i}] {name!r} lists subjects {sorted(str(s) for s in subjects)} but "
                f"its non-zero counts are {non_zero}")

        # (6) examples real, and present when the count is non-zero.
        if total > 0 and not examples:
            segments.append(
                f"categories[{i}] {name!r} has {total} answer(s) but gives no example question "
                f"id; spec 13/E0 asks for 2 so the owner can check the grouping")
        if answer_id_set:
            unknown = [e for e in examples if str(e) not in answer_id_set]
            if unknown:
                segments.append(
                    f"categories[{i}] {name!r} gives example(s) {unknown} that are not among this "
                    f"tag's answers")

    # (3) reconcile the totals -- nothing silently dropped.
    if answer_ids:
        if total_counted + len(unclear) != len(answer_ids):
            segments.append(
                f"the per-subject counts total {total_counted} and `unclear` holds "
                f"{len(unclear)}, which is {total_counted + len(unclear)} of "
                f"{len(answer_ids)} answers given; every answer must go into exactly one group or "
                f"into `unclear`")
        # (7) unclear ids real.
        unknown_unclear = [u for u in unclear if str(u) not in answer_id_set]
        if unknown_unclear:
            segments.append(
                f"`unclear` names {unknown_unclear}, which are not among this tag's answers")
    else:
        segments.append(
            "the input carried no `answers` list, so 'every answer goes into exactly one group' "
            "could not be reconciled -- the counts are this step's entire output, so they must "
            "never be accepted unreconciled")

    return segments


def check(data, context):
    if not isinstance(data, dict):
        return False, "E0 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    if "student_must" in data:
        segments = _check_open_look(data, context)
    elif "categories" in data:
        segments = _check_grouper(data, context)
    else:
        return False, ("E0 output matches neither worker's shape: e0-open-look writes "
                        "`student_must`, e0-category-grouper writes `categories`")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
