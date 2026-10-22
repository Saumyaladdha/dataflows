#!/usr/bin/env python3
"""Two deliverable workbooks, distinct from the review workbook.

    python3 scripts/build_final_exports.py

Writes into exports/<today>/:

  final_data.xlsx   The BANK ITSELF -- the actual output, one row per question with everything
                    known about it, plus the NCERT material it is anchored to. This is the thing
                    the project exists to produce.

  data_steps.xlsx   The PIPELINE AUDIT -- one row per step saying, in plain English, what that
                    step was GIVEN, what it EXTRACTED, where it saved it, how many items it has
                    processed, and a REAL sample value taken from live data so the shape of the
                    output is visible rather than described.

Why three workbooks and not one: they answer different questions. `pipeline_review.xlsx` asks
"what needs attention?", `final_data.xlsx` asks "what have we produced?", and `data_steps.xlsx`
asks "what does each step actually do to the data?". Merging them would bury each.

NOT A RELEASE. Spec Section 14/F5 reserves released output for `export_tables.py` -> `data/`,
and only for a chapter whose review queue is empty and which has a sign-off row in
`review/releases.csv`. None of that has happened. Every row here still carries its flags and
confidence so nothing can be mistaken for approved data.
"""
import argparse
import collections
import datetime
import json
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import runner_core as rc  # noqa: E402
from lib import io as lib_io  # noqa: E402

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

RED = PatternFill("solid", fgColor="F8D7DA")
AMBER = PatternFill("solid", fgColor="FFF3CD")
GREEN = PatternFill("solid", fgColor="D6EFD8")
GREY = PatternFill("solid", fgColor="E9ECEF")
HEAD = PatternFill("solid", fgColor="1F3A5F")
F_HEAD = Font(bold=True, color="FFFFFF", size=11)
F_TITLE = Font(bold=True, size=14, color="1F3A5F")
F_NOTE = Font(italic=True, size=10, color="444444")
F_BOLD = Font(bold=True)
THIN = Side(style="thin", color="BBBBBB")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def _read_jsonl(p):
    if not os.path.exists(p):
        return []
    out = []
    with open(p, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def _read_json(p):
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _flat(v, limit=None):
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        s = " | ".join(_flat(x) for x in v)
    elif isinstance(v, dict):
        s = json.dumps(v, ensure_ascii=False, sort_keys=True)
    else:
        s = str(v)
    return s[:limit] if limit else s


def _sheet(wb, title, heading, what, look):
    ws = wb.create_sheet(title[:31])
    ws["A1"] = heading
    ws["A1"].font = F_TITLE
    ws["A2"] = f"WHAT THIS IS:  {what}"
    ws["A2"].font = F_NOTE
    ws["A3"] = f"WHAT TO LOOK AT:  {look}"
    ws["A3"].font = F_NOTE
    ws.freeze_panes = "A6"
    return ws


def _write(ws, start, cols, rows, fills=None, widths=None):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=start, column=i, value=c)
        cell.fill, cell.font, cell.border = HEAD, F_HEAD, BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[start].height = 30
    r = start + 1
    for item in rows:
        rf = fills(item) if fills else {}
        for i, c in enumerate(cols, 1):
            cell = ws.cell(row=r, column=i, value=item.get(c, ""))
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=(i > 1))
            if c in rf:
                cell.fill = rf[c]
        r += 1
    for i, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(c, 18)


def _records():
    d = rc.pp("papers", "records")
    out = []
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.startswith("Q-") and fn.endswith(".json"):
                r = _read_json(os.path.join(d, fn))
                if r:
                    out.append(r)
    return out


# ===========================================================================
# Plain-English meanings. Anyone reading an export should not have to find the
# spec to learn what a code means, so every status and every flag code the
# pipeline can raise is explained here in one sentence, with what to do about it.
# ===========================================================================

_STATUS_MEANING = {
    "pass": ("Done and checked", "Nothing to do."),
    "flagged": ("Done, but the pipeline is unsure about something",
                "A person should confirm it. The value is usable meanwhile."),
    "blocked": ("Could not finish", "Something it needed was missing. Fix that, then re-run."),
    "skipped": ("Did not apply to this item", "Nothing to do; this is normal."),
    "stale": ("Was done, but an input changed underneath it", "It will re-run automatically."),
}

