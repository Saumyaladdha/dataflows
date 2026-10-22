#!/usr/bin/env python3
"""Re-tests every open flag's factual premise against the data as it stands now.

    python3 scripts/audit_flags.py                    # report
    python3 scripts/audit_flags.py --draft-decisions  # also write a DRAFT decisions file

Why this exists. A flag records a condition observed at one moment. Steps then re-run, upstream
holes get filled, and some conditions stop being true -- but nothing in the pipeline re-checks
them, so `flags/flags.jsonl` accumulates claims that are no longer so. Measured when this was
written: every one of the 9 `A2_UNREADABLE` flags named a page that has SINCE been read
successfully, and every one of the 12 `A3_SECTION_SPANS_UNREAD_PAGE` flags named a section that
now has A3 output. A reviewer reading the queue would have been asked to adjudicate 21 blockers
whose premise had already evaporated.

**This script never closes a flag.** Spec 14/F3 makes closing a reviewer's act, recorded in
`review/decisions.csv` with a named reviewer, and CLAUDE.md says people review only at Stage F.
Writing those rows here would forge a human sign-off, which is precisely what the review gate
exists to prevent. So this reports, and with --draft-decisions writes a file the owner can read,
edit and apply themselves -- with `reviewer` left EMPTY so it cannot be applied by accident.

Only mechanically checkable codes are judged. Anything needing a person's eye on a page is
reported as "needs a human" rather than guessed at.
"""

import argparse
import collections
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402


def _rows(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return out


def _has_output(step, item_id):
    for run in ("runA", "runB", "retry1", "retry2", "adjudicated"):
        if os.path.exists(rc.pp("steps", step, "out", f"{item_id}.{run}.json")):
            return True
    return False


def _records():
    out = {}
    d = rc.pp("papers", "records")
    if not os.path.isdir(d):
        return out
    for fn in os.listdir(d):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        try:
            with open(os.path.join(d, fn), encoding="utf-8") as fh:
                r = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(r, dict) and r.get("question_id"):
            out[r["question_id"]] = r
    return out


def _booklet_codes():
    path = rc.pp("register", "papers.csv")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return {r.get("paper_id"): (r.get("booklet_code") or "").strip()
                for r in csv.DictReader(fh) if r.get("file_kind") == "paper"}


def _verdict(flag, records, codes, answered_papers):
    """(state, why). state is 'stale', 'still_true', or 'needs_human'."""
    code = flag.get("code")
    item = flag.get("item_id") or ""

    if code == "A2_UNREADABLE":
        if _has_output("A2", item):
            return "stale", "the page has since been read; A2 output exists on disk"
        return "still_true", "no A2 output for this page yet"

    if code == "A3_SECTION_SPANS_UNREAD_PAGE":
        if _has_output("A3", item):
            return "stale", "the section has since been split; A3 output exists on disk"
        return "still_true", "the section still has no A3 output"

    if code == "A2_SPECIAL_UNREAD":
        if _has_output("A2S", item):
            return "stale", "the special block has since been transcribed; A2S output exists"
        return "still_true", "no A2S output for this block yet"

    if code == "B5_KEY_ROW_MISSING":
        # premise: the register row has no booklet code, so no key page can be found
        paper = item[: -len("-key")] if item.endswith("-key") else item
        has_code = bool(codes.get(paper))
        answered = answered_papers.get(paper, 0)
        if has_code and answered:
            return "stale", (f"register now has booklet_code {codes[paper]!r} and {answered} "
                             f"question(s) of this paper carry an official answer")
        if not has_code:
            return "still_true", "the register row still has no booklet code"
        return "needs_human", (f"booklet_code {codes[paper]!r} is now set but no question of this "
                               "paper is extracted yet, so the flag can be neither confirmed "
                               "nor cleared from data alone")

    if code == "S0_MISSING_INPUT":
        ev = flag.get("evidence") or []
        present = [e for e in ev if os.path.exists(rc.pp(e))]
        if ev and len(present) == len(ev):
            return "stale", f"every evidence path now exists: {present}"
        return "still_true", "the named input is still absent"

    if code in {"D1_NO_CHAPTERS", "D2_NO_SUBTOPICS", "D3_NO_PASSAGES"}:
        return "needs_human", ("depends on how far the NCERT index has progressed; re-run the "
                               "step rather than judging the flag")

    return "needs_human", "no mechanical test for this code"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft-decisions", action="store_true",
                    help="write review/decisions.DRAFT.csv for the owner to review (never applied)")
    args = ap.parse_args()

    flags = [f for f in _rows(rc.pp("flags", "flags.jsonl")) if f.get("status") == "open"]
    records = _records()
    codes = _booklet_codes()
    answered = collections.Counter()
    for r in records.values():
        if r.get("official_answer") is None:
            continue
        pref = f"NEET-{r.get('year')}-{r.get('sitting')}-"
        for c in (r.get("paper_codes") or []):
            answered[pref + str(c).rpartition(":")[0].replace(pref, "")] += 1

    buckets = collections.defaultdict(list)
    for f in flags:
        state, why = _verdict(f, records, codes, answered)
        buckets[state].append((f, why))

    print(f"open flags: {len(flags)}")
    for state in ("stale", "still_true", "needs_human"):
        print(f"  {state:12s} {len(buckets[state])}")

    print("\nSTALE, by code (premise verified false against current data):")
    for code, n in collections.Counter(f["code"] for f, _ in buckets["stale"]).most_common():
        print(f"  {code:34s} {n}")
    for f, why in buckets["stale"][:6]:
        print(f"    {f['flag_id']} {f['item_id']}: {why}")

    print("\nSTILL TRUE, by code:")
    for code, n in collections.Counter(f["code"] for f, _ in buckets["still_true"]).most_common():
        print(f"  {code:34s} {n}")

    print("\nNEEDS A HUMAN, by code:")
    for code, n in collections.Counter(f["code"] for f, _ in buckets["needs_human"]).most_common():
        print(f"  {code:34s} {n}")

    if args.draft_decisions and buckets["stale"]:
        out = rc.pp("review", "decisions.DRAFT.csv")
        with open(out, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["flag_id_or_item", "field", "decision", "corrected_value_json",
                        "reviewer", "comment", "decided_at"])
            for f, why in sorted(buckets["stale"], key=lambda t: t[0]["flag_id"]):
                w.writerow([f["flag_id"], "", "approve", "", "",
                            f"AUTOMATED EVIDENCE, NOT A DECISION: {why}", ""])
        print(f"\nwrote {os.path.relpath(out, rc.pp())}")
        print("  `reviewer` is deliberately EMPTY so this cannot be applied as-is. A person must")
        print("  put their name on each row they agree with, rename it to review/decisions.csv,")
        print("  and run scripts/apply_review.py --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
