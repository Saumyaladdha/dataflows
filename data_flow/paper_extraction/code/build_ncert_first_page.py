#!/usr/bin/env python3
"""Build the NCERT-first Biology page: one solution, NCERT's words, diagrams, old NCERT below.

WHAT CHANGED AND WHY
--------------------
The old card classified a question against an exam taxonomy, printed two solutions, and showed
the NCERT mapping last. A teacher reviewing 2024_S1 and the owner both landed on the same
conclusion from opposite directions, so the order is inverted here: NCERT is extracted first and
everything downstream speaks its vocabulary.

    gone      why this chapter · why this subtopic · subtopic 1 / subtopic 2 (exam taxonomy)
              the publisher's solution as a second block to read
    kept      subject · branch · NCERT chapter · ncert_subtopic · syllabus
    new       ONE solution, written from the NCERT lines, in NCERT's words
              the exact NCERT line quoted as "what NCERT says", so a student can go back to it
              diagrams inside the solution, where the question or the book has one
              the older edition as its own section BELOW the solution, never mixed in

The exam topic-mapping subtopics are NOT deleted from the data -- `classification.
examtopicmapping_subtopics` stays exactly where it was, because the owner intends to map it
properly later. It simply stops being displayed, since showing both invited the confusion the
review kept reporting ("Not an NCERT heading. Should be 'Inheritance of One Gene'").

THE ANSWER COMPARISON SURVIVES, AS ONE LINE
-------------------------------------------
Only one solution is shown, as asked. But the comparison behind it is kept and printed as a
single line, because it is the one check in this pipeline that has proved itself: across 200
questions it flagged exactly the five the teacher flagged by hand -- q040, q125, q147, q157,
q191 -- with no misses and no false alarms, and on q147 and q157 the printed key turned out to
be wrong. A disagreement prints as MARKED FOR REVIEW rather than being resolved silently.

Usage:
    python3 code/build_ncert_first_page.py --paper 2024_S1 --questions q101,q106,q107,q153,q157
    python3 code/build_ncert_first_page.py --paper 2024_S1 --questions ... --apply
"""

import argparse
import collections
import html
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS = os.path.join(os.path.dirname(HERE), "ncert_to_paper_maps")

CSS = """
:root{--ink:#231f20;--rule:#d7e0da;--soft:#f6faf8;--head:#1f4f3a;--warn:#8a5a00;--bad:#8a2318}
*{box-sizing:border-box}
body{margin:0;background:#eef2f0;color:var(--ink);
 font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:900px;margin:0 auto;padding:28px 18px 64px}
h1{font:600 20px/1.3 -apple-system,sans-serif;margin:0 0 4px}
.sub{color:#5a6b63;font-size:13px;margin:0 0 24px}
.q{background:#fff;border:1px solid var(--rule);border-radius:8px;margin:0 0 22px;overflow:hidden}
.qhead{display:flex;align-items:baseline;gap:10px;padding:12px 16px;background:var(--soft);
 border-bottom:1px solid var(--rule)}
.qno{font:700 15px -apple-system,sans-serif;color:var(--head)}
.qsub{font:11px -apple-system,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#5a6b63}
.sy{margin-left:auto;font:700 10px -apple-system,sans-serif;letter-spacing:.05em;
 text-transform:uppercase;padding:3px 9px;border-radius:3px}
.sy-in{background:#d8efdf;color:#13543a}.sy-out{background:#f6d6d2;color:var(--bad)}
.sy-rev{background:#fdecc8;color:#7a5200}
.place{padding:10px 16px;font:13px/1.5 -apple-system,sans-serif;color:#3a4a43;
 background:#fbfdfc;border-bottom:1px solid var(--rule)}
.place b{color:var(--head);font-weight:600}
.stem{padding:16px;font:17px/1.6 Georgia,serif}
.opts{list-style:none;margin:0;padding:0 16px 14px}
.opts li{padding:5px 0 5px 30px;position:relative;font:15px/1.55 Georgia,serif}
.opts li:before{content:"(" attr(data-k) ")";position:absolute;left:0;color:#6b7a73;font-size:13px}
.opts li.right{font-weight:600;color:#13543a}
.opts li.right:after{content:" ✓";color:#13543a}
figure{margin:0;padding:0 16px 14px}
figure img{max-width:100%;border:1px solid var(--rule);border-radius:4px;background:#fff}
figcaption{font:12px -apple-system,sans-serif;color:#6b7a73;margin-top:5px}
.sol{padding:16px;border-top:1px solid var(--rule)}
.sol h4{margin:0 0 10px;font:700 11px -apple-system,sans-serif;letter-spacing:.06em;
 text-transform:uppercase;color:var(--head)}
.says{margin:0 0 12px;padding:11px 13px;background:#fffdf0;border-left:3px solid #e8cf4d;
 border-radius:0 3px 3px 0}
.says .lab{display:block;font:700 10px -apple-system,sans-serif;letter-spacing:.05em;
 text-transform:uppercase;color:#7a5200;margin-bottom:4px}
.says q{font:italic 15px/1.6 Georgia,serif;color:var(--ink)}
.says .src{display:block;margin-top:5px;font:10px ui-monospace,Menlo,monospace;color:#8a7a4a}
.expl{margin:0 0 14px;font:16px/1.7 Georgia,serif}
.wrongs{margin:0;padding:0;list-style:none;border-top:1px solid var(--rule);padding-top:11px}
.wrongs li{padding:4px 0;font:14px/1.55 Georgia,serif;color:#3a4a43}
.wrongs b{color:var(--bad);font-weight:600}
.verdict{margin-top:14px;padding:9px 12px;border-radius:4px;background:#f2f5f3;
 font:13px -apple-system,sans-serif;color:#3a4a43}
.verdict.bad{background:#fdecc8;color:#7a5200;font-weight:600}
.older{border-top:1px solid var(--rule);padding:13px 16px;background:#fffdfa}
.older h4{margin:0 0 8px;font:700 11px -apple-system,sans-serif;letter-spacing:.06em;
 text-transform:uppercase;color:#7a4f28}
.older q{font:italic 14px/1.6 Georgia,serif;color:#3a4a43}
.older .src{display:block;margin:3px 0 9px;font:10px ui-monospace,Menlo,monospace;color:#8a7a6a}
.gone{padding:10px 13px;background:#fdf0ee;border-left:3px solid #d9a69c;border-radius:0 3px 3px 0;
 font:13px/1.55 -apple-system,sans-serif;color:var(--bad)}
.beyond{margin-top:9px;font:12px -apple-system,sans-serif;color:var(--warn)}
"""


