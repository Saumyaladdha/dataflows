"""Step-specific check for FIGC (agents/figc-structure-reader.md + schemas/FIGC.json).

The schema fixes the shape. This is the chemistry the schema cannot see, and it is code, not the
writer -- the whole point of the split (lib/chem_cards.py):

  (1) EVERY FIGURE GETS A CARD. The input lists the figures; a card missing for one is a drawing
      that silently never gets a structure.
  (2) EVERY SMILES PARSES, every reaction SMILES parses, a wildcard [*] says what it stands for.
  (3) THE NAME REBUILDS THE SAME MOLECULE. OPSIN turns the printed name back into a structure and
      its InChIKey must equal the SMILES's. A `mismatch` FAILS the card and goes back to the agent
      word for word -- the team guide's loop, and the only check that catches meta labelled para.
      `unparsed` (ions, radicals, resonance forms) and `not_run` (no Java) are recorded, not failed.
  (4) EVERY CARD SAYS WHAT IT SHOWS IN WORDS. `text` is what the question's searchable text carries
      in place of the picture; without it 2017_A q061's whole reaction scheme was absent from the
      question as a query returns it ("Consider the reactions : Identify A, X, Y and Z").
  (6) EVERY SMILES IS THE PRINTED MOLECULE. Where the booklet's figure is a vector drawing
      (lib/print_trace.py), each structure on the page is read as a graph -- bonds, double and
      triple lines, labels such as OCH3 and NO2 with their hydrogens -- and each SMILES must lay on
      one of them atom for atom; every printed structure must have its SMILES. This is what catches
      meta written for para, or a methyl where the print has an ethyl, before anything is drawn.
      Such a figure is then DRAWN on that geometry, so (5) is satisfied by construction for it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import chem_cards, figure_text, print_trace  # noqa: E402
import figure_plugins  # noqa: E402


def check(output, item=None, **_kwargs):
    if not isinstance(output, dict):
        return False, "output is not a JSON object"
    if "error" in output:
        return True, "agent reported an error: %s" % output["error"]
    problems = []
    cards = output.get("figures") or []
    wanted = [f["figure_id"] for f in ((item or {}).get("figures") or [])]
    have = [c.get("figure_id") for c in cards]
    for figure_id in wanted:
        if figure_id not in have:
            problems.append("no card for figure %s" % figure_id)
    for figure_id in have:
        if wanted and figure_id not in wanted:
            problems.append("card for unknown figure %s" % figure_id)
    printed = {f["figure_id"]: f.get("printed_text") for f in ((item or {}).get("figures") or [])}
    boxes = {f["figure_id"]: f for f in ((item or {}).get("figures") or [])}
    for card in cards:
        traced = False
        box = boxes.get(card.get("figure_id")) or {}
        if card.get("kind") != "not_a_structure" and (item or {}).get("source_pdf"):
            trace = figure_plugins.trace_of(item["source_pdf"], item["dpi"], box.get("page"),
                                            box.get("bbox"))
            if trace is not None and print_trace.usable(trace):
                traced = True
                _results, wrong = print_trace.assign(trace, card.get("species") or [])
                problems += ["figure %s: %s" % (card["figure_id"], w) for w in wrong]
        # (5) NOTHING PRINTED IS DROPPED. Every word inside the figure's box on the page must be
        #     drawn (a label, scheme text, an arrow's conditions, an annotation), be chemistry the
        #     structure shows itself, or be listed in `excluded_text` with why.
        if not traced and card.get("kind") != "not_a_structure" and printed.get(card.get("figure_id")):
            gone = figure_text.missing(printed[card["figure_id"]], chem_cards.drawn_texts(card),
                                       [e.get("text", "") for e in card.get("excluded_text") or []],
                                       elements=chem_cards.elements(card))
            if gone:
                problems.append("figure %s: printed text not in the drawing: %s -- draw each (scheme "
                                "text, arrow above/below, species label, annotation) or list it in "
                                "`excluded_text` with why" % (card["figure_id"], ", ".join(gone)))
        if card.get("kind") == "reaction" and not card.get("scheme"):
            problems.append("figure %s is a reaction with no `scheme`: the arrow's printed "
                            "conditions are only drawn from the scheme (rule 12)" % card.get("figure_id"))
        if not (card.get("text") or "").strip():
            problems.append("figure %s has no `text`: write the figure out in one line (rule 10)"
                            % card.get("figure_id"))
        problems += chem_cards.check_card(card)
        for n, species in enumerate(card.get("species") or [], 1):
            status, detail = chem_cards.name_check(species.get("name"), species.get("smiles") or "")
            if status == "mismatch":
                problems.append("%s species %d: the name %r does not give this SMILES (%s)"
                                % (card.get("figure_id"), n, species.get("name"), detail))
    if problems:
        return False, "; ".join(problems)
    return True, "ok"
