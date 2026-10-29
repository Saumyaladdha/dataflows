#!/usr/bin/env python3
"""Draw a labelled grid on a page image, and say which cells each node claims.

    python code/grid_overlay.py BIO12L-ch01 --page 001
    python code/grid_overlay.py BIO12L-ch01 --all

Writes, per page, into `steps/A2R/grid/`:

    <item>-p<NNN>.grid.png     the ORIGINAL page with an A..T / 1..26 grid drawn over it
    <item>-p<NNN>.claims.json  what our data says occupies each cell

WHY A GRID
----------
Every review of this pipeline so far has compared two pictures by eye, and eye comparison is
why the same defects survived round after round: "the figure looks too big" is an impression,
and an impression cannot be checked, filed, or regression-tested. "Figure 1.9 occupies C4-G11
on the page but our box claims C4-G19" is a fact, and the next build either reproduces it or
does not.

The grid also makes ABSENCE visible, which is the failure mode eye comparison is worst at. A
reviewer reading our render has nothing to tell them that cell K6 of the original holds a
photograph we never extracted -- there is simply nothing there to notice. Listing the claims
cell by cell turns that into an empty row in a table.

WHAT THE AGENT IS ASKED
-----------------------
For each occupied cell: what does the ORIGINAL print here, and does the claim match? Three
answers are useful and all are checkable -- `match`, `wrong` (something is claimed here that
the page does not print), `missing` (the page prints something no node claims).
"""

import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from PIL import Image, ImageDraw, ImageFont         # noqa: E402

COLS, ROWS = 16, 22                                  # A..P across, 1..22 down
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cells_for(bbox):
    """`C4:G11` -- the grid range a fractional bbox covers."""
    x0, y0, x1, y1 = bbox
    c0, c1 = int(x0 * COLS), min(COLS - 1, int(x1 * COLS - 1e-9))
    r0, r1 = int(y0 * ROWS) + 1, min(ROWS, int(y1 * ROWS - 1e-9) + 1)
    c0, c1 = max(0, min(c0, COLS - 1)), max(0, min(c1, COLS - 1))
    a, b = f"{LETTERS[c0]}{r0}", f"{LETTERS[c1]}{r1}"
    return a if a == b else f"{a}:{b}"


def draw_grid(src, dst):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im, "RGBA")
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
    except Exception:                                          # noqa: BLE001
        font = ImageFont.load_default()
    for c in range(COLS + 1):
        x = W * c / COLS
        d.line([(x, 0), (x, H)], fill=(255, 0, 0, 90), width=2)
    for r in range(ROWS + 1):
        y = H * r / ROWS
        d.line([(0, y), (W, y)], fill=(255, 0, 0, 90), width=2)
    for c in range(COLS):
        x = W * (c + 0.5) / COLS
        for yy in (6, H - 34):
            d.rectangle([x - 16, yy - 2, x + 16, yy + 30], fill=(255, 255, 255, 215))
            d.text((x - 10, yy), LETTERS[c], fill=(200, 0, 0), font=font)
    for r in range(ROWS):
        y = H * (r + 0.5) / ROWS
        for xx in (6, W - 46):
            d.rectangle([xx - 2, y - 16, xx + 42, y + 16], fill=(255, 255, 255, 215))
            d.text((xx, y - 13), str(r + 1), fill=(200, 0, 0), font=font)
    im.save(dst)
    return im.size


def walk(ns):
    for n in ns:
        yield n
        if n.get("children"):
            yield from walk(n["children"])


def claims_for(doc, page_file):
    out = []
    for n in walk(doc["tree"]):
        for b in (n.get("boxes") or []):
            bb = b.get("bbox")
            pf = b.get("page_file") or n.get("page_file")
            if not bb or pf != page_file:
                continue
            body = (n.get("body") or n.get("title") or n.get("caption") or "").strip()
            out.append({
                "cells": cells_for(bb),
                "kind": n["kind"],
                "id": n.get("id"),
                "geometry": b.get("src"),
                "text": (body[:90] + "…") if len(body) > 90 else body,
                "image": os.path.basename(n.get("image_local") or "") or None,
            })
    page = next((p for p in doc.get("pages") or []
                 if p.get("page_file") == page_file), {})
    for a in (page.get("art") or []):
        if a.get("bbox"):
            out.append({"cells": cells_for(a["bbox"]), "kind": "page art",
                        "id": None, "geometry": "crop",
                        "text": "", "image": os.path.basename(a.get("file") or "")})
    for f in (page.get("furniture") or []):
        if f.get("bbox"):
            out.append({"cells": cells_for(f["bbox"]), "kind": f"furniture:{f.get('kind')}",
                        "id": None, "geometry": "a2l-agent",
                        "text": (f.get("text") or ""), "image": None})
    out.sort(key=lambda c: (c["cells"]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("item")
    ap.add_argument("--page")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()

    jpaths = glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                    "chapter.json"))
    doc = None
    for p in jpaths:
        with open(p, encoding="utf-8") as fh:
            d = json.load(fh)
        if f"{d['book_id']}-ch{d['chapter']['number']:02d}" == a.item:
            doc = d
            break
    if not doc:
        raise SystemExit(f"no built chapter for {a.item}")

    out_dir = os.path.join(ROOT, "steps", "A2R", "grid")
    os.makedirs(out_dir, exist_ok=True)
    pages = [p["page_file"] for p in doc["pages"]]
    if a.page:
        pages = [p for p in pages if p == a.page]

    for pf in pages:
        src = os.path.join(ROOT, "steps", "A2", "work", f"{a.item}-p{pf}.png")
        if not os.path.exists(src):
            print(f"{a.item} p{pf}: no page image at {os.path.relpath(src, ROOT)}")
            continue
        png = os.path.join(out_dir, f"{a.item}-p{pf}.grid.png")
        draw_grid(src, png)
        claims = claims_for(doc, pf)
        with open(os.path.join(out_dir, f"{a.item}-p{pf}.claims.json"), "w",
                  encoding="utf-8") as fh:
            json.dump({"item_id": a.item, "page_file": pf,
                       "grid": {"cols": COLS, "rows": ROWS,
                                "columns": list(LETTERS[:COLS]),
                                "note": "A1 is top-left; letters run across, numbers down"},
                       "claims": claims}, fh, indent=1, ensure_ascii=False)
        print(f"{a.item} p{pf}: {len(claims)} claims -> "
              f"{os.path.relpath(png, ROOT)}")


if __name__ == "__main__":
    main()
