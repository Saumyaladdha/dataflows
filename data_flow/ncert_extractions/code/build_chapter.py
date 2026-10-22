#!/usr/bin/env python3
"""Build ONE chapter's complete folder: layout, figures, HTML, Markdown and DynamoDB items.

    python code/build_chapter.py BIO11L-ch03
    python code/build_chapter.py --book BIO12O --all
    python code/build_chapter.py --book BIO11L --all --book BIO11O --all

Writes everything under, and only under:

    data/<old|new>_ncert/class_<11|12>/<subject>/ch<NN>_<slug>/
        chapter.html        the book page by page, at the real trim, furniture drawn
        chapter.md          the same text as Markdown, for reading and diffing
        layout.json         every element with its position, role and formatting
        figures/            one PNG per real figure, named by printed folio
        README.md           what this chapter is and where each file came from

and one item file per page under `data/dynamodb/`.

THE FOLDER PATH IS THE FILE'S IDENTITY. `data/new_ncert/class_11/biology/ch03_plant-kingdom/`
tells you the edition, the class, the subject and the chapter without opening anything. That is
the point: the previous layout spread the same chapter across `ncert/layout/BIO11L-ch03.json`,
`exports/review/html_data/BIO11L-ch03_layout.json`, `exports/chapters/BIO11L-ch03/` and
`ncert/figures/`, and the only thing that said which edition `L` meant was a line in a spec.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib  # noqa: E402
import cut_figures  # noqa: E402
import extract_page_layout as extract_mod  # noqa: E402
import render_chapter_html as render_mod  # noqa: E402

PY = sys.executable
EDITION_WORD = {"L": "new", "O": "old"}
SUBJECT_WORD = {"BIO": "biology", "CHE": "chemistry", "PHY": "physics"}


def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", (s or "").strip().lower()).strip("-")
    return s or "chapter"


def chapter_dir(book_id, chapter_num, title):
    subject, klass, edition = design_lib.parse_book_id(book_id)
    return os.path.join(
        ROOT, "data", f"{EDITION_WORD[edition]}_ncert", f"class_{klass}",
        SUBJECT_WORD[subject], f"ch{chapter_num:02d}_{slugify(title)}")


def chapter_title_from(layout):
    for e in layout["pages"][0]["elements_in_reading_order"]:
        if e["role"] == "chapter_title":
            t = e["text"].strip()
            if re.fullmatch(r"(?i)chapter\s*\d+", t):
                continue
            t = re.sub(r"(?i)^chapter\s*\d+\s*", "", t).strip()
            if t:
                return t
    # Fall back to the running head, which prints the chapter title on every recto.
    for p in layout["pages"][1:]:
        for e in p["elements_in_reading_order"]:
            if e["role"] == "running_header" and e.get("text"):
                t = e["text"].strip()
                if t.lower() not in ("biology", "chemistry", "physics"):
                    return t
    return ""


def to_markdown(layout, title):
    out = [f"# {title or layout['book_id']} (chapter {layout['chapter_num']})", ""]
    out.append(f"*Source:* `{layout['source_pdf']}`  ")
    out.append(f"*Sheet:* {layout['sheet_pt'][0]:.0f} x {layout['sheet_pt'][1]:.0f} pt  ")
    out.append("")
    for p in layout["pages"]:
        folio = p.get("printed_page_number")
        out.append(f"---\n\n## Page {folio if folio is not None else '?'} "
                   f"({p.get('page_side', '?')})\n")
        for e in p["elements_in_reading_order"]:
            role, text = e["role"], (e.get("text") or "").strip()
            if role in ("page_furniture", "page_number", "running_header", "reprint_line"):
                continue
            if role == "figure":
                f = e.get("figure_file")
                if f:
                    out.append(f"![figure](figures/{f})\n")
                continue
            if not text:
                continue
            if role == "chapter_title":
                out.append(f"### {text}\n")
            elif role == "section_heading":
                out.append(f"#### {text}\n")
            elif role == "contents_entry":
                out.append(f"- {text}")
            elif role == "figure_caption":
                out.append(f"*{text}*\n")
            elif role == "side_note":
                out.append(f"> {text}\n")
            else:
                out.append(f"{text}\n")
        out.append("")
    return "\n".join(out)


def to_dynamodb_items(layout, title, chap_rel):
    """One item per printed page, shaped for a single-table DynamoDB write.

    PK is the BOOK, SK is the printed FOLIO -- not the PDF page index. The folio is what the
    book prints, what an evidence citation quotes, and the only page identifier that is stable
    when a chapter PDF is re-scanned with a different number of leading pages.
    """
    book_id = layout["book_id"]
    subject, klass, edition = design_lib.parse_book_id(book_id)
    items = []
    for i, p in enumerate(layout["pages"]):
        folio = p.get("printed_page_number")
        sk = f"PAGE#{folio:04d}" if isinstance(folio, int) else f"INDEX#{i + 1:04d}"
        blocks = [{
            "role": e["role"],
            "text": e.get("text", ""),
            "bbox": e.get("bbox_sheet") or e["bbox"],
            "size_rel": e.get("size_rel"),
            "column": e.get("column"),
            **({"figure_file": e["figure_file"]} if e.get("figure_file") else {}),
            **({"runs": e["runs"]} if e.get("runs") else {}),
        } for e in p["elements_in_reading_order"] if e["role"] != "page_furniture"]
        items.append({
            "PK": f"BOOK#{book_id}",
            "SK": f"CH#{layout['chapter_num']:02d}#{sk}",
            "book_id": book_id,
            "subject": subject, "class": klass,
            "edition": {"L": "new", "O": "old"}[edition],
            "chapter_num": layout["chapter_num"],
            "chapter_title": title,
            "printed_page_number": folio,
            "page_side": p.get("page_side"),
            "imprint": p.get("imprint"),
            "sheet_pt": p.get("sheet_pt"),
            "source_pdf": layout["source_pdf"],
            "chapter_folder": chap_rel,
            "blocks": blocks,
        })
    return items


def build(book_id, chapter_num, allow_unmeasured=False):
    chapter = f"{book_id}-ch{chapter_num:02d}"
    layout = extract_mod.extract(book_id, chapter_num)
    title = chapter_title_from(layout)
    cdir = chapter_dir(book_id, chapter_num, title)
    os.makedirs(cdir, exist_ok=True)

    layout_path = os.path.join(cdir, "layout.json")
    with open(layout_path, "w", encoding="utf-8") as fh:
        json.dump(layout, fh, indent=1, ensure_ascii=False)

    n_figs = len(cut_figures.cut(layout["source_pdf"], layout, os.path.join(cdir, "figures")))
    with open(layout_path, "w", encoding="utf-8") as fh:
        json.dump(layout, fh, indent=1, ensure_ascii=False)

    with open(os.path.join(cdir, "chapter.html"), "w", encoding="utf-8") as fh:
        fh.write(render_mod.render(layout, fig_rel="figures", title=title))
    with open(os.path.join(cdir, "chapter.md"), "w", encoding="utf-8") as fh:
        fh.write(to_markdown(layout, title))

    chap_rel = os.path.relpath(cdir, ROOT)
    items = to_dynamodb_items(layout, title, chap_rel)
    ddb_dir = os.path.join(ROOT, "data", "dynamodb")
    os.makedirs(ddb_dir, exist_ok=True)
    with open(os.path.join(ddb_dir, f"{chapter}.json"), "w", encoding="utf-8") as fh:
        json.dump(items, fh, indent=1, ensure_ascii=False)

    folios = [p.get("printed_page_number") for p in layout["pages"]]
    real = [f for f in folios if isinstance(f, int)]
    with open(os.path.join(cdir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(chapter_readme(book_id, chapter_num, title, layout, n_figs, real))
    return cdir, len(layout["pages"]), n_figs


def chapter_readme(book_id, chapter_num, title, layout, n_figs, folios):
    subject, klass, edition = design_lib.parse_book_id(book_id)
    d = design_lib.design_for(book_id)
    ed = EDITION_WORD[edition]
    span = f"{min(folios)}-{max(folios)}" if folios else "unknown"
    measured = sum(1 for p in layout["pages"] if p["sheet_note"].startswith("measured"))
    return f"""# {title or '(untitled)'} — chapter {chapter_num}

