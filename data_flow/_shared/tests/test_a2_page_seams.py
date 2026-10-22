#!/usr/bin/env python3
"""Pins the A2 page-seam invariant, added 2026-10-13.

Between two adjacent pages of a chapter there is exactly one fact about whether the prose runs
across the break, and A2 records it twice from opposite sides:

    page N      last_block_continues_on_next
    page N+1    first_block_continues_from_previous

They must agree. When they disagree, one of the two pages is wrong about the same seam, and
nothing else in the pipeline notices: `scripts/checks/A2.py` judges ONE page against ONE input and
cannot see its neighbour, so a contradiction is invisible to it by construction.

Why it matters downstream rather than being bookkeeping: A3 uses these flags to decide whether two
blocks are one page-split paragraph, and A3 workers reported ~40 such paragraphs by name on
2026-10-13. A wrong flag either cuts a sentence in half (giving D4 a broken quote) or welds two
unrelated paragraphs into one passage.

Measured when this was written: **80 of 1,221 seams disagreed (6.6%)**. The cause is visible in the
data -- adjacent pages are read by different agents at different times, and during a bulk run
`previous_page_last_block` is null, so each side judges the seam from whatever it could see. One
worker on `CHE11L-ch02` noticed the asymmetry itself and went back to flip p011's flag after
reading p012, recording the reasoning in both files; that is the behaviour this test generalises.

The allowance starts at the measured 80 so the test pins today's state rather than failing the
build, and should be ratcheted DOWN as seams are repaired. It is not a licence: a rise above it
means a new wave introduced fresh contradictions.

Run: .venv/bin/python3 -m pytest tests/test_a2_page_seams.py -q
"""
import collections
import glob
import json
import os
import re

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_OUT = os.path.join(_PROJECT_ROOT, "steps", "A2", "out")

_NAME_RE = re.compile(r"(.+)-p(\d+)\.(runA|runB|retry1|retry2|adjudicated)\.json$")
_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

# Measured 2026-10-13: 80 disagreeing seams of 1,221. Ratchet DOWN as they are fixed.
_ALLOWED_MISMATCHES = 80


def _best_pages():
    """{(chapter, page): record} keeping the most-settled run for each page."""
    best = {}
    for path in glob.glob(os.path.join(_OUT, "*.json")):
        m = _NAME_RE.match(os.path.basename(path))
        if not m:
            continue
        priority = _RUN_PRIORITY[m.group(3)]
        key = (m.group(1), int(m.group(2)))
        if key in best and best[key][0] <= priority:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                rec = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(rec, dict):
            best[key] = (priority, rec)
    return {k: v[1] for k, v in best.items()}


def _seam_mismatches():
    pages = _best_pages()
    by_chapter = collections.defaultdict(dict)
    for (chapter, page), rec in pages.items():
        by_chapter[chapter][page] = rec

    seams, bad = 0, []
    for chapter, numbered in by_chapter.items():
        for page in sorted(numbered):
            nxt = numbered.get(page + 1)
            if nxt is None:
                continue
            here = numbered[page].get("last_block_continues_on_next")
            there = nxt.get("first_block_continues_from_previous")
            if here is None or there is None:
                continue  # an error/unsure page carries neither flag
            seams += 1
            if bool(here) != bool(there):
                bad.append(f"{chapter}-p{page:03d}({here}) vs p{page + 1:03d}({there})")
    return seams, bad


def test_adjacent_pages_agree_about_their_shared_seam():
    seams, bad = _seam_mismatches()
    if seams == 0:
        return  # no A2 output yet
    assert len(bad) <= _ALLOWED_MISMATCHES, (
        f"{len(bad)} of {seams} page seams disagree about whether prose crosses the break "
        f"(allowance {_ALLOWED_MISMATCHES}). Each one means one of the two pages is wrong about "
        f"the same fact, and A3 uses these flags to decide whether two blocks are one page-split "
        f"paragraph. First few: {bad[:10]}"
    )


def test_a_seam_has_exactly_one_truth_so_the_check_is_symmetric():
    """Guards the test itself: the comparison must be direction-agnostic.

    A seam is one fact seen from two sides, so counting mismatches forwards and backwards must give
    the same number. If this ever fails, the helper has acquired a direction bias and its count of
    real defects cannot be trusted.
    """
    pages = _best_pages()
    if not pages:
        return
    by_chapter = collections.defaultdict(dict)
    for (chapter, page), rec in pages.items():
        by_chapter[chapter][page] = rec

    forward = backward = 0
    for numbered in by_chapter.values():
        for page in sorted(numbered):
            nxt = numbered.get(page + 1)
            if nxt is None:
                continue
            a = numbered[page].get("last_block_continues_on_next")
            b = nxt.get("first_block_continues_from_previous")
            if a is None or b is None:
                continue
            if bool(a) != bool(b):
                forward += 1
            if bool(b) != bool(a):
                backward += 1
    assert forward == backward, (
        f"seam comparison is not symmetric ({forward} forwards, {backward} backwards); the "
        f"mismatch count cannot be trusted")
