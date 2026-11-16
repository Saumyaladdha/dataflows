#!/usr/bin/env python3
"""Load `ncert_content` from the FINISHED chapter extractions.

THE SOURCE IS `DATA_NCERT/<folder>/<chapter>/chapter.json`, NOT `ncert_index/`
-----------------------------------------------------------------------------
An earlier version of this script read `ncert_index/blocks/*.jsonl`. That is a partial derived
index and it loses most of the extraction:

                              ncert_index      chapter.json
    biology chapters               43               70
    content nodes               3,111            6,709
    nodes carrying bold/italic       0            2,148
    pages with a printed number      0              997
    BIO11L passage->subtopic links   0            1,692
    exercise questions               0              891

`chapter.json` is what the pipeline actually finalises (`consumer_finalise`), and it already
carries the three things NCERT_STORAGE_DESIGN.md listed as "to be folded in later":
formatting marks, printed page numbers, and the subtopic links. So they are folded in here.

WHAT A ROW LOOKS LIKE, AND WHY
------------------------------
    BOOK#BIO12O            META                  book
    BOOK#BIO12O            CH#05                 chapter
    BOOK#BIO12O#CH#05      PGMETA#003            page (printed number, geometry, furniture)
    BOOK#BIO12O#CH#05      PG#003#BL#0007        content node   <- the atom
    BOOK#BIO12O#CH#05      PS#BIO12O-CH05-P01    passage
    BOOK#BIO12O#CH#05      ST#BIO12-CH05-ST03    subtopic
    PAIR#BIO11             LATEST#01             old <-> new chapter pairing
    RUN#<date>             BOOK#BIO12O#CH#05     manifest

`SK = PG#<page_file>#BL#<seq>` where `seq` is the node's depth-first position in the chapter.
The tree IS reading order, so a depth-first walk is the page as printed. Carrying the page in
the key keeps `begins_with("PG#003")` working for a single page, and `order` carries the same
seq as a number so a client never has to parse a key to sort.

`chapter_id` CARRIES THE EDITION (`BIO12O-CH05`). The index files emitted it edition-neutral,
so both editions claimed `BIO12-CH05` -- exactly the join the design doc forbids, since the
editions renumber. The only edition-neutral identifiers are `subtopic_id` and `PAIR#` rows:
that is the hinge on which old and new text meet.

`runs` is built from `body` + `marks` and is ASSERTED to concatenate back to `body` character
for character. `text` stays byte-identical to `body` because that is the string the evidence
pipeline verifies quotes against; `runs` is what renders.

A GSI key attribute is OMITTED when unknown, never written as null -- DynamoDB rejects the
item outright ("Type mismatch for Index Key"). That is what makes a sparse index sparse.

Usage:
    python3 scripts/export_to_dynamo.py --out /tmp/items.jsonl        # dry run
    python3 scripts/export_to_dynamo.py --purge --apply               # replace the table
"""

import argparse
import collections
import datetime
import decimal
import hashlib
import json
import os
import re
import sys

#: Source roots are SEARCHED RECURSIVELY for `chapter.json`, and the folder names are never
#: read -- `book_id`, `grade`, `edition` and `reprint` all come from inside the file. The two
#: drops nest differently (`DATA_NCERT/<book>/<ch>/` vs `DATA_NCERT 2/new/11th/Physics/<ch>/`)
#: and they overlap: every biology chapter.json in the second drop is byte-identical to the
#: first. So chapters are keyed on (book_id, chapter number) and the first one wins, with the
#: repeats counted rather than silently dropped.
DEFAULT_SRC = [os.path.expanduser("~/Downloads/DATA_NCERT"),
               os.path.expanduser("~/Downloads/DATA_NCERT 2")]

#: marks -> run keys, per NCERT_STORAGE_DESIGN.md 2.2
MARK_KEYS = ("b", "i", "sub", "sup", "sc", "color", "frac")

#: A node is stored WHOLE. An earlier version kept a hand-picked subset, which was enough to
#: render a reflowed approximation and NOT enough to rebuild the book's own page: the exact
#: renderer places every block absolutely from its bbox on a fixed sheet, and needs
#: `line_geom`, `line_starts`, `first_indent_pt`, `layout_*`, `parts`, `panels`, `image_bbox`
#: and the caption_* family, none of which were being carried. Measured before committing to
#: it: 7,733 nodes, median 1.4 KB, max 17.9 KB; 1,182 pages, max 140 KB -- nothing approaches
#: the 400 KB item limit, and the whole corpus is 16.6 MB. So the rule is now simply: store
#: every field the extraction produced, and promote the ones worth querying to the top level.
#: `children` is the single exception -- the hierarchy is carried by `order` + `parent_id`,
#: and keeping it too would store every subtree twice.
NODE_DROP = ("children",)


