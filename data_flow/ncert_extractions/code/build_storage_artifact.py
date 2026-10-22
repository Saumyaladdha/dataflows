#!/usr/bin/env python3
"""Builds a shareable page explaining how one NCERT chapter's printed pages are saved in DynamoDB.

    python3 scripts/build_storage_artifact.py BIO11L-ch01 --pages 003 004 007

Writes `ncert_book_mapping/ncert_dynamodb_storage.html`, self-contained: the page scans are
embedded as JPEG data URIs and every row shown is generated from `ncert/layout/<CHAPTER>.json`,
so the document cannot drift from the data it documents.

The page scans carry the saved `bbox` drawn on top of them as overlay rectangles. That is the
whole point of the document -- a reader can see that the stored position IS the printed position,
rather than taking a table of numbers on trust.
"""

import argparse
import base64
import html
import io
import json
import os
import re
import sys

import pymupdf

SUBJECT = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}
EDITION = {"L": "latest", "O": "older"}
ROLE_ORDER = ["chapter_title", "section_heading", "paragraph", "list", "side_note",
              "figure_caption", "running_header", "reprint_line", "image"]


def esc(s):
    return html.escape(s or "", quote=False)


def page_jpeg(pdf_path, page_index, dpi=105, quality=74):
    doc = pymupdf.open(pdf_path)
    pix = doc[page_index].get_pixmap(dpi=dpi)
    png = pix.tobytes("png")
    doc.close()
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(png)).convert("RGB")
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=quality, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode(), pix.width, pix.height
    except ImportError:
        return "data:image/png;base64," + base64.b64encode(png).decode(), pix.width, pix.height


def item_for(el, n, meta, page, printed):
    """The DynamoDB item this element is saved as. Mirrors docs/NCERT_STORAGE_DESIGN.md 2.2."""
    book = meta["book_id"]
    it = {
        "PK": "BOOK#%s#CH#%02d" % (book, meta["chapter_num"]),
        "SK": "PG#%s#BL#%03d" % (page["page_file"], n),
        "kind": el["role"],
        "column": el["column"],
        "bbox": ["%.4f" % v for v in el["bbox"]],
        "size_rel": "%.2f" % el["size_rel"],
    }
    if el["runs"]:
        it["color"] = el["runs"][0]["color"]
    if el["role"] == "section_heading":
        m = re.match(r"^((?:\d+\.)*\d+)\s+(.*)$", el["text"])
        if m:
            it["number"], it["title"] = m.group(1), m.group(2)
            it["level"] = m.group(1).count(".") + 2
    it["text"] = el["text"]
    runs = []
    for r in el["runs"]:
        if not r["t"]:
            continue
        o = {"t": r["t"]}
        for k in ("b", "i", "sc"):
            if r.get(k):
                o[k] = True
        if r.get("script"):
            o[r["script"]] = True
        runs.append(o)
    it["runs"] = runs
    it.update({"book_id": book, "subject": SUBJECT[book[:3]], "class": int(book[3:5]),
               "edition": EDITION[book[5]], "chapter_num": meta["chapter_num"],
               "page_file": page["page_file"]})
    if printed:
        it["page_printed"] = printed
    return it


def printed_number(page):
    """The printed page number, READ off the running header rather than computed from an offset.
    NCERT prints `4 Biology` on a verso and `The Living World 5` on a recto."""
    for el in page["elements_in_reading_order"]:
        if el["role"] == "running_header":
            m = re.match(r"^(\d+)\b", el["text"]) or re.search(r"\b(\d+)$", el["text"].strip())
            if m:
                return int(m.group(1))
    return None


def shorten(obj, limit=300):
    """Trim long run/text values for display without pretending they are short."""
    o = json.loads(json.dumps(obj))
    if isinstance(o.get("text"), str) and len(o["text"]) > limit:
        o["text"] = o["text"][:limit] + " …"
    for r in o.get("runs", []):
        if len(r["t"]) > limit:
            r["t"] = r["t"][:limit] + " …"
    return o


def json_html(obj):
    """Pretty JSON with the keys that matter picked out, as spans."""
    raw = json.dumps(obj, ensure_ascii=False, indent=2)
    out = []
    for line in raw.split("\n"):
        m = re.match(r'^(\s*)"([^"]+)":\s*(.*)$', line)
        if m:
            pad, key, rest = m.groups()
            cls = "k-key"
            if key in ("PK", "SK"):
                cls = "k-key is-key"
            elif key in ("bbox", "column", "size_rel", "color"):
                cls = "k-key is-pos"
            elif key == "runs":
                cls = "k-key is-run"
            out.append('%s<span class="%s">"%s"</span>: %s' % (pad, cls, esc(key), esc(rest)))
        else:
            out.append(esc(line))
    return "\n".join(out)


def runs_preview(el):
    """What the stored runs render as, using real markup."""
    bits = []
    for r in el["runs"]:
        if not r["t"]:
            continue
        t = esc(r["t"])
        if r.get("sc"):
            t = '<span class="sc">%s</span>' % t
        if r.get("b"):
            t = "<strong>%s</strong>" % t
        if r.get("i"):
            t = "<em>%s</em>" % t
        if r.get("script") == "sup":
            t = "<sup>%s</sup>" % t
        if r.get("script") == "sub":
            t = "<sub>%s</sub>" % t
        bits.append(t)
    return "".join(bits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--pages", nargs="+", required=True)
    ap.add_argument("--out", default="ncert_book_mapping/ncert_dynamodb_storage.html")
    a = ap.parse_args()

    data = json.load(open(os.path.join("ncert", "layout", a.chapter + ".json"), encoding="utf-8"))
    by_page = {p["page_file"]: p for p in data["pages"]}
    book = data["book_id"]

    spreads = []
    for pf in a.pages:
        page = by_page[pf]
        uri, w, h = page_jpeg(data["source_pdf"], int(pf) - 1)
        printed = printed_number(page)
        els = [e for e in page["elements_in_reading_order"] if e["role"] != "image"]
        items = [item_for(e, i + 1, data, page, printed) for i, e in enumerate(els)]
        spreads.append({"page": page, "uri": uri, "w": w, "h": h,
                        "printed": printed, "els": els, "items": items})

    chapter_title = next((e["text"] for p in data["pages"]
                          for e in p["elements_in_reading_order"]
                          if e["role"] == "chapter_title" and e["text"] != "Unit 1"), a.chapter)

    palette = {}
    for p in data["pages"]:
        for e in p["elements_in_reading_order"]:
            if e["runs"] and e["role"] not in ("image",):
                palette.setdefault(e["role"], e["runs"][0]["color"])

    html_out = render(a.chapter, book, data, spreads, chapter_title, palette)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(html_out)
    print("%s  %.1f MB  (%d pages, %d rows shown)"
          % (a.out, os.path.getsize(a.out) / 1e6, len(spreads),
             sum(len(s["items"]) for s in spreads)))


def render(chapter, book, data, spreads, chapter_title, palette):
    # imported lazily so the template lives next to the data it formats
    from storage_artifact_template import build
    return build(chapter, book, data, spreads, chapter_title, palette,
                 json_html=json_html, runs_preview=runs_preview, shorten=shorten,
                 esc=esc, ROLE_ORDER=ROLE_ORDER)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
