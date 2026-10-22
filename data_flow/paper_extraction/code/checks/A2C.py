#!/usr/bin/env python3
"""Check for A2C (a2c-structure-transcriber): one drawn structure read into SMILES.

Validates shape only. It deliberately does NOT validate the chemistry -- parsing SMILES would
need RDKit, and a check that silently rejected a correct-but-unusual structure because a parser
disliked it would be worse than no check. What it does enforce is that the agent cannot be vague:
a `structure` must name at least one species, a `reaction` must give a reaction SMILES, and
`not_a_structure` must carry neither. Every record must say what it read.
"""
import json
import sys


def check(path):
    try:
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return False, "unreadable: %s" % exc

    kind = rec.get("kind")
    if kind not in ("structure", "reaction", "not_a_structure"):
        return False, "kind must be structure, reaction or not_a_structure"
    if not (rec.get("note") or "").strip():
        return False, "note is required -- say what was read and what constrained it"

    species = rec.get("species") or []
    reaction = (rec.get("reaction_smiles") or "").strip()

    if kind == "structure":
        if not species:
            return False, "kind=structure but no species listed"
        for i, sp in enumerate(species):
            if not (sp.get("smiles") or "").strip():
                return False, "species[%d] has no smiles" % i
        if reaction:
            return False, "kind=structure must not carry reaction_smiles"
    elif kind == "reaction":
        if not reaction:
            return False, "kind=reaction but no reaction_smiles"
        if reaction.count(">") < 2:
            return False, "reaction_smiles must be reactants>agents>products"
        if species:
            return False, "kind=reaction must not also list species"
    else:
        if species or reaction:
            return False, "kind=not_a_structure must carry neither species nor reaction_smiles"

    if rec.get("confidence") not in (None, "certain", "probable", "unsure"):
        return False, "confidence must be certain, probable or unsure"
    return True, "ok"


if __name__ == "__main__":
    ok, msg = check(sys.argv[1])
    print(msg)
    sys.exit(0 if ok else 1)
