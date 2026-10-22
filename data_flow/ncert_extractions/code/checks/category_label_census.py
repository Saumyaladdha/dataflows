#!/usr/bin/env python3
"""Count the labels on every category axis, and reconcile three populations per axis.

    python3 scripts/checks/category_label_census.py

Three different things get called "the categories", and conflating them is how the trap total came
out wrong once already:

  * what `docs/question_categories/RULEBOOK.md` DEFINES  (v2, written against a 55-row showcase)
  * what the 580-question corpus actually USES           (v1 tagging, `exports/discovery/QUESTIONS.xlsx`)
  * what survives the v1 -> v2 mapping                   (live, after retirements and renames)

A label in use but undefined is the dangerous case: the rulebook is supposed to be the single source
of truth, so anything applied to a question but absent from the rulebook is being applied from
memory. This script exists so that number is measured rather than typed.
"""

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import runner_core as rc  # noqa: E402

CORPUS = ("exports", "discovery", "QUESTIONS.xlsx")
RULEBOOK = ("docs", "question_categories", "RULEBOOK.md")

#: which spreadsheet column carries each axis
COLUMN = {
    "E1": "E1 question type",
    "E2": "E2 format",
    "E3": "E3 content shape",
    "E4": "E4 thinking",
    "E5": "E5 trap",
}
#: the rulebook section that governs each axis
SECTION = {"E1": "1.", "E2": "2.", "E3": "3.", "E4": "4.", "E5": "5."}

#: labels the rulebook states in prose rather than in a table, so the table scrape cannot see them
PROSE_LABELS = {
    # section 4c lists the strategies inline
    "E4": ["elimination", "estimation", "symmetry", "dimensional_check", "unit_sanity"],
    # section 3 names the content shapes it re-scopes but never tabulates the full list
    "E3": [],
}

BLANK = ("", "none", "-")


def rulebook_sections():
    """Split RULEBOOK.md on its `## ` headings, keyed by the leading section number."""
    text = open(rc.pp(*RULEBOOK), encoding="utf-8").read()
    out = {}
    for chunk in re.split(r"\n## ", text):
        title = chunk.split("\n", 1)[0].strip()
        m = re.match(r"^(\d+\.)", title)
        if m:
            out[m.group(1)] = chunk
    return out


def table_labels(section):
    """Labels in the FIRST cell of each table row -- that cell is the label by convention.

    A row may define two at once (`structure_options` / `reaction_options`), so both are taken.
    """
    pairs = re.findall(
        r"^\|\s*`([a-z][a-z0-9_]*)`(?:\s*/\s*`([a-z][a-z0-9_]*)`)?\s*\|", section, re.M)
    return [x for pair in pairs for x in pair if x]


def split_retired(section):
    """Separate a section's live labels from the ones its retirement table lists.

    Section 5 has two tables, live then retired, divided by the `**Retired, and why**` heading. The
    retired table's first cell can hold two comma-separated labels retired to one replacement.
    """
    # the heading is written as "**Retired**", "**Retired, and why**" or "**Retired:**"
    parts = re.split(r"\*\*Retired(?:\*\*|,|:|\s)", section, maxsplit=1)
    live = table_labels(parts[0])
    retired = []
    if len(parts) > 1:
        for row in re.findall(r"^\|\s*([^|]+?)\s*\|", parts[1], re.M):
            retired += re.findall(r"`([a-z][a-z0-9_]*)`", row)
        # section 4 states its retirements in a prose paragraph, not a table
        retired += re.findall(r"`([a-z][a-z0-9_]*)`(?=\s*\(->|\s*\(→)", parts[1])
    # The prose "Retired:" paragraph used by section 4 writes each retirement as
    #   `old` (-> `new`),  and sometimes  `old_a` and `old_b` (-> somewhere)
    # so a label followed directly by "(" misses every item in a shared list. Drop the
    # parenthesised replacements first; whatever backticks remain are the retired labels.
    for para in re.findall(r"\*\*Retired:\*\*(.+?)(?:\n\n|\Z)", section, re.S):
        retired += re.findall(r"`([a-z][a-z0-9_]*)`", re.sub(r"\([^)]*\)", " ", para))
    return live, sorted(set(retired))


