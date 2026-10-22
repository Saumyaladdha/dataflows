#!/usr/bin/env python3
"""The shared page-layout engine for NCERT CHEMISTRY CLASS 12, plus the inorganic entry point.

This module measures and lays out THE BOOK, not a branch of chemistry. Unit 5 (inorganic) and
Unit 9 (organic) are printed from the same design -- one trim, one palette, one furniture set, one
column system, one panel design -- so everything about the PAGE lives here and is shared, and only
the CHEMISTRY differs per subject.

Subject flows attach through `HOOKS` and supply their own main():

    export_inorganic_chemistry_html.py   coordination diagrams, cropped from the page
    export_organic_chemistry_html.py     ring structures as SVG, reactions as live mathematics

It was originally written for Unit 5 and named for it, which was misleading the moment organic
reused it: a fix for an organic defect usually lands here, and reading the filename it looked like
a change to inorganic. The name now says what the code is, and the two subject entry points are
separate files so neither can quietly edit the other.

Original docstring follows.

Builds the Markdown and HTML renders of one NCERT INORGANIC CHEMISTRY chapter.

    python3 scripts/export_inorganic_chemistry_html.py CHE12L-ch05 \\
        --pdf inputs/ncert/latest/Class_12th/Chemistry/Chapter_5.pdf

Writes, under `exports/review/`:

    <CHAPTER>_INORGANIC.md              the chapter as Markdown, with its structure named
    <CHAPTER>_inorg_figures/*.png       diagram crops -- WATERMARK-FREE (see below)
    html/<CHAPTER>_INORG_READER.html    the chapter as the book sets it
    html_data/<CHAPTER>_inorganic_layout.json   written by the measurement step

WHY THIS IS A SEPARATE FLOW
---------------------------
`export_ncert_chapter_html.py` keeps every per-subject difference in one `_SUBJECT_PROFILES`
table keyed by the chapter id's first three letters. That key cannot tell organic chemistry from
inorganic -- both are `CHE` -- and the entry it holds is a copy of Biology's defaults: A4 sheet,
no furniture, no panels, continuous flow. Rendering Coordination Compounds through it produced a
page with the wrong trim, no folio, no worked-example panels and no Summary.

Fixing that in place would mean either changing `CHE` (which re-renders the organic chapters that
were already approved) or adding a fourth profile key the table has no way to select. So this is
its own module. It REUSES everything that is genuinely shared -- the A2/A2S/A2B/A2N loaders, the
PDF helpers, the chapter model -- and shares no layout code at all, which is the only way a
change made for this book cannot reach Biology or Physics.

WHAT IS DIFFERENT ABOUT THIS BOOK, AND WHAT THAT BUYS
-----------------------------------------------------
The latest-edition Chemistry PDFs are not scans. They carry a real text layer and a real vector
layer, and three things follow that no scan-based flow can do:

  1. EQUATIONS AND FORMULAE ARE SET AS TEXT, NOT SHIPPED AS SCREENSHOTS. NCERT prints
     `[Co(NH3)6]3+` as five spans at three point sizes on three baselines. A flattened text layer
     loses that and reads "[Co(NH3)6]3+", which is why chemistry has always come out with its
     subscripts inlined and its displayed working cropped to a picture. The measurement keeps
     each span's size and baseline, so the real sub/superscript structure is recovered and set as
     live, selectable, searchable text. Only genuine DIAGRAMS are cropped.

  2. THE CROPS CARRY NO WATERMARK. `(c) NCERT / not to be republished` is a separate image object
     here, not ink burned into a bitmap, so it is removed before a figure is rendered. Every
     other flow in this project has to state in its README that its crops carry the mark; this
     one does not.

  3. THE LAYOUT IS MEASURED, NOT ESTIMATED, AND COVERS EVERY PAGE. See
     scripts/inorganic_chemistry_measure.py.
"""

import argparse
import datetime
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys

import pymupdf as fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import chemistry_model as model_mod  # noqa: E402
from chemistry_measure import measure as measure_pdf  # noqa: E402

_FIG_DPI = 300          # diagram crops: vector art, so this is sharp rather than merely big
# The type is never trimmed below this to make a page fit. A reflowed render of a hand-set book
# runs 10-25% longer for the same words -- the publisher breaks lines and places figures by hand
# -- and chasing that with type size took the page to 80% of the book's, at which point it no
# longer looks like the book, which was the entire objective. Below this floor a sheet is allowed
# to continue onto a second printed page instead: nothing is clipped and the build says which.
_FIT_FLOOR = 0.80
_CROP_PAD = 0.004       # a hair of air around a cropped diagram, as a fraction of the sheet


# --------------------------------------------------------------------------------------------
# Typed text -> Markdown and HTML
# --------------------------------------------------------------------------------------------
_SUB_UNICODE = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
                "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋", "−": "₋",
                "(": "₍", ")": "₎", "a": "ₐ", "e": "ₑ", "o": "ₒ", "x": "ₓ",
                "h": "ₕ", "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "p": "ₚ",
                "s": "ₛ", "t": "ₜ"}
_SUP_UNICODE = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
                "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻", "−": "⁻",
                "(": "⁽", ")": "⁾", "n": "ⁿ", "i": "ⁱ"}


# LaTeX that is nothing but prose in a \text{} wrapper is not an equation.
#
# A2S sometimes transcribes an equation block by copying the nearest words instead -- on Amines
# p022 two blocks came back as `\text{Answers to Some Intext Questions}`, the heading printed
# beside them. Rendered as display mathematics that printed the chapter's heading three times in
# a row, which reads as corruption. A real displayed reaction in this book always carries an
# operator, an arrow, a charge or a script; prose in a box carries none.
_UNREADABLE_LATEX = ("unsure", "unsure.", "n/a", "none", "-")
# A vertical bond is a DRAWING, not mathematics.
#
# NCERT writes an amide as the carbon with an O stacked above it on a double bond, and A2S
# transcribes that as \overset{\text{O}}{\overset{\|}{\text{C}}}. KaTeX lays it out as linear
# maths, so it prints as "C2H5 - N - C - CH3 + H - Cl" with the substituents collapsed underneath
# and the bonds lost -- which is not the molecule. A charge (\overset{+}{N}) is fine and stays as
# mathematics; a stacked BOND is a two-dimensional structure and belongs in the artwork.
_BOND_2D = re.compile(r"\\\||\\parallel")


def is_two_d_structure(latex):
    return bool(_BOND_2D.search(latex or ""))


_MATHY = ("xrightarrow", "rightarrow", "longrightarrow", "\\to", "\\ce",
          "overset", "underset", "frac", "equiv", "rightleftharpoons",
          "^", "_", "=", "+", "Delta", "alpha", "beta")


def _is_prose_not_maths(latex):
    """True when this `latex` is a mis-transcription: words, with nothing mathematical in them."""
    t = (latex or "").strip()
    if not t:
        return False
    if any(tok in t for tok in _MATHY):
        return False
    stripped = re.sub(r"\\text\{([^{}]*)\}", r"\1", t)
    stripped = re.sub(r"[\\{}$]", "", stripped).strip()
    return bool(stripped) and bool(re.fullmatch(r"[A-Za-z0-9 ,.'\-]+", stripped))


def _is_real_latex(latex):
    """True when this is something worth setting as mathematics."""
    t = (latex or "").strip()
    if not t or t.lower().rstrip(".") in _UNREADABLE_LATEX:
        return False
    return not _is_prose_not_maths(latex)


def _esc(s):
    return html.escape(s or "", quote=False)


def runs_to_markdown(runs):
    """Typed runs as Markdown.

    Sub/superscripts are written as the real Unicode characters where they exist, because for
    this book they almost always do -- chemistry's scripts are digits, charges and brackets -- and
    `[Co(NH₃)₆]³⁺` survives being pasted anywhere, which `[Co(NH<sub>3</sub>)<sub>6</sub>]` does
    not. The HTML tag is used only for the handful of letters Unicode has no script form for, so
    nothing is ever silently flattened.
    """
    out = []
    for r in runs:
        text, variant, bold = r["t"], r.get("v", ""), r.get("b")
        if variant in ("sub", "sup"):
            table = _SUB_UNICODE if variant == "sub" else _SUP_UNICODE
            if all(ch in table or ch.isspace() for ch in text):
                text = "".join(table.get(ch, ch) for ch in text)
            else:
                text = "<%s>%s</%s>" % (variant, text, variant)
        if r.get("i") and text.strip():
            text = "*%s*" % text
        if bold:
            text = "**%s**" % text if text.strip() else text
        out.append(text)
    return "".join(out)


def runs_to_html(runs):
    """Typed runs as HTML.

    Carries everything the book sets and the measurement recorded: real <sub>/<sup>, <strong> for
    bold runs, <em> for italics (which are meaning in chemistry -- `n-`, `o-`, `p-`, `in situ`,
    `ortho` -- not decoration), and the book's own colour coding, where an amino group is magenta
    and a halogen or leaving group green so a reader can see which part of the molecule reacts.
    """
    out = []
    for r in runs:
        frag = _esc(r["t"])
        variant = r.get("v", "")
        if variant in ("sub", "sup"):
            frag = "<%s>%s</%s>" % (variant, frag, variant)
        if r.get("i") and r["t"].strip():
            frag = "<em>%s</em>" % frag
        if r.get("c") and r["t"].strip():
            frag = '<span style="color:%s">%s</span>' % (r["c"], frag)
        if r.get("b") and r["t"].strip():
            frag = "<strong>%s</strong>" % frag
        out.append(frag)
    return "".join(out)


def _plain(runs):
    return "".join(r["t"] for r in runs)


# --------------------------------------------------------------------------------------------
# Diagram crops
# --------------------------------------------------------------------------------------------
def _page_without_overlays(doc, page_num, overlays):
    """One page with its watermark and paper background removed.

    This is the step that makes a chemistry crop clean. `(c) NCERT / not to be republished` is an
    ordinary image object on these PDFs, repeated at the same rectangle on every page -- which is
    how the measurement identifies it without being told. Deleting it before rendering gives a
    diagram with nothing across it; the Biology and Physics flows cannot do this because their
    sources are flat scans with the mark baked into the only raster on the page.
    """
    page = doc[page_num - 1]
    w, h = page.rect.width, page.rect.height
    for im in page.get_image_info(xrefs=True):
        r = fitz.Rect(im["bbox"])
        frac = [r.x0 / w, r.y0 / h, r.x1 / w, r.y1 / h]
        if _is_overlay(frac, overlays):
            try:
                page.delete_image(im["xref"])
            except Exception:
                pass          # the crop is still usable; it just keeps the mark
    return page


def build_label_vectors(pdf_path, m, measurement, fig_dir):
    """Write each panel label ("Example 9.3", "Solution", "Summary", "Objectives") as vector.

    Padded generously and taken straight from the page: these sit alone in white space, so a loose
    crop costs nothing, and the CropBox offset that used to cut every crop on this book is fixed.
    """
    overlays = measurement.get("page_overlays_ignored") or []
    out = {}
    for page in m["pages"]:
        for it in page["items"]:
            it["_page"] = page["page"]
            lb = it.get("label_bbox")
            if not lb:
                continue
            name = "label_p%03d_b%s.svg" % (page["page"], it["n"])
            box = [max(0.0, lb[0] - 0.006), max(0.0, lb[1] - 0.010),
                   min(1.0, lb[2] + 0.010), min(1.0, lb[3] + 0.012)]
            if svg_region(pdf_path, page["page"], box, os.path.join(fig_dir, name),
                          overlays, pad=0.0):
                out[(page["page"], it["n"])] = name
    return out


def _heading_box(bbox, measurement):
    """A section heading's PRINTED extent, which is wider and taller than its measured box.

    The display face draws each glyph several times at sub-point offsets and hangs swashes below
    the baseline, and neither is inside the box the text layer reports -- so cropping to that box
    cut the right-hand edge and the last line off every heading in the chapter ("5.1 Werner's
    Theory of Coordinat"). The margin column is otherwise white, so taking its full width and
    padding the height costs nothing and cannot clip.
    """
    tm = measurement.get("text_measure") or {}
    margin = tm.get("margin_column") or [0.07, 0.29]
    # The right bound is where the BODY COLUMN starts, not where the margin column was measured
    # to end. A heading's swash can overhang the measured column by a few thousandths, which was
    # still enough to shave the last letter off "Coordination" and "Nomenclature".
    # A fixed overshoot, not a measured bound. The chapter-level body column's left edge is the
    # minimum across every page, so on a chapter with two-column pages it sits well left of the
    # text measure and is useless as a right bound here. The margin is white either side of a
    # heading, so overshooting into it cannot pick anything up and cannot clip.
    x0 = min(bbox[0], margin[0]) - 0.010
    x1 = max(bbox[2] + 0.055, margin[1] + 0.020)
    return [max(0.0, x0), max(0.0, bbox[1] - 0.012), min(1.0, x1), min(1.0, bbox[3] + 0.028)]


def _page_prose(measurement, page_num, body_left):
    """Everything on this page a figure crop must NOT swallow.

    Three kinds, all of which were observed inside crops:
      * BODY PROSE in the text column -- NCERT wraps it around a marginal diagram, so the tail of
        a line reaches into the diagram's region (p004's "ligands. Ligand");
      * the FIGURE'S OWN PRINTED CAPTION -- the exporter already sets that as text beneath the
        artwork, so leaving it in the crop printed it twice (Figs 5.3, 5.5, 5.7, 5.12);
      * PAGE FURNITURE -- the folio and running header, which a crop reaching low on the page
        picks up (Fig 5.7 carried "Chemistry 126" inside it).
    """
    rec = next((p for p in measurement["pages"] if p["page"] == page_num), None)
    if not rec:
        return []
    out = []
    for tb in rec.get("text_blocks", []):
        role = tb.get("role")
        for ln in tb.get("lines", []):
            # A line is PROSE if it starts at the text measure -- that is what a paragraph does
            # and what a figure's own label never does. Width alone was the wrong test: it kept
            # full lines but dropped the SHORT LAST LINE of a paragraph, which is exactly the
            # fragment that ends up sitting against a figure ("the anion formed by phthalimide.").
            # Centred labels under a structure start wherever the structure does, so they are
            # left alone.
            x0, x1 = ln["bbox"][0], ln["bbox"][2]
            at_measure = abs(x0 - body_left) < 0.035 or abs(x0 - (body_left + 0.03)) < 0.02
            if role in ("body", "demi", "italic") and (at_measure or (x1 - x0) > 0.30):
                out.append(ln)
            # NOT caption-role lines in general: a figure's own internal labels are set in the
            # same face and size as a caption, so redacting the role wholesale stripped the row
            # labels out of the orbital diagrams on pp.129-130. Only the specific caption lines
            # of the figure being cropped are removed, and the caller passes those explicitly.
            elif role == "imprint" or ln["bbox"][1] > 0.895:
                out.append(ln)            # folio, running header, print-year line
    return out


def _is_overlay(frac, overlays, tol=0.02):
    for o in overlays:
        if all(abs(a - b) <= tol for a, b in zip(frac, o)):
            return True
    return False


