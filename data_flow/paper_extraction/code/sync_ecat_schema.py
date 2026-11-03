#!/usr/bin/env python3
"""Copy the ECAT vocabularies from config/allowed_values.yaml into schemas/ECAT.json.

    python3 code/sync_ecat_schema.py          # report drift
    python3 code/sync_ecat_schema.py --apply  # fix it

ONE SOURCE OF TRUTH, ENFORCED BY A SCRIPT RATHER THAN BY MEMORY. The vocabulary lives in the
YAML; the schema holds a copy because a JSON Schema cannot read YAML. That copy went stale the
first time the vocabulary was renamed -- the YAML said `fact_line` and `arithmetic_slip`, the
schema still said `ncert_fact` and `calculation_error`, and the brief pointed at the YAML. A
rater following the brief produced output the schema rejected, which is the drift that put four
different trap lists in four files in the first place.
"""
import argparse, json, sys, yaml

AXES = (("qtype", ("qtype",)), ("asks", ("asks",)),
        ("trap_v2", ("trap", "properties", "label")))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    av = yaml.safe_load(open("config/allowed_values.yaml", encoding="utf-8"))
    s = json.load(open("schemas/ECAT.json", encoding="utf-8"))
    props = s["oneOf"][0]["properties"]["ratings"]["items"]["properties"]
    drift = []
    for key, path in AXES:
        node = props
        for p in path:
            node = node[p] if p in node else node["properties"][p]
        # A value list shared by two sites lives in `$defs` and is reached by `$ref`, so the
        # walk has to follow it -- otherwise the enum reads as empty and every value looks new.
        while "$ref" in node:
            target = node["$ref"].lstrip("#/").split("/")
            node = s
            for seg in target:
                node = node[seg]
        if node.get("enum") != av[key]:
            drift.append((key, node.get("enum"), av[key]))
            if a.apply:
                node["enum"] = av[key]
    if not drift:
        print("in sync")
        return 0
    for key, old, new in drift:
        print("DRIFT %s: schema has %d values, yaml has %d" % (key, len(old or []), len(new)))
        print("   only in schema:", sorted(set(old or []) - set(new)) or "-")
        print("   only in yaml  :", sorted(set(new) - set(old or [])) or "-")
    if a.apply:
        json.dump(s, open("schemas/ECAT.json", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("schema updated")
        return 0
    print("(pass --apply to fix)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
