#!/usr/bin/env python3
"""Flatten one chapter.json into DynamoDB rows -- the 7 kinds of `ncert_content`.

    python code/export_rows.py BIO11O-ch02
    python code/export_rows.py --all

Writes `data/dynamodb/<BOOK_ID>/<BOOK_ID>-ch<NN>.json`, one file per chapter, plus
`data/dynamodb/_style/STYLE_<DESIGN>.json` and `data/dynamodb/_pairs/PAIR_<SUBJ><CLASS>.json`.

    PK                     SK                      kind
    BOOK#BIO11#EN          META                    book
    BOOK#BIO11#EN          UNIT#1                  unit
    CH#BIO11-01#EN         META                    chapter
    CH#BIO11-01#EN         N#003.005.001           node      <- almost all rows
    CH#BIO11-01#EN         PG#007                  page
    CH#BIO11-01#EN         TERM#genus              term
    CH#BIO11-01#EN         CHG#<reprint>#<id>      change
    STYLE#BIO11            V1                      the design, shared by both editions
    PAIR#BIO11             LATEST#01               old <-> new, matched on TITLE

WHY THE SORT KEY IS A TREE PATH AND NOT THE BOOK'S OWN NUMBER
---------------------------------------------------------------
`N#003.005.001` sorts the chapter into reading order for free, so "all of topic 1.2" is
`begins_with(SK, "N#003")` and the whole chapter is the bare partition. The book's number is
kept in its own `topic_no` / `subtopic_no` field, but it cannot be the key:

  * as text, `1.10` sorts before `1.2`
  * intro paragraphs, Summary and Exercises have no number at all
  * numbers clash -- in Physics Class 11 Chapter 4, `4.5` is both a section (Newton's second
    law) and an exercise question

WHY EVERY NODE CARRIES ITS CHAPTER, TOPIC AND SUBTOPIC
--------------------------------------------------------
DynamoDB cannot join. A product uses ONE row at a time -- an NCERT line card, a flashcard, a
PYQ link, a search hit, an AI prompt -- and each needs
`Ch 1 The Living World > 1.2 Taxonomic Categories > 1.2.2 Genus` right there. Denormalising it
costs about 150 characters a row, roughly 6 MB across the whole corpus, and it cannot go stale
because the loader rewrites it from chapter.json every time.
"""

import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib  # noqa: E402

SUBJECT_SHORT = {"biology": "Bio", "chemistry": "Chem", "physics": "Phy"}
# `class` and `text` are DynamoDB RESERVED WORDS -- every query naming them needs an expression
# alias. Renamed at the source so no caller ever has to remember.
RESERVED_RENAMES = {"class": "grade", "text": "body"}


def _num(v, dp=4):
    return f"{float(v):.{dp}f}"


def _walk(nodes, parents=()):
    for n in nodes:
        yield n, parents
        if n.get("children"):
            yield from _walk(n["children"], parents + (n,))


def _levels(parents):
    """(topic, subtopic, sub_subtopic) -- the numbered sections above this node."""
    secs = [p for p in parents if p.get("kind") in ("section", "summary", "exercises")]
    out = [None, None, None]
    for i, s in enumerate(secs[:3]):
        out[i] = s
    return out


def _address(doc, parents, node, para_no):
    bits = [f"{SUBJECT_SHORT.get(doc['subject'], doc['subject'])} {doc['grade']}",
            f"Ch {doc['chapter']['number']}"]
    for p in parents:
        if p.get("kind") in ("section", "summary", "exercises"):
            bits.append(" ".join(x for x in (p.get("number"), p.get("title")) if x))
    if node["kind"] == "para" and para_no:
        bits.append(f"¶{para_no}")
    elif node.get("number"):
        bits.append(node["number"])
    return " › ".join(bits)


