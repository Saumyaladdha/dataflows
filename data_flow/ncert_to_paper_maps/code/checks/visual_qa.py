#!/usr/bin/env python3
"""Visual QA gate: compare a generated chapter PDF against its source NCERT PDF.

This script MAKES NO JUDGEMENTS about whether a chapter is good. It measures
rendered pixels and reports numbers plus a mechanical PASS/WARN/FAIL against the
named thresholds at the top of this file. Every threshold is a constant with a
comment saying what it is for, so a disagreement about "how clean is clean" is a
one-line edit, not an argument with the code.

Usage:
    .venv/bin/python3 scripts/checks/visual_qa.py <CHAPTER> \
        --generated exports/chapters/<CHAPTER>/<CHAPTER>.pdf \
        --source "inputs/ncert/.../Old_ncert_<...>.pdf" [--json]
    .venv/bin/python3 scripts/checks/visual_qa.py --self-test

Exit code: 0 if no check FAILs, 1 if any check FAILs (WARN does not fail the
gate, NOT_MEASURED does not fail the gate but is reported loudly).

What is measured from PIXELS only, and what uses the PDF text layer
-------------------------------------------------------------------
Checks 1-6 are pure pixel measurements at RENDER_DPI. In particular the
"content clipped at a sheet edge" check (6) NEVER asks the text layer whether
something is truncated: a visually clipped word is still fully present in the
text layer with a bbox inside the page, which is exactly how this project got
confident, wrong "0 truncated" reports before. Check 6 counts dark rendered
pixels inside the trim strip; the text layer is used only to CLASSIFY which of
those already-measured pixels sit inside a glyph box (so that a band, a rule or
a bleeding decorative corner is not reported as a clipped word).

Check 7 (text under page furniture) measures the band geometry from pixels and
then uses text-layer span rectangles for position only -- it is a question about
where text sits relative to furniture, not about whether text is visible.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np

try:
    import pymupdf  # PyMuPDF >= 1.24 exposes the modern name
except ImportError:  # pragma: no cover - older PyMuPDF
    import fitz as pymupdf


# --------------------------------------------------------------------------
# Thresholds. Every number the gate decides on lives here.
# --------------------------------------------------------------------------

# Render resolution for every pixel measurement. 100dpi is enough to see a
# clipped glyph (a 10pt glyph is ~14px tall) and cheap enough for a 65-sheet
# chapter.
RENDER_DPI = 100

# A pixel counts as "ink" (anything other than bare paper) below this
# luminance. Paper renders at 255; the lightest real furniture fill seen in
# these books is ~#f2efe7 (luma 240), so 200 keeps faint tints out of the ink
# number while still catching every tint that carries content.
INK_LUMA_MAX = 200

# A pixel counts as "glyph-dark" below this luminance. Body text renders at
# #221f1f / #212121 (luma ~33) and antialiased glyph edges stay well under 128;
# light furniture fills (#c6eafb, #fef7db, #dbdcde) are all above it.
GLYPH_LUMA_MAX = 128

# Check 2: a sheet whose ink coverage is below this is BLANK. A real NCERT text
# sheet never goes under ~5%; 0.5% allows for a stray running header on a sheet
# that is otherwise empty, which is still a blank sheet.
BLANK_INK_MAX_FRACTION = 0.005

# Check 3: a sheet below this (but above blank) is SPARSE -- it carries some
# content but is not using the paper the way the book does.
SPARSE_INK_MAX_FRACTION = 0.04

# Check 3 verdict: more than this share of sheets being sparse means the
# chapter is systematically under-filling its pages, not just ending a section.
SPARSE_SHEETS_MAX_FRACTION = 0.15

# Check 4: generated mean ink coverage must be at least this multiple of the
# source book's mean ink coverage. Below it, the chapter is spreading the same
# content over more paper than the book did.
MEAN_INK_MIN_RATIO_VS_SOURCE = 0.75

# Check 1: generated sheet count may exceed the source page count by at most
# this fraction. The book's own page count is the ground truth for "how much
# paper this chapter takes"; 5% absorbs a legitimate one-sheet spill on a long
# chapter and nothing more.
SHEET_COUNT_EXCESS_MAX_FRACTION = 0.05

# Check 5: the header band is looked for in the top this-fraction of a sheet.
BAND_TOP_FRACTION = 0.08

# Check 5: per-channel tolerance when matching a rendered pixel against the
# declared band colour. Renderer rounding moves a channel by 1-2 (#4a7435 ->
# #4a7333); 24 absorbs that without letting a different fill match.
BAND_COLOR_TOLERANCE = 24

# Check 5: a pixel row counts as a band row when at least this fraction of its
# pixels match the band colour. The band in these books runs across most, but
# not all, of the sheet width.
BAND_MIN_ROW_COVERAGE = 0.30

# Check 5: a band must be at least this many rows tall (at RENDER_DPI) to be a
# band rather than a rule line. 4px at 100dpi is ~1mm.
BAND_MIN_ROWS = 4

# Check 5: a colour must cover at least this share of the top strip to be
# reported as the sheet's observed top fill.
BAND_MIN_STRIP_SHARE = 0.03

# Check 5 verdict: the share of generated sheets showing the band may fall
# below the share of SOURCE pages showing it by at most this much. Comparing
# against the book (rather than demanding 100%) lets chapter openers and the
# last sheet legitimately have no running band.
BAND_SHEET_FRACTION_TOLERANCE = 0.10

# Check 6: how close to the bottom/right trim edge content must be to count as
# clipped.
TRIM_MARGIN_MM = 2.0

# Check 6 verdict: glyph pixels allowed inside the trim strip per chapter
# before it is a hard failure. A clipped word leaves dozens of dark pixels in a
# 2mm strip; 12 absorbs an antialiased descender from a glyph box that merely
# touches the strip.
EDGE_GLYPH_PX_MAX = 12

# Check 7: a text span counts as dark (body-like, not a reversed-out header
# label) below this colour luminance.
DARK_TEXT_LUMA_MAX = 160

# Check 7: a text that appears inside the band on at least this share of the
# banded sheets is the chapter's running header (page furniture), not an
# intruder. These books alternate two running headers across verso/recto (e.g.
# "BIOLOGY" / "HUMAN REPRODUCTION"), so a single modal text is not enough;
# 0.15 keeps both of a pair while a stray body line on one or two sheets stays
# foreign.
RUNNING_HEADER_MIN_SHEET_FRACTION = 0.15

# Check 9: embedded images in the generated PDF, as a fraction of the figure
# crops on disk, below which figures look dropped. Only a WARN: the crop
# directory is produced by a different stage and may legitimately hold more
# crops than the chapter places.
FIGURE_PLACED_MIN_RATIO = 0.90

# Check 8: template placeholders that must never survive into a reader HTML.
PLACEHOLDER_RE = re.compile(r"@[A-Z][A-Z0-9_]{2,}@")
# The "unsure" sentinel only matters when it was rendered as maths.
UNSURE_RE = re.compile(r"unsure", re.IGNORECASE)
MATH_CONTEXT_RE = re.compile(
    r"(\\\([^()]{0,400}?\\\))"          # \( ... \)
    r"|(\\\[[\s\S]{0,400}?\\\])"        # \[ ... \]
    r"|(\$\$[\s\S]{0,400}?\$\$)"        # $$ ... $$
    r"|(<(?:span|div|math)[^>]*(?:class=\"[^\"]*(?:math|mjx|katex)[^\"]*\"|\bmath\b)[^>]*>[\s\S]{0,400}?</(?:span|div|math)>)",
    re.IGNORECASE,
)

FIGURE_CROP_RE = re.compile(r"^p\d+_b\d+\.(png|jpg|jpeg)$", re.IGNORECASE)

PASS, WARN, FAIL, NOT_MEASURED = "PASS", "WARN", "FAIL", "NOT_MEASURED"


# --------------------------------------------------------------------------
# Pure measurement helpers (these are what --self-test exercises)
# --------------------------------------------------------------------------

def luminance(rgb: np.ndarray) -> np.ndarray:
    """Rec.601 luma of an (H, W, 3) uint8 array, as float32 (H, W)."""
    a = rgb.astype(np.float32)
    return 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]


def ink_coverage(rgb: np.ndarray, luma_max: int = INK_LUMA_MAX) -> float:
    """Fraction of pixels that are not bare paper."""
    return float((luminance(rgb) < luma_max).mean())


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise ValueError(f"not a hex colour: {value!r}")
    return (int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))


def rgb_to_hex(rgb) -> str:
    return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


def colour_mask(rgb: np.ndarray, colour, tolerance: int = BAND_COLOR_TOLERANCE) -> np.ndarray:
    """Boolean mask of pixels within +/-tolerance per channel of `colour`."""
    target = np.array(colour, dtype=np.int16)
    diff = np.abs(rgb.astype(np.int16) - target)
    return (diff <= tolerance).all(axis=2)


def band_rows_for_colour(
    rgb: np.ndarray,
    colour,
    tolerance: int = BAND_COLOR_TOLERANCE,
    top_fraction: float = BAND_TOP_FRACTION,
    min_row_coverage: float = BAND_MIN_ROW_COVERAGE,
    min_rows: int = BAND_MIN_ROWS,
):
    """Find a horizontal band of `colour` in the top `top_fraction` of a sheet.

    Returns (present, (row_start, row_end_exclusive) or None, matched_fraction
    of the top strip). Only contiguous runs of at least `min_rows` rows count,
    so a single-pixel rule line is not reported as a band.
    """
    h = rgb.shape[0]
    top_h = max(1, int(round(top_fraction * h)))
    strip = rgb[:top_h]
    mask = colour_mask(strip, colour, tolerance)
    matched_fraction = float(mask.mean())
    row_cov = mask.mean(axis=1)
    hit = row_cov >= min_row_coverage

    best = None
    run_start = None
    for i, flag in enumerate(hit.tolist() + [False]):
        if flag and run_start is None:
            run_start = i
        elif not flag and run_start is not None:
            if (i - run_start) >= min_rows and (best is None or (i - run_start) > (best[1] - best[0])):
                best = (run_start, i)
            run_start = None
    return (best is not None), best, matched_fraction


def dominant_top_fill(
    rgb: np.ndarray,
    top_fraction: float = BAND_TOP_FRACTION,
    min_share: float = BAND_MIN_STRIP_SHARE,
):
    """Most common non-paper colour in the sheet's top strip.

    Returns (hex or None, share of the top strip). This is measured without
    reference to any declared colour, so a chapter that paints a band in the
    WRONG colour reports a band here and a colour mismatch in check 5, instead
    of silently reporting "no band".
    """
    h = rgb.shape[0]
    top_h = max(1, int(round(top_fraction * h)))
    strip = rgb[:top_h].reshape(-1, 3)
    lum = 0.299 * strip[:, 0] + 0.587 * strip[:, 1] + 0.114 * strip[:, 2]
    non_paper = strip[lum < 245]
    if non_paper.size == 0:
        return None, 0.0
    colours, counts = np.unique(non_paper, axis=0, return_counts=True)
    j = int(np.argmax(counts))
    share = float(counts[j]) / float(strip.shape[0])
    if share < min_share:
        return None, share
    return rgb_to_hex(colours[j]), share


def edge_ink(
    rgb: np.ndarray,
    strip_px: int,
    glyph_rects=None,
    luma_max: int = GLYPH_LUMA_MAX,
):
    """Dark ink inside the bottom and right trim strips, measured in pixels.

    `glyph_rects` is an optional iterable of (x0, y0, x1, y1) pixel rectangles
    (from the text layer) used ONLY to classify which measured dark pixels sit
    inside a glyph box. Presence is always decided by pixels; when
    `glyph_rects` is None the glyph counts equal the raw dark counts.

    Returns a dict with bottom/right raw dark-pixel counts and the subset that
    falls inside a glyph box.
    """
    h, w = rgb.shape[0], rgb.shape[1]
    strip_px = max(1, min(strip_px, h, w))
    dark = luminance(rgb) < luma_max

    glyph = None
    if glyph_rects is not None:
        glyph = np.zeros((h, w), dtype=bool)
        for x0, y0, x1, y1 in glyph_rects:
            cx0 = max(0, int(np.floor(x0)))
            cy0 = max(0, int(np.floor(y0)))
            cx1 = min(w, int(np.ceil(x1)))
            cy1 = min(h, int(np.ceil(y1)))
            if cx1 > cx0 and cy1 > cy0:
                glyph[cy0:cy1, cx0:cx1] = True

    def count(region_mask):
        raw = int((dark & region_mask).sum())
        if glyph is None:
            return raw, raw
        return raw, int((dark & region_mask & glyph).sum())

    bottom_region = np.zeros((h, w), dtype=bool)
    bottom_region[h - strip_px:, :] = True
    right_region = np.zeros((h, w), dtype=bool)
    right_region[:, w - strip_px:] = True

    bottom_raw, bottom_glyph = count(bottom_region)
    right_raw, right_glyph = count(right_region)
    return {
        "strip_px": strip_px,
        "bottom_dark_px": bottom_raw,
        "bottom_glyph_px": bottom_glyph,
        "right_dark_px": right_raw,
        "right_glyph_px": right_glyph,
    }


# --------------------------------------------------------------------------
# Rendering / PDF access
# --------------------------------------------------------------------------

def render_rgb(page, dpi: int = RENDER_DPI) -> np.ndarray:
    pm = page.get_pixmap(dpi=dpi)
    arr = np.frombuffer(pm.samples, dtype=np.uint8).reshape(pm.height, pm.width, pm.n)
    return np.ascontiguousarray(arr[:, :, :3])


def text_spans(page, scale: float):
    """Text-layer spans as (rect_in_px, text, colour_luma). Position only."""
    out = []
    try:
        data = page.get_text("dict")
    except Exception:
        return out
    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                x0, y0, x1, y1 = span["bbox"]
                c = int(span.get("color", 0))
                r, g, b = (c >> 16) & 255, (c >> 8) & 255, c & 255
                out.append(
                    {
                        "rect_px": (x0 * scale, y0 * scale, x1 * scale, y1 * scale),
                        "text": span.get("text", ""),
                        "luma": 0.299 * r + 0.587 * g + 0.114 * b,
                    }
                )
    return out


def count_embedded_images(doc):
    """(unique image xrefs, total image placements) in a PDF."""
    xrefs, placements = set(), 0
    for page in doc:
        imgs = page.get_images(full=True)
        placements += len(imgs)
        for img in imgs:
            xrefs.add(img[0])
    return len(xrefs), placements


# --------------------------------------------------------------------------
# Per-PDF sheet measurement
# --------------------------------------------------------------------------

def measure_pdf(path: Path, declared_band_rgb, want_text_layer: bool):
    doc = pymupdf.open(path)
    strip_px = max(1, int(round(TRIM_MARGIN_MM * RENDER_DPI / 25.4)))
    sheets = []
    for idx, page in enumerate(doc):
        rgb = render_rgb(page)
        h, w = rgb.shape[0], rgb.shape[1]
        scale = h / page.rect.height if page.rect.height else 1.0

        cov = ink_coverage(rgb)
        observed_hex, observed_share = dominant_top_fill(rgb)

        if declared_band_rgb is not None:
            declared_present, declared_span, declared_frac = band_rows_for_colour(rgb, declared_band_rgb)
        else:
            declared_present, declared_span, declared_frac = None, None, None

        if observed_hex is not None:
            obs_present, obs_span, _ = band_rows_for_colour(rgb, hex_to_rgb(observed_hex))
        else:
            obs_present, obs_span = False, None

        spans = text_spans(page, scale) if want_text_layer else []
        glyph_rects = [s["rect_px"] for s in spans] if want_text_layer else None
        edges = edge_ink(rgb, strip_px, glyph_rects=glyph_rects)

        # Check 7: dark text sitting inside the observed band's vertical span.
        under_straddling, under_contained = [], []
        if obs_span is not None:
            y0b, y1b = obs_span
            for s in spans:
                if s["luma"] >= DARK_TEXT_LUMA_MAX:
                    continue  # reversed-out / light label on the band
                sy0, sy1 = s["rect_px"][1], s["rect_px"][3]
                if sy1 <= y0b or sy0 >= y1b:
                    continue
                if sy0 < y1b < sy1:
                    under_straddling.append(s["text"].strip())
                else:
                    under_contained.append(s["text"].strip())

        sheets.append(
            {
                "sheet": idx + 1,
                "px": [w, h],
                "ink_coverage": round(cov, 5),
                "observed_top_fill": observed_hex,
                "observed_top_fill_share": round(observed_share, 4),
                "observed_band_rows": list(obs_span) if obs_span else None,
                "declared_band_present": declared_present,
                "declared_band_rows": list(declared_span) if declared_span else None,
                "declared_band_match_fraction": (
                    round(declared_frac, 4) if declared_frac is not None else None
                ),
                "edges": edges,
                "text_straddling_band": under_straddling,
                "text_inside_band": under_contained,
            }
        )
    unique_imgs, img_placements = count_embedded_images(doc)
    page_count = len(doc)
    doc.close()
    return {
        "path": str(path),
        "page_count": page_count,
        "sheets": sheets,
        "unique_image_xrefs": unique_imgs,
        "image_placements": img_placements,
    }


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def build_report(chapter: str, generated: Path, source: Path, layout_path: Path,
                 reader_html: Path, figures_dir: Path) -> dict:
    declared_band_hex = None
    layout_note = None
    if layout_path.exists():
        try:
            layout = json.loads(layout_path.read_text())
            declared_band_hex = (
                layout.get("colors_used_by_the_book", {})
                .get("page_header_band_fill", {})
                .get("value")
            )
        except Exception as exc:  # pragma: no cover
            layout_note = f"could not read {layout_path}: {exc}"
    else:
        layout_note = f"missing {layout_path}"
    declared_band_rgb = hex_to_rgb(declared_band_hex) if declared_band_hex else None

    gen = measure_pdf(generated, declared_band_rgb, want_text_layer=True)
    src = measure_pdf(source, declared_band_rgb, want_text_layer=False)

    checks: dict[str, dict] = {}

    # 1. Sheet count -------------------------------------------------------
    delta = gen["page_count"] - src["page_count"]
    excess = delta / src["page_count"] if src["page_count"] else 0.0
    checks["sheet_count"] = {
        "status": FAIL if excess > SHEET_COUNT_EXCESS_MAX_FRACTION else PASS,
        "generated_sheets": gen["page_count"],
        "source_pages": src["page_count"],
        "delta": delta,
        "excess_fraction": round(excess, 4),
        "threshold": SHEET_COUNT_EXCESS_MAX_FRACTION,
        "hard": False,
    }

    # 2. Blank sheets (HARD) ----------------------------------------------
    blank = [s["sheet"] for s in gen["sheets"] if s["ink_coverage"] < BLANK_INK_MAX_FRACTION]
    src_blank = [s["sheet"] for s in src["sheets"] if s["ink_coverage"] < BLANK_INK_MAX_FRACTION]
    checks["blank_sheets"] = {
        "status": FAIL if blank else PASS,
        "generated_blank_sheets": blank,
        "generated_blank_count": len(blank),
        "source_blank_pages": src_blank,
        "threshold": BLANK_INK_MAX_FRACTION,
        "hard": True,
    }

    # 3. Sparse sheets -----------------------------------------------------
    sparse = [
        s["sheet"]
        for s in gen["sheets"]
        if BLANK_INK_MAX_FRACTION <= s["ink_coverage"] < SPARSE_INK_MAX_FRACTION
    ]
    src_sparse = [
        s["sheet"]
        for s in src["sheets"]
        if BLANK_INK_MAX_FRACTION <= s["ink_coverage"] < SPARSE_INK_MAX_FRACTION
    ]
    sparse_frac = len(sparse) / gen["page_count"] if gen["page_count"] else 0.0
    checks["sparse_sheets"] = {
        "status": WARN if sparse_frac > SPARSE_SHEETS_MAX_FRACTION else PASS,
        "generated_sparse_sheets": sparse,
        "generated_sparse_count": len(sparse),
        "generated_sparse_fraction": round(sparse_frac, 4),
        "source_sparse_pages": src_sparse,
        "threshold": SPARSE_SHEETS_MAX_FRACTION,
        "hard": False,
    }

    # 4. Mean ink coverage -------------------------------------------------
    gen_mean = float(np.mean([s["ink_coverage"] for s in gen["sheets"]])) if gen["sheets"] else 0.0
    src_mean = float(np.mean([s["ink_coverage"] for s in src["sheets"]])) if src["sheets"] else 0.0
    ratio = gen_mean / src_mean if src_mean else 0.0
    checks["mean_ink_coverage"] = {
        "status": WARN if ratio < MEAN_INK_MIN_RATIO_VS_SOURCE else PASS,
        "generated_mean": round(gen_mean, 5),
        "source_mean": round(src_mean, 5),
        "ratio": round(ratio, 4),
        "threshold": MEAN_INK_MIN_RATIO_VS_SOURCE,
        "hard": False,
    }

    # 5. Band at sheet top -------------------------------------------------
    if declared_band_rgb is None:
        checks["band_at_sheet_top"] = {
            "status": NOT_MEASURED,
            "reason": layout_note or "no page_header_band_fill in layout file",
            "hard": False,
        }
    else:
        gen_with = [s["sheet"] for s in gen["sheets"] if s["declared_band_present"]]
        gen_without = [s["sheet"] for s in gen["sheets"] if not s["declared_band_present"]]
        src_with = [s["sheet"] for s in src["sheets"] if s["declared_band_present"]]
        gen_frac = len(gen_with) / gen["page_count"] if gen["page_count"] else 0.0
        src_frac = len(src_with) / src["page_count"] if src["page_count"] else 0.0
        # What colour the generated sheets actually paint at the top, so a
        # wrong-colour band is reported as a mismatch rather than as "absent".
        observed = Counter(
            s["observed_top_fill"] for s in gen["sheets"] if s["observed_top_fill"]
        )
        src_observed = Counter(
            s["observed_top_fill"] for s in src["sheets"] if s["observed_top_fill"]
        )
        gen_banded_any = [s["sheet"] for s in gen["sheets"] if s["observed_band_rows"]]
        shortfall = src_frac - gen_frac
        gen_modal = observed.most_common(1)[0] if observed else (None, 0)
        if shortfall > BAND_SHEET_FRACTION_TOLERANCE:
            status = FAIL
            if gen_modal[0] and gen_modal[1] >= 0.5 * gen["page_count"]:
                reason = (
                    f"BAND_COLOUR_MISMATCH: generated sheets paint {gen_modal[0]} at the top on "
                    f"{gen_modal[1]}/{gen['page_count']} sheets, but the book's measured band fill "
                    f"is {declared_band_hex}"
                )
            else:
                reason = "BAND_MISSING: generated sheets show no header band where the book has one"
        else:
            status, reason = PASS, None
        checks["band_at_sheet_top"] = {
            "status": status,
            "reason": reason,
            "declared_band_colour": declared_band_hex,
            "generated_sheets_with_band": len(gen_with),
            "generated_sheets_without_band": gen_without,
            "generated_band_fraction": round(gen_frac, 4),
            "source_pages_with_band": len(src_with),
            "source_band_fraction": round(src_frac, 4),
            "shortfall_vs_source": round(shortfall, 4),
            "generated_sheets_with_any_top_band": len(gen_banded_any),
            "generated_observed_top_fills": observed.most_common(4),
            "source_observed_top_fills": src_observed.most_common(4),
            "threshold": BAND_SHEET_FRACTION_TOLERANCE,
            "hard": False,
        }

    # 6. Content clipped at a sheet edge (HARD, pixels only) ---------------
    clipped = []
    total_glyph_edge_px = 0
    total_raw_edge_px = 0
    for s in gen["sheets"]:
        e = s["edges"]
        gpx = e["bottom_glyph_px"] + e["right_glyph_px"]
        total_glyph_edge_px += gpx
        total_raw_edge_px += e["bottom_dark_px"] + e["right_dark_px"]
        if gpx > EDGE_GLYPH_PX_MAX:
            clipped.append(
                {
                    "sheet": s["sheet"],
                    "bottom_glyph_px": e["bottom_glyph_px"],
                    "right_glyph_px": e["right_glyph_px"],
                }
            )
    checks["content_clipped_at_edge"] = {
        "status": FAIL if clipped else PASS,
        "trim_margin_mm": TRIM_MARGIN_MM,
        "strip_px": gen["sheets"][0]["edges"]["strip_px"] if gen["sheets"] else None,
        "clipped_sheets": clipped,
        "clipped_count": len(clipped),
        "total_glyph_px_in_trim_strips": total_glyph_edge_px,
        "total_dark_px_in_trim_strips": total_raw_edge_px,
        "note": "dark pixels in the trim strip are classified by glyph box; non-glyph edge ink (bands, rules, bleeding corners) is counted separately and does not fail",
        "threshold": EDGE_GLYPH_PX_MAX,
        "hard": True,
    }

    # 7. Text under page furniture ----------------------------------------
    # Only sheets whose top band is the chapter's RUNNING band count here. A
    # spill-over sheet whose top strip happens to hold a grey box panel has no
    # header band, and text sitting in that panel is content, not an intruder.
    gen_top_fills = Counter(s["observed_top_fill"] for s in gen["sheets"] if s["observed_top_fill"])
    modal_top_fill = gen_top_fills.most_common(1)[0][0] if gen_top_fills else None
    banded = [
        s for s in gen["sheets"]
        if s["observed_band_rows"] and s["observed_top_fill"] == modal_top_fill
    ]
    sheets_with_band = len(banded)
    straddling = [
        {"sheet": s["sheet"], "text": s["text_straddling_band"][:4]}
        for s in banded if s["text_straddling_band"]
    ]
    inside_texts = Counter()
    for s in banded:
        for t in set(s["text_inside_band"]):
            if t:
                inside_texts[t] += 1
    min_sheets = max(2, RUNNING_HEADER_MIN_SHEET_FRACTION * max(1, sheets_with_band))
    running_headers = sorted(t for t, n in inside_texts.items() if n >= min_sheets)
    foreign_inside = [
        {"sheet": s["sheet"],
         "text": [t for t in s["text_inside_band"] if t and t not in running_headers]}
        for s in banded
        if [t for t in s["text_inside_band"] if t and t not in running_headers]
    ]
    if sheets_with_band == 0:
        furniture_status = NOT_MEASURED
        furniture_reason = "no top band found on any generated sheet, so there is no band span to test"
    elif straddling:
        furniture_status, furniture_reason = FAIL, "dark text crosses the band's bottom edge"
    elif foreign_inside:
        furniture_status, furniture_reason = WARN, "dark text other than the running header sits inside the band span"
    else:
        furniture_status, furniture_reason = PASS, None
    checks["text_under_furniture"] = {
        "status": furniture_status,
        "reason": furniture_reason,
        "sheets_with_measurable_band": sheets_with_band,
        "running_band_colour": modal_top_fill,
        "running_header_texts": running_headers,
        "texts_inside_band_by_sheet_count": inside_texts.most_common(6),
        "sheets_with_text_straddling_band": straddling,
        "sheets_with_foreign_text_in_band": foreign_inside,
        "hard": False,
    }

    # 8. Placeholders ------------------------------------------------------
    if not reader_html.exists():
        checks["placeholders"] = {
            "status": NOT_MEASURED,
            "reason": f"missing {reader_html}",
            "hard": False,
        }
    else:
        html = reader_html.read_text(errors="replace")
        found = sorted(set(PLACEHOLDER_RE.findall(html)))
        math_unsure = 0
        for m in MATH_CONTEXT_RE.finditer(html):
            if UNSURE_RE.search(m.group(0)):
                math_unsure += 1
        total_unsure = len(UNSURE_RE.findall(html))
        checks["placeholders"] = {
            "status": FAIL if (found or math_unsure) else PASS,
            "file": str(reader_html),
            "template_placeholders": found,
            "unsure_in_math": math_unsure,
            "unsure_total_occurrences": total_unsure,
            "hard": False,
        }

    # 9. Figure count ------------------------------------------------------
    if not figures_dir.exists():
        checks["figure_count"] = {
            "status": NOT_MEASURED,
            "reason": f"missing {figures_dir}",
            "hard": False,
        }
    else:
        crops = sorted(p.name for p in figures_dir.iterdir() if FIGURE_CROP_RE.match(p.name))
        other = sorted(
            p.name
            for p in figures_dir.iterdir()
            if p.is_file() and not FIGURE_CROP_RE.match(p.name)
        )
        fratio = gen["unique_image_xrefs"] / len(crops) if crops else 0.0
        checks["figure_count"] = {
            "status": WARN if (crops and fratio < FIGURE_PLACED_MIN_RATIO) else PASS,
            "generated_unique_images": gen["unique_image_xrefs"],
            "generated_image_placements": gen["image_placements"],
            "figure_crops_on_disk": len(crops),
            "other_files_in_figures_dir": other,
            "source_unique_images": src["unique_image_xrefs"],
            "ratio_unique_images_to_crops": round(fratio, 4),
            "threshold": FIGURE_PLACED_MIN_RATIO,
            "hard": False,
        }

    statuses = [c["status"] for c in checks.values()]
    overall = FAIL if FAIL in statuses else (WARN if WARN in statuses else PASS)

    return {
        "chapter": chapter,
        "generated_pdf": str(generated),
        "source_pdf": str(source),
        "render_dpi": RENDER_DPI,
        "overall": overall,
        "checks": checks,
        "per_sheet": [
            {
                "sheet": s["sheet"],
                "ink_coverage": s["ink_coverage"],
                "blank": s["ink_coverage"] < BLANK_INK_MAX_FRACTION,
                "sparse": BLANK_INK_MAX_FRACTION <= s["ink_coverage"] < SPARSE_INK_MAX_FRACTION,
                "declared_band_present": s["declared_band_present"],
                "observed_top_fill": s["observed_top_fill"],
                "bottom_glyph_px": s["edges"]["bottom_glyph_px"],
                "right_glyph_px": s["edges"]["right_glyph_px"],
                "bottom_dark_px": s["edges"]["bottom_dark_px"],
                "right_dark_px": s["edges"]["right_dark_px"],
                "text_straddling_band": s["text_straddling_band"],
            }
            for s in gen["sheets"]
        ],
        "source_per_page": [
            {
                "page": s["sheet"],
                "ink_coverage": s["ink_coverage"],
                "declared_band_present": s["declared_band_present"],
                "observed_top_fill": s["observed_top_fill"],
            }
            for s in src["sheets"]
        ],
    }


# --------------------------------------------------------------------------
# Printing
# --------------------------------------------------------------------------

def fmt_list(values, limit=14):
    values = list(values)
    if not values:
        return "-"
    if len(values) > limit:
        return ", ".join(str(v) for v in values[:limit]) + f", ... (+{len(values)-limit})"
    return ", ".join(str(v) for v in values)


def print_report(rep: dict) -> None:
    c = rep["checks"]
    w = 96
    print("=" * w)
    print(f"VISUAL QA  {rep['chapter']}   overall: {rep['overall']}   ({rep['render_dpi']}dpi)")
    print(f"  generated: {rep['generated_pdf']}")
    print(f"  source   : {rep['source_pdf']}")
    print("=" * w)
    print(f"{'#':<3}{'CHECK':<26}{'STATUS':<14}MEASUREMENT")
    print("-" * w)

    def row(n, name, chk, measurement):
        hard = "  (hard)" if chk.get("hard") else ""
        print(f"{n:<3}{name:<26}{chk['status'] + hard:<14}{measurement}")

    row(1, "sheet count", c["sheet_count"],
        f"generated {c['sheet_count']['generated_sheets']} vs source {c['sheet_count']['source_pages']}"
        f"  delta {c['sheet_count']['delta']:+d} ({c['sheet_count']['excess_fraction']*100:+.1f}%)"
        f"  limit +{SHEET_COUNT_EXCESS_MAX_FRACTION*100:.0f}%")

    b = c["blank_sheets"]
    row(2, "blank sheets", b,
        f"{b['generated_blank_count']} below {BLANK_INK_MAX_FRACTION*100:.1f}% ink"
        f"  [{fmt_list(b['generated_blank_sheets'])}]  (source: {fmt_list(b['source_blank_pages'])})")

    s = c["sparse_sheets"]
    row(3, "sparse sheets", s,
        f"{s['generated_sparse_count']}/{rep['checks']['sheet_count']['generated_sheets']}"
        f" below {SPARSE_INK_MAX_FRACTION*100:.0f}% ink ({s['generated_sparse_fraction']*100:.1f}%)"
        f"  [{fmt_list(s['generated_sparse_sheets'])}]  (source: {fmt_list(s['source_sparse_pages'])})")

    m = c["mean_ink_coverage"]
    row(4, "mean ink coverage", m,
        f"generated {m['generated_mean']*100:.2f}%  vs source {m['source_mean']*100:.2f}%"
        f"  ratio {m['ratio']:.2f} (min {MEAN_INK_MIN_RATIO_VS_SOURCE})")

    bd = c["band_at_sheet_top"]
    if bd["status"] == NOT_MEASURED:
        row(5, "band at sheet top", bd, bd.get("reason", ""))
    else:
        row(5, "band at sheet top", bd,
            f"declared {bd['declared_band_colour']}: {bd['generated_sheets_with_band']}/"
            f"{c['sheet_count']['generated_sheets']} generated"
            f" vs {bd['source_pages_with_band']}/{c['sheet_count']['source_pages']} source")
        print(f"{'':29}{'':14}missing on sheets: {fmt_list(bd['generated_sheets_without_band'])}")
        print(f"{'':29}{'':14}top fill observed  generated {bd['generated_observed_top_fills']}")
        print(f"{'':29}{'':14}                   source    {bd['source_observed_top_fills']}")
        if bd.get("reason"):
            print(f"{'':29}{'':14}-> {bd['reason']}")

    cl = c["content_clipped_at_edge"]
    row(6, "clipped at sheet edge", cl,
        f"{cl['clipped_count']} sheets with glyph ink in the {cl['trim_margin_mm']}mm trim strip"
        f" ({cl['strip_px']}px); glyph px total {cl['total_glyph_px_in_trim_strips']},"
        f" all dark edge px {cl['total_dark_px_in_trim_strips']}")
    for item in cl["clipped_sheets"][:12]:
        print(f"{'':29}{'':14}sheet {item['sheet']}: bottom {item['bottom_glyph_px']}px,"
              f" right {item['right_glyph_px']}px")

    f = c["text_under_furniture"]
    row(7, "text under furniture", f,
        f"band measurable on {f['sheets_with_measurable_band']} sheets;"
        f" straddling-band sheets {len(f.get('sheets_with_text_straddling_band', []))},"
        f" foreign-text-in-band sheets {len(f.get('sheets_with_foreign_text_in_band', []))}"
        + (f"; running headers {f['running_header_texts']}" if f.get("running_header_texts") else ""))
    for item in f.get("sheets_with_text_straddling_band", [])[:8]:
        print(f"{'':29}{'':14}sheet {item['sheet']}: {item['text']}")
    for item in f.get("sheets_with_foreign_text_in_band", [])[:8]:
        print(f"{'':29}{'':14}sheet {item['sheet']} foreign: {item['text']}")

    p = c["placeholders"]
    if p["status"] == NOT_MEASURED:
        row(8, "placeholders", p, p.get("reason", ""))
    else:
        row(8, "placeholders", p,
            f"@PLACEHOLDER@ {len(p['template_placeholders'])} {p['template_placeholders'] or ''}"
            f"  'unsure' in maths {p['unsure_in_math']} (total 'unsure' {p['unsure_total_occurrences']})")

    fg = c["figure_count"]
    if fg["status"] == NOT_MEASURED:
        row(9, "figure count", fg, fg.get("reason", ""))
    else:
        row(9, "figure count", fg,
            f"generated embeds {fg['generated_unique_images']} unique"
            f" ({fg['generated_image_placements']} placements) vs {fg['figure_crops_on_disk']} crops"
            f"  ratio {fg['ratio_unique_images_to_crops']:.2f} (min {FIGURE_PLACED_MIN_RATIO});"
            f" source PDF embeds {fg['source_unique_images']}")

    print("-" * w)
    print("PER SHEET")
    print(f"  {'sh':>3} {'ink%':>7} {'state':<7} {'band':<6} {'topfill':<9} {'botGlyph':>9} {'rtGlyph':>8}")
    for s in rep["per_sheet"]:
        state = "BLANK" if s["blank"] else ("sparse" if s["sparse"] else "ok")
        band = "yes" if s["declared_band_present"] else "NO"
        print(f"  {s['sheet']:>3} {s['ink_coverage']*100:>7.2f} {state:<7} {band:<6}"
              f" {str(s['observed_top_fill'] or '-'):<9} {s['bottom_glyph_px']:>9} {s['right_glyph_px']:>8}")
    print("=" * w)
    fails = [k for k, v in c.items() if v["status"] == FAIL]
    warns = [k for k, v in c.items() if v["status"] == WARN]
    nm = [k for k, v in c.items() if v["status"] == NOT_MEASURED]
    print(f"FAIL: {fmt_list(fails) if fails else 'none'}")
    print(f"WARN: {fmt_list(warns) if warns else 'none'}")
    print(f"NOT_MEASURED: {fmt_list(nm) if nm else 'none'}")


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def self_test() -> int:
    def white(h=200, w=160):
        return np.full((h, w, 3), 255, dtype=np.uint8)

    results = []

    def check(name, condition, detail=""):
        results.append((name, bool(condition), detail))

    # --- ink coverage / blank ------------------------------------------
    blank_page = white()
    cov = ink_coverage(blank_page)
    check("blank page measures ~0 ink", cov == 0.0, f"cov={cov}")
    check("blank page classified blank", cov < BLANK_INK_MAX_FRACTION, f"cov={cov}")

    inked = white()
    inked[20:120, 20:140] = 30  # 100x120 of 200x160 = 37.5%
    cov = ink_coverage(inked)
    check("dense page measures expected ink", abs(cov - 0.375) < 1e-6, f"cov={cov}")
    check("dense page not blank and not sparse",
          cov >= SPARSE_INK_MAX_FRACTION, f"cov={cov}")

    sparse = white()
    sparse[0:10, 0:64] = 30  # 640 / 32000 = 2%
    cov = ink_coverage(sparse)
    check("sparse page measures 2% ink", abs(cov - 0.02) < 1e-6, f"cov={cov}")
    check("sparse page classified sparse",
          BLANK_INK_MAX_FRACTION <= cov < SPARSE_INK_MAX_FRACTION, f"cov={cov}")

    faint = white()
    faint[:, :] = (242, 239, 231)  # near-paper tint must not count as ink
    check("near-paper tint is not ink", ink_coverage(faint) == 0.0)

    # --- band detection --------------------------------------------------
    band_hex = "#4a7435"
    band_rgb = hex_to_rgb(band_hex)
    banded = white()
    banded[2:14, 0:120] = band_rgb  # 12 rows, 75% of width, inside top 8% (16 rows)
    present, span, frac = band_rows_for_colour(banded, band_rgb)
    check("coloured top strip detected as banded", present, f"span={span} frac={frac}")
    check("band row span is the painted rows", span == (2, 14), f"span={span}")

    present2, _, _ = band_rows_for_colour(white(), band_rgb)
    check("plain white page is not banded", not present2)

    # renderer rounding must still match
    rounded = white()
    rounded[2:14, 0:120] = hex_to_rgb("#4a7333")
    present3, _, _ = band_rows_for_colour(rounded, band_rgb)
    check("band matches through renderer rounding", present3)

    # a different colour must NOT match the declared band
    wrong = white()
    wrong[2:14, 0:120] = hex_to_rgb("#00acef")
    present4, _, _ = band_rows_for_colour(wrong, band_rgb)
    check("wrong-colour band does not match declared colour", not present4)
    obs_hex, obs_share = dominant_top_fill(wrong)
    check("wrong-colour band still reported as observed top fill",
          obs_hex == "#00acef", f"obs={obs_hex} share={obs_share}")

    # a 1px rule must not be called a band
    rule = white()
    rule[5:6, :] = band_rgb
    present5, _, _ = band_rows_for_colour(rule, band_rgb)
    check("1px rule is not a band", not present5)

    # a band painted below the top strip must not count
    low = white()
    low[100:120, 0:120] = band_rgb
    present6, _, _ = band_rows_for_colour(low, band_rgb)
    check("band outside the top strip is not counted", not present6)

    obs_none, _ = dominant_top_fill(white())
    check("white page has no observed top fill", obs_none is None)

    # --- clipping --------------------------------------------------------
    strip = max(1, int(round(TRIM_MARGIN_MM * RENDER_DPI / 25.4)))

    clean = white()
    clean[20:120, 20:140] = 30
    e = edge_ink(clean, strip, glyph_rects=[(20, 20, 140, 120)])
    check("page with ink away from the edges is not clipped",
          e["bottom_glyph_px"] == 0 and e["right_glyph_px"] == 0, str(e))

    bottom_clip = white()
    bottom_clip[190:200, 40:100] = 30  # ink in the last 10 rows
    e = edge_ink(bottom_clip, strip, glyph_rects=[(40, 150, 100, 200)])
    check("ink at the bottom edge detected as clipped",
          e["bottom_glyph_px"] > EDGE_GLYPH_PX_MAX, str(e))

    right_clip = white()
    right_clip[40:100, 152:160] = 30
    e = edge_ink(right_clip, strip, glyph_rects=[(100, 40, 160, 100)])
    check("ink at the right edge detected as clipped",
          e["right_glyph_px"] > EDGE_GLYPH_PX_MAX, str(e))

    # furniture bleeding to the edge is measured but not called a glyph
    furniture = white()
    furniture[190:200, :] = 30
    e = edge_ink(furniture, strip, glyph_rects=[(20, 20, 140, 120)])
    check("edge furniture counted as dark ink but not as glyph ink",
          e["bottom_dark_px"] > 0 and e["bottom_glyph_px"] == 0, str(e))

    # light furniture at the edge is not even dark ink
    light_edge = white()
    light_edge[190:200, :] = hex_to_rgb("#c6eafb")
    e = edge_ink(light_edge, strip, glyph_rects=None)
    check("light fill at the edge is not glyph-dark ink", e["bottom_dark_px"] == 0, str(e))

    # with no glyph rects supplied, glyph counts fall back to raw dark counts
    e = edge_ink(bottom_clip, strip, glyph_rects=None)
    check("no text layer -> glyph count falls back to dark count",
          e["bottom_glyph_px"] == e["bottom_dark_px"] > 0, str(e))

    # --- placeholders ----------------------------------------------------
    check("placeholder regex finds @FOO_BAR@",
          PLACEHOLDER_RE.findall("x @CHAPTER_TITLE@ y") == ["@CHAPTER_TITLE@"])
    check("placeholder regex ignores plain text",
          PLACEHOLDER_RE.findall("email@example.com and @a@") == [])
    math_hit = [m.group(0) for m in MATH_CONTEXT_RE.finditer(r"text \(unsure\) z")]
    check("unsure inside \\( \\) seen as maths",
          any(UNSURE_RE.search(h) for h in [m for m in math_hit]) or
          any(UNSURE_RE.search(m.group(0)) for m in MATH_CONTEXT_RE.finditer(r"a \(unsure\) b")),
          str(math_hit))
    check("unsure inside a math span seen as maths",
          any(UNSURE_RE.search(m.group(0))
              for m in MATH_CONTEXT_RE.finditer('<span class="math">unsure</span>')))

    # --- figure crop naming ----------------------------------------------
    check("figure crop pattern matches p002_b3.png", bool(FIGURE_CROP_RE.match("p002_b3.png")))
    check("figure crop pattern rejects _corner.png", not FIGURE_CROP_RE.match("_corner.png"))

    width = max(len(n) for n, _, _ in results) + 2
    failed = 0
    for name, ok, detail in results:
        if not ok:
            failed += 1
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<{width}}{'' if ok else detail}")
    print(f"\nself-test: {len(results) - failed}/{len(results)} passed")
    return 0 if failed == 0 else 1


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("chapter", nargs="?", help="chapter id, e.g. PHY12O-ch01")
    ap.add_argument("--generated", help="path to the generated chapter PDF")
    ap.add_argument("--source", help="path to the source NCERT chapter PDF")
    ap.add_argument("--layout", help="override the measured layout json path")
    ap.add_argument("--reader-html", help="override the READER.html path")
    ap.add_argument("--figures-dir", help="override the figures directory")
    ap.add_argument("--json", action="store_true", help="emit a machine-readable dict")
    ap.add_argument("--self-test", action="store_true",
                    help="run the measurement helpers against synthetic images and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    if not args.chapter or not args.generated or not args.source:
        ap.error("CHAPTER, --generated and --source are required (or use --self-test)")

    chapter = args.chapter
    generated = Path(args.generated)
    source = Path(args.source)
    for p in (generated, source):
        if not p.exists():
            print(f"ERROR: missing PDF {p}", file=sys.stderr)
            return 2

    layout = Path(args.layout) if args.layout else Path(
        f"exports/review/html_data/{chapter}_layout.json")
    reader_html = Path(args.reader_html) if args.reader_html else Path(
        f"exports/chapters/{chapter}/{chapter}_READER.html")
    figures_dir = Path(args.figures_dir) if args.figures_dir else Path(
        f"exports/chapters/{chapter}/figures")

    rep = build_report(chapter, generated, source, layout, reader_html, figures_dir)

    if args.json:
        print(json.dumps(rep, indent=2))
    else:
        print_report(rep)

    return 1 if rep["overall"] == FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
