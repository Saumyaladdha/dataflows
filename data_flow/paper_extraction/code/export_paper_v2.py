#!/usr/bin/env python3
"""Export the v2 corpus as a CSV and as a paper-like HTML, for judging extraction by eye.

    python3 scripts/export_paper_v2.py --csv --html
    python3 scripts/export_paper_v2.py --html --paper-id 2024_Q2

WHY AN HTML THAT LOOKS LIKE THE PAPER
-------------------------------------
A CSV answers "did a row come out". It cannot answer "is this the question that was printed", and
that is the question worth asking: the first corpus scored 87% on a row count while losing a digit
out of a stem (`22000` read as `2200`), which no row count can see. Rebuilding the paper's own
appearance -- question, four options, the official answer, and the figure in place -- puts the
extraction next to the thing it claims to be a copy of.

So each question is rendered with its figure crop inline, and every crop carries the measured
`target_box_in_crop` drawn over it, because a figure crop is grown outward on purpose and a reader
has to see which part the transcriber was told was the subject.

WHAT THE HTML DELIBERATELY SHOWS AS A PROBLEM
---------------------------------------------
Nothing is tidied for presentation. A question whose text draft has fewer than four options, or no
printed answer, or a figure whose crop is suspiciously wide, is marked on the page rather than
quietly rendered as if clean -- the export exists to find those, not to hide them.
"""

import argparse
import re
import collections
import csv
import glob
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import texhtml  # noqa: E402

CORPUS = ("papers_v2",)
#: Where B3V writes the agent's read of each question. When one exists it REPLACES the text draft in
#: every export, because the draft is a cross-check and the agent's read of the image is the record.
B3V_OUT = ("steps", "B3V", "out")
#: Where b6-blind-solver's independent answer lands.
B6V_OUT = ("steps", "B6V", "out")
QSUBJ_OUT = ("steps", "QSUBJ", "out")
QCHAP_OUT = ("steps", "QCHAP", "out")
QTOPIC_OUT = ("steps", "QTOPIC", "out")


def _mapping(out_dir, paper_id, qno):
    path = rc.pp(*out_dir, "%s__q%03d.runA.json" % (paper_id, qno))
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except ValueError:
        return None
    return None if "error" in data else data


def chapter_topic(paper_id, qno):
    """(chapter names, topic names, confidence) from the mapping chain, or empties.

    Reported as names for a reader and as codes in the CSV, because the CODE is what the product
    stores -- two chapters have shared a code in this taxonomy, so a name alone is not an identifier.
    """
    chapter = _mapping(QCHAP_OUT, paper_id, qno) or {}
    topic = _mapping(QTOPIC_OUT, paper_id, qno) or {}
    drop = {"unsure", ""}
    return ([c for c in (chapter.get("chapter_codes") or []) if c not in drop],
            [c for c in (chapter.get("chapter_names") or []) if c.lower() not in drop],
            [t for t in (topic.get("topic_ids") or []) if t not in drop],
            [t for t in (topic.get("topic_names") or []) if t.lower() not in drop],
            chapter.get("confidence") or "")


#: A chapter or topic title quoted inside an agent's note, e.g. "Expected chapter: 'The s-Block
#: Elements' ...". Outputs written before the `proposed_chapter` field existed named the wanted
#: chapter this way, and there are hundreds of them -- worth reading rather than re-running.
NAMED_IN_NOTE = re.compile(r"['\u2018\u201c]([A-Z][^'\u2019\u201d]{3,60})['\u2019\u201d]")


def named_in_note(note):
    """The quoted title an agent named in prose, or "". Only the first: notes that name a wanted
    chapter put it first and any later quotes are the near-miss alternatives it rejected."""
    match = NAMED_IN_NOTE.search(note or "")
    return match.group(1) if match else ""


#: Repeated "<n>. (<d>)" pairs -- the shape of a row of the booklet's PRINTED ANSWER-KEY GRID.
KEY_GRID = re.compile(r"\b\d{1,3}\.\s*\(\s*[1-4]\s*\)")
#: Three pairs is already impossible in a real stem; 2019_P1 q050 carries 138 of them.
KEY_GRID_MIN = 3


def is_key_grid(stem):
    """True when this 'question' is really a row of the answer-key table on the booklet's last page.

    Found by two mapping agents independently, on 2019_P1 q031 and q050: the boundary finder ran off
    the end of the questions and segmented the printed key grid as though it were more questions.
    Both have an empty options object and a stem of nothing but `31. (1) 32. (1) ...`.

    This is worth its own detector rather than a note, because such an item is not a hard question or
    a badly-read one -- it is NOT A QUESTION, and every later step that treats it as one wastes an
    agent call and files a wrong row. It also means the ANSWER KEY is sitting inside the question
    stream, which matters for any step that must not see the key.
    """
    return len(KEY_GRID.findall(stem or "")) >= KEY_GRID_MIN


def taxonomy_gap(paper_id, qno):
    """The chapter or topic the agent WANTED and the taxonomy does not have, or "".

    Without this, a question whose chapter came back `unsure` renders with no chapter chip at all --
    indistinguishable on the page from a question nobody has mapped yet. The two are opposites: one
    is unmapped, the other was mapped carefully and found the vocabulary wanting. Saying which is
    the whole reason the agents were allowed to answer `unsure` in the first place.
    """
    chapter = _mapping(QCHAP_OUT, paper_id, qno) or {}
    topic = _mapping(QTOPIC_OUT, paper_id, qno) or {}
    if chapter.get("chapter_codes") == ["unsure"]:
        wanted = (chapter.get("proposed_chapter") or named_in_note(chapter.get("note"))).strip()
        return ("chapter missing from the taxonomy: %s" % wanted if wanted
                else "no chapter in the taxonomy teaches this")
    if topic.get("topic_ids") == ["unsure"]:
        wanted = (topic.get("proposed_topic") or named_in_note(topic.get("note"))).strip()
        return ("topic missing from the chapter: %s" % wanted if wanted
                else "this chapter has no topic for it")
    return ""


STREAMS = ("papers_v2", "mappings", "chapter_streams.json")
_STREAMS = {}


def _streams():
    """{chapter_code: {stream|branch,...}}, loaded once."""
    if not _STREAMS:
        path = rc.pp(*STREAMS)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            _STREAMS.update(data.get("by_chapter_code") or {})
            _STREAMS["__names__"] = data.get("by_chapter_name") or {}
    return _STREAMS


def stream_and_branch(subject, branch, chapter_codes, chapter_names):
    """(stream, branch) for one question -- the part of the subject a student revises by.

    NEITHER IS IN THE SOURCE TABLE. A full scan of `ExamChapterTopicMappings` carries `subject` as
    physics / chemistry / biology and nothing finer: no physical/inorganic/organic split, and no
    botany/zoology split, even though NEET prints Botany and Zoology as separate sections and
    students revise Chemistry in three streams. So both are DERIVED, and derived at the CHAPTER
    level rather than per question -- "Alcohols, Phenols and Ethers" is organic for every question
    in it, so the judgement is made 59 times instead of 1,869, and is reviewable as one file.

    Branch has a precedence, and it matters: a PRINTED heading wins, because that is a measurement
    of what the paper itself said. Only 2022, 2023 and 2024 print BOTANY and ZOOLOGY; the other
    seven booklets print just BIOLOGY, which is why 1,569 questions had an empty branch. For those,
    the chapter's branch fills in -- and `both` is preserved rather than forced, because cell
    biology and genetics genuinely are taught in both sections.
    """
    table = _streams()
    records = [table.get(code) for code in (chapter_codes or []) if table.get(code)]
    if not records:
        by_name = table.get("__names__") or {}
        records = [by_name[name.lower()] for name in (chapter_names or [])
                   if name.lower() in by_name]
    stream = ""
    if (subject or "").lower() == "chemistry":
        found = [r.get("stream") for r in records if r.get("stream")]
        stream = found[0] if found else ""
    if (subject or "").lower() == "biology" and not branch:
        found = [r.get("branch") for r in records if r.get("branch")]
        branch = found[0] if found else ""
    return stream, branch


