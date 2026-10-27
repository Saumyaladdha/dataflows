"""Check a physics figure spec (FIGP) against the booklet's VECTOR drawing, so it can be drawn on it.

WHY. A spec is the agent's reading of a figure in its own coordinates. Drawn by
lib/physics_figure.py it is a fair diagram but never the booklet's: 2017_A q016's isotherms came out
flatter, its process arrows as filled triangles where the print has open chevrons, its roman
numerals in the wrong face. Where the booklet's figure is a vector drawing (lib/print_trace.py),
the figure is drawn on the print's own geometry instead -- and the spec stays the checked DATA
(labels, netlist, angles) that says what the figure is.

That swap is only honest if the spec IS this figure, so this module checks it:

  1. LABELS. Every label the spec draws must be printed in the figure, and the labels that occur
     once on both sides fix the map from the spec's frame to the page (x and y each scaled and
     shifted; the spec is y-up, the page y-down).
  2. INK, BOTH WAYS. With that map, the spec's lines and curves must lie on the print's ink
     (precision) and the print's ink must be covered by the spec (recall), each within a tolerance
     of a few percent of the figure. A spec that misses a resistor, or draws one the print lacks,
     fails here.
"""
import collections
import re

import numpy as np
import pymupdf
from scipy.spatial import cKDTree

from lib import physics_figure, print_trace

#: Ink of each drawing is sampled on a raster of this many points per spec/page unit.
ZOOM = 2.0
#: Tolerance as a fraction of the figure's diagonal.
TOLERANCE = 0.03


def _norm(text):
    return re.sub(r"\s+", "", text or "").replace("−", "-").replace("–", "-")


def _bare(text):
    """Letters and digits only: "a = g" printed with its "=" drawn as two lines still reads "ag"."""
    return re.sub(r"[^0-9A-Za-zͰ-Ͽ]", "", text or "")


def printed_words(trace):
    """[(text, (x, y))] of every printed word AND every run of up to four words on one line
    ("300 K" is two words on the page, one label in a spec)."""
    words = []
    for word in print_trace._words(trace.glyphs):
        mains = [g for g in word if g.script is None] or word
        words.append(("".join(g.c for g in word), word, mains[0].origin[1], mains[0].size,
                      min(g.bbox[0] for g in word)))
    lines = []
    for w in sorted(words, key=lambda w: w[2]):
        for line in lines:
            if abs(w[2] - line[0][2]) < 0.3 * max(w[3], line[0][3]):
                line.append(w)
                break
        else:
            lines.append([w])
    out = []
    for line in lines:
        line.sort(key=lambda w: w[4])
        for i in range(len(line)):
            for j in range(i + 1, min(i + 4, len(line)) + 1):
                glyphs = [g for w in line[i:j] for g in w[1]]
                xs = [g.bbox[0] for g in glyphs] + [g.bbox[2] for g in glyphs]
                ys = [g.bbox[1] for g in glyphs] + [g.bbox[3] for g in glyphs]
                out.append(("".join(w[0] for w in line[i:j]),
                            ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)))
    return out


def font_styles(spec, trace):
    """{printed font: {"italic": bool, "serif": bool}} by majority of the spec labels set in it."""
    votes = collections.defaultdict(lambda: [0, 0, 0])      # italic, serif, total
    style_of = collections.defaultdict(list)
    for item in spec.get("draw") or []:
        if item.get("kind") == "label":
            text = _norm((item.get("text") or "") + (item.get("sub") or "") + (item.get("sup") or ""))
            style_of[text].append((bool(item.get("italic")), item.get("style") == "serif"))
    for word in print_trace._words(trace.glyphs):
        styles = style_of.get(_norm("".join(g.c for g in word)))
        if not styles:
            continue
        italic = sum(s[0] for s in styles) * 2 > len(styles)
        serif = sum(s[1] for s in styles) * 2 > len(styles)
        for g in word:
            if g.script is None:
                v = votes[g.font]
                v[0] += italic
                v[1] += serif
                v[2] += 1
    return {font: {"italic": v[0] * 2 > v[2], "serif": v[1] * 2 > v[2]} for font, v in votes.items()}


