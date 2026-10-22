"""Turn the rulebook's own definition tables into a glossary the exports can show.

WHY
---
`config/allowed_values.yaml` carries the labels; `docs/question_categories/RULEBOOK.md` carries what
each one MEANS. Until now only the labels reached the output, so a page showed a question tagged
`format_reflex_option` and gave the reader no way to know what that is or why this question has it.
A label nobody can read is not a classification, it is a code.

So the glossary is parsed from the rulebook rather than retyped: a definition that drifts from the
rulebook is worse than no definition, because the reader then checks the work against the wrong
rule. The rulebook stays the single source, exactly as it is for `build_allowed_values.py`.

WHAT IT PARSES
--------------
Every `| \\`label\\` | means ... |` row in the rulebook, under whichever `## N. EN · ...` heading it
sits, so each label also knows which axis it belongs to. The third column, where present, is the
evidence the rulebook REQUIRES for that label -- which is the thing a reviewer checks the agent's
reason against, so it is kept too.
"""

import argparse
import collections
import json
import os
import re

import runner_core as rc

RULEBOOK = ("docs", "question_categories", "RULEBOOK.md")
OUT = ("papers_v2", "mappings", "label_glossary.json")

#: `## 5. E5 · Trap — one option, one mistake, or nothing`
HEADING = re.compile(r"^##\s+\d+\.\s+(E\d)\s*·\s*(.+?)\s*$", re.M)
#: A table row whose first cell holds one or more backticked labels. The rulebook defines some
#: pairs on ONE row -- "`structure_options` / `reaction_options` | the four OPTIONS are structures /
#: reactions" -- so the first cell is captured whole and split, rather than only its first label.
ROW = re.compile(r"^\|\s*((?:`[a-z0-9_]+`\s*/?\s*)+)\|([^|]*)\|?([^|]*)\|?\s*$", re.M)
LABELS_IN_CELL = re.compile(r"`([a-z0-9_]+)`")
#: `**\`elimination\` requires a demonstrated shortcut:** name the one pair ... ` -- a definition
#: written as a bold paragraph rather than a table row.
PROSE_DEF = re.compile(r"\*\*`([a-z0-9_]+)`[^*]{0,60}?\*\*\s*([^\n]{10,320})")


def build():
    with open(rc.pp(*RULEBOOK), encoding="utf-8") as fh:
        text = fh.read()

    # Which axis each region of the file belongs to, so a label picks up its own heading.
    marks = [(m.start(), m.group(1), m.group(2)) for m in HEADING.finditer(text)]
    marks.append((len(text), None, None))

    glossary, by_axis, axes_meta = {}, collections.Counter(), {}
    for index in range(len(marks) - 1):
        start, axis, axis_name = marks[index]
        end = marks[index + 1][0]
        if not axis:
            continue
        # The heading itself names the axis and says in plain words what it decides:
        # "E1 - Question type - the shape on the page". Split so the page can show both.
        name, _, gloss = (axis_name or "").partition("\u2014")
        axes_meta[axis] = {"name": name.strip(), "means": gloss.strip()}
        for row in ROW.finditer(text[start:end]):
            labels = LABELS_IN_CELL.findall(row.group(1))
            # The rulebook is markdown, so a definition may carry `**emphasis**` or backticks. The
            # page is not markdown, and the asterisks were printing literally.
            means = re.sub(r"\s+", " ", row.group(2)).strip()
            means = re.sub(r"\*\*(.+?)\*\*", r"\1", means).replace("`", "")
            evidence = re.sub(r"\s+", " ", row.group(3) or "").strip()
            if not means or means.lower() in ("means", "---"):
                continue
            for label in labels:
                # A label defined in two axes keeps the FIRST definition: the rulebook defines each
                # label once and mentions it elsewhere, so a later row is a mention, not a
                # redefinition.
                if label in glossary:
                    continue
                glossary[label] = {"axis": axis, "axis_name": axis_name,
                                   "means": means.strip(" *`"),
                                   "requires": evidence.strip(" *`") or None}
                by_axis[axis] += 1
    # PROSE DEFINITIONS. Not every label is defined in a table: `strategy_available`'s five values
    # are introduced as a bare list, and two of them are then explained in bold paragraphs --
    # "**`elimination` requires a demonstrated shortcut:** name the one pair or fact and the options
    # it strikes out". Those are real definitions and were being missed, so the page said "not
    # defined in the rulebook" about a label the rulebook does define.
    for match in PROSE_DEF.finditer(text):
        label, means = match.group(1), re.sub(r"\s+", " ", match.group(2)).strip()
        means = re.sub(r"\*\*(.+?)\*\*", r"\1", means).replace("`", "")
        if label in glossary or not means:
            continue
        axis = "E4" if label in ("elimination", "estimation", "symmetry", "dimensional_check",
                                 "unit_sanity") else None
        glossary[label] = {"axis": axis, "axis_name": axes_meta.get(axis, {}).get("name", ""),
                           "means": means.rstrip(" .") , "requires": None, "from": "prose"}
        if axis:
            by_axis[axis] += 1
    return glossary, by_axis, axes_meta


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    glossary, by_axis, axes_meta = build()
    print("labels defined in the rulebook: %d" % len(glossary))
    for axis in sorted(axes_meta):
        print("  %s  %-26s %s" % (axis, axes_meta[axis]["name"], axes_meta[axis]["means"]))
    for axis, count in sorted(by_axis.items()):
        print("  %-4s %3d" % (axis, count))

    # Anything in the allowed list with no definition is a gap worth seeing: the agent may emit it
    # and the page would then show a label it cannot explain.
    try:
        import yaml
        allowed = yaml.safe_load(open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8"))
        axes = ("question_type", "format", "content_shape", "cognitive_demand",
                "solution_structure", "strategy_available", "trap")
        missing = [(axis, value) for axis in axes for value in (allowed.get(axis) or [])
                   if value not in glossary]
        print("allowed values with NO rulebook definition: %d" % len(missing))
        for axis, value in missing[:20]:
            print("  %-20s %s" % (axis, value))
    except Exception as exc:                       # pragma: no cover - reporting only
        print("could not cross-check allowed_values.yaml: %s" % exc)

    if args.apply:
        path = rc.pp(*OUT)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"source": "docs/question_categories/RULEBOOK.md",
                       "axes": axes_meta, "labels": glossary}, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % os.path.relpath(path, rc.pp()))
    else:
        print("(nothing written -- pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
