#!/usr/bin/env python3
"""F5 · Release and export (spec Section 14/F5, Section 6.6, CLAUDE.md rule 12).

THE ONLY PATH BY WHICH ANYTHING IS RELEASED. Nothing else in this repository may write to
`data/`, and this script writes a chapter's rows only when EVERY gate condition below holds. It
refuses loudly and by default; there is no flag, environment variable or argument that skips the
sign-off requirement.

    python3 scripts/export_tables.py --gate-report          # show every chapter's gate status
    python3 scripts/export_tables.py --chapters BIO12-CH01  # release that chapter, if it qualifies
    python3 scripts/export_tables.py --all-eligible         # release every chapter that qualifies

The gate (spec 14/F5). A chapter is released when ALL of these hold:
  1. its review queue is empty — no open flag maps to the chapter, and every audit-sample item
     and draft item for it has been decided;
  2. its subtopic list is approved — review/approvals.jsonl has an `approve` for
     `subtopic_list:<CHAPTER>`;
  3. every change-log row for it is approved — an `approve` for each `change_log_row:<CL-ID>`;
  4. its audit sample meets the target — every sampled item decided, and the approve rate at or
     above --audit-target (default 0.95);
  5. a real sign-off row exists in review/releases.csv — naming the chapter, with a non-empty
     `signed_by` and `released_at`;
  6. nothing in it is blocked by a reviewer — no question with
     `release_status = blocked_by_reviewer`, no block on the chapter in review/blocks.jsonl.

Writes `data/questions.csv` (Layer 1), `data/ncert_links.csv` (Layer 2, one row per
question-subtopic), `data/tags.csv` (Layer 3) and `data/subtopic_stats.csv` (Layer 4, straight
from F4's output — never recomputed here and never typed), plus `data/_release_log.jsonl`
recording which chapter was released, by whom, against which sign-off row.
"""
import argparse
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import compute_counts  # noqa: E402
import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import records as lib_records  # noqa: E402

DATA_DIR = fc.pp("data")
QUESTIONS_PATH = os.path.join(DATA_DIR, "questions.csv")
LINKS_PATH = os.path.join(DATA_DIR, "ncert_links.csv")
TAGS_PATH = os.path.join(DATA_DIR, "tags.csv")
SUBTOPIC_STATS_PATH = os.path.join(DATA_DIR, "subtopic_stats.csv")
RELEASE_LOG_PATH = os.path.join(DATA_DIR, "_release_log.jsonl")

DEFAULT_AUDIT_TARGET = 0.95  # the lowest content target in spec 1.1 (subtopic correct >= 95%)

# Layer 1 (spec 3.2): text, options, figures, official answer, status, source, booklet codes,
# repeat links. Columns are the record's own field names (spec 6.3) plus review_status (6.6).
QUESTION_COLUMNS = [
    "question_id", "exam", "year", "sitting", "paper_codes", "option_map",
    "subject", "branch", "stem_en", "statements", "list_i", "list_ii", "options_en",
    "option_images", "structure", "negative_words", "has_figure", "figure_file",
    "official_answer", "answer_source", "status", "issue_reason", "corrected_answer",
    "corrected_stem", "latest_answer", "answer_changed", "change_note",
    "trust", "source_file", "source_page",
    "repeat_group_id", "repeat_label", "related_ids",
    "review_status", "release_status", "released_at",
]

# Layer 2 (spec 6.6): one row per question-subtopic.
LINK_COLUMNS = [
    "question_id", "chapter_id", "subtopic_id", "link_type", "evidence",
    "derivation_steps", "covers", "older_evidence", "syllabus_status", "note_type",
    "reason_note", "change_ids", "fact_line", "review_status",
]

# Layer 3 (spec 3.2): E1-E6 values and the codebook version.
TAG_COLUMNS = [
    "question_id", "question_type", "format", "content_shape", "category_primary",
    "category_secondary", "category_why", "option_traps", "stem_context", "answer_form",
    "negation", "item_count", "constants_given", "figure_role", "descriptive_tags",
    "codebook_version", "legacy_chapter", "legacy_topic", "legacy_question_type",
    "explanation_source", "review_status",
]

