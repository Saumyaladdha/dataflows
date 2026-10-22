#!/usr/bin/env python3
"""Builds inputs/manifest.csv for real, by walking the actual inputs/ tree and parsing each
filename according to the patterns documented in NEET_PYQ_Input_Collection_Codebook.md (the
2026-10-09 manual audit of the real data drop). It does NOT invent rows for files that don't
exist (inputs/notices/ and inputs/coaching/ are empty in this drop and correctly produce zero
rows).

Updated 2026-10-12 for two real intake defects:
  - the NCERT walk was flat (os.listdir per subject folder), so a subject whose PDFs sit in
    part-volume subfolders registered ZERO rows. Class-11 older Chemistry is exactly that shape
    (P1/ + P2/ in the source drop), so its 19 files were invisible to the manifest. Now walked
    recursively.
  - source-path probing assumed one spelling of the source subject folder ("Biology"), but
    OLD_NCERT/Class_11th spells it "Biology_class_11th" -- the folder-name sibling of the
    filename inconsistency logged on 2026-10-09. Now tries both spellings.
Together these are why Class-11 older NCERT was reported missing when 60 real chapter PDFs
existed all along.

Public entry point: run() -> (rows, unparsed)
  - writes inputs/manifest.csv (columns per spec Section 8/S0 Reads: file, kind, subject, class,
    edition, year, sitting, booklet_code, source, downloaded_on) and returns the rows written.
  - `unparsed` is a list of (file, reason) pairs for every file whose year/sitting/booklet_code
    could not be confidently determined from its filename alone. Per the task's instruction to
    "leave fields blank rather than guessing wrong", those fields are left blank in the manifest
    row itself; this list is the audit trail of *why*, since manifest.csv's own fixed column set
    (spec Section 8) has no notes column to record that inline.

Run standalone: `python3 scripts/build_manifest.py`

This is a one-off/utility builder, not one of the Sections 8-14 pipeline steps. S0
(scripts/intake_check.py) *reads* inputs/manifest.csv as ground truth; it does not regenerate
it. Re-run this script by hand if inputs/ changes (e.g. the lab manuals or Class 11 older NCERT
land later, per docs/OPEN_QUESTIONS.md).
"""
import os
import re
import sys

try:
    from scripts.lib import io as lib_io
    from scripts.lib import sittings
except ImportError:  # running as `python3 scripts/build_manifest.py` directly: scripts/ itself
    # is on sys.path, not the project root, so the `scripts.` package prefix isn't importable yet.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from scripts.lib import io as lib_io
    from scripts.lib import sittings

# The real original source tree this drop was copied from (NEET_PYQ_Input_Collection_Codebook.md
# header). Used only to recover each file's `source` column by checking whether the obvious
# original path still exists; never written to, never required to exist.
SRC_ROOT = "/Users/saumyaladdha/Downloads/Saumya_NEET_work"

NCERT_ROOT = lib_io.project_path("inputs", "ncert")
PAPERS_ROOT = lib_io.project_path("inputs", "papers")
KEYS_ROOT = lib_io.project_path("inputs", "keys")
LEGACY_ROOT = lib_io.project_path("inputs", "legacy_sheets")

MANIFEST_FIELDS = ["file", "kind", "subject", "class", "edition", "year", "sitting",
                    "booklet_code", "source", "downloaded_on"]

SUBJECT_DIRS = ("Physics", "Chemistry", "Biology")  # excludes the bonus Maths folders
# (NEET_PYQ_Input_Collection_Codebook.md Section 1: "Bonus, out of original scope"; NEET has no
# Maths paper at all, so the Maths_class_11th folder in the Class-11 older drop is not copied.)

# The source drop does NOT name its subject folders uniformly. NEW_NCERT (both classes) and
# OLD_NCERT/Class_12th use the plain subject name; OLD_NCERT/Class_11th uses
# "<Subject>_class_11th". This is the folder-name sibling of the filename inconsistency already
# logged on 2026-10-09, and it is why only the Class-11 *older* set went unnoticed: every
# source-path probe here built the plain name and silently missed. `source` is provenance only,
# so the miss cost a blank column rather than a wrong row -- but it is still a real defect.
_SOURCE_SUBJECT_DIR_VARIANTS = ("{subject}", "{subject}_class_{class_num}th")


