#!/usr/bin/env python3
"""ONE workbook with everything. Replaces the four separate workbooks and the loose CSVs.

    python3 scripts/build_master_workbook.py        # -> exports/<today>/NEET_PYQ_pipeline.xlsx
    python3 scripts/build_master_workbook.py --keep-parts   # don't delete the old files

The exports folder had grown to four .xlsx files plus eleven loose .csv files, several of which
said the same thing in different shapes. That is worse than no export: a reader cannot tell which
file is current or authoritative. This builds a single workbook, in pipeline order, and removes
the superseded pieces.

Tab order follows the pipeline, so reading left to right is reading the process:

    START HERE     what every tab is, and how to read the colours
    PROGRESS       milestone status
    0  INTAKE      what arrived, what is missing
    A  ...         the textbook: books, chapters, passages, subtopics
    B  ...         the questions: the bank, the blind check
    C  DUPLICATES  merges across booklet codes
    D  MAPPING     question -> chapter -> subtopic -> quoted NCERT line
    E  TAGS        what Stage E will hold (not built out yet)
    WORK LIST      every flag, worst first
    SOURCES        where the papers and books came from, and how far each is trusted
    SOURCE CHECK   the three-way verification of extracted text
    FIGURES        per-paper figure coverage

Colour is never the only signal: every coloured cell has a neighbouring column saying the same
thing in words, so the file survives printing, copying, and colour-blind readers.

NOT A RELEASE. Spec 14/F5 reserves released data for `export_tables.py` -> `data/`, only after a
chapter's review queue is empty and a person has signed it off. Every row here still carries its
flags, so nothing can be mistaken for approved output.
"""
import argparse
import collections
import csv
import datetime
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

RED = PatternFill("solid", fgColor="F8D7DA")
AMBER = PatternFill("solid", fgColor="FFF3CD")
GREEN = PatternFill("solid", fgColor="D6EFD8")
GREY = PatternFill("solid", fgColor="E9ECEF")
HEAD = PatternFill("solid", fgColor="1F3A5F")
F_HEAD = Font(bold=True, color="FFFFFF", size=11)
F_TITLE = Font(bold=True, size=14, color="1F3A5F")
F_NOTE = Font(italic=True, size=10, color="444444")
F_BOLD = Font(bold=True)
THIN = Side(style="thin", color="BBBBBB")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

SEV = {"blocker": RED, "high": AMBER, "normal": AMBER, "low": GREY}
STAT = {"pass": GREEN, "flagged": AMBER, "blocked": RED, "skipped": GREY, "stale": AMBER}


def _jsonl(p):
    out = []
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for ln in f:
                ln = ln.strip()
                if ln:
                    try:
                        out.append(json.loads(ln))
                    except Exception:
                        pass
    return out


def _json(p):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _csv(p):
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def _flat(v, limit=None):
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        s = " | ".join(_flat(x) for x in v)
    elif isinstance(v, dict):
        s = json.dumps(v, ensure_ascii=False, sort_keys=True)
    else:
        s = str(v)
    return s[:limit] if limit else s


def _tab(wb, title, heading, what, look=""):
    ws = wb.create_sheet(title[:31])
    ws["A1"] = heading
    ws["A1"].font = F_TITLE
    ws["A2"] = what
    ws["A2"].font = F_NOTE
    if look:
        ws["A3"] = "LOOK AT: " + look
        ws["A3"].font = F_NOTE
    ws.freeze_panes = "A6"
    return ws


def _write(ws, cols, rows, start=5, fills=None, widths=None, wrap_from=2):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=start, column=i, value=c)
        cell.fill, cell.font, cell.border = HEAD, F_HEAD, BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[start].height = 30
    r = start + 1
    for item in rows:
        rf = fills(item) if fills else {}
        for i, c in enumerate(cols, 1):
            cell = ws.cell(row=r, column=i, value=item.get(c, ""))
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=(i >= wrap_from))
            if c in rf:
                cell.fill = rf[c]
        r += 1
    for i, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(c, 18)
    ws.auto_filter.ref = f"A{start}:{get_column_letter(len(cols))}{max(r-1, start)}"


