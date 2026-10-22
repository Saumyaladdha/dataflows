#!/usr/bin/env python3
"""Run the WHOLE extraction for one chapter, end to end.

    python code/run_chapter.py BIO11O-ch02
    python code/run_chapter.py --old --class 11 --subject biology --chapter 2
    python code/run_chapter.py BIO11O-ch02 --upload        # also push crops to the CDN

This is the single entry point. It runs, in order:

    1  extract_page_layout   geometry from the PDF                     [script]
    2  join_agent_text       the A2 agent's words onto those boxes     [script, reads agents]
    3  cut_figures           figure and table crops                    [script]
    4  build_chapter_json    the tree -> chapter.json  (THE TRUTH)     [script]
    5  to_markdown           chapter.md                                [script]
    6  render_from_tree      chapter.html                              [script]
    7  export_rows           DynamoDB rows -> data/dynamodb/           [script]
    8  upload_assets         CDN urls, only with --upload              [script, needs token]

IT REFUSES TO PRETEND. Step 2 reports how many pages actually had an agent read. A chapter
whose pages were never read by `a2-page-reader` is built with text-layer text, which is good
prose and unreliable notation -- so the run prints a WARNING naming the pages, and
`--require-agent` turns that warning into a hard stop. Nothing silently claims a provenance it
does not have; every node carries `source` either way.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import book_design as design_lib        # noqa: E402
import build_chapter_json as bcj        # noqa: E402

SUBJ_CODE = {"biology": "BIO", "chemistry": "CHE", "physics": "PHY"}


def resolve(args):
    """A chapter id from either `BIO11O-ch02` or the plain-words form."""
    if args.chapter_id:
        m = re.fullmatch(r"([A-Z]{3}\d{2}[LO])-ch(\d+)", args.chapter_id)
        if not m:
            raise SystemExit(f"bad chapter id {args.chapter_id!r}; expected like BIO11O-ch02")
        return m.group(1), int(m.group(2))
    if not (args.subject and args.klass and args.chapter):
        raise SystemExit("give either BIO11O-ch02, or --subject --class --chapter (+ --old/--new)")
    subj = SUBJ_CODE.get(args.subject.lower())
    if not subj:
        raise SystemExit(f"unknown subject {args.subject!r}")
    edition = "O" if args.old else "L"
    return f"{subj}{int(args.klass):02d}{edition}", int(args.chapter)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter_id", nargs="?")
    ap.add_argument("--old", action="store_true", help="older / pre-rationalisation edition")
    ap.add_argument("--new", action="store_true", help="latest / rationalised edition")
    ap.add_argument("--subject")
    ap.add_argument("--class", dest="klass")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--lang", default="EN")
    ap.add_argument("--upload", action="store_true", help="push crops to the CDN")
    ap.add_argument("--require-agent", action="store_true",
                    help="fail if any page lacks an a2-page-reader read")
    ap.add_argument("--allow-unmeasured", action="store_true")
    a = ap.parse_args()

    book_id, num = resolve(a)
    cid = f"{book_id}-ch{num:02d}"
    subject, klass, edition = design_lib.parse_book_id(book_id)
    ed_word = "old" if edition == "O" else "new"
    print(f"=== {cid}  ({ed_word} NCERT, class {klass}, "
          f"{bcj.SUBJECT_WORD[subject]}, {a.lang})")

    if not design_lib.is_measured(book_id) and not a.allow_unmeasured:
        raise SystemExit(
            f"{book_id}: this book's page design has not been measured page by page.\n"
            f"Only {sorted(design_lib.MEASURED_KEYS)} have been. Re-run with "
            f"--allow-unmeasured to build it on the provisional design, knowing the layout "
            f"is a draft.")

    # ---- 1-5 ---------------------------------------------------------------------------
    cdir, doc, n_figs = bcj.write_chapter(book_id, num, use_agent=True, lang=a.lang)
    join = doc.get("text_join") or {}
    n_pages = join.get("pages", len(doc["pages"]))
    n_agent = join.get("pages_with_agent", 0)
    missing = join.get("pages_missing") or []

    nodes = sum(1 for _ in bcj._walk_iter(doc["tree"])) if hasattr(bcj, "_walk_iter") else None
    print(f"  tree      {len(doc['pages'])} pages, {n_figs} figures -> "
          f"{os.path.relpath(cdir, ROOT)}")
    print(f"  agent     {n_agent}/{n_pages} pages read by a2-page-reader, "
          f"{join.get('blocks_replaced', 0)} blocks replaced")
    if missing:
        msg = (f"  WARNING   {len(missing)} page(s) have NO agent read: {missing}\n"
               f"            their text comes from the PDF text layer, which is good prose "
               f"and unreliable notation.\n"
               f"            Run:  python code/run_step.py A2 --list   and dispatch "
               f"a2-page-reader for them.")
        print(msg)
        if a.require_agent:
            raise SystemExit("stopped: --require-agent and some pages are unread")

    # ---- 6 rows FIRST: the deliverable -------------------------------------------------------------------------
    r = subprocess.run([sys.executable, os.path.join(HERE, "export_rows.py"), cid],
                       cwd=ROOT, capture_output=True, text=True)
    for line in (r.stdout or "").strip().splitlines():
        print("  rows      " + line)
    if r.returncode:
        print("  rows      FAILED:", (r.stderr or "").strip()[:300])

    # ---- 7 html: the proof the rows are enough -------------------------------------------------------------------------
    try:
        import render_from_tree
        html_path = render_from_tree.write(doc, cdir)
        print(f"  html      {os.path.relpath(html_path, ROOT)}")
    except Exception as e:                                    # noqa: BLE001
        print(f"  html      SKIPPED ({type(e).__name__}: {e})")

    # ---- 8 cdn --------------------------------------------------------------------------
    if a.upload:
        import upload_assets
        done, skipped, failed = upload_assets.chapter_assets(cdir)
        print(f"  cdn       {done} uploaded, {skipped} unchanged, {failed} failed")
    else:
        print("  cdn       skipped (pass --upload with ARIVIHAN_TOKEN set)")

    # ---- 9 CHECK: every defect we have already shipped once ----------------------------
    try:
        import check_chapter
        res = check_chapter.check(doc, cdir)
        fails = [r for r in res if r[0] == "FAIL"]
        warns = [r for r in res if r[0] == "WARN"]
        print(f"  check     {len(fails)} fail, {len(warns)} warn")
        for lvl, code, msg in res:
            print(f"      {lvl:<4} {code:<22} {msg}")
        if fails and a.require_agent:
            raise SystemExit("stopped: --require-agent and the chapter has FAIL findings")
    except ImportError:
        pass

    print(f"\ndone: {os.path.relpath(cdir, ROOT)}")


if __name__ == "__main__":
    main()