def spec_labels(spec):
    """[(text, (x, y))] of the spec's labels in its own (y-up) frame."""
    out = []
    for item in spec.get("draw") or []:
        if item.get("kind") != "label":
            continue
        at = item.get("at")
        if at is None and item.get("beside"):
            spot = item["beside"]
            at = physics_figure.beside(spot["from"], spot["to"], spot.get("offset", 40),
                                       spot.get("side", 1))
        if at is not None:
            out.append(((item.get("text") or "") + (item.get("sub") or "") + (item.get("sup") or ""),
                        tuple(at)))
    return out


def _pairs(spec, trace):
    """Label pairs (spec point, page point) for texts printed once and labelled once, and the
    spec labels nowhere in the print."""
    printed, bare = collections.defaultdict(list), collections.defaultdict(list)
    for text, at in printed_words(trace):
        printed[_norm(text)].append(at)
        if _bare(text):
            bare[_bare(text)].append(at)
    labelled = collections.defaultdict(list)
    for text, at in spec_labels(spec):
        labelled[_norm(text)].append(at)
    pairs, missing = [], []
    for text, spots in labelled.items():
        found = printed.get(text) or (bare.get(_bare(text)) if _bare(text) else None)
        if found:
            if len(spots) == 1 and len(found) == 1:
                pairs.append((spots[0], found[0]))
            continue
        # NOT MISSING, only not an anchor: a sign with no letters ("-", which 2018_AA q036 prints
        # as an unmapped glyph), a piece of a printed phrase the spec drew in parts ("Bcos30°" of
        # q026's "IlB cos 30°"), or any label at all where the figure's lettering is drawn as
        # outlines and the page has no text in it (q001's V, O, T, A, B).
        if not _bare(text) or not trace.glyphs:
            continue
        if any(text in p or (_bare(text) and _bare(text) in _bare(p)) for p in printed):
            continue
        # ...or its letters are all printed in and around the figure, in whatever order or
        # direction (a label set along a slope, or half outside the box)
        if not collections.Counter(_bare(text)) - collections.Counter(
                _bare(getattr(trace, "nearby_text", ""))):
            continue
        missing.append(text)
    return pairs, missing, printed, labelled


def fit(spec, trace, spec_ink=None, print_ink=None):
    """(ax, bx, ay, by) with page = (ax*x + bx, ay*y + by): from three or more labels printed once
    and labelled once; from two, as one scale with y flipped; else from the extent of the two
    drawings' ink (a figure with one label is still a figure)."""
    pairs, _missing, _printed, _labelled = _pairs(spec, trace)
    S = np.array([p[0] for p in pairs], float).reshape(-1, 2)
    P = np.array([p[1] for p in pairs], float).reshape(-1, 2)
    if len(pairs) >= 3 and np.ptp(S[:, 0]) > 1e-6 and np.ptp(S[:, 1]) > 1e-6:
        ax, bx = np.polyfit(S[:, 0], P[:, 0], 1)
        ay, by = np.polyfit(S[:, 1], P[:, 1], 1)
        return float(ax), float(bx), float(ay), float(by)
    if len(pairs) == 2 and np.hypot(*(S[0] - S[1])) > 1e-6:
        k = float(np.hypot(*(P[0] - P[1])) / np.hypot(*(S[0] - S[1])))
        return k, float(np.mean(P[:, 0] - k * S[:, 0])), -k, float(np.mean(P[:, 1] + k * S[:, 1]))
    if spec_ink is not None and print_ink is not None and len(spec_ink) and len(print_ink):
        (sx0, sy0), (sx1, sy1) = spec_ink.min(axis=0), spec_ink.max(axis=0)
        (px0, py0), (px1, py1) = print_ink.min(axis=0), print_ink.max(axis=0)
        if sx1 - sx0 > 1e-6 and sy1 - sy0 > 1e-6:
            ax = (px1 - px0) / (sx1 - sx0)
            ay = -(py1 - py0) / (sy1 - sy0)          # spec y-up, page y-down
            return float(ax), float(px0 - ax * sx0), float(ay), float(py0 - ay * sy1)
    return None


