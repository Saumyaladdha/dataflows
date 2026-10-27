#!/usr/bin/env python3
"""Lift every cut figure out of the booklet PDF as VECTOR SVG -- the printed drawing, exactly.

    python3 code/vector_figures.py --paper-id 2017_A --dry-run
    python3 code/vector_figures.py --paper-id 2017_A --apply

WHY THE FIGURE IS LIFTED, NOT REDRAWN
-------------------------------------
These booklets are vector PDFs: a structure's rings, a circuit's wires and an arrow's head are paths
in the file, and its labels are text in the publisher's own font. So the drawing a reader should see
already exists, exactly, and the only question is how to get it out without the page around it.

    1. copy the page into a scratch document;
    2. strip every RASTER image from it -- the watermark and the page background are images, the
       drawing is not, so this removes the pink "Vedantu" wash and nothing of the figure;
    3. delete the text and line art lying wholly outside the figure's box, so the file holds the
       figure and not a clipped copy of the whole page (400 KB per figure before, a few KB after);
    4. crop to the box and write SVG with text as glyph outlines, so every label keeps the printed
       typeface instead of falling back to a system font.

Redrawing from SMILES or a netlist is a different job with a different purpose -- machine-readable
chemistry and circuits, checked by code -- and it cannot be byte-identical to an Aakash or Vedantu
drawing, whose bond lengths, fonts and label spacing are their own. This step is the exact copy.

WHAT IT READS: the PAGE boxes cut_agent_figures.py records beside every figure it cuts --
`agent_figure_boxes`, `agent_option_boxes` and `solution_figures[].bbox` -- so the vector copy is
exactly the region of the PNG beside it. WHAT IT WRITES: `<image>.svg` next to each `<image>.png`,
and `question["vector"] = {png path: svg path}`. A page that is a sliced scan has no vector art, so
its figures keep the PNG and are reported, never silently.
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

CORPUS = rc.corpus()
#: A stroked path that goes nowhere: `M x y` followed by a zero move (`V0`, `H0`, `L x y` to itself
#: is not emitted by PyMuPDF in practice; these two forms are what the booklets carry).
ZERO_LENGTH = re.compile(r'<path [^>]*\sd="M0 0[VH]0"\s*/>')
#: A line that opens with the publisher's answer or solution marker...
MARKER_LINE = re.compile(r"^\s*(Answer|Ans\b|Sol\b|Solution)", re.I)
#: ...and the spans of it that ARE the marker: the word, the `(2)` / `(1 & 2)*` after it, a colon.
MARKER_WORD = re.compile(r"^\s*(Answer(\s*Key)?|Ans\.?|Sol\.?|Solution|:|\.|"
                         r"\(\s*[1-4a-dA-D](\s*(&|,|and)\s*[1-4a-dA-D])*\s*\)\*?)\s*$", re.I)


def regions(question):
    """[(png path, page index, box in pixels)] for every figure this question has cut."""
    out = []
    for image, box in zip(question.get("agent_figure_images") or [],
                          question.get("agent_figure_boxes") or []):
        out.append((image, box["page"], box["bbox"]))
    option_boxes = question.get("agent_option_boxes") or {}
    for key, image in sorted((question.get("agent_option_images") or {}).items()):
        if key in option_boxes:
            out.append((image, option_boxes[key]["page"], option_boxes[key]["bbox"]))
    for figure in question.get("solution_figures") or []:
        out.append((figure["image"], figure["page"], figure["bbox"]))
    for figure in question.get("figures") or []:
        if figure.get("image"):
            out.append((figure["image"], figure["page"], figure["crop_bbox"]))
    return out


_ROOT_SIZE = re.compile(r'(<svg\b[^>]*?\swidth=")([\d.]+)("[^>]*?\sheight=")([\d.]+)(")')


def _scale_root(svg, factor):
    """Multiply the root <svg> element's width and height by `factor`, leaving its viewBox alone."""
    return _ROOT_SIZE.sub(lambda m: "%s%.2f%s%.2f%s" % (m.group(1), float(m.group(2)) * factor,
                                                        m.group(3), float(m.group(4)) * factor,
                                                        m.group(5)), svg, count=1)


