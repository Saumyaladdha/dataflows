"""Step-specific check for A2L (page layout): geometry is self-consistent, bboxes are real
fractions inside the page, every element sits in a declared column, sizes are ratios not pixel
counts, and any block `n` claimed actually exists on the page.

Convention: def check(data, context) -> (bool, str); see scripts/checks/S0.py's docstring.
"""

_COLUMN_IDS = {"full", "left", "right"}

# A size_rel is a RATIO to body text. Real pages run from about 0.7 (a small marginal note) to
# about 3.0 (a chapter title). A value far outside that is almost always an agent reporting a
# PIXEL height instead of a ratio -- the single most likely way to misread this field, and
# invisible downstream because a number is a number. Caught here instead.
_SIZE_REL_MIN, _SIZE_REL_MAX = 0.4, 4.0

# Furniture roles carry no quotable content, so they are expected to have no A2 block number.
_FURNITURE_ROLES = {
    "chapter_banner", "rule_bar", "page_header_band", "footer_rule",
    "decorative_image", "qr_code", "page_number", "running_header",
}


def _bbox_problem(bb):
    if not isinstance(bb, (list, tuple)) or len(bb) != 4:
        return "is not a 4-number list"
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in bb):
        return "has a non-numeric coordinate"
    x0, y0, x1, y1 = bb
    if any(v < 0 or v > 1 for v in bb):
        return (f"is not in page fractions 0-1 ({bb}) -- bboxes are fractions of page "
                f"width/height, not pixels")
    if x1 <= x0 or y1 <= y0:
        return f"is empty or inverted ({bb})"
    return None


