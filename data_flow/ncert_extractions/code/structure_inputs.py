#!/usr/bin/env python3
"""A3 / A4 inputs built from the FINISHED chapter tree, so passages and subtopics address nodes
that exist.

    python code/structure_inputs.py BIO11L-ch01 a3      # writes steps/A3/work/<cid>-sNN.tree.input.json
    python code/structure_inputs.py BIO11L-ch01 a4      # after A3: steps/A4/work/<key>.tree.input.json

WHY THE OLD JOIN COULD NOT BE REPAIRED
----------------------------------------
`join_agent_structure.apply_agent_structure` read A3's block numbers as A2's `a2_block_n`. But
A3 numbers blocks WITHIN A SECTION, while `a2_block_n` restarts on every PAGE -- so "block 1"
collected the first block of every page. Measured on BIO11L ch01: passage P01 held `CHAPTER 1`,
the whole Ernst Mayr biography and paragraphs from four different pages (`pages: [4, 5, 8, 9]`),
and the join also ran before later passes renumbered the node ids, leaving 31 passage node ids
and 25 subtopic node ids pointing at nothing. The A3 inputs that defined the numbering were
not kept, so the old outputs cannot be re-read correctly.

So the inputs are built from chapter.json itself, AFTER every tree pass, and each numbered
block records a FINGERPRINT of the node it came from (kind + normalised text). The join matches
fingerprints, not ids, so a rebuild that renumbers paths cannot detach a passage again.

Sections are the tree's own: the unit pages, the chapter's opening (titles + the prose before
the first heading), then every heading node with the content directly under it.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

RUN = "tree"
HEADING_KINDS = ("section", "summary", "exercises")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def node_text(n):
    k = n.get("kind")
    if k in HEADING_KINDS:
        return " ".join(x for x in (n.get("number"), n.get("title") or n.get("body")) if x)
    if k in ("figure", "table"):
        return (n.get("caption") or "").strip()
    if k == "question":
        subs = " ".join(s.get("body") or "" for s in n.get("parts") or [])
        return f"{n.get('number')}. {n.get('body') or ''} {subs}".strip()
    return (n.get("body") or "").strip()


def fingerprint(n):
    return f"{n.get('kind')}|{norm(node_text(n))[:80]}"


def sections(doc):
    """[(heading_text, [nodes])] in reading order."""
    out = []
    unit = [n for n in doc["tree"] if n.get("belongs") == "unit"]
    if unit:
        out.append(("Unit pages", unit))
    opening, rest = [], []
    for n in doc["tree"]:
        if n.get("belongs") == "unit":
            continue
        if n.get("kind") in HEADING_KINDS:
            rest.append(n)
        elif rest:
            rest.append(n)
        else:
            opening.append(n)
    if opening:
        out.append(("Chapter opening", opening))

    def rec(n):
        own = [n] + [c for c in n.get("children") or [] if c.get("kind") not in HEADING_KINDS]
        out.append((node_text(n), own))
        for c in n.get("children") or []:
            if c.get("kind") in HEADING_KINDS:
                rec(c)
    for n in rest:
        if n.get("kind") in HEADING_KINDS:
            rec(n)
        else:
            out[-1][1].append(n)
    return out


def chapter_paths(cid):
    import cdn_publish
    cdir = cdn_publish.chapter_dir(cid)
    with open(os.path.join(cdir, "chapter.json"), encoding="utf-8") as fh:
        return cdir, json.load(fh)


def write_a3(cid):
    _, doc = chapter_paths(cid)
    work = os.path.join(ROOT, "steps", "A3", "work")
    os.makedirs(work, exist_ok=True)
    made = []
    for i, (head, nodes) in enumerate(sections(doc), 1):
        blocks = [{"n": k, "kind": n.get("kind"), "text": node_text(n)}
                  for k, n in enumerate(nodes, 1)]
        item = f"{cid}-s{i:02d}"
        path = os.path.join(work, f"{item}.{RUN}.input.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"book_id": doc["book_id"], "chapter": doc["chapter"]["number"],
                       "section_heading": head, "blocks": blocks,
                       "_fingerprints": {str(k): fingerprint(n) for k, n in enumerate(nodes, 1)}},
                      fh, ensure_ascii=False, indent=1)
        made.append((item, path, os.path.join(ROOT, "steps", "A3", "out", f"{item}.{RUN}.json")))
    return made


def write_a4(cid):
    import join_agent_structure as jas
    _, doc = chapter_paths(cid)
    passages = jas.tree_passages(doc, cid)
    if not passages:
        raise SystemExit(f"{cid}: no A3 `{RUN}` outputs to build subtopics from")
    heads = []

    def rec(ns):
        for n in ns:
            if n.get("kind") in HEADING_KINDS:
                heads.append({"number": n.get("number"), "text": n.get("title") or n.get("body")})
            rec(n.get("children") or [])
    rec(doc["tree"])
    key = f"{doc['book']}-CH{doc['chapter']['number']:02d}"
    work = os.path.join(ROOT, "steps", "A4", "work")
    os.makedirs(work, exist_ok=True)
    path = os.path.join(work, f"{key}.{RUN}.input.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"chapter": key, "chapter_title": doc["chapter"]["title"], "headings": heads,
                   "passages": [{"id": p["passage_id"], "kind": p["kinds"][0],
                                 "text": p["text"][:200]} for p in passages]},
                  fh, ensure_ascii=False, indent=1)
    return path, os.path.join(ROOT, "steps", "A4", "out", f"{key}.{RUN}.json")


if __name__ == "__main__":
    cid, step = sys.argv[1], sys.argv[2]
    if step == "a3":
        for item, i, o in write_a3(cid):
            print(f"{item} | a3-passage-splitter | {os.path.relpath(i, ROOT)} | {os.path.relpath(o, ROOT)}")
    else:
        i, o = write_a4(cid)
        print(f"a4-subtopic-writer | {os.path.relpath(i, ROOT)} | {os.path.relpath(o, ROOT)}")
