#!/usr/bin/env python3
"""Pins A2S's handling of `kind: "box"`, added 2026-10-13.

Why this test exists. SPEC 9/A2S names three kinds (table, figure, equation), but A2's kind enum
includes `box` and A2 agents legitimately mark a box needs_special when a worked example's display
equations would be lost to plain text extraction. Six such blocks are in the real corpus -- CHE12L
ch01 p005/p008/p016, CHE12L ch09 p005/p006, PHY11L ch06 p017 -- and four of them carry `text: ""`,
so their prose was never captured anywhere and the box cannot be quoted at all.

Before the fix the kind was simply undefined here, and five separate A2S workers each improvised:
two relabelled the box as `equation` (which discards the prose), three kept `box` and invented a
`text` field. The check's `else` branch would have rejected the latter three as "unknown kind".

The property that matters is the one asserted hardest below: a box MUST deliver `text`. A citation
is matched word-for-word against passage text by `quote_verify.find`, so a box returned with
`latex` alone looks complete to every downstream step and is still permanently uncitable -- the
exact failure mode this project cares most about.

Run: .venv/bin/python3 -m pytest tests/test_a2s_box.py -q
"""
import os
import sys

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_ROOT, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
from checks import A2S as a2s_check  # noqa: E402

_CTX = {"item_id": "CHE12L-ch01-p008-b3", "step": "A2S"}

_REAL_BOX_TEXT = (
    "Example 1.4 If N2 gas is bubbled through water at 293 K, how many millimoles of N2 gas "
    "would dissolve in 1 litre of water? Solution"
)


def _check(data):
    return a2s_check.check(data, _CTX)


def test_box_with_prose_passes():
    ok, msg = _check({"kind": "box", "number": "Example 1.4", "text": _REAL_BOX_TEXT,
                      "latex": "m = \\frac{p}{K_H}", "note": ""})
    assert ok, msg


def test_box_without_prose_fails():
    """The whole point: latex alone is not a transcription, because it cannot be quoted."""
    ok, msg = _check({"kind": "box", "text": "", "latex": "m = \\frac{p}{K_H}", "note": ""})
    assert not ok
    assert "quotable" in msg


def test_box_needs_no_latex():
    """PHY11L ch06 p017 b22 is a real box with no display equation; requiring latex would fail
    a correct transcription of it."""
    ok, msg = _check({"kind": "box", "text": _REAL_BOX_TEXT, "note": ""})
    assert ok, msg


def test_box_broken_latex_still_caught():
    ok, msg = _check({"kind": "box", "text": _REAL_BOX_TEXT,
                      "latex": "m = \\frac{p}{K_H", "note": ""})
    assert not ok
    assert "parse" in msg


def test_schema_requires_text_for_box():
    good = {"kind": "box", "text": _REAL_BOX_TEXT, "note": ""}
    bad = {"kind": "box", "latex": "x = 1", "note": ""}
    ok_good, err_good = rc.validate_schema("A2S", good)
    ok_bad, _ = rc.validate_schema("A2S", bad)
    assert ok_good, err_good
    assert not ok_bad, "schema accepted a box with no text"


def test_other_kinds_unaffected():
    ok, _ = _check({"kind": "equation", "latex": "R = \\rho \\frac{l}{A}",
                    "number": "(3.16)", "note": ""})
    assert ok
    ok, msg = _check({"kind": "sidebar", "note": ""})
    assert not ok and "unknown kind" in msg
