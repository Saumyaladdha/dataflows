#!/usr/bin/env python3
"""Crops an image for every NCERT passage that has no text, and links it on the passage record.

The problem this solves. 264 of 2,469 passages carry `text: ""` -- 236 figures, 19 tables, 6
equations, 3 boxes -- because A2 recorded the block's position but never its content. A passage
with no text is not merely thin: it is **unquotable**, and quoting is the whole purpose of a
passage. `quote_verify.find` matches an agent's citation word-for-word against passage text, so
against an empty string every citation fails. Stage D would offer these passages as an answer's
NCERT basis and no agent could ever use one.

Why a script may do this. Each block already carries a `bbox` from A2 and every page is already
rendered to PNG under steps/A2/work/ (2,924 of them). Cropping a recorded rectangle out of an
existing image is arithmetic, not judgement: nothing is interpreted, nothing is chosen, and the
result is reproducible from the same inputs. The script does NOT attempt to read the figure --
transcribing it is A2S's job and an agent's judgement.

What this does and does not fix. After this runs, a figure passage has a real image a reviewer
can look at and an agent can be shown. It still has no TEXT, so it still cannot be quoted. The
two fixes are complementary: this one makes the content visible, A2S makes it quotable. Both are
needed, and the counts printed at the end say how many still await A2S.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
from lib import pdf as lib_pdf  # noqa: E402

#: book_id -> (class_num, subject) so a chapter can be resolved back to its source PDF.
#: The suffix is the edition: L = latest, O = older (spec 6.1 naming).
_SUBJ = {"BIO": "Biology", "CHE": "Chemistry", "PHY": "Physics"}


def _source_pdf(book_id, chapter_num):
    """The real PDF a book_id + chapter came from, or None.

    Cropping is done from the SOURCE PDF rather than the already-rendered page PNG. The PNG
    route looked cheaper but mixes coordinate systems: A2's bbox is in pixels at DEFAULT_DPI,
    while pymupdf treats a PNG-backed page as points (612x784), so clamping mangled every box
    and silently cropped the wrong region for any that happened to fit. `lib_pdf.crop_box`
    takes a bbox in px at a given dpi and does the conversion properly -- it is the tool this
    project already has for exactly this job.
    """
    m = re.match(r"^(BIO|CHE|PHY)(\d{2})([LO])$", book_id or "")
    if not m:
        return None
    subject, cls, edition = _SUBJ[m.group(1)], int(m.group(2)), m.group(3)
    want_edition = "latest" if edition == "L" else "older"
    for relpath, abspath in rc.iter_ncert_files():
        info = rc.parse_ncert_relpath(relpath)
        if not info:
            continue
        if (info.get("edition_code") == want_edition
                and info.get("class_num") == cls
                and info.get("subject") == subject
                and info.get("chapter_num") == int(chapter_num)):
            return abspath
    return None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSAGES = os.path.join(ROOT, "ncert", "passages")
BLOCKS = os.path.join(ROOT, "ncert", "blocks")
A2_WORK = os.path.join(ROOT, "steps", "A2", "work")
FIGS = os.path.join(ROOT, "ncert", "figures")
#: Pad the recorded bbox a little. A figure's caption and axis labels often sit just outside the
#: block rectangle A2 drew, and a crop that clips them is far less useful to a reviewer than one
#: with a few pixels of margin. Clamped to the page below.
PAD = 12


def _jsonl(path):
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


def main():
    os.makedirs(FIGS, exist_ok=True)
    made, skipped, failed = 0, Counter(), []
    _ = lib_pdf  # crop uses pymupdf directly on the already-rendered page PNG
    still_textless = Counter()

    # Match passages to blocks BY ORDINAL within (book, chapter, page, kind).
    #
    # The obvious join -- passage["blocks"] -> block["n"] -- does not work, and silently returns
    # nothing rather than erring: A3 renumbers blocks 1..n LOCAL TO EACH SECTION (its own input
    # comment says so, because A2's `n` resets every page), so a passage recording blocks=[3]
    # means "the 3rd block of its section", not "block 3 of its page".
    #
    # What is reliable is order. A3 emits passages in block order within a section and sections
    # run in page order, so within one (book, chapter, page, kind) the k-th text-less passage is
    # the k-th empty block of that kind on that page. Measured before relying on it: 156 of the
    # 264 have exactly one candidate and are unambiguous either way; the ordinal rule resolves
    # the remaining 108. Any group where the two counts disagree is reported and skipped rather
    # than zipped approximately -- a figure cropped from the wrong rectangle is worse than none.
    pass_by, blk_by = defaultdict(list), defaultdict(list)
    books = {}
    for pf in sorted(os.listdir(PASSAGES)):
        if not pf.endswith(".jsonl"):
            continue
        book = pf[: -len(".jsonl")]
        ps = _jsonl(os.path.join(PASSAGES, pf))
        books[book] = ps
        for p in ps:
            if (p.get("text") or "").strip():
                continue
            try:
                key = (book, int(p["chapter_num"]), int(str(p["page_start"])), p.get("kind"))
            except (TypeError, ValueError, KeyError):
                failed.append((p.get("passage_id"), "no usable chapter/page/kind"))
                continue
            pass_by[key].append(p)
        for b in _jsonl(os.path.join(BLOCKS, f"{book}.jsonl")):
            if (b.get("text") or "").strip() or not b.get("bbox"):
                continue
            try:
                key = (book, int(b["chapter_num"]), int(str(b["page"])), b.get("kind"))
            except (TypeError, ValueError, KeyError):
                continue
            blk_by[key].append(b)

    for key, plist in sorted(pass_by.items()):
        book, ch, page, kind = key
        blist = blk_by.get(key, [])
        if len(blist) != len(plist):
            for p in plist:
                failed.append((p.get("passage_id"),
                               f"{len(plist)} text-less passages but {len(blist)} empty {kind} "
                               f"blocks on ch{ch} p{page} -- cannot match by order safely"))
            continue
        pdf = _source_pdf(book, ch)
        if not pdf:
            for p in plist:
                failed.append((p.get("passage_id"), f"no source PDF found for {book} ch{ch}"))
            continue
        png = os.path.join(A2_WORK, f"{book}-ch{ch:02d}-p{page:03d}.png")
        for p, b in zip(plist, blist):
            pid = p.get("passage_id")
            if p.get("figure_path") and os.path.exists(os.path.join(ROOT, p["figure_path"])):
                skipped["already had an image"] += 1
                continue
            x0, y0, x1, y1 = b["bbox"]
            crop_px = [max(0, int(x0) - PAD), max(0, int(y0) - PAD), int(x1) + PAD, int(y1) + PAD]
            if crop_px[2] - crop_px[0] < 8 or crop_px[3] - crop_px[1] < 8:
                failed.append((pid, f"bbox {b['bbox']} is degenerate"))
                continue
            out_rel = os.path.join("ncert", "figures", f"{pid}.png")
            try:
                lib_pdf.crop_box(pdf, page, crop_px, os.path.join(ROOT, out_rel), unit="px")
            except Exception as exc:  # noqa: BLE001
                failed.append((pid, f"crop failed: {exc}"))
                continue
            p["figure_path"] = out_rel
            p["figure_source"] = {"pdf": os.path.relpath(pdf, ROOT), "page": page,
                                  "bbox_px": crop_px, "source_bbox": b["bbox"],
                                  "padded_by": PAD,
                                  "matched_by": "ordinal within page+kind"}
            p["text_status"] = ("no text extracted; image cropped from the page. Still NOT "
                                "quotable -- A2S must transcribe it before it can be cited.")
            still_textless[kind] += 1
            made += 1

    for book, ps in books.items():
        tmp = os.path.join(PASSAGES, f"{book}.jsonl.tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            for p in ps:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
        os.replace(tmp, os.path.join(PASSAGES, f"{book}.jsonl"))

    print(f"images cropped and linked : {made}")
    if skipped:
        for k, v in skipped.items():
            print(f"skipped                   : {v} ({k})")
    print(f"\nby kind: {dict(still_textless)}")
    if failed:
        print(f"\ncould not crop            : {len(failed)}")
        for pid, why in failed[:12]:
            print(f"    {pid}: {why}")
    print(f"\nNOTE: every one of these {made} passages still has NO text and so still cannot be")
    print("quoted as evidence. The image makes the content visible; A2S must transcribe it")
    print("before quote_verify can match a citation against it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
