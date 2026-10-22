#!/usr/bin/env python3
"""Diff the OLD and NEW edition of one chapter into `change` rows.

    python code/build_change_rows.py --book BIO11 --chapter 1
    python code/build_change_rows.py --all

A `change` row records what NCERT did to a piece of text between two books. The schema's own
example is reprint-to-reprint (`CHG#2027-28#…`) -- what a new YEAR's printing altered. That is
one case of two, and it is the smaller one.

THE BIGGER CASE IS RATIONALISATION: OLD EDITION -> NEW EDITION
----------------------------------------------------------------
Between the pre-rationalisation book and the current one, NCERT deleted whole sections,
renumbered what remained and rewrote paragraphs. Measured on Class 11 Biology Chapter 1:

    1.1 What is 'Living'?          present in the old book, REMOVED from the new
    1.4 Taxonomical Aids           present in the old book, REMOVED from the new
    1.2 Taxonomic Categories       was 1.3 in the old book  -- MOVED
    1.2.2 Genus                    was 1.3.2                -- MOVED

Both kinds of change matter to a student and to a question bank, and they are the same shape of
fact: this text was added / removed / moved / edited, here is where it was, here is where it is
now. So they are the same row kind, separated by a `change_type` and by which two books were
compared.

Why this is not the `PAIR#` row's job: the pair row says "new chapter 4 is old chapter 5". That
is the CHAPTER level. A change row is the PARAGRAPH level, and it is what lets a product answer
"has the line my question was built from survived?" -- which is the whole reason `ncert_links`
exists.

HOW THE MATCH IS MADE
-----------------------
By TEXT, not by position -- position is the thing that changed. Paragraphs are normalised
(case, punctuation and whitespace folded away) and matched exactly first; what is left over is
matched on a similarity ratio, so a paragraph with a small edit is recognised as the same
paragraph rather than as one removal plus one addition. Anything still unmatched is a genuine
add or delete.

A MOVE IS NOT A CHANGE TO THE TEXT. Where the text is identical and only the address differs,
the row is `moved` and the node keeps its id -- which is exactly what makes an id worth having:
a question mapped to that paragraph before rationalisation still resolves afterwards.
"""

import argparse
import difflib
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

SIMILAR_ENOUGH = 0.82          # below this it is a different paragraph, not an edit


def _norm(s):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", (s or "").lower())).strip()


def _walk(nodes, parents=()):
    for n in nodes:
        yield n, parents
        if n.get("children"):
            yield from _walk(n["children"], parents + (n,))


def _address(doc, parents, node):
    bits = [f"Ch {doc['chapter']['number']}"]
    for p in parents:
        if p.get("kind") in ("section", "summary", "exercises"):
            bits.append(" ".join(x for x in (p.get("number"), p.get("title")) if x))
    return " › ".join(bits)


def _pieces(doc):
    """Every quotable piece of a chapter, with where it sits."""
    out = []
    for n, parents in _walk(doc["tree"]):
        if n["kind"] not in ("para", "list", "section", "summary", "exercises"):
            continue
        body = n.get("body") or " ".join(
            i.get("body", "") for i in (n.get("items") or [])) or n.get("title") or ""
        if not body.strip():
            continue
        out.append({"id": n["id"], "path": n["path"], "kind": n["kind"],
                    "number": n.get("number"), "title": n.get("title"),
                    "body": body, "norm": _norm(body),
                    "address": _address(doc, parents, n),
                    "pages": n.get("pages") or []})
    return out


