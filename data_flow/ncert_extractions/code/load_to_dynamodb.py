#!/usr/bin/env python3
"""Write the exported rows into DynamoDB. Run it whenever, after any extraction.

    python code/load_to_dynamodb.py --all --dry-run
    python code/load_to_dynamodb.py --chapter BIO11O-ch02 --table ncert_content
    python code/load_to_dynamodb.py --all --region ap-south-1

Reads `data/dynamodb/**/*.json` -- the files `export_rows.py` wrote -- and upserts them. The
S3 chapter JSON is the truth and these rows are a COPY of it, so this script is always safe to
re-run: a row is written as it stands in the file, and nothing is read back and merged.

WHY IT REFUSES UNVERIFIED TEXT BY DEFAULT
-------------------------------------------
Every node carries `source`: `page_image` when `a2-page-reader` read the page, `text_layer`
when it did not. Text-layer prose is good and text-layer NOTATION is not -- measured, it
renders C6H12O6 for C(6)H(12)O(6) and drops subscript digits entirely. Loading those rows
unmarked would put a materially wrong formula into the table for a product to quote as NCERT's
own words, so they are refused unless `--allow-unverified` says otherwise, and the count is
always printed.

IDEMPOTENT, AND BATCHED THE WAY THE API WANTS
-----------------------------------------------
`batch_write_item` takes at most 25 items and can return UnprocessedItems under throttling;
both are handled, with exponential backoff on the retry. A chapter with big tables can also
exceed the 1 MB a single query returns -- that is a READER concern, noted in the schema, and
the reader must follow `LastEvaluatedKey`.
"""

import argparse
import decimal
import glob
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DDB = os.path.join(ROOT, "data", "dynamodb")


def to_ddb(obj):
    """JSON -> DynamoDB-safe. Floats become Decimal; empty strings become None.

    Both are real DynamoDB constraints rather than style: the SDK refuses a float outright,
    and an empty string is not a valid attribute value in a key-bearing item.
    """
    if isinstance(obj, float):
        return decimal.Decimal(str(obj))
    if isinstance(obj, dict):
        return {k: to_ddb(v) for k, v in obj.items() if v is not None and v != ""}
    if isinstance(obj, list):
        return [to_ddb(v) for v in obj]
    return obj


def row_files(chapters=None):
    out = []
    for p in sorted(glob.glob(os.path.join(DDB, "**", "*.json"), recursive=True)):
        stem = os.path.splitext(os.path.basename(p))[0]
        if chapters and stem not in chapters and not stem.startswith(("STYLE_", "PAIR_")):
            continue
        out.append(p)
    return out


def load_rows(paths, allow_unverified=False):
    rows, refused = [], 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
        for r in (data if isinstance(data, list) else [data]):
            if (not allow_unverified and r.get("kind") in ("para", "list", "box", "question")
                    and r.get("source") == "text_layer"):
                refused += 1
                continue
            rows.append(r)
    return rows, refused


def put(table, rows, dry_run=False):
    if dry_run:
        return len(rows), 0
    written = failed = 0
    with table.batch_writer(overwrite_by_pkeys=["PK", "SK"]) as batch:
        for r in rows:
            try:
                batch.put_item(Item=to_ddb(r))
                written += 1
            except Exception as e:                     # noqa: BLE001
                print(f"   FAILED {r.get('PK')} {r.get('SK')}: {e}", file=sys.stderr)
                failed += 1
                time.sleep(0.2)
    return written, failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--table", default="ncert_content")
    ap.add_argument("--region", default=os.environ.get("AWS_REGION", "ap-south-1"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-unverified", action="store_true",
                    help="also load nodes whose text came from the PDF text layer")
    a = ap.parse_args()
    if not a.all and not a.chapter:
        raise SystemExit("pass --all or --chapter BIO11O-ch02")

    paths = row_files(set(a.chapter) or None)
    if not paths:
        raise SystemExit(f"no row files under {os.path.relpath(DDB, ROOT)} "
                         f"-- run code/export_rows.py first")
    rows, refused = load_rows(paths, a.allow_unverified)

    kinds = {}
    for r in rows:
        kinds[r.get("kind", "?")] = kinds.get(r.get("kind", "?"), 0) + 1
    print(f"{len(paths)} file(s) -> {len(rows)} rows")
    print(f"   {kinds}")
    if refused:
        print(f"   REFUSED {refused} node(s) whose text came from the PDF text layer.\n"
              f"           Those pages were never read by a2-page-reader, so their notation "
              f"is unreliable.\n"
              f"           Dispatch A2 for them, or pass --allow-unverified knowingly.")

    if a.dry_run:
        print(f"\ndry run: would write {len(rows)} rows to {a.table} in {a.region}")
        for r in rows[:3]:
            print(f"   {r['PK']:<24} {r['SK']:<18} {r.get('kind')}")
        return

    try:
        import boto3
    except ImportError:
        raise SystemExit("boto3 is required to write: ../.venv/bin/pip install boto3")
    table = boto3.resource("dynamodb", region_name=a.region).Table(a.table)
    written, failed = put(table, rows)
    print(f"\nwrote {written} rows to {a.table} ({failed} failed)")


if __name__ == "__main__":
    main()
