#!/usr/bin/env python3
"""One tab per step, showing the REAL data: what each item was given, and what came back.

    python3 scripts/build_step_data_workbook.py        # -> exports/<today>/step_data.xlsx
    python3 scripts/build_step_data_workbook.py --max-rows 40

The other three workbooks describe the pipeline. This one shows the actual values:

  pipeline_review.xlsx  -> what needs attention
  final_data.xlsx       -> what we have produced
  data_steps.xlsx       -> what each step does, one line each
  step_data.xlsx        -> THIS: per step, per item, the real input and the real output

It reads what is genuinely on disk -- `steps/<STEP>/work/<item>.<run>.input.json` is literally
the file handed to the worker, and `steps/<STEP>/out/<item>.<run>.json` is literally what came
back -- so nothing here is reconstructed or paraphrased. If a value looks wrong in this workbook,
it is wrong in the pipeline.

Two source tabs are included as well, because "what was given" for the whole project starts
outside the pipeline: the legacy sheets (which hold the figures and LaTeX) and the owner's
year->sitting index.

Long values are truncated for readability; the `given (full)`/`extracted (full)` character counts
tell you when that has happened so a truncated cell is never mistaken for a short value.

NOT A RELEASE -- same caveat as every other export: spec 14/F5 reserves released data for
`export_tables.py` -> `data/` after sign-off, which has not happened.
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

CAP = 1200  # per-cell character cap; Excel's own limit is 32767 but long cells are unreadable


def _read_json(p):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _read_jsonl(p):
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


def _pretty(obj):
    """Render a work/out JSON as readable 'key: value' lines rather than raw JSON."""
    if obj is None:
        return "", 0
    if not isinstance(obj, dict):
        s = str(obj)
        return s[:CAP], len(s)
    parts = []
    for k, v in obj.items():
        if isinstance(v, (dict, list)):
            v = json.dumps(v, ensure_ascii=False)
        v = str(v)
        if len(v) > 300:
            v = v[:300] + f" …(+{len(v)-300} chars)"
        parts.append(f"{k}: {v}")
    s = "\n".join(parts)
    return s[:CAP], len(s)


def _sheet(wb, title, heading, what):
    ws = wb.create_sheet(title[:31])
    ws["A1"] = heading
    ws["A1"].font = F_TITLE
    ws["A2"] = what
    ws["A2"].font = F_NOTE
    ws["A3"] = ("Left = exactly what the worker was handed.  Right = exactly what it returned.  "
                "Nothing here is paraphrased.  A GREY 'QUEUED' row means the work was prepared but "
                "no agent has been asked to do it yet - that is a backlog, not a failure.")
    ws["A3"].font = F_NOTE
    ws.freeze_panes = "A6"
    return ws


def _write(ws, start, cols, rows, fills=None, widths=None):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=start, column=i, value=c)
        cell.fill, cell.font, cell.border = HEAD, F_HEAD, BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[start].height = 28
    r = start + 1
    for item in rows:
        rf = fills(item) if fills else {}
        for i, c in enumerate(cols, 1):
            cell = ws.cell(row=r, column=i, value=item.get(c, ""))
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if c in rf:
                cell.fill = rf[c]
        ws.row_dimensions[r].height = 92
        r += 1
    for i, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(c, 18)


_RUN_RE = re.compile(r"^(?P<item>.+)\.(?P<run>runA|runB|retry1|adjudicated)\.(input\.)?json$")

# step -> (tab title, one-line description of the exchange)
_STEP_DESC = {
    "S0":  ("step00 S0 intake",      "GIVEN the source folder -> EXTRACTED the input list and missing-input flags"),
    "A1":  ("step01 A1 books",       "GIVEN a book's cover page -> EXTRACTED its exact edition, copied verbatim"),
    "A2":  ("step02 A2 pages",       "GIVEN one page image -> EXTRACTED ordered text blocks copied word for word"),
    "A2S": ("step02b A2S special",   "GIVEN blocks too complex for text -> EXTRACTED preserved tables/figures/equations"),
    "A3":  ("step03 A3 passages",    "GIVEN a chapter's block stream -> EXTRACTED one-idea passages"),
    "A4":  ("step04 A4 subtopics",   "GIVEN headings + passages (twice) -> EXTRACTED the subtopic list"),
    "A5":  ("step05 A5 links",       "GIVEN a passage + the subtopic list -> EXTRACTED which subtopic it belongs to"),
    "A6":  ("step06 A6 pair",        "GIVEN old and new passages -> EXTRACTED which pair with which"),
    "A7":  ("step07 A7 diff",        "GIVEN paired passages -> EXTRACTED the word-level differences"),
    "A8":  ("step08 A8 judge",       "GIVEN a difference -> EXTRACTED whether it is a real fact change or rewording"),
    "A9":  ("step09 A9 changelog",   "GIVEN the judged changes -> EXTRACTED the change log"),
    "B1":  ("step10 B1 papers",      "GIVEN a paper cover + key -> EXTRACTED year, sitting, code, trust"),
    "B2":  ("step11 B2 boundaries",  "GIVEN a paper page -> EXTRACTED where each question starts and ends"),
    "B3":  ("step12 B3 read",        "GIVEN one question's image -> EXTRACTED stem, options, statements"),
    "B4":  ("step13 B4 reread",      "GIVEN the same question again -> EXTRACTED an independent second reading"),
    "B5":  ("step14 B5 key",         "GIVEN the official key page -> EXTRACTED the official answer per question"),
    "B6":  ("step15 B6 blind solve", "GIVEN the question ONLY (never the key) -> EXTRACTED an independent answer"),
    "B7":  ("step16 B7 subject",     "GIVEN the question text -> EXTRACTED subject and chemistry branch"),
    "B8":  ("step17 B8 faulty",      "GIVEN a dropped/bonus question -> EXTRACTED what was wrong and a fix"),
    "B9":  ("step18 B9 figures",     "GIVEN candidate figures -> EXTRACTED which one belongs to the question"),
    "C1":  ("step19 C1 duplicates",  "GIVEN the same question in two codes -> EXTRACTED whether they are identical"),
    "D1":  ("step20 D1 chapter",     "GIVEN the question + chapter list -> EXTRACTED which NCERT chapter"),
    "D2":  ("step21 D2 subtopic",    "GIVEN the question + subtopic list -> EXTRACTED which subtopic"),
    "D3":  ("step22 D3 passages",    "GIVEN the chosen subtopics -> EXTRACTED candidate evidence passages"),
    "D4":  ("step23 D4 evidence",    "GIVEN question + passages -> EXTRACTED the exact proving NCERT line"),
}


def _step_rows(step, max_rows):
    """Pair every work-input file with its output file for one step."""
    wdir, odir = rc.pp("steps", step, "work"), rc.pp("steps", step, "out")
    given = {}
    if os.path.isdir(wdir):
        for fn in os.listdir(wdir):
            m = _RUN_RE.match(fn)
            if m and fn.endswith(".input.json"):
                given[(m.group("item"), m.group("run"))] = os.path.join(wdir, fn)
    got = {}
    if os.path.isdir(odir):
        for fn in os.listdir(odir):
            m = _RUN_RE.match(fn)
            if m and not fn.endswith(".input.json"):
                got[(m.group("item"), m.group("run"))] = os.path.join(odir, fn)

    keys = sorted(set(given) | set(got))
    rows = []
    for item, run in keys[:max_rows]:
        gtext, glen = _pretty(_read_json(given[(item, run)])) if (item, run) in given else ("(no input file)", 0)
        if (item, run) in got:
            otext, olen = _pretty(_read_json(got[(item, run)]))
        else:
            # Staged but not answered. `--list` writes a work-input file (and renders its page
            # image) for EVERY candidate, whether or not anyone dispatches it -- so an unanswered
            # row means "queued, nobody has started it", NOT "an agent was asked and failed".
            # Corpus-wide this is the normal majority state: 2,501 of 2,924 staged A2 inputs were
            # never dispatched. Saying "not answered yet" read as failure, which it is not.
            otext, olen = ("QUEUED - no agent has been asked to do this one yet "
                           "(staging a work file is not the same as dispatching it)", 0)
        st = rc.read_item_status(step, item) or {}
        rows.append({"item": item, "run": run,
                     "GIVEN (what the worker received)": gtext,
                     "EXTRACTED (what it returned)": otext,
                     "given chars": glen, "extracted chars": olen,
                     "status": st.get("status") or "",
                     "note / why": (st.get("check_message") or "")[:300]})
    return rows, len(keys)


def tab_index(wb, present):
    ws = wb.create_sheet("START HERE")
    ws["A1"] = "Real data, step by step"
    ws["A1"].font = Font(bold=True, size=16, color="1F3A5F")
    ws["A2"] = ("Each tab shows, for one step: the exact file the worker was given, and the exact "
                "file it returned. Read straight off disk — nothing is paraphrased.")
    ws["A2"].font = F_NOTE
    ws["A4"] = "TABS"
    ws["A4"].font = F_BOLD
    r = 5
    for title, desc, n in present:
        ws.cell(row=r, column=1, value=title).font = F_BOLD
        ws.cell(row=r, column=2, value=desc)
        ws.cell(row=r, column=3, value=f"{n} items")
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="SOURCE TABS").font = F_BOLD
    r += 1
    for t, d in [("src legacy sheets", "The 22 spreadsheets — where the figures and LaTeX live"),
                 ("src paper index", "The owner's year → sitting → file index")]:
        ws.cell(row=r, column=1, value=t).font = F_BOLD
        ws.cell(row=r, column=2, value=d)
        r += 1
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 86
    ws.column_dimensions["C"].width = 12


def tab_legacy(wb, max_rows):
    ws = _sheet(wb, "src legacy sheets", "SOURCE · THE 22 LEGACY SPREADSHEETS",
                "Not pipeline output — this is raw source material. It holds the figure images "
                "(as Mathpix URLs) and LaTeX that the scraped papers lost.")
    ws["A3"] = ("Only the figure and LaTeX are usable. The chapter/topic columns are coaching "
                "judgements known to be wrong for many 2018-19 questions and must never reach "
                "the mapping steps.")
    ws["A3"].font = F_NOTE
    rows = []
    d = rc.pp("inputs", "legacy_sheets")
    try:
        import openpyxl as _o
    except ImportError:
        return
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not fn.endswith(".xlsx"):
            continue
        try:
            swb = _o.load_workbook(os.path.join(d, fn), data_only=True, read_only=True)
        except Exception:
            continue
        sws = swb[swb.sheetnames[0]]
        hdr = [c.value for c in next(sws.iter_rows(min_row=1, max_row=1))]
        try:
            qi = hdr.index("Question")
        except ValueError:
            swb.close()
            continue
        n = nfig = nltx = 0
        first = ""
        for row in sws.iter_rows(min_row=2, values_only=True):
            if not row or not row[qi]:
                continue
            n += 1
            t = str(row[qi])
            if "cdn.mathpix.com" in t:
                nfig += 1
            if "$" in t or "\\frac" in t:
                nltx += 1
            if not first:
                first = t[:400]
        rows.append({"sheet": fn, "questions": n, "with a figure URL": nfig,
                     "with LaTeX": nltx, "columns": ", ".join(str(h) for h in hdr if h),
                     "first question (real)": first})
        swb.close()
    _write(ws, 6, ["sheet", "questions", "with a figure URL", "with LaTeX", "columns",
                   "first question (real)"], rows,
           fills=lambda r: {"with a figure URL": GREEN if r["with a figure URL"] else GREY},
           widths={"sheet": 38, "questions": 11, "with a figure URL": 15, "with LaTeX": 11,
                   "columns": 52, "first question (real)": 90})


def tab_index_src(wb):
    ws = _sheet(wb, "src paper index", "SOURCE · THE OWNER'S PAPER INDEX",
                "The hand-maintained map of year -> sitting -> file. Ground truth for which "
                "paper belongs to which sitting.")
    try:
        import sitting_index
        data = sitting_index.parse()
    except Exception as e:
        ws.cell(row=6, column=1, value=f"could not parse: {e}").fill = AMBER
        return
    rows = []
    for year in sorted(data):
        for e in data[year]:
            rows.append({"year": year, "sitting": e.get("sitting"),
                         "pdf named": e.get("pdf") or "-",
                         "pdf on disk": "yes" if e.get("pdf_present") else "NO",
                         "xlsx named": e.get("xlsx") or "-",
                         "xlsx on disk": "yes" if e.get("xlsx_present") else "NO"})
    _write(ws, 6, ["year", "sitting", "pdf named", "pdf on disk", "xlsx named", "xlsx on disk"],
           rows,
           fills=lambda r: {"pdf on disk": GREEN if r["pdf on disk"] == "yes" else RED,
                            "xlsx on disk": GREEN if r["xlsx on disk"] == "yes" else RED},
           widths={"year": 7, "sitting": 10, "pdf named": 46, "pdf on disk": 12,
                   "xlsx named": 40, "xlsx on disk": 12})


def main(argv=None):
    ap = argparse.ArgumentParser(description="Per-step real given/extracted data workbook.")
    ap.add_argument("--max-rows", type=int, default=25,
                    help="Max items shown per step tab (default 25).")
    ap.add_argument("--out")
    args = ap.parse_args(argv)

    out = args.out or rc.pp("exports", datetime.date.today().isoformat(), "step_data.xlsx")
    lib_io.ensure_parent(out)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    placeholder = wb.create_sheet("_tmp")

    present = []
    for step in sorted(_STEP_DESC, key=lambda s: _STEP_DESC[s][0]):
        title, desc = _STEP_DESC[step]
        rows, total = _step_rows(step, args.max_rows)
        if not rows:
            continue
        ws = _sheet(wb, title, f"{step} — {desc}",
                    f"{total} items processed so far"
                    + (f"; showing the first {len(rows)}" if total > len(rows) else ""))
        _write(ws, 6, ["item", "run", "GIVEN (what the worker received)",
                       "EXTRACTED (what it returned)", "given chars", "extracted chars",
                       "status", "note / why"], rows,
               fills=lambda r: {"status": {"pass": GREEN, "flagged": AMBER,
                                           "blocked": RED}.get(r["status"], GREY),
                                "EXTRACTED (what it returned)":
                                    GREY if r["EXTRACTED (what it returned)"].startswith("QUEUED") else GREEN},
               widths={"item": 22, "run": 8, "GIVEN (what the worker received)": 62,
                       "EXTRACTED (what it returned)": 72, "given chars": 9,
                       "extracted chars": 10, "status": 10, "note / why": 44})
        present.append((title, desc, total))

    tab_legacy(wb, args.max_rows)
    tab_index_src(wb)
    tab_index(wb, present)
    wb.move_sheet("START HERE", offset=-len(wb.sheetnames) + 1)
    wb.remove(placeholder)
    wb.save(out)

    print(f"step_data.xlsx -> {out}")
    for t, d, n in present:
        print(f"   {t:<26} {n:>5} items")
    print("   + src legacy sheets, src paper index")
    return 0


if __name__ == "__main__":
    sys.exit(main())
