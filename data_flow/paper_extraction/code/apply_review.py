#!/usr/bin/env python3
"""F3 · Apply decisions and run the cascade (spec Section 14/F3).

    python3 scripts/apply_review.py                  # dry run: say what would happen
    python3 scripts/apply_review.py --apply          # apply decisions, mark the cascade stale
    python3 scripts/apply_review.py --apply --run    # ... and re-run the script-only stale steps
    python3 scripts/apply_review.py --apply --rebuild-pack   # ... then F1 --new-only

Procedure (spec 14/F3):
  1. Read NEW rows of review/decisions.csv (rows already applied are remembered by digest in
     review/applied_decisions.jsonl, so running this twice does nothing the second time).
  2. approve → close the flag; set the value's status `approved`, with reviewer and date.
  3. correct / edit → write the new value as an output of step F2 for that item (history),
     update the record, append to review/corrections.jsonl, close the flag, call the cascade.
  4. block → release_status = blocked_by_reviewer.
  5. Cascade: mark the reading steps stale for the affected items, follow transitively, re-run in
     stage order. An unchanged re-run raises no flag; flags that no longer apply become
     `auto_closed`. (All of that lives in cascade.py.)
  6. Rebuild the pack with --new-only.

Two rules this file exists to keep:
  * **Never edit an agent's output.** A correction is a NEW file under steps/F2/out/ plus a
    record update. The original step's output file is never touched, so the history of what the
    agent actually said survives the correction.
  * **Approvals never rewrite an agent's file either.** They go to review/approvals.jsonl, which
    is what F5's release gate reads (see f_common.load_approvals for the full reasoning).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import cascade  # noqa: E402
import f_common as fc  # noqa: E402
from lib import io as lib_io  # noqa: E402
from lib import records as lib_records  # noqa: E402

F2_STEP = "F2"
F2_OUT_DIR = fc.pp("steps", F2_STEP, "out")
F2_PROMPT_VERSION_PATH = fc.pp("steps", F2_STEP, "prompt_version.txt")


def f2_prompt_version():
    """F2's "prompt version" is the reviewer process version. There is no agent prompt, but spec
    5.9 wants every output attributed to one, and field_sources entries need a value."""
    if os.path.exists(F2_PROMPT_VERSION_PATH):
        with open(F2_PROMPT_VERSION_PATH, "r", encoding="utf-8") as f:
            return f.read().strip() or "v1"
    return "v1"


# --------------------------------------------------------------------------------------------
# Resolving a decisions.csv row to a real target
# --------------------------------------------------------------------------------------------

class Unresolvable(Exception):
    pass


def resolve_target(row, flags_by_id, records):
    """What one decisions.csv row is about.

    `flag_id_or_item` is either a flag id (`FL-000123`), a pack pseudo-id for a draft
    (`subtopic_list:BIO12-CH01`, `change_log_row:CL-0014`), an audit-sample pack id
    (`audit:D4:Q-000015`), an E4 agreement pack id (`e4_agreement:Q-000015`), or a bare item id
    (a QID / chapter id — spec 14/F2 lets a reviewer edit any field of any item "even if it
    passed", which has no flag behind it at all).

    Returns {kind, flag, item_id, chapter_ids, field}."""
    raw = (row.get("flag_id_or_item") or "").strip()
    if not raw:
        raise Unresolvable("empty flag_id_or_item")
    field = (row.get("field") or "").strip()

    if raw in flags_by_id:
        flag = flags_by_id[raw]
        return {"kind": "flag", "flag": flag, "item_id": flag.get("item_id"),
                "chapter_ids": fc.item_chapter_ids(flag.get("item_id"), records),
                "field": field or None}

    if re.match(r"^FL-\d+$", raw):
        raise Unresolvable(f"{raw} is not in flags/flags.jsonl")

    for prefix, kind in (("subtopic_list:", "subtopic_list"),
                         ("change_log_row:", "change_log_row"),
                         ("audit:", "audit_sample"),
                         ("e4_agreement:", "e4_agreement")):
        if raw.startswith(prefix):
            rest = raw[len(prefix):]
            if kind == "audit_sample":
                step, _, item_id = rest.partition(":")
                return {"kind": kind, "flag": None, "item_id": item_id,
                        "chapter_ids": fc.item_chapter_ids(item_id, records),
                        "field": field or None, "audit_step": step, "pack_id": raw}
            item_id = rest
            default_field = {"subtopic_list": "subtopic_list",
                             "change_log_row": "change_log_row",
                             "e4_agreement": "category_primary"}[kind]
            chapter_ids = ([item_id] if kind == "subtopic_list"
                           else fc.item_chapter_ids(item_id, records))
            if kind == "change_log_row":
                chapter_ids = [r.get("chapter_id") for r in fc.change_log_rows()
                               if r.get("change_id") == item_id and r.get("chapter_id")]
            return {"kind": kind, "flag": None, "item_id": item_id,
                    "chapter_ids": chapter_ids, "field": field or default_field,
                    "pack_id": raw}

    # A bare item id: a reviewer editing something that was never flagged.
    return {"kind": "item", "flag": None, "item_id": raw,
            "chapter_ids": fc.item_chapter_ids(raw, records), "field": field or None}


def _parse_value(row):
    """`corrected_value_json` as a Python value.

    JSON first (that is what the column is called and what the pack writes). A reviewer typing a
    bare string into a spreadsheet is the common real case, so an unparseable cell is kept as the
    literal string rather than rejected — a correction must never be silently dropped because of
    a missing pair of quotes."""
    raw = row.get("corrected_value_json")
    if raw is None or str(raw).strip() == "":
        return None, False
    text = str(raw)
    try:
        return json.loads(text), True
    except json.JSONDecodeError:
        return text, True


def next_f2_output_path(item_id, field):
    """A fresh steps/F2/out/<ITEM>.correctionNNN.json — never an existing one.

    Rule 2 of the task and CLAUDE.md: a correction is recorded as a NEW F2-step output, never by
    overwriting the original. So this always returns a path that does not exist yet, and the
    sequence number preserves the order of successive corrections to the same field."""
    safe_item = "".join(c if c.isalnum() or c in "-_" else "_" for c in str(item_id))
    safe_field = "".join(c if c.isalnum() or c in "-_" else "_" for c in str(field or "value"))
    n = 1
    existing = glob.glob(os.path.join(F2_OUT_DIR, f"{safe_item}.correction*.json"))
    if existing:
        nums = [int(m.group(1)) for m in
                (re.search(r"\.correction(\d+)", p) for p in existing) if m]
        n = (max(nums) + 1) if nums else len(existing) + 1
    return os.path.join(F2_OUT_DIR, f"{safe_item}.correction{n:03d}.{safe_field}.json")


def current_value(target, records):
    """The value a correction replaces, for the `old` half of review/corrections.jsonl."""
    field = target.get("field")
    item_id = target.get("item_id") or ""
    if fc._RE_QID.match(item_id):
        rec = records.get(item_id) or {}
        if field == "chapter_ids":
            return fc.record_chapter_ids(rec)
        if field == "subtopic_ids":
            return fc.record_subtopic_ids(rec)
        if field in rec:
            return rec.get(field)
    flag = target.get("flag")
    if flag is not None:
        return flag.get("provisional_value")
    if target["kind"] == "subtopic_list":
        for draft in fc.subtopic_list_drafts():
            if draft["chapter_id"] == item_id:
                return draft["subtopics"]
    if target["kind"] == "change_log_row":
        for r in fc.change_log_rows():
            if r.get("change_id") == item_id:
                return r
    return None


# --------------------------------------------------------------------------------------------
# The four decision kinds
# --------------------------------------------------------------------------------------------

def close_flag(flag, decision, reviewer, decided_at, comment):
    flag["status"] = "blocked_by_reviewer" if decision == "block" else "closed"
    flag["decision"] = decision
    flag["reviewer"] = reviewer or None
    flag["decided_at"] = decided_at or fc.now_iso()
    if comment:
        flag["reviewer_comment"] = comment


def record_approval(target, row, decided_at):
    """Append one approval to review/approvals.jsonl, keyed so F5 can look it up.

    A flag's approval is ALSO recorded under its subject's own target key when the flag is the
    one that stands for a draft (an A4_SUBTOPICS_DRAFT flag on chapter C is how a reviewer
    approves C's subtopic list) — otherwise F5's gate would never see the approval, because F1
    de-duplicates the standalone draft item away when a flag for it exists."""
    reviewer = (row.get("reviewer") or "").strip()
    comment = (row.get("comment") or "").strip()
    base = {"decision": "approve", "reviewer": reviewer or None, "at": decided_at,
            "comment": comment or None, "item_id": target.get("item_id"),
            "field": target.get("field"), "chapter_ids": target.get("chapter_ids") or []}
    targets = []
    flag = target.get("flag")
    if flag is not None:
        targets.append(fc.flag_target(flag["flag_id"], target.get("field")))
        if (flag.get("code") == "A4_SUBTOPICS_DRAFT" or target.get("field") == "subtopic_list") \
                and flag.get("item_id"):
            targets.append(fc.subtopic_list_target(flag["item_id"]))
        if target.get("field") == "change_log_row" and flag.get("item_id"):
            targets.append(fc.change_log_target(flag["item_id"]))
    if target["kind"] == "subtopic_list":
        targets.append(fc.subtopic_list_target(target["item_id"]))
    if target["kind"] == "change_log_row":
        targets.append(fc.change_log_target(target["item_id"]))
    if target["kind"] == "audit_sample":
        targets.append(f"audit:{target.get('audit_step')}:{target['item_id']}")
    if target["kind"] == "e4_agreement":
        targets.append(f"e4_agreement:{target['item_id']}")
    if target["kind"] == "item":
        targets.append(f"item:{target['item_id']}:{target.get('field') or '*'}")
    for t in targets:
        lib_io.append_jsonl(fc.APPROVALS_PATH, dict(base, target=t))
    return targets


def mark_field_approved(item_id, field, reviewer, decided_at):
    """"Set the value's status `approved` with reviewer and date" (spec 14/F3 step 2).

    For a question that means its record's `field_sources[field]` gains a `review` block. The
    field's own `step` and `prompt_version` are left exactly as they were — the value is still
    the agent's; only its review status changed."""
    if not fc._RE_QID.match(item_id or "") or not field:
        return False
    rec = lib_records.read_record(item_id)
    if not rec:
        return False
    sources = rec.setdefault("field_sources", {})
    entry = sources.setdefault(field, {"step": None, "prompt_version": None, "status": "pass"})
    entry["review"] = {"status": "approved", "reviewer": reviewer or None, "at": decided_at}
    rec["review_status"] = "reviewed"
    lib_io.atomic_write_json(lib_records.record_path(item_id), rec)
    return True


def apply_correction(target, row, decided_at, records, dry_run):
    """approve's opposite: write the new value as a NEW F2 output, update the record, log the
    correction. Returns a dict describing what was (or would be) written."""
    item_id = target["item_id"]
    field = target.get("field")
    new_value, provided = _parse_value(row)
    if not provided:
        raise Unresolvable("decision is correct/edit but corrected_value_json is empty")
    if not field:
        raise Unresolvable("decision is correct/edit but no `field` was given")

    old_value = current_value(target, records)
    reviewer = (row.get("reviewer") or "").strip() or None
    comment = (row.get("comment") or "").strip() or None
    flag = target.get("flag")

    f2_payload = {
        "step": F2_STEP,
        "item_id": item_id,
        "item_type": target["kind"],
        "field": field,
        "old": old_value,
        "new": new_value,
        "reviewer": reviewer,
        "comment": comment,
        "decided_at": decided_at,
        "flag_id": (flag or {}).get("flag_id"),
        "prompt_version": f2_prompt_version(),
        "note": ("Stage F correction. Written as a NEW F2 output so the original step's output "
                 "file is preserved unmodified (CLAUDE.md: never edit an agent's output)."),
    }
    out_path = next_f2_output_path(item_id, field)
    result = {"f2_output": os.path.relpath(out_path, fc.PROJECT_ROOT),
              "old": old_value, "new": new_value, "record_updated": False}

    if dry_run:
        return result

    lib_io.atomic_write_json(out_path, f2_payload)

    if fc._RE_QID.match(item_id or ""):
        rec = lib_records.read_record(item_id)
        rec["question_id"] = item_id
        # Write the spec 6.3 field name, and keep any d1_/d2_ alias the pipeline actually uses in
        # step with it, so a corrected chapter is not silently shadowed by the stale alias.
        rec[field] = new_value
        alias = {"chapter_ids": "d1_chapter_ids", "subtopic_ids": "d2_subtopic_ids"}.get(field)
        if alias and alias in rec:
            rec[alias] = new_value
        sources = rec.setdefault("field_sources", {})
        sources[field] = {
            "step": F2_STEP, "prompt_version": f2_prompt_version(), "status": "approved",
            "review": {"status": "corrected", "reviewer": reviewer, "at": decided_at},
            "corrected_from_step": (sources.get(field) or {}).get("step"),
            "f2_output": result["f2_output"],
        }
        if alias and alias in rec:
            sources[alias] = dict(sources[field])
        rec["review_status"] = "reviewed"
        lib_io.atomic_write_json(lib_records.record_path(item_id), rec)
        result["record_updated"] = True
    return result


def apply_block(target, row, decided_at, dry_run):
    """block → `release_status = blocked_by_reviewer` (spec 14/F3 step 4).

    For a question that is a field on its record. A chapter, register row or intake item has no
    record, so the block is recorded in review/blocks.jsonl, which F5's gate also reads — a
    blocked chapter must never be releasable just because the block had nowhere to live."""
    item_id = target["item_id"]
    reviewer = (row.get("reviewer") or "").strip() or None
    comment = (row.get("comment") or "").strip() or None
    out = {"record_updated": False, "blocks_jsonl": False}
    if dry_run:
        out["record_updated"] = bool(fc._RE_QID.match(item_id or ""))
        out["blocks_jsonl"] = True
        return out
    if fc._RE_QID.match(item_id or ""):
        rec = lib_records.read_record(item_id)
        rec["question_id"] = item_id
        rec["release_status"] = "blocked_by_reviewer"
        rec["review_status"] = "blocked"
        sources = rec.setdefault("field_sources", {})
        sources["release_status"] = {"step": F2_STEP, "prompt_version": f2_prompt_version(),
                                     "status": "blocked_by_reviewer",
                                     "review": {"reviewer": reviewer, "at": decided_at}}
        lib_io.atomic_write_json(lib_records.record_path(item_id), rec)
        out["record_updated"] = True
    lib_io.append_jsonl(fc.BLOCKS_PATH, {
        "at": decided_at, "item_id": item_id, "item_kind": target["kind"],
        "field": target.get("field"), "chapter_ids": target.get("chapter_ids") or [],
        "reviewer": reviewer, "comment": comment,
        "flag_id": (target.get("flag") or {}).get("flag_id"),
        "release_status": "blocked_by_reviewer",
    })
    out["blocks_jsonl"] = True
    return out


# --------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------

def apply_decisions(apply=False, run=False, transitive=True, decisions_path=None,
                    rebuild_pack=False):
    records = fc.load_records()
    flags = fc.load_flags()
    flags_by_id = {f["flag_id"]: f for f in flags}
    rows = fc.read_decisions(decisions_path)
    already = fc.applied_digests()
    dry_run = not apply

    report = {"rows_total": len(rows), "rows_new": 0, "applied": [], "skipped": [],
              "errors": [], "cascade": {"pairs": 0, "steps": [], "notes": []},
              "dry_run": dry_run}

    all_plans = []
    flags_dirty = False

    for row in rows:
        digest = fc.decision_digest(row)
        if digest in already:
            report["skipped"].append({"target": row.get("flag_id_or_item"),
                                      "why": "already applied (same digest)"})
            continue
        report["rows_new"] += 1
        decision = (row.get("decision") or "").strip().lower()
        decided_at = (row.get("decided_at") or "").strip() or fc.today_iso()
        reviewer = (row.get("reviewer") or "").strip()

        if decision not in fc.DECISION_VALUES:
            report["errors"].append({"target": row.get("flag_id_or_item"),
                                     "why": f"decision {decision!r} is not one of "
                                            f"{', '.join(fc.DECISION_VALUES)}"})
            continue
        if not reviewer:
            report["errors"].append({"target": row.get("flag_id_or_item"),
                                     "why": "no reviewer named; spec 14/F3 requires the "
                                            "reviewer and date on every decision"})
            continue
        try:
            target = resolve_target(row, flags_by_id, records)
        except Unresolvable as e:
            report["errors"].append({"target": row.get("flag_id_or_item"), "why": str(e)})
            continue

        entry = {"target": row.get("flag_id_or_item"), "decision": decision,
                 "item_id": target["item_id"], "field": target.get("field"),
                 "kind": target["kind"], "chapter_ids": target.get("chapter_ids") or [],
                 "reviewer": reviewer, "decided_at": decided_at}

        try:
            if decision == "approve":
                if not dry_run:
                    entry["approval_targets"] = record_approval(target, row, decided_at)
                    entry["field_marked_approved"] = mark_field_approved(
                        target["item_id"], target.get("field"), reviewer, decided_at)
                    if target.get("flag") is not None:
                        close_flag(target["flag"], "approve", reviewer, decided_at,
                                   row.get("comment"))
                        flags_dirty = True
                else:
                    entry["would"] = "close flag, record approval, mark field approved"

            elif decision in ("correct", "edit"):
                entry.update(apply_correction(target, row, decided_at, records, dry_run))
                if not dry_run:
                    correction = {
                        "item_id": target["item_id"], "field": target.get("field"),
                        "old": entry.get("old"), "new": entry.get("new"),
                        "step_corrected": (target.get("flag") or {}).get("step"),
                        "reviewer": reviewer, "reason": (row.get("comment") or "").strip() or None,
                        "flag_id": (target.get("flag") or {}).get("flag_id"),
                        "at": decided_at, "f2_output": entry.get("f2_output"),
                        "cascade": [],
                    }
                    if target.get("flag") is not None:
                        close_flag(target["flag"], decision, reviewer, decided_at,
                                   row.get("comment"))
                        flags_dirty = True
                plan = cascade.plan_for_change(target.get("field"), target["item_id"],
                                               transitive=transitive)
                entry["cascade_direct"] = len(plan["direct"])
                entry["cascade_transitive"] = len(plan["transitive"])
                entry["cascade_steps"] = sorted({p["step"] for p in plan["direct"] + plan["transitive"]},
                                                key=fc.step_index)
                report["cascade"]["notes"].extend(plan["notes"])
                if not dry_run:
                    correction["cascade"] = [{"step": p["step"], "item_id": p["item_id"],
                                              "scope": p["scope"]}
                                             for p in plan["direct"] + plan["transitive"]]
                    lib_io.append_jsonl(fc.CORRECTIONS_PATH, correction)
                all_plans.append(plan)

            elif decision == "block":
                entry.update(apply_block(target, row, decided_at, dry_run))
                if not dry_run and target.get("flag") is not None:
                    close_flag(target["flag"], "block", reviewer, decided_at, row.get("comment"))
                    flags_dirty = True
        except Unresolvable as e:
            report["errors"].append({"target": row.get("flag_id_or_item"), "why": str(e)})
            continue

        report["applied"].append(entry)
        if not dry_run:
            lib_io.append_jsonl(fc.APPLIED_PATH, {
                "digest": digest, "at": fc.now_iso(), "target": row.get("flag_id_or_item"),
                "decision": decision, "item_id": target["item_id"],
                "field": target.get("field"), "reviewer": reviewer,
            })

    if flags_dirty:
        fc.save_flags(flags)

    merged = {"direct": [], "transitive": []}
    seen = set()
    for plan in all_plans:
        for bucket in ("direct", "transitive"):
            for p in plan[bucket]:
                k = (p["step"], p["item_id"])
                if k in seen:
                    continue
                seen.add(k)
                merged[bucket].append(p)
    merged["direct"].sort(key=lambda p: (fc.step_index(p["step"]), p["item_id"]))
    merged["transitive"].sort(key=lambda p: (fc.step_index(p["step"]), p["item_id"]))
    report["cascade"]["pairs"] = len(merged["direct"]) + len(merged["transitive"])
    report["cascade"]["steps"] = sorted({p["step"] for p in merged["direct"] + merged["transitive"]},
                                        key=fc.step_index)

    if report["cascade"]["pairs"]:
        applied_pairs = cascade.apply_plan(merged, dry_run=dry_run)
        report["cascade"]["marked_stale"] = len(applied_pairs)
        if run and not dry_run:
            report["cascade"]["rerun"] = cascade.run_plan(applied_pairs)

    if rebuild_pack and not dry_run:
        proc = subprocess.run(
            [sys.executable, "scripts/build_review_pack.py", "--new-only", "--json"],
            cwd=fc.PROJECT_ROOT, capture_output=True, text=True)
        report["pack_rebuild"] = {"returncode": proc.returncode,
                                 "stdout_tail": (proc.stdout or "")[-2000:],
                                 "stderr_tail": (proc.stderr or "")[-1000:]}
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description="F3 · apply review decisions and cascade (spec 14/F3).")
    ap.add_argument("--apply", action="store_true",
                    help="Actually apply. Without it this is a dry run that changes nothing.")
    ap.add_argument("--run", action="store_true",
                    help="After applying, re-run the stale script-only steps in stage order.")
    ap.add_argument("--rebuild-pack", action="store_true",
                    help="After applying, rebuild the pack with --new-only (spec 14/F3 step 6).")
    ap.add_argument("--no-transitive", action="store_true",
                    help="Cascade only the explicit config/cascade.yaml lists.")
    ap.add_argument("--decisions", help="Path to a decisions.csv (default review/decisions.csv).")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    report = apply_decisions(apply=args.apply, run=args.run,
                             transitive=not args.no_transitive,
                             decisions_path=args.decisions,
                             rebuild_pack=args.rebuild_pack)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 1 if report["errors"] else 0

    mode = "APPLIED" if args.apply else "DRY RUN (nothing changed; pass --apply)"
    print(f"F3 apply_review · {mode}")
    print(f"  decisions.csv rows : {report['rows_total']} ({report['rows_new']} new, "
          f"{len(report['skipped'])} already applied)")
    for e in report["applied"]:
        print(f"  {e['decision']:8s} {str(e['target']):22s} field={e.get('field')!r} "
              f"item={e['item_id']}"
              + (f" -> {e['f2_output']}" if e.get("f2_output") else "")
              + (f" cascade={e.get('cascade_direct', 0)}+{e.get('cascade_transitive', 0)} "
                 f"[{','.join(e.get('cascade_steps') or [])}]" if "cascade_direct" in e else ""))
    for s in report["skipped"]:
        print(f"  skip     {s['target']}: {s['why']}")
    for e in report["errors"]:
        print(f"  ERROR    {e['target']}: {e['why']}")
    c = report["cascade"]
    print(f"  cascade            : {c['pairs']} (item, step) pair(s) across "
          f"{len(c['steps'])} step(s): {','.join(c['steps']) or '(none)'}")
    for note in dict.fromkeys(c["notes"]):
        print(f"    note: {note}")
    if "rerun" in c:
        r = c["rerun"]
        for x in r["ran"]:
            print(f"    ran {x['step']} rc={x.get('returncode')} items={len(x['items'])}")
        for d in r["needs_dispatch"]:
            print(f"    NEEDS A PERSON: {d['step']} is agent-driven; run "
                  f"`python3 scripts/run_step.py {d['step']} --list --items "
                  f"{','.join(d['items'][:8])}{'...' if len(d['items']) > 8 else ''}`, invoke the "
                  f"named subagent per line, then --check.")
        print(f"    unchanged re-runs (no flag): {len(r['unchanged'])}; changed: {len(r['changed'])}; "
              f"flags auto_closed: {len(r['auto_closed'])}")
    if report["errors"]:
        print("\nSome rows were rejected. Fix them in review/decisions.csv and run again; "
              "accepted rows have already been recorded and will not be re-applied.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
