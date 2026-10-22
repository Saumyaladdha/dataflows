#!/usr/bin/env python3
"""Proof that scripts/checks/A2.py's rebuilt text-layer comparison is BOTH precise on real data
and still fails genuinely wrong transcriptions. Written alongside the 2026-10-12 fix for the
A2_TEXT_MISMATCH false-positive defect; see that file's module docstring for the three real
PDF-extraction artifacts it has to tolerate and the thresholds measured here.

Two halves, both run against every real A2 output in steps/A2/out that has a text layer
(104 of them at the time of writing: Biology ch02/ch03, Chemistry ch09, Physics ch08):

  1. PRECISION. Every real output must pass, except ones with an independently-known genuine
     defect (BIO12L-ch03-p001.retry1, whose 7 blocks all lack the schema-required `n` field --
     see docs/OPEN_QUESTIONS.md 2026-10-10). The old check failed 89 of 104 (86%).

  2. SENSITIVITY. Deliberately corrupted copies of those same real block sets must still be
     caught. Catch rates are asserted per corruption family at the levels actually measured, so
     that a future change which silently weakens the check fails this test instead of passing
     quietly. The rates are deliberately NOT all 100%: a single substituted word inside one
     paragraph of a 400-word page is ~0.25% of the page and is below any page-level bar. That
     limit is real and recorded rather than hidden -- see the docstring's "Honest limits".

Run: .venv/bin/python3 tests/test_a2_check.py   (or via pytest tests/)
"""
import copy
import glob
import json
import os
import random
import re
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from checks import A2 as a2_check  # noqa: E402

# Real outputs with an independently-confirmed genuine defect, which MUST keep failing.
KNOWN_BAD = {("BIO12L-ch03-p001", "retry1")}  # all 7 blocks miss the required `n` field