def img(url, caption):
    if not url:
        return ""
    return ('<figure><img src="%s" alt="%s" loading="lazy">%s</figure>'
            % (html.escape(url), html.escape(caption),
               ('<figcaption>%s</figcaption>' % html.escape(caption)) if caption else ""))


def figures_for(q):
    """Every diagram worth showing with the solution, in the order a reader wants them."""
    out, qq = [], q.get("question") or {}
    for f in (qq.get("figures") or []):
        u = (((f.get("printed") or {}).get("png") or {}).get("cdn_url"))
        if u:
            out.append((u, f.get("text") or "figure printed with the question"))
    for o in (qq.get("options") or []):
        f = o.get("figure") or {}
        u = (((f.get("printed") or {}).get("png") or {}).get("cdn_url"))
        if u:
            out.append((u, "option %s — %s" % (o.get("key"), f.get("text") or "")))
    for f in ((q.get("solution") or {}).get("figures") or []):
        u = (((f.get("printed") or {}).get("png") or {}).get("cdn_url"))
        if u:
            out.append((u, f.get("text") or "diagram from the printed solution"))
    return out


def card(q, d12, d5):
    qid = q["question_id"].split("__")[-1]
    cls = q.get("classification") or {}
    syl = q.get("syllabus") or {}
    m = q.get("ncert_mapping") or {}
    qq = q.get("question") or {}
    ans = q.get("answer") or {}

    sy = {"in_syllabus": ("In syllabus", "sy-in"), "out_of_syllabus": ("Out of syllabus", "sy-out")}
    face, scls = sy.get(syl.get("label"), ("Needs review", "sy-rev"))

    subs = "; ".join(("%s %s" % (s.get("printed_number") or "", s.get("name") or "")).strip()
                     for s in (m.get("ncert_subtopics") or []))
    chap = "; ".join((m.get("chapter") or {}).get("ncert_chapter_ids") or [])
    place = ('<div class="place"><b>NCERT</b> %s%s%s</div>'
             % (html.escape(chap or "—"),
                (" &middot; <b>%s</b>" % html.escape(subs)) if subs else "",
                (" &middot; %s" % html.escape(cls.get("branch_merged") or "")) if cls.get("branch_merged") else ""))

    right = str(d12.get("answer_is") or ans.get("publisher") or "")
    opts = "".join('<li data-k="%s"%s>%s</li>'
                   % (html.escape(str(o.get("key"))),
                      ' class="right"' if str(o.get("key")) == right else "",
                      html.escape((o.get("text") or "").strip()
                                  or ((o.get("figure") or {}).get("text") or "")))
                   for o in (qq.get("options") or []))

    says = ""
    if d12.get("what_ncert_says"):
        says = ('<div class="says"><span class="lab">What NCERT says</span><q>%s</q>%s</div>'
                % (html.escape(d12["what_ncert_says"]),
                   ('<span class="src">%s</span>' % html.escape(d12.get("what_ncert_says_source") or ""))
                   if d12.get("what_ncert_says_source") else ""))

    wrongs = "".join('<li><b>(%s)</b> %s</li>' % (html.escape(str(w.get("option"))),
                                                  html.escape(str(w.get("why") or "")))
                     for w in (d12.get("why_other_options_fail") or []))

    # the one-line comparison, kept because it is the check that works
    pr, ai, agr = ans.get("publisher"), ans.get("ai"), ans.get("verdict")
    if agr == "agree":
        verdict = ('<div class="verdict">printed answer <b>(%s)</b> &middot; independently solved '
                   '<b>(%s)</b> &middot; they agree</div>' % (html.escape(str(pr)), html.escape(str(ai))))
    else:
        verdict = ('<div class="verdict bad">MARKED FOR REVIEW — printed answer (%s), '
                   'independently solved (%s)%s</div>'
                   % (html.escape(str(pr)), html.escape(str(ai)),
                      (" &middot; " + html.escape(d12["note"])) if d12.get("note") else ""))

    beyond = ""
    if d12.get("terms_beyond_ncert"):
        beyond = ('<div class="beyond">Not NCERT\'s wording: %s</div>'
                  % html.escape("; ".join(str(t) for t in d12["terms_beyond_ncert"])))

    figs = "".join(img(u, c) for u, c in figures_for(q))

    older = ""
    lines = (d5 or {}).get("older") or []
    if lines:
        body = "".join('<q>%s</q><span class="src">%s</span>'
                       % (html.escape(e.get("exact_line") or ""), html.escape(e.get("passage_id") or ""))
                       for e in lines if e.get("exact_line"))
        gone = ""
        if d12.get("rests_on_ncert") == "no":
            gone = ('<div class="gone">The latest NCERT no longer carries this. A student on the '
                    'current syllabus would not meet it.</div>')
        older = '<div class="older"><h4>In the older NCERT</h4>%s%s</div>' % (gone, body)

    return ('<div class="q" id="%s"><div class="qhead"><span class="qno">Q%s</span>'
            '<span class="qsub">%s</span><span class="sy %s">%s</span></div>%s'
            '<div class="stem">%s</div><ul class="opts">%s</ul>%s'
            '<div class="sol"><h4>Solution</h4>%s<p class="expl">%s</p>'
            '<ul class="wrongs">%s</ul>%s%s</div>%s</div>'
            % (qid, qid.lstrip("q").lstrip("0"), html.escape(cls.get("subject") or ""),
               scls, html.escape(face), place,
               html.escape(qq.get("stem") or ""), opts, figs,
               says, html.escape(d12.get("explanation") or ""), wrongs, beyond, verdict, older))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out", default="ncert_first_preview.html")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    year = a.paper.split("_")[0]
    base = os.path.join(HERE, "data", year, a.paper)
    doc = json.load(open(os.path.join(base, "questions.json"), encoding="utf-8"))
    Q = {q["question_id"].split("__")[-1]: q for q in doc["questions"]}

    report = collections.Counter()
    cards = []
    for qid in [x.strip() for x in a.questions.split(",") if x.strip()]:
        q = Q.get(qid)
        if not q:
            report["no such question"] += 1
            continue
        p = os.path.join(MAPS, "steps", "D12", "out", "%s.%s.runA.json" % (a.paper, qid))
        if not os.path.exists(p):
            report["no D12 solution yet"] += 1
            continue
        d12 = json.load(open(p, encoding="utf-8"))
        if d12.get("error"):
            report["D12 reported an error"] += 1
            continue
        p5 = os.path.join(MAPS, "steps", "D5", "out", "%s.%s.runA.json" % (a.paper, qid))
        d5 = json.load(open(p5, encoding="utf-8")) if os.path.exists(p5) else {}
        cards.append(card(q, d12, d5))
        report["rendered"] += 1
        report["with a diagram"] += 1 if figures_for(q) else 0
        report["rests on NCERT: %s" % d12.get("rests_on_ncert")] += 1

    for k, v in sorted(report.items()):
        print("   %-34s %d" % (k, v))
    if not cards:
        print("nothing to render")
        return
    page = ("<!doctype html><meta charset=utf-8>"
            "<meta name=viewport content='width=device-width,initial-scale=1'>"
            "<title>NEET %s · NCERT-first Biology</title><style>%s</style>"
            "<div class=wrap><h1>NEET %s &middot; Biology, NCERT-first</h1>"
            "<p class=sub>Chapter, subtopic and every term come from NCERT. One solution, "
            "written from the book's own lines. The older edition is reported separately.</p>"
            "%s</div>" % (a.paper, CSS, a.paper, "".join(cards)))
    out = os.path.join(base, a.out)
    if not a.apply:
        print("(nothing written -- pass --apply)   would write %s (%.0f KB)"
              % (os.path.relpath(out, HERE), len(page) / 1000))
        return
    open(out, "w", encoding="utf-8").write(page)
    print("wrote %s (%.0f KB)" % (os.path.relpath(out, HERE), len(page) / 1000))


if __name__ == "__main__":
    main()
