#!/usr/bin/env python3
"""Builds a human-readable Markdown export of one NCERT chapter, for review against the source PDF.

    python3 scripts/export_ncert_chapter_review.py PHY12O-ch01 \\
        --pdf "/path/to/Old_ncert_Physics_Chapter_1.pdf"

Writes `exports/review/<CHAPTER>_FULL_EXTRACT.md` plus `exports/review/<CHAPTER>_figures/*.png`
(every figure/table cropped straight from the source PDF; equations stay as text, not images --
see "Why equations are not cropped" below).

This is a REVIEW AID, not a pipeline deliverable: nothing it writes feeds back into the pipeline,
and nothing downstream reads its output. It exists so a person can read a chapter's extraction
next to the real page and judge the quality directly.

Three defects an earlier, ad-hoc version of this script had, found by the owner auditing its
first output and fixed here:

  1. **Leaked the local filesystem path and username** in the document header (the absolute
     source-PDF path). Fixed: only the project-relative pieces are shown; the real source path
     lives in `register/books.csv` for anyone who needs it, not duplicated here.
  2. **Dumped every page's internal `note` field into the reading flow** -- 50+ paragraphs of the
     *agent's own reasoning about how it judged a page* ("previous_page_last_block was null in
     the input, so continuation is judged against..."), interleaved with the actual chapter
     content. That is provenance for an auditor, not something a reader should have to read
     through to find the chapter text. Fixed: notes are OFF by default (`--notes` turns them back
     on, written into a clearly separate `> QA note:` block, never mixed into a sentence).
  3. **Cropped figures/tables to their bare `bbox`, with no padding.** The real A2S step grows a
     block's crop outward toward its neighbours specifically because NCERT captions sit in the
     white space below the artwork, not inside its bbox -- see the long comment above
     `A2SPlugin.list_items`'s padding logic in `scripts/step_plugins.py`, which this script
     reimplements (same constants, same neighbour-aware growth) rather than cropping tight and
     losing the caption the way the first version of this script did.

Why equations are not cropped as images: a displayed equation is tiny and unreadable at a glance
compared to a real figure, and this export's job is readability, not completeness -- if A2S has
since transcribed the equation's LaTeX, that text is shown directly (searchable, readable); if not,
the page/block is named so the real crop can be found on disk, with no placeholder pretending the
missing content is "equation, displayed - not yet transcribed" trivia. That framing undersold real,
multi-line, page-spanning derivations in the first version of this export and is not repeated here.
"""

import argparse
import glob
import json
import os
import re
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import lib.pdf as lib_pdf  # noqa: E402

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}

# Same constants and growth rule as A2SPlugin.list_items (scripts/step_plugins.py) -- a figure's
# caption sits in the white space below its artwork, not inside the recorded bbox, so the crop
# must grow toward the nearest neighbouring block, not just add a fixed pad.
_MAX_GROW, _OPEN_GROW, _GAP = 260, 200, 8


def _best_page_outputs(chapter):
    """{page_num: (run_label, record)} keeping the most-settled run for each page."""
    best = {}
    for path in glob.glob(rc.pp("steps", "A2", "out", f"{chapter}-p*.*.json")):
        m = re.match(rf"{re.escape(chapter)}-p(\d+)\.(\w+)\.json$", os.path.basename(path))
        if not m:
            continue
        page_num, run_label = int(m.group(1)), m.group(2)
        priority = _RUN_PRIORITY.get(run_label, 9)
        key = page_num
        if key in best and best[key][0] <= priority:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                rec = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(rec, dict) and "blocks" in rec:
            best[key] = (priority, run_label, rec)
    return {k: (v[1], v[2]) for k, v in sorted(best.items())}


def _load_sibling_json(step, item_id):
    """Most-settled output for one item_id under steps/<step>/out/, or None."""
    best, best_pri = None, 99
    for path in glob.glob(rc.pp("steps", step, "out", f"{item_id}.*.json")):
        run_label = path.rsplit(".", 2)[-2]
        pri = _RUN_PRIORITY.get(run_label, 9)
        if pri < best_pri:
            try:
                with open(path, encoding="utf-8") as fh:
                    best, best_pri = json.load(fh), pri
            except (OSError, json.JSONDecodeError):
                continue
    return best


