#!/usr/bin/env python3
"""F4 · Compute the counts (spec Section 14/F4).

    python3 scripts/compute_counts.py
    python3 scripts/compute_counts.py --chapters BIO12-CH01
    python3 scripts/compute_counts.py --dry-run
    python3 scripts/compute_counts.py --json

Per subtopic, computed twice — over ALL questions and over RELEASED questions only:
  unique_questions          each repeat group counted once
  questions_total           every question-subtopic link
  years_asked               the distinct years, sorted
  last_asked                the most recent year
  category_mix_recent       primary thinking category, questions since 2021
  format_mix_recent         format, questions since 2021
  question_type_mix_recent  question type, questions since 2021
  repeat_groups             the repeat groups with 2 or more members in this subtopic

SELF-CHECK (spec 14/F4, and rule 3 of the Stage F brief): the sum of `questions_total` across
every subtopic MUST equal the number of question-subtopic links counted independently from the
records. If it does not, this script writes nothing and exits non-zero. Nothing here types a
count; every number is a len() or a max() over the records.

Writes steps/F4/out/<SUBTOPIC>.json plus steps/F4/out/_all.json. It does NOT write to data/ —
only export_tables.py may (spec 6.6), and only for a chapter that has passed the release gate.
"""
import argparse
import collections
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402

RECENT_SINCE = 2021  # spec 14/F4: "primary thinking since 2021"
OUT_DIR = fc.pp("steps", "F4", "out")
ALL_PATH = os.path.join(OUT_DIR, "_all.json")

MIX_FIELDS = {
    "category_mix_recent": "category_primary",
    "format_mix_recent": "format",
    "question_type_mix_recent": "question_type",
}


class CountMismatch(Exception):
    """The self-check failed. Raised, never swallowed — a wrong count is worse than no count."""


def question_subtopic_links(records):
    """Every question-subtopic link as a sorted list of (qid, subtopic_id) pairs.

    This is the independent denominator the self-check compares against, so it is deliberately
    computed straight off the records and shares no code with the per-subtopic aggregation. Each
    (question, subtopic) pair counts once even if a record lists the same subtopic twice — a
    duplicate in one record is a data defect, not two links, and counting it twice would make the
    subtopic look busier than it is."""
    links = set()
    for qid, rec in sorted(records.items()):
        for st in fc.record_subtopic_ids(rec):
            links.add((qid, st))
    return sorted(links)


def _released(rec):
    return (rec.get("release_status") or "unreleased") == "released"


def _repeat_key(qid, rec):
    """What "counted once" means for unique_questions: a question's repeat group if it has one,
    otherwise the question itself. Two questions in RG-0042 are one unique question; a question
    with no group is its own."""
    return rec.get("repeat_group_id") or f"__solo__{qid}"


