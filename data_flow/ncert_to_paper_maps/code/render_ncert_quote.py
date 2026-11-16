#!/usr/bin/env python3
"""Render the exact NCERT page a D4 quote came from, with the quoted line highlighted.

WHY THE QUOTE DOES NOT MATCH THE PAGE BY SUBSTRING
--------------------------------------------------
`exact_html` lays the page out the way the book prints it: every printed LINE is its own
absolutely-positioned, non-wrapping div (`<div class="blk p ln" style="left:..;top:..">`). A
sentence therefore arrives split across several divs at the exact points the typesetter broke
it -- "In grasses, certain adaxial epidermal cells along the veins modify themselves in" /
"to large, empty, colourless cells." D4 quotes the SENTENCE, so a plain `quote in html` test
fails on almost every real quote. (It also fails on `&amp;`-style escapes and on the `<span
class="math">` wrappers inside a line.)

So the page's line divs are flattened into one string, with a map from each position back to
the div and offset it came from. The quote is found in the flat string; the match is then cut
back into per-div ranges and `<mark>` is inserted at those offsets. The result is the book's
own page, untouched except for the highlight.

Usage:
    python3 code/render_ncert_quote.py --paper 2024_S1 --question q106 --out /tmp/q106.html
    python3 code/render_ncert_quote.py --paper 2024_S1 --all --out-dir maps/quote_pages
"""

import argparse
import collections
import glob
import html as htmllib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINE_DIV = re.compile(r'(<div class="[^"]*\bln\b[^"]*"[^>]*>)(.*?)(</div>)', re.S)
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def _plain(fragment):
    """The visible text of one line div, tags removed and entities resolved."""
    return htmllib.unescape(TAG.sub("", fragment))


def flatten(page_html):
    """[(span_start, span_end, inner_html)] for each line div, plus the flat visible text
    and a map from flat position -> (div index, offset into that div's PLAIN text)."""
    divs, flat, index = [], [], []
    for m in LINE_DIV.finditer(page_html):
        i = len(divs)
        divs.append(m)
        text = _plain(m.group(2))
        for off, chx in enumerate(text):
            if WS.match(chx):
                if flat and flat[-1] != " ":
                    flat.append(" ")
                    index.append((i, off))
                continue
            flat.append(chx)
            index.append((i, off))
        # a line break behaves as a space between lines
        if flat and flat[-1] != " ":
            flat.append(" ")
            index.append((i, len(text)))
    return divs, "".join(flat), index


def locate(flat, index, quote):
    """(start, end) positions in the flat text, or None. Tries progressively looser forms."""
    want = WS.sub(" ", htmllib.unescape(quote)).strip()
    for probe in (want, want.rstrip("."), WS.sub(" ", TAG.sub("", want))):
        if not probe:
            continue
        at = flat.find(probe)
        if at == -1:
            at = flat.lower().find(probe.lower())
        if at != -1:
            return at, at + len(probe)
    return None


def highlight(page_html, quotes):
    """The page with every locatable quote wrapped in <mark>. Returns (html, hits, misses)."""
    divs, flat, index = flatten(page_html)
    if not divs:
        return page_html, 0, len(quotes)

    # Collect per-div character ranges to wrap, then apply them right-to-left so earlier
    # offsets stay valid.
    marks = collections.defaultdict(list)
    hits = misses = 0
    for q in quotes:
        found = locate(flat, index, q)
        if not found:
            misses += 1
            continue
        hits += 1
        a, b = found
        per = collections.defaultdict(lambda: [10 ** 9, -1])
        for pos in range(a, min(b, len(index))):
            d, off = index[pos]
            per[d][0] = min(per[d][0], off)
            per[d][1] = max(per[d][1], off + 1)
        for d, (lo, hi) in per.items():
            marks[d].append((lo, hi))

    out, last = [], 0
    for i, m in enumerate(divs):
        out.append(page_html[last:m.start()])
        inner = m.group(2)
        if i in marks:
            # Work on the PLAIN text of the div: a line's inner html may hold <span
            # class="math"> wrappers, and splicing by plain-text offset would cut them in half.
            # Lines carrying markup are wrapped whole instead of partially.
            if TAG.search(inner):
                inner = '<mark class="ncq">%s</mark>' % inner
            else:
                plain = htmllib.unescape(inner)
                for lo, hi in sorted(marks[i], reverse=True):
                    lo, hi = max(0, lo), min(len(plain), hi)
                    plain = (plain[:lo] + '<mark class="ncq">'
                             + htmllib.escape(plain[lo:hi]) + "</mark>" + plain[hi:])
                inner = plain
        out.append(m.group(1) + inner + m.group(3))
        last = m.end()
    out.append(page_html[last:])
    return "".join(out), hits, misses