def _relpath(full):
    return os.path.relpath(full, lib_io.PROJECT_ROOT).replace(os.sep, "/")


def _blank_row(file_rel, kind, source=""):
    return {"file": file_rel, "kind": kind, "subject": "", "class": "", "edition": "",
            "year": "", "sitting": "", "booklet_code": "", "source": source, "downloaded_on": ""}


# ---------------------------------------------------------------------------
# NCERT (one PDF per chapter; see docs/OPEN_QUESTIONS.md 2026-10-09 Section 9 A1/A2 entries)
# ---------------------------------------------------------------------------

def _guess_ncert_source(edition_dir, class_dir, subject_dir, class_num, sub_relpath):
    """Best-effort provenance: the original path this copy came from, or "" if it can't be
    confirmed on disk. Tries every real subject-folder spelling in the source drop (see
    _SOURCE_SUBJECT_DIR_VARIANTS) and preserves `sub_relpath` -- the path of the file *below*
    the subject folder, which is not always just a filename: Class-11 older Chemistry is split
    into P1/P2 part-volume subfolders in the source and is copied that way."""
    sub_root = "NEW_NCERT" if edition_dir == "latest" else "OLD_NCERT"
    for variant in _SOURCE_SUBJECT_DIR_VARIANTS:
        src_subject_dir = variant.format(subject=subject_dir, class_num=class_num)
        candidate = os.path.join(SRC_ROOT, "English_NCERT", sub_root, class_dir,
                                 src_subject_dir, *sub_relpath.split("/"))
        if os.path.exists(candidate):
            return candidate
    return ""


def _guess_labman_source(fname):
    candidate = os.path.join(SRC_ROOT, "NCERT_Manual", fname)
    return candidate if os.path.exists(candidate) else ""


def walk_ncert_rows():
    rows = []
    for edition_dir, edition_val in (("latest", "latest"), ("older", "older")):
        base = os.path.join(NCERT_ROOT, edition_dir)
        if not os.path.isdir(base):
            continue
        for class_dir in sorted(os.listdir(base)):
            class_path = os.path.join(base, class_dir)
            m = re.match(r"Class_(\d+)th$", class_dir)
            if not os.path.isdir(class_path) or not m:
                continue
            class_num = m.group(1)
            for subject_dir in sorted(os.listdir(class_path)):
                subject_path = os.path.join(class_path, subject_dir)
                if not os.path.isdir(subject_path) or subject_dir not in SUBJECT_DIRS:
                    continue
                # Walk, don't listdir: a subject folder is not always flat. Class-11 older
                # Chemistry arrives as two part-volume subfolders (P1/P2), which a flat
                # os.listdir() skips entirely -- it sees two directories and no PDFs, and
                # registers zero rows for a subject that really has 19 files. Confirmed on real
                # data. The part folders are kept rather than flattened because both volumes
                # contain a file named "1 Prelims.pdf" (flattening would collide) and because
                # the volume is what disambiguates P2's restarted chapter numbering (see
                # scripts/runner_core.py :: extract_chapter_num).
                for dirpath, dirnames, fnames in os.walk(subject_path):
                    dirnames.sort()
                    for fname in sorted(fnames):
                        if not fname.lower().endswith(".pdf"):
                            continue
                        full = os.path.join(dirpath, fname)
                        sub_relpath = os.path.relpath(full, subject_path).replace(os.sep, "/")
                        rows.append({
                            "file": _relpath(full), "kind": "ncert", "subject": subject_dir,
                            "class": class_num, "edition": edition_val, "year": "", "sitting": "",
                            "booklet_code": "",
                            "source": _guess_ncert_source(edition_dir, class_dir, subject_dir,
                                                          class_num, sub_relpath),
                            "downloaded_on": "",
                        })

    # Lab manuals. Was empty in the original drop; as of 2026-10-12 it holds the NCERT Senior
    # Secondary Microscale Chemistry Laboratory Kit manual (NCERT 2018, ISBN 978-93-5007-861-7,
    # 146 pp), reclassified here from inputs/_reference/ncert_model_kits/ after its content was
    # re-checked directly and found to be real experiment material (87 "experiment", 44
    # "apparatus", 30 "titration", 13 "observation" whole-word hits, with aim/procedure/
    # observation/precaution write-ups and a qualitative-analysis section). Physics still has
    # none, and that gap stays open.
    labman_base = os.path.join(NCERT_ROOT, "lab_manuals")
    if os.path.isdir(labman_base):
        for root, _dirs, fnames in os.walk(labman_base):
            for fname in sorted(fnames):
                if not fname.lower().endswith(".pdf"):
                    continue
                full = os.path.join(root, fname)
                # Match on the path *below* inputs/ (never the absolute path): the absolute path
                # includes the machine's home/checkout directories, so an unrelated ancestor
                # folder containing "phys" or "chem" would silently decide a manual's subject.
                low = os.path.relpath(full, lib_io.project_path("inputs")).lower()
                subject = "Physics" if "phys" in low else ("Chemistry" if "chem" in low else "")
                rows.append({
                    "file": _relpath(full), "kind": "lab_manual", "subject": subject,
                    "class": "", "edition": "lab_manual", "year": "", "sitting": "",
                    "booklet_code": "", "source": _guess_labman_source(fname),
                    "downloaded_on": "",
                })
    return rows


