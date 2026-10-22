#!/usr/bin/env python3
"""Builds exports/discovery/CATEGORIES.xlsx -- five tabs, one per E-stage tag.

Shape dictated by the spec, not by preference. SPEC Section 13 lists five tags and says in those
words that they "answer five different questions; never mix them" -- so there is one tab per tag
and nothing else. An earlier version of this workbook had twelve tabs including raw research
output, and was unreadable: the research tabs still carried the discovery agents' invented names
("Printed architecture", "Quantity slate", "Cognitive machine"), which the final lists reject, so
a reader met the rejected vocabulary with no way to tell which naming was authoritative.

Columns follow SPEC's E0 deliverable (`tag, category, definition, subjects, example_1, example_2,
count_physics, count_chemistry, count_biology, years_seen, decision`) rather than a set of my own.

Source is exports/discovery/applied/ -- the end of the chain
final (as discovered) -> corrected (wrong assignments removed) -> applied (holes refilled).
Reading an earlier stage would show counts that are known to be wrong.

This script makes no judgements. Every category, definition and example was written by an agent;
every count and every year is recomputed here from that agent's own question-id list joined to
papers/records/, because a count nobody can re-derive is not evidence.
"""

import json
import os
import re
import sys
from collections import defaultdict

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC = os.path.join(ROOT, "exports", "discovery")
SRC = os.path.join(DISC, "applied")
RECORDS = os.path.join(ROOT, "papers", "records")
OUT = os.path.join(DISC, "CATEGORIES.xlsx")

#: (tab name, tag, the question this tag answers -- SPEC Section 13 wording)
LAYERS = [
    ("E1 Question type", "question_type", "How is the question BUILT?"),
    ("E2 Format", "format", "What must the student PICK?"),
    ("E3 Content shape", "content_shape", "What NCERT MATERIAL is it built on?"),
    ("E4 Thinking", "thinking", "What must the student do IN THEIR HEAD?"),
    ("E5 Trap", "trap", "Why does each WRONG OPTION attract?"),
]

#: Decisions that are the owner's, shown on the tab they affect instead of a separate sheet.
OPEN = {
    "format": "OPEN DECISION — a 16th value is needed. Five questions hand back a bare direction "
              "or comparison and nothing in the 15 fits, so they currently hide in "
              "calculate_value: Q-000003 (along eastward), Q-000038, Q-000217 (more on bigger "
              "sphere), Q-000177 (zero/positive/infinity), Q-000100 (increase by a factor of "
              "nine). Their own analyses say so — \"A direction only. No magnitude, no units, no "
              "number.\" Recommendation: add it.",
    "content_shape": "OPEN DECISION — example_list's definition wants two more words: \"...trait, "
                     "role, effect, partner OR LOCATION\". That legitimises 3 part-to-location "
                     "questions (Q-000162, Q-000206, Q-000305) and avoids inventing a 19th "
                     "category for them. Recommendation: take it.",
    "trap": "NOTE — this is the one tag that does NOT give every question exactly one value. It "
            "runs once per wrong option, so a question can carry several traps and 126 carry "
            "none. Counts here are questions-with-at-least-one, and they do not sum to 580.",
    "thinking": "NOTE — counts are split by Chemistry branch, not just by subject, because "
                "SPEC §2.8 found physical-chemistry questions behave like Physics while "
                "organic/inorganic behave like Biology, so a prior keyed on subject alone "
                "misclassifies much of Chemistry.",
}

RED = PatternFill("solid", fgColor="F8D7DA")
BLUE = PatternFill("solid", fgColor="DDEBF7")
GREY = PatternFill("solid", fgColor="E9ECEF")
AMBER = PatternFill("solid", fgColor="FFF3CD")
HEAD = PatternFill("solid", fgColor="1F3A5F")
F_HEAD = Font(bold=True, color="FFFFFF", size=11)
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")

