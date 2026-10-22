"""Step-specific check for D11 (spec Section 12/D11 'Checks' + d11-group-confirmer.md and
codebook/D11.md §2 "The mechanics you must satisfy").

spec 12/D11 Checks, verbatim: "every member exactly once; first = earliest year/sitting; groups
>= 2 members; runs agree." The first three are per-run and live here; "runs agree" needs both
runs at once and lives in step_plugins.D11Plugin.check() (the same split as D1/D2/A4).

  (1) EVERY INPUT MEMBER EXACTLY ONCE, across groups + related + removed combined. Nothing may be
      dropped silently and nothing may appear twice -- including appearing in two different
      groups after a split. And no id may appear that was not in the candidate group at all.
  (2) `first` = earliest year, earliest sitting within a year. The within-year sitting order is
      NOT invented here: it is the index of the sitting in lib/sittings.py's REQUIRED_SITTINGS
      for that year, which is already written in chronological order (2016: [MAIN, PH2]; 2026:
      [CANCELLED (3 May), REEXAM (21 Jun)]) and is the project's single source of truth for the
      exam calendar. A year or sitting the calendar does not list falls back to alphabetical,
      which is deterministic but arbitrary -- flagged in the message when it happens rather than
      passed off as authoritative.
  (3) groups >= 2 members (also schema-enforced); exactly ONE member of each group carries the
      label `first`, and it is the member the group's own `first` field names.
  (4) codebook/D11.md §2: "Every label is relative to that first member, never to the member
      before it." Not mechanically checkable (it is about how the agent reasoned), but its one
      mechanical consequence is: no member other than the first may be labelled `first`. Checked
      in (3).
  (5) `related[i].related_to` must be a member of the candidate group -- codebook/D11.md §3 says
      it points at the group's first member, so a related_to that is not any group's `first` is
      reported (as a soft segment, since a candidate group that produced NO group at all has no
      first to point at, and in that case related_to pointing at any input member is the only
      honest thing the agent can write).

What is DELIBERATELY NOT checked here: whether a label is the RIGHT label (exact_same vs reworded
vs same_fact_new_format vs same_problem_new_numbers), or whether a removal was correct. Those are
the judgement D11 exists to make; disagreement between the two runs is what routes them to the
adjudicator (D11_ADJUDICATED, normal), not a script's opinion.

Convention: def check(data, context) -> (bool, str). Segments are ';'-joined.
"""
import os
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from lib import sittings as lib_sittings  # noqa: E402

_LABELS = {"first", "exact_same", "reworded", "same_fact_new_format", "same_problem_new_numbers"}


def sitting_sort_key(year, sitting):
    """Chronological sort key for one (year, sitting) pair, for 'first = earliest year/sitting'.

    Reuses lib/sittings.py::REQUIRED_SITTINGS, whose per-year lists are already in chronological
    order (verbatim from spec Section 8 / S0's procedure: 2016 MAIN then PH2; 2026 CANCELLED on
    3 May then REEXAM on 21 Jun). Returns (year, rank, sitting) where rank is the sitting's index
    in that year's list, or a large sentinel for a sitting the calendar does not list for that
    year -- in which case the trailing `sitting` string makes the order deterministic
    (alphabetical) rather than unstable. step_plugins.D11Plugin imports this same function so the
    check and the runner can never disagree about which member is earliest.
    """
    year_int = int(year) if year is not None else 0
    calendar = lib_sittings.REQUIRED_SITTINGS.get(year_int) or []
    sitting_str = (sitting or "")
    try:
        rank = calendar.index(sitting_str)
    except ValueError:
        rank = 99
    return (year_int, rank, sitting_str)


def _is_calendar_known(year, sitting):
    calendar = lib_sittings.REQUIRED_SITTINGS.get(int(year) if year is not None else 0) or []
    return (sitting or "") in calendar


