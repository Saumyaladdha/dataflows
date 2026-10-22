#!/usr/bin/env python3
"""Build one colour-coded Excel workbook showing everything the pipeline holds, stage by stage.

    python3 scripts/build_review_workbook.py            # -> exports/<today>/pipeline_review.xlsx
    python3 scripts/build_review_workbook.py --out X.xlsx

WHY THIS EXISTS, AND WHAT IT IS NOT
-----------------------------------
`scripts/export_snapshot.py` writes flat CSVs for machine use. This writes the *human* view: one
tab per stage, in pipeline order, each with a plain-English header saying what the tab holds and
what to look at, and every cell that deserves attention coloured. The owner asked to be able to
open one file and understand the data without reading code.

It is NOT the Stage F review pack (`build_review_pack.py`, spec 14/F1) and must not be mistaken
for it. The review pack is the formal decision surface: it carries an approve/correct/block form
per item and writes `review/decisions.csv`, which drives the cascade. This workbook is read-only
reporting -- it collects no decisions, writes nothing back into the pipeline, and confers no
approval. Keeping them separate matters because spec Section 14 makes the pack the only route by
which a human judgement enters the data.

COLOUR KEY (identical on every tab, also written onto the first tab)
  RED    blocker            - this item cannot proceed; something is missing or contradictory
  AMBER  needs a look       - the pipeline is unsure and said so; a person should confirm
  GREEN  verified           - a real check passed, or two independent runs agreed
  GREY   not reached yet    - no work has been attempted; absence of data, not a problem

Colour encodes the SAME information as the text in the row (there is always a `status` or
`concern` column saying it in words), so the file stays readable if colours are lost in a copy,
export or print, and for a colour-blind reader.
"""
import argparse
import collections
import datetime
import json
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
from lib import io as lib_io  # noqa: E402

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:  # pragma: no cover
    print("openpyxl is required:  pip install openpyxl", file=sys.stderr)
    raise

# ---------------------------------------------------------------------------
# palette
# ---------------------------------------------------------------------------
RED = PatternFill("solid", fgColor="F8D7DA")
AMBER = PatternFill("solid", fgColor="FFF3CD")
GREEN = PatternFill("solid", fgColor="D6EFD8")
GREY = PatternFill("solid", fgColor="E9ECEF")
HEAD = PatternFill("solid", fgColor="1F3A5F")
SUBHEAD = PatternFill("solid", fgColor="DDE5EE")

F_HEAD = Font(bold=True, color="FFFFFF", size=11)
F_TITLE = Font(bold=True, size=14, color="1F3A5F")
F_NOTE = Font(italic=True, size=10, color="444444")
F_BOLD = Font(bold=True)

THIN = Side(style="thin", color="BBBBBB")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

SEV_FILL = {"blocker": RED, "high": AMBER, "normal": AMBER, "low": GREY}
STATUS_FILL = {"pass": GREEN, "flagged": AMBER, "blocked": RED,
               "skipped": GREY, "stale": AMBER, "": GREY, None: GREY}


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def _read_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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


# ---------------------------------------------------------------------------
# sheet scaffolding
# ---------------------------------------------------------------------------

def _sheet(wb, title, step_label, what_it_is, what_to_look_at):
    """Every tab opens with the same three-line explanation, so a reader never has to guess
    what they are looking at or which column matters."""
    ws = wb.create_sheet(title[:31])
    ws["A1"] = f"{step_label} — {what_it_is}"
    ws["A1"].font = F_TITLE
    ws["A2"] = f"WHAT THIS IS:  {what_it_is}"
    ws["A2"].font = F_NOTE
    ws["A3"] = f"WHAT TO LOOK AT:  {what_to_look_at}"
    ws["A3"].font = F_NOTE
    ws["A4"] = "Colours:  RED = blocker   AMBER = needs a look   GREEN = verified   GREY = not reached yet"
    ws["A4"].font = F_NOTE
    ws.freeze_panes = "A7"
    return ws


def _header(ws, row, cols):
    for i, c in enumerate(cols, start=1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.fill = HEAD
        cell.font = F_HEAD
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = BORDER
    ws.row_dimensions[row].height = 28


def _write(ws, start_row, cols, rows, fills=None, widths=None):
    """rows = list of dicts; fills = fn(row_dict) -> {col_name: PatternFill}."""
    _header(ws, start_row, cols)
    r = start_row + 1
    for item in rows:
        rowfill = fills(item) if fills else {}
        for i, c in enumerate(cols, start=1):
            cell = ws.cell(row=r, column=i, value=item.get(c, ""))
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=(i > 2))
            if c in rowfill:
                cell.fill = rowfill[c]
        r += 1
    for i, c in enumerate(cols, start=1):
        w = (widths or {}).get(c, 18)
        ws.column_dimensions[get_column_letter(i)].width = w
    return r