def confirmed_subject(paper_id, question):
    """(subject, branch, how) -- the agent's confirmation where there is one, else the paper's.

    A subject read off a printed section heading is a measurement and is never re-judged. A subject
    guessed from the question NUMBER is a fallback with a measured failure rate -- on 2015 Code-A it
    was wrong on every one of the 43 questions an agent has checked so far -- so where
    `q-subject-confirmer` has ruled, its answer replaces the guess and `subject_from` says so.
    """
    how = question.get("subject_from") or ""
    if "printed heading" in how:
        return question.get("subject"), question.get("branch"), how
    path = rc.pp(*QSUBJ_OUT, "%s__q%03d.runA.json" % (paper_id, question["qno"]))
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError:
            data = {}
        if data.get("subject") and data["subject"] != "unsure" and "error" not in data:
            branch = data.get("branch")
            return (data["subject"], None if branch == "unsure" else branch,
                    "confirmed by q-subject-confirmer (position had guessed %s)"
                    % (question.get("subject") or "nothing"))
    return question.get("subject"), question.get("branch"), how

def verdict(official, solved):
    """One word for how the booklet's printed answer and our own solve stand to each other.

    THE BOOKLET'S PRINTED ANSWER IS THE OFFICIAL ANSWER, by the owner's decision of 2026-10-21 and
    on measured evidence. The separately published NTA key PDFs were joined in until now and have
    been removed from the flow entirely. NEET prints the same questions in ~24 booklet codes with
    the options rotated, so a key is only meaningful against the code it was published for -- and
    the PDFs for 2016, 2017 and 2022 carry no code heading to join on. Joining them anyway
    disagreed with the printed answer on 71%, 74% and 78% of questions: not a finding, just a
    wrong join that looked authoritative. A source that is silently wrong is worse than no source.

    That leaves two answers that fail differently: the booklet's, which is what the paper itself
    declares, and the solve, which has seen neither the booklet nor any key. A disagreement is a
    question worth a person's time rather than an error to reconcile.
    """
    if not (official and solved):
        return "unchecked"
    if official == solved:
        return "agree"
    if solved == "unsure":
        return "solve was unsure"
    return "solved differs from official"


def solved_answer(paper_id, qno):
    """b6-blind-solver's own answer for this question, or (None, None, None).

    Returned with its confidence and reasoning, because a disagreement is only worth a reader's
    time when they can see what the solver actually argued.
    """
    path = rc.pp(*B6V_OUT, "%s__q%03d.runA.json" % (paper_id, qno))
    if not os.path.exists(path):
        return None, None, None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "error" in data:
        return None, None, None
    return data.get("answer"), data.get("confidence"), data.get("reason")


def agent_read(paper_id, qno):
    """b3-question-reader's read of one question, or None if B3V has not reached it yet."""
    path = rc.pp(*B3V_OUT, "%s__q%03d.runA.json" % (paper_id, qno))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return None if "error" in data else data


def reading(paper_id, question):
    """(source, stem, options, answer) -- the agent's read where there is one, else the draft.

    The distinction is carried into the output rather than resolved silently: a reader has to know
    whether a row came from the image or from a text layer that cannot represent fractions.
    """
    draft = question["text_layer_draft"]
    read = agent_read(paper_id, question["qno"])
    if read:
        return ("agent", read.get("stem_en") or "", read.get("options_en") or {},
                draft.get("official_answer"))
    return ("draft", draft.get("stem") or "", draft.get("options") or {},
            draft.get("official_answer"))


def load(paper_id=None):
    out = []
    for path in sorted(glob.glob(rc.pp(*CORPUS, "papers", "*.json"))):
        if paper_id and os.path.basename(path) != "%s.json" % paper_id:
            continue
        with open(path, encoding="utf-8") as fh:
            out.append(json.load(fh))
    return out


def write_csv(papers, out_path):
    """One row per question. Flat, so it can be sorted and filtered without a tool.

    Written per booklet AND as one combined file. Per booklet because that is the unit a person
    checks against a printed paper -- a 1,869-row file mixing ten booklets cannot be read beside
    one paper -- and combined because that is the unit a script counts.
    """
    fields = ["paper_id", "year", "booklet_code", "qno", "page", "stem", "option_1", "option_2",
              "option_3", "option_4",
              # THE THREE ANSWERS, never collapsed into one column: the publisher's, NTA's own, and
              # an independent solve that saw neither. See verdict() for why that matters.
              "subject", "stream", "branch", "subject_from",
              "chapter_codes", "chapter_names", "topic_ids", "topic_names", "chapter_confidence",
              "answer_official", "answer_solved", "answer_verdict",
              "solved_confidence", "answer_starred", "n_options",
              "n_figures", "figure_roles", "figure_source", "figure_folder", "figure_files",
              "text_layer_reliable", "needs_image_read", "read_from", "question_image",
              "source_pdf"]
    rows = 0
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for paper in papers:
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            for q in paper["questions"]:
                draft = q["text_layer_draft"]
                source, stem_text, options, booklet_ans = reading(paper_id, q)
                solved, confidence, _why = solved_answer(paper_id, q["qno"])
                writer.writerow({
                    "paper_id": paper_id, "year": q["year"], "booklet_code": q["booklet_code"],
                    "qno": q["qno"], "page": q["page"], "stem": stem_text,
                    "option_1": options.get("1", ""), "option_2": options.get("2", ""),
                    "option_3": options.get("3", ""), "option_4": options.get("4", ""),
                    "chapter_codes": "; ".join(chapter_topic(paper_id, q["qno"])[0]),
                    "chapter_names": "; ".join(chapter_topic(paper_id, q["qno"])[1]),
                    "topic_ids": "; ".join(chapter_topic(paper_id, q["qno"])[2]),
                    "topic_names": "; ".join(chapter_topic(paper_id, q["qno"])[3]),
                    "chapter_confidence": chapter_topic(paper_id, q["qno"])[4],
                    "subject": (confirmed_subject(paper_id, q)[0] or ""),
                    "stream": stream_and_branch(
                        confirmed_subject(paper_id, q)[0],
                        confirmed_subject(paper_id, q)[1],
                        chapter_topic(paper_id, q["qno"])[0],
                        chapter_topic(paper_id, q["qno"])[1])[0],
                    "branch": stream_and_branch(
                        confirmed_subject(paper_id, q)[0],
                        confirmed_subject(paper_id, q)[1],
                        chapter_topic(paper_id, q["qno"])[0],
                        chapter_topic(paper_id, q["qno"])[1])[1] or "",
                    "subject_from": confirmed_subject(paper_id, q)[2],
                    "answer_official": booklet_ans or "",
                    "answer_solved": solved or "",
                    "answer_verdict": verdict(booklet_ans, solved),
                    "solved_confidence": confidence or "",
                    "answer_starred": "yes" if draft["answer_starred"] else "",
                    "n_options": len(options), "n_figures": len(q["figures"]),
                    "figure_roles": "; ".join(f["role"] for f in q["figures"]),
                    "figure_source": ("agent" if q.get("agent_figure_images")
                                      else ("geometry" if q.get("figure_images") else "")),
                    "figure_folder": (os.path.dirname((q.get("agent_figure_images")
                                                       or q.get("figure_images") or [""])[0])
                                      or ""),
                    "figure_files": "; ".join(q.get("agent_figure_images")
                                              or q.get("figure_images") or []),
                    "text_layer_reliable": ("yes" if q.get("text_layer_reliable", True) else "no"),
                    "needs_image_read": ("yes" if q.get("needs_image_read") else ""),
                    "read_from": source,
                    "question_image": q["question_image"], "source_pdf": q["source_pdf"],
                })
                rows += 1
    return rows


#: WAS a CDN KaTeX bundle. Removed: the page is read as a local file in an editor preview, where
#: external scripts are blocked, so every formula showed as literal `$\frac{4}{9}$` source -- harder
#: to read than either rendered maths or plain text. The LaTeX is now rendered at export time by
#: scripts/lib/texhtml.py, so the page needs nothing but itself.
KATEX_REMOVED = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
  if (!window.renderMathInElement) return;
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "$", right: "$", display: false},
      {left: "\\(", right: "\\)", display: false},
      {left: "\\[", right: "\\]", display: true}
    ],
    // A stray dollar in prose must not blank the rest of the page.
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  });
});
</script>
"""

PART_CSS = """
.opts.pics li{margin:.4em 0}
.optimg{max-width:min(100%,22em);height:auto;display:block;
 border:1px solid color-mix(in srgb,currentColor 12%,transparent);border-radius:4px}
