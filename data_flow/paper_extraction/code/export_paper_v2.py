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
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import cdn  # noqa: E402
from lib import texhtml  # noqa: E402
from lib import sibling_text  # noqa: E402
import record_v3  # noqa: E402
import paper_md  # noqa: E402

CORPUS = rc.corpus()
#: Where B3V writes the agent's read of each question. When one exists it REPLACES the text draft in
#: every export, because the draft is a cross-check and the agent's read of the image is the record.
B3V_OUT = ("steps", "B3V", "out")
#: Where b6-blind-solver's independent answer lands.
B6V_OUT = ("steps", "B6V", "out")
QSUBJ_OUT = ("steps", "QSUBJ", "out")
QCHAP_OUT = ("steps", "QCHAP", "out")
QTOPIC_OUT = ("steps", "QTOPIC", "out")
#: b3s-solution-reader's read of the publisher's printed worked solution.
B3S_OUT = ("steps", "B3S", "out")
#: b3f-figure-transcriber's caption and labels for one figure crop.
B3F_OUT = ("steps", "B3F", "out")
#: The committed deliverable: data/<year>/<paper_code>/{questions.json, question_paper.html,
#: question_paper.md}.
DATA = ("data",)
#: questions.json's own schema tag. Bumped only when a field changes meaning.
RECORD_SCHEMA = record_v3.SCHEMA


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


STREAMS = rc.mappings() + ("chapter_streams.json",)
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
    if solved in accepted(official):
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
    answer = printed_answer(draft)
    if read:
        source, stem, options = "agent", read.get("stem_en") or "", read.get("options_en") or {}
    else:
        source, stem, options = "draft", draft.get("stem") or "", draft.get("options") or {}
    opening = restored_opening(question)
    if opening and not stem.startswith(opening["text"]):
        stem = opening["text"] + " " + stem
    return (source, stem, options, answer)


def restored_opening(question):
    """The opening words this booklet lost, read from the same exam's other booklet codes, or None.

    Only for a question the extractor split off with NO printed number (split_unnumbered): that is
    the sign its first line fell off the page, as 2017 Code-A q130 did. The words come verbatim from
    the siblings' text layers (lib/sibling_text.py), and the record says which siblings."""
    if question.get("number_printed", True) or not question.get("source_pdf"):
        return None
    pdf = os.path.join(rc.source_dir(), question["source_pdf"])
    if not os.path.exists(pdf):
        return None
    return sibling_text.restored_opening(pdf, (question.get("text_layer_draft") or {}).get("stem"))


#: A printed solution that says the question has no correct option as printed (2017_A q3: "No
#: option is correct", then it answers a corrected reading of the question).
NO_OPTION_CORRECT = re.compile(
    r"\bno (?:option|answer|choice) is (?:correct|right)\b"
    r"|\bnone of the (?:options|answers|choices|given options) (?:is|are) correct\b", re.I)


def _booklet(pdf_name):
    m = re.search(r"Code_([A-Z0-9]+)", pdf_name or "")
    return "Code %s" % m.group(1) if m else pdf_name


def record_flags(question, publisher, ai, solution_steps):
    """What a reader must know before trusting this question, as [{code, text}].

    Each flag is decided from the record itself, never from a reviewer's memory, so the same
    defect in another booklet is flagged the same way. The JSON carries them in `flags`; the review
    page shows them on the card."""
    flags = []
    if not question.get("number_printed", True):
        opening = restored_opening(question)
        if opening:
            where = ", ".join("%s q%d" % (_booklet(s["pdf"]), s["qno"]) for s in opening["sources"])
            flags.append({"code": "opening_restored",
                          "text": "The booklet lost this question's number and first line. The "
                                  "opening \"%s\" is restored word for word from %s (same exam)."
                                  % (opening["text"], where)})
        else:
            flags.append({"code": "opening_missing",
                          "text": "The booklet lost this question's number and first line, and no "
                                  "other booklet code of this exam prints it; the stem starts "
                                  "mid-sentence."})
    if (question.get("text_layer_draft") or {}).get("answer_bonus"):
        flags.append({"code": "bonus",
                      "text": "The booklet prints \"%s\": NTA dropped this question and gave every "
                              "candidate its marks, so it has no keyed answer."
                              % (question["text_layer_draft"].get("answer_line") or "Bonus").strip()})
    said = next((s for s in solution_steps or [] if NO_OPTION_CORRECT.search(s)), None)
    if said:
        flags.append({"code": "publisher_no_option_correct",
                      "text": "The printed solution says \"%s\": the question has no correct option "
                              "as printed, and the printed answer comes from a corrected reading."
                              % said.strip()})
    if publisher and ai and ai not in accepted(publisher):
        flags.append({"code": "answers_differ",
                      "text": "The independent solve chose (%s); the booklet prints (%s)."
                              % (ai, publisher)})
    return flags


#: How several accepted options are joined into one answer string: `1 & 2`.
ACCEPTED_JOIN = " & "


def printed_answer(draft):
    """The booklet's printed answer: one option, or every accepted option joined by ` & `.

    2017 Code-A prints `Answer (1 & 2)* Both answers are correct.` for q18. Read as a single option it
    was `None`, so the page said "no printed answer found" about a question that prints one.
    """
    if draft.get("official_answer"):
        return draft["official_answer"]
    accepted = draft.get("official_answers") or []
    return ACCEPTED_JOIN.join(accepted) if accepted else None


def accepted(answer):
    """The set of options a printed answer accepts: `"1 & 2"` -> {"1", "2"}."""
    return set((answer or "").split(ACCEPTED_JOIN)) - {""}


def image_src(q, image, out_path, counts):
    """The `src` for one of this question's images: its CDN URL, else the local file.

    Every image is meant to be a CDN link (code/upload_paper_assets.py). The local fallback keeps a page
    readable before the upload has run, and each fallback is COUNTED so the export says how many
    images would break the moment the page leaves this machine.
    """
    url = cdn.url_for(q, image)
    if url:
        counts["images_cdn"] += 1
        # the file's fingerprint rides on the link: a drawing re-uploaded under its old name
        # (2017_A's chemistry, redrawn on the booklet's geometry) is not served stale from a cache
        sha = cdn.sha_for(q, image)
        return "%s?v=%s" % (url, sha[:12]) if sha else url
    counts["images_local"] += 1
    return os.path.relpath(os.path.join(rc.pp(*CORPUS), image), os.path.dirname(out_path))