# ---------------------------------------------------------------------------
# Papers (inputs/papers/) — filenames are genuinely inconsistent; see Codebook Section 2.
# ---------------------------------------------------------------------------

_CODE_RE = re.compile(r"^neet_(\d{4})_code-(.+)\.pdf$", re.IGNORECASE)
_WHOLE_YEAR_RE = re.compile(r"^(\d{4})\.pdf$")
_AIPMT_YEAR_ONLY_RE = re.compile(r"^AIPMT (\d{4})\.pdf$", re.IGNORECASE)
_AIPMT_PRELIM_RE = re.compile(r"^AIPMT-(\d{4})-Preliminary", re.IGNORECASE)
_AIPMT_MAIN_WORD_RE = re.compile(r"^AIPMT-(\d{4})-Main", re.IGNORECASE)
_AIPMT_ALLEN_RE = re.compile(r"^AIPMT_(\d{4})_NEET_UG", re.IGNORECASE)
_AIPMT_LOWER_MAIN_RE = re.compile(r"^aipmt-(\d{4})-main\.pdf$", re.IGNORECASE)


def _sitting_for_bare_year(year):
    """A filename with no sitting marker at all. Safe to call it MAIN only when that year has
    exactly one official sitting (or isn't on the 2016-2026 calendar at all, in which case there
    is still only ever one file per year in this drop, so the same single-sitting read applies).
    Otherwise leave it blank rather than guess which of the two it is."""
    if year in sittings.MULTI_SITTING_YEARS:
        required = "/".join(sittings.REQUIRED_SITTINGS[year])
        return "", (f"{year} has more than one official sitting ({required}) and this filename "
                     f"has no marker distinguishing which; left blank")
    return "MAIN", ""


