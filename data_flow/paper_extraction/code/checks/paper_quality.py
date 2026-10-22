#!/usr/bin/env python3
"""Mechanical quality checks over the extracted question records.

    python3 scripts/checks/paper_quality.py                 # every paper
    python3 scripts/checks/paper_quality.py --paper 2022     # one paper
    python3 scripts/checks/paper_quality.py --csv            # machine-readable

Exists because a hand audit of NEET 2022 found ~150 defects, and most of them fall into a handful
of shapes a script can recognise. A reviewer's time should go on the judgement calls -- is this
figure the right figure, is this key correct -- not on spotting that three options read "57".

Each check reports WHY it fires and what the consequence is, because severity here is not about
tidiness. An option list with two identical entries means the keyed answer is indistinguishable:
the question cannot be answered correctly even in principle, however clean the rest of the row.

What this cannot check, and deliberately does not guess at:
  * whether a figure's panel order matches the option order (needs the real paper)
  * whether a topic tag is right (needs subject knowledge)
  * whether the official key itself is right
Those stay with the human reviewer; this only clears the mechanical ground in front of them.
"""

import argparse
import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import runner_core as rc  # noqa: E402

PLACEHOLDER = re.compile(r"image option\s*[—–-]\s*will be added soon", re.I)
# A number whose exponent has been flattened: "10–2", "102 m", "m3", "sp2", "cm-3".
FLAT_EXP = re.compile(r"(?:10\s*[–—-]\s*\d|\b10[2-9]\b|\bm[23]\b|\bsp[23]\b|\bcm\s*[–—-]\s*\d)")
# A value whose leading integer and decimal point were stripped, e.g. "1.32 g" printed as "32 g".
# The discriminating signal is NOT "this option is a plain number" -- "20 / 40 / 60 / 80 minutes"
# and "1985 / 1992 / 1986 / 2002" are perfectly ordinary option sets, and an earlier version of
# this check flagged all of them, which made the finding useless. What actually marks the defect
# is INCONSISTENCY INSIDE ONE OPTION SET: some options keep a decimal point while others of
# similar magnitude have none ("25 g | 32 g | 65 g | 9.50 g"), or a value carries a meaningless
# leading zero ("0385 V", "05 V") that only makes sense as the tail of "1.0385" and "1.05".
LEADING_ZERO = re.compile(r"^\$?\s*0\d")
NUMERIC_OPT = re.compile(r"^\$?\s*(\d+(?:\.\d+)?)")


def _items(v):
    out = []
    for it in v or []:
        if isinstance(it, dict):
            out.append(f"{(it.get('label') or '').strip()} {(it.get('text') or '').strip()}".strip())
        else:
            out.append(str(it).strip())
    return [x for x in out if x]


def _norm_opt(s):
    """An option reduced to what distinguishes it: case-folded, whitespace and LaTeX spacing
    removed. Two options that differ only by `\\,` or a stray space are the SAME option to a
    candidate reading the paper."""
    s = re.sub(r"\\[,;:!]|\\mathrm|\\text|[{}$\s]", "", s or "")
    return s.lower()


