#!/usr/bin/env python3
"""Bring the agent-facing codebooks onto the current category vocabulary.

    python3 scripts/migrate_codebooks.py --dry-run
    python3 scripts/migrate_codebooks.py --apply

`codebook/E1.md` .. `codebook/E5.md` are what the E-step agents actually read -- roughly 78k
characters of per-label guidance, worked examples and tie-break notes built against real questions.
All five still teach the v0.2 vocabulary, so an agent reading `codebook/E5.md` would answer
`swapped_positions` or `opposite_answer` and its own schema would then reject the answer.

WHAT THIS DOES AND DELIBERATELY DOES NOT DO
-------------------------------------------
A retirement with exactly ONE replacement is a rename, and renaming it in prose is safe and
mechanical. A retirement offering a CHOICE is a split -- `sign_or_direction` became one of four
labels depending on what actually reversed -- and rewriting those passages requires reading the
question each one cites. Picking the first option automatically would silently assign one meaning
out of four and look like a completed migration.

So: renames are applied, splits are marked in place with a visible marker and listed for authoring.
Nothing is deleted; the guidance those paragraphs carry is the reason not to regenerate the files.

The marker is a blockquote the agent will read as an instruction, which is the point: until a human
or an authoring agent rewrites the passage, the agent is told the label is gone and what to use.
"""

import argparse
import collections
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks"))
import runner_core as rc  # noqa: E402
import category_label_census as census  # noqa: E402

AXES = ["E1", "E2", "E3", "E4", "E5"]
MARKER = "RETIRED-SPLIT"


#: `config/allowed_values.yaml` key -> the axis whose codebook it governs. Needed because the SAME
#: v0.2 name lived on two axes: `process` was an E3 content shape AND an E4 thinking value, and it
#: is still live on E3 while E4 retired it. An axis-blind rename rewrites E3's live label.
KEY_AXIS = {
    "question_type": "E1",
    "format": "E2",
    "content_shape": "E3",
    "cognitive_demand": "E4",
    "solution_structure": "E4",
    "strategy_available": "E4",
    # the generator records E4's lineage under the pre-split key name, since that is what the
    # retired values belonged to before the axis became three keys
    "thinking": "E4",
    "trap": "E5",
    "trap_verdict": "E5",
}

#: v0.2 names that are also ordinary English words. Even confined to code spans these are risky, so
#: they are reported and never auto-renamed: `formula` reads as a formula, `list` as a list.
ENGLISH_WORDS = {"list", "table", "formula", "exception", "process", "comparison", "graph",
                 "diagram", "reaction", "trend", "one_line"}

#: Mappings this project authored by hand and rated weak. A weak mapping is fine as a lineage entry
#: (it keeps the chain total) and wrong as an automatic rewrite of guidance prose, because the
#: paragraph it rewrites describes a task the new label does not quite name.
WEAK = {"odd_one_out": "the v2 label grades every option; odd-one-out is arguably its own task"}


def lineage():
    """Per axis: {old: [replacements]} and that axis's live set.

    Kept per axis rather than merged. A name retired on one axis can be live on another, and the
    merged view cannot tell the difference.
    """
    secs = census.rulebook_sections()
    options, live = {}, {}
    for axis in AXES:
        section = secs.get(census.SECTION[axis], "")
        options[axis] = census.replacement_options(section)
        lv, _ = census.split_retired(section)
        live[axis] = set(lv) | set(census.PROSE_LABELS.get(axis, ()))
    return options, live


