#!/usr/bin/env python3
"""Put the A3 PASSAGES and A4 SUBTOPICS onto the chapter tree.

    from join_agent_structure import apply_agent_structure
    stats = apply_agent_structure(doc, layout, "BIO11L-ch01")

The fourth joiner. `join_agent_text` brings the words, `join_agent_layout` the arrangement,
`join_agent_special` the tables and equations; this one brings the chapter's MEANING-level
structure, which is the part no geometry can supply at all.

A3 · `a3-passage-splitter` -- WHICH BLOCKS FORM ONE PASSAGE
------------------------------------------------------------
Per section it returns block numbers grouped into passages:

    {"passages": [[1, 2], [3], [7, 8, 9, 10]],
     "note": "Blocks 7-10 are one passage: the introductory sentence plus the numbered rules
              of binomial nomenclature, of which block 10 is the last rule."}

That grouping is a reading judgement. A paragraph and the four numbered rules under it are one
passage because the rules only mean anything with the sentence that introduces them -- nothing
in the geometry says so, and a heading-based split would separate them.

A passage is also the unit an exam question's evidence CITES. `D4` quotes a passage id, so if
the passages are wrong the citation points at the wrong text.

A4 · `a4-subtopic-writer` -- WHAT THE PASSAGES ARE ABOUT
---------------------------------------------------------
    {"chapter": "BIO11-CH01",
     "subtopics": [{"n": 1, "name": "Diversity of living organisms and the need for
                    classification", "passages": ["BIO11L-CH01-P17", "BIO11L-CH01-P14", ...]}]}

Note the chapter key `BIO11-CH01` has NO EDITION LETTER while the passage ids inside it do
(`BIO11L-...`). That is deliberate and it is what lets one subtopic span both editions: the
same idea is taught in both books, under different section numbers, and the subtopic is the
thing that does not renumber. It is also why `topic_*` on a row can be populated for a chapter
whose own headings were rationalised away.

WHY THIS IS NOT DERIVED FROM THE NUMBERED HEADINGS
----------------------------------------------------
The tree already nests by printed heading (`1.2` -> `1.2.2`), and for a chapter that prints a
full heading hierarchy that is enough. But NCERT does not always print one: a chapter's
opening prose sits under no heading at all, Summary and Exercises are unnumbered, and the older
edition's `1.1 What is 'Living'?` was removed outright in the new one. The subtopic is the
layer that survives all of that, so it is stored ALONGSIDE the heading hierarchy, never instead
of it.
"""

import glob
import json
import os
import re

_RUN_PRIORITY = {"adjudicated": 0, "retry2": 1, "retry1": 2, "runB": 3, "runA": 4}


def _best(paths):
    return sorted(paths, key=lambda p: _RUN_PRIORITY.get(
        os.path.basename(p).split(".")[-2], 9))[0] if paths else None


def a3_passages(chapter, steps_dir="steps"):
    """[[block numbers], ...] for the chapter, in section order."""
    by_section = {}
    for path in glob.glob(os.path.join(steps_dir, "A3", "out", f"{chapter}-s*.json")):
        m = re.search(r"-s(\d+)\.(\w+)\.json$", os.path.basename(path))
        if not m:
            continue
        by_section.setdefault(int(m.group(1)), []).append(path)
    out = []
    for sec in sorted(by_section):
        path = _best(by_section[sec])
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        for grp in d.get("passages") or []:
            if grp:
                out.append({"section": sec, "blocks": list(grp),
                            "note": d.get("note") or ""})
    return out


def a4_subtopics(book_base, chapter_num, steps_dir="steps"):
    """A4's subtopics for this chapter, keyed WITHOUT the edition letter."""
    key = f"{book_base}-CH{chapter_num:02d}"
    paths = glob.glob(os.path.join(steps_dir, "A4", "out", f"{key}.*.json"))
    path = _best(paths)
    if not path:
        return []
    try:
        with open(path, encoding="utf-8") as fh:
            return (json.load(fh) or {}).get("subtopics") or []
    except (OSError, json.JSONDecodeError):
        return []


def _walk(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from _walk(n["children"])


def apply_agent_structure(doc, layout, chapter, steps_dir="steps"):
    """Attach passages and subtopics to `doc` (the chapter tree), in place."""
    book_base = doc["book"]
    chn = doc["chapter"]["number"]
    stats = {"passages": 0, "passage_nodes": 0, "subtopics": 0, "subtopic_links": 0,
             "a3_found": False, "a4_found": False}

    # --- A3: group the tree's nodes into passages --------------------------------------
    groups = a3_passages(chapter, steps_dir)
    stats["a3_found"] = bool(groups)
    if groups:
        by_block = {}
        for n in _walk(doc["tree"]):
            bn = n.get("a2_block_n")
            if bn is not None:
                by_block.setdefault(bn, []).append(n)
        passages = []
        for i, g in enumerate(groups, 1):
            pid = f"{doc['book_id']}-CH{chn:02d}-P{i:02d}"
            members = [n for b in g["blocks"] for n in by_block.get(b, [])]
            if not members:
                continue
            for n in members:
                n["passage_id"] = pid
                stats["passage_nodes"] += 1
            passages.append({
                "passage_id": pid, "section": g["section"],
                "node_ids": [n["id"] for n in members],
                "blocks": g["blocks"],
                "pages": sorted({p for n in members for p in (n.get("pages") or [])}),
                "text": " ".join((n.get("body") or "") for n in members).strip(),
                "note": g["note"],
                "source": "a3-agent",
            })
        doc["passages"] = passages
        stats["passages"] = len(passages)

    # --- A4: name the subtopics and link them to passages ------------------------------
    subs = a4_subtopics(book_base, chn, steps_dir)
    stats["a4_found"] = bool(subs)
    if subs:
        out = []
        pid_to_nodes = {}
        for p in doc.get("passages") or []:
            pid_to_nodes[p["passage_id"]] = p["node_ids"]
        for st in subs:
            name = st.get("name") or ""
            pids = [p for p in (st.get("passages") or [])]
            node_ids = [i for p in pids for i in pid_to_nodes.get(p, [])]
            out.append({"n": st.get("n"), "name": name, "passages": pids,
                        "node_ids": node_ids,
                        "from_heading": st.get("from_heading"),
                        "source": "a4-agent"})
            stats["subtopic_links"] += len(node_ids)
        doc["subtopics"] = out
        stats["subtopics"] = len(out)
        # Stamp each node with the subtopic it belongs to, so a single row carries it without
        # a second fetch -- the same reason chapter/topic/subtopic are denormalised.
        by_id = {n["id"]: n for n in _walk(doc["tree"])}
        for st in out:
            for nid in st["node_ids"]:
                n = by_id.get(nid)
                if n is not None:
                    n["agent_subtopic_n"] = st["n"]
                    n["agent_subtopic_name"] = st["name"]

    doc["structure_join"] = stats
    return stats
