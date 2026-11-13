#!/usr/bin/env python3
"""Reuse a finished booklet's per-question agent outputs on ANOTHER CODE OF THE SAME EXAM.

    python code/reuse_from_sibling.py --target 2022_R4 --source 2022_Q1            # report only
    python code/reuse_from_sibling.py --target 2022_R4 --source 2022_Q1 --apply

WHY: every booklet code of one NEET sitting prints the same 200 questions, shuffled -- question
order and option order both. Re-asking an agent for a question's chapter, subtopic or blind solve
on the second code costs a full paper (~$28 on Opus) to learn nothing new. What IS new on another
code is how that booklet PRINTS each question (its own B3V read, which is never reused) and how it
keys and solves it (its own printed answer and B3S read, also never reused).

HOW A QUESTION IS MATCHED (both sides from their own B3V reads, never the text layer):
  stem      normalised text, SequenceMatcher ratio >= STEM_MIN, best candidate in the same subject
  options   each target option paired to a source option by normalised text, one-to-one, every
            pair >= OPTION_MIN. Picture options (empty text) cannot be paired by text, so such a
            question gets its option-free steps copied and its option-dependent steps left to run.

WHAT IS COPIED (only where the target has no output yet -- nothing is overwritten):
  QCHAP, QTOPIC   as-is: a chapter and subtopic belong to the question, not to its option order
  B6V             only with a full option map: `answer` and every "option N" / "(N)" in its text
                  are renumbered into the target's option order
NOT copied: B3V, B3S (this booklet's own printing and solutions), E7V, FIGP, FIGC.

The source booklet is only READ. Every decision is written to steps/_reuse/<target>.json, so a
copied output can always be traced to the source question it came from.
"""

import argparse
import difflib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

STEM_MIN = 0.90
OPTION_MIN = 0.90
COPY_PLAIN = ("QCHAP", "QTOPIC")


