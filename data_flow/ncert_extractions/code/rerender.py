#!/usr/bin/env python3
"""Re-write chapter.md and both HTML files FROM the existing chapter.json.

    python code/rerender.py BIO11L-ch01
    python code/rerender.py --all

WHY THIS IS NOT `run_chapter.py`
--------------------------------
`run_chapter.py` rebuilds the tree from the PDF and the agent outputs, which is right after an
extraction changes -- and wrong after a CDN upload. `upload_assets.py` writes the live URLs
onto the nodes of chapter.json; a rebuild regenerates those nodes and every URL is lost. The
two must therefore run in this order:

    run_chapter.py  (build)  ->  upload_assets.py  (urls)  ->  rerender.py  (outputs)

and never `run_chapter.py` again until the next extraction. This script only reads
chapter.json and rewrites the files derived from it, so the URLs survive.
"""

import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build_chapter_json as bcj          # noqa: E402
import render_exact                       # noqa: E402


def rerender(path):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    cdir = os.path.dirname(path)
    with open(os.path.join(cdir, "chapter.md"), "w", encoding="utf-8") as fh:
        fh.write(bcj.to_markdown(doc))
    # chapter.html is not a deliverable (2026-10-24); only the exact render is written.
    render_exact.write(doc, cdir)
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                           "chapter.json"))):
        with open(p, encoding="utf-8") as fh:
            d = json.load(fh)
        cid = f"{d['book_id']}-ch{d['chapter']['number']:02d}"
        if a.chapters and cid not in a.chapters:
            continue
        doc = rerender(p)

        def walk(ns):
            for n in ns:
                yield n
                if n.get("children"):
                    yield from walk(n["children"])
        figs = [n for n in walk(doc["tree"]) if n["kind"] in ("figure", "table")]
        cdn = [n for n in figs if (n.get("image") or "").startswith("http")]
        print(f"{cid}: chapter.md + chapter-exact.html rewritten "
              f"({len(cdn)}/{len(figs)} figures on CDN)")


if __name__ == "__main__":
    main()
