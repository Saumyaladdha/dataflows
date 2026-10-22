#!/usr/bin/env python3
"""A7 - find the differences between each paired old/new passage in one chapter (spec
docs/SPEC.md Section 9/A7, 6.4, schemas/A7.json).

Pure SCRIPT step, no agent (spec 9/A7, config/steps.yaml A7: agent "script", input_fields []).
Procedure: word-level diff after normalise_quote, on each *paired* passage from A6's output.
Identical pairs are dropped entirely -- only non-identical pairs produce a diff entry. A moved
page break never counts as a difference; that's handled upstream by A2 joining text split across
a page break before any passage is ever written, so by the time a passage reaches this script its
text has no page-break artefacts left to special-case here (spec 9/A7's own wording: "A2 joined
text first").

Usage:
    python3 scripts/diff_pairs.py --chapter-id BIO12-CH06
"""
import argparse
import difflib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import io as lib_io
from lib.text_normalise import normalise_quote


def load_passage_texts(book_id, passages_dir=None):
    """passage_id -> text, from ncert/passages/<BOOK>.jsonl (spec 6.4)."""
    path = os.path.join(passages_dir or lib_io.project_path("ncert", "passages"), f"{book_id}.jsonl")
    return {p["passage_id"]: p["text"] for p in lib_io.read_jsonl(path)}


def word_diff(old_text, new_text):
    """Word-level diff of two passages after normalise_quote (spec 9/A7). Returns
    (identical, diff) where diff is a list of {"old", "new"} differing spans in the SequenceMatcher
    opcode order, each span joined back into readable text (not single tokens) so a human or A8
    can read old vs. new fragments directly. A pure delete has new="", a pure insert has old="".
    Returns identical=True (diff=[]) when the two normalised word sequences match exactly --
    including when normalise_quote alone erases the only difference (whitespace, a moved page
    break already re-joined by A2, curly-quote/ligature spelling, end-of-line hyphenation)."""
    old_words = normalise_quote(old_text).split()
    new_words = normalise_quote(new_text).split()

    sm = difflib.SequenceMatcher(None, old_words, new_words, autojunk=False)
    diff = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        diff.append({
            "old": " ".join(old_words[i1:i2]),
            "new": " ".join(new_words[j1:j2]),
        })
    return (len(diff) == 0), diff


def diff_chapter(chapter_id, old_book=None, new_book=None, pairs_path=None, passages_dir=None, out_path=None):
    """Run A7 for one chapter: read its A6 pairs file, diff every result=='pair' entry, and
    write one JSONL line per NON-identical pair (schemas/A7.json) to ncert/diffs/<CHAPTER>.jsonl.
    Rewrites the file fresh each run (full overwrite, not append) so reruns are idempotent and
    never accumulate duplicate or stale lines from a since-corrected A6 pairing."""
    pairs_path = pairs_path or lib_io.project_path("ncert", "pairs", f"{chapter_id}.json")
    if not os.path.exists(pairs_path):
        raise FileNotFoundError(f"A7 needs A6's output first: {pairs_path} does not exist")
    import json
    with open(pairs_path, "r", encoding="utf-8") as f:
        pairs = json.load(f)

    if old_book is None or new_book is None:
        from pair_passages import derive_book_ids
        default_old, default_new = derive_book_ids(chapter_id)
        old_book = old_book or default_old
        new_book = new_book or default_new

    old_texts = load_passage_texts(old_book, passages_dir)
    new_texts = load_passage_texts(new_book, passages_dir)

    lines = []
    n_identical = 0
    for entry in pairs:
        if entry.get("result") != "pair":
            continue
        old_id, new_id = entry["old_passage_id"], entry["new_passage_id"]
        if old_id not in old_texts:
            raise KeyError(f"A7: paired old_passage_id {old_id!r} not found in ncert/passages/{old_book}.jsonl")
        if new_id not in new_texts:
            raise KeyError(f"A7: paired new_passage_id {new_id!r} not found in ncert/passages/{new_book}.jsonl")

        identical, diff = word_diff(old_texts[old_id], new_texts[new_id])
        if identical:
            n_identical += 1
            continue  # spec 9/A7: "Identical -> drop" -- no line written at all
        lines.append({"pair": [old_id, new_id], "identical": False, "diff": diff})

    out_path = out_path or lib_io.project_path("ncert", "diffs", f"{chapter_id}.jsonl")
    lib_io.ensure_parent(out_path)
    text = "".join(json.dumps(line, ensure_ascii=False) + "\n" for line in lines)
    lib_io.atomic_write_text(out_path, text)

    print(
        f"A7 diff_pairs: chapter={chapter_id} old_book={old_book} new_book={new_book} "
        f"pairs_checked={n_identical + len(lines)} identical_dropped={n_identical} "
        f"non_identical_written={len(lines)} -> {out_path}"
    )
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chapter-id", required=True, help="e.g. BIO12-CH06")
    parser.add_argument("--old-book", help="default: derived as {SUBJ}{CLASS}O from --chapter-id")
    parser.add_argument("--new-book", help="default: derived as {SUBJ}{CLASS}L from --chapter-id")
    parser.add_argument("--pairs-file", help="override ncert/pairs/<CHAPTER>.json")
    parser.add_argument("--passages-dir", help="override ncert/passages (testing)")
    parser.add_argument("--out", help="override output path (default ncert/diffs/<CHAPTER>.jsonl)")
    args = parser.parse_args()

    try:
        diff_chapter(
            chapter_id=args.chapter_id,
            old_book=args.old_book,
            new_book=args.new_book,
            pairs_path=args.pairs_file,
            passages_dir=args.passages_dir,
            out_path=args.out,
        )
    except (FileNotFoundError, KeyError) as exc:
        print(f"A7 diff_pairs FAILED for chapter {args.chapter_id}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
