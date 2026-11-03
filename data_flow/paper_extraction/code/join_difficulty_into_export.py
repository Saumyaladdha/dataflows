#!/usr/bin/env python3
"""Write the re-rated difficulty into the three deliverables.

    python3 code/join_difficulty_into_export.py --paper 2017_A --apply

WHY A JOINER AND NOT A RE-EXPORT
--------------------------------
`export_paper_v2.py` rebuilds the page from the v2 pipeline, and 2017_A is not in that set -- it
is a finished export, which is the same reason E7V could not see it and the packets had to be
built from the export in the first place. So the difficulty block is replaced in place, the way
the category cards are.

WHAT IT REPLACES
----------------
The whole `<table class="classify">` that begins with a `difficulty` row, matched by its own
opening tag and closed at the first `</table>`. That table is generated as one unit and contains
no nested table, so this cannot run past it -- unlike the card remover that once scanned past a
card it no longer recognised and emptied 29 question blocks.

Band counts in the summary strip are updated too, because a page whose strip says 101 easy while
its questions say 61 is worse than one with no strip at all.
"""

import argparse
import collections
import glob
import html
import json
import os
import re

import runner_core as rc

OUT = ("steps", "E7V", "out")


def ratings(paper_id):
    out = {}
    for p in sorted(glob.glob(rc.pp(*OUT, "%s__q*.runA.json" % paper_id))):
        m = re.search(r"__q(\d{3})\.runA\.json$", p)
        if not m:
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except ValueError:
            continue
        if "error" not in d:
            out[int(m.group(1))] = d
    return out


def _table(r):
    steps = r.get("steps") or []
    n = r.get("steps_to_solve") or 0
    rows = ['<tr><th>difficulty</th><td><b>%s</b>%s</td></tr>'
            % (html.escape(r.get("difficulty") or ""),
               " &middot; %d step%s" % (n, "" if n == 1 else "s") if n else "")]
    rows.append('<tr><th>steps</th><td>%s</td></tr>'
                % (html.escape(" → ".join(steps)) or "<i>none listed</i>"))
    live = r.get("live_options")
    if live:
        keys = [str(k) for k in (r.get("live_option_keys") or [])]
        bits = "<b>%s of 4</b>" % html.escape(str(live))
        if keys:
            bits += " &middot; option%s %s" % ("" if len(keys) == 1 else "s",
                                               html.escape(", ".join(keys)))
        if r.get("long_to_execute"):
            bits += ' &middot; <span class="longexec">long to execute</span>'
        if r.get("why_live"):
            bits += '<div class="livewhy">%s</div>' % html.escape(r["why_live"])
        rows.append('<tr><th>confusing options</th><td>%s</td></tr>' % bits)
    if r.get("why"):
        rows.append('<tr><th>why this band</th><td>%s</td></tr>' % html.escape(r["why"]))
    if r.get("what_makes_it_hard"):
        rows.append('<tr><th>the catch</th><td>%s</td></tr>'
                    % html.escape(r["what_makes_it_hard"]))
    if r.get("note"):
        rows.append('<tr><th>note</th><td>%s</td></tr>' % html.escape(r["note"]))
    return '<table class="classify">%s</table>' % "".join(rows)


CSS = (".livewhy{color:var(--ink2);margin-top:3px;line-height:1.45}"
       ".longexec{color:#8a1c1c;font-weight:600}")


