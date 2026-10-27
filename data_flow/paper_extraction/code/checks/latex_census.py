#!/usr/bin/env python3
"""LaTeX census and gate: every text field the export shows, rendered, with every failure counted.

    python3 code/checks/latex_census.py --paper-id 2017_A          # report
    python3 code/checks/latex_census.py --paper-id 2017_A --strict # exit 1 on any failure

WHY THIS EXISTS. lib/texhtml.py renders LaTeX at export time and shows a command it does not know
in red, by design. That design only works if someone looks: on 2017 Code-A the first full export
carried `\\ge` in red inside a printed solution, and nothing stopped it shipping. The renderer's
symbol table is meant to be built from a CENSUS of what the corpus emits; this script IS that census,
and `--strict` turns it into a gate the export runs before it writes anything.

WHAT COUNTS AS A FAILURE, each seen in real output:
  unknown   a `\\command` the renderer has no rendering for (shown red)
  raw       LaTeX that survived rendering as literal text: a backslash command, a `$`, or a brace
            pair the reader would see -- the "N_B" or "{-1}" that makes a formula unreadable
"""

import argparse
import collections
import glob
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import runner_core as rc  # noqa: E402
from lib import texhtml  # noqa: E402

#: Which fields of which step outputs reach the page, and so must render cleanly.
FIELDS = {
    "B3V": ("stem_en", "options_en", "statements", "list_i", "list_ii"),
    "B3S": ("solution_stepwise", "note"),
    "B6V": ("steps", "working", "reason", "note"),
    "E7V": ("steps", "why", "what_makes_it_hard"),
    "QSUBJ": ("why",),
    "QCHAP": ("why",),
    "QTOPIC": ("why",),
}
UNKNOWN = re.compile(r'<span class="tex-unknown">\\([A-Za-z]+)</span>')
#: Text left after rendering, with tags stripped: a backslash command, a dollar, or a {...} group.
RAW = re.compile(r"\\[A-Za-z]+|\$|\{[^{}]*\}")


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)


def census(paper_id):
    unknown, raw, examples = collections.Counter(), collections.Counter(), {}
    for step, fields in FIELDS.items():
        for path in sorted(glob.glob(rc.pp("steps", step, "out", "%s__q*.runA.json" % paper_id))):
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            item = os.path.basename(path).split(".")[0]
            for field in fields:
                for text in strings(data.get(field)):
                    out = texhtml.to_html(text)
                    for name in UNKNOWN.findall(out):
                        unknown["\\" + name] += 1
                        examples.setdefault("\\" + name, "%s %s.%s: %s" % (step, item, field, text[:90]))
                    # MALFORMED SOURCE. The JSON is read by other renderers (the app's KaTeX), which
                    # fail on an unpaired `$` or an unbalanced brace where this one degrades quietly.
                    bare = re.sub(r"\\[{}$]", "", text)
                    if bare.count("$") % 2:
                        raw["unpaired $"] += 1
                        examples.setdefault("unpaired $", "%s %s.%s: %s" % (step, item, field, text[:90]))
                    if bare.count("{") != bare.count("}"):
                        raw["unbalanced {}"] += 1
                        examples.setdefault("unbalanced {}", "%s %s.%s: %s" % (step, item, field, text[:90]))
                    visible = html.unescape(re.sub(r"<[^>]+>", "", UNKNOWN.sub("", out)))
                    # AN EMPTY SCRIPT is a script whose argument was not parsed: `120^\circ` once
                    # gave "120<sup></sup>circ", the command name spilled out as plain text.
                    if re.search(r"<(sup|sub)>\s*</\1>", out):
                        raw["empty script"] += 1
                        examples.setdefault("empty script", "%s %s.%s: %s" % (step, item, field, text[:90]))
                    # AN ARGUMENT PRINTED AS TEXT: an arrow's [below] label once rendered as
                    # "573 K]" -- no backslash, no dollar, so nothing above saw it. A square bracket
                    # the source balances and the rendering does not is that leak.
                    if (bare.count("[") == bare.count("]")
                            and visible.count("[") != visible.count("]")):
                        raw["unbalanced []"] += 1
                        examples.setdefault("unbalanced []", "%s %s.%s: %s" % (step, item, field, text[:90]))
                    for hit in RAW.findall(visible):
                        if hit.startswith("{") and "\\{" in text:
                            continue          # `\{a, c, d\}` IS a set in braces: correct output
                        raw[hit] += 1
                        examples.setdefault(hit, "%s %s.%s: %s" % (step, item, field, text[:90]))
    return unknown, raw, examples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    unknown, raw, examples = census(args.paper_id)
    print("LaTeX census for %s" % args.paper_id)
    print("  unknown commands (rendered red): %d distinct, %d uses"
          % (len(unknown), sum(unknown.values())))
    for name, n in unknown.most_common():
        print("    %-14s %4d   e.g. %s" % (name, n, examples[name]))
    print("  raw LaTeX left visible: %d distinct, %d uses" % (len(raw), sum(raw.values())))
    for name, n in raw.most_common(40):
        print("    %-14s %4d   e.g. %s" % (name, n, examples[name]))
    failed = bool(unknown or raw)
    print("FAIL" if failed else "PASS")
    return 1 if (failed and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
