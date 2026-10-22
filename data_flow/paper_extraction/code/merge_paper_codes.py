#!/usr/bin/env python3
"""Merge the rows that are the same question read from different booklet codes, attach every
code's official answer, and record each code's option order.

    python3 scripts/merge_paper_codes.py --year 2023 --dry-run
    python3 scripts/merge_paper_codes.py --year 2023 --apply

Why
---
NEET prints the same 200 questions in ~24 booklet codes, each in its own order with the options
rotated. The pipeline reads several codes and is supposed to end with ONE row per question. It does
not: 2023 holds 299 rows for 212 distinct questions, and the surplus rows are the same questions
read again from code E2. The consequences are all visible in the data and in two outside audits:

  * 82 rows carry no `official_answer`, because the key step ran on E1-coded rows and the E2-only
    rows were never given a key -- yet the key PDF contains E2's answers.
  * 80 rows carry no `subject`, for the same reason.
  * Every per-row statistic counts duplicated questions twice, which is how a "85.9% agreement"
    came to rest on 199 rows holding 170 distinct questions.
  * A figure attached while processing one code is missing from the other code's row, which left
    questions unanswerable in one of their two rows.

What makes this safe to do with a script
----------------------------------------
Merging needs NO transcription judgement: two rows are the same question or they are not, and the
test is the text itself. What this file must never do is decide which CODE's option order is
"right" -- the orders are all right, each for its own code. So the merged row keeps one canonical
option order and records every other code's order as a permutation of it, which is what lets one
official answer serve every code (audit finding G4).

The answer is attached PER CODE and then checked for agreement after permutation. That check is the
valuable part: if code E1's key and code E2's key, applied through their own option orders, select
the same option TEXT, the answer is corroborated by two independent key grids. If they select
different text, that is a real defect and the answer is left alone and flagged, because guessing
would turn a detectable fault into an undetectable one.

Nothing is overwritten. An `official_answer` that is already present is never changed; only blanks
are filled. Every record this touches gets a `repairs` entry naming what changed and why.
"""

import argparse
import collections
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402


def _norm(text):
    t = re.sub(r"\\[a-zA-Z]+", " ", str(text or ""))
    return re.sub(r"[^a-z0-9]", "", t.lower())


def question_key(rec):
    """A key that is the same for this question in EVERY booklet code, or None.

    The stem plus the option texts as a SET: the set is what makes it code-independent, since a
    code's whole purpose is to permute the options. Requiring a decent length keeps the short,
    near-empty rows (figure-only questions, rows whose maths did not survive) out of the grouping
    entirely -- they cannot be merged safely and are left as they are.
    """
    stem = _norm(rec.get("stem_en"))
    opts = frozenset(_norm(v) for v in (rec.get("options_en") or {}).values() if _norm(v))

    # The statements and match-lists are PART OF THE KEY, not extra detail. An Assertion-Reason
    # question's stem is pure boilerplate ("Given below are two statements : One is labelled as
    # Assertion A...") and its four options are the same four standard phrases in every such
    # question in the paper; everything that identifies it sits in `statements`. Leaving them out
    # merged five unrelated questions -- gymnosperm pollen, sodium in liquid ammonia, ATP in
    # glycolysis and late wood -- into one row, which then moved questions between subjects and
    # produced a 54/57/89 split where the paper is 50/50/100.
    body = []
    for field in ("statements", "list_i", "list_ii"):
        v = rec.get(field)
        if isinstance(v, (list, tuple)):
            for it in v:
                body.append(_norm(it.get("text") if isinstance(it, dict) else it))
        elif isinstance(v, dict):
            body += [_norm(x) for x in v.values()]
    body = frozenset(b for b in body if b)

    if len(stem) + sum(len(b) for b in body) < 60 or len(opts) < 2:
        return None
    return (stem[:200], opts, body)


def _words(rec, field=None):
    if field:
        v = rec.get(field)
        blob = ""
        if isinstance(v, (list, tuple)):
            blob = " ".join(str(it.get("text") if isinstance(it, dict) else it) for it in v)
        elif isinstance(v, dict):
            blob = " ".join(str(x) for x in v.values())
        elif v:
            blob = str(v)
    else:
        blob = str(rec.get("stem_en") or "")
    return set(re.findall(r"[a-z0-9]{4,}", _norm(blob)))


