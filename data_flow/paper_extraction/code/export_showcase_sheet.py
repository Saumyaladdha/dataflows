#!/usr/bin/env python3
"""Picks the smallest showcase set of questions that covers every discovery category, and exports it.

    python3 scripts/export_showcase_sheet.py --max 55

Writes `exports/discovery/QUESTIONS_SHOWCASE.xlsx`: one row per chosen question with its value and
reason on all five axes, plus a Coverage tab proving which categories the set reaches.

Why a solver and not a sample. The five axes hold 85 categories between them (E1 18, E2 16, E3 18,
E4 13, E5 20). Picking 55 questions at random covers the common ones several times over and misses
the rare ones entirely -- and the rare ones are the point of a showcase. So this runs a greedy set
cover: repeatedly take the question that adds the most not-yet-covered categories. Ties are broken
toward questions that already have `why` text written, then toward the subject seen least so far,
so the sheet reads as a balanced sample rather than a pile of whichever subject sorts first.

Categories with no question in the corpus cannot be covered by any selection; they are reported
separately rather than counted as a failure. Measured when this was written, four are empty by
construction -- `new_type`, `new_format`, `new_trap` are placeholders for values a future pass may
need, and `old_ncert_fact` has no instances because the NCERT change log is still empty.
"""

import argparse
import collections
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import question_assets as qa  # noqa: E402

AXES = [
    ("E1", "question_type", "How is the question BUILT?"),
    ("E2", "format", "What must the student PICK?"),
    ("E3", "content_shape", "What NCERT MATERIAL is it built on?"),
    ("E4", "thinking", "What must the student do IN THEIR HEAD?"),
    ("E5", "trap", "Why does each WRONG OPTION attract?"),
]

# One tint per axis so the five blocks read apart at a glance.
AXIS_TINT = {"E1": "E8EDF9", "E2": "E6F2EA", "E3": "FFF3E0", "E4": "F1E9F8", "E5": "FDE9EA"}
AXIS_HEAD = {"E1": "1F3864", "E2": "1E5631", "E3": "8A5200", "E4": "4B2E73", "E5": "962A33"}

_ALT = PatternFill("solid", fgColor="FAFBFD")
_GAP = PatternFill("solid", fgColor="FFF6E5")
_THIN = Side(style="thin", color="D5DBE5")
_BORDER = Border(left=_THIN, right=_THIN, top=_THIN, bottom=_THIN)


def load_axes(final_dir):
    """question -> {axis: [values]}, axis -> {category: n}, axis -> {category: definition}."""
    tags = collections.defaultdict(lambda: collections.defaultdict(list))
    whys = collections.defaultdict(dict)
    sizes, defs = {}, {}
    for axis, tag, _ in AXES:
        with open(os.path.join(final_dir, f"{tag}.json"), encoding="utf-8") as fh:
            doc = json.load(fh)
        sizes[axis], defs[axis] = {}, {}
        for cat in doc.get("categories") or []:
            if not isinstance(cat, dict):
                continue
            name = cat.get("name")
            ids = cat.get("question_ids") or []
            sizes[axis][name] = len(ids)
            defs[axis][name] = (cat.get("definition") or "").strip()
            for qid in ids:
                tags[qid][axis].append(name)
            for ex in (cat.get("examples") or []):
                if isinstance(ex, dict) and ex.get("question_id") and ex.get("why"):
                    whys[ex["question_id"]].setdefault(axis, ex["why"])
    return tags, whys, sizes, defs


def meaning_text(axis, values, defs):
    """The definition of each value the question carries, so a reader meeting `pick_ratio` for the
    first time learns what it is without leaving the row. Multi-valued cells get one line each,
    named, because E5 can legitimately carry six traps."""
    out = []
    for v in values:
        d = defs.get(axis, {}).get(v, "")
        out.append(f"{v}: {d}" if len(values) > 1 else d)
    return "\n\n".join(x for x in out if x.strip())


