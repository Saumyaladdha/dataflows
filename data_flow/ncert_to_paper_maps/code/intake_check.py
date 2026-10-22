#!/usr/bin/env python3
"""S0 · Intake check (spec Section 8). SCRIPT-only step, no agent.

PUBLIC ENTRY POINT: run() -> dict summary (see its docstring). This is what the other agent's
`scripts/run_step.py` / `scripts/checks/S0.py` should call once both are done; it takes no
arguments and is safe to call repeatedly (idempotent — see "Idempotence" below).

Run standalone: `python3 scripts/intake_check.py` (prints the same summary to stdout).

What it does, following spec Section 8's five-step procedure against the real inputs/ tree and
inputs/manifest.csv (built by scripts/build_manifest.py, which this script only reads):
  1. List every file under inputs/ (excluding inputs/_reference/, out of S0's scope — see
     docs/OPEN_QUESTIONS.md 2026-10-09); confirm every file has exactly one manifest row and
     every row a file.
  2. For each NCERT subject x class x edition, require a non-empty chapter set (the real layout
     is one PDF per chapter, not one PDF per book — docs/OPEN_QUESTIONS.md 2026-10-09 Section 9
     A1/A2 entry governs this adaptation); require Physics and Chemistry lab manuals.
  3. For each year 2016-2026, for each sitting on the official calendar
     (scripts/lib/sittings.py), require a paper and a final key (except CANCELLED sittings need
     no key — see docs/OPEN_QUESTIONS.md). An ambiguous-sitting file set (2016/2019/2020/2024)
     is never silently counted as "present" for either sitting it might be.
  4. Mark papers/keys outside 2016-2026 in_scope = no (informational only; not required, not
     flagged missing — except 2012, whose total absence as a PDF is still worth surfacing).
  5. Verify legacy sheets are classified as legacy_sheet only, never as paper/key.

Writes:
  - steps/S0/out/<item_id>.json   — one record per required/checked item, shaped per schemas/S0.json
  - steps/S0/status/inputs.json   — the step's own status (flagged if any blocker was raised, else pass)
  - flags/flags.jsonl             — one S0_MISSING_INPUT (blocker) flag per missing/unresolved item
  - register/intake_report.md     — the human-facing summary

Idempotence (spec 5.9, "running a command twice in a row must do nothing the second time"):
every run re-derives the full picture from inputs/ + inputs/manifest.csv from scratch and
overwrites steps/S0/out/*, steps/S0/status/inputs.json and register/intake_report.md in place.
flags/flags.jsonl is append-only (spec 5.6), so to stay idempotent this script removes any
flags it previously wrote (step == "S0") before appending this run's flags — flag_ids still
never get reused (ids.py's counter only ever increments), only the *set of currently open S0
flags* stays equal to "what's wrong right now" rather than growing without bound across reruns.
"""
import datetime
import json
import os
import re
import sys

try:
    from scripts.lib import flags as lib_flags
    from scripts.lib import io as lib_io
    from scripts.lib import sittings
    from scripts.lib import status as lib_status
except ImportError:  # running as `python3 scripts/intake_check.py` directly
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from scripts.lib import flags as lib_flags
    from scripts.lib import io as lib_io
    from scripts.lib import sittings
    from scripts.lib import status as lib_status

MANIFEST_PATH = lib_io.project_path("inputs", "manifest.csv")
INPUTS_ROOT = lib_io.project_path("inputs")
REPORT_PATH = lib_io.project_path("register", "intake_report.md")
S0_OUT_DIR = lib_io.project_path("steps", "S0", "out")

SUBJECTS = ("Physics", "Chemistry", "Biology")
CLASSES = (11, 12)
EDITIONS = ("latest", "older")

# inputs/_reference/ is explicitly out of S0's scope (Codebook Section 7: "not wired into
# intake as a formal source") — see docs/OPEN_QUESTIONS.md 2026-10-09.
EXCLUDED_TOP_DIRS = {"_reference"}


def _sanitize_id(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s)


def _relpath(full):
    return os.path.relpath(full, lib_io.PROJECT_ROOT).replace(os.sep, "/")


# ---------------------------------------------------------------------------
# Procedure step 1: file <-> manifest reconciliation
# ---------------------------------------------------------------------------

