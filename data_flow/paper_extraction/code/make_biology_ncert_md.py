#!/usr/bin/env python3
"""Rewrite the Biology sections of `question_paper.md` to match the NCERT-first card.

WHY THIS TRANSFORMS THE MARKDOWN INSTEAD OF REGENERATING IT
-----------------------------------------------------------
`code/paper_md.py` builds the whole file from the v3 records inside `export_paper_v2.py`, and
five of this corpus's papers can no longer be exported -- their source PDFs are not on this
machine. Regenerating would therefore work for some papers and silently skip others. The
markdown is plain text with one `## Q<n>` section per question, so each Biology section is
edited where it stands, exactly as the HTML cards are.

WHAT CHANGES, PER BIOLOGY QUESTION
----------------------------------
    replaced   **Publisher's solution** (our numbering of prose the publisher never numbered)
               **Solved independently** (the second solution)
                    -> one **Solution** block: the NCERT line, what it means, then the
                       reasoning and the per-option refusals

    replaced   **Subtopic:** <coaching subtopic>
                    -> **NCERT:** <chapter title> · <printed subtopic> · **Difficulty:** ...

    added      a line naming the picture D13 chose, when it chose one

Physics and Chemistry sections are not touched.

Usage:
    python3 code/make_biology_ncert_md.py --paper 2024_S1
    python3 code/make_biology_ncert_md.py --paper 2024_S1 --apply
"""

import argparse
import collections
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")

ROMAN = {"9": "IX", "10": "X", "11": "XI", "12": "XII"}


def chapter_name(pages, ch_id):
    for pgno in sorted((pages.get(ch_id) or {}))[:3]:
        for m in re.finditer(r'<div class="blk ct"[^>]*>(.*?)</div>', pages[ch_id][pgno], re.S):
            t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if t and not re.fullmatch(r'(Chapter|Unit)\s*\d+', t, re.I):
                return t.title() if t.isupper() else t
    return ""


def ncert_where(pages, q):
    mp = q.get("ncert_mapping") or {}
    ids = (mp.get("chapter") or {}).get("ncert_chapter_ids") or []
    bits = []
    for cid in ids:
        m = re.match(r'([A-Z]+)(\d+)([LO])-CH(\d+)', cid)
        name = chapter_name(pages, cid)
        if m:
            bits.append("%s (Class %s, Chapter %d)"
                        % (name or cid, ROMAN.get(m.group(2), m.group(2)), int(m.group(4))))
        else:
            bits.append(name or cid)
    subs = "; ".join(("%s %s" % (s.get("printed_number") or "", s.get("name") or "")).strip()
                     for s in (mp.get("ncert_subtopics") or []))
    return " / ".join(bits), subs


def solution_md(q, nf):
    """The one solution, as the card shows it: the line, its meaning, then the reasoning."""
    out = ["**Solution** — answer (%s)" % (nf.get("answer_is") or "—"), ""]
    if nf.get("disagrees_with_printed_key"):
        out += ["> ⚠ **Marked for review.** NCERT supports option %s, but the booklet prints "
                "(%s). %s" % (nf.get("answer_is"),
                              (q.get("answer") or {}).get("publisher") or "—",
                              nf.get("note") or ""), ""]
    if nf.get("what_ncert_says"):
        out += ["> *%s*" % nf["what_ncert_says"].strip()]
        if nf.get("what_ncert_says_source"):
            out += [">", "> — `%s`" % nf["what_ncert_says_source"]]
        out += [""]
    if nf.get("in_short"):
        out += [nf["in_short"].strip(), ""]
    d = nf.get("diagram") or {}
    if d.get("decision") and d["decision"] != "none":
        where = {"annotate": "the printed diagram, with the deciding parts marked",
                 "ncert_figure": "NCERT's own figure for this topic",
                 "draw": "a diagram drawn for this solution"}.get(d["decision"], d["decision"])
        out += ["*Figure on the card: %s.%s*"
                % (where, (" " + d["caption"].strip()) if d.get("caption") else ""), ""]
    if nf.get("explanation"):
        out += ["<details><summary>the full reason, and why each other option fails</summary>",
                "", nf["explanation"].strip(), ""]
        for w in nf.get("why_other_options_fail") or []:
            out.append("- **(%s)** %s" % (w.get("option"), (w.get("why") or "").strip()))
        out += ["", "</details>", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    md = open(os.path.join(base, "question_paper.md"), encoding="utf-8").read()
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))
    pages = json.load(open(os.path.join(MAPS, "maps", "page_html.json"), encoding="utf-8"))

    # every `## Q<n>` section, in order, so each can be rewritten where it stands
    starts = [(int(m.group(1)), m.start()) for m in re.finditer(r'^## Q(\d+)\s*$', md, re.M)]
    bounds = {}
    for i, (n, at) in enumerate(starts):
        bounds[n] = (at, starts[i + 1][1] if i + 1 < len(starts) else len(md))

    report, edits = collections.Counter(), []
    for q in doc["questions"]:
        if ((q.get("classification") or {}).get("subject") or "") != "Biology":
            continue
        report["biology"] += 1
        nf = q.get("ncert_first")
        if not nf:
            report["no ncert_first yet -- section left alone"] += 1
            continue
        qno = q.get("qno") or int(re.sub(r'\D', '', q["question_id"].split("__")[-1]))
        if qno not in bounds:
            report["no `## Q<n>` section found"] += 1
            continue
        lo, hi = bounds[qno]
        sec = md[lo:hi]

        # out: the two old solution blocks, from their heading to the next bold heading
        sec, n1 = re.subn(r"\*\*Publisher's solution\*\*\n\n.*?(?=\n\*\*|\n## |\Z)",
                          "", sec, flags=re.S)
        sec, n2 = re.subn(r"\*\*Solved independently\*\*.*?(?=\n\*\*|\n## |\Z)",
                          "", sec, flags=re.S)
        report["old solution blocks removed"] += n1 + n2

        # in: the one solution, placed where they were -- just after the Answer line
        m = re.search(r'^\*\*Answer\*\* .*$', sec, re.M)
        block = solution_md(q, nf)
        if m:
            sec = sec[:m.end() + 1] + "\n" + block + sec[m.end() + 1:]
            report["NCERT-first solution written"] += 1

        # the subtopic line now names NCERT's chapter and printed subtopic
        where, subs = ncert_where(pages, q)
        sec, n3 = re.subn(r'^\*\*Subtopic:\*\* .*?· (\*\*Difficulty:\*\*.*)$',
                          lambda d: "**NCERT:** %s%s · %s"
                          % (where or "not mapped", (" · " + subs) if subs else "", d.group(1)),
                          sec, count=1, flags=re.M)
        report["subtopic line now NCERT's"] += n3
        edits.append((lo, hi, sec))

    for k, v in sorted(report.items()):
        print("   %-44s %d" % (k, v))
    if not edits:
        print("nothing to change")
        return
    out, last = [], 0
    for lo, hi, sec in sorted(edits):
        out.append(md[last:lo])
        out.append(sec)
        last = hi
    out.append(md[last:])
    new = "".join(out)
    print("   %-44s %.0f KB -> %.0f KB" % ("markdown", len(md) / 1000, len(new) / 1000))
    if not a.apply:
        print("(nothing written -- pass --apply)")
        return
    open(os.path.join(base, "question_paper.md"), "w", encoding="utf-8", newline="\n").write(new)
    print("wrote question_paper.md")


if __name__ == "__main__":
    main()
