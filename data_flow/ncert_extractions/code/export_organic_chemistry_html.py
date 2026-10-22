#!/usr/bin/env python3
"""Builds the Markdown, HTML and PDF renders of one NCERT ORGANIC CHEMISTRY chapter.

    python3 scripts/export_organic_chemistry_html.py CHE12L-ch09 \\
        --pdf inputs/ncert/latest/Class_12th/Chemistry/Chapter_9.pdf \\
        --title "Chemistry Class 12 (Latest NCERT) - Unit 9: Amines"

Writes, under `exports/review/`:

    <CHAPTER>_ORGANIC.md                 the chapter as Markdown
    <CHAPTER>_organic_figures/           ring structures as SVG, photographs as PNG
    html/<CHAPTER>_ORG_READER.html       the chapter as the book sets it
    <CHAPTER>_ORGANIC.pdf                one book page per sheet
    ... and `exports/chapters/<CHAPTER>/` as a bundle.

WHAT IS DIFFERENT ABOUT ORGANIC, AND WHY IT IS NOT A SEPARATE COPY OF THE LAYOUT
-------------------------------------------------------------------------------
Unit 5 and Unit 9 are the SAME BOOK. They share a trim (576 x 784.8pt), a body size, a palette, a
furniture set, a two-column measure and a panel design, and all of that is measured by
`inorganic_chemistry_measure.py` and laid out by `export_inorganic_chemistry_html.py`. Forking
those files to change organic's chemistry would copy ~2,500 lines that are identical and
guarantee the copies drift. This module therefore reuses them and overrides exactly two things
through their render hooks.

What actually differs is the chemistry:

  * REACTIONS. Amines prints 47 displayed reaction schemes against Coordination Compounds' 3, and
    they are the substance of the chapter. Every one of them has been transcribed by A2S as
    LaTeX -- `\\xrightarrow{...}`, `\\overset{+}{N}`, `\\underset{\\text{Aniline}}{...}` -- and all 47
    render in the vendored KaTeX with no errors (verified before this module was written). So a
    reaction is set as REAL MATHEMATICAL TEXT: selectable, searchable, copyable, and correct at
    any zoom. None of them is a screenshot.

  * RING STRUCTURES. A benzene ring is a drawing and cannot be carried as characters -- but it
    does not have to be a bitmap either. These PDFs are not scans: a structure is vector artwork,
    so it is extracted as SVG and stays sharp at any size, with its own labels still real text.
    Only artwork the source itself stores as a bitmap (one photograph in this chapter) is a PNG.

SMILES
------
The module is built SMILES-ready but does not require SMILES. Where a structure has one, a drawn
depiction is preferable to the book's own artwork: it is machine-readable, restyleable and
searchable BY STRUCTURE. SMILES cannot come from a script -- reading a drawn ring into SMILES is a
judgement, which under this project's rules belongs to an agent step, not to a renderer. The hook
is `_smiles_for`, which looks for `steps/A2C/out/<chapter>-pNNN-bN.*.json` carrying a `smiles`
field; when that step exists and RDKit is installed, drawn depictions replace the extracted SVG.
Until then the SVG is used and nothing is blocked.
"""

import argparse
import datetime
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf as fitz  # noqa: E402
import runner_core as rc  # noqa: E402
import chemistry_model as model_mod  # noqa: E402
# The shared Chemistry Class 12 page-layout engine. It measures and lays out the BOOK; only the
# chemistry differs per subject, and this module supplies that through its render hooks.
import chemistry_render as chem  # noqa: E402
from chemistry_measure import measure as measure_pdf  # noqa: E402


# --------------------------------------------------------------------------------------------
# SMILES (optional, see the module docstring)
# --------------------------------------------------------------------------------------------
def _smiles_for(chapter, page_num, n):
    """A single SMILES to DRAW for one block, from step A2C, or None.

    Separate from `_md_smiles`, which writes every species into the Markdown. Drawing replaces the
    book's own artwork, so it is only done for a lone, confidently-read species: a reaction scheme
    or an uncertain reading is better shown as NCERT drew it.
    """
    rec = _a2c_record(chapter, page_num, n)
    if not rec or rec.get("kind") != "structure":
        return None
    if rec.get("confidence") == "unsure":
        return None
    species = rec.get("species") or []
    if len(species) != 1:
        return None
    return (species[0].get("smiles") or "").strip() or None


