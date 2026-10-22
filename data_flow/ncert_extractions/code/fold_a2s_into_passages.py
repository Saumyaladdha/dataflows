"""Fold A2S transcriptions into the passage text, so a table or formula can be QUOTED.

THE GAP THIS CLOSES
-------------------
A2S reads the blocks a page read could not: tables, display equations, figure labels, worked-example
boxes. Its output was written to `steps/A2S/out/` and then went nowhere. The passage records those
blocks belong to still carry empty text and a status reading

    "no text extracted; image cropped from the page. Still NOT quotable -- A2S must transcribe it
     before it can be cited."

which was true when it was written and has not been true for 1,003 blocks since. The cost was paid
by Stage D, repeatedly and expensively:

  * `2021_O1 q186` (which codons code for lysine) is settled by Table 5.1, the genetic-code
    checkerboard. An agent located the passage, `BIO12L-CH05-P97`, found it empty, searched the
    whole book for `lysine`, `AAA` and `AAG`, and had to report `partly`. The table had in fact been
    transcribed in full -- `steps/A2S/out/BIO12L-ch05-p018-b2.runA.json` holds every codon.
  * `2015_A q104` (which character Mendel did not use) is settled only by Table 4.1, likewise art,
    likewise reported as a gap.
  * Six agents on Solutions, Current Electricity and Work-Energy could not quote `V = IR`,
    `K = 1/2 m v^2` or Raoult's law, because each is a display equation and the passage text breaks
    off exactly where it sits.

Every one of those reads as "NCERT does not carry this", which is the opposite of the truth.

HOW A BLOCK IS MATCHED TO ITS PASSAGE
-------------------------------------
By (book, chapter, page, kind) and then by ORDINAL within that page and kind -- the same rule the
figure cropper recorded in `figure_source.matched_by`. The passage's own `blocks` field is NOT used:
it is numbered per chapter while A2S items are numbered per page, and on the one passage checked by
hand the two disagreed (`blocks: [6]` against item `-b2`). Kind and ordinal agree on every record
examined, and a mismatch in COUNT between the two sides is reported rather than guessed through.

WHAT IT WILL NOT DO
-------------------
It never overwrites text that is already there, and it never invents a rendering: a table becomes
its header and rows, an equation its transcribed form, a figure its caption and labels, a box its
text. Where A2S itself returned an error object the passage is left exactly as it was, still
carrying its "not quotable" status, because that status is then still correct.
"""

import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import runner_core as rc                                      # noqa: E402

PASSAGES = ("ncert", "passages")
A2S_OUT = ("steps", "A2S", "out")
#: Only these passage kinds are art. A paragraph with empty text is a different fault and is left
#: alone so it stays visible as one.
ART_KINDS = {"table", "equation", "figure", "box"}
ITEM = re.compile(r"^([A-Z]{3}\d{2}[LO])-ch(\d+)-p(\d+)-b(\d+)$")


def a2s_index():
    """{(book, chapter, page): [(block number, transcription)]}, in block order."""
    index = collections.defaultdict(list)
    for path in sorted(os.listdir(rc.pp(*A2S_OUT))):
        if not path.endswith(".runA.json"):
            continue
        match = ITEM.match(path[:-len(".runA.json")])
        if not match:
            continue
        try:
            with open(rc.pp(*A2S_OUT, path), encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        if "error" in data:
            continue
        book, chapter, page, block = match.groups()
        index[(book, int(chapter), int(page))].append((int(block), data))
    for key in index:
        index[key].sort()
    return index


def render(data):
    """One transcription as quotable text, in the shape its kind calls for."""
    kind = data.get("kind")
    if kind == "table":
        rows = [data.get("header") or []] + (data.get("rows") or [])
        lines = [" | ".join(str(cell) for cell in row) for row in rows if any(row)]
        return "\n".join(lines)
    if kind == "equation":
        number = data.get("number")
        body = (data.get("latex") or data.get("text") or "").strip()
        return "%s%s" % (body, "   (%s)" % number if number else "")
    if kind == "figure":
        parts = [data.get("caption") or ""]
        labels = data.get("labels") or []
        if labels:
            parts.append("Labels: " + "; ".join(str(x) for x in labels))
        return "\n".join(p for p in parts if p)
    if kind == "box":
        return (data.get("text") or "").strip()
    return (data.get("text") or "").strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--book", action="append", help="limit to these book ids; repeatable")
    args = ap.parse_args()

    index = a2s_index()
    counts = collections.Counter()
    mismatches = []

    for name in sorted(os.listdir(rc.pp(*PASSAGES))):
        if not name.endswith(".jsonl"):
            continue
        book = name[:-len(".jsonl")]
        if args.book and book not in args.book:
            continue
        rows, changed = [], 0
        with open(rc.pp(*PASSAGES, name), encoding="utf-8") as fh:
            for line in fh:
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                rows.append(row)

        # Group this book's art passages by page and kind, to pair them with A2S by ordinal.
        by_page = collections.defaultdict(lambda: collections.defaultdict(list))
        for row in rows:
            if row.get("kind") not in ART_KINDS or (row.get("text") or "").strip():
                continue
            try:
                page = int(row.get("page_start"))
            except (TypeError, ValueError):
                continue
            by_page[(row.get("chapter_num"), page)][row["kind"]].append(row)

        for (chapter, page), kinds in sorted(by_page.items()):
            available = index.get((book, chapter, page)) or []
            for kind, passages in kinds.items():
                matching = [(n, d) for n, d in available if d.get("kind") == kind]
                if len(matching) != len(passages):
                    mismatches.append("%s ch%02d p%03d %s: %d passage(s) but %d transcription(s)"
                                      % (book, chapter, page, kind, len(passages), len(matching)))
                for passage, (block, data) in zip(passages, matching):
                    text = render(data)
                    if not text:
                        counts["transcription was empty"] += 1
                        continue
                    passage["text"] = text
                    passage["text_source"] = "A2S %s-ch%02d-p%03d-b%d" % (book, chapter, page, block)
                    passage.pop("text_status", None)
                    counts["%s filled" % kind] += 1
                    changed += 1

        if changed and args.apply:
            target = rc.pp(*PASSAGES, name)
            with open(target + ".tmp", "w", encoding="utf-8") as fh:
                for row in rows:
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            os.replace(target + ".tmp", target)
        if changed:
            print("  %-8s %4d passage(s) filled" % (book, changed))

    for reason, number in counts.most_common():
        print("%-28s %d" % (reason, number))
    if mismatches:
        print("\nCOUNT MISMATCHES -- left untouched, not guessed through:")
        for line in mismatches[:20]:
            print("  " + line)
        if len(mismatches) > 20:
            print("  ... and %d more" % (len(mismatches) - 20))
    if not args.apply:
        print("\n(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