# ---------------------------------------------------------------------------
# tabs
# ---------------------------------------------------------------------------

def tab_start(wb, stats):
    ws = wb.create_sheet("START HERE")
    ws["A1"] = "NEET PYQ pipeline — data review workbook"
    ws["A1"].font = Font(bold=True, size=16, color="1F3A5F")
    ws["A2"] = f"Generated {rc.now_iso()}"
    ws["A2"].font = F_NOTE
    ws["A3"] = ("This is a READ-ONLY view of what the pipeline currently holds. It is not the "
                "Stage F review pack: approving anything here has no effect, because no decision "
                "is collected or written back.")
    ws["A3"].font = F_NOTE

    ws["A5"] = "HOW TO READ THE COLOURS"
    ws["A5"].font = F_BOLD
    key = [("RED", "Blocker — cannot proceed; something is missing or contradictory", RED),
           ("AMBER", "Needs a look — the pipeline is unsure and said so", AMBER),
           ("GREEN", "Verified — a real check passed, or two independent runs agreed", GREEN),
           ("GREY", "Not reached yet — no work attempted; absence of data, not a problem", GREY)]
    r = 6
    for name, meaning, fill in key:
        ws.cell(row=r, column=1, value=name).fill = fill
        ws.cell(row=r, column=1).font = F_BOLD
        ws.cell(row=r, column=1).border = BORDER
        ws.cell(row=r, column=2, value=meaning)
        r += 1
    ws.cell(row=r + 1, column=1,
            value="Every colour is also stated in words in a status/concern column, so nothing "
                  "is lost if colours don't survive a copy or print.").font = F_NOTE

    r += 3
    ws.cell(row=r, column=1, value="THE TABS, IN PIPELINE ORDER").font = F_BOLD
    r += 1
    tabs = [
        ("step00 intake", "Step 0 — Did every input we need actually arrive?",
         "RED rows = a required input is missing."),
        ("step01 books", "Step 1 — Each NCERT book and the exact edition we are reading.",
         "The reprint line is copied verbatim off the real cover; editions must not be guessed."),
        ("step02 ncert pages", "Step 2 — The textbook, turned into searchable passages.",
         "One row per chapter. GREY = not indexed yet; that is the main bottleneck."),
        ("step03 passages", "Step 3 — The actual passages. THIS is what answers get quoted from.",
         "If a passage is wrong here, every quote built on it is wrong."),
        ("step04 subtopics", "Step 4 — Each chapter split into subtopics, with passages linked.",
         "AMBER = a subtopic with no linked passage; questions routed there will block."),
        ("step05 edition changes", "Step 5 — What changed between the old and new NCERT.",
         "Drives 'answer changed' detection. Empty = the comparison has not been run for real."),
        ("step06 papers", "Step 6 — Which papers and answer keys are registered.",
         "'trust' says how sure we are of the source. Keys are official; papers are not yet."),
        ("step07 questions", "Step 7 — The question bank itself.",
         "AMBER in 'blind check' = the independent solver disagreed or could not run."),
        ("step08 blind check", "Step 8 — The independent solve, done WITHOUT seeing the key.",
         "The main accuracy check. RED = it disagreed with the official answer: look at these."),
        ("step09 duplicates", "Step 9 — Same question across booklet codes, merged into one.",
         "Each row is a merge actually performed."),
        ("step10 mapping", "Step 10 — Each question tied to a chapter, subtopic and NCERT quote.",
         "RED = blocked (usually its chapter is not indexed). AMBER = a low-confidence guess."),
        ("step11 tags", "Step 11 — How each question is built and what thinking it needs.",
         "Stage E is not built yet, so this tab explains what will go here."),
        ("step12 flags", "Everything the pipeline flagged, worst first.",
         "This is the work list. RED first, then AMBER."),
        ("step13 progress", "Milestone status against the plan.",
         "Honest percentages; GREY means not started."),
    ]
    for name, what, look in tabs:
        ws.cell(row=r, column=1, value=name).font = F_BOLD
        ws.cell(row=r, column=2, value=what)
        ws.cell(row=r, column=3, value=look)
        r += 1

    r += 2
    ws.cell(row=r, column=1, value="HEADLINE NUMBERS").font = F_BOLD
    r += 1
    for k, v in stats.items():
        ws.cell(row=r, column=1, value=k).font = F_BOLD
        ws.cell(row=r, column=2, value=v)
        r += 1

    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 62
    ws.column_dimensions["C"].width = 60