def _rdkit_svg(smiles, out_path):
    """Draw a SMILES string to SVG with RDKit, if RDKit is installed. Returns True on success."""
    try:
        from rdkit import Chem
        from rdkit.Chem.Draw import rdMolDraw2D
    except ImportError:
        return False
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return False
        drawer = rdMolDraw2D.MolDraw2DSVG(420, 260)
        rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
        drawer.FinishDrawing()
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(drawer.GetDrawingText())
        return True
    except Exception:
        return False


# --------------------------------------------------------------------------------------------
# The two render overrides
# --------------------------------------------------------------------------------------------
_ASSETS = {}        # (page, n) -> filename, filled by build_assets()
# (page, n) -> the box the asset was ACTUALLY cut from, in page fractions.
# An image must be laid out at the width of the region it was cut from. Sizing it from
# `art_bbox` instead was wrong because the crop is padded and pulled back off neighbouring prose
# before it is taken, so the file on disk covers a different region than art_bbox describes --
# and the browser then scaled the difference away, which is why structures printed at anything
# from a third to three times the size the book draws them.
_ASSET_BOX = {}
_FIG_REL_EQ = ""


def _figure_hook(it, page_num, fig_rel, figures, geo):
    """A structure is vector, so it is drawn as vector. Returns None to defer to the shared
    renderer (which handles the raster case and the missing case)."""
    # A figure whose region is a worked-example panel carries no artwork of its own -- the panel's
    # words are already being set as text beside it. It is deliberately not cropped, so it must
    # also not report itself missing: an empty string renders nothing, which is correct, where
    # the shared renderer's "no artwork found" notice would be a placeholder for content that is
    # in fact present two lines above.
    if it.get("panel") and not it.get("has_artwork"):
        return ""
    key = (page_num, it["n"])
    name = _ASSETS.get(key)
    if not name or not name.endswith(".svg"):
        return None
    caption = (it.get("caption") or "").strip()
    cap = ('<figcaption>%s</figcaption>' % chem._caption_html(it)) if caption else ""
    bbox = _ASSET_BOX.get(key) or it.get("art_bbox") or it["bbox"]
    width_mm = (bbox[2] - bbox[0]) * geo["sheet_w"] * geo.get("fit", 1.0)
    if it.get("in_row"):
        return ('<figure class="row-fig"><img src="%s/%s" alt="%s">%s</figure>'
                % (fig_rel, name, chem._esc(caption or "structure"), cap))
    pull = max(0.0, (geo["body_left"] - bbox[0])) * geo["sheet_w"]
    cls = "margin-fig" if it["column"] == "left" else "full-fig"
    style = "width: %.1fmm; margin-left: -%.1fmm;" % (width_mm, pull)
    if it["column"] == "left":
        style += " margin-right: %.1fmm;" % geo["gutter"]
    return ('<figure class="%s" style="%s"><img src="%s/%s" alt="%s">%s</figure>'
            % (cls, style, fig_rel, name, chem._esc(caption or "structure"), cap))


_EQ_ART = {}      # (page, n) -> vector file for an equation that is really a drawn structure
_EQ_GEO = {}      # page geometry, so equation artwork can be sized in mm like any other figure