def svg_region(pdf_path, page_num, bbox_frac, out_path, overlays, pad=0.004,
               prose_lines=(), keep=()):
    """Write one region of a page as a true SVG -- vector, not a picture of vector.

    Used for the book's DISPLAY FACES. NCERT sets its section headings, its chapter title and its
    worked-example labels in three proprietary faces (a brush script, a shaded display roman, a
    Garamond cut). None of them can be licensed into this export, and substituting the nearest
    widely-available face gets the class right and the letterforms wrong -- a thin formal
    copperplate where the book prints a round casual brush, which is visibly not the same book.

    Taking the region as vector sidesteps the substitution entirely: these are the book's own
    outlines at any zoom, with no font to install and nothing to approximate. `text_as_path=1`
    converts the glyphs to outlines, so the shapes do not depend on a font being present; the
    words are kept searchable by the caller, which prints them as text alongside.
    """
    doc = fitz.open(pdf_path)
    try:
        page = doc[page_num - 1]
        w, h = page.rect.width, page.rect.height
        for im in page.get_image_info(xrefs=True):
            r = fitz.Rect(im["bbox"])
            if _is_overlay([r.x0 / w, r.y0 / h, r.x1 / w, r.y1 / h], overlays):
                try:
                    page.delete_image(im["xref"])
                except Exception:
                    pass
        clip = fitz.Rect(max(0.0, bbox_frac[0] - pad) * w, max(0.0, bbox_frac[1] - pad) * h,
                         min(1.0, bbox_frac[2] + pad) * w, min(1.0, bbox_frac[3] + pad) * h)
        if clip.width < 2 or clip.height < 2:
            return False
        keep_boxes = [tuple(round(v, 4) for v in k) for k in keep]
        redacted = False
        for lb in prose_lines:
            if tuple(round(v, 4) for v in lb) in keep_boxes:
                continue
            r = fitz.Rect(lb[0] * w, lb[1] * h, lb[2] * w, lb[3] * h)
            if r.intersects(clip):
                page.add_redact_annot(r, fill=(1, 1, 1))
                redacted = True
        if redacted:
            try:
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
            except Exception:
                pass
        # set_cropbox() takes MEDIABOX coordinates; page.rect is in CROPBOX coordinates. On this
        # book the CropBox is inset (18, 18) from the MediaBox, so a clip computed from page.rect
        # and handed straight to set_cropbox landed 36pt too high -- about two lines of type --
        # and every figure crop in the chapter carried the tail of the paragraph above it.
        #
        # This was the single cause behind eleven failed attempts to fix those crops by adjusting
        # the box: the box was right every time and the frame it was applied in was not.
        off = page.cropbox_position
        page.set_cropbox(clip + (off.x, off.y, off.x, off.y))
        svg = page.get_svg_image(text_as_path=1)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(svg)
        return True
    except Exception:
        return False
    finally:
        doc.close()


