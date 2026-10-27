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
    6  (chapter.html no longer built -- deliverables are exact.html, json, md)
    6b render_exact          chapter-exact.html (the printed-book view) [script]
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
    ap.add_argument("--no-cdn", action="store_true",
                    help="leave local figures/ paths (skip the CDN publish step)")
    ap.add_argument("--no-compare", action="store_true",
                    help="skip the page-by-page render-vs-PDF comparison (qa/compare/<id>/)")
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

    # TIME EVERY STEP, so a slow build says where the time went (BIO12L ch01 once ran 45 min
    # on a cache miss nobody could see).
    import time
    t_all = t0 = time.time()
    timings = []

    def lap(name):
        nonlocal t0
        now = time.time()
        timings.append((name, now - t0))
        t0 = now

    # ---- 1-5 ---------------------------------------------------------------------------
    cdir, doc, n_figs = bcj.write_chapter(book_id, num, use_agent=True, lang=a.lang)
    lap("build")
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

    lap("rows")
    # ---- 7 chapter.html is NOT built. The owner decided (2026-10-24) that the deliverables are
    # chapter-exact.html, chapter.json and chapter.md only; `render_from_tree` stays as a library
    # (render_exact uses its fonts and fit factor) but writes no page of its own.
    # ---- 7b exact html: THE DELIVERABLE that looks like the printed book -------------------
    # It was a separate command (`render_exact.py`), so a chapter built here came out without
    # it -- or with a stale copy from before its last rebuild. It reads only chapter.json, so it
    # runs after every build, from the same tree the reflowed page and the rows came from.
    try:
        import render_exact
        exact_path = render_exact.write(doc, cdir)
        print(f"  exact     {os.path.relpath(exact_path, ROOT)}")
    except Exception as e:                                    # noqa: BLE001
        print(f"  exact     FAILED ({type(e).__name__}: {e})")

    lap("exact.html")
    # ---- 8 cdn: every build of a published chapter ENDS with CDN links ------------------
    # The deliverables carry CDN links only (`cdn_publish.py`). Publishing used to be a
    # separate command, so any rebuild -- by anyone -- silently put `figures/...` paths back
    # into chapter.json, chapter.md and both HTML files: BIO11L ch01 lost all 7 links that
    # way minutes after being published. A chapter that has been published (it has a link
    # map) is therefore re-published here on every build: unchanged crops are re-linked from
    # the map with no network call, changed ones are uploaded (needs ARIVIHAN_TOKEN).
    has_map = os.path.exists(os.path.join(cdir, "figures", "_cdn_map.json"))
    if (a.upload or has_map or os.environ.get("ARIVIHAN_TOKEN")) and not a.no_cdn:
        import cdn_publish
        try:
            _, st = cdn_publish.publish(cid)
            left = {k: len(v) for k, v in cdn_publish.local_refs(cdir).items() if v}
            print(f"  cdn       {st['uploaded']} uploaded, {st['reused']} re-linked from map, "
                  f"{st['already']} already linked, {len(st['failed'])} failed; "
                  f"local paths left: {left or 'none'}")
            for f in st["failed"]:
                print(f"            FAILED {f}")
        except Exception as e:                                # noqa: BLE001
            print(f"  cdn       FAILED ({type(e).__name__}: {e}) -- files keep local paths")
    else:
        print("  cdn       skipped (never published: run with ARIVIHAN_TOKEN set, or "
              "code/cdn_publish.py)")

    lap("cdn")
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

    lap("check")

    # ---- 10 COMPARE: the exact render beside the book, every page (`compare_render.py`) ---
    # The owner reviews every page against the PDF; this puts the pairs and the worst pages in
    # front of whoever runs the build, instead of a hand-made script after it.
    if not a.no_compare:
        try:
            import compare_render
            rows, out_dir = compare_render.compare(cid)
            look = [r for r in rows if r[1] > 12 or r[2] > 6]
            print(f"  compare   {len(rows)} pages -> {os.path.relpath(out_dir, ROOT)}; "
                  f"look at: {', '.join(f'p{p:02d}' for p, _d, _c in look) or 'none flagged'}")
        except SystemExit as e:
            print(f"  compare   skipped ({e})")
        except Exception as e:                                # noqa: BLE001
            print(f"  compare   FAILED ({type(e).__name__}: {e})")
        lap("compare")

    print("  time      " + ", ".join(f"{n} {t:.0f}s" for n, t in timings)
          + f"; total {time.time() - t_all:.0f}s")
    print(f"\ndone: {os.path.relpath(cdir, ROOT)}")


if __name__ == "__main__":
    main()