def load_records():
    out = {}
    d = rc.pp("papers", "records")
    for fn in sorted(os.listdir(d)):
        if fn.startswith("Q-") and fn.endswith(".json"):
            try:
                with open(os.path.join(d, fn), encoding="utf-8") as fh:
                    rec = json.load(fh)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(rec, dict) and rec.get("question_id"):
                out[rec["question_id"]] = rec
    return out


def select(tags, whys, universe, records, limit):
    """Greedy set cover, then fill remaining slots with the best-documented leftovers."""
    covered, chosen = set(), []
    subj = collections.Counter()
    pool = set(tags)

    def pairs(qid):
        return {(a, v) for a, vs in tags[qid].items() for v in vs}

    while pool and len(chosen) < limit and covered < universe:
        best, best_key = None, None
        for qid in pool:
            gain = len(pairs(qid) - covered)
            if gain == 0:
                continue
            s = (records.get(qid, {}) or {}).get("subject", "")
            key = (gain, len(whys.get(qid, {})), -subj[s], qid)
            if best_key is None or key > best_key:
                best, best_key = qid, key
        if best is None:
            break
        chosen.append(best)
        covered |= pairs(best)
        subj[(records.get(best, {}) or {}).get("subject", "")] += 1
        pool.discard(best)

    # Any slots left over go to the most fully documented questions, keeping subjects even.
    while pool and len(chosen) < limit:
        best, best_key = None, None
        for qid in pool:
            s = (records.get(qid, {}) or {}).get("subject", "")
            key = (len(whys.get(qid, {})), len(tags[qid]), -subj[s], qid)
            if best_key is None or key > best_key:
                best, best_key = qid, key
        chosen.append(best)
        subj[(records.get(best, {}) or {}).get("subject", "")] += 1
        pool.discard(best)
    return chosen, covered


def question_text(rec):
    parts = [(rec.get("stem_en") or "").strip()]
    for field, label in (("statements", ""), ("list_i", "List I"), ("list_ii", "List II")):
        entries = [e for e in (rec.get(field) or []) if isinstance(e, dict)]
        if entries:
            if label:
                parts.append(f"{label}:")
            parts.extend(f"({e.get('label')}) {e.get('text')}" for e in entries)
    return "\n".join(p for p in parts if p)


