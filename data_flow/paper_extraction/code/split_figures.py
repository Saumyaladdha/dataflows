#!/usr/bin/env python3
"""Step B10 mechanics: cut a recovered figure into one image per option / list entry.

    python3 scripts/split_figures.py --prepare   # write steps/B10/work/<QID>.runA.input.json
    python3 scripts/split_figures.py --apply     # crop agent boxes -> papers/figures/<QID>/<slot>.png
    python3 scripts/split_figures.py --report    # what is covered and what is not

Why this step exists. B3 reads what is printed. For a question whose options ARE pictures, nothing
is printed, so every option reads `(Image option - will be added soon)` and every match-list entry
reads `[missing content - no text printed]`. B9 then recovers the figure, but recovers it as ONE
image holding all four pictures. A reader sent to that sheet still cannot tell which quadrant is
option 3.

So this step turns one figure into one file per picture. Where a slot can be named, its text
becomes a pointer to that slot's exact picture:

    (A) [refer image: papers/figures/Q-000353/list_i_A.png]
    (B) [refer image: papers/figures/Q-000353/list_i_B.png]

Where it cannot -- which is EVERY option slot, see `crop_panels` -- the pictures are still cut and
kept under the label printed on them, and the sheet says the mapping is unverified:

    1) (this option is a picture - see the note below)
    NOTE: the option pictures were recovered and cut to papers/figures/Q-000343/panel_1.png ...
    labelled 1/2/3/4 by the SOURCE paper. Which panel is which option number here is NOT verified.

Measured when this was written: 16 questions carry placeholder content across 63 slots; 14 of them
have a recovered figure to cut from, giving 5 exact slot pictures and 36 slots covered by an
unverified panel set.

The boxes are a judgement (panels are a 2x2 grid for option graphs and a vertical column for match
structures, and the printed labels may not be our option order), so the `b10-figure-splitter` agent
decides them. This script only prepares the input and performs the crop. It makes no judgement and
never chooses a box.
"""

import argparse
import glob
import json
import os
import re
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402

STEP = "B10"
PLACEHOLDER_RE = re.compile(
    r"image option|will be added soon|image not available|missing content|no text printed"
    r"|unreadable glyph", re.I)

# What a slot's text becomes once its own picture exists. The wording matters: the question has to
# read as an instruction to a person, not as a bare path dumped in a cell.
POINTER = "[refer image: {path}]"


def placeholder_slots(rec):
    """(slot, current_text) for every slot whose content was a picture that was never captured."""
    out = []
    for key, val in sorted((rec.get("options_en") or {}).items()):
        if PLACEHOLDER_RE.search(str(val or "")):
            out.append((f"opt{key}", str(val or "")))
    for field in ("list_i", "list_ii", "statements"):
        for entry in (rec.get(field) or []):
            if isinstance(entry, dict) and PLACEHOLDER_RE.search(str(entry.get("text") or "")):
                out.append((f"{field}:{entry.get('label')}", str(entry.get("text") or "")))
    return out


def slot_filename(slot):
    """`list_i:A` -> `list_i_A.png`; `opt3` -> `opt3.png`."""
    return re.sub(r"[^A-Za-z0-9_]+", "_", slot) + ".png"


def image_size(path):
    with pymupdf.open(path) as doc:
        page = doc[0]
        # A PNG page rect is in points (pixels * 72/96), so scale back to report real pixels.
        return int(round(page.rect.width / 0.75)), int(round(page.rect.height / 0.75))


def load_records():
    out = {}
    d = rc.pp("papers", "records")
    for fn in sorted(os.listdir(d)):
        if not (fn.startswith("Q-") and fn.endswith(".json")):
            continue
        try:
            with open(os.path.join(d, fn), encoding="utf-8") as fh:
                rec = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(rec, dict) and rec.get("question_id") and not rec.get("merged_into"):
            out[rec["question_id"]] = rec
    return out