def _grown_bbox(bbox, kind, siblings_on_page, this_n):
    """Reimplementation of A2SPlugin's neighbour-aware crop growth -- same constants, same rule.
    See the module docstring and scripts/step_plugins.py for why a fixed pad is not enough."""
    k = (kind or "").strip().lower()
    if k == "table":
        pad_top, pad_bottom = 96, 56
    elif k == "figure":
        pad_top, pad_bottom = 72, 96
    else:
        pad_top, pad_bottom = 72, 72
    pad_x = 56

    x0, y0, x1, y1 = bbox
    top, bottom = y0 - pad_top, y1 + pad_bottom
    left, right = x0 - pad_x, x1 + pad_x
    up = down = lf = rt = None
    for sib in siblings_on_page:
        sb = sib.get("bbox")
        if not sb or sib.get("n") == this_n:
            continue
        if min(x1, sb[2]) - max(x0, sb[0]) > 0:
            if sb[3] <= y0:
                up = sb[3] if up is None else max(up, sb[3])
            elif sb[1] >= y1:
                down = sb[1] if down is None else min(down, sb[1])
        if min(y1, sb[3]) - max(y0, sb[1]) > 0:
            if sb[2] <= x0:
                lf = sb[2] if lf is None else max(lf, sb[2])
            elif sb[0] >= x1:
                rt = sb[0] if rt is None else min(rt, sb[0])
    top = min(top, max(up + _GAP, y0 - _MAX_GROW)) if up is not None else y0 - _OPEN_GROW
    bottom = max(bottom, min(down - _GAP, y1 + _MAX_GROW)) if down is not None else y1 + _OPEN_GROW
    left = min(left, max(lf + _GAP, x0 - _MAX_GROW)) if lf is not None else x0 - _OPEN_GROW
    right = max(right, min(rt - _GAP, x1 + _MAX_GROW)) if rt is not None else x1 + _OPEN_GROW
    return [left, top, right, bottom]


# A2's recorded bbox is measurably SHORT on a lot of blocks -- see docs/OPEN_QUESTIONS.md,
# "target_box_in_crop is systematically ~one line short": the bottom line of a caption, a
# reaction scheme's sub-labels ("Primary(1°)", "(1° amine)"), or the denominator of a displayed
# fraction sit just below the recorded edge. A flat 22px margin was not enough to recover them
# and chemistry reaction schemes came out visibly clipped. So the margin scales with the block
# and is asymmetric: more at the bottom, because that is where the clipped content always is.
_MARGIN_MIN_X, _MARGIN_MIN_TOP, _MARGIN_MIN_BOTTOM = 30, 34, 56
_MARGIN_FRAC_X, _MARGIN_FRAC_TOP, _MARGIN_FRAC_BOTTOM = 0.04, 0.06, 0.12


def _tight_bbox(bbox, tight_x=False):
    """Crop to the block's own bbox plus a proportional, bottom-weighted margin.

    Only safe once A2S has transcribed the block, and that is the whole point: the reason
    `_grown_bbox` reaches generously toward neighbours is to catch a caption printed in the
    white space OUTSIDE the recorded bbox. When A2S has already supplied that caption as text
    (the exporter prints it under the image), the image no longer has to carry it -- so the crop
    can be tight to the artwork, which is what a reader actually wants to look at.

    Measured problem this solves: on a page whose figure neighbours are ordinary paragraphs
    (which carry no bbox in A2 output, so growth has nothing to stop against), the grown crop
    ran to the flat 200px open pad and swallowed half a column of unrelated prose plus the
    page-number badge.
    """
    x0, y0, x1, y1 = bbox
    w, h = max(1, x1 - x0), max(1, y1 - y0)
    mx = 6.0 if tight_x else max(_MARGIN_MIN_X, w * _MARGIN_FRAC_X)
    mt = max(_MARGIN_MIN_TOP, h * _MARGIN_FRAC_TOP)
    mb = max(_MARGIN_MIN_BOTTOM, h * _MARGIN_FRAC_BOTTOM)
    return [x0 - mx, y0 - mt, x1 + mx, y1 + mb]