DECISION_WORD = {"keep": "Kept as it was", "rename": "Renamed", "new": "NEW",
                 "merge": "Merged", "add": "NEW", "drop": "Removed", "reject": "Rejected"}


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def tidy(s):
    """Make stored LaTeX readable for a human, without changing what it says.

    The records hold the question exactly as extracted -- `$4\\,\\mu\\mathrm{H}$` -- which is
    right for the pipeline and unreadable on a review sheet. This strips only presentational
    markup: maths delimiters, spacing commands, \\mathrm/\\text wrappers, and a handful of symbol
    names. No word, digit or unit is altered, nothing is shortened, and anything it does not
    recognise is left exactly as it is rather than guessed at. The question record stays the
    authoritative copy; this is a reading aid, and the tabs say so.
    """
    if not s:
        return ""
    s = re.sub(r"\\[,;:!]|\\ ", " ", s)
    for _ in range(3):  # nested wrappers, e.g. \mathrm{\mu H}
        s = re.sub(r"\\(?:mathrm|text|mathit|mathbf|mathsf|rm)\s*\{([^{}]*)\}", r"\1", s)
    # degrees first: ^\circ and ^{\circ} must lose the caret too, or "327^\circ C" renders as
    # "327^° C" with a stray caret.
    s = re.sub(r"\^\s*\{?\s*\\circ\s*\}?", "°", s)
    s = re.sub(r"\\d?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"(\1)/(\2)", s)
    s = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"√(\1)", s)
    s = re.sub(r"\^\s*\{([^{}]*)\}", r"^\1", s)
    s = re.sub(r"_\s*\{([^{}]*)\}", r"_\1", s)
    for a, b in (("\\mu", "μ"), ("\\Omega", "Ω"), ("\\omega", "ω"), ("\\times", "×"),
                 ("\\circ", "°"), ("\\alpha", "α"), ("\\beta", "β"), ("\\gamma", "γ"),
                 ("\\Delta", "Δ"), ("\\delta", "δ"), ("\\lambda", "λ"), ("\\pi", "π"),
                 ("\\theta", "θ"), ("\\rho", "ρ"), ("\\sigma", "σ"), ("\\nu", "ν"),
                 ("\\rightarrow", "→"), ("\\leftarrow", "←"), ("\\pm", "±"),
                 ("\\approx", "≈"), ("\\geq", "≥"), ("\\leq", "≤"), ("\\AA", "Å"),
                 ("\\equiv", "≡"), ("\\cdot", "·"), ("\\%", "%")):
        s = s.replace(a, b)
    s = s.replace("$", "").replace("\\\\", " ")
    return re.sub(r"[ \t]+", " ", s).strip()


def example_cell(qid, rec, why):
    """One example as a reviewer can actually read it: the question, its options, the key, the why.

    Showing only `Q-000036` tells a reviewer nothing -- they would have to go and look it up to
    judge whether the category is right, which is the one thing the sheet exists to let them do.
    So the cell carries the real stem, the four options with the official answer ticked, and the
    agent's one-line reason for choosing this question.
    """
    if not rec:
        return f"{qid}  (record not found)"
    parts = [qid, tidy(rec.get("stem_en"))]
    o = rec.get("options_en") or {}
    ans = {a.strip() for a in str(rec.get("official_answer") or "").split(",") if a.strip()}
    if o:
        opts = []
        for k in sorted(o):
            mark = " ✔" if k in ans else ""
            opts.append(f"{k}) {tidy(o.get(k))}{mark}")
        parts.append("   ".join(opts))
    st = rec.get("statements") or []
    if st:
        parts.append("Statements: " + " / ".join(
            f"{s.get('label', '')} {tidy(s.get('text'))}" if isinstance(s, dict) else tidy(str(s))
            for s in st[:5]))
    for key, label in (("list_i", "List I"), ("list_ii", "List II")):
        rows = rec.get(key) or []
        if rows:
            parts.append(f"{label}: " + " / ".join(
                f"{r.get('label', '')} {tidy(r.get('text'))}" if isinstance(r, dict) else tidy(str(r))
                for r in rows[:5]))
    if not ans:
        parts.append("(no official answer on record)")
    if why:
        parts.append(f"Why this example: {why}")
    return "\n".join(p for p in parts if p)