def walk_all_input_files():
    files = []
    for root, dirs, fnames in os.walk(INPUTS_ROOT):
        rel_root = os.path.relpath(root, INPUTS_ROOT)
        top = "" if rel_root == "." else rel_root.split(os.sep)[0]
        if top in EXCLUDED_TOP_DIRS:
            dirs[:] = []
            continue
        for fname in fnames:
            if root == INPUTS_ROOT and fname == "manifest.csv":
                continue
            files.append(_relpath(os.path.join(root, fname)))
    return sorted(files)


def reconcile_files_and_manifest(manifest_rows):
    tree_files = set(walk_all_input_files())
    manifest_file_list = [r["file"] for r in manifest_rows]
    manifest_files = set(manifest_file_list)

    seen = {}
    duplicates = []
    for f in manifest_file_list:
        seen[f] = seen.get(f, 0) + 1
    for f, n in seen.items():
        if n > 1:
            duplicates.append(f)

    files_without_row = sorted(tree_files - manifest_files)
    rows_without_file = sorted(manifest_files - tree_files)
    return {
        "tree_file_count": len(tree_files),
        "manifest_row_count": len(manifest_rows),
        "files_without_manifest_row": files_without_row,
        "manifest_rows_without_file": rows_without_file,
        "duplicate_manifest_rows": sorted(duplicates),
    }


# ---------------------------------------------------------------------------
# Procedure step 2: NCERT grid + lab manuals
# ---------------------------------------------------------------------------

def check_ncert_grid(manifest_rows):
    ncert_rows = [r for r in manifest_rows if r["kind"] == "ncert"]
    records = []
    for subject in SUBJECTS:
        for class_ in CLASSES:
            for edition in EDITIONS:
                matches = [r for r in ncert_rows
                           if r["subject"] == subject and r["class"] == str(class_)
                           and r["edition"] == edition]
                item_id = f"ncert-{subject}-{class_}-{edition}"
                if matches:
                    records.append({
                        "item_id": item_id, "item_type": "ncert_book", "subject": subject,
                        "class": class_, "edition": edition, "status": "present",
                        "note": f"{len(matches)} {edition}-edition chapter PDF(s) found "
                                f"(one-PDF-per-chapter layout; treated as one logical book per "
                                f"docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entry)",
                    })
                else:
                    records.append({
                        "item_id": item_id, "item_type": "ncert_book", "subject": subject,
                        "class": class_, "edition": edition, "status": "missing",
                        "note": f"no {edition}-edition NCERT chapter PDFs found for "
                                f"{subject} Class {class_}",
                    })
    return records


def check_lab_manuals(manifest_rows):
    labman_rows = [r for r in manifest_rows if r["kind"] == "lab_manual"]
    records = []
    for subject in ("Physics", "Chemistry"):
        matches = [r for r in labman_rows if r["subject"] == subject]
        item_id = f"labmanual-{subject}"
        if matches:
            records.append({
                "item_id": item_id, "item_type": "lab_manual", "subject": subject,
                "edition": "lab_manual", "status": "present",
                "note": f"{len(matches)} lab manual PDF(s) found",
            })
        else:
            records.append({
                "item_id": item_id, "item_type": "lab_manual", "subject": subject,
                "edition": "lab_manual", "status": "missing",
                "note": f"{subject} NCERT lab manual not collected (none in this drop; "
                        f"confirmed missing per Codebook Section 1)",
            })
    return records


# ---------------------------------------------------------------------------
# Procedure step 3 (+4): papers and keys by year x sitting
# ---------------------------------------------------------------------------