def _trim_edge_rules(path):
    """Shave a border rule off a saved crop.

    A rule is a line of pixels that is almost entirely ONE tone and is not white -- the hairline
    round a panel, or the salmon rule under a heading. Artwork never fills a whole edge with a
    single tone, so this cannot eat a drawing: it stops at the first row or column that varies.
    """
    try:
        from PIL import Image
    except ImportError:
        return
    try:
        im = Image.open(path).convert("RGB")
    except OSError:
        return
    w, h = im.size
    if w < 24 or h < 24:
        return
    px = im.load()

    def flat(seq):
        vals = list(seq)
        if not vals:
            return False
        if all(min(v) > 244 for v in vals):
            return False                      # bare paper, not a rule
        r = [v[0] for v in vals]; g = [v[1] for v in vals]; b = [v[2] for v in vals]
        return (max(r) - min(r) < 26 and max(g) - min(g) < 26 and max(b) - min(b) < 26)

    step = max(1, w // 120)
    top, bottom, left, right = 0, h, 0, w
    while top < h // 8 and flat(px[x, top] for x in range(0, w, step)):
        top += 1
    while bottom > h - h // 8 and flat(px[x, bottom - 1] for x in range(0, w, step)):
        bottom -= 1
    stepy = max(1, h // 120)
    while left < w // 8 and flat(px[left, y] for y in range(top, bottom, stepy)):
        left += 1
    while right > w - w // 8 and flat(px[right - 1, y] for y in range(top, bottom, stepy)):
        right -= 1
    if (right - left) > w * 0.5 and (bottom - top) > h * 0.5 and (
            top or left or bottom != h or right != w):
        im.crop((left, top, right, bottom)).save(path)


def crop_diagram(doc, page_num, bbox_frac, out_path, overlays, prose_lines=(), keep=()):
    """Render one diagram region to PNG, watermark removed, at _FIG_DPI.

    `prose_lines` are the fractional bboxes of BODY PROSE on this page. They are painted out
    before the crop, because NCERT wraps its prose around a marginal diagram and the last words of
    a line routinely reach into the diagram's own region: p004's nitrito-N/nitrito-O crop caught
    the tail "ligands. Ligand" from the paragraph above it, which then printed inside the figure
    AND again in its own paragraph, reading as duplicated text. A figure's own labels
    ("nitrito-N", "thiocyanato-S") are not prose and are not painted out -- they are part of the
    artwork and the caller only passes lines set in the body column.
    """
    page = _page_without_overlays(doc, page_num, overlays)
    w, h = page.rect.width, page.rect.height
    # NEVER paint out a line that belongs to THIS block. The first version redacted every body
    # line overlapping the crop, which for p002's tabulated "1 mol CoCl3.6NH3 (Yellow) gave 3 mol
    # AgCl" rows meant erasing the block's entire content: the crop came out a blank 2 KB image.
    keep_boxes = [tuple(round(v, 4) for v in k) for k in keep]
    for lb in prose_lines:
        if tuple(round(v, 4) for v in lb) in keep_boxes:
            continue
        rect = fitz.Rect(lb[0] * w, lb[1] * h, lb[2] * w, lb[3] * h)
        if rect.intersects(fitz.Rect(bbox_frac[0] * w, bbox_frac[1] * h,
                                     bbox_frac[2] * w, bbox_frac[3] * h)):
            page.add_redact_annot(rect, fill=(1, 1, 1))
    if prose_lines:
        try:
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        except Exception:
            pass          # the crop is still usable, it just keeps the stray words
    x0 = max(0.0, bbox_frac[0] - _CROP_PAD) * w
    y0 = max(0.0, bbox_frac[1] - _CROP_PAD) * h
    x1 = min(1.0, bbox_frac[2] + _CROP_PAD) * w
    y1 = min(1.0, bbox_frac[3] + _CROP_PAD) * h
    if x1 - x0 < 2 or y1 - y0 < 2:
        return False
    pix = page.get_pixmap(dpi=_FIG_DPI, clip=fitz.Rect(x0, y0, x1, y1))
    pix.save(out_path)
    _trim_edge_rules(out_path)
    return True


# --------------------------------------------------------------------------------------------
# MARKDOWN
# --------------------------------------------------------------------------------------------
# Roles that open a fenced region in the Markdown. The fence exists so the structure the book
# prints survives the round trip: a reader sees a labelled block, and a tool reading the file back
# can tell a worked example from the prose beside it without guessing from punctuation.
_MD_FENCES = {
    "objectives": "objectives",
    "example": "example",
    "solution": "solution",
    "example_body": "example",
    "scientist": "scientist",
    "feature": "feature",
    "summary": "summary",
    "summary_body": "summary",
    "intext": "intext-questions",
    "note": "note",
}

_MD_HEAD = """# {chapter} — {title}

Inorganic Chemistry, rendered from this pipeline's extracted data (steps A2/A2S/A2B/A2N) with the
printed layout measured directly from the source PDF's text and vector layer.

- source: `{pdf}`
- sheet: {w_mm} × {h_mm} mm ({w_pt} × {h_pt} pt) — **not A4**
- body type: {body_pt} pt
- pages: {pages}

Formulae are set as real text: `[Co(NH₃)₆]³⁺`, not a picture of it. Sub- and superscripts are
recovered from the source's own span sizes and baselines, so they are searchable and copyable.
Only genuine **diagrams** are images, and those carry **no watermark** — on this book the
`© NCERT / not to be republished` mark is a separate object and is removed before rendering.

---
"""


def build_markdown(m, chapter, title, pdf_path, fig_dir_name, figures):
    out = [_MD_HEAD.format(
        chapter=chapter, title=title, pdf=os.path.basename(pdf_path),
        w_mm=m["trim_mm"][0], h_mm=m["trim_mm"][1],
        w_pt=m["trim_pt"][0], h_pt=m["trim_pt"][1],
        body_pt=m["body_size_pt"], pages=len(m["pages"]))]

    open_fence = None
    for page in m["pages"]:
        if open_fence:
            out.append(":::")
            open_fence = None
        head = "## Page %03d" % page["page"]
        bits = []
        if page["folio"]:
            bits.append("folio %s" % page["folio"])
        if page["running_header"]:
            bits.append(page["running_header"])
        if page["continues"]:
            bits.append("continues from the previous page")
        if bits:
            head += "  ·  " + "  ·  ".join(bits)
        out.append("\n" + head + "\n")

        for it in page["items"]:
            role, runs = it["role"], it["runs"]
            fence = _MD_FENCES.get(role)
            if open_fence and fence != open_fence:
                out.append(":::")
                open_fence = None
            if fence and not open_fence:
                label = (" " + it["label"]) if it["label"] else ""
                out.append("::: %s%s" % (fence, label))
                open_fence = fence

            if role == "chapter_title":
                lines = it["text"].split("\n")
                out.append("\n# %s\n" % " — ".join(s.strip() for s in lines if s.strip()))
            elif role == "margin_heading":
                out.append("\n## %s\n" % _plain(runs).replace("\n", " ").strip())
                out.append("*(printed in the outer margin, in the book's script face)*\n")
            elif role == "sub_heading":
                out.append("\n### %s\n" % _plain(runs).replace("\n", " ").strip())
            elif role == "letter_heading":
                out.append("\n#### %s\n" % _plain(runs).replace("\n", " ").strip())
            elif role == "strapline":
                out.append("\n*%s*\n" % runs_to_markdown(runs).replace("\n", " ").strip())
            elif role in ("run_in_heading", "exercises_heading", "answers_heading"):
                out.append("\n### %s\n" % _plain(runs).replace("\n", " ").strip())
            elif role == "table":
                out.append(_md_table(it, page["page"], fig_dir_name, figures))
            elif role == "figure":
                out.append(_md_figure(it, page["page"], fig_dir_name, figures))
            elif role == "equation":
                out.append(_md_equation(it))
            elif role == "list":
                body = runs_to_markdown(runs)
                out.append("\n" + "  \n".join(ln for ln in body.split("\n")) + "\n")
            else:
                body = runs_to_markdown(runs)
                if role in ("objectives", "example", "solution", "summary", "intext",
                            "scientist", "feature", "note", "example_body", "summary_body"):
                    body = "  \n".join(body.split("\n"))
                out.append("\n" + body + "\n")
            if it.get("notation_corrected"):
                out.append("*(notation corrected by A2N)*\n")

    if open_fence:
        out.append(":::")
    return "\n".join(out) + "\n"


def _md_table(it, page_num, fig_dir_name, figures):
    header, rows = it.get("header") or [], it.get("rows") or []
    if header:
        # Cells are re-typed from the book's own glyphs here too, so the Markdown carries
        # `PdCl₂.4NH₃` rather than `PdCl2.4NH3`. The HTML and the Markdown must not disagree
        # about what the page says -- that is the whole reason both are rendered from one model.
        stream = _cell_stream(it)

        def cell(c):
            return _typed_cell(c, stream, to_markdown=True).replace("|", "\\|")

        lines = ["", "| " + " | ".join(cell(c) for c in header) + " |",
                 "|" + "---|" * len(header)]
        for r in rows:
            lines.append("| " + " | ".join(cell(c) for c in r) + " |")
        lines.append("")
        return "\n".join(lines)
    key = (page_num, it["n"])
    if key in figures:
        return "\n![table, page %d block %s](%s/%s)\n" % (page_num, it["n"], fig_dir_name,
                                                          figures[key])
    return "\n*(table on page %d block %s — not transcribed by A2S and no region to crop)*\n" % (
        page_num, it["n"])


def _md_figure(it, page_num, fig_dir_name, figures):
    extra = HOOKS.get("md_figure")
    tail = extra(it, page_num) if extra else ""
    key = (page_num, it["n"])
    caption = (it.get("caption") or "").strip()
    parts = []
    if key in figures:
        parts.append("\n![%s](%s/%s)\n" % (caption or "figure page %d block %s" % (page_num, it["n"]),
                                           fig_dir_name, figures[key]))
    else:
        parts.append("\n*(figure on page %d block %s — no artwork region found to crop)*\n"
                     % (page_num, it["n"]))
    if caption:
        parts.append("***%s***\n" % caption)
    labels = it.get("labels") or []
    if labels:
        parts.append("*labels:* %s\n" % ", ".join(labels))
    if not caption and not it.get("untranscribed"):
        parts.append("*(no caption printed on this figure)*\n")
    if tail:
        parts.append(tail)
    return "\n".join(parts)


def _md_equation(it):
    """A displayed equation as TEXT.

    The order is deliberate. A2S's LaTeX is preferred when it exists, because it is an explicit
    transcription. Failing that the measured runs are used -- the book's own characters with their
    real sub/superscripts -- which is still text and still searchable. An image is never produced
    for an equation: a cropped picture of `E = hv` is unreadable at a glance, cannot be copied and
    cannot be searched, and this book's text layer makes it unnecessary.
    """
    latex = (it.get("latex") or "").strip()
    if latex and latex.lower().rstrip(".") not in ("unsure", "n/a", "none", "-"):
        return "\n$$%s$$\n" % latex
    body = runs_to_markdown(it["runs"]).strip()
    if body:
        return "\n> %s\n" % "  \n> ".join(body.split("\n"))
    return "\n*(equation, block %s — not transcribed and no text layer under it)*\n" % it["n"]


# --------------------------------------------------------------------------------------------
# HTML
# --------------------------------------------------------------------------------------------
# The stylesheet is a template with @TOKENS@ filled from the measurement, never from constants:
# the trim, the body size, the leading, the two column widths and every ink are this chapter's
# own numbers. Nothing here is shared with the Biology or Physics stylesheet, by design.
_CSS = r"""
@font-face { font-family: "NCERTBookman"; font-style: normal; font-weight: 400;
             src: url("fonts/texgyrebonum-regular.otf") format("opentype"); }
@font-face { font-family: "NCERTBookman"; font-style: italic; font-weight: 400;
             src: url("fonts/texgyrebonum-italic.otf") format("opentype"); }
@font-face { font-family: "NCERTBookman"; font-style: normal; font-weight: 700;
             src: url("fonts/texgyrebonum-bold.otf") format("opentype"); }
@font-face { font-family: "NCERTBookman"; font-style: italic; font-weight: 700;
             src: url("fonts/texgyrebonum-bolditalic.otf") format("opentype"); }

:root {
  --sheet-w: @SHEET_W@mm;
  --sheet-h: @SHEET_H@mm;
  --body-pt: @BODY_PT@pt;
  --page-zoom: @ZOOM@;
  --leading: @LEADING@;
  --edge-l: @EDGE_L@mm;        /* outer edge of the margin column */
  --margin-w: @MARGIN_W@mm;    /* the script-heading / marginal-figure column */
  --gutter: @GUTTER@mm;
  --measure: @MEASURE@mm;      /* the body text column */
  --top: @TOP@mm;
  --bottom: @BOTTOM@mm;

  --ink: @INK@;                /* body prose */
  --furniture: @FURNITURE@;    /* captions, sub-headings, bold runs, folio -- grey, not black */
  --panel-label: @PANEL_LABEL@;
  --objectives: @OBJECTIVES@;
  --strapline: @STRAPLINE@;
  --example-tab: @EXAMPLE_TAB@;
  --feature-tab: @FEATURE_TAB@;
  --summary-tab: @SUMMARY_TAB@;
  --margin-bar: @MARGIN_BAR@;
  --table-head: @TABLE_HEAD@;
  --folio: @FOLIO@;
  --hairline: @HAIRLINE@;
  --banner: @BANNER@;
  --banner-strip: @BANNER_STRIP@;
  --banner-tab: @BANNER_TAB@;

  /* The book's three display faces are proprietary (BallroomTango, Crazy1, a Garamond cut).
     Each is approximated by the nearest widely-available face of the same CLASS -- a formal
     script, a heavy shaded serif, an old-style serif -- rather than substituted with the body
     face, which would erase the distinction the book draws between them. */
  --font-body: "NCERTBookman", "Bookman Old Style", "URW Bookman L", Georgia, serif;
  /* The book's face is BallroomTango, a round casual brush script that cannot be licensed into
     this export. Apple Chancery is the closest widely-available face of the same class -- upright
     chancery with swash capitals -- and is preferred over the thin, strongly-sloped copperplate
     of Snell Roundhand, which reads as a different kind of book entirely. */
  --font-script: "Apple Chancery", "Snell Roundhand", "Lucida Calligraphy", "Segoe Script",
                 "Brush Script MT", cursive;
  /* The banner title is set in a HEAVY shaded display face, not the light script the margin
     headings use. Running both through one stack made the chapter title read as a thin italic
     where the book prints a bold white letter with a dark keyline. */
  --font-title: "Snell Roundhand", "Apple Chancery", "Brush Script MT", "Segoe Script", cursive;
  --font-display: "Hoefler Text", "Baskerville", "Palatino Linotype", Palatino, Georgia, serif;
}

* { box-sizing: border-box; }
html { background: #4a4a4f; }
body {
  margin: 0; padding: 10mm 0 16mm;
  font-family: var(--font-body);
  font-size: var(--body-pt);
  line-height: var(--leading);
  color: var(--ink);
  -webkit-font-smoothing: antialiased;
}

/* ---- viewer chrome (screen only) ---------------------------------------------------------- */
.toolbar {
  position: sticky; top: 0; z-index: 40;
  display: flex; align-items: center; gap: 10px;
  padding: 7px 14px; margin: -10mm 0 10mm;
  background: #26262a; color: #e8e8ea; font-size: 12px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}
.toolbar .name { font-weight: 700; letter-spacing: .02em; }
.toolbar .spacer { flex: 1; }
.toolbar input { width: 44px; text-align: center; background: #3a3a40; color: inherit;
                 border: 1px solid #55555c; border-radius: 3px; padding: 2px 4px; font: inherit; }
.toolbar button { background: #3a3a40; color: inherit; border: 1px solid #55555c;
                  border-radius: 3px; padding: 2px 9px; font: inherit; cursor: pointer; }
.toolbar button:hover { background: #4a4a52; }

/* ---- the sheet ---------------------------------------------------------------------------- */
#viewer { transform-origin: top center; }
.sheet {
  position: relative;
  width: var(--sheet-w); min-height: var(--sheet-h);
  margin: 0 auto 9mm; padding: var(--top) 0 var(--bottom);
  background: #fff; overflow: hidden;
  box-shadow: 0 2px 14px rgba(0,0,0,.45);
}
.flow {
  zoom: var(--page-zoom);
  /* Body prose always starts at the measured text column, whether or not anything is printed in
     the margin beside it. Marginal items are pulled back out of this padding by their own
     negative margin, which is how NCERT sets them: the measure never moves. */
  padding-left: calc(var(--edge-l) + var(--margin-w) + var(--gutter));
  padding-right: calc(var(--sheet-w) - var(--edge-l) - var(--margin-w) - var(--gutter) - var(--measure));
}
.flow::after { content: ""; display: block; clear: both; }

/* ---- prose -------------------------------------------------------------------------------- */
/* NCERT Chemistry separates paragraphs with a FIRST-LINE INDENT and no space at all -- measured
   18.0pt (6.3mm) across 41 paragraphs of this chapter. Setting a 0.9mm inter-paragraph margin on
   top of a 1.6mm block margin added about 25mm to a ten-paragraph page: a tenth of the sheet,
   which is most of why every page overran its own depth and the whole book was being shrunk to
   compensate. A book that indents does not also space. */
p.para { margin: 0; text-indent: @INDENT@mm; text-align: justify;
         text-justify: inter-word; hyphens: auto; }
/* A paragraph carried over from the previous page is set flush, as the book sets it. */
p.para.flush { text-indent: 0; }
.block { margin: 0 0 1.4mm; }
p.para.block { margin-bottom: 0; }
strong { font-weight: 700; color: var(--furniture); }
sub, sup { font-size: .62em; line-height: 0; }
sub { vertical-align: -.22em; }
sup { vertical-align: .50em; }

/* ---- headings ----------------------------------------------------------------------------- */
/* A numbered section heading is printed in the OUTER MARGIN in the book's script face, with a
   thin salmon rule under it running to the page edge. It is not a banner across the measure --
   that is what every generic render of this book has made it, and it is the single most visible
   way those renders stop looking like the book. */
.sec-head {
  float: left; clear: both;
  width: var(--margin-w);
  /* A heading NEVER breaks inside a word. `anywhere` split "Nomenclature" as "Nomenclatur / e";
     `break-word` still does so whenever a single word is wider than the column, which at this
     size several of them are. A long word is allowed to run into the white margin beside it
     instead -- the column is empty there, and an overhanging word reads correctly where a broken
     one does not. */
  overflow-wrap: normal; word-break: keep-all; hyphens: none;
  margin: 2.2mm var(--gutter) 2.0mm calc(-1 * (var(--margin-w) + var(--gutter)));
  font-family: var(--font-script);
  font-size: 1.42em; line-height: 1.18; color: var(--ink);
  padding-bottom: 1.6mm;
  border-bottom: .35mm solid var(--margin-bar);
}
.sec-head .no { font-style: italic; padding-right: .22em; }
/* The vector form of the same heading: it fills the outer column, keeps its own aspect, and
   carries the words beside it for search in a span no one sees. */
.sec-head.is-svg { padding-bottom: 2.0mm; }
.sec-head.is-svg img { display: block; width: 100%; height: auto; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden;
      clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
.sub-head {
  clear: both; margin: 2.6mm 0 1.1mm;
  font-family: var(--font-body); font-weight: 700;
  font-size: 1.0em; color: var(--furniture); letter-spacing: .01em;
}
.sub-head .no { padding-right: .7em; }
.letter-head {
  margin: 2.2mm 0 .9mm -2.0mm;
  font-family: var(--font-body); font-weight: 700; font-style: italic;
  font-size: .92em; color: var(--furniture); letter-spacing: .055em;
}
.run-head {
  margin: 2.6mm 0 1.0mm; font-weight: 700; font-style: italic;
  font-size: .92em; color: var(--furniture); letter-spacing: .03em;
}
.centre-head {
  clear: both; margin: 5mm 0 2.4mm; text-align: center;
  font-weight: 700; font-size: 1.02em; color: var(--ink); letter-spacing: .03em;
}

/* ---- the chapter opener ------------------------------------------------------------------- */
.opener { position: relative; margin-bottom: 3mm; }
.opener-banner {
  position: relative;
  /* Measured: the banner runs from the body column out PAST the trim, so it bleeds off the
     outer edge of the sheet rather than stopping at the measure. */
  margin-right: calc(-1 * (var(--sheet-w) - var(--edge-l) - var(--margin-w) - var(--gutter) - var(--measure)));
  background: var(--banner);
  border-bottom: @STRIP_H@mm solid var(--banner-strip);
  padding: 13mm 6mm 6mm; min-height: @BANNER_H@mm;
  text-align: center;
}
/* The type is centred on the TAB, not on the banner. Measured: the banner runs x 0.441-1.037
   (centre 0.739) while "Unit", the numeral and the title all centre on 0.685-0.687 -- which is
   the cream tab's own centre (0.591-0.777 -> 0.684). Centring on the banner set the whole stack
   about 11mm right of where the book prints it, so "Unit" sat beside the tab instead of on it. */
.opener-banner > .opener-unit,
.opener-banner > .opener-no,
.opener-banner > .opener-title { margin-right: @TYPE_SHIFT@%; }
/* The cream tab bleeds off the TOP of the sheet (measured y -0.019 to 0.175), behind the
   numeral. It is drawn under the type, so the type sets its own stacking context above it. */
.opener-tab {
  position: absolute; top: calc(-1 * var(--top)); left: @TAB_X@%;
  width: @TAB_W@%; height: @TAB_H@mm; background: var(--banner-tab); z-index: 1;
}
.opener-unit {
  position: relative; z-index: 2;
  font-family: var(--font-title); font-weight: 700;
  font-size: 2.3em; color: #fff; line-height: 1;
  -webkit-text-stroke: .3px rgba(45,28,50,.7); paint-order: stroke fill;
}
.opener-no {
  position: relative; z-index: 2;
  font-family: var(--font-display); font-weight: 700; font-size: 7.6em;
  line-height: .82; color: #fff; margin: -.10em 0 .02em;
  -webkit-text-stroke: .4px rgba(45,28,50,.7); paint-order: stroke fill;
  text-shadow: 1px 1.2px 0 rgba(70,50,78,.26);
}
.opener-title {
  position: relative; z-index: 2;
  font-family: var(--font-title); font-weight: 700;
  font-size: 2.9em; line-height: 1.1; color: #fff;
  /* The book's display face is drawn with a dark keyline round white letters; an outline is the
     closest a web face gets to it, and without one the white type disappears into the lavender. */
  /* A THIN keyline with one soft drop, which is what the book's shaded face actually prints.
     A heavy stroke plus a doubled shadow muddied the counters and read as a bevel. */
  -webkit-text-stroke: .35px rgba(45,28,50,.75);
  paint-order: stroke fill;
  text-shadow: 1px 1.2px 0 rgba(70,50,78,.28);
}
.strapline {
  margin: 3.2mm 0 3.6mm; font-style: italic; font-size: .88em;
  color: var(--strapline); text-align: left;
}

/* The Objectives panel: an L of salmon rule -- a thick bar down the outer edge with a short
   horizontal stroke across its head -- with the list set inside it in small type. */
.objectives {
  float: left; clear: both;
  width: calc(var(--margin-w) + var(--gutter) + 18mm);
  margin: 0 4mm 4mm calc(-1 * (var(--margin-w) + var(--gutter)));
  padding: 0 0 0 5.2mm;
  border-left: 2.2mm solid var(--margin-bar);
  border-top: .7mm solid var(--margin-bar);
  font-size: .92em; text-align: justify;
}
.objectives .label {
  display: block; margin: -1.4mm 0 1.6mm;
  font-family: var(--font-script); font-size: 1.9em; color: var(--objectives);
}
.objectives ul { margin: 0; padding-left: 4mm; }
.objectives li { margin-bottom: .7mm; }

/* ---- panels ------------------------------------------------------------------------------- */
/* A worked example, a scientist's life, a feature box and the Summary are all the same object in
   the book: a white panel with a hairline round it and ONE coloured bar down one edge. Which edge
   and which colour are measured per panel, not assumed -- this chapter prints the bar on the left
   on three pages and on the right on four. */
/* Position comes from the measurement, inline, per panel -- see build_html. */
.panel {
  position: relative; clear: both; margin: 3.4mm 0 4.2mm;
  /* A worked example is one object. Allowed to split, it printed as a narrow strip carrying only
     "Example 9.5 / Solution" with its content stranded elsewhere. */
  break-inside: avoid; page-break-inside: avoid;
  padding: 3.4mm 5mm 3.6mm;
  background: #fff; border: .2mm solid var(--hairline); border-radius: 2.4mm;
}
.panel::after {
  content: ""; position: absolute; top: -.6mm; bottom: -.6mm; width: 3.4mm;
  border-radius: 1.6mm; background: var(--tab, var(--example-tab));
}
.panel.tab-right::after { right: -1.0mm; }
.panel.tab-left::after  { left: -1.0mm; }
.panel.tab-right { padding-right: 9mm; }
.panel.tab-left  { padding-left: 9mm; }
.panel-example { --tab: var(--example-tab); }
.panel-feature { --tab: var(--feature-tab); }
.panel-summary { --tab: var(--summary-tab); }
.panel .label {
  display: block; text-align: right; margin-bottom: 1.4mm;
  font-family: var(--font-script); font-size: 1.32em; color: var(--panel-label);
}
.panel .label i { font-style: normal; border-bottom: .25mm solid var(--panel-label);
                  padding-bottom: .4mm; }
/* The vector form of the same label: the book's own letterforms, sized to the line it replaces. */
.panel .label.label-svg { line-height: 0; }
.panel .label.label-svg img { display: inline-block; height: 5.2mm; width: auto; }
.panel-summary .label.label-svg img { height: 7.4mm; }
.objectives .label.label-svg img { height: 7.0mm; width: auto; display: block;
                                   margin: -1.4mm 0 1.6mm; }
.panel-summary .label { color: var(--ink); font-size: 1.7em; }
.panel-summary .label i { border-bottom-color: var(--ink); }
.panel-feature > .title {
  display: block; text-align: center; margin-bottom: 1.6mm;
  font-weight: 700; letter-spacing: .06em; font-size: 1.02em;
}
.panel p { text-align: justify; margin: 0 0 1.2mm; }
/* The scientist panel hangs its portrait out of the panel's outer edge, over a block of the same
   yellow as the bar -- measured on p003, where the photograph sits left of and above the panel. */
.panel-scientist .portrait {
  float: left; width: 30mm; margin: -8mm 5mm 2mm -11mm;
  padding: 1.4mm 2.4mm 2.4mm 1.4mm; background: var(--feature-tab);
}
.panel-scientist .portrait img { display: block; width: 100%; border: .2mm solid var(--hairline); }
.panel-scientist .portrait .years {
  display: block; margin-top: 1.4mm; text-align: center;
  font-family: var(--font-script); font-size: 1.1em;
}
.panel-scientist .lead { font-family: var(--font-script); font-size: 1.5em; padding-right: .18em; }

/* Intext Questions and Exercises are marked by a salmon bar in the outer margin rather than a
   panel -- measured on pp.008, 011, 018, 021-023. */
/* Intext Questions: the book prints them in a panel with a salmon bar down the inner edge, not
   as bare text beside a rule. Rendering only the bar left them looking like an aside rather than
   the boxed exercise set they are. */
.marked {
  clear: both; position: relative;
  margin: 3.4mm 0 4.0mm calc(-1 * (var(--margin-w) + var(--gutter)));
  padding: 3.0mm 5mm 3.2mm calc(var(--margin-w) + var(--gutter));
  border-left: 2.6mm solid var(--margin-bar);
  background: #fff; border-top: .2mm solid var(--hairline);
  border-right: .2mm solid var(--hairline); border-bottom: .2mm solid var(--hairline);
  border-radius: 0 2.4mm 2.4mm 0;
}
.marked > .label {
  display: block; margin-bottom: 1.6mm; font-weight: 700;
  letter-spacing: .05em; color: var(--ink); font-size: 1.02em;
}

/* ---- figures ------------------------------------------------------------------------------ */
figure { margin: 0 0 2.6mm; }
figure img { display: block; width: 100%; height: auto; }
figcaption {
  margin-top: 1.2mm; font-size: .9em; font-style: italic; font-weight: 700;
  color: var(--furniture); line-height: 1.22;
}
/* A marginal figure is pulled out of the measure into the outer column and the prose wraps it,
   exactly as the book sets it. Its width is its OWN measured width, not the column's: this book
   routinely runs a structural diagram wider than the margin and lets the text wrap at whatever
   point the diagram actually ends. */
/* A measured two-column stretch: the outer column and the body column, at their own widths. */
.row { display: flex; align-items: flex-start; clear: both; margin-bottom: 1.6mm; }
.row-left { min-width: 0; }
.row-right { flex: 1; min-width: 0; }
.row-left > * , .row-right > * { max-width: 100%; }
/* A block the book sets across the measure in columns (p003's Solution). */
.cols { margin: 0 0 1.2mm; max-width: 100%; overflow-x: auto; }
.cols .crow { display: flex; align-items: baseline; white-space: nowrap; }
.cols .ccell { min-width: 0; }
.cols .crow:last-child { margin-bottom: 0; }
figure.row-fig { margin-bottom: 1.6mm; }
/* No figure smaller than a third of the measure. Fig 9.2's measured box is narrow because its
   molecules are widely spaced, and rendering it at that width made it unreadable. */
figure img { min-width: 34%; }
figure.row-fig img, .row-left figure img { min-width: 0; }
figure.row-fig figcaption { text-align: left; }
/* Inside a measured row the outer column IS the column, so anything in it must stop trying to
   float itself out into a margin that is no longer there. Without this the script section
   headings kept their float and their negative pull and were dragged off the left of the sheet,
   leaving only the salmon rule under them visible (p004's "5.2 Definitions of ..." vanished). */
.row-left .sec-head, .row-right .sec-head {
  float: none; clear: none; width: auto; margin-left: 0; margin-right: 0;
}
.row-left .objectives, .row-right .objectives { float: none; width: auto; margin-left: 0; }
.row-left figure.margin-fig, .row-right figure.margin-fig {
  float: none; width: 100% !important; margin-left: 0 !important; margin-right: 0 !important;
}
figure.margin-fig { float: left; clear: left; }
figure.margin-fig figcaption { text-align: left; }
figure.full-fig { clear: both; }
figure.full-fig figcaption { text-align: center; }
.fig-missing {
  clear: both; margin: 2mm 0; padding: 2mm 3mm; font-size: .86em;
  color: #8a5a00; background: #fff6e0; border-left: 1mm solid #e8a32c;
}

/* ---- tables ------------------------------------------------------------------------------- */
.table-caption {
  margin: 2.6mm 0 1.2mm; font-weight: 700; font-size: .9em;
  color: var(--furniture); letter-spacing: .03em;
}
/* A caption is set BOLD ITALIC in this book -- plain text reads as body copy that has drifted
   under the artwork. */
figcaption { font-weight: 700; font-style: italic; }
table.tbl { width: 100%; border-collapse: collapse; margin: 0 0 3mm; font-size: .9em; }
table.tbl thead th {
  background: var(--table-head); color: #fff; font-weight: 700;
  padding: 1.4mm 2mm; text-align: center; border: .2mm solid var(--table-head);
}
table.tbl tbody td {
  padding: 1.0mm 2mm; text-align: center; border-left: .2mm solid var(--table-head);
  border-right: .2mm solid var(--table-head);
}
table.tbl tbody tr:last-child td { border-bottom: .3mm solid var(--hairline); }

/* ---- displayed equations (TEXT, never a screenshot) ---------------------------------------- */
.eqline { margin-bottom: .6mm; }
.equation {
  clear: both; margin: 2.2mm 0 2.6mm 6mm;
  font-family: var(--font-body); white-space: pre-wrap;
  /* A reaction series can be set wider than the measure (p015's spectrochemical series runs the
     full width of the printed page). Scrolling it keeps every term reachable; clipping silently
     dropped the last ligand in the series. */
  max-width: 100%; overflow-x: auto; overflow-y: hidden;
}
/* NCERT ranges its displayed reactions LEFT, indented from the measure -- it does not centre
   them. KaTeX centres display maths by default, which left a wide gap on the left of every
   reaction and pushed the long ones against the right margin. */
/* KaTeX sizes display mathematics at roughly 1.21x the surrounding text and then adds its own
   display scaling, which printed these reactions far larger than the book sets them -- big enough
   to collide with the paragraph above. NCERT sets a displayed reaction at about body size. */
.katex-display { margin: 2.4mm 0; text-align: left; }
.katex-display > .katex { text-align: left; font-size: 1.0em; }
.equation .katex { font-size: 1.0em; }
.equation { overflow-x: auto; overflow-y: visible; }

/* ---- footer furniture --------------------------------------------------------------------- */
/* The folio: a short yellow tab carrying the page number, the chapter or subject name beside it,
   and a yellow rule running from the tab to the OUTER edge of the sheet. It mirrors per spread --
   number inboard on a verso, outboard on a recto -- which is measured, not assumed. */
.folio {
  position: absolute; left: 0; right: 0; bottom: @FOLIO_BOTTOM@mm;
  display: flex; align-items: center; font-size: .9em; color: var(--furniture);
}
.folio .num {
  background: var(--folio); color: var(--furniture); font-weight: 700;
  padding: .5mm 2.2mm; min-width: @FOLIO_W@mm; text-align: center;
}
.folio .head { padding: 0 2.6mm; white-space: nowrap; letter-spacing: .04em; }
.folio .rule { flex: 1; height: .7mm; background: var(--folio); }
.folio-verso { padding-left: var(--edge-l); flex-direction: row; }
.folio-verso .head { order: 0; } .folio-verso .num { order: 1; } .folio-verso .rule { order: 2; }
.folio-recto { padding-right: var(--edge-l); }
.folio-recto .rule { order: 0; } .folio-recto .num { order: 1; } .folio-recto .head { order: 2; }
.folio-recto .rule { margin-right: 0; }
.imprint {
  position: absolute; left: 0; right: 0; bottom: @IMPRINT_BOTTOM@mm;
  text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: 8pt; color: #000;
}

/* ---- what the extraction is still missing, stated rather than hidden ---------------------- */
/* Stated, never hidden -- but printed BESIDE the sheet, not on it. Inside the sheet it landed
   under the absolutely-positioned folio and the two overprinted each other. */
.gaps {
  width: var(--sheet-w); margin: -7mm auto 9mm; padding: 2mm 3mm; font-size: 9pt;
  background: #fdf0f0; border-left: 1mm solid #c0392b; color: #7a2b22;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}
.gaps ul { margin: .8mm 0 0; padding-left: 4mm; }

@media print {
  @page { size: @SHEET_W@mm @SHEET_H@mm; margin: 0; }
  /* A worked example, a Summary or an Intext set is one object; split, it prints as a strip
     carrying only its label with the content stranded elsewhere. */
  .panel, .marked { break-inside: avoid; page-break-inside: avoid; }
  html, body { background: #fff; }
  /* The screen padding must go. 10mm above the first sheet and 16mm below the last pushed the
     stack past the paper at both ends -- the trailing 16mm alone printed an extra empty page. */
  body { padding: 0; margin: 0; }
  .toolbar { display: none !important; }
  .sheet {
    box-shadow: none; margin: 0 auto;
    /* One book page = one printed page. `break-inside: avoid` is what enforces it: without it a
       sheet whose box lands a fraction of a millimetre over the page spills a sliver onto a
       second, which is how 23 book pages printed as 33. The 1mm of slack absorbs the rounding
       between the CSS sheet height and the @page box so a sheet that FITS can never spill. */
    /* A FIXED height, not a minimum. With a minimum, a sheet whose box ends up a millimetre
       over carries its absolutely-positioned folio and imprint past the page edge, and those two
       elements then print on a page of their own -- which is exactly what pages carrying nothing
       but "Chemistry 126 / Reprint 2026-27" were. Pinning the height cannot lose content here
       because the fit loop has already verified, in this same engine, that every sheet's content
       clears its own depth with headroom to spare. */
    height: calc(var(--sheet-h) - 2mm); overflow: hidden;
    break-inside: avoid; break-after: page;
  }
  .sheet:last-child { break-after: auto; }
}
"""

_JS = r"""<script>
(function () {
  var sheets = [].slice.call(document.querySelectorAll('.sheet'));
  var viewer = document.getElementById('viewer');
  var input = document.getElementById('pg');
  var zoomLabel = document.getElementById('zoomv');
  var zoom = 1, STEPS = [.4,.5,.6,.7,.8,.9,1,1.15,1.35,1.6,2,2.5];
  function setZoom(z) {
    zoom = z; viewer.style.transform = 'scale(' + z + ')';
    viewer.style.height = (viewer.scrollHeight * z) + 'px';
    zoomLabel.textContent = Math.round(z * 100) + '%';
  }
  document.getElementById('zin').onclick = function () {
    for (var i = 0; i < STEPS.length; i++) if (STEPS[i] > zoom + .001) return setZoom(STEPS[i]);
  };
  document.getElementById('zout').onclick = function () {
    for (var i = STEPS.length - 1; i >= 0; i--) if (STEPS[i] < zoom - .001) return setZoom(STEPS[i]);
  };
  document.getElementById('prt').onclick = function () { window.print(); };
  input.addEventListener('change', function () {
    var n = parseInt(input.value, 10);
    if (n >= 1 && n <= sheets.length) sheets[n - 1].scrollIntoView({behavior: 'smooth'});
  });
  window.addEventListener('scroll', function () {
    var mid = window.scrollY + window.innerHeight / 3, best = 1;
    for (var i = 0; i < sheets.length; i++) {
      if (sheets[i].offsetTop * zoom <= mid) best = i + 1;
    }
    if (document.activeElement !== input) input.value = best;
  }, {passive: true});
})();
</script>"""


_RE_UNIT = re.compile(r"^\s*Unit\s+(\d+)\s*\n(.+)$", re.S | re.I)
_RE_NUMBERED = re.compile(r"^\s*(\d+\.\d+(?:\.\d+)?)\s+(.*)$", re.S)
_RE_LETTERED = re.compile(r"^\s*\(\s*([a-z])\s*\)\s*(.*)$", re.S | re.I)
_RE_BULLET = re.compile(r"^\s*[•·]\s*")
# One list marker as the book prints it, delimiters included: "5.29 ", "(i) ", "(a) ", "1. ".
_RE_MARKER = re.compile(r"^\s*(?:\(\s*[a-zA-Z0-9]{1,4}\s*\)|\d+(?:\.\d+)?[.)]?)\s+")


def _panel_group(items):
    """Group consecutive items that the measurement puts inside the SAME printed panel.

    A2 reads a worked example as three blocks -- the question, the table in it and the solution --
    because that is what they are in reading order. The book draws ONE panel around all three. The
    grouping is taken from the measured panel rectangle rather than from the text, which is also
    what keeps the Summary whole where it runs across two sheets and only its first block says
    "Summary".
    """
    groups, current, loose = [], None, []
    for it in items:
        key = tuple((it["panel"] or {}).get("bbox") or []) if it["panel"] else None
        if key:
            if loose:
                groups.append((None, loose))
                loose = []
            if current and current[0] == key:
                current[1].append(it)
                continue
            if current:
                groups.append(current)
            current = (key, [it])
            continue
        if current:
            groups.append(current)
            current = None
        # Consecutive items OUTSIDE any panel are kept together in ONE group. Emitting each as
        # its own group was the bug that silently disabled two-column rows: the row detector is
        # handed a group at a time, and a group of one item can never contain both a left-column
        # figure and the prose printed beside it. Every page in the chapter therefore fell back to
        # the float path the rows were written to replace.
        loose.append(it)
    if current:
        groups.append(current)
    if loose:
        groups.append((None, loose))
    return groups


# Two measured lines belong to the same printed ROW when their vertical centres are within this
# fraction of the sheet. Measured on p003's Solution: the two entries of its first row sit at
# identical y, and the rows themselves are 0.023 apart.
_ROW_BAND = 0.008
# Pieces closer than this are one run of text the text layer split (a superscript breaks a line
# into three spans); anything wider apart is a real column boundary. Measured on p021: inside a
# split line the gap is 0.000, between two option columns it is 0.04 or more.
_CELL_JOIN = 0.018


def _columned_html(item, geo=None):
    """The block laid out LINE BY LINE as the book prints it, or None.

    NCERT sets its exercises, its answers and its worked solutions in columns: exercise 5.6 runs
    its ten options as two columns of five, and 5.5 as three columns. Reflowing those into one
    stacked list is not what the page says and takes nearly twice the depth -- p021 needed 801px
    for what the book prints in about half a page.

    The lines come from the text-stream alignment (`item["lines"]`), so they are this block's own
    printed lines and nothing else's. Within a band, pieces separated by a HAIRLINE gap are one
    run of text that the text layer happened to split (a superscript breaks a line into three
    spans); only a real gap is a column boundary.

    Returns None when the block is a single column, which is the common case and is better served
    by reflowing it.
    """
    lines = item.get("lines") or []
    if len(lines) < 3:
        return None

    # Banded by VERTICAL OVERLAP, not by centre distance. A fragment that is mostly superscript
    # sits higher than its own line -- p023's "2+ -> BaSO4 (s)" has its centre 0.003 above the
    # "+ Ba" it continues -- so a centre test split one printed reaction into three stacked
    # fragments. Two pieces printed on the same line always overlap vertically.
    bands = []
    for ln in sorted(lines, key=lambda l: (round(l["bbox"][1], 3), l["bbox"][0])):
        y0, y1 = ln["bbox"][1], ln["bbox"][3]
        for band in bands:
            ov = min(y1, band["y1"]) - max(y0, band["y0"])
            if ov > 0.35 * min(y1 - y0, band["y1"] - band["y0"]):
                band["cells"].append(ln)
                band["y0"] = min(band["y0"], y0)
                band["y1"] = max(band["y1"], y1)
                break
        else:
            bands.append({"y0": y0, "y1": y1, "cells": [ln]})

    merged_bands = []
    for band in bands:
        cells, cur = [], None
        for ln in sorted(band["cells"], key=lambda l: l["bbox"][0]):
            if cur and ln["bbox"][0] - cur["x1"] < _CELL_JOIN:
                cur["runs"] = cur["runs"] + list(ln["runs"])
                cur["x1"] = max(cur["x1"], ln["bbox"][2])
                continue
            cur = {"x0": ln["bbox"][0], "x1": ln["bbox"][2], "runs": list(ln["runs"])}
            cells.append(cur)
        merged_bands.append(cells)

    if not any(len(cells) > 1 for cells in merged_bands):
        return None

    x0 = min(c["x0"] for cells in merged_bands for c in cells)
    out = []
    for cells in merged_bands:
        parts = []
        prev = x0
        for c in cells:
            pad = max(0.0, c["x0"] - prev)
            style = "flex: 0 0 auto;"
            if pad > 0.004 and geo:
                style += " margin-left: %.1fmm;" % (pad * geo["sheet_w"])
            parts.append('<span class="ccell" style="%s">%s</span>'
                         % (style, runs_to_html(c["runs"])))
            prev = c["x1"]
        out.append('<div class="crow">%s</div>' % "".join(parts))
    return '<div class="cols">%s</div>' % "".join(out)


def _printed_lines(item):
    """`item`'s measured pieces grouped into the LINES they are printed on.

    Returns [[run, ...], ...] -- one run-list per printed line, pieces in reading order. Used for
    blocks recovered straight from the text layer, where there is no A2 text to reflow and the
    only honest structure is the one the page actually has.

    `_columned_html` cannot serve this: it answers "is this block set in columns?" and returns
    None when it is not, which for a reaction scheme meant falling back to one fragment per line.
    p023's four ionisation-isomer reactions came out as twelve stacked pieces, each charge on a
    line of its own.
    """
    lines = item.get("lines") or []
    if not lines:
        return []
    bands = []
    for ln in sorted(lines, key=lambda l: (round(l["bbox"][1], 3), l["bbox"][0])):
        y0, y1 = ln["bbox"][1], ln["bbox"][3]
        for band in bands:
            ov = min(y1, band["y1"]) - max(y0, band["y0"])
            if ov > 0.35 * min(y1 - y0, band["y1"] - band["y0"]):
                band["cells"].append(ln)
                band["y0"], band["y1"] = min(band["y0"], y0), max(band["y1"], y1)
                break
        else:
            bands.append({"y0": y0, "y1": y1, "cells": [ln]})

    out = []
    for band in bands:
        runs, prev_x1 = [], None
        for ln in sorted(band["cells"], key=lambda l: l["bbox"][0]):
            if prev_x1 is not None and ln["bbox"][0] - prev_x1 > 0.004:
                runs.append({"t": "  ", "v": "", "b": False})
            runs.extend(ln["runs"])
            prev_x1 = ln["bbox"][2]
        out.append(runs)
    return out


def _list_html(runs):
    """A `list` block as the book sets it: one line per entry, bullets and numbering preserved.

    A2 records a list's line breaks as STRUCTURE (one per question, per option, per bullet). A
    Markdown paragraph swallows a lone newline and an HTML paragraph swallows it too, so the
    21-item Exercises run came out as one wall of prose in earlier renders of other chapters. Each
    line is emitted as its own row with a hanging indent, which is how NCERT prints them.
    """
    rows, buf = [], []
    for r in runs:
        parts = r["t"].split("\n")
        for i, part in enumerate(parts):
            if i:
                rows.append(buf)
                buf = []
            if part:
                buf.append({"t": part, "v": r.get("v", ""), "b": r.get("b")})
    if buf:
        rows.append(buf)

    # A new ITEM starts a row; a CONTINUATION line joins the row above it.
    #
    # A2 records a list with the source's hard line wraps -- one newline per PRINTED line, not one
    # per item. Making every line its own row froze the book's line breaks into the render: each
    # continuation line kept a short line in a measure that could have held far more, so p021's
    # ten exercises occupied 801px where the same words need about 335px, i.e. 95% of the sheet
    # for half a page of the book. Merging continuations lets the text reflow, which is the whole
    # point of a reflowed render.
    items = []
    for row in rows:
        if not row:
            continue
        plain = "".join(x["t"] for x in row)
        if not plain.strip():
            continue
        marker, body = "", row
        m = _RE_BULLET.match(plain)
        if m:
            marker, body = "\u2022", _strip_prefix(row, m.end())
        else:
            # The marker is taken WITH its delimiters. Capturing only the inner token left the
            # closing bracket at the head of the text, so NCERT's "(i) If ..." came out as a
            # marker "i" followed by a body beginning ") If ...".
            m = _RE_MARKER.match(plain)
            if m and len(m.group(0).strip()) <= 9:
                marker, body = m.group(0).strip(), _strip_prefix(row, m.end())
        if marker or not items:
            items.append([marker, body])
        else:
            items[-1][1] = items[-1][1] + [{"t": " ", "v": "", "b": False}] + body

    out = ['<div class="li"><span class="li-mark">%s</span><span class="li-body">%s</span></div>'
           % (_esc(mark), runs_to_html(body)) for mark, body in items]
    return '<div class="list">%s</div>' % "".join(out)


def _strip_prefix(runs, n):
    """Drop the first n characters from a run list, keeping each remaining run's typing."""
    out, left = [], n
    for r in runs:
        if left <= 0:
            out.append(r)
            continue
        if len(r["t"]) <= left:
            left -= len(r["t"])
            continue
        out.append({"t": r["t"][left:], "v": r.get("v", ""), "b": r.get("b")})
        left = 0
    return out


# Roles whose type size is taken from the measurement. Headings carry their own scale in the
# stylesheet (they are sized relative to the body by design), so only running matter is adjusted.
_SIZED_ROLES = {"paragraph", "list", "strapline", "note", "summary", "summary_body",
                "example", "example_body", "solution", "intext", "feature", "scientist",
                "objectives", "equation"}


def _size_style(it, geo):
    """`font-size: Nem` when the book sets this block at something other than the body size."""
    if it["role"] not in _SIZED_ROLES:
        return ""
    size = it.get("size_pt")
    body = geo.get("body_pt") or 10.5
    if not size or abs(size - body) < body * 0.03:
        return ""
    return "font-size: %.3fem;" % (size / body)


def _item_html(it, page_num, fig_rel, figures, geo, heads=None):  # noqa: C901
    heads = heads or {}
    role, runs = it["role"], it["runs"]

    if role == "chapter_title":
        m = _RE_UNIT.match(it["text"])
        unit = m.group(1) if m else ""
        name = (m.group(2) if m else it["text"]).strip()
        # The banner is NOT the measure wide. NCERT sets it from the body column out past the
        # trim (measured x 0.441 to 1.037), so it bleeds off the outer edge; and the cream tab
        # bleeds off the TOP. Both are emitted at their measured positions.
        return ('<div class="opener"><div class="opener-banner">'
                '<div class="opener-tab"></div>'
                '<div class="opener-unit">Unit</div>'
                '<div class="opener-no">%s</div>'
                '<div class="opener-title">%s</div></div></div>'
                % (_esc(unit), _esc(name).replace("\n", "<br>")))

    if role == "objectives":
        lines = [ln for ln in it["text"].split("\n") if ln.strip()]
        intro = [ln for ln in lines[1:] if not _RE_BULLET.match(ln)]
        bullets = [_RE_BULLET.sub("", ln) for ln in lines[1:] if _RE_BULLET.match(ln)]
        head = intro[0] if intro else ""
        return ('<aside class="objectives"><span class="label">Objectives</span>'
                '<div class="intro">%s</div><ul>%s</ul></aside>'
                % (_esc(head), "".join("<li>%s</li>" % _esc(b) for b in bullets)))

    if role == "margin_heading":
        plain = _plain(runs).replace("\n", " ").strip()
        key = (page_num, it["n"])
        if key in heads:
            # The book's own outlines, with the words still present as text for search and for a
            # screen reader -- the look is exact and nothing becomes unsearchable.
            return ('<h2 class="sec-head is-svg">'
                    '<img src="%s/%s" alt="%s">'
                    '<span class="sr">%s</span></h2>'
                    % (fig_rel, heads[key], _esc(plain), _esc(plain)))
        m = _RE_NUMBERED.match(plain)
        no, rest = (m.group(1), m.group(2)) if m else ("", plain)
        return ('<h2 class="sec-head"><span class="no">%s</span>%s</h2>'
                % (_esc(no), _esc(rest.strip())))

    if role == "sub_heading":
        m = _RE_NUMBERED.match(_plain(runs))
        no, rest = (m.group(1), m.group(2)) if m else ("", _plain(runs))
        return ('<h3 class="sub-head"><span class="no">%s</span>%s</h3>'
                % (_esc(no), _esc(rest.replace("\n", " ").strip())))

    if role == "letter_heading":
        return '<h4 class="letter-head">%s</h4>' % runs_to_html(runs).replace("\n", " ")

    if role == "strapline":
        return '<p class="strapline">%s</p>' % runs_to_html(runs).replace("\n", " ")

    if role == "run_in_heading":
        return '<p class="run-head">%s</p>' % runs_to_html(runs).replace("\n", " ")

    if role in ("exercises_heading", "answers_heading"):
        return '<h3 class="centre-head">%s</h3>' % _esc(_plain(runs).replace("\n", " ").strip())

    # A TABLE that A2S never transcribed AND whose region holds no artwork is a tabulated
    # paragraph, not a drawing -- p002's "1 mol CoCl3.6NH3 (Yellow) gave 3 mol AgCl" rows. It is
    # set as type rather than shipped as a picture of type.
    #
    # The conditions are deliberately narrow. A first version asked only "does this region contain
    # artwork", and that was far too broad: it intercepted Table 5.1, which HAS transcribed rows
    # and belongs in a real <table> with the book's salmon header, and it intercepted the Werner
    # portrait, whose artwork simply did not register. Both came out as bare text.
    if (role == "table" and not (it.get("header") or [])
            and it.get("has_artwork") is False):
        inner = _columned_html(it, geo)
        if inner:
            return inner
        text = runs_to_html(it["runs"]).strip()
        if text:
            return '<p class="para block">%s</p>' % text.replace("\n", "<br>")

    if role == "figure":
        return _figure_html(it, page_num, fig_rel, figures, geo)

    if role == "table":
        return _table_html(it, page_num, fig_rel, figures, geo)

    if role == "equation":
        return _equation_html(it)

    if role == "list":
        inner = _columned_html(it, geo) or _list_html(runs)
        size = _size_style(it, geo)
        return ('<div style="%s">%s</div>' % (size, inner)) if size else inner

    if role in ("example", "solution", "summary", "intext", "scientist", "feature",
                "note", "example_body", "summary_body"):
        inner = _panel_body_html(it)
        size = _size_style(it, geo)
        return ('<div style="%s">%s</div>' % (size, inner)) if size else inner

    body = runs_to_html(runs).replace("\n", " ")
    # Indent to where this paragraph is ACTUALLY set when the book insets it from the measure.
    # The chapter-opening page is the case that forces this: its two opening paragraphs are set
    # in a narrow column at x 0.441 beside the Objectives panel, not across the full measure, and
    # setting them at the measure made them run out of copy a third of the way up the page --
    # which left the 5.1 margin heading stranded below with nothing beside it.
    style = _size_style(it, geo)
    # Indent to where this paragraph is ACTUALLY set when the book insets it from the measure.
    # The chapter-opening page forces this: its two opening paragraphs sit in a narrow column at
    # x 0.441 beside the Objectives panel, not across the full measure.
    #
    # A MARGIN, never a width. A block with an explicit width does not shrink away from a float --
    # only its line boxes do -- so the block overlapped the marginal figure beside it AND then
    # shortened its lines inside that overlap, squeezing p016's prose to about eight characters a
    # line behind the crystal-field diagram.
    if not it.get("in_row") and it.get("bbox") and it["column"] in ("right", "full"):
        inset = (it["bbox"][0] - geo["body_left"]) * geo["sheet_w"]
        if inset > 3.0:
            style = "margin-left: %.1fmm; " % inset + style
    return '<p class="para block"%s>%s</p>' % (
        (' style="%s"' % style.strip()) if style.strip() else "", body)


_RE_LABEL_LINE = re.compile(r"^\s*(Example\s+[\d.]+|Solution|Summary|Intext\s+Questions)\s*\n?",
                            re.I)


def _panel_body_html(it):  # noqa: C901
    """One block inside a panel: its printed label lifted into a label line, the rest as prose."""
    text = it["text"]
    runs = it["runs"]
    m = _RE_LABEL_LINE.match(text)
    label = ""
    if m:
        label = m.group(1).strip()
        runs = _strip_prefix(runs, m.end())
    if it["role"] == "feature" and not label:
        lines = text.split("\n")
        if lines and len(lines[0]) < 60 and lines[0].strip() and not lines[0].rstrip().endswith("."):
            label = ""
            title = lines[0].strip()
            rest = runs_to_html(_strip_prefix(runs, len(lines[0]) + 1))
            return ('<span class="title">%s</span>%s'
                    % (_esc(title), _paras(rest)))
    if it["role"] == "scientist":
        # The book opens the life with the subject's surname set large in the script face, RUN IN
        # to the first sentence ("Werner was born on December 12, 1866, ..."). Setting the name
        # and the sentence as two blocks put "was born on ..." on its own line under the name.
        name = it["label"]
        rest = runs_to_html(_strip_prefix(runs, len(name)))
        return _paras('<span class="lead">%s</span>%s' % (_esc(name), rest))
    # The book's own letterforms where we have them. These labels are set in a display script
    # that cannot be licensed, and substituting the nearest available face is the single most
    # visible way the page stops looking like NCERT. They carry no information a reader searches
    # for, so taking them as vector costs nothing and is exact.
    key = (it.get("_page"), it["n"])
    if label and key in _LABELS:
        head = ('<span class="label label-svg"><img src="%s/%s" alt="%s"></span>'
                % (_FIG_REL, _LABELS[key], _esc(label)))
    elif label:
        head = '<span class="label"><i>%s</i></span>' % _esc(label)
    else:
        head = ""
    columned = _columned_html(it, _GEO) if it["role"] in ("solution", "example_body") else None
    if columned:
        return head + columned
    if it["role"] in ("summary", "summary_body", "scientist", "feature"):
        return head + _paras_from_lines(it, runs_to_html(runs))
    return head + _paras(runs_to_html(runs))


def _paras_from_lines(it, html_fallback):
    """Split a panel's prose into the paragraphs the book actually prints.

    A2 records a box as one run of text with a newline per printed LINE, not per paragraph, so
    splitting on blank lines finds none and the whole Summary runs together as a single block --
    the book sets it as four paragraphs. The breaks are not in the text, but they are on the page:
    NCERT starts a paragraph with a first-line indent, measured at 18pt for this book. A line that
    begins indented from the block's own left edge is therefore the start of a new paragraph.
    """
    # `lines` is located by matching this block's text in the page stream, which fails when A2's
    # text and the printed text diverge too far -- p019's half of the Summary locates nothing at
    # all. The box-derived lines are a coarser answer but a correct one for this purpose, since
    # all that is needed is where each printed line starts.
    lines = it.get("lines") or it.get("measured_lines") or []
    if len(lines) < 4:
        return _paras(html_fallback)
    left = min(l["bbox"][0] for l in lines)
    paras, cur = [], []
    for ln in sorted(lines, key=lambda l: (round(l["bbox"][1], 3), l["bbox"][0])):
        indented = (ln["bbox"][0] - left) > 0.012      # ~2.5mm of the sheet; the measured indent
        if indented and cur:
            paras.append(cur)
            cur = []
        cur.append(ln)
    if cur:
        paras.append(cur)
    if len(paras) < 2:
        return _paras(html_fallback)
    return "".join(
        "<p>%s</p>" % runs_to_html([r for ln in para for r in ln["runs"]]) for para in paras)


def _paras(html_text):
    """Split a panel's body on blank lines into real paragraphs, keeping single breaks as breaks."""
    chunks = [c for c in re.split(r"\n\s*\n", html_text) if c.strip()]
    if not chunks:
        return ""
    return "".join("<p>%s</p>" % c.replace("\n", "<br>") for c in chunks)


def _caption_html(it):
    """The figure's printed caption, re-typed from the book's own glyphs.

    A2S records a caption as a flat string, so "[Co(en)3] 3+" and "[CoCl2(en)2]" lose the
    subscripts and the charge the book sets them with. The caption's own printed lines are in the
    measurement, so the typing is carried across the same way a table cell's is.
    """
    caption = (it.get("caption") or "").strip()
    if not caption:
        return ""
    lines = it.get("caption_lines") or []
    if not lines:
        return _esc(caption)
    chars, variants, sizes = [], [], []
    for ln in lines:
        for r in ln["runs"]:
            for ch in r["t"]:
                if ch.isspace():
                    continue
                chars.append(ch)
                variants.append(r["v"])
                sizes.append(None)
    runs = model_mod.transfer_variants(caption, ("".join(chars), variants, sizes))
    return runs_to_html(runs)


def _figure_html(it, page_num, fig_rel, figures, geo):
    hook = HOOKS.get("figure")
    if hook:
        out = hook(it, page_num, fig_rel, figures, geo)
        if out is not None:
            return out
    key = (page_num, it["n"])
    caption = (it.get("caption") or "").strip()
    labels = it.get("labels") or []
    if key not in figures:
        return ('<div class="fig-missing">Figure on block [%s] — no artwork region was found '
                'under its recorded box, so nothing is shown rather than a blank frame.</div>'
                % _esc(str(it["n"])))

    bbox = it.get("art_bbox") or it["bbox"]
    # Scaled by the SAME factor as the type. Shrinking only the type left the artwork at its
    # printed size, so on a figure-heavy page the fit stalled -- trimming the body from 100% to
    # 82% moved the worst sheet's overrun only from 16% to 6%, because the figures were most of
    # the height and did not move at all. Scaling both together keeps the book's own ratio
    # between a diagram and the prose beside it, which is itself part of looking like the book.
    width_mm = (bbox[2] - bbox[0]) * geo["sheet_w"]
    cap = '<figcaption>%s</figcaption>' % _caption_html(it) if caption else ""

    if it.get("in_row"):
        # Inside a measured two-column row the figure simply fills its column.
        return '<figure class="row-fig"><img src="%s/%s" alt="%s">%s</figure>' % (
            fig_rel, figures[key], _esc(caption or "figure"), cap)

    if it["column"] == "left":
        # A marginal figure with no prose measured beside it: floated into the outer column.
        pull = max(0.0, (geo["body_left"] - bbox[0])) * geo["sheet_w"]
        style = ('width: %.1fmm; margin-left: -%.1fmm; margin-right: %.1fmm;'
                 % (width_mm, pull, geo["gutter"]))
        return '<figure class="margin-fig" style="%s"><img src="%s/%s" alt="%s">%s</figure>' % (
            style, fig_rel, figures[key], _esc(caption or "figure"), cap)

    pull_l = max(0.0, (geo["body_left"] - bbox[0])) * geo["sheet_w"]
    style = "width: %.1fmm; margin-left: -%.1fmm;" % (width_mm, pull_l)
    return '<figure class="full-fig" style="%s"><img src="%s/%s" alt="%s">%s</figure>' % (
        style, fig_rel, figures[key], _esc(caption or "figure"), cap)


# A cell shorter than this is not re-typed from the stream. A one-character cell is ambiguous by
# construction: the "2" in Table 5.1's second column matched the first subscript "2" anywhere in
# the table and came out as "₂", turning a count of 2 moles into a subscript. Three characters is
# the shortest cell in this chapter that identifies itself ("535", "1:3"), and no formula worth
# typing is shorter than that.
_MIN_TYPED_CELL = 3


def _typed_cell(cell, stream, to_markdown=False):
    """One table cell re-typed from the book's glyphs, or left plain when that is not safe."""
    text = str(cell)
    if len(text.strip()) < _MIN_TYPED_CELL:
        return text if to_markdown else _esc(text)
    runs = model_mod.transfer_variants(text, stream)
    return runs_to_markdown(runs) if to_markdown else runs_to_html(runs)


def _cell_html(cell, stream):
    """One table cell, re-typed from the book's own glyphs.

    A2S hands back a cell as a flat string, because a transcription schema has one text field per
    cell. For a chemistry table that loses the whole point: `[Co(NH3)6]3+3Cl-` is printed
    `[Co(NH₃)₆]³⁺3Cl⁻`.

    Matching a cell to a whole measured LINE does not work, and the reason is the same one that
    broke paragraph matching: the text layer's line boundaries are not the table's cell
    boundaries. PyMuPDF reports the whole of Table 5.1's first row as one line
    ("Yellow[Co(NH3)6]3+3Cl-1:3 electrolyte"), so no cell ever equalled a line and every cell in
    the chapter's tables came out flat. The cell is therefore located as a SUBSTRING of the
    table's own character stream, which is exactly the join that already works page-wide.
    """
    return _typed_cell(cell, stream)


def _cell_stream(it):
    """The table's printed characters in order, each carrying its typing."""
    chars, variants, sizes = [], [], []
    for runs in it.get("cell_runs") or []:
        for r in runs:
            for ch in r["t"]:
                if ch.isspace():
                    continue
                chars.append(ch)
                variants.append(r["v"])
                sizes.append(None)
    return "".join(chars), variants, sizes


def _table_html(it, page_num, fig_rel, figures, geo=None):
    header, rows = it.get("header") or [], it.get("rows") or []
    caption = (it.get("caption") or "").strip()
    cap = '<div class="table-caption">%s</div>' % _esc(caption) if caption else ""
    if header and not it.get("describes_artwork"):
        stream = _cell_stream(it)
        head = "".join("<th>%s</th>" % _cell_html(c, stream) for c in header)
        body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _cell_html(c, stream) for c in r)
                       for r in rows)
        size = ""
        if geo and it.get("size_pt") and geo.get("body_pt"):
            ratio = it["size_pt"] / geo["body_pt"]
            if abs(ratio - 1.0) > 0.03:
                size = ' style="font-size: %.3fem;"' % ratio
        return ('%s<table class="tbl"%s><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
                % (cap, size, head, body))
    key = (page_num, it["n"])
    if key in figures:
        return ('%s<figure class="full-fig"><img src="%s/%s" alt="table"></figure>'
                % (cap, fig_rel, figures[key]))
    return ('%s<div class="fig-missing">Table on block [%s] — A2S has not transcribed its rows '
            'and no region was found to crop.</div>' % (cap, _esc(str(it["n"]))))