_FLAG_MEANING = {
    "S0_MISSING_INPUT": ("A file the project needs was not supplied",
                         "Source the file. Until then anything depending on it cannot run."),
    "A1_REGISTER_DRAFT": ("Every registered book starts as a draft",
                          "Routine. Confirm the edition line at review."),
    "A2_CHECK_FAILED": ("A page reading failed its automatic check",
                        "Look at the page; it may need re-reading."),
    "A2_JOIN_ADJUDICATED": ("Two pages disagreed about whether text continues across the break",
                            "Usually harmless — figures interrupt the flow. Confirm at review."),
    "A2_TEXT_MISMATCH": ("The transcription did not match the page's own text layer closely enough",
                         "Often a false alarm on heading-heavy pages. Check a sample."),
    "A4_SUBTOPICS_DRAFT": ("A chapter's subtopic list needs approval before it is used for real",
                           "Faculty should approve the list."),
    "B1_REGISTER_DRAFT": ("Every registered paper starts as a draft",
                          "Routine. Confirm year/sitting/code at review."),
    "B4_MISMATCH_ADJUDICATED": ("Two independent readings of the question disagreed",
                                "The disagreement was resolved automatically — worth spot-checking."),
    "B6_IMAGE_INPUT_UNSAFE": ("The blind solver refused this question because it needs a figure",
                              "Deliberate: the only image available also shows the answer. "
                              "Now that figures are recovered, these could be re-tried."),
    "B8_CORRECTION": ("The exam board dropped or bonused this question; a correction was proposed",
                      "Faculty must confirm the correction before it is used."),
    "B9_FIGURE_RECOVERED": ("A missing figure was found in the legacy sheets and attached",
                            "Confirm the picture matches the question."),
    "B9_FIGURE_EXTRA_IMAGES": ("The source row had more than one image; only the first was attached",
                               "Check whether the unused image was actually needed."),
    "B9_FIGURE_UNMATCHED": ("No figure could be confidently matched to this question",
                            "The question stays without its diagram."),
    "B9_FIGURE_THIN_MARGIN": ("The match was accepted but the runner-up was close behind",
                              "Worth a quick look at the attached picture."),
    "D1_NO_CHAPTERS": ("No NCERT chapter for this subject has been indexed yet",
                       "Index the subject's chapters. Nothing can be mapped until then."),
    "D1_GUESS": ("Both attempts and the adjudicator were unsure which chapter this tests",
                 "Usually means the real chapter is not indexed yet. Treat the chapter as unreliable."),
    "D2_GUESS": ("Same as D1_GUESS, for the subtopic", "Treat the subtopic as unreliable."),
    "D3_NO_PASSAGES": ("The chosen subtopic has no textbook passages linked to it",
                       "Nothing can be quoted as evidence. Usually a subtopic that was drafted "
                       "but never linked."),
    "C1_UNMATCHED": ("A question in one booklet code had no twin in the other", "Kept separate."),
    "C1_KEY_INCONSISTENT": ("Two codes' keys point at different answers for the same question",
                            "Serious — check the key reading for that sitting."),
    "C1_READING_FIXED": ("Two codes disagreed; an adjudicator decided one reading was a misread",
                         "Confirm the merge is right."),
    "E4_NO_CODEBOOK": ("Thinking tags were produced without the owner's codebook",
                       "Tags are provisional until the codebook exists and they are re-run."),
}


# ===========================================================================
# The full target schema, straight from SPEC Section 6.3's question record.
# (column, group, which step fills it, record field, one-line meaning)
# Columns whose step has not run yet still appear, empty -- so the shape of a
# finished question is visible, and the gaps are explicit rather than absent.
# ===========================================================================