def image_attrs(q, image, out_path, counts):
    """`src`/`data-local`/`onerror` for one image: the CDN URL first, the local file as fallback.

    The handover's rule: the page must work online AND from a clean clone. A clean clone has no
    `papers/` (it is git-ignored), so the CDN URL is the src; a machine with no network has the
    local file, so it is carried as `data-local` and swapped in only if the URL fails to load. The
    swap is an inline attribute, not a script file -- nothing is fetched to make it work.
    """
    # THE EXACT VECTOR COPY WINS. vector_figures.py lifts every cut figure out of the PDF as SVG --
    # the publisher's own paths and glyphs, no watermark -- and records it as this PNG's twin.
    svg = (q.get("vector") or {}).get(image)
    if svg and (cdn.url_for(q, svg) or os.path.exists(os.path.join(rc.pp(*CORPUS), svg))):
        counts["images_vector"] += 1
        image = svg
    src = image_src(q, image, out_path, counts)
    local = os.path.relpath(os.path.join(rc.pp(*CORPUS), image), os.path.dirname(out_path))
    if src == local:
        return 'src="%s"' % html.escape(local.replace("\\", "/"))
    return ('src="%s" data-local="%s" onerror="if(this.dataset.local&amp;&amp;'
            'this.getAttribute(\'src\')!==this.dataset.local){this.src=this.dataset.local}"'
            % (html.escape(src), html.escape(local.replace("\\", "/"))))


WITHHELD_NOTE = ('<p class="flag">our drawing is withheld: it did not pass the check against the '
                 'print (reason in questions.json)</p>')


def drawn_html(q, image, out_path, counts):
    """The pipeline's own drawing of one figure, as a panel under the printed copy -- or nothing.

    Shown BESIDE the exact copy, never instead of it: a card can be self-consistent and still not be
    the printed figure, and only a reader comparing the two catches that (FIGURE_RENDERING_PLAN 3.6).
    A card that failed its check is said so in red, so a missing drawing is never mistaken for a
    figure that needed none.
    """
    entry = (q.get("drawn") or {}).get(image)
    if not entry:
        return ""
    source = ("on the booklet's own geometry, every structure checked atom for atom against its SMILES"
              if entry.get("layout") == "booklet" and entry.get("source") == "smiles" else
              "on the booklet's own geometry, its figure spec checked against it (labels and lines)"
              if entry.get("layout") == "booklet" else
              # a picture-printed figure traced from the booklet's own picture (render_figure_cards);
              # labelled as RDKit or a spec drawing, it claimed a layout the card does not show
              "traced from the booklet's printed picture, its SMILES checked"
              if entry.get("layout") == "traced" and entry.get("source") == "smiles" else
              "traced from the booklet's printed picture"
              if entry.get("layout") == "traced" else
              "from SMILES (RDKit)" if entry.get("source") == "smiles" else "from a figure spec")
    if entry.get("status") == "failed_check":
        counts["drawn_failed"] += 1
        # ONE SHORT LINE. The check's full report (2018_AA q052: ten clauses about the solution's
        # structures) is for whoever fixes the card and stays in questions.json as drawn.message;
        # printed under every figure and option it buried the question. question_card keeps the
        # first of these per card.
        return WITHHELD_NOTE
    if entry.get("status") != "drawn" or not entry.get("svg"):
        return ""
    counts["drawn_shown"] += 1
    facts = ""
    if entry.get("source") == "smiles":
        species = (entry.get("card") or {}).get("species") or []
        facts = " &middot; ".join(
            "%s%s <code>%s</code>%s" % (
                html.escape(sp.get("label") or ""), " " if sp.get("label") else "",
                html.escape(sp.get("formula") or ""),
                {"match": " name&nbsp;✓", "mismatch": ' <b class="bad">name&nbsp;✗</b>'}.get(
                    sp.get("name_check"), ""))
            for sp in species)
    return ('<details class="drawn" open><summary>drawn by the pipeline %s%s</summary>'
            '<img %s alt="drawing of %s" loading="lazy"></details>'
            % (source, (" &middot; " + facts) if facts else "",
               image_attrs(q, entry["svg"], out_path, counts), html.escape(entry["figure_id"])))


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
              "question_image_url", "figure_urls", "source_pdf"]
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
                    "question_image": q["question_image"],
                    "question_image_url": cdn.url_for(q, q["question_image"]) or "",
                    "figure_urls": "; ".join(
                        cdn.url_for(q, f) or "" for f in (q.get("agent_figure_images")
                                                          or q.get("figure_images") or [])),
                    "source_pdf": q["source_pdf"],
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
.optimg{max-width:min(100%,22em);height:auto;display:block;background:#fff;
 border:1px solid color-mix(in srgb,currentColor 12%,transparent);border-radius:4px}
.opttext{margin:.25em 0 .1em}
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
figure.part{display:block;margin:0 0 .3em 0}
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
.warnline{font-size:12.5px;background:var(--warn-bg);color:var(--warn);border-left:3px solid
 var(--warn);padding:6px 10px;margin:0 0 10px;border-radius:4px}
.meta{font-size:11px;color:var(--ink2);margin-top:10px;border-top:1px dashed var(--rule);
 padding-top:7px}
a{color:var(--accent)}
.qhead{margin-bottom:10px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start}
@media (max-width:760px){.pair{grid-template-columns:1fr}}
.side{min-width:0}
.sidelabel{font-size:10px;text-transform:uppercase;letter-spacing:.09em;color:var(--ink2);
 border-bottom:1px solid var(--rule);padding-bottom:4px;margin-bottom:9px}
.sidelabel.solshot{margin-top:14px}
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


GLOSSARY = rc.mappings() + ("label_glossary.json",)
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


