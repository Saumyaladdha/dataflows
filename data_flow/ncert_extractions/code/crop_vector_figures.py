#!/usr/bin/env python3
"""Crop figures that have a measured box but no image file.

    python code/crop_vector_figures.py BIO11L-ch01
    python code/crop_vector_figures.py --all

WHY A FIGURE CAN HAVE NO FILE
-----------------------------
`cut_figures.py` crops from EMBEDDED IMAGE BLOCKS. That covers every photograph and every
scanned plate, and it covers nothing else -- because a diagram drawn as vector paths is not an
image block. NCERT draws its flowcharts, its labelled cross-sections and most of its process
diagrams that way, so those figures reached `chapter.json` with a caption, a number and no
artwork at all. Figure 1.1 of Class 11 Chapter 1 -- the taxonomic hierarchy, the single most
cited diagram in the chapter -- is one of them.

The box is known: either the text layer measured it, or `a2l-layout-reader` did by reading the
page image (on Class 11 p008 it reported the figure sitting in the left rail on a pale-yellow
panel, `#fffac1`, with its caption as a separate box beneath). So the page region is rendered
straight out of the PDF at that box. Vector art rasterises cleanly, which is why this works at
all -- it is the same operation `cut_figures` performs, pointed at a box that came from a
measurement rather than from an image block.

ONLY A MEASURED BOX IS CROPPED. An `estimated` box is a reading-order guess; cropping it would
produce a confident picture of the wrong part of the page, which is worse than no picture.
"""

import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import pymupdf                                              # noqa: E402

DPI = 200
PAD_PT = 2.0
MIN_PT = 24.0          # smaller than this is a caption line, not a diagram