.labelrow{margin:.12em 0}
.concept{font-style:italic}
.axis{display:inline-block;font-family:ui-monospace,monospace;font-weight:700;\n padding:0 .3em;border-radius:3px;border:1px solid currentColor;margin-right:.35em;\n font-size:.92em;letter-spacing:0}\n.classify th .means{display:block;text-transform:none;letter-spacing:0;font-weight:400;\n opacity:.6;font-size:.95em;max-width:14em;white-space:normal}
.label{font-family:ui-monospace,monospace;font-size:.92em;font-weight:600}
.means{display:block;opacity:.72;font-size:.95em;line-height:1.35}
.means.undefined{color:#b33;font-style:italic}
.because{display:block;font-size:.95em;line-height:1.35;margin-top:.1em}
.cats{display:grid;grid-template-columns:repeat(auto-fit,minmax(19em,1fr));gap:.6em;
 margin:.7em 0 .2em 0}
.axis-card.wide{grid-column:1/-1}
.axis-card{border:1px solid color-mix(in srgb,currentColor 14%,transparent);border-radius:7px;
 padding:.5em .65em;min-width:0}
.axis-card header{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4em;margin-bottom:.35em}
.axis-name{font-weight:650;font-size:.93em}
.axis-means{flex-basis:100%;opacity:.5;font-size:.84em;line-height:1.3}
.axis-body .labelrow+.labelrow{margin-top:.45em;padding-top:.45em;
 border-top:1px dashed color-mix(in srgb,currentColor 12%,transparent)}
.opt{display:inline-block;font-size:.78em;font-weight:700;letter-spacing:.04em;opacity:.65;
 margin-right:.4em;text-transform:uppercase}
.means b,.because b{display:inline-block;font-size:.74em;font-weight:700;letter-spacing:.07em;
 text-transform:uppercase;opacity:.5;margin-right:.35em}
.because{opacity:.95;margin-top:.3em}
.classify{border-collapse:collapse;margin:.3em 0 .7em 0;font-size:.86em}
.classify th{text-align:left;font-weight:600;letter-spacing:.06em;text-transform:uppercase;
 opacity:.55;padding:.1em 1.1em .1em 0;white-space:nowrap;vertical-align:top;font-size:.88em}
.classify td{padding:.1em 0;vertical-align:top}
.classify tr.unset td{opacity:.6;font-style:italic}\n.classify tr.reason th{opacity:.38}\n.classify tr.reason td{opacity:.8;max-width:54em;font-size:.97em}
.chip.gap{border-style:dashed;opacity:.85}
.stmts,.match{border-collapse:collapse;margin:.6em 0;width:100%;font-size:.95em}
.stmts td,.match td{border:1px solid currentColor;padding:.26em .5em;vertical-align:top}
.stmts td,.match td{border-color:color-mix(in srgb,currentColor 22%,transparent)}
.stmts .lbl,.match .lbl{white-space:nowrap;text-align:center;width:1%;opacity:.8}
.part{display:flex;gap:.55em;align-items:flex-start;margin:.45em 0}
.partlet{font-weight:600;min-width:1.1em;opacity:.75}
.partbody{flex:1;min-width:0}
figure.part{margin:0 0 .3em 0}
figure.part img{max-width:100%;height:auto}
"""


CSS = """
/* FOUR OF THESE WERE MISSING AND THREE RULES SILENTLY DID NOTHING (found 2026-10-21).
   `--defect`, `--defect-soft`, `--accent-soft` and `--accent-ink` were referenced below but
   declared nowhere, so `table.answers.mismatch` -- the band that marks a question where the blind
   solve DISAGREES with the booklet's printed answer -- rendered with no background and no colour,
   on every paper page since the export was written. A disagreement is the single most important
   thing this page can tell a reader, and it was being shown as an ordinary row. */
:root{--paper:#fbfaf7;--ink:#1a1a1a;--ink2:#555;--rule:#d9d6cf;--accent:#8a1c1c;
 --accent-soft:#f6eaea;--accent-ink:#6d1616;
 --defect:#9a2525;--defect-soft:#fbeeee;
 --warn:#8a5a00;--warn-bg:#fdf5e3;--ok:#1d6b3f;--card:#fff;}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#15150f;--ink:#ece9e1;
 --ink2:#a39f95;--rule:#363329;--accent:#e08b8b;--accent-soft:#2c1a1a;--accent-ink:#f0c9c9;
 --defect:#f0a0a0;--defect-soft:#2e1818;
 --warn:#e0b45c;--warn-bg:#2a2113;--ok:#7fcf9f;--card:#1d1c15;}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font:15px/1.55 "Iowan Old Style",Palatino,Georgia,serif;}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:22px;margin:0 0 4px;letter-spacing:.01em}
.sub{color:var(--ink2);font-size:13px;margin-bottom:22px}
.stats{display:flex;flex-wrap:wrap;gap:14px;margin:0 0 26px;padding:12px 14px;
 background:var(--card);border:1px solid var(--rule);border-radius:7px}
.stat b{display:block;font-size:19px;font-variant-numeric:tabular-nums}
.stat span{font-size:11px;color:var(--ink2);text-transform:uppercase;letter-spacing:.06em}
.q{background:var(--card);border:1px solid var(--rule);border-radius:7px;
 padding:16px 18px;margin:0 0 16px}
.qno{float:left;font-weight:700;margin-right:10px;color:var(--accent);
 font-variant-numeric:tabular-nums}
.stem{margin:0 0 12px}
ol.opts{list-style:none;margin:0;padding:0}
ol.opts li{padding:3px 0 3px 30px;position:relative}
ol.opts li:before{content:"(" counter(o) ")";counter-increment:o;position:absolute;left:0;
 color:var(--ink2);font-variant-numeric:tabular-nums}
ol.opts{counter-reset:o}
ol.opts li.key{color:var(--ok);font-weight:600}
ol.opts li.key:after{content:" \\2190 printed answer";font-size:11px;font-weight:400;color:var(--ok)}
figure{margin:12px 0;padding:0}
figure img{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:4px;
 background:#fff;display:block}
figcaption{font-size:11px;color:var(--ink2);margin-top:4px;letter-spacing:.03em}
.flag{display:inline-block;font-size:11px;padding:1px 7px;border-radius:99px;
 background:var(--warn-bg);color:var(--warn);border:1px solid var(--warn);margin-left:6px}
.meta{font-size:11px;color:var(--ink2);margin-top:10px;border-top:1px dashed var(--rule);
 padding-top:7px}
a{color:var(--accent)}
.qhead{margin-bottom:10px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start}
@media (max-width:760px){.pair{grid-template-columns:1fr}}
.side{min-width:0}
.sidelabel{font-size:10px;text-transform:uppercase;letter-spacing:.09em;color:var(--ink2);
 border-bottom:1px solid var(--rule);padding-bottom:4px;margin-bottom:9px}
img.shot{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:4px;background:#fff;
 display:block}
.missing{font-size:12px;color:var(--warn);margin:0}
table.answers{border-collapse:collapse;margin:12px 0 0;font-size:12px;width:100%}
table.answers th{font-size:9.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink2);
 font-weight:500;text-align:left;padding:3px 9px 3px 0;border-bottom:1px solid var(--rule)}
table.answers td{padding:5px 9px 5px 0;font-weight:700;font-size:15px;
 font-variant-numeric:tabular-nums}
table.answers td:last-child{font-weight:400;font-size:11.5px;color:var(--ink2)}
table.answers.mismatch td:last-child{color:var(--defect);font-weight:600}
table.answers.mismatch{background:var(--defect-soft);border-radius:5px}
table.answers.mismatch th,table.answers.mismatch td{padding-left:9px}
.subj{display:inline-block;font-size:10px;text-transform:uppercase;letter-spacing:.07em;
 padding:2px 8px;border-radius:99px;background:var(--accent-soft);color:var(--accent-ink);
 border:1px solid var(--rule);margin-right:6px;cursor:help}
.chip{display:inline-block;font-size:10px;letter-spacing:.04em;padding:2px 8px;border-radius:99px;
 background:var(--card);color:var(--ink2);border:1px solid var(--rule);margin-right:5px}
.chip.topic{background:var(--warn-bg);color:var(--warn);border-color:var(--warn)}
.conf{font-size:10px;font-weight:400;color:var(--ink2);text-transform:uppercase}
.why{font-size:11.5px;color:var(--defect);margin:6px 0 0;line-height:1.45}
.pictopts{font-size:13px;color:var(--ink2);background:var(--warn-bg);border:1px solid var(--rule);
 border-radius:5px;padding:8px 11px;margin:10px 0 0}
""" + texhtml.CSS + PART_CSS + """
"""


#: An option whose printed content is a PICTURE, written by the agent as a bracketed placeholder
#: because there is no text to copy. Listing four of these as "(1) [structure diagram]" tells a
#: reader nothing the image does not tell them better, so the image is shown in their place.
PICTURE_OPTION = re.compile(
    r"^[\[(]\s*(?:structure|reaction|graph|diagram|figure|circuit|image|picture|plot|"
    r"chemical structure|skeletal)[^\])]*[\])]$", re.I)


#: A labelled part inside a stem: `a.` / `b)` at a line start or after whitespace.
PART_MARKER = re.compile(r"(?:(?<=\s)|^)([a-d])[.)]\s*")


def split_parts(stem, figure_count):
    """Split a stem into its lettered parts, saying which parts are DRAWN rather than written.

    Papers that ask "for the following reactions: a. ... b. ... c. ..." draw two of the three as
    structures. The text layer then shows the written part and runs the drawn ones together as
    `b. c.`, because the drawing contributes no characters -- which is exactly how question 5 of
    2016 Code X reads today. Returning the parts lets the export put each figure back under the
    letter it belongs to instead of stacking unlabelled images below the stem.

    Returns (lead, [(letter, text, is_drawn)], closing) or None when there are no parts to split.
    """
    marks = list(PART_MARKER.finditer(stem))
    if len(marks) < 2 or figure_count < 1:
        return None
    letters = [m.group(1) for m in marks]
    if letters != sorted(set(letters)) or letters[0] != "a":
        return None                      # out of order or not starting at a: not a part list
    lead = stem[:marks[0].start()].strip()
    parts, closing = [], ""
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(stem)
        parts.append([mark.group(1), stem[mark.end():end].strip(), False])
    for part in parts:
        part[2] = not part[1]            # a part with no text of its own is a drawing
    # A trailing part that still carries text, where a figure is waiting for it, is the common
    # flattening: the closing sentence got glued onto the last drawn part. Only move it when the
    # figure count actually demands another drawn part, so a genuine written part is never stolen.
    while sum(1 for _, _, drawn in parts if drawn) < figure_count:
        movable = [part for part in parts if not part[2] and part[1]]
        if not movable or movable[-1] is not parts[-1]:
            break
        closing, parts[-1][1], parts[-1][2] = parts[-1][1], "", True
    return (lead, [tuple(part) for part in parts], closing)


#: A row whose content is DRAWN rather than written. `b3-question-reader` marks these explicitly --
#: "[drawn structural reaction: ... -- see figure]" -- because a reaction scheme has no text form.
DRAWN_ROW = re.compile(r"\[(?:drawn|structure|diagram|reaction scheme)[^\]]*\]|see figure", re.I)


def lists_html(read, figures=None):
    """The statement list and the two match-columns, as HTML tables rather than a cropped picture.

    b3-question-reader already reads these into `statements`, `list_i` and `list_ii` -- structured,
    with every cell's own LaTeX -- and the export used to drop all three on the floor and fall back
    to showing a crop of the printed table. A picture of a table cannot be searched, cannot be
    re-flowed on a narrow screen, and cannot be checked against the options. So the structure the
    agent recovered is rendered, and the crop stops being the only way to read the question.

    Returns "" when the question has none, so a plain question is unaffected.
    """
    out = []
    spare = list(figures or [])
    statements = read.get("statements") or []
    if statements:
        cells = []
        for item in statements:
            text = item.get("text") or ""
            body = texhtml.to_html(text)
            # THE FIGURE GOES IN ITS OWN ROW. Parts b and c of 2016_X q005 ARE two drawn reactions,
            # and the agent says so in the row text. Appending the figures below the table instead
            # left the reader matching a strip of drawings to letters by position -- and position is
            # exactly what a lettered list exists to stop anyone having to do.
            if DRAWN_ROW.search(text) and spare:
                body = '<figure class="part">%s</figure>' % spare.pop(0)
            cells.append('<tr><td class="lbl">%s</td><td>%s</td></tr>'
                         % (texhtml.to_html(item.get("label") or ""), body))
        rows = "".join(cells)
        # One statement per ROW, never run together: "Statement I ... Statement II ..." on a single
        # line is the single most common way these questions become unreadable.
        out.append('<table class="stmts">%s</table>' % rows)
    first, second = read.get("list_i") or [], read.get("list_ii") or []
    if first or second:
        head = ""
        rows = []
        for index in range(max(len(first), len(second))):
            left = first[index] if index < len(first) else {}
            right = second[index] if index < len(second) else {}
            rows.append('<tr><td class="lbl">%s</td><td>%s</td>'
                        '<td class="lbl">%s</td><td>%s</td></tr>'
                        % (texhtml.to_html(left.get("label") or ""),
                           texhtml.to_html(left.get("text") or ""),
                           texhtml.to_html(right.get("label") or ""),
                           texhtml.to_html(right.get("text") or "")))
        out.append('<table class="match">%s%s</table>' % (head, "".join(rows)))
    return "".join(out)


def mapping_reasons(paper_id, qno):
    """(why this chapter, why this subtopic) -- the agents' own one-line reasons.

    Both steps require a `why` naming THE FACT THE CORRECT ANSWER DEPENDS ON, not what the stem
    mentions: a question whose stem describes a circuit but whose answer turns on Ohm's law belongs
    to the chapter that teaches Ohm's law. That sentence is the whole justification for the
    assignment, and the export was writing it to disk and then dropping it. A reader who doubts a
    chapter needs the reason to disagree WITH; without it the only choices are to accept the label
    or re-derive the mapping from scratch.
    """
    chapter = _mapping(QCHAP_OUT, paper_id, qno) or {}
    topic = _mapping(QTOPIC_OUT, paper_id, qno) or {}
    return (chapter.get("why") or "", topic.get("why") or "")


def classification_html(subject, stream, branch, chap_names, topic_names, confidence, gap,
                        chapter_why="", topic_why=""):
    """The question's classification, with every field LABELLED.

    This replaced a row of bare chips. Chips look tidy and are useless to the person who has to
    check the work: `Aldehydes, Ketones and Carboxylic Acids` beside `Nucleophilic Addition
    Reactions` gives no way to tell which is the chapter and which the subtopic, and a reviewer
    cannot confirm an assignment they cannot name. Each row says what it is, and a field that was
    not assigned says so rather than vanishing -- an absent row and an empty row look the same on a
    page, but they mean opposite things.

    Subtopics are numbered because two are allowed and their ORDER is meaningful: the first is the
    topic the answer turns on, the second is a genuine second home, not a synonym.
    """
    rows = []

    def add(label, value, css="", extra=""):
        """`extra` is trusted HTML built here; `value` is always escaped. Keeping them apart stops
        the confidence span being printed as literal markup, which is what happened when the test
        was 'does the value happen to start with a tag'."""
        rows.append('<tr class="%s"><th>%s</th><td>%s%s</td></tr>'
                    % (css, html.escape(label), html.escape(value), extra))

    add("subject", subject or "not assigned")
    if (subject or "").lower() == "chemistry":
        add("stream", stream or "not assigned (chapter unmapped)")
    if (subject or "").lower() == "biology":
        add("branch", branch or "not assigned (chapter unmapped)")
    if chap_names:
        add("chapter", "; ".join(chap_names),
            extra=(' <span class="conf">%s confidence</span>' % html.escape(confidence)
                   if confidence else ""))
        # The reason gets its OWN labelled row rather than sitting inside the chapter's. A reason
        # tucked under the value it justifies reads as a continuation of that value; as its own row
        # it is scannable -- someone checking fifty questions can run down the reasons alone.
        if chapter_why:
            add("why this chapter", chapter_why, "reason")
    else:
        add("chapter", gap or "not mapped yet", "unset")
    for index, name in enumerate(topic_names or [], start=1):
        add("subtopic %d" % index, name)
    # One reason after both ids: QTOPIC gives a single `why` for its choice, and repeating it under
    # each id would imply each was argued for separately.
    if topic_why:
        add("why this subtopic", topic_why, "reason")
    if not topic_names:
        add("subtopic", "not mapped yet" if chap_names else "blocked: needs a chapter first",
            "unset")
    return '<table class="classify">%s</table>' % "".join(rows)


#: `(a)`/`(b)`... and `(i)`/`(ii)`... as they appear in a flattened match-list stem.
MATCH_LETTER = re.compile(r"\((?P<label>[a-dA-D])\)\s*")
MATCH_ROMAN = re.compile(r"\((?P<label>[ivxIVX]{1,4})\)\s*")
#: Phrases a match stem puts around the table, which are not part of any row.
#: Everything before the first `(a)`: the instruction plus the printed column HEADINGS, which are
#: themselves bracketed -- "Match List-I with List-II List-I List-II (Electromagnetic waves)
#: (Wavelength)". An earlier version capped this at 60 non-dot characters and matched nothing,
#: because the headings alone run past that.
MATCH_LEAD = re.compile(r"^(.*?Match\b.{0,160}?)(?=\((?:[a-dA-D])\)\s)", re.S)
MATCH_TAIL = re.compile(r"(Choose\s+the\s+correct\s+answer.*|Select\s+the\s+correct.*)$", re.S | re.I)


def parse_match_lists(stem):
    """Recover List-I / List-II from a FLATTENED stem, or None.

    `b3-question-reader` reads these as structured `list_i` / `list_ii`, but nine of the ten
    booklets have no image read yet, and their text layer flattens the whole printed table into one
    sentence -- `... (a) AM radio waves (i) 10^{-10} m (b) Microwaves (ii) 10^{2} m ...`. Shown as
    prose that is unreadable, and showing a CROP of the table instead means the content cannot be
    searched, re-flowed, or checked against the options.

    The printed table interleaves the columns row by row, so the flattened text alternates
    letter-marker, text, roman-marker, text. That alternation is the signal, and it is why this is
    parsed rather than guessed: a stem that does not alternate is not a match list and returns None.

    Returns (lead, [(letter, left, roman, right)], tail).
    """
    if not stem or "atch" not in stem:
        return None
    tail = ""
    tail_match = MATCH_TAIL.search(stem)
    if tail_match:
        tail = tail_match.group(1).strip()
        stem = stem[:tail_match.start()]
    lead_match = MATCH_LEAD.match(stem)
    if not lead_match:
        return None
    lead, rest = lead_match.group(1).strip(), stem[lead_match.end(1):]

    # Walk the markers in the order they appear; a row is one letter followed by one roman.
    marks = []
    for pattern, kind in ((MATCH_LETTER, "letter"), (MATCH_ROMAN, "roman")):
        for found in pattern.finditer(rest):
            marks.append((found.start(), found.end(), kind, found.group("label")))
    marks.sort()
    # A roman numeral is also a letter in brackets -- `(i)` matches both patterns. Keep the ROMAN
    # reading when both matched the same position, since a match list labels its first column a-d.
    deduped = []
    for mark in marks:
        if deduped and deduped[-1][0] == mark[0]:
            if mark[2] == "roman":
                deduped[-1] = mark
            continue
        deduped.append(mark)
    rows, index = [], 0
    while index + 1 < len(deduped):
        left, right = deduped[index], deduped[index + 1]
        if left[2] != "letter" or right[2] != "roman":
            return None                  # not the alternation a match list produces
        end = deduped[index + 2][0] if index + 2 < len(deduped) else len(rest)
        rows.append((left[3], rest[left[1]:right[0]].strip(), right[3],
                     rest[right[1]:end].strip()))
        index += 2
    if len(rows) < 3:
        return None                      # two rows is not a table worth rebuilding
    return (lead, rows, tail)


def match_table_html(parsed):
    """The recovered table, rendered with each cell's own LaTeX."""
    lead, rows, tail = parsed
    body = "".join('<tr><td class="lbl">(%s)</td><td>%s</td>'
                   '<td class="lbl">(%s)</td><td>%s</td></tr>'
                   % (html.escape(letter), texhtml.to_html(left),
                      html.escape(roman), texhtml.to_html(right))
                   for letter, left, roman, right in rows)
    return ("%s<table class=\"match\">%s</table>%s"
            % ('<p>%s</p>' % texhtml.to_html(lead) if lead else "",
               body, '<p>%s</p>' % texhtml.to_html(tail) if tail else ""))


GLOSSARY = ("papers_v2", "mappings", "label_glossary.json")
E7V_OUT = ("steps", "E7V", "out")
ECAT_OUT = ("steps", "ECAT", "out")
#: Ratings moved out of the live directory so their trap routes could be rewritten.
#: Read by the export as a fallback, never by the agents -- see categories_of().
RERATING = ("legacy", "retired_2026-10-21", "ecat_refute_only")
_GLOSSARY = {}


_AXES = {}


def glossary():
    """{label: {axis, means, requires}} parsed from the rulebook by build_label_glossary.py."""
    if not _GLOSSARY:
        path = rc.pp(*GLOSSARY)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            _GLOSSARY.update(data.get("labels") or {})
            _AXES.update(data.get("axes") or {})
    return _GLOSSARY


def axis_label(axis, fallback):
    """"E1 · Question type — the shape on the page", from the rulebook's own heading.

    The axis codes are not self-explanatory and never will be: E1 through E5 mean nothing to someone
    reading a paper for the first time. The rulebook names each axis and says in one phrase what it
    decides, so both are carried onto the page instead of leaving a bare `E4`.
    """
    glossary()
    entry = _AXES.get(axis) or {}
    name, means = entry.get("name") or fallback, entry.get("means") or ""
    return ('<span class="axis">%s</span> %s%s'
            % (html.escape(axis), html.escape(name),
               ' <span class="means">%s</span>' % html.escape(means) if means else ""))


def free_text_html(value):
    """A field that is prose, not a label from a closed list.

    `concept` names the actual concept a question turns on -- "Electron configuration of gadolinium:
    ten electrons beyond [Xe] placed as 6s2 5d1 4f7". It is deliberately open: the rulebook pairs it
    with `content_shape` because the broad label alone is not revisable. Running it through the
    glossary printed "no definition in the rulebook" under every one of them, which reads as a defect
    in the data when it is a defect in the lookup.
    """
    # RENDERED, not merely escaped. Stopping the glossary lookup here was right -- concept is prose,
    # so "not defined in the rulebook" under every one was a lookup defect -- but it also dropped the
    # maths rendering, and a concept names compounds and quantities constantly:
    # "$\mathrm{O_2^{+}}$ 2.5" was printing as its own source.
    return '<span class="concept">%s</span>' % texhtml.to_html(value)


def label_html(value, reason=""):
    """One classification label: the label, what the rulebook says it means, and why it is here.

    A label on its own is a code, not a classification. `format_reflex_option` tells a reader nothing
    unless the page also says what that is, and nothing about THIS question unless the rater's own
    reason sits beside it. Both are shown, because a reviewer checking the work needs the rule and
    the application of it in the same place -- looking the rule up in another file is how tags stop
    being checked at all.

    The definition comes from the rulebook and is never retyped here: a gloss that has drifted from
    the rule is worse than none, since the reader then checks the work against the wrong rule.
    """
    entry = glossary().get(value) or {}
    means = entry.get("means") or ""
    out = ['<span class="label">%s</span>' % html.escape(value)]
    # THE TWO LINES ARE LABELLED, because they answer different questions and ran together without
    # it. The first is the RULE, identical on every question carrying this label; the second is why
    # THIS question carries it. A reader who cannot tell them apart cannot check either one -- is
    # the definition wrong, or is this application of it wrong?
    if means:
        out.append('<span class="means"><b>means</b> %s</span>' % texhtml.to_html(means))
    # NOTHING is printed when the rulebook has no definition. It used to say so in red, on the
    # reasoning that an undefined label is a gap worth seeing -- but the gap is in the RULEBOOK, not
    # in this question, and a red line under four of the five `strategy_available` values on dozens
    # of questions tells a reader checking those questions nothing they can act on. The gap is
    # reported once, where it can be fixed: build_label_glossary.py prints it, and
    # docs/OPEN_QUESTIONS.md records it.
    if reason:
        # Routed through the renderer, not escaped raw: a trap route is full of `m/s^2` and `10^{-2}`
        # written the way the rater typed them.
        out.append('<span class="because"><b>why here</b> %s</span>'
                   % texhtml.to_html(str(reason)))
    return '<div class="labelrow">%s</div>' % "".join(out)


def free_text_html(value):
    """A field that is prose, not a label from a closed list.

    `concept` names the actual concept a question turns on. It is deliberately open: the rulebook
    pairs it with `content_shape` because the broad label alone is not revisable. Running it through
    the glossary printed "not defined in the rulebook" under every one, which reads as a defect in
    the data when it is a defect in the lookup.
    """
    # RENDERED, not merely escaped. Stopping the glossary lookup here was right -- concept is prose,
    # so "not defined in the rulebook" under every one was a lookup defect -- but it also dropped the
    # maths rendering, and a concept names compounds and quantities constantly:
    # "$\mathrm{O_2^{+}}$ 2.5" was printing as its own source.
    return '<span class="concept">%s</span>' % texhtml.to_html(value)


def axis_card(axis, fallback, body, wide=False):
    """One axis as its own card: the code, its name, and what it decides.

    E1 through E5 mean nothing to someone reading a paper for the first time, and a flat table of
    rows mixed label, definition and reason into one column until none of them could be scanned.
    Each axis now owns a block, headed by its rulebook name and the phrase that says what it is for.
    """
    glossary()
    entry = _AXES.get(axis) or {}
    return ('<section class="axis-card%s">' % (" wide" if wide else "") +
            '<header><span class="axis">%s</span><span class="axis-name">%s</span>'
            '<span class="axis-means">%s</span></header><div class="axis-body">%s</div>'
            '</section>'
            % (html.escape(axis), html.escape(entry.get("name") or fallback),
               html.escape(entry.get("means") or ""), body))


def difficulty_of(paper_id, qno):
    """(band, steps_to_solve, steps, why, what_makes_it_hard) from E7V, or empties."""
    data = _mapping(E7V_OUT, paper_id, qno) or {}
    if "error" in data:
        return ("", 0, [], "", "")
    return (data.get("difficulty") or "", data.get("steps_to_solve") or 0,
            data.get("steps") or [], data.get("why") or "",
            data.get("what_makes_it_hard") or "")


def categories_of(paper_id, qno):
    """The E1-E5 rating for one question, pulled out of its ECAT GROUP output.

    ECAT's item is a group of up to six questions, so its output holds a `ratings` array and the
    row for this question has to be found inside it -- unlike every other step here, whose output
    file is the answer for one question.
    """
    wanted = ("%s#q%03d" % (paper_id, qno), "%s__q%03d" % (paper_id, qno))
    # THE LIVE DIRECTORY FIRST, then any rating pulled out of it for re-rating. The agents must not
    # see the quarantined copies -- their brief skips a packet whose output already exists -- but a
    # READER should: a question whose rating is being improved is not the same as one never rated,
    # and blanking its card mid-rewrite makes the page worse than leaving the older rating up. A
    # rewritten rating always wins, because the live directory is searched first.
    for folder in (ECAT_OUT, RERATING):
        for path in sorted(glob.glob(rc.pp(*folder, "*.json"))):
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
            except ValueError:
                continue
            for rating in (data.get("ratings") or []):
                if rating.get("question_id") in wanted:
                    return rating, data.get("group_note") or ""
    return None, ""


def picture_options(options):
    """True when EVERY present option is a picture placeholder rather than real text."""
    values = [(v or "").strip() for v in options.values() if (v or "").strip()]
    return bool(values) and all(PICTURE_OPTION.match(v) for v in values)


def question_card(paper_id, q, out_path, counts=None, show_paper=False):
    """One question's card: printed crop, what was read, classification, E1-E5, the answers.

    Lifted out of write_html so that `build_ncert_paper_map.py` renders through THIS code rather
    than a second implementation of it. Two renderings of the same record drift apart silently,
    and the drift shows up as a reader believing the two pages disagree about the data when they
    only disagree about the drawing of it.

    `out_path` is the file the card will be written into: every image src is relative to it, so a
    card rendered for a page in another directory still finds its crops.
    """
    counts = collections.Counter() if counts is None else counts
    # `show_paper` names the booklet on the card itself. The paper export leaves it off because the
    # whole page is one booklet; a page that mixes booklets -- the NCERT evidence map -- would
    # otherwise show "24." with no way to tell WHICH paper's question 24 it is.
    paper_chip = ('<span class="paperid">%s</span>'
                  % html.escape(paper_id.replace("_", " Code ")) if show_paper else "")
    draft = q["text_layer_draft"]
    source, stem_text, options, answer = reading(paper_id, q)
    solved, confidence, why = solved_answer(paper_id, q["qno"])
    stand = verdict(answer, solved)
    counts[("verdict_" + stand.lower().replace(" ", "_"))] += 1
    counts["read_by_agent" if source == "agent" else "read_from_draft"] += 1
    flags = []
    if source == "draft" and q.get("needs_image_read"):
        flags.append("TEXT LAYER CANNOT REPRESENT THIS: %s \u2014 awaiting B3V"
                     % "; ".join(q.get("needs_image_read_why") or []))
    if source == "agent":
        counts["agent_ok"] += 1
    if len(options) != 4:
        flags.append("only %d options in the text draft" % len(options))
        counts["short_options"] += 1
    if not answer:
        flags.append("no printed answer found")
    if is_key_grid(stem_text):
        flags.append("NOT A QUESTION: this is a row of the booklet's printed answer-key grid")
        counts["key_grid_rows"] += 1
        counts["no_answer"] += 1
    if not stem_text:
        flags.append("empty stem")
        counts["empty_stem"] += 1
    if not q.get("text_layer_reliable", True):
        flags.append("page is a sliced scan: this text is OCR, read the crop")
        counts["ocr_text"] += 1
    if draft["answer_starred"]:
        flags.append("answer printed with * (NTA later altered this question)")
        counts["starred"] += 1
    counts["questions"] += 1
    counts["figures"] += len(q["figures"])

    crop = q.get("question_image")
    crop_abs = rc.pp(*CORPUS, crop) if crop else None
    subj, br, subj_how = confirmed_subject(paper_id, q)
    _codes, chap_names, _tids, topic_names, chap_conf = chapter_topic(paper_id, q["qno"])
    stream, br = stream_and_branch(subj, br, _codes, chap_names)
    subject_label = subj or "unassigned"
    # The part of the subject a student actually revises by -- organic chemistry, or zoology --
    # shown next to the subject rather than hidden in a column.
    if stream or br:
        subject_label += " / " + (stream or br)
    if chap_names:
        counts["mapped_to_chapter"] += 1
    # `subject_from` is shown, not just the subject: a subject read off a printed heading and
    # one guessed from the question number are not the same claim, and 2 of 10 booklets in this
    # corpus print their sections in a NON-standard order, so the guess is wrong there.
    parts = ['<div class="q"><div class="qhead">%s<span class="qno">Q%d</span>'
             '<span class="subj" title="%s">%s</span>%s</div>'
             % (paper_chip, q["qno"], html.escape(subj_how), html.escape(subject_label),
                "".join('<span class="flag">%s</span>' % html.escape(f) for f in flags)),
             classification_html(subj, stream, br, chap_names, topic_names, chap_conf,
                                 taxonomy_gap(paper_id, q["qno"]),
                                 *mapping_reasons(paper_id, q["qno"]))]
    parts.append('<div class="pair">')
    # LEFT: what the booklet printed
    if crop_abs and os.path.exists(crop_abs):
        rel = os.path.relpath(crop_abs, os.path.dirname(out_path))
        parts.append('<div class="side"><div class="sidelabel">printed in the booklet</div>'
                     '<img class="shot" src="%s" alt="printed question %d" loading="lazy">'
                     '</div>' % (html.escape(rel), q["qno"]))
    else:
        parts.append('<div class="side"><div class="sidelabel">printed in the booklet</div>'
                     '<p class="missing">no crop was cut for this question</p></div>')
    # RIGHT: what we extracted
    parts.append('<div class="side"><div class="sidelabel">%s</div>'
                 % ("READ FROM THE IMAGE by b3-question-reader" if source == "agent"
                    else "text-layer draft &mdash; not the record"))
    # The figures this question owns. The agent's crop wins: it was cut from a box the agent
    # reported while reading, where the geometric crops come from clustering vector paths and
    # under-count. Built here, before the stem, because a stem with lettered parts needs them.
    figure_html = []
    for image in (q.get("agent_figure_images") or []):
        rel = os.path.relpath(os.path.join(rc.pp(*CORPUS), image), os.path.dirname(out_path))
        figure_html.append(
            '<img src="%s" alt="figure for question %d" loading="lazy">'
            '<figcaption>figure reported by the agent &middot; <code>papers_v2/%s</code>'
            '</figcaption>' % (html.escape(rel), q["qno"], html.escape(image)))
    if not figure_html:
        for figure in q["figures"]:
            image = figure.get("image")
            if not image:
                continue
            rel = os.path.relpath(os.path.join(rc.pp(*CORPUS), image),
                                  os.path.dirname(out_path))
            figure_html.append(
                '<img src="%s" alt="%s figure for question %d" loading="lazy">'
                '<figcaption>%s, found by geometry &middot; <code>papers_v2/%s</code>'
                '</figcaption>' % (html.escape(rel), figure["role"], q["qno"],
                                   figure["role"], html.escape(image)))
    read_now = agent_read(paper_id, q["qno"])
    # GEOMETRIC FIGURES THE AGENT'S READ HAS SUPERSEDED. Where the agent read the question from
    # the image and says it has no figure, and every option came back as real text, a crop the
    # geometric pass labelled `option_panels` or `stem_figure` is a PICTURE OF THE SAME TABLE
    # the options already say in words -- q054 of 2015_A showed its four options twice, once as
    # two images and once as text. The agent looked at the page; the geometric pass only
    # clustered vector paths, so where they disagree the agent wins.
    if read_now and not read_now.get("has_figure") and not picture_options(options) \
            and len(options) == 4:
        figure_html = []
        counts["redundant_crop_suppressed"] += 1
    tables, stem_shown = "", stem_text
    if read_now:
        tables = lists_html(read_now, figure_html)
    else:
        parsed = parse_match_lists(stem_text)
        if parsed:
            # The flattened stem IS the table, so it is replaced by it rather than printed twice.
            stem_shown, tables = "", match_table_html(parsed)
            counts["match_list_rebuilt"] += 1
    if tables:
        # The table IS the question's content, so a crop of the same table is noise. Dropping it
        # here also stops the geometric figure pass from presenting a picture of a table as a
        # "figure" the question depends on.
        figure_html = [f for f in figure_html if "option_panels" not in f]
    split = split_parts(stem_text, len(figure_html))
    if split:
        lead, lettered, closing = split
        counts["stem_with_parts"] += 1
        block = []
        if lead:
            block.append('<p>%s</p>' % texhtml.to_html(lead))
        spare = list(figure_html)
        for letter, text, drawn in lettered:
            shown = texhtml.to_html(text)
            if drawn and spare:
                shown = ('<figure class="part">%s</figure>' % spare.pop(0)) + shown
            elif drawn:
                shown = '<span class="missing">(drawn &mdash; no figure was cut)</span>'
            block.append('<div class="part"><span class="partlet">%s.</span>'
                         '<div class="partbody">%s</div></div>' % (letter, shown))
        if closing:
            block.append('<p>%s</p>' % texhtml.to_html(closing))
        parts.append('<div class="stem">%s%s</div>' % ("".join(block), tables))
        figure_html = spare
    else:
        parts.append('<div class="stem">%s%s</div>'
                     % (texhtml.to_html(stem_shown)
                        or ("" if tables else "<em>(no stem text)</em>"), tables))
    for item in figure_html:
        parts.append("<figure>%s</figure>" % item)
    # `agent_figure_note` is NOT shown. It records why a reported figure was not cut -- almost
    # always "it sits below the printed Answer/Sol. line, so it is the publisher's worked
    # solution". That is a note about the EXTRACTION, addressed to whoever tunes the figure
    # cutter, and on 20 of 2015_A's questions it appeared as a paragraph explaining the absence
    # of something a reader was never going to miss. It stays on the record in the JSON.
    option_images = q.get("agent_option_images") or {}
    if options and option_images:
        # EACH PICTURE OPTION BESIDE ITS OWN NUMBER. The alternative -- one tall strip of four
        # drawings above four `[structure diagram]` lines -- makes the reader count down the
        # strip to decide which drawing is option 3, which is exactly the kind of counting a
        # printed paper never asks of anyone.
        items = []
        for key in "1234":
            if key not in options:
                continue
            cls = ' class="key"' if answer == key else ""
            image = option_images.get(key)
            if image:
                rel = os.path.relpath(os.path.join(rc.pp(*CORPUS), image),
                                      os.path.dirname(out_path))
                cell = ('<img class="optimg" src="%s" alt="option %s of question %d" '
                        'loading="lazy">' % (html.escape(rel), key, q["qno"]))
            else:
                cell = texhtml.to_html(options[key]) or "<em>(blank)</em>"
            items.append("<li%s>%s</li>" % (cls, cell))
        parts.append('<ol class="opts pics">%s</ol>' % "".join(items))
        counts["option_crops_shown"] += 1
        # The whole-group strip is redundant once every option is cut out of it.
        figure_html = [f for f in figure_html if "q%03d.png" % q["qno"] not in f]
    elif options and picture_options(options):
        # The options ARE the picture. The figure above already shows all four panels with their
        # printed numbers, so repeating "(1) [structure diagram]" four times adds nothing.
        parts.append('<p class="pictopts">The four options are pictures &mdash; see the figure '
                     'above. Printed answer: <b>(%s)</b>.%s</p>'
                     % (html.escape(answer or "?"),
                        " Panel order is booklet-code specific, so b10-figure-splitter decides "
                        "which panel is which option." if answer else ""))
        counts["picture_options"] += 1
    elif options:
        items = []
        for key in "1234":
            if key not in options:
                continue
            cls = ' class="key"' if answer == key else ""
            items.append("<li%s>%s</li>"
                         % (cls, texhtml.to_html(options[key]) or "<em>(blank)</em>"))
        parts.append("<ol class=\"opts\">%s</ol>" % "".join(items))
    # The SOURCE, so any extracted row can be opened against the booklet it came from. Without
    # it a reader who doubts a question has no way back to the page that settles it.
    # THE TWO ANSWERS THAT ARE JUDGED, side by side and never collapsed. The booklet is the
    # publisher's reading and publishers get questions wrong; the solve has seen neither the
    # publisher's answer nor any key. Agreement is evidence; a disagreement is a question worth
    # a person's time, so it is highlighted rather than reconciled. The official NTA key is
    # recorded in the CSV but not shown -- see verdict() for the measurement behind that.
    bad = "differs" in stand or stand == "solve was unsure"
    parts.append(
        '<table class="answers %s"><tr><th>printed in the booklet</th>'
        '<th>solved independently</th><th>verdict</th></tr>'
        '<tr><td>%s</td><td>%s%s</td><td>%s</td></tr></table>'
        % ("mismatch" if bad else "",
           html.escape(answer or "\u2014"),
           html.escape(solved or "not solved yet"),
           (' <span class="conf">%s</span>' % html.escape(confidence)) if confidence else "",
           html.escape(stand)))
    band, steps_count, steps, band_why, band_hard = difficulty_of(paper_id, q["qno"])
    if band:
        counts["difficulty_" + band] += 1
        parts.append(
            '<table class="classify"><tr><th>difficulty</th><td><b>%s</b>%s</td></tr>'
            '<tr><th>steps</th><td>%s</td></tr>%s%s</table>'
            % (html.escape(band),
               ' &middot; %d step%s' % (steps_count, "" if steps_count == 1 else "s")
               if steps_count else "",
               texhtml.greek_in_relation(" \u2192 ".join(steps)) or "<i>none listed</i>",
               '<tr><th>why</th><td>%s</td></tr>'
               % texhtml.greek_in_relation(band_why) if band_why else "",
               # The schema field is `what_makes_it_hard`, but it is NOT a claim that the
               # question is hard: SPEC E7 defines it as the factor OTHER than step count -- a
               # trap option, an unstated assumption, a unit conversion that moves the order of
               # magnitude. An easy question can have one, and q008 does: both of the first two
               # options account for the ten electrons beyond Xe, so counting alone cannot
               # separate them. Labelling that "what makes it hard" on a question banded easy
               # reads as a contradiction, so the page says what the field actually holds.
               # No gloss here. It read "the factor besides step count: a trap, an unstated
               # assumption, a conversion" under all 90 of these -- a drafting instruction to
               # the rater, repeated at the reader. The row label already says what it holds.
               '<tr><th>the catch</th><td>%s</td></tr>'
               % html.escape(band_hard) if band_hard else ""))
    rating, _group_note = categories_of(paper_id, q["qno"])
    if rating:
        counts["categorised"] += 1
        cards = []
        for axis, fallback, fields in (
                ("E1", "Question type", ("question_type", "secondary_type")),
                ("E2", "Format", ("format",)),
                ("E3", "Content shape", ("content_shape", "concept")),
                ("E4", "Thinking", ("cognitive_demand", "solution_structure",
                                    "strategy_available")),
        ):
            # NOT `body`: that name holds the whole page's accumulator in this function, and
            # reusing it here silently rebound it, so only the LAST question survived -- the
            # file came out with one question in it instead of 177.
            shown = []
            for field in fields:
                value = rating.get(field)
                if not value:
                    continue
                render = free_text_html if field == "concept" else label_html
                for one in (value if isinstance(value, list) else [value]):
                    shown.append(render(one))
            if shown:
                cards.append(axis_card(axis, fallback, "".join(shown)))
        # E5 is its own shape: a trap is {label, option, route}, because rulebook rule 5 says
        # every trap names the option AND the route or there is no tag. The option is shown as
        # its own marker so a reader can line the trap up against the printed options above.
        traps = rating.get("traps") or []
        if traps:
            cards.append(axis_card("E5", "Trap", "".join(
                label_html(t.get("label") if isinstance(t, dict) else t,
                           t.get("route") if isinstance(t, dict) else "")
                .replace('<div class="labelrow">',
                         '<div class="labelrow"><span class="opt">option %s</span>'
                         % html.escape(str(t.get("option"))) if isinstance(t, dict) else
                         '<div class="labelrow">')
                for t in traps)))
        elif rating.get("note"):
            cards.append(axis_card("E5", "Trap",
                                   '<div class="labelrow"><span class="means">no option '
                                   'carries a nameable device \u2014 an empty list is a real '
                                   'answer, not an omission</span></div>'))
        # `reason` is deliberately NOT shown, for the same reason `group_note` is not: it
        # argues the rating rules, not the question. Each axis already carries its definition
        # and each trap its own route, which is what a reader checking one question needs. The
        # field stays in the JSON for whoever audits the labelling itself.
        if cards:
            parts.append('<div class="cats">%s</div>' % "".join(cards))
    if why and bad:
        parts.append('<p class="why">solver reasoning: %s</p>' % html.escape(str(why)[:300]))

    src = q.get("source_pdf") or ""
    # Resolved INSIDE the repo. This link used to point into the owner's Downloads folder, which
    # made it dead for every other reader and printed that folder's structure to anyone who opened
    # the page. The shareable builds strip it; it now resolves for anyone who has the repo.
    src_abs = os.path.join(rc.pp("inputs", "papers_v2_sources"), src) if src else ""
    if src_abs and not os.path.exists(src_abs):
        src_abs = ""
    parts.append(
        '<div class="meta">page %d &middot; printed answer %s'
        '%s%s</div>'
        % (q["page"], html.escape(answer or "none"),
           ' &middot; <a href="file://%s#page=%d">open source PDF at this page</a>'
           % (html.escape(src_abs), q["page"]) if src_abs else "",
           ' &middot; <code>%s</code>' % html.escape(os.path.basename(src)) if src else ""))
    parts.append("</div></div>")      # close .side (extracted) and .pair
    parts.append("</div>")            # close .q
    return "".join(parts)


def write_html(paper, out_path):
    meta = paper["meta"]
    paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
    questions = paper["questions"]
    counts = collections.Counter()
    body = []
    for q in questions:
        body.append(question_card(paper_id, q, out_path, counts))

    stats = [
        ("questions", counts["questions"]),
        ("figures", counts["figures"]),
        ("no printed answer", counts["no_answer"]),
        ("fewer than 4 options", counts["short_options"]),
        ("empty stem", counts["empty_stem"]),
        ("answer starred", counts["starred"]),
        ("OCR text", counts["ocr_text"]),
        ("read from the image", counts["read_by_agent"]),
        ("still only a text draft", counts["read_from_draft"]),
        ("stems split into lettered parts", counts["stem_with_parts"]),
        ("match-lists rebuilt as tables", counts["match_list_rebuilt"]),
        ("redundant crops suppressed", counts["redundant_crop_suppressed"]),
        ("difficulty easy", counts["difficulty_easy"]),
        ("difficulty medium", counts["difficulty_medium"]),
        ("difficulty hard", counts["difficulty_hard"]),
        ("rated on E1-E5", counts["categorised"]),
        ("options are pictures", counts["picture_options"]),
        ("mapped to a chapter", counts["mapped_to_chapter"]),
        ("answers all agree", counts["verdict_all_agree"] + counts["verdict_agree"]),
        ("answer disagreements", counts["verdict_solved_differs_from_official"]
         + counts["verdict_solved_differs_from_booklet"]),
    ]
    head = (
        "<title>NEET %s Code %s &middot; extraction v2</title>"
        "<style>%s</style>" % (meta["year"], meta["booklet_code"] or "NA", CSS))
    page = (
        '%s<div class="wrap"><h1>NEET (UG) %s &middot; Code %s</h1>'
        '<div class="sub">extraction v2 from <code>%s</code> &middot; family <b>%s</b> &middot; '
        '%d pages &middot; %d chars/page &middot; rendered at %d dpi<br>'
        'Flags are shown, not hidden: this page exists to find extraction faults, so a short option '
        'list or a missing answer is marked rather than tidied away. The text shown is the '
        '<b>text-layer draft</b> &mdash; B3 reads the question image and is the record. '
        'Each question shows the crop cut straight from the booklet on the LEFT and what was '
        'extracted on the RIGHT, so the two can be read against each other line by line.</div>'
        '<div class="stats">%s</div>%s</div>'
        % (head, meta["year"], meta["booklet_code"] or "NA", html.escape(meta["source_pdf"]),
           meta["family"], meta["pages"], meta["chars_per_page"], meta["dpi"],
           "".join('<div class="stat"><b>%d</b><span>%s</span></div>' % (v, k) for k, v in stats),
           "".join(body)))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(page)
    return counts


def write_index(summaries, out_path):
    rows = "".join(
        '<tr><td><a href="%s">%s</a></td><td>%d</td><td>%d</td><td>%d</td><td>%d</td>'
        '<td>%d</td><td>%d</td><td>%d</td></tr>'
        % (html.escape(s["href"]), html.escape(s["paper_id"]), s["questions"], s["figures"],
           s["no_answer"], s["short_options"], s["starred"], s["ocr_text"], s["by_agent"])
        for s in summaries)
    page = (
        "<title>NEET extraction v2 &middot; index</title><style>%s"
        "table{border-collapse:collapse;width:100%%;font-size:14px}"
        "th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--rule);"
        "font-variant-numeric:tabular-nums}th{font-size:11px;text-transform:uppercase;"
        "letter-spacing:.06em;color:var(--ink2)}</style>"
        '<div class="wrap"><h1>Extraction v2 &middot; every booklet</h1>'
        '<div class="sub">One page per booklet, rebuilt to look like the paper so the extraction '
        'can be read against what was printed. Counts are faults, not scores: lower is better in '
        'every column after the first two.</div>'
        "<table><tr><th>booklet</th><th>questions</th><th>figures</th><th>no answer</th>"
        "<th>&lt;4 options</th><th>starred</th><th>OCR text</th><th>read from image</th></tr>"
        "%s</table></div>" % (CSS, rows))
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(page)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", action="store_true")
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--paper-id")
    args = ap.parse_args()
    if not (args.csv or args.html):
        ap.error("pass --csv and/or --html")

    papers = load(args.paper_id)
    if not papers:
        print("no v2 papers found -- run scripts/extract_paper_v2.py --apply first")
        return 1

    if args.csv:
        for paper in papers:
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            out = rc.pp(*CORPUS, "exports", "csv", "%s.csv" % paper_id)
            rows = write_csv([paper], out)
            print("csv   %-52s %d rows" % (os.path.relpath(out, rc.pp()), rows))
        out = rc.pp(*CORPUS, "exports", "questions_v2_all.csv")
        rows = write_csv(papers, out)
        print("csv   %-52s %d rows (all booklets)" % (os.path.relpath(out, rc.pp()), rows))

    if args.html:
        summaries = []
        for paper in papers:
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            out = rc.pp(*CORPUS, "exports", "html", "%s.html" % paper_id)
            counts = write_html(paper, out)
            summaries.append({"paper_id": paper_id, "href": "%s.html" % paper_id,
                              "questions": counts["questions"], "figures": counts["figures"],
                              "no_answer": counts["no_answer"],
                              "short_options": counts["short_options"],
                              "starred": counts["starred"],
                              "ocr_text": counts["ocr_text"],
                              "by_agent": counts["read_by_agent"]})
            print("html  %-52s %d questions, %d figures"
                  % (os.path.relpath(out, rc.pp()), counts["questions"], counts["figures"]))
        index = rc.pp(*CORPUS, "exports", "html", "index.html")
        write_index(summaries, index)
        print("html  %-52s index of %d booklet(s)"
              % (os.path.relpath(index, rc.pp()), len(summaries)))
    return 0


if __name__ == "__main__":
    sys.exit(main())


def page_shell(title, body, extra_css="", lede="", force_light=False):
    """The document around a set of `question_card`s, sharing this module's CSS.

    `force_light` pins the page to the white paper ground instead of following the viewer's theme.
    The NCERT map uses it because the thing being judged on that page is a SCANNED BOOK PAGE: the
    screenshots are black ink on white, and floating them on a dark card makes the page read as two
    different documents stapled together.
    """
    css = CSS + extra_css
    if force_light:
        css += ("\n:root,:root[data-theme=dark]{--paper:#fff;--card:#fff;--ink:#141414;"
                "--ink2:#555;--rule:#d8d8d2}\n"
                "@media (prefers-color-scheme:dark){:root:not([data-theme=light]){"
                "--paper:#fff;--card:#fff;--ink:#141414;--ink2:#555;--rule:#d8d8d2}}\n")
    return ('<title>%s</title><style>%s</style><div class="wrap">%s%s</div>'
            % (html.escape(title), css,
               '<div class="sub">%s</div>' % lede if lede else "", body))
