#!/usr/bin/env python3
"""Join a2b-bold-marker and a2i-italic-marker onto the page's runs.

    from join_agent_marks import join
    stats = join(layout, "BIO12L-ch01")

WHY THIS FILE HAD TO EXIST
--------------------------
It did not, and that was the bug. There were joiners for A2 (text), A2L (layout), A2S
(special) and A2C (structure) -- and none for A2B and A2I. Eighteen result files sat in
`steps/A2B/out/` and `steps/A2I/out/`, correct and complete, and nothing in the pipeline read
them. Class 12 Chapter 1's Markdown therefore carried ZERO bold marks across 45,000 characters
while the agents had already identified every one of them.

The agents noticed before the pipeline did. Several A2I runs reported, unprompted, that their
input's `bold_terms` arrived empty for a block whose image plainly showed eight bold terms --
"that is an A2B gap, not an A2I one". They were describing this missing joiner from the other
side of it.

ON A SCAN THESE AGENTS ARE THE ONLY SOURCE OF EMPHASIS
------------------------------------------------------
A born-digital page carries font flags, so bold and italic come free. A scan carries none: the
only record that `syngamy` is bold or that `Hibiscus` is italic is an agent having looked at
the page. Dropping that on the floor loses it permanently.

HOW A TERM BECOMES A MARK
-------------------------
Each agent reports terms as plain strings per block. A term is located in the block's text and
the run carrying it is split so the term -- and only the term -- takes the flag. Matching is
IN ORDER and non-overlapping, which matters: a2b-bold-marker warned that on page 8 the phrase
`the stigma, style and ovary` is bold AND `stigma` and `ovary` are each bold again later, so a
naive first-match for `stigma` lands inside the earlier phrase and marks the wrong characters.
Longer terms are placed first and their spans excluded, so each later term finds its own.
"""

import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load(step, item_id):
    """{page_file: {block_n: [terms]}} for one step."""
    key = "bold_terms" if step == "A2B" else "italic_terms"
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", step, "out",
                                              f"{item_id}-p*.json"))):
        pf = os.path.basename(path).split("-p")[-1].split(".")[0]
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:                                      # noqa: BLE001
            continue
        per = {}
        for blk in data.get("blocks") or []:
            terms = [t for t in (blk.get(key) or []) if isinstance(t, str) and t.strip()]
            if terms and blk.get("n") is not None:
                per[int(blk["n"])] = terms
        if per:
            out[pf] = per
    return out


def _spans(text, terms):
    """[(start, end)] for each term, in order, never overlapping an earlier one.

    Longest first, because a short term is frequently a substring of a longer bold phrase on
    the same page and would otherwise steal its position.
    """
    taken, found = [], []
    for term in sorted(terms, key=len, reverse=True):
        t = re.sub(r"\s+", " ", term).strip()
        if not t:
            continue
        for m in re.finditer(re.escape(t), text):
            if all(m.end() <= s or m.start() >= e for s, e in taken):
                taken.append((m.start(), m.end()))
                found.append((m.start(), m.end()))
                break
    return sorted(found)


def _apply(el, spans, flag):
    """Split the element's runs so exactly `spans` carry `flag`."""
    runs = el.get("runs") or []
    if not runs or not spans:
        return 0
    text = "".join(r.get("t", "") for r in runs)
    marks = [False] * len(text)
    for s, e in spans:
        for i in range(max(0, s), min(len(text), e)):
            marks[i] = True
    base = dict(runs[0])
    base.pop("t", None)
    new, pos = [], 0
    for r in runs:
        t = r.get("t", "")
        if not t:
            continue
        i = 0
        while i < len(t):
            on = marks[pos + i] if pos + i < len(marks) else False
            j = i
            while j < len(t) and pos + j < len(marks) and marks[pos + j] == on:
                j += 1
            piece = dict(r)
            piece["t"] = t[i:j]
            if on:
                piece[flag] = True
            new.append(piece)
            i = j
        pos += len(t)
    el["runs"] = [r for r in new if r.get("t")]
    return len(spans)


def join(layout, item_id):
    """Apply A2B and A2I to `layout` in place. Returns a stats dict."""
    bold, italic = _load("A2B", item_id), _load("A2I", item_id)
    stats = {"pages": len(layout.get("pages") or []), "pages_with_agent": 0,
             "bold_marks": 0, "italic_marks": 0, "unmatched": 0}
    for page in layout.get("pages") or []:
        pf = page.get("page_file")
        b_map, i_map = bold.get(pf) or {}, italic.get(pf) or {}
        if not b_map and not i_map:
            continue
        stats["pages_with_agent"] += 1
        for el in page.get("elements_in_reading_order") or []:
            # `a2_block_n` is what join_agent_text records when it places an agent block.
            n = el.get("a2_block_n")
            if n is None:
                continue
            text = "".join(r.get("t", "") for r in (el.get("runs") or []))
            if not text.strip():
                continue
            for src, flag, key in ((b_map, "b", "bold_marks"),
                                   (i_map, "i", "italic_marks")):
                terms = src.get(int(n))
                if not terms:
                    continue
                spans = _spans(text, terms)
                stats["unmatched"] += len(terms) - len(spans)
                stats[key] += _apply(el, spans, flag)
    layout["marks_join"] = stats
    return stats