def ddb(o):
    """Make a value DynamoDB-safe without going through binary float.

    DynamoDB's N is decimal-exact, but a Python float has already lost the decimal digits by
    the time it gets here -- 0.4522 is stored as 0.45220000000000005 and a rendered block moves.
    Decimal(str(f)) keeps exactly the digits the JSON carried.
    """
    if isinstance(o, float):
        return decimal.Decimal(str(o))
    if isinstance(o, list):
        return [ddb(x) for x in o]
    if isinstance(o, dict):
        return {k: ddb(v) for k, v in o.items()}
    return o


FONT_RE = re.compile(r"src:url\(data:font/([a-z0-9]+);base64,([A-Za-z0-9+/=]+)\)")


def exact_css(chapter_dir):
    """The chapter's own exact-render stylesheet, with each font payload lifted out.

    The CSS is NOT shared: biology chapters differ from each other and physics is 20 KB against
    biology's 8 KB. So it belongs on the chapter row. The fonts ARE shared -- five distinct
    payloads across all 144 files -- so each is stored once under FONT#<sha> and referenced
    here by `__FONT:<sha>__`, which a renderer substitutes back.
    """
    path = os.path.join(chapter_dir, "chapter-exact.html")
    if not os.path.exists(path):
        return None, []
    html = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not m:
        return None, []
    css, fonts = m.group(1), []

    def sub(mo):
        fmt, b64 = mo.group(1), mo.group(2)
        sha = hashlib.sha256(b64.encode()).hexdigest()[:16]
        fonts.append((sha, fmt, b64))
        return "src:url(__FONT:%s__)" % sha

    return FONT_RE.sub(sub, css), fonts


SHEET_RE = re.compile(r'<section class="sheet"[^>]*id="x([^"]+)"[^>]*>(.*?)</section>', re.S)


def exact_sheets(chapter_dir):
    """Each page's own exact-render markup, keyed by page_file.

    The structured rows are what you QUERY; this is what you RENDER. Reimplementing the
    renderer from bbox alone does not reproduce the book: the exact markup places each printed
    line as its own non-wrapping div, and a block-level box lets the browser re-wrap the text
    with its own metrics, which overflows the sheet. Storing the fragment costs a mean 9.6 KB
    per page (max 23 KB) and removes the reimplementation entirely.

    The <img> sources are CloudFront URLs already present in chapter.json, so the figures
    resolve from the CDN without anything further being stored.
    """
    path = os.path.join(chapter_dir, "chapter-exact.html")
    if not os.path.exists(path):
        return {}
    doc = open(path, encoding="utf-8", errors="replace").read()
    body = doc.split("</style>", 1)[-1]
    return {m.group(1): m.group(0) for m in SHEET_RE.finditer(body)}


def build_runs(body, marks):
    """Split `body` into runs at every formatting boundary.

    Marks overlap (a bold span containing an italic species name), so this works per character
    and then groups, rather than trying to nest spans. Returns runs plus whether they rebuild
    the body exactly -- a mismatch is a bug, not an update, so the caller counts it.
    """
    body = body or ""
    if not body:
        return [], True
    if not marks:
        return [{"t": body}], True

    attrs = [dict() for _ in range(len(body))]
    for m in marks:
        a, b = m.get("from"), m.get("to")
        if a is None or b is None:
            continue
        a, b = max(0, int(a)), min(len(body), int(b))
        for k in MARK_KEYS:
            if m.get(k) not in (None, False):
                for i in range(a, b):
                    attrs[i][k if k != "color" else "c"] = m[k]

    runs, start = [], 0
    for i in range(1, len(body) + 1):
        if i == len(body) or attrs[i] != attrs[start]:
            run = {"t": body[start:i]}
            run.update(attrs[start])
            runs.append(run)
            start = i
    return runs, ("".join(r["t"] for r in runs) == body)