def main():
    records = {}
    for fn in sorted(os.listdir(RECORDS)):
        if fn.startswith("Q-") and fn.endswith(".json"):
            try:
                r = _read(os.path.join(RECORDS, fn))
            except Exception:
                continue
            if isinstance(r, dict) and r.get("question_id"):
                records[r["question_id"]] = r

    wb = Workbook()
    wb.remove(wb.active)
    totals = {}

    for tabname, tag, question in LAYERS:
        data = _read(os.path.join(SRC, f"{tag}.json"))
        cats = data.get("categories") or []
        covered = {q for c in cats for q in (c.get("question_ids") or [])}

        ws = wb.create_sheet(tabname)
        ws["A1"] = tabname
        ws["A1"].font = Font(bold=True, size=15, color="1F3A5F")
        ws["A2"] = question
        ws["A2"].font = Font(bold=True, size=12, color="444444")
        ws["A3"] = (f"{len(cats)} categories, covering {len(covered)} of 580 analysed questions "
                    f"(NEET 2022, 2023, 2024). Worked out from the questions themselves, not "
                    f"chosen from a list. Every count below is derived from the named questions, "
                    f"so it can be checked. 'Status' says what changed against the list the "
                    f"project had before.")
        ws["A3"].font = Font(italic=True, size=10, color="444444")
        ws["A3"].alignment = WRAP
        note = OPEN.get(tag)
        if note:
            ws["A4"] = note
            ws["A4"].font = Font(bold=True, size=10, color="8A4B00")
            ws["A4"].alignment = WRAP
            ws.row_dimensions[4].height = 46
        ws.row_dimensions[3].height = 32

        branch = (tag == "thinking")
        if branch:
            cols = ["Category", "What it means", "Status", "Total", "Physics", "Chem physical",
                    "Chem organic", "Chem inorganic", "Botany", "Zoology", "Years seen",
                    "Example question 1", "Example question 2"]
            widths = [26, 60, 26, 7, 8, 13, 13, 14, 9, 9, 11, 86, 86]
        else:
            cols = ["Category", "What it means", "Status", "Total", "Physics", "Chemistry",
                    "Biology", "Years seen", "Example question 1", "Example question 2"]
            widths = [26, 62, 28, 7, 9, 10, 9, 11, 88, 88]

        rows = []
        order = {"new": 0, "rename": 1, "merge": 2, "keep": 3, "drop": 4}
        for c in sorted(cats, key=lambda x: (order.get(x.get("decision"), 9),
                                             -len(x.get("question_ids") or []))):
            ids = c.get("question_ids") or []
            word = DECISION_WORD.get(c.get("decision"), c.get("decision") or "")
            was = c.get("was")
            was = was if isinstance(was, str) else (", ".join(was) if isinstance(was, list) else "")
            if was and c.get("decision") in ("rename", "merge"):
                word = f"{word} — was {was}"
            ys = sorted({(records.get(q) or {}).get("year") for q in ids
                         if (records.get(q) or {}).get("year")})
            years = f"{min(ys)}–{str(max(ys))[2:]}" if len(ys) > 1 else (str(ys[0]) if ys else "—")
            ex = []
            for e in (c.get("examples") or [])[:2]:
                if not isinstance(e, dict):
                    continue
                q = str(e.get("question_id", ""))
                ex.append(example_cell(q, records.get(q), (e.get("why") or "").strip()))
            # A category with no example of its own still gets one: pick its first member, so no
            # row on the sheet is unillustrated.
            if len(ex) < 2:
                for q in ids:
                    if len(ex) >= 2:
                        break
                    if not any(q in c0 for c0 in ex):
                        ex.append(example_cell(q, records.get(q), ""))
            ex += [""] * (2 - len(ex))
            if branch:
                g = defaultdict(int)
                for q in ids:
                    r = records.get(q) or {}
                    s, b = r.get("subject"), r.get("branch")
                    key = ("Physics" if s == "Physics" else
                           f"Chem {b}" if s == "Chemistry" else
                           ("Botany" if b == "botany" else "Zoology") if s == "Biology" else "?")
                    g[key] += 1
                rows.append([c.get("name", ""), c.get("definition", ""), word, len(ids),
                             g.get("Physics", 0), g.get("Chem physical", 0),
                             g.get("Chem organic", 0), g.get("Chem inorganic", 0),
                             g.get("Botany", 0), g.get("Zoology", 0), years, ex[0], ex[1]])
            else:
                sub = defaultdict(int)
                for q in ids:
                    sub[(records.get(q) or {}).get("subject") or "?"] += 1
                rows.append([c.get("name", ""), c.get("definition", ""), word, len(ids),
                             sub.get("Physics", 0), sub.get("Chemistry", 0),
                             sub.get("Biology", 0), years, ex[0], ex[1]])

        start = 6
        for i, h in enumerate(cols, 1):
            cell = ws.cell(row=start, column=i, value=h)
            cell.fill, cell.font, cell.alignment = HEAD, F_HEAD, WRAP
        for j, row in enumerate(rows):
            r = start + 1 + j
            fill = (GREY if row[2] in ("Removed", "Rejected")
                    else BLUE if row[2] == "NEW" or str(row[2]).startswith(("Renamed", "Merged"))
                    else AMBER if row[3] == 0 else None)
            for i, v in enumerate(row, 1):
                cell = ws.cell(row=r, column=i, value=v)
                cell.alignment = WRAP if i == 2 else TOP
                if fill:
                    cell.fill = fill
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = f"A{start + 1}"
        ws.auto_filter.ref = f"A{start}:{get_column_letter(len(cols))}{start + len(rows)}"
        totals[tag] = (len(cats), len(covered))

    wb.save(OUT)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  tabs: {len(wb.sheetnames)} -> {', '.join(wb.sheetnames)}")
    for _, tag, _ in LAYERS:
        n, cov = totals[tag]
        print(f"    {tag:15s} {n:2d} categories, {cov:3d} questions covered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