def _posix(path):
    """A stored relative path with forward slashes. The extractor joins paths with os.path.join, so
    on Windows the records hold backslashes; the deliverable must read the same on every OS, or two
    machines exporting the same data produce different bytes."""
    return path.replace("\\", "/") if isinstance(path, str) else path


def publisher_solution(paper_id, qno):
    """b3s-solution-reader's read of the printed worked solution, or None if B3S has not run."""
    return _mapping(B3S_OUT, paper_id, qno)


def solve_record(paper_id, qno):
    """b6-blind-solver's whole output for this question, or None."""
    return _mapping(B6V_OUT, paper_id, qno)


#: Where a solver's one-string `working` is split into steps: after a sentence or clause end that is
#: followed by the start of the next move. Used ONLY for outputs written before B6 had `steps` --
#: the handover's rule is that those solves are split, not re-run.
STEP_BREAK = re.compile(r"(?<=[.;])\s+(?=[A-Z$\\(\[])|\n+")


def ai_steps(solve):
    """The AI's reasoning as steps: B6's own `steps` where it wrote them, else its `working` split
    on sentence boundaries, else its one-line `reason`."""
    if not solve:
        return []
    if solve.get("steps"):
        return [step for step in solve["steps"] if step.strip()]
    working = (solve.get("working") or "").strip()
    if working:
        return [part.strip() for part in STEP_BREAK.split(working) if part.strip()]
    reason = (solve.get("reason") or "").strip()
    return [reason] if reason else []


def verdict_self(publisher_answer, concludes):
    """Does the booklet's printed answer agree with its OWN worked solution?

    A defect class nothing else catches: a booklet printing `Answer (3)` above a solution that works
    out to 1. Found only by reading the working, which is what B3S's `concludes` records.
    """
    if not publisher_answer or not concludes:
        return "unchecked"
    if concludes == "unclear":
        return "unclear"
    return "agree" if concludes in accepted(publisher_answer) else "publisher_contradicts_itself"


def verdict_code(publisher_answer, ai_answer):
    """verdict() in the record's closed vocabulary: agree / differs / ai_unsure / unchecked."""
    if not (publisher_answer and ai_answer):
        return "unchecked"
    if ai_answer == "unsure":
        return "ai_unsure"
    return "agree" if ai_answer in accepted(publisher_answer) else "differs"


def solutions_html(paper_id, q, options, answer, solved, confidence, out_path, counts):
    """The publisher's printed solution and our independent one, each in its own labelled block.

    Read from B3S where it has run. Where it has not, the TEXT-LAYER lines are shown and labelled as a
    draft, never as the solution -- a worked solution is fractions and exponents, the very content the
    text layer cannot represent. A question with no printed solution says so rather than showing an
    empty block, because "none printed" and "not read yet" are opposites (SPEC Rule 19).
    """
    out = []
    draft_lines = (q.get("text_layer_draft") or {}).get("solution_lines") or []
    read = publisher_solution(paper_id, q["qno"])
    image = q.get("solution_image")
    head = ('<div class="solhead">The publisher\'s solution<span>printed answer (%s)</span></div>'
            % html.escape(answer or "none"))
    body = []
    if read and "error" not in read:
        counts["publisher_solution_read"] += 1
        steps = read.get("solution_stepwise") or []
        body.append(steps_with_figures(q, steps, out_path, counts))
        concludes = read.get("concludes")
        self_check = verdict_self(answer, concludes)
        body.append('<p class="concl">&rarr; the working concludes: <b>%s</b></p>'
                    % html.escape("option %s" % concludes if concludes in "1234" and concludes
                                  else (concludes or "?")))
        if self_check == "publisher_contradicts_itself":
            counts["publisher_contradicts_itself"] += 1
            body.append('<p class="flag">THE BOOKLET CONTRADICTS ITSELF: it prints Answer (%s) but '
                        'its own working arrives at option %s</p>'
                        % (html.escape(answer or "?"), html.escape(concludes)))
        if read.get("complete") is False:
            counts["solution_clipped"] += 1
            body.append('<p class="flag">solution crop is clipped: %s</p>'
                        % texhtml.to_html(read.get("note") or "the working continues past the crop"))
    elif draft_lines:
        counts["publisher_solution_draft"] += 1
        body.append('<p class="draftlabel">text-layer draft &mdash; not the record, awaiting '
                    'b3s-solution-reader</p><div class="draftsol">%s</div>'
                    % "<br>".join(texhtml.to_html(line) for line in draft_lines))
    elif not image:
        counts["no_solution_printed"] += 1
        body.append('<p class="missing">no worked solution is printed for this question</p>')
    else:
        body.append('<p class="missing">solution not read yet (B3S)</p>')
    if image and (cdn.url_for(q, image) or os.path.exists(rc.pp(*CORPUS, image))):
        # The whole printed block is a REFERENCE, folded away. The reader's solution is the steps
        # above with each drawing at the step that uses it; showing the full crop underneath them
        # repeated the solution as one long picture below the answer.
        body.append('<details class="solsrc"><summary>printed solution, as in the booklet</summary>'
                    '<figure class="solimg"><img %s alt="printed solution of question %d" '
                    'loading="lazy"></figure></details>'
                    % (image_attrs(q, image, out_path, counts), q["qno"]))
    out.append('<div class="sol pub">%s%s</div>' % (head, "".join(body)))

    solve = solve_record(paper_id, q["qno"])
    head = ('<div class="solhead">Solved independently (answer withheld)<span>AI: %s%s</span></div>'
            % (html.escape(solved or "not solved yet"),
               (" &middot; " + html.escape(confidence)) if confidence else ""))
    steps = ai_steps(solve)
    if steps:
        body = '<ol class="steps">%s</ol>' % "".join("<li>%s</li>" % texhtml.to_html(step)
                                                      for step in steps)
    else:
        body = '<p class="missing">not solved yet (B6V)</p>'
    out.append('<div class="sol ai">%s%s</div>' % (head, body))
    return "".join(out)