# A figure's printed caption band usually sits INSIDE the recorded bbox (NCERT tints it and
# places it directly under the artwork). When A2S has transcribed that caption we print it as
# text beneath the image -- so leaving it in the crop as well shows the same sentence twice,
# which is exactly what it looked like on BIO12O-ch03 p002's "Figure 3.1(a)". Measured on the
# real crops, the band occupies roughly the bottom 12-18% of the block; trimming 15% removes it
# while keeping the artwork whole. Only done when we actually HAVE the caption as text.
def _crop_for(bbox, kind, blocks, n, have_transcription, tight_x=False):
    """(bbox_to_crop, needs_target_border). Tight when the caption is already text; grown
    otherwise, and then the border is drawn so the reader can tell block from context."""
    if have_transcription:
        return _tight_bbox(bbox, tight_x=tight_x), False
    return _grown_bbox(bbox, kind, blocks, n), True


def _trim_caption_band(img_path):
    """Remove the printed caption band from a saved figure crop, top edge and bottom edge.

    Detection is by UNIFORM LIGHT TINT, not by brightness. Two earlier attempts failed on real
    crops and both are worth recording, because the obvious signal is the wrong one:

      * a fixed fraction (15%) cut p002's "Figure 3.1(a)" through the middle of its first line;
      * "mostly not near-white" fired on artwork too -- p012's uterus diagram is dense red and
        pink, so the scan climbed out of the band and deleted two thirds of the figure.

    NCERT's caption band is a flat wash (measured #fff2e2 / #fef2e2 on this chapter): every pixel
    across the row is nearly the SAME light colour. Artwork never is. So a band row is one whose
    sampled pixels are both light (all channels high) and tightly clustered around one value.
    """
    try:
        img = Image.open(img_path).convert("RGB")
    except OSError:
        return
    w, h = img.size
    if h < 60:
        return
    step = max(1, w // 160)

    def band_row(px, y):
        """True when this row's BACKGROUND is the flat caption tint.

        It must tolerate dark glyphs: a caption band row is mostly tint with the caption's own
        text sitting on it. An earlier version demanded 92% light pixels, which no row carrying
        text can ever satisfy -- which is exactly why p002's band survived every rebuild. So the
        test is on the background: enough tinted pixels, not much bare white, and the tint itself
        tightly clustered (artwork is saturated and varied, and fails on both counts).
        """
        vals = [px[x, y] for x in range(0, w, step)]
        if not vals:
            return False
        # The band tint is a WARM off-white: #fff2e2 has R=255, so testing `max < 252` rejected
        # the exact colour being looked for -- which is why the band survived every attempt. What
        # separates tint from paper is the MINIMUM channel: 226 here versus 255 for bare white.
        tint = [v for v in vals if 200 < min(v) <= 248]
        white = [v for v in vals if min(v) > 248]
        if len(tint) / len(vals) < 0.50:           # not enough tinted background
            return False
        if len(white) / len(vals) > 0.28:          # mostly bare paper
            return False
        rs = [v[0] for v in tint]; gs = [v[1] for v in tint]; bs = [v[2] for v in tint]
        return (max(rs) - min(rs) < 30 and max(gs) - min(gs) < 30 and max(bs) - min(bs) < 30)

    def run_from(px, y_start, direction, limit):
        y = y_start
        found_top = found_bottom = None
        while 0 <= y < h and (y - y_start) * direction <= limit:
            if band_row(px, y):
                if found_top is None:
                    found_top = found_bottom = y
                else:
                    found_bottom = y
            elif found_top is not None:
                break
            y += direction
        return found_top, found_bottom

    px = img.load()
    # Bottom edge: the band sits under the artwork, possibly above a white gutter.
    #
    # The run is NOT contiguous. A band row carrying caption text has its tint fraction pushed
    # below the bar by the glyphs, so insisting on consecutive band rows stopped at the first
    # line of type and trimmed a sliver. Collect every band row in the search window instead and
    # take their extent; the intervening text rows are part of the same band by construction.
    hits = [y for y in range(h - 1, int(h * 0.45), -1) if band_row(px, y)]
    if hits:
        lo, hi = min(hits), max(hits)
        # Artwork is saturated and never reads as this flat warm tint, so the only way the extent
        # grows large is a genuinely tall band -- but cap it anyway rather than risk the figure.
        if 10 <= (hi - lo) <= h * 0.28:
            img = img.crop((0, 0, w, max(10, lo - 1)))

    # Top edge: a crop can begin inside the PREVIOUS figure's band.
    px2 = img.load()
    h2 = img.size[1]
    y = 0
    while y < h2 * 0.18 and band_row(px2, y):
        y += 1
    if 8 <= y < h2 * 0.18:
        img = img.crop((0, y + 1, w, h2))
    img.save(img_path)


def _mark_target_box(img_path, bbox, grown):
    """Draw a border around the block's own bbox inside its saved (grown) crop.

    The grow toward neighbouring blocks exists so a caption sitting in the gap below a figure
    never gets clipped -- but on a page where neighbouring paragraph/heading blocks carry no
    bbox of their own (A2 only records one for needs_special blocks), growth has nothing to stop
    against and falls back to a flat open-ended pad, which can read as "the crop swallowed the
    surrounding prose". It did not swallow it by mistake -- the prose really is in the saved
    image, for caption safety -- but a human reviewer has no way to tell the block's own region
    from the context around it without this. The border is the fix: it answers "which part of
    this image is actually the block" without shrinking the crop and risking a clipped caption.
    Real case this was added for: a Chemistry figure crop (CHE12L-ch09 p002 b2) whose grown
    region included two full neighbouring paragraphs because neither carried a bbox.
    """
    left, top, right, bottom = grown
    x0, y0, x1, y1 = bbox
    box = (x0 - left, y0 - top, x1 - left, y1 - top)
    try:
        img = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        draw.rectangle(box, outline=(220, 30, 30), width=3)
        img.save(img_path)
    except OSError:
        pass  # the crop itself still exists and is still usable; the border is a nicety


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", help="e.g. PHY12O-ch01")
    ap.add_argument("--pdf", required=True, help="path to the source PDF for this chapter")
    ap.add_argument("--title", default=None, help="chapter title for the header, if known")
    ap.add_argument("--notes", action="store_true",
                    help="include each page's internal QA note (off by default -- see module docstring)")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        print(f"source PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    pages = _best_page_outputs(args.chapter)
    if not pages:
        print(f"no A2 output found for {args.chapter}", file=sys.stderr)
        return 1

    fig_dir_name = f"{args.chapter}_figures"
    fig_dir = rc.pp("exports", "review", fig_dir_name)
    os.makedirs(fig_dir, exist_ok=True)

    title_line = f"# {args.chapter}" + (f" — {args.title}" if args.title else "")
    lines = [
        title_line + "\n",
        f"Source: registered in `register/books.csv` as `{args.chapter}` "
        f"(file `{os.path.basename(args.pdf)}`).\n",
        f"Raw per-page JSON: `steps/A2/out/{args.chapter}-p0NN.<run>.json`\n",
        "\nFigures and tables are embedded inline, cropped from the source PDF with the same "
        "neighbour-aware padding the real pipeline uses (so captions are not clipped). Where A2S "
        "has transcribed a figure's caption/labels, or an equation's LaTeX, that text is shown "
        "alongside it. Where A2N has corrected flattened notation (exponents, radicals, "
        "inequalities) or A2B has marked bold terms, the corrected/annotated text is shown, with "
        "the original noted only where it differs.\n",
        "\n---\n",
    ]

    n_blocks = n_fig_cropped = n_eq_shown = n_eq_pending = 0
    for page_num, (run_label, rec) in pages.items():
        lines.append(f"\n## Page {page_num:03d}  (`{args.chapter}-p{page_num:03d}.{run_label}.json`)\n")
        rh = rec.get("running_header_footer_removed")
        if rh:
            lines.append(f"*removed furniture: {rh}*\n")

        blocks = rec.get("blocks") or []
        n2_item = f"{args.chapter}-p{page_num:03d}"
        n2b = _load_sibling_json("A2B", n2_item)
        n2n = _load_sibling_json("A2N", n2_item)
        bold_by_n = {b["n"]: b.get("bold_terms") or [] for b in (n2b or {}).get("blocks", [])}
        corr_by_n = {b["n"]: b for b in (n2n or {}).get("blocks", []) if b.get("corrected_text")}

        for b in blocks:
            n_blocks += 1
            kind, n = b.get("kind", "?"), b.get("n", "?")
            if b.get("needs_special"):
                bbox = b.get("bbox")
                if kind in ("figure", "table") and bbox:
                    a2s = _load_sibling_json("A2S", f"{args.chapter}-p{page_num:03d}-b{n}")
                    box, needs_border = _crop_for(bbox, kind, blocks, n, bool(a2s))
                    img_path = os.path.join(fig_dir, f"p{page_num:03d}_b{n}.png")
                    lib_pdf.crop_box(args.pdf, page_num, box, img_path, unit="px")
                    if needs_border:
                        _mark_target_box(img_path, bbox, box)
                    n_fig_cropped += 1
                    rel = f"{fig_dir_name}/p{page_num:03d}_b{n}.png"
                    lines.append(f"\n**[{n}] ({kind})**\n\n![{kind} p{page_num} block {n}]({rel})\n")
                    if a2s and kind == "figure":
                        cap = a2s.get("caption") or "(no caption printed)"
                        labs = a2s.get("labels") or []
                        lines.append(f"\n*transcribed caption:* **{cap}**")
                        if labs:
                            lines.append(f"\n*labels:* {', '.join(labs)}\n")
                    elif a2s and kind == "table":
                        hdr, rows = a2s.get("header") or [], a2s.get("rows") or []
                        if hdr:
                            lines.append("\n" + "| " + " | ".join(hdr) + " |")
                            lines.append("|" + "---|" * len(hdr))
                            for r in rows:
                                lines.append("| " + " | ".join(str(c) for c in r) + " |")
                    elif not a2s:
                        lines.append(f"\n*(not yet transcribed by A2S — image above is the real crop)*\n")
                else:
                    # equation/box (or a figure/table with no bbox): never cropped, per module docstring
                    a2s = _load_sibling_json("A2S", f"{args.chapter}-p{page_num:03d}-b{n}")
                    box_text = (a2s or {}).get("text") if kind == "box" else None
                    if box_text:
                        # Box: `text` is what makes it quotable -- show it, not just its latex (a
                        # box transcribed with text but no latex is COMPLETE, not pending; showing
                        # only latex here would silently drop the prose, same mistake the step's
                        # own brief warns the transcriber itself against making).
                        n_eq_shown += 1
                        num = a2s.get("number")
                        label = f" {num}" if num else ""
                        # Same structural-newline rule as the non-special branch below.
                        lines.append(f"\n**[{n}] (box{label})**  {box_text.replace(chr(10), '  ' + chr(10))}\n")
                        if a2s.get("latex"):
                            lines.append(f"\n  `{a2s['latex']}`\n")
                    elif a2s and a2s.get("latex"):
                        n_eq_shown += 1
                        num = a2s.get("number")
                        lines.append(f"\n**[{n}] (equation{f' {num}' if num else ''})**  `{a2s['latex']}`\n")
                    else:
                        n_eq_pending += 1
                        lines.append(f"\n**[{n}] ({kind}) — not yet transcribed "
                                     f"(see `steps/A2/out/{args.chapter}-p{page_num:03d}.{run_label}.json` "
                                     f"block n={n} for its bbox)**\n")
            else:
                fix = corr_by_n.get(n)
                txt = (fix["corrected_text"] if fix else (b.get("text") or "")).strip()
                bold = bold_by_n.get(n) or []
                if bold:
                    for term in sorted(bold, key=len, reverse=True):
                        if term in txt:
                            txt = txt.replace(term, f"**{term}**", 1)
                # A `list` or `box` block's newlines are STRUCTURAL -- one per numbered question,
                # per option, per line of a worked example -- but a lone newline inside a Markdown
                # paragraph renders as a space, so they have to be made into hard breaks (two
                # trailing spaces) or the structure is silently lost. A `paragraph`'s newlines are
                # incidental PDF hard-wraps and correctly stay collapsed. Real defect this fixes:
                # BIO12O-ch03 p015's 21-question EXERCISES list came out as one wall of prose.
                if kind in ("list", "box") and "\n" in txt:
                    txt = txt.replace("\n", "  \n")
                lines.append(f"\n**[{n}] ({kind})**  {txt}\n")
                if fix:
                    lines.append(f"\n*(notation corrected by A2N: {len(fix.get('fixes') or [])} fix(es))*\n")

        if args.notes and rec.get("note"):
            lines.append(f"\n> QA note: {rec['note']}\n")
        lines.append("\n---\n")

    out_path = rc.pp("exports", "review", f"{args.chapter}_FULL_EXTRACT.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"pages: {len(pages)} | blocks: {n_blocks} | figures/tables cropped: {n_fig_cropped}")
    print(f"equations shown as text: {n_eq_shown} | equations still pending A2S: {n_eq_pending}")
    print(f"wrote {os.path.relpath(out_path, rc.pp())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
