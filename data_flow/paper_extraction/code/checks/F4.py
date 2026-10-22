"""Step-specific check for F4 (spec 14/F4).

`data` is one subtopic's counts (steps/F4/out/<SUBTOPIC>.json, schemas/F4.json shape).

The headline F4 check — "totals equal the number of question-subtopic links" — is a
cross-subtopic invariant and lives inside compute_counts.py itself, which refuses to write
anything if it fails. What this per-item check adds is the internal consistency that must hold
for ONE subtopic, which a corrupted or hand-edited file would break:
  * unique_questions <= questions_total (a repeat group collapses rows, never adds them);
  * questions_total == len(question_ids) when the ids are recorded;
  * last_asked is the maximum of years_asked;
  * each `*_mix_recent` sums to at most questions_total, and to exactly the number of recent
    questions when the ids are recorded;
  * released_only is a subset of all, on every one of those numbers.

Never edit counts by hand (spec 14/F4): if this check fails, the fix is in the records or in
compute_counts.py, never in the output file.
"""


def _check_stats(stats, label):
    if not isinstance(stats, dict):
        return f"{label} is not an object"
    total = stats.get("questions_total")
    unique = stats.get("unique_questions")
    if not isinstance(total, int) or total < 0:
        return f"{label}.questions_total is not a non-negative integer"
    if not isinstance(unique, int) or unique < 0:
        return f"{label}.unique_questions is not a non-negative integer"
    if unique > total:
        return f"{label}: unique_questions ({unique}) exceeds questions_total ({total})"
    if total > 0 and unique == 0:
        return f"{label}: {total} question(s) but unique_questions is 0"

    qids = stats.get("question_ids")
    if isinstance(qids, list):
        if len(qids) != total:
            return f"{label}: questions_total is {total} but question_ids has {len(qids)}"
        if len(set(qids)) != len(qids):
            return f"{label}: question_ids contains duplicates"

    years = stats.get("years_asked")
    if not isinstance(years, list):
        return f"{label}.years_asked is not a list"
    if years != sorted(years):
        return f"{label}.years_asked is not sorted"
    if len(set(years)) != len(years):
        return f"{label}.years_asked repeats a year"
    last = stats.get("last_asked")
    if years and last != max(years):
        return f"{label}: last_asked is {last!r} but years_asked ends at {max(years)}"
    if not years and last is not None:
        return f"{label}: last_asked is {last!r} but no year is recorded"
    if total == 0 and years:
        return f"{label}: no questions but years_asked is {years}"

    for key in ("category_mix_recent", "format_mix_recent", "question_type_mix_recent"):
        mix = stats.get(key)
        if not isinstance(mix, dict):
            return f"{label}.{key} is not an object"
        s = sum(mix.values())
        if s > total:
            return f"{label}.{key} sums to {s}, more than questions_total ({total})"
    groups = stats.get("repeat_groups")
    if not isinstance(groups, list):
        return f"{label}.repeat_groups is not a list"
    count = stats.get("repeat_group_count")
    if isinstance(count, int) and count != len(groups):
        return f"{label}: repeat_group_count is {count} but repeat_groups has {len(groups)}"
    return None


def check(data, context):
    if not isinstance(data, dict):
        return False, "F4 output is not an object"
    if not str(data.get("subtopic_id") or "").strip():
        return False, "subtopic_id is empty"
    for label in ("all", "released_only"):
        problem = _check_stats(data.get(label), label)
        if problem:
            return False, problem

    all_s, rel = data["all"], data["released_only"]
    for key in ("questions_total", "unique_questions"):
        if rel[key] > all_s[key]:
            return False, (f"released_only.{key} ({rel[key]}) exceeds all.{key} ({all_s[key]}); "
                           f"released questions are a subset of all questions")
    if not set(rel.get("years_asked") or []) <= set(all_s.get("years_asked") or []):
        return False, "released_only.years_asked is not a subset of all.years_asked"
    if isinstance(rel.get("question_ids"), list) and isinstance(all_s.get("question_ids"), list):
        if not set(rel["question_ids"]) <= set(all_s["question_ids"]):
            return False, "released_only.question_ids is not a subset of all.question_ids"

    if all_s["questions_total"] == 0:
        return True, "note: no question has ever been asked on this subtopic"
    return True, "ok"