def chapter_rows(doc):
    book, grade, lang = doc["book"], doc["grade"], doc["lang"]
    chn = doc["chapter"]["number"]
    pk = f"CH#{book}-{chn:02d}#{lang}"
    base = {"book": book, "book_id": doc["book_id"], "grade": grade,
            "subject": doc["subject"], "edition": doc["edition"],
            "lang": lang, "reprint": doc["reprint"],
            "chapter_no": chn, "chapter_title": doc["chapter"]["title"]}
    rows = []

    counts = {}
    para_counter = {}
    terms = {}

    for node, parents in _walk(doc["tree"]):
        counts[node["kind"]] = counts.get(node["kind"], 0) + 1
        topic, sub, subsub = _levels(parents)
        key = id(parents[-1]) if parents else 0
        para_no = None
        if node["kind"] == "para":
            para_counter[key] = para_counter.get(key, 0) + 1
            para_no = para_counter[key]

        row = {"PK": pk, "SK": f"N#{node['path']}", "id": node["id"],
               "kind": node["kind"], **base}
        for lvl, name in ((topic, "topic"), (sub, "subtopic"), (subsub, "sub_subtopic")):
            if lvl is None:
                continue
            row[f"{name}_no"] = lvl.get("number")
            row[f"{name}_title"] = lvl.get("title")
            row[f"{name}_id"] = lvl.get("id")
        row["address"] = _address(doc, parents, node, para_no)
        if para_no:
            row["para_no"] = para_no
        for k in ("number", "title", "body", "body_md", "marks", "sentences", "terms",
                  "pages", "boxes", "items", "caption", "table_text",
                  "image", "image_local", "image_sha256", "source", "qa",
                  "line_pitch_pt", "moved_from_printed_position"):
            if node.get(k) not in (None, [], ""):
                row[k] = node[k]
        # GSI2: ready-made lists -- every figure, every table, every question in a book.
        if node["kind"] in ("figure", "table", "question", "equation"):
            row["list_key"] = f"{book}#{lang}#{node['kind']}"
        rows.append(row)

        for t in node.get("terms") or []:
            terms.setdefault(t.lower(), (t, node, topic, sub))

    # ---- page rows -----------------------------------------------------------------------
    for p in doc["pages"]:
        if p.get("printed") is None:
            continue
        rows.append({"PK": pk, "SK": f"PG#{p['printed']:03d}", "kind": "page", **base,
                     "printed_page_number": p["printed"], "page_side": p.get("page_side"),
                     "page_file": p.get("page_file"), "size_pt": p.get("size_pt"),
                     "header": p.get("header"), "footer": p.get("footer"),
                     "has_text_layer": p.get("has_text_layer"),
                     "source": "page_image" if p.get("text_source") == "a2-agent"
                               else "text_layer"})

    # ---- term rows -----------------------------------------------------------------------
    for low, (term, node, topic, sub) in sorted(terms.items()):
        slug = re.sub(r"[^a-z0-9]+", "-", low).strip("-")
        row = {"PK": pk, "SK": f"TERM#{slug}", "kind": "term", **base,
               "term": term, "defined_in": node["id"], "defined_at": f"N#{node['path']}",
               "list_key": f"TERM#{slug}"}
        if topic:
            row["topic_no"], row["topic_title"] = topic.get("number"), topic.get("title")
        if sub:
            row["subtopic_no"], row["subtopic_title"] = sub.get("number"), sub.get("title")
        rows.append(row)

    # ---- passage rows (A3) ------------------------------------------------------------
    # A passage is the unit an exam question's evidence CITES, so it is a row of its own and
    # not merely a field on the nodes it spans.
    for ps in doc.get("passages") or []:
        rows.append({"PK": pk, "SK": f"PS#{ps['passage_id']}", "kind": "passage", **base,
                     "passage_id": ps["passage_id"], "node_ids": ps.get("node_ids"),
                     "pages": ps.get("pages"), "body": ps.get("text", ""),
                     "a3_blocks": ps.get("blocks"), "note": ps.get("note") or None,
                     "source": ps.get("source", "a3-agent"),
                     "list_key": f"{book}#{lang}#passage"})

    # ---- subtopic rows (A4) -----------------------------------------------------------
    # Keyed WITHOUT the edition letter on purpose: the same subtopic spans the old and the new
    # book, which is what lets a question mapped once stay mapped after rationalisation.
    for st in doc.get("subtopics") or []:
        n = st.get("n")
        rows.append({"PK": pk, "SK": f"ST#{int(n):02d}" if n else f"ST#{st['name'][:20]}",
                     "kind": "subtopic", **base,
                     "subtopic_key": f"{book}-CH{chn:02d}",
                     "n": n, "name": st.get("name"),
                     "passages": st.get("passages"), "node_ids": st.get("node_ids"),
                     "from_heading": st.get("from_heading"),
                     "source": st.get("source", "a4-agent"),
                     "list_key": f"{book}#{lang}#subtopic"})

    # ---- chapter row ----------------------------------------------------------------------
    rows.append({"PK": pk, "SK": "META", "kind": "chapter", **base,
                 "id": doc["chapter"]["id"],
                 "title": doc["chapter"]["title"],
                 "unit": doc["chapter"].get("unit"),
                 "pages": doc["chapter"].get("pages"),
                 "counts": counts,
                 "design_key": doc.get("design_key"),
                 "sheet_pt": doc.get("sheet_pt"),
                 "source_pdf": doc.get("source_pdf"),
                 "ncert_file": doc.get("ncert_file"),
                 "text_join": doc.get("text_join"),
                 "layout_join": doc.get("layout_join"),
                 "special_join": doc.get("special_join"),
                 "structure_join": doc.get("structure_join"),
                 "passages": len(doc.get("passages") or []),
                 "subtopics": len(doc.get("subtopics") or [])})

    # ---- book row -------------------------------------------------------------------------
    rows.append({"PK": f"BOOK#{book}#{lang}", "SK": "META", "kind": "book",
                 "book": book, "grade": grade, "subject": doc["subject"], "lang": lang,
                 "design_key": doc.get("design_key")})
    if doc["chapter"].get("unit"):
        rows.append({"PK": f"BOOK#{book}#{lang}", "SK": f"UNIT#{doc['chapter']['unit']}",
                     "kind": "unit", "book": book, "grade": grade, "lang": lang,
                     "unit": doc["chapter"]["unit"]})
    return rows


