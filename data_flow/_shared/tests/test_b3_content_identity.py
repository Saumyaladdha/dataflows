#!/usr/bin/env python3
"""Two cross-item invariants on B3's extracted questions, added 2026-10-13.

Nothing in the pipeline looked across questions before this. Both invariants below were found by
hand while auditing the nine `B3_DUPLICATE_OPTIONS` flags, and both are mechanical, so they belong
in code rather than in a reviewer's lap.

**1. A question cannot appear twice in one booklet.** NTA prints each question once per booklet;
the same content at two question numbers in the same `paper_id` means the scrape served one
question's image twice, and the two records cannot both be right. Measured when this was written:
exactly one such pair exists, `NEET-2024-MAIN-Q1` q0001/q0014 (the logic-circuit truth table).
Both carry a collapsed truth table and scrambled Boolean options, and q0014 additionally has a
booklet-instruction preamble glued to its stem -- so the surrounding pages of that scrape are
disturbed too, which is why this is worth catching automatically rather than noting once.

**2. Cross-booklet matches must not vanish.** Booklet codes are shuffles of ONE question set, so
the same question legitimately appears under different numbers in different codes -- 66 such pairs
exist between 2023 E1 and E2. That agreement was never requested: two independent extraction runs
over two differently-ordered scans produced byte-identical stems, lists and options. It is
therefore free evidence that B3 transcribes reproducibly, and a drop in the count is a signal that
a B3 or crop change has destabilised transcription. Guarded loosely (a floor, not an equality)
because the count legitimately GROWS as more of 2023 E2 is extracted.

Why `stem_en` alone is not the key, since it is the obvious thing to reach for and it is wrong:
assertion-reason and match-the-list questions have a boilerplate stem and hold all their
discriminating content in `list_i`, `list_ii` and `statements`. Seventeen questions in 2024-Q1
share one byte-identical "Match List I with List II" stem. Keying on the stem reports 15
intra-booklet duplicates where there is 1.

Run: .venv/bin/python3 -m pytest tests/test_b3_content_identity.py -q
"""
import collections
import glob
import json
import os
import re

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_TESTS_DIR)
_OUT = os.path.join(_PROJECT_ROOT, "steps", "B3", "out")

# The one known-bad pair, kept explicit so a NEW duplicate fails the test while this one does not
# silently mask it. Remove the entry once the pair is adjudicated.
_KNOWN_INTRA_DUPES = {("NEET-2024-MAIN-Q1", ("q0001", "q0014"))}

_CROSS_BOOKLET_FLOOR = 60  # 66 measured 2026-10-13; a floor, since this count grows with coverage

_NAME_RE = re.compile(
    r"(NEET-\d{4}-[A-Z0-9]+-[A-Z0-9]+)-(q\d+)\.(runA|runB|retry1|retry2|adjudicated)\.json$")
_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}


def _norm(s):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).split())


def _content_key(d):
    """Everything a reader needs to tell two questions apart -- NOT just the stem."""
    parts = [_norm(d.get("stem_en"))]
    for field in ("list_i", "list_ii", "statements"):
        for entry in (d.get(field) or []):
            if isinstance(entry, dict):
                parts.append(_norm(entry.get("label")) + ":" + _norm(entry.get("text")))
    opts = d.get("options_en") or {}
    for k in sorted(opts):
        parts.append(_norm(opts[k]))
    return "|".join(parts)


def _best_outputs():
    """One record per (paper, question), preferring the most-settled run."""
    best = {}
    for path in glob.glob(os.path.join(_OUT, "*.json")):
        m = _NAME_RE.match(os.path.basename(path))
        if not m:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        key = (m.group(1), m.group(2))
        priority = _RUN_PRIORITY[m.group(3)]
        if key not in best or priority < best[key][0]:
            best[key] = (priority, data)
    return {k: v[1] for k, v in best.items()}


def test_no_unexpected_duplicate_question_within_one_booklet():
    records = _best_outputs()
    if not records:
        return
    groups = collections.defaultdict(lambda: collections.defaultdict(set))
    for (paper, q), data in records.items():
        key = _content_key(data)
        if len(key) < 60:  # too thin to compare; an unreadable or near-empty extraction
            continue
        groups[paper][key].add(q)

    found = {(paper, tuple(sorted(qs)))
             for paper, keys in groups.items() for qs in keys.values() if len(qs) > 1}
    unexpected = found - _KNOWN_INTRA_DUPES
    assert not unexpected, (
        "the same question content appears at two numbers in one booklet, which cannot happen in a "
        f"real paper: {sorted(unexpected)}")


def test_cross_booklet_content_matches_have_not_collapsed():
    """Booklet codes are shuffles of one question set, so these matches SHOULD exist."""
    records = _best_outputs()
    if len(records) < 400:  # not enough extracted yet for the floor to mean anything
        return
    by_key = collections.defaultdict(set)
    for (paper, q), data in records.items():
        key = _content_key(data)
        if len(key) < 60:
            continue
        by_key[key].add(paper)
    matches = sum(1 for papers in by_key.values() if len(papers) > 1)
    assert matches >= _CROSS_BOOKLET_FLOOR, (
        f"only {matches} questions match across booklet codes, below the floor of "
        f"{_CROSS_BOOKLET_FLOOR}. Booklet codes are shuffles of one question set, so this "
        "agreement is free corroboration that B3 transcribes reproducibly; a drop suggests a B3 "
        "prompt or crop change has destabilised transcription.")