def v02_predecessors():
    """{axis: {old v0.2 name: current label}} from the generated lineage, kept per axis."""
    import yaml
    allowed = yaml.safe_load(open(rc.pp("config", "allowed_values.yaml"), encoding="utf-8"))
    out = collections.defaultdict(dict)
    for key, mapping in (allowed.get("category_retired") or {}).items():
        axis = KEY_AXIS.get(key)
        if axis:
            out[axis].update(mapping or {})
    ambiguous = set(allowed.get("category_ambiguous") or {})
    return out, ambiguous


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("pass --dry-run or --apply")

    options, live = lineage()
    v02, ambiguous = v02_predecessors()

    total = collections.Counter()
    for axis in AXES:
        path = rc.pp("codebook", "%s.md" % axis)
        if not os.path.exists(path):
            continue
        text = original = open(path, encoding="utf-8").read()
        axis_live, axis_opts = live[axis], options[axis]

        # A v0.2 name is renamable on THIS axis only if: the rulebook gives it exactly one
        # replacement, it is not itself still live here, it is not an ordinary English word, and the
        # source records its successor unambiguously.
        renames, splits, held, moved = {}, {}, {}, {}
        for old, new in v02.get(axis, {}).items():
            if old in axis_live:
                held[old] = "still a live label on %s" % axis
            elif old in ambiguous:
                held[old] = "two v1 rows both claim this name"
            elif old in ENGLISH_WORDS:
                held[old] = "also an ordinary English word"
            elif old in WEAK:
                held[old] = WEAK[old]
            elif len(axis_opts.get(old, [new])) > 1:
                splits[old] = axis_opts[old]
            elif new in axis_live:
                renames[old] = new
            elif new in set().union(*live.values()):
                # the label did not disappear, it MOVED to another axis; the paragraph here needs
                # rewriting, and the agent must be told not to answer with it on this axis
                moved[old] = new
            else:
                held[old] = "target %r is live on no axis" % new
        for old, news in axis_opts.items():
            if len(news) > 1 and old not in axis_live:
                splits[old] = news

        applied = collections.Counter()
        for old, new in sorted(renames.items(), key=lambda kv: -len(kv[0])):
            # ONLY inside a code span. Label references in these codebooks are backticked by
            # convention, and renaming bare prose rewrote English words into label names.
            pattern = re.compile(r"`%s`" % re.escape(old))
            text, n = pattern.subn("`%s`" % new, text)
            if n:
                applied[old] = n

        found_splits = collections.Counter()
        for old, news in sorted(splits.items(), key=lambda kv: -len(kv[0])):
            n = len(re.findall(r"`%s`" % re.escape(old), text))
            if n:
                found_splits[old] = n

        # Every retired label still readable in this file must be warned about, including the ones
        # held back on purpose. A held-back rename is a decision not to rewrite prose -- it is NOT a
        # decision to let an agent answer with a label its own schema will reject.
        found_held = collections.Counter()
        for old in held:
            n = len(re.findall(r"`%s`" % re.escape(old), text))
            if n:
                found_held[old] = n

        found_moved = collections.Counter()
        for old in moved:
            n = len(re.findall(r"`%s`" % re.escape(old), text))
            if n:
                found_moved[old] = n

        # one marker block per file, naming every split and every cross-axis move it still contains
        if (found_splits or found_moved or found_held) and MARKER not in text:
            lines = ["", "> **%s -- this codebook still teaches labels that were split.**" % MARKER,
                     "> Each label below no longer exists on its own. Do NOT answer with it; choose",
                     "> the replacement that matches what the question actually does, and if none",
                     "> does, use this axis's escape hatch and describe what you saw.", ">"]
            for old, n in found_splits.most_common():
                lines.append("> - `%s` (%d mentions below) -> choose between %s"
                             % (old, n, ", ".join("`%s`" % x for x in splits[old])))
            for old, n in found_moved.most_common():
                lines.append("> - `%s` (%d mentions below) left this axis entirely -> `%s`. Never"
                             " answer it here." % (old, n, moved[old]))
            for old, n in found_held.most_common():
                target = v02.get(axis, {}).get(old)
                lines.append("> - `%s` (%d mentions below) is retired%s. The guidance was left in"
                             " place because %s."
                             % (old, n, (" -> `%s`" % target) if target else "", held[old]))
            lines += ["> The passages below have not yet been rewritten; the rulebook"
                      " (`docs/question_categories/RULEBOOK.md`) is authoritative where they"
                      " disagree.", ""]
            # insert after the file's first heading so the agent reads it before any guidance
            m = re.search(r"^#.*$", text, re.M)
            at = m.end() if m else 0
            text = text[:at] + "\n" + "\n".join(lines) + text[at:]

        changed = sum(applied.values())
        print("codebook/%s.md  %d renames applied, %d split + %d moved mentions flagged"
              % (axis, changed, sum(found_splits.values()), sum(found_moved.values())))
        for old, n in applied.most_common(6):
            print("      %-30s -> %-28s x%d" % (old, renames[old], n))
        if found_splits or found_moved or found_held:
            print("      NEEDS AUTHORING: %s"
                  % ", ".join(["%s x%d (split)" % (o, n) for o, n in found_splits.most_common()]
                              + ["%s x%d (moved to another axis)" % (o, n)
                                 for o, n in found_moved.most_common()]
                              + ["%s x%d (held)" % (o, n) for o, n in found_held.most_common()]))
        if held:
            print("      held back deliberately: %s"
                  % "; ".join("%s (%s)" % (o, why) for o, why in sorted(held.items())))
        missing = sorted(l for l in axis_live if ("`%s`" % l) not in text)
        if missing:
            print("      live %s labels with NO guidance here: %d  %s"
                  % (axis, len(missing), ", ".join(missing[:6])
                     + (" ..." if len(missing) > 6 else "")))
        total["renames"] += changed
        total["flagged"] += (sum(found_splits.values()) + sum(found_moved.values())
                             + sum(found_held.values()))
        total["undocumented"] += len(missing)

        if args.apply and text != original:
            open(path, "w", encoding="utf-8").write(text)
        elif args.dry_run and text != original:
            diff = list(difflib.unified_diff(original.splitlines(), text.splitlines(), n=0))
            print("      (%d diff lines)" % len(diff))
        print()

    print("%d renames, %d split mentions flagged, %d live labels with no guidance"
          % (total["renames"], total["flagged"], total["undocumented"]))
    if args.dry_run:
        print("(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
