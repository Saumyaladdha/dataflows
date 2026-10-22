#!/usr/bin/env python3
"""Measure how accurately the questions were extracted, against an original paper.

    python3 scripts/checks/extraction_accuracy.py --year 2024
    python3 scripts/checks/extraction_accuracy.py --year 2024 --show truncated_number

Every check in this repo before this one compared the extraction with itself: the second reader
(B4) re-read the same scrape, the quality checks tested records for internal consistency, and
cross-code matching compared booklet codes that all came from the same third-party scrape. None of
them can see a value the scrape never carried correctly. This file compares the records with the
printed paper in `inputs/papers/`, which is the first evidence from outside the scrape.

It reports a profile of DISCREPANCIES, not a grade. A discrepancy is not automatically our error:
the page's own text layer is damaged in places (symbol fonts render as private-use characters,
maths reflows, a scanned figure carries its caption as pixels), and the booklet in hand is usually
a different code from the records. So each class below says what it is evidence OF, and the two
that are near-certain errors are separated from the ones that need a person.

Classes, in the order they are tested:

  content_dropped   -- most of what is printed is absent from the record. Evidence of a truncated
                       read: a missing fourth option, a dropped statement block, a truth table or
                       match-list that never made it into any field.
  foreign_content   -- the record holds a lot that is not printed anywhere in that question.
                       Evidence of a bad match OR of content borrowed from a neighbouring question.
  truncated_number  -- a number in the record is the printed number with its leading digits cut
                       off: 1.98 -> 98, 2.271098 -> 271098, 0.0315 -> 0.315. NEAR-CERTAIN ERROR,
                       and the one class cross-code consensus provably cannot find, because the
                       corruption happened upstream of the code split and every code shows it.
  number_mismatch   -- some other numeric difference. Needs a person: it is as often the page's
                       maths reflowing as it is our value being wrong.
  clean             -- every word and number in the record appears in the printed question.

`clean` is a statement about the words on the page, not about correctness: it does not check the
answer key, and it cannot see an option whose ORDER differs from ours, because order is a property
of the booklet code.
"""

import argparse
import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import runner_core as rc  # noqa: E402
from paper_source_match import (match, parse_booklet, record_text, _tokens)  # noqa: E402

NUM = re.compile(r"\d+(?:\.\d+)?")


def numbers(text, is_page=False):
    """Numbers that are part of the CONTENT, with the structural ones removed.

    On a printed page the question's own number, its option labels "(1)".."(4)" and the running
    head's year are all numbers that no record would ever contain. Left in, they make every single
    record look like it lost four or five numbers -- the first run of this check reported 147 of
    179 records as numerically wrong and 0 as clean, which was entirely this.
    """
    t = re.sub(r"\\[a-zA-Z]+", " ", text or "")
    if is_page:
        t = re.sub(r"^\s*\d{1,3}\s*\.", " ", t)
        t = re.sub(r"\(\s*(\d)\s*\)", " ", t)
        t = re.sub(r"NEET\s*\(UG\)[^\n]{0,40}", " ", t)
    return collections.Counter(NUM.findall(t))


def truncations(page_nums, our_nums):
    """[(printed, ours)] where ours is the printed number with one or two characters cut off.

    The test is on the DIGIT STRING with the decimal point removed, and it accepts a loss at EITHER
    end, because the scrape produces both: a dropped integer part with its point ("1.98" -> "98",
    "2.271098" -> "271098", "0.0315" -> "0.315") and a dropped trailing digit ("52" -> "5"). An
    earlier version tested only for a dropped prefix of three digits or more and found 1 of these
    where reading the pages by eye found several.

    Two guards keep coincidence out, and both matter because short numbers are substrings of each
    other constantly: the printed number must be ABSENT from the record, and the record's number
    must be ABSENT from the page. A question printing both 198 and 19.8 as options therefore raises
    nothing, while a record holding 98 where the page prints only 1.98 does.
    """
    out = []
    for p in page_nums:
        if p in our_nums:
            continue
        pd = p.replace(".", "")
        for o in our_nums:
            if o in page_nums:
                continue
            od = o.replace(".", "")
            if len(od) >= 2 and od != pd and od in pd and len(pd) - len(od) <= 2:
                out.append((p, o))
    return out