def a2l_figure_boxes(book_chapter):
    """{page_file: [bbox, ...]} -- the figure boxes a2l-layout-reader MEASURED.

    The tree's figure node frequently carries the CAPTION's box rather than the artwork's:
    the caption is text, so the text layer finds it, while a vector diagram leaves no block
    at all. On Class 11 p008 that gave the figure node a box 1.2% of the page tall -- a
    caption line -- while the actual taxonomic-hierarchy flowchart sits above it at
    [0.128, 0.19, 0.362, 0.496] on a pale-yellow panel, which A2L measured by reading the
    page image. That measurement is the only record of where the diagram is.
    """
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "steps", "A2L", "out",
                                           f"{book_chapter}-p*.json"))):
        pf = os.path.basename(f).split("-p")[-1].split(".")[0]
        try:
            with open(f, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:                                    # noqa: BLE001
            continue
        for el in data.get("elements") or []:
            if el.get("role") in ("figure", "table") and el.get("bbox"):
                bb = el["bbox"]
                if len(bb) == 4 and (bb[2] - bb[0]) > 0.04 and (bb[3] - bb[1]) > 0.04:
                    out.setdefault(pf, []).append((el["role"], bb, el.get("fill")))
    return out


def crop_chapter(cdir, doc):
    src = os.path.join(ROOT, doc.get("source_pdf") or "")
    if not os.path.exists(src):
        return 0, "no source pdf"
    pages = {p.get("page_file"): i for i, p in enumerate(doc.get("pages") or [])}
    a2l_boxes = a2l_figure_boxes(
        f"{doc['book_id']}-ch{doc['chapter']['number']:02d}")
    pdf = pymupdf.open(src)
    figs_dir = os.path.join(cdir, "figures")
    os.makedirs(figs_dir, exist_ok=True)
    made = 0

    def walk(ns):
        for n in ns:
            yield n
            if n.get("children"):
                yield from walk(n["children"])

    for n in walk(doc["tree"]):
        if n.get("kind") not in ("figure", "table"):
            continue
        if n.get("image") or n.get("image_local"):
            continue
        box = next((b for b in (n.get("boxes") or [])
                    if b.get("bbox") and b.get("src") in ("measured", "a2l-agent")), None)
        if not box:
            continue
        # The box's own page file, or the page whose printed folio this node sits on.
        # A figure node built from a caption often carries neither directly -- the caption
        # was stitched in from a page that prints no folio -- so both routes are tried
        # before giving up, rather than silently skipping the figure.
        pf = box.get("page_file") or n.get("page_file")
        if pf not in pages:
            folio = (n.get("pages") or [None])[0]
            pf = next((q.get("page_file") for q in (doc.get("pages") or [])
                       if q.get("printed") == folio), None)
        if pf not in pages:
            continue
        # PREFER A2L'S MEASURED ARTWORK BOX over the node's own, which is routinely the
        # caption's. Matched by page and kind, nearest in y to the node's box so a page with
        # two figures still pairs them correctly.
        cands = [c for c in a2l_boxes.get(pf, []) if c[0] == n["kind"]]
        if cands:
            ny = box["bbox"][1]
            role, bb_a2l, fill_a2l = min(
                cands, key=lambda c: abs(c[1][1] - ny))
            if (bb_a2l[3] - bb_a2l[1]) > (box["bbox"][3] - box["bbox"][1]):
                box = {**box, "bbox": bb_a2l, "src": "a2l-agent"}
                if fill_a2l:
                    n.setdefault("layout_fill", fill_a2l)
                # WRITE THE ARTWORK BOX BACK ONTO THE NODE.
                # Cropping the right region and leaving the node pointing at the caption's
                # box meant the renderer placed the full taxonomic-hierarchy flowchart into
                # a 1.2%-tall caption slot -- `object-fit:contain` then shrank it to a
                # yellow sliver. The crop and the node must agree on where the figure is.
                n["boxes"] = [{**box, "page_file": pf}] + [
                    b for b in (n.get("boxes") or [])[1:]]
                n["figure_box_source"] = "a2l-agent"
        page = pdf[pages[pf]]
        w, h = page.rect.width, page.rect.height
        x0, y0, x1, y1 = box["bbox"]
        rect = pymupdf.Rect(max(0, x0 * w - PAD_PT), max(0, y0 * h - PAD_PT),
                            min(w, x1 * w + PAD_PT), min(h, y1 * h + PAD_PT))
        # A box the height of one line is a CAPTION that was typed as a figure, not artwork.
        # Cropping it yields a 7mm sliver -- which is exactly what an earlier build shipped.
        if rect.width < MIN_PT or rect.height < MIN_PT:
            continue
        name = f"{pf}_vec{made + 1:02d}.png"
        page.get_pixmap(dpi=DPI, clip=rect).save(os.path.join(figs_dir, name))
        n["image_local"] = f"figures/{name}"
        n["image_source"] = "vector_crop"
        made += 1
    # A FIGURE A2L MEASURED BUT THE TREE NEVER HELD.
    #
    # The Ernst Mayr portrait is the case this exists for. The only crop containing it was a
    # scan of the WHOLE page -- portrait, caption and every word of the biography -- which is
    # correctly dropped, because drawing it would print the biography twice: once as live
    # text and once as pixels underneath. That left the page with no portrait at all and no
    # node to attach one to, because a photograph on a page whose text layer describes only
    # the prose produces no figure block.
    #
    # A2L read the page image and measured the portrait at [0.127, 0.383, 0.394, 0.636] with
    # its caption as a separate box. That measurement is the only record that the photograph
    # exists, so a node is created from it rather than the artwork being lost.
    existing = {(b.get("page_file"), round(b["bbox"][1], 2))
                for n in walk(doc["tree"]) if n.get("kind") in ("figure", "table")
                for b in (n.get("boxes") or []) if b.get("bbox")}
    pdf2 = pymupdf.open(src)
    for pf, cands in a2l_boxes.items():
        if pf not in pages:
            continue
        for role, bb, fill in cands:
            if (pf, round(bb[1], 2)) in existing:
                continue
            page = pdf2[pages[pf]]
            w, h = page.rect.width, page.rect.height
            rect = pymupdf.Rect(max(0, bb[0] * w - PAD_PT), max(0, bb[1] * h - PAD_PT),
                                min(w, bb[2] * w + PAD_PT), min(h, bb[3] * h + PAD_PT))
            if rect.width < MIN_PT or rect.height < MIN_PT:
                continue
            made += 1
            name = f"{pf}_a2l{made:02d}.png"
            page.get_pixmap(dpi=DPI, clip=rect).save(os.path.join(figs_dir, name))
            node = {"kind": role, "image_local": f"figures/{name}",
                    "image_source": "a2l_measured", "caption": "",
                    "page_file": pf, "belongs": "chapter",
                    "boxes": [{"page": None, "page_file": pf, "src": "a2l-agent",
                               "bbox": [round(v, 4) for v in bb]}],
                    "pages": []}
            if fill:
                node["layout_fill"] = fill
            doc["tree"].append(node)
    pdf2.close()

    pdf.close()
    return made, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                           "chapter.json"))):
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
        cid = f"{doc['book_id']}-ch{doc['chapter']['number']:02d}"
        if a.chapters and cid not in a.chapters:
            continue
        made, err = crop_chapter(os.path.dirname(p), doc)
        if err:
            print(f"{cid}: {err}")
            continue
        if made:
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(doc, fh, indent=1, ensure_ascii=False)
        print(f"{cid}: {made} vector figure(s) cropped")


if __name__ == "__main__":
    main()