# Layer 4 (spec 14/F4): per-subtopic statistics, both populations.
SUBTOPIC_STAT_COLUMNS = [
    "subtopic_id", "chapter_id", "population",
    "questions_total", "unique_questions", "years_asked", "last_asked",
    "repeat_groups", "repeat_group_count",
    "category_mix_recent", "format_mix_recent", "question_type_mix_recent", "recent_since",
    "computed_at",
]


def _cell(value):
    """One CSV cell. Lists and dicts are stored as compact JSON so a released table round-trips
    back to the record's value exactly; None becomes empty."""
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


# --------------------------------------------------------------------------------------------
# The gate
# --------------------------------------------------------------------------------------------

def _chapter_questions(chapter_id, records):
    return sorted(q for q, r in records.items() if chapter_id in fc.record_chapter_ids(r))


def _decided_targets(decisions):
    """{target: decision} from review/decisions.csv, latest row winning."""
    out = {}
    for row in decisions:
        t = (row.get("flag_id_or_item") or "").strip()
        d = (row.get("decision") or "").strip().lower()
        if t and d in fc.DECISION_VALUES:
            out[t] = d
    return out


def gate(chapter_id, records=None, audit_target=DEFAULT_AUDIT_TARGET):
    """Evaluate every gate condition for one chapter. Returns a report; `report["ok"]` is True
    only when every condition passed."""
    records = fc.canonical_records() if records is None else records
    index = fc.qid_index()
    approvals = fc.approval_index()
    decisions = fc.read_decisions()
    decided = _decided_targets(decisions)
    qids = _chapter_questions(chapter_id, records)

    conditions = []

    # 1 · queue empty -------------------------------------------------------------------------
    open_for_chapter = [f for f in fc.open_flags()
                        if chapter_id in fc.item_chapter_ids(f.get("item_id"), records, index)]
    conditions.append({
        "id": "queue_empty",
        "requirement": "no open flag maps to this chapter (spec 14/F5 'its queue is empty')",
        "ok": not open_for_chapter,
        "detail": (f"{len(open_for_chapter)} open flag(s): "
                   + ", ".join(f"{f['flag_id']}/{f['code']}" for f in open_for_chapter[:10])
                   + ("..." if len(open_for_chapter) > 10 else "")) if open_for_chapter
                  else "no open flags",
    })

    # 2 · subtopic list approved --------------------------------------------------------------
    st_target = fc.subtopic_list_target(chapter_id)
    st_approved = (approvals.get(st_target) or {}).get("decision") == "approve"
    drafts = {d["chapter_id"] for d in fc.subtopic_list_drafts()}
    conditions.append({
        "id": "subtopic_list_approved",
        "requirement": f"review/approvals.jsonl has an `approve` for {st_target}",
        "ok": st_approved,
        "detail": ("approved by " + str((approvals.get(st_target) or {}).get("reviewer"))
                   if st_approved else
                   ("not approved" if chapter_id in drafts else
                    f"no ncert/subtopics/{chapter_id}.json exists at all — there is no subtopic "
                    f"list to approve, so this chapter cannot be released")),
    })

    # 3 · change-log rows approved ------------------------------------------------------------
    rows = [r for r in fc.change_log_rows() if (r.get("chapter_id") or "").strip() == chapter_id]
    unapproved = [r.get("change_id") for r in rows
                  if (approvals.get(fc.change_log_target(r.get("change_id"))) or {}).get("decision")
                  != "approve"]
    conditions.append({
        "id": "change_log_rows_approved",
        "requirement": "every ncert/change_log.csv row for this chapter is approved",
        "ok": not unapproved,
        "detail": (f"{len(unapproved)} unapproved: {', '.join(map(str, unapproved[:10]))}"
                   if unapproved else f"{len(rows)} change-log row(s), all approved"),
    })

    # 4 · audit sample meets target -----------------------------------------------------------
    audit_rows = [r for r in lib_io.read_jsonl(fc.pp("review", "audit_sample.jsonl"))
                  if chapter_id in (r.get("chapter_ids") or [])]
    undecided = [r["pack_id"] for r in audit_rows if r["pack_id"] not in decided]
    outcomes = [decided[r["pack_id"]] for r in audit_rows if r["pack_id"] in decided]
    approve_rate = (outcomes.count("approve") / len(outcomes)) if outcomes else None
    audit_ok = (not undecided) and (approve_rate is None or approve_rate >= audit_target)
    if audit_rows and not outcomes:
        audit_detail = f"{len(audit_rows)} sampled item(s), none decided yet"
    elif not audit_rows:
        audit_detail = ("no audit-sample item for this chapter in review/audit_sample.jsonl "
                        "(run build_review_pack.py first; a chapter with nothing sampled passes "
                        "this condition trivially)")
    else:
        audit_detail = (f"{len(outcomes)}/{len(audit_rows)} decided, approve rate "
                        f"{approve_rate:.0%} vs target {audit_target:.0%}"
                        + (f", {len(undecided)} still undecided" if undecided else ""))
    conditions.append({
        "id": "audit_sample_meets_target",
        "requirement": f"every audit-sample item decided and approve rate >= {audit_target:.0%}",
        "ok": audit_ok,
        "detail": audit_detail,
    })

    # 5 · sign-off ----------------------------------------------------------------------------
    signoff = fc.signoff_for(chapter_id)
    conditions.append({
        "id": "signoff_row",
        "requirement": ("a row in review/releases.csv for this chapter with a non-empty "
                        "`signed_by` and `released_at` (CLAUDE.md: never release a chapter; only "
                        "export_tables.py does, after a sign-off row in review/releases.csv)"),
        "ok": signoff is not None,
        "detail": (f"signed by {signoff.get('signed_by')!r} at {signoff.get('released_at')!r}"
                   if signoff else "no valid sign-off row"),
    })

    # 6 · nothing blocked ---------------------------------------------------------------------
    blocked_q = [q for q in qids
                 if (records[q].get("release_status") or "") == "blocked_by_reviewer"]
    chapter_blocked = chapter_id in fc.blocked_chapters()
    conditions.append({
        "id": "nothing_blocked",
        "requirement": "no question blocked by a reviewer and no block on the chapter itself",
        "ok": not blocked_q and not chapter_blocked,
        "detail": (("chapter itself is blocked; " if chapter_blocked else "")
                   + (f"{len(blocked_q)} blocked question(s): {', '.join(blocked_q[:10])}"
                      if blocked_q else "nothing blocked")),
    })

    return {
        "chapter_id": chapter_id,
        "ok": all(c["ok"] for c in conditions),
        "conditions": conditions,
        "questions": qids,
        "signoff": signoff,
        "audit_target": audit_target,
    }