|  |  |
|---|---|
| book | **{d.name}** |
| edition | **{ed} NCERT** (`{edition}` = {'latest / rationalised' if edition == 'L' else 'older / pre-rationalisation'}) |
| book id | `{book_id}` |
| printed pages | {len(layout['pages'])} (folios {span}) |
| imprint | `{layout['pages'][0].get('imprint') or d.imprint(edition)}` |
| figures cut | {n_figs} |
| source PDF | `{layout['source_pdf']}` |
| sheet | {d.trim_pt[0]:.0f} x {d.trim_pt[1]:.0f} pt — the canonical NCERT trim, same for every book |

## Files

| file | what it is |
|---|---|
| `chapter.html` | the chapter page by page at the real trim, the book's own furniture drawn from the measured design. Self-contained: fonts are embedded, figures are the PNGs in `figures/`. |
| `chapter.md` | the same text as Markdown — for reading, diffing and feeding to an agent. |
| `layout.json` | every element with its role, its position on the canonical sheet (`bbox_sheet`) and its formatting runs. This is the record; the HTML and the Markdown are both rendered from it. |
| `figures/` | one PNG per real figure, named `p<folio>_fig<n>.png`. The page ground, the watermark, the header art and the QR code are NOT in here — they are page furniture, not artwork. |

