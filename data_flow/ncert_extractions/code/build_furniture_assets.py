#!/usr/bin/env python3
"""Cut each BOOK's reusable page furniture ONCE, into assets/furniture/<DESIGN_KEY>/.

    python code/build_furniture_assets.py BIO11
    python code/build_furniture_assets.py --all

WHY THIS IS PER BOOK AND NOT PER PAGE
--------------------------------------
NCERT prints the same header strip, the same folio tab and the same footer bar on every body
page of a book. Cutting them per page therefore re-does one crop dozens of times, and the
copies are NOT identical -- measured on the two Evolution chapters:

    BIO12L ch06   17 header crops ->  2 distinct images   (15 of them redundant)
    BIO12O ch07   25 header crops ->  3 distinct images,
                                      and 8 of the 25 were only 295 BYTES -- near-empty

So a third of that chapter's pages carried a broken header and the rest carried a good one,
which is exactly the page-to-page inconsistency the owner reported. The furniture is a property
of the BOOK, so it is cut once from the page that shows it best and every page then points at
the same file. One image cannot disagree with itself.

WHAT IS AND IS NOT SHARED
--------------------------
Shared (cut once per book, mirrored per side):
    header strip / band art, the leaf motif, the folio tab art, the footer bar
Not shared (cut per chapter, because they are genuinely different each time):
    the chapter-opener artwork -- its QR code and its illustration are unique to the chapter

The "best" crop is chosen by FILE SIZE, which is a proxy for how much ink the crop actually
caught. That is what rejects the 295-byte near-empty crops: a crop that caught the artwork is
always larger than one that caught the paper beside it.
"""

import argparse
import collections
import hashlib
import os
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib  # noqa: E402
import extract_page_layout as extract_mod  # noqa: E402

DPI = 200
EDITION_WORD = {"L": "new", "O": "old"}
SUBJECT_WORD = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}


def asset_dir(design_key):
    return os.path.join(ROOT, "assets", "furniture", design_key)


def _chapters_for(book_id):
    subject, klass, edition = design_lib.parse_book_id(book_id)
    base = os.path.join(ROOT, "source_pdfs", EDITION_WORD[edition],
                        f"class_{klass}", SUBJECT_WORD[subject])
    if not os.path.isdir(base):
        return []
    import re
    nums = set()
    for f in sorted(os.listdir(base)):
        if not f.lower().endswith(".pdf"):
            continue
        m = re.search(r"(?:^|[_ ])(\d{1,2})[. _]", f) or re.search(r"Chapter_(\d+)", f)
        if m:
            nums.add(int(m.group(1)))
    return sorted(nums)


def build(design_key, books, max_chapters=3, dpi=DPI):
    """Cut the shared furniture for one design from the first few chapters of its books."""
    out_dir = asset_dir(design_key)
    os.makedirs(out_dir, exist_ok=True)
    # candidates[(kind, side)] = list of (nbytes, pngbytes)
    candidates = collections.defaultdict(list)

    for book_id in books:
        for num in _chapters_for(book_id)[:max_chapters]:
            try:
                layout = extract_mod.extract(book_id, num)
            except SystemExit:
                continue
            doc = pymupdf.open(layout["source_pdf"])
            for pi, page in enumerate(layout["pages"]):
                # The OPENER is skipped: its artwork is chapter-specific, not book furniture.
                if pi == 0:
                    continue
                side = page.get("page_side") or "recto"
                p = doc[pi]
                pw, ph = p.rect.width, p.rect.height
                for el in page["elements_in_reading_order"]:
                    if el["role"] != "page_furniture":
                        continue
                    kind = el.get("furniture")
                    if kind != "header art":
                        continue
                    x0, y0, x1, y1 = el["bbox_pt"]
                    rect = pymupdf.Rect(max(0, x0), max(0, y0), min(pw, x1), min(ph, y1))
                    if rect.width < 8 or rect.height < 8:
                        continue
                    png = p.get_pixmap(dpi=dpi, clip=rect).tobytes("png")
                    candidates[("header", side)].append((len(png), png, (x0, y0, x1, y1),
                                                         (pw, ph)))
            doc.close()

    written = {}
    for (kind, side), cands in candidates.items():
        if not cands:
            continue
        # Largest = most ink caught. This is what rejects the near-empty crops.
        nbytes, png, bbox, pagesz = max(cands, key=lambda c: c[0])
        name = f"{kind}_{side}.png"
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(png)
        distinct = len({hashlib.md5(c[1]).hexdigest() for c in cands})
        written[name] = {"bytes": nbytes, "from_candidates": len(cands),
                         "distinct_candidates": distinct,
                         "bbox_pt": [round(v, 1) for v in bbox],
                         "page_pt": [round(v, 1) for v in pagesz]}
    return out_dir, written


DESIGN_BOOKS = {
    "BIO11": ["BIO11L", "BIO11O"],
    "BIO12": ["BIO12L", "BIO12O"],
    "CHE11": ["CHE11L", "CHE11O"],
    "CHE12": ["CHE12L", "CHE12O"],
    "PHY11": ["PHY11L", "PHY11O"],
    "PHY12": ["PHY12L", "PHY12O"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("design", nargs="*", help="e.g. BIO11 BIO12")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dpi", type=int, default=DPI)
    a = ap.parse_args()
    keys = list(DESIGN_BOOKS) if a.all else (a.design or ["BIO11", "BIO12"])
    for key in keys:
        books = DESIGN_BOOKS.get(key)
        if not books:
            print(f"!! unknown design {key}")
            continue
        out, written = build(key, books, dpi=a.dpi)
        if not written:
            print(f"{key}: no shared header art found (this book may draw it in vector)")
            continue
        print(f"{key} -> {os.path.relpath(out, ROOT)}")
        for name, info in sorted(written.items()):
            print(f"   {name:22s} {info['bytes']:7d}B  "
                  f"chosen from {info['from_candidates']} crops "
                  f"({info['distinct_candidates']} distinct)")


if __name__ == "__main__":
    main()