def steps_with_figures(q, steps, out_path, counts):
    """The printed steps as a numbered list, each solution figure drawn right after its step.

    `after_step` comes from b3s-solution-reader (0 = before the first step). A figure is shown as
    its exact vector copy where vector_figures.py made one, else its PNG.
    """
    by_step = collections.defaultdict(list)
    for figure in q.get("solution_figures") or []:
        by_step[min(int(figure.get("after_step") or 0), len(steps))].append(figure)

    def figure_html(figure):
        counts["solution_step_figures"] += 1
        return ('<figure class="stepfig"><img %s alt="figure in the solution of question %d" '
                'loading="lazy">%s</figure>'
                % (image_attrs(q, figure["image"], out_path, counts), q["qno"],
                   drawn_html(q, figure["image"], out_path, counts)))
    lead = "".join(figure_html(f) for f in by_step.get(0, []))
    items = "".join("<li>%s%s</li>" % (texhtml.to_html(step),
                                       "".join(figure_html(f) for f in by_step.get(n, [])))
                    for n, step in enumerate(steps, 1))
    return '%s<ol class="steps">%s</ol>' % (lead, items)


def _status(done, unsure=False):
    return "unsure" if unsure else ("done" if done else "not_run")


#: Which step is owed for each status field, so `pending` names the work rather than the gap.
PENDING_STEP = {"question": "B3V", "publisher_solution": "B3S", "ai_solution": "B6V",
                "subject": "QSUBJ", "chapter": "QCHAP", "subtopic": "QTOPIC",
                "difficulty": "E7V", "figures": "B3V"}