def replacement_targets(section):
    """Live labels that exist as the REPLACEMENT for something retired.

    The corpus is tagged in v1 names, so a v2 replacement name cannot appear in it -- by
    construction, not by oversight. Reporting those as "defined but never used" would hide the
    labels that really have never been applied to anything.
    """
    out = []
    # the heading is written as "**Retired**", "**Retired, and why**" or "**Retired:**"
    parts = re.split(r"\*\*Retired(?:\*\*|,|:|\s)", section, maxsplit=1)
    if len(parts) > 1:
        for row in re.findall(r"^\|[^|]*\|\s*([^|]+?)\s*\|", parts[1], re.M):
            out += re.findall(r"`([a-z][a-z0-9_]*)`", row)
    for para in re.findall(r"\*\*Retired:\*\*(.+?)(?:\n\n|\Z)", section, re.S):
        for inner in re.findall(r"\(([^)]*)\)", para):
            out += re.findall(r"`([a-z][a-z0-9_]*)`", inner)
    # the closing sentence of section 5 names its replacements outright
    for para in re.findall(r"are\s*\nREPLACEMENTS[^.]*\.", section):
        out += re.findall(r"`([a-z][a-z0-9_]*)`", para)
    return set(out)


def replacement_map(section):
    """{retired label: its current replacement}, from a section's retirement table or paragraph.

    A retirement row is `| old | replaced by | reason |`, and either cell may name several labels --
    two labels retired to one replacement, or one label retired to a choice of three that must be
    re-judged. Where a choice is offered, the FIRST replacement is recorded as the default target so
    the lineage is total; the rulebook row remains the authority on when the others apply.
    """
    out = {}
    parts = re.split(r"\*\*Retired(?:\*\*|,|:|\s)", section, maxsplit=1)
    if len(parts) > 1:
        for old_cell, new_cell in re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", parts[1], re.M):
            olds = re.findall(r"`([a-z][a-z0-9_]*)`", old_cell)
            news = re.findall(r"`([a-z][a-z0-9_]*)`", new_cell)
            for old in olds:
                if news:
                    out[old] = news[0]
    # section 4's prose form: `old` (-> `new`), `a` and `b` (-> `new`)
    for para in re.findall(r"\*\*Retired:\*\*(.+?)(?:\n\n|\Z)", section, re.S):
        for chunk in re.findall(r"((?:`[a-z][a-z0-9_]*`(?:,| and )?\s*)+)\((?:->|→)([^)]*)\)", para):
            news = re.findall(r"`([a-z][a-z0-9_]*)`", chunk[1])
            for old in re.findall(r"`([a-z][a-z0-9_]*)`", chunk[0]):
                if news:
                    out[old] = news[0]
    return out


def replacement_options(section):
    """{retired label: [every replacement the rulebook offers]}.

    `replacement_map` collapses this to one default target so a lineage is total. The ARITY matters
    separately: a retirement with ONE replacement is a rename and can be applied mechanically, while
    one offering a choice ("`sign_or_direction` -> `sign_reversed_magnitude_right`,
    `inverted_ratio`, `reversed_order` or `semantic_reversal`") is a split that needs a judgement per
    occurrence. Renaming a split automatically would silently pick one meaning out of four.
    """
    out = {}
    parts = re.split(r"\*\*Retired(?:\*\*|,|:|\s)", section, maxsplit=1)
    if len(parts) > 1:
        for old_cell, new_cell in re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", parts[1], re.M):
            news = re.findall(r"`([a-z][a-z0-9_]*)`", new_cell)
            for old in re.findall(r"`([a-z][a-z0-9_]*)`", old_cell):
                if news:
                    out[old] = news
    for para in re.findall(r"\*\*Retired:\*\*(.+?)(?:\n\n|\Z)", section, re.S):
        for chunk in re.findall(r"((?:`[a-z][a-z0-9_]*`(?:,| and )?\s*)+)\((?:->|→)([^)]*)\)", para):
            news = re.findall(r"`([a-z][a-z0-9_]*)`", chunk[1])
            for old in re.findall(r"`([a-z][a-z0-9_]*)`", chunk[0]):
                if news:
                    out[old] = news
    return out


def corpus_usage():
    """How often each label is applied across the real corpus, per axis."""
    import openpyxl
    wb = openpyxl.load_workbook(rc.pp(*CORPUS), read_only=True)
    rows = list(wb["Questions"].iter_rows(values_only=True))
    head = {h: i for i, h in enumerate(rows[0]) if h}
    used, tagged = {}, {}
    for axis, col in COLUMN.items():
        counts = collections.Counter()
        n = 0
        for raw in rows[1:]:
            value = str(raw[head[col]] or "").strip()
            if value.lower() not in BLANK:
                n += 1
            for label in value.split(";"):
                label = label.strip()
                if label and label.lower() not in BLANK:
                    counts[label] += 1
        used[axis], tagged[axis] = counts, n
    return used, tagged, len(rows) - 1


