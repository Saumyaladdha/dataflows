"""Step-specific check for B3F (docs/PAPER_EXTRACTION_V2.md + schemas/B3F.json).

The schema fixes the shape. This adds the rules a JSON schema cannot state, each one standing for a
way a figure transcription goes wrong:

  (1) LABELS ARE COPIED, NOT DESCRIBED. Nothing in this pipeline writes prose about a drawing --
      a2-special-transcriber says "No description of the drawing" and this is its paper-side twin.
      A "label" like "an arrow pointing right" is a description wearing a label's clothes, and it
      poisons everything downstream, because the labels ARE the figure's content for every later
      step.

  (2) A FIGURE WITH NO LABELS AND NO CAPTION HAS TO SAY WHY. Plenty of real NEET diagrams carry no
      printed label at all, so an empty list is legitimate -- but it is indistinguishable from "did
      not look", and SPEC Rule 19 requires those two states to look different.

  (3) A TABLE MUST ACTUALLY CARRY ITS TABLE. `kind: table` with empty rows is the one combination
      that is never right: the rows are the only reason to call it a table.

  (4) A STRUCTURE STOPS HERE. `kind: structure` must not come back with a SMILES string or a
      chemical reading in `note` -- a2c-structure-transcriber is the only step allowed to read a
      drawing as chemistry, and it has its own rules about R groups and stereochemistry that this
      agent has never been told.

  (5) PANELS ARE NOT SPLIT HERE. A crop holding the four option graphs is reported, not divided and
      not assigned to option numbers: b10-figure-splitter owns that because it knows the
      booklet-code trap (a panel printed (2) here may be option 4 in another code, SPEC Rule 16).

WHAT IS DELIBERATELY NOT HERE: any judgement of whether a label was read correctly. A script cannot
see the crop. What it can do is refuse an answer that breaks a stated rule, and that is all this
does.
"""

import json
import os
import re

#: Phrases that mean the agent described the drawing instead of copying what it prints.
DESCRIPTION = [
    r"\ban arrow\b", r"\ba dashed\b", r"\ba solid line\b", r"\bpointing (?:right|left|up|down)\b",
    r"\bshows? a\b", r"\bdepicts?\b", r"\bdiagram of\b", r"\billustrat", r"\brepresent(?:s|ing) a\b",
    r"\bcurve going\b", r"\bgraph of a\b", r"\bthere (?:is|are) a\b",
]
#: A SMILES-looking string in a figure label almost always means the agent read chemistry it was
#: told to leave to a2c-structure-transcriber.
SMILES_HINT = re.compile(r"[A-Za-z][0-9]?(?:\[[A-Za-z@+\-0-9]+\]|[=#()]){3,}")


def check(output, item=None, record=None, root=".", **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]

    kind = output.get("kind")
    labels = output.get("labels") or []
    caption = (output.get("caption") or "").strip()
    note = (output.get("note") or "").strip()
    rows = output.get("table_rows") or []
    problems, notes = [], []

    given = item or {}
    for field in ("paper_id", "qno"):
        if given.get(field) is not None and output.get(field) != given.get(field):
            problems.append("%s is %r but the input said %r -- output written against another figure"
                            % (field, output.get(field), given.get(field)))

    # (1) descriptions masquerading as labels
    for text in labels + [caption]:
        for pattern in DESCRIPTION:
            match = re.search(pattern, str(text), re.I)
            if match:
                problems.append("%r describes the drawing (%r); copy what the figure PRINTS, and put "
                                "anything that cannot be recovered from its labels in `note`"
                                % (str(text)[:60], match.group(0)))
                break

    # (2) an empty figure has to account for itself
    if kind not in ("not_a_figure", "structure") and not labels and not caption and not rows:
        if len(note.split()) < 4:
            problems.append("no caption, no labels and no rows, and `note` does not say why. An "
                            "unlabelled diagram is a real and common case, but it must not look the "
                            "same as not having looked (SPEC Rule 19)")
        else:
            notes.append("no printed labels; agent accounted for it")

    # (3) a table is its rows
    if kind == "table" and not rows:
        problems.append("kind is `table` but `table_rows` is empty -- the rows are the only reason "
                        "to call a crop a table")
    if kind != "table" and rows:
        problems.append("`table_rows` filled but kind is %r" % kind)

    # (4) a structure stops here
    if kind == "structure":
        for text in labels + [note]:
            if SMILES_HINT.search(str(text)):
                problems.append("kind is `structure` and the output carries what looks like SMILES "
                                "(%r). Stop at `structure`: a2c-structure-transcriber is the only "
                                "step allowed to read a drawing as chemistry" % str(text)[:50])
                break

    # (5) panels are reported, not split
    if output.get("holds_multiple_panels"):
        if re.search(r"option\s*[1-4]\b", note, re.I) and "b10" not in note.lower():
            notes.append("note assigns an option number; b10-figure-splitter decides that, because "
                         "a panel printed (2) here may be option 4 in another code")
        notes.append("holds several panels -> b10-figure-splitter")

    if output.get("complete") is False:
        notes.append("CLIPPED at a crop edge -> B3F_FIGURE_CLIPPED; the geometry wants widening")
    if kind == "not_a_figure":
        notes.append("NOT A FIGURE -> B3F_NOT_A_FIGURE; the geometry pass emitted a crop that holds "
                     "text, a watermark or furniture, and wants fixing rather than transcribing "
                     "around")

    if problems:
        return False, "; ".join(problems[:6])
    return True, ("kind=%s, %d label(s)%s%s"
                  % (kind, len(labels), ", %d table row(s)" % len(rows) if rows else "",
                     "; " + "; ".join(notes) if notes else ""))


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--item")
    args = ap.parse_args(argv)
    with open(args.output, encoding="utf-8") as fh:
        data = json.load(fh)
    item = None
    if args.item:
        with open(args.item, encoding="utf-8") as fh:
            item = json.load(fh)
    ok, message = check(data, item=item)
    print(("PASS  " if ok else "FAIL  ") + message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