## How this chapter was placed on the sheet

{measured} of {len(layout['pages'])} pages could measure their own crop against the book's
printed text grid (inner margin {d.inner_margin_pt:.0f}pt, measure {d.measure_pt:.0f}pt); the
rest inherited the chapter median. The offset applied was
`{layout['pages'][0]['sheet_offset_pt']}` pt.

That matters because the scans are not all the same size. A page rendered at its own scan size
comes out a different width from the same page in the other edition — which is exactly what
made the new Class 12 books render narrower than Class 11. Everything here is on one sheet.

## Rebuild

```bash
python code/build_chapter.py {book_id}-ch{chapter_num:02d}
```
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*", help="e.g. BIO11L-ch03")
    ap.add_argument("--book", action="append", default=[])
    ap.add_argument("--all", action="store_true", help="every chapter of each --book")
    ap.add_argument("--allow-unmeasured", action="store_true")
    a = ap.parse_args()

    jobs = []
    for c in a.chapters:
        m = re.fullmatch(r"([A-Z]{3}\d{2}[LO])-ch(\d+)", c)
        if not m:
            raise SystemExit(f"bad chapter id {c!r}; expected like BIO11L-ch03")
        jobs.append((m.group(1), int(m.group(2))))
    for book in a.book:
        subject, klass, edition = design_lib.parse_book_id(book)
        base = os.path.join(ROOT, "source_pdfs", EDITION_WORD[edition],
                            f"class_{klass}", SUBJECT_WORD[subject])
        if not os.path.isdir(base):
            print(f"!! no source folder for {book}: {base}", file=sys.stderr)
            continue
        nums = set()
        for f in sorted(os.listdir(base)):
            if not f.lower().endswith(".pdf"):
                continue
            m = re.search(r"(?:^|[_ ])(\d{1,2})[. _]", f) or re.search(r"Chapter_(\d+)", f)
            if m:
                nums.add(int(m.group(1)))
        for n in sorted(nums):
            jobs.append((book, n))

    ok = fail = 0
    for book, num in jobs:
        if not design_lib.is_measured(book) and not a.allow_unmeasured:
            print(f"SKIP {book}-ch{num:02d}: design not measured "
                  f"(pass --allow-unmeasured to render a draft)")
            continue
        try:
            cdir, pages, figs = build(book, num, a.allow_unmeasured)
            print(f"OK   {book}-ch{num:02d}  {pages:>3} pages  {figs:>3} figures  "
                  f"-> {os.path.relpath(cdir, ROOT)}")
            ok += 1
        except SystemExit as e:
            print(f"SKIP {book}-ch{num:02d}: {e}")
            fail += 1
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {book}-ch{num:02d}: {type(e).__name__}: {e}")
            fail += 1
    print(f"\n{ok} built, {fail} skipped/failed")


if __name__ == "__main__":
    main()