#: The PRODUCTION vocabulary: which `config/allowed_values.yaml` key feeds each axis. This is the
#: list the runner actually validates against, via schemas/E1-E5.json -- so a label the rulebook
#: retired can still be emitted by a live step, and a label the rulebook added cannot be emitted at
#: all. The rulebook is authoritative for MEANING; this file is authoritative for what passes a
#: check. They have to agree, and nothing was comparing them.
ALLOWED_KEY = {
    "E1": ["question_type"],
    "E2": ["format"],
    "E3": ["content_shape"],
    # E4 is three sub-axes in v2, so it is three keys. It was one key (`thinking_draft` plus an
    # owner-decision list) while the axis was still conflating demand, structure and strategy.
    "E4": ["cognitive_demand", "solution_structure", "strategy_available"],
    # `trap_verdict` holds section 5a's two NON-trap verdicts. They are allowed values of the axis
    # and must count here, but they are deliberately NOT in the `trap` enum.
    "E5": ["trap", "trap_verdict"],
}

#: Which schema field carries each axis's vocabulary. Needed because a schema holds several enums --
#: schemas/E4.json also has `branch_used` (physical/organic/botany/...) and every schema has
#: `confidence`. Taking the union of all enums in a file reports those as vocabulary drift.
SCHEMA_FIELD = {
    "E1": [("E1", "question_type")],
    "E2": [("E2", "format")],
    "E3": [("E3", "content_shape")],
    "E4": [("E4", "primary"), ("E4", "secondary")],
    "E5": [("E5", "trap")],
}


def production_vocabulary():
    """Per axis, the values a live step is allowed to emit."""
    import yaml
    with open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8") as fh:
        allowed = yaml.safe_load(fh)
    out = {}
    for axis, keys in ALLOWED_KEY.items():
        names = set()
        for key in keys:
            value = allowed.get(key) or []
            names |= set(value if isinstance(value, list) else value.keys())
        out[axis] = names
    return out, allowed.get("version")


def schema_enums():
    """The enum each step's output schema enforces for ITS OWN axis field, so drift is visible.

    Read field by field, not as the union of every enum in the file: schemas/E4.json also carries
    `branch_used`, and taking the union reported physical/organic/botany as category drift.
    """
    out = {}
    for axis, fields in SCHEMA_FIELD.items():
        found = set()
        for schema, field in fields:
            path = rc.pp("schemas", "%s.json" % schema)
            if not os.path.exists(path):
                continue
            blob = open(path, encoding="utf-8").read()
            m = re.search(r'"%s"\s*:\s*\{[^{}]*?"enum"\s*:\s*\[(.*?)\]' % re.escape(field),
                          blob, re.S)
            if m:
                found |= set(re.findall(r'"([a-z][a-z0-9_]*)"', m.group(1)))
        out[axis] = found
    return out


def builder_retirements():
    """v1 labels the sheet builder already maps onto a v2 label -- i.e. retired in code.

    Imported rather than restated, so the two files cannot disagree about what was retired.
    """
    import build_category_sheet_v2 as b
    out = set(b.E4_DEMAND) | set(b.E4_STRUCTURE) | set(b.E4_MOVED)
    out |= set(b.E5_RENAME) | set(b.E5_RETIRED) | set(b.E5_NEEDS_REJUDGE)
    # a label that maps to ITSELF was kept, not retired
    return out - set(b.E4_DEMAND.get(k) == k and k or "" for k in b.E4_DEMAND)


