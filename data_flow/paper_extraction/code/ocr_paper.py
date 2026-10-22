#!/usr/bin/env python3
"""Give a scanned paper a text layer, so the rest of the pipeline can read it.

    python3 scripts/ocr_paper.py --paper 2022
    python3 scripts/ocr_paper.py --all

Two of the printed volumes are pure scans: `2022.pdf` carries 18 text characters across 26 pages
and `2021.pdf` 18 across 27. Nothing that reads a text layer can see anything in them -- the
question matcher finds 2 of 18 figure-needing questions for 2022 against 36 of 40 for 2024, and the
extraction check cannot run at all. OCR is the whole difference.

The result is written to `papers/ocr_cache/`, NOT back into `inputs/`. CLAUDE.md forbids editing
`inputs/` and the rule is right: the scan as received is the evidence, and an OCR pass is an
interpretation of it. The cache is keyed by file name and is safe to delete -- it rebuilds.

What OCR can and cannot be trusted for, measured on these files: running text comes out well enough
to MATCH a question by its words, which is all the matcher needs. Match-list options do not --
"A-iv B-ii C-iii D-i" comes back as "Adi Biv Ci Deii". So an OCR'd page is used to FIND a question
and to crop its picture, never to correct the question's text. The crop is pixels from the original
scan either way, so a figure cut from an OCR'd page is exactly as good as one cut from a born-digital
page; only the finding step depends on the OCR.
"""

import argparse
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

CACHE = ("papers", "ocr_cache")
#: Below this many characters per page a PDF is a scan rather than a text document. The real files
#: sit at either extreme -- 0.7 chars per page for the scans, 2,600 and up for the rest -- so the
#: threshold is not delicate.
TEXT_CHARS_PER_PAGE = 50


def needs_ocr(path):
    import fitz
    doc = fitz.open(path)
    chars = sum(len(p.get_text() or "") for p in doc)
    return chars < TEXT_CHARS_PER_PAGE * max(1, doc.page_count), chars, doc.page_count


def ocr_path(path):
    """Where the OCR'd copy of this paper lives (whether or not it exists yet)."""
    return rc.pp(*CACHE, os.path.basename(path))


def ensure_ocr(path, dpi=300, force=False, quiet=False):
    """Return a path with a readable text layer: the OCR'd copy for a scan, else the original.

    Rendered at 300 dpi because the scans are grey and 200 dpi lost the subscripts in chemical
    formulae; tesseract is given the page as an image and asked for a one-page searchable PDF,
    which keeps the original pixels underneath so later crops are unaffected by the OCR.
    """
    import fitz
    scan, chars, pages = needs_ocr(path)
    if not scan:
        return path
    out = ocr_path(path)
    if os.path.exists(out) and not force:
        return out
    os.makedirs(os.path.dirname(out), exist_ok=True)

    src = fitz.open(path)
    merged = fitz.open()
    tmp_dir = rc.pp(*CACHE, "_tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    for i, page in enumerate(src):
        png = os.path.join(tmp_dir, f"p{i:04d}.png")
        page.get_pixmap(dpi=dpi).save(png)
        stem = os.path.join(tmp_dir, f"p{i:04d}")
        r = subprocess.run(["tesseract", png, stem, "pdf"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"tesseract failed on page {i + 1}: {r.stderr[:200]}")
        with fitz.open(stem + ".pdf") as one:
            merged.insert_pdf(one)
        for f in (png, stem + ".pdf"):
            if os.path.exists(f):
                os.remove(f)
        if not quiet and (i + 1) % 5 == 0:
            print(f"      {i + 1}/{pages} pages", flush=True)
    merged.save(out)
    merged.close()
    if os.path.isdir(tmp_dir) and not os.listdir(tmp_dir):
        os.rmdir(tmp_dir)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", help="file name or a substring of it, e.g. 2022")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dpi", type=int, default=300)
    args = ap.parse_args()
    if not (args.paper or args.all):
        ap.error("pass --paper or --all")

    papers = sorted(glob.glob(rc.pp("inputs", "papers", "*.pdf")))
    if args.paper:
        papers = [p for p in papers if args.paper in os.path.basename(p)]
    if not papers:
        print("no matching paper")
        return 1

    for path in papers:
        scan, chars, pages = needs_ocr(path)
        name = os.path.basename(path)
        if not scan:
            if args.paper:
                print(f"{name}: already has a text layer ({chars} chars over {pages} pages)")
            continue
        print(f"{name}: a scan ({chars} chars over {pages} pages) -- running OCR at {args.dpi} dpi")
        out = ensure_ocr(path, dpi=args.dpi, force=args.force)
        import fitz
        got = sum(len(p.get_text() or "") for p in fitz.open(out))
        print(f"   wrote {os.path.relpath(out, rc.pp())} -- {got} characters "
              f"({got // max(1, pages)} per page)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