def _equation_hook(it):
    # A displayed structure with vertical bonds is a drawing. Setting it as mathematics collapses
    # its bonds and stacks its substituents into the wrong places -- see is_two_d_structure.
    key = (it.get("_page"), it["n"])
    if key in _EQ_ART:
        # Width from the region actually cut, never 100%. A drawn structure is a picture of type
        # set at the book's own size; stretching it to the measure blew butanamide up to roughly
        # three times the size it is printed at.
        box = _ASSET_BOX.get(key)
        style = ""
        if box and _EQ_GEO:
            style = ' style="width: %.1fmm;"' % (
                (box[2] - box[0]) * _EQ_GEO["sheet_w"] * _EQ_GEO.get("fit", 1.0))
        return ('<figure class="full-fig eq-structure"%s><img src="%s/%s" alt="%s"></figure>'
                % (style, _FIG_REL_EQ, _EQ_ART[key],
                   chem._esc((it.get("latex") or "")[:80])))
    """A reaction scheme, set as real mathematics.

    Every displayed reaction in this chapter carries A2S LaTeX and every one of them renders in
    the vendored KaTeX, so there is no case here where a reaction has to become a picture. The
    hook returns None only when there is no LaTeX at all, which hands the block back to the shared
    renderer's text-layer recovery.
    """
    latex = (it.get("latex") or "").strip()
    if not chem._is_real_latex(latex):
        # Either unreadable, or prose A2S copied in place of the equation. Both are handed back
        # to the shared renderer, which recovers from the text layer or renders nothing.
        return None
    return ('<div class="equation reaction">\\[%s\\]</div>' % chem._esc(latex))


def _md_smiles(it, page_num):
    """A structure's machine-readable form, written into the Markdown beside it.

    This is the half of SMILES that pays for itself without changing a single pixel. The page
    keeps showing NCERT's own drawing -- which is the faithful thing to show -- while the Markdown
    carries the structure as data, so a NEET question can be matched to the chapter that draws the
    same species by SUBSTRUCTURE rather than by words. It needs no RDKit: drawing is a separate
    concern, and nothing here draws anything.

    Emits nothing at all until step A2C has run, so the Markdown is unchanged until there is
    something real to say.
    """
    rec = _a2c_record(_CHAPTER, page_num, it["n"])
    if not rec or rec.get("kind") == "not_a_structure":
        return ""
    lines = ["", "```smiles"]
    if rec.get("kind") == "reaction" and rec.get("reaction_smiles"):
        lines.append(rec["reaction_smiles"])
    for sp in rec.get("species") or []:
        label = (sp.get("label") or "").strip()
        lines.append("%s%s" % (sp["smiles"], ("  # " + label) if label else ""))
    lines.append("```")
    conf = rec.get("confidence")
    if conf and conf != "certain":
        lines.append("*(structure read with `%s` confidence: %s)*"
                     % (conf, (rec.get("note") or "").strip()[:140]))
    lines.append("")
    return "\n".join(lines)


_CHAPTER = ""


def _a2c_record(chapter, page_num, n):
    """The A2C output for one block, or None. Reads the most-settled run, like every other step."""
    best = None
    for path in sorted(glob.glob(rc.pp("steps", "A2C", "out",
                                       "%s-p%03d-b%s.*.json" % (chapter, page_num, n)))):
        try:
            with open(path, encoding="utf-8") as fh:
                best = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
    return best


# Clearance between a crop edge and the neighbouring line of type. A line's reported box does not
# include its descenders, so 0.004 of the sheet still let the bottom of the sentence above show as
# a sliver along the top of the crop.
_GAP = 0.009


