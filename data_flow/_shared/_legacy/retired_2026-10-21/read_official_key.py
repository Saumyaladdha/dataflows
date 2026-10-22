#!/usr/bin/env python3
"""Read an official NTA answer-key PDF into {question number: answer}, per booklet code.

    python3 scripts/read_official_key.py --probe
    python3 scripts/read_official_key.py --year 2015 --apply

WHY THE OFFICIAL KEY IS A THIRD SOURCE, NOT A CONFIRMATION
----------------------------------------------------------
Three different things can tell us the answer to a question, and they are not the same thing:

  booklet   the `Solution: (3)` the publisher printed beside the question. It is the publisher's
            reading of the paper, not NTA's, and publishers get questions wrong.
  official  NTA's own final key, published per booklet code. The authority -- but it is matched in
            from a separate file, and a wrong join is silent.
  solved    `b6-blind-solver` answering the question without seeing either. Catches the cases where
            the other two agree and are both wrong, and catches a bad join.

Keeping them in three columns rather than collapsing them is the point: agreement is evidence, and a
disagreement is a question worth a human's time. The first corpus had only the booklet's answer and
could not tell a publisher's error from a scrape error.

BOOKLET CODES MATTER. NEET prints the same 200 questions in ~24 codes with the options rotated, so an
answer is only meaningful against the code it was printed for (SPEC Rule 16). A key read for code AA
must never be applied to code BB.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

KEY_ROOT = os.path.expanduser("~/Downloads/Saumya_NEET_work/Old/NEET_PYQ/NEET_official_Answer_key")
SETS_ROOT = os.path.expanduser("~/Downloads/Saumya_NEET_work/Old/all_neet_sets_and_ans_key")
OUT = ("papers_v2", "official_keys")

#: The two layouts these keys use. A key is a grid, and the grid is either "Q. No. / Answer" column
#: pairs or a flat run of `12. (3)` pairs. Both are matched; neither is assumed.
PAIR = re.compile(r"\b(\d{1,3})\s*[.)]?\s*[-:]?\s*\(?([1-4])\)?(?!\d)")
CODE_IN_NAME = re.compile(r"[-_]([A-Z]{2}|[A-Z]\d|\d{2})(?:\.pdf|$)", re.I)
#: Each code's section heading inside a multi-code key: `BOOK : M1`, `BOOKLET CODE : AA`.
BOOK_HEADING = re.compile(r"BOOK(?:LET)?\s*(?:CODE)?\s*[:\-]\s*([A-Z]{1,2}\d?|\d{2})\b", re.I)


def read_key(path):
    """{booklet code: {qno: answer}} from one key PDF.

    ONE FILE HOLDS MANY CODES. NEET publishes its final key as a run of sections, each headed
    `BOOK : M1`, and each section is a complete 200-question key for THAT code only. Parsing the
    file as one grid takes whichever answer appears first and silently applies one code's key to
    every code -- which is the exact failure SPEC Rule 16 is about, since the codes differ precisely
    in the order their options are printed. Measured: a flat parse of the 2021 key reported 3,478
    conflicting pairs, one for nearly every question that differs between its four codes.

    So the text is split on the `BOOK :` headings first, and each section is parsed alone. A file
    with no heading is one key, and its code comes from the filename.
    """
    import pymupdf
    doc = pymupdf.open(path)
    text = "\n".join(page.get_text("text") for page in doc)
    doc.close()

    sections = []
    marks = list(BOOK_HEADING.finditer(text))
    if marks:
        for index, mark in enumerate(marks):
            end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
            sections.append((mark.group(1).upper(), text[mark.end():end]))
    else:
        code = CODE_IN_NAME.search(os.path.basename(path))
        sections.append((code.group(1).upper() if code else None, text))

    out = {}
    for code, chunk in sections:
        answers, conflicts = {}, 0
        for number, answer in PAIR.findall(chunk):
            n = int(number)
            if not 1 <= n <= 200:
                continue
            if n in answers and answers[n] != answer:
                conflicts += 1
                continue
            answers.setdefault(n, answer)
        if answers:
            out[code] = {"answers": answers, "conflicts": conflicts}
    return out


def probe():
    import pymupdf
    rows = []
    for path in sorted(glob.glob(os.path.join(KEY_ROOT, "*.pdf"))):
        name = os.path.basename(path)
        year = re.search(r"(20\d\d)", name)
        for code, data in sorted(read_key(path).items()):
            rows.append((year.group(1) if year else "?", code or "-",
                         len(data["answers"]), data["conflicts"], name))
    print("%-6s %-5s %7s %10s  %s" % ("year", "code", "answers", "conflicts", "file"))
    for row in sorted(rows):
        print("%-6s %-5s %7d %10d  %s" % row)
    print("\n%d key file(s). A usable key covers 150+ questions; fewer means the grid did not parse."
          % len(rows))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--year", nargs="*")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.probe:
        return probe()
    if not args.apply:
        ap.error("pass --probe or --apply")

    out_dir = rc.pp(*OUT)
    os.makedirs(out_dir, exist_ok=True)
    written = 0
    for path in sorted(glob.glob(os.path.join(KEY_ROOT, "*.pdf"))):
        name = os.path.basename(path)
        year = re.search(r"(20\d\d)", name)
        if not year or (args.year and year.group(1) not in args.year):
            continue
        for code, data in sorted(read_key(path).items()):
            answers, conflicts = data["answers"], data["conflicts"]
            if len(answers) < 150:
                print("skip %-40s code %-4s only %d answers parsed"
                      % (name[:40], code or "?", len(answers)))
                continue
            record = {
                "year": int(year.group(1)),
                "booklet_code": code,
                "source_pdf": os.path.relpath(path, os.path.dirname(KEY_ROOT)),
                "answers": {str(k): v for k, v in sorted(answers.items())},
                "parsed": len(answers),
                "conflicting_pairs_ignored": conflicts,
            }
            stem = "%s_%s" % (record["year"], code or "ALL")
            with open(os.path.join(out_dir, "%s.json" % stem), "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=1)
            print("wrote %-20s %3d answers  (code %s, %d pairs ignored)"
                  % (stem + ".json", len(answers), code or "unknown", conflicts))
            written += 1
    print("\n%d official key(s) written to papers_v2/official_keys/" % written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