_COLUMNS = [
    # --- identity -----------------------------------------------------------
    ("question id",        "Identity", "B3",  "question_id",      "Our permanent id for this question"),
    ("exam",               "Identity", "B1",  "exam",             "NEET or AIPMT"),
    ("year",               "Identity", "B1",  "year",             "Exam year"),
    ("sitting",            "Identity", "B1",  "sitting",          "MAIN / PH2 / REEXAM"),
    ("paper codes",        "Identity", "B1",  "paper_codes",      "Which booklet codes it appeared in, and at what number"),
    ("option map",         "Identity", "C1",  "option_map",       "How options line up between booklet codes"),
    ("merged from",        "Identity", "C1",  "merged_from",      "Duplicate records folded into this one"),
    # --- classification -----------------------------------------------------
    ("subject",            "Subject",  "B7",  "subject",          "Physics / Chemistry / Biology"),
    ("branch",             "Subject",  "B7",  "branch",           "Chemistry: physical/organic/inorganic. Biology: botany/zoology"),
    # --- the question itself ------------------------------------------------
    ("question",           "Content",  "B3",  "stem_en",          "The question text, copied word for word"),
    ("statements",         "Content",  "B3",  "statements",       "Lettered statements, if any"),
    ("list I",             "Content",  "B3",  "list_i",           "Left-hand list in a match question"),
    ("list II",            "Content",  "B3",  "list_ii",          "Right-hand list in a match question"),
    ("option 1",           "Content",  "B3",  None,               "Option 1 text"),
    ("option 2",           "Content",  "B3",  None,               "Option 2 text"),
    ("option 3",           "Content",  "B3",  None,               "Option 3 text"),
    ("option 4",           "Content",  "B3",  None,               "Option 4 text"),
    ("shape",              "Content",  "B3",  "structure",        "plain / statements / lists"),
    ("negative words",     "Content",  "B3",  "negative_words",   "NOT, EXCEPT, INCORRECT... — these flip what is being asked"),
    ("needs a figure",     "Content",  "B3",  "has_figure",       "Whether the question cannot be answered without a diagram"),
    ("figure recovered",   "Content",  "B9",  "figure_path",      "The diagram, recovered from the legacy sheets"),
    # --- the answer ---------------------------------------------------------
    ("correct answer",     "Answer",   "B5",  "official_answer",  "Option number, from the official NTA key"),
    ("correct answer text", "Answer",  "B5",  None,               "What that option actually says — the number alone is not readable"),
    ("answer source",      "Answer",   "B5",  "answer_source",    "Which key file it came from"),
    ("official status",    "Answer",   "B5",  "status",           "normal / dropped / bonus / multiple accepted"),
    ("why faulty",         "Answer",   "B8",  "issue_reason",     "If dropped or bonused, what was wrong with it"),
    ("corrected answer",   "Answer",   "B8",  "corrected_answer", "Proposed fix for a faulty question"),
    ("latest answer",      "Answer",   "D7",  "latest_answer",    "The answer by TODAY'S textbook — can differ from the official one"),
    ("answer changed",     "Answer",   "D7",  "answer_changed",   "True if the textbook changed and the answer moved with it"),
    # --- independent check --------------------------------------------------
    ("blind answer",       "Check",    "B6",  "b6_answer",        "Answered independently, never having seen the key"),
    ("blind agrees",       "Check",    "B6",  "b6_agrees_with_key", "Whether that independent answer matched the official one"),
    ("blind confidence",   "Check",    "B6",  "b6_confidence",    "How sure the independent solver was"),
    ("blind reasoning",    "Check",    "B6",  "b6_reason",        "Its reasoning — useful when it disagrees"),
    # --- where it sits in NCERT ---------------------------------------------
    ("NCERT chapter",      "Mapping",  "D1",  "d1_chapter_ids",   "Which textbook chapter it tests"),
    ("chapter confidence", "Mapping",  "D1",  "d1_confidence",    "How sure that chapter pick is"),
    ("NCERT subtopic",     "Mapping",  "D2",  "d2_subtopic_ids",  "Which subtopic within the chapter"),
    ("link type",          "Mapping",  "D4",  "link_type",        "How the answer connects: stated outright / a rule applied / beyond NCERT"),
    ("evidence quote",     "Mapping",  "D4",  None,               "The exact NCERT line proving the answer, verified word for word"),
    ("derivation steps",   "Mapping",  "D4",  "derivation_steps", "The maths between the quoted rule and the answer"),
    ("evidence covers",    "Mapping",  "D4",  "covers",           "fully / partly / not at all"),
    ("older edition line", "Mapping",  "D5",  "older_evidence",   "The same fact in the previous textbook edition"),
    ("syllabus status",    "Mapping",  "D6",  "syllabus_status",  "In the current book / removed / outside NCERT"),
    ("note type",          "Mapping",  "D6",  "note_type",        "How to describe the edition situation to a student"),
    ("reason note",        "Mapping",  "D6",  "reason_note",      "That explanation, written out"),
    # --- repeats ------------------------------------------------------------
    ("fact line",          "Repeats",  "D8",  "fact_line",        "The one fact this question tests, in plain words"),
    ("repeat group",       "Repeats",  "D11", "repeat_group_id",  "Questions across years that test the same thing"),
    ("repeat label",       "Repeats",  "D11", "repeat_label",     "exact same / reworded / same fact new format / same problem new numbers"),
    ("related questions",  "Repeats",  "D11", "related_ids",      "Related but not a repeat"),
    # --- tagging ------------------------------------------------------------
    ("question type",      "Tags",     "E1",  "question_type",    "How the question is BUILT (assertion-reason, match the lists...)"),
    ("format",             "Tags",     "E2",  "format",           "What the student must PICK (correct / incorrect / calculate...)"),
    ("content shape",      "Tags",     "E3",  "content_shape",    "What NCERT material it is built on (a formula, a process, a table...)"),
    ("thinking (primary)", "Tags",     "E4",  "category_primary", "What the student must DO IN THEIR HEAD"),
    ("thinking (second)",  "Tags",     "E4",  "category_secondary", "A secondary thinking demand, if any"),
    ("option traps",       "Tags",     "E5",  "option_traps",     "Why each WRONG option is tempting"),
    ("stem context",       "Tags",     "E6",  "stem_context",     "plain / experiment / data given / reaction given..."),
    ("answer form",        "Tags",     "E6",  "answer_form",      "term / number with unit / ratio / combination code..."),
    ("negation",           "Tags",     "E6",  "negation",         "none / single / double"),
    ("item count",         "Tags",     "E6",  "item_count",       "How many lettered items it asks about"),
    ("constants given",    "Tags",     "E6",  "constants_given",  "Whether the stem supplies constants"),
    ("figure role",        "Tags",     "E6",  "figure_role",      "none / needed / decorative / options are figures"),
    ("codebook version",   "Tags",     "E*",  "codebook_version", "Which codebook produced these tags"),
    # --- provenance and review ----------------------------------------------
    ("source trust",       "Source",   "B1",  "trust",            "official = an NTA document; unsure = a third-party copy"),
    ("source file",        "Source",   "B1",  "source_file",      "The file the question was read from"),
    ("legacy chapter",     "Source",   "E*",  "legacy_chapter",   "What the old coaching sheet called it (shown for comparison, never used)"),
    ("review status",      "Review",   "F2",  "review_status",    "Whether a person has checked this question"),
    ("release status",     "Review",   "F5",  "release_status",   "Whether it has been released"),
]