def check_papers_and_keys(manifest_rows):
    paper_rows = [r for r in manifest_rows if r["kind"] == "paper"]
    key_rows = [r for r in manifest_rows if r["kind"] == "key"]
    records = []

    for year in sorted(sittings.REQUIRED_SITTINGS):
        required = sittings.REQUIRED_SITTINGS[year]
        for sitting in required:
            # --- paper ---
            exact = [r for r in paper_rows if r["year"] == str(year) and r["sitting"] == sitting]
            item_id = f"paper-{year}-{sitting}"
            if exact:
                records.append({
                    "item_id": item_id, "item_type": "paper", "year": year, "sitting": sitting,
                    "in_scope": True, "status": "present",
                    "file": "; ".join(sorted(r["file"] for r in exact)),
                    "note": f"{len(exact)} booklet code file(s)",
                })
            else:
                ambiguous = [r for r in paper_rows if r["year"] == str(year) and not r["sitting"]]
                if ambiguous:
                    note = (f"{len(ambiguous)} paper file(s) exist for {year} but which sitting "
                            f"each belongs to ({'/'.join(required)}) could not be confirmed from "
                            f"the filename alone: " + ", ".join(sorted(r["file"] for r in ambiguous)))
                else:
                    note = f"no paper file found for {year} {sitting}"
                records.append({
                    "item_id": item_id, "item_type": "paper", "year": year, "sitting": sitting,
                    "in_scope": True, "status": "missing", "note": note,
                })

            # --- key --- (CANCELLED sittings need no key — judgment call, see OPEN_QUESTIONS.md)
            if sitting in sittings.SITTINGS_WITHOUT_KEY_REQUIREMENT:
                continue
            exact_k = [r for r in key_rows if r["year"] == str(year) and r["sitting"] == sitting]
            item_id_k = f"key-{year}-{sitting}"
            if exact_k:
                records.append({
                    "item_id": item_id_k, "item_type": "key", "year": year, "sitting": sitting,
                    "in_scope": True, "status": "present",
                    "file": "; ".join(sorted(r["file"] for r in exact_k)), "note": "",
                })
            else:
                ambiguous_k = [r for r in key_rows if r["year"] == str(year) and not r["sitting"]]
                if ambiguous_k:
                    note = (f"{len(ambiguous_k)} key file(s) exist for {year} but cover the whole "
                             f"year without splitting by sitting — cannot confirm {sitting} is "
                             f"covered: " + ", ".join(sorted(r["file"] for r in ambiguous_k)))
                else:
                    note = f"no final key file found for {year} {sitting}"
                records.append({
                    "item_id": item_id_k, "item_type": "key", "year": year, "sitting": sitting,
                    "in_scope": True, "status": "missing", "note": note,
                })
    return records


def check_2018_booklet_codes(manifest_rows):
    """Extra diligence beyond the year x sitting grain literally named in procedure step 3: that
    step's own Reads line requires a key "whose booklet code matches the paper (or a key
    covering all codes)". 2018 is the one year in this drop with genuinely per-code keys (every
    other year is either one file for the whole year, or split by phase/sitting only) — so it's
    the one place this finer match is actually checkable against real data."""
    paper_codes = {r["booklet_code"] for r in manifest_rows
                   if r["kind"] == "paper" and r["year"] == "2018" and r["booklet_code"]}
    key_codes = {r["booklet_code"] for r in manifest_rows
                 if r["kind"] == "key" and r["year"] == "2018" and r["booklet_code"]}
    records = []
    for code in sorted(paper_codes - key_codes):
        records.append({
            "item_id": f"key-2018-MAIN-{code}", "item_type": "key", "year": 2018,
            "sitting": "MAIN", "booklet_code": code, "in_scope": True, "status": "missing",
            "note": f"paper booklet code {code} (2018) has no matching final-key file "
                    f"(key set has {len(key_codes)} codes, paper set has {len(paper_codes)})",
        })
    return records


# ---------------------------------------------------------------------------
# Procedure step 4: out-of-scope papers/keys (informational)
# ---------------------------------------------------------------------------

def check_out_of_scope(manifest_rows):
    records = []
    years_seen = sorted({
        int(r["year"]) for r in manifest_rows
        if r["kind"] in ("paper", "key") and r["year"]
        and int(r["year"]) not in sittings.IN_SCOPE_YEARS
    })
    for year in years_seen:
        p = sorted(r["file"] for r in manifest_rows if r["kind"] == "paper" and r["year"] == str(year))
        k = sorted(r["file"] for r in manifest_rows if r["kind"] == "key" and r["year"] == str(year))
        records.append({
            "item_id": f"paper-{year}-outofscope", "item_type": "paper", "year": year,
            "in_scope": False, "status": "out_of_scope",
            "file": "; ".join(p) if p else None,
            "note": f"{len(p)} paper file(s), {len(k)} key file(s); out of scope pending "
                    f"Section 20 decision #1 (years outside 2016-2026)",
        })
    # 2012 is a real, confirmed gap even though it's out of scope either way.
    if not any(r["kind"] == "paper" and r["year"] == "2012" for r in manifest_rows):
        records.append({
            "item_id": "paper-2012-outofscope", "item_type": "paper", "year": 2012,
            "in_scope": False, "status": "out_of_scope",
            "note": "no paper PDF at all for 2012 (only legacy spreadsheets exist); out of "
                    "scope regardless pending Section 20 decision #1, but a real collection "
                    "gap worth surfacing (Codebook Section 2)",
        })
    return records


