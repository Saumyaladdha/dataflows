"""Step-specific check for FIGP (agents/figp-figure-redrawer.md + schemas/FIGP.json).

Physics has no OPSIN -- no rule-based second route back to the drawing. What it has instead is that
a figure ASSERTS quantities, and an asserted quantity is recomputable from the coordinates that were
drawn (FIGURE_RENDERING_PLAN.md 3.2). So the check is lib/physics_figure.check_spec():

  (1) the spec RENDERS -- every primitive is one the renderer draws, with its required keys;
  (2) every angle the figure labels is CLAIMED, and the claim equals the drawn angle within 1.5
      degrees -- the pilot's first draft drew a vector at 40.7 degrees under a 60-degree label;
  (3) a circuit's NETLIST matches the connectivity its wires actually make -- a wire to the wrong
      node looks perfectly fine on screen and is the error that matters most in a schematic;
  (4) a figure declared out of scope says why, in `unreadable`, so nobody re-attempts it blind.
  (6) THE SPEC IS THE PRINTED FIGURE. Where the booklet's figure is a vector drawing, every label
      the spec draws must be printed in it, and laid on the print by those labels the spec's lines
      must lie on the printed ones and cover them (lib/spec_trace.py). Such a figure is then DRAWN
      on the booklet's own geometry -- the spec stays the checked data -- so it looks like the print.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import figure_text, physics_figure  # noqa: E402
import figure_plugins  # noqa: E402

#: A circuit's components, by primitive kind. A spec that draws two or more of them is a circuit and
#: must declare its netlist, or the most important check here never runs.
CIRCUIT_KINDS = ("resistor", "capacitor", "battery", "inductor", "switch", "diode", "cell", "meter")


def check(output, item=None, **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]
    if output.get("out_of_scope"):
        if not output.get("unreadable"):
            return False, "out_of_scope is true but `unreadable` does not say why"
        return True, "out of scope: %s" % "; ".join(output["unreadable"])
    spec = output.get("spec") or {}
    problems = physics_figure.check_spec(spec)
    components = [d for d in spec.get("draw") or [] if d.get("kind") in physics_figure.TWO_TERMINAL]
    if len(components) >= 2:
        missing_id = [d.get("kind") for d in components if not d.get("id")]
        if missing_id:
            problems.append("circuit components without an `id`: %s -- every component needs one "
                            "so the netlist can be checked" % missing_id)
        if not spec.get("netlist"):
            problems.append("a circuit with %d components declares no `netlist`" % len(components))
    # (5) NOTHING PRINTED IS DROPPED: every word inside the figure's box on the page is a drawn
    #     label, or is listed in `excluded_text` with why (lib/figure_text.py).
    if (item or {}).get("printed_text"):
        gone = figure_text.missing(item["printed_text"], drawn_texts(spec),
                                   [e.get("text", "") for e in output.get("excluded_text") or []])
        if gone:
            problems.append("printed text not in the drawing: %s -- draw each as a `label` (with "
                            "sub/sup) or list it in `excluded_text` with why" % ", ".join(gone))
    if not problems and (item or {}).get("source_pdf"):
        _trace, wrong = figure_plugins.physics_trace(item, item, spec)
        problems += ["not the printed figure: %s" % w for w in wrong]
    if problems:
        return False, "; ".join(problems)
    return True, "ok"


def drawn_texts(spec):
    """Every text the spec draws: labels with their sub/superscripts, meter letters."""
    out = []
    for item in spec.get("draw") or []:
        for key in ("text", "sub", "sup"):
            if item.get(key):
                out.append(str(item[key]))
        if item.get("text") and (item.get("sub") or item.get("sup")):
            out.append("%s%s%s" % (item["text"], item.get("sub") or "", item.get("sup") or ""))
    return out