def flatten(tree):
    """Depth-first walk, which is reading order. Yields (seq, depth, parent_id, node)."""
    seq = 0
    stack = [(n, 0, None) for n in reversed(tree)]
    while stack:
        node, depth, parent = stack.pop()
        seq += 1
        yield seq, depth, parent, node
        kids = node.get("children") or []
        for k in reversed(kids):
            stack.append((k, depth + 1, node.get("id")))


def chapter_items(doc, report, chapter_dir):
    book_id = doc["book_id"]
    ch = doc.get("chapter") or {}
    ch_num = ch.get("number")
    if ch_num is None:
        report["chapters_skipped"] += 1
        return [], []

    base = {"book_id": book_id, "subject": doc.get("subject"),
            "class": doc.get("grade"), "edition": doc.get("edition"),
            "reprint": doc.get("reprint"), "lang": doc.get("lang") or "EN"}
    ckey = "CH#%02d" % int(ch_num)
    part = "BOOK#%s#%s" % (book_id, ckey)
    chapter_id = "%s-CH%02d" % (book_id, int(ch_num))

    out = []
    css, fonts = exact_css(chapter_dir)
    sheets = exact_sheets(chapter_dir)

    # ---- chapter row: everything the renderer needs that is not per-node, the chapter's own
    #      exact stylesheet included, so a consumer never has to find the source tree.
    crow = dict(base, PK="BOOK#%s" % book_id, SK=ckey, kind="chapter",
                chapter_num=int(ch_num), chapter_id=chapter_id,
                title=ch.get("title") or "", unit=ch.get("unit"),
                chapter_uid=ch.get("id"),
                printed_pages=ch.get("pages") or [],
                page_files=ch.get("page_files") or [],
                sheet_pt=doc.get("sheet_pt"), design_key=doc.get("design_key"),
                source_pdf=doc.get("source_pdf"), ncert_file=doc.get("ncert_file"),
                reprint_inferred=doc.get("reprint_inferred"),
                unit_pages=doc.get("unit_pages"),
                unit_page_records=doc.get("unit_page_records"),
                text_join=doc.get("text_join"), layout_join=doc.get("layout_join"),
                special_join=doc.get("special_join"),
                structure_join=doc.get("structure_join"),
                consumer_finalise=doc.get("consumer_finalise"))
    if css:
        crow["exact_css"] = css
        crow["exact_css_fonts"] = sorted({f[0] for f in fonts})
        report["chapters_with_css"] += 1
    out.append(crow)

    # ---- page rows: the WHOLE page record. `furniture`, `art`, `decor`, `folio`, `imprint`
    #      and `size_pt` are what place the header bands, the folio tab and the figure crops
    #      on the sheet; without them an exact page cannot be rebuilt from the table alone.
    printed_by_file = {}
    for pg in doc.get("pages") or []:
        pf = pg.get("page_file")
        if not pf:
            continue
        pr = pg.get("printed")
        if pr is not None:
            printed_by_file[str(pf)] = int(pr)
        row = dict(pg)
        row.update(base)
        row.update(PK=part, SK="PGMETA#%s" % pf, kind="page",
                   chapter_num=int(ch_num), chapter_id=chapter_id, page_file=str(pf))
        row.pop("printed", None)
        if pr is not None:
            row["page_printed"] = int(pr)
        sheet = sheets.get(str(pf))
        if sheet:
            row["exact_html"] = sheet
            report["pages_with_exact_html"] += 1
        out.append(row)

    # ---- content nodes, stored whole
    passages = collections.OrderedDict()
    subtopics = collections.OrderedDict()

    for seq, depth, parent, n in flatten(doc.get("tree") or []):
        pf = str(n.get("page_file") or (n.get("page_files") or [""])[0] or "")
        body = n.get("body") or n.get("title") or n.get("caption") or ""
        runs, exact = build_runs(body, n.get("marks"))
        if not exact:
            report["runs_mismatch"] += 1

        row = {k: v for k, v in n.items() if k not in NODE_DROP}
        row.update(base)
        row.update(
            PK=part,
            SK="PG#%s#BL#%04d" % (pf or "000", seq),
            kind=n.get("kind") or "para",
            order=seq, depth=depth,
            node_id=n.get("id"),
            chapter_num=int(ch_num), chapter_id=chapter_id,
            page_file=pf,
            text=body,
            runs=runs,
            has_children=bool(n.get("children")),
            child_count=len(n.get("children") or []),
        )
        if parent:
            row["parent_id"] = parent
        if pf in printed_by_file:
            row["page_printed"] = printed_by_file[pf]

        pid = n.get("passage_id")
        if pid:
            p = passages.setdefault(pid, {"nodes": [], "heading": "", "pages": set()})
            p["nodes"].append(row["SK"])
            p["pages"].add(pf)
            if n.get("kind") in ("section", "chapter_title") and not p["heading"]:
                p["heading"] = n.get("title") or body
        stn, stname = n.get("agent_subtopic_n"), n.get("agent_subtopic_name")
        if stn is not None:
            # subtopic ids are EDITION-NEUTRAL on purpose: the family, not the book. That is
            # what lets an older-edition passage and a latest-edition passage meet.
            sid = "%s-CH%02d-ST%02d" % (book_id[:-1], int(ch_num), int(stn))
            row["subtopic_id"] = sid
            st = subtopics.setdefault(sid, {"name": stname or "", "passages": set()})
            if pid:
                st["passages"].add(pid)
        out.append(row)

    for pid, p in passages.items():
        out.append(dict(base, PK=part, SK="PS#%s" % pid, kind="passage",
                        passage_id=pid, chapter_num=int(ch_num), chapter_id=chapter_id,
                        section_heading=p["heading"],
                        nodes=p["nodes"], node_count=len(p["nodes"]),
                        pages=sorted(x for x in p["pages"] if x), order=0))
        report["passages"] += 1

    for sid, st in subtopics.items():
        out.append(dict(base, PK=part, SK="ST#%s" % sid, kind="subtopic",
                        subtopic_id=sid, name=st["name"],
                        passages=sorted(st["passages"]),
                        chapter_num=int(ch_num), chapter_id=chapter_id, order=0))
        report["subtopics"] += 1

    report["chapters"] += 1
    return out, fonts