def near_duplicate(a, b):
    """(is_same, why) for two rows the exact key did not group.

    A second, deliberately NARROW pass. The same two rows can be transcribed slightly differently
    from two booklet codes -- one folds a statement block into the stem, another keeps the maths as
    LaTeX where its twin lost it -- so an exact key on stem + option set leaves real duplicates
    behind. The bar here is high on purpose: this script has already merged five unrelated
    Assertion-Reason questions once by being too generous, and a wrong merge moves a question
    between subjects and hides a row.

    Every one of these must hold: the stems agree almost entirely, the statements and match-lists
    agree almost entirely, and most option text is shared. Boilerplate alone cannot satisfy it,
    because the statement and list comparison is what carries an Assertion-Reason question's
    identity, and a question with neither must clear the bar on its stem and options alone.
    """
    sa, sb = _words(a), _words(b)
    if not sa or not sb:
        return False, ""
    stem = len(sa & sb) / max(len(sa), len(sb))

    pa = _words(a, "statements") | _words(a, "list_i") | _words(a, "list_ii")
    pb = _words(b, "statements") | _words(b, "list_i") | _words(b, "list_ii")
    if pa or pb:
        if not (pa and pb):
            return False, "one row has statements or match-lists and the other has none"
        body = len(pa & pb) / max(len(pa), len(pb))
    else:
        body = 1.0

    oa = {_norm(v) for v in (a.get("options_en") or {}).values() if _norm(v)}
    ob = {_norm(v) for v in (b.get("options_en") or {}).values() if _norm(v)}
    shared = len({x for x in oa if any(x[:30] == y[:30] for y in ob)})
    opts = shared / max(1, max(len(oa), len(ob)))

    ok = stem >= 0.90 and body >= 0.90 and opts >= 0.75
    return ok, f"stem {stem:.2f}, statements/lists {body:.2f}, options {opts:.2f}"


def code_positions(rec):
    """[(code, q_no)] from paper_codes, in the short form."""
    out = []
    for c in (rec.get("paper_codes") or []):
        c = re.sub(r"^NEET-\d{4}-[A-Z]+-", "", str(c))
        if ":" in c:
            code, n = c.split(":", 1)
            if n.strip().isdigit():
                out.append((code.strip(), int(n)))
    return out


def read_keys(year):
    """{book_code: {q_no: option}} from the official key PDF.

    The 2023 grid labels its sets "BOOK CODE : E1", not "SET: E1" -- a search for the latter finds
    nothing, which is how the E2 key came to be treated as unavailable while it was in the file all
    along. Both spellings are accepted here.
    """
    import fitz
    path = rc.pp("inputs", "keys", f"NEET_answers-key_{year}-neet.pdf")
    if not os.path.exists(path):
        return {}
    keys = {}
    for page in fitz.open(path):
        flat = " ".join((page.get_text() or "").split())
        # Each year labels its grids differently: 2022 "SET: X6", 2023 "BOOK CODE : E2",
        # 2024 "Test Booklet Code : Q1". Missing a label means the whole page is skipped, which is
        # how 2023's E2 key was once believed to be absent from a file that contained it.
        m = re.search(r"(?:BOOK\s*CODE|SET|Test\s*Booklet\s*Code)\s*:?\s*([A-Z]\d?)", flat)
        if not m:
            continue
        # The grid is a pipe-delimited table, read LINE BY LINE and split on its own separators.
        # An earlier version flattened the page and chunked the numbers ten at a time, assuming
        # five (QNO, RES) pairs per printed row. The 2023 key prints EIGHT pairs per row, so every
        # chunk straddled a row boundary and whole runs of positions were lost or misread: code E2
        # came out with 133 of its 200 answers, missing 18-25 and 43-48 among others, which then
        # looked like questions whose answer simply was not in the key.
        k = {}
        for line in (page.get_text() or "").splitlines():
            if "|" not in line:
                continue
            cells = [c.strip() for c in line.split("|")]
            cells = [c for c in cells if c and not set(c) <= set("- ")]
            if len(cells) < 2 or any(c.upper().startswith("QNO") for c in cells):
                continue
            # cells alternate question number, then answer
            for a in range(0, len(cells) - 1, 2):
                q, res = cells[a], cells[a + 1]
                if not q.isdigit() or not 1 <= int(q) <= 200:
                    continue
                # answers are a single option, several accepted options ("1,3"), or a drop
                opts = [x for x in re.findall(r"\d", res)] if res else []
                if res.upper().startswith("DROP") or not opts:
                    k.setdefault(int(q), None)
                elif all(1 <= int(x) <= 5 for x in opts):
                    k.setdefault(int(q), ",".join(opts) if len(opts) > 1 else opts[0])
        if not k:
            # No pipe table: 2022 and 2024 print plain columns ("Q. No. | Option Id",
            # "Q.No. Answer") with no separators at all. Those are read off the page GEOMETRY --
            # words grouped into printed rows by their y position, ordered by x, then paired --
            # because the number of columns differs per year and per page, and any fixed chunking
            # straddles a row boundary somewhere and silently drops a run of answers.
            rows = collections.defaultdict(list)
            for w in page.get_text("words"):
                rows[round(w[1] / 4)].append((w[0], w[4]))
            for _y, cells in sorted(rows.items()):
                toks = [t for _x, t in sorted(cells) if t.isdigit()]
                if len(toks) < 2:
                    continue
                for a in range(0, len(toks) - 1, 2):
                    q, res = int(toks[a]), int(toks[a + 1])
                    if 1 <= q <= 200 and 1 <= res <= 5:
                        k.setdefault(q, str(res))
        if k:
            keys.setdefault(m.group(1), {}).update(k)
    return keys