def parse_paper_filename(fname):
    """Return dict(year, sitting, booklet_code, note) or None if the filename matches no known
    pattern at all. Never guesses a sitting it isn't confident about (task instruction: leave
    blank rather than guess wrong)."""
    m = _CODE_RE.match(fname)
    if m:
        year, code = int(m.group(1)), m.group(2)
        sitting, note = _sitting_for_bare_year(year)
        return {"year": year, "sitting": sitting, "booklet_code": code, "note": note}

    m = _WHOLE_YEAR_RE.match(fname)
    if m:
        year = int(m.group(1))
        sitting, note = _sitting_for_bare_year(year)
        return {"year": year, "sitting": sitting, "booklet_code": "", "note": note}

    m = _AIPMT_YEAR_ONLY_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "MAIN", "booklet_code": "", "note": ""}

    m = _AIPMT_PRELIM_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "", "booklet_code": "",
                "note": "AIPMT's 'Preliminary' stage has no matching value in the spec's sitting "
                        "enum (MAIN/PH2/REEXAM/RETEST/CANCELLED); left blank"}

    m = _AIPMT_MAIN_WORD_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "MAIN", "booklet_code": "", "note": ""}

    m = _AIPMT_ALLEN_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "MAIN", "booklet_code": "",
                "note": "filename indicates a coaching (ALLEN) transcription, not confirmed as "
                        "an official scan — flag for B1 trust assessment later"}

    m = _AIPMT_LOWER_MAIN_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "MAIN", "booklet_code": "", "note": ""}

    return None


def _guess_paper_source(fname, parsed):
    if parsed and parsed.get("booklet_code"):
        candidate = os.path.join(SRC_ROOT, "all_neet_sets_and_ans_key", str(parsed["year"]),
                                  f"code-{parsed['booklet_code']}", fname)
        if os.path.exists(candidate):
            return candidate
    candidate = os.path.join(SRC_ROOT, "NEET_PYQ", "Paper", fname)
    return candidate if os.path.exists(candidate) else ""


# ---------------------------------------------------------------------------
# Keys (inputs/keys/)
# ---------------------------------------------------------------------------

_KEY_PHASE_RE = re.compile(r"^NEET_answers-key_(\d{4})-phase-(\d)\.pdf$", re.IGNORECASE)
_KEY_REEXAM_RE = re.compile(r"^NEET_answers-key_(\d{4})-Re_neet\.pdf$", re.IGNORECASE)
_KEY_CODE_RE = re.compile(r"^NEET_answers-key_(\d{4})-([A-Z]{2})\.pdf$")
_KEY_NEET_SUFFIX_RE = re.compile(r"^NEET_answers-key_(\d{4})-neet\.pdf$", re.IGNORECASE)
_KEY_YEAR_ONLY_RE = re.compile(r"^NEET_answers-key_(\d{4})\.pdf$")


def parse_key_filename(fname):
    m = _KEY_PHASE_RE.match(fname)
    if m:
        year, phase = int(m.group(1)), m.group(2)
        return {"year": year, "sitting": "MAIN" if phase == "1" else "PH2",
                "booklet_code": "", "note": ""}

    m = _KEY_REEXAM_RE.match(fname)
    if m:
        return {"year": int(m.group(1)), "sitting": "REEXAM", "booklet_code": "", "note": ""}

    m = _KEY_CODE_RE.match(fname)
    if m:
        year, code = int(m.group(1)), m.group(2)
        sitting, note = _sitting_for_bare_year(year)
        return {"year": year, "sitting": sitting, "booklet_code": code, "note": note}

    m = _KEY_NEET_SUFFIX_RE.match(fname)
    if m:
        year = int(m.group(1))
        sitting, note = _sitting_for_bare_year(year)
        if not sitting:
            note = (f"{year} key is a single whole-year file that doesn't split by sitting "
                     f"({sittings.REQUIRED_SITTINGS.get(year)}); cannot confirm which sitting(s) "
                     f"it covers — see Codebook Section 3 open question")
        return {"year": year, "sitting": sitting, "booklet_code": "", "note": note}

    m = _KEY_YEAR_ONLY_RE.match(fname)
    if m:
        year = int(m.group(1))
        sitting, note = _sitting_for_bare_year(year)
        return {"year": year, "sitting": sitting, "booklet_code": "", "note": note}

    return None


def _guess_key_source(fname):
    candidate = os.path.join(SRC_ROOT, "NEET_PYQ", "NEET_official_Answer_key", fname)
    return candidate if os.path.exists(candidate) else ""