def _norm(text):
    text = (text or "").lower()
    text = re.sub(r"\\(?:mathrm|text|mathbf|rm|left|right|,|;|!|quad)\b", " ", text)
    text = re.sub(r"[\s${}\\]+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _read(paper, step, qno):
    path = rc.pp("steps", step, "out", "%s__q%03d.runA.json" % (paper, qno))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return None if "error" in data else data


def _full_stem(read):
    parts = [read.get("stem_en") or ""]
    for name in ("list_i", "list_ii", "statements"):
        for row in read.get(name) or []:
            parts.append(row.get("text", "") if isinstance(row, dict) else str(row))
    return _norm(" ".join(parts))


def _option_map(t_opts, s_opts):
    """{target key: source key}, one-to-one over all four, or None."""
    t = {k: _norm(v) for k, v in (t_opts or {}).items()}
    s = {k: _norm(v) for k, v in (s_opts or {}).items()}
    if len(t) != 4 or len(s) != 4 or not all(t.values()) or not all(s.values()):
        return None
    out, used = {}, set()
    for tk, tv in sorted(t.items(), key=lambda kv: -len(kv[1])):
        best = max(((difflib.SequenceMatcher(None, tv, sv).ratio(), sk)
                    for sk, sv in s.items() if sk not in used), default=(0, None))
        if best[0] < OPTION_MIN:
            return None
        out[tk] = best[1]
        used.add(best[1])
    # two different source options must not read identically, or the pairing is a guess
    if len(set(s.values())) != 4:
        return None
    return out


#: An option reference in an agent's prose: "option 3", "option $3$", "Option (3)", "options 1, 2
#: and 4", "options $1$ and $3$" -- the word, then one or more numbers each optionally wrapped in
#: $...$ or (...), joined by commas / and / or. Or a bare printed label "(3)".
#: The first version matched only "option 3" and missed "option $3$", the solver's usual form, so
#: 158-171 copied solves per paper ended on the SOURCE booklet's option number (2022_R4 q006: answer
#: 4, last step "which is option 3").
_OPTION_REF = re.compile(
    r"(?i)(?P<word>\boptions?\b\s*)"
    r"(?P<nums>[\(\$]?\s*[1-4]\s*[\)\$]?(?:\s*(?:,|and|or|&|/)\s*[\(\$]?\s*[1-4]\s*[\)\$]?)*)(?![\d.])"
    r"|\((?P<label>[1-4])\)")


def _renumber(value, back):
    """Rewrite option references (source -> target numbering) inside a string or list. One pass,
    so a number renumbered once is never renumbered again."""
    if isinstance(value, list):
        return [_renumber(v, back) for v in value]
    if not isinstance(value, str):
        return value

    def swap(m):
        if m.group("label"):
            # A bare "(2)" is an option label only in prose: never after a letter, digit, ")" or
            # "]" ("\sqrt(2)", "k(2)", "t(2)", ")(3)"), and never inside $...$ maths. Renumbering
            # those turned 2022_S1 q011's V_0/sqrt(2) into sqrt(4).
            before = value[:m.start()]
            if (before and re.search(r"[A-Za-z0-9)\]\\]$", before)) or \
                    len(re.findall(r"(?<!\\)\$", before)) % 2 == 1:
                return m.group(0)
            return "(%s)" % back[m.group("label")]
        return m.group("word") + re.sub(r"[1-4]", lambda d: back[d.group()], m.group("nums"))

    return _OPTION_REF.sub(swap, value)


def match(target, source):
    paper = json.load(open(rc.pp(*rc.corpus(), "papers", "%s.json" % target), encoding="utf-8"))
    src_paper = json.load(open(rc.pp(*rc.corpus(), "papers", "%s.json" % source), encoding="utf-8"))
    subj = {q["qno"]: q.get("subject") for q in src_paper["questions"]}
    src = {}
    for q in src_paper["questions"]:
        r = _read(source, "B3V", q["qno"])
        if r:
            src[q["qno"]] = (r, _full_stem(r))
    rows = []
    for q in paper["questions"]:
        r = _read(target, "B3V", q["qno"])
        row = {"qno": q["qno"], "source_qno": None, "stem_ratio": 0.0, "option_map": None}
        if r:
            stem = _full_stem(r)
            pool = [(n, v) for n, v in src.items() if subj.get(n) == q.get("subject")] or src.items()
            best = max(((difflib.SequenceMatcher(None, stem, s[1]).ratio(), n) for n, s in pool),
                       default=(0, None))
            row["stem_ratio"] = round(best[0], 3)
            if best[0] >= STEM_MIN:
                row["source_qno"] = best[1]
                row["option_map"] = _option_map(r.get("options_en"), src[best[1]][0].get("options_en"))
        rows.append(row)
    # one source question may serve one target question only
    seen = {}
    for row in rows:
        if row["source_qno"] is None:
            continue
        other = seen.get(row["source_qno"])
        if other is not None:
            loser = row if row["stem_ratio"] <= other["stem_ratio"] else other
            loser.update(source_qno=None, option_map=None, clash=True)
            if loser is other:
                seen[row["source_qno"]] = row
        else:
            seen[row["source_qno"]] = row
    return rows


def apply(target, source, rows, write):
    counts = {s: 0 for s in COPY_PLAIN + ("B6V",)}
    for row in rows:
        if row["source_qno"] is None:
            continue
        for step in COPY_PLAIN + ("B6V",):
            out = rc.pp("steps", step, "out", "%s__q%03d.runA.json" % (target, row["qno"]))
            data = _read(source, step, row["source_qno"])
            if os.path.exists(out) or data is None:
                continue
            if step == "B6V":
                if not row["option_map"]:
                    continue
                back = {sk: tk for tk, sk in row["option_map"].items()}
                data = {k: (back.get(v, v) if k == "answer" else _renumber(v, back))
                        for k, v in data.items()}
            counts[step] += 1
            if write:
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, "w", encoding="utf-8", newline="\n") as fh:
                    json.dump(data, fh, ensure_ascii=False, indent=2)
    return counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    rows = match(a.target, a.source)
    matched = [r for r in rows if r["source_qno"]]
    mapped = [r for r in matched if r["option_map"]]
    print("%s <- %s: %d of %d questions matched, %d with a full option map"
          % (a.target, a.source, len(matched), len(rows), len(mapped)))
    print("   unmatched: %s" % [r["qno"] for r in rows if not r["source_qno"]])
    print("   matched, options not mappable (pictures or differing text): %s"
          % [r["qno"] for r in matched if not r["option_map"]])
    counts = apply(a.target, a.source, rows, a.apply)
    print("   %s: %s" % ("copied" if a.apply else "would copy", counts))
    if a.apply:
        path = rc.pp("steps", "_reuse", "%s.json" % a.target)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"target": a.target, "source": a.source, "stem_min": STEM_MIN,
                       "option_min": OPTION_MIN, "questions": rows}, fh, ensure_ascii=False, indent=1)
        print("   wrote %s" % os.path.relpath(path, rc.pp()))


if __name__ == "__main__":
    main()
