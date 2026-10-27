"""Step-specific check for B3S (agents/b3s-solution-reader.md + schemas/B3S.json).

The schema fixes the shape. This adds the rules a JSON schema cannot state, each one standing for a
way a solution transcription goes wrong:

  (1) A COMPLETE SOLUTION HAS STEPS, OR IS A DRAWING. `complete: true` with an empty
      `solution_stepwise` and no figure says "I read it all and it said nothing", which is never the
      case for a printed worked solution.

  (2) THE STEPS ARE COPIED, NOT PARAPHRASED INTO ONE. A single step longer than this is the
      publisher's working merged into a paragraph -- the brief's rule 3. Measured nothing yet on v2,
      so the bound is generous: a printed step is a line or two, and 600 characters is several.

  (3) AN UNCLEAR CONCLUSION, OR A CLIPPED CROP, HAS TO SAY WHY in `note`. SPEC Rule 19: a blank
      with a reason and a field nobody judged must not look the same.

  (4) A FIGURE NEEDS A BOX. `has_figure: true` with no `figure_bbox` cannot be cut, so the figure
      silently disappears -- the same case cut_agent_figures.py records for B3V.

WHAT IS DELIBERATELY NOT HERE: whether `concludes` agrees with the printed answer. That
disagreement is a FINDING, raised as B3S_CONTRADICTS_PRINTED_ANSWER by the plugin, never a failure:
the agent is right to report what the working says even when the booklet's answer line says
otherwise.
"""

#: See rule (2) above.
MAX_STEP_CHARS = 600


def check(output, item=None, record=None, root=".", **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]
    steps = output.get("solution_stepwise") or []
    note = (output.get("note") or "").strip()
    problems = []
    # ...unless the whole printed solution IS a drawing. 2017 Code-A q52 (a reaction scheme) and q53
    # (a BCl3 structure) print no words at all, and a figure is never transcribed here, so an empty
    # step list with `has_figure: true` is the correct answer, not an omission.
    if output.get("complete") and not steps and not output.get("has_figure"):
        problems.append("complete is true but solution_stepwise is empty and no figure is reported")
    long_steps = [n for n, step in enumerate(steps, 1) if len(step) > MAX_STEP_CHARS]
    if long_steps:
        problems.append("step(s) %s exceed %d characters -- one entry per PRINTED step, not a "
                        "merged paragraph" % (",".join(map(str, long_steps)), MAX_STEP_CHARS))
    if output.get("concludes") == "unclear" and not note:
        problems.append("concludes is 'unclear' with an empty note -- say why the working does not "
                        "land on an option")
    if output.get("complete") is False and not note:
        problems.append("complete is false with an empty note -- say where the crop cuts off")
    if output.get("has_figure") and not output.get("figure_bbox"):
        problems.append("has_figure is true but figure_bbox is null")
    # (5) EVERY FIGURE IS BOXED AT A REAL STEP. A solution with three free-body diagrams reported one
    # box (2017_A q36) -- the other two were lost. `figures` lists them all; each must sit after a
    # step that exists, or it cannot be placed where the working uses it.
    figures = output.get("figures")
    if output.get("has_figure") and figures is None:
        problems.append("has_figure is true but there is no `figures` list -- box every drawing "
                        "with its after_step")
    if figures is not None:
        if output.get("has_figure") and not figures:
            problems.append("has_figure is true but figures is empty -- box every drawing")
        for n, figure in enumerate(figures, 1):
            box = figure.get("bbox") or []
            if len(box) != 4 or box[2] - box[0] < 4 or box[3] - box[1] < 4:
                problems.append("figures[%d] has a degenerate bbox %s" % (n, box))
            if figure.get("after_step", 0) > len(steps):
                problems.append("figures[%d] is placed after step %d but there are %d steps"
                                % (n, figure.get("after_step"), len(steps)))
    if problems:
        return False, "; ".join(problems)
    return True, "ok"