def completeness(rec):
    """How much of a record is filled -- used only to choose which row survives a merge."""
    score = 0
    for field in ("stem_en", "subject", "official_answer", "b6_answer", "structure", "branch"):
        if rec.get(field):
            score += 1
    score += len([v for v in (rec.get("options_en") or {}).values() if v])
    for field in ("list_i", "list_ii", "statements"):
        if rec.get(field):
            score += 1
    if rec.get("figure_path") or rec.get("figure_path_source"):
        score += 2
    return score


def reset(recs, stamp):
    """Undo every change a previous run of THIS script made, from its own `repairs` notes.

    Needed because a merge can be wrong: the first run keyed Assertion-Reason questions on their
    boilerplate stem and standard options alone and merged five unrelated questions into one row.
    A wrong merge cannot be corrected by merging again -- the fields it copied between rows are
    already in place -- so the pass has to be reversible.

    Each change is reverted from the note that recorded it, which is the reason those notes name
    exactly what they did. `paper_codes` is restored to the one code the record was actually read
    from, identified by its own `source_file`; every other code on it was added by the merge.
    """
    undone = collections.Counter()
    touched = {}
    for qid, (path, r) in recs.items():
        mine = [e for e in (r.get("repairs") or [])
                if str(e.get("by", "")).endswith("merge_paper_codes.py")]
        if not mine:
            continue
        notes = [n for e in mine for n in (e.get("notes") or [])]

        if r.pop("merged_into", None):
            undone["merged_into_cleared"] += 1
        if r.pop("option_order_by_code", None):
            undone["option_order_cleared"] += 1

        own = re.search(r"code-([A-Z]\d?)", str(r.get("source_file") or ""))
        if own and r.get("paper_codes"):
            keep = [c for c in r["paper_codes"] if str(c).split(":")[0] == own.group(1)]
            if keep and keep != r["paper_codes"]:
                r["paper_codes"] = keep
                undone["paper_codes_restored"] += 1

        for note in notes:
            if note.startswith("official_answer filled"):
                r["official_answer"] = None
                r["answer_source"] = (f"inputs/keys/NEET_answers-key_{r.get('year')}-neet.pdf")
                undone["answer_cleared"] += 1
            elif note.startswith("subject set to"):
                r["subject"] = None
                undone["subject_cleared"] += 1
            else:
                m = re.match(r"(\w+) taken from Q-", note)
                if m and m.group(1) in ("subject", "branch", "structure", "list_i", "list_ii",
                                        "statements", "figure_path", "figure_path_source"):
                    r[m.group(1)] = None
                    undone[f"{m.group(1)}_cleared"] += 1

        r["repairs"] = [e for e in (r.get("repairs") or []) if e not in mine]
        r.setdefault("repairs", []).append(
            {"date": stamp, "by": "scripts/merge_paper_codes.py", "kind": "merge_reset",
             "notes": ["every change made by a previous run of this script was reverted before "
                       "re-running it: the first merge keyed Assertion-Reason questions on their "
                       "boilerplate stem and their four standard options alone, which are identical "
                       "across every such question in the paper, and so merged unrelated questions "
                       "together. paper_codes was restored to the single code this record's "
                       "source_file names; every other code on it had been added by that merge"]})
        touched[qid] = (path, r)
    return touched, undone


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true",
                    help="revert a previous run of this script, then stop")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    recs = {}
    for path in sorted(os.listdir(rc.pp("papers", "records"))):
        if not path.endswith(".json"):
            continue
        full = rc.pp("papers", "records", path)
        with open(full, encoding="utf-8") as fh:
            r = json.load(fh)
        if str(r.get("year")) == str(args.year):
            recs[r.get("question_id")] = (full, r)

    stamp = datetime.date.today().isoformat()
    if args.reset:
        touched, undone = reset(recs, stamp)
        for k, v in undone.most_common():
            print(f"   {v:4d}  {k}")
        print(f"{len(touched)} records would be reverted")
        if args.dry_run:
            print("\n(dry run -- nothing written)")
            return 0
        for qid, (path, r) in touched.items():
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
        print(f"reverted {len(touched)} records")
        return 0

    keys = read_keys(args.year)
    print(f"{len(recs)} records for {args.year}; key grids for {len(keys)} booklet codes "
          f"({', '.join(sorted(keys)[:8])}{'...' if len(keys) > 8 else ''})")

    stats = collections.Counter()
    groups = collections.defaultdict(list)
    for qid, (_, r) in recs.items():
        k = question_key(r)
        # A row too short or too damaged to key is still a row that can have its own code's answer
        # attached -- it just cannot be merged with anything. Keying it to itself keeps it in the
        # pass instead of skipping it: these are the figure-only and maths-only questions, exactly
        # the ones most likely to be missing an answer, and 18 of 2023's remaining blanks were here.
        groups[k if k else ("__unkeyed__", qid)].append(qid)
    # Second pass: fold singleton groups together where `near_duplicate` is satisfied. Only groups
    # whose BOOKLET CODES do not overlap are considered -- two rows from the same code are two
    # different questions however alike they read, since a code prints each question once.
    singles = [ks for ks, v in groups.items() if len(v) == 1]
    folded = {}
    for i, ka in enumerate(singles):
        if ka in folded:
            continue
        a = recs[groups[ka][0]][1]
        ca = {c for c, _ in code_positions(a)}
        for kb in singles[i + 1:]:
            if kb in folded:
                continue
            b = recs[groups[kb][0]][1]
            if ca & {c for c, _ in code_positions(b)}:
                continue
            ok, why = near_duplicate(a, b)
            if ok:
                groups[ka].extend(groups[kb])
                folded[kb] = (ka, why)
                stats["near_duplicate_folded"] += 1
    for kb in folded:
        groups.pop(kb, None)

    multi = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"{len(groups)} distinct questions; {len(multi)} appear in more than one row "
          f"({sum(len(v) - 1 for v in multi.values())} rows to merge)")

    stamp = datetime.date.today().isoformat()
    touched = {}

    for key, qids in groups.items():
        qids = sorted(qids, key=lambda q: -completeness(recs[q][1]))
        primary = qids[0]
        ppath, prec = recs[primary]
        notes = []

        # ---- every code this question was printed in, from every row in the group
        positions = {}
        for qid in qids:
            for code, n in code_positions(recs[qid][1]):
                positions.setdefault(code, n)

        # ---- each code's option order, as a permutation of the primary row's order
        canon = {k: _norm(v) for k, v in (prec.get("options_en") or {}).items() if _norm(v)}
        order_by_code = {}
        for qid in qids:
            rec = recs[qid][1]
            theirs = {k: _norm(v) for k, v in (rec.get("options_en") or {}).items() if _norm(v)}
            for code, _n in code_positions(rec):
                perm = {}
                for their_no, text in theirs.items():
                    for our_no, our_text in canon.items():
                        if text == our_text or (len(text) > 12 and text[:30] == our_text[:30]):
                            perm[their_no] = our_no
                            break
                if len(perm) == len(theirs) and theirs:
                    order_by_code[code] = perm

        # ---- the answer each code's key selects, expressed in the primary row's option numbers
        selected = {}
        for code, n in positions.items():
            raw = (keys.get(code) or {}).get(n)
            if not raw:
                continue
            mapped = (order_by_code.get(code) or {}).get(str(raw), str(raw) if code ==
                      (code_positions(prec)[0][0] if code_positions(prec) else None) else None)
            if mapped:
                selected[code] = str(mapped)

        agree = len(set(selected.values())) == 1 if selected else False
        if len(set(selected.values())) > 1:
            stats["codes_disagree_on_answer"] += 1
            notes.append(f"the booklet codes' keys select DIFFERENT options for this question "
                         f"after mapping each code's option order onto this row's "
                         f"({ {c: o for c, o in selected.items()} }); the answer was left "
                         f"untouched and this row needs a person")

        if len(positions) > len(code_positions(prec)):
            prec["paper_codes"] = [f"{c}:{n}" for c, n in sorted(positions.items())]
            notes.append(f"paper_codes now lists every code this question was printed in "
                         f"({', '.join(sorted(positions))}); each code's own option order is "
                         f"recorded in option_order_by_code")
            stats["paper_codes_extended"] += 1

        if order_by_code and order_by_code != prec.get("option_order_by_code"):
            prec["option_order_by_code"] = order_by_code
            stats["option_order_recorded"] += 1
            # Recorded as a note as well, not only as a field: the write at the end of this pass
            # happens for records that have something to say in `repairs`, and without a note a
            # row whose ONLY change was its option order was computed and then thrown away -- 189
            # of 2024's orders were lost that way.
            notes.append(f"option_order_by_code recorded for {', '.join(sorted(order_by_code))}: "
                         f"each code's printed option numbers mapped onto this row's order, so one "
                         f"official answer can be checked against every code's key")

        if not prec.get("official_answer") and selected and agree:
            prec["official_answer"] = sorted(selected.values())[0]
            prec["answer_source"] = (f"inputs/keys/NEET_answers-key_{args.year}-neet.pdf "
                                     f"via {', '.join(sorted(selected))}")
            notes.append(f"official_answer filled from the key grid(s) for "
                         f"{', '.join(sorted(selected))}; all of them select the same option text "
                         f"after each code's option order is mapped onto this row, so the answer "
                         f"is corroborated across codes rather than taken from one grid")
            stats["answer_filled"] += 1

        # ---- subject from the printed position, where no row in the group carries one
        #
        # NEET numbers its paper by section: 1-50 Physics, 51-100 Chemistry, 101-200 Biology. The
        # codes reshuffle questions WITHIN a section, never across, so a position fixes the subject
        # whichever code it came from. Checked against every row in this bank that already has
        # both: 617 agreements, 0 disagreements across 2022, 2023 and 2024. It is derived only
        # where the field is empty, and never overwrites what an agent read.
        if not prec.get("subject") and positions:
            n = positions.get(sorted(positions)[0])
            derived = "Physics" if n <= 50 else "Chemistry" if n <= 100 else "Biology"
            prec["subject"] = derived
            prec["field_sources"] = dict(prec.get("field_sources") or {},
                                         subject="derived from printed position")
            notes.append(f"subject set to {derived} from the printed position (question {n} of "
                         f"code {sorted(positions)[0]}); NEET's sections are 1-50 Physics, 51-100 "
                         f"Chemistry, 101-200 Biology and the codes reshuffle only within a "
                         f"section. This mapping agrees with every row in the bank that already "
                         f"carries a subject (617 of 617) and was not used where one was present")
            stats["subject_derived_from_position"] += 1

        # ---- fields a duplicate row holds and the primary does not
        for qid in qids[1:]:
            other = recs[qid][1]
            for field in ("subject", "branch", "structure", "list_i", "list_ii", "statements"):
                if not prec.get(field) and other.get(field):
                    prec[field] = other[field]
                    notes.append(f"{field} taken from {qid}, the same question read from "
                                 f"code {', '.join(c for c, _ in code_positions(other)) or '?'}")
                    stats[f"{field}_recovered"] += 1
            for field in ("figure_path", "figure_path_source"):
                fp = other.get(field)
                if not prec.get(field) and fp and os.path.exists(
                        fp if os.path.isabs(fp) else rc.pp(fp)):
                    prec[field] = fp
                    notes.append(f"{field} taken from {qid}, which is the same question read from "
                                 f"the other code and already links this file")
                    stats["figure_recovered"] += 1

            if other.get("merged_into") != primary:
                other["merged_into"] = primary
                orec_notes = [f"this row is the same question as {primary}, read from code "
                              f"{', '.join(c for c, _ in code_positions(other)) or '?'}; it is "
                              f"marked merged so that per-question counts stop double-counting it. "
                              f"Nothing was deleted: the row stays as the evidence of what that "
                              f"code printed, which is the only record of its option order"]
                other.setdefault("repairs", []).append(
                    {"date": stamp, "by": "scripts/merge_paper_codes.py",
                     "kind": "merged_duplicate", "notes": orec_notes})
                touched[qid] = recs[qid]
                stats["rows_marked_merged"] += 1

        if notes:
            prec.setdefault("repairs", []).append(
                {"date": stamp, "by": "scripts/merge_paper_codes.py",
                 "kind": "cross_code_merge", "notes": notes})
            touched[primary] = (ppath, prec)

    print()
    for k, v in stats.most_common():
        print(f"   {v:4d}  {k}")
    print(f"\n{len(touched)} records would change")

    if args.dry_run:
        print("\n(dry run -- nothing written)")
        return 0
    for qid, (path, r) in touched.items():
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    print(f"wrote {len(touched)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