def _mix_key(value):
    """One key of a mix. A tag is normally a single string, but a Stage F correction can legally
    put a list or an object there (a reviewer may decide a question has two thinking categories),
    and an unhashable value must not crash the counts — it is rendered as compact JSON so it is
    still visible and still distinct."""
    if value is None or value == "":
        return "(untagged)"
    if isinstance(value, (list, dict, set, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _mix(qids, records, field):
    """A {value: count} mix over recent questions. Questions with no value for the field are
    counted under the key "(untagged)" rather than dropped, so the mix always sums to the number
    of recent questions and a half-tagged subtopic is visibly half-tagged."""
    counter = collections.Counter()
    for qid in qids:
        rec = records[qid]
        year = rec.get("year")
        if not isinstance(year, int) or year < RECENT_SINCE:
            continue
        counter[_mix_key(rec.get(field))] += 1
    return dict(sorted(counter.items(), key=lambda kv: (-kv[1], str(kv[0]))))


def _stats_for(qids, records):
    """Every per-subtopic number, for one population of questions (all, or released only)."""
    years = sorted({records[q].get("year") for q in qids
                    if isinstance(records[q].get("year"), int)})
    groups = collections.Counter()
    for q in qids:
        gid = records[q].get("repeat_group_id")
        if gid:
            groups[gid] += 1
    stats = {
        "questions_total": len(qids),
        "unique_questions": len({_repeat_key(q, records[q]) for q in qids}),
        "years_asked": years,
        "last_asked": years[-1] if years else None,
        "repeat_groups": sorted(g for g, n in groups.items() if n >= 2),
        "repeat_group_count": sum(1 for _, n in groups.items() if n >= 2),
        "question_ids": sorted(qids),
    }
    for out_key, field in MIX_FIELDS.items():
        stats[out_key] = _mix(qids, records, field)
    stats["recent_since"] = RECENT_SINCE
    return stats


def compute(chapters=None, records=None):
    """Compute every subtopic's counts and run the self-check. Raises CountMismatch on failure."""
    records = fc.canonical_records() if records is None else records

    # The aggregation builds its own index here, straight from the records, and
    # `question_subtopic_links()` counts the links in a SEPARATE pass. The self-check below then
    # compares two independently derived numbers. That separation is the whole point: if the two
    # shared one list, the check would only be comparing a list with itself and would pass no
    # matter how wrong either side was.
    by_subtopic = collections.defaultdict(list)
    for qid in sorted(records):
        seen = set()
        for st in fc.record_subtopic_ids(records[qid]):
            if st in seen:
                continue
            seen.add(st)
            by_subtopic[st].append(qid)

    # Every subtopic that EXISTS, not only those with questions: a subtopic with no past question
    # is a real and useful answer for the test generator ("nothing has ever been asked here"),
    # and leaving it out would silently hide it.
    known_subtopics = set(by_subtopic)
    for draft in fc.subtopic_list_drafts():
        for st in draft["subtopics"]:
            sid = (st or {}).get("subtopic_id")
            if sid:
                known_subtopics.add(sid)

    chapter_filter = set(chapters) if chapters else None
    out = {}
    for st in sorted(known_subtopics):
        chapter_id = st.rsplit("-ST", 1)[0] if "-ST" in st else None
        if chapter_filter is not None and chapter_id not in chapter_filter:
            continue
        qids = sorted(by_subtopic.get(st, []))
        released = [q for q in qids if _released(records[q])]
        out[st] = {
            "subtopic_id": st,
            "chapter_id": chapter_id,
            "computed_at": fc.now_iso(),
            "all": _stats_for(qids, records),
            "released_only": _stats_for(released, records),
        }

    # ---- the self-check (spec 14/F4) -------------------------------------------------------
    # Compared over the SAME scope that was computed, so a --chapters run checks its own slice.
    links = question_subtopic_links(records)
    unknown = sorted({q for q, _ in links if q not in records})
    if unknown:
        raise CountMismatch(
            f"F4 self-check FAILED: {len(unknown)} question-subtopic link(s) name a question with "
            f"no canonical record: {', '.join(unknown[:10])}"
            + ("..." if len(unknown) > 10 else "")
            + ". Nothing was written — fix the cause, never the count.")
    in_scope_links = [(q, s) for q, s in links
                      if chapter_filter is None
                      or (s.rsplit("-ST", 1)[0] if "-ST" in s else None) in chapter_filter]
    total_from_subtopics = sum(v["all"]["questions_total"] for v in out.values())
    if total_from_subtopics != len(in_scope_links):
        raise CountMismatch(
            f"F4 self-check FAILED: the subtopic totals sum to {total_from_subtopics} but there "
            f"are {len(in_scope_links)} question-subtopic links in the same scope. Nothing was "
            f"written. This means the aggregation and the records disagree — fix the cause, never "
            f"the count."
        )
    released_links = [(q, s) for q, s in in_scope_links if _released(records[q])]
    total_released = sum(v["released_only"]["questions_total"] for v in out.values())
    if total_released != len(released_links):
        raise CountMismatch(
            f"F4 self-check FAILED (released-only): the subtopic totals sum to {total_released} "
            f"but there are {len(released_links)} released question-subtopic links. Nothing was "
            f"written."
        )

    summary = {
        "computed_at": fc.now_iso(),
        "chapters": sorted(chapter_filter) if chapter_filter else None,
        "subtopics": len(out),
        "subtopics_with_questions": sum(1 for v in out.values() if v["all"]["questions_total"]),
        "question_subtopic_links": len(in_scope_links),
        "released_question_subtopic_links": len(released_links),
        "questions_considered": len(records),
        "self_check": {
            "links_counted_independently": len(in_scope_links),
            "sum_of_subtopic_totals": total_from_subtopics,
            "released_links_counted_independently": len(released_links),
            "sum_of_released_subtopic_totals": total_released,
            "passed": True,
        },
        "recent_since": RECENT_SINCE,
    }
    return summary, out


def write(summary, per_subtopic):
    os.makedirs(OUT_DIR, exist_ok=True)
    for st, data in per_subtopic.items():
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in st)
        lib_io.atomic_write_json(os.path.join(OUT_DIR, f"{safe}.json"), data)
    lib_io.atomic_write_json(ALL_PATH, {"summary": summary, "subtopics": per_subtopic})


def load_counts():
    """steps/F4/out/_all.json, for export_tables.py. Returns None if F4 has not run."""
    if not os.path.exists(ALL_PATH):
        return None
    try:
        with open(ALL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def main(argv=None):
    ap = argparse.ArgumentParser(description="F4 · compute the counts (spec 14/F4).")
    ap.add_argument("--chapters", help="Comma-separated chapter ids to scope to.")
    ap.add_argument("--dry-run", action="store_true", help="Compute and self-check; write nothing.")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    try:
        summary, per_subtopic = compute(chapters=fc.parse_list_arg(args.chapters))
    except CountMismatch as e:
        print(str(e), file=sys.stderr)
        return 2

    if not args.dry_run:
        write(summary, per_subtopic)

    if args.json:
        print(json.dumps({"summary": summary, "subtopics": per_subtopic}, indent=2))
        return 0

    print("F4 compute_counts")
    print(f"  subtopics                      : {summary['subtopics']} "
          f"({summary['subtopics_with_questions']} with at least one question)")
    print(f"  question-subtopic links        : {summary['question_subtopic_links']}")
    print(f"  released links                 : {summary['released_question_subtopic_links']}")
    print(f"  self-check                     : PASSED "
          f"({summary['self_check']['sum_of_subtopic_totals']} == "
          f"{summary['self_check']['links_counted_independently']})")
    with_q = [(st, v) for st, v in sorted(per_subtopic.items()) if v["all"]["questions_total"]]
    for st, v in with_q[:40]:
        a = v["all"]
        print(f"    {st:24s} total={a['questions_total']:4d} unique={a['unique_questions']:4d} "
              f"years={a['years_asked']} last={a['last_asked']} groups={a['repeat_group_count']}")
    if len(with_q) > 40:
        print(f"    ... and {len(with_q) - 40} more")
    if not args.dry_run:
        print(f"  written                        : {os.path.relpath(ALL_PATH, fc.PROJECT_ROOT)} "
              f"(+ one file per subtopic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