def classify(rec, chunk):
    """(class, detail) for one matched record."""
    ours_t = set(_tokens(record_text(rec)))
    page_t = set(_tokens(chunk["text"]))
    if not page_t or not ours_t:
        return "clean", ""
    shared = ours_t & page_t
    recall = len(shared) / len(page_t)         # how much of the page we hold
    precision = len(shared) / len(ours_t)      # how much of ours is on the page

    if recall < 0.60:
        return "content_dropped", (f"only {recall:.0%} of the printed question's words are in the "
                                   f"record; absent: "
                                   f"{', '.join(sorted(page_t - ours_t)[:6])}")
    if precision < 0.85:
        return "foreign_content", (f"{1 - precision:.0%} of the record's words are not printed in "
                                   f"this question: {', '.join(sorted(ours_t - page_t)[:6])}")

    pn, on = numbers(chunk["text"], True), numbers(record_text(rec))
    trunc = truncations(pn, on)
    if trunc:
        return "truncated_number", "; ".join(f"paper prints {p!r}, record holds {o!r}"
                                             for p, o in trunc[:3])
    missing = sorted(d for d in pn if pn[d] > on.get(d, 0) and len(d) >= 2)
    if missing:
        return "number_mismatch", f"printed numbers absent from the record: {missing[:6]}"
    return "clean", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--pdf")
    ap.add_argument("--show", help="print every record in this class")
    ap.add_argument("--csv", action="store_true")
    args = ap.parse_args()

    path = args.pdf or rc.pp("inputs", "papers", f"{args.year}.pdf")
    # A scanned volume is read through its OCR'd copy (scripts/ocr_paper.py). The OCR is good
    # enough to MATCH a question by its running text, which is what this check needs; it is not
    # good enough to correct a question's text, and this file never does that -- it only reports
    # where the record and the page differ.
    cached = rc.pp("papers", "ocr_cache", f"{args.year}.pdf")
    if os.path.exists(cached) and os.path.getsize(path) and \
            sum(1 for _ in open(path, "rb").read(1)) and os.path.exists(cached):
        import fitz
        if sum(len(p.get_text() or "") for p in fitz.open(path)) < 2000:
            path = cached
    doc, chunks = parse_booklet(path)
    if not chunks:
        print(f"{os.path.basename(path)}: no questions could be parsed -- "
              f"{sum(len(p.get_text()) for p in doc)} text characters, so this is a scan and "
              f"nothing can be compared until it is OCR'd")
        return 1

    recs = [json.load(open(p, encoding="utf-8"))
            for p in sorted(glob.glob(rc.pp("papers", "records", "Q-*.json")))]
    # Live questions only. A row marked `merged_into` is the same question read from another
    # booklet code (scripts/merge_paper_codes.py); counting it again would report one question
    # twice and, because the surplus rows are the less complete of each pair, would understate the
    # match rate -- 2023 read as 142 of 299 rather than 142 of 200.
    recs = [r for r in recs
            if str(r.get("year")) == str(args.year) and not r.get("merged_into")]
    pairs = match(recs, chunks)

    tally = collections.Counter()
    rows = []
    for rec, chunk, score in pairs:
        if not chunk:
            tally["not_matched"] += 1
            continue
        cls, detail = classify(rec, chunk)
        tally[cls] += 1
        rows.append({"question_id": rec.get("question_id"), "subject": rec.get("subject"),
                     "source_q_no": chunk["qno"], "match_score": score,
                     "class": cls, "detail": detail,
                     "stem_head": " ".join((rec.get("stem_en") or "").split())[:80]})
        if args.show and cls == args.show:
            print(f"  {rec.get('question_id')}  q{chunk['qno']:<4} {detail}")

    matched = sum(v for k, v in tally.items() if k != "not_matched")
    print(f"\n{os.path.basename(path)} vs {len(recs)} records for {args.year}: "
          f"{matched} matched, {tally['not_matched']} not matched")
    for cls in ("clean", "truncated_number", "number_mismatch", "foreign_content",
                "content_dropped"):
        if tally[cls]:
            print(f"   {tally[cls]:4d}  {cls}"
                  f"{'   <-- near-certain error' if cls == 'truncated_number' else ''}")
    if matched:
        print(f"\n   {tally['clean'] / matched:.0%} of matched records carry every word and number "
              f"that is printed in the paper")

    if args.csv:
        out = rc.pp("exports", "review", "papers", f"EXTRACTION_{args.year}.csv")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            order = {"truncated_number": 0, "content_dropped": 1, "foreign_content": 2,
                     "number_mismatch": 3, "clean": 4}
            w.writerows(sorted(rows, key=lambda r: (order.get(r["class"], 9), r["question_id"])))
        print(f"wrote {os.path.relpath(out, rc.pp())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