def candidates(records):
    """Questions with placeholder slots, split by whether a figure exists to cut from."""
    ready, blocked = [], []
    for qid, rec in records.items():
        slots = placeholder_slots(rec)
        if not slots:
            continue
        fig = (rec.get("figure_path") or "").strip()
        if fig and os.path.exists(rc.pp(fig)):
            ready.append((qid, rec, slots, fig))
        else:
            blocked.append((qid, rec, slots))
    return ready, blocked


def cmd_prepare(records):
    work = rc.pp("steps", STEP, "work")
    os.makedirs(work, exist_ok=True)
    os.makedirs(rc.pp("steps", STEP, "out"), exist_ok=True)
    ready, blocked = candidates(records)
    written = 0
    for qid, rec, slots, fig in ready:
        out_path = os.path.join(work, f"{qid}.runA.input.json")
        width, height = image_size(rc.pp(fig))
        payload = {
            "question_id": qid,
            "figure_image": fig,
            "image_width": width,
            "image_height": height,
            "stem": rec.get("stem_en") or "",
            "slots": [s for s, _ in slots],
            "slot_texts": {s: t for s, t in slots},
        }
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
        written += 1
    print(f"prepared {written} input file(s) in steps/{STEP}/work/")
    for qid, _, slots, _ in ready:
        print(f"  {qid}: {len(slots)} slot(s) -> {[s for s, _ in slots]}")
    if blocked:
        print(f"\n{len(blocked)} question(s) have placeholder slots but NO recovered figure to cut "
              f"from, so they cannot be split yet:")
        for qid, _, slots in blocked:
            print(f"  {qid}: {len(slots)} slot(s)")
    return 0


def crop_panels(qid, panels, figure_rel=None):
    """Cut every usable panel out of a question's recovered figure.

    Returns `(made, unmapped)`: `made` is {slot: path} for panels tied to one of our slots,
    `unmapped` is {printed_label: path} for panels that are real pictures but cannot be tied to a
    slot. Both are written to disk; nothing is discarded.

    Only a LIST slot may be filled from a printed label. The asymmetry is real:

      * `list_i:A` / `list_ii:I` -- our record already holds entries labelled A-D and I-IV, and the
        picture prints the same labels against the same content, so A->A matches content to content
        and is checkable.
      * `opt1`..`opt4` -- our option text is EMPTY (that is why we are here), so a printed `(1)`
        has nothing in our record to agree with. It is the source paper's option order, and booklet
        codes shuffle option order. Q-000343 proves it: the official key for our code says 4, and
        the physically correct plot in the picture is printed (2).

    So a numeric printed label is NOT evidence of our option number, however much it looks like our
    slot name.
    """
    if figure_rel is None:
        rec_path = rc.pp("papers", "records", f"{qid}.json")
        try:
            with open(rec_path, encoding="utf-8") as fh:
                figure_rel = (json.load(fh).get("figure_path") or "").strip()
        except (OSError, json.JSONDecodeError):
            return {}, {}
    fig_abs = rc.pp(figure_rel) if figure_rel else ""
    if not fig_abs or not os.path.exists(fig_abs):
        return {}, {}

    out_dir = rc.pp("papers", "figures", qid)
    os.makedirs(out_dir, exist_ok=True)
    made, unmapped = {}, {}
    with pymupdf.open(fig_abs) as doc:
        page = doc[0]
        rect = page.rect
        for i, panel in enumerate(panels, 1):
            slot = panel.get("slot")
            box = panel.get("box")
            if not (isinstance(box, list) and len(box) == 4):
                continue
            x0, y0, x1, y1 = [float(v) for v in box]
            clip = pymupdf.Rect(rect.x0 + x0 * rect.width, rect.y0 + y0 * rect.height,
                                rect.x0 + x1 * rect.width, rect.y0 + y1 * rect.height)
            if clip.is_empty or clip.width <= 1 or clip.height <= 1:
                continue
            if slot and slot != "unknown" and slot.startswith(("list_i:", "list_ii:",
                                                               "statements:")):
                fn = slot_filename(slot)
                made[slot] = os.path.join("papers", "figures", qid, fn)
            else:
                label = re.sub(r"[^A-Za-z0-9]+", "", str(panel.get("printed_label") or "")) or str(i)
                fn = f"panel_{label}.png"
                unmapped[label] = os.path.join("papers", "figures", qid, fn)
            page.get_pixmap(clip=clip, dpi=200).save(os.path.join(out_dir, fn))
    return made, unmapped