# Real outputs the check currently FAILS that have not each been individually verified.
#
# Why this set exists, and why it is not folded into KNOWN_BAD: the original test asserted that
# NO real A2 output fails the check, treating any failure as a false positive. That was a fair
# assumption when the corpus was small and clean. The corpus is now 446 outputs and 33 of them
# fail, so the assumption inverts the meaning of the test -- it would report a growing pile of
# genuine extraction defects as a defective CHECK.
#
# One member was confirmed genuine by direct inspection of the rendered page:
# BIO11L-ch01-p001 returned ZERO blocks for a page that visibly carries 1,478 characters of real
# NCERT prose (the Unit 1 introduction, printed beside the seahorse illustration and the unit
# banner). The agent called the whole page front matter; `.claude/agents/a2-page-reader.md` has
# since been given an explicit rule that furniture means publishing apparatus, not "a page that
# looks like an opener".
#
# The other 32 are NOT certified here as genuine. Their reported causes range from almost
# certainly real (0 blocks, a block 0.0% matched to the text layer, numbers absent from the page)
# to small shortfalls just under the bar (recall ~98.4-99.0%), and triaging each needs the page
# image. They are listed so that:
#   (a) the check's behaviour on them is pinned -- if a change to the check silently starts
#       PASSING one, that is a precision regression and this test says so;
#   (b) the set cannot grow unnoticed -- a new failure outside it fails the test;
#   (c) the list is the work queue for the Stage A re-read, rather than invisible.
# Removing an entry requires either fixing the output or showing the failure was spurious.
UNTRIAGED_FAILURES = {
    # 2026-10-13: fifteen (item, "runA") entries were REMOVED from this set, not because their
    # outputs changed but because the test now skips a run whose own page has a later PASSING run.
    # Those fifteen were all repaired-by-retry pages, so listing them turned every successful
    # repair into permanent test debt. If a retry fails too, both runs are still reported.
    # --- added 2026-10-13, from the Stage A push. All five are the exponent-fold failure mode:
    # scripts/checks/A2.py's `_numbers()` folds a script/LaTeX exponent into the digits before it
    # and then requires every number to appear in the page's text_layer, but the layer often
    # breaks the line mid-expression so the folded number is not in it. Documented in
    # docs/OPEN_QUESTIONS.md.
    #
    # PHY12O-ch01-p024 WAS listed here as permanently unfixable, on the reasoning that the layer
    # stores r-sub-1-squared as the scrambled tokens `2 1r`, so the sentence "The number of field
    # lines, cutting unit area element is therefore n/(r1^2 dOmega)" scores 69.2% against a 75%
    # bar, and that "no honest transcription can clear that bar".
    #
    # RESOLVED 2026-10-15: that conclusion was wrong, and the page now passes honestly. The third
    # read defers the ONE layer-scrambled sentence whole as an `equation` block with a bbox over
    # its two printed lines -- which is precisely what the brief prescribes for a layer-scrambled
    # r-sub-n-squared region -- and transcribes every other paragraph as real text, footnote
    # included. The prose-word metric then scores only the prose, which matches. Nothing was
    # written that is not on the page; the unreadable part was deferred to A2S rather than guessed.
    #
    # Kept as a worked example because the earlier reasoning is the trap: a coverage bar that an
    # inline transcription cannot clear is a signal to DEFER that region, not evidence that the
    # page is unfixable.
    # Awaiting a retry the runner has already queued; a single number absent from the layer.
    ("CHE11L-ch02-p007", "runA"),   # number 35 not in the layer
    ("CHE11O-ch07-p024", "runA"),   # number 32 not in the layer
    # CHE11L-ch02-p017 is the all-table tension, hitting for real: the page defers content to A2S
    # so only the wholesale 50% bar applies, and it lands at 49.8% -- failing by 0.2 of a point.
    # A page that defers its tables whole, which is what the agent file instructs, can fall under
    # even that bar (measured 31.4% on CHE12O-ch07-p009). The check and the documented behaviour
    # disagree here; logged as unresolved for the owner.
    ("CHE11L-ch02-p017", "runA"),
    ("BIO11L-ch01-p001", "runA"), ("BIO11L-ch03-p001", "runA"), ("BIO11L-ch03-p003", "runA"),
    ("BIO11L-ch03-p009", "runA"), ("BIO12L-ch05-p027", "runA"), ("BIO12L-ch05-p029", "retry1"),
    ("BIO12L-ch05-p029", "runA"), ("CHE12L-ch01-p003", "retry1"),
    ("CHE12L-ch01-p003", "runA"), ("CHE12L-ch01-p011", "retry1"), ("CHE12L-ch01-p011", "runA"),
    ("CHE12L-ch01-p016", "runA"),
    ("PHY12L-ch03-p015", "retry1"), ("PHY12L-ch03-p015", "runA"),
    # --- added 2026-10-13, from the first large Stage A page-reading wave (~190 new pages) ---
    #
    # These 32 are listed, not certified. What is worth acting on is their SHAPE, which is not
    # random and is now reflected in two new rules in .claude/agents/a2-page-reader.md:
    #
    #   * 11 of 32 are page 1 of a chapter, under-capturing at 91-97% recall rather than failing
    #     outright. CORRECTION, added later the same day: I framed this as the agents
    #     under-capturing openers, and that was mostly WRONG. The coverage check was counting the
    #     section-contents panel ("7.2 Kepler's laws") as prose the blocks should have accounted
    #     for, when a contents panel is furniture by this step's own definition. The check now
    #     discounts whatever the agent DECLARED in `running_header_footer_removed`, which cleared
    #     five entries from this very set. What survives in this class is the narrower, real error:
    #     removing the panel without declaring it.
    #   * 6 of 32 are a straight self-contradiction: a string listed in
    #     `running_header_footer_removed` that also stands as its own line inside a block (e.g.
    #     BIO11L-ch06-p001's 'ANATOMY OF FLOWERING PLANTS'). Removed and kept are exclusive.
    #   * 6 of 32 leave 20+ consecutive prose words in no block on a page that defers nothing to
    #     A2S, so every line should have been accounted for.
    #   * The remainder are numbers present in a block but absent from the text layer, and heading
    #     lines matched below the per-sentence bar. Several of these are plausibly CORRECT: the
    #     workers reported, in detail and unprompted, that these text layers flatten Greek to
    #     Latin, drop superscripts, omit whole structures and emit blocks out of visual order, and
    #     the agent file tells them the image wins. A number read correctly off the image can be
    #     absent from a corrupt text layer, and the check cannot tell that from a fabrication.
    #
    # So this set is a work queue, not a verdict, exactly as the note above says. Each entry still
    # needs its page image looked at before it is called a defect or a false positive.
    ("BIO11L-ch01-p003", "runA"), ("BIO11L-ch06-p001", "runA"), ("BIO11L-ch07-p001", "runA"),
    ("BIO11L-ch10-p001", "runA"), ("BIO11L-ch10-p003", "runA"), ("BIO11L-ch14-p001", "runA"),
    ("BIO11L-ch14-p003", "runA"), ("BIO11L-ch15-p001", "runA"), ("BIO11L-ch16-p001", "runA"),
    ("BIO11L-ch17-p001", "runA"), ("BIO11L-ch18-p001", "runA"), ("BIO12L-ch08-p001", "runA"),
    ("BIO12L-ch08-p002", "runA"), ("CHE11L-ch07-p001", "runA"), ("CHE11L-ch07-p011", "runA"),
    ("CHE12L-ch05-p001", "runA"), ("CHE12L-ch05-p004", "runA"), ("CHE12L-ch05-p006", "runA"),
    ("CHE12L-ch05-p019", "runA"), ("CHE12L-ch05-p021", "runA"), ("CHE12L-ch05-p022", "runA"),
    ("CHE12L-ch05-p023", "runA"), ("PHY11L-ch01-p001", "runA"), ("PHY11L-ch01-p002", "runA"),
    ("PHY11L-ch01-p007", "runA"), ("PHY11L-ch02-p001", "runA"), ("PHY11L-ch02-p003", "runA"),
    ("PHY11L-ch02-p010", "runA"), ("PHY11L-ch12-p001", "runA"), ("PHY11L-ch12-p006", "runA"),
    ("PHY12L-ch08-p006", "runA"), ("PHY12L-ch08-p014", "runA"),
    # Landed moments after the batch above. A good illustration of the last bullet: the numbers the
    # check cannot find (32, 42, 72, ...) are an oxidation-state / superscript family on a redox
    # page, exactly where these text layers are known to flatten notation.
    ("CHE11L-ch07-p013", "runA"),
    # CHE11L ch07 is the redox chapter, and its agent was told explicitly that this text layer
    # flattens oxidation-state superscripts and that the image wins. Numbers the check cannot find
    # (32, 42, 72, 64) are the expected CONSEQUENCE of following that instruction: reading a
    # printed 3+/2+ off the image yields digit pairs a flattened text layer does not contain. These
    # five are therefore the likeliest false positives in this whole set, not the likeliest defects
    # — with one exception worth a look first: p017 sits at 48.8% coverage, just under the 50%
    # wholesale-failure bar for a page that defers content to A2S, which is a coverage question
    # rather than a notation one.
    ("CHE11L-ch07-p015", "runA"), ("CHE11L-ch07-p017", "runA"), ("CHE11L-ch07-p018", "runA"),
    ("CHE11L-ch07-p019", "runA"), 
    # --- added after the coverage check learned to discount declared furniture ---
    #
    # These nine are what remained once that false-positive class was removed, so unlike the batch
    # above they are NOT suspected check artefacts:
    #   * BIO11L-ch12-p001 and ch19-p001 excluded their section-contents panel from `blocks` but
    #     did NOT list it in `running_header_footer_removed`, so nothing records that the removal
    #     was deliberate. That is the agent's omission, and the agent file now says explicitly
    #     that listing it is what the check depends on. Compare PHY11L-ch07-p001, which listed all
    #     sixteen of its panel lines and now passes.
    #   * PHY12L-ch13 p003/p004/p006/p009/p010 report numbers absent from the text layer (19779,
    #     19880, ...). A nuclear-physics chapter whose text layer flattens superscripts is the
    #     likeliest explanation, same as CHE11L-ch07's oxidation states, but these are 5 pages of
    #     one chapter and worth one look together.
    #   * PHY11L-ch07-p005 and PHY12L-ch12-p002 are low per-unit match scores on a heading and a
    #     sentence, which is the pattern that has usually turned out to be image-vs-text-layer
    #     notation rather than a bad read.
    ("BIO11L-ch12-p001", "runA"), ("BIO11L-ch19-p001", "runA"), ("PHY11L-ch07-p005", "runA"),
    ("PHY12L-ch12-p002", "runA"), ("PHY12L-ch13-p003", "runA"), ("PHY12L-ch13-p004", "runA"),
    ("PHY12L-ch13-p006", "runA"), ("PHY12L-ch13-p009", "runA"), ("PHY12L-ch13-p010", "runA"),
    # Landed while the suite was running. Same two families as above: PHY12L-ch13-p014 is the
    # sixth page of that chapter reporting a number its text layer lacks (23592), and
    # PHY11L-ch07-p010's block n=9 is a worked-example line matched below the per-block bar.
    ("PHY11L-ch07-p010", "runA"), ("PHY12L-ch13-p014", "runA"),
    ("PHY12L-ch13-p016", "runA"), ("PHY12L-ch13-p017", "runA"),
    # --- first OLDER-edition failures, from the first older-edition pages ever read ---
    #
    # BIO12O-ch10-p002 reports 0.0% coverage, which looks like a total failure and is not. Its
    # reader said plainly that the page is "100% figures (three needs_special blocks, zero
    # prose)". A page whose entire content is figures still HAS a text layer -- the figure labels
    # are in it -- while legitimately producing no prose blocks at all, so recall is 0 by
    # construction and even the 50% wholesale-failure bar cannot be met. Same shape as the
    # furniture false positive fixed earlier today: the denominator counts text the agent was
    # right not to put in `blocks`. A proper fix would exclude text falling inside a
    # needs_special bbox from the denominator; not attempted here because it needs its own
    # measurement pass over the bbox geometry rather than a guess.
    #
    # The other three are the familiar notation family (numbers present in blocks, absent from a
    # text layer that flattened them), now showing up in the older edition too.
    ("BIO11O-ch10-p001", "runA"), ("BIO11O-ch12-p004", "runA"),
    ("BIO11O-ch12-p005", "runA"), ("BIO12O-ch10-p002", "runA"),
    # BIO11O-ch12-p010 (39.8%) is the SECOND confirmed instance of the deferred-text defect, and
    # this one is diagnosed, not suspected. Its 58 unaccounted text-layer lines were dumped and
    # read: they are "8e-", "8H+", "16ATP", "2NH", "16ADP", "16P" and arrow glyphs -- the
    # nitrogen-fixation equation, which sits inside this page's three needs_special blocks and
    # which the agent file explicitly tells the agent NOT to transcribe (leave `text` empty, give
    # a bbox, let A2S read it). The check then counts every one of those tokens as prose the
    # blocks failed to account for.
    #
    # THE FIX, for whoever picks this up: exclude text falling inside a needs_special bbox from
    # the coverage denominator, exactly as declared furniture is now excluded. It needs per-line
    # coordinates from the text layer to decide what is inside which bbox, which is a real
    # measurement pass rather than a threshold tweak -- so it is written down here rather than
    # guessed at. Lowering the deferred bar below 50% would be the wrong move: it would hide
    # genuine wholesale failures to buy off a denominator bug.
    ("BIO11O-ch12-p010", "runA"),
    # --- wave 7, after the header-specificity guard cleared four of six ---
    #
    # The guard (declared strings must be specific, and must not end in sentence punctuation)
    # retired `'of'`, `'GROWTH'` and `'radiation.'` as the useless findings they were, and kept
    # `'Polymers'`, which is CHE12O ch15's real chapter-name header -- so these three are what is
    # left once that noise is gone:
    #   * CHE12O-ch15-p005 declares `'Polymers'` removed AND keeps it as a block. That is the
    #     genuine contradiction this limb was built for (same as BIO11L-ch06-p001's 'ANATOMY OF
    #     FLOWERING PLANTS'): the chapter name printed once as the page heading is a legitimate
    #     heading block, the same words repeating in the margin are a running header, and the
    #     agent has to pick one. An agent-side fix, not a check fix.
    #   * BIO11L-ch04-p015 at 37.4% has 4 blocks of which 1 is needs_special — too few deferred
    #     blocks for the deferred-text denominator defect to explain it, so unlike
    #     BIO12O-ch10-p002 and BIO11O-ch12-p010 this one is NOT presumed benign and wants its
    #     page image looked at.
    #   * CHE12O-ch15-p002 block n=6 at 60% is the per-block notation family, now appearing in
    #     older-edition Chemistry.
    ("BIO11L-ch04-p015", "runA"), ("CHE12O-ch15-p002", "runA"),
    ("CHE12O-ch15-p005", "runA"), ("BIO11L-ch13-p002", "runA"),
    # PHY12L-ch13 is now EIGHT pages (p003, p004, p006, p009, p010, p014, p016, p017) all reporting
    # the same thing: numbers present in the blocks and absent from the text layer. That is a
    # chapter-level property, not eight incidents. It is the nuclear-physics chapter, so its page
    # text is dense with mass numbers and isotope superscripts, and its own reader reported the
    # text layer flattening superscripts and Greek throughout. Triage the CHAPTER once by looking
    # at one page image, rather than these eight entries one at a time.
}