def check_record(rec):
    """[(severity, code, detail)] for one record."""
    out = []
    stem = (rec.get("stem_en") or "").strip()
    structure = rec.get("structure") or "plain"
    li, lii = _items(rec.get("list_i")), _items(rec.get("list_ii"))
    stmts = _items(rec.get("statements"))
    opts = rec.get("options_en") or {}
    vals = [(k, (opts.get(k) or "").strip()) for k in ("1", "2", "3", "4")]
    official = str(rec.get("official_answer") or "")

    # --- the question has to exist at all -------------------------------------------------
    full = " ".join([stem] + stmts + li + lii).strip()
    if not full:
        out.append(("CRITICAL", "EMPTY_QUESTION",
                    "no stem, statements or lists -- nothing to answer"))
    elif not stem:
        out.append(("MEDIUM", "EMPTY_STEM",
                    "stem_en is empty; the question survives only through its lists/statements"))

    # A structured question whose structure is missing is unanswerable even with a stem, because
    # the options refer to items that are not there.
    if structure == "match" and not (li and lii):
        out.append(("CRITICAL", "MATCH_WITHOUT_LISTS",
                    f"structure=match but list_i={len(li)} list_ii={len(lii)}"))
    if structure in ("statement_i_ii", "assertion_reason", "statements") and not stmts:
        out.append(("CRITICAL", "STATEMENTS_MISSING",
                    f"structure={structure} but no statements recorded"))
    if structure == "match" and li and lii and len(li) != len(lii):
        out.append(("HIGH", "MATCH_LIST_LENGTH",
                    f"list_i has {len(li)} items, list_ii has {len(lii)}"))
    # Duplicate labels in List-II make the key's mapping impossible to apply -- the audit found
    # exactly this on Q-000392, where List-II carried two "(i)" and no "(iv)".
    labs = [re.match(r"^\(?([ivx]+|[a-d])\)?", x.strip(), re.I) for x in lii]
    labs = [m.group(1).lower() for m in labs if m]
    dup = [l for l, c in collections.Counter(labs).items() if c > 1]
    if dup:
        out.append(("CRITICAL", "LIST_LABEL_DUPLICATE",
                    f"List-II repeats label(s) {dup}; the key's mapping cannot be applied"))

    # --- the options have to be distinguishable -------------------------------------------
    present = [(k, v) for k, v in vals if v]
    if len(present) < 4:
        out.append(("HIGH", "OPTIONS_MISSING",
                    f"only {len(present)} of 4 options have text"))
    norm = collections.Counter(_norm_opt(v) for _, v in present)
    same = [n for n, c in norm.items() if c > 1 and n]
    if same:
        keys = [k for k, v in present if _norm_opt(v) in same]
        sev = "CRITICAL" if official in keys else "HIGH"
        out.append((sev, "OPTIONS_IDENTICAL",
                    f"options {keys} are indistinguishable"
                    + (f"; the keyed answer ({official}) is among them, so the question cannot be"
                       " answered correctly" if official in keys else "")))
    ph = [k for k, v in present if PLACEHOLDER.search(v)]
    if ph:
        out.append(("CRITICAL", "OPTION_PLACEHOLDER",
                    f"options {ph} are 'image option will be added soon' placeholders"))
    zeros = [k for k, v in present if LEADING_ZERO.match(v)]
    if zeros:
        # This one IS reliable: no paper prints "0385 V" or "05 V" as an option. A leading zero
        # followed directly by another digit (not a decimal point) only arises from a stripped
        # integer part. "0.05" does not match, because the character after the zero is a dot.
        out.append(("HIGH", "OPTION_LOST_LEADING_DIGITS",
                    f"options {zeros} begin with a leading zero followed by a digit"
                    " -- '0385' is the tail of '1.0385'; no option is printed that way"))
    else:
        # Mixed decimal/integer formatting within one set, where the numbers are the same order
        # of magnitude -- the shape "25 | 32 | 65 | 9.50" leaves.
        nums = [(k, NUMERIC_OPT.match(v).group(1)) for k, v in present if NUMERIC_OPT.match(v)]
        if len(nums) == 4:
            withdot = [k for k, n in nums if "." in n]
            nodot = [k for k, n in nums if "." not in n]
            if withdot and nodot and len(withdot) < 4:
                try:
                    small = min(float(n) for k, n in nums if "." in n)
                    big = min(float(n) for k, n in nums if "." not in n)
                    # the undotted ones being LARGER than the dotted one is the giveaway: a lost
                    # "1." makes 1.32 -> 32, which is bigger than the option that kept its decimal
                    if big > small:
                        # MEDIUM and honestly named. This detects inconsistent number FORMATTING
                        # within an option set, which is the shape a stripped leading "1." leaves
                        # ("1.32 g" -> "32 g", confirmed on Q82/Q83/Q87/Q88 of NEET 2022). But the
                        # same shape occurs legitimately -- "0.05 N/kg | 50 | 20 | 180" and
                        # "0.25 A | 5 | 1 | 2" are real option sets -- and distinguishing the two
                        # needs the official values, which this check does not have. So it points
                        # a reviewer at a set worth comparing against the paper; it does not claim
                        # the set is wrong.
                        out.append(("MEDIUM", "OPTION_FORMAT_INCONSISTENT",
                                    f"options {nodot} are bare integers while {withdot} keep a"
                                    f" decimal, and the integers are larger. This is the shape a"
                                    f" stripped leading '1.' leaves (1.32 -> 32), but also occurs"
                                    f" legitimately -- compare against the paper"))
                except ValueError:
                    pass

    # --- notation carried over flattened ---------------------------------------------------
    flat = []
    for label, text in [("stem", stem)] + [(f"option_{k}", v) for k, v in present]:
        if FLAT_EXP.search(text):
            flat.append(label)
    if flat:
        out.append(("MEDIUM", "FLATTENED_EXPONENT",
                    f"{', '.join(flat)} contain(s) an exponent that reads as a digit"
                    " (e.g. '10-2', 'm3', 'sp2')"))
    if "[unreadable notation]" in (stem or "") or any(
            "[unreadable notation]" in v for _, v in present):
        out.append(("HIGH", "UNREADABLE_NOTATION",
                    "the extraction itself marked part of this question unreadable"))

    # --- figures ----------------------------------------------------------------------------
    fig = rec.get("figure_path")
    if rec.get("has_figure") and not fig:
        out.append(("HIGH", "FIGURE_FLAGGED_NO_PATH", "has_figure is set but no figure_path"))
    if fig and not (os.path.exists(fig) or os.path.exists(rc.pp(fig))):
        out.append(("HIGH", "FIGURE_MISSING_ON_DISK", f"figure_path does not exist: {fig}"))
    # A question that SAYS it has a figure but carries none is unanswerable, and the phrase is a
    # reliable signal -- the audit found several ("as shown in the figure", "the given circuits").
    if not fig and re.search(r"\b(shown in the figure|given circuit|the given graph|"
                             r"following reaction sequence|truth table for the given)\b",
                             full, re.I):
        out.append(("HIGH", "FIGURE_REFERENCED_BUT_ABSENT",
                    "the question text refers to a figure/circuit/graph but none is attached"))

    # --- answer provenance -------------------------------------------------------------------
    if official and official not in ("1", "2", "3", "4"):
        out.append(("MEDIUM", "ANSWER_OUT_OF_RANGE",
                    f"official_answer is {official!r}; NTA uses 5 to mark a dropped question"))
    b6 = str(rec.get("b6_answer") or "")
    if official and b6 and official != b6:
        out.append(("LOW", "B6_DISAGREES",
                    f"blind solver answered {b6}, key says {official} -- worth a human look"))
    return out