def _why_incomplete(r, open_codes):
    """One plain sentence saying what is missing from this row and why, or '' if nothing is."""
    bits = []
    if not r.get("official_answer") and r.get("status") in ("dropped", "bonus"):
        bits.append("the exam board dropped this question, so there is no official answer")
    if r.get("b6_answer") is None:
        bits.append("the blind check could not run"
                    + (" (needs a figure)" if r.get("has_figure") else ""))
    if "D1_NO_CHAPTERS" in open_codes:
        bits.append("its subject's NCERT chapters are not indexed yet, so it cannot be mapped")
    elif "D1_GUESS" in open_codes or "D2_GUESS" in open_codes:
        bits.append("the chapter/subtopic is a low-confidence guess, probably because the real "
                    "chapter is not indexed")
    if "D3_NO_PASSAGES" in open_codes:
        bits.append("no textbook passages are linked to its subtopic, so no evidence can be quoted")
    if not r.get("d4_evidence"):
        bits.append("no NCERT evidence line has been quoted yet")
    if not r.get("subject"):
        bits.append("its subject could not be detected")
    return "; ".join(bits)


# ===========================================================================
# final_data.xlsx  --  the bank itself
# ===========================================================================

def build_final(path, flags_by_item):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    recs = [r for r in _records() if not r.get("merged_into")]

    ws = _sheet(wb, "Questions", "THE QUESTION BANK",
                "Every unique question, with its answer, where it comes from, and what the "
                "pipeline has worked out about it. Duplicates across booklet codes are already "
                "merged, so one row = one real question.",
                "'confidence' and 'open flags' tell you how much to trust the row. A row with a "
                "blocker flag is NOT finished data.")
    def _col_value(r, col, field, opts, ans, open_codes):
        """Fill one column from the record, with the few that need assembling handled here."""
        special = {
            "option 1": opts.get("1"), "option 2": opts.get("2"),
            "option 3": opts.get("3"), "option 4": opts.get("4"),
            "correct answer text": opts.get(str(ans)) if ans else "",
            "evidence quote": [e.get("exact_line") for e in (r.get("d4_evidence") or [])
                               if isinstance(e, dict)],
            "blind agrees": r.get("b6_agrees_with_key"),
            "needs a figure": "yes" if r.get("has_figure") else "",
            "figure recovered": os.path.basename(r["figure_path"]) if r.get("figure_path") else "",
            "source file": os.path.basename(_flat(r.get("source_file"))),
            "review status": r.get("review_status") or "not reviewed",
            "release status": r.get("release_status") or "unreleased",
        }
        if col in special:
            return _flat(special[col], 400)
        if col == "statements":
            st = r.get("statements") or []
            if st and isinstance(st[0], dict):
                st = [f"{s.get('label','')}. {s.get('text','')}".strip() for s in st]
            return _flat(st, 400)
        return _flat(r.get(field), 400) if field else ""

    rows = []
    for r in recs:
        opts = r.get("options_en") or {}
        ans = r.get("official_answer")
        qid = r.get("question_id")
        open_codes = [f["code"] for f in flags_by_item.get(qid, []) if f.get("status") == "open"]
        worst = ""
        sev_order = {"blocker": 3, "high": 2, "normal": 1, "low": 0}
        if open_codes:
            worst = max((f.get("severity", "low") for f in flags_by_item.get(qid, [])
                         if f.get("status") == "open"), key=lambda s: sev_order.get(s, 0))
        stmts = r.get("statements") or []
        if stmts and isinstance(stmts[0], dict):
            stmts = [f"{s.get('label','')}. {s.get('text','')}".strip() for s in stmts]
        row = {c: _col_value(r, c, f, opts, ans, open_codes) for c, _g, _s, f, _d in _COLUMNS}
        row["open flags"] = _flat(open_codes)
        row["worst flag"] = worst
        row["WHAT IS MISSING / WHY"] = _why_incomplete(r, open_codes)
        rows.append(row)
    ws.cell(row=4, column=1, value=f"{len(rows)} unique questions").font = F_BOLD
    cols = [c for c, _g, _s, _f, _d in _COLUMNS] + ["open flags", "worst flag",
                                                    "WHAT IS MISSING / WHY"]
    widths = {"question": 62, "statements": 44, "option 1": 22, "option 2": 22, "option 3": 22,
              "option 4": 22, "correct answer text": 24, "evidence quote": 50,
              "answer source": 24, "open flags": 26, "question id": 12, "year": 7,
              "blind reasoning": 55, "WHAT IS MISSING / WHY": 78, "source file": 22,
              "reason note": 40, "fact line": 40, "option traps": 36, "list I": 24,
              "list II": 24, "older edition line": 34, "derivation steps": 30}
    _write(ws, 6, cols, rows,
           fills=lambda x: {
               "worst flag": {"blocker": RED, "high": AMBER, "normal": AMBER}.get(
                   x["worst flag"], GREEN if not x["open flags"] else AMBER),
               "blind agrees": GREEN if x.get("blind agrees") == "True" else AMBER,
               "evidence quote": GREEN if x.get("evidence quote") else AMBER,
               "figure recovered": GREEN if x.get("figure recovered") else
                   (AMBER if x.get("needs a figure") else GREY),
               "chapter confidence": AMBER if x.get("chapter confidence") in ("low", "") else GREEN,
               "source trust": GREEN if x.get("source trust") == "official" else AMBER,
               "branch": AMBER if x.get("branch") in ("unsure",) else GREY,
               "WHAT IS MISSING / WHY": GREEN if not x["WHAT IS MISSING / WHY"] else AMBER,
               **{c: GREY for c, _g, _s, _f, _d in _COLUMNS if not x.get(c)},
           }, widths=widths)

    # ---- column guide: what every column is, and whether it is filled yet ----
    wsg = _sheet(wb, "Column guide", "WHAT EVERY COLUMN MEANS",
                 "The full shape of a finished question, straight from the spec. Columns whose "
                 "step has not run yet are listed too, so the gaps are visible rather than absent.",
                 "'filled for' tells you how many of the questions actually have that value. "
                 "0 means that step has not produced anything yet.")
    grows = []
    for c, group, step, _f, desc in _COLUMNS:
        filled = sum(1 for x in rows if str(x.get(c, "")).strip())
        grows.append({"group": group, "column": c, "filled by step": step,
                      "what it means": desc,
                      "filled for": f"{filled} of {len(rows)}",
                      "state": "filled" if filled else "step has not run yet"})
    _write(wsg, 6, ["group", "column", "filled by step", "what it means", "filled for", "state"],
           grows,
           fills=lambda r: {"state": GREEN if r["state"] == "filled" else GREY,
                            "filled for": GREEN if not r["filled for"].startswith("0 ") else GREY},
           widths={"group": 12, "column": 22, "filled by step": 13, "what it means": 82,
                   "filled for": 12, "state": 22})

    # ---- the NCERT material behind the answers ------------------------------
    ws2 = _sheet(wb, "NCERT passages", "THE NCERT TEXT WE CAN QUOTE FROM",
                 "Every passage indexed out of the real textbooks. Answers are proved by quoting "
                 "these word for word.",
                 "If a chapter you care about is absent here, no question from it can be mapped.")
    prows = []
    pdir = rc.pp("ncert", "passages")
    for fn in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if fn.endswith(".jsonl"):
            for p_ in _read_jsonl(os.path.join(pdir, fn)):
                prows.append({"passage id": _flat(p_.get("passage_id")),
                              "book": _flat(p_.get("book_id")),
                              "chapter": _flat(p_.get("chapter_id")),
                              "heading": _flat(p_.get("section_heading"), 70),
                              "page": _flat(p_.get("page_start")),
                              "kind": _flat(p_.get("kind")),
                              "text": _flat(p_.get("text"))})
    ws2.cell(row=4, column=1, value=f"{len(prows)} passages").font = F_BOLD
    _write(ws2, 6, ["passage id", "book", "chapter", "heading", "page", "kind", "text"], prows,
           widths={"passage id": 20, "book": 10, "chapter": 14, "heading": 38, "page": 7,
                   "kind": 11, "text": 115})

    # ---- where it all came from ---------------------------------------------
    ws3 = _sheet(wb, "Sources", "WHERE EVERYTHING CAME FROM",
                 "The books and papers behind the bank, and how far each is trusted.",
                 "'trust' = official means an official NTA document. The papers are currently "
                 "third-party copies, which is why they read 'unsure'.")
    srows = []
    for b in (lib_io.read_csv(rc.pp("register", "books.csv"))
              if os.path.exists(rc.pp("register", "books.csv")) else []):
        srows.append({"kind": "NCERT book", "id": _flat(b.get("book_id")),
                      "detail": f"{_flat(b.get('subject'))} class {_flat(b.get('class'))} "
                                f"({_flat(b.get('edition'))})",
                      "edition / trust": _flat(b.get("reprint_text_exact")),
                      "state": _flat(b.get("status"))})
    for pr in (lib_io.read_csv(rc.pp("register", "papers.csv"))
               if os.path.exists(rc.pp("register", "papers.csv")) else []):
        srows.append({"kind": _flat(pr.get("file_kind")), "id": _flat(pr.get("paper_id")),
                      "detail": f"{_flat(pr.get('year'))} {_flat(pr.get('sitting'))} "
                                f"code {_flat(pr.get('booklet_code')) or '?'}",
                      "edition / trust": _flat(pr.get("trust")),
                      "state": _flat(pr.get("status"))})
    _write(ws3, 6, ["kind", "id", "detail", "edition / trust", "state"], srows,
           fills=lambda x: {"edition / trust": GREEN if x["edition / trust"] == "official"
                            else (AMBER if x["kind"] in ("paper", "key") else GREEN)},
           widths={"kind": 14, "id": 24, "detail": 34, "edition / trust": 24, "state": 10})

    # ---- where it went wrong -------------------------------------------------
    ws4 = _sheet(wb, "Where it went wrong", "WHERE THINGS WENT WRONG",
                 "One row per problem, newest concern first. This is the list to work through.",
                 "'what it means' and 'what to do' are plain English — you should not need the "
                 "spec to act on a row.")
    sev_rank = {"blocker": 0, "high": 1, "normal": 2, "low": 3}
    wrows = []
    for qid, fl in flags_by_item.items():
        for f in fl:
            if f.get("status") != "open":
                continue
            code = f.get("code", "")
            meaning, todo = _FLAG_MEANING.get(code, ("", "Check the message."))
            wrows.append({"severity": f.get("severity", ""), "step": f.get("step", ""),
                          "item": _flat(qid), "code": code,
                          "what it means": meaning,
                          "what to do": todo,
                          "the pipeline's own message": _flat(f.get("message"), 320)})
    wrows.sort(key=lambda r: (sev_rank.get(r["severity"], 9), r["step"], r["code"]))
    counts = collections.Counter(r["severity"] for r in wrows)
    ws4.cell(row=4, column=1,
             value="  ".join(f"{k}: {counts.get(k, 0)}"
                             for k in ("blocker", "high", "normal", "low"))).font = F_BOLD
    _write(ws4, 6, ["severity", "step", "item", "code", "what it means", "what to do",
                    "the pipeline's own message"], wrows,
           fills=lambda r: {"severity": {"blocker": RED, "high": AMBER,
                                         "normal": AMBER}.get(r["severity"], GREY)},
           widths={"severity": 10, "step": 7, "item": 26, "code": 26, "what it means": 56,
                   "what to do": 56, "the pipeline's own message": 70})

    # ---- journey of each question -------------------------------------------
    ws5 = _sheet(wb, "Question journey", "EACH QUESTION, STEP BY STEP",
                 "Follow one question across every step that touched it, and see exactly where "
                 "it stopped.",
                 "Read a row left to right. The first non-green cell is where that question got "
                 "stuck.")
    journey_steps = [("B3", "read"), ("B4", "re-read"), ("B5", "key"), ("B6", "blind solve"),
                     ("B7", "subject"), ("B8", "faulty?"), ("B9", "figure"), ("C1", "duplicate"),
                     ("D1", "chapter"), ("D2", "subtopic"), ("D3", "passages"), ("D4", "evidence")]
    jrows = []
    for r in recs:
        qid = r.get("question_id")
        row = {"question id": _flat(qid), "question": _flat(r.get("stem_en"), 90)}
        stopped = ""
        for code, label in journey_steps:
            st = (rc.read_item_status(code, qid) or {}).get("status")
            if st is None:
                # C1 keys items by a pair id, not a single qid; look for a merge instead.
                if code == "C1":
                    st = "merged" if r.get("merged_from") else "—"
                else:
                    st = "—"
            row[f"{code} {label}"] = st
            if not stopped and st in ("blocked",):
                stopped = f"{code} ({label})"
        row["stopped at"] = stopped or "still moving / done"
        jrows.append(row)
    jcols = ["question id", "question"] + [f"{c} {l}" for c, l in journey_steps] + ["stopped at"]
    _write(ws5, 6, jcols, jrows,
           fills=lambda r: {**{f"{c} {l}": {"pass": GREEN, "flagged": AMBER, "blocked": RED,
                                            "merged": GREEN}.get(r.get(f"{c} {l}"), GREY)
                               for c, l in journey_steps},
                            "stopped at": RED if r["stopped at"] != "still moving / done" else GREEN},
           widths={"question id": 12, "question": 60, "stopped at": 20,
                   **{f"{c} {l}": 12 for c, l in journey_steps}})

    # ---- glossary ------------------------------------------------------------
    ws6 = _sheet(wb, "What the words mean", "GLOSSARY",
                 "Every status and every flag code the pipeline can produce, in plain English.",
                 "Use this when a code in another tab is unfamiliar.")
    grows = [{"kind": "status", "code": k, "what it means": v[0], "what to do": v[1]}
             for k, v in _STATUS_MEANING.items()]
    grows += [{"kind": "flag", "code": k, "what it means": v[0], "what to do": v[1]}
              for k, v in sorted(_FLAG_MEANING.items())]
    _write(ws6, 6, ["kind", "code", "what it means", "what to do"], grows,
           fills=lambda r: {"kind": GREY},
           widths={"kind": 9, "code": 28, "what it means": 70, "what to do": 70})

    wb.save(path)
    return len(rows), len(prows)