def _equation_html(it):
    """A displayed equation, always as TEXT. See _md_equation for why never as an image."""
    hook = HOOKS.get("equation")
    if hook:
        out = hook(it)
        if out is not None:
            return out
    latex = (it.get("latex") or "").strip()
    if _is_real_latex(latex):
        return '<div class="equation">\\[%s\\]</div>' % _esc(latex)
    if latex and _is_prose_not_maths(latex):
        # Mis-transcribed prose. It is already on the page as the heading or paragraph it was
        # copied from, so rendering it again would duplicate it.
        return ""
    columned = _columned_html(it, _GEO)
    if columned:
        return '<div class="equation">%s</div>' % columned
    printed = _printed_lines(it)
    if printed:
        return ('<div class="equation">%s</div>'
                % "".join('<div class="eqline">%s</div>' % runs_to_html(r) for r in printed))
    body = runs_to_html(it["runs"]).strip()
    if body:
        return '<div class="equation">%s</div>' % body.replace("\n", "<br>")
    # Nothing renders. The block is genuinely unreadable from the data: A2S returned "unsure"
    # and A2's recorded box points at the paragraph beside it rather than at the equation, so
    # there is neither a transcription to set nor a region to crop.
    #
    # A yellow diagnostic box in the middle of a chapter is not an improvement on that. The gap is
    # already reported -- the build prints a count, the Markdown names the block, and the bundle
    # manifest records it -- so omitting it here hides nothing from anyone who needs to know, and
    # spares the reader a message meant for the pipeline.
    return ""



