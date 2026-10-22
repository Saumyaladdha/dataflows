#!/usr/bin/env python3
"""Consolidates one chapter's measured page layouts (step A2L) into a single, plainly-named
JSON that the HTML review exporter reads instead of hard-coded CSS constants.

    python3 scripts/build_html_layout_data.py BIO12O-ch03

Writes `exports/review/html_data/<CHAPTER>_layout.json`.

Why this file exists, and why its keys are spelled out in full:

The HTML exporter originally carried a hand-written palette and type scale per subject, sampled
by eye from ONE chapter's opening page. That produced correct colours for that one book and
generalises to nothing -- there are ~100 chapters across three subjects, each with its own
palette and opener design. Step A2L measures the real thing from each page image; this script
is the join between that per-page measurement and the one-per-chapter summary a stylesheet
actually needs.

Every key is named for what it IS rather than abbreviated, because the point of the file is that
a person can open it and immediately see which number governs which part of the rendering:
`text_alignment_by_role.paragraph = "justify"` needs no decoding, `align.p = "j"` does.

Each summary value is accompanied by how many pages voted for it and what the runners-up were,
so a value that was close-run is visible as close-run rather than presented as settled fact.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

# Roles whose fill colour defines a chapter's palette, mapped to the self-describing key name
# the output file uses for each.
_FILL_KEYS = {
    "chapter_banner": "chapter_banner_fill",
    "rule_bar": "opener_rule_bar_fill",
    "page_header_band": "page_header_band_fill",
    "footer_rule": "footer_rule_fill",
    "contents_panel": "contents_panel_fill",
    # A worked-example / SUMMARY panel has its own tint in the book (BIO12O-ch03 p014:
    # pale yellow #fef7db). It was measured from the start but never exported, so the
    # stylesheet fell back to a wash derived from the heading colour -- a green panel
    # where the book prints a yellow one.
    "box": "box_panel_fill",
    # NCERT sets a figure caption on its own tinted band directly under the artwork
    # (measured #fef2e2 on 11 of BIO12O-ch03's pages), not on bare paper.
    "figure_caption": "figure_caption_band_fill",
    # The folio tab has its own colour: physics prints a pale blue #c6eafb box, not the cyan
    # of its rule bar, and biology an orange one. Using the bar colour made the physics tab
    # a saturated cyan the book never prints.
    "page_number": "page_number_fill",
}
_TEXT_COLOUR_KEYS = {
    "section_heading": "section_heading_text_color",
    "major_heading": "major_heading_text_color",
    "chapter_title": "chapter_title_text_color",
    # A figure caption carries the chapter's accent in some books even when the numbered
    # headings do not: on PHY12O-ch01 the x.y headings are grey #6d6e71 while captions,
    # sub-headings and box bars are cyan #00adef -- so leaving this out meant the exporter
    # rendered a grey physics chapter where the book is unmistakably blue.
    "figure_caption": "figure_caption_text_color",
    "paragraph": "body_text_color",
}


def _best_layouts(chapter):
    """{page_num: layout_record} keeping the most-settled A2L run per page."""
    best = {}
    for path in glob.glob(rc.pp("steps", "A2L", "out", f"{chapter}-p*.*.json")):
        m = re.match(rf"{re.escape(chapter)}-p(\d+)\.(\w+)\.json$", os.path.basename(path))
        if not m:
            continue
        page_num, run_label = int(m.group(1)), m.group(2)
        pri = _RUN_PRIORITY.get(run_label, 9)
        if page_num in best and best[page_num][0] <= pri:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                rec = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(rec, dict) and "elements" in rec and "page" in rec:
            best[page_num] = (pri, rec)
    return {k: v[1] for k, v in sorted(best.items())}


def _consensus(values):
    """(winner, support, runners_up) -- the most common value, how many pages agreed, and the
    alternatives. Returns (None, 0, []) when nothing was measured."""
    vals = [v for v in values if v not in (None, "")]
    if not vals:
        return None, 0, []
    counts = collections.Counter(vals).most_common()
    winner, support = counts[0]
    return winner, support, [{"value": v, "pages": c} for v, c in counts[1:]]


def _summarise(pages):
    by_role_fill = collections.defaultdict(list)
    by_role_text = collections.defaultdict(list)
    by_role_align = collections.defaultdict(list)
    by_role_font = collections.defaultdict(list)
    by_role_size = collections.defaultdict(list)
    ratios = []

    for rec in pages.values():
        pg = rec.get("page") or {}
        w, h = pg.get("width_px"), pg.get("height_px")
        if isinstance(w, int) and isinstance(h, int) and h:
            ratios.append(round(w / h, 4))
        for el in rec.get("elements") or []:
            role = el.get("role")
            if not role:
                continue
            if el.get("fill"):
                by_role_fill[role].append(el["fill"])
            if el.get("text_color"):
                by_role_text[role].append(el["text_color"])
            if el.get("align"):
                by_role_align[role].append(el["align"])
            if el.get("font"):
                by_role_font[role].append(el["font"])
            sr = el.get("size_rel")
            if isinstance(sr, (int, float)) and not isinstance(sr, bool):
                by_role_size[role].append(float(sr))

    def pick(bucket, role):
        winner, support, runners = _consensus(bucket.get(role, []))
        if winner is None:
            return None
        return {"value": winner, "measured_on_pages": support, "other_values_seen": runners}

    palette = {}
    for role, key in _FILL_KEYS.items():
        got = pick(by_role_fill, role)
        if got:
            palette[key] = got
    for role, key in _TEXT_COLOUR_KEYS.items():
        got = pick(by_role_text, role)
        if got:
            palette[key] = got

    type_scale = {}
    for role, sizes in sorted(by_role_size.items()):
        if not sizes:
            continue
        sizes_sorted = sorted(sizes)
        median = sizes_sorted[len(sizes_sorted) // 2]
        type_scale[role] = {
            "size_relative_to_body_text": round(median, 3),
            "measured_on_elements": len(sizes),
            "range_seen": [round(min(sizes), 3), round(max(sizes), 3)],
        }

    alignment = {r: pick(by_role_align, r) for r in sorted(by_role_align)}
    fonts = {r: pick(by_role_font, r) for r in sorted(by_role_font)}

    ratio_winner, ratio_support, ratio_runners = _consensus(ratios)
    a4 = 210 / 297
    geometry = {
        "page_width_over_height": ratio_winner,
        "measured_on_pages": ratio_support,
        "other_values_seen": ratio_runners,
        "matches_a4_portrait": (ratio_winner is not None
                                and abs(ratio_winner - a4) < 0.01),
        "a4_portrait_for_reference": round(a4, 4),
    }
    return palette, type_scale, alignment, fonts, geometry


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. BIO12O-ch03")
    args = ap.parse_args()

    pages = _best_layouts(args.chapter)
    if not pages:
        print(f"no A2L layout output found for {args.chapter} -- run "
              f"`python3 scripts/run_step.py A2L --list --chapters {args.chapter}` first",
              file=sys.stderr)
        return 1

    palette, type_scale, alignment, fonts, geometry = _summarise(pages)

    columns_by_page, elements_by_page = {}, {}
    for page_num, rec in pages.items():
        key = f"page_{page_num:03d}"
        cols = (rec.get("page") or {}).get("columns") or []
        columns_by_page[key] = {
            "number_of_columns": len(cols),
            "columns_left_to_right": [
                {"id": c.get("id"),
                 "starts_at_fraction_of_page_width": c.get("x0"),
                 "ends_at_fraction_of_page_width": c.get("x1")}
                for c in cols
            ],
        }
        elements_by_page[key] = {
            "body_text_size_px_on_this_page": (rec.get("page") or {}).get("body_text_size_px"),
            "page_width_px": (rec.get("page") or {}).get("width_px"),
            "page_height_px": (rec.get("page") or {}).get("height_px"),
            "measurement_note": rec.get("note"),
            "elements_in_reading_order": rec.get("elements") or [],
        }

    out = {
        "chapter": args.chapter,
        "what_this_file_is": (
            "Measured PRINTED LAYOUT of this NCERT chapter, consolidated from step A2L "
            "(one agent measurement per page). It describes how the real book page is "
            "arranged -- column structure, which colour fills each panel, how big each kind "
            "of text is relative to body prose, and how each kind of text is aligned -- so "
            "the HTML review export can reproduce the page instead of relying on hand-picked "
            "CSS constants. Values are summarised across the chapter's pages; each one records "
            "how many pages it was measured on and what other values were seen, so a close-run "
            "value is visible as close-run."
        ),
        "produced_by": "scripts/build_html_layout_data.py from steps/A2L/out/",
        "pages_measured": len(pages),
        "page_geometry": geometry,
        "colors_used_by_the_book": palette,
        "type_scale_relative_to_body_text": type_scale,
        "text_alignment_by_role": alignment,
        "font_class_by_role": fonts,
        "column_layout_by_page": columns_by_page,
        "full_detail_by_page": elements_by_page,
        "how_to_read_this": {
            "bbox": "[x0, y0, x1, y1] as FRACTIONS of page width/height (0-1), not pixels, so "
                    "the layout is independent of the DPI a page was rendered at.",
            "size_rel": "An element's text size divided by that page's own body-text size. "
                        "Body prose is 1.0 by definition; a chapter title around 2.5-3.0.",
            "column": "'left'/'right' name a declared side column; 'full' means the element "
                      "spans every column (a banner, a rule bar, a full-width figure).",
            "role": "What the element IS on the printed page. 'qr_code' and 'decorative_image' "
                    "are publishing furniture carrying no subject content.",
        },
    }

    out_dir = rc.pp("exports", "review", "html_data")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{args.chapter}_layout.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"{args.chapter}: {len(pages)} pages measured")
    print(f"  page ratio      : {geometry['page_width_over_height']} "
          f"(A4 portrait: {geometry['matches_a4_portrait']})")
    print(f"  colours found   : {len(palette)}")
    print(f"  roles with sizes: {len(type_scale)}")
    print(f"wrote {os.path.relpath(out_path, rc.pp())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
