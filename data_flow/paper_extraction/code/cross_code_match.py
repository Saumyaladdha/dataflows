#!/usr/bin/env python3
"""Match the same question across every booklet code of one NEET year, and use the agreement
between codes as evidence.

    python3 scripts/cross_code_match.py --year 2022 --limit 3
    python3 scripts/cross_code_match.py --year 2022 --csv

NEET prints the same 200 questions in ~24 booklet codes, each in a different order, and the
official key gives an answer per code. That redundancy is the only independent evidence available
here, because every code PDF in this corpus came from the same third-party scrape -- there is no
official NTA booklet to compare against.

What the redundancy can and cannot settle:

  CAN -- whether the option ORDER is consistent with the key. If code Q1 prints an option set in
  one order and code R1 prints the same question rotated, and each code's key points at the SAME
  option text, then the orders and the key agree and only the option VALUES are suspect. If they
  point at different text, the key and the printed order genuinely disagree, which is the single
  most serious defect a question bank can carry.

  CANNOT -- recover a value the scrape destroyed. Checked directly on the 2022 CaCO3 question:
  all 24 codes print "25 / 32 / 65 / 9.50", so the lost leading digits are lost everywhere. The
  corruption happened upstream of the code split.

Matching is on normalised question text rather than question number, because the number differs by
code and the printed numbers are not reliably parseable from the scrape's layout.
"""

import argparse
import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

BASE = "/Users/saumyaladdha/Downloads/Saumya_NEET_work/all_neet_sets_and_ans_key"


def _norm(text):
    """Question text reduced to a comparison key: letters and digits only.

    Deliberately crude. The same question in two codes is byte-identical in this scrape apart from
    option order, so a strict key is enough and avoids the false pairings a fuzzy match would make
    between the many near-identical NEET questions.
    """
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def read_key(year):
    """{booklet_code: {q_no: option}} from the official key PDF."""
    import fitz
    path = rc.pp("inputs", "keys", f"NEET_answers-key_{year}-neet.pdf")
    if not os.path.exists(path):
        return {}
    keys = {}
    for pg in fitz.open(path):
        t = " ".join(pg.get_text().split())
        m = re.search(r"(?:SET|BOOK\s*CODE)\s*:?\s*([A-Z]\d?)", t)
        if not m:
            continue
        grid = re.sub(r"Q\.\s*No\.|Option\s*Id|(?:SET|BOOK\s*CODE)\s*:?\s*[A-Z]\d?", " ", t)
        nums = [int(x) for x in re.findall(r"\b\d+\b", grid)]
        k = {}
        # the grid prints five (q, option) pairs per printed row, read left to right
        for a in range(0, len(nums) - 9, 10):
            row = nums[a:a + 10]
            for b in range(0, 10, 2):
                q, o = row[b], row[b + 1]
                if 1 <= q <= 200 and 1 <= o <= 5:
                    k.setdefault(q, o)
        if k:
            keys[m.group(1)] = k
    return keys


