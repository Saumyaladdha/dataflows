#!/usr/bin/env python3
"""Resolves the image files that belong to a question, for any sheet that needs to show them.

    from question_assets import question_images, figure_fields, asset_columns, asset_values

Two different pictures exist per question and they are not interchangeable:

  * **the question image** -- `papers/questions/<paper_id>/<qno>.png`, the crop of the question as
    it was read. Every one of the 697 records has at least one; 34 have two because the same
    question appears under two booklet codes.
  * **the recovered figure** -- `papers/figures/<QID>.png`, written by step B9 when the question's
    own source dropped its diagram. 49 of the 66 questions that need one have it.

Why this module exists. `paper_codes` stores SHORT codes (`E1:1`, `Q1:75`) with a few full ids
mixed in (`NEET-2023-MAIN-E1:3`), and `Q1` is ambiguous on its own -- both 2022 and 2024 have a Q1
-- so the record's `year` and `sitting` are needed to build the directory name. A naive
`paper_codes.rpartition(":")` resolves 200 of 697 and silently reports the rest as having no
image, which is exactly the bug this replaces: a sheet showed "[missing content - no text
printed]" while the picture sat on disk.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

QUESTIONS_DIR_PARTS = ("papers", "questions")
FIGURES_DIR_PARTS = ("papers", "figures")

# Columns every question sheet should carry, in order, as (header, width, wrap).
#
# There is deliberately NO blanket "question image" column. Every one of the 662 questions has a
# crop at papers/questions/<paper>/<n>.png, but a question whose text is complete does not need one
# -- printing a path on all 662 rows buries the handful that actually depend on a picture. These
# columns stay EMPTY unless the question genuinely needs a figure, so a non-empty cell means
# something.
ASSET_COLUMNS = [
    ("figure file", 28, True),
    ("figure source", 30, True),
    ("figure match", 11, False),
]


def question_images(rec):
    """Every (paper_id, qno, relative_path) this record has a crop for, in paper_codes order.

    Returns [] only if no file exists, which currently happens for no record at all.
    """
    out = []
    exam = rec.get("exam") or "NEET"
    year = rec.get("year")
    sitting = rec.get("sitting") or "MAIN"
    for code in (rec.get("paper_codes") or []):
        paper, _, qno = str(code).rpartition(":")
        if not qno.isdigit() or not paper:
            continue
        # A short code like "E1" needs the record's own year and sitting to become a directory
        # name; "Q1" alone is ambiguous between 2022 and 2024.
        paper_id = paper if paper.count("-") >= 2 else f"{exam}-{year}-{sitting}-{paper}"
        rel = os.path.join(*QUESTIONS_DIR_PARTS, paper_id, f"{int(qno)}.png")
        if os.path.exists(rc.pp(rel)) and rel not in [o[2] for o in out]:
            out.append((paper_id, int(qno), rel))
    return out


def figure_fields(rec):
    """(path_or_status, source, confidence) for the B9-recovered figure.

    `path_or_status` deliberately says NEEDED rather than staying blank when the question declares
    a figure and none has been recovered: a blank cell reads as "no figure needed", which is the
    opposite of the truth and hides the gap.
    """
    path = (rec.get("figure_path") or "").strip()
    if path:
        if not os.path.exists(rc.pp(path)):
            path = f"{path}  (RECORDED BUT FILE MISSING)"
    elif rec.get("has_figure"):
        path = "NEEDED - not recovered yet"
    source = (rec.get("figure_source_row") or rec.get("figure_source_url") or "").strip()
    return path, source, (rec.get("figure_match_confidence") or "").strip()


def asset_values(rec):
    """The ASSET_COLUMNS values for one record. All empty for a question needing no picture."""
    return list(figure_fields(rec))


# --------------------------------------------------------------------------- slot pointers
#
# A question whose options ARE pictures has nothing printed in them, so B3 recorded
# "(Image option - will be added soon)" or "[missing content - no text printed]". Step B10 cuts the
# recovered figure into one file per option, and these helpers put the path to THAT option's
# picture where the placeholder was, so a reader is sent to the one picture that is that option
# rather than to a sheet of four.

import re  # noqa: E402  (kept beside the only code that uses it)

_PLACEHOLDER_RE = re.compile(
    r"image option|will be added soon|image not available|missing content|no text printed"
    r"|unreadable glyph", re.I)

_POINTER = "[refer image: {path}]"


def _slot_crops(qid):
    """{slot: relative_path} for the per-option crops B10 produced, read from disk."""
    out = {}
    d = rc.pp(*FIGURES_DIR_PARTS, qid)
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".png"):
            continue
        stem = fn[:-4]
        slot = stem
        for field in ("list_i", "list_ii", "statements"):
            if stem.startswith(field + "_"):
                slot = f"{field}:{stem[len(field) + 1:]}"
                break
        out[slot] = os.path.join(*FIGURES_DIR_PARTS, qid, fn)
    return out


def _resolve(text, qid, slot, crops):
    """Replace a placeholder with a pointer to that slot's own picture, if one exists."""
    if not _PLACEHOLDER_RE.search(str(text or "")):
        return text
    path = crops.get(slot)
    return _POINTER.format(path=path) if path else text