def question_record(paper_id, meta, q):
    """One question in the handover's section-11 shape, from the SAME helpers the HTML uses.

    Every field is present on every record. A field nobody has judged is null with its `status`
    saying `not_run`, never omitted: an absent field and an empty one look identical to a consumer
    and mean opposite things (SPEC Rule 19).
    """
    qno = q["qno"]
    draft = q.get("text_layer_draft") or {}
    source, stem, options, publisher = reading(paper_id, q)
    read = agent_read(paper_id, qno) or {}
    solve = solve_record(paper_id, qno) or {}
    sol = publisher_solution(paper_id, qno) or {}
    if "error" in sol:
        sol = {}
    subject, branch, subject_from = confirmed_subject(paper_id, q)
    qsubj = _mapping(QSUBJ_OUT, paper_id, qno) or {}
    qchap = _mapping(QCHAP_OUT, paper_id, qno) or {}
    qtopic = _mapping(QTOPIC_OUT, paper_id, qno) or {}
    codes, chap_names, topic_ids, topic_names, chap_conf = chapter_topic(paper_id, qno)
    stream, branch = stream_and_branch(subject, branch, codes, chap_names)
    band, steps_count, band_steps, band_why, band_hard = difficulty_of(paper_id, qno)
    ai = solve.get("answer")
    concludes = sol.get("concludes")

    vector = q.get("vector") or {}   # PNG path -> its exact vector twin
    figures = []
    for n, figure in enumerate(q.get("figures") or [], 1):
        local = figure.get("image")
        # B3F's item for this crop is `<paper>#q###_<role>_<n>` (b3f_plugin.py), so its output file
        # is found by the same name; its caption and labels are what the figure carries as text.
        b3f = None
        path = rc.pp(*B3F_OUT, "%s__q%03d_%s_%d.runA.json" % (paper_id, qno, figure.get("role"), n))
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    b3f = json.load(fh)
            except ValueError:
                b3f = None
        figures.append({
            "role": figure.get("role"), "kinds": figure.get("kinds") or [],
            "page": figure.get("page", 0) + 1 if figure.get("page") is not None else None,
            "crop_bbox": figure.get("crop_bbox"), "target_box_in_crop": figure.get("target_box_in_crop"),
            "local": _posix(local), "cdn_url": cdn.url_for(q, local) if local else None,
            "sha256": cdn.sha_for(q, local) if local else None,
            "svg": _posix(vector.get(local)) if local else None,
            "svg_cdn_url": cdn.url_for(q, vector.get(local)) if local and vector.get(local) else None,
            "caption": (b3f or {}).get("caption") or "", "labels": (b3f or {}).get("labels") or [],
            # A geometric crop is a guess from clustered vector paths; the agent READ the question.
            # Where the read found no figure, or cut its own, this crop is not the question's figure
            # -- on 2017 Code-A, B3F found q058's "stem figure" was the previous question's options
            # and q081's "option panels" a solution diagram. Kept for audit, never presented as real.
            # ...and where the agent cut the OPTIONS' drawings: 2018_AA q068's geometric
            # "option panels" was a mis-cut strip of one option plus the next question's text.
            "superseded_by_agent": bool(read) and (not read.get("has_figure")
                                                   or bool(q.get("agent_figure_images"))
                                                   or bool(q.get("agent_option_images"))),
        })

    def image_record(path):
        """One image as the record carries it: the PNG and its exact vector twin, both linked."""
        svg = vector.get(path)
        drawn = (q.get("drawn") or {}).get(path)
        record = {"local": _posix(path), "cdn_url": cdn.url_for(q, path),
                  "sha256": cdn.sha_for(q, path),
                  "svg": _posix(svg), "svg_cdn_url": cdn.url_for(q, svg) if svg else None,
                  "drawn": None}
        if drawn:
            # The pipeline's own drawing: the checked card it was drawn from (SMILES with formula,
            # InChIKey and name-check result, or the physics spec), and the drawing's own links.
            record["drawn"] = {
                "source": drawn.get("source"), "status": drawn.get("status"),
                "svg": _posix(drawn.get("svg")),
                "svg_cdn_url": cdn.url_for(q, drawn["svg"]) if drawn.get("svg") else None,
                "card": drawn.get("card") if drawn.get("source") == "smiles" else None,
                "spec": drawn.get("spec") if drawn.get("source") == "spec" else None,
                "message": drawn.get("message")}
        return record

    agent_figures = [image_record(p) for p in q.get("agent_figure_images") or []]
    option_images = {k: image_record(p)
                     for k, p in sorted((q.get("agent_option_images") or {}).items())}
    # The solution's drawings, each at the step that uses it -- before these the JSON's solution held
    # text only, and its pictures existed nowhere but inside one whole-block crop.
    solution_figures = [dict(image_record(f["image"]), after_step=f.get("after_step", 0),
                             kind=f.get("kind") or None)
                        for f in q.get("solution_figures") or []]

    subject_settled = "printed heading" in (subject_from or "") or bool(qsubj)
    chapter_unsure = qchap.get("chapter_codes") == ["unsure"]
    topic_unsure = qtopic.get("topic_ids") == ["unsure"]
    if read:
        figure_status = ("none" if not read.get("has_figure")
                         else ("done" if q.get("agent_figure_images") else "unsure"))
    else:
        figure_status = "not_run"
    status = {
        "question": _status(source == "agent"),
        "publisher_solution": ("none" if not q.get("solution_image") else _status(bool(sol))),
        "ai_solution": _status(bool(solve)),
        "subject": _status(subject_settled, qsubj.get("subject") == "unsure"),
        "chapter": _status(bool(qchap), chapter_unsure),
        "subtopic": _status(bool(qtopic), topic_unsure),
        "difficulty": _status(bool(band), band == "unsure"),
        "figures": figure_status,
        "categories": "excluded",
    }
    pending = [PENDING_STEP[k] for k, v in status.items() if v == "not_run" and k in PENDING_STEP]
    pending = sorted(set(pending), key=pending.index)

    def option_text(key):
        return options.get(key) if key and key in options else None

    return {
        "question_id": "%s__q%03d" % (paper_id, qno),
        "paper_code": paper_id, "year": q.get("year"), "booklet_code": q.get("booklet_code"),
        "qno": qno,
        "flags": record_flags(q, publisher, ai, sol.get("solution_stepwise") or []),
        "restored_opening": restored_opening(q),

        "question_text": stem, "options": options,
        "statements": read.get("statements") or [], "list_i": read.get("list_i") or [],
        "list_ii": read.get("list_ii") or [],
        "structure": read.get("structure") if read else None,
        "negative_words_seen": read.get("negative_words_seen") or [],

        "publisher_answer": draft.get("official_answer"),
        "publisher_answer_text": option_text(draft.get("official_answer")),
        "publisher_answer_starred": bool(draft.get("answer_starred")),
        # Every option the booklet accepts. One entry normally; two where it prints `Answer (1 & 2)*`
        # -- then `publisher_answer` is null, because a single field cannot hold both.
        "publisher_answers_accepted": draft.get("official_answers") or ([publisher] if publisher else []),
        "publisher_answer_line": draft.get("answer_line"),
        "publisher_solution_stepwise": sol.get("solution_stepwise") or [],
        "publisher_solution_draft": draft.get("solution_lines") or [],
        "publisher_concludes": concludes,
        "publisher_solution_complete": sol.get("complete") if sol else None,
        "publisher_solution_figures": solution_figures,
        "solution_image": _posix(q.get("solution_image")),
        "solution_image_cdn": cdn.url_for(q, q.get("solution_image")) if q.get("solution_image") else None,

        "ai_answer": ai, "ai_answer_text": option_text(ai),
        "ai_solution_stepwise": ai_steps(solve),
        "ai_why": solve.get("reason"), "ai_confidence": solve.get("confidence"),

        "verdict_answer": verdict_code(publisher, ai),
        "verdict_self": verdict_self(publisher, concludes),

        "subject": subject, "subject_from": subject_from,
        "subject_why": qsubj.get("why"), "subject_confidence": qsubj.get("confidence"),
        "agrees_with_position": qsubj.get("agrees_with_position"),
        "stream": stream or None, "branch": branch or None,

        "chapter_code": codes[0] if codes else None,
        "chapter_name": chap_names[0] if chap_names else None,
        "chapter_why": qchap.get("why"), "chapter_confidence": chap_conf or None,

        "subtopic_1_id": topic_ids[0] if topic_ids else None,
        "subtopic_1_name": topic_names[0] if topic_names else None,
        "subtopic_1_why": qtopic.get("why") if topic_ids else None,
        "subtopic_2_id": topic_ids[1] if len(topic_ids) > 1 else None,
        "subtopic_2_name": topic_names[1] if len(topic_names) > 1 else None,
        # QTOPIC writes ONE `why` for its pick; it is not copied onto the second subtopic, because a
        # reason the agent gave for the first is not a reason it gave for the second.
        "subtopic_2_why": None,
        "taxonomy_gap": taxonomy_gap(paper_id, qno),

        "difficulty_level": band or None, "difficulty_steps": steps_count or None,
        "difficulty_step_list": band_steps, "difficulty_why": band_why or None,
        "what_makes_it_hard": band_hard or None,

        "figures": figures, "agent_figures": agent_figures, "option_images": option_images,

        "source_pdf": _posix(q.get("source_pdf")), "page": q.get("page"),
        "question_image": _posix(q.get("question_image")),
        "question_image_cdn": cdn.url_for(q, q.get("question_image")) if q.get("question_image") else None,
        "read_from": source, "read_note": read.get("note") if read else None,
        "text_layer_reliable": q.get("text_layer_reliable", True),
        "needs_image_read": bool(q.get("needs_image_read")),
        "is_key_grid_row": is_key_grid(stem),

        "status": status, "pending": pending,
    }


#: Booklet facts carried into questions.json. `extracted_at` is deliberately NOT one of them: the
#: deliverable must be byte-identical across re-exports, and a date changes it on every new day.
META_FIELDS = ("year", "booklet_code", "booklet_code_from", "family", "layout", "pages",
               "chars_per_page", "option_style", "dpi", "source_pdf", "sha256_16")


