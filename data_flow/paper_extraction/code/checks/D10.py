"""Step-specific check for D10 (spec Section 12/D10).

spec 12/D10, verbatim and complete: "Item: one subtopic · Worker: SCRIPT (build_groups.py):
union-find over D9 links; one candidate group per connected component; each question in at most
one group per subtopic. No judgement."

D10 is a pure SCRIPT step, so this check is not auditing an agent -- it is auditing
scripts/build_groups.py's own union-find, which is exactly where a silent off-by-one or a
double-add would be invisible otherwise. schemas/D10.json already pins the shape, the RG-nnnn
group-id format and `minItems: 2` on members. This file verifies the three properties that make
the output a correct partition:

  (1) "each question in at most one group per subtopic": no qid appears in two groups, and no qid
      appears both in a group and in `singletons`.
  (2) "one candidate group per connected component": every link in `links_used` has BOTH
      endpoints in the SAME group. If a link crosses two groups, the components were not fully
      merged -- the classic union-find bug. And every member of every group must be reachable
      through `links_used` from the rest of its group, i.e. a group may not contain a question
      that no recorded link connects to it (checked as: every group member appears in at least
      one of that group's links).
  (3) groups have >= 2 members (schema-enforced, re-stated here so a hand-built or future
      non-schema-validated writer can't slip past), and every id in `links_used` is accounted for
      in some group.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "D10 output is not an object"

    groups = data.get("groups")
    singletons = data.get("singletons")
    links = data.get("links_used")
    if not isinstance(groups, list):
        return False, "groups is not a list"
    if not isinstance(singletons, list):
        return False, "singletons is not a list"
    if not isinstance(links, list):
        return False, "links_used is not a list"

    segments = []

    # (1) partition: no qid in two groups, no qid in both a group and singletons.
    owner = {}
    group_ids = set()
    for g in groups:
        if not isinstance(g, dict):
            segments.append("groups contains a non-object item")
            continue
        gid = g.get("group_id")
        members = g.get("members")
        if gid in group_ids:
            segments.append(f"group_id {gid!r} appears twice")
        group_ids.add(gid)
        if not isinstance(members, list):
            segments.append(f"group {gid!r} members is not a list")
            continue
        if len(members) < 2:
            segments.append(
                f"group {gid!r} has {len(members)} member(s); a candidate group needs >= 2 "
                f"(a lone question belongs in `singletons`)"
            )
        if len(members) != len(set(members)):
            segments.append(f"group {gid!r} repeats a member")
        for qid in members:
            if qid in owner:
                segments.append(
                    f"{qid!r} is in two groups ({owner[qid]!r} and {gid!r}); each question is in "
                    f"at most one group per subtopic"
                )
            owner[qid] = gid

    both = sorted(set(singletons) & set(owner))
    if both:
        segments.append(f"{both} appear in both a group and `singletons`")
    if len(singletons) != len(set(singletons)):
        segments.append("singletons repeats an id")

    # (2) every link's endpoints in the same group; every group member touched by a link.
    touched_by_group = {}
    for pair in links:
        if not isinstance(pair, list) or len(pair) != 2:
            segments.append(f"links_used contains a malformed pair: {pair!r}")
            continue
        a, b = pair
        ga, gb = owner.get(a), owner.get(b)
        if ga is None or gb is None:
            segments.append(
                f"link [{a!r}, {b!r}] has an endpoint in no group at all (ga={ga!r}, gb={gb!r}); "
                f"a linked question is never a singleton"
            )
            continue
        if ga != gb:
            segments.append(
                f"link [{a!r}, {b!r}] crosses two groups ({ga!r} and {gb!r}); the connected "
                f"components were not fully merged"
            )
            continue
        touched_by_group.setdefault(ga, set()).update((a, b))

    for g in groups:
        if not isinstance(g, dict):
            continue
        gid, members = g.get("group_id"), g.get("members") or []
        untouched = sorted(set(members) - touched_by_group.get(gid, set()))
        if untouched:
            segments.append(
                f"group {gid!r} contains {untouched}, which no recorded link connects to the rest "
                f"of the group"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