def tab_s0(wb):
    ws = _sheet(wb, "step00 intake", "STEP 00 · INTAKE (S0)",
                "Did every input the pipeline needs actually arrive?",
                "RED = a required input is missing. Everything downstream of a missing input is "
                "limited by it.")
    flags = [f for f in _read_jsonl(rc.pp("flags", "flags.jsonl")) if f.get("step") == "S0"]
    rows = []
    for f in flags:
        rows.append({"what is missing": _flat(f.get("item_id")),
                     "severity": _flat(f.get("severity")),
                     "status": "OPEN" if f.get("status") == "open" else _flat(f.get("status")),
                     "details": _flat(f.get("message"), 300)})
    manifest = lib_io.read_csv(rc.pp("inputs", "manifest.csv")) if os.path.exists(
        rc.pp("inputs", "manifest.csv")) else []
    counts = collections.Counter(r.get("kind") for r in manifest)
    ws.cell(row=5, column=1,
            value=f"Inputs registered: {len(manifest)} files  ({', '.join(f'{k}={v}' for k, v in sorted(counts.items()) if k)})").font = F_BOLD
    _write(ws, 7, ["what is missing", "severity", "status", "details"], rows,
           fills=lambda r: {"severity": SEV_FILL.get(r["severity"], GREY),
                            "what is missing": SEV_FILL.get(r["severity"], GREY)},
           widths={"what is missing": 34, "severity": 12, "status": 10, "details": 90})
    if not rows:
        ws.cell(row=8, column=1, value="No missing inputs. ").fill = GREEN


def tab_ncert(wb):
    ws = _sheet(wb, "step02 ncert pages", "STEP 02 · NCERT PAGES READ (A1-A3)",
                "The textbook turned into searchable passages, chapter by chapter.",
                "GREY = chapter not indexed yet. A question whose chapter is not indexed CANNOT "
                "be mapped in Stage D — this is the pipeline's main bottleneck today.")
    passages = collections.Counter()
    for fn in sorted(os.listdir(rc.pp("ncert", "passages"))) if os.path.isdir(rc.pp("ncert", "passages")) else []:
        if fn.endswith(".jsonl"):
            for p in _read_jsonl(rc.pp("ncert", "passages", fn)):
                passages[p.get("chapter_id")] += 1
    rows = []
    cdir = rc.pp("ncert", "chapters")
    if os.path.isdir(cdir):
        for fn in sorted(os.listdir(cdir)):
            if not fn.endswith(".json"):
                continue
            data = _read_json(os.path.join(cdir, fn))
            for ch in (data if isinstance(data, list) else [data]):
                if not isinstance(ch, dict):
                    continue
                cid = ch.get("chapter_id")
                n = passages.get(cid, 0)
                rows.append({"chapter": _flat(cid), "title": _flat(ch.get("title")),
                             "headings found": len(ch.get("headings") or []),
                             "passages indexed": n,
                             "state": "indexed" if n else "no passages yet",
                             "concern": "" if n else "indexed but no passages — Stage D cannot quote from it"})
    books = lib_io.read_csv(rc.pp("register", "books.csv")) if os.path.exists(rc.pp("register", "books.csv")) else []
    ws.cell(row=5, column=1,
            value=f"Books registered: {len(books)}   Chapters indexed: {len(rows)}   "
                  f"Passages total: {sum(passages.values())}").font = F_BOLD
    _write(ws, 7, ["chapter", "title", "headings found", "passages indexed", "state", "concern"],
           rows,
           fills=lambda r: {"state": GREEN if r["passages indexed"] else AMBER,
                            "passages indexed": GREEN if r["passages indexed"] else AMBER,
                            "concern": AMBER if r["concern"] else GREEN},
           widths={"chapter": 16, "title": 46, "headings found": 14, "passages indexed": 16,
                   "state": 16, "concern": 60})


def tab_books(wb):
    ws = _sheet(wb, "step01 books", "STEP 01 · BOOKS AND EDITIONS (A1)",
                "Each NCERT book we are reading, and the exact edition it is.",
                "The reprint line is copied verbatim off the real cover. Edition matters: a "
                "question's answer can change between editions, so a wrong edition here quietly "
                "corrupts everything downstream.")
    rows = []
    for b in (lib_io.read_csv(rc.pp("register", "books.csv"))
              if os.path.exists(rc.pp("register", "books.csv")) else []):
        rows.append({"book": _flat(b.get("book_id")), "subject": _flat(b.get("subject")),
                     "class": _flat(b.get("class")), "edition": _flat(b.get("edition")),
                     "reprint line (copied exactly)": _flat(b.get("reprint_text_exact")),
                     "state": _flat(b.get("status")),
                     "concern": "" if b.get("reprint_text_exact") else "no reprint line read — edition unconfirmed"})
    ws.cell(row=5, column=1, value=f"Books registered: {len(rows)}").font = F_BOLD
    _write(ws, 7, ["book", "subject", "class", "edition", "reprint line (copied exactly)",
                   "state", "concern"], rows,
           fills=lambda r: {"state": STATUS_FILL.get(r["state"], GREY),
                            "concern": AMBER if r["concern"] else GREEN},
           widths={"book": 11, "subject": 12, "class": 7, "edition": 10,
                   "reprint line (copied exactly)": 26, "state": 10, "concern": 52})


