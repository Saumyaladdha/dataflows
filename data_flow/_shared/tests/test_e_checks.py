#!/usr/bin/env python3
"""Unit tests for Stage E: the seven schemas, the seven check modules, and the E-stage scripts.

    .venv/bin/python3 -m pytest tests/test_e_checks.py -q

HOW THESE TESTS ARE GROUNDED, honestly labelled, because it is the thing most worth knowing about
them. Stage E cannot run end to end -- the runner plugins do not exist yet (deliberately; they are
someone else's task). So nothing here is an end-to-end verification. What each test IS:

  * REAL-DATA tests read the 10 real canonical records in `papers/records/` and the real
    `config/allowed_values.yaml` / `codebook/E*.md` files on disk, and assert against the real
    outputs of `scripts/type_patterns.py` and `scripts/describe_tags.py`. These are marked
    `# REAL DATA` and are the ones that would catch a wrong rule.
  * FIXTURE-ONLY tests use hand-built records under `tests/fixtures/stage_e/`, which exist only
    for the three cases the real bank cannot produce (see that directory's README). They are
    marked `# FIXTURE-ONLY` and prove the rule is implemented, not that it is right on real data.
  * The AGENT OUTPUTS in every test are invented: no E agent has ever been dispatched in this
    project, so there is no real E output to test against. A check rejecting an invented bad
    output proves the check has teeth; it does not prove a real agent would produce that output.

NOTHING HERE WRITES INTO A REAL PIPELINE PATH. Fixture data written into a real path was a real
mistake made once already (docs/OPEN_QUESTIONS.md 2026-10-10). The one test that writes a file at
all writes into pytest's own tmp_path, and there is an explicit test asserting that
scripts/e0_category_sheet.py REFUSES to write a codebook markdown file.
"""
import json
import os
import sys

import jsonschema
import pytest

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import codebook_version  # noqa: E402
import describe_tags  # noqa: E402
import e0_category_sheet  # noqa: E402
import legacy_match  # noqa: E402
import runner_core as rc  # noqa: E402
import tag_values  # noqa: E402
import type_patterns  # noqa: E402

E_STEPS = ("E0", "E1", "E2", "E3", "E4", "E5", "E6")
FIXTURES = os.path.join(_TESTS_DIR, "fixtures", "stage_e")


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _check(step, data, context):
    return rc.load_check_module(step).check(data, context)