def book_rows(by_book):
    out = []
    for book_id, info in sorted(by_book.items()):
        out.append(dict(info["base"], PK="BOOK#%s" % book_id, SK="META", kind="book",
                        chapters_extracted=info["chapters"],
                        content_nodes=info["nodes"],
                        passages=info["passages"], subtopics=info["subtopics"],
                        pages=info["pages"]))
    return out


def pair_rows(root, keep, report):
    out = []
    d = os.path.join(root, "data", "dynamodb", "_pairs")
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        for row in json.load(open(os.path.join(d, fn), encoding="utf-8")):
            if (row.get("book") or "") + "L" in keep:
                out.append(dict(row, lang="EN"))
                report["pairs"] += 1
    return out


def manifest_rows(items, run_id):
    counts = collections.Counter()
    for it in items:
        if "#CH#" in it.get("PK", "") and it.get("chapter_num") is not None:
            counts[(it["book_id"], it["chapter_num"], it.get("kind"))] += 1
    rows = {}
    for (book, ch, kind), n in counts.items():
        key = (book, ch)
        rows.setdefault(key, {
            "PK": "RUN#%s" % run_id, "SK": "BOOK#%s#CH#%02d" % (book, ch),
            "kind": "manifest", "book_id": book, "chapter_num": ch,
            "source": "DATA_NCERT/chapter.json",
            "folds_applied": ["runs_formatting", "page_printed", "passage_ids",
                              "subtopic_links", "layout_bbox"],
            "folds_pending": ["old_new_chapter_pairing(A6)", "change_rows(A8)"],
        })
        rows[key]["%s_count" % kind] = n
    return list(rows.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", nargs="+", default=DEFAULT_SRC)
    ap.add_argument("--out")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--purge", action="store_true",
                    help="delete every existing row first (the key scheme changed)")
    ap.add_argument("--table", default="ncert_content")
    ap.add_argument("--region", default="ap-southeast-1")
    args = ap.parse_args()

    run_id = datetime.date.today().isoformat()
    report = collections.Counter()
    items = []
    by_book = {}

    found = []
    for root in args.src:
        if not os.path.isdir(root):
            print("skipping missing source root: %s" % root)
            continue
        for dirpath, _dirnames, filenames in os.walk(root):
            if "chapter.json" in filenames:
                found.append(os.path.join(dirpath, "chapter.json"))
    found.sort()
    print("found %d chapter.json across %d root(s)" % (len(found), len(args.src)))

    seen_chapters = {}
    font_rows = {}
    for path in found:
        doc = json.load(open(path, encoding="utf-8"))
        bid, num = doc.get("book_id"), (doc.get("chapter") or {}).get("number")
        if not bid or num is None:
            report["chapter_unidentified"] += 1
            continue
        ckey = (bid, int(num))
        if ckey in seen_chapters:
            report["duplicate_chapter_files"] += 1
            continue
        seen_chapters[ckey] = path
        got, fonts = chapter_items(doc, report, os.path.dirname(path))
        for sha, fmt, b64 in fonts:
            if sha not in font_rows:
                font_rows[sha] = {"PK": "FONT#%s" % sha, "SK": "META", "kind": "font",
                                  "sha": sha, "format": fmt, "bytes_b64": len(b64),
                                  "data_b64": b64}
        if got:
            info = by_book.setdefault(bid, {
                "base": {"book_id": bid, "subject": doc.get("subject"),
                         "class": doc.get("grade"), "edition": doc.get("edition"),
                         "reprint": doc.get("reprint"), "lang": doc.get("lang") or "EN"},
                "chapters": 0, "nodes": 0, "passages": 0, "subtopics": 0, "pages": 0})
            info["chapters"] += 1
            info["nodes"] += sum(1 for g in got if "order" in g and g.get("kind")
                                 not in ("passage", "subtopic", "chapter", "page"))
            info["passages"] += sum(1 for g in got if g.get("kind") == "passage")
            info["subtopics"] += sum(1 for g in got if g.get("kind") == "subtopic")
            info["pages"] += sum(1 for g in got if g.get("kind") == "page")
            items += got

    items += list(font_rows.values())
    items += book_rows(by_book)
    items += pair_rows(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       set(by_book), report)
    items += manifest_rows(items, run_id)

    dup = [k for k, v in collections.Counter((i["PK"], i["SK"]) for i in items).items() if v > 1]
    if dup:
        sys.exit("ABORT: %d duplicate (PK, SK), e.g. %s" % (len(dup), dup[:3]))

    kinds = collections.Counter(i.get("kind") for i in items)
    big = sorted(((len(json.dumps(i, ensure_ascii=False, default=str)), i["PK"], i["SK"])
                  for i in items), reverse=True)[:1]
    if big and big[0][0] > 380000:
        sys.exit("ABORT: item %s/%s is %d bytes, over the 400 KB limit" % (big[0][1], big[0][2], big[0][0]))
    print("books   : %s" % ", ".join("%s(%d ch)" % (b, by_book[b]["chapters"])
                                     for b in sorted(by_book)))
    print("items   : %d" % len(items))
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print("    %-14s %6d" % (k, v))
    print("checks  : runs_mismatch=%d chapters=%d (css on %d) passages=%d subtopics=%d "
          "pairs=%d fonts=%d dup_chapter_files=%d"
          % (report["runs_mismatch"], report["chapters"], report["chapters_with_css"],
             report["passages"], report["subtopics"], report["pairs"], len(font_rows),
             report["duplicate_chapter_files"]))
    print("largest item: %d bytes (%s / %s)" % big[0])
    print("pages carrying exact_html: %d" % report["pages_with_exact_html"])

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            for i in items:
                fh.write(json.dumps(i, ensure_ascii=False, default=str) + "\n")
        print("wrote %s" % args.out)

    if args.apply:
        import boto3
        table = boto3.resource("dynamodb", region_name=args.region).Table(args.table)
        if args.purge:
            n, lek = 0, None
            while True:
                kw = {"ProjectionExpression": "PK,SK"}
                if lek:
                    kw["ExclusiveStartKey"] = lek
                r = table.scan(**kw)
                with table.batch_writer() as bw:
                    for it in r["Items"]:
                        bw.delete_item(Key={"PK": it["PK"], "SK": it["SK"]})
                        n += 1
                lek = r.get("LastEvaluatedKey")
                if not lek:
                    break
            print("purged %d existing rows" % n)
        done = 0
        with table.batch_writer() as bw:
            for it in items:
                bw.put_item(Item=ddb({k: v for k, v in it.items()
                                      if v is not None and v != []}))
                done += 1
                if done % 2000 == 0:
                    print("  %d/%d" % (done, len(items)))
        print("loaded %d items into %s (%s)" % (done, args.table, args.region))


if __name__ == "__main__":
    main()
