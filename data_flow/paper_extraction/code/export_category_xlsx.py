#!/usr/bin/env python3
"""Exports the question-category sheets as one .xlsx workbook.

    python3 scripts/export_category_xlsx.py        # -> docs/question_categories/question_traps.xlsx

Reads the CSVs that build_category_sheet.py writes. Two tabs:

  * **Questions** -- one row per question: id, category, the question text, its options, then the
    four handling steps as E1..E4.
  * **Categories** -- one row per category: the content shape, the trap mechanism, how to spot it,
    its four steps as E1..E4, and how many questions in the corpus fall in it.

Nothing is computed here beyond column widths; the numbers come from the CSVs and meta.json.
"""

import argparse
import csv
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

DEFECT_CATS = {"C14", "C15"}  # source defects, not exam traps -- tinted differently

_HEAD_FILL = PatternFill("solid", fgColor="1F3864")
_HEAD_FONT = Font(color="FFFFFF", bold=True, size=11)
_DEFECT_FILL = PatternFill("solid", fgColor="FCE8EA")
_ALT_FILL = PatternFill("solid", fgColor="F4F6FA")
_THIN = Side(style="thin", color="D5DBE5")
_BORDER = Border(left=_THIN, right=_THIN, top=_THIN, bottom=_THIN)

# (header, csv field, width, wrap)
Q_COLS = [
    ("Question ID", "question_id", 26, False),
    ("Category", "cat_id", 10, False),
    ("Category name", "category_name", 26, True),
    ("Question", "question_text", 70, True),
    ("Options", "options", 55, True),
    ("E1", "step_1", 34, True),
    ("E2", "step_2", 34, True),
    ("E3", "step_3", 34, True),
    ("E4", "step_4", 34, True),
    ("Structure", "structure", 16, False),
    ("Negative words", "negative_words", 15, False),
    ("Has figure", "has_figure", 11, False),
]

C_COLS = [
    ("Category", "cat_id", 10, False),
    ("Category name", "category_name", 28, True),
    ("Question type", "question_type", 17, False),
    ("Content shape", "content_shape", 44, True),
    ("Trap mechanism", "trap_mechanism", 62, True),
    ("How to spot it", "how_to_spot", 36, True),
    ("E1", "step_1", 34, True),
    ("E2", "step_2", 34, True),
    ("E3", "step_3", 34, True),
    ("E4", "step_4", 34, True),
    ("Count in corpus", "count_in_corpus", 13, False),
]


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _sheet(wb, title, cols, rows, numeric_fields=()):
    ws = wb.create_sheet(title)
    ws.append([c[0] for c in cols])
    for i, (_, _, width, _) in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = width
    for cell in ws[1]:
        cell.fill = _HEAD_FILL
        cell.font = _HEAD_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = _BORDER
    ws.row_dimensions[1].height = 30

    for n, row in enumerate(rows, start=2):
        values = []
        for _, field, _, _ in cols:
            v = row.get(field, "")
            if field in numeric_fields:
                try:
                    v = int(v)
                except (TypeError, ValueError):
                    pass
            values.append(v)
        ws.append(values)
        defect = row.get("cat_id") in DEFECT_CATS
        for i, (_, _, _, wrap) in enumerate(cols, 1):
            cell = ws.cell(row=n, column=i)
            cell.alignment = Alignment(vertical="top", wrap_text=wrap)
            cell.border = _BORDER
            if defect:
                cell.fill = _DEFECT_FILL
            elif n % 2 == 0:
                cell.fill = _ALT_FILL

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(rows) + 1}"
    return ws


def _readme(wb, meta, n_cats, n_qs):
    ws = wb.create_sheet("Read me", 0)
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 108
    lines = [
        ("Question traps workbook", ""),
        ("", ""),
        ("Questions classified", meta["questions_classified"]),
        ("Categories", n_cats),
        ("Worked examples", n_qs),
        ("", ""),
        ("E1 - E4", "The four handling steps for that question's category: what to do first, "
                    "second, third, fourth. They come from the category, so every question in a "
                    "category shares them."),
        ("Questions tab", "One row per example question: the real question id, the text as "
                          "transcribed from the source image, its options, then E1-E4."),
        ("Categories tab", "One row per category: the content shape the question needs, the trap "
                           "mechanism, how to spot it, and its E1-E4."),
        ("", ""),
        ("Pink rows", "Categories C14 and C15 are NOT exam traps. They are defects in our source "
                      "material: C14's options contain a genuine duplicate, so no single answer "
                      "exists as printed; C15's options are pictures the scrape never captured. "
                      "A trap is solved; a defect has to be re-acquired from an official PDF."),
        ("Why counts exceed the total", "A question can belong to several categories (a figure "
                                        "question with numeric options is both C11 and C03), so the "
                                        "category counts sum to more than the question total."),
        ("Question text", "For match and assertion-reason shapes the stem alone is boilerplate, so "
                          "the lists and statements are included in the Question column - that is "
                          "where the discriminating content lives."),
        ("Nothing reconstructed", "Question text is as transcribed. Where the source is defective "
                                  "the defect is recorded rather than repaired."),
    ]
    for label, value in lines:
        ws.append([label, value])
    ws["A1"].font = Font(bold=True, size=15, color="1F3864")
    for r in range(3, len(lines) + 2):
        ws.cell(row=r, column=1).font = Font(bold=True, size=10)
        ws.cell(row=r, column=1).alignment = Alignment(vertical="top")
        ws.cell(row=r, column=2).alignment = Alignment(vertical="top", wrap_text=True)
    return ws


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=rc.pp("docs", "question_categories"))
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cats = _read(os.path.join(args.dir, "categories.csv"))
    qs = _read(os.path.join(args.dir, "questions.csv"))
    with open(os.path.join(args.dir, "meta.json"), encoding="utf-8") as fh:
        meta = json.load(fh)

    wb = Workbook()
    wb.remove(wb.active)
    _readme(wb, meta, len(cats), len(qs))
    _sheet(wb, "Questions", Q_COLS, qs)
    _sheet(wb, "Categories", C_COLS, cats, numeric_fields={"count_in_corpus"})

    out = args.out or os.path.join(args.dir, "question_traps.xlsx")
    wb.save(out)
    print(f"wrote {os.path.relpath(out, rc.pp())}")
    print(f"  Read me / Questions ({len(qs)} rows) / Categories ({len(cats)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