def _real_record(qid):
    with open(rc.pp("papers", "records", f"{qid}.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def _fixture_record(name):
    with open(os.path.join(FIXTURES, name), "r", encoding="utf-8") as f:
        return json.load(f)


def _real_canonical_ids():
    out = []
    for fn in sorted(os.listdir(rc.pp("papers", "records"))):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _real_record(fn[:-len(".json")])
        if isinstance(rec, dict) and not rec.get("merged_into"):
            out.append(rec["question_id"])
    return out


def _failed(result, code=None):
    """True when check() failed, optionally with a specific flag code in the message."""
    ok, msg = result
    if ok:
        return False
    return code is None or code in msg


# ===========================================================================
# Schemas
# ===========================================================================

@pytest.mark.parametrize("step", E_STEPS)
def test_schema_is_valid_draft7(step):
    with open(rc.pp("schemas", f"{step}.json"), "r", encoding="utf-8") as f:
        jsonschema.Draft7Validator.check_schema(json.load(f))


def test_no_schema_enum_invents_an_allowed_value():
    """REAL DATA (config/allowed_values.yaml): every enum in every schemas/E*.json must be
    exactly its list in the owner's file, in both directions. This is the guard that makes it
    impossible for Stage E to quietly accept a value the owner never approved -- including the
    two real taxonomy gaps found on real data (`list_of_reactions`, a reaction `answer_form`),
    which are deliberately NOT patched in."""
    assert tag_values.audit_schemas() == []


def test_universal_error_branch_accepted_by_every_schema():
    """Universal rule 8: a broken input makes the agent write only {"error": "..."}."""
    for step in E_STEPS:
        ok, msg = rc.validate_schema(step, {"error": "input file missing"})
        assert ok, f"{step}: {msg}"


# ===========================================================================
# E1 -- question_type
# ===========================================================================

_E1_NEW_TYPE = {"question_type": "new_type",
                 "new_description": "the four options are each a chemical reaction",
                 "confidence": "high"}


def test_e1_new_type_needs_a_description():
    data = dict(_E1_NEW_TYPE, new_description="")
    assert _failed(_check("E1", data, {"item_id": "Q-000005"}), "E_NEW_CATEGORY")


def test_e1_agent_must_not_answer_a_question_the_script_decided():
    """REAL DATA: 9 of the 10 real canonical questions are decided by scripts/type_patterns.py,
    so an E1 agent output for any of them means the item should never have been dispatched."""
    decided = []
    for qid in _real_canonical_ids():
        value, _rule = type_patterns.classify(_real_record(qid))
        if value is None:
            continue
        decided.append(qid)
        data = {"question_type": value, "new_description": "", "confidence": "high"}
        ok, msg = _check("E1", data, {"item_id": qid})
        assert not ok and "already decides" in msg, f"{qid} should have been rejected: {msg}"
    # Deliberately NOT asserting a fixed count. This said `== 9`, a snapshot of the bank when it
    # held 10 questions, and broke the moment extraction grew it to 236 -- encoding live data as an
    # assertion. The invariant that actually matters is above: EVERY script-decided question must
    # be rejected when an agent answers it anyway. The count only needs to be non-trivial.
    assert len(decided) >= 5, f"too few script-decided questions to be a real test: {len(decided)}"


def test_e1_real_q5_is_the_one_question_the_agent_legitimately_gets():
    """REAL DATA: Q-000005's four options are each a chemical reaction -- a shape no spec 13/E1
    pattern covers (the confirmed gap, codebook/E1.md §4). `new_type` is what codebook/E1.md §4
    says to answer until the owner rules on `list_of_reactions`."""
    assert type_patterns.classify(_real_record("Q-000005"))[0] is None
    ok, msg = _check("E1", _E1_NEW_TYPE, {"item_id": "Q-000005"})
    assert ok, msg


def test_e1_real_q5_must_not_be_called_statement_options():
    """REAL DATA: the exact mis-tag already found and fixed on this real question -- four LaTeX
    reaction strings each read as a long 'statement'. A reaction equation is not a statement."""
    data = {"question_type": "statement_options", "new_description": "", "confidence": "high"}
    ok, msg = _check("E1", data, {"item_id": "Q-000005"})
    assert not ok and "not four statements to judge" in msg


def test_e1_near_value_on_the_gap_is_reported_not_absorbed():
    """REAL DATA: any value other than new_type on the options-are-reactions gap would hide the
    gap inside a near value, which is invisible in Stage F."""
    data = {"question_type": "single_statement", "new_description": "", "confidence": "high"}
    assert _failed(_check("E1", data, {"item_id": "Q-000005"}))


# ===========================================================================
# E2 -- the negative-word guard
# ===========================================================================

def _e2(fmt, confidence="high", new_description=""):
    return {"format": fmt, "new_description": new_description, "confidence": confidence}


def test_e2_guard_real_negative_with_single_item_options():
    """REAL DATA: Q-000005 carries negative_words ["NOT"] and its options are four reactions,
    which answer_form reads as `expression` -- the constrained family. Spec 13/E2's first guard
    row: the format must be the one that grades whole claims.

    UPDATED for allowed_values v0.3. The guard used to accept `pick_incorrect` or `odd_one_out`;
    v1 merged both (and `identify_reaction_or_process_name`) into `pick_correct_statement`, which
    grades every option and picks one -- the correct one, or the incorrect one when the stem is
    negated. So the surviving rule is: a negated stem over single-item options takes
    `pick_correct_statement` and NOT a letter-code format. The negation itself is recorded in
    `task_polarity` (rulebook section 6), not in the format."""
    record = _real_record("Q-000005")
    assert record["negative_words"] == ["NOT"]
    assert describe_tags.answer_form(record) == "expression"
    ctx = {"item_id": "Q-000005"}

    ok, msg = _check("E2", _e2("pick_correct_statement"), ctx)
    assert ok, msg

    # a letter-code format over single-item options is still wrong, negative or not
    assert _failed(_check("E2", _e2("pick_match_code"), ctx), "E2_NEGATIVE_GUARD")
    assert _failed(_check("E2", _e2("predict_product"), ctx), "E2_NEGATIVE_GUARD")


def test_e2_guard_failure_carries_specs_own_retry_sentence():
    """Spec 13/E2: 'retry with "The stem contains <word>"'. The segment detail must begin with
    that literal sentence so the plugin can forward it unchanged."""
    ok, msg = _check("E2", _e2("pick_correct"), {"item_id": "Q-000005"})
    assert not ok
    assert "The stem contains NOT." in msg


def test_e2_no_negative_word_no_longer_constrains_the_format():
    """REAL DATA: Q-000015 has no negative word at all (B3 recorded none, and none appears in the
    stem or its four statements).

    THIS TEST ASSERTS THE REMOVAL OF A CHECK, deliberately. Spec 13/E2's third guard row was
    "format is pick_incorrect but the stem carries no negative word -> fail". That inference died
    with allowed_values v0.3: `pick_incorrect` merged into `pick_correct_statement`, which is the
    correct format for a POSITIVE stem too ("Which of the following is correct?"), so the same
    condition now proves nothing. The check was deleted rather than loosened -- a weakened check
    that still looks like the original is worse than none -- and scripts/checks/E2.py returns a
    note saying where the negation is verified instead.

    What must NOT happen is a silent pass that still claims to have checked negation, so the note
    is asserted here."""
    record = _real_record("Q-000015")
    assert record["negative_words"] == []
    ok, msg = _check("E2", _e2("pick_correct_statement"), {"item_id": "Q-000015"})
    assert ok, msg
    assert "task_polarity" in msg, (
        "E2 must say that negation is no longer verifiable from the format, not pass silently; "
        f"got {msg!r}")
    ok, msg = _check("E2", _e2("pick_correct_combination"), {"item_id": "Q-000015"})
    assert ok, msg


def test_e2_guard_negative_with_combination_options_keeps_the_format():
    """FIXTURE-ONLY: spec 13/E2's second guard row. No real canonical record has a negative word
    AND combination options -- Q-000005 has the negative but single-item options, Q-000015 has
    combination options but no negative. See tests/fixtures/stage_e/README.md."""
    record = _fixture_record("record_negative_with_combination_options.json")
    assert describe_tags.answer_form(record) == "combination_code"
    ctx = {"item_id": "FIXTURE-E2-COMBO", "input_data": {"record": record}}

    ok, msg = _check("E2", _e2("pick_correct_combination"), ctx)
    assert ok, msg
    # The negative belongs in E6's `negation`, not in the format.
    assert describe_tags.negation(record) == "single"
    assert _failed(_check("E2", _e2("pick_incorrect"), ctx), "E2_NEGATIVE_GUARD")
    assert _failed(_check("E2", _e2("odd_one_out"), ctx), "E2_NEGATIVE_GUARD")


def test_e2_guard_negative_with_match_code_options_keeps_the_format():
    """FIXTURE-ONLY: the same guard row for match codes. No real canonical record is a
    match-the-lists question at all."""
    record = _fixture_record("record_negative_with_match_code_options.json")
    assert describe_tags.answer_form(record) == "match_code"
    ctx = {"item_id": "FIXTURE-E2-MATCH", "input_data": {"record": record}}

    ok, msg = _check("E2", _e2("pick_match_code"), ctx)
    assert ok, msg
    assert _failed(_check("E2", _e2("pick_incorrect"), ctx), "E2_NEGATIVE_GUARD")
    # The wrong code-shaped format is also caught.
    assert _failed(_check("E2", _e2("pick_correct_combination"), ctx), "E2_NEGATIVE_GUARD")


def test_e2_guard_is_never_skipped_silently_without_a_record():
    """A missing record must FAIL, not pass. The guard is the one E2 rule that may never be
    skipped quietly."""
    assert _failed(_check("E2", _e2("pick_correct"), {"item_id": "NO-SUCH-QID"}),
                    "E2_NEGATIVE_GUARD")


def test_e2_new_format_needs_a_description():
    data = _e2("new_format", new_description="")
    assert _failed(_check("E2", data, {"item_id": "Q-000015"}), "E_NEW_CATEGORY")
    ok, msg = _check("E2", _e2("new_format", new_description="pick the matching reaction route"),
                      {"item_id": "Q-000015"})
    assert ok, msg


# ===========================================================================
# E3 -- content_shape
# ===========================================================================

def _e3(shape, why="Evidence is the ordered stages of mitosis.", confidence="high",
         new_description=""):
    return {"content_shape": shape, "why": why, "new_description": new_description,
             "confidence": confidence}


def test_e3_why_must_have_substance():
    assert _failed(_check("E3", _e3("process", why="recall"), {"item_id": "Q-000015"}))
    ok, msg = _check("E3", _e3("process"), {"item_id": "Q-000015"})
    assert ok, msg


def test_e3_why_must_not_just_restate_the_tag():
    assert _failed(_check("E3", _e3("cycle_or_pathway", why="cycle or pathway."),
                            {"item_id": "Q-000015"}))


def test_e3_medium_confidence_is_a_flag_not_a_failure():
    """Spec 13/E3: medium confidence raises E3_MEDIUM (low). codebook/E3.md §4 tells the agent to
    use medium whenever no evidence was available, which is most real questions today."""
    ok, msg = _check("E3", _e3("one_line", confidence="medium"), {"item_id": "Q-000015"})
    assert ok and "E3_MEDIUM" in msg


def test_e3_current_affairs_needs_evidence_and_must_not_contradict_d6():
    """FIXTURE-ONLY for the D6 half: no real record has a syllabus_status yet (D6 has never run)."""
    ctx_no_evidence = {"item_id": "Q-000015", "input_data": {"evidence": []}}
    assert _failed(_check("E3", _e3("current_affairs", why="Nothing in NCERT states this date."),
                            ctx_no_evidence))

    ctx_contradiction = {"item_id": "Q-000015",
                          "input_data": {"evidence": [{"exact_line": "x"}],
                                           "record": dict(_real_record("Q-000015"),
                                                            syllabus_status="latest_ncert")}}
    assert _failed(_check("E3", _e3("current_affairs", why="Nothing in NCERT states this date."),
                            ctx_contradiction))


# ===========================================================================
# E4 -- thinking, and the branch rule
# ===========================================================================

_REAL_E4_VERSION = codebook_version.version_for_step("E4")


def _e4(primary, secondary=None, why="The student must judge four separate statements.",
         confidence="high", version=None, branch_used="none"):
    return {"primary": primary, "secondary": secondary, "why": why, "confidence": confidence,
             "codebook_version": _REAL_E4_VERSION if version is None else version,
             "branch_used": branch_used}


def _e4_ctx(qid, record=None, with_branch=True):
    input_data = {}
    rec = record or _real_record(qid)
    if with_branch:
        input_data["branch"] = rec.get("branch")
    input_data["record"] = rec
    return {"item_id": qid, "step": "E4", "input_data": input_data}


def test_e4_fails_when_the_input_never_carried_the_branch():
    """THE CHECK THAT MAKES BRANCH-BLINDNESS IMPOSSIBLE, not merely discouraged. REAL DATA:
    Q-000005 is Chemistry/organic. If the plugin never puts `branch` in the agent input, the
    agent cannot have conditioned on it and no check of the OUTPUT could reveal that."""
    ok, msg = _check("E4", _e4("elimination", branch_used="organic",
                                 why="Four reagent routes must each be judged separately."),
                       _e4_ctx("Q-000005", with_branch=False))
    assert not ok and "carried no `branch` field" in msg


def test_e4_branch_used_must_match_the_real_branch():
    """REAL DATA: Q-000005 is Chemistry/organic; Q-000001 is Physics and has no branch at all,
    which `branch_used` spells 'none'.

    Asserts the INVARIANT -- branch_used must equal whatever the record says -- rather than a
    specific branch value for the Biology case. An earlier version of this test hard-coded
    `Q-000015["branch"] == "unsure"` and broke the moment B7 started assigning Biology's
    botany/zoology, i.e. it failed because the data got BETTER. A test that has to be edited
    whenever the pipeline improves is testing the pipeline's current output, not its rule.
    """
    assert _real_record("Q-000005")["branch"] == "organic"
    assert _real_record("Q-000001").get("branch") is None
    bio = _real_record("Q-000015")
    assert bio["subject"] == "Biology"
    assert bio["branch"] in {"botany", "zoology", "unsure"}, bio["branch"]

    ok, msg = _check("E4", _e4("elimination", branch_used="organic",
                                 why="Four reagent routes must each be judged separately."),
                       _e4_ctx("Q-000005"))
    assert ok, msg
    assert _failed(_check("E4", _e4("elimination", branch_used="physical",
                                      why="Four reagent routes must each be judged separately."),
                            _e4_ctx("Q-000005")))
    # Physics: the record has no branch, so "none" is right and anything else is wrong.
    ok, msg = _check("E4", _e4("numerical", branch_used="none",
                                 why="One formula, stress = W/A, with one substitution."),
                       _e4_ctx("Q-000001"))
    assert ok, msg
    assert _failed(_check("E4", _e4("numerical", branch_used="organic",
                                      why="One formula, stress = W/A, with one substitution."),
                            _e4_ctx("Q-000001")))


def test_e4_chemistry_tag_against_its_branch_prior_must_say_why():
    """REAL DATA: Q-000005 is organic, whose confirmed prior is recall/elimination. `numerical`
    there is LEGITIMATE -- codebook/E4.md §1: 'if your tag contradicts the prior, that is normal
    -- say why in one clause and keep your tag' -- but it must be accounted for."""
    short = _e4("numerical", branch_used="organic", why="It is a calculation.")
    assert _failed(_check("E4", short, _e4_ctx("Q-000005")))

    accounted = _e4("numerical", branch_used="organic",
                     why="Unusually for organic chemistry this needs a real mole computation "
                         "before the product can be chosen.")
    ok, msg = _check("E4", accounted, _e4_ctx("Q-000005"))
    assert ok, msg
    assert "contradicts the organic prior" in msg


def test_e4_chemistry_with_no_branch_must_say_the_branch_was_unavailable():
    """FIXTURE-ONLY: no real record is Chemistry with branch `unsure` -- both real Chemistry
    records resolved to `organic`. codebook/E4.md §1: take no prior, and say so in `why`."""
    record = dict(_real_record("Q-000005"), branch="unsure")
    ctx = _e4_ctx("Q-000005", record=record)
    silent = _e4("recall", branch_used="unsure",
                  why="One remembered fact about amine preparation decides it.")
    assert _failed(_check("E4", silent, ctx))

    stated = _e4("recall", branch_used="unsure",
                  why="Branch was unavailable so no prior was used; one remembered fact decides.")
    ok, msg = _check("E4", stated, ctx)
    assert ok, msg


def test_e4_biology_branch_is_carried_but_takes_no_prior():
    """REAL DATA: Q-000015 (the female reproductive cycle) is Biology, and B7 now assigns it a real
    botany/zoology branch. E4's branch PRIOR is Chemistry-only, so a Biology record must pass
    whatever its branch says -- the branch is still copied verbatim, because that copy is the only
    evidence the branch was read, but no prior is applied to it.

    This test previously asserted the OPPOSITE state: that Biology's branch was permanently
    `unsure` because no step ever assigned one, and that E4 should name that taxonomy gap in its
    message. That gap was real when written and is now closed (botany 141, zoology 145, unsure 0),
    so the test is rewritten to the rule rather than deleted -- the thing worth protecting is that
    E4 accepts a Biology branch without applying a Chemistry prior to it.
    """
    record = _real_record("Q-000015")
    branch = record["branch"]
    assert branch in {"botany", "zoology"}, f"expected a real Biology branch, got {branch!r}"
    ok, msg = _check("E4", _e4("elimination", branch_used=branch,
                                 why="Each of the four statements needs its own verdict."),
                       _e4_ctx("Q-000015"))
    assert ok, msg
    # A Chemistry branch name must still be rejected on a Biology record: branch_used is copied,
    # never chosen.
    assert _failed(_check("E4", _e4("elimination", branch_used="organic",
                                      why="Each of the four statements needs its own verdict."),
                            _e4_ctx("Q-000015")))


def test_e4_low_confidence_goes_to_the_adjudicator():
    """Spec 13/E4 Checks: 'confidence not low'."""
    assert _failed(_check("E4", _e4("recall", confidence="low",
                                      why="One remembered fact about error types decides it."),
                            _e4_ctx("Q-000011")), "E4_ADJUDICATED")


def test_e4_recall_and_elimination_may_never_be_paired():
    """codebook/E4.md §4: two points on one scale, not two kinds of thinking."""
    for primary, secondary in (("recall", "elimination"), ("elimination", "recall")):
        data = _e4(primary, secondary,
                    why="Several separate facts must each be settled before answering.")
        assert _failed(_check("E4", data, _e4_ctx("Q-000011")))


def test_e4_secondary_may_not_repeat_the_primary():
    data = _e4("numerical", "numerical", why="Two formulae and a ratio must be combined.")
    assert _failed(_check("E4", data, _e4_ctx("Q-000004")))


def test_e4_codebook_version_none_while_the_file_exists_is_a_wiring_failure():
    """REAL DATA: codebook/E4.md really is on disk, so an output claiming "none" means the
    codebook never reached the agent -- the one failure that is otherwise invisible."""
    assert _REAL_E4_VERSION != codebook_version.NONE
    data = _e4("recall", version="none",
                why="One remembered NCERT definition of random error decides it.")
    ok, msg = _check("E4", data, _e4_ctx("Q-000011"))
    assert not ok and "never reached the agent" in msg


def test_e4_codebook_version_must_be_the_real_hash():
    data = _e4("recall", version="deadbeef1234",
                why="One remembered NCERT definition of random error decides it.")
    assert _failed(_check("E4", data, _e4_ctx("Q-000011")))


# ===========================================================================
# E5 -- one wrong option
# ===========================================================================

def _e5(option, trap, why="Menopause is a different event with a confusably similar name.",
         confidence="high", new_description=""):
    return {"option": option, "trap": trap, "why": why, "new_description": new_description,
             "confidence": confidence}


def _e5_ctx(qid, number, record=None, change_log=None):
    rec = record or _real_record(qid)
    options = rec.get("options_en") or {}
    return {"item_id": f"{qid}#opt{number}", "step": "E5",
             "input_data": {"record": rec,
                              "wrong_option": {"number": str(number),
                                                 "text": options.get(str(number))},
                              "change_log_entries": change_log or []}}


def test_e5_never_tags_the_correct_option():
    """REAL DATA: Q-000015's official answer is option 4 ('A, C and D only'), independently
    confirmed by B6's blind solve. There is no trap on the answer."""
    assert _real_record("Q-000015")["official_answer"] == "4"
    ok, msg = _check("E5", _e5("4", "partial_combination"), _e5_ctx("Q-000015", 4))
    # "an answer", not "the answer": a multiple_accepted question has more than one correct
    # option (B5 records them comma-joined, e.g. "1,3"), so answer_taught() returns a SET and the
    # message was reworded to match. Before that fix the comparison was `option == "1,3"`, which
    # could never be true -- silently disabling this very rule on exactly those questions.
    assert not ok and "IS an answer students are taught" in msg


def test_e5_real_three_wrong_options_of_q15_all_pass():
    """REAL DATA: the only fully worked real three-option E5 example in the bank
    (codebook/E5.md §3), whose answer and statement truth-values were independently confirmed by
    B6's blind solve. Three items, three traps, one question -- exactly E5's granularity."""
    traps = {
        "1": ("partial_combination", "Both named items are true but C is wrongly left out."),
        "2": ("look_alike_term", "Includes statement B, which says menopause for menarche."),
        "3": ("look_alike_term", "Includes the same false statement B, menopause for menarche."),
    }
    for number, (trap, why) in traps.items():
        ok, msg = _check("E5", _e5(number, trap, why=why), _e5_ctx("Q-000015", number))
        assert ok, f"option {number}: {msg}"


def test_e5_option_must_be_the_one_this_item_is_for():
    """E5's item is ONE wrong option; tagging another silently attributes the trap to the wrong
    distractor."""
    assert _failed(_check("E5", _e5("3", "look_alike_term"), _e5_ctx("Q-000015", 2)))


def test_e5_item_id_suffix_is_enough_when_the_plugin_passes_no_wrong_option():
    ctx = {"item_id": "Q-000015#opt2", "step": "E5"}
    ok, msg = _check("E5", _e5("2", "look_alike_term"), ctx)
    assert ok, msg


def test_e5_old_ncert_fact_needs_a_real_change_log_entry():
    """REAL DATA on the precondition's own state: ncert/change_log.csv holds only its header row,
    so this trap is effectively untaggable today and an agent producing it has guessed."""
    assert _failed(_check("E5", _e5("2", "old_ncert_fact", why="Menopause was the older answer."),
                            _e5_ctx("Q-000015", 2)))
    ok, msg = _check("E5", _e5("2", "old_ncert_fact", why="The older edition said 20 billion."),
                      _e5_ctx("Q-000015", 2,
                               change_log=[{"passage_id": "BIO12L-CH03-P14",
                                              "change_type": "fact_changed"}]))
    assert ok, msg


def test_e5_calculation_slip_must_name_the_slip():
    """REAL DATA: Q-000004's answer is the ratio 3 : 5; option 2 is '5 : 3', the inverted ratio
    -- a nameable slip (codebook/E5.md §3)."""
    assert _failed(_check("E5", _e5("2", "calculation_slip", why="Arithmetic error."),
                            _e5_ctx("Q-000004", 2)))
    ok, msg = _check("E5", _e5("2", "calculation_slip", why="The ratio is inverted: 5 : 3."),
                      _e5_ctx("Q-000004", 2))
    assert ok, msg


def test_e5_partial_combination_needs_combination_options():
    """REAL DATA both ways: Q-000015's options are combination_code (the value applies);
    Q-000009's are LaTeX expressions (it cannot)."""
    assert describe_tags.answer_form(_real_record("Q-000015")) == "combination_code"
    ok, msg = _check("E5", _e5("1", "partial_combination",
                                 why="Both named items are true but C is wrongly left out."),
                       _e5_ctx("Q-000015", 1))
    assert ok, msg

    assert describe_tags.answer_form(_real_record("Q-000009")) == "expression"
    assert _failed(_check("E5", _e5("1", "partial_combination",
                                      why="Both named items are true but one is left out."),
                            _e5_ctx("Q-000009", 1)))


def test_e5_question_with_no_answer_cannot_be_trap_tagged():
    """REAL DATA: Q-000004 is `dropped` with no official_answer. It has a B8 corrected_answer of
    '1', which IS the answer taught -- so option 1 must be refused and the others allowed."""
    record = _real_record("Q-000004")
    assert record["status"] == "dropped" and record["corrected_answer"] == "1"
    assert _failed(_check("E5", _e5("1", "calculation_slip", why="Squared the ratio: 9 : 25."),
                            _e5_ctx("Q-000004", 1)))
    ok, msg = _check("E5", _e5("3", "calculation_slip", why="Dropped the factor of 2."),
                      _e5_ctx("Q-000004", 3))
    assert ok, msg


# ===========================================================================
# E6 -- stem_context
# ===========================================================================

def _e6(value, why="Both a figure and a reaction apply; the reaction is what is needed.",
         confidence="high"):
    return {"stem_context": value, "why": why, "confidence": confidence}


def test_e6_real_q13_is_the_one_agent_case_in_the_whole_bank():
    """REAL DATA: Q-000013 is the only canonical record where two context patterns fire at once
    (reaction_given + figure_given), so it is the only one the agent legitimately gets."""
    assert describe_tags.stem_context(_real_record("Q-000013"))[0] is None
    ok, msg = _check("E6", _e6("reaction_given"), {"item_id": "Q-000013"})
    assert ok, msg


def test_e6_plain_can_never_win_a_tie_break():
    """codebook/E6.md §2: if two patterns fired, something applies, so `plain` is wrong."""
    ok, msg = _check("E6", _e6("plain"), {"item_id": "Q-000013"})
    assert not ok and "never a tie-break winner" in msg


def test_e6_agent_must_not_run_when_the_script_decided():
    """REAL DATA: 9 of the 10 canonical records are decided by describe_tags' own patterns."""
    decided = []
    for qid in _real_canonical_ids():
        value, _why = describe_tags.stem_context(_real_record(qid))
        if value is None:
            continue
        decided.append(qid)
        ok, msg = _check("E6", _e6(value), {"item_id": qid})
        assert not ok and "already decides" in msg, f"{qid}: {msg}"
    # Same reasoning as the E1 version: the per-question rejection above is the real assertion;
    # a hardcoded total just breaks whenever the bank grows.
    assert len(decided) >= 5, f"too few script-decided stems to be a real test: {len(decided)}"


def test_e6_unsure_is_an_outcome_not_a_failure():
    ok, msg = _check("E6", _e6("unsure", why="Neither the figure nor the reaction is removable."),
                      {"item_id": "Q-000013"})
    assert ok and "E6_CONTEXT_UNSURE" in msg


def test_e6_value_outside_the_fired_set_is_reported_not_failed():
    """codebook/E6.md §4.2 records two real cases where the script's patterns under-detect, so an
    agent may legitimately name a framing no regex covers."""
    ok, msg = _check("E6", _e6("case_scenario",
                                 why="A chemist is described carrying out the reduction."),
                       {"item_id": "Q-000013"})
    assert ok and "not one of the contexts" in msg


def test_e6_why_must_have_substance():
    assert _failed(_check("E6", _e6("reaction_given", why="reaction"), {"item_id": "Q-000013"}))


# ===========================================================================
# E0 -- category discovery
# ===========================================================================

_E0_OPEN_LOOK = {
    "student_must": "check each of four statements about the menstrual cycle and reject the one "
                    "that names the wrong event",
    "built_as": "four lettered statements in the stem, options are combinations of letters",
    "asks_to_pick": "which combination of statements is right",
    "ncert_material": "the described phases of the human female reproductive cycle",
    "wrong_options": {"1": "leaves out a true statement",
                        "2": "includes the statement that names the wrong event",
                        "3": "includes the same wrong event and drops a true one"},
}


def test_e0_open_look_passes_clean_free_text():
    """REAL DATA: the answer comes from real Q-000015 (official answer 4), so the three
    wrong_options keys are the real wrong options."""
    ok, msg = _check("E0", _E0_OPEN_LOOK, {"item_id": "Q-000015"})
    assert ok, msg


def test_e0_open_look_must_not_name_a_category():
    """The one rule that makes E0 worth running: E0.1 runs with NO categories shown, so a free
    answer naming `elimination` means the discovery has become a matching exercise."""
    leaked = dict(_E0_OPEN_LOOK, student_must="use elimination across four statements")
    ok, msg = _check("E0", leaked, {"item_id": "Q-000015"})
    assert not ok and "elimination" in msg

    leaked2 = dict(_E0_OPEN_LOOK, built_as="an assertion reason pair")
    assert _failed(_check("E0", leaked2, {"item_id": "Q-000015"}))


def test_e0_open_look_ordinary_english_is_not_a_leak():
    """`process`, `list`, `comparison` and the like are ordinary English a plain description
    cannot avoid; flagging them would make the check fire on correct free text."""
    plain = dict(_E0_OPEN_LOOK,
                  student_must="follow the process in the right order and compare two stages")
    ok, msg = _check("E0", plain, {"item_id": "Q-000015"})
    assert ok, msg


def test_e0_open_look_must_not_explain_the_correct_option():
    """REAL DATA: Q-000015's answer is option 4."""
    bad = dict(_E0_OPEN_LOOK, wrong_options=dict(_E0_OPEN_LOOK["wrong_options"],
                                                    **{"4": "looks right"}))
    ok, msg = _check("E0", bad, {"item_id": "Q-000015"})
    assert not ok and "correct answer" in msg


def test_e0_grouper_reconciles_every_answer():
    """FIXTURE-ONLY: E0 has never run and cannot yet (10 questions, spec asks ~300)."""
    data = _fixture_record("e0_grouper_output.json")
    data = {k: v for k, v in data.items() if k != "_fixture"}
    # The fixture's per-subject counts total 10 and `unclear` holds 1, so the pool is 11.
    answers = [{"question_id": f"FIXTURE-Q-{i}", "subject": "Biology", "year": 2023, "text": "x"}
               for i in range(1, 12)]
    ctx = {"item_id": "thinking", "step": "E0",
            "input_data": {"starting_list": tag_values.values("thinking"), "answers": answers}}
    ok, msg = _check("E0", data, ctx)
    assert ok, msg

    # Drop an answer from the pool -> the counts no longer reconcile.
    ctx_short = {"item_id": "thinking", "step": "E0",
                  "input_data": {"starting_list": tag_values.values("thinking"),
                                   "answers": answers[:5]}}
    assert _failed(_check("E0", data, ctx_short))


def test_e0_grouper_new_must_not_name_an_existing_category():
    data = _fixture_record("e0_grouper_output.json")
    data = {k: v for k, v in data.items() if k != "_fixture"}
    data["categories"][2]["name"] = "recall"  # `new` but already on the starting list
    answers = [{"question_id": f"FIXTURE-Q-{i}"} for i in range(1, 12)]
    ctx = {"item_id": "thinking", "step": "E0",
            "input_data": {"starting_list": tag_values.values("thinking"), "answers": answers}}
    ok, msg = _check("E0", data, ctx)
    assert not ok and "already on the starting list" in msg


def test_e0_grouper_subjects_must_match_non_zero_counts():
    data = _fixture_record("e0_grouper_output.json")
    data = {k: v for k, v in data.items() if k != "_fixture"}
    data["categories"][1]["subjects"] = ["Physics", "Biology"]  # Biology count is 0
    answers = [{"question_id": f"FIXTURE-Q-{i}"} for i in range(1, 12)]
    ctx = {"item_id": "thinking", "step": "E0",
            "input_data": {"starting_list": tag_values.values("thinking"), "answers": answers}}
    assert _failed(_check("E0", data, ctx))


def test_e0_output_matching_neither_worker_is_rejected():
    assert _failed(_check("E0", {"tag": "thinking"}, {"item_id": "x"}))


# ===========================================================================
# E0's category sheet -- the "never write a codebook" guarantee
# ===========================================================================

def test_e0_sheet_refuses_to_write_a_codebook_markdown_file():
    """Spec 13/E0: 'Never: write codebook/E*.md. Those are the owner's.' Enforced as a
    precondition in code, not as a comment."""
    for path in ("codebook/E4.md", "/tmp/E1.md", "codebook/E0_findings/notes.md"):
        with pytest.raises(ValueError, match="NEVER write a codebook"):
            e0_category_sheet._assert_writable(path)


def test_e0_sheet_refuses_any_destination_but_category_sheet_csv():
    for path in ("codebook/E0_findings/other.csv", "/tmp/out.csv", "data/questions.csv"):
        with pytest.raises(ValueError):
            e0_category_sheet._assert_writable(path)
    assert e0_category_sheet._assert_writable("x/category_sheet.csv")


def test_e0_reports_its_sample_state_consistently():
    """REAL DATA, and deliberately NOT pinned to a count.

    This test twice encoded a live number as an assertion -- first `total == 10`, then
    `total == real` recomputed here -- and both broke, the second one because extraction is
    actively creating records and the count genuinely changes BETWEEN the sheet reading the
    directory and this test re-reading it. Racing live data is not a test.

    What is actually invariant, and what E0 exists to get right: it reports its own sample
    honestly, its per-subject counts add up to its total, and its refusal is a pure function of
    whether the sample clears spec 13/E0's floors. The refusal lifting once the bank passes ~300
    is the real signal, and this asserts the rule rather than today's side of it."""
    _rows, total, per_subject, _unassigned = e0_category_sheet.sample_state()
    assert total >= 0 and all(per_subject[s] >= 0 for s in e0_category_sheet.SUBJECTS)
    assert sum(per_subject[s] for s in e0_category_sheet.SUBJECTS) + _unassigned == total, \
        "per-subject counts plus unassigned must equal the reported total"
    clears = (total >= e0_category_sheet.SAMPLE_FLOOR and
              all(per_subject[s] >= e0_category_sheet.PER_SUBJECT_FLOOR
                  for s in e0_category_sheet.SUBJECTS))
    assert e0_category_sheet.report_sample() is clears, \
        f"E0 must refuse exactly when the sample is short (total={total}, per_subject={dict(per_subject)})"


def test_e0_sheet_lays_out_specs_eleven_columns(tmp_path):
    """FIXTURE-ONLY, and written into pytest's tmp_path -- never into codebook/."""
    inputs = tmp_path / "in"
    inputs.mkdir()
    data = _fixture_record("e0_grouper_output.json")
    (inputs / "thinking.json").write_text(json.dumps(data), encoding="utf-8")

    out = tmp_path / "category_sheet.csv"
    outputs = e0_category_sheet.load_grouper_outputs(str(inputs))
    assert len(outputs) == 1
    rows = e0_category_sheet.rows_from(outputs)
    e0_category_sheet.write_sheet(rows, str(out))

    import csv
    with open(out, newline="", encoding="utf-8") as f:
        read = list(csv.DictReader(f))
    assert list(read[0].keys()) == e0_category_sheet.COLUMNS
    assert [r["category"] for r in read] == ["elimination", "calculation", "spot the exception"]
    assert [r["decision"] for r in read] == ["keep", "keep", "new"]
    assert read[0]["count_biology"] == "3" and read[0]["example_1"] == "FIXTURE-Q-1"
    assert read[2]["example_2"] == ""   # only one example, and no column invented for it


# ===========================================================================
# legacy_match and the two shared helpers
# ===========================================================================

def test_legacy_fields_never_reach_an_agent():
    """Spec Section 13: the three legacy fields 'are never inputs to any agent'."""
    with pytest.raises(ValueError):
        legacy_match.assert_no_legacy({"q": {"stem_en": "x"}, "m": [{"legacy_topic": "t"}]})
    assert legacy_match.assert_no_legacy({"q": {"stem_en": "x"}, "allowed": ["a"]})


def test_legacy_match_ranks_the_right_sheet_row_on_real_data():
    """REAL DATA, and a REAL FINDING: spec's 'similarity >= 0.85 on word 3-grams' matches NOTHING
    on this corpus, yet the top-ranked row is the right one every time, by a wide gap. Both halves
    are asserted so neither can regress silently."""
    record = _real_record("Q-000015")
    result = legacy_match.match_one(record)
    assert result["best"] is not None
    assert result["best"]["legacy_chapter"] == "Human Reproduction"
    assert result["best"]["legacy_topic"] == "Menstrual Cycle"
    # Ranked correctly, by a wide margin...
    assert result["similarity"] > 4 * result["runner_up"]
    # ...and still below spec's absolute threshold, so nothing is stored.
    assert result["similarity"] < legacy_match.MATCH_THRESHOLD
    assert result["matched"] is False and result["fields"] == {}


def test_codebook_version_matches_the_formula_already_in_step_plugins():
    """scripts/step_plugins.py::_d_codebook already computes sha256(raw)[:12] for D11. This module
    must produce the identical value so the two can never disagree."""
    import hashlib
    path = rc.pp("codebook", "E4.md")
    with open(path, "rb") as f:
        raw = f.read()
    assert codebook_version.version_for_step("E4") == hashlib.sha256(raw).hexdigest()[:12]
    assert codebook_version.for_step("NOPE") == (None, "none")


def test_every_codebook_on_disk_is_declared_in_steps_yaml():
    """REAL DATA. This test replaces an earlier one that asserted the codebooks were NOT wired --
    a temporary state it encoded as an assertion, which then failed the moment the state was
    fixed. Inverted here so it guards the correct state instead.

    Why declaring matters even where a plugin hardcodes its path: D4Plugin already read
    codebook/D4_link_type.md off disk, but `codebook_file: null` hid that dependency from the
    Section 15 cascade, so editing the codebook would NOT have re-run D4 and its tags would have
    kept a stale codebook_version. The declaration is what makes the dependency visible."""
    cfg = rc.load_steps_config()
    for step in ("D4", "D11", "E1", "E2", "E3", "E4", "E5", "E6"):
        text, version = codebook_version.for_step(step)
        assert text is not None, f"codebook for {step} is missing from disk"
        assert version != codebook_version.NONE
        declared = (cfg[step] or {}).get("codebook_file")
        assert declared, (
            f"{step}'s codebook exists on disk but config/steps.yaml says codebook_file: "
            f"{declared!r} -- the cascade cannot see it and every tag it produces would record "
            f"codebook_version 'none'")
    # E0 is the one whose null is load-bearing and must STAY null: e0-open-look's entire purpose
    # is to describe questions with NO categories in front of it, so handing it a codebook would
    # defeat the step.
    assert (cfg["E0"] or {}).get("codebook_file") is None


def test_the_two_script_halves_still_pass_their_own_self_tests():
    """scripts/type_patterns.py (11 spec boundary cases) and scripts/describe_tags.py (10 cases)
    were real-tested before this build; the E schemas and checks are written to agree with them,
    so a regression in either would invalidate the checks."""
    assert type_patterns._self_test() == 0
    assert describe_tags._self_test() == 0