def tab_passages(wb):
    ws = _sheet(wb, "step03 passages", "STEP 03 · THE PASSAGES (A3)",
                "The one-idea chunks of NCERT text. This is what every answer gets quoted from.",
                "If a passage is wrong or truncated here, every quote built on it is wrong too. "
                "Spot-check a few against the real book.")
    rows = []
    pdir = rc.pp("ncert", "passages")
    for fn in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if not fn.endswith(".jsonl"):
            continue
        for p in _read_jsonl(os.path.join(pdir, fn)):
            txt = p.get("text") or ""
            rows.append({"passage": _flat(p.get("passage_id")), "chapter": _flat(p.get("chapter_id")),
                         "heading": _flat(p.get("section_heading"), 60),
                         "page": _flat(p.get("page_start")), "kind": _flat(p.get("kind")),
                         "characters": len(txt), "text": _flat(txt, 400),
                         "concern": "very short — may be a fragment" if len(txt) < 40 else ""})
    short = sum(1 for r in rows if r["concern"])
    ws.cell(row=5, column=1,
            value=f"Passages: {len(rows)}   Suspiciously short: {short}").font = F_BOLD
    _write(ws, 7, ["passage", "chapter", "heading", "page", "kind", "characters", "text",
                   "concern"], rows,
           fills=lambda r: {"concern": AMBER if r["concern"] else GREEN,
                            "characters": AMBER if r["concern"] else GREEN},
           widths={"passage": 20, "chapter": 14, "heading": 34, "page": 7, "kind": 11,
                   "characters": 11, "text": 95, "concern": 30})


def tab_changes(wb):
    ws = _sheet(wb, "step05 edition changes", "STEP 05 · EDITION CHANGES (A6-A9)",
                "What actually changed between the old and the new NCERT.",
                "This drives 'the answer changed' detection. An EMPTY tab means the comparison "
                "has not been run on real data yet — not that nothing changed.")
    path = rc.pp("ncert", "change_log.csv")
    rows = []
    for r in (lib_io.read_csv(path) if os.path.exists(path) else []):
        rows.append({"change": _flat(r.get("change_id")), "chapter": _flat(r.get("chapter_id")),
                     "type": _flat(r.get("change_type")),
                     "old text": _flat(r.get("older_text"), 220),
                     "new text": _flat(r.get("latest_text"), 220),
                     "concern": "fact changed — answers may differ by edition"
                                if r.get("change_type") == "fact_changed" else ""})
    if not rows:
        ws.cell(row=5, column=1,
                value="NOT RUN YET. A6/A7/A9 have only been tested on hand-built fixtures, and "
                      "A8 (the agent that judges whether a change is a real fact change or just "
                      "rewording) has never run on real data. Nothing here means 'unknown', not "
                      "'no changes'.").fill = AMBER
        ws.cell(row=5, column=1).font = F_BOLD
    _write(ws, 7, ["change", "chapter", "type", "old text", "new text", "concern"], rows,
           fills=lambda r: {"concern": AMBER if r["concern"] else GREEN},
           widths={"change": 12, "chapter": 14, "type": 16, "old text": 60, "new text": 60,
                   "concern": 42})


def tab_papers(wb):
    ws = _sheet(wb, "step06 papers", "STEP 06 · PAPERS AND KEYS (B1)",
                "Which question papers and answer keys are registered, and how far we trust each.",
                "'trust' is the column that matters. The answer KEYS are official. The PAPERS are "
                "currently third-party copies, so they read 'unsure' — that is honest, not a bug.")
    rows = []
    for p in (lib_io.read_csv(rc.pp("register", "papers.csv"))
              if os.path.exists(rc.pp("register", "papers.csv")) else []):
        trust = _flat(p.get("trust"))
        rows.append({"paper": _flat(p.get("paper_id")), "kind": _flat(p.get("file_kind")),
                     "year": _flat(p.get("year")), "sitting": _flat(p.get("sitting")),
                     "booklet code": _flat(p.get("booklet_code")) or "(not confirmed)",
                     "trust": trust, "in scope": _flat(p.get("in_scope")),
                     "state": _flat(p.get("status")),
                     "concern": "" if trust == "official" else
                                "third-party copy — content not verified against an official paper"})
    ws.cell(row=5, column=1, value=f"Papers and keys registered: {len(rows)}").font = F_BOLD
    _write(ws, 7, ["paper", "kind", "year", "sitting", "booklet code", "trust", "in scope",
                   "state", "concern"], rows,
           fills=lambda r: {"trust": GREEN if r["trust"] == "official" else AMBER,
                            "state": STATUS_FILL.get(r["state"], GREY),
                            "concern": AMBER if r["concern"] else GREEN},
           widths={"paper": 22, "kind": 8, "year": 7, "sitting": 9, "booklet code": 15,
                   "trust": 11, "in scope": 9, "state": 9, "concern": 60})


