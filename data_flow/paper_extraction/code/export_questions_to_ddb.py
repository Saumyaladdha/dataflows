#!/usr/bin/env python3
"""Turn the extracted papers into DynamoDB rows, and load them.

    python3 code/export_questions_to_ddb.py --src ~/Downloads/papers_extracted --out /tmp/ddb
    python3 code/export_questions_to_ddb.py --src ~/Downloads/papers_extracted --out /tmp/ddb \
            --create-table --load --table neetPYQs --region ap-south-1

Two halves that can be run apart. `--out` writes the rows as JSON so they can be read before any
of them reaches AWS; `--load` sends what is in `--out`. Nothing is sent unless `--load` is passed.

ONE ROW PER QUESTION
--------------------
Everything about a question sits in a single item: the stem, the options, the answer, the worked
solution, the figures, the chapter and subtopics, and the difficulty rating. Whoever opens a
question gets all of it in one read.

    GetItem  pk = PAPER#2017_A, sk = Q#001

An earlier cut of this script split those into three items, so that re-rating a difficulty band
would not rewrite the stem and the CDN urls with it. Measured, a merged row is 3 KB at the median
and 12.6 KB at the worst against a 400 KB item limit, so the split was paying a real cost in
usability for a saving that does not exist. The paper's own metadata stays its own row (sk = META)
because it belongs to the paper, not to any one question.

WHAT IS DROPPED, AND WHY
------------------------
`html`, `full_text` and `render_css`. They are a rendering of fields that are already here, they
are a third of the record, and nothing downstream reads them -- the page is built from the JSON,
not the other way round. Also dropped: `screenshot.path` and `.sha256` (a local path is no use to
a reader, and the sha was only ever an upload check), and `superseded_geometric_crops`, which
points at crops the pipeline has already replaced.

WHAT IS KEPT THAT A READER MIGHT NOT EXPECT
-------------------------------------------
`chemistry`. 513 structures across the corpus carry a SMILES string, a formula and an InChIKey
alongside the drawn SVG -- so a client can render the structure itself rather than showing a
picture of one, and the picture is still there when it would rather not.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys
import time

SCHEMA_VERSION = 1


def cdn(obj):
    """The CDN url out of a {path, cdn_url, sha256, type} block, or None."""
    if isinstance(obj, dict):
        u = obj.get("cdn_url")
        return u if isinstance(u, str) and u.startswith("http") else None
    return None


def chem(items):
    """Chemistry structures, flattened: the SMILES a client can draw, and our drawing of it."""
    out = []
    for c in items or []:
        if not c.get("smiles"):
            continue
        out.append({k: v for k, v in {
            "name": c.get("name"),
            "smiles": c.get("smiles"),
            "formula": c.get("formula"),
            "inchikey": c.get("inchikey"),
            "name_verified": c.get("name_check") == "match",
            "shown_as": c.get("shown_as"),
            "svg_url": cdn(c.get("image")),
        }.items() if v not in (None, "")})
    return out


def figures(figs):
    """Every figure, with the printed crop, our redraw, and any structures drawn inside it.

    `drawn.species[]` holds one SVG per molecule in a chemistry figure -- 759 of them across the
    corpus. Taking only `drawn.image` loses the per-molecule drawings a client needs to show a
    single structure rather than the whole scheme.
    """
    out = []
    for f in figs or []:
        printed = f.get("printed") or {}
        drawn = f.get("drawn") or {}
        row = {k: v for k, v in {
            "id": f.get("id"),
            "alt": f.get("text"),
            "png": cdn(printed.get("png")),
            "svg": cdn(printed.get("svg")),
            "drawn_svg": cdn(drawn.get("image")),
        }.items() if v}
        species = [u for u in (cdn(sp.get("image")) for sp in (drawn.get("species") or []))
                   if u]
        if species:
            row["species_svg"] = species
        if any(k in row for k in ("png", "svg", "drawn_svg", "species_svg")):
            out.append(row)
    return out


def question_rows(paper_code, year, q):
    """(question, classification, difficulty) rows for one question. Any may be None."""
    qno = q["qno"]
    pk = "PAPER#%s" % paper_code
    qu = q.get("question") or {}
    ans = q.get("answer") or {}
    sol = q.get("solution") or {}
    ai = q.get("ai_solution") or {}
    src = q.get("source") or {}

    media = {}
    for key, block in (("question_png", qu.get("screenshot")),
                       ("solution_png", sol.get("screenshot"))):
        u = cdn(block)
        if u:
            media[key] = u
    figs = figures(qu.get("figures"))
    if figs:
        media["figures"] = figs
    # THE SOLUTION'S OWN DIAGRAMS. Ray diagrams, circuits and reaction schemes drawn inside the
    # worked solution -- 1,300 links across the corpus, and all of them were being dropped.
    sol_figs = figures(sol.get("figures"))
    if sol_figs:
        media["solution_figures"] = sol_figs

    options = []
    for o in qu.get("options") or []:
        row = {"key": str(o.get("key")), "text": o.get("text") or ""}
        c = chem(o.get("chemistry"))
        if c:
            row["chemistry"] = c
        fig = figures([o["figure"]]) if isinstance(o.get("figure"), dict) else []
        if fig:
            row["figure"] = fig[0]
        options.append(row)

    question = {
        "pk": pk, "sk": "Q#%03d" % qno,
        "entity": "question",
        "question_id": q.get("question_id") or "%s__q%03d" % (paper_code, qno),
        "paper_code": paper_code, "qno": qno, "year": year,
        "stem": qu.get("stem") or "",
        "format": qu.get("format"),
        "options": options,
        "answer": {k: v for k, v in {
            "printed": ans.get("publisher"),
            "printed_text": ans.get("publisher_text"),
            "accepted": ans.get("publisher_accepted") or [],
            "printed_line": ans.get("publisher_line"),
            "starred": bool(ans.get("publisher_starred")),
            "independent": ans.get("ai"),
            "independent_confidence": ans.get("ai_confidence"),
            "verdict": ans.get("verdict"),
        }.items() if v not in (None, "", [])},
        "source": {k: v for k, v in {
            "page": src.get("page"),
            "read_from": src.get("read_from"),
            "text_layer_reliable": src.get("text_layer_reliable"),
        }.items() if v is not None},
        "flags": q.get("flags") or [],
        "schema_version": SCHEMA_VERSION,
        "extraction_version": 1,
    }
    for key, val in (("statements", qu.get("statements")), ("list_i", qu.get("list_i")),
                     ("list_ii", qu.get("list_ii")),
                     ("negative_words", qu.get("negative_words"))):
        if val:
            question[key] = val
    c = chem(qu.get("chemistry"))
    if c:
        question["chemistry"] = c
    if sol.get("steps"):
        question["solution_steps"] = sol["steps"]
        question["solution_concludes"] = sol.get("concludes")
        question["solution_complete"] = bool(sol.get("complete"))
    if ai.get("steps"):
        question["independent_steps"] = ai["steps"]
        if ai.get("why"):
            question["independent_why"] = ai["why"]
    if media:
        question["media"] = media

    # --- classification -----------------------------------------------------------------
    cls = q.get("classification") or {}
    classification = None
    chap = cls.get("chapter") or {}
    if cls.get("subject"):
        subs = [{"id": s.get("id"), "name": s.get("name")}
                for s in (cls.get("subtopics") or []) if isinstance(s, dict) and s.get("name")]
        classification = {
            "pk": pk, "sk": "Q#%03d#CLASS" % qno,
            "entity": "classification",
            "question_id": question["question_id"],
            "paper_code": paper_code, "qno": qno, "year": year,
            "subject": cls["subject"],
            "branch": cls.get("branch"),
            "chapter_code": chap.get("code"),
            "chapter_name": chap.get("name"),
            "chapter_confidence": chap.get("confidence"),
            "subtopics": subs,
            "taxonomy_gap": cls.get("taxonomy_gap"),
            "schema_version": SCHEMA_VERSION,
            "classified_version": 1,
        }
        sort = "%s#%s#%03d" % (year, paper_code, qno)
        if chap.get("code"):
            classification["gsi1pk"] = "CHAP#%s" % chap["code"]
            classification["gsi1sk"] = sort
            if subs and subs[0].get("id"):
                classification["gsi3pk"] = "TOPIC#%s#%s" % (chap["code"], subs[0]["id"])
                classification["gsi3sk"] = sort
        classification = {k: v for k, v in classification.items() if v not in (None, "")}

    # --- difficulty ---------------------------------------------------------------------
    dif = q.get("difficulty") or {}
    difficulty = None
    if dif.get("level"):
        difficulty = {
            "pk": pk, "sk": "Q#%03d#DIFF" % qno,
            "entity": "difficulty",
            "question_id": question["question_id"],
            "paper_code": paper_code, "qno": qno, "year": year,
            "level": dif["level"],
            "steps": dif.get("steps"),
            "step_list": dif.get("step_list") or [],
            "why": dif.get("why"),
            "catch": dif.get("what_makes_it_hard"),
            "schema_version": SCHEMA_VERSION,
            "rated_version": 1,
        }
        # the second spine, where the paper has been re-rated
        for a, b in (("live_options", "live_options"), ("live_option_keys", "live_option_keys"),
                     ("why_live", "why_live"), ("long_to_execute", "long_to_execute")):
            if dif.get(a) is not None:
                difficulty[b] = dif[a]
                difficulty["rated_version"] = 2
        subject = (cls.get("subject") or "unknown").lower()
        difficulty["gsi2pk"] = "DIFF#%s#%s" % (subject, dif["level"])
        difficulty["gsi2sk"] = "%s#%s#%03d" % (year, paper_code, qno)
        difficulty = {k: v for k, v in difficulty.items() if v not in (None, "")}

    # ONE ROW PER QUESTION. The stem, the chapter and topic, and the difficulty live together, so
    # whoever opens a question sees all of it at once instead of stitching three keys together.
    # The earlier split was defended as saving a rewrite when a band is re-rated; a merged row is
    # 3 KB at the median and 12.6 KB at the worst, against a 400 KB limit, so there was nothing to
    # save. The index keys move up here because the GSIs now point at this one row.
    for part, name in ((classification, "classification"), (difficulty, "difficulty")):
        if not part:
            continue
        nested = {k: v for k, v in part.items()
                  if k not in ("pk", "sk", "entity", "question_id", "paper_code", "qno", "year",
                               "schema_version") and not k.startswith("gsi")}
        question[name] = nested
        for k, v in part.items():
            if k.startswith("gsi"):
                question[k] = v

    return question


def paper_row(paper_code, meta, n):
    return {k: v for k, v in {
        "pk": "PAPER#%s" % paper_code, "sk": "META",
        "entity": "paper",
        "paper_code": paper_code,
        "year": meta.get("year"), "booklet_code": meta.get("booklet_code"),
        "exam": "NEET",
        "family": meta.get("family"), "layout": meta.get("layout"),
        "pages": meta.get("pages"), "dpi": meta.get("dpi"),
        "question_count": n,
        "source_pdf": meta.get("source_pdf"),
        "source_sha256": meta.get("sha256_16"),
        "schema_version": SCHEMA_VERSION,
        "extraction_version": 1,
    }.items() if v not in (None, "")}


def build(src, out_dir):
    files = sorted(glob.glob(os.path.join(src, "*", "*", "questions.json")))
    by_sha = {}
    papers, skipped = [], []
    for p in files:
        doc = json.load(open(p, encoding="utf-8"))
        meta = doc.get("meta") or {}
        code = "%s_%s" % (meta.get("year"), meta.get("booklet_code"))
        sha = meta.get("sha256_16")
        # THE SAME PDF TWICE IS ONE PAPER. 2018_PP and 2018_AA are the same booklet with the
        # same sha; loading both would have one silently overwrite the other on an identical key.
        if sha and sha in by_sha:
            skipped.append((os.path.basename(os.path.dirname(p)), code, by_sha[sha]))
            continue
        by_sha[sha] = code
        papers.append((code, doc))

    os.makedirs(out_dir, exist_ok=True)
    counts = collections.Counter()
    for code, doc in papers:
        rows = [paper_row(code, doc["meta"], len(doc["questions"]))]
        counts["paper"] += 1
        for q in doc["questions"]:
            qr = question_rows(code, doc["meta"].get("year"), q)
            rows.append(qr); counts["question"] += 1
            if qr.get("classification"):
                counts["with_classification"] += 1
            if qr.get("difficulty"):
                counts["with_difficulty"] += 1
        with open(os.path.join(out_dir, "%s.json" % code), "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=1)

    print("papers written : %d" % len(papers))
    for folder, code, kept_as in skipped:
        print("  SKIPPED %s -- same source pdf as %s (already in as %s)" % (folder, kept_as, kept_as))
    print("rows: %s" % dict(counts))
    # counts["with_*"] describe what the question rows carry; they are not rows of their own.
    print("total rows: %d" % (counts["paper"] + counts["question"]))
    return out_dir


def _sizes(out_dir):
    big = []
    n = 0
    for p in glob.glob(os.path.join(out_dir, "*.json")):
        for r in json.load(open(p, encoding="utf-8")):
            n += 1
            s = len(json.dumps(r, ensure_ascii=False).encode("utf-8"))
            if s > 300_000:
                big.append((r["pk"], r["sk"], s))
    return n, big


def create_table(table, region):
    import boto3
    ddb = boto3.client("dynamodb", region_name=region)
    try:
        ddb.describe_table(TableName=table)
        print("table %s already exists" % table)
        return
    except ddb.exceptions.ResourceNotFoundException:
        pass
    attrs = [("pk", "S"), ("sk", "S"), ("gsi1pk", "S"), ("gsi1sk", "S"),
             ("gsi2pk", "S"), ("gsi2sk", "S"), ("gsi3pk", "S"), ("gsi3sk", "S")]
    ddb.create_table(
        TableName=table,
        AttributeDefinitions=[{"AttributeName": a, "AttributeType": t} for a, t in attrs],
        KeySchema=[{"AttributeName": "pk", "KeyType": "HASH"},
                   {"AttributeName": "sk", "KeyType": "RANGE"}],
        BillingMode="PAY_PER_REQUEST",
        DeletionProtectionEnabled=True,
        GlobalSecondaryIndexes=[
            {"IndexName": "gsi_chapter",
             "KeySchema": [{"AttributeName": "gsi1pk", "KeyType": "HASH"},
                           {"AttributeName": "gsi1sk", "KeyType": "RANGE"}],
             "Projection": {"ProjectionType": "INCLUDE",
                            "NonKeyAttributes": ["question_id", "paper_code", "qno", "year",
                                                 "subject", "chapter_name", "subtopics"]}},
            {"IndexName": "gsi_difficulty",
             "KeySchema": [{"AttributeName": "gsi2pk", "KeyType": "HASH"},
                           {"AttributeName": "gsi2sk", "KeyType": "RANGE"}],
             "Projection": {"ProjectionType": "INCLUDE",
                            "NonKeyAttributes": ["question_id", "paper_code", "qno", "year",
                                                 "level", "steps"]}},
            {"IndexName": "gsi_subtopic",
             "KeySchema": [{"AttributeName": "gsi3pk", "KeyType": "HASH"},
                           {"AttributeName": "gsi3sk", "KeyType": "RANGE"}],
             "Projection": {"ProjectionType": "INCLUDE",
                            "NonKeyAttributes": ["question_id", "paper_code", "qno", "year",
                                                 "chapter_name"]}},
        ])
    print("creating %s in %s ..." % (table, region))
    ddb.get_waiter("table_exists").wait(TableName=table)
    ddb.update_continuous_backups(
        TableName=table,
        PointInTimeRecoverySpecification={"PointInTimeRecoveryEnabled": True})
    print("table ready, PITR on, deletion protection on")


def load(out_dir, table, region):
    import boto3
    from boto3.dynamodb.types import TypeSerializer
    ser = TypeSerializer()
    ddb = boto3.client("dynamodb", region_name=region)

    def to_item(r):
        # DynamoDB has no float type; the corpus has none either, but guard anyway.
        clean = json.loads(json.dumps(r), parse_float=str)
        return {k: ser.serialize(v) for k, v in clean.items()}

    sent = failed = 0
    t0 = time.time()
    for p in sorted(glob.glob(os.path.join(out_dir, "*.json"))):
        rows = json.load(open(p, encoding="utf-8"))
        for i in range(0, len(rows), 25):
            batch = [{"PutRequest": {"Item": to_item(r)}} for r in rows[i:i + 25]]
            for attempt in range(6):
                resp = ddb.batch_write_item(RequestItems={table: batch})
                un = resp.get("UnprocessedItems", {}).get(table) or []
                if not un:
                    break
                # UNPROCESSED ITEMS ARE NOT AN ERROR AND ARE NOT RETRIED FOR YOU. Dropping them
                # here is how a load silently lands short of the row count it reports.
                batch = un
                time.sleep(2 ** attempt * 0.1)
            else:
                failed += len(batch)
                print("  FAILED %d item(s) after retries in %s" % (len(batch),
                                                                   os.path.basename(p)))
            sent += len(rows[i:i + 25])
        print("  %-12s %4d rows" % (os.path.basename(p)[:-5], len(rows)))
    print("\nsent %d rows in %.0fs, %d failed" % (sent, time.time() - t0, failed))
    n = ddb.describe_table(TableName=table)["Table"]["ItemCount"]
    print("table reports %d items (DynamoDB updates this count every ~6 hours, so it lags)" % n)
    return failed


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--table", default="neetPYQs")
    ap.add_argument("--region", default="ap-south-1")
    ap.add_argument("--create-table", action="store_true")
    ap.add_argument("--load", action="store_true")
    a = ap.parse_args()

    src = os.path.expanduser(a.src)
    build(src, a.out)
    n, big = _sizes(a.out)
    print("rows on disk: %d   items over 300 KB: %s" % (n, big or "none"))

    if a.create_table:
        create_table(a.table, a.region)
    if a.load:
        return 1 if load(a.out, a.table, a.region) else 0
    if not a.create_table:
        print("\n(nothing sent to AWS -- pass --create-table and/or --load)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