def _ink(svg_text, zoom):
    """Dark pixels of an SVG rasterised at `zoom`, as (u, v) in SVG user units."""
    doc = pymupdf.open(stream=svg_text.encode("utf-8"), filetype="svg")
    pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False, colorspace=pymupdf.csGRAY)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    v, u = np.nonzero(img < 128)
    return np.stack([u / zoom, v / zoom], axis=1)


def agreement(spec, trace):
    """{fit, missing_labels, precision, recall, tolerance} -- how far the spec IS the print."""
    pairs, missing, _p, _l = _pairs(spec, trace)
    out = {"missing_labels": missing, "anchors": len(pairs), "fit": None,
           "precision": None, "recall": None}
    pad, scale = spec.get("pad", 14), spec.get("scale", 1.0)
    geometry = dict(spec, draw=[d for d in spec.get("draw") or [] if d.get("kind") != "label"])
    spec_ink = _ink(physics_figure.render(geometry), ZOOM)
    x0, y0 = trace.rect[0] - 3.0, trace.rect[1] - 3.0
    print_ink = _ink(print_trace.svg(trace, keep_glyphs=set(), scale=1.0), ZOOM)
    if not len(spec_ink) or not len(print_ink):
        return out
    # SVG px -> spec units (y-up); print SVG units -> page points
    spec_units = np.stack([(spec_ink[:, 0] - pad) / scale,
                           spec["height"] - (spec_ink[:, 1] - pad) / scale], axis=1)
    print_on_page = print_ink + np.array([x0, y0])
    m = fit(spec, trace, spec_units, print_on_page)
    out["fit"] = m
    if m is None:
        return out
    ax, bx, ay, by = m
    spec_on_page = np.stack([ax * spec_units[:, 0] + bx, ay * spec_units[:, 1] + by], axis=1)
    diag = float(np.hypot(trace.rect[2] - trace.rect[0], trace.rect[3] - trace.rect[1]))
    tol = TOLERANCE * diag
    rng = np.random.default_rng(0)

    def sample(points, n=4000):
        return points if len(points) <= n else points[rng.choice(len(points), n, replace=False)]

    a, b = sample(spec_on_page), sample(print_on_page)
    out["precision"] = float(np.mean(cKDTree(print_on_page).query(a)[0] <= tol))
    out["recall"] = float(np.mean(cKDTree(spec_on_page).query(b)[0] <= tol))
    out["tolerance"] = tol
    return out


#: A spec passes when it is the printed figure to this degree, both ways. Low on purpose: a spec
#: is the agent's freehand reading (2017_A q017's circuit is drawn wider than printed, q036's
#: spring with other coils), so ink agreement only catches a spec of a DIFFERENT figure -- laid on
#: a neighbouring figure, specs score far below this on at least one side. The labels, which must
#: all be printed, are the sharp test.
MIN_PRECISION = 0.5
MIN_RECALL = 0.5


def problems(spec, trace):
    """Reasons this spec is not the printed figure ([] when it is)."""
    found = agreement(spec, trace)
    out = []
    if found["missing_labels"]:
        out.append("labels the print does not have: %s" % ", ".join(found["missing_labels"]))
    if found["fit"] is None:
        out.append("cannot lay the spec on the print")
        return out
    if found["precision"] is not None and found["precision"] < MIN_PRECISION:
        out.append("%.0f%% of what the spec draws is not on the printed figure (needs %.0f%%): a "
                   "line, curve or component is misplaced or not printed"
                   % (100 * found["precision"], 100 * MIN_PRECISION))
    if found["recall"] is not None and found["recall"] < MIN_RECALL:
        out.append("%.0f%% of the printed figure is drawn by the spec (needs %.0f%%): something "
                   "printed is missing or misplaced" % (100 * found["recall"], 100 * MIN_RECALL))
    return out
