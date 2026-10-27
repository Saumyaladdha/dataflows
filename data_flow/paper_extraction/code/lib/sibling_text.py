"""Recover a question opening that one booklet code lost, from the other codes of the same exam.

2017 Code-A prints q130 without its number or first line ("protein with 333 amino acids, ..."):
the line fell off the top of the page. Codes C (q28) and D (q89) print the same question whole.
Every NEET exam is printed in several codes with the same questions in a different order, so the
missing words exist verbatim in a sibling booklet's text layer. This module finds them there; it
never writes words of its own.

`restored_opening(pdf_path, first_text)` looks for `first_text` (the first words the damaged
booklet DID print) in every other PDF in the same folder, and returns the text between the sibling's
question number and those words.
"""
import functools
import glob
import os
import re
from collections import Counter

import fitz

#: How many of the damaged booklet's first words must match in the sibling.
ANCHOR_WORDS = 8
#: A question number at the start of a question in the sibling's flattened text: `28. `
QNO = re.compile(r"(?:^| )(\d{1,3})\. ")
#: An opening longer than this, or one that crosses an answer/solution line, is not one lost line.
MAX_OPENING = 300
CROSSES = re.compile(r"Answer\s*\(|\bSol\b")


def _flat(text):
    text = text.replace("’", "'").replace("‘", "'")
    return " ".join(text.split())


@functools.lru_cache(maxsize=None)
def _pages(pdf_path):
    with fitz.open(pdf_path) as doc:
        return tuple(_flat(page.get_text()) for page in doc)


def siblings(pdf_path):
    """The other booklets of the same exam: every other PDF in the same folder."""
    folder = os.path.dirname(os.path.abspath(pdf_path))
    me = os.path.normcase(os.path.abspath(pdf_path))
    return [p for p in sorted(glob.glob(os.path.join(folder, "*.pdf")))
            if os.path.normcase(os.path.abspath(p)) != me]


def restored_opening(pdf_path, first_text):
    """{text, sources[{pdf, page, qno}]} or None.

    `text` is the opening every sibling that has the question agrees on most; `sources` names each
    sibling it was read from, so the restored words can be checked against the page they came from.
    """
    words = _flat(first_text or "").split()
    if len(words) < ANCHOR_WORDS:
        return None
    anchor = " ".join(words[:ANCHOR_WORDS])
    found = []
    for sib in siblings(pdf_path):
        for n, text in enumerate(_pages(sib)):
            at = text.find(anchor)
            if at < 0:
                continue
            numbers = list(QNO.finditer(text, max(0, at - MAX_OPENING), at))
            if not numbers:
                continue
            opening = text[numbers[-1].end():at].strip()
            if opening and not CROSSES.search(opening):
                found.append((opening, os.path.basename(sib), n + 1, int(numbers[-1].group(1))))
            break
    if not found:
        return None
    best = Counter(f[0] for f in found).most_common(1)[0][0]
    return {"text": best,
            "sources": [{"pdf": pdf, "page": page, "qno": qno}
                        for opening, pdf, page, qno in found if opening == best]}