def check_coverage(recs):
    """Per-paper, per-booklet-code completeness. Returns [(severity, code, detail)].

    Nothing in the pipeline checked this, and two whole classes of defect walked straight through
    as a result. On NEET 2023 the E2 booklet was extracted only as far as question 116 -- the
    remaining 84 questions simply were not there, and because every row that DID exist looked fine,
    no per-row check could notice. Nine further questions had no row at all. A paper is a known
    quantity: NEET prints 200 questions per booklet, numbered 1..200. Anything short of that is a
    fact about the extraction, not about the paper, and is cheap to assert.

    Truncation is reported separately from scattered gaps because the causes differ: a contiguous
    missing TAIL means the run stopped, while holes in the middle mean individual questions were
    dropped. The first is a process failure, the second a reading failure.
    """
    out = []
    by_code = collections.defaultdict(collections.Counter)
    for r in recs:
        paper = "_".join(str(r.get(k) or "?") for k in ("exam", "year", "sitting"))
        for c in r.get("paper_codes") or []:
            c = str(c).replace(f"NEET-{r.get('year')}-MAIN-", "")
            if ":" not in c:
                continue
            code, n = c.split(":", 1)
            if n.isdigit():
                by_code[(paper, code)][int(n)] += 1

    for (paper, code), counts in sorted(by_code.items()):
        present = set(counts)
        if not present:
            continue
        expected = set(range(1, 201))
        missing = sorted(expected - present)
        # a contiguous missing tail = the extraction stopped partway
        if missing and max(present) < 200:
            tail = [n for n in missing if n > max(present)]
            if len(tail) >= 10:
                out.append(("CRITICAL", "BOOKLET_TRUNCATED",
                            f"{paper} code {code}: highest question extracted is"
                            f" {max(present)}; questions {min(tail)}-200 ({len(tail)}) are absent"
                            f" -- the extraction stopped rather than finishing the booklet"))
                missing = [n for n in missing if n not in set(tail)]
        if missing:
            sev = "HIGH" if len(missing) <= 20 else "CRITICAL"
            shown = ", ".join(str(n) for n in missing[:15])
            out.append((sev, "QUESTIONS_MISSING",
                        f"{paper} code {code}: {len(missing)} question(s) have no row"
                        f" -- {shown}{' ...' if len(missing) > 15 else ''}"))
        repeated = sorted(n for n, c in counts.items() if c > 1)
        if repeated:
            out.append(("HIGH", "BOOKLET_POSITION_REUSED",
                        f"{paper} code {code}: position(s) {repeated[:12]} are claimed by more"
                        f" than one row, so the same printed question number maps to two records"))
    return out


