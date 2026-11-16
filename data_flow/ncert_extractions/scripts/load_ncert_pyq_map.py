#!/usr/bin/env python3
"""Load the NCERT <-> PYQ mapping into `ncert_content`.

WHAT THE MAPPING IS
-------------------
`DATA_NCERT 2/Mapping/<subject>/<class>/chapter*/..._ncert_paper_map.json` holds, for each past
question, where in NCERT the answer actually lives -- and it does it TWICE, once against the
latest edition and once against the older one. That second half is the thing the storage design
has been waiting for: a question anchored in both editions at once, so "what did this change
between editions" has something to stand on.

Measured before writing anything: 378 questions, 756 edition-sides (every question carries both
BIO11L and BIO11O), 1,994 quotes, across 9 papers and 22 chapters.

TWO ROW SHAPES, BECAUSE THERE ARE TWO QUESTIONS TO ASK
------------------------------------------------------
    QMAP#2015_A__q047    BIO11L                        edition side -- the full finding
    QMAP#2015_A__q047    BIO11O                        the same question against the old book
    BOOK#BIO11L#CH#02    MAPQ#2015_A__q047#BIO11L-CH02-P37    one quote, one passage

The first answers "which NCERT passage answers this PYQ, in each edition?" -- one Query on
`QMAP#<question_id>` returns both sides side by side. The second answers the reverse, "which
PYQs does this passage answer?", and it carries `passage_id`, so it lands in the existing
`by_passage` GSI without a table change.

The quote rows are deliberately THIN -- question id, what the quote is for, the link type and
whether it supports the answer. The `exact_line` text and the `missing` list stay on the QMAP
row only, so the same prose is not stored 1,994 times. A reader who wants the wording follows
the question id.

The CHAPTER COMES FROM THE PASSAGE ID, NOT THE FOLDER NAME. `Mapping/Bio/11th/chapter1/` holds
`biological_classification_...`, whose passages are `BIO11L-CH02-*` -- the folders are numbered
by file, not by NCERT chapter, and trusting the folder would file every row one chapter off.

Usage:
    python3 scripts/load_ncert_pyq_map.py --out /tmp/map.jsonl
    python3 scripts/load_ncert_pyq_map.py --apply
"""

import argparse
import collections
import decimal
import glob
import json
import os
import re
import sys

DEFAULT_SRC = os.path.expanduser("~/Downloads/DATA_NCERT 2/Mapping")
CH_RE = re.compile(r"-CH(\d+)-")


def ddb(o):
    if isinstance(o, float):
        return decimal.Decimal(str(o))
    if isinstance(o, list):
        return [ddb(x) for x in o]
    if isinstance(o, dict):
        return {k: ddb(v) for k, v in o.items()}
    return o


def build(src, report):
    rows, seq = [], 0
    for path in sorted(glob.glob(os.path.join(src, "**", "*_ncert_paper_map.json"),
                                 recursive=True)):
        try:
            doc = json.load(open(path, encoding="utf-8"))
        except Exception:
            report["unreadable_files"] += 1
            continue
        report["files"] += 1
        for q in doc:
            qid = q.get("question_id")
            if not qid:
                report["rows_without_question_id"] += 1
                continue
            paper = qid.split("__")[0]
            ans = q.get("answer") or {}
            for side in ("latest", "older"):
                s = q.get(side) or {}
                if not s:
                    report["missing_side_%s" % side] += 1
                    continue
                book = s.get("book")
                if not book:
                    report["side_without_book"] += 1
                    continue
                quotes = s.get("quotes") or []
                rows.append({
                    "PK": "QMAP#%s" % qid, "SK": book, "kind": "pyq_ncert_map",
                    "question_id": qid, "paper_code": paper,
                    "edition": "latest" if side == "latest" else "older",
                    "edition_label": s.get("label"), "book_id": book,
                    "verdict": s.get("verdict"), "link_type": s.get("link_type"),
                    "supports_answer": s.get("supports_answer"),
                    "missing": s.get("missing") or [], "note": s.get("note"),
                    "quotes": quotes, "quote_count": len(quotes),
                    "answer_option": ans.get("option"), "answer_text": ans.get("text"),
                    "answer_source": ans.get("source"),
                    "subtopics": q.get("subtopics") or [],
                    "source_file": os.path.relpath(path, src),
                })
                report["sides"] += 1

                for qn, qu in enumerate(quotes):
                    pid = qu.get("passage_id")
                    if not pid:
                        report["quotes_without_passage"] += 1
                        continue
                    m = CH_RE.search(pid)
                    if not m:
                        report["passage_id_without_chapter"] += 1
                        continue
                    seq += 1
                    rows.append({
                        "PK": "BOOK#%s#CH#%02d" % (book, int(m.group(1))),
                        # the quote index is part of the key because one question quotes the
                        # SAME passage more than once -- 2015_A__q047 cites BIO11L-CH02-P37
                        # twice, for two different halves of the same statement. 370 rows
                        # collided on (qid, passage) alone, which the duplicate guard caught.
                        "SK": "MAPQ#%s#%s#%02d" % (qid, pid, qn),
                        "kind": "pyq_link",
                        "question_id": qid, "paper_code": paper,
                        "passage_id": pid, "order": seq,
                        "book_id": book, "chapter_num": int(m.group(1)),
                        "edition": "latest" if side == "latest" else "older",
                        "link_type": s.get("link_type"),
                        "supports_answer": s.get("supports_answer"),
                        "quote_n": qn,
                        "quote_for": qu.get("for"),
                        "named_ok": qu.get("named_ok"),
                        "found_in": qu.get("found_in"),
                    })
                    report["links"] += 1
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=DEFAULT_SRC)
    ap.add_argument("--out")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--table", default="ncert_content")
    ap.add_argument("--region", default="ap-southeast-1")
    args = ap.parse_args()

    report = collections.Counter()
    rows = build(args.src, report)

    dup = [k for k, v in collections.Counter((r["PK"], r["SK"]) for r in rows).items() if v > 1]
    if dup:
        sys.exit("ABORT: %d duplicate (PK, SK), e.g. %s" % (len(dup), dup[:3]))

    kinds = collections.Counter(r["kind"] for r in rows)
    papers = collections.Counter(r["paper_code"] for r in rows if r["kind"] == "pyq_ncert_map")
    print("files read      : %d" % report["files"])
    print("rows            : %d  %s" % (len(rows), dict(kinds)))
    print("questions       : %d" % (report["sides"] // 2))
    print("papers          : %s" % dict(sorted(papers.items())))
    skipped = {k: v for k, v in report.items()
               if k not in ("files", "sides", "links") and v}
    print("skipped/odd     : %s" % (skipped or "none"))

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
        print("wrote %s" % args.out)

    if args.apply:
        import boto3
        t = boto3.resource("dynamodb", region_name=args.region).Table(args.table)
        done = 0
        with t.batch_writer() as bw:
            for r in rows:
                bw.put_item(Item=ddb({k: v for k, v in r.items()
                                      if v is not None and v != []}))
                done += 1
                if done % 500 == 0:
                    print("  %d/%d" % (done, len(rows)))
        print("loaded %d rows into %s (%s)" % (done, args.table, args.region))


if __name__ == "__main__":
    main()