def diff_editions(old_doc, new_doc):
    """[change rows] describing what rationalisation did to this chapter."""
    old, new = _pieces(old_doc), _pieces(new_doc)
    book = new_doc["book"]
    chn = new_doc["chapter"]["number"]
    pk = f"CH#{book}-{chn:02d}#{new_doc['lang']}"
    base = {"kind": "change", "book": book, "grade": new_doc["grade"],
            "subject": new_doc["subject"], "lang": new_doc["lang"],
            "chapter_no": chn, "chapter_title": new_doc["chapter"]["title"],
            "from_edition": old_doc["edition"], "from_reprint": old_doc["reprint"],
            "to_edition": new_doc["edition"], "to_reprint": new_doc["reprint"],
            "compared": f"{old_doc['book_id']}→{new_doc['book_id']}"}

    by_norm = {}
    for o in old:
        by_norm.setdefault(o["norm"], []).append(o)
    rows, used_old, seq = [], set(), 0

    def add(ctype, o, n, note=None):
        nonlocal seq
        seq += 1
        r = {"PK": pk, "SK": f"CHG#{new_doc['reprint']}#{seq:03d}", **base,
             "change_type": ctype}
        if o:
            r.update({"from_address": o["address"], "from_number": o["number"],
                      "from_id": o["id"], "from_pages": o["pages"]})
        if n:
            r.update({"to_address": n["address"], "to_number": n["number"],
                      "to_id": n["id"], "to_pages": n["pages"],
                      "body": n["body"][:600]})
        elif o:
            r["body"] = o["body"][:600]
        if note:
            r["note"] = note
        r["list_key"] = f"{book}#{new_doc['lang']}#change"
        rows.append(r)

    # 1 exact text matches -- unchanged text, possibly MOVED
    for n in new:
        cands = [o for o in by_norm.get(n["norm"], []) if id(o) not in used_old]
        if not cands:
            continue
        o = cands[0]
        used_old.add(id(o))
        n["_matched"] = True
        if o["address"] != n["address"] or o["number"] != n["number"]:
            add("moved", o, n,
                f"text unchanged; address {o['address']} → {n['address']}")

    # 2 near matches -- EDITED
    rest_old = [o for o in old if id(o) not in used_old]
    for n in new:
        if n.get("_matched"):
            continue
        best, ratio = None, 0.0
        for o in rest_old:
            r = difflib.SequenceMatcher(None, o["norm"][:400], n["norm"][:400]).ratio()
            if r > ratio:
                best, ratio = o, r
        if best is not None and ratio >= SIMILAR_ENOUGH:
            used_old.add(id(best))
            rest_old = [o for o in rest_old if id(o) not in used_old]
            n["_matched"] = True
            add("edited", best, n, f"similarity {ratio:.2f}")

    # 3 what is left
    for n in new:
        if not n.get("_matched"):
            add("added", None, n)
    for o in old:
        if id(o) not in used_old:
            add("removed", o, None,
                "present in the older edition, not found in the latest")
    return rows


def load(book, chn):
    out = {}
    for p in glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                    "chapter.json")):
        with open(p, encoding="utf-8") as fh:
            d = json.load(fh)
        if d["book"] == book and d["chapter"]["number"] == chn:
            out[d["edition"]] = d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()

    jobs = []
    if a.all:
        seen = set()
        for p in glob.glob(os.path.join(ROOT, "data", "*_ncert", "class_*", "*", "*",
                                        "chapter.json")):
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)
            jobs.append((d["book"], d["chapter"]["number"])) if (
                d["book"], d["chapter"]["number"]) not in seen else None
            seen.add((d["book"], d["chapter"]["number"]))
    else:
        if not (a.book and a.chapter):
            raise SystemExit("pass --book BIO11 --chapter 1, or --all")
        jobs = [(a.book, a.chapter)]

    out_dir = os.path.join(ROOT, "data", "dynamodb", "_changes")
    total = 0
    for book, chn in jobs:
        eds = load(book, chn)
        if "older" not in eds or "latest" not in eds:
            print(f"{book}-ch{chn:02d}: SKIP — need BOTH editions built "
                  f"(have: {sorted(eds) or 'none'})")
            continue
        rows = diff_editions(eds["older"], eds["latest"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"CHG_{book}-ch{chn:02d}.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1, ensure_ascii=False)
        kinds = {}
        for r in rows:
            kinds[r["change_type"]] = kinds.get(r["change_type"], 0) + 1
        print(f"{book}-ch{chn:02d}: {len(rows)} change rows  {kinds}")
        total += len(rows)
    print(f"\n{total} change rows -> data/dynamodb/_changes/")


if __name__ == "__main__":
    main()
