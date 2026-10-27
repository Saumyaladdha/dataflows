#!/usr/bin/env python3
"""Put the exact render beside the book, page by page -- the check every chapter needs.

    python code/compare_render.py BIO12L-ch01
    python code/compare_render.py BIO12L-ch01 --pages 3,5,7 --dpi 60

The owner reviews chapter-exact.html against the PDF by eye, and every defect fixed so far was
one a build reported as clean. This makes that review a pipeline step instead of a hand-run
script: it prints the render with a headless browser (each `.sheet` is one PDF page), sets every
sheet beside its book page, and reports per page

  * `collide` -- pairs of printed lines that overlap (text on text);
  * `diff`    -- how different the two pages look (0 = identical, mean absolute grey
                 difference after a light blur, so a font substitute's width does not count
                 but a missing panel, band, figure or paragraph does).

Images go to `qa/compare/<chapter id>/` (never into the chapter's deliverable folder):
`pNN.png` per page and `contact.png` for the whole chapter. Pages are listed worst first.
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def browser():
    for b in _BROWSERS:
        if os.path.exists(b):
            return b
    for name in ("msedge", "chrome", "google-chrome", "chromium"):
        p = shutil.which(name)
        if p:
            return p
    raise SystemExit("no Edge/Chrome found for headless printing")


def print_html(html_path, pdf_out):
    """chapter-exact.html -> PDF, one page per `.sheet` (fonts and CDN images loaded)."""
    url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    subprocess.run([browser(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=30000", f"--print-to-pdf={pdf_out}", url],
                   capture_output=True, timeout=300)
    if not os.path.exists(pdf_out):
        raise SystemExit(f"headless print produced nothing for {html_path}")


def _gray(pix):
    import numpy as np
    import fitz
    if pix.n != 1:
        pix = fitz.Pixmap(fitz.csGRAY, pix)
    return np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width).astype(float)


def page_diff(a_pix, b_pix):
    """Mean absolute grey difference (0-255) of two page images, lightly blurred."""
    import numpy as np
    from scipy import ndimage
    a, b = _gray(a_pix), _gray(b_pix)
    h, w = min(a.shape[0], b.shape[0]), min(a.shape[1], b.shape[1])
    a = ndimage.uniform_filter(a[:h, :w], 5)
    b = ndimage.uniform_filter(b[:h, :w], 5)
    return float(np.abs(a - b).mean())


def collisions(page):
    lines = [l["bbox"] for blk in page.get_text("dict")["blocks"] for l in blk.get("lines", [])
             if "".join(s["text"] for s in l["spans"]).strip()]
    n = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            a, b = lines[i], lines[j]
            if (min(a[2], b[2]) - max(a[0], b[0]) > 20
                    and min(a[3], b[3]) - max(a[1], b[1]) > 3):
                n += 1
    return n


def side_by_side(a_pix, b_pix, out_path):
    import fitz
    a = fitz.Pixmap(fitz.csRGB, a_pix) if a_pix.n != 3 else a_pix
    b = fitz.Pixmap(fitz.csRGB, b_pix) if b_pix.n != 3 else b_pix
    img = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, a.width + b.width + 8,
                                              max(a.height, b.height)), False)
    img.clear_with(70)
    a.set_origin(0, 0)
    img.copy(a, a.irect)
    b.set_origin(a.width + 8, 0)
    img.copy(b, b.irect)
    img.save(out_path)


def compare(cid, pages=None, dpi=60, out_dir=None):
    """[(page_no, diff, collide)] for the chapter, worst first; writes the images."""
    import fitz
    import cdn_publish
    cdir = cdn_publish.chapter_dir(cid)
    with open(os.path.join(cdir, "chapter.json"), encoding="utf-8") as fh:
        doc = json.load(fh)
    src = doc.get("source_pdf") or ""
    pdf = src if os.path.isabs(src) else os.path.join(ROOT, src)
    out_dir = out_dir or os.path.join(ROOT, "qa", "compare", cid)
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(tempfile.mkdtemp(prefix="cmp_"), "render.pdf")
    print_html(os.path.join(cdir, "chapter-exact.html"), tmp)
    book, render = fitz.open(pdf), fitz.open(tmp)
    rows = []
    n = min(len(book), len(render))
    for i in range(n):
        if pages and (i + 1) not in pages:
            continue
        a = book[i].get_pixmap(dpi=dpi)
        b = render[i].get_pixmap(dpi=dpi)
        side_by_side(a, b, os.path.join(out_dir, f"p{i + 1:02d}.png"))
        rows.append((i + 1, round(page_diff(a, b), 1), collisions(render[i])))
    # A contact sheet of every pair, small, for a one-look review.
    thumbs = sorted(glob.glob(os.path.join(out_dir, "p[0-9][0-9].png")))
    if thumbs:
        from PIL import Image
        ims = [Image.open(t) for t in thumbs]
        for im in ims:
            im.thumbnail((520, 360))
        cols = 3
        W = max(im.width for im in ims)
        H = max(im.height for im in ims)
        sheet = Image.new("RGB", (cols * W, ((len(ims) + cols - 1) // cols) * H), (70, 70, 70))
        for k, im in enumerate(ims):
            sheet.paste(im, ((k % cols) * W, (k // cols) * H))
        sheet.save(os.path.join(out_dir, "contact.png"))
    if len(book) != len(render):
        print(f"  compare   WARNING book has {len(book)} pages, render {len(render)} sheets")
    return sorted(rows, key=lambda r: (-r[1], -r[2])), out_dir


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter_id")
    ap.add_argument("--pages", help="comma-separated page numbers, e.g. 3,5,7")
    ap.add_argument("--dpi", type=int, default=60)
    a = ap.parse_args()
    pages = {int(x) for x in a.pages.split(",")} if a.pages else None
    rows, out_dir = compare(a.chapter_id, pages, a.dpi)
    print(f"compare -> {os.path.relpath(out_dir, ROOT)}  (worst first)")
    for p, d, c in rows:
        flag = "  <-- look" if d > 12 or c > 6 else ""
        print(f"  p{p:02d}  diff {d:5.1f}  collide {c:3d}{flag}")


if __name__ == "__main__":
    main()