def tab_blind(wb):
    ws = _sheet(wb, "step08 blind check", "STEP 08 · THE BLIND CHECK (B6)",
                "A second solver answered each question WITHOUT ever seeing the official key.",
                "This is the pipeline's main accuracy test. RED = it disagreed with the official "
                "answer — those are the questions worth a human eye. AMBER = it could not run, "
                "usually because the question needs a figure we do not have.")
    rows = []
    rdir = rc.pp("papers", "records")
    for fn in sorted(os.listdir(rdir)) if os.path.isdir(rdir) else []:
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _read_json(os.path.join(rdir, fn)) or {}
        if rec.get("merged_into"):
            continue
        opts = rec.get("options_en") or {}
        off, b6 = rec.get("official_answer"), rec.get("b6_answer")
        if b6 is None:
            verdict, why = "COULD NOT RUN", "needs a figure we do not have" if rec.get("has_figure") else "not dispatched yet"
        elif not off:
            verdict, why = "NO KEY", "question was dropped by the board — nothing to compare"
        elif str(off) == str(b6):
            verdict, why = "AGREES", ""
        else:
            verdict, why = "DISAGREES", "blind solver and official key differ — review this"
        rows.append({"question": _flat(rec.get("question_id")),
                     "subject": _flat(rec.get("subject")),
                     "official answer": f"{_flat(off)} {_flat(opts.get(str(off)), 40)}" if off else "—",
                     "blind answer": f"{_flat(b6)} {_flat(opts.get(str(b6)), 40)}" if b6 else "—",
                     "verdict": verdict,
                     "solver's reasoning": _flat(rec.get("b6_reason"), 260),
                     "concern": why})
    agree = sum(1 for r in rows if r["verdict"] == "AGREES")
    dis = sum(1 for r in rows if r["verdict"] == "DISAGREES")
    ws.cell(row=5, column=1,
            value=f"Agreed: {agree}   Disagreed: {dis}   Could not run: "
                  f"{sum(1 for r in rows if r['verdict'] == 'COULD NOT RUN')}").font = F_BOLD
    _write(ws, 7, ["question", "subject", "official answer", "blind answer", "verdict",
                   "solver's reasoning", "concern"], rows,
           fills=lambda r: {"verdict": {"AGREES": GREEN, "DISAGREES": RED}.get(r["verdict"], AMBER),
                            "concern": GREEN if not r["concern"] else AMBER},
           widths={"question": 12, "subject": 12, "official answer": 30, "blind answer": 30,
                   "verdict": 15, "solver's reasoning": 70, "concern": 42})


def tab_tags(wb):
    ws = _sheet(wb, "step11 tags", "STEP 11 · TAGS (STAGE E)",
                "How each question is built, what it asks for, and what thinking it needs.",
                "Stage E is NOT BUILT yet. This tab lists what will appear here, so the gap is "
                "visible rather than silently absent.")
    planned = [
        ("E1 question_type", "How the question is BUILT", "assertion_reason, match_the_lists, statement_i_ii, ... (18 values)"),
        ("E2 format", "What the student must PICK", "pick_correct, pick_incorrect, calculate_value, ... (25 values)"),
        ("E3 content_shape", "What NCERT material it is built on", "one_line, formula, reaction_mechanism, ... (29 values)"),
        ("E4 thinking", "What the student must do IN THEIR HEAD", "8 draft categories; needs the owner's codebook to be reliable"),
        ("E5 trap", "Why each WRONG option attracts", "19 values, judged per wrong option (3 per question)"),
        ("E6 descriptive", "Answer form, negation, item count, figure role", "filled by script, not judgement"),
    ]
    rows = [{"tag": a, "answers the question": b, "values": c, "state": "NOT BUILT"}
            for a, b, c in planned]
    ws.cell(row=5, column=1,
            value="Stage E is not built. The taxonomy behind it HAS been validated against 10 "
                  "real papers, but no scripts or agents exist yet, and the owner's codebooks "
                  "(which E4 needs to be trustworthy) are not written.").fill = AMBER
    ws.cell(row=5, column=1).font = F_BOLD
    _write(ws, 7, ["tag", "answers the question", "values", "state"], rows,
           fills=lambda r: {"state": GREY},
           widths={"tag": 20, "answers the question": 46, "values": 72, "state": 12})