def known_chapters(records=None):
    """Every chapter the pipeline knows about: those with a subtopic list, those a question cites,
    and those named in the change log."""
    records = fc.canonical_records() if records is None else records
    chs = {d["chapter_id"] for d in fc.subtopic_list_drafts()}
    for rec in records.values():
        chs |= set(fc.record_chapter_ids(rec))
    for row in fc.change_log_rows():
        if (row.get("chapter_id") or "").strip():
            chs.add(row["chapter_id"].strip())
    return sorted(c for c in chs if c)


# --------------------------------------------------------------------------------------------
# Export
# --------------------------------------------------------------------------------------------

def _existing(path, key_columns):
    """Rows already in a data/ table, keyed so a re-export of one chapter replaces only its own
    rows and leaves every other released chapter untouched."""
    rows = lib_io.read_csv(path)
    return {tuple(r.get(k, "") for k in key_columns): r for r in rows}


def export_chapter(chapter_id, report, records, counts, dry_run=False):
    """Write one qualifying chapter's released rows into data/. Called only after gate() passed."""
    qids = report["questions"]
    written = {"questions": 0, "links": 0, "tags": 0, "subtopic_stats": 0}
    released_at = (report["signoff"] or {}).get("released_at") or fc.today_iso()

    q_rows = _existing(QUESTIONS_PATH, ["question_id"])
    l_rows = _existing(LINKS_PATH, ["question_id", "subtopic_id"])
    t_rows = _existing(TAGS_PATH, ["question_id"])
    s_rows = _existing(SUBTOPIC_STATS_PATH, ["subtopic_id", "population"])

    for qid in qids:
        rec = records[qid]
        base = {"review_status": rec.get("review_status") or "pending",
                "release_status": "released", "released_at": released_at}
        q_rows[(qid,)] = {c: _cell(base.get(c, rec.get(c))) for c in QUESTION_COLUMNS}
        q_rows[(qid,)]["question_id"] = qid
        t_rows[(qid,)] = {c: _cell(base.get(c, rec.get(c))) for c in TAG_COLUMNS}
        t_rows[(qid,)]["question_id"] = qid
        written["questions"] += 1
        written["tags"] += 1
        for st in fc.record_subtopic_ids(rec):
            row = {c: _cell(rec.get(c)) for c in LINK_COLUMNS}
            row.update({"question_id": qid, "subtopic_id": st,
                        "chapter_id": st.rsplit("-ST", 1)[0] if "-ST" in st else chapter_id,
                        "review_status": _cell(rec.get("review_status") or "pending")})
            l_rows[(qid, st)] = row
            written["links"] += 1

    for st, data in (counts or {}).get("subtopics", {}).items():
        if data.get("chapter_id") != chapter_id:
            continue
        for population in ("all", "released_only"):
            stats = data[population]
            row = {
                "subtopic_id": st, "chapter_id": data.get("chapter_id"),
                "population": population, "computed_at": data.get("computed_at"),
            }
            for c in SUBTOPIC_STAT_COLUMNS:
                if c in row:
                    continue
                row[c] = _cell(stats.get(c))
            s_rows[(st, population)] = row
            written["subtopic_stats"] += 1

    if dry_run:
        return written

    os.makedirs(DATA_DIR, exist_ok=True)
    lib_io.write_csv(QUESTIONS_PATH, [q_rows[k] for k in sorted(q_rows)], QUESTION_COLUMNS)
    lib_io.write_csv(LINKS_PATH, [l_rows[k] for k in sorted(l_rows)], LINK_COLUMNS)
    lib_io.write_csv(TAGS_PATH, [t_rows[k] for k in sorted(t_rows)], TAG_COLUMNS)
    lib_io.write_csv(SUBTOPIC_STATS_PATH, [s_rows[k] for k in sorted(s_rows)],
                     SUBTOPIC_STAT_COLUMNS)

    # Mark the questions released, so F4's released-only counts and any later re-export agree
    # with what data/ actually holds.
    for qid in qids:
        rec = lib_records.read_record(qid)
        rec["question_id"] = qid
        rec["release_status"] = "released"
        rec["released_at"] = released_at
        sources = rec.setdefault("field_sources", {})
        sources["release_status"] = {
            "step": "F5", "prompt_version": "v1", "status": "released",
            "signed_by": (report["signoff"] or {}).get("signed_by"),
            "released_at": released_at,
        }
        lib_io.atomic_write_json(lib_records.record_path(qid), rec)

    lib_io.append_jsonl(RELEASE_LOG_PATH, {
        "at": fc.now_iso(), "chapter_id": chapter_id,
        "signed_by": (report["signoff"] or {}).get("signed_by"),
        "released_at": released_at,
        "gold_score_snapshot": (report["signoff"] or {}).get("gold_score_snapshot"),
        "open_flags_at_signoff": (report["signoff"] or {}).get("open_flags"),
        "audit_target_used": report["audit_target"],
        "questions": qids, "written": written,
        "gate": [{"id": c["id"], "ok": c["ok"], "detail": c["detail"]}
                 for c in report["conditions"]],
    })
    return written