def _merge_intext_runs(items):
    """Fold a split Intext Questions set back into one block, in place."""
    first = None
    for it in list(items):
        if it["role"] != "intext":
            continue
        if first is None:
            first = it
            continue
        first["text"] = first["text"].rstrip() + "\n" + it["text"].lstrip()
        first["runs"] = (first["runs"] + [{"t": "\n", "v": "", "b": False}] + it["runs"])
        first["lines"] = (first.get("lines") or []) + (it.get("lines") or [])
        items.remove(it)


def _side_by_side_runs(items):
    """Split a page's items into [(kind, [items])] where kind is "row" or "flow".

    A "row" is a stretch the book sets in TWO columns at once -- a structural diagram in the outer
    column with the prose that belongs to it alongside. Those stretches are laid out as an
    explicit two-column row rather than with CSS floats.

    Floats were the first attempt and they are the wrong tool here. A float only shortens the LINE
    boxes beside it, so a paragraph that also carries a measured left inset ends up shrunk twice --
    once by its own indent and again by the float -- and on p016 that squeezed the prose beside the
    tetrahedral-splitting diagram to about four characters a line. A row says what the page
    actually does: two columns, side by side, each at its measured width.
    """
    out, run = [], []
    for it in items:
        if it["column"] in ("left", "right") and it.get("bbox"):
            run.append(it)
            continue
        if run:
            out.extend(_bands(run))
            run = []
        out.append(("flow", [it]))
    if run:
        out.extend(_bands(run))
    return out


