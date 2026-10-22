#!/usr/bin/env python3
"""Measure where a book actually sets its body text, and report it against the design.

    python code/measure_text_block.py BIO11L
    python code/measure_text_block.py --all

WHY THIS EXISTS
---------------
"The content does not fit the page" was diagnosed for a long time as a type-size problem and
answered by shrinking -- a `--fit` factor, then a floor on it, then clipping below the floor.
It was never a type-size problem.

`fit_factor` computes a page's content height from the BOOK'S OWN measured line counts and line
pitch. So when it reports that a page needs 142% of the available height, it is not saying the
type is too big. It is saying the height we are giving the text is smaller than the height the
book gives it. Measured on Class 11 Biology ch01: the design declared a 610pt text block; NCERT
sets 643pt on a median page and 662pt on the fullest. We were short by up to four lines a page,
on every page, and then shrinking the type to hide it.

The lesson generalises: when a derived number looks wrong, check the inputs it was derived
from before adjusting the output. `LESSONS.md` 0.3.
"""

import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as dl                                    # noqa: E402
import pymupdf                                              # noqa: E402

# Furniture sits OUTSIDE the text block, so counting it makes the block look taller than it is.
FURNITURE = re.compile(
    r"^(?:\d{1,3}|\d{4}-\d{2}|Reprint\s+\d{4}-\d{2}"
    r"|BIOLOGY|Biology|PHYSICS|Physics|CHEMISTRY|Chemistry"
    r"|[A-Z][A-Z \-']{6,})$")


def measure(pdf_path):
    """(median_top, median_bottom, deepest_top, deepest_bottom) in points, body text only."""
    doc = pymupdf.open(pdf_path)
    tops, bots = [], []
    for page in doc:
        ys = []
        for blk in page.get_text("dict")["blocks"]:
            for line in blk.get("lines", []):
                for sp in line.get("spans", []):
                    t = (sp.get("text") or "").strip()
                    if len(t) > 3 and sp["size"] > 7 and not FURNITURE.match(t):
                        ys.append((sp["bbox"][1], sp["bbox"][3]))
        if len(ys) > 8:
            tops.append(min(y[0] for y in ys))
            bots.append(max(y[1] for y in ys))
    doc.close()
    if not tops:
        return None
    tops.sort(); bots.sort()
    return (tops[len(tops) // 2], bots[len(bots) // 2], min(tops), max(bots))


def report(book_id, pdf_path):
    m = measure(pdf_path)
    if not m:
        return f"{book_id:<8} no body text (scan -- A2L must measure this book)"
    mt, mb, dt, db = m
    d = dl.design_for(book_id)
    have = d.text_foot_pt - d.text_top_pt
    want = mb - mt
    lines = (want - have) / (d.body_pt * d.leading)
    verdict = ("ok" if abs(lines) < 0.75 else
               f"SHORT BY {lines:.1f} LINES -- pages will appear to overflow")
    return (f"{book_id:<8} design {d.text_top_pt:5.0f}->{d.text_foot_pt:5.0f} ({have:4.0f}pt)  "
            f"book {mt:5.0f}->{mb:5.0f} ({want:4.0f}pt)  deepest {db - dt:4.0f}pt   {verdict}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("books", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    pdfs = sorted(glob.glob(os.path.join(ROOT, "source_pdfs", "**", "*.pdf"), recursive=True))
    seen = set()
    for p in pdfs:
        rel = os.path.relpath(p, ROOT)
        ed = "O" if "/old/" in rel else "L"
        subj = next((s for s in ("biology", "chemistry", "physics") if f"/{s}/" in rel), None)
        kl = "11" if "class_11" in rel else "12" if "class_12" in rel else None
        if not (subj and kl):
            continue
        bid = f"{ {'biology':'BIO','chemistry':'CHE','physics':'PHY'}[subj] }{kl}{ed}"
        if bid in seen or (a.books and bid not in a.books):
            continue
        seen.add(bid)
        print(report(bid, p))


if __name__ == "__main__":
    main()