# ===========================================================================
# data_steps.xlsx  --  what each step is given, and what it produces
# ===========================================================================

# (step, name, GIVEN, EXTRACTED, saved_to, sample_source)
# sample_source is a callable returning one real value from live data, or None.
_STEPS = [
    ("S0", "Intake check",
     "The folder of source files",
     "A list of every input file, and a flag for anything required but missing",
     "inputs/manifest.csv, flags/flags.jsonl", "manifest"),
    ("A1", "Register books",
     "The cover/copyright page of each NCERT book",
     "The book's exact edition, copied verbatim off the page (never guessed)",
     "register/books.csv", "book"),
    ("A2", "Read pages",
     "One rendered page image at a time",
     "Ordered text blocks: paragraph / heading / list / box / figure, each copied word for word",
     "ncert/blocks/<BOOK>.jsonl", "block"),
    ("A2S", "Special blocks",
     "Blocks A2 marked too complex for plain text",
     "Tables, figures and equations preserved as regions rather than mangled into text",
     "ncert/blocks/<BOOK>.jsonl (needs_special)", None),
    ("A3", "Split passages",
     "The whole block stream for a chapter",
     "One-idea passages -- the unit every answer is later quoted from",
     "ncert/passages/<BOOK>.jsonl", "passage"),
    ("A4", "Write subtopics",
     "A chapter's headings and passages (two independent runs)",
     "The chapter's subtopic list; disagreements go to an adjudicator",
     "ncert/subtopics/<CHAPTER>.json", "subtopic"),
    ("A5", "Link passages",
     "Each passage plus the chapter's subtopic list",
     "Which subtopic each passage belongs to",
     "ncert/links/<BOOK>.jsonl", "link"),
    ("A6-A9", "Compare editions",
     "Old and new edition passages for the same chapter",
     "What changed between editions, and whether it is a real fact change or rewording",
     "ncert/change_log.csv, ncert/deleted_topics.csv", None),
    ("B1", "Register papers",
     "A paper's cover page and its answer key file",
     "Year, sitting, booklet code, and how far the source is trusted",
     "register/papers.csv", "paper"),
    ("B2", "Find questions",
     "A rendered paper page",
     "Where each question starts and ends on the page",
     "steps/B2/out/", None),
    ("B3", "Read the question",
     "One question's region of the page",
     "Stem, statements, the four options, and whether a figure is needed",
     "papers/records/<QID>.json", "stem"),
    ("B4", "Second reading",
     "The same question, read independently a second time",
     "A cross-check that catches misreadings before they enter the bank",
     "papers/records/<QID>.json", None),
    ("B5", "Copy the key",
     "The official NTA answer key page",
     "The official answer, joined to the question by (paper, question number)",
     "papers/records/<QID>.json", "answer"),
    ("B6", "Blind solve",
     "The question ONLY -- never the answer key, never a marked-up image",
     "An independent answer, compared against the official one. The main accuracy check.",
     "papers/records/<QID>.json", "blind"),
    ("B7", "Tag subject",
     "The question text",
     "Subject, and for Chemistry the branch (physical / organic / inorganic)",
     "papers/records/<QID>.json", "subject"),
    ("B8", "Fix faulty questions",
     "A question the board officially dropped or bonused",
     "What was wrong with it, and a proposed correction",
     "steps/B8/out/", None),
    ("C1", "Merge duplicates",
     "The same question as printed in two different booklet codes",
     "One merged record covering both codes; nothing is deleted",
     "papers/records/<QID>.json", "merge"),
    ("D1", "Pick the chapter",
     "The question, its answer, and the subject's chapter list (two runs)",
     "Which NCERT chapter the question tests",
     "papers/records/<QID>.json", "chapter"),
    ("D2", "Pick the subtopic",
     "The question plus that chapter's subtopic list (two runs)",
     "Which subtopic within the chapter",
     "papers/records/<QID>.json", None),
    ("D3", "Fetch passages",
     "The chosen subtopics",
     "The candidate NCERT passages the evidence could come from",
     "steps/D3/out/<QID>.json", None),
    ("D4", "Quote the evidence",
     "The question, its answer, and those passages",
     "The exact NCERT line that proves the answer -- verified word for word by script",
     "papers/records/<QID>.json", "quote"),
    ("D5-D11", "Older edition, repeats",
     "The question, both editions, and other questions in the same subtopic",
     "Older-edition line, whether the answer changed, a fact line, and repeat groups",
     "(not built)", None),
    ("E0-E6", "Tagging",
     "The question, its answer and its evidence",
     "How it is built, what it asks for, what thinking it needs, why wrong options attract",
     "(not built)", None),
    ("F1-F5", "Review and release",
     "Everything flagged, plus a sample of what passed",
     "Human decisions, re-runs of affected steps, counts, and the released tables",
     "(not built)", None),
]