def style_row(design_key, book_ids):
    d = design_lib.design_for(book_ids[0])
    mm = design_lib.pt_to_mm
    x0, _, x1, _ = d.text_box("recto")

    def g(attr):
        return getattr(d, attr, None)
    return {
        "PK": f"STYLE#{design_key}", "SK": "V1", "kind": "style",
        "name": d.name, "applies_to": book_ids,
        "measured": design_lib.is_measured(book_ids[0]),
        "page": {"trim_mm": [round(mm(d.trim_pt[0]), 2), round(mm(d.trim_pt[1]), 2)],
                 "inner_margin_mm": round(mm(d.inner_margin_pt), 2),
                 "measure_mm": round(mm(d.measure_pt), 2),
                 "text_top_mm": round(mm(d.text_top_pt), 2),
                 "text_foot_mm": round(mm(d.text_foot_pt), 2),
                 "mirrors": True},
        "type": {"body_pt": d.body_pt, "leading": d.leading, "ink": d.ink,
                 "font_body": d.body_font, "font_display": d.display_font},
        "header": {"band": g("header_band"), "strip": g("header_strip"),
                   "corner": g("header_corner"), "motif": g("header_motif")},
        "folio": g("folio"),
        "running_head": g("running_head"),
        "footer": {"bar": g("footer_bar"), "imprint": g("imprint")},
        "opener": g("opener"),
        "kinds": {
            "para": {"size_rel": 1.0, "align": "justify", "color": d.ink},
            "section": {"size_rel": d.heading_size_rel, "color": d.heading_ink,
                        "variant": "small-caps", "weight": 700, "align": "left"},
            "list": {"size_rel": 1.0, "align": "left"},
            "figure": {"render": "image"}, "table": {"render": "image"},
            "box": {"size_rel": 0.95, "align": "left"},
            "summary": {"size_rel": d.heading_size_rel, "color": d.heading_ink},
            "exercises": {"size_rel": d.heading_size_rel, "color": d.heading_ink},
        },
        "furniture_assets": f"assets/furniture/{design_key}/",
        "imprint_by_edition": d.imprint_by_edition,
    }


def load_docs():
    docs = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                           "chapter.json"))):
        with open(p, encoding="utf-8") as fh:
            docs.append((p, json.load(fh)))
    return docs


def pair_rows(docs):
    """old <-> new, matched on TITLE. Never on chapter number -- the editions renumber."""
    by = {}
    for _p, d in docs:
        key = (d["book"], re.sub(r"[^a-z0-9]+", " ",
                                 (d["chapter"]["title"] or "").lower()).strip())
        by.setdefault(key, {})[d["edition"]] = d
    out = []
    for (book, title), eds in sorted(by.items()):
        if "latest" in eds and "older" in eds and title:
            out.append({"PK": f"PAIR#{book}", "SK": f"LATEST#{eds['latest']['chapter']['number']:02d}",
                        "kind": "pair", "chapter_title": eds["latest"]["chapter"]["title"],
                        "latest_chapter_num": eds["latest"]["chapter"]["number"],
                        "older_chapter_num": eds["older"]["chapter"]["number"],
                        "matched_on": "title", "book": book,
                        "grade": eds["latest"]["grade"], "subject": eds["latest"]["subject"]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()

    docs = load_docs()
    want = set(a.chapters)
    ddb = os.path.join(ROOT, "data", "dynamodb")
    designs, written = {}, 0
    for path, doc in docs:
        cid = f"{doc['book_id']}-ch{doc['chapter']['number']:02d}"
        if want and cid not in want:
            continue
        rows = chapter_rows(doc)
        out_dir = os.path.join(ddb, doc["book_id"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"{cid}.json"), "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1, ensure_ascii=False)
        designs.setdefault(doc.get("design_key") or doc["book"], set()).add(doc["book_id"])
        kinds = {}
        for r in rows:
            kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
        print(f"{cid}: {len(rows)} rows  {kinds}")
        written += 1

    os.makedirs(os.path.join(ddb, "_style"), exist_ok=True)
    for dk, books in designs.items():
        with open(os.path.join(ddb, "_style", f"STYLE_{dk}.json"), "w", encoding="utf-8") as fh:
            json.dump(style_row(dk, sorted(books)), fh, indent=1, ensure_ascii=False)

    pairs = pair_rows(docs)
    if pairs:
        os.makedirs(os.path.join(ddb, "_pairs"), exist_ok=True)
        by_book = {}
        for r in pairs:
            by_book.setdefault(r["PK"].split("#")[1], []).append(r)
        for b, rs in by_book.items():
            with open(os.path.join(ddb, "_pairs", f"PAIR_{b}.json"), "w",
                      encoding="utf-8") as fh:
                json.dump(rs, fh, indent=1, ensure_ascii=False)
    print(f"\n{written} chapters, {len(designs)} style rows, {len(pairs)} pair rows "
          f"-> {os.path.relpath(ddb, ROOT)}")


if __name__ == "__main__":
    main()