def join(paper_id, apply_=False):
    year = paper_id.split("_")[0]
    base = rc.pp("data", year, paper_id)
    rats = ratings(paper_id)
    print("%s: %d per-question difficulty rating(s)" % (paper_id, len(rats)))
    if not rats:
        raise SystemExit("nothing to join")
    bands = collections.Counter(r.get("difficulty") for r in rats.values())
    print("  bands: %s" % dict(bands))
    if not apply_:
        print("(nothing written -- pass --apply)")
        return rats

    # --- questions.json ---------------------------------------------------------------
    jpath = os.path.join(base, "questions.json")
    doc = json.load(open(jpath, encoding="utf-8"))
    hit = 0
    for row in doc.get("questions") or []:
        r = rats.get(row.get("qno"))
        if not r:
            continue
        row["difficulty"] = {
            "level": r.get("difficulty"), "steps": r.get("steps_to_solve"),
            "step_list": r.get("steps") or [], "why": r.get("why") or "",
            "what_makes_it_hard": r.get("what_makes_it_hard") or None,
            # the second and third spines, recorded beside the band they produced
            "live_options": r.get("live_options"),
            "live_option_keys": r.get("live_option_keys") or [],
            "why_live": r.get("why_live") or "",
            "long_to_execute": bool(r.get("long_to_execute")),
            "confidence": r.get("confidence"), "note": r.get("note") or "",
        }
        row.setdefault("status", {})["difficulty"] = (
            "unsure" if r.get("difficulty") == "unsure" else "done")
        hit += 1
    counts = doc.setdefault("counts", {})
    counts["difficulty"] = {"done": hit}
    for b in ("easy", "medium", "hard", "unsure"):
        counts["difficulty_" + b] = bands.get(b, 0)
    json.dump(doc, open(jpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("  json: %d question(s) updated" % hit)

    # --- question_paper.html ----------------------------------------------------------
    hpath = os.path.join(base, "question_paper.html")
    if os.path.exists(hpath):
        page = open(hpath, encoding="utf-8").read()
        if ".livewhy{" not in page:
            page = page.replace("</style>", CSS + "</style>", 1)
        # Each question block carries exactly one difficulty table; replace the Nth as we walk
        # the blocks in order, so a question with no rating keeps whatever it had.
        done = 0
        for qno in sorted(rats):
            anchor = page.find('<div class="q" id="q%03d"' % qno)
            if anchor == -1:
                continue
            nxt = page.find('<div class="q" id="q%03d"' % (qno + 1))
            end = nxt if nxt != -1 else len(page)
            block = page[anchor:end]
            m = re.search(r'<table class="classify"><tr><th>difficulty</th>.*?</table>',
                          block, re.S)
            if not m:
                continue
            page = page[:anchor] + block[:m.start()] + _table(rats[qno]) + \
                block[m.end():] + page[end:]
            done += 1
        for b in ("easy", "medium", "hard"):
            page = re.sub(r'(<div class="stat"><b>)\d+(</b><span>difficulty %s</span></div>)' % b,
                          lambda mm, n=bands.get(b, 0): "%s%d%s" % (mm.group(1), n, mm.group(2)),
                          page, count=1)
        open(hpath, "w", encoding="utf-8").write(page)
        print("  html: %d difficulty block(s) replaced" % done)

    # --- question_paper.md ------------------------------------------------------------
    mpath = os.path.join(base, "question_paper.md")
    if os.path.exists(mpath):
        md = open(mpath, encoding="utf-8").read()
        # The md prints the band inline on the subtopic line -- `**Difficulty:** easy (1 step)`
        # -- not as a bullet of its own. Walk the question headings so each replacement lands
        # in the right question rather than counting matches.
        done = 0
        for qno in sorted(rats):
            r = rats[qno]
            a = md.find("\n## Q%d\n" % qno)
            if a == -1:
                continue
            b = md.find("\n## Q%d\n" % (qno + 1))
            b = b if b != -1 else len(md)
            block = md[a:b]
            n = r.get("steps_to_solve") or 0
            new_bit = "**Difficulty:** %s (%d step%s" % (r.get("difficulty"), n,
                                                         "" if n == 1 else "s")
            if r.get("live_options"):
                new_bit += ", %d of 4 options live" % r["live_options"]
            new_bit += ")"
            block2, k = re.subn(r"\*\*Difficulty:\*\* [^\n·]*", new_bit, block, count=1)
            if k:
                md = md[:a] + block2 + md[b:]
                done += 1
        open(mpath, "w", encoding="utf-8").write(md)
        print("  md:   %d line(s) updated" % done)
    return rats


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    join(a.paper, a.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
