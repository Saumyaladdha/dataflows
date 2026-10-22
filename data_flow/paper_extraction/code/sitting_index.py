#!/usr/bin/env python3
"""Parse the owner's year -> sitting -> file index into a machine-readable map.

    python3 scripts/sitting_index.py            # print the map and which files are missing
    python3 scripts/sitting_index.py --json     # emit JSON for another script to consume

SOURCE: `inputs/_reference/paper_index_2010_2026.csv`, supplied by the owner 2026-10-12 and
copied verbatim from `~/Downloads/NEET PYQ 2010-2026 - Sheet1.csv`. It is a hand-maintained
spreadsheet, not a generated file: a loose grid with merged-looking blank cells, a three-column
header (NEET / PRELIMINARY / AIIMS) and, per year, one row naming the PDFs and the next naming
the matching XLSX. This module turns that human layout into a clean mapping.

WHY IT MATTERS: before this, `scripts/intake_check.py` could not tell which sitting several paper
files belonged to and flagged them "sitting could not be confirmed from the filename alone". The
index states it outright, so for the files it covers this replaces inference with a stated fact.

WHAT IT DELIBERATELY DOES NOT DO -- the important part
------------------------------------------------------
It does NOT define which sittings EXIST. The index records what the owner HOLDS, and those are
different things. `scripts/lib/sittings.py` requires 2019 -> [MAIN, REEXAM], 2020 -> [MAIN,
REEXAM] and 2024 -> [MAIN, RETEST], and on the real history that is correct: NEET 2019 had an
Odisha re-exam after Cyclone Fani, 2020 had an October re-exam for containment-zone candidates,
and 2024 had a 23 June re-test for 1,563 candidates in the grace-marks case. The index simply
lists one paper for each of those years because the re-exam papers were never collected.

So this module reports those as MISSING inputs, never as non-existent sittings, and nothing here
may be used to relax `sittings.py`. Treating an absence of evidence as evidence of absence is
exactly the failure this comment exists to prevent.

It also covers only the 15 year-wise `NEET_PYQ/Paper/` files and the 22 sheets. The 166 scraped
per-booklet-code files are not in the index at all and still need text-matching to place.
"""
import argparse
import csv
import json
import os
import re
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402

INDEX_REL = ("inputs", "_reference", "paper_index_2010_2026.csv")

# The sheet's two right-hand columns are headed PRELIMINARY and AIIMS. For 2010-2012 those really
# are the two AIPMT sittings. For later years the same columns are reused for whatever that year's
# two sittings were (2016 Phase I/II; 2026 main/re-NEET), and for single-sitting years only one
# column is filled. So position alone cannot name the sitting -- the filename has to be read too.
_PHASE_RE = re.compile(r"phase\s*(i{1,2}|1|2)", re.IGNORECASE)
_RE_NEET_RE = re.compile(r"re-?neet|re-?exam|re-?test|retest", re.IGNORECASE)
_PRE_RE = re.compile(r"\bpre(liminary)?\b", re.IGNORECASE)
_MAIN_RE = re.compile(r"\bmain(s)?\b", re.IGNORECASE)


def _sitting_for(filename, column_hint, n_sittings_this_year, year=None):
    """Name the sitting from the filename, falling back to the column it sat under.

    `n_sittings_this_year` matters and is not cosmetic: a year with only ONE paper has only one
    sitting, which `scripts/lib/sittings.py` calls MAIN -- even though that lone file sits in the
    spreadsheet's left-hand (PRELIMINARY) column purely by position. Without this, every
    single-sitting year 2017-2025 came out labelled PRELIM and would not have matched the
    pipeline's own required-sitting names. Only 2010-2012, which genuinely ran a Preliminary and
    a Main, should ever yield PRELIM."""
    m = _PHASE_RE.search(filename)
    if m:
        tok = m.group(1).lower()
        return "MAIN" if tok in ("i", "1") else "PH2"
    if _RE_NEET_RE.search(filename):
        return "REEXAM"
    # 2026's first sitting was CANCELLED, and `scripts/lib/sittings.py` requires
    # 2026 -> [CANCELLED, REEXAM]. The index calls it a normal exam, so naming it MAIN here
    # produced a sitting the pipeline never expects and left 2026 CANCELLED looking unmatched
    # in intake. A cancelled sitting is never scored and so has no official key, which
    # `SITTINGS_WITHOUT_KEY_REQUIREMENT` already accounts for -- mislabelling it MAIN would
    # silently reintroduce a key requirement that cannot be met.
    if year == 2026 and n_sittings_this_year > 1 and not _RE_NEET_RE.search(filename):
        return "CANCELLED"
    if _PRE_RE.search(filename):
        return "PRELIM"
    if _MAIN_RE.search(filename):
        return "MAIN"
    if n_sittings_this_year <= 1:
        return "MAIN"
    if column_hint == "PRELIMINARY" and year is not None and year <= 2012:
        # Preliminary/Main is an AIPMT-era structure only. After 2012 the same spreadsheet column
        # is reused for whatever that year's first sitting was, so reading it as "Preliminary"
        # would invent a sitting that never happened.
        return "PRELIM"
    return "MAIN"


