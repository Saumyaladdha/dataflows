#!/usr/bin/env python3
"""Turn `new_*` proposals from a rating run into real vocabulary values.

    python3 code/promote_ecat_proposals.py --paper 2017_A                  # show them
    python3 code/promote_ecat_proposals.py --paper 2017_A --apply --min 2  # add them

WHY PROMOTION IS A SEPARATE STEP
--------------------------------
A rater that meets a question the lists cannot say writes `new_trap` and proposes a name. That
is deliberately NOT the same as adding the value: one rater, on one question, is exactly the
evidence that produced the 23-trap list that had to be cut back to 9, where five values had a
single question each and no family could form.

So a proposal becomes a value when the SAME device is proposed on more than one question
(`--min`, default 2), and stays a proposal otherwise -- visible, named, countable, and not yet
part of the vocabulary. A value with one question is a card with a long name.

Promoting writes the value into `allowed_values.yaml` (the list, `category_means`, and
`display`), re-points the ratings that proposed it, and leaves the schema to
`sync_ecat_schema.py --apply`, which is the one place that copies a list into the schema.
"""

import argparse
import collections
import glob
import json
import os
import re

AXES = {"trap": ("trap_v2", "trap"), "asks": ("asks", "asks"), "qtype": ("qtype", "qtype")}


def gather(paper_id):
    """{axis: {proposed_name: [(path, rating, where, obj), ...]}}"""
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in sorted(glob.glob(os.path.join("steps", "ECAT", "out",
                                           "ex__%s__*.json" % paper_id))):
        try:
            doc = json.load(open(p, encoding="utf-8"))
        except ValueError:
            continue
        for r in doc.get("ratings") or []:
            # the DOC travels with the proposal. Re-reading the file at write time would
            # discard the edits made here and write the proposal back unchanged.
            sites = [("trap", r.get("trap") or {})]
            sites += [("also", x) for x in (r.get("also") or [])]
            for where, obj in sites:
                if str(obj.get("label", "")).startswith("new_"):
                    pr = obj.get("proposed") or {}
                    if pr.get("name"):
                        out["trap"][pr["name"]].append((p, doc, r, where, obj, pr.get("why", "")))
            for field in ("asks", "qtype"):
                if str(r.get(field, "")).startswith("new_"):
                    pr = r.get("%s_proposed" % field) or r.get("proposed") or {}
                    if pr.get("name"):
                        out[field][pr["name"]].append((p, doc, r, field, r, pr.get("why", "")))
    return out


def readable(name):
    """`true_but_not_asked` -> `True but not asked` -- a label, not a slug, on the card."""
    s = name.replace("_", " ").strip()
    return s[:1].upper() + s[1:]


def add_value(yaml_text, list_key, name, means):
    """Append to the list, to category_means and to display, keeping the file's own shape."""
    m = re.search(r"^%s:\n((?:- .*\n)+)" % re.escape(list_key), yaml_text, re.M)
    if not m:
        raise SystemExit("cannot find the %s list" % list_key)
    items = [l[2:].strip() for l in m.group(1).strip().split("\n")]
    if name in items:
        return yaml_text, False
    # before the `new_*` escape hatch, which stays last
    tail = [i for i in items if i.startswith("new_")]
    body = [i for i in items if not i.startswith("new_")] + [name] + tail
    yaml_text = (yaml_text[:m.start()] + "%s:\n" % list_key
                 + "".join("- %s\n" % v for v in body) + yaml_text[m.end():])
    for block, value in (("category_means", means), ("display", readable(name))):
        mm = re.search(r"^%s:\n(?:.*\n)*?  %s:\n" % (re.escape(block), re.escape(list_key)),
                       yaml_text, re.M)
        if mm:
            yaml_text = yaml_text[:mm.end()] + "    %s: '%s'\n" % (name, value.replace("'", "''")) \
                        + yaml_text[mm.end():]
    return yaml_text, True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--min", type=int, default=2,
                    help="how many questions must ask for it before it becomes a value")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    found = gather(a.paper)
    if not found:
        print("no proposals in this paper's ratings")
        return 0

    promote = []
    for axis, names in sorted(found.items()):
        print("\n%s" % axis.upper())
        for name, uses in sorted(names.items(), key=lambda kv: -len(kv[1])):
            qs = [r["question_id"] for _, _, r, _, _, _ in uses]
            verdict = "PROMOTE" if len(uses) >= a.min else "stays a proposal"
            print("  %-28s %d question(s)  %-18s %s"
                  % (name, len(uses), verdict, ", ".join(qs[:6])))
            print("      %s" % " ".join(uses[0][5].split())[:220])
            if len(uses) >= a.min:
                promote.append((axis, name, uses))

    if not promote:
        print("\nnothing reaches --min %d; every proposal stays a proposal" % a.min)
        return 0
    if not a.apply:
        print("\n(nothing written -- pass --apply)")
        return 0

    text = open("config/allowed_values.yaml", encoding="utf-8").read()
    for axis, name, uses in promote:
        list_key = AXES[axis][0]
        text, added = add_value(text, list_key, name, " ".join(uses[0][5].split())[:110])
        print("%s: %s %s" % (list_key, name, "added" if added else "already present"))
    open("config/allowed_values.yaml", "w", encoding="utf-8").write(text)

    # re-point the ratings that asked for it
    touched = {}
    for axis, name, uses in promote:
        for path, doc, rating, where, obj, _why in uses:
            if axis == "trap":
                obj["label"] = name
                obj.pop("proposed", None)
            else:
                rating[axis] = name
                rating.pop("%s_proposed" % axis, None)
            touched[path] = doc
    for path, doc in touched.items():
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nnow run: python3 code/sync_ecat_schema.py --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