def booklet_document(paper):
    """questions.json for one booklet: meta, roll-up counts, every question record (v3 shape).

    question_record() still computes every value -- it is the one place each field is decided --
    and record_v3.build() groups those values into the v3 record (record_v3.py says why)."""
    meta = paper["meta"]
    paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
    flats = [question_record(paper_id, meta, q) for q in paper["questions"]]
    records = [record_v3.build(q, flat, agent_read(paper_id, q["qno"]) or {})
               for q, flat in zip(paper["questions"], flats)]
    counts = collections.OrderedDict([("questions", len(records))])
    for field in ("question", "publisher_solution", "ai_solution", "subject", "chapter",
                  "subtopic", "difficulty", "figures"):
        tally = collections.Counter(r["status"][field] for r in records)
        counts[field] = dict(sorted(tally.items()))
    counts["verdict_answer"] = dict(sorted(collections.Counter(
        r["answer"]["verdict"] for r in records).items()))
    counts["verdict_self"] = dict(sorted(collections.Counter(
        r["solution"]["agrees_with_answer"] for r in records).items()))
    assets = [a for r in records for a in record_v3.assets_in(r)]
    counts["images"] = len(assets)
    counts["images_without_cdn"] = sum(1 for a in assets if not a.get("cdn_url"))
    counts["drawn_figures"] = sum(
        1 for r in records for f in (r["question"]["figures"] + r["solution"]["figures"]
                                     + [o["figure"] for o in r["question"]["options"] if o["figure"]])
        if (f.get("drawn") or {}).get("status") == "drawn")
    counts["number_not_printed"] = [r["qno"] for r in records if not r["question"]["number_printed"]]
    counts["flagged"] = {code: [r["qno"] for r in records if any(f["code"] == code for f in r["flags"])]
                         for code in sorted({f["code"] for r in records for f in r["flags"]})}
    return collections.OrderedDict([
        ("schema", RECORD_SCHEMA), ("paper_code", paper_id),
        ("meta", {k: _posix(meta.get(k)) for k in META_FIELDS}),
        ("render_css", record_v3.RENDER_CSS),
        ("counts", counts), ("questions", records)])


def _write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def write_data(paper):
    """data/<year>/<paper_code>/questions.json + question_paper.html + question_paper.md, fresh
    every run.

    The booklet's folder is cleared first, so nothing from an earlier export survives beside the new
    one, and both files are written with no timestamp and fixed ordering -- running the export twice
    leaves `git status` clean.
    """
    import shutil
    meta = paper["meta"]
    paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
    folder = rc.pp(*DATA, str(meta["year"]), paper_id)
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    document = booklet_document(paper)
    _write_json(os.path.join(folder, "questions.json"), document)
    counts = write_html(paper, os.path.join(folder, "question_paper.html"))
    # the third deliverable, from the same records as the JSON (code/paper_md.py)
    paper_md.write(document, os.path.join(folder, "question_paper.md"))
    return folder, document, counts


#: An option read as "[structure (1) - see figure]": a pointer to a drawing, not printed words
#: (the same test record_v3 applies to the JSON's option text).
OPTION_PLACEHOLDER = re.compile(r"\s*\[[^\]]*(structure|figure|image)[^\]]*\]\s*", re.I)


