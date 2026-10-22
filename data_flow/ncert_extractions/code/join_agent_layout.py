#!/usr/bin/env python3
"""Put the A2L AGENT's measured LAYOUT onto the extracted elements.

    from join_agent_layout import apply_agent_layout
    stats = apply_agent_layout(layout, "BIO11L-ch02")

The twin of `join_agent_text.py`. That one brings the agent's WORDS; this one brings the
agent's ARRANGEMENT -- which column an element sits in, how it is aligned, what face it is set
in, and the colours of the bands and panels the page prints.

WHY THIS IS NEEDED AT ALL, GIVEN THE PDF IS MEASURED EXACTLY
--------------------------------------------------------------
`extract_page_layout.py` reads the text layer, so for a TEXT element it already knows the bbox
to a tenth of a point, the font name, the size and the colour -- better than any agent looking
at a picture. What it cannot know is everything that is not text:

  * WHICH COLUMN an element belongs to. The extractor clusters x-positions, which is a guess.
    A2L is asked to decide the page's columns FIRST and then place elements in them, which is
    the judgement the clustering is standing in for. Measured consequence: on BIO11L ch02 every
    figure was placed by a bbox heuristic and came out 9 right, 1 left and 0 full-width -- the
    book prints several across the full measure.

  * THE FILLS. The caption band under a figure (`#fef2e2`), the rule bar across the head of a
    page (`#4c7435`), the contents panel on an opener (`#ffe5ca`), a table's header row -- all
    of these are VECTOR drawings. They do not appear in the text layer at all, so the only way
    the renderer has had them so far is a hard-coded per-book table, which is right for the one
    book it was sampled from and generalises to nothing.

  * ALIGNMENT AND FACE. `justify` vs `center` vs `left`, and serif vs sans vs serif-italic. The
    extractor has the font NAME but not the designer's intent for a caption or a panel.

  * PAGES WITH NO TEXT LAYER. 12% of the corpus. There the extractor has nothing and A2L is the
    only source of layout there will ever be.

So: the PDF owns the precise box of a text element; A2L owns the arrangement. Where they
disagree about a box, the PDF wins -- an agent's bbox read off an image is an estimate, and
overriding an exact measurement with an estimate makes the render worse, not better.

HOW THEY ARE MATCHED
----------------------
A2L reports `n` for elements it could tie to a numbered block and `null` for furniture it saw
on the page but that has no block. Numbered elements are matched on `n`; everything else is
matched by BOX OVERLAP, so a rule bar or a caption band finds the extracted element it covers.
Anything that matches nothing is carried through as a NEW furniture element -- that is the
whole point for fills, which the extractor never had.

Every element records `layout_source`, so a page cannot claim an arrangement it was never
measured for.
"""

import glob
import json
import os

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

# Roles A2L reports that are page FURNITURE -- they carry the fills the renderer needs and
# must never become readable content.
_FURNITURE_ROLES = {"chapter_banner", "rule_bar", "page_header_band", "footer_rule",
                    "decorative_image", "qr_code", "page_number", "running_header"}

# What A2L calls a thing -> what the extractor calls it, where they differ.
_ROLE_ALIAS = {"major_heading": "section_heading", "marginal_note": "side_note",
               "contents_panel": "contents_entry", "table_caption": "figure_caption",
               "epigraph": "side_note"}


def best_a2l_path(chapter, page_num, steps_dir="steps"):
    cands = glob.glob(os.path.join(steps_dir, "A2L", "out",
                                   f"{chapter}-p{page_num:03d}.*.json"))
    if not cands:
        return None
    return sorted(cands, key=lambda p: _RUN_PRIORITY.get(
        os.path.basename(p).split(".")[-2], 9))[0]


def _iou(a, b):
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    ix0, iy0 = max(ax0, bx0), max(ay0, by0)
    ix1, iy1 = min(ax1, bx1), min(ay1, by1)
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    inter = (ix1 - ix0) * (iy1 - iy0)
    ua = (ax1 - ax0) * (ay1 - ay0) + (bx1 - bx0) * (by1 - by0) - inter
    return inter / ua if ua > 0 else 0.0


