#!/usr/bin/env python3
"""D10 - build candidate repeat groups for one subtopic (spec docs/SPEC.md Section 12/D10,
schemas/D10.json).

SCRIPT-only, and deliberately so. Spec 12/D10, verbatim and complete:

    Item: one subtopic - Worker: SCRIPT (build_groups.py): union-find over D9 links; one
    candidate group per connected component; each question in at most one group per subtopic.
    No judgement.

"No judgement" is the whole point of this step: D9 casts a wide net, D10 only takes the
transitive closure of what D9 found, and D11 is the strict verdict. This file therefore contains
no similarity measure, no threshold and no tie-break -- nothing that could quietly decide
anything. If two questions end up in one group it is because D9 linked them, directly or through
a chain.

Usage (per scripts/CONVENTIONS.md's own escape hatch for a step whose item is not a chapter --
D10's item is a SUBTOPIC, so it takes --subtopic-id, documented in that file's table):

    python3 scripts/build_groups.py --subtopic-id BIO12-CH03-ST04
    python3 scripts/build_groups.py --all        # every subtopic that has any D9-resolved question

Writes steps/D10/out/<SUBTOPIC_ID>.json. Spec names no output path for D10, so this build uses
the ordinary steps/<STEP>/out/<ITEM>.json shape of spec 5.8 with no run label -- the same choice
D3 (fetch_passages.py) made for its own script-written per-question output.

Where the links come from
-------------------------
`papers/records/<QID>.json`'s `d9_possible_repeats`, written into the record by
step_plugins.D9Plugin when D9 resolved for that question (every step writes its field both to
steps/<STEP>/out/ for history and into the record as the current value, spec 5.8). A question with
no `d9_possible_repeats` key has not had D9 resolved and is skipped entirely (not treated as
"linked to nothing") -- so a half-run subtopic cannot silently produce groups that are missing
members. A question whose D9 said `none` has the key present and empty, and correctly lands in
`singletons`.

Links are UNDIRECTED here. Spec 12/D9 says "every question runs D9, so links are seen from both
sides; a one-sided link is kept" -- so A listing B is the same edge as B listing A, and one side
alone is enough.

Links are SCOPED to the subtopic being built. A link from a question in this subtopic to a
question that is not in it is dropped for this subtopic's purposes (it will be used in that other
subtopic's own file if the two share one). This is what "each question in at most one group per
subtopic" means in practice, and it is why the same question can legitimately appear in two
different subtopics' D10 files.

Idempotence (spec 5.9: "running a command twice in a row must do nothing the second time")
------------------------------------------------------------------------------------------
Repeat-group ids are counter-backed and never reused (lib/ids.py::next_repeat_group_id, spec 6.1),
so blindly re-minting on every run would burn ids and change the file on a no-op rerun. Instead
this script reads its own previous output for the subtopic first and REUSES the group_id of any
component whose member set is exactly unchanged; a genuinely new component mints a new id. A
rerun with unchanged input therefore writes byte-identical output and mints nothing.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.lib import ids as lib_ids
from scripts.lib import io as lib_io


def _records():
    """{qid: record} for every CANONICAL question record (spec/C1 convention: a record carrying
    `merged_into` is the absorbed half of a booklet-code merge and must be skipped by every
    downstream record walk -- docs/OPEN_QUESTIONS.md 2026-10-11)."""
    out = {}
    records_dir = lib_io.project_path("papers", "records")
    if not os.path.isdir(records_dir):
        return out
    for fn in sorted(os.listdir(records_dir)):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        with open(os.path.join(records_dir, fn), "r", encoding="utf-8") as f:
            record = json.load(f)
        if record.get("merged_into"):
            continue
        out[fn[: -len(".json")]] = record
    return out


def _d9_resolved(record):
    """True when D9 has actually been resolved for this question (the key exists at all), as
    opposed to "D9 found nothing" (key present, list empty)."""
    return "d9_possible_repeats" in record


def subtopics_with_work(records=None):
    """Every subtopic id that has at least one D9-resolved question in it."""
    records = records if records is not None else _records()
    out = set()
    for record in records.values():
        if not _d9_resolved(record):
            continue
        for sid in record.get("d2_subtopic_ids") or []:
            if sid and sid != "unsure":
                out.add(sid)
    return sorted(out)


def _out_path(subtopic_id):
    return lib_io.project_path("steps", "D10", "out", f"{subtopic_id}.json")


def _previous_groups(subtopic_id):
    """{frozenset(members): group_id} from this subtopic's own previous D10 output, for id reuse."""
    path = _out_path(subtopic_id)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (ValueError, OSError):
        return {}
    out = {}
    for g in data.get("groups") or []:
        members = g.get("members") or []
        gid = g.get("group_id")
        if members and gid:
            out[frozenset(members)] = gid
    return out


class _UnionFind:
    """Plain union-find with path compression. No weighting, no judgement -- see module docstring."""

    def __init__(self):
        self.parent = {}

    def add(self, x):
        self.parent.setdefault(x, x)

    def find(self, x):
        self.add(x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            # Deterministic merge direction (lexicographically smaller root wins) so two runs over
            # the same input always produce the same parent map.
            lo, hi = sorted((ra, rb))
            self.parent[hi] = lo


def build_for_subtopic(subtopic_id, records=None):
    records = records if records is not None else _records()

    in_subtopic = {
        qid: record for qid, record in records.items()
        if subtopic_id in (record.get("d2_subtopic_ids") or []) and _d9_resolved(record)
    }

    uf = _UnionFind()
    for qid in in_subtopic:
        uf.add(qid)

    links = set()
    for qid, record in in_subtopic.items():
        for other in record.get("d9_possible_repeats") or []:
            if other == qid or other not in in_subtopic:
                continue  # out of this subtopic -> belongs to that other subtopic's own file
            links.add(tuple(sorted((qid, other))))
    for a, b in links:
        uf.union(a, b)

    components = {}
    for qid in in_subtopic:
        components.setdefault(uf.find(qid), []).append(qid)

    previous = _previous_groups(subtopic_id)
    groups, singletons = [], []
    for _root, members in sorted(components.items(), key=lambda kv: sorted(kv[1])):
        members = sorted(members)
        if len(members) < 2:
            singletons.extend(members)
            continue
        gid = previous.get(frozenset(members)) or lib_ids.next_repeat_group_id()
        groups.append({"group_id": gid, "members": members})
    groups.sort(key=lambda g: g["members"])

    out = {
        "subtopic_id": subtopic_id,
        "groups": groups,
        "singletons": sorted(singletons),
        "links_used": sorted([list(pair) for pair in links]),
    }
    path = _out_path(subtopic_id)
    lib_io.ensure_parent(path)
    lib_io.atomic_write_json(path, out)
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="D10: build candidate repeat groups for one subtopic (union-find over D9 links)."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--subtopic-id", help="Subtopic id, e.g. BIO12-CH03-ST04.")
    group.add_argument("--all", action="store_true",
                       help="Every subtopic that has at least one D9-resolved question.")
    args = parser.parse_args(argv)

    records = _records()
    targets = [args.subtopic_id] if args.subtopic_id else subtopics_with_work(records)
    if not targets:
        print("build_groups.py: no subtopic has a D9-resolved question yet; nothing to do.")
        return 0

    for subtopic_id in targets:
        out = build_for_subtopic(subtopic_id, records)
        print(f"build_groups.py {subtopic_id}: groups={len(out['groups'])} "
              f"singletons={len(out['singletons'])} links={len(out['links_used'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