def _bands(run):
    """Split a two-column run into the BANDS the book actually prints.

    A run of left/right items is not one row. On p016 the run holds, in reading order, the prose
    beside Fig 5.9, the figure itself, the 5.5.5 heading and the prose beside THAT -- two separate
    bands, one above the other. Laid out as a single row they collapse into two stacked columns,
    which puts the 5.5.5 heading underneath the figure and both paragraphs in one column: the page
    reads top-to-bottom in the wrong order.

    A band is a set of items that actually share horizontal space on the page, which the measured
    y-extents say directly.
    """
    # Walked in READING ORDER, never sorted by position. Sorting re-ordered the page: on p014 the
    # Solution to Example 5.7 was moved below the Crystal Field Theory text that follows it, and
    # on p021 the second half of the Summary landed after the Exercises heading. A2's order is the
    # order the chapter is read in and nothing here may change it; position only decides which
    # consecutive items share a band.
    bands, current, bottom = [], [], None
    for it in run:
        y0, y1 = it["bbox"][1], it["bbox"][3]
        if current and y0 >= bottom - _BAND_OVERLAP:
            bands.append(current)
            current, bottom = [it], y1
            continue
        current.append(it)
        bottom = max(bottom, y1) if bottom is not None else y1
    if current:
        bands.append(current)
    return [("row" if _is_row(b) else "flow", b) for b in bands]


# Two items share a band when their printed y-ranges overlap by more than this fraction of the
# sheet. Below it they are simply stacked, however close together they sit.
_BAND_OVERLAP = 0.012


def _is_row(run):
    """A run is a two-column stretch only if it really has content on BOTH sides."""
    return (any(i["column"] == "left" for i in run)
            and any(i["column"] == "right" for i in run))


def _row_html(run, page_num, fig_rel, figures, geo, render):
    """One measured two-column stretch: the outer column, then the body column."""
    # Within a band the two columns are genuinely side by side, so emitting the outer column
    # before the body column is the page's arrangement, not a re-ordering of the reading.
    left = [i for i in run if i["column"] == "left"]
    right = [i for i in run if i["column"] != "left"]
    lx0 = min(i["bbox"][0] for i in left)
    lx1 = max(i["bbox"][2] for i in left)
    rx0 = min(i["bbox"][0] for i in right) if right else geo["body_left"]
    flow_left = geo["edge_l"] + geo["margin_w"] + geo["gutter"]
    pull = flow_left - lx0 * geo["sheet_w"]
    left_w = (lx1 - lx0) * geo["sheet_w"]
    gap = max(2.0, (rx0 - lx1) * geo["sheet_w"])
    return ('<div class="row" style="margin-left: -%.1fmm;">'
            '<div class="row-left" style="flex: 0 0 %.1fmm; margin-right: %.1fmm;">%s</div>'
            '<div class="row-right">%s</div></div>'
            % (pull, left_w, gap,
               "".join(render(i) for i in left),
               "".join(render(i) for i in right)))


_GEO = {}
_LABELS = {}      # (page, block n) -> vector file for that panel's printed label
_FIG_REL = ""

# Render hooks, so a sibling subject flow can change HOW a block is drawn without forking this
# module's 2,000 lines of page layout.
#
# The Chemistry Class 12 book is one book: Unit 5 (inorganic) and Unit 9 (organic) share a trim,
# a palette, a furniture set and a column system, and all of that is measured and laid out here.
# What genuinely differs is the chemistry -- organic prints reaction schemes and ring structures
# where inorganic prints coordination diagrams. Copying the file to change those two renderers
# would duplicate everything that is the same and guarantee the two copies drift, which is the
# failure this project's own notes warn about repeatedly. Two hooks are enough.
HOOKS = {}

_PANEL_CLASS = {"example": "panel-example", "feature": "panel-feature",
                "summary": "panel-summary"}


def build_html(m, chapter, title, fig_rel, figures, geo, portraits, gap_sink=None,
               heads=None):
    heads = heads or {}
    global _GEO, _FIG_REL
    _GEO = geo
    _FIG_REL = fig_rel
    sheets, gaps_total = [], 0
    for page in m["pages"]:
        body, page_gaps = [], []
        for panel_bbox, group in _panel_group(page["items"]):
            if panel_bbox:
                kind = (group[0]["panel"] or {}).get("kind", "example")
                side = (group[0]["panel"] or {}).get("tab_side", "right")
                cls = _PANEL_CLASS.get(kind, "panel-example")
                scientist = any(g["role"] == "scientist" for g in group)
                inner = []
                for it in group:
                    if scientist and it["role"] == "figure":
                        key = (page["page"], it["n"])
                        if key in figures:
                            portraits.add(key)
                            inner.append(
                                '<div class="portrait"><img src="%s/%s" alt="portrait">'
                                '<span class="years">%s</span></div>'
                                % (fig_rel, figures[key], _esc(it.get("caption") or "")))
                            continue
                    inner.append(_item_html(it, page["page"], fig_rel, figures, geo, heads))
                    page_gaps.extend(_gaps_of(it))
                # The panel is placed at ITS OWN measured extent, not at a fixed inset. A single
                # negative margin for every panel overflowed the sheet by ~31mm on the right,
                # which cut off the blue tab and the cyan "Example 5.1" label set against it --
                # and this book does not place its panels alike anyway: p003 runs x 0.107-0.932,
                # p007 x 0.073-0.925, p020 x 0.138-0.911.
                px0, _py0, px1, _py1 = panel_bbox
                flow_left = geo["edge_l"] + geo["margin_w"] + geo["gutter"]
                pull = flow_left - px0 * geo["sheet_w"]
                width = (px1 - px0) * geo["sheet_w"]
                style = ' style="margin-left: %.1fmm; margin-right: 0; width: %.1fmm;"' % (
                    -pull, width)
                body.append('<section class="panel %s tab-%s%s"%s>%s</section>'
                            % (cls, side, " panel-scientist" if scientist else "",
                               style, "".join(inner)))
                continue
            first_n = next((i["n"] for i in page["items"]), None)
            carried = page.get("continues")

            def render(it, _p=page["page"], _first=first_n, _carried=carried, _h=heads):
                if it["role"] == "intext":
                    rest = _strip_prefix(it["runs"], len("Intext Questions") + 1)
                    return ('<section class="marked" style="%s">'
                            '<span class="label">Intext Questions</span>%s</section>'
                            % (_size_style(it, geo), _list_html(rest)))
                frag = _item_html(it, _p, fig_rel, figures, geo, _h)
                if _carried and it["n"] == _first and it["role"] == "paragraph":
                    frag = frag.replace('class="para block"', 'class="para block flush"', 1)
                return frag

            # One Intext Questions box, not several. NCERT prints the set as a single panel, but
            # A2 splits it wherever a figure interrupts -- on Amines p004 "Intext Questions / 9.1"
            # and "9.2 (i) Write structures ..." came back as two boxes with the structures figure
            # between them, so the page showed the heading, then a box, then the rest loose. The
            # second and later pieces are folded into the first.
            _merge_intext_runs(group)

            for kind, run in _side_by_side_runs(group):
                if kind == "row":
                    for it in run:
                        it["in_row"] = True
                    body.append(_row_html(run, page["page"], fig_rel, figures, geo, render))
                else:
                    body.extend(render(it) for it in run)
                for it in run:
                    page_gaps.extend(_gaps_of(it))

        gaps_total += len(page_gaps)
        if gap_sink is not None:
            gap_sink.extend("page %03d: %s" % (page["page"], g) for g in page_gaps)
        # Extraction gaps are NOT printed on the reading page. They are still counted, still
        # returned to the caller, and still written into the Markdown export -- the owner asked
        # for the reader to be the book and nothing else, and a notice between every pair of
        # sheets is not in the book. Nothing is hidden by this: the build prints the chapter-wide
        # count, and `<CHAPTER>_INORGANIC.md` names each gap against the block it belongs to.
        gaps = ""

        folio = ""
        # The book prints NO folio on a chapter-opening page -- it paints a white patch over the
        # tab, which the measurement records. A2 still reports the number as removed furniture,
        # so taking the folio from A2 alone stamped a "118" the book does not show.
        # The book prints a folio on every page EXCEPT the chapter opener, where it paints a
        # white patch over the tab. Gating on whether the measurement happened to record the tab
        # dropped the footer from pages 134 and 137, which do print one.
        is_opener = page["page"] == m["pages"][0]["page"]
        if page["folio"] and not is_opener:
            side = "recto" if int(page["folio"]) % 2 else "verso"
            folio = ('<div class="folio folio-%s"><span class="head">%s</span>'
                     '<span class="num">%s</span><span class="rule"></span></div>'
                     % (side, _esc(page["running_header"]), _esc(page["folio"])))
        imprint = ('<div class="imprint">%s</div>' % _esc(page["imprint"])) if page["imprint"] else ""

        sheets.append('<section class="sheet" id="p%03d"><div class="flow">%s</div>%s%s</section>%s'
                      % (page["page"], "".join(body), folio, imprint, gaps))

    css = _css_for(m, geo)
    head = (
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s — %s</title>'
        '<link rel="stylesheet" href="vendor/katex.min.css">'
        '<style>%s</style>' % (_esc(chapter), _esc(title), css))
    toolbar = (
        '<div class="toolbar"><span class="name">%s</span>'
        '<span>%s</span><span class="spacer"></span>'
        '<input id="pg" value="1"><span>/ %d</span>'
        '<button id="zout">&minus;</button><span id="zoomv">100%%</span><button id="zin">+</button>'
        '<button id="prt">Print</button></div>'
        % (_esc(chapter), _esc(title), len(m["pages"])))
    katex = ('<script src="vendor/katex.min.js"></script>'
             '<script src="vendor/auto-render.min.js"></script>'
             '<script>document.addEventListener("DOMContentLoaded",function(){'
             'renderMathInElement(document.body,{delimiters:['
             '{left:"\\\\[",right:"\\\\]",display:true}],throwOnError:false});});</script>')
    return ("<!doctype html><html lang=\"en\"><head>%s</head><body>%s"
            "<main id=\"viewer\">%s</main>%s%s%s</body></html>"
            % (head, toolbar, "".join(sheets), katex, _JS, _FIT_PROBE)), gaps_total