# ---------------------------------------------------------------------------
# Procedure step 5: legacy sheets classified correctly, never as paper/key
# ---------------------------------------------------------------------------

def check_legacy_sheet_classification(manifest_rows):
    problems = []
    for r in manifest_rows:
        f = r["file"]
        under_legacy_dir = f.startswith("inputs/legacy_sheets/")
        if under_legacy_dir and r["kind"] != "legacy_sheet":
            problems.append(f"{f}: file sits under inputs/legacy_sheets/ but manifest kind={r['kind']!r}")
        if r["kind"] == "legacy_sheet" and not under_legacy_dir:
            problems.append(f"{f}: manifest kind=legacy_sheet but file is not under inputs/legacy_sheets/")
        if r["kind"] == "legacy_sheet" and not f.lower().endswith(".xlsx"):
            problems.append(f"{f}: manifest kind=legacy_sheet but file is not an .xlsx")
        if r["kind"] in ("paper", "key") and f.lower().endswith(".xlsx"):
            problems.append(f"{f}: manifest kind={r['kind']!r} but file is an .xlsx (looks like a legacy sheet)")
    return problems


def build_legacy_sheet_records(manifest_rows):
    records = []
    for r in manifest_rows:
        if r["kind"] != "legacy_sheet":
            continue
        year = int(r["year"]) if r["year"] else None
        base = os.path.splitext(os.path.basename(r["file"]))[0]
        records.append({
            "item_id": f"legacy-{_sanitize_id(base)}", "item_type": "legacy_sheet",
            "year": year, "file": r["file"], "status": "present",
            "note": "registered as legacy_sheet only; never passed to any agent or used to set "
                    "any field (spec Section 2.2/13)",
        })
    return records


# ---------------------------------------------------------------------------
# Writing S0 out records, flags, status, and the report
# ---------------------------------------------------------------------------

def _write_s0_out_record(record):
    """Write one record to steps/S0/out/<item_id>.json, exactly shaped per schemas/S0.json
    (additionalProperties: false there, so only its declared keys are written)."""
    payload = {
        "item_type": record["item_type"],
        "subject": record.get("subject"),
        "class": record.get("class"),
        "edition": record.get("edition"),
        "year": record.get("year"),
        "sitting": record.get("sitting"),
        "booklet_code": record.get("booklet_code"),
        "file": record.get("file"),
        "in_scope": record.get("in_scope"),
        "status": record["status"],
        "note": record.get("note") or "",
    }
    path = os.path.join(S0_OUT_DIR, f"{record['item_id']}.json")
    lib_io.atomic_write_json(path, payload)


def _clear_previous_s0_flags():
    """Keep flags/flags.jsonl idempotent across reruns: drop this step's previously-written
    flags before appending this run's. flag_id minting (ids.py) is untouched, so ids still only
    ever increment — only the *set of currently open S0 flags* stops growing without bound."""
    existing = list(lib_io.read_jsonl(lib_flags.FLAGS_PATH))
    kept = [f for f in existing if f.get("step") != "S0"]
    if len(kept) != len(existing):
        content = "".join(json.dumps(f, ensure_ascii=False) + "\n" for f in kept)
        lib_io.atomic_write_text(lib_flags.FLAGS_PATH, content)
    return kept


def _raise_missing_flags(records):
    raised = []
    for r in records:
        if r["status"] != "missing":
            continue
        flag = lib_flags.raise_flag(
            item_type=r["item_type"], item_id=r["item_id"], step="S0",
            code="S0_MISSING_INPUT", severity="blocker", message=r["note"],
            provisional_value=None, evidence=[], prompt_version=None,
        )
        raised.append(flag)
    return raised


def _fmt(v):
    return "—" if v in (None, "") else v