def cmd_apply(records):
    done = skipped = crops = 0
    for path in sorted(glob.glob(rc.pp("steps", STEP, "out", "*.json"))):
        qid = os.path.basename(path).split(".")[0]
        rec = records.get(qid)
        if rec is None:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                verdict = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if verdict.get("error"):
            print(f"  {qid}: agent reported error -- {verdict['error']}")
            skipped += 1
            continue
        panels = verdict.get("panels") or []
        if not panels:
            print(f"  {qid}: no panels (agent note: {str(verdict.get('note'))[:90]})")
            skipped += 1
            continue

        fig_rel = (rec.get("figure_path") or "").strip()
        fig_abs = rc.pp(fig_rel)
        if not os.path.exists(fig_abs):
            print(f"  {qid}: figure missing at {fig_rel}")
            skipped += 1
            continue

        made, unmapped = crop_panels(qid, panels, fig_rel)
        crops += len(made) + len(unmapped)

        if made:
            print(f"  {qid}: {len(made)} slot crop(s) -> papers/figures/{qid}/")
            done += 1
        elif unmapped:
            print(f"  {qid}: {len(unmapped)} panel(s) cut but NOT mapped to a slot "
                  f"(source labels {sorted(unmapped)}); sheet will show them as an unverified set")
            done += 1
        else:
            print(f"  {qid}: panels present but none usable "
                  f"(labels_match_our_slots={verdict.get('labels_match_our_slots')})")
            skipped += 1
    print(f"\nsplit {done} question(s) into {crops} crop(s); skipped {skipped}")
    print("Crops are NOT written into papers/records/ -- the sheet resolves them from disk, so a "
          "re-run of this step cannot corrupt a record.")
    return 0


def slot_images(qid):
    """{slot: relative_path} for crops that exist on disk. Used by the sheet exporters."""
    out = {}
    d = rc.pp("papers", "figures", qid)
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".png"):
            continue
        stem = fn[:-4]
        slot = stem
        if stem.startswith("list_i_") or stem.startswith("list_ii_") or stem.startswith(
                "statements_"):
            field, _, label = stem.rpartition("_")
            slot = f"{field}:{label}"
        out[slot] = os.path.join("papers", "figures", qid, fn)
    return out


def pointer_for(qid, slot):
    """The text an exported sheet should show in place of a placeholder, or None."""
    img = slot_images(qid).get(slot)
    return POINTER.format(path=img) if img else None


def cmd_report(records):
    ready, blocked = candidates(records)
    total_slots = sum(len(s) for _, _, s, _ in ready) + sum(len(s) for _, _, s in blocked)
    filled = 0
    print(f"questions with placeholder slots : {len(ready) + len(blocked)}")
    print(f"  with a figure to cut from      : {len(ready)}")
    print(f"  without one                    : {len(blocked)}")
    print(f"placeholder slots in total       : {total_slots}\n")
    for qid, _, slots, _ in ready:
        have = slot_images(qid)
        got = [s for s, _ in slots if s in have]
        filled += len(got)
        mark = "OK " if len(got) == len(slots) else "   "
        print(f"  {mark}{qid}: {len(got)}/{len(slots)} slot image(s)")
    print(f"\nslots now pointing at their own picture: {filled} of {total_slots}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prepare", action="store_true")
    g.add_argument("--apply", action="store_true")
    g.add_argument("--report", action="store_true")
    args = ap.parse_args()
    records = load_records()
    if args.prepare:
        return cmd_prepare(records)
    if args.apply:
        return cmd_apply(records)
    return cmd_report(records)


if __name__ == "__main__":
    sys.exit(main())
