"""Step-specific check for F1 (spec 14/F1).

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
`data` is one review-pack run summary (schemas/F1.json shape — review/review_pack/_manifest.json
or build_review_pack.build()'s first return value).

What this enforces beyond the schema:
  * the audit sample's seed is present and is the FIXED seed the step was asked to use, because
    "reproducible" is a requirement of the step, not a nicety (spec 14/F1);
  * every pack id has a page, and no two pack ids share one page file — a collision would hide
    one item's evidence behind another's;
  * queue_size agrees with the number of pack ids, so the queue a person is told about is the
    queue the pack contains.
"""


def check(data, context):
    if not isinstance(data, dict):
        return False, "F1 output is not an object"

    seed = data.get("seed")
    if not isinstance(seed, int):
        return False, "seed is missing or not an integer; the audit sample must be reproducible"
    expected = (context or {}).get("expected_seed")
    if expected is not None and seed != expected:
        return False, f"seed is {seed}, expected the fixed seed {expected}"

    pack_ids = data.get("pack_ids")
    if not isinstance(pack_ids, list):
        return False, "pack_ids is missing or not a list"
    if len(set(pack_ids)) != len(pack_ids):
        dupes = sorted({p for p in pack_ids if pack_ids.count(p) > 1})
        return False, f"duplicate pack_ids: {dupes[:5]}"

    queue_size = data.get("queue_size")
    if isinstance(queue_size, int) and queue_size != len(pack_ids):
        return False, (f"queue_size is {queue_size} but the pack has {len(pack_ids)} item(s); "
                       f"the queue and the pack must describe the same work")

    pages = data.get("pages")
    if pages is not None:
        if not isinstance(pages, dict):
            return False, "pages is not an object"
        missing = [p for p in pack_ids if p not in pages]
        if missing:
            return False, f"{len(missing)} pack id(s) have no page: {missing[:5]}"
        values = list(pages.values())
        if len(set(values)) != len(values):
            return False, "two pack ids share one page file; one item's evidence would hide the other's"

    if not pack_ids:
        return True, "note: the queue is empty — nothing needs review in this scope"
    return True, "ok"