def question_text(rec):
    """Stem plus lists and statements, with any picture-only entry pointing at its own crop.

    The stem alone is boilerplate for match and assertion-reason shapes, so the lists and
    statements are included -- that is where the discriminating content sits.
    """
    qid = rec.get("question_id") or ""
    crops = _slot_crops(qid)
    parts = [(rec.get("stem_en") or "").strip()]
    for field, label in (("statements", ""), ("list_i", "List I"), ("list_ii", "List II")):
        entries = [e for e in (rec.get(field) or []) if isinstance(e, dict)]
        if entries:
            if label:
                parts.append(f"{label}:")
            for e in entries:
                txt = _resolve(e.get("text"), qid, f"{field}:{e.get('label')}", crops)
                parts.append(f"({e.get('label')}) {txt}")
    return "\n".join(p for p in parts if p)


def _unmapped_panels(qid):
    """{source_label: path} for panels cut from the figure but NOT tied to one of our options."""
    out = {}
    for slot, path in _slot_crops(qid).items():
        if slot.startswith("panel_"):
            out[slot[len("panel_"):]] = path
    return out


def options_text(rec, one_per_line=True, tick=True):
    """The four options, each picture-only option pointing at its own crop.

    `tick` marks the official answer, which is how CATEGORIES.xlsx already shows examples.

    Two cases for a picture-only option, and they are not the same:

      * the slot has its OWN crop (list entries, where the printed label is tied to the content) --
        the cell points straight at that one file.
      * the panels were cut but could not be tied to our option numbers -- the cell lists the
        files and says the mapping is unverified. It must NOT silently claim panel_1 is option 1:
        a printed label is the SOURCE paper's option order, and booklet codes shuffle it.
    """
    qid = rec.get("question_id") or ""
    crops = _slot_crops(qid)
    opts = {k: (v or "").strip() for k, v in sorted((rec.get("options_en") or {}).items())}
    ans = str(rec.get("official_answer") or "")
    lines, needs_note = [], False
    for k, v in opts.items():
        if not v:
            continue
        shown = _resolve(v, qid, f"opt{k}", crops)
        if shown == v and _PLACEHOLDER_RE.search(v) and _unmapped_panels(qid):
            shown = "(this option is a picture — see the note below)"
            needs_note = True
        lines.append(f"{k}) {shown}" + ("  ✔" if tick and k == ans else ""))
    if needs_note:
        panels = _unmapped_panels(qid)
        files = ", ".join(panels[lbl] for lbl in sorted(panels))
        lines.append(
            f"NOTE: the option pictures were recovered and cut to {files} — labelled "
            f"{'/'.join(sorted(panels))} by the SOURCE paper. Which panel is which option number "
            f"here is NOT verified, because booklet codes shuffle option order and this "
            f"question's own option text was never printed.")
    return ("\n" if one_per_line else " | ").join(lines)


def coverage(records):
    """Counts for a sheet's Read me tab, so no number there is hand-typed.

    Records carrying `merged_into` are excluded: step C1 merges the same question seen under two
    booklet codes into one survivor (which gets `merged_from`) and leaves the absorbed record on
    disk marked `merged_into`. 35 such records exist, and counting them would report the same
    question twice. They are correctly absent from the 580-question discovery set.
    """
    live = [r for r in records if not r.get("merged_into")]
    with_img = sum(1 for r in live if question_images(r))
    needs_fig = sum(1 for r in live if r.get("has_figure"))
    has_fig = sum(1 for r in live if (r.get("figure_path") or "").strip())
    return {"questions": len(live), "absorbed_by_a_merge": len(records) - len(live),
            "with_question_image": with_img, "declare_a_figure": needs_fig,
            "figure_recovered": has_fig, "figure_still_needed": needs_fig - has_fig}


def load_records():
    out = {}
    d = rc.pp("papers", "records")
    for fn in sorted(os.listdir(d)):
        if fn.startswith("Q-") and fn.endswith(".json"):
            try:
                with open(os.path.join(d, fn), encoding="utf-8") as fh:
                    rec = json.load(fh)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(rec, dict) and rec.get("question_id"):
                out[rec["question_id"]] = rec
    return out


if __name__ == "__main__":
    recs = load_records()
    cov = coverage(list(recs.values()))
    for k, v in cov.items():
        print(f"  {k:24s} {v}")
    multi = [q for q, r in recs.items() if len(question_images(r)) > 1]
    print(f"  questions with 2 crops   {len(multi)}  e.g. {multi[:4]}")
    missing = [q for q, r in recs.items() if not question_images(r)]
    print(f"  questions with NO crop   {len(missing)}" + (f"  {missing[:6]}" if missing else ""))