def options_text(rec):
    """House style: each option on its own line, the official answer ticked."""
    opts = {k: (v or "").strip() for k, v in sorted((rec.get("options_en") or {}).items())}
    ans = str(rec.get("official_answer") or "")
    return "\n".join(f"{k}) {v}" + ("  ✔" if k == ans else "")
                     for k, v in opts.items() if v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=55)
    ap.add_argument("--final-dir", default=rc.pp("exports", "discovery", "final"))
    ap.add_argument("--out", default=rc.pp("exports", "discovery", "QUESTIONS_SHOWCASE.xlsx"))
    args = ap.parse_args()

    tags, whys, sizes, defs = load_axes(args.final_dir)
    records = load_records()

    universe = {(a, c) for a, cats in sizes.items() for c, n in cats.items() if n}
    empty = sorted((a, c) for a, cats in sizes.items() for c, n in cats.items() if not n)
    chosen, covered = select(tags, whys, universe, records, args.max)

    wb = Workbook()
    wb.remove(wb.active)

    # ------------------------------------------------------------------ Read me
    ws = wb.create_sheet("Read me")
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 104
    pct = 100.0 * len(covered) / len(universe) if universe else 0.0
    info = [
        ("Question showcase", ""),
        ("", ""),
        ("What this is", f"{len(chosen)} questions chosen out of 580 so that between them they "
                         f"cover as many of the discovery categories as possible. Every question "
                         f"carries its value and the reason for it on all five axes."),
        ("Categories covered", f"{len(covered)} of {len(universe)} reachable  ({pct:.0f}%)"),
        ("Questions shown", len(chosen)),
        ("", ""),
        ("The five axes", "Each question is described five different ways. They are not competing "
                          "labels; all five apply to the same question at once."),
    ]
    for axis, tag, question in AXES:
        got = len({c for a, c in covered if a == axis})
        tot = len([c for c, n in sizes[axis].items() if n])
        info.append((f"{axis}  {tag}", f"{question}    —    {got} of {tot} categories shown"))
    info += [
        ("", ""),
        ("How these were picked", "A greedy set cover, not a sample: repeatedly take the question "
                                  "that adds the most categories not yet covered. Ties go to "
                                  "questions that already have written reasons, then to the "
                                  "subject seen least, so the set stays balanced. A random 55 "
                                  "would repeat the common categories and miss the rare ones, "
                                  "which are the whole point of a showcase."),
        ("Multi-valued cells", "E1 and E5 can hold more than one value, joined by ';'. E1 because "
                               "some questions are built two ways at once (a plain MCQ that is "
                               "also a figure to read); E5 because that axis runs once per WRONG "
                               "OPTION, so one question can carry several traps."),
        ("Three columns per axis", "'value' is the category name. 'what it means' is that "
                                   "category's definition, so a reader meeting pick_ratio or "
                                   "ignores_exception for the first time learns what it is without "
                                   "leaving the row — it is filled for every cell. 'why this "
                                   "question' is the reason THIS question sits in that category."),
        ("Empty 'why this question'", "Tinted. Those per-question reasons come from each "
                                      "category's worked examples, so only some questions have "
                                      "one. The 'what it means' column beside it is never empty, "
                                      "so no cell leaves a category unexplained."),
        ("Figure file", "papers/figures/<QID>.png — recovered by step B9 where the question's own "
                        "source dropped its diagram. Tinted 'NEEDED' means it declares a figure "
                        "that has not been recovered; blank means none is needed. The figure's "
                        "own (1)(2)(3)(4) labels belong to ITS source paper, possibly a different "
                        "booklet code, so they are not this question's option numbers."),
        ("Blank E5", "Not always a gap. That axis is per wrong option, and 126 of the 580 "
                     "questions genuinely carry no trap worth naming."),
    ]
    if empty:
        info.append(("Unreachable categories",
                     f"{len(empty)} categories have no question in the corpus, so no selection can "
                     f"reach them: " + ", ".join(f"{a} {c}" for a, c in empty) +
                     ". The three 'new_*' values are placeholders for a future pass; "
                     "old_ncert_fact has no instances while the NCERT change log is empty."))
    for label, value in info:
        ws.append([label, value])
    ws["A1"].font = Font(bold=True, size=16, color="1F3864")
    for r in range(3, len(info) + 2):
        ws.cell(row=r, column=1).font = Font(bold=True, size=10)
        ws.cell(row=r, column=1).alignment = Alignment(vertical="top", wrap_text=True)
        ws.cell(row=r, column=2).alignment = Alignment(vertical="top", wrap_text=True)

    # ---------------------------------------------------------------- Questions
    # The asset columns matter: every question has a crop at papers/questions/<paper>/<n>.png, and
    # B9 recovers a figure at papers/figures/<QID>.png for questions whose own source dropped it.
    # Without them a row shows "[missing content - no text printed]" while the picture sits on disk.
    cols = [("#", 5, False), ("question_id", 14, False), ("subject", 11, False),
            ("year", 7, False), ("question", 54, True), ("options", 32, True)]
    cols += qa.ASSET_COLUMNS
    for axis, _, _ in AXES:
        cols.append((f"{axis} value", 21, True))
        cols.append((f"{axis} what it means", 50, True))
        cols.append((f"{axis} why this question", 42, True))

    qs = wb.create_sheet("Questions")
    qs.append([c[0] for c in cols])
    for i, (_, width, _) in enumerate(cols, 1):
        qs.column_dimensions[get_column_letter(i)].width = width
    for i, (head, _, _) in enumerate(cols, 1):
        cell = qs.cell(row=1, column=i)
        axis = head.split()[0] if head.split()[0] in AXIS_HEAD else None
        cell.fill = PatternFill("solid", fgColor=AXIS_HEAD.get(axis, "1F3864"))
        cell.font = Font(color="FFFFFF", bold=True, size=11)
        cell.alignment = Alignment(vertical="center", wrap_text=True, horizontal="left")
        cell.border = _BORDER
    qs.row_dimensions[1].height = 30

    for n, qid in enumerate(chosen, start=2):
        rec = records.get(qid, {}) or {}
        row = [n - 1, qid, rec.get("subject", ""), rec.get("year", ""),
               qa.question_text(rec), qa.options_text(rec),
               *qa.asset_values(rec)]
        for axis, _, _ in AXES:
            values = tags[qid].get(axis, [])
            row.append(";".join(values))
            row.append(meaning_text(axis, values, defs))
            row.append(whys.get(qid, {}).get(axis, ""))
        qs.append(row)
        for i, (head, _, wrap) in enumerate(cols, 1):
            cell = qs.cell(row=n, column=i)
            cell.alignment = Alignment(vertical="top", wrap_text=wrap)
            cell.border = _BORDER
            axis = head.split()[0] if head.split()[0] in AXIS_TINT else None
            if head == "figure file" and str(cell.value or "").startswith("NEEDED"):
                cell.fill = _GAP
            elif head.endswith("why this question") and not cell.value:
                cell.fill = _GAP
            elif axis:
                cell.fill = PatternFill("solid", fgColor=AXIS_TINT[axis])
            elif n % 2 == 0:
                cell.fill = _ALT
    qs.freeze_panes = "E2"
    qs.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(chosen) + 1}"

    # ----------------------------------------------------------------- Coverage
    cv = wb.create_sheet("Coverage")
    cv.append(["axis", "axis question", "category", "what it means", "questions in corpus",
               "shown in this sheet", "which of the 55"])
    for i, w in enumerate((7, 34, 28, 66, 16, 15, 34), 1):
        cv.column_dimensions[get_column_letter(i)].width = w
    for cell in cv[1]:
        cell.fill = PatternFill("solid", fgColor="1F3864")
        cell.font = Font(color="FFFFFF", bold=True, size=11)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = _BORDER
    chosen_set = set(chosen)
    r = 1
    for axis, tag, question in AXES:
        for cat, n in sorted(sizes[axis].items(), key=lambda kv: -kv[1]):
            who = [q for q in chosen if cat in tags[q].get(axis, [])]
            r += 1
            cv.append([axis, question, cat, defs[axis].get(cat, ""), n, len(who),
                       ", ".join(who[:4])])
            for i in range(1, 8):
                c = cv.cell(row=r, column=i)
                c.border = _BORDER
                c.alignment = Alignment(vertical="top", wrap_text=i in (2, 4, 7))
                if not n:
                    c.fill = PatternFill("solid", fgColor="EFEFEF")
                elif not who:
                    c.fill = _GAP
                else:
                    c.fill = PatternFill("solid", fgColor=AXIS_TINT[axis])
    cv.freeze_panes = "C2"
    cv.auto_filter.ref = f"A1:G{r}"

    wb.save(args.out)
    print(f"wrote {os.path.relpath(args.out, rc.pp())}")
    print(f"  questions   : {len(chosen)}")
    print(f"  coverage    : {len(covered)} of {len(universe)} reachable categories ({pct:.0f}%)")
    for axis, _, _ in AXES:
        got = len({c for a, c in covered if a == axis})
        tot = len([c for c, n in sizes[axis].items() if n])
        print(f"    {axis}: {got}/{tot}")
    miss = sorted(universe - covered)
    if miss:
        print(f"  NOT covered ({len(miss)}): {', '.join(f'{a} {c}' for a, c in miss)}")
    if empty:
        print(f"  unreachable (no question exists): "
              f"{', '.join(f'{a} {c}' for a, c in empty)}")
    subj = collections.Counter((records.get(q, {}) or {}).get("subject", "?") for q in chosen)
    print(f"  subjects    : {dict(subj)}")
    whyn = sum(len(whys.get(q, {})) for q in chosen)
    print(f"  why cells   : {whyn} of {len(chosen) * 5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