def check(data, context):
    if not isinstance(data, dict):
        return False, "A2L output is not an object"
    if "error" in data:
        return False, f"agent reported error: {data['error']}"

    segments = []

    page = data.get("page")
    if not isinstance(page, dict):
        return False, "A2L_LAYOUT_BAD: missing `page` object"

    for key in ("width_px", "height_px"):
        v = page.get(key)
        if not isinstance(v, int) or isinstance(v, bool) or v <= 0:
            segments.append(f"A2L_LAYOUT_BAD: page.{key} must be a positive integer, got {v!r}")

    body = page.get("body_text_size_px")
    if not isinstance(body, (int, float)) or isinstance(body, bool) or body <= 0:
        segments.append(f"A2L_LAYOUT_BAD: page.body_text_size_px must be a positive number, "
                        f"got {body!r}")
    elif isinstance(page.get("height_px"), int) and body >= page["height_px"] * 0.25:
        # One line of body text taking a quarter of the page height is not a measurement, it is
        # a mistake -- most often the height of a whole paragraph or of the page itself.
        segments.append(f"A2L_LAYOUT_BAD: page.body_text_size_px={body} is implausibly large for "
                        f"a single line on a {page['height_px']}px-tall page")

    columns = page.get("columns")
    declared = set()
    if not isinstance(columns, list) or not columns:
        segments.append("A2L_LAYOUT_BAD: page.columns must be a non-empty list")
    else:
        for i, col in enumerate(columns):
            if not isinstance(col, dict):
                segments.append(f"A2L_LAYOUT_BAD: columns[{i}] is not an object")
                continue
            cid = col.get("id")
            if cid not in _COLUMN_IDS:
                segments.append(f"A2L_LAYOUT_BAD: columns[{i}].id {cid!r} not one of "
                                f"{sorted(_COLUMN_IDS)}")
            elif cid in declared:
                segments.append(f"A2L_LAYOUT_BAD: column id {cid!r} declared twice")
            else:
                declared.add(cid)
            x0, x1 = col.get("x0"), col.get("x1")
            if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in (x0, x1)):
                segments.append(f"A2L_LAYOUT_BAD: columns[{i}] x0/x1 must be numbers")
            elif not (0 <= x0 < x1 <= 1):
                segments.append(f"A2L_LAYOUT_BAD: columns[{i}] span {x0}..{x1} is not an "
                                f"increasing range inside 0-1")

    elements = data.get("elements")
    if not isinstance(elements, list):
        return False, "A2L_LAYOUT_BAD: missing `elements` list"
    if not elements:
        # A page with no elements at all is possible only for a genuinely blank page, and that
        # does not reach this step -- A2 would not have produced blocks for it.
        segments.append("A2L_LAYOUT_BAD: `elements` is empty -- every page has at least a "
                        "page number or one block")

    # `n` must refer to a block that exists. A wrong match renders the wrong text in that
    # position, which is worse than an honest null, so this is checked rather than trusted.
    known_ns = set()
    blocks = (context or {}).get("blocks") if isinstance(context, dict) else None
    # The runner (`resolve_single_run_items`) hands the agent's input as `input_data`, not as
    # `blocks` -- so under the runner this test silently never ran (found on BIO11L ch11-13,
    # 2026-10-25). Read the blocks from there too.
    if blocks is None and isinstance(context, dict) and isinstance(context.get("input_data"), dict):
        blocks = context["input_data"].get("blocks")
    if isinstance(blocks, list):
        known_ns = {b.get("n") for b in blocks if isinstance(b, dict)}

    seen_ns = {}
    for i, el in enumerate(elements):
        if not isinstance(el, dict):
            segments.append(f"A2L_LAYOUT_BAD: elements[{i}] is not an object")
            continue
        where = f"elements[{i}] (role={el.get('role')!r})"

        problem = _bbox_problem(el.get("bbox"))
        if problem:
            segments.append(f"A2L_LAYOUT_BAD: {where} bbox {problem}")

        col = el.get("column")
        if col not in _COLUMN_IDS:
            segments.append(f"A2L_LAYOUT_BAD: {where} column {col!r} not one of "
                            f"{sorted(_COLUMN_IDS)}")
        elif col != "full" and declared and col not in declared:
            # "full" means "spans every column" and is always legitimate -- a banner or rule bar
            # on a two-column page is `full`, exactly as the brief instructs. Only a named
            # side column has to have been declared.
            segments.append(f"A2L_COLUMN_UNDECLARED: {where} sits in column {col!r}, which is "
                            f"not among the page's declared columns {sorted(declared)}")

        sr = el.get("size_rel")
        if not isinstance(sr, (int, float)) or isinstance(sr, bool) or sr <= 0:
            segments.append(f"A2L_LAYOUT_BAD: {where} size_rel must be a positive number, "
                            f"got {sr!r}")
        elif not (_SIZE_REL_MIN <= sr <= _SIZE_REL_MAX):
            segments.append(
                f"A2L_SIZE_NOT_RATIO: {where} size_rel={sr} is outside {_SIZE_REL_MIN}-"
                f"{_SIZE_REL_MAX}; size_rel is a RATIO to page.body_text_size_px (body prose = "
                f"1.0), not a pixel height"
            )

        for field in ("fill", "text_color"):
            val = el.get(field)
            if val is None or val == "":
                continue
            if not (isinstance(val, str) and len(val) == 7 and val[0] == "#"
                    and all(c in "0123456789abcdefABCDEF" for c in val[1:])):
                segments.append(f"A2L_LAYOUT_BAD: {where} {field}={val!r} is not a #rrggbb hex")

        n = el.get("n")
        if n is None:
            continue
        if not isinstance(n, int) or isinstance(n, bool):
            segments.append(f"A2L_LAYOUT_BAD: {where} n={n!r} is not an integer or null")
            continue
        if known_ns and n not in known_ns:
            segments.append(f"A2L_BLOCK_UNKNOWN: {where} claims block n={n}, which is not a "
                            f"block on this page")
        if n in seen_ns:
            segments.append(f"A2L_BLOCK_DUPLICATE: block n={n} is claimed by two elements "
                            f"({seen_ns[n]} and {where}) -- one block is printed in one place")
        else:
            seen_ns[n] = where
        if el.get("role") in _FURNITURE_ROLES:
            segments.append(
                f"A2L_ROLE_CONFLICT: {where} is furniture (no quotable content) yet claims "
                f"block n={n}; furniture elements take n: null"
            )

    if not (data.get("note") or "").strip():
        segments.append("A2L_LAYOUT_BAD: `note` is required and must not be empty")

    if segments:
        return False, "; ".join(segments)
    return True, "ok"