def check(data, context):
    if not isinstance(data, dict):
        return False, "D11 output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    groups = data.get("groups")
    related = data.get("related")
    removed = data.get("removed")
    if not isinstance(groups, list):
        return False, "groups is not a list"
    if not isinstance(related, list):
        return False, "related is not a list"
    if not isinstance(removed, list):
        return False, "removed is not a list"

    input_data = context.get("input_data") or {}
    members_meta = input_data.get("members") or {}  # {qid: {"year": int, "sitting": str}}
    candidate_ids = set(members_meta.keys())

    segments = []
    placements = {}  # qid -> list of where it was placed

    def place(qid, where):
        placements.setdefault(qid, []).append(where)

    firsts = set()
    for gi, g in enumerate(groups):
        if not isinstance(g, dict):
            segments.append(f"groups[{gi}] is not an object")
            continue
        gmembers = g.get("members")
        declared_first = g.get("first")
        if not isinstance(gmembers, list):
            segments.append(f"groups[{gi}] members is not a list")
            continue
        if len(gmembers) < 2:
            segments.append(
                f"groups[{gi}] has {len(gmembers)} member(s); a group needs >= 2 (a lone survivor "
                f"goes to related or removed)"
            )

        ids_here, labelled_first = [], []
        for m in gmembers:
            if not isinstance(m, dict):
                segments.append(f"groups[{gi}] contains a non-object member")
                continue
            qid, label = m.get("id"), m.get("label")
            ids_here.append(qid)
            place(qid, f"groups[{gi}]")
            if label not in _LABELS:
                segments.append(f"groups[{gi}] member {qid!r} has label {label!r}, not one of {sorted(_LABELS)}")
            if label == "first":
                labelled_first.append(qid)

        if len(labelled_first) != 1:
            segments.append(
                f"groups[{gi}] has {len(labelled_first)} member(s) labelled 'first' ({labelled_first}); "
                f"exactly one is required, and every other label is relative to it"
            )
        elif declared_first != labelled_first[0]:
            segments.append(
                f"groups[{gi}] declares first={declared_first!r} but the member labelled 'first' "
                f"is {labelled_first[0]!r}"
            )
        if declared_first:
            firsts.add(declared_first)

        known = [q for q in ids_here if q in members_meta]
        if known and declared_first in members_meta:
            earliest = min(
                known,
                key=lambda q: sitting_sort_key(members_meta[q].get("year"), members_meta[q].get("sitting")),
            )
            if earliest != declared_first:
                unknown_cal = [q for q in known
                               if not _is_calendar_known(members_meta[q].get("year"),
                                                         members_meta[q].get("sitting"))]
                extra = (f" (note: sitting(s) of {unknown_cal} are not on lib/sittings.py's "
                         f"calendar for their year, so their within-year order fell back to "
                         f"alphabetical)") if unknown_cal else ""
                segments.append(
                    f"groups[{gi}] first={declared_first!r} "
                    f"({members_meta[declared_first].get('year')}/"
                    f"{members_meta[declared_first].get('sitting')}) is not the earliest member; "
                    f"{earliest!r} ({members_meta[earliest].get('year')}/"
                    f"{members_meta[earliest].get('sitting')}) is earlier{extra}"
                )

    for ri, r in enumerate(related):
        if not isinstance(r, dict):
            segments.append(f"related[{ri}] is not an object")
            continue
        place(r.get("id"), f"related[{ri}]")

    for qid in removed:
        place(qid, "removed")

    # (1) every input member exactly once; nothing invented.
    for qid in sorted(candidate_ids):
        where = placements.get(qid) or []
        if not where:
            segments.append(f"candidate member {qid!r} appears nowhere in groups/related/removed")
        elif len(where) > 1:
            segments.append(f"candidate member {qid!r} appears {len(where)} times ({where})")
    for qid in sorted(set(placements) - candidate_ids):
        segments.append(
            f"{qid!r} appears in the output but was not a member of this candidate group "
            f"({sorted(candidate_ids)})"
        )

    # (5) related_to points at a group's first (soft -- see module docstring).
    for ri, r in enumerate(related):
        if not isinstance(r, dict):
            continue
        rt = r.get("related_to")
        if firsts and rt not in firsts:
            segments.append(
                f"related[{ri}].related_to={rt!r} is not any group's first member ({sorted(firsts)})"
            )
        elif not firsts and candidate_ids and rt not in candidate_ids:
            segments.append(
                f"related[{ri}].related_to={rt!r} is not a member of this candidate group"
            )

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