def _gaps_of(it):
    """What this item's extraction is still missing, named concretely rather than hidden."""
    out = []
    if it.get("untranscribed") and not it.get("recovered_from_text_layer"):
        if it["role"] == "figure":
            # The diagram itself IS shown -- only its caption and labels are outstanding. Saying
            # "no transcription" overstated that: it reads as though the figure were absent.
            out.append("[%s] figure is shown, but its caption and labels are not yet "
                       "transcribed by A2S" % it["n"])
        else:
            out.append("[%s] %s has no A2S transcription" % (it["n"], it["a2_kind"]))
    elif it["role"] == "figure" and not (it.get("caption") or "").strip():
        out.append("[%s] figure has no transcribed caption" % it["n"])
    elif it["role"] == "table" and not (it.get("header") or []):
        out.append("[%s] table has no structured rows — shown as an image" % it["n"])
    if it.get("match_score") is not None and it["match_score"] < 0.75:
        out.append("[%s] matched to its printed position at only %.2f confidence"
                   % (it["n"], it["match_score"]))
    return out


def _css_for(m, geo):
    p = m["palette"]
    repl = {
        "@SHEET_W@": "%.1f" % geo["sheet_w"], "@SHEET_H@": "%.1f" % geo["sheet_h"],
        "@BODY_PT@": "%.2f" % m["body_size_pt"],
        "@ZOOM@": "%.4f" % geo.get("fit", 1.0),
        "@INDENT@": "%.2f" % geo["indent_mm"], "@LEADING@": "%.2f" % geo["leading"],
        "@EDGE_L@": "%.1f" % geo["edge_l"], "@MARGIN_W@": "%.1f" % geo["margin_w"],
        "@GUTTER@": "%.1f" % geo["gutter"], "@MEASURE@": "%.1f" % geo["measure"],
        "@TOP@": "%.1f" % geo["top"], "@BOTTOM@": "%.1f" % geo["bottom"],
        "@INK@": p["body_ink"], "@FURNITURE@": p["furniture_ink"],
        "@PANEL_LABEL@": p["panel_label_ink"], "@OBJECTIVES@": p["objectives_ink"],
        "@STRAPLINE@": p["strapline_ink"], "@EXAMPLE_TAB@": p["example_tab"],
        "@FEATURE_TAB@": p["feature_tab"], "@SUMMARY_TAB@": p["summary_tab"],
        "@MARGIN_BAR@": p["margin_bar"], "@TABLE_HEAD@": p["table_head"],
        "@FOLIO@": p["folio"], "@HAIRLINE@": p["hairline"],
        "@BANNER@": p["opener_banner"], "@BANNER_STRIP@": p["opener_strip"],
        "@BANNER_TAB@": p["opener_tab"],
        "@BANNER_H@": "%.1f" % geo["banner_h"], "@STRIP_H@": "%.1f" % geo["strip_h"],
        "@TAB_X@": "%.1f" % geo["tab_x"], "@TAB_W@": "%.1f" % geo["tab_w"],
        "@TAB_H@": "%.1f" % geo["tab_h"],
        "@TYPE_SHIFT@": "%.1f" % geo["type_shift"],
        "@FOLIO_BOTTOM@": "%.1f" % geo["folio_bottom"],
        "@FOLIO_W@": "%.1f" % geo["folio_w"],
        "@IMPRINT_BOTTOM@": "%.1f" % geo["imprint_bottom"],
    }
    css = _CSS
    for token, value in repl.items():
        css = css.replace(token, value)
    css += ("\n.list { margin: 0 0 1.6mm; }\n"
            ".list .li { display: flex; gap: 2.2mm; }\n"
            ".list .li-mark { flex: 0 0 auto; min-width: 7mm; padding-right: 1.6mm;"
            " font-weight: 700; color: var(--ink); }\n"
            ".list .li-body { flex: 1; text-align: justify; }\n"
            ".objectives .intro { margin-bottom: 1.2mm; }\n")
    return css