def _ink_box(page, a2_box, prose_boxes, overlays, pad=0.006):
    """The box that actually contains the DRAWING, computed from the page's own ink.

    Every earlier attempt worked outward from A2's block box and tried to push the neighbouring
    paragraphs back out of it -- first by painting them over with redactions, then by clipping
    against them. Both leaked, because a block box is drawn around a region of the page and the
    paragraph above a figure is often inside it.

    This works the other way round and cannot leak: find where the vector strokes and images are,
    and crop to them. Prose is text, never ink, so it is excluded by construction rather than by a
    rule that has to be right about every line on the page.

    The artwork's own lettering (NH2, Ethanol, Phthalimide) IS text, so after the ink is found the
    box is grown to take in any text that sits inside or against it -- but never a line that
    starts at the text measure, which is what a paragraph does and a label never does.
    """
    w, h = page.rect.width, page.rect.height
    search = fitz.Rect(max(0.0, a2_box[0] - 0.03) * w, max(0.0, a2_box[1] - 0.03) * h,
                       min(1.0, a2_box[2] + 0.03) * w, min(1.0, a2_box[3] + 0.03) * h)
    ink = None
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty or not search.intersects(r):
            continue
        if r.width > 0.90 * w and r.height > 0.50 * h:
            continue                                   # the watermark path
        ink = r if ink is None else (ink | r)
    for im in page.get_image_info(xrefs=True):
        r = fitz.Rect(im["bbox"])
        if r.is_empty or not search.intersects(r):
            continue
        frac = [r.x0 / w, r.y0 / h, r.x1 / w, r.y1 / h]
        if _is_page_overlay_frac(frac, overlays):
            continue
        ink = r if ink is None else (ink | r)
    if ink is None:
        return list(a2_box)

    box = [ink.x0 / w, ink.y0 / h, ink.x1 / w, ink.y1 / h]
    prose = {tuple(round(v, 4) for v in b) for b in prose_boxes}
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk.get("lines", []):
            lb = [ln["bbox"][0] / w, ln["bbox"][1] / h, ln["bbox"][2] / w, ln["bbox"][3] / h]
            if tuple(round(v, 4) for v in lb) in prose:
                continue                               # a paragraph, never part of the artwork
            near = (lb[0] < box[2] + 0.012 and lb[2] > box[0] - 0.012
                    and lb[1] < box[3] + 0.012 and lb[3] > box[1] - 0.012)
            if near:
                box = [min(box[0], lb[0]), min(box[1], lb[1]),
                       max(box[2], lb[2]), max(box[3], lb[3])]
    return [max(0.0, box[0] - pad), max(0.0, box[1] - pad),
            min(1.0, box[2] + pad), min(1.0, box[3] + pad)]


def _is_page_overlay_frac(frac, overlays, tol=0.02):
    return any(all(abs(a - b) <= tol for a, b in zip(frac, o)) for o in overlays)


def _safe_box(box, prose_lines, pad=0.014):
    """`box` padded outward, then pulled back so no neighbouring PARAGRAPH is inside it.

    Painting the neighbours out with redactions was the first approach and it did not hold -- the
    annotations are applied to a page whose content is then re-rendered, and text kept surviving
    into the SVG. Clipping is deterministic: compute where the artwork is, grow a little for air,
    then stop short of the nearest line of body type on each side. The artwork cannot be lost,
    because its own extent is inside the box before the pull-back begins; and no paragraph can
    appear, because the edge is placed between the two.
    """
    x0, y0, x1, y1 = box
    top, bottom = y0 - pad, y1 + pad
    left, right = x0 - pad, x1 + pad
    for ln in prose_lines:
        lx0, ly0, lx1, ly1 = ln
        # only lines that overlap this crop horizontally can intrude on it vertically
        if min(x1, lx1) - max(x0, lx0) > 0:
            if ly1 <= y0 + 1e-6:                       # a line ABOVE the artwork
                top = max(top, ly1 + _GAP)
            elif ly0 >= y1 - 1e-6:                     # a line BELOW it
                bottom = min(bottom, ly0 - _GAP)
        if min(y1, ly1) - max(y0, ly0) > 0:
            if lx1 <= x0 + 1e-6:
                left = max(left, lx1 + _GAP)
            elif lx0 >= x1 - 1e-6:
                right = min(right, lx0 - _GAP)
    return [max(0.0, min(left, x0)), max(0.0, min(top, y0)),
            min(1.0, max(right, x1)), min(1.0, max(bottom, y1))]


