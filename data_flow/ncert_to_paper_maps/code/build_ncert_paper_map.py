"""Build `ncert_paper_map` -- the papers_v2 question card with its NCERT evidence appended.

WHY IT RENDERS THROUGH THE PAPER EXPORT'S OWN CODE
--------------------------------------------------
A first version of this page drew its own compact cards and was rejected, correctly. The reader of
this page is the reader of the paper export doing the same checking in the same order: look at the
printed crop, read what was extracted from it, check the classification, then check the evidence. A
different layout here means re-learning the page, and worse, means two renderings of the same record
that drift apart silently -- the drift then reads as the DATA disagreeing when only the drawing of it
does. So the card is `export_paper_v2.question_card`, imported, and the shell is its `page_shell`.

WHAT THIS PAGE ADDS
-------------------
One block the paper export has no business carrying, appended INSIDE each card:

  NEW NCERT     the printed page image of the page the quote came from, beside that passage's
                extracted text with the quoted lines HIGHLIGHTED inside it
  OLD NCERT     the same for the older edition, which is where a 2015 or 2016 paper's evidence
                often has to come from, the 2023 rationalisation having cut the section
  STATUS        verified / partial / pending / not-in-this-edition

HIGHLIGHTING IS THE POINT, AND IT IS ALSO A CHECK
-------------------------------------------------
A quote printed beside a page image proves nothing on its own -- the reader still has to find it on
the page. Marking it inside the extracted text is what makes the claim checkable at a glance. It
also checks us: the highlighter can only mark a span it actually finds, so a quote that has drifted
from the book shows up as an unmarked passage carrying a warning, rather than as a confident claim.

THE PAGE IS PINNED WHITE
------------------------
Everything judged here is black ink on white paper -- booklet crops and NCERT page scans. On a dark
ground those float as cut-outs and the page reads as two documents stapled together.
"""

import argparse
import collections
import csv
import glob
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import runner_core as rc                                      # noqa: E402
import export_paper_v2 as paper                               # noqa: E402
from lib import texhtml                                       # noqa: E402

WORK = ("steps", "D4V", "work")
OUT = ("steps", "D4V", "out")
QCA_OUT = ("steps", "QCA", "out")
A2_WORK = ("steps", "A2", "work")
A2_OUT = ("steps", "A2", "out")
TARGET_DIR = ("ncert_book_mapping",)
CORPUS = ("papers_v2",)

#: Sections the 2023 rationalisation removed from a chapter that otherwise survives. A question on
#: one of these can never have latest-edition evidence, which is a fact about the BOOK and not a gap
#: in our extraction -- so it is reported as `cut`, not as `missing`. See `status_for`.
CUT_SECTIONS = {
    "Current Electricity": {"potentiometer": "3.15 Potentiometer",
                            "meter bridge": "3.14 Meter Bridge"},
}