def main():
    secs = rulebook_sections()
    used, tagged, total = corpus_usage()
    mapped_away = builder_retirements()

    print("corpus: %s -- %d questions\n" % (os.path.join(*CORPUS), total))
    grand = collections.Counter()
    for axis in ("E1", "E2", "E3", "E4", "E5"):
        section = secs.get(SECTION[axis], "")
        live, retired = split_retired(section)
        live = sorted(set(live) | set(PROSE_LABELS.get(axis, [])))
        retired = [r for r in retired if r not in live]
        counts = used[axis]
        targets = replacement_targets(section)
        # Some labels are absent from the rulebook yet already RETIRED in the builder's maps --
        # a retirement that was made in code and never written down. That is a documentation gap,
        # not a missing definition, and counting it as the latter inflates the axis total.
        retired = sorted(set(retired) | {l for l in counts if l in mapped_away})
        undefined = sorted((l for l in counts if l not in live and l not in retired),
                           key=lambda l: -counts[l])
        # a v2 replacement absent from a v1-tagged corpus is expected; anything else is not
        awaiting = sorted(l for l in live if l not in counts and l in targets)
        unused = sorted(l for l in live if l not in counts and l not in targets)

        print("%s  rulebook defines %2d live + %2d retired     corpus uses %2d "
              "(%d tags on %d/%d questions)"
              % (axis, len(live), len(retired), len(counts), sum(counts.values()),
                 tagged[axis], total))
        print("      in use but NOT in the rulebook : %2d%s"
              % (len(undefined),
                 ("   " + ", ".join("%s(%d)" % (l, counts[l]) for l in undefined)) if undefined else ""))
        print("      v2 replacement, awaits re-judge: %2d%s"
              % (len(awaiting), ("   " + ", ".join(awaiting)) if awaiting else ""))
        print("      never applied to any question  : %2d%s"
              % (len(unused), ("   " + ", ".join(unused)) if unused else ""))
        print("      TOTAL once the gaps are written: %2d\n" % (len(live) + len(undefined)))
        grand["defined"] += len(live)
        grand["retired"] += len(retired)
        grand["in_use"] += len(counts)
        grand["undefined"] += len(undefined)
        grand["awaiting"] += len(awaiting)
        grand["unused"] += len(unused)
        grand["total"] += len(live) + len(undefined)

    prod, version = production_vocabulary()
    enums = schema_enums()
    print("--- the production vocabulary (config/allowed_values.yaml %s + schemas/E*.json) ---"
          % version)
    print("This is what a live step may emit. A rulebook label absent here CANNOT be produced;\n"
          "an allowed value the rulebook retired CAN still be produced and would pass its check.\n")
    gap = collections.Counter()
    for axis in ("E1", "E2", "E3", "E4", "E5"):
        section = secs.get(SECTION[axis], "")
        live, retired = split_retired(section)
        live = set(live) | set(PROSE_LABELS.get(axis, ()))
        allowed = prod.get(axis, set())
        unemittable = sorted(live - allowed)
        emittable_but_retired = sorted(allowed & set(retired))
        unknown = sorted(allowed - live - set(retired))
        print("%s  rulebook live %2d   allowed_values %2d   schema enum %2d"
              % (axis, len(live), len(allowed), len(enums.get(axis, ()))))
        print("      rulebook label a step CANNOT emit : %2d%s"
              % (len(unemittable), ("   " + ", ".join(unemittable)) if unemittable else ""))
        print("      retired, yet still emittable      : %2d%s"
              % (len(emittable_but_retired),
                 ("   " + ", ".join(emittable_but_retired)) if emittable_but_retired else ""))
        print("      allowed, unknown to the rulebook  : %2d%s"
              % (len(unknown), ("   " + ", ".join(unknown)) if unknown else ""))
        if enums.get(axis) and enums[axis] - allowed:
            print("      SCHEMA DRIFT, enum beyond allowed : %s"
                  % ", ".join(sorted(enums[axis] - allowed)))
        gap["unemittable"] += len(unemittable)
        gap["retired_emittable"] += len(emittable_but_retired)
        gap["unknown"] += len(unknown)
        print()
    print("   production gap: %d rulebook labels unemittable, %d retired labels still emittable, "
          "%d allowed values undefined\n"
          % (gap["unemittable"], gap["retired_emittable"], gap["unknown"]))

    print("across all five axes")
    print("   defined live in the rulebook   : %3d" % grand["defined"])
    print("   documented as retired          : %3d" % grand["retired"])
    print("   distinct labels the corpus uses: %3d" % grand["in_use"])
    print("   IN USE BUT UNDEFINED           : %3d   <- applied from memory, not from the rulebook"
          % grand["undefined"])
    print("   v2 replacements awaiting re-judge: %1d" % grand["awaiting"])
    print("   never applied to any question  : %3d" % grand["unused"])
    print("   TOTAL once the gaps are written: %3d" % grand["total"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