def _samples():
    """One real value per step, pulled from live data -- so the reader sees the actual shape."""
    s = {}
    man = rc.pp("inputs", "manifest.csv")
    if os.path.exists(man):
        rows = lib_io.read_csv(man)
        if rows:
            s["manifest"] = f"{rows[0].get('file')}  (kind={rows[0].get('kind')})"
    bk = lib_io.read_csv(rc.pp("register", "books.csv")) if os.path.exists(rc.pp("register", "books.csv")) else []
    if bk:
        s["book"] = f"{bk[0].get('book_id')}  reprint='{bk[0].get('reprint_text_exact')}'"
    pp_ = lib_io.read_csv(rc.pp("register", "papers.csv")) if os.path.exists(rc.pp("register", "papers.csv")) else []
    if pp_:
        s["paper"] = f"{pp_[0].get('paper_id')}  trust={pp_[0].get('trust')}"
    bdir = rc.pp("ncert", "blocks")
    for fn in sorted(os.listdir(bdir)) if os.path.isdir(bdir) else []:
        if fn.endswith(".jsonl"):
            b = _read_jsonl(os.path.join(bdir, fn))
            if b:
                s["block"] = f"[{b[0].get('kind')}] {_flat(b[0].get('text'), 150)}"
                break
    pdir = rc.pp("ncert", "passages")
    for fn in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if fn.endswith(".jsonl"):
            p = _read_jsonl(os.path.join(pdir, fn))
            if p:
                s["passage"] = f"{p[0].get('passage_id')}: {_flat(p[0].get('text'), 150)}"
                break
    sdir = rc.pp("ncert", "subtopics")
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if fn.endswith(".json"):
            d = _read_json(os.path.join(sdir, fn)) or {}
            sts = d.get("subtopics") or []
            if sts:
                s["subtopic"] = f"{sts[0].get('subtopic_id')}: {sts[0].get('name')}"
                break
    ldir = rc.pp("ncert", "links")
    for fn in sorted(os.listdir(ldir)) if os.path.isdir(ldir) else []:
        if fn.endswith(".jsonl"):
            l = _read_jsonl(os.path.join(ldir, fn))
            if l:
                s["link"] = f"{l[0].get('passage_id')} -> {l[0].get('subtopic_id')}"
                break
    for r in _records():
        if r.get("merged_into"):
            continue
        s.setdefault("stem", _flat(r.get("stem_en"), 170))
        if r.get("official_answer"):
            opts = r.get("options_en") or {}
            s.setdefault("answer", f"{r['official_answer']} = "
                                   f"{_flat(opts.get(str(r['official_answer'])), 60)}")
        if r.get("b6_answer"):
            s.setdefault("blind", f"blind said {r['b6_answer']}, official "
                                  f"{r.get('official_answer')} -> "
                                  f"{'agree' if r.get('b6_agrees_with_key') else 'DISAGREE'}")
        if r.get("subject"):
            s.setdefault("subject", f"{r['subject']}"
                                    + (f" / {r['branch']}" if r.get("branch") else ""))
        if r.get("merged_from"):
            s.setdefault("merge", f"{r.get('question_id')} now covers "
                                  f"{_flat(r.get('paper_codes'))}")
        if r.get("d1_chapter_ids"):
            s.setdefault("chapter", _flat(r.get("d1_chapter_ids")))
        ev = r.get("d4_evidence") or []
        if ev and isinstance(ev[0], dict):
            s.setdefault("quote", _flat(ev[0].get("exact_line"), 150))
    return s