# ---------------------------------------------------------------------------
# Legacy sheets (inputs/legacy_sheets/) — never fed to any agent (spec Section 2.2/13)
# ---------------------------------------------------------------------------

_LEGACY_YEAR_RE = re.compile(r"(\d{4})")


def _guess_legacy_source(fname):
    candidate = os.path.join(SRC_ROOT, "NEET_PYQ", "Excel", fname)
    return candidate if os.path.exists(candidate) else ""


# ---------------------------------------------------------------------------

def run():
    rows = []
    unparsed = []  # [(file, reason)]

    rows.extend(walk_ncert_rows())

    if os.path.isdir(PAPERS_ROOT):
        for fname in sorted(os.listdir(PAPERS_ROOT)):
            full = os.path.join(PAPERS_ROOT, fname)
            if not os.path.isfile(full) or not fname.lower().endswith(".pdf"):
                continue
            relf = _relpath(full)
            parsed = parse_paper_filename(fname)
            if parsed is None:
                rows.append(_blank_row(relf, "paper", _guess_paper_source(fname, None)))
                unparsed.append((relf, "filename matches no known paper pattern at all; "
                                        "year/sitting/booklet_code left blank"))
                continue
            rows.append({
                "file": relf, "kind": "paper", "subject": "", "class": "", "edition": "",
                "year": str(parsed["year"]), "sitting": parsed["sitting"],
                "booklet_code": parsed["booklet_code"],
                "source": _guess_paper_source(fname, parsed), "downloaded_on": "",
            })
            if parsed.get("note"):
                unparsed.append((relf, parsed["note"]))

    if os.path.isdir(KEYS_ROOT):
        for fname in sorted(os.listdir(KEYS_ROOT)):
            full = os.path.join(KEYS_ROOT, fname)
            if not os.path.isfile(full) or not fname.lower().endswith(".pdf"):
                continue
            relf = _relpath(full)
            parsed = parse_key_filename(fname)
            if parsed is None:
                rows.append(_blank_row(relf, "key", _guess_key_source(fname)))
                unparsed.append((relf, "filename matches no known key pattern at all; "
                                        "year/sitting/booklet_code left blank"))
                continue
            rows.append({
                "file": relf, "kind": "key", "subject": "", "class": "", "edition": "",
                "year": str(parsed["year"]), "sitting": parsed["sitting"],
                "booklet_code": parsed["booklet_code"],
                "source": _guess_key_source(fname), "downloaded_on": "",
            })
            if parsed.get("note"):
                unparsed.append((relf, parsed["note"]))

    if os.path.isdir(LEGACY_ROOT):
        for fname in sorted(os.listdir(LEGACY_ROOT)):
            full = os.path.join(LEGACY_ROOT, fname)
            if not os.path.isfile(full) or not fname.lower().endswith(".xlsx"):
                continue
            relf = _relpath(full)
            m = _LEGACY_YEAR_RE.search(fname)
            rows.append({
                "file": relf, "kind": "legacy_sheet", "subject": "", "class": "", "edition": "",
                "year": m.group(1) if m else "", "sitting": "", "booklet_code": "",
                "source": _guess_legacy_source(fname), "downloaded_on": "",
            })

    # inputs/notices/ and inputs/coaching/ are empty in this drop (confirmed) — no rows invented
    # for files that don't exist. inputs/ncert/lab_manuals/ is no longer empty (see
    # walk_ncert_rows) but is still missing Physics.

    out_path = lib_io.project_path("inputs", "manifest.csv")
    lib_io.write_csv(out_path, rows, MANIFEST_FIELDS)
    return rows, unparsed


if __name__ == "__main__":
    written_rows, ambiguous = run()
    print(f"Wrote {len(written_rows)} rows to inputs/manifest.csv")
    by_kind = {}
    for row in written_rows:
        by_kind[row["kind"]] = by_kind.get(row["kind"], 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")
    print(f"\n{len(ambiguous)} file(s) with incomplete/ambiguous metadata (left blank, not guessed):")
    for f, reason in ambiguous:
        print(f"  {f}\n    -> {reason}")