def figure_svg(pymupdf, source, page_index, box_px, dpi):
    """The vector drawing inside `box_px` on one page, as SVG text, rasters and surroundings removed."""
    box = pymupdf.Rect([v * 72.0 / dpi for v in box_px])
    scratch = pymupdf.open()
    scratch.insert_pdf(source, from_page=page_index, to_page=page_index)
    page = scratch[0]
    box &= page.rect
    # 1. every raster image goes: the watermark and the page background are images, the figure is not
    page.add_redact_annot(page.rect)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                          text=pymupdf.PDF_REDACT_TEXT_NONE)
    # 2. the publisher's own markers go: `Answer (2)` above a solution figure and the `Sol.` beside
    #    it are never part of a drawing, but a box generous enough to keep a figure's labels reaches
    #    them -- 2017_A q17 kept "...swer (2)", q36 kept the "l." of "Sol.", and the lone full stops
    #    left behind read as stray dots. Removed only on a line that STARTS with the marker, so an
    #    option label "(2)" inside a figure, on its own line, is never touched.
    markers = 0
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = "".join(s.get("text", "") for s in spans)
            if not MARKER_LINE.match(text):
                continue
            for span in spans:
                if MARKER_WORD.match(span.get("text", "")):
                    page.add_redact_annot(pymupdf.Rect(span["bbox"]))
                    markers += 1
    if markers:
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                              text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    # 3. everything wholly outside the box goes, so the SVG holds the figure, not the whole page
    width, height = page.rect.width, page.rect.height
    for outside in (pymupdf.Rect(0, 0, width, box.y0), pymupdf.Rect(0, box.y1, width, height),
                    pymupdf.Rect(0, box.y0, box.x0, box.y1), pymupdf.Rect(box.x1, box.y0, width, box.y1)):
        if outside.is_empty or outside.width < 0.5 or outside.height < 0.5:
            continue
        page.add_redact_annot(outside)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                          text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    # 4. crop to the figure and write it, text as the printed glyph outlines
    page.set_cropbox(box)
    svg = page.get_svg_image(text_as_path=True)
    scratch.close()
    # A ZERO-LENGTH STROKE is a dot. The booklet carries degenerate paths (`d="M0 0V0"`, round
    # caps) that print as nothing in the PDF but that a browser draws as a visible dot -- one sat in
    # the corner of 2017_A q17's and q36's solution figures. They draw nothing, so they go.
    svg = ZERO_LENGTH.sub("", svg)
    # DISPLAY SIZE = THE CROP'S. PyMuPDF sizes the SVG in POINTS, so on a page it showed at about a
    # third of the PNG crop beside it (cut at `dpi`): q36's free-body diagrams came out thumbnail
    # small. The viewBox -- the geometry -- is untouched; only the declared size scales by dpi/72.
    return _scale_root(svg, dpi / 72.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    import pymupdf
    import extract_paper_v2 as extractor
    paper_path = rc.pp(*CORPUS, "papers", "%s.json" % args.paper_id)
    with open(paper_path, encoding="utf-8") as fh:
        paper = json.load(fh)
    source_path = os.path.join(os.path.dirname(extractor.SOURCE_ROOT), paper["meta"]["source_pdf"])
    source = pymupdf.open(source_path)
    dpi = paper["meta"]["dpi"]

    counts, sizes = collections.Counter(), []
    for question in paper["questions"]:
        vector = {}
        for image, page_index, box in regions(question):
            if not question.get("text_layer_reliable", True):
                counts["scan_page_kept_png"] += 1     # a sliced scan has no vector art to lift
                continue
            svg_rel = image[:-4] + ".svg" if image.endswith(".png") else image + ".svg"
            if args.apply:
                svg = figure_svg(pymupdf, source, page_index, box, dpi)
                path = rc.pp(*CORPUS, svg_rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(svg)
                sizes.append(len(svg))
            vector[image] = svg_rel
            counts["svg"] += 1
        question["vector"] = vector
    source.close()

    print("%s: %d figure(s) lifted as vector SVG" % (args.paper_id, counts["svg"]))
    if sizes:
        sizes.sort()
        print("   svg size: median %d bytes, largest %d bytes" % (sizes[len(sizes) // 2], sizes[-1]))
    if counts["scan_page_kept_png"]:
        print("   on a sliced-scan page, PNG kept: %d" % counts["scan_page_kept_png"])
    if args.dry_run:
        print("(dry run -- nothing written)")
        return 0
    with open(paper_path, "w", encoding="utf-8") as fh:
        json.dump(paper, fh, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