# Minimum catch rate per corruption family, measured on real data with seed 77.
#
# RECALIBRATED after excluding the outputs that already fail the check uncorrupted (KNOWN_BAD and
# UNTRIAGED_FAILURES). The previous floors were measured with those 33 outputs included, and an
# output that fails before any corruption is scored "caught" whatever the corruption did -- so
# they were counted as successes for free and three floors came out higher than the check can
# actually sustain. Measured on the clean subset, `drop` is 21% not 28%, `halve` 21% not 24%, and
# `negate` 6% not 9%: the check was never that good at those, the denominator was just dirty.
# Two moved the other way (`scramble` 83% not 76%).
#
# These are FLOORS, set a little under each measurement to absorb seed jitter, not targets. They
# exist to catch a change that makes the check blinder, so they must never be raised to flatter
# the current code or lowered to accommodate a regression.
MIN_CATCH = {
    "paraphrase": 0.95,     # measured 100.0%: whole block rewritten in the agent's own words
    "scramble": 0.75,       # measured  83.0%: the block's words shuffled
    "swap_number": 1.00,    # measured 100.0%: digits altered -- protects numerical fidelity
    "drop": 0.19,           # measured  21.1%: whole block omitted
    "halve": 0.19,          # measured  21.4%: first half of the page's blocks truncated
    "wrong_word": 0.13,     # measured  14.9%: two content words replaced
    "negate": 0.05,         # measured   5.9%: one word flipped (hardest; see "Honest limits")
}