def find_duplicates(recs):
    """{question_id: [other ids with the same question]} -- rows that are the same question.

    A per-record check cannot see this, which is why an earlier version of this script reported
    zero duplicates on a paper that is 36% duplicate rows. NEET prints the same 200 questions in
    several booklet codes in different orders, and this corpus holds both the E1 and E2 orderings
    of 2023 as separate rows: 299 rows covering 191 distinct questions.

    Matching is on the question TEXT, not on `paper_codes`, because a row extracted from the E2
    booklet records only its E2 position -- it never declares which E1 question it is the twin of,
    so the codes cannot reveal the pairing. Text is what the two share.
    """
    groups = collections.defaultdict(list)
    for r in recs:
        parts = [(r.get("stem_en") or "")]
        for key in ("list_i", "list_ii", "statements"):
            for it in r.get(key) or []:
                parts.append(it.get("text", "") if isinstance(it, dict) else str(it))
        for k in ("1", "2", "3", "4"):
            parts.append((r.get("options_en") or {}).get(k) or "")
        norm = re.sub(r"[^a-z0-9]", "", " ".join(parts).lower())
        # short keys collide by accident; a real question has plenty of text
        if len(norm) >= 60:
            groups[norm[:200]].append(r)
    out = {}
    for members in groups.values():
        if len(members) < 2:
            continue
        for r in members:
            out[r.get("question_id")] = [m.get("question_id") for m in members
                                         if m.get("question_id") != r.get("question_id")]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper")
    ap.add_argument("--csv", action="store_true")
    args = ap.parse_args()

    rec_dir = rc.pp("papers", "records")
    all_recs = []
    for name in sorted(os.listdir(rec_dir)):
        if name.endswith(".json"):
            with open(os.path.join(rec_dir, name), encoding="utf-8") as fh:
                all_recs.append(json.load(fh))
    dups = find_duplicates(all_recs)
    by_id = {r.get("question_id"): r for r in all_recs}
    findings = []
    seen = 0
    for sev, code, detail in check_coverage(
            [r for r in all_recs
             if not args.paper
             or args.paper in "_".join(str(r.get(k) or "?")
                                      for k in ("exam", "year", "sitting"))]):
        findings.append({"paper": detail.split(" code ")[0], "q_no": None,
                         "question_id": "(paper-level)", "subject": "",
                         "severity": sev, "code": code, "detail": detail})
    for name in sorted(os.listdir(rec_dir)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(rec_dir, name), encoding="utf-8") as fh:
            rec = json.load(fh)
        paper = "_".join(str(rec.get(k) or "?") for k in ("exam", "year", "sitting"))
        if args.paper and args.paper not in paper:
            continue
        seen += 1
        qno = None
        for c in rec.get("paper_codes") or []:
            tail = str(c).split(":")[-1]
            if tail.isdigit():
                qno = int(tail)
                break
        twins = dups.get(rec.get("question_id")) or []
        # A duplicate that has been RESOLVED is not a finding. scripts/merge_paper_codes.py marks
        # the surplus rows `merged_into: <primary>` and leaves them in place deliberately, because
        # each one is the only record of what its own booklet code printed -- its option order. So
        # the finding is now raised only where the twins were never reconciled; a row that points
        # at its primary, and a primary whose twins all point back at it, are both correct.
        unresolved = [t for t in twins
                      if not (by_id.get(t) or {}).get("merged_into")] if twins else []
        if twins and not rec.get("merged_into") and unresolved:
            findings.append({"paper": paper, "q_no": qno,
                             "question_id": rec.get("question_id"),
                             "subject": rec.get("subject"), "severity": "HIGH",
                             "code": "DUPLICATE_ROW",
                             "detail": f"same question as {', '.join(unresolved)} -- these are the"
                                       f" same question extracted from different booklet codes and"
                                       f" neither is marked merged_into the other, so any per-row"
                                       f" statistic counts it more than once"})
        for sev, code, detail in check_record(rec):
            findings.append({"paper": paper, "q_no": qno,
                             "question_id": rec.get("question_id"),
                             "subject": rec.get("subject"), "severity": sev,
                             "code": code, "detail": detail})

    order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    findings.sort(key=lambda f: (order.get(f["severity"], 9), f["paper"], f["q_no"] or 0))

    if args.csv:
        out = rc.pp("exports", "review", "papers", "QUALITY_FINDINGS.csv")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["paper", "q_no", "question_id", "subject",
                                               "severity", "code", "detail"])
            w.writeheader()
            w.writerows(findings)
        print(f"wrote {os.path.relpath(out, rc.pp())}")

    by_sev = collections.Counter(f["severity"] for f in findings)
    by_code = collections.Counter(f["code"] for f in findings)
    print(f"{seen} records checked, {len(findings)} findings")
    print("  by severity:", dict(by_sev))
    print("  by code:")
    for code, n in by_code.most_common():
        sev = next(f["severity"] for f in findings if f["code"] == code)
        print(f"     {n:4d}  {sev:8s} {code}")
    crit = [f for f in findings if f["severity"] == "CRITICAL"]
    if crit:
        print(f"\n  CRITICAL ({len(crit)}) -- these questions cannot be answered as they stand:")
        for f in crit[:25]:
            print(f"     {f['paper']} Q{f['q_no']} {f['question_id']}: {f['code']} — {f['detail']}")
        if len(crit) > 25:
            print(f"     ... and {len(crit) - 25} more")
    return 1 if crit else 0


if __name__ == "__main__":
    sys.exit(main())