def read_code(path):
    """[(q_no, stem, {opt: text})] for one booklet-code PDF.

    The scrape prints each question as "<n>. <stem>" followed by "(1) ... (4) ...". Both are taken
    from the text layer; this file makes no attempt to repair notation, because its job is to
    COMPARE codes, and comparing two equally-damaged renderings is still informative.
    """
    import fitz
    doc = fitz.open(path)
    whole = "\n".join(pg.get_text() for pg in doc)
    out = []
    # The scrape's layout, confirmed by reading the text layer directly: the question NUMBER sits
    # alone on its own line, the stem follows, each option is "(n)" alone on a line with its text
    # on the next, then "Hide solution" and "CORRECT ANSWER: <letter>" and the worked solution.
    # An earlier version of this parser looked for "12. stem" on one line, which this layout never
    # produces -- it found one question per 118-page PDF and silently reported almost nothing.
    chunks = re.split(r"\n(\d{1,3})\n", "\n" + whole)
    i = 1
    while i < len(chunks) - 1:
        try:
            qno = int(chunks[i])
        except ValueError:
            i += 2
            continue
        body = chunks[i + 1]
        i += 2
        if not 1 <= qno <= 200:
            continue
        head = re.split(r"Hide solution", body)[0]
        opts = dict(re.findall(r"\((\d)\)\s*\n\s*([^\n]{1,200})", head))
        stem = re.split(r"\n\(1\)\s*\n", head)[0]
        stated = re.search(r"CORRECT ANSWER\s*:\s*([A-E])", body)
        if len(_norm(stem)) >= 40 and len(opts) >= 2:
            out.append((qno, stem.strip(), opts,
                        stated.group(1) if stated else None))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--limit", type=int, help="only read this many codes (quick look)")
    ap.add_argument("--csv", action="store_true")
    args = ap.parse_args()

    pdfs = sorted(glob.glob(os.path.join(BASE, args.year, "code-*",
                                         f"neet_{args.year}_code-*.pdf")))
    if args.limit:
        pdfs = pdfs[:args.limit]
    keys = read_key(args.year)
    print(f"{len(pdfs)} booklet-code PDFs, {len(keys)} key grids")

    # question-key -> {code: (q_no, options)}
    groups = collections.defaultdict(dict)
    for p in pdfs:
        code = p.split("code-")[-1].split(".")[0]
        try:
            qs = read_code(p)
        except Exception as exc:                     # a damaged PDF must not stop the sweep
            print(f"  {code}: unreadable ({exc})")
            continue
        for qno, stem, opts, stated in qs:
            groups[_norm(stem)[:220]][code] = (qno, opts, stated)
        print(f"  {code}: {len(qs)} questions parsed")

    multi = {k: v for k, v in groups.items() if len(v) >= 2}
    print(f"\n{len(groups)} distinct questions; {len(multi)} appear in 2+ codes")

    rows = []
    agree = disagree = unknown = 0
    for qkey, percode in multi.items():
        # what option TEXT does each code's key point at?
        picks = {}
        for code, (qno, opts, _stated) in percode.items():
            ans = (keys.get(code) or {}).get(qno)
            if ans is None or str(ans) not in opts:
                continue
            picks[code] = _norm(opts[str(ans)])[:60]
        distinct = set(picks.values())
        if not picks:
            verdict, unknown = "no_key", unknown + 1
        elif len(distinct) == 1:
            verdict, agree = "key_consistent", agree + 1
        else:
            verdict, disagree = "KEY_POINTS_AT_DIFFERENT_TEXT", disagree + 1
        rows.append({
            "codes": " ".join(sorted(percode)),
            "n_codes": len(percode),
            "q_nos": " ".join(f"{c}:{percode[c][0]}" for c in sorted(percode)),
            "verdict": verdict,
            "distinct_keyed_texts": len(distinct),
            "keyed_text_sample": sorted(distinct)[0][:60] if distinct else "",
            "stem_key": qkey[:80],
        })

    print(f"\n  key points at the SAME option text in every code : {agree}")
    print(f"  key points at DIFFERENT text between codes        : {disagree}")
    print(f"  no key entry found                                : {unknown}")
    print("\n  A question in the first group has its option order corroborated by every code that")
    print("  prints it: the orders differ, yet each code's key selects the same answer text. The")
    print("  second group is where the printed options and the official key genuinely disagree.")

    if args.csv:
        out = rc.pp("exports", "review", "papers", f"CROSS_CODE_{args.year}.csv")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["stem_key"])
            w.writeheader()
            w.writerows(sorted(rows, key=lambda r: (r["verdict"] != "KEY_POINTS_AT_DIFFERENT_TEXT",
                                                    -r["n_codes"])))
        print(f"\nwrote {os.path.relpath(out, rc.pp())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