def print_gate(report):
    mark = "PASS" if report["ok"] else "REFUSED"
    print(f"{report['chapter_id']}: {mark}")
    for c in report["conditions"]:
        print(f"    [{'ok ' if c['ok'] else 'NO '}] {c['id']}: {c['detail']}")
        if not c["ok"]:
            print(f"           needs: {c['requirement']}")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="F5 · release and export (spec 14/F5). The only writer of data/.")
    ap.add_argument("--chapters", help="Comma-separated chapter ids to release.")
    ap.add_argument("--all-eligible", action="store_true",
                    help="Release every chapter that passes the gate.")
    ap.add_argument("--gate-report", action="store_true",
                    help="Print each chapter's gate status and exit; write nothing.")
    ap.add_argument("--audit-target", type=float, default=DEFAULT_AUDIT_TARGET,
                    help=f"Minimum audit-sample approve rate (default {DEFAULT_AUDIT_TARGET}).")
    ap.add_argument("--dry-run", action="store_true",
                    help="Evaluate the gate and count what would be written; write nothing.")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if not 0 < args.audit_target <= 1:
        print("--audit-target must be greater than 0 and at most 1.", file=sys.stderr)
        return 2

    records = fc.canonical_records()
    requested = fc.parse_list_arg(args.chapters)

    if args.gate_report or (not requested and not args.all_eligible):
        chapters = requested or known_chapters(records)
        reports = [gate(c, records, args.audit_target) for c in chapters]
        if args.json:
            print(json.dumps(reports, indent=2))
            return 0
        print("F5 release gate (spec 14/F5). Nothing is being written.")
        if not chapters:
            print("  no chapters known yet.")
        for r in reports:
            print_gate(r)
        eligible = [r["chapter_id"] for r in reports if r["ok"]]
        print(f"\n  eligible for release: {', '.join(eligible) if eligible else 'none'}")
        if not args.gate_report:
            print("  (no --chapters given, so this was a gate report. Pass "
                  "--chapters <ID> to release one, or --all-eligible.)")
        return 0

    chapters = requested or [c for c in known_chapters(records)
                             if gate(c, records, args.audit_target)["ok"]]
    counts = compute_counts.load_counts()
    if counts is None:
        print("REFUSED: steps/F4/out/_all.json does not exist — F4 has not computed the counts. "
              "Run `python3 scripts/compute_counts.py` first; Layer 4 must be computed, never "
              "typed (spec 14/F4).", file=sys.stderr)
        return 2

    results, refused = [], []
    for chapter_id in chapters:
        report = gate(chapter_id, records, args.audit_target)
        if not report["ok"]:
            refused.append(report)
            continue
        written = export_chapter(chapter_id, report, records, counts, dry_run=args.dry_run)
        results.append({"chapter_id": chapter_id, "written": written,
                        "signed_by": (report["signoff"] or {}).get("signed_by")})

    if args.json:
        print(json.dumps({"released": results,
                          "refused": [{"chapter_id": r["chapter_id"],
                                       "failed": [c["id"] for c in r["conditions"] if not c["ok"]]}
                                      for r in refused],
                          "dry_run": args.dry_run}, indent=2))
        return 1 if refused else 0

    for r in results:
        print(f"RELEASED {r['chapter_id']} (signed by {r['signed_by']!r}): "
              f"{r['written']['questions']} question(s), {r['written']['links']} link(s), "
              f"{r['written']['tags']} tag row(s), {r['written']['subtopic_stats']} subtopic "
              f"stat row(s)" + (" [dry run: nothing written]" if args.dry_run else ""))
    for r in refused:
        print(f"\nREFUSED to release {r['chapter_id']} — the release gate is not satisfied:")
        print_gate(r)
    if refused:
        print("\nNo part of a refused chapter was written. There is no override: fix the "
              "conditions above (and get a sign-off row into review/releases.csv) and run again.")
        return 1
    if not results:
        print("Nothing to release.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