# ---------------------------------------------------------------------------

def _records():
    d = rc.pp("papers", "records")
    out = []
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.startswith("Q-") and fn.endswith(".json"):
                r = _json(os.path.join(d, fn))
                if r:
                    out.append(r)
    return out


def _flags_by_item():
    by = collections.defaultdict(list)
    for f in _jsonl(rc.pp("flags", "flags.jsonl")):
        by[f.get("item_id")].append(f)
    return by


_FLAG_MEANING = {
    "S0_MISSING_INPUT": "A file the project needs was not supplied",
    "A1_REGISTER_DRAFT": "Every registered book starts as a draft — routine",
    "A2_CHECK_FAILED": "A page reading failed its automatic check",
    "A2_JOIN_ADJUDICATED": "Two pages disagreed about text continuing across the break",
    "A2_TEXT_MISMATCH": "Transcription didn't match the page's own text layer closely enough",
    "A2_UNREADABLE": "The page could not be read at all (infrastructure, not data)",
    "A2_SPECIAL_UNREAD": "A table/figure/equation block still needs transcribing",
    "A4_SUBTOPICS_DRAFT": "A chapter's subtopic list needs approval before real use",
    "B1_REGISTER_DRAFT": "Every registered paper starts as a draft — routine",
    "B4_MISMATCH_ADJUDICATED": "Two independent readings of the question disagreed",
    "B6_IMAGE_INPUT_UNSAFE": "Blind solver refused: the only image also shows the answer",
    "B8_CORRECTION": "Board dropped/bonused this question; a correction was proposed",
    "B9_FIGURE_RECOVERED": "A missing figure was found in the legacy sheets and attached",
    "B9_FIGURE_EXTRA_IMAGES": "Source row had more than one image; only the first was attached",
    "B9_FIGURE_UNMATCHED": "No figure could be confidently matched",
    "D1_NO_CHAPTERS": "No NCERT chapter for this subject is indexed yet",
    "D1_GUESS": "Runs and adjudicator were unsure which chapter — low confidence",
    "D2_GUESS": "Same, for the subtopic",
    "D3_NO_PASSAGES": "The chosen subtopic has no textbook passages linked to it",
    "D5_NO_OLDER_PASSAGES": "No older-edition book is indexed, so nothing to compare",
    "D6_STATUS_UNVERIFIABLE": "Syllabus status can't be verified without the change log",
    "E4_NO_CODEBOOK": "Thinking tags produced without the owner's codebook",
}