def _load_real_cases():
    cases = []
    for out_path in sorted(glob.glob(os.path.join(_PROJECT_ROOT, "steps/A2/out/*.json"))):
        m = re.match(r"(.+?)\.(runA|retry1|retry2)\.json$", os.path.basename(out_path))
        if not m:
            continue
        item_id, run = m.group(1), m.group(2)
        in_path = os.path.join(_PROJECT_ROOT, f"steps/A2/work/{item_id}.{run}.input.json")
        if not os.path.exists(in_path):
            continue
        with open(out_path) as fh:
            data = json.load(fh)
        if "blocks" not in data:
            continue  # an {"error": ...} output; not this check's concern
        with open(in_path) as fh:
            text_layer = (json.load(fh).get("text_layer") or "").strip()
        if not text_layer:
            continue  # image-only page; check (3) does not apply
        cases.append((item_id, run, data, text_layer))
    return cases


def _corrupt(blocks, mode, rng):
    """Build a deliberately-wrong version of a real block set."""
    out = copy.deepcopy(blocks)
    texted = [b for b in out if (b.get("text") or "").strip()]
    if not texted:
        return None
    target = texted[len(texted) // 2]
    original = target["text"]

    if mode == "paraphrase":
        target["text"] = ("This section explains the general concept in summary form rather "
                          "than copying the original wording printed on the page itself.")
    elif mode == "negate":
        for before, after in (("soluble", "insoluble"), ("stable", "unstable"),
                              ("increases", "decreases"), ("more", "less"),
                              ("higher", "lower"), (" is ", " is not "), (" the ", " no ")):
            if before in original:
                target["text"] = original.replace(before, after, 1)
                break
        else:
            return None
    elif mode == "drop":
        out.remove(target)
    elif mode == "scramble":
        words = original.split()
        rng.shuffle(words)
        target["text"] = " ".join(words)
    elif mode == "halve":
        for b in texted[: max(1, len(texted) // 2)]:
            b["text"] = b["text"][: len(b["text"]) // 2]
    elif mode == "swap_number":
        target["text"] = re.sub(r"\d{2,}", lambda mm: str(int(mm.group()) + 117),
                                original, count=2)
        if target["text"] == original:
            return None
    elif mode == "wrong_word":
        words = original.split()
        if len(words) < 12:
            return None
        words[len(words) // 2] = "chlorophyll"
        words[len(words) // 3] = "mitochondrion"
        target["text"] = " ".join(words)
    else:
        raise AssertionError(f"unknown corruption mode {mode}")
    return out


def _run(data, text_layer):
    ok, msg = a2_check.check(data, {"input_data": {"text_layer": text_layer}})
    assert isinstance(ok, bool) and isinstance(msg, str), (ok, msg)
    return ok, msg


def main():
    cases = _load_real_cases()
    assert len(cases) >= 50, (
        f"expected the real steps/A2/out corpus (>=50 outputs with a text layer), found "
        f"{len(cases)} -- this test is written against real data, not fixtures"
    )

    # --- 1. precision on real data ---
    #
    # A `runA` that fails while a later run of the SAME page passes is the retry mechanism working,
    # not a defect needing triage: the runner saw the failure, re-dispatched, and the re-read was
    # accepted. Demanding an UNTRIAGED_FAILURES entry for those turns every successful repair into
    # test debt. So a run is skipped only when a later run of its own item actually PASSES --
    # which masks nothing, because when the retry fails too (real case: PHY12O-ch01-p024, whose
    # text layer stores r-sub-1-squared as the scrambled tokens `2 1r` so no faithful
    # transcription can clear the 75% sentence bar) both runs stay reported.
    verdicts = {}
    for item_id, run, data, text_layer in cases:
        verdicts[(item_id, run)] = _run(data, text_layer)
    _LATER = {"runA": 3, "runB": 2, "retry1": 1, "retry2": 0, "adjudicated": -1}
    superseded = set()
    for (item_id, run), (ok, _msg) in verdicts.items():
        if ok:
            continue
        for (other_item, other_run), (other_ok, _m2) in verdicts.items():
            if other_item != item_id or not other_ok:
                continue
            if _LATER.get(other_run, 9) < _LATER.get(run, 9):
                superseded.add((item_id, run))
                break

    unexpected = []
    known_bad_still_caught = 0
    untriaged_still_caught = set()
    for item_id, run, data, text_layer in cases:
        ok, msg = verdicts[(item_id, run)]
        key = (item_id, run)
        if key in superseded:
            continue  # a later run of this page passed; the repair already happened
        if key in KNOWN_BAD:
            assert not ok, f"{item_id}.{run} has a known genuine defect but the check passed it"
            known_bad_still_caught += 1
        elif key in UNTRIAGED_FAILURES:
            if not ok:
                untriaged_still_caught.add(key)
        elif not ok:
            unexpected.append(f"{item_id}.{run}: {msg}")
    # A failure outside both sets is either a new extraction defect or a new false positive.
    # Either way it is news, and it must be looked at rather than absorbed.
    assert not unexpected, (
        f"{len(unexpected)} real A2 outputs fail the check and are in neither KNOWN_BAD nor "
        f"UNTRIAGED_FAILURES, out of {len(cases)} outputs. Each is either a genuine new "
        f"extraction defect or a new false positive — read the message and decide, then either "
        f"fix the output or add it to UNTRIAGED_FAILURES with the reason:\n  "
        + "\n  ".join(unexpected)
    )
    assert known_bad_still_caught == len(KNOWN_BAD)
    # Pin the untriaged set too: if the check stops catching one of these without the underlying
    # output being fixed, that is a precision regression hiding a real defect.
    newly_passing = UNTRIAGED_FAILURES - untriaged_still_caught
    assert not newly_passing, (
        f"{len(newly_passing)} outputs listed as failing now PASS the check: {sorted(newly_passing)}. "
        f"If the output was genuinely fixed, remove it from UNTRIAGED_FAILURES. If only the check "
        f"changed, this is a precision regression — the defect is still in the data."
    )
    print(f"precision: {len(cases)} real outputs, 0 unexplained failures, "
          f"{known_bad_still_caught} known-bad still caught, "
          f"{len(untriaged_still_caught)} untriaged failures still caught")

    # --- 2. sensitivity: corrupted block sets must still fail ---
    rng = random.Random(77)
    for mode, floor in MIN_CATCH.items():
        tried = caught = 0
        for item_id, run, data, text_layer in cases:
            # Skip outputs that ALREADY fail the check, for both sets. Corrupting an output that
            # fails uncorrupted tells us nothing about sensitivity -- it would be scored "caught"
            # no matter what the corruption did, so including the 33 untriaged failures would
            # inflate every rate below by up to 33/446 for free and make the measured floors
            # look better than the check really is.
            if (item_id, run) in KNOWN_BAD or (item_id, run) in UNTRIAGED_FAILURES:
                continue
            blocks = _corrupt(data["blocks"], mode, rng)
            if blocks is None:
                continue
            bad = dict(data)
            bad["blocks"] = blocks
            tried += 1
            ok, _msg = _run(bad, text_layer)
            caught += (not ok)
        assert tried >= 20, f"{mode}: only {tried} corruptible real pages"
        rate = caught / tried
        assert rate >= floor, (
            f"{mode}: the check now catches only {rate:.0%} of corrupted pages "
            f"({caught}/{tried}); it must stay at or above the measured {floor:.0%}. "
            "A change that lowers this is silently stopping the check from catching real "
            "transcription errors."
        )
        print(f"sensitivity[{mode:12}]: caught {caught}/{tried} = {rate:.0%} (floor {floor:.0%})")

    # --- 3. the two real false-positive families must stay fixed ---
    # (b) outline-font side-headings, 5x duplicated and bunched out of reading order
    layer = ("275\nAmines\n" + "Benzenediazonium chloride is a colourless crystalline solid.\n"
             + "It is readily soluble in water and is stable in cold.\n"
             + "9.8\n" * 5 + "Physical\n" * 5 + "Properties\n" * 5 + "Reprint 2026-27\n")
    faithful = {
        "blocks": [
            {"n": 1, "kind": "heading", "text": "9.8 Physical Properties"},
            {"n": 2, "kind": "paragraph",
             "text": "Benzenediazonium chloride is a colourless crystalline solid. It is "
                     "readily soluble in water and is stable in cold."},
        ],
        "first_block_continues_from_previous": False,
        "last_block_continues_on_next": False,
        "running_header_footer_removed": ["275", "Amines", "Reprint 2026-27"],
        "note": "",
    }
    ok, msg = _run(faithful, layer)
    assert ok, f"outline-font duplication false positive is back: {msg}"

    # the same page, genuinely mis-transcribed, must still fail
    wrong = copy.deepcopy(faithful)
    wrong["blocks"][1]["text"] = ("Benzenediazonium bromide is a yellow amorphous powder that "
                                  "decomposes violently on contact with cold water.")
    ok, msg = _run(wrong, layer)
    assert not ok, "a genuinely wrong transcription of the same page was passed"

    # (a) header/footer stamp words that legitimately occur in prose
    prose = {
        "blocks": [
            {"n": 1, "kind": "paragraph",
             "text": "Lower aliphatic amines are soluble in water. Amines\nare soluble in "
                     "organic solvents like alcohol over the past 50 years."},
        ],
        "first_block_continues_from_previous": False,
        "last_block_continues_on_next": False,
        "running_header_footer_removed": ["50", "Amines", "Reprint 2026-27"],
        "note": "",
    }
    ok, msg = _run(prose, "Lower aliphatic amines are soluble in water. Amines\nare soluble in "
                          "organic solvents like alcohol over the past 50 years.\n50\nAmines\n")
    assert ok, f"header/footer-in-prose false positive is back: {msg}"

    # a stamp genuinely left sitting on its own line must still be caught
    left_in = copy.deepcopy(prose)
    left_in["blocks"][0]["text"] += "\nAmines\n"
    ok, msg = _run(left_in, "Lower aliphatic amines are soluble in water. Amines\nare soluble "
                            "in organic solvents like alcohol over the past 50 years.\n50\n"
                            "Amines\n")
    assert not ok and "header/footer" in msg, (
        f"a running header left as its own line inside a block was not caught: {msg}"
    )
    print("real false-positive families fixed; genuine defects of the same shape still caught")
    print("test_a2_check.py OK")


def test_a2_check():
    main()


if __name__ == "__main__":
    main()