#: `exact_css` names its fonts by content hash -- `src:url(__FONT:f34157fdecb5d6b2__)`. The
#: bytes were never stored: a table-wide scan for `FONT#` rows returns ZERO, and no .otf/.ttf
#: exists anywhere under the NCERT source either. An @font-face whose src cannot resolve makes
#: the browser retry and fall back anyway, so the rule is dropped and the fallback stack in the
#: same declaration does the work. The page keeps its real geometry -- every line is absolutely
#: positioned by the rest of the CSS -- but the glyphs are a substitute, and the caption says so
#: rather than letting the page claim to be pixel-exact.
FONT_FACE = re.compile(r"@font-face\s*\{[^}]*__FONT:[0-9a-f]+__[^}]*\}", re.S)


def usable_css(css):
    """(css with unresolvable @font-face rules removed, how many were removed)."""
    kept, n = FONT_FACE.subn("", css or "")
    return kept, n


CSS = """
mark.ncq{background:#fff3a3;color:inherit;padding:0;box-shadow:0 0 0 1px #e8cf4d}
body{margin:0;background:#8d8d8d;font-family:Georgia,'Times New Roman',serif}
.wrap{max-width:100%;overflow-x:auto;padding:18px}
.cap{font:13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:#fff;margin:0 0 10px}
.cap b{color:#fff3a3}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--question")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--out-dir")
    ap.add_argument("--pages", default=os.path.join(HERE, "maps", "page_html.json"))
    a = ap.parse_args()

    if not os.path.exists(a.pages):
        sys.exit("no page cache at %s -- run scripts/cache_page_html.py first" % a.pages)
    pages = json.load(open(a.pages, encoding="utf-8"))
    passages = json.load(open(os.path.join(HERE, "maps", "passage_pages.json"), encoding="utf-8"))

    targets = ([a.question] if a.question else
               sorted(os.path.basename(p).split(".")[1]
                      for p in glob.glob(os.path.join(HERE, "steps", "D4", "out",
                                                      "%s.*.runA.json" % a.paper))))
    report = collections.Counter()
    for qid in targets:
        d4_path = os.path.join(HERE, "steps", "D4", "out", "%s.%s.runA.json" % (a.paper, qid))
        if not os.path.exists(d4_path):
            report["no D4 output"] += 1
            continue
        d4 = json.load(open(d4_path, encoding="utf-8"))
        by_page = collections.defaultdict(list)
        for e in (d4.get("evidence") or []):
            pid, line = e.get("passage_id"), e.get("exact_line")
            if not (pid and line):
                continue
            info = passages.get(pid)
            if not info:
                report["passage not in the page map"] += 1
                continue
            for pg in info["pages"]:
                by_page[(info["chapter_id"], pg)].append(line)
        if not by_page:
            report["no locatable evidence"] += 1
            continue

        blocks, hits, misses = [], 0, 0
        for (ch, pg), quotes in sorted(by_page.items()):
            raw = (pages.get(ch) or {}).get(pg)
            if not raw:
                report["page html not cached"] += 1
                continue
            marked, h, m = highlight(raw, quotes)
            hits += h
            misses += m
            blocks.append('<p class="cap">%s &middot; printed page <b>%s</b> &middot; '
                          '%d line(s) highlighted</p>%s'
                          % (htmllib.escape(ch), htmllib.escape(pg), h, marked))
        if not blocks:
            continue
        css, dropped = usable_css((pages.get("_css") or {}).get(ch, ""))
        if dropped:
            report["@font-face rules dropped (bytes never stored)"] += dropped
            blocks.append('<p class="cap">Geometry is the book\'s own; %d embedded font(s) '
                          'could not be resolved, so the glyphs are a fallback.</p>' % dropped)
        doc = ("<!doctype html><meta charset=utf-8><title>%s %s &mdash; NCERT</title>"
               "<style>%s</style><style>%s</style><div class=wrap>%s</div>"
               % (a.paper, qid, css, CSS, "".join(blocks)))
        out = a.out or os.path.join(a.out_dir or ".", "%s.%s.html" % (a.paper, qid))
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        open(out, "w", encoding="utf-8").write(doc)
        report["rendered"] += 1
        report["quotes highlighted"] += hits
        report["quotes not located"] += misses
        if a.question:
            print("wrote %s  (%d highlighted, %d not located)" % (out, hits, misses))
    for k, v in sorted(report.items()):
        print("   %-32s %4d" % (k, v))


if __name__ == "__main__":
    main()