def option_structures(q):
    """{option key: [(name, svg path)]} -- the structures a checked FIGC card drew for each option
    inside a shared figure (2017_A q052 prints all four options in one panel)."""
    out = collections.defaultdict(list)
    for entry in (q.get("drawn") or {}).values():
        if entry.get("source") != "smiles" or entry.get("status") != "drawn":
            continue
        singles = entry.get("species_svgs") or []
        for n, sp in enumerate((entry.get("card") or {}).get("species") or []):
            m = record_v3.OPTION_LABEL.match(sp.get("label") or "")
            if m and n < len(singles) and singles[n]:
                out[m.group(1)].append((sp.get("name") or "", singles[n]))
    return out


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
    # The figures the card SHOWS: the agent's cuts where it made them, else the geometric crops.
    # Counting only the geometric ones said "6 figures" on a page showing 15 figure questions.
    counts["figures"] += len(q.get("agent_figure_images") or []) or len(q["figures"])

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
    # The record's flags (record_flags) as full sentences, above everything else: a restored
    # opening or a question the publisher itself calls broken must be seen before the question is
    # read. `answers_differ` is left to the answers table, which already marks it.
    sol = publisher_solution(paper_id, q["qno"]) or {}
    warnings = [f["text"] for f in record_flags(q, answer, solved,
                                                 [] if "error" in sol else
                                                 sol.get("solution_stepwise") or [])
                if f["code"] != "answers_differ"]
    parts = ['<div class="q" id="q%03d"><div class="qhead">%s<span class="qno">Q%d</span>'
             '<span class="subj" title="%s">%s</span>%s</div>%s'
             % (q["qno"], paper_chip, q["qno"], html.escape(subj_how), html.escape(subject_label),
                "".join('<span class="flag">%s</span>' % html.escape(f) for f in flags),
                "".join('<div class="warnline">⚠ %s</div>' % html.escape(w) for w in warnings)),
             classification_html(subj, stream, br, chap_names, topic_names, chap_conf,
                                 taxonomy_gap(paper_id, q["qno"]),
                                 *mapping_reasons(paper_id, q["qno"]))]
    parts.append('<div class="pair">')
    # LEFT: what the booklet printed -- the question, and under it the publisher's printed
    # solution, so the whole printed record of the question reads top to bottom in one column.
    left = ['<div class="side"><div class="sidelabel">printed in the booklet</div>']
    if crop and (cdn.url_for(q, crop) or os.path.exists(crop_abs)):
        left.append('<img class="shot" %s alt="printed question %d" loading="lazy">'
                    % (image_attrs(q, crop, out_path, counts), q["qno"]))
    else:
        left.append('<p class="missing">no crop was cut for this question</p>')
    sol_crop = q.get("solution_image")
    if sol_crop and (cdn.url_for(q, sol_crop) or os.path.exists(rc.pp(*CORPUS, sol_crop))):
        left.append('<div class="sidelabel solshot">publisher&rsquo;s solution, as printed</div>'
                    '<img class="shot" %s alt="printed solution %d" loading="lazy">'
                    % (image_attrs(q, sol_crop, out_path, counts), q["qno"]))
        counts["solution_shots_shown"] += 1
    left.append("</div>")
    parts.append("".join(left))
    # RIGHT: what we extracted
    parts.append('<div class="side"><div class="sidelabel">%s</div>'
                 % ("READ FROM THE IMAGE by b3-question-reader" if source == "agent"
                    else "text-layer draft &mdash; not the record"))
    # The figures this question owns. The agent's crop wins: it was cut from a box the agent
    # reported while reading, where the geometric crops come from clustering vector paths and
    # under-count. Built here, before the stem, because a stem with lettered parts needs them.
    figure_html = []
    for image in (q.get("agent_figure_images") or []):
        attrs = image_attrs(q, image, out_path, counts)
        figure_html.append(
            '<img %s alt="figure for question %d" loading="lazy">'
            '<figcaption>printed figure (%s) &middot; <code>%s</code>'
            '</figcaption>%s' % (attrs, q["qno"],
                                 # a raster-printed figure (2016_A) has no vector twin: its PNG is the copy
                                 "exact vector copy" if (q.get("vector") or {}).get(image)
                                 else "cut from the booklet",
                                 html.escape(_posix(image)),
                                 drawn_html(q, image, out_path, counts)))
    # ...and the agent's per-option crops win too, as `superseded_by_agent` already says in the
    # JSON: 2019_P1 q065 showed its options 3 and 4 a second time as geometric "option panels",
    # the second cut off before its "CH2Cl + H2O".
    if not figure_html and not q.get("agent_option_images"):
        for figure in q["figures"]:
            image = figure.get("image")
            if not image:
                continue
            attrs = image_attrs(q, image, out_path, counts)
            figure_html.append(
                '<img %s alt="%s figure for question %d" loading="lazy">'
                '<figcaption>%s, found by geometry &middot; <code>%s</code>'
                '</figcaption>' % (attrs, figure["role"], q["qno"],
                                   figure["role"], html.escape(_posix(image))))
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
        if read_now.get("list_i"):
            counts["match_list_rebuilt"] += 1
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
            cls = ' class="key"' if key in accepted(answer) else ""
            image = option_images.get(key)
            if image:
                attrs = image_attrs(q, image, out_path, counts)
                # The option's printed WORDS stay with its drawing: 2017_A q080 prints a structure
                # AND "and cine substitution reaction" -- half of what each option claims.
                words = options.get(key) or ""
                words = "" if PICTURE_OPTION.match(words.strip()) else words
                # ...but not the reader's "[structure: ...]" notes about the drawing (2018_AA q052)
                card = ((q.get("drawn") or {}).get(image) or {}).get("card") or {}
                words = record_v3.option_words(words, len(card.get("species") or []), True)
                cell = ('<img class="optimg" %s alt="option %s of question %d" '
                        'loading="lazy">%s%s' % (attrs, key, q["qno"],
                                                 drawn_html(q, image, out_path, counts),
                                                 '<div class="opttext">%s</div>'
                                                 % texhtml.to_html(words) if words.strip() else ""))
            else:
                cell = texhtml.to_html(options[key]) or "<em>(blank)</em>"
            items.append("<li%s>%s</li>" % (cls, cell))
        parts.append('<ol class="opts pics">%s</ol>' % "".join(items))
        counts["option_crops_shown"] += 1
        if option_images:
            counts["picture_options"] += 1
        # The whole-group strip is redundant once every option is cut out of it.
        figure_html = [f for f in figure_html if "q%03d.png" % q["qno"] not in f]
    elif options and option_structures(q) and all(
            OPTION_PLACEHOLDER.fullmatch(v or "") for v in options.values()):
        # Each option's own structure, cut from the drawing checked against its SMILES, with its
        # name -- not "(1) [structure (1) - see figure]" four times.
        drawn_opts = option_structures(q)
        items = []
        for key in "1234":
            if key not in options:
                continue
            cls = ' class="key"' if key in accepted(answer) else ""
            cell = "".join('<img class="optimg" %s alt="option %s of question %d" loading="lazy">'
                           '<div class="opttext">%s</div>'
                           % (image_attrs(q, svg, out_path, counts), key, q["qno"], html.escape(name))
                           for name, svg in drawn_opts.get(key, [])) or texhtml.to_html(options[key])
            items.append("<li%s>%s</li>" % (cls, cell))
        parts.append('<ol class="opts pics">%s</ol>' % "".join(items))
        counts["picture_options"] += 1
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
            cls = ' class="key"' if key in accepted(answer) else ""
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
    parts.append(solutions_html(paper_id, q, options, answer, solved, confidence, out_path,
                                counts))
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
        parts.append('<p class="why">solver reasoning: %s</p>' % texhtml.to_html(str(why)))

    src = q.get("source_pdf") or ""
    # Resolved INSIDE the repo. This link used to point into the owner's Downloads folder, which
    # made it dead for every other reader and printed that folder's structure to anyone who opened
    # the page. The shareable builds strip it; it now resolves for anyone who has the repo.
    # RELATIVE to the page, like every local image src: an absolute file://C:\Users\... link
    # opened only on the machine that built the page.
    src_abs = os.path.join(rc.source_dir(), src) if src else ""
    src_href = ""
    if src_abs and os.path.exists(src_abs):
        src_href = urllib.parse.quote(_posix(os.path.relpath(src_abs, os.path.dirname(
            os.path.abspath(out_path)))))
    parts.append(
        '<div class="meta">page %d &middot; printed answer %s'
        '%s%s</div>'
        % (q["page"], html.escape(answer or "none"),
           ' &middot; <a href="%s#page=%d">open source PDF at this page</a>'
           % (html.escape(src_href), q["page"]) if src_href else "",
           ' &middot; <code>%s</code>' % html.escape(os.path.basename(src)) if src else ""))
    parts.append("</div></div>")      # close .side (extracted) and .pair
    parts.append("</div>")            # close .q
    card = "".join(parts)
    # one card is checked as a whole, so a failed check withholds every drawing on it: say it once
    at = card.find(WITHHELD_NOTE)
    if at >= 0:
        end = at + len(WITHHELD_NOTE)
        card = card[:end] + card[end:].replace(WITHHELD_NOTE, "")
    return card


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
        ("images NOT yet on the CDN", counts["images_local"]),
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
        "<style>%s%s</style>" % (meta["year"], meta["booklet_code"] or "NA", CSS, SOLUTION_CSS))
    page = (
        '%s<div class="wrap"><h1>NEET (UG) %s &middot; Code %s</h1>'
        '<div class="sub">extraction v2 from <code>%s</code> &middot; family <b>%s</b> &middot; '
        '%d pages &middot; %d chars/page &middot; rendered at %d dpi<br>'
        'Flags are shown, not hidden: this page exists to find extraction faults, so a short option '
        'list or a missing answer is marked rather than tidied away. Text labelled <b>read from '
        'the image</b> is b3-question-reader&rsquo;s read and is the record; anything still on the '
        '<b>text-layer draft</b> says so on its card. '
        'Each question shows the crop cut straight from the booklet on the LEFT and what was '
        'extracted on the RIGHT, so the two can be read against each other line by line.</div>'
        '<div class="stats">%s</div>%s</div>'
        % (head, meta["year"], meta["booklet_code"] or "NA", html.escape(meta["source_pdf"]),
           meta["family"], meta["pages"], meta["chars_per_page"], meta["dpi"],
           "".join('<div class="stat"><b>%d</b><span>%s</span></div>' % (v, k) for k, v in stats),
           "".join(body)))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(page)
    return counts