def apply_agent_layout(layout, chapter, steps_dir="steps", min_iou=0.30):
    """Merge A2L's arrangement into `layout`, in place. Returns counts, never a claim."""
    stats = {"pages": 0, "pages_with_agent": 0, "elements_enriched": 0,
             "furniture_added": 0, "pages_missing": []}
    for pi, page in enumerate(layout["pages"], 1):
        stats["pages"] += 1
        path = best_a2l_path(chapter, pi, steps_dir)
        els = page["elements_in_reading_order"]
        if not path:
            stats["pages_missing"].append(page.get("printed_page_number") or pi)
            page["layout_source"] = "measured (NO A2L READ)"
            for e in els:
                e.setdefault("layout_source", "measured")
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                a2l = json.load(fh)
        except (OSError, json.JSONDecodeError):
            page["layout_source"] = "measured (A2L unreadable)"
            continue

        stats["pages_with_agent"] += 1
        page["layout_source"] = "a2l-agent"
        page["a2l_run"] = os.path.basename(path)
        # The page's REAL columns, decided by the agent rather than clustered from x-positions.
        cols = (a2l.get("page") or {}).get("columns") or []
        if cols:
            page["layout_columns"] = cols

        by_n = {e.get("a2_block_n"): e for e in els if e.get("a2_block_n") is not None}
        used = set()
        for ae in a2l.get("elements") or []:
            abox = ae.get("bbox")
            target = None
            n = ae.get("n")
            if n is not None and n in by_n:
                target = by_n[n]
            elif abox:
                best, best_i = None, 0.0
                for e in els:
                    if id(e) in used:
                        continue
                    i = _iou(abox, e.get("bbox_sheet") or e["bbox"])
                    if i > best_i:
                        best, best_i = e, i
                if best_i >= min_iou:
                    target = best

            if target is None:
                # Furniture the extractor never had -- a rule bar, a caption band, a panel.
                # THIS is where the fills come from.
                if ae.get("role") in _FURNITURE_ROLES or ae.get("fill"):
                    els.append({"role": "page_furniture", "furniture": ae.get("role"),
                                "bbox": abox, "bbox_sheet": abox, "runs": [], "text": "",
                                "fill": ae.get("fill"), "column": ae.get("column"),
                                "size_rel": ae.get("size_rel", 1.0),
                                "layout_source": "a2l-agent", "from_a2l": True})
                    stats["furniture_added"] += 1
                continue

            used.add(id(target))
            target["layout_source"] = "a2l-agent"
            target["layout_role"] = ae.get("role")
            for k in ("column", "align", "font", "fill", "text_color"):
                if ae.get(k) is not None:
                    target[f"layout_{k}" if k != "column" else "column"] = ae[k]
            # ON A SCAN, THE AGENT'S BOX IS THE ONLY MEASUREMENT THERE IS.
            #
            # The rule below -- keep the extractor's bbox, because a measured box beats an
            # estimated one -- is right for a born-digital page, where the text layer's box
            # IS a measurement. On a page with NO text layer it is exactly backwards: the
            # extractor has nothing to measure, so its "box" is the invented 0.10-0.90
            # reading-order placeholder, and A2L's is the only real measurement of the page.
            #
            # Keeping the placeholder while stamping `layout_source: a2l-agent` on it was the
            # worst of both: 127 boxes in Class 12 ch01 carried guessed coordinates under an
            # agent's name, so `ESTIMATED_GEOMETRY` stopped firing and the exact renderer
            # placed almost every block at 0.1-0.9. That is LESSONS 0.1 again -- a guess that
            # cannot be told from a measurement -- reappearing because provenance was decided
            # by WHO produced a box rather than by whether anything was actually measured.
            if abox and (page.get("has_text_layer") is False
                         or target.get("bbox_estimated")):
                target["bbox"] = abox
                target["bbox_sheet"] = abox
                target.pop("bbox_estimated", None)
                target["layout_source"] = "a2l-agent"
                stats["boxes_replaced"] = stats.get("boxes_replaced", 0) + 1

            # A2L's role is a judgement about what the element IS; the extractor's is inferred
            # from size and position. Where the agent is more specific, it wins -- and on a
            # page WITH a text layer the extractor's own `bbox` is never overwritten, because
            # there a measured box really does beat an estimated one.
            role = _ROLE_ALIAS.get(ae.get("role"), ae.get("role"))
            if role and role != target.get("role") and target.get("role") in (
                    "paragraph", "list", "side_note"):
                target["role"] = role
            stats["elements_enriched"] += 1

    layout["layout_join"] = stats
    return stats