def questions(chapters, papers, staged_only=True):
    """The CSV rows for every question in scope, in paper then question order.

    `staged_only` keeps the page to the questions that ARE IN THE EVIDENCE STAGE -- the ones with a
    D4V input, i.e. whose chapter is extracted. Without it the page is 93% rows that say "this
    chapter has no NCERT passages yet", which buries the 70 questions a reader came to check.
    """
    rows = []
    for path in sorted(glob.glob(rc.pp(*CORPUS, "exports", "csv", "*.csv"))):
        if "questions_v2" in os.path.basename(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                names = [n.strip() for n in (row["chapter_names"] or "").split(";") if n.strip()]
                if chapters and not any(n in chapters for n in names):
                    continue
                if papers and row["paper_id"] not in papers:
                    continue
                item = "%s__q%03d" % (row["paper_id"], int(row["qno"]))
                # Staged means "this question is IN one of the two evidence routes" -- it has a D4V
                # input (its chapter is extracted and a quote is being sought) or it has a QCA
                # record (its route is a concept instead). Testing only for the D4V input silently
                # dropped every physics question, because the routing change stopped building D4V
                # inputs for them: 89 concept records existed and none could reach the page.
                if staged_only and not (
                        os.path.exists(rc.pp(*WORK, "%s.runA.input.json" % item))
                        or os.path.exists(rc.pp(*QCA_OUT, "%s.runA.json" % item))):
                    continue
                rows.append(row)
    return rows


def _load(folder, item, suffix=".runA.json"):
    path = rc.pp(*folder, "%s%s" % (item.replace("#", "__"), suffix))
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except ValueError:
        return None
    return None if isinstance(data, dict) and "error" in data else data


def highlight(text, quotes):
    """(marked-up text, quotes actually found). Whitespace-insensitive, otherwise exact.

    Insensitive to whitespace because the extracted text wraps where the book wraps, so a quote
    lifted from it may carry a newline the agent did not reproduce. Exact in every other respect:
    no fuzzy matching and no partial credit, because a quote that is not in the book has to show as
    absent rather than be bent until it matches.
    """
    marked, found = html.escape(text), []
    for quote in quotes:
        quote = (quote or "").strip()
        if len(quote) < 12:
            continue
        target = re.compile(r"\s+".join(re.escape(w) for w in html.escape(quote).split()))
        match = target.search(marked)
        if match:
            marked = (marked[:match.start()] + "<mark>" + match.group(0) + "</mark>"
                      + marked[match.end():])
            found.append(quote)
    return marked, found


def page_image(passage_id, page, out_dir):
    """Relative path to that NCERT page's rendered image, or None.

    `BIO12L-CH04-P39` + printed page 39 -> `steps/A2/work/BIO12L-ch04-p039.png`.
    """
    match = re.match(r"([A-Z]{3}\d{2}[LO])-CH(\d+)-P", passage_id or "")
    if not match or not page:
        return None
    path = rc.pp(*A2_WORK, "%s-ch%02d-p%03d.png"
                 % (match.group(1), int(match.group(2)), int(page)))
    return os.path.relpath(path, out_dir) if os.path.exists(path) else None


def passage_from_book(passage_id):
    """One passage read straight out of `ncert/passages/<BOOK>.jsonl`, or None.

    WHY THE SHORTLIST IS NOT ENOUGH TO RENDER FROM
    ----------------------------------------------
    The evidence agent may now quote a passage it FETCHED from the book when the ranked shortlist
    did not carry the one that settles the question -- a change made because nine of twelve agents
    reported, and three proved, that the decisive passage was routinely ranked out of the top
    fifteen. Eleven questions moved from `not_at_all` or `partly` to `fully` on exactly that.

    This page was still looking those quotes up in the shortlist alone. So a card could say
    "verified against NCERT", name the link type, and then show NO NCERT at all -- `2016_X q077`
    is quoted from `BIO12L-CH04-P88`, fetched from the book, and rendered as an empty section. The
    claim was right and the page silently dropped its evidence, which is the worst of both.
    """
    match = re.match(r"([A-Z]{3}\d{2}[LO])-CH\d+-P", passage_id or "")
    if not match:
        return None
    path = rc.pp("ncert", "passages", "%s.jsonl" % match.group(1))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get("passage_id") == passage_id:
                return {"passage_id": passage_id,
                        "section_heading": row.get("section_heading") or "",
                        "page_start": row.get("page_start"),
                        "text": row.get("text") or ""}
    return None


def older_chapter_titles(book):
    """{chapter number: printed chapter title} for one book, read off its A2 page reads.

    WHY THE OLDER EDITION'S CHAPTER NUMBER CANNOT BE ASSUMED
    -------------------------------------------------------
    The editions RENUMBER. `Principles of Inheritance and Variation` is Chapter 4 of the latest
    Class XII Biology and Chapter 5 of the older one, because the rationalisation removed a chapter
    ahead of it. Looking up the same number in the older book therefore fetches a different chapter
    entirely -- for this very question it would have shown `Reproductive Health` and labelled it the
    older edition of a genetics page. A wrong page presented as evidence is worse than no page.

    The title is read from the chapter's own first page, where NCERT prints `CHAPTER 5` followed by
    the title as two heading blocks. That is the book stating its own numbering, which is the only
    source that cannot drift.
    """
    titles = {}
    for path in sorted(glob.glob(rc.pp(*A2_OUT, "%s-ch*-p001.runA.json" % book))):
        match = re.search(r"-ch(\d+)-p001", path)
        if not match:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        headings = [(b.get("text") or "").strip() for b in (data.get("blocks") or [])
                    if b.get("kind") == "heading"]
        # The first heading is "CHAPTER N"; the title is the next one that is not.
        title = next((h for h in headings if h and not re.match(r"(?i)^chapter\b", h)), "")
        if title:
            titles[int(match.group(1))] = title
    return titles


def older_chapter_numbers(book, chapter_numbers, chapter_title):
    """The older edition's number(s) for a chapter, matched BY TITLE. Empty when it cannot be told.

    Returning EMPTY rather than the latest edition's number is the whole point. Measured: the older
    Class XII Biology's chapter 4 is `REPRODUCTIVE HEALTH`, so falling back to the number on a
    `Principles of Inheritance and Variation` question would print a reproductive-health page and
    label it that question's older-edition evidence. Showing nothing is correct; showing the wrong
    page as evidence is not recoverable by a reader, because the page looks authoritative.

    The number is only reused when the older book has no title information at all -- i.e. nothing of
    it is extracted yet, so there is no claim being made either way.
    """
    old = older_book(book)
    if not old:
        return []
    titles = older_chapter_titles(old)
    if not titles:
        return []                       # nothing extracted: say nothing
    if not chapter_title:
        return []                       # no title to match on: do not guess a number
    wanted = re.sub(r"[^a-z]", "", chapter_title.lower())
    return [number for number, title in titles.items()
            if wanted and wanted == re.sub(r"[^a-z]", "", title.lower())]


def older_book(book):
    """The older-edition book id for a latest-edition one: `BIO12L` -> `BIO12O`."""
    return book[:-1] + "O" if book and book.endswith("L") else None


def status_for(row, evidence, inp):
    if concept_only(row):
        record = concept_approach(row["paper_id"], int(row["qno"]))
        if record.get("concept"):
            return "concept", "concept and approach recorded"
        return "pending", "concept and approach not recorded yet"
    chapter = (row["chapter_names"] or "").split(";")[0].strip()
    subtopics = [t.strip().lower() for t in (row["topic_names"] or "").split(";") if t.strip()]
    for needle, section in (CUT_SECTIONS.get(chapter) or {}).items():
        if any(needle in t for t in subtopics):
            return "cut", "cut from the new edition &mdash; NCERT &sect;%s, removed 2023" % section
    if evidence:
        return {"fully": ("verified", "verified against NCERT"),
                "partly": ("partial", "partly supported by NCERT")}.get(
                    evidence.get("supports_answer"),
                    ("missing", "no supporting line found in this chapter"))
    if inp and inp.get("passages"):
        return "pending", "NCERT passages ready &mdash; line not quoted yet"
    return "missing", "no NCERT passages for this chapter yet"


EXTRA_CSS = """
/* =============================================================================================
   THE SYSTEM

   Four colour roles, each carrying meaning, and nothing coloured for decoration:

     SUBJECT  one hue per subject, as a three-step ramp (deep / mid / soft). It drives the card's
              rail, its paper chip, its section numerals and its header wash. 155 cards deep, a
              reader wants to know what KIND of question this is before reading a word of it, and
              subject is a fact about the question rather than a choice about the card.
     STATUS   semantic, and only on the pills: verified, partial, concept, cut, pending, missing.
     AXES     the five E-axes keep five fixed hues, so E3 looks the same on every card.
     QUOTE    one amber, used nowhere else, so a highlight can never be read as styling.

   GROUND vs CARD. The page takes a soft slate tint and the cards stay pure white, lifted off it.
   That split is not taste: what is judged here is black ink on white paper -- booklet crops and
   NCERT page scans -- and a scan needs white behind it or it reads as a cut-out. Tinting the page
   gives the design somewhere to breathe without touching the evidence.

   TYPE. Three voices, each with one job. A serif for anything being READ (question stems, NCERT
   prose, the concept) because that is continuous reading. A sans for structure and labels. A
   monospace for identifiers -- passage ids, paper codes, page numbers -- which are looked up rather
   than read, and want fixed widths.

   SPACING. One scale, used everywhere: 6, 9, 14, 20, 28, 42.
   ============================================================================================= */
:root{
  --ink:#11151d; --ink2:#4c5460; --ink3:#78808d;
  --rule:#d2d9e5; --rule2:#e4e9f1;
  --card:#fff; --paper:#fff; --tint:#eff3f9;
  --ground:#dfe5f0;                               /* the page ground -- see note at --ground below */
  --accent:#1d3156; --accent-mid:#2f4c7d; --accent-soft:#e3eaf5;
  --ok:#0d5239; --ok-soft:#e0efe7; --ok-edge:#a6d2bd;
  --warn:#71500a; --warn-soft:#f8eed6; --warn-edge:#ddc382;
  --cut:#573670; --cut-soft:#efe8f4;
  --info:#244568; --info-soft:#e3ebf4;
  --quote:#ffdf85; --quote-edge:#c79f2c;
  --serif:ui-serif,Georgia,"Iowan Old Style","Times New Roman",serif;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;
}
/* Each subject's ramp. `deep` carries weight (rails, chips), `mid` carries text, `soft` is a wash. */
.s-bio{--accent:#0d4e32;--accent-mid:#166845;--accent-soft:#dfeee6}
.s-phy{--accent:#1d3156;--accent-mid:#2f4c7d;--accent-soft:#e3eaf5}
.s-che{--accent:#653f08;--accent-mid:#875611;--accent-soft:#f6ecda}

body{background:var(--ground);font-variant-numeric:tabular-nums}
.wrap{max-width:1560px;padding:32px 32px 110px}
/* The page opens with its own identity rather than an empty margin: the three subject hues, quiet. */
.wrap::before{content:"";display:block;height:4px;border-radius:99px;margin:0 0 28px;
 background:linear-gradient(90deg,#0d4e32 0 33%,#1d3156 33% 66%,#653f08 66% 100%)}

/* THE INDEX: what is on this page, and one click to any card. ---------------------------------- */
.index{margin:0 0 48px;padding:26px 28px;border:1px solid var(--rule);border-radius:12px;
 background:var(--card);box-shadow:0 1px 2px rgba(20,30,54,.05),0 12px 30px -18px rgba(20,30,54,.30)}
.legend{display:flex;flex-wrap:wrap;gap:9px;margin-bottom:20px}
.lchip{font:650 11.5px/1 var(--sans);padding:8px 13px;border-radius:99px;
 border:1px solid currentColor;letter-spacing:.005em}
.lchip.verified{color:var(--ok);background:var(--ok-soft)}
.lchip.concept{color:var(--info);background:var(--info-soft)}
.lchip.partial{color:var(--warn);background:var(--warn-soft)}
.lchip.cut{color:var(--cut);background:var(--cut-soft)}
.lchip.pending{color:var(--info);background:var(--info-soft)}
.lchip.missing{color:var(--ink2);background:var(--tint)}
.igroup{margin-top:20px;padding-top:16px;border-top:1px solid var(--rule2)}
.igroup:first-of-type{margin-top:0;padding-top:0;border-top:0}
.ihead{display:flex;align-items:baseline;gap:9px;margin-bottom:9px;
 font:700 10.5px/1.4 var(--sans);letter-spacing:.15em;text-transform:uppercase;color:var(--accent)}
.ihead b{font:600 11.5px/1.4 var(--mono);color:var(--ink3);letter-spacing:0}
.ichips{display:flex;flex-wrap:wrap;gap:6px}
.ichip{display:inline-flex;align-items:center;gap:7px;text-decoration:none;
 font:600 11.5px/1 var(--mono);color:var(--ink2);
 padding:7px 10px;border:1px solid var(--rule);border-radius:7px;background:var(--tint);
 transition:border-color .12s,background .12s,color .12s}
.ichip:hover{border-color:var(--accent);background:var(--accent-soft);color:var(--accent)}
.idot{width:7px;height:7px;border-radius:50%;background:var(--ink3);flex:none}
.ichip.verified .idot{background:var(--ok)}
.ichip.concept .idot{background:var(--info)}
.ichip.partial .idot{background:var(--warn)}
.ichip.cut .idot{background:var(--cut)}
.ichip.pending .idot{background:var(--info)}
.ichip.missing .idot{background:#c3c9d2}

/* THE CARD ------------------------------------------------------------------------------------ */
.q{margin:0 0 56px;padding:0 0 34px;background:var(--card);
 border:1px solid var(--rule);border-left:4px solid var(--accent);border-radius:12px;
 box-shadow:0 1px 2px rgba(20,30,54,.05),0 12px 30px -18px rgba(20,30,54,.30);
 overflow:hidden;scroll-margin-top:8px}
.q:target{box-shadow:0 0 0 3px var(--accent-soft),0 0 0 4px var(--accent)}

/* HEADER BAND: who this question is, and what state it is in. Sticky, because a card runs several
   screens and a reader deep in the E1-E5 cards otherwise cannot tell which question they are in. */
.qhead{display:flex;align-items:center;gap:13px;flex-wrap:wrap;margin:0;padding:18px 30px;
 background:linear-gradient(180deg,var(--accent-soft),color-mix(in srgb,var(--accent-soft) 45%,#fff));
 border-bottom:1px solid var(--rule);position:sticky;top:0;z-index:5}
.paperid{font:700 11.5px/1 var(--mono);letter-spacing:.06em;padding:7px 11px;border-radius:6px;
 background:var(--accent);color:#fff}
.qno{font:800 19px/1 var(--sans);color:var(--ink);letter-spacing:-.015em}
.qhead .subj{font:650 11px/1 var(--sans);letter-spacing:.11em;color:var(--accent);
 border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);background:transparent}
.qhead .evstat{margin-left:auto}
.qhead .flag{background:var(--warn-soft);color:var(--warn);border-color:var(--warn-edge)}

/* SUMMARY STRIP: the whole question in one row, so a page of cards can be scanned. */
.strip{display:flex;flex-wrap:wrap;gap:0;margin:0;padding:18px 30px;background:var(--card);
 border-bottom:1px solid var(--rule)}
.chip2{display:flex;flex-direction:column;gap:6px;padding:0 26px 0 0;margin-right:26px;
 border-right:1px solid var(--rule2)}
.chip2:last-child{border-right:0;margin-right:0;padding-right:0}
.chiplab{font:700 10px/1.3 var(--sans);letter-spacing:.14em;text-transform:uppercase;
 color:var(--ink3)}
.chipval{font:600 15.5px/1.35 var(--sans);color:var(--ink);letter-spacing:-.005em}

/* SECTION BARS: nothing used to say where one kind of claim stopped and the next began. */
.sec{display:flex;align-items:baseline;gap:13px;flex-wrap:wrap;margin:36px 30px 18px;
 padding-top:24px;border-top:1px solid var(--rule2)}
.sec:first-of-type{border-top:0;padding-top:0}
.secno{flex:none;width:23px;height:23px;border-radius:50%;background:var(--accent);color:#fff;
 font:700 12px/23px var(--sans);text-align:center;letter-spacing:0;
 box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 12%,transparent)}
.sectitle{font:700 17px/1.3 var(--sans);color:var(--ink);letter-spacing:-.012em}
.secblurb{font:400 12.5px/1.55 var(--sans);color:var(--ink2);flex:1 1 18em;min-width:12em}
.pair,.duo,.place,.cats,.ncert{margin-left:30px;margin-right:30px}
/* Placement runs full width now that the answer table is gone from beside it: its reasons are
   sentences, and a sentence in a half-width column wraps four times. */
.placegrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:36px;
 align-items:start}
@media (max-width:900px){.placegrid{grid-template-columns:1fr}}

/* ACROSS, NOT DOWN. The answer and placement tables are narrow; stacking them full width is what
   made a card metres tall. */
.duo{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.45fr);gap:36px;align-items:start}
@media (max-width:760px){.duo{grid-template-columns:1fr}}
.duocell{min-width:0}
.duocell .sec{margin:0 0 14px;padding-top:0;border-top:0}
.pair{grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:36px}
.sidelabel{font:700 10px/1.5 var(--sans);letter-spacing:.15em;text-transform:uppercase;
 color:var(--ink3);border-bottom:1px solid var(--rule2);padding-bottom:7px;margin-bottom:11px}
.stem{font-family:var(--serif);font-size:15.5px;line-height:1.6}
ol.opts{font-family:var(--serif);font-size:15px;line-height:1.75}

/* TABLES: one rhythm. Identifiers in mono, labels small and quiet, values plain. */
table.classify{font-size:14.5px}
table.classify th{font:700 10.5px/1.5 var(--sans);letter-spacing:.14em;text-transform:uppercase;
 color:var(--ink3);text-align:left;padding:9px 22px 9px 0;white-space:nowrap;vertical-align:top}
table.classify td{padding:10px 0;vertical-align:top;line-height:1.65}
table.answers{font-size:13px}
table.answers th{font:700 9.5px/1.5 var(--sans);letter-spacing:.15em;text-transform:uppercase;
 color:var(--ink3);text-align:left;padding:0 18px 7px 0}
table.answers td{padding:8px 18px 8px 0;font-size:15px;font-weight:600}
table.answers.mismatch{background:var(--warn-soft);box-shadow:inset 3px 0 0 var(--warn)}

/* E1-E5: five fixed hues, cards sized to their own content. */
/* E1-E4 are a label and a definition each; E5 is a LIST of per-option reasoning and runs four or
   five times longer. Giving all five equal columns made E5 a tower beside four stubs, with a
   screen of white under them. E5 now spans the row beneath, where its reasoning reads as prose. */
.cats{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));align-items:start;
 gap:16px}
@media (max-width:1180px){.cats{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.cats{grid-template-columns:1fr}}
.axis-card:nth-child(5){grid-column:1/-1}
/* Its per-option rows sit side by side rather than stacked, for the same reason. */
.axis-card:nth-child(5) .axis-body{display:grid;grid-template-columns:repeat(auto-fit,minmax(21em,1fr));
 gap:18px 26px}
.axis-card{height:auto;border:1px solid var(--rule);border-left-width:3px;border-radius:9px;
 background:var(--card);padding:16px 18px 18px}
.axis-card:nth-child(1){border-left-color:#225679;background:linear-gradient(180deg,#eaf2f8,#fff 65%)}
.axis-card:nth-child(2){border-left-color:#166845;background:linear-gradient(180deg,#e7f3ec,#fff 65%)}
.axis-card:nth-child(3){border-left-color:#8a5f0b;background:linear-gradient(180deg,#f8efdb,#fff 65%)}
.axis-card:nth-child(4){border-left-color:#573670;background:linear-gradient(180deg,#f1eaf5,#fff 65%)}
.axis-card:nth-child(5){border-left-color:#813434;background:linear-gradient(180deg,#f7e9e9,#fff 65%)}
.axis-card .axis{background:var(--card);font-family:var(--mono)}
.axis-card:nth-child(1) .axis{color:#225679;border-color:#225679}
.axis-card:nth-child(2) .axis{color:#166845;border-color:#166845}
.axis-card:nth-child(3) .axis{color:#8a5f0b;border-color:#8a5f0b}
.axis-card:nth-child(4) .axis{color:#573670;border-color:#573670}
.axis-card:nth-child(5) .axis{color:#813434;border-color:#813434}
.axis-name{font:700 13.5px/1.4 var(--sans);color:var(--ink)}
.axis-means{font:400 12.5px/1.5 var(--sans);color:var(--ink3)}
.label{font-family:var(--mono);font-size:13.5px}
.means{font:400 13.5px/1.58 var(--sans);color:var(--ink2)}
.means b,.because b{font:700 9.5px/1.7 var(--sans);letter-spacing:.15em;color:var(--ink3)}

/* CONCEPT AND APPROACH: for physics and physical chemistry these two lines ARE the record, so they
   are set to be read first and read as prose. */
.concept{margin:14px 0 0;padding:18px 20px;border:1px solid var(--rule);
 border-left:3px solid var(--accent);border-radius:10px;
 background:linear-gradient(180deg,var(--accent-soft),#fff 70%);display:grid;gap:12px}
.crow{display:grid;grid-template-columns:7.5em minmax(0,1fr);gap:16px;align-items:baseline}
.clab{font:700 9.5px/1.8 var(--sans);letter-spacing:.17em;text-transform:uppercase;
 color:var(--accent)}
.cval{font:600 19px/1.45 var(--serif);color:var(--ink);letter-spacing:-.005em}
.capp{font:400 14.5px/1.65 var(--serif);color:var(--ink)}

/* NCERT: the printed page beside its own text, new edition above old. */
.ncert h4{font:700 10px/1.4 var(--sans);letter-spacing:.17em;text-transform:uppercase;
 color:var(--ink3);margin:20px 0 9px}
.ncert h4:first-of-type{margin-top:6px}
.edition{min-width:0;border:1px solid var(--rule);border-radius:10px;padding:20px 22px 22px;
 margin-bottom:22px;background:linear-gradient(180deg,var(--tint),#fff 50%)}
.edition h4{margin-top:0;color:var(--accent)}
.edrow{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:22px;align-items:start}
@media (max-width:900px){.edrow{grid-template-columns:1fr}}
.edshot,.edtext{min-width:0}
.pageimg{width:100%;height:auto;border:1px solid var(--rule);border-radius:7px;background:#fff;
 box-shadow:0 2px 10px -6px rgba(20,30,54,.4)}
.where{display:block;font:600 10.5px/1.6 var(--mono);color:var(--ink3);margin-bottom:6px;
 letter-spacing:.02em}
/* NO SCROLLBOX. A capped, scrolling passage can hide the highlighted quote entirely -- the one
   thing on the page that must be seen -- and on paper it simply ends mid-sentence. Shown whole. */
.passage{font:400 14.5px/1.74 var(--serif);white-space:pre-wrap;overflow-wrap:anywhere;
 border-left:2px solid var(--rule);padding:2px 0 2px 14px;color:var(--ink)}
.ncert mark{background:var(--quote);color:var(--ink);padding:.12em .18em;border-radius:3px;
 box-shadow:0 0 0 1px var(--quote-edge) inset}

/* "HOW TO READ A CARD": said once, at the top, instead of on every card. */
.howto{margin:0 0 20px;padding:0 0 18px;border-bottom:1px solid var(--rule2)}
.howto summary{cursor:pointer;font:650 12px/1 var(--sans);color:var(--accent);
 letter-spacing:.02em;list-style:none}
.howto summary::-webkit-details-marker{display:none}
.howto summary::before{content:"?";display:inline-flex;align-items:center;justify-content:center;
 width:17px;height:17px;margin-right:9px;border-radius:50%;background:#1d3156;color:#fff;
 font:700 11px/1 var(--sans);vertical-align:-3px}
.howto ol{margin:14px 0 0;padding-left:1.3em;font:400 13px/1.7 var(--sans);color:var(--ink2)}
.howto ol b{color:var(--ink)}
.howto p{margin:12px 0 0;font:400 13px/1.7 var(--sans);color:var(--ink2);max-width:72ch}

/* 10 -- DIFFICULTY AS AN ORDERED METER. The word alone does not say where on the scale it sits. */
.meter{display:inline-flex;gap:3px;margin-right:8px;vertical-align:1px}
.meter i{width:6px;height:6px;border-radius:50%;background:var(--rule)}
.meter i.on{background:var(--ink2)}
.meter.easy i.on{background:#0d5239} .meter.medium i.on{background:#8a5f0b}
.meter.hard i.on{background:#813434}

/* 6 -- A DISPUTED ANSWER MARKS THE CARD. An independent solve disagreeing with the printed answer
   is the most consequential thing here; it used to be a pale table background. */
.q.disputed{border-left-color:#a82d2d}
.q.disputed .qhead{background:linear-gradient(180deg,#f7e4e4,#fff 72%)}
.q.disputed .qhead::after{content:"answers disagree";order:99;flex:none;
 font:700 9.5px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:#fff;
 background:#a82d2d;padding:7px 11px;border-radius:99px}

/* 12 -- STATUS CARRIES AN ICON, so colour is never the only signal. */
.evstat::before{margin-right:7px;font-weight:700}
.evstat.verified::before{content:"✓"}        /* check */
.evstat.partial::before{content:"◑"}         /* half-filled circle */
.evstat.concept::before{content:"ƒ"}         /* florin, for a formula */
.evstat.cut::before{content:"✂"}             /* scissors */
.evstat.pending::before{content:"○"}         /* empty circle */
.evstat.missing::before{content:"—"}         /* em dash */

/* 13 -- chapter hue in the index, 15 -- a quote marker that survives greyscale */
.ichap{width:3px;height:13px;border-radius:2px;background:var(--ch,var(--rule));flex:none}
.ncert mark{border-left:3px solid var(--quote-edge);padding-left:5px}

/* 23 + 25 + 30 -- the tools on an evidence block, and where its quote came from */
.edtools{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 14px;
 padding-bottom:12px;border-bottom:1px solid var(--rule2)}
.sectionno{font:700 12.5px/1.4 var(--sans);color:var(--ink);letter-spacing:-.005em}
.edid{font:600 10.5px/1.5 var(--mono);color:var(--ink3)}
.qbtn{font:650 10.5px/1 var(--sans);padding:6px 10px;border-radius:6px;cursor:pointer;
 border:1px solid var(--rule);background:var(--card);color:var(--ink2)}
.qbtn:hover{border-color:var(--accent);color:var(--accent)}
.prov{margin-left:auto;font:400 11px/1.5 var(--sans);color:var(--ink3);font-style:italic}

/* 28 -- per-card navigation, quiet until hovered */
.cnav{display:inline-flex;gap:4px;margin-left:10px}
.cn{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;
 border-radius:7px;text-decoration:none;border:1px solid var(--rule);background:var(--card);
 color:var(--ink3);font:700 13px/1 var(--sans)}
.cn:hover{border-color:var(--accent);color:var(--accent)}

/* 19 -- A RULE BETWEEN THE STEM AND THE OPTIONS, and nothing else.
   DO NOT set `padding` on `ol.opts li` here. The export positions each "(n)" marker ABSOLUTELY at
   left:0 and reserves its room with `padding-left:30px` on the item; a shorthand `padding` in this
   file drops that reservation and every marker lands on top of its own option text. It did. */
ol.opts{border-top:1px solid var(--rule2);margin-top:16px;padding-top:14px}
ol.opts li{padding-top:4px;padding-bottom:4px}

/* 8 -- compact mode: the same card, scanned rather than read */
body.compact .q{margin-bottom:22px;padding-bottom:18px}
body.compact .sec{margin:20px 30px 10px;padding-top:14px}
body.compact .strip,body.compact .payload,body.compact .qhead{padding-top:11px;padding-bottom:11px}
body.compact .passage{font-size:13px;line-height:1.55}
body.compact .edition{padding:13px 15px 15px;margin-bottom:14px}
body.compact .secblurb{display:none}

/* THE PAYLOAD LINE: the quoted NCERT line, or the concept, directly under the strip. */
.payload{display:flex;gap:18px;align-items:baseline;padding:18px 30px 20px;background:var(--card);
 border-bottom:1px solid var(--rule)}
.plab{flex:none;font:700 9.5px/1.8 var(--sans);letter-spacing:.17em;text-transform:uppercase;
 color:var(--accent)}
.pval{font:400 16px/1.6 var(--serif);color:var(--ink)}
.vcell .chipval{display:inline-flex;align-items:center;gap:5px}
.vagree{color:var(--ok)} .vdiffer{color:var(--warn)}

/* THE FOLD: everything past the question, behind one control. */
details.more{margin:0}
.moresum{list-style:none;cursor:pointer;margin:30px 30px 0;padding:14px 18px;border-radius:9px;
 border:1px solid var(--rule);background:var(--tint);
 font:650 12px/1 var(--sans);color:var(--accent);letter-spacing:.02em;
 display:flex;align-items:center;gap:9px;user-select:none}
.moresum::-webkit-details-marker{display:none}
.moresum::before{content:"+";font:700 15px/1 var(--mono);color:var(--accent)}
details.more[open] .moresum::before{content:"−"}   /* minus */
.moresum:hover{border-color:var(--accent);background:var(--accent-soft)}
details.more .moreshut{display:none}
details.more[open] .moreopen{display:none}
details.more[open] .moreshut{display:inline}

/* ZOOM: a scan opens full size in a new tab. */
a.zoom{display:block;position:relative;cursor:zoom-in}
a.zoom::after{content:"open full size";position:absolute;right:8px;bottom:8px;
 font:650 9.5px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:#fff;
 background:rgba(20,23,32,.78);padding:6px 9px;border-radius:5px;opacity:0;transition:opacity .12s}
a.zoom:hover::after{opacity:1}

/* FILTERS */
.filters{display:flex;flex-wrap:wrap;gap:18px;align-items:center;margin:0 0 18px;
 padding-bottom:16px;border-bottom:1px solid var(--rule2)}
.fgroup{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.fgroup.right{margin-left:auto}
.flab{font:700 9.5px/1.4 var(--sans);letter-spacing:.15em;text-transform:uppercase;
 color:var(--ink3);margin-right:3px}
.fbtn{font:650 11.5px/1 var(--sans);padding:7px 11px;border-radius:7px;cursor:pointer;
 border:1px solid var(--rule);background:var(--card);color:var(--ink2)}
.fbtn:hover{border-color:#1d3156;color:#1d3156}
.fbtn.on{background:#1d3156;border-color:#1d3156;color:#fff}
.icount{margin:16px 0 0;font:400 12px/1.5 var(--sans);color:var(--ink3)}
.icount #shown{font-weight:700;color:var(--ink)}

/* STATUS PILLS: semantic, and the only place these colours appear. */
.evstat{display:inline-block;font:650 11.5px/1 var(--sans);padding:8px 14px;border-radius:99px;
 border:1px solid currentColor;letter-spacing:.005em}
.evstat.verified{color:var(--ok);background:var(--ok-soft);border-color:var(--ok-edge)}
.evstat.partial{color:var(--warn);background:var(--warn-soft);border-color:var(--warn-edge)}
.evstat.concept{color:var(--accent);background:#fff;
 border-color:color-mix(in srgb,var(--accent) 40%,transparent)}
.evstat.cut{color:var(--cut);background:var(--cut-soft)}
.evstat.pending{color:var(--info);background:var(--info-soft)}
.evstat.missing{color:var(--ink2);background:var(--tint);border-color:var(--rule)}

/* SUPPORTING BLOCKS */
.deriv{margin:20px 0 0;padding:16px 20px;border:1px solid var(--rule);border-radius:10px;
 background:var(--tint)}
.deriv h4,.similar h4,.worked h4{margin-top:0}
.deriv ol{margin:0;padding-left:1.4em;font:400 14px/1.7 var(--serif)}
.deriv li{margin-bottom:7px}
.worked{margin:20px 0 0;padding:16px 20px;border:1px solid var(--rule);border-radius:10px;
 background:linear-gradient(180deg,var(--tint),#fff 60%)}
.worked .passage{border-left:0;padding-left:0;max-height:none}
.similar{margin:20px 0 0}
table.sibs{border-collapse:collapse;width:100%;font-size:13.5px}
table.sibs td{border-top:1px solid var(--rule2);padding:9px 14px 9px 0;vertical-align:top;
 line-height:1.6;font-family:var(--serif)}
table.sibs tr:hover td{background:var(--tint)}
.sibid{white-space:nowrap;font:600 11.5px/1.7 var(--mono)!important;color:var(--accent)}
.sibmeta{white-space:nowrap;font:400 11.5px/1.7 var(--sans)!important;color:var(--ink3)}
.howlink{font:400 13px/1.6 var(--sans);color:var(--ink2);margin:11px 0 2px}
.noevid{font:400 13px/1.6 var(--sans);color:var(--ink2);margin:6px 0}
.gap{font:400 13px/1.6 var(--sans);color:var(--warn);margin:9px 0;padding-left:12px;
 border-left:2px solid var(--warn-edge)}

/* =============================================================================================
   PRINT / PDF
   This page is sent to people, so the PDF is a real output and not an afterthought. Three things
   break on paper unless they are undone, and each would silently LOSE CONTENT rather than merely
   look wrong:

     a scrolling box has no scrollbar on paper -- `.passage` is capped at 22rem on screen, so an
     NCERT passage longer than that would simply end mid-sentence, and the highlighted quote could
     fall in the part that never printed;
     a sticky header prints once per page in some engines and overlaps the card body;
     background colours are dropped by default, which would take the quote highlight with them --
     the one thing on the page that must survive.
   ============================================================================================= */
@media print{
  :root{--ground:#fff}
  body{background:#fff}
  .wrap{max-width:none;padding:0}
  .wrap::before{margin-bottom:18px}
  /* Nothing may be hidden behind a scrollbar on paper. */
  .passage{max-height:none!important;overflow:visible!important}
  .qhead{position:static;backdrop-filter:none}
  /* A folded card prints as a header and a button. Everything is open on paper. */
  details.more{display:block!important}
  details.more>*:not(summary){display:revert!important}
  .moresum,.filters,.icount{display:none!important}
  a.zoom::after{display:none}
  .q[hidden]{display:none!important}
  /* Keep a question whole where it fits, and never split a card's header from its first section. */
  .q{break-inside:avoid;page-break-inside:avoid;box-shadow:none;margin-bottom:18px}
  .edition,.axis-card,.concept,.deriv,.worked{break-inside:avoid;page-break-inside:avoid}
  .index{break-after:page;page-break-after:always;box-shadow:none}
  .ichip{text-decoration:none}
  /* The highlight, the status pills and the subject washes are MEANING here, not decoration. */
  *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  a{color:inherit}
}
@page{size:A3 portrait;margin:12mm}
"""










SECTIONS = (
    ("pair", "1", "The question", "left: exactly as it is printed in the booklet. "
                                  "right: what we extracted from that image."),
    ("ncert", "2", "What the answer rests on",
     "the NCERT page as printed, beside that page's extracted text with the quoted line marked. "
     "For Physics and Physical Chemistry, the concept and the approach instead \u2014 a "
     "numerical's answer is a value NCERT never prints."),
    ("where", "3", "Where it belongs, and how hard it is",
     "subject, branch, chapter and subtopic, each with the reason it was chosen, and the solving "
     "steps behind its difficulty band."),
    ("cats", "4", "How it is categorised", "the five fixed axes E1-E5. Each label shows what it "
                                           "MEANS and why this question has it."),
)

#: WHY THE EVIDENCE SITS SECOND AND SPANS THE FULL WIDTH
#: Two attempts came before this one. Putting it last left the reader scrolling a screen down from
#: the question to the book page that supports it. Hoisting the page scans into the left column
#: under the booklet crop fixed that and created a worse problem: a full-page scan is tall and the
#: extraction beside it is short, so the card grew a column of dead white space running down its
#: right-hand side. Full width, second, is the arrangement with neither fault -- the scan sits
#: beside its own highlighted paragraph, the editions stack new above old, and nothing is left
#: holding up an empty column.


def section_head(number, title, blurb, show_blurb=False):
    """A numbered section heading. The blurb is OFF by default.

    Each blurb explained how to read its section -- useful once, and then printed again on every
    card for the rest of the page. Twenty-four copies of "left: exactly as it is printed in the
    booklet" is noise that pushes the content down the screen. They are collected once into the
    page's own "how to read this" block instead.
    """
    return ('<div class="sec"><span class="secno">%s</span>'
            '<span class="sectitle">%s</span>%s</div>'
            % (number, title,
               '<span class="secblurb">%s</span>' % blurb if show_blurb else ""))


#: One hue per subject. The page is 155 cards deep and a reader scanning it wants to know what KIND
#: of question each one is before reading a word of it -- so the accent is driven by the subject,
#: which is a fact about the question, rather than chosen to decorate the card. Everything else keeps
#: its own meaning: status pills stay semantic (verified / partial / concept / missing), the five
#: E-axes keep their five hues, and the highlight stays the one yellow on the page.
SUBJECT_CLASS = {"biology": "s-bio", "physics": "s-phy", "chemistry": "s-che"}


def subject_class(row):
    return SUBJECT_CLASS.get((row.get("subject") or "").strip().lower(), "s-none")


def summary_strip(row, fields, record):
    """The whole question in one row, and under it THE SENTENCE the card is about.

    Two things were buried. The VERDICT -- whether an independent blind solve agreed with the
    booklet's printed answer -- sat in a table two sections down, although it is the single most
    consequential fact a card can carry. And the PAYLOAD -- the quoted NCERT line, or the concept
    for a subject that has no quotable line -- sat three sections down, although it is the reason
    the card exists at all. A reader scanning should not have to open a card to learn either.
    """
    paper_id, qno = row["paper_id"], int(row["qno"])
    band = paper.difficulty_of(paper_id, qno)[0]
    subtopics = [t.strip() for t in (row["topic_names"] or "").split(";") if t.strip()]
    verdict = (row.get("answer_verdict") or "").strip()
    # The strip carries the ANSWER-SIDE facts only. Chapter and subtopic used to sit here as well
    # and are now in the placement table directly below the question, where their reasons are --
    # printing a chapter name twice, three inches apart, taught nobody anything.
    # A three-step meter beside the word. Difficulty is ORDERED, and a word alone makes a reader
    # read three cards to learn whether "medium" is the middle or the top of the scale.
    dots = {"easy": 1, "medium": 2, "hard": 3}.get(band, 0)
    meter = "".join('<i class="%s"></i>' % ("on" if i < dots else "off") for i in range(3))
    chips = [("difficulty", ('<span class="meter %s">%s</span>%s'
                             % (band, meter, html.escape(band))) if band else ""),
             ("steps", str(paper.difficulty_of(paper_id, qno)[1] or "") or ""),
             ("printed answer", row.get("answer_official") or ""),
             ("blind solve", row.get("answer_solved") or "")]
    # `difficulty` arrives pre-rendered (it carries a meter); the rest are plain values.
    shown = "".join('<div class="chip2"><span class="chiplab">%s</span>'
                    '<span class="chipval">%s</span></div>'
                    % (label, value if label == "difficulty" else html.escape(str(value)))
                    for label, value in chips if str(value).strip())
    if verdict:
        agree = verdict.lower().startswith("agree") or "all agree" in verdict.lower()
        shown += ('<div class="chip2 vcell"><span class="chiplab">verdict</span>'
                  '<span class="chipval %s">%s %s</span></div>'
                  % ("vagree" if agree else "vdiffer", "&check;" if agree else "&#9888;",
                     html.escape(verdict)))

    # The payload: the quoted line where there is one, else the concept.
    payload, kind = "", ""
    quote = (fields.get("quoted_lines") or "").split(" || ")[0].strip()
    if quote:
        payload, kind = quote, "NCERT says"
    elif record.get("concept"):
        payload, kind = record["concept"], "concept"
    lead = ('<div class="payload"><span class="plab">%s</span>'
            '<span class="pval">%s</span></div>'
            % (kind, (texhtml.greek_in_relation if kind == "concept" else texhtml.to_html)(
                payload[:260] + ("\u2026" if len(payload) > 260 else "")))
            if payload else "")
    return '<div class="strip">%s</div>%s' % (shown, lead)


def anchor_id(paper_id, qno):
    """A stable id per question, so a card can be linked to and returned to."""
    return "%s-q%03d" % (paper_id.lower(), qno)


def index_html(entries):
    """A compact index: what is on this page, and a way to reach any card in one click.

    WHY A PAGE THIS LONG NEEDS ONE
    ------------------------------
    155 cards is about forty screens. Without an index a reader cannot tell what the page contains
    without scrolling all of it, cannot get back to a card they have already read, and cannot answer
    the first question anyone actually asks -- "how much of this is verified?" -- at all. This is a
    working index and not a banner: every chip is a link, and the counts are measured from the same
    rows the cards are built from, so the two cannot disagree.
    """
    by_subject = collections.OrderedDict()
    for entry in entries:
        by_subject.setdefault(entry["subject"], []).append(entry)
    counts = collections.Counter(e["status"] for e in entries)

    legend = "".join(
        '<span class="lchip %s">%d %s</span>' % (key, counts[key], label)
        for key, label in (("verified", "verified against NCERT"), ("concept", "concept &amp; approach"),
                           ("partial", "partly supported"), ("cut", "cut from this edition"),
                           ("pending", "not quoted yet"), ("missing", "no line found"))
        if counts[key])

    groups = []
    for subject, rows in by_subject.items():
        chips = "".join(
            '<a class="ichip %s" href="#%s" title="%s" style="--ch:%s">'
            '<span class="ichap"></span>%s<span class="idot"></span></a>'
            % (row["status"], row["anchor"], html.escape(row["tip"]), row["chapter_hue"],
               html.escape(row["short"]))
            for row in rows)
        groups.append('<div class="igroup %s"><div class="ihead">%s<b>%d</b></div>'
                      '<div class="ichips">%s</div></div>'
                      % (rows[0]["cls"], html.escape(subject), len(rows), chips))

    subjects = sorted({e["subject_key"] for e in entries})
    bands = [b for b in ("easy", "medium", "hard", "unrated")
             if any(e["difficulty"] == b for e in entries)]
    statuses = [k for k in ("verified", "partial", "concept", "cut", "pending", "missing")
                if counts[k]]

    def group(name, key, values, labels=None):
        buttons = "".join(
            '<button class="fbtn" data-key="%s" data-value="%s">%s</button>'
            % (key, html.escape(v), html.escape((labels or {}).get(v, v).title()))
            for v in values)
        return ('<div class="fgroup"><span class="flab">%s</span>'
                '<button class="fbtn on" data-key="%s" data-value="">All</button>%s</div>'
                % (name, key, buttons))

    controls = ('<div class="filters">%s%s%s'
                '<div class="fgroup right">'
                '<button class="fbtn" id="expandall">Open every card</button>'
                '<button class="fbtn" id="collapseall">Close every card</button>'
                '<button class="fbtn" id="compact">Compact spacing</button></div>'
                '</div>'
                % (group("subject", "subject", subjects),
                   group("status", "status", statuses),
                   group("difficulty", "difficulty", bands)))

    howto = ('<details class="howto"><summary>How to read a card</summary><ol>%s</ol>'
             '<p>Each card opens with the question as printed beside what was extracted from it, '
             'then where it belongs and how hard it is. The NCERT evidence and the E1&ndash;E5 '
             'rating sit behind the control on each card. A highlighted line is a quote re-found '
             'word for word in the book; click any book page to open it full size.</p></details>'
             % "".join("<li><b>%s</b> &mdash; %s</li>" % (title, blurb)
                       for _key, _n, title, blurb in SECTIONS))

    return ('<nav class="index" id="index"><div class="legend">%s</div>%s%s%s'
            '<p class="icount"><span id="shown">%d</span> of %d questions shown</p></nav>'
            % (legend, howto, controls, "".join(groups), len(entries), len(entries)))


def restructure(card, evidence="", strip="", fold=True, pill="", nav=""):
    """Re-order one imported card into five labelled sections laid out ACROSS, not DOWN.

    THE BUG THIS FUNCTION EXISTS TO UNDO
    ------------------------------------
    The paper export builds a card as: header, classification table, then a two-column `.pair` of
    crop | extraction -- and everything after the extraction (answers, difficulty, E1-E5, meta) is
    emitted INSIDE the extraction column, which is only closed at the very end of the card. On that
    page it reads fine, because the column is wide and the blocks are what the reader is checking.
    Here it produced the defect visible on screen: every section after the question crammed into the
    right half, with a column of dead white space running down the left under a short crop.

    So the `.pair` is closed as soon as the extraction ends, and everything after it is re-emitted
    at FULL WIDTH: the answer beside the placement tables, then the E1-E5 cards in columns, then the
    evidence. The NCERT page scans go into the left column under the crop, which is both where the
    space was and where the comparison belongs -- printed question above printed book page.

    Every anchor is markup this module's own export emits. If one is missing the card is returned
    UNCHANGED rather than half-rebuilt: a card that reads oddly is recoverable, one whose tags were
    cut in the wrong place is not.
    """
    #: `question_card` ends by closing the extraction column, the pair, and the card itself.
    CLOSERS = "</div></div></div>"
    split = card.find('<table class="answers')
    if not card.endswith(CLOSERS) or split < 0 or '<div class="pair">' not in card:
        return card

    def lift(open_tag, close_tag, text):
        """(text without the first such block, that block) -- or (text, "") if there is none."""
        i = text.find(open_tag)
        if i < 0:
            return text, ""
        j = text.find(close_tag, i)
        if j < 0:
            return text, ""
        j += len(close_tag)
        return text[:i] + text[j:], text[i:j]

    head, tail = card[:split], card[split:-len(CLOSERS)]
    if pill or nav:
        at = head.find("</div>")              # the end of .qhead
        if at > 0:
            head = head[:at] + pill + nav + head[at:]

    # The classification table sits between the header and the pair, i.e. in `head`. Moving it down
    # is the other half of the re-order: the export opens with the tags because its reader is
    # checking tags, while a reader meeting the question needs to see the question first.
    head, classification = lift('<table class="classify">', "</table>", head)
    # THE ANSWER TABLE IS DROPPED, NOT LAID OUT. It held three cells -- printed answer, blind solve,
    # verdict -- and all three now sit in the strip at the top of the card, where a reader sees them
    # without opening anything. Keeping both put a three-cell table in a column sized for the
    # placement table's long reasons, which is the hand's width of white space the owner pointed at.
    tail, _answers = lift('<table class="answers', "</table>", tail)
    tail, difficulty = lift('<table class="classify">', "</table>", tail)
    tail, _meta = lift('<div class="meta">', "</div>", tail)      # extraction provenance: dropped

    at = head.find('<div class="pair">')
    head = head[:at] + strip + section_head("1", SECTIONS[0][2], SECTIONS[0][3]) + head[at:]

    duo = ('<div class="place">%s<div class="placegrid">%s%s</div></div>'
           % (section_head("3", SECTIONS[2][2], SECTIONS[2][3]), classification, difficulty))

    # EVERYTHING PAST THE QUESTION FOLDS AWAY. A card runs several screens and 24 of them run
    # forty; a reader scanning for the right question should not have to scroll a rating they did
    # not ask for. The header, the strip and the question itself stay open, because those are what
    # scanning is FOR -- the fold starts exactly where detail starts.
    # WHAT STAYS OPEN, AND WHY. The question, and then where it belongs and how hard it is -- the
    # owner's call, and the right one: those reasons ("why this chapter", the solving steps, the
    # catch) are what a reader is deciding from, while the NCERT page and the E1-E5 rating are what
    # they check afterwards. So the fold starts at the evidence, not at the placement.
    above = duo
    detail = (evidence
              + (section_head("4", SECTIONS[3][2], SECTIONS[3][3])
                 if '<div class="cats">' in tail else "")
              + tail)
    if not fold:
        return head + "</div></div>" + above + detail
    return (head + "</div></div>"                 # close the extraction column and the pair
            + above
            + '<details class="more" open><summary class="moresum">'
              '<span class="moreopen">show the NCERT evidence and the E1&ndash;E5 rating'
              '</span><span class="moreshut">hide the NCERT evidence and the rating</span>'
              '</summary>'
            + detail
            + "</details>")                       # the card itself is closed by the caller


#: Branches whose evidence is a CONCEPT, not a quotation. The reason is measured, not stylistic: a
#: numerical's answer is a value that appears nowhere in NCERT, and twelve evidence agents working
#: these subjects returned "partly supported" again and again because what the solution needed was a
#: display equation, a table constant, or a relation from another chapter -- never a sentence. For
#: these questions a half-matched NCERT paragraph is worse than none, because it looks like evidence.
#: Organic chemistry is NOT here: its reactions are printed as equations and are quoted like any
#: other evidence.
CONCEPT_BRANCHES = {("physics", ""), ("physics", "physics"), ("chemistry", "physical")}


def concept_only(row):
    """True when this question gets a concept INSTEAD of an NCERT quotation.

    Every question gets the approach. What this decides is whether NCERT is quoted beside it:
    Biology, Organic and Inorganic content is in the book, so the line is quoted and highlighted;
    a Physics or Physical Chemistry answer is a value the book never prints, so there is nothing
    honest to quote and a part-matched paragraph would read as evidence it is not.


    Decided on the CONFIRMED subject, the same rule `qca_plugin` uses, and never on the paper's
    positional guess. The guess was wrong on all 43 checked questions of 2015 Code A and all 179 of
    2017 Code C, so routing on it would send biology questions down the physics path and show them
    a concept box that nothing will ever fill.
    """
    subject = (row.get("subject") or "").strip().lower()
    if (row.get("subject_from") or "").lower().startswith("position"):
        return False
    stream = (row.get("stream") or "").strip().lower()
    if subject == "physics":
        return True
    return (subject, stream) in CONCEPT_BRANCHES


def concept_approach(paper_id, qno):
    """{concept, approach, also_uses, note} from QCA, or {}."""
    return _load(QCA_OUT, "%s#q%03d" % (paper_id, qno)) or {}


def concept_html(record):
    """The concept and the approach, which for these subjects IS the record."""
    if not record.get("concept"):
        return ('<p class="noevid">The concept and approach for this question have not been '
                'recorded yet.</p>')
    also = record.get("also_uses") or []
    return ('<div class="concept">'
            '<div class="crow"><span class="clab">concept</span>'
            '<span class="cval">%s</span></div>'
            '<div class="crow"><span class="clab">approach</span>'
            '<span class="capp">%s</span></div>%s</div>'
            % (texhtml.greek_in_relation(record["concept"]),
               texhtml.greek_in_relation(record.get("approach") or ""),
               '<div class="crow"><span class="clab">also uses</span><span class="cval">%s</span>'
               '</div>' % " &nbsp;&middot;&nbsp; ".join(texhtml.greek_in_relation(a) for a in also)
               if also else ""))


def derivation_html(evidence):
    """The agent's own route from the quoted lines to the answer, as a numbered chain.

    This was on the record and shown nowhere. `derivation_steps` is the half of an evidence packet
    that explains WHY the quoted lines reach this option -- a quote plus a number is not an
    argument, and a reader checking a numerical has to redo the algebra themselves without it. The
    step list is restricted by the step's own rules to algebra, arithmetic, unit conversion and
    logic: anything needing a fact has its own quote, so the chain is checkable line by line.
    """
    steps = [str(x) for x in (evidence.get("derivation_steps") or []) if str(x).strip()]
    if not steps:
        return ""
    return ('<div class="deriv"><h4>how the quoted lines reach this answer</h4><ol>%s</ol></div>'
            % "".join("<li>%s</li>" % texhtml.to_html(step) for step in steps))


def similar_html(row, index, out_dir, on_page=()):
    """Other questions in the corpus testing the same subtopic -- the same idea at other values.

    WHY SUBTOPIC AND NOT CHAPTER. A chapter match returns thirty questions with nothing in common
    but a heading. The subtopic is the level at which two questions are genuinely the same question
    with different numbers -- "Mole Fraction" asked in 2015 and asked again in 2020 -- which is what
    makes the comparison worth printing: a reader can see at once whether the pattern repeats, and
    whether our difficulty and trap labels stayed consistent across the two.
    """
    subtopics = [t.strip() for t in (row["topic_names"] or "").split(";") if t.strip()]
    if not subtopics:
        return ""
    mine = (row["paper_id"], int(row["qno"]))
    seen, items = set(), []
    for subtopic in subtopics:
        for other in index.get(subtopic.lower(), []):
            key = (other["paper_id"], other["qno"])
            if key == mine or key in seen:
                continue
            seen.add(key)
            items.append(other)
    if not items:
        return ""
    items.sort(key=lambda o: (o["paper_id"], o["qno"]))
    def name(o):
        """A link when that question is a card on this page, plain text when it is not. A link to
        nowhere is worse than no link: a reader clicks it and the page does not move."""
        label = "%s &middot; Q%d" % (html.escape(o["paper_id"].replace("_", " Code ")), o["qno"])
        if (o["paper_id"], o["qno"]) in on_page:
            return '<a href="#%s">%s</a>' % (anchor_id(o["paper_id"], o["qno"]), label)
        return label

    rows = "".join(
        '<tr><td class="sibid">%s</td><td>%s</td>'
        '<td class="sibmeta">%s%s</td></tr>'
        % (name(o),
           texhtml.to_html(o["stem"][:190] + ("..." if len(o["stem"]) > 190 else "")),
           html.escape(o["difficulty"] or "unrated"),
           " &middot; answer %s" % html.escape(o["answer"]) if o["answer"] else "")
        for o in items[:6])
    return ('<div class="similar"><h4>the same subtopic elsewhere in these papers '
            '&middot; %d found</h4><table class="sibs">%s</table>%s</div>'
            % (len(items), rows,
               '<p class="noevid">%d more not listed.</p>' % (len(items) - 6)
               if len(items) > 6 else ""))


EXAMPLE = re.compile(r"\bExample\s+\d+\.\d+", re.I)


def worked_example(passages, question_words):
    """NCERT's OWN worked example of the same calculation, or None.

    WHY A NUMERICAL NEEDS THIS AND A BIOLOGY QUESTION DOES NOT
    ---------------------------------------------------------
    For a Biology question the answer is a sentence NCERT prints, so highlighting that sentence is
    the whole of the evidence. For a numerical there is no such sentence: the answer is a number
    that appears nowhere in the book. What the book does carry is the same calculation done at
    DIFFERENT VALUES -- "Example 1.4: if N2 gas is bubbled through water at 293 K..." -- and that
    example is the most useful thing on the page for anyone checking the method, because it shows
    the formula in use, the constant being looked up, and the arithmetic laid out, all from NCERT.

    Matched on the question's own content words against the example's text, so the example returned
    is one about the same quantity rather than merely the nearest example in the chapter.
    """
    wanted, best, score = set(question_words), None, 0
    for passage in passages:
        text = passage.get("text") or ""
        if not EXAMPLE.search(text) and not EXAMPLE.search(passage.get("section_heading") or ""):
            continue
        hit = len(wanted & set(re.findall(r"[a-z]{5,}", text.lower())))
        if hit > score:
            best, score = passage, hit
    return best if best and score >= 4 else None


def worked_example_html(passage, out_dir):
    if not passage:
        return ""
    label = EXAMPLE.search(passage.get("text") or "")
    image = page_image(passage["passage_id"], passage.get("page_start"), out_dir)
    return ('<div class="worked"><h4>NCERT works this same calculation, at other values '
            '&middot; %s</h4><div class="passage">%s</div>'
            '<span class="where">%s &middot; printed page %s%s</span></div>'
            % (html.escape(label.group(0) if label else "worked example"),
               html.escape(passage["text"]),
               html.escape(passage["passage_id"]), html.escape(str(passage.get("page_start"))),
               " &middot; page shown above" if image else ""))


def subtopic_index(all_rows):
    """{subtopic: [{paper_id, qno, stem, difficulty, answer}]} over the WHOLE corpus.

    Built from every exported paper, not just the ones on this page, because the point of the
    comparison is to reach questions a reader is not currently looking at.
    """
    index = collections.defaultdict(list)
    for row in all_rows:
        entry = None
        for subtopic in (t.strip() for t in (row["topic_names"] or "").split(";")):
            if not subtopic:
                continue
            if entry is None:
                band = paper.difficulty_of(row["paper_id"], int(row["qno"]))[0]
                entry = {"paper_id": row["paper_id"], "qno": int(row["qno"]),
                         "stem": row.get("stem") or "", "difficulty": band,
                         "answer": row.get("answer_official") or ""}
            index[subtopic.lower()].append(entry)
    return index


def provenance(passage_id, inp):
    """Where this passage came from, said plainly.

    A reader cannot otherwise tell a quote the ranker handed the agent from one the agent went and
    found in the book -- and after the search change most of the decisive quotes are the second
    kind. Both are verified the same way, a script re-finding every line in the book, so this is
    not a confidence grade. It is the audit trail, and the first thing a reviewer asks for.
    """
    shortlisted = {p["passage_id"] for p in ((inp or {}).get("passages") or [])}
    return ("from the ranked shortlist" if passage_id in shortlisted
            else "fetched from the book \u2014 the shortlist did not carry it")


def edition_block(label, book, chapter_numbers, passage, quotes, out_dir, inp=None):
    """One edition: the printed page beside that page's text, with the quotes marked.

    Side by side because the claim and its source have to be checkable in one glance -- a quote
    printed a screen away from the page it came from is an assertion, not evidence. Returns "" when
    nothing is extracted for this edition: an empty block is a statement about our pipeline, and the
    reader came here to see the book.
    """
    if not passage:
        return ""
    marked, found = highlight(passage["text"], quotes)
    image = page_image(passage["passage_id"], passage.get("page_start"), out_dir)
    section = (passage.get("section_heading") or "(no section heading)").strip()
    tools = ('<div class="edtools"><span class="sectionno">%s</span>'
             '<span class="edid">%s &middot; page %s</span>'
             '<button class="qbtn jumpq" type="button">jump to the quote</button>'
             '<button class="qbtn copyq" type="button">copy the quote</button>'
             '<span class="prov">%s</span></div>'
             % (html.escape(section), html.escape(passage["passage_id"]),
                html.escape(str(passage.get("page_start"))),
                provenance(passage["passage_id"], inp)))
    shot = ('<a class="zoom" href="%s" target="_blank" rel="noopener" '
            'title="open this page full size">'
            '<img class="pageimg" src="%s" alt="NCERT page %s" loading="lazy"></a>'
            % (html.escape(image), html.escape(image),
               html.escape(str(passage.get("page_start"))))
            if image else '<p class="noevid">page image not rendered</p>')
    warn = ('<p class="gap">the quoted line was not found in this text &mdash; check the quote '
            'against the book</p>' if quotes and len(found) < len(quotes) else "")
    return ('<div class="edition" data-quote="%s"><h4>%s &middot; %s ch%s</h4>%s'
            '<div class="edrow"><div class="edshot">%s</div>'
            '<div class="edtext"><div class="passage">%s</div>%s</div></div></div>'
            % (html.escape((quotes[0] if quotes else "")[:400]), label,
               html.escape(book or "?"),
               ", ".join(str(n) for n in (chapter_numbers or [])),
               tools, shot, marked, warn))


def _page_text(path):
    """(text, first heading) of one A2 page read, or (None, "")."""
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return None, ""
    if "error" in data:
        return None, ""
    blocks = data.get("blocks") or []
    heading = next((b.get("text") or "" for b in blocks if b.get("kind") == "heading"), "")
    text = "\n".join((b.get("text") or "").strip() for b in blocks if (b.get("text") or "").strip())
    return (text or None), heading


def older_passage(book, chapter_numbers, quote_words, chapter_title=""):
    """The older edition's best-matching text for a quoted line, or None.

    TWO SOURCES, IN ORDER
    ---------------------
    1. `ncert/passages/<BOOK>O.jsonl` -- proper section-split passages, where the A2 -> A2S -> A3
       chain has completed. At the time of writing that is BIO11O alone.
    2. The A2 PAGE READS themselves, `steps/A2/out/<BOOK>O-chNN-pNNN.runA.json`. A page read is the
       transcription of one printed page, which is exactly what this page needs to show -- the
       screenshot of that page beside its text. Waiting for the section split before showing
       anything would leave old NCERT blank for every chapter but one, while the text sits on disk.

    Matched on shared long words rather than by section number, because the older edition numbers
    its sections differently -- that renumbering is why the pairing step exists at all.
    """
    old = older_book(book)
    if not old or not chapter_numbers:
        return None
    # Resolved by title, because the editions renumber -- see `older_chapter_titles`.
    chapter_numbers = older_chapter_numbers(book, chapter_numbers, chapter_title)
    wanted = set(quote_words)
    if not wanted:
        return None
    best, score = None, 0

    path = rc.pp("ncert", "passages", "%s.jsonl" % old)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                if row.get("chapter_num") not in set(chapter_numbers):
                    continue
                hit = len(wanted & set(re.findall(r"[a-z]{5,}", (row.get("text") or "").lower())))
                if hit > score:
                    best, score = {"passage_id": row["passage_id"],
                                   "section_heading": row.get("section_heading") or "",
                                   "page_start": row.get("page_start"),
                                   "text": row["text"]}, hit

    for number in chapter_numbers:
        for read in sorted(glob.glob(rc.pp(*A2_OUT, "%s-ch%02d-p*.runA.json" % (old, int(number))))):
            page = int(re.search(r"-p(\d+)\.runA\.json$", read).group(1))
            text, heading = _page_text(read)
            if not text:
                continue
            hit = len(wanted & set(re.findall(r"[a-z]{5,}", text.lower())))
            if hit > score:
                best, score = {"passage_id": "%s-CH%02d-P%03d" % (old, int(number), page),
                               "section_heading": heading or "page %d as printed" % page,
                               "page_start": page, "text": text}, hit
    return best if best and score >= 3 else None


def ncert_block(row, item, out_dir, siblings=""):
    """The NCERT half of one card, and the CSV fields that describe the same thing."""
    inp = _load(WORK, item, ".runA.input.json")
    evidence = _load(OUT, item)
    code, label = status_for(row, evidence, inp)
    chapter = (inp or {}).get("chapter") or {}
    book, numbers = chapter.get("ncert_book"), chapter.get("ncert_chapter_number") or []
    # The pill itself is hoisted into the card header -- a reader deciding whether to read a card
    # should not have to reach section 5 to learn what state it is in.
    out = [section_head("2", SECTIONS[1][2], SECTIONS[1][3]), '<div class="ncert">']

    fields = {"ncert_book": book or "", "ncert_chapter": ";".join(str(n) for n in numbers),
              "link_type": "", "supports_answer": "", "passage_id": "", "ncert_page": "",
              "section_heading": "", "quoted_lines": "", "missing_from_ncert": "",
              "evidence_status": code, "concept": "", "approach": "", "also_uses": "",
              "evidence_label": label}

    record = concept_approach(row["paper_id"], int(row["qno"]))
    if record.get("concept"):
        out.append(concept_html(record))
        fields["concept"] = record["concept"]
        fields["approach"] = record.get("approach") or ""
        fields["also_uses"] = "; ".join(record.get("also_uses") or [])
    if concept_only(row):
        # AND NOTHING FROM NCERT. Not even a supporting quote, and not a note about its absence:
        # for these subjects the concept and the approach ARE the record, a part-matched paragraph
        # underneath invites a reader to treat it as evidence it is not, and "no supporting line
        # found" labels an expected absence as a defect.
        if not record.get("concept"):
            out.append(concept_html(record))
        out.append('</div>')
        return "".join(out), fields, record
    if evidence:
        if evidence.get("link_type"):
            out.append('<p class="howlink">how NCERT reaches this answer: <b>%s</b></p>'
                       % html.escape(evidence["link_type"].replace("_", " ")))
        fields["link_type"] = evidence.get("link_type") or ""
        fields["supports_answer"] = evidence.get("supports_answer") or ""
        fields["missing_from_ncert"] = "; ".join(evidence.get("missing") or [])
        lookup = {p["passage_id"]: p for p in ((inp or {}).get("passages") or [])}
        by_passage = collections.OrderedDict()
        for line in (evidence.get("evidence") or []):
            by_passage.setdefault(line.get("passage_id"), []).append(line.get("exact_line") or "")
        for passage_id, quotes in by_passage.items():
            # The shortlist first, then the book itself -- see `passage_from_book`.
            passage = lookup.get(passage_id) or passage_from_book(passage_id)
            words = re.findall(r"[a-z]{5,}", " ".join(quotes).lower())
            older = older_passage(book, numbers, words,
                                  chapter_title=chapter.get("ncert_chapter_title") or "")
            out.append('<div class="editions">%s%s</div>'
                       % (edition_block("new NCERT", book, numbers, passage, quotes, out_dir, inp),
                          edition_block("old NCERT", older_book(book), numbers, older, quotes,
                                        out_dir, inp)))
            if passage:
                fields["passage_id"] = fields["passage_id"] or passage_id
                fields["ncert_page"] = fields["ncert_page"] or str(passage.get("page_start") or "")
                fields["section_heading"] = (fields["section_heading"]
                                             or passage.get("section_heading") or "")
        fields["quoted_lines"] = " || ".join(q for qs in by_passage.values() for q in qs)
        if evidence.get("missing"):
            out.append('<p class="gap">needed by the solution but not in NCERT: %s</p>'
                       % html.escape("; ".join(evidence["missing"])))
        if not by_passage:
            out.append('<p class="noevid">No line in this chapter supports the answer. The '
                       'section the solution needs is named above.</p>')
        out.append(derivation_html(evidence))
        # Only where the answer is computed. On a question whose answer is a stated fact, NCERT's
        # worked examples are noise -- the quoted sentence already is the evidence.
        if (evidence.get("derivation_steps")
                or evidence.get("link_type") in ("rule_used", "rules_chained")):
            words = re.findall(r"[a-z]{5,}",
                               ((inp or {}).get("question", {}).get("stem_en") or "").lower())
            out.append(worked_example_html(
                worked_example((inp or {}).get("passages") or [], words), out_dir))
    elif code == "cut":
        out.append('<p class="noevid">This chapter is extracted, but the section the question '
                   'tests is gone from the new edition &mdash; its evidence can only come from '
                   'the older one.</p>')

    elif inp and inp.get("passages"):
        out.append('<p class="noevid">The chapter is extracted and its candidate passages are '
                   'ready; the exact line has not been quoted yet. Closest passage below.</p>')
        out.append(edition_block("new NCERT", book, numbers, inp["passages"][0], [], out_dir, inp))
    else:
        out.append('<p class="noevid">This chapter has no NCERT passages extracted yet.</p>')
    out.append(siblings)
    out.append('</div>')
    return "".join(out), fields, record


SCRIPT = """
<script>
/* Filtering and fold control. Plain DOM, no library: the page is sent to people as a single file
   and opened from disk, so anything fetched from a network would simply not be there. */
(function () {
  var state = {subject: "", status: "", difficulty: ""};
  var cards = Array.prototype.slice.call(document.querySelectorAll(".q"));
  var shown = document.getElementById("shown");

  function apply() {
    var n = 0;
    cards.forEach(function (card) {
      var ok = Object.keys(state).every(function (key) {
        return !state[key] || card.getAttribute("data-" + key) === state[key];
      });
      card.hidden = !ok;
      if (ok) { n++; }
    });
    if (shown) { shown.textContent = n; }
  }

  document.querySelectorAll(".fbtn[data-key]").forEach(function (button) {
    button.addEventListener("click", function () {
      var key = button.getAttribute("data-key");
      state[key] = button.getAttribute("data-value");
      document.querySelectorAll('.fbtn[data-key="' + key + '"]').forEach(function (sibling) {
        sibling.classList.toggle("on", sibling === button);
      });
      apply();
    });
  });

  function fold(open) {
    document.querySelectorAll("details.more").forEach(function (d) { d.open = open; });
  }
  /* The markup ships open so that a reader without JavaScript, and the printer, see everything.
     Folding is this script's job, done once on load -- except when the URL points at a card. */
  if (!location.hash) { fold(false); }

  var openAll = document.getElementById("expandall");
  var shutAll = document.getElementById("collapseall");
  if (openAll) { openAll.addEventListener("click", function () { fold(true); }); }
  if (shutAll) { shutAll.addEventListener("click", function () { fold(false); }); }

  /* 23 + 25: reach the quote, and take it away with you. */
  document.querySelectorAll(".jumpq").forEach(function (button) {
    button.addEventListener("click", function () {
      var mark = button.closest(".edition").querySelector("mark");
      if (mark) { mark.scrollIntoView({block: "center", behavior: "smooth"}); }
    });
  });
  document.querySelectorAll(".copyq").forEach(function (button) {
    button.addEventListener("click", function () {
      var quote = button.closest(".edition").getAttribute("data-quote") || "";
      /* navigator.clipboard needs a secure context, and this file is opened from disk as often as
         from a server, so the textarea fallback is the path that actually runs most of the time. */
      var done = function () {
        var was = button.textContent;
        button.textContent = "copied";
        setTimeout(function () { button.textContent = was; }, 1400);
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(quote).then(done, done);
      } else {
        var box = document.createElement("textarea");
        box.value = quote;
        box.style.position = "fixed";
        box.style.opacity = "0";
        document.body.appendChild(box);
        box.select();
        try { document.execCommand("copy"); } catch (e) { /* nothing to do */ }
        document.body.removeChild(box);
        done();
      }
    });
  });

  /* 28: previous / next, skipping anything a filter has hidden. */
  function visible() {
    return cards.filter(function (card) { return !card.hidden; });
  }
  cards.forEach(function (card) {
    var prev = card.querySelector(".cn.prev");
    var next = card.querySelector(".cn.next");
    var step = function (delta) {
      return function (event) {
        event.preventDefault();
        var list = visible();
        var at = list.indexOf(card);
        var to = list[at + delta];
        if (to) {
          var d = to.querySelector("details.more");
          if (d) { d.open = true; }
          to.scrollIntoView({block: "start", behavior: "smooth"});
        }
      };
    };
    if (prev) { prev.addEventListener("click", step(-1)); }
    if (next) { next.addEventListener("click", step(1)); }
  });

  /* 8: a density switch, for scanning rather than reading. */
  var dense = document.getElementById("compact");
  if (dense) {
    dense.addEventListener("click", function () {
      document.body.classList.toggle("compact");
      dense.classList.toggle("on");
      dense.textContent = document.body.classList.contains("compact")
        ? "Comfortable spacing" : "Compact spacing";
    });
  }

  /* A link into a folded card has to open it, or the reader lands on a card that looks empty. */
  function openTarget() {
    var el = document.querySelector(":target");
    if (!el) { return; }
    var d = el.querySelector("details.more");
    if (d) { d.open = true; }
  }
  window.addEventListener("hashchange", openTarget);
  openTarget();
}());
</script>
"""

CSV_COLUMNS = ["paper_id", "qno", "subject", "branch", "stream", "chapter", "subtopic_1",
               "subtopic_2", "difficulty", "steps_to_solve", "what_makes_it_hard",
               "answer_official", "answer_solved", "answer_verdict",
               "e1_question_type", "e2_format", "e3_content_shape",
               "e4_cognitive_demand", "e4_solution_structure", "e4_strategy",
               "e4_strategy_evidence", "e5_traps", "e5_routes",
               "concept", "why_this_type",
               "concept", "approach", "also_uses",
               "ncert_book", "ncert_chapter", "evidence_status", "link_type", "supports_answer",
               "passage_id", "ncert_page", "section_heading", "quoted_lines", "missing_from_ncert"]

#: The reason columns follow the ECAT record's OWN shape rather than a tidy e1..e5 symmetry. There
#: is no per-axis "why" in that record: E1-E3 share one `reason` (why this question is of this
#: type), E4's justification is `strategy_evidence`, and E5 carries a `route` for each trap --
#: the route being the pull that makes a wrong option attractive, not merely the error it causes.
#: Inventing five parallel reason columns would mean filling four of them with the same sentence.


def _flat(value):
    """Collapse runs of whitespace, so a cell stays one line in a spreadsheet.

    NCERT headings arrive with newlines in them -- `3.11\nCELLS IN SERIES\nAND IN PARALLEL` -- and
    a quoted multi-line cell is valid CSV but makes `cut`, `awk` and a human eye all read the file
    wrongly.
    """
    return re.sub(r"\s+", " ", str(value or "")).strip()


def csv_row(row, fields):
    """One CSV row: the same facts the card shows, flattened one question to a line."""
    paper_id, qno = row["paper_id"], int(row["qno"])
    band, steps_to_solve, _steps, _why, hard = paper.difficulty_of(paper_id, qno)
    rating, _group_note = paper.categories_of(paper_id, qno)
    rating = rating or {}
    subtopics = [t.strip() for t in (row["topic_names"] or "").split(";") if t.strip()]
    traps = rating.get("traps") or []
    out = {
        "paper_id": paper_id, "qno": qno,
        "subject": row.get("subject") or "", "branch": row.get("branch") or "",
        "stream": row.get("stream") or "",
        "chapter": (row["chapter_names"] or "").split(";")[0].strip(),
        "subtopic_1": subtopics[0] if subtopics else "",
        "subtopic_2": subtopics[1] if len(subtopics) > 1 else "",
        "difficulty": band, "steps_to_solve": steps_to_solve or "", "what_makes_it_hard": hard,
        "answer_official": row.get("answer_official") or "",
        "answer_solved": row.get("answer_solved") or "",
        "answer_verdict": row.get("answer_verdict") or "",
        "e1_question_type": rating.get("question_type") or "",
        "e2_format": rating.get("format") or "",
        "e3_content_shape": rating.get("content_shape") or "",
        "e4_cognitive_demand": rating.get("cognitive_demand") or "",
        "e4_solution_structure": rating.get("solution_structure") or "",
        "e4_strategy": "; ".join(rating.get("strategy_available") or []),
        "e4_strategy_evidence": rating.get("strategy_evidence") or "",
        "e5_traps": "; ".join("%s (option %s)" % (t.get("label"), t.get("option"))
                              for t in traps if isinstance(t, dict)),
        "e5_routes": " || ".join("%s: %s" % (t.get("label"), t.get("route") or "")
                                 for t in traps if isinstance(t, dict)),
        "concept": rating.get("concept") or "",
        "why_this_type": rating.get("reason") or "",
    }
    out.update(fields)
    return {k: _flat(v) for k, v in out.items()}


#: A showcase page is for reading, not for coverage. These counts are what one sitting can take in.
SAMPLE = collections.OrderedDict([("biology", 10), ("physics", 10), ("chemistry", 4)])


def completeness(row, fields):
    """How finished a card is, for choosing which ones to show.

    A sample page should show the BEST examples of the work, not the first ten rows that happen to
    qualify -- a card whose quote is highlighted against its printed page teaches a reader what this
    page is, and a card with a bare status pill teaches them nothing. So the ranking rewards exactly
    the things a reader looks at: a verified quote, then the supporting reasoning, then the rating.
    """
    score = 0
    if fields["evidence_status"] == "verified":
        score += 8
    elif fields["evidence_status"] == "partial":
        score += 3
    if fields["quoted_lines"].strip():
        score += 6
    if fields["concept"].strip():
        score += 5
    if fields["approach"].strip():
        score += 2
    if paper.difficulty_of(row["paper_id"], int(row["qno"]))[0]:
        score += 2
    rating = paper.categories_of(row["paper_id"], int(row["qno"]))[0] or {}
    score += 2 if rating.get("question_type") else 0
    score += 2 if rating.get("traps") else 0
    # A question whose subtopic is recorded reads better than one shown as "no subtopic".
    score += 1 if (row["topic_names"] or "").strip() else 0
    return score


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chapter", action="append", help="limit to this product chapter; repeatable")
    ap.add_argument("--papers", nargs="*", help="limit to these paper ids")
    ap.add_argument("--name", default="ncert_paper_map")
    ap.add_argument("--no-fold", action="store_true",
                    help="render every card fully open and omit the fold control. Use for the PDF "
                         "build: a closed <details> is not laid out at all by a print engine, so a "
                         "folded page prints as 24 headers and loses every card's content.")
    ap.add_argument("--sample", nargs="?", const="default", metavar="SPEC",
                    help="keep only the most complete cards, N per subject. Default "
                         "biology=10,physics=10,chemistry=4; give your own as "
                         "`biology=12,physics=8`.")
    ap.add_argument("--finished", action="store_true",
                    help="only questions whose record is actually WRITTEN: an NCERT quote for a "
                         "quote-subject, or a concept and approach for any subject. Without it the "
                         "page fills with cards whose chapter is merely extracted.")
    ap.add_argument("--complete", action="store_true",
                    help="only questions that already carry a difficulty AND an E1-E5 rating, so "
                         "every row on the page is filled in end to end")
    ap.add_argument("--all", action="store_true",
                    help="include questions whose chapter has no NCERT extraction yet")
    args = ap.parse_args()

    rows = questions(set(args.chapter or []), set(args.papers or []),
                     staged_only=not args.all)
    if not rows:
        print("no questions matched")
        return 1
    os.makedirs(rc.pp(*TARGET_DIR), exist_ok=True)
    target = rc.pp(*TARGET_DIR, "%s.html" % args.name)
    csv_target = rc.pp(*TARGET_DIR, "%s.csv" % args.name)
    out_dir = os.path.dirname(target)

    index = subtopic_index(questions(set(), set(), staged_only=False))
    on_page = {(r["paper_id"], int(r["qno"])) for r in rows}
    cards, csv_rows, entries, tally = [], [], [], collections.Counter()
    for row in rows:
        paper_id, qno = row["paper_id"], int(row["qno"])
        record = None
        with open(rc.pp(*CORPUS, "papers", "%s.json" % paper_id), encoding="utf-8") as fh:
            for candidate in json.load(fh)["questions"]:
                if candidate["qno"] == qno:
                    record = candidate
                    break
        if record is None:
            continue
        item = "%s#q%03d" % (paper_id, qno)
        if args.finished:
            # A question BELONGS on this page when something has been written about it, and what
            # counts differs by subject -- which is the whole routing rule, applied to the page.
            #
            #   Physics, Physical Chemistry   a concept and approach. Their D4V packets exist but
            #                                 are leftovers from before the routing change: they
            #                                 are what MEASURED the problem (2 of 27 reached
            #                                 `fully`), not results anyone should read as evidence.
            #   Biology, Organic, Inorganic   a quoted NCERT line -- or a concept, where the
            #                                 question solves something.
            has_concept = bool(concept_approach(paper_id, qno).get("concept"))
            evidence = _load(OUT, item)
            has_quote = bool(evidence and (evidence.get("evidence") or []))
            if not (has_concept or (has_quote and not concept_only(row))):
                tally["nothing written yet"] += 1
                continue
        if args.complete:
            band = paper.difficulty_of(paper_id, qno)[0]
            rated = paper.categories_of(paper_id, qno)[0]
            if not band or not rated:
                tally["chain incomplete"] += 1
                continue
        card = paper.question_card(paper_id, record, target, show_paper=True)
        block, fields, record = ncert_block(row, item, out_dir,
                                           siblings=similar_html(row, index, out_dir, on_page))
        tally[fields["evidence_status"]] += 1
        # The NCERT block belongs INSIDE the card, so it is spliced in before the card's own closing
        # tag rather than appended after it -- otherwise the evidence sits in the gap between two
        # questions and a reader cannot tell which of them it belongs to.
        card = card.replace(
            '<div class="q">',
            '<div class="q %s" id="%s" data-subject="%s" data-status="%s" data-difficulty="%s">'
            % (subject_class(row), anchor_id(paper_id, qno),
               html.escape((row.get("subject") or "").strip().lower()),
               html.escape(fields["evidence_status"]),
               html.escape(paper.difficulty_of(paper_id, qno)[0] or "unrated")), 1)
        # A BLIND SOLVE THAT DISAGREES WITH THE BOOKLET is the most consequential thing a card can
        # say, and it was a faint table background. It now marks the card itself.
        if "differ" in (row.get("answer_verdict") or "").lower():
            card = card.replace('<div class="q ', '<div class="q disputed ', 1)
        subtopics = [t.strip() for t in (row["topic_names"] or "").split(";") if t.strip()]
        entries.append({
            "subject": (row.get("stream") or row.get("subject") or "?").title(),
            "cls": subject_class(row),
            "anchor": anchor_id(paper_id, qno),
            "short": "%s Q%d" % (paper_id.replace("_", " "), qno),
            "status": fields["evidence_status"],
            "subject_key": (row.get("subject") or "?").strip().lower(),
            "difficulty": paper.difficulty_of(paper_id, qno)[0] or "unrated",
            # A stable hue per chapter, derived from its name so it never shifts between builds.
            # Repeat chapters then read as repeats in the index without a legend.
            "chapter_hue": "hsl(%d 45%% 38%%)" % (
                sum(ord(c) for c in (row["chapter_names"] or "").split(";")[0].strip()) * 37 % 360),
            "score": completeness(row, fields),
            "tip": "%s  |  %s  |  %s" % ((row["chapter_names"] or "").split(";")[0].strip(),
                                         subtopics[0] if subtopics else "no subtopic",
                                         fields["evidence_label"]),
        })
        card = restructure(card, block, summary_strip(row, fields, record),
                           fold=not args.no_fold,
                           nav='<span class="cnav"><a class="cn" href="#index" title="back to the index">&#9650;</a>'
            '<a class="cn prev" href="#" title="previous question">&#8249;</a>'
            '<a class="cn next" href="#" title="next question">&#8250;</a></span>',
        pill='<span class="evstat %s">%s</span>'
                                % (fields["evidence_status"], fields["evidence_label"]))
        cards.append(card + "</div>")
        csv_rows.append(csv_row(row, fields))

    if args.sample:
        wanted = collections.OrderedDict(SAMPLE)
        if args.sample != "default":
            wanted = collections.OrderedDict(
                (k.strip().lower(), int(v)) for k, v in
                (part.split("=") for part in args.sample.split(",") if "=" in part))
        picked, kept = collections.Counter(), []
        order = sorted(range(len(cards)), key=lambda i: -entries[i]["score"])
        for i in order:
            subject = entries[i]["subject_key"]
            if picked[subject] >= wanted.get(subject, 0):
                continue
            picked[subject] += 1
            kept.append(i)
        kept.sort()                                  # back into paper order for reading
        cards = [cards[i] for i in kept]
        entries = [entries[i] for i in kept]
        csv_rows = [csv_rows[i] for i in kept]
        tally = collections.Counter(e["status"] for e in entries)
        print("sampled %d card(s): %s"
              % (len(cards), ", ".join("%s %d" % (k, v) for k, v in picked.most_common())))

    with open(target, "w", encoding="utf-8") as fh:
        fh.write(paper.page_shell(title="NCERT evidence map",
                                  body=index_html(entries) + "".join(cards) + SCRIPT,
                                  extra_css=EXTRA_CSS, force_light=True))
    with open(csv_target, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for out in csv_rows:
            writer.writerow(out)

    print("html  %-46s %3d questions" % (os.path.relpath(target, rc.pp()), len(cards)))
    print("csv   %-46s %3d rows, %d columns"
          % (os.path.relpath(csv_target, rc.pp()), len(csv_rows), len(CSV_COLUMNS)))
    for key in ("concept", "verified", "partial", "pending", "cut", "missing"):
        if tally[key]:
            print("  %-10s %d" % (key, tally[key]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