def tab_subtopics(wb):
    ws = _sheet(wb, "step04 subtopics", "STEP 04 · SUBTOPICS + LINKS (A4-A5)",
                "Each chapter split into subtopics, with textbook passages linked to them.",
                "AMBER = a subtopic with ZERO linked passages. This is a real defect: a question "
                "routed to it has no evidence available and will block in Stage D.")
    links = collections.Counter()
    ldir = rc.pp("ncert", "links")
    if os.path.isdir(ldir):
        for fn in sorted(os.listdir(ldir)):
            if fn.endswith(".jsonl"):
                for l in _read_jsonl(os.path.join(ldir, fn)):
                    links[l.get("subtopic_id")] += 1
    rows = []
    sdir = rc.pp("ncert", "subtopics")
    if os.path.isdir(sdir):
        for fn in sorted(os.listdir(sdir)):
            if not fn.endswith(".json"):
                continue
            data = _read_json(os.path.join(sdir, fn)) or {}
            for st in data.get("subtopics") or []:
                sid = st.get("subtopic_id")
                n = links.get(sid, 0)
                rows.append({"subtopic": _flat(sid), "chapter": _flat(data.get("chapter_id")),
                             "name": _flat(st.get("name")),
                             "from heading": _flat(st.get("from_heading")),
                             "passages linked": n,
                             "concern": "" if n else "NO passages linked — a question sent here will block"})
    bad = sum(1 for r in rows if not r["passages linked"])
    ws.cell(row=5, column=1,
            value=f"Subtopics: {len(rows)}   With no linked passage: {bad}").font = F_BOLD
    _write(ws, 7, ["subtopic", "chapter", "name", "from heading", "passages linked", "concern"],
           rows,
           fills=lambda r: {"passages linked": GREEN if r["passages linked"] else AMBER,
                            "concern": GREEN if not r["concern"] else AMBER},
           widths={"subtopic": 20, "chapter": 14, "name": 48, "from heading": 13,
                   "passages linked": 15, "concern": 56})


def tab_questions(wb, flags_by_item):
    ws = _sheet(wb, "step07 questions", "STEP 07 · THE QUESTION BANK (B1-B8)",
                "Every question extracted from the papers, with its official answer.",
                "'blind check' is the key column: an independent solver answered WITHOUT seeing "
                "the key. GREEN = it agreed. AMBER = it disagreed or could not run (e.g. the "
                "question needs a figure we do not have).")
    rows = []
    rdir = rc.pp("papers", "records")
    for fn in sorted(os.listdir(rdir)) if os.path.isdir(rdir) else []:
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _read_json(os.path.join(rdir, fn)) or {}
        if rec.get("merged_into"):
            continue
        opts = rec.get("options_en") or {}
        ans = rec.get("official_answer")
        b6 = rec.get("b6_answer")
        agree = rec.get("b6_agrees_with_key")
        if b6 is None:
            blind = "not run"
        elif agree:
            blind = "AGREES"
        else:
            blind = "DISAGREES"
        codes = [f["code"] for f in flags_by_item.get(rec.get("question_id"), [])
                 if f.get("status") == "open"]
        rows.append({
            "question": _flat(rec.get("question_id")),
            "year": _flat(rec.get("year")),
            "codes": _flat(rec.get("paper_codes")),
            "subject": _flat(rec.get("subject")) or "(not tagged)",
            "needs figure": "YES" if rec.get("has_figure") else "",
            "question text": _flat(rec.get("stem_en"), 220),
            "official answer": f"{_flat(ans)}  {_flat(opts.get(str(ans)), 50)}" if ans else "(dropped / none)",
            "blind check": blind,
            "open flags": _flat(codes),
        })
    agreed = sum(1 for r in rows if r["blind check"] == "AGREES")
    ws.cell(row=5, column=1,
            value=f"Questions in bank: {len(rows)}   Blind-solver agreed with the official key: "
                  f"{agreed}   Disagreed: {sum(1 for r in rows if r['blind check'] == 'DISAGREES')}"
                  f"   Could not run: {sum(1 for r in rows if r['blind check'] == 'not run')}").font = F_BOLD
    def fill(r):
        f = {}
        f["blind check"] = {"AGREES": GREEN, "DISAGREES": RED}.get(r["blind check"], AMBER)
        f["needs figure"] = AMBER if r["needs figure"] else GREEN
        f["subject"] = AMBER if r["subject"] == "(not tagged)" else GREEN
        f["open flags"] = AMBER if r["open flags"] else GREEN
        return f
    _write(ws, 7, ["question", "year", "codes", "subject", "needs figure", "question text",
                   "official answer", "blind check", "open flags"], rows, fills=fill,
           widths={"question": 12, "year": 7, "codes": 16, "subject": 13, "needs figure": 12,
                   "question text": 70, "official answer": 30, "blind check": 13,
                   "open flags": 30})


