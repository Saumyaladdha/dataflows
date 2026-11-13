#!/usr/bin/env python3
"""Fill a booklet's official answers from a SEPARATE NTA answer-key PDF.

    python code/apply_answer_key.py --paper-id 2026_70 \
        --key "E:/neet paper/source papers/NEET_2026_21_june/Answers_key/Neet_2026_21_6_26_Answers_key.pdf"
    ... --apply

extract_paper_v2.py reads an answer printed under each question, or a key table printed inside the
booklet. Re-NEET 2026 Code-70 has neither: the answers are in NTA's provisional key, one page per
booklet code ("Test Booklet Code: 70"), as Q.No / Ans pairs. This writes them into the same fields
extract_paper_v2 fills from an in-booklet key, with `answer_from: "nta_key_pdf"`.

  "1".."4"   one answer
  "2, 3"     several accepted -- official_answer None, all of them in official_answers
  "Drop"     dropped question -- no answer, answer_bonus True

Re-running extract_paper_v2.py --apply rebuilds the paper file and drops these: run this again after.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402


def read_key(path, code):
    """{qno: [answers] | "drop"} for one booklet code's page of the key."""
    import pymupdf
    doc = pymupdf.open(path)
    for page in doc:
        text = page.get_text()
        found = re.search(r"Test Booklet Code:\s*(\S+)", text)
        if not found or found.group(1) != str(code):
            continue
        cells = [line.strip() for line in text.split("\n") if line.strip()]
        start = max(i for i, c in enumerate(cells) if c == "Ans") + 1
        body = cells[start:]
        key = {}
        # pairs in reading order: Q.No then Ans
        for qno, ans in zip(body[0::2], body[1::2]):
            if not qno.isdigit():
                raise SystemExit("unexpected key cell %r beside %r" % (qno, ans))
            if ans.lower() == "drop":
                key[int(qno)] = "drop"
            else:
                key[int(qno)] = [a.strip() for a in re.split(r"\s*,\s*", ans)]
        return key
    raise SystemExit("no page for booklet code %s in %s" % (code, path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--code", help="booklet code on the key page; default: the paper's own")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    path = rc.pp(*rc.corpus(), "papers", "%s.json" % args.paper_id)
    with open(path, encoding="utf-8") as fh:
        paper = json.load(fh)
    questions = paper["questions"]
    code = args.code or questions[0]["booklet_code"]
    key = read_key(args.key, code)
    qnos = {q["qno"] for q in questions}
    if set(key) != qnos:
        raise SystemExit("key has %d answers, paper %d questions; differ at %s"
                         % (len(key), len(qnos), sorted(set(key) ^ qnos)[:10]))
    counts = {"single": 0, "several": 0, "drop": 0, "kept": 0}
    for q in questions:
        draft = q["text_layer_draft"]
        if draft.get("official_answer") is not None or draft.get("official_answers"):
            counts["kept"] += 1
            continue
        entry = key[q["qno"]]
        if entry == "drop":
            draft.update(official_answer=None, official_answers=[], answer_bonus=True,
                         answer_line="Answer Key: Drop")
            counts["drop"] += 1
        else:
            draft.update(official_answer=entry[0] if len(entry) == 1 else None,
                         official_answers=entry,
                         answer_line="Answer Key: " + ", ".join(map(str, entry)))
            counts["single" if len(entry) == 1 else "several"] += 1
        draft.update(answer_from="nta_key_pdf", answer_starred=False)
    print("%s code %s: %d single, %d several accepted, %d dropped, %d already had an answer"
          % (args.paper_id, code, counts["single"], counts["several"], counts["drop"], counts["kept"]))
    if args.apply:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(paper, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % os.path.relpath(path, rc.pp()))


if __name__ == "__main__":
    main()