def _geometry(m, measurement):
    """Every length the stylesheet needs, in millimetres, derived from the measurement.

    Nothing here is a constant. The sheet is the book's own trim, the two columns are where its
    type is actually set, and the furniture positions are where its own vector rectangles sit.
    """
    sheet_w, sheet_h = m["trim_mm"]
    tm = m["text_measure"]
    margin_col = tm.get("margin_column") or [0.074, 0.278]
    # The body column's LEFT edge is where prose starts on an ordinary single-measure page. Taken
    # as the most common value across the chapter rather than the minimum, because on the pages
    # that run two real columns the minimum is the left column's edge, not the measure's.
    lefts = []
    for page in m["pages"]:
        for it in page["items"]:
            if it["role"] in ("paragraph", "list") and it.get("bbox") and it["column"] in ("right", "full"):
                lefts.append(round(it["bbox"][0], 2))
    body_left = max(set(lefts), key=lefts.count) if lefts else 0.302
    rights = [round(it["bbox"][2], 2) for page in m["pages"] for it in page["items"]
              if it["role"] in ("paragraph", "list") and it.get("bbox")]
    body_right = max(set(rights), key=rights.count) if rights else 0.90

    edge_l = margin_col[0] * sheet_w
    margin_w = (margin_col[1] - margin_col[0]) * sheet_w
    gutter = max(2.0, (body_left - margin_col[1]) * sheet_w)
    measure = (body_right - body_left) * sheet_w

    # The first-line indent, measured off the chapter's own paragraphs: the first printed line's
    # left edge against the median of the lines under it.
    indents = []
    for page in measurement["pages"]:
        for tb in page["text_blocks"]:
            if tb.get("role") != "body" or len(tb.get("lines") or []) < 3:
                continue
            xs = [ln["bbox"][0] for ln in tb["lines"]]
            rest = sorted(xs[1:])
            delta = (xs[0] - rest[len(rest) // 2]) * sheet_w
            if 0.5 < delta < 14.0:
                indents.append(delta)
    indents.sort()
    indent_mm = indents[len(indents) // 2] if indents else 6.3

    # The MEDIAN first-block position, not the minimum. Taking the minimum let a single page
    # that starts low set a deep top margin for all 23 sheets, shrinking the text area on every
    # one of them and forcing the print fit down to compensate.
    firsts = []
    for page in m["pages"]:
        if page["page"] == m["pages"][0]["page"]:
            continue
        ys = [it["bbox"][1] for it in page["items"] if it.get("bbox")]
        if ys:
            firsts.append(min(ys))
    firsts.sort()
    top = (firsts[len(firsts) // 2] if firsts else 0.083) * sheet_h

    # Furniture positions, read off the measured rectangles rather than assumed.
    folio_rects = [f for page in m["pages"] for f in page["furniture"] if f["role"] == "folio_tab"]
    folio_bottom = ((1.0 - max(f["bbox"][3] for f in folio_rects)) * sheet_h) if folio_rects else 7.0
    folio_w = ((sum(f["bbox"][2] - f["bbox"][0] for f in folio_rects) / len(folio_rects))
               * sheet_w) if folio_rects else 8.0

    opener = next((page for page in m["pages"] if page["page"] == 1), None)
    banner_h, strip_h, tab_x, tab_w, tab_h = 60.0, 3.0, 55.0, 19.0, 20.0
    banner_box = tab_box = None
    type_shift = 0.0
    if opener:
        for f in opener["furniture"]:
            x0, y0, x1, y1 = f["bbox"]
            if f["role"] == "opener_banner":
                banner_h = (y1 - y0) * sheet_h
                banner_box = (x0, x1)
            elif f["role"] == "opener_strip":
                strip_h = max(1.0, (y1 - y0) * sheet_h)
            elif f["role"] == "opener_tab":
                tab_x = max(0.0, x0 - (body_left - 0.02)) / max(1e-6, body_right - body_left) * 100
                tab_w = (x1 - x0) / max(1e-6, body_right - body_left) * 100
                tab_h = max(0.0, y1) * sheet_h
                tab_box = (x0, x1)
    if banner_box and tab_box:
        banner_mid = (banner_box[0] + banner_box[1]) / 2.0
        tab_mid = (tab_box[0] + tab_box[1]) / 2.0
        span = max(1e-6, banner_box[1] - banner_box[0])
        type_shift = max(0.0, min(40.0, (banner_mid - tab_mid) / span * 200.0))

    return {
        "body_pt": m["body_size_pt"], "indent_mm": indent_mm,
        "sheet_w": sheet_w, "sheet_h": sheet_h,
        "edge_l": edge_l, "margin_w": margin_w, "gutter": gutter, "measure": measure,
        "body_left": body_left, "body_right": body_right,
        # Reserved from the MEASURED folio position plus the imprint line below it. A flat 22mm
        # was less than the furniture actually occupies, so on any page whose reflowed copy ran
        # past the book's own depth the last lines were set underneath the folio.
        # Reserved from the MEASURED folio, plus just enough for the imprint line beneath it.
        # A flat 10mm of slack under the folio cost ~7mm of text area on every sheet.
        "top": top, "bottom": max(18.0, folio_bottom + 4.0), "leading": 1.20,
        "banner_h": banner_h, "strip_h": strip_h,
        "tab_x": tab_x, "tab_w": tab_w, "tab_h": tab_h,
        "folio_bottom": folio_bottom, "folio_w": folio_w, "imprint_bottom": 3.0,
        # How far left of the banner's own centre the title stack sits, as a percentage of the
        # banner's width -- derived from the measured tab, which is what the type centres on.
        "type_shift": type_shift,
    }


_FIT_PROBE = """<script>
(function () {
  /* Reports how far the WORST sheet overruns its own depth, into document.title, where a
     headless --dump-dom pass can read it. Measuring in the real engine is the only honest way to
     ask this: it depends on the web font's metrics, on hyphenation and on where KaTeX breaks, and
     none of that is knowable from the source PDF. */
  function probe() {
    var worst = 1;
    document.querySelectorAll('.sheet').forEach(function (sheet) {
      var flow = sheet.querySelector('.flow');
      if (!flow) return;
      var cs = getComputedStyle(sheet);
      /* Measured against the sheet's INTENDED height, taken from the stylesheet variable -- never
         against its computed height. On screen the sheet grows to fit its content, so its
         computed height always equals what is in it and the ratio came out 1.00 for every page:
         the loop concluded the chapter fitted at full size while pages were in fact running past
         the folio and being clipped in print. */
      var mm = parseFloat(getComputedStyle(document.documentElement)
                            .getPropertyValue('--sheet-h')) || 0;
      var sheetPx = mm * 96 / 25.4;
      var avail = sheetPx - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
      var z = parseFloat(getComputedStyle(flow).zoom) || 1;
      if (avail > 0) worst = Math.max(worst, (flow.scrollHeight * z) / avail);
    });
    document.title = 'FIT:' + worst.toFixed(4);
  }
  if (document.readyState === 'complete') setTimeout(probe, 400);
  else window.addEventListener('load', function () { setTimeout(probe, 400); });
})();
</script>"""


def _chrome():
    return next((c for c in (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"), shutil.which("chromium")) if c and os.path.exists(c)), None)


def _measure_fit(html_path):
    """The worst sheet's overrun as a ratio (1.0 = everything fits), or None.

    NCERT's typesetter breaks lines and places figures by hand, so the printed page packs tighter
    than any automatic reflow of the same words. Without correcting for that the chapter printed
    43 sheets for 23 book pages -- every page that overran spilled onto a nearly empty second one.
    The correction is measured rather than guessed, because how much a page overruns depends on
    the substituted font's metrics and on where the browser hyphenates.
    """
    chrome = _chrome()
    if not chrome:
        return None
    try:
        res = subprocess.run([chrome, "--headless", "--disable-gpu", "--dump-dom",
                              "--virtual-time-budget=30000",
                              "file://" + os.path.abspath(html_path)],
                             capture_output=True, text=True, timeout=300)
    except (subprocess.SubprocessError, OSError):
        return None
    m = re.search(r"FIT:([0-9.]+)", res.stdout or "")
    return float(m.group(1)) if m else None


def _print_pdf(html_path, pdf_path):
    """Print the reader page to PDF with headless Chrome. Returns the sheet count, or None.

    Chrome rather than a Python HTML-to-PDF library, for the same reason the bundle exporter uses
    it: the page already carries real `@page` rules at this book's measured trim and loads its own
    web fonts, so printing it in the engine that renders it gives a PDF that matches what the
    reader shows instead of a second renderer's approximation of it.
    """
    chrome = _chrome()
    if not chrome:
        return None
    try:
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=40000",
                        "--print-to-pdf=" + pdf_path,
                        "file://" + os.path.abspath(html_path)],
                       capture_output=True, timeout=420)
    except (subprocess.SubprocessError, OSError) as exc:
        print("  (PDF step failed: %s)" % exc)
        return None
    if not os.path.exists(pdf_path):
        return None
    try:
        with fitz.open(pdf_path) as doc:
            return doc.page_count
    except Exception:
        return 0



_BUNDLE_README = """# {chapter} — export bundle

{title}

Built {built_at} by `{builder}` from this pipeline's extracted data, with the printed layout
measured directly from the source PDF's text and vector layer.

## What each file is

| File | What it is | Use it for |
|---|---|---|
| `{chapter}_{kind}.pdf` | The chapter printed one book page per sheet, at the book's own {trim} trim. | Reading offline, sharing, printing. |
| `{chapter}_READER.html` | The same chapter as a page: selectable, searchable, responsive. | Reading, searching, copying formulae. |
| `{chapter}_{kind}.md` | The same content as Markdown, with its structure named in fences. | Feeding other tools, diffing, pasting elsewhere. |
| `{chapter}_layout.json` | The measured printed layout: trim, columns, every panel and rule with its own ink, and each block's position, size and formula typing. | Rebuilding the page; restyling without re-measuring. |
| `manifest.json` | Provenance and gaps: which agent run produced every page, file checksums, what is still outstanding. | Auditing what a given bundle actually showed. |
| `figures/` | Diagram crops cut from the source pages at 300 dpi. | Diagrams the text cannot carry. |
| `vendor/`, `fonts/` | KaTeX and TeX Gyre Bonum (a free Bookman metric clone, the book's body face), vendored so the page renders with no network. | — |

## Three things to know

**This bundle is not a release.** `docs/SPEC.md` releases chapters through `export_tables.py`
after a sign-off row in `review/releases.csv`. These are keepable artifacts built from the same
extracted data, not that release — do not substitute one for the other.

**The crops carry NO watermark.** This differs from the Biology and Physics bundles, and the
reason is the source: those books are flat scans with `© NCERT / not to be republished` baked
into the only raster on the page. The latest-edition Chemistry PDFs are not scans — the mark is a
separate image object, repeated at the same rectangle on every page, so it is identified and
removed before any figure is rendered.

**Formulae are text, not pictures.** `[Co(NH₃)₆]³⁺` is live, selectable, searchable text, with its
sub- and superscripts recovered from the source's own span sizes and baselines. {script_chars}
characters in this chapter are set as real script. Only genuine **diagrams** are images: {n_fig}
of them, against {n_text} blocks of text. No equation is an image.

## Completeness at build time

{gaps}
"""


def write_bundle(chapter, title, m, geo, figures, gaps_list, review, fig_dir_name,
                 reader_path, md_path, layout_path, pdf_path, pdf_pages,
                 kind="INORGANIC", builder="scripts/export_inorganic_chemistry_html.py",
                 subject="inorganic chemistry"):
    """Assemble `exports/chapters/<CHAPTER>/` so this chapter sits beside the other bundles.

    Written here rather than through `scripts/export_chapter_bundle.py` for the same reason this
    whole flow is separate: that script drives the shared Biology/Physics exporters and copies the
    files they produce under the names they produce them under. Pointing it at this chapter would
    mean teaching it a second set of names and a second renderer, which is how a change made for
    one book starts reaching another.
    """
    out_dir = rc.pp("exports", "chapters", chapter)
    os.makedirs(out_dir, exist_ok=True)

    copies = [
        (pdf_path, "%s_%s.pdf" % (chapter, kind)),
        (md_path, "%s_%s.md" % (chapter, kind)),
        (layout_path, chapter + "_layout.json"),
    ]
    for src, dest in copies:
        if src and os.path.exists(src):
            shutil.copy2(src, os.path.join(out_dir, dest))

    # The reader references ../<CHAPTER>_inorg_figures/ from exports/review/html; inside the
    # bundle those sit in figures/ beside it, so the hrefs are rewritten to match.
    if os.path.exists(reader_path):
        with open(reader_path, encoding="utf-8") as fh:
            page = fh.read()
        page = page.replace("../%s/" % fig_dir_name, "figures/")
        with open(os.path.join(out_dir, chapter + "_READER.html"), "w", encoding="utf-8") as fh:
            fh.write(page)

    for src_dir, dest_name in ((os.path.join(review, fig_dir_name), "figures"),
                               (os.path.join(review, "html", "vendor"), "vendor"),
                               (os.path.join(review, "html", "fonts"), "fonts")):
        if os.path.isdir(src_dir):
            dest = os.path.join(out_dir, dest_name)
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            shutil.copytree(src_dir, dest)

    files = {}
    for root, _dirs, names in os.walk(out_dir):
        for fn in sorted(names):
            if fn in ("manifest.json", "README.md"):
                continue
            full = os.path.join(root, fn)
            h = hashlib.sha256()
            with open(full, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            files[os.path.relpath(full, out_dir)] = {
                "bytes": os.path.getsize(full), "sha256": h.hexdigest()}

    n_fig = sum(1 for page in m["pages"] for it in page["items"] if it["role"] == "figure")
    n_text = sum(len(page["items"]) for page in m["pages"]) - n_fig
    script_chars = sum(len(r["t"]) for page in m["pages"] for it in page["items"]
                       for r in it["runs"] if r.get("v"))
    built_at = datetime.datetime.now().astimezone().isoformat(timespec="seconds")

    manifest = {
        "chapter": chapter,
        "title": title,
        "built_at": built_at,
        "built_by": builder,
        "subject_flow": subject,
        "this_is_not_a_release": (
            "docs/SPEC.md releases chapters via export_tables.py after a sign-off row in "
            "review/releases.csv. This bundle is a keepable artifact built from the same "
            "extracted data, not that release."),
        "watermark": (
            "NONE. Unlike the Biology and Physics bundles, this book's source is not a scan: "
            "'(c) NCERT / not to be republished' is a separate image object repeated at the same "
            "rectangle on every page, identified as such and removed before every crop."),
        "trim_mm": m["trim_mm"],
        "trim_pt": m["trim_pt"],
        "body_size_pt": m["body_size_pt"],
        "print_scale": round(geo.get("print_fit", 1.0), 3),
        "pages_in_book": len(m["pages"]),
        "pages_in_pdf": pdf_pages,
        "blocks": {"figures_as_images": n_fig, "blocks_as_text": n_text,
                   "characters_set_as_sub_or_superscript": script_chars,
                   "equations_as_images": 0},
        "page_provenance": {"page_%03d" % page["page"]: {"A2": page["run"]}
                            for page in m["pages"]},
        "outstanding": gaps_list,
        "files": files,
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    gap_text = ("\n".join("- " + g for g in gaps_list) if gaps_list
                else "- every block in the chapter is transcribed")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(_BUNDLE_README.format(
            chapter=chapter, title=title, built_at=built_at, kind=kind, builder=builder,
            trim="%.1f x %.1f mm" % (m["trim_mm"][0], m["trim_mm"][1]),
            script_chars=script_chars, n_fig=n_fig, n_text=n_text, gaps=gap_text))
    return out_dir, files


# --------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("chapter", help="e.g. CHE12L-ch05")
    ap.add_argument("--pdf", required=True, help="path to this chapter's source PDF")
    ap.add_argument("--title", default=None, help="chapter title for the header")
    ap.add_argument("--fit", type=float, default=None,
                    help="force a body-type scale instead of measuring the page fit "
                         "(1.0 = the book's own size)")
    ap.add_argument("--no-bundle", action="store_true",
                    help="skip assembling exports/chapters/<CHAPTER>/")
    ap.add_argument("--no-pdf", action="store_true",
                    help="skip the printed PDF (the HTML and Markdown are still written)")
    ap.add_argument("--skip-measure", action="store_true",
                    help="reuse the existing measurement instead of re-reading the PDF")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        print("source PDF not found: " + args.pdf, file=sys.stderr)
        return 1

    review = rc.pp("exports", "review")
    html_dir = os.path.join(review, "html")
    data_dir = os.path.join(review, "html_data")
    fig_dir_name = args.chapter + "_inorg_figures"
    fig_dir = os.path.join(review, fig_dir_name)
    for d in (html_dir, data_dir, fig_dir):
        os.makedirs(d, exist_ok=True)

    # ---- 1. measure ----------------------------------------------------------------------
    layout_path = os.path.join(data_dir, args.chapter + "_inorganic_layout.json")
    if args.skip_measure and os.path.exists(layout_path):
        measurement = model_mod.load_measurement(args.chapter)
        print("measurement: reused %s" % os.path.relpath(layout_path, rc.pp()))
    else:
        measurement = measure_pdf(args.pdf)
        measurement["chapter"] = args.chapter
        with open(layout_path, "w", encoding="utf-8") as fh:
            json.dump(measurement, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("measurement: %d pages, %d panels, trim %.0fx%.0fpt"
              % (measurement["pages_measured"],
                 sum(len(p["panels"]) for p in measurement["pages"]),
                 measurement["trim_pt"][0], measurement["trim_pt"][1]))

    # ---- 2. model ------------------------------------------------------------------------
    m = model_mod.build(args.chapter, measurement)
    if not m["pages"]:
        print("no A2 output found for %s" % args.chapter, file=sys.stderr)
        return 1
    n_items = sum(len(p["items"]) for p in m["pages"])
    print("model: %d pages, %d blocks" % (len(m["pages"]), n_items))

    # ---- 3. diagram crops ----------------------------------------------------------------
    overlays = measurement.get("page_overlays_ignored") or []
    body_left = _geometry(m, measurement)["body_left"]
    doc = fitz.open(args.pdf)
    figures, n_fig = {}, 0
    for page in m["pages"]:
        for it in page["items"]:
            if it["role"] not in ("figure", "table"):
                continue
            bbox = it.get("art_bbox") or it.get("bbox")
            if it["role"] == "table" and (it.get("header") or []):
                continue              # transcribed: it is set as a real table, not a picture
            if (it["role"] == "table" and not (it.get("header") or [])
                    and it.get("has_artwork") is False):
                continue              # pure type: rendered as text, never as a picture of text
            if not bbox:
                continue
            name = "p%03d_b%s.png" % (page["page"], it["n"])
            # Prose on this page that the crop must not pick up: lines set at body size in the
            # body column, excluding any that belong to this figure's own region entirely.
            prose = [ln["bbox"] for ln in _page_prose(measurement, page["page"], body_left)]
            # `keep` protects a block's OWN content from redaction -- but NOT its caption, which
            # is deliberately removed from the crop and set as text underneath instead.
            caption_boxes = {tuple(round(v, 4) for v in ln["bbox"])
                             for ln in (it.get("caption_lines") or [])}
            keep = [ln["bbox"] for ln in (it.get("lines") or [])
                    if tuple(round(v, 4) for v in ln["bbox"]) not in caption_boxes]
            if crop_diagram(doc, page["page"], bbox, os.path.join(fig_dir, name), overlays,
                            prose + [ln["bbox"] for ln in (it.get("caption_lines") or [])],
                            keep):
                figures[(page["page"], it["n"])] = name
                n_fig += 1
    doc.close()
    # The book's display-face headings, taken as vector so their letterforms are the book's own
    # rather than the nearest licensable approximation.
    # Section headings are TEXT. This is settled, not a trade-off to revisit.
    #
    # Taking them as vector gives the book's exact letterforms, and after the CropBox fix the crop
    # is exact -- but the owner rejected it twice, and the reason stands on its own: a heading that
    # is an image cannot reflow, cannot be searched, cannot be selected, and goes wrong silently
    # when anything about the crop is off. Text can only ever be the wrong FACE, which is a
    # smaller failure than being the wrong SHAPE.
    heads = {}
    n_heads = sum(1 for page in m["pages"] for it in page["items"]
                  if it["role"] == "margin_heading")
    print("headings: %d set as live text (searchable, reflowable, never cropped)" % n_heads)
    # Panel labels are text, for the same reason as the headings above.
    _LABELS.clear()

    print("figures: %d diagram crops (watermark removed), %d equations kept as text"
          % (n_fig, sum(1 for p in m["pages"] for it in p["items"] if it["role"] == "equation")))

    # ---- 4. Markdown ---------------------------------------------------------------------
    title = args.title or args.chapter
    md = build_markdown(m, args.chapter, title, args.pdf, fig_dir_name, figures)
    md_path = os.path.join(review, args.chapter + "_INORGANIC.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(md)
    print("markdown: %s (%.0f KB)" % (os.path.relpath(md_path, rc.pp()), len(md) / 1024))

    # ---- 5. HTML -------------------------------------------------------------------------
    geo = _geometry(m, measurement)
    out_path = os.path.join(html_dir, args.chapter + "_INORG_READER.html")

    gap_list = []

    def _write(fit):
        geo["fit"] = fit
        del gap_list[:]
        html_doc, n_gaps = build_html(m, args.chapter, title, "../" + fig_dir_name, figures,
                                      geo, set(), gap_list, heads)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(html_doc)
        return html_doc, n_gaps

    doc_html, gaps = _write(args.fit if args.fit else 1.0)
    print("html    : %s (%.0f KB)  |  %d outstanding extraction gap(s) (named in the Markdown)"
          % (os.path.relpath(out_path, rc.pp()), len(doc_html) / 1024, gaps))

    pdf_pages_written = None

    # ---- 6. PDF --------------------------------------------------------------------------
    #
    # The PDF is printed from its OWN copy of the page, not from the reader.
    #
    # They want different things. The reader scrolls, so it should show the chapter at the book's
    # own type size and let a page be as deep as its content needs. A printed sheet cannot: a book
    # page that runs even 2% past the sheet either spills a sliver onto a second page or, with
    # break-inside honoured, pushes the whole sheet over and leaves a blank behind it. Making the
    # reader pay for that -- shrinking the type a reader sees so that a printer is happy -- is the
    # wrong trade, so the fit is applied only to the copy that gets printed.
    if not args.no_pdf:
        pdf_out = os.path.join(review, args.chapter + "_INORGANIC.pdf")
        print_path = os.path.join(html_dir, args.chapter + "_INORG_PRINT.html")

        def _write_print(fit):
            geo["fit"] = fit
            html_doc, _ = build_html(m, args.chapter, title, "../" + fig_dir_name, figures,
                                     geo, set(), None, heads)
            with open(print_path, "w", encoding="utf-8") as fh:
                fh.write(html_doc)

        fit, first = args.fit or 1.0, None
        _write_print(fit)
        if not args.fit:
            # ITERATED and damped: trimming the type reflows every line, so the next measurement
            # is not the previous one scaled. Each pass asks the real engine again and tightens
            # only as far as that answer demands, giving the LARGEST size at which every book page
            # still prints on one page.
            for _ in range(6):
                ratio = _measure_fit(print_path)
                if ratio is None:
                    break
                if first is None:
                    first = ratio
                # Target a little UNDER the sheet, not exactly at its edge. At the brim three
                # sheets still spilled their absolutely-positioned folio and imprint onto a page
                # of their own -- three printed pages carrying nothing but "Reprint 2026-27".
                if ratio <= 0.985:
                    break
                # Zoom scales BOTH dimensions, so the correction is the ratio itself, not its
                # square root: halving the overrun needs only that much less zoom.
                fit = max(_FIT_FLOOR, fit * max(0.90, 1.0 / ratio))
                _write_print(fit)
                if fit <= _FIT_FLOOR + 1e-9:
                    break
        if first is None:
            print("fit     : not measured")
        elif fit >= 0.999:
            print("fit     : printed at the book's own body size; reader likewise")
        else:
            print("fit     : reader at the book's own size; PRINT copy at %.0f%% "
                  "(worst sheet overran by %.1f%%)" % (fit * 100, (first - 1) * 100))
        geo["fit"] = 1.0
        geo["print_fit"] = fit
        pages_written = pdf_pages_written = _print_pdf(print_path, pdf_out)
        if pages_written is None:
            print("pdf     : skipped (no Chrome/Edge/Chromium found)")
        else:
            print("pdf     : %s (%d sheets, %.1f MB)"
                  % (os.path.relpath(pdf_out, rc.pp()), pages_written,
                     os.path.getsize(pdf_out) / 1e6))
            if pages_written != len(m["pages"]):
                print("          NOTE: %d printed pages for %d book pages"
                      % (pages_written, len(m["pages"])))
        try:
            os.remove(print_path)
        except OSError:
            pass
    # ---- 7. bundle -----------------------------------------------------------------------
    if not args.no_bundle:
        bundle_dir, bundle_files = write_bundle(
            args.chapter, title, m, geo, figures, gap_list, review, fig_dir_name,
            out_path, md_path,
            os.path.join(data_dir, args.chapter + "_inorganic_layout.json"),
            os.path.join(review, args.chapter + "_INORGANIC.pdf") if not args.no_pdf else None,
            pdf_pages_written)
        print("bundle  : %s (%d files, %.1f MB)"
              % (os.path.relpath(bundle_dir, rc.pp()), len(bundle_files),
                 sum(v["bytes"] for v in bundle_files.values()) / 1e6))

    print("geometry: sheet %.1fx%.1fmm | margin col %.1fmm | gutter %.1fmm | measure %.1fmm"
          % (geo["sheet_w"], geo["sheet_h"], geo["margin_w"], geo["gutter"], geo["measure"]))
    print("built at %s" % datetime.datetime.now().astimezone().isoformat(timespec="seconds"))
    return run_checks(args.chapter, "inorganic")


def run_checks(chapter, kind):
    """Run the export's own invariant checks and make the BUILD fail if they fail.

    This is the pipeline change that matters. Until now a build printed "built at ..." and exited
    0 whatever it had produced -- so a chapter could ship with a worked example printed twice, a
    structure cropped in half and a heading broken mid-word, and nothing said a word. Every defect
    in the owner's review reached them that way. A build that cannot fail is not a build; it is a
    file copier.

    The checks are not a substitute for looking at the page -- a script cannot see a clipped
    benzene ring, which is what step A2R exists for -- but they catch, in seconds, every class of
    defect that can be stated as a rule.
    """
    script = rc.pp("scripts", "check_%s_export.py" % kind)
    if not os.path.exists(script):
        print("checks  : none defined for %s" % kind)
        return 0
    res = subprocess.run([sys.executable, script, chapter], capture_output=True, text=True)
    tail = [l for l in (res.stdout or "").strip().splitlines() if l.strip()]
    failed = [l for l in tail if l.strip().startswith("FAIL")]
    print("checks  : %s" % (tail[-1] if tail else "no output"))
    for line in failed:
        print("          " + line.strip())
    if failed:
        print("          BUILD NOT CLEAN -- the files above were written, but do not ship them.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
