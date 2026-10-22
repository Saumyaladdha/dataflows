#!/usr/bin/env python3
"""Put the A2S AGENT's transcriptions of TABLES, EQUATIONS and FIGURES onto the elements.

    from join_agent_special import apply_agent_special
    stats = apply_agent_special(layout, "BIO11L-ch01")

The third joiner, after `join_agent_text` (words) and `join_agent_layout` (arrangement). A2S is
asked for the things a page's running text does not contain: the cells of a table, the LaTeX of
an equation, the content of a figure.

WHY THE AGENT BEATS THE GEOMETRY HERE, MEASURED
-------------------------------------------------
A table's columns CAN be rebuilt from span positions -- `_cell_grid` in
`extract_page_layout.py` does it, clustering the x of every span. On BIO11L ch01's Table 1.1
that recovers a 6 x 7 grid, which is the right shape. But it recovers it IMPERFECTLY:

    geometry grid   'Monocotyledona'     'Phylum/'  +  'Division'  as two header rows
    A2S             'Monocotyledonae'    'Phylum/ Division'        as one header cell

The truncation is not a bug in the clustering; it is the text layer cutting a word at a column
boundary, and no amount of geometry recovers a character that is not there. The agent read the
page image and transcribed what is printed.

So A2S wins for a table, and the geometry grid stays as the FALLBACK for the pages A2S has not
covered -- which is most of them: 1,014 A2S outputs exist corpus-wide against ~3,300 pages.

WHAT A2S RETURNS, BY KIND
---------------------------
    table      caption, header[], rows[][], repeated_header
    equation   latex
    figure     the figure's own text content and labels

Each file is named `<chapter>-p<page>-b<block>.<run>.json`, so it is matched on the PAGE and the
BLOCK NUMBER -- the same `n` A2 assigned, which `join_agent_text` has already written onto the
element as `a2_block_n`. That makes the match exact rather than positional; nothing is matched
by guessing which table on the page was meant.
"""

import glob
import json
import os
import re

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}
_NAME_RE = re.compile(r"-p(\d+)-b(\d+)\.(\w+)\.json$")


def a2s_files(chapter, steps_dir="steps"):
    """{(page, block): path} keeping the most-settled run for each block."""
    best = {}
    for path in glob.glob(os.path.join(steps_dir, "A2S", "out", f"{chapter}-p*-b*.json")):
        m = _NAME_RE.search(os.path.basename(path))
        if not m:
            continue
        key = (int(m.group(1)), int(m.group(2)))
        rank = _RUN_PRIORITY.get(m.group(3), 9)
        if key not in best or rank < best[key][0]:
            best[key] = (rank, path)
    return {k: v[1] for k, v in best.items()}


def apply_agent_special(layout, chapter, steps_dir="steps"):
    """Merge A2S transcriptions into `layout`, in place. Returns counts."""
    stats = {"files": 0, "tables": 0, "equations": 0, "figures": 0, "unmatched": 0}
    files = a2s_files(chapter, steps_dir)
    stats["files"] = len(files)
    if not files:
        layout["special_join"] = stats
        return stats

    for (page_no, block_n), path in sorted(files.items()):
        if page_no < 1 or page_no > len(layout["pages"]):
            stats["unmatched"] += 1
            continue
        page = layout["pages"][page_no - 1]
        try:
            with open(path, encoding="utf-8") as fh:
                sp = json.load(fh)
        except (OSError, json.JSONDecodeError):
            stats["unmatched"] += 1
            continue

        target = next((e for e in page["elements_in_reading_order"]
                       if e.get("a2_block_n") == block_n), None)
        if target is None:
            # The block may not have survived as its own element -- a table's caption is merged
            # with its rows, a figure's label is absorbed into the artwork. Fall back to the
            # element of the right KIND on that page, which is unambiguous when there is one.
            kind = (sp.get("kind") or "").lower()
            want = {"table": "table", "equation": "paragraph", "figure": "figure"}.get(kind)
            cands = [e for e in page["elements_in_reading_order"] if e["role"] == want]
            target = cands[0] if len(cands) == 1 else None
        if target is None:
            stats["unmatched"] += 1
            continue

        kind = (sp.get("kind") or "").lower()
        if kind == "table":
            header = sp.get("header") or []
            rows = sp.get("rows") or []
            if header or rows:
                target["role"] = "table"
                # The AGENT's grid replaces the geometry one. The geometry grid is kept beside
                # it so a reviewer can see both, and so a later check can flag a disagreement
                # instead of silently preferring one.
                if target.get("table_grid"):
                    target["table_grid_measured"] = target["table_grid"]
                target["table_grid"] = {
                    "rows": len(rows) + (1 if header else 0),
                    "cols": max([len(header)] + [len(r) for r in rows] or [0]),
                    "cells": ([header] if header else []) + rows,
                    "repeated_header": sp.get("repeated_header", False),
                    "source": "a2s-agent",
                }
                if sp.get("caption"):
                    target["table_caption"] = sp["caption"]
                target["special_source"] = "a2s-agent"
                stats["tables"] += 1
        elif kind == "equation" and sp.get("latex"):
            target["latex"] = sp["latex"]
            target["special_source"] = "a2s-agent"
            stats["equations"] += 1
        elif kind == "figure":
            for k in ("caption", "labels", "description"):
                if sp.get(k):
                    target[f"figure_{k}"] = sp[k]
            target["special_source"] = "a2s-agent"
            stats["figures"] += 1

    layout["special_join"] = stats
    return stats