def _counts():
    out = {}
    sd = rc.pp("steps")
    if not os.path.isdir(sd):
        return out
    for step in os.listdir(sd):
        stat = os.path.join(sd, step, "status")
        if not os.path.isdir(stat):
            continue
        c = collections.Counter()
        for fn in os.listdir(stat):
            if fn.endswith(".json") and ".pending." not in fn and ".last_block." not in fn \
                    and not fn.startswith("_"):
                c[(_read_json(os.path.join(stat, fn)) or {}).get("status")] += 1
        out[step] = c
    return out


def build_steps(path):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    ws = _sheet(wb, "data by step", "WHAT EACH STEP IS GIVEN, AND WHAT IT PRODUCES",
                "The pipeline in order. For every step: what goes in, what comes out, where it "
                "is saved, how many items have been processed, and a REAL example from live data.",
                "The 'real example' column shows actual current data, not a description — so you "
                "can see the shape of what each step produces.")
    samples, counts = _samples(), _counts()
    rows = []
    for code, name, given, extracted, saved, skey in _STEPS:
        c = counts.get(code, collections.Counter())
        done = sum(c.values())
        if saved.startswith("(not built"):
            state = "NOT BUILT"
        elif done == 0:
            state = "not run yet"
        else:
            bits = [f"{v} {k}" for k, v in sorted(c.items(), key=lambda kv: str(kv[0])) if k]
            state = ", ".join(bits)
        rows.append({"step": code, "what it does": name,
                     "GIVEN (input)": given, "EXTRACTED (output)": extracted,
                     "saved to": saved, "processed so far": state,
                     "real example from current data": samples.get(skey, "") if skey else ""})
    _write(ws, 6, ["step", "what it does", "GIVEN (input)", "EXTRACTED (output)", "saved to",
                   "processed so far", "real example from current data"], rows,
           fills=lambda x: {"processed so far": GREY if x["processed so far"] in
                            ("NOT BUILT", "not run yet") else GREEN},
           widths={"step": 9, "what it does": 20, "GIVEN (input)": 44, "EXTRACTED (output)": 54,
                   "saved to": 34, "processed so far": 22,
                   "real example from current data": 78})
    wb.save(path)
    return len(rows)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build final_data.xlsx and data_steps.xlsx.")
    ap.add_argument("--outdir")
    args = ap.parse_args(argv)
    outdir = args.outdir or rc.pp("exports", datetime.date.today().isoformat())
    rc.ensure_dir(outdir)

    flags = _read_jsonl(rc.pp("flags", "flags.jsonl"))
    by_item = collections.defaultdict(list)
    for f in flags:
        by_item[f.get("item_id")].append(f)

    fp = os.path.join(outdir, "final_data.xlsx")
    nq, npass = build_final(fp, by_item)
    sp = os.path.join(outdir, "data_steps.xlsx")
    ns = build_steps(sp)

    print(f"final_data.xlsx   -> {fp}")
    print(f"   Questions tab:      {nq} unique questions")
    print(f"   NCERT passages tab: {npass} passages")
    print(f"data_steps.xlsx   -> {sp}")
    print(f"   {ns} steps documented, each with a real sample value")
    return 0


if __name__ == "__main__":
    sys.exit(main())
