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


TREE_RUN = "tree"


def _tree_inputs(chapter, steps_dir="steps"):
    return sorted(glob.glob(os.path.join(steps_dir, "A3", "work",
                                         f"{chapter}-s*.{TREE_RUN}.input.json")))


def tree_passages(doc, chapter, steps_dir="steps"):
    """Passages from A3 `tree` runs, whose inputs were built from the finished chapter.json
    (`structure_inputs.py`). Each block is matched back to a node by its FINGERPRINT, so a
    rebuild that renumbers ids cannot detach a passage."""
    import structure_inputs as si
    by_fp = {}
    for n in _walk(doc["tree"]):
        by_fp.setdefault(si.fingerprint(n), []).append(n)
    out, k = [], 0
    for ipath in _tree_inputs(chapter, steps_dir):
        m = re.search(r"-s(\d+)\.", os.path.basename(ipath))
        opath = os.path.join(steps_dir, "A3", "out",
                             os.path.basename(ipath).replace(".input.json", ".json"))
        if not (m and os.path.exists(opath)):
            continue
        with open(ipath, encoding="utf-8") as fh:
            inp = json.load(fh)
        with open(opath, encoding="utf-8") as fh:
            res = json.load(fh)
        fps = inp.get("_fingerprints") or {}
        for grp in res.get("passages") or []:
            members = []
            for b in grp:
                cand = by_fp.get(fps.get(str(b)), [])
                hit = next((c for c in cand if c not in members), None)
                if hit is not None:
                    members.append(hit)
            if not members:
                continue
            k += 1
            files = []
            for n in members:
                for f in n.get("page_files") or [n.get("page_file")]:
                    if f and f not in files:
                        files.append(f)
            out.append({
                "passage_id": f"{doc['book_id']}-CH{doc['chapter']['number']:02d}-P{k:02d}",
                "section": int(m.group(1)), "section_heading": inp.get("section_heading"),
                "blocks": list(grp), "node_ids": [n["id"] for n in members],
                "kinds": [n.get("kind") for n in members],
                "page_files": files,
                "pages": sorted({p for n in members for p in (n.get("pages") or [])}),
                "text": " ".join(_passage_text(n) for n in members).strip(),
                "note": res.get("note") or "", "source": "a3-agent",
                "_members": members})
    return out


def _passage_text(n):
    """A node's text as its passage carries it. A TABLE CARRIES ITS ROWS: its passage held only
    the caption (`TABLE 2.1 Characteristics of the Five Kingdoms`, BIO11L ch02 P03), so a search
    or a PYQ match over passages never saw a single cell. Rows follow the caption one per line,
    cells joined ` | ` as in the node's `body`. (`node_text` stays caption-only: it is also the
    fingerprint that matches agent passages back to nodes.)"""
    import structure_inputs as si
    t = si.node_text(n)
    if n.get("kind") == "table" and (n.get("body") or "").strip():
        t = f"{t}\n{n['body'].strip()}".strip()
    return t


def apply_tree_structure(doc, chapter, steps_dir="steps"):
    """Passages and subtopics for a chapter whose A3/A4 ran on the finished tree. Returns
    None when there are no such runs (the chapter keeps whatever it had)."""
    if not _tree_inputs(chapter, steps_dir):
        return None
    for n in _walk(doc["tree"]):
        for k in ("passage_id", "agent_subtopic_n", "agent_subtopic_name"):
            n.pop(k, None)
    passages = tree_passages(doc, chapter, steps_dir)
    for p in passages:
        for n in p.pop("_members"):
            n["passage_id"] = p["passage_id"]
    doc["passages"] = passages
    stats = {"passages": len(passages), "passage_nodes": sum(len(p["node_ids"]) for p in passages),
             "subtopics": 0, "subtopic_links": 0, "source": "tree"}
    key = f"{doc['book']}-CH{doc['chapter']['number']:02d}"
    sub_path = os.path.join(steps_dir, "A4", "out", f"{key}.{TREE_RUN}.json")
    by_pid = {p["passage_id"]: p for p in passages}
    by_id = {n["id"]: n for n in _walk(doc["tree"])}
    subs = []
    if os.path.exists(sub_path):
        with open(sub_path, encoding="utf-8") as fh:
            for st in (json.load(fh) or {}).get("subtopics") or []:
                pids = [p for p in st.get("passages") or [] if p in by_pid]
                node_ids = [i for p in pids for i in by_pid[p]["node_ids"]]
                subs.append({"n": st.get("n"), "name": st.get("name") or "", "passages": pids,
                             "node_ids": node_ids, "from_heading": st.get("from_heading"),
                             "source": "a4-agent"})
                for nid in node_ids:
                    if nid in by_id:
                        by_id[nid]["agent_subtopic_n"] = st.get("n")
                        by_id[nid]["agent_subtopic_name"] = st.get("name")
    doc["subtopics"] = subs
    stats["subtopics"] = len(subs)
    stats["subtopic_links"] = sum(len(s["node_ids"]) for s in subs)
    doc["structure_join"] = stats
    return stats


def apply_agent_structure(doc, layout, chapter, steps_dir="steps"):
    """Attach passages and subtopics to `doc` (the chapter tree), in place."""
    book_base = doc["book"]
    chn = doc["chapter"]["number"]
    stats = {"passages": 0, "passage_nodes": 0, "subtopics": 0, "subtopic_links": 0,
             "a3_found": False, "a4_found": False}
    # A chapter with A3 runs on the FINISHED tree is joined at the very end of the build
    # (`apply_tree_structure`), after ids are final. The block-number join below reads A3's
    # per-section numbers as per-page `a2_block_n`, which is what scrambled BIO11L ch01's
    # passages; it must not also run.
    if _tree_inputs(chapter, steps_dir):
        doc["passages"], doc["subtopics"] = [], []
        doc["structure_join"] = {**stats, "deferred_to": "tree"}
        return doc["structure_join"]

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