#: The two solution blocks. Tokens only from the page's own palette (`--rule`, `--ink2`), so they
#: follow its light and dark themes; nothing is loaded from outside the file.
SOLUTION_CSS = (
    ".sol{margin:12px 0;padding:10px 12px;border:1px solid var(--rule);border-radius:6px}"
    ".sol.pub{border-left:4px solid #b7791f}.sol.ai{border-left:4px solid #2b6cb0}"
    ".solhead{font-weight:600;font-size:13px;display:flex;justify-content:space-between;"
    "gap:8px;margin-bottom:6px}.solhead span{font-weight:400;color:var(--ink2)}"
    ".steps{margin:4px 0 4px 20px;padding:0}.steps li{margin:3px 0}"
    ".concl{margin:6px 0 0}.draftlabel{font-size:12px;color:#b7791f;margin:2px 0}"
    ".drawn{margin:4px 0 8px;font-size:12px;color:var(--ink2)}.drawn summary{cursor:pointer}"
    ".drawn img{display:block;max-width:min(100%,30em);height:auto;background:#fff;margin-top:4px;"
    "border:1px dashed var(--rule);border-radius:4px;padding:4px}.drawn .bad{color:#c02a2a}"
    ".stepfig{margin:6px 0 8px}.stepfig img{max-width:min(100%,30em);height:auto;background:#fff;"
    "border:1px solid var(--rule);border-radius:4px;padding:4px}"
    ".solsrc{margin-top:8px;font-size:12px;color:var(--ink2)}.solsrc summary{cursor:pointer}"
    ".draftsol{font-size:13px;color:var(--ink2)}.solimg img{max-width:100%;height:auto;"
    "border:1px solid var(--rule);border-radius:4px;background:#fff}")


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
    ap.add_argument("--json", action="store_true",
                    help="exports/json/questions_v2_all.json: every record, section-11 shape")
    ap.add_argument("--data", action="store_true",
                    help="data/<year>/<paper_code>/questions.json + question_paper.html")
    ap.add_argument("--allow-latex-gaps", action="store_true",
                    help="write data/ even when the LaTeX census finds unrenderable text")
    ap.add_argument("--paper-id")
    args = ap.parse_args()
    if not (args.csv or args.html or args.json or args.data):
        ap.error("pass --csv, --html, --json and/or --data")

    papers = load(args.paper_id)
    if not papers:
        print("no v2 papers found -- run code/extract_paper_v2.py --apply first")
        return 1

    # FRESH OUTPUT. A full export replaces what it writes -- the CSV folder, the HTML folder, or both
    # -- rather than writing over it, so a booklet dropped from the corpus does not leave its old page
    # and CSV behind looking current. A one-booklet export replaces only that booklet's files.
    if not args.paper_id:
        import shutil
        for wanted, name in ((args.csv, "csv"), (args.html, "html")):
            folder = rc.pp(*CORPUS, "exports", name)
            if wanted and os.path.isdir(folder):
                shutil.rmtree(folder)
                print("cleared %s (previous export)" % os.path.relpath(folder, rc.pp()))

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

    if args.json:
        records = []
        for paper in papers:
            records += booklet_document(paper)["questions"]
        out = rc.pp(*CORPUS, "exports", "json", "questions_v2_all.json")
        _write_json(out, {"schema": RECORD_SCHEMA, "questions": records})
        print("json  %-52s %d records" % (os.path.relpath(out, rc.pp()), len(records)))

    if args.data:
        # THE LATEX GATE. A command the renderer does not know prints red, and on 2017 Code-A `\ge`
        # shipped that way inside a printed solution because nothing stopped it. The deliverable is
        # not written while any field would render a gap; --allow-latex-gaps writes it anyway, for a
        # draft that is knowingly incomplete.
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
        import latex_census
        blocked = False
        for paper in papers:
            pid = "%s_%s" % (paper["meta"]["year"], paper["meta"]["booklet_code"] or "NA")
            unknown, raw, examples = latex_census.census(pid)
            if unknown or raw:
                blocked = True
                print("LATEX GATE  %s: %d unknown command(s), %d raw leak(s) -- e.g. %s"
                      % (pid, sum(unknown.values()), sum(raw.values()),
                         examples[next(iter(unknown or raw))]))
        if blocked and not args.allow_latex_gaps:
            print("data/ NOT written. Fix lib/texhtml.py (run code/checks/latex_census.py "
                  "--paper-id <id> for the full list) or pass --allow-latex-gaps.")
            return 1
        for paper in papers:
            folder, document, counts = write_data(paper)
            print("data  %-52s %d questions, %d image(s) without a CDN link"
                  % (os.path.relpath(folder, rc.pp()), len(document["questions"]),
                     document["counts"]["images_without_cdn"]))

    if args.html:
        summaries, local_only = [], 0
        for paper in papers:
            meta = paper["meta"]
            paper_id = "%s_%s" % (meta["year"], meta["booklet_code"] or "NA")
            out = rc.pp(*CORPUS, "exports", "html", "%s.html" % paper_id)
            counts = write_html(paper, out)
            local_only += counts["images_local"]
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
        if local_only:
            print("WARNING  %d image(s) on these pages are LOCAL paths, not CDN links -- run "
                  "code/upload_paper_assets.py, then export again" % local_only)
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