def tab_duplicates(wb):
    ws = _sheet(wb, "step09 duplicates", "STEP 09 · DUPLICATES MERGED (C1)",
                "The same question printed in different booklet codes, merged into one record.",
                "Each row is a merge the pipeline actually performed. Nothing is deleted — the "
                "absorbed record is kept and points at the one it was merged into.")
    rows = []
    rdir = rc.pp("papers", "records")
    for fn in sorted(os.listdir(rdir)) if os.path.isdir(rdir) else []:
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _read_json(os.path.join(rdir, fn)) or {}
        if not rec.get("merged_from"):
            continue
        rows.append({"kept as": _flat(rec.get("question_id")),
                     "absorbed": _flat(rec.get("merged_from")),
                     "now covers codes": _flat(rec.get("paper_codes")),
                     "question text": _flat(rec.get("stem_en"), 180),
                     "state": "merged — verified identical"})
    ws.cell(row=5, column=1, value=f"Merges performed: {len(rows)}").font = F_BOLD
    _write(ws, 7, ["kept as", "absorbed", "now covers codes", "question text", "state"], rows,
           fills=lambda r: {"state": GREEN},
           widths={"kept as": 12, "absorbed": 14, "now covers codes": 20, "question text": 80,
                   "state": 26})


def tab_mapping(wb):
    ws = _sheet(wb, "step10 mapping", "STEP 10 · MAPPED TO NCERT (D1-D4)",
                "Each question tied to its NCERT chapter, subtopic and the exact proving line.",
                "RED = blocked, almost always because the question's real chapter is not indexed "
                "yet. AMBER = the pipeline guessed with low confidence and said so.")
    rows = []
    rdir = rc.pp("papers", "records")
    for fn in sorted(os.listdir(rdir)) if os.path.isdir(rdir) else []:
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        rec = _read_json(os.path.join(rdir, fn)) or {}
        if rec.get("merged_into"):
            continue
        qid = rec.get("question_id")
        d1 = rc.read_item_status("D1", qid) or {}
        d3 = rc.read_item_status("D3", qid) or {}
        st = d1.get("status") or "not reached"
        rows.append({
            "question": _flat(qid),
            "subject": _flat(rec.get("subject")) or "(none)",
            "chapter chosen": _flat(rec.get("d1_chapter_ids")) or "—",
            "subtopic chosen": _flat(rec.get("d2_subtopic_ids")) or "—",
            "confidence": _flat(rec.get("d1_confidence")) or "—",
            "D1 state": st,
            "D3 passages": d3.get("status") or "not reached",
            "concern": _flat(d1.get("check_message"), 150),
        })
    ws.cell(row=5, column=1,
            value=f"Questions reaching Stage D: {len(rows)}   "
                  f"Blocked: {sum(1 for r in rows if r['D1 state'] == 'blocked')}").font = F_BOLD
    _write(ws, 7, ["question", "subject", "chapter chosen", "subtopic chosen", "confidence",
                   "D1 state", "D3 passages", "concern"], rows,
           fills=lambda r: {"D1 state": STATUS_FILL.get(r["D1 state"], GREY),
                            "D3 passages": STATUS_FILL.get(r["D3 passages"], GREY),
                            "confidence": AMBER if r["confidence"] in ("low", "—") else GREEN,
                            "concern": AMBER if r["concern"] else GREEN},
           widths={"question": 12, "subject": 12, "chapter chosen": 18, "subtopic chosen": 20,
                   "confidence": 11, "D1 state": 12, "D3 passages": 13, "concern": 60})


def tab_flags(wb, flags):
    ws = _sheet(wb, "step12 flags", "STEP 12 · THE WORK LIST (every problem)",
                "Every point where the pipeline was unsure, or found something wrong.",
                "Worst first. RED must be resolved before the affected item can proceed; AMBER "
                "wants a human eye but does not stop the pipeline.")
    order = {"blocker": 0, "high": 1, "normal": 2, "low": 3}
    rows = []
    for f in sorted(flags, key=lambda x: (order.get(x.get("severity"), 9), x.get("step") or "")):
        rows.append({"severity": _flat(f.get("severity")), "step": _flat(f.get("step")),
                     "code": _flat(f.get("code")), "item": _flat(f.get("item_id")),
                     "what it means": _flat(f.get("message"), 400),
                     "status": _flat(f.get("status"))})
    c = collections.Counter(r["severity"] for r in rows)
    ws.cell(row=5, column=1,
            value="   ".join(f"{k}={c.get(k,0)}" for k in ("blocker", "high", "normal", "low"))
            ).font = F_BOLD
    _write(ws, 7, ["severity", "step", "code", "item", "what it means", "status"], rows,
           fills=lambda r: {"severity": SEV_FILL.get(r["severity"], GREY),
                            "code": SEV_FILL.get(r["severity"], GREY)},
           widths={"severity": 11, "step": 7, "code": 28, "item": 26, "what it means": 95,
                   "status": 10})