def tab_start(wb, stats):
    ws = wb.create_sheet("START HERE")
    ws["A1"] = "NEET PYQ pipeline — all data, one workbook"
    ws["A1"].font = Font(bold=True, size=16, color="1F3A5F")
    ws["A2"] = f"Generated {rc.now_iso()}"
    ws["A2"].font = F_NOTE
    ws["A3"] = ("Read-only. This is NOT released data — nothing here has been through review or "
                "signed off.")
    ws["A3"].font = F_NOTE

    r = 5
    ws.cell(row=r, column=1, value="COLOURS").font = F_BOLD
    r += 1
    for name, meaning, fill in [
            ("RED", "Blocker — cannot proceed until fixed", RED),
            ("AMBER", "Needs a look — the pipeline said it was unsure", AMBER),
            ("GREEN", "Verified — a real check passed", GREEN),
            ("GREY", "Not reached yet — no work attempted", GREY)]:
        c = ws.cell(row=r, column=1, value=name)
        c.fill, c.font, c.border = fill, F_BOLD, BORDER
        ws.cell(row=r, column=2, value=meaning)
        r += 1
    ws.cell(row=r, column=1,
            value="Colour is never the only signal — a neighbouring column always says the same "
                  "thing in words.").font = F_NOTE
    r += 2

    ws.cell(row=r, column=1, value="HEADLINE NUMBERS").font = F_BOLD
    r += 1
    for k, v in stats.items():
        ws.cell(row=r, column=1, value=k).font = F_BOLD
        ws.cell(row=r, column=2, value=v)
        r += 1
    r += 1

    ws.cell(row=r, column=1, value="THE TABS").font = F_BOLD
    r += 1
    for name, desc in [
        ("PROGRESS", "Milestone status against the plan"),
        ("0 INTAKE", "What arrived and what is missing"),
        ("A BOOKS", "Each NCERT book and its exact edition"),
        ("A CHAPTERS", "Chapters indexed, and how many passages each has"),
        ("A PASSAGES", "The NCERT text answers get quoted from"),
        ("A SUBTOPICS", "Subtopics, and whether passages are actually linked to them"),
        ("B QUESTIONS", "The question bank — one row per unique question"),
        ("B BLIND CHECK", "The independent solve, done without seeing the key"),
        ("C DUPLICATES", "Same question across booklet codes, merged"),
        ("D MAPPING", "Question -> chapter -> subtopic -> the quoted NCERT line"),
        ("E TAGS", "What Stage E will hold (taxonomy built, tagging not run)"),
        ("WORK LIST", "Every flag, worst first — this is the to-do list"),
        ("SOURCES", "Where papers and books came from, and how far each is trusted"),
        ("SOURCE CHECK", "Three-way verification that the extracted text is faithful"),
        ("FIGURES", "Per-paper figure coverage"),
    ]:
        ws.cell(row=r, column=1, value=name).font = F_BOLD
        ws.cell(row=r, column=2, value=desc)
        r += 1

    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 92