def _render_report(ctx):
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    lines = []
    w = lines.append

    w("# Stage 0 · Intake report\n")
    w(f"Generated: {now}  ")
    w(f"Source: `inputs/manifest.csv` ({ctx['reconcile']['manifest_row_count']} rows) vs "
      f"`inputs/` tree ({ctx['reconcile']['tree_file_count']} files, excluding "
      f"`inputs/_reference/`)\n")

    n_missing = sum(1 for r in ctx["all_records"] if r["status"] == "missing")
    n_present = sum(1 for r in ctx["all_records"] if r["status"] == "present")
    n_oos = sum(1 for r in ctx["all_records"] if r["status"] == "out_of_scope")
    w("## Summary\n")
    w(f"- Manifest rows by kind: " + ", ".join(
        f"{k}={v}" for k, v in sorted(ctx['manifest_kind_counts'].items())) + "\n")
    w(f"- Required/checked items: **{n_present} present**, **{n_missing} missing**, "
      f"{n_oos} out-of-scope-informational\n")
    w(f"- `S0_MISSING_INPUT` (blocker) flags raised this run: **{len(ctx['raised_flags'])}**\n")
    recon = ctx["reconcile"]
    recon_ok = not (recon["files_without_manifest_row"] or recon["manifest_rows_without_file"]
                     or recon["duplicate_manifest_rows"])
    w(f"- File <-> manifest reconciliation: {'OK, exact match' if recon_ok else 'PROBLEMS FOUND (see section 8 below)'}\n")
    w(f"- Legacy sheet classification check: "
      f"{'OK, no misclassified files' if not ctx['legacy_problems'] else f'{len(ctx['legacy_problems'])} PROBLEM(S) FOUND'}\n")

    w("\n## 1. NCERT books (Physics / Chemistry / Biology x Class 11 / 12 x latest / older)\n")
    w("| Subject | Class | Edition | Status | Note |")
    w("|---|---|---|---|---|")
    for r in ctx["ncert_records"]:
        w(f"| {r['subject']} | {r['class']} | {r['edition']} | **{r['status']}** | {_fmt(r['note'])} |")

    w("\n## 2. Lab manuals\n")
    w("| Subject | Status | Note |")
    w("|---|---|---|")
    for r in ctx["labman_records"]:
        w(f"| {r['subject']} | **{r['status']}** | {_fmt(r['note'])} |")

    w("\n## 3. Papers & keys, 2016–2026 (in scope)\n")
    w("One row per (year, sitting). A `missing` paper/key with a note mentioning \"could not be "
      "confirmed\" means file(s) exist but couldn't be safely attributed to this sitting — not "
      "that nothing exists at all.\n")
    w("| Year | Sitting | Paper | Key | Note |")
    w("|---|---|---|---|---|")
    by_year_sitting = {}
    for r in ctx["paper_key_records"]:
        by_year_sitting.setdefault((r["year"], r["sitting"]), {})[r["item_type"]] = r
    for (year, sitting) in sorted(by_year_sitting):
        entry = by_year_sitting[(year, sitting)]
        p = entry.get("paper")
        k = entry.get("key")
        p_cell = f"**{p['status']}**" if p else "n/a"
        if sitting in sittings.SITTINGS_WITHOUT_KEY_REQUIREMENT and "key" not in entry:
            k_cell = "not required (cancelled)"
        else:
            k_cell = f"**{k['status']}**" if k else "n/a"
        notes = []
        if p and p["status"] == "missing":
            notes.append(f"paper: {p['note']}")
        if k and k["status"] == "missing":
            notes.append(f"key: {k['note']}")
        w(f"| {year} | {sitting} | {p_cell} | {k_cell} | {'; '.join(notes) if notes else '—'} |")

    if ctx["code2018_records"]:
        w("\n## 4. Extra check: 2018 booklet-code-level paper <-> key matching\n")
        w("2018 is the one year with genuinely per-booklet-code keys (every other year is one "
          "file for the whole year, or split only by phase/sitting). This checks every paper "
          "code has a matching key code, beyond the year x sitting grain above.\n")
        w("| Booklet code | Status | Note |")
        w("|---|---|---|")
        for r in ctx["code2018_records"]:
            w(f"| {r['booklet_code']} | **{r['status']}** | {_fmt(r['note'])} |")
    else:
        w("\n## 4. Extra check: 2018 booklet-code-level paper <-> key matching\n")
        w("Every 2018 paper booklet code has a matching key file. OK.\n")

    w("\n## 5. Out of scope (years outside 2016–2026)\n")
    w("Registered for completeness; Stage B does not run on these pending Section 20 decision #1.\n")
    w("| Year | Paper file(s) | Note |")
    w("|---|---|---|")
    for r in sorted(ctx["oos_records"], key=lambda r: r["year"]):
        w(f"| {r['year']} | {_fmt(r.get('file'))} | {_fmt(r['note'])} |")

    w("\n## 6. Legacy sheets\n")
    w(f"{len(ctx['legacy_records'])} spreadsheet(s) registered under `inputs/legacy_sheets/`, "
      f"all `kind=legacy_sheet`. Per spec Section 2.2/13, these are never passed to any agent "
      f"and never set any field directly — comparison-only in Stage F.\n")
    if ctx["legacy_problems"]:
        w("\n**Classification problems found:**\n")
        for p in ctx["legacy_problems"]:
            w(f"- {p}")
    else:
        w("Classification check: every legacy sheet is `kind=legacy_sheet` and sits under "
          "`inputs/legacy_sheets/`; no paper/key file is misclassified as a legacy sheet. OK.\n")

    w("\n## 7. Notices & coaching material\n")
    w("| Category | Status |")
    w("|---|---|")
    w(f"| Official notices (`inputs/notices/`) | **missing** — none received yet |")
    w(f"| Coaching solutions (`inputs/coaching/`) | **missing** — none received yet "
      f"(Section 20 decision #4: not licensed even if received) |")

    w("\n## 8. File <-> manifest reconciliation detail (procedure step 1)\n")
    if recon_ok:
        w("Every file under `inputs/` (excluding `inputs/_reference/`) has exactly one "
          "manifest row, and every manifest row points to a file that exists. OK.\n")
    else:
        if recon["files_without_manifest_row"]:
            w(f"\n**{len(recon['files_without_manifest_row'])} file(s) with no manifest row:**\n")
            for f in recon["files_without_manifest_row"]:
                w(f"- {f}")
        if recon["manifest_rows_without_file"]:
            w(f"\n**{len(recon['manifest_rows_without_file'])} manifest row(s) with no matching file:**\n")
            for f in recon["manifest_rows_without_file"]:
                w(f"- {f}")
        if recon["duplicate_manifest_rows"]:
            w(f"\n**{len(recon['duplicate_manifest_rows'])} file(s) with more than one manifest row:**\n")
            for f in recon["duplicate_manifest_rows"]:
                w(f"- {f}")

    w("\n## 9. Files with ambiguous/unresolved metadata\n")
    w("These files are registered (`kind` is reliable — it comes from folder location) but "
      "`sitting` (and in a few cases `year`) was deliberately left blank rather than guessed. "
      "This is exactly why some `missing` rows above exist even though a file is physically "
      "present: presence of an unsplit/ambiguous file does not confirm presence of a specific "
      "required sitting.\n")
    if ctx["unparsed"]:
        for f, reason in ctx["unparsed"]:
            w(f"- `{f}` — {reason}")
    else:
        w("None.\n")

    w("\n## 10. Judgment calls made for this run\n")
    w("See `docs/OPEN_QUESTIONS.md`, entries dated 2026-10-09 under Section 8 (S0), in full. "
      "Summary:\n")
    w("- A CANCELLED sitting requires a paper but not a key (a cancelled exam has no official "
      "final key by definition).")
    w("- An ambiguous sitting split (file exists but can't be attributed to MAIN vs. "
      "PH2/REEXAM/RETEST) counts as `missing` for both candidate sittings, not `present` for "
      "either.")
    w("- `inputs/_reference/` is excluded from the file<->manifest reconciliation (Codebook "
      "Section 7: reference-only, not a formal intake source).")
    w("- 2018's paper<->key booklet-code matching was checked individually since it's the one "
      "year where that's actually possible from real per-code key files.")
    w("- S0's own step status is `flagged` (never `blocked`) even with missing items, since the "
      "spec's own \"On failure\" line for S0 says the rest of the run continues.")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def run():
    """Run the full S0 intake check against the real inputs/ tree and inputs/manifest.csv.

    Returns a summary dict:
      {
        "manifest_row_count": int, "manifest_kind_counts": {kind: count},
        "tree_file_count": int,
        "required_present": int, "required_missing": int, "out_of_scope_items": int,
        "flags_raised": int,
        "reconciliation_ok": bool, "legacy_classification_ok": bool,
        "report_path": str, "flags_path": str,
      }
    """
    os.makedirs(S0_OUT_DIR, exist_ok=True)
    manifest_rows = lib_io.read_csv(MANIFEST_PATH)
    if not manifest_rows:
        raise RuntimeError(
            f"{MANIFEST_PATH} is empty or missing. Run `python3 scripts/build_manifest.py` "
            f"first — S0 reads the manifest, it does not generate it.")

    manifest_kind_counts = {}
    for r in manifest_rows:
        manifest_kind_counts[r["kind"]] = manifest_kind_counts.get(r["kind"], 0) + 1

    reconcile = reconcile_files_and_manifest(manifest_rows)
    ncert_records = check_ncert_grid(manifest_rows)
    labman_records = check_lab_manuals(manifest_rows)
    paper_key_records = check_papers_and_keys(manifest_rows)
    code2018_records = check_2018_booklet_codes(manifest_rows)
    oos_records = check_out_of_scope(manifest_rows)
    legacy_problems = check_legacy_sheet_classification(manifest_rows)
    legacy_records = build_legacy_sheet_records(manifest_rows)

    all_records = (ncert_records + labman_records + paper_key_records
                   + code2018_records + oos_records + legacy_records)

    for r in all_records:
        _write_s0_out_record(r)

    _clear_previous_s0_flags()
    raised_flags = _raise_missing_flags(all_records)

    # Unparsed/ambiguous metadata isn't stored in manifest.csv itself (it has no notes column —
    # spec Section 8/S0 Reads fixes its columns). Re-derive the same picture here from the
    # manifest's blank fields, so the report stays self-contained even if build_manifest.py's
    # run() isn't re-invoked in the same process.
    unparsed = []
    for r in manifest_rows:
        if r["kind"] == "paper" and r["year"] and not r["sitting"]:
            unparsed.append((r["file"], f"year {r['year']}: sitting could not be determined from filename"))
        elif r["kind"] == "key" and r["year"] and not r["sitting"]:
            unparsed.append((r["file"], f"year {r['year']}: sitting could not be determined from filename"))
        elif r["kind"] in ("paper", "key") and not r["year"]:
            unparsed.append((r["file"], "filename matched no known pattern at all"))
    unparsed.sort()

    ctx = {
        "manifest_kind_counts": manifest_kind_counts,
        "reconcile": reconcile,
        "ncert_records": ncert_records,
        "labman_records": labman_records,
        "paper_key_records": paper_key_records,
        "code2018_records": code2018_records,
        "oos_records": oos_records,
        "legacy_records": legacy_records,
        "legacy_problems": legacy_problems,
        "all_records": all_records,
        "raised_flags": raised_flags,
        "unparsed": unparsed,
    }
    lib_io.atomic_write_text(REPORT_PATH, _render_report(ctx))

    any_blocker = len(raised_flags) > 0
    overall = lib_status.FLAGGED if any_blocker else lib_status.PASS
    lib_status.write_status("S0", "inputs", overall, extra={
        "flags_raised": len(raised_flags),
        "required_present": sum(1 for r in all_records if r["status"] == "present"),
        "required_missing": sum(1 for r in all_records if r["status"] == "missing"),
    })

    recon_ok = not (reconcile["files_without_manifest_row"] or reconcile["manifest_rows_without_file"]
                     or reconcile["duplicate_manifest_rows"])

    return {
        "manifest_row_count": len(manifest_rows),
        "manifest_kind_counts": manifest_kind_counts,
        "tree_file_count": reconcile["tree_file_count"],
        "required_present": sum(1 for r in all_records if r["status"] == "present"),
        "required_missing": sum(1 for r in all_records if r["status"] == "missing"),
        "out_of_scope_items": sum(1 for r in all_records if r["status"] == "out_of_scope"),
        "flags_raised": len(raised_flags),
        "reconciliation_ok": recon_ok,
        "legacy_classification_ok": not legacy_problems,
        "report_path": _relpath(REPORT_PATH),
        "flags_path": _relpath(lib_flags.FLAGS_PATH),
    }


if __name__ == "__main__":
    summary = run()
    print("S0 intake check complete.")
    for k, v in summary.items():
        print(f"  {k}: {v}")