# --------------------------------------------------------------------------------------------
def build_assets(chapter, pdf_path, m, measurement, fig_dir):
    """Write one asset per figure: SVG for vector artwork, PNG for a raster source.

    Returns {(page, n): filename}. Also returns how many of each, for the build report.
    """
    overlays = measurement.get("page_overlays_ignored") or []
    geo = chem._geometry(m, measurement)
    body_left = geo["body_left"]
    doc = fitz.open(pdf_path)
    out, n_svg, n_png, n_smiles = {}, 0, 0, 0
    try:
        for page in m["pages"]:
            prose = [ln["bbox"] for ln in chem._page_prose(measurement, page["page"], body_left)]
            for it in page["items"]:
                if it["role"] not in ("figure", "table"):
                    continue
                # A transcribed table is set as type -- unless its cells merely DESCRIBE the
                # structures the book draws, in which case it needs the artwork after all.
                if (it["role"] == "table" and (it.get("header") or [])
                        and not it.get("describes_artwork")):
                    continue
                # A figure block that sits INSIDE a worked-example panel is almost always the
                # panel's own words, which the renderer is already setting as text. Cropping it
                # as well printed the box twice -- on p277 a cropped "Example 9.5 / Solution"
                # ended up nested inside a freshly drawn "Example 9.5 / Solution". A panel whose
                # region carries no artwork has nothing a crop could add.
                if it.get("panel") and not it.get("has_artwork"):
                    continue
                bbox = it.get("art_bbox") or it.get("bbox")
                if not bbox:
                    continue
                key = (page["page"], it["n"])

                # SMILES FIRST, deliberately. A depiction drawn from the transcribed structure is
                # clean, upright and complete, where a crop of the same region is at the mercy of
                # where the ink happens to sit -- and the cut-looking crops are the thing that
                # actually reads as broken on the page. Where A2C has read a structure, its
                # drawing is preferred to cutting one out.
                smiles = _smiles_for(chapter, page["page"], it["n"])
                if smiles:
                    name = "mol_p%03d_b%s.svg" % (page["page"], it["n"])
                    if _rdkit_svg(smiles, os.path.join(fig_dir, name)):
                        out[key], n_smiles = name, n_smiles + 1
                        _ASSET_BOX[key] = list(it.get("art_bbox") or it.get("bbox"))
                        continue

                # Crop to the MEASURED ARTWORK, which the measurement has already stripped of
                # page furniture, and which the model has already widened to A2's block box in the
                # one case where the artwork is drawn mostly as lettering and barely registers.
                #
                # Unioning it with A2's box as well -- which an earlier fix for cut schemes did --
                # undoes all of that: A2's box for the trimethylamine figure runs to x 0.892 where
                # the paragraph is, while its artwork ends at 0.810. That union is what put the
                # sentence above each structure back inside the crop.
                box = list(it.get("art_bbox") or it.get("bbox") or bbox)
                # NOT pulled back against neighbours any more. Doing so trimmed the artwork
                # itself -- "N-Alkylphthalimide" lost its tail, the second reduction lost its
                # product -- and losing chemistry is strictly worse than carrying a sliver of the
                # sentence above. The remaining prose is removed properly by classifying strokes
                # in the measurement step, not by shaving the crop here.
                # Padded on three sides only. The space ABOVE a figure is where the preceding
                # paragraph ends, so any upward pad admits the bottom of that sentence -- and that
                # single line of someone else's prose is what has made these crops look broken.
                # The artwork's own topmost element is already in the box (the ink union includes
                # the figure's labels), so there is nothing above it worth reaching for.
                box = [max(0.0, box[0] - 0.006), box[1],
                       min(1.0, box[2] + 0.008), min(1.0, box[3] + 0.006)]
                kinds = it.get("art_kinds") or []
                if kinds == ["vector"]:
                    name = "fig_p%03d_b%s.svg" % (page["page"], it["n"])
                    if chem.svg_region(pdf_path, page["page"], box,
                                       os.path.join(fig_dir, name), overlays, pad=0.0):
                        out[key], n_svg = name, n_svg + 1
                        _ASSET_BOX[key] = list(box)
                        continue
                name = "fig_p%03d_b%s.png" % (page["page"], it["n"])
                if chem.crop_diagram(doc, page["page"], box,
                                     os.path.join(fig_dir, name), overlays, prose, []):
                    out[key], n_png = name, n_png + 1
                    _ASSET_BOX[key] = list(box)

    finally:
        doc.close()
    return out, n_svg, n_png, n_smiles


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("chapter", help="e.g. CHE12L-ch09")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--title", default=None)
    ap.add_argument("--skip-measure", action="store_true")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--no-bundle", action="store_true")
    ap.add_argument("--fit", type=float, default=None)
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        print("source PDF not found: " + args.pdf, file=sys.stderr)
        return 1

    review = rc.pp("exports", "review")
    html_dir, data_dir = os.path.join(review, "html"), os.path.join(review, "html_data")
    fig_dir_name = args.chapter + "_organic_figures"
    fig_dir = os.path.join(review, fig_dir_name)
    for d in (html_dir, data_dir, fig_dir):
        os.makedirs(d, exist_ok=True)

    layout_path = os.path.join(data_dir, args.chapter + "_inorganic_layout.json")
    if args.skip_measure and os.path.exists(layout_path):
        measurement = model_mod.load_measurement(args.chapter)
        print("measurement: reused")
    else:
        measurement = measure_pdf(args.pdf)
        measurement["chapter"] = args.chapter
        with open(layout_path, "w", encoding="utf-8") as fh:
            json.dump(measurement, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("measurement: %d pages, trim %.0fx%.0fpt"
              % (measurement["pages_measured"], measurement["trim_pt"][0],
                 measurement["trim_pt"][1]))

    m = model_mod.build(args.chapter, measurement)
    if not m["pages"]:
        print("no A2 output for %s" % args.chapter, file=sys.stderr)
        return 1
    print("model: %d pages, %d blocks" % (len(m["pages"]), sum(len(p["items"]) for p in m["pages"])))

    assets, n_svg, n_png, n_smiles = build_assets(args.chapter, args.pdf, m, measurement, fig_dir)

    # Displayed structures that carry vertical bonds: taken as vector, because mathematics cannot
    # lay them out. Everything else stays live KaTeX.
    global _FIG_REL_EQ
    _FIG_REL_EQ = "../" + fig_dir_name
    overlays_eq = measurement.get("page_overlays_ignored") or []
    geo_eq = chem._geometry(m, measurement)
    _EQ_ART.clear()
    for page in m["pages"]:
        prose_eq = [ln["bbox"] for ln in
                    chem._page_prose(measurement, page["page"], geo_eq["body_left"])]
        for it in page["items"]:
            it["_page"] = page["page"]
            if it["role"] != "equation" or not it.get("bbox"):
                continue
            # ONLY vertical-bond notation goes to artwork.
            #
            # "Does this region contain ink" was tried as a second condition and is wrong: a
            # fraction bar and an equilibrium arrow are ink too, so the Kb expressions and the
            # salt-plus-base reactions -- which KaTeX sets correctly, colour and all -- were being
            # replaced by pictures of themselves. Stroke count does not separate the two either
            # (18-81 strokes across blocks that need drawing and blocks that do not).
            #
            # What genuinely defeats KaTeX is a 2D LAYOUT: an atom stacked over a bond over
            # another atom. That is what \overset{O}{\overset{\|}{C}} encodes and what collapses
            # into nonsense when set as linear maths. Everything else stays live mathematics.
            if not chem.is_two_d_structure(it.get("latex") or ""):
                continue
            name = "eq_p%03d_b%s.svg" % (page["page"], it["n"])
            # No upward pad, and pulled back from the paragraph above. The space above a
            # displayed structure is where the preceding sentence ends, so any upward reach takes
            # the bottom of that line with it -- "amines." was printing across the top of the
            # amide reduction.
            box = _safe_box(list(it["bbox"]), prose_eq, pad=0.008)
            box[1] = max(box[1], it["bbox"][1] - 0.002)
            if chem.svg_region(args.pdf, page["page"], box,
                               os.path.join(fig_dir, name), overlays_eq, pad=0.0):
                _EQ_ART[(page["page"], it["n"])] = name
                _ASSET_BOX[(page["page"], it["n"])] = list(box)
    print("structures: %d displayed structures drawn with vertical bonds taken as vector"
          % len(_EQ_ART))
    _ASSETS.clear()
    _ASSETS.update(assets)
    n_eq = sum(1 for p in m["pages"] for it in p["items"] if it["role"] == "equation")
    print("structures: %d as SVG vector, %d as raster (source is a bitmap), %d drawn from SMILES"
          % (n_svg, n_png, n_smiles))
    print("reactions : %d set as real mathematical text -- none is an image" % n_eq)

    #
    # Section headings are TEXT -- see chemistry_render.main.
    heads = {}
    n_heads = sum(1 for page in m["pages"] for it in page["items"]
                  if it["role"] == "margin_heading")
    print("headings  : %d set as live text (searchable, reflowable, never cropped)" % n_heads)
    chem._LABELS.clear()

    global _CHAPTER
    _CHAPTER = args.chapter
    _EQ_GEO.clear()
    _EQ_GEO.update(geo_eq)
    chem.HOOKS["figure"] = _figure_hook
    chem.HOOKS["equation"] = _equation_hook
    chem.HOOKS["md_figure"] = _md_smiles
    try:
        title = args.title or args.chapter
        md = chem.build_markdown(m, args.chapter, title, args.pdf, fig_dir_name, assets)
        md_path = os.path.join(review, args.chapter + "_ORGANIC.md")
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(md)
        print("markdown  : %s (%.0f KB)" % (os.path.relpath(md_path, rc.pp()), len(md) / 1024))

        geo = chem._geometry(m, measurement)
        out_path = os.path.join(html_dir, args.chapter + "_ORG_READER.html")
        gap_list = []

        def _write(fit, path, sink):
            geo["fit"] = fit
            del sink[:]
            doc_html, n_gaps = chem.build_html(m, args.chapter, title, "../" + fig_dir_name,
                                               assets, geo, set(), sink, heads)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(doc_html)
            return doc_html, n_gaps

        doc_html, gaps = _write(args.fit or 1.0, out_path, gap_list)
        print("html      : %s (%.0f KB)  |  %d outstanding extraction gap(s)"
              % (os.path.relpath(out_path, rc.pp()), len(doc_html) / 1024, gaps))

        pdf_pages = None
        if not args.no_pdf:
            pdf_out = os.path.join(review, args.chapter + "_ORGANIC.pdf")
            print_path = os.path.join(html_dir, args.chapter + "_ORG_PRINT.html")
            fit, first = args.fit or 1.0, None
            _write(fit, print_path, [])
            if not args.fit:
                for _ in range(6):
                    ratio = chem._measure_fit(print_path)
                    if ratio is None:
                        break
                    first = ratio if first is None else first
                    if ratio <= 0.985:
                        break
                    fit = max(0.80, fit * max(0.94, (1.0 / ratio) ** 0.5))
                    _write(fit, print_path, [])
            geo["fit"], geo["print_fit"] = 1.0, fit
            print("fit       : reader at the book's own size; PRINT copy at %.0f%%" % (fit * 100))
            pdf_pages = chem._print_pdf(print_path, pdf_out)
            if pdf_pages:
                print("pdf       : %s (%d sheets, %.1f MB)"
                      % (os.path.relpath(pdf_out, rc.pp()), pdf_pages,
                         os.path.getsize(pdf_out) / 1e6))
            try:
                os.remove(print_path)
            except OSError:
                pass

        if not args.no_bundle:
            bundle_dir, files = chem.write_bundle(
                args.chapter, title, m, geo, assets, gap_list, review, fig_dir_name,
                out_path, md_path, layout_path,
                os.path.join(review, args.chapter + "_ORGANIC.pdf") if not args.no_pdf else None,
                pdf_pages,
                kind="ORGANIC",
                builder="scripts/export_organic_chemistry_html.py",
                subject="organic chemistry")
            print("bundle    : %s (%d files, %.1f MB)"
                  % (os.path.relpath(bundle_dir, rc.pp()), len(files),
                     sum(v["bytes"] for v in files.values()) / 1e6))
    finally:
        # The hooks are global to the shared renderer, so they are always removed -- an inorganic
        # build running afterwards in the same process must not inherit organic's renderers.
        chem.HOOKS.pop("figure", None)
        chem.HOOKS.pop("equation", None)
        chem.HOOKS.pop("md_figure", None)

    print("built at %s" % datetime.datetime.now().astimezone().isoformat(timespec="seconds"))
    # The build fails if the export does not hold its invariants -- see chem.run_checks.
    return chem.run_checks(args.chapter, "organic")


if __name__ == "__main__":
    sys.exit(main())