def main(argv=None):
    ap = argparse.ArgumentParser(description="One workbook with everything.")
    ap.add_argument("--keep-parts", action="store_true",
                    help="Keep the superseded CSVs and per-topic workbooks.")
    ap.add_argument("--outdir")
    args = ap.parse_args(argv)

    outdir = args.outdir or rc.pp("exports", datetime.date.today().isoformat())
    rc.ensure_dir(outdir)
    out = os.path.join(outdir, "NEET_PYQ_pipeline.xlsx")

    recs = _records()
    canon = [r for r in recs if not r.get("merged_into")]
    by_item = _flags_by_item()
    flags = _jsonl(rc.pp("flags", "flags.jsonl"))

    passages, chapters, subtopics = [], [], []
    links = collections.Counter()
    pdir = rc.pp("ncert", "passages")
    for fn in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if fn.endswith(".jsonl"):
            passages += _jsonl(os.path.join(pdir, fn))
    ldir = rc.pp("ncert", "links")
    for fn in sorted(os.listdir(ldir)) if os.path.isdir(ldir) else []:
        if fn.endswith(".jsonl"):
            for l in _jsonl(os.path.join(ldir, fn)):
                links[l.get("subtopic_id")] += 1
    cdir = rc.pp("ncert", "chapters")
    for fn in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        if fn.endswith(".json"):
            d = _json(os.path.join(cdir, fn))
            chapters += d if isinstance(d, list) else [d]
    sdir = rc.pp("ncert", "subtopics")
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if fn.endswith(".json"):
            d = _json(os.path.join(sdir, fn)) or {}
            for st in d.get("subtopics") or []:
                st["_chapter"] = d.get("chapter_id")
                subtopics.append(st)

    pcount = collections.Counter(p.get("chapter_id") for p in passages)
    sev = collections.Counter(f.get("severity") for f in flags)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    tab_start(wb, {
        "Questions in the bank": len(canon),
        "NCERT chapters indexed": len(chapters),
        "NCERT passages": len(passages),
        "Subtopics": len(subtopics),
        "Open flags": len(flags),
        "  blockers": sev.get("blocker", 0),
        "  need a look": sev.get("high", 0) + sev.get("normal", 0),
    })

    # ---- PROGRESS ----------------------------------------------------------
    ws = _tab(wb, "PROGRESS", "MILESTONE STATUS", "Where the project stands against the plan.")
    nq = len(canon)
    _write(ws, ["milestone", "what it means", "status", "what is needed"], [
        {"milestone": "1. Category check sheet", "what it means":
         "~300 questions described with no categories shown, grouped, sent to the owner to approve",
         "status": "BLOCKED", "what is needed":
         f"~300 questions; the bank has {nq}. Everything else for it is built."},
        {"milestone": "2a. Stage A — index NCERT", "what it means":
         "Every chapter indexed; D1 needs the full chapter list",
         "status": f"{len(chapters)} chapters", "what is needed":
         f"{len(chapters)} of roughly 37 needed."},
        {"milestone": "2b. Stage A — change log", "what it means":
         "Old vs new edition compared and judged", "status": "NOT RUN",
         "what is needed": "No older-edition book is indexed yet; A8 has never run on real data."},
        {"milestone": "2c. Stage B — extract papers", "what it means":
         "Every in-scope paper read into question records",
         "status": f"{nq} questions", "what is needed":
         "A single year holds roughly 1,800. Extraction run in progress."},
        {"milestone": "3a. Faculty agreement (150)", "what it means":
         "50 per subject shown to faculty WITHOUT the pipeline's tags; target >=85% agreement",
         "status": "BLOCKED", "what is needed": "Needs Stage E tagging to have run."},
        {"milestone": "3b. Gold set (90)", "what it means":
         "30 per subject, every field confirmed by a reviewer", "status": "BLOCKED",
         "what is needed": "Needs a reviewed pilot to sample from."},
        {"milestone": "4. Pilot — 3 chapters A-F", "what it means":
         "One chapter per subject end to end, then scored and fixed", "status": "NOT STARTED",
         "what is needed": "Needs Stage E output and a review round."},
        {"milestone": "5. Full run", "what it means": "All papers, all chapters, then release",
         "status": "NOT STARTED", "what is needed": "Follows the pilot meeting its targets."},
    ], fills=lambda r: {"status": GREY if ("NOT" in r["status"] or "BLOCK" in r["status"]) else AMBER},
       widths={"milestone": 30, "what it means": 66, "status": 16, "what is needed": 70})

    # ---- 0 INTAKE ----------------------------------------------------------
    ws = _tab(wb, "0 INTAKE", "STEP 0 — INTAKE", "Did every input the pipeline needs arrive?",
              "RED = a required input is missing.")
    _write(ws, ["what is missing", "severity", "details"],
           [{"what is missing": _flat(f.get("item_id")), "severity": _flat(f.get("severity")),
             "details": _flat(f.get("message"), 300)}
            for f in flags if f.get("step") == "S0"],
           fills=lambda r: {"severity": SEV.get(r["severity"], GREY)},
           widths={"what is missing": 34, "severity": 11, "details": 96})

    # ---- A BOOKS / CHAPTERS / PASSAGES / SUBTOPICS -------------------------
    ws = _tab(wb, "A BOOKS", "STAGE A — BOOKS AND EDITIONS",
              "Each NCERT book and the exact edition we are reading.",
              "The reprint line is copied verbatim off the real cover; a wrong edition quietly "
              "corrupts everything downstream.")
    _write(ws, ["book", "subject", "class", "edition", "reprint line (verbatim)", "state"],
           [{"book": b.get("book_id"), "subject": b.get("subject"), "class": b.get("class"),
             "edition": b.get("edition"), "reprint line (verbatim)": b.get("reprint_text_exact"),
             "state": b.get("status")} for b in _csv(rc.pp("register", "books.csv"))],
           fills=lambda r: {"state": STAT.get(r["state"], GREY)},
           widths={"book": 11, "subject": 12, "class": 7, "edition": 10,
                   "reprint line (verbatim)": 24, "state": 10})

    ws = _tab(wb, "A CHAPTERS", "STAGE A — CHAPTERS INDEXED",
              "The textbook turned into searchable passages, chapter by chapter.",
              "A question whose chapter is not indexed CANNOT be mapped in Stage D.")
    _write(ws, ["chapter", "title", "headings", "passages", "concern"],
           [{"chapter": c.get("chapter_id"), "title": c.get("title"),
             "headings": len(c.get("headings") or []),
             "passages": pcount.get(c.get("chapter_id"), 0),
             "concern": "" if pcount.get(c.get("chapter_id")) else "indexed but no passages yet"}
            for c in sorted(chapters, key=lambda x: _flat(x.get("chapter_id")))],
           fills=lambda r: {"passages": GREEN if r["passages"] else AMBER,
                            "concern": GREEN if not r["concern"] else AMBER},
           widths={"chapter": 15, "title": 52, "headings": 10, "passages": 11, "concern": 40})

    ws = _tab(wb, "A PASSAGES", "STAGE A — THE PASSAGES",
              "The one-idea chunks of NCERT text. Every answer is proved by quoting these.",
              "If a passage is wrong here, every quote built on it is wrong.")
    _write(ws, ["passage", "chapter", "heading", "page", "kind", "chars", "text"],
           [{"passage": p.get("passage_id"), "chapter": p.get("chapter_id"),
             "heading": _flat(p.get("section_heading"), 60), "page": p.get("page_start"),
             "kind": p.get("kind"), "chars": len(p.get("text") or ""),
             "text": _flat(p.get("text"), 900)} for p in passages],
           widths={"passage": 20, "chapter": 14, "heading": 34, "page": 7, "kind": 11,
                   "chars": 8, "text": 110})

    ws = _tab(wb, "A SUBTOPICS", "STAGE A — SUBTOPICS",
              "Each chapter split into subtopics, with textbook passages linked to them.",
              "AMBER = a subtopic with ZERO linked passages. A question sent there has no "
              "evidence available and will block.")
    _write(ws, ["subtopic", "chapter", "name", "from heading", "passages linked", "concern"],
           [{"subtopic": s.get("subtopic_id"), "chapter": s.get("_chapter"), "name": s.get("name"),
             "from heading": s.get("from_heading"),
             "passages linked": links.get(s.get("subtopic_id"), 0),
             "concern": "" if links.get(s.get("subtopic_id")) else "NO passages linked"}
            for s in subtopics],
           fills=lambda r: {"passages linked": GREEN if r["passages linked"] else AMBER,
                            "concern": GREEN if not r["concern"] else AMBER},
           widths={"subtopic": 20, "chapter": 14, "name": 50, "from heading": 13,
                   "passages linked": 14, "concern": 26})

    # ---- B QUESTIONS / BLIND CHECK ----------------------------------------
    def qrow(r):
        o = r.get("options_en") or {}
        a = r.get("official_answer")
        codes = [f["code"] for f in by_item.get(r.get("question_id"), [])
                 if f.get("status") == "open"]
        return {
            "question id": r.get("question_id"), "year": r.get("year"),
            "paper codes": _flat(r.get("paper_codes")), "subject": r.get("subject") or "",
            "branch": r.get("branch") or "", "question": _flat(r.get("stem_en")),
            "option 1": _flat(o.get("1")), "option 2": _flat(o.get("2")),
            "option 3": _flat(o.get("3")), "option 4": _flat(o.get("4")),
            "answer": _flat(a), "answer text": _flat(o.get(str(a))) if a else "",
            "official status": r.get("status") or "",
            "NCERT chapter": _flat(r.get("d1_chapter_ids")),
            "NCERT subtopic": _flat(r.get("d2_subtopic_ids")),
            "evidence quote": _flat([e.get("exact_line") for e in (r.get("d4_evidence") or [])
                                     if isinstance(e, dict)], 500),
            "needs figure": "yes" if r.get("has_figure") else "",
            "figure found": os.path.basename(r["figure_path"]) if r.get("figure_path") else "",
            "open flags": _flat(codes),
        }
    ws = _tab(wb, "B QUESTIONS", "STAGE B — THE QUESTION BANK",
              "Every unique question. Duplicates across booklet codes are already merged.",
              "'evidence quote' is the NCERT line proving the answer — empty means Stage D "
              "hasn't got there yet.")
    _write(ws, ["question id", "year", "paper codes", "subject", "branch", "question",
                "option 1", "option 2", "option 3", "option 4", "answer", "answer text",
                "official status", "NCERT chapter", "NCERT subtopic", "evidence quote",
                "needs figure", "figure found", "open flags"],
           [qrow(r) for r in canon],
           fills=lambda r: {"evidence quote": GREEN if r["evidence quote"] else AMBER,
                            "open flags": AMBER if r["open flags"] else GREEN,
                            "subject": AMBER if not r["subject"] else GREEN,
                            "figure found": GREEN if r["figure found"] else
                                (AMBER if r["needs figure"] else GREY)},
           widths={"question id": 12, "year": 7, "paper codes": 15, "subject": 11, "branch": 10,
                   "question": 62, "option 1": 20, "option 2": 20, "option 3": 20,
                   "option 4": 20, "answer": 8, "answer text": 22, "official status": 13,
                   "NCERT chapter": 15, "NCERT subtopic": 18, "evidence quote": 55,
                   "needs figure": 11, "figure found": 16, "open flags": 26})

    ws = _tab(wb, "B BLIND CHECK", "STAGE B — THE BLIND CHECK",
              "A second solver answered each question WITHOUT ever seeing the official key.",
              "This is the main accuracy test. RED = it disagreed with the official answer.")
    brows = []
    for r in canon:
        o = r.get("options_en") or {}
        off, b6 = r.get("official_answer"), r.get("b6_answer")
        if b6 is None:
            v = "COULD NOT RUN"
        elif not off:
            v = "NO KEY (dropped)"
        elif str(off) == str(b6):
            v = "AGREES"
        else:
            v = "DISAGREES"
        brows.append({"question id": r.get("question_id"), "subject": r.get("subject") or "",
                      "official": f"{_flat(off)} {_flat(o.get(str(off)), 36)}" if off else "—",
                      "blind answer": f"{_flat(b6)} {_flat(o.get(str(b6)), 36)}" if b6 else "—",
                      "verdict": v, "confidence": r.get("b6_confidence") or "",
                      "solver's reasoning": _flat(r.get("b6_reason"), 400)})
    agree = sum(1 for r in brows if r["verdict"] == "AGREES")
    ws.cell(row=4, column=1, value=f"Agreed {agree} · Disagreed "
            f"{sum(1 for r in brows if r['verdict']=='DISAGREES')} · Could not run "
            f"{sum(1 for r in brows if r['verdict']=='COULD NOT RUN')}").font = F_BOLD
    _write(ws, ["question id", "subject", "official", "blind answer", "verdict", "confidence",
                "solver's reasoning"], brows,
           fills=lambda r: {"verdict": {"AGREES": GREEN, "DISAGREES": RED}.get(r["verdict"], AMBER)},
           widths={"question id": 12, "subject": 11, "official": 28, "blind answer": 28,
                   "verdict": 16, "confidence": 11, "solver's reasoning": 85})

    # ---- C DUPLICATES ------------------------------------------------------
    ws = _tab(wb, "C DUPLICATES", "STAGE C — DUPLICATES MERGED",
              "The same question printed in different booklet codes, merged into one record.",
              "Nothing is deleted — the absorbed record is kept and points at its twin.")
    _write(ws, ["kept as", "absorbed", "now covers codes", "question"],
           [{"kept as": r.get("question_id"), "absorbed": _flat(r.get("merged_from")),
             "now covers codes": _flat(r.get("paper_codes")),
             "question": _flat(r.get("stem_en"), 220)}
            for r in recs if r.get("merged_from")],
           widths={"kept as": 12, "absorbed": 14, "now covers codes": 20, "question": 100})

    # ---- D MAPPING ---------------------------------------------------------
    ws = _tab(wb, "D MAPPING", "STAGE D — MAPPED TO THE TEXTBOOK",
              "Each question tied to its NCERT chapter, subtopic and the exact proving line.",
              "RED = blocked. AMBER = the pipeline guessed with low confidence and said so.")
    drows = []
    for r in canon:
        qid = r.get("question_id")
        drows.append({"question id": qid, "subject": r.get("subject") or "",
                      "chapter": _flat(r.get("d1_chapter_ids")) or "—",
                      "confidence": r.get("d1_confidence") or "—",
                      "subtopic": _flat(r.get("d2_subtopic_ids")) or "—",
                      "link type": r.get("link_type") or "",
                      "evidence quote": _flat([e.get("exact_line")
                                               for e in (r.get("d4_evidence") or [])
                                               if isinstance(e, dict)], 500),
                      "D1": (rc.read_item_status("D1", qid) or {}).get("status") or "—",
                      "D3": (rc.read_item_status("D3", qid) or {}).get("status") or "—",
                      "D4": (rc.read_item_status("D4", qid) or {}).get("status") or "—"})
    _write(ws, ["question id", "subject", "chapter", "confidence", "subtopic", "link type",
                "evidence quote", "D1", "D3", "D4"], drows,
           fills=lambda r: {k: STAT.get(r[k], GREY) for k in ("D1", "D3", "D4")} |
                           {"confidence": AMBER if r["confidence"] in ("low", "—") else GREEN,
                            "evidence quote": GREEN if r["evidence quote"] else AMBER},
           widths={"question id": 12, "subject": 11, "chapter": 15, "confidence": 11,
                   "subtopic": 20, "link type": 15, "evidence quote": 70,
                   "D1": 9, "D3": 9, "D4": 9})

    # ---- E TAGS ------------------------------------------------------------
    ws = _tab(wb, "E TAGS", "STAGE E — TAGS",
              "How each question is built, what it asks, and what thinking it needs.",
              "Stage E is built but has not run — it needs Stage D output first. This lists "
              "what will appear here.")
    _write(ws, ["tag", "answers the question", "example values", "state"], [
        {"tag": "E1 question_type", "answers the question": "How is it BUILT?",
         "example values": "assertion_reason, match_the_lists, list_of_statements …(19)",
         "state": "not run"},
        {"tag": "E2 format", "answers the question": "What must the student PICK?",
         "example values": "pick_correct, pick_incorrect, calculate_value …(26)", "state": "not run"},
        {"tag": "E3 content_shape", "answers the question": "What NCERT material is it on?",
         "example values": "formula, process, reaction_mechanism …(29)", "state": "not run"},
        {"tag": "E4 thinking", "answers the question": "What must they do IN THEIR HEAD?",
         "example values": "8 draft categories; Chemistry MUST condition on branch",
         "state": "not run"},
        {"tag": "E5 trap", "answers the question": "Why does each WRONG option attract?",
         "example values": "19 values, judged per wrong option (3 per question)", "state": "not run"},
        {"tag": "E6 descriptive", "answers the question": "Answer form, negation, item count …",
         "example values": "filled by script, not judgement", "state": "partly scripted"},
    ], fills=lambda r: {"state": GREY}, widths={"tag": 20, "answers the question": 40,
                                                "example values": 72, "state": 16})

    # ---- WORK LIST ---------------------------------------------------------
    ws = _tab(wb, "WORK LIST", "EVERYTHING FLAGGED — THE TO-DO LIST",
              "Every point where the pipeline was unsure or found something wrong.",
              "Worst first. RED must be resolved before the item can proceed.")
    order = {"blocker": 0, "high": 1, "normal": 2, "low": 3}
    frows = sorted(({"severity": f.get("severity"), "step": f.get("step"), "code": f.get("code"),
                     "item": f.get("item_id"),
                     "what it means": _FLAG_MEANING.get(f.get("code"), ""),
                     "the pipeline's message": _flat(f.get("message"), 300)}
                    for f in flags),
                   key=lambda r: (order.get(r["severity"], 9), r["step"] or "", r["code"] or ""))
    ws.cell(row=4, column=1, value="  ".join(f"{k}: {sev.get(k,0)}"
            for k in ("blocker", "high", "normal", "low"))).font = F_BOLD
    _write(ws, ["severity", "step", "code", "item", "what it means", "the pipeline's message"],
           frows, fills=lambda r: {"severity": SEV.get(r["severity"], GREY)},
           widths={"severity": 10, "step": 7, "code": 26, "item": 26, "what it means": 62,
                   "the pipeline's message": 80})

    # ---- SOURCES -----------------------------------------------------------
    ws = _tab(wb, "SOURCES", "WHERE EVERYTHING CAME FROM",
              "The papers and keys behind the bank, and how far each is trusted.",
              "'official' = an NTA document. The papers are third-party copies, which is why "
              "they read 'unsure'.")
    _write(ws, ["paper", "kind", "year", "sitting", "code", "trust", "in scope", "state"],
           [{"paper": p.get("paper_id"), "kind": p.get("file_kind"), "year": p.get("year"),
             "sitting": p.get("sitting"), "code": p.get("booklet_code") or "(unconfirmed)",
             "trust": p.get("trust"), "in scope": p.get("in_scope"), "state": p.get("status")}
            for p in _csv(rc.pp("register", "papers.csv"))],
           fills=lambda r: {"trust": GREEN if r["trust"] == "official" else AMBER,
                            "state": STAT.get(r["state"], GREY)},
           widths={"paper": 24, "kind": 8, "year": 7, "sitting": 9, "code": 15, "trust": 11,
                   "in scope": 9, "state": 10})

    # ---- SOURCE CHECK + FIGURES (from the verifier's own CSVs) -------------
    for fname, tabname, heading, what in [
        ("source_verification.csv", "SOURCE CHECK", "IS THE EXTRACTED TEXT FAITHFUL?",
         "Each question compared against the year-wise book AND the legacy sheet — three "
         "independent transcriptions."),
        ("figure_coverage_by_paper.csv", "FIGURES", "FIGURE COVERAGE PER PAPER",
         "Which paper files actually contain their diagrams."),
    ]:
        rows = _csv(os.path.join(outdir, fname))
        if not rows:
            continue
        ws = _tab(wb, tabname, heading, what)
        cols = list(rows[0].keys())
        _write(ws, cols, rows, widths={c: 20 for c in cols})

    wb.save(out)

    removed = []
    if not args.keep_parts:
        for fn in os.listdir(outdir):
            p = os.path.join(outdir, fn)
            if fn == os.path.basename(out) or fn.startswith("~$"):
                continue
            if fn.endswith(".csv") or (fn.endswith(".xlsx")) or fn == "README.txt":
                try:
                    os.remove(p)
                    removed.append(fn)
                except OSError as e:          # a file open in Excel cannot be removed
                    print(f"  could not remove {fn} ({e.strerror}) -- close it and re-run")

    print(f"ONE workbook: {out}")
    print(f"  {len(wb.sheetnames)} tabs: {', '.join(wb.sheetnames)}")
    if removed:
        print(f"  removed {len(removed)} superseded file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
