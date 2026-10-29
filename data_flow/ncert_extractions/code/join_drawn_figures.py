#!/usr/bin/env python3
"""Draw the chapter's FIGP specs and hang them on its figure nodes.

    python code/join_drawn_figures.py PHY11L-ch01

WHY A CHAPTER DRAWS ITS OWN FIGURES
-----------------------------------
`cut_figures.py` crops the book's artwork off the page, and for a born-digital book (Biology)
that crop IS the drawing: it is sharp, it has no page wash, and nothing is lost. The Physics
books are not born-digital. Every page is a 2480x3508 raster with a text layer laid over it, so
a crop of a figure is a crop of a scan -- soft at any size, carrying the page's grey and the
standing `(c) NCERT / not to be republished` watermark across it.

So for those we draw the figure ourselves: `figp-figure-redrawer` reads the printed figure and
writes a SPEC of primitives, `render_figure.render` draws the spec as SVG, and this script puts
the result on the node as `image_drawn`. The redraw is vector, carries its labels as real text,
and has no wash.

WHAT THIS DOES NOT DO
---------------------
It does not replace the crop or the CDN url. `chapter.json` keeps `image` (the CDN url, for
reference) and `image_local` (the crop) exactly as they were; `image_drawn` is added beside
them. `render_exact.fig_src` is the only place that prefers one over another, and a figure with
no spec -- a photograph, a pictorial apparatus, anything the redrawer marked `out_of_scope` --
simply has no `image_drawn` and goes on rendering from the CDN url or the crop.

A spec that fails to render is REPORTED, never swallowed: a figure silently falling back to a
blurred crop is the failure this step exists to prevent.
"""

import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import cdn_publish                 # noqa: E402
import render_figure               # noqa: E402


def _walk(nodes):
    for n in nodes:
        yield n
        for c in n.get("children") or []:
            yield from _walk([c])


def specs_for(cid):
    """[(figure_id, spec_dict)] for every FIGP output this chapter has, in id order."""
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "steps", "FIGP", "out",
                                              f"{cid}-fig*.runA.json"))):
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        fid = os.path.basename(path).split(".")[0]
        if doc.get("error"):
            print(f"  SKIP  {fid}: the redrawer reported {doc['error']!r}")
            continue
        if doc.get("out_of_scope"):
            why = "; ".join(doc.get("unreadable") or []) or "pictorial"
            print(f"  SKIP  {fid}: out of scope ({why}) -- keeps the crop / CDN image")
            continue
        if not (doc.get("spec") or {}).get("draw"):
            print(f"  SKIP  {fid}: no draw items")
            continue
        out.append((fid, doc["spec"]))
    return out


def join(cid):
    cdir = cdn_publish.chapter_dir(cid)
    cpath = os.path.join(cdir, "chapter.json")
    with open(cpath, encoding="utf-8") as fh:
        doc = json.load(fh)

    figs = [n for n in _walk(doc["tree"]) if n.get("kind") == "figure"]
    pairs = specs_for(cid)
    if not pairs:
        print(f"  no FIGP specs for {cid}; every figure keeps its crop / CDN image")
        return 0

    fig_dir = os.path.join(cdir, "figures")
    os.makedirs(fig_dir, exist_ok=True)
    drawn = 0
    for fid, spec in pairs:
        # `PHY11L-ch01-fig01` -> the chapter's 1st figure node, in printed order.
        try:
            idx = int(fid.rsplit("fig", 1)[1].split(".")[0].lstrip("0") or "1") - 1
        except (IndexError, ValueError):
            print(f"  SKIP  {fid}: cannot read a figure number out of the id")
            continue
        if idx >= len(figs):
            print(f"  SKIP  {fid}: the chapter has only {len(figs)} figure node(s)")
            continue
        try:
            svg = render_figure.render(spec)
        except Exception as exc:                      # reported, never swallowed
            print(f"  FAIL  {fid}: {type(exc).__name__}: {exc}")
            continue
        name = f"{fid}.svg"
        with open(os.path.join(fig_dir, name), "w", encoding="utf-8") as fh:
            fh.write(svg)
        node = figs[idx]
        node["image_drawn"] = f"figures/{name}"
        node["image_drawn_spec"] = f"steps/FIGP/out/{fid}.runA.json"
        drawn += 1
        print(f"  drew  {fid} -> figures/{name}  ({len(svg)} bytes, "
              f"{len(spec['draw'])} items) onto {node.get('caption', '')[:44]!r}")

    with open(cpath, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"  {drawn} of {len(figs)} figure(s) now carry a redraw; "
          f"the rest keep the CDN image or the crop")
    return drawn


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("chapter_id")
    a = ap.parse_args()
    join(a.chapter_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