_YEAR_RE = re.compile(r"neet\s*(\d{4})", re.IGNORECASE)


def parse(path=None):
    """-> {year:int -> [ {sitting, pdf, xlsx, pdf_present, xlsx_present}, ... ]}"""
    path = path or rc.pp(*INDEX_REL)
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))

    out = {}
    current_year = None
    for row in rows:
        cells = [c.strip() for c in row]
        nonempty = [c for c in cells if c]
        if not nonempty:
            continue

        m = _YEAR_RE.search(nonempty[0])
        if m:
            # A year row: the year label, then this year's PDFs in the later columns.
            current_year = int(m.group(1))
            pdfs = [c for c in nonempty[1:] if c.lower().endswith(".pdf")]
            out[current_year] = [{"pdf": p, "xlsx": None} for p in pdfs]
            continue

        if current_year is None:
            continue
        xlsxs = [c for c in nonempty if c.lower().endswith(".xlsx")]
        if xlsxs:
            # The row after a year row carries that year's sheets, in the same column order.
            entries = out.setdefault(current_year, [])
            for i, x in enumerate(xlsxs):
                if i < len(entries):
                    entries[i]["xlsx"] = x
                else:
                    entries.append({"pdf": None, "xlsx": x})

    # Name each sitting and check what is actually on disk.
    hints = ["PRELIMINARY", "AIIMS"]
    for year, entries in out.items():
        for i, e in enumerate(entries):
            name = e["pdf"] or e["xlsx"] or ""
            e["sitting"] = _sitting_for(name, hints[i] if i < len(hints) else "",
                                         len(entries), year)
            e["pdf_present"] = _exists(e["pdf"]) if e["pdf"] else None
            e["xlsx_present"] = _exists(e["xlsx"]) if e["xlsx"] else None
    return out


_SEARCH_ROOTS = [
    os.path.expanduser("~/Downloads/Saumya_NEET_work"),
]


def _exists(filename):
    """The index names bare filenames; find them anywhere under the real source tree."""
    for root in _SEARCH_ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirnames, files in os.walk(root):
            if filename in files:
                return True
    # also accept a copy already inside the project
    for sub in ("inputs/papers", "inputs/legacy_sheets"):
        if os.path.exists(rc.pp(*sub.split("/"), filename)):
            return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="Parse the owner's paper index (spec-external input).")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    data = parse()
    if args.json:
        print(json.dumps({str(k): v for k, v in sorted(data.items())}, indent=2))
        return 0

    missing_pdf, missing_xlsx = [], []
    print(f"{'year':<6}{'sitting':<9}{'pdf':<52}{'pdf?':<10}{'xlsx?'}")
    for year in sorted(data):
        for e in data[year]:
            pp = "present" if e["pdf_present"] else ("MISSING" if e["pdf"] else "-")
            xp = "present" if e["xlsx_present"] else ("MISSING" if e["xlsx"] else "-")
            print(f"{year:<6}{e['sitting']:<9}{(e['pdf'] or '-')[:50]:<52}{pp:<10}{xp}")
            if e["pdf"] and not e["pdf_present"]:
                missing_pdf.append((year, e["sitting"], e["pdf"]))
            if e["xlsx"] and not e["xlsx_present"]:
                missing_xlsx.append((year, e["sitting"], e["xlsx"]))

    print(f"\nSittings named by the index: {sum(len(v) for v in data.values())} "
          f"across {len(data)} years")
    print(f"PDFs named but not on disk:  {len(missing_pdf)}")
    for y, s, f in missing_pdf:
        print(f"    {y} {s:<8} {f}")
    print(f"XLSX named but not on disk:  {len(missing_xlsx)}")
    for y, s, f in missing_xlsx:
        print(f"    {y} {s:<8} {f}")

    print("\nNOTE: this index records what the owner HOLDS, not what EXISTS. The 2019 Odisha "
          "re-exam, the 2020 October re-exam and the 2024 June re-test are real sittings whose "
          "papers are simply absent here; they stay REQUIRED in scripts/lib/sittings.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