_MILESTONES = [
    ("1. Category check sheet (E0)",
     "~300 questions sampled, categories grouped, sent to the owner to approve",
     "NOT STARTED", "E0 is not built, and it needs ~300 questions; the bank has {nq}."),
    ("2a. Stage A — all NCERT indexed",
     "Every chapter of every book indexed; D1 needs the full chapter list",
     "{a_pct}% ", "{nch} chapters indexed of roughly 37 needed."),
    ("2b. Stage A — change log",
     "Old vs new edition compared, changes judged and logged",
     "NOT RUN", "A6/A7/A9 tested on fixtures only; A8 (the judge) has never run on real data."),
    ("2c. Stage B — all papers extracted",
     "Every in-scope paper read into question records",
     "{b_pct}%", "{nq} questions extracted; a single year holds roughly 1,800."),
    ("3a. Faculty agreement test (150)",
     "50 questions per subject shown to faculty WITHOUT the pipeline's tags; target >=85% agreement",
     "BLOCKED", "Needs Stage E (tagging), which is not built."),
    ("3b. Gold set (90)",
     "30 per subject, every field confirmed by a reviewer, used to score every step",
     "BLOCKED", "Needs a reviewed pilot to sample from."),
    ("4. Pilot — 3 chapters through A-F",
     "One chapter per subject taken end to end, then scored and fixed",
     "NOT STARTED", "Stages E and F do not exist. Note the spec's pilot chapters are not the "
                    "ones currently indexed — a choice is needed."),
    ("5. Full run",
     "All papers, all chapters, then release chapter by chapter",
     "NOT STARTED", "Last milestone; follows the pilot meeting its targets."),
]


def tab_progress(wb, nq, nch):
    ws = _sheet(wb, "step13 progress", "STEP 13 · MILESTONE STATUS",
                "Where the project stands against the five agreed milestones.",
                "Percentages are counted from real files, not estimated. GREY = not started.")
    a_pct = int(round(nch / 37 * 100)) if nch else 0
    b_pct = round(nq / 1800 * 100, 1)
    rows = []
    for name, what, state, why in _MILESTONES:
        rows.append({"milestone": name, "what it means": what,
                     "status": state.format(a_pct=a_pct, b_pct=b_pct),
                     "why / what is needed": why.format(nq=nq, nch=nch)})
    _write(ws, 7, ["milestone", "what it means", "status", "why / what is needed"], rows,
           fills=lambda r: {"status": GREY if "NOT" in r["status"] or "BLOCKED" in r["status"] else AMBER},
           widths={"milestone": 32, "what it means": 62, "status": 14,
                   "why / what is needed": 72})


# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the colour-coded pipeline review workbook.")
    ap.add_argument("--out")
    args = ap.parse_args(argv)

    out = args.out or rc.pp("exports", datetime.date.today().isoformat(), "pipeline_review.xlsx")
    lib_io.ensure_parent(out)

    flags = _read_jsonl(rc.pp("flags", "flags.jsonl"))
    by_item = collections.defaultdict(list)
    for f in flags:
        by_item[f.get("item_id")].append(f)

    rdir = rc.pp("papers", "records")
    recs = [_read_json(os.path.join(rdir, fn)) for fn in os.listdir(rdir)
            if fn.startswith("Q-") and fn.endswith(".json")] if os.path.isdir(rdir) else []
    canonical = [r for r in recs if r and not r.get("merged_into")]
    nch = 0
    cdir = rc.pp("ncert", "chapters")
    if os.path.isdir(cdir):
        for fn in os.listdir(cdir):
            if fn.endswith(".json"):
                d = _read_json(os.path.join(cdir, fn))
                nch += len(d) if isinstance(d, list) else 1

    sev = collections.Counter(f.get("severity") for f in flags)
    stats = {
        "Questions in the bank": len(canonical),
        "NCERT chapters indexed": nch,
        "Open flags": len(flags),
        "  of which blockers": sev.get("blocker", 0),
        "  of which need a look": sev.get("high", 0) + sev.get("normal", 0),
    }

    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    tab_start(wb, stats)
    tab_s0(wb)            # step00
    tab_books(wb)         # step01
    tab_ncert(wb)         # step02
    tab_passages(wb)      # step03
    tab_subtopics(wb)     # step04
    tab_changes(wb)       # step05
    tab_papers(wb)        # step06
    tab_questions(wb, by_item)  # step07
    tab_blind(wb)         # step08
    tab_duplicates(wb)    # step09
    tab_mapping(wb)       # step10
    tab_tags(wb)          # step11
    tab_flags(wb, flags)  # step12
    tab_progress(wb, len(canonical), nch)  # step13
    wb.save(out)

    print(f"Workbook written to {out}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
