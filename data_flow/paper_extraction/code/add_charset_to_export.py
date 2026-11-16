#!/usr/bin/env python3
"""Prepend a charset declaration to a finished export, so it reads the same on every machine.

THE BUG
-------
`question_paper.html` began at `<title>` -- no doctype, no `<html>`, no `<head>`, and no
charset. The bytes are valid UTF-8 (verified: U+2113 SCRIPT SMALL L 12 times, U+03C9 OMEGA 51,
U+2192 ARROW 516, and no double-encoded text anywhere), but with nothing declaring that, each
browser falls back to its own locale default. On a machine defaulting to UTF-8 the page is
perfect; on one defaulting to Windows-1252 every non-ASCII character breaks, and

    T = mℓω²        is read as        T = mâ„“Ï‰²

because the three UTF-8 bytes E2 84 93 of "ℓ" are shown as three Latin-1 characters. Nothing is
wrong with the file's content -- it was never told how to be read. All 19 exported papers have
this defect.

WHY PREPEND AND NOT REGENERATE
------------------------------
`export_paper_v2.py` now emits the declaration, so new exports are fine. But most papers in
`data/` cannot be rebuilt -- it answers "no v2 papers found" for them -- and five were made by
a generator that is not in the repo at all. For those the only route is to patch in place.

The declaration must land in the FIRST 1024 BYTES: that is all a browser scans before deciding.
Prepending puts it at byte 0. The attribute is written unquoted (`charset=utf-8`), which is
valid HTML5 and is also what survives being embedded in either kind of Python string literal --
two earlier attempts at the generator broke on exactly that.

Usage:
    python3 code/add_charset_to_export.py --paper 2024_S1
    python3 code/add_charset_to_export.py --paper 2024_S1 --apply
    python3 code/add_charset_to_export.py --all --apply
"""

import argparse
import glob
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#: `viewport` rides along because the same page is opened on laptops of very different widths
#: and without it a narrow screen renders the card tables at desktop width and clips them.
HEAD = "<!doctype html><meta charset=utf-8>" \
       "<meta name=viewport content='width=device-width,initial-scale=1'>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if not (a.paper or a.all):
        sys.exit("give --paper <code> or --all")

    pattern = os.path.join(HERE, "data", "*", a.paper or "*", "question_paper.html")
    done = skipped = broken = 0
    for path in sorted(glob.glob(pattern)):
        rel = os.path.relpath(path, os.path.join(HERE, "data"))
        raw = open(path, "rb").read()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            # Declaring utf-8 over bytes that are not utf-8 would make things worse, not better.
            print("  %-28s NOT VALID UTF-8 (%s) -- left alone" % (rel, exc.reason))
            broken += 1
            continue
        if b"charset" in raw[:1024].lower():
            print("  %-28s already declares a charset" % rel)
            skipped += 1
            continue
        print("  %-28s %7d bytes -> adding %d-byte head" % (rel, len(raw), len(HEAD)))
        done += 1
        if a.apply:
            open(path, "wb").write(HEAD.encode("utf-8") + raw)

    print("%s %d file(s); %d already fine, %d not valid UTF-8"
          % ("patched" if a.apply else "would patch", done, skipped, broken))
    if not a.apply and done:
        print("(nothing written -- pass --apply)")


if __name__ == "__main__":
    main()
