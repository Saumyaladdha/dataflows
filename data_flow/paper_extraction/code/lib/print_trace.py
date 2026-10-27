"""Trace a printed chemistry figure from the booklet's VECTOR drawing, and check it against SMILES.

WHY. RDKit lays a molecule out its own way: 2017_A q089's aldehyde came out on the right with its
methyl labelled CH3, q052's options as different-looking ring pairs, q064's benzene rings without
their circles. A reader comparing the printed figure with ours saw a different picture and, more
than once, a different compound. The booklets are vector PDFs, so every bond line and every label
of a printed structure is on the page with exact coordinates. This module reads them and:

  1. builds the printed molecule as a GRAPH -- bond lines (single/double/triple from parallel
     lines), ring circles, atom labels read character by character (OCH3, NO2, H2N, the explicit
     H of H-C=O), and bonds typeset as text ("NH2 - NH - C - NH2");
  2. MATCHES each SMILES the agent wrote against those graphs, atom for atom: every printed bond to
     a SMILES bond of the same order (an aromatic bond may be printed single or double), every
     label to the atoms it stands for, hydrogen counts included. A SMILES that does not match the
     drawing fails, with the reason, and goes back to the agent;
  3. DRAWS the matched figure on the print's own geometry: the structures, and everything around
     them -- arrows, curved mechanism arrows, "<", charges, conditions -- where the booklet put them.

So "our drawing" looks like the booklet because it IS the booklet's geometry, and the SMILES in the
JSON is proven to be the printed molecule rather than asserted to be.

Text that belongs to the question rather than the figure (the stem's "is" running into q089's box)
is the page's body font and is left out; so is anything the figure box cuts through.
"""
import collections
import html
import math
import re

import networkx as nx
from networkx.algorithms import isomorphism
from rdkit import Chem

#: Elements a printed structure label is made of. Deliberately short: "X", "Y", "Z" and "A" are the
#: booklet's unknowns, never atoms, so they must not parse as labels.
ELEMENTS = {"H", "B", "C", "N", "O", "F", "Si", "P", "S", "Cl", "Br", "I", "Na", "K", "Li", "Mg",
            "Al", "Sn", "Se", "Ag", "Cu", "Zn", "Hg",
            # metals of the coordination and d-block figures (2018_AA q073's Ni(CO)4)
            "Fe", "Co", "Ni", "Cr", "Mn", "Pt", "Pd", "Au", "Pb", "Ti", "Ca", "Ba", "Sr", "Be",
            "Cd", "Ge", "As", "Sb", "Bi", "Xe"}
TOKEN = re.compile(r"([A-Z][a-z]?)(\d*)")
LABEL = re.compile(r"^(?:[A-Z][a-z]?\d*)+$")
DASHES = "–—−-"
#: "(1)", "(iv)", "(B)": the labels a figure of options or parts is laid out by
OPTION_LABEL = re.compile(r"^\((?:[1-9]|[ivxIVX]{1,4}|[a-dA-D])\)$")
CHARGES = "+–−-⊕⊖"
#: Symbol-font private-use characters as the booklets set them (U+F0xx = Symbol code xx).
SYMBOL = {"D": "Δ", "a": "α", "b": "β", "g": "γ", "d": "δ",
          "e": "ε", "f": "φ", "j": "ϕ", "w": "ω", "r": "ρ",
          "h": "η", "t": "τ", "n": "ν", "c": "χ", "y": "ψ",
          "x": "ξ", "z": "ζ", "k": "κ", "u": "υ", "Q": "Θ",
          "F": "Φ", "Y": "Ψ", "L": "Λ", "P": "Π", "S": "Σ",
          "G": "Γ",
          "l": "λ", "m": "μ", "p": "π", "q": "θ", "s": "σ",
          "W": "Ω", "®": "→", "°": "°", "´": "×",
          "±": "±", "-": "−", "+": "+", "=": "=", "¢": "′",
          "º": "≡", "¬": "←", "«": "↔", "­": "↑",
          "¯": "↓", "Å": "⊕", "Ä": "⊗", "\\": "∴"}


# ------------------------------------------------------------------------------------------------
# reading the page
# ------------------------------------------------------------------------------------------------

def _pt(p):
    return (float(p.x), float(p.y))


def _dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _bezier(p0, p1, p2, p3, n=10):
    out = []
    for i in range(1, n + 1):
        t = i / n
        u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


class Subpath:
    """One continuous piece of a drawing: its SVG commands and its points."""

    def __init__(self, drawing):
        self.drawing = drawing
        self.commands = []          # ("M"|"L"|"C"|"Z", points...)
        self.points = []
        self.has_curve = False

    @property
    def bbox(self):
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        return (min(xs), min(ys), max(xs), max(ys))


def _subpaths(drawing):
    out, cur, last = [], None, None
    for item in drawing["items"]:
        op = item[0]
        if op == "re":
            r = item[1]
            sp = Subpath(drawing)
            corners = [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
            sp.commands = [("M", corners[0])] + [("L", c) for c in corners[1:]] + [("Z",)]
            sp.points = corners
            out.append(sp)
            cur, last = None, None
            continue
        if op == "qu":
            q = item[1]
            sp = Subpath(drawing)
            corners = [_pt(q.ul), _pt(q.ur), _pt(q.lr), _pt(q.ll)]
            sp.commands = [("M", corners[0])] + [("L", c) for c in corners[1:]] + [("Z",)]
            sp.points = corners
            out.append(sp)
            cur, last = None, None
            continue
        start = _pt(item[1])
        if cur is None or last is None or _dist(start, last) > 0.05:
            cur = Subpath(drawing)
            cur.commands.append(("M", start))
            cur.points.append(start)
            out.append(cur)
        if op == "l":
            end = _pt(item[2])
            cur.commands.append(("L", end))
            cur.points.append(end)
        elif op == "c":
            c1, c2, end = _pt(item[2]), _pt(item[3]), _pt(item[4])
            cur.commands.append(("C", c1, c2, end))
            cur.points.extend(_bezier(start, c1, c2, end))
            cur.has_curve = True
        last = cur.points[-1]
    if drawing.get("closePath") and out:
        out[-1].commands.append(("Z",))
    return out


def _inside(box, rect, slack=1.5):
    return (box[0] >= rect[0] - slack and box[1] >= rect[1] - slack and
            box[2] <= rect[2] + slack and box[3] <= rect[3] + slack)


def _is_white(color):
    return color is not None and all(c > 0.9 for c in color)


class Glyph:
    __slots__ = ("c", "bbox", "origin", "size", "font", "color", "bold", "script", "host")

    def __init__(self, c, bbox, origin, size, font, color, bold):
        self.c, self.bbox, self.origin, self.size = c, bbox, origin, size
        self.font, self.color, self.bold = font, color, bold
        self.script = None          # "sub" | "sup" for a small character set beside a big one
        self.host = None


def _glyphs(page, rect):
    out = []
    raw = page.get_text("rawdict", clip=None)
    for block in raw.get("blocks", []):
        for line in block.get("lines", []):
            # A WORD THAT RUNS OUT OF THE BOX is the page's text, not a figure label: the tail of
            # "Answer", the "ol" of "Sol." (2017_A q017, q008). Its other words stay -- q089's
            # drawn "H" shares a line with the clipped step number "1.".
            def inside(ch):
                return (rect[0] - 0.5 <= ch["bbox"][0] and ch["bbox"][2] <= rect[2] + 0.5
                        and rect[1] - 0.5 <= ch["bbox"][1] and ch["bbox"][3] <= rect[3] + 0.5)
            cut = set()
            word = []
            font_of = {id(ch): span.get("font") for span in line.get("spans", [])
                       for ch in span.get("chars", [])}
            for ch in [ch for span in line.get("spans", []) for ch in span.get("chars", [])] + [None]:
                if ch is None or ch["c"].isspace():
                    flags = [inside(c) for c in word]
                    if any(flags) and not all(flags):
                        cut |= {id(c) for c in word}
                    word = []
                else:
                    word.append(ch)
            # ...and the rest of that sentence, in the clipped word's font: the "(2)" of "Answer (2)"
            cut_fonts = {font_of[i] for i in cut}
            cut |= {i for i, f in font_of.items() if f in cut_fonts}
            for span in line.get("spans", []):
                font = span.get("font", "")
                for ch in span.get("chars", []):
                    if id(ch) in cut:
                        continue
                    c = ch["c"]
                    box = tuple(ch["bbox"])
                    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
                    if not (rect[0] <= cx <= rect[2] and rect[1] <= cy <= rect[3]):
                        continue
                    if "Symbol" in font and len(c) == 1 and 0xF000 <= ord(c) <= 0xF0FF:
                        c = SYMBOL.get(chr(ord(c) - 0xF000), chr(ord(c) - 0xF000))
                    color = span.get("color", 0)
                    out.append(Glyph(c, box, tuple(ch["origin"]), span["size"], font,
                                     "#%06x" % color, bool(span.get("flags", 0) & 16)
                                     or "Bold" in font))
    return out


def _body_font(page):
    """The (font, size) most of the page's characters are set in: the question text, not a figure."""
    tally = collections.Counter()
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                tally[(span["font"], round(span["size"], 1))] += len(span["text"].strip())
    return tally.most_common(1)[0][0] if tally else None


# ------------------------------------------------------------------------------------------------
# the figure's geometry
# ------------------------------------------------------------------------------------------------

class Segment:
    __slots__ = ("a", "b", "width", "subpaths", "order", "parallels", "contour")

    def __init__(self, a, b, width, subpaths, contour=None):
        self.a, self.b, self.width, self.subpaths = a, b, width, set(subpaths)
        self.order = 1
        self.parallels = []
        self.contour = contour      # id of the filled drawing whose outline this edge was read from

    @property
    def length(self):
        return _dist(self.a, self.b)

    def direction(self):
        L = self.length or 1.0
        return ((self.b[0] - self.a[0]) / L, (self.b[1] - self.a[1]) / L)


def _fit_circle(points):
    if len(points) < 12:
        return None
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    radii = [_dist(p, (cx, cy)) for p in points]
    r = sum(radii) / len(radii)
    if r < 1.5:
        return None
    spread = (sum((x - r) ** 2 for x in radii) / len(radii)) ** 0.5
    # a closed loop all the way round, not an arc
    angles = sorted(math.atan2(p[1] - cy, p[0] - cx) for p in points)
    gaps = [b - a for a, b in zip(angles, angles[1:])] + [angles[0] + 2 * math.pi - angles[-1]]
    if spread / r < 0.08 and max(gaps) < 1.2:
        return (cx, cy, r)
    return None


def _cluster(points, tol):
    """Greedy seed clustering: a point joins the first cluster whose SEED is within tol. No
    chaining, so a polygonised circle does not collapse into one point."""
    seeds, members = [], []
    labels = []
    for p in points:
        for k, s in enumerate(seeds):
            if _dist(p, s) <= tol:
                members[k].append(p)
                labels.append(k)
                break
        else:
            seeds.append(p)
            members.append([p])
            labels.append(len(seeds) - 1)
    centres = [(sum(q[0] for q in m) / len(m), sum(q[1] for q in m) / len(m)) for m in members]
    return labels, centres


def _stroke_width(subpaths):
    widths = []
    for sp in subpaths:
        if sp.drawing.get("type") == "s" or sp.has_curve:
            continue
        pts = sp.points
        if 4 <= len(pts) <= 6:
            edges = sorted(_dist(a, b) for a, b in zip(pts, pts[1:] + pts[:1]) if _dist(a, b) > 0.1)
            # a line's outline is long and narrow; a lone-pair dot is a tiny square and says
            # nothing about the pen (2017_A q065's dots made every bond read as two lines)
            if edges and edges[-1] > 3 * edges[0]:
                widths.append(edges[0])
    for sp in subpaths:
        # a hairline drawn round a filled shape is not the pen the bonds are drawn with
        if sp.drawing.get("type") == "s" and (sp.drawing.get("width") or 0) >= 0.4:
            widths.append(sp.drawing["width"])
    if not widths:
        return 0.9
    widths.sort()
    return widths[len(widths) // 2]


def _thin_line(points, w):
    """(a, b) when the points lie along one thin straight band -- a single bond's outline, however
    the PDF built it (a quad, or a stroke with rounded curve caps) -- else None."""
    if len(points) < 2:
        return None
    mx = sum(p[0] for p in points) / len(points)
    my = sum(p[1] for p in points) / len(points)
    sxx = sum((p[0] - mx) ** 2 for p in points)
    syy = sum((p[1] - my) ** 2 for p in points)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in points)
    angle = 0.5 * math.atan2(2 * sxy, sxx - syy)
    dx, dy = math.cos(angle), math.sin(angle)
    along = [(p[0] - mx) * dx + (p[1] - my) * dy for p in points]
    across = [-(p[0] - mx) * dy + (p[1] - my) * dx for p in points]
    length = max(along) - min(along)
    if length < 3 * w or max(across) - min(across) > 2.6 * w:
        return None
    cap = min(w / 2, length / 4)              # the outline runs half a stroke past each end
    lo, hi = min(along) + cap, max(along) - cap
    return ((mx + lo * dx, my + lo * dy), (mx + hi * dx, my + hi * dy))


def _simplify(points, eps):
    """Ramer-Douglas-Peucker: the polyline's corners, without the points along its straight runs."""
    if len(points) < 3:
        return list(points)
    a, b = points[0], points[-1]
    L = _dist(a, b)
    best, k = -1.0, 0
    for i in range(1, len(points) - 1):
        p = points[i]
        if L < 1e-9:
            d = _dist(p, a)
        else:
            d = abs((b[0] - a[0]) * (a[1] - p[1]) - (a[0] - p[0]) * (b[1] - a[1])) / L
        if d > best:
            best, k = d, i
    if best <= eps:
        return [a, b]
    return _simplify(points[:k + 1], eps)[:-1] + _simplify(points[k:], eps)


def _fat(points):
    """True for a shape about as wide as it is long (an arrowhead), not a thin bond outline."""
    mx = sum(p[0] for p in points) / len(points)
    my = sum(p[1] for p in points) / len(points)
    sxx = sum((p[0] - mx) ** 2 for p in points)
    syy = sum((p[1] - my) ** 2 for p in points)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in points)
    angle = 0.5 * math.atan2(2 * sxy, sxx - syy)
    dx, dy = math.cos(angle), math.sin(angle)
    along = [(p[0] - mx) * dx + (p[1] - my) * dy for p in points]
    across = [-(p[0] - mx) * dy + (p[1] - my) * dx for p in points]
    return (max(across) - min(across)) > 0.3 * (max(along) - min(along))


def _raw_segments(subpaths, w):
    """Centre lines of every straight stroke, whether the PDF stroked it or filled its outline."""
    segs, circles, detail = [], [], []
    heads, curve_ends = [], []
    for sp in subpaths:
        circle = _fit_circle(sp.points)
        if circle:
            circles.append((circle, sp))
            continue
        # A closed stroked shape is an OUTLINE (2017_A q065 strokes a hairline round every filled
        # bond): read like a filled one, or each bond comes out as two lines.
        closed = len(sp.points) >= 4 and _dist(sp.points[0], sp.points[-1]) < 0.5
        outline = sp.drawing.get("type") != "s" or closed
        if outline:
            line = _thin_line(sp.points, w)
            if line:
                segs.append(Segment(line[0], line[1], w, [id(sp)]))
                continue
            corners = _simplify(sp.points + sp.points[:1], 0.5 * w)[:-1]
            box = sp.bbox
            if 3 <= len(corners) <= 5 and _fat(corners):
                detail.append(sp)          # a filled triangle: an arrowhead, not a bond...
                if max(box[2] - box[0], box[3] - box[1]) < 3 * w:
                    continue               # ...or a dot of a dotted bond, far too small for one
                heads.append((sp.bbox, (sum(p[0] for p in corners) / len(corners),
                                        sum(p[1] for p in corners) / len(corners))))
                continue
        if not outline:
            if sp.has_curve:
                detail.append(sp)
                curve_ends += [sp.points[0], sp.points[-1]]
                continue
            # a stroked line is often many tiny collinear pieces (2017_A q080's NH2 bond is four):
            # simplified first, so each straight run is one segment
            pts = _simplify(sp.points, 0.6 * w)
            pieces = list(zip(pts, pts[1:]))
            # ...but a curved mechanism arrow drawn as straight pieces stays many short ones
            if len(pieces) >= 3 and all(_dist(a, b) < 6 * w for a, b in pieces):
                detail.append(sp)
                curve_ends += [sp.points[0], sp.points[-1]]
                continue
            for a, b in pieces:
                segs.append(Segment(a, b, sp.drawing.get("width") or w, [id(sp)]))
            continue
        if sp.has_curve:
            detail.append(sp)
            continue
        labels, centres = _cluster(sp.points, 2.3 * w)
        seen = set()
        n = len(labels)
        for i in range(n):
            j = (i + 1) % n
            a, b = labels[i], labels[j]
            if a == b:
                continue
            key = (min(a, b), max(a, b))
            if key in seen:
                continue
            seen.add(key)
            segs.append(Segment(centres[a], centres[b], w, [id(sp)], contour=id(sp.drawing)))
    return segs, circles, detail, heads, curve_ends


def _offset(s, t):
    """Perpendicular distance of t's midpoint from s's line, and the overlap of t on s."""
    dx, dy = s.direction()
    mx, my = (t.a[0] + t.b[0]) / 2 - s.a[0], (t.a[1] + t.b[1]) / 2 - s.a[1]
    off = abs(-dy * mx + dx * my)
    ta = (t.a[0] - s.a[0]) * dx + (t.a[1] - s.a[1]) * dy
    tb = (t.b[0] - s.a[0]) * dx + (t.b[1] - s.a[1]) * dy
    lo, hi = max(0.0, min(ta, tb)), min(s.length, max(ta, tb))
    return off, max(0.0, hi - lo)


def _parallel(s, t, tol_deg=8.0):
    ds, dt = s.direction(), t.direction()
    return abs(ds[0] * dt[1] - ds[1] * dt[0]) < math.sin(math.radians(tol_deg))


def _merge_duplicates(segs, w):
    """An outlined ring is two contours, outer and inner, a stroke-width apart: one bond each.
    Only edges read from the SAME filled outline are merged: two separate lines that close are a
    double bond drawn tight (2017_A q052's C=O), not one stroke's two edges."""
    out = []
    for s in sorted(segs, key=lambda x: -x.length):
        for t in out:
            if s.contour is not None and s.contour == t.contour and _parallel(s, t):
                off, overlap = _offset(t, s)
                if off < 1.7 * w and overlap > 0.7 * min(s.length, t.length):
                    t.subpaths |= s.subpaths
                    break
        else:
            out.append(s)
    return out


def _join_collinear(segs, w):
    """A bond whose outline has a point halfway along comes out as two straight halves meeting
    where nothing else ends: one bond. (2017_A q080's rings read as twelve-membered without this.)"""
    tol = 1.6 * w
    changed = True
    while changed:
        changed = False
        for i, s in enumerate(segs):
            for j in range(i + 1, len(segs)):
                t = segs[j]
                if not _parallel(s, t, 4.0):
                    continue
                for sp_, sq in ((s.a, s.b), (s.b, s.a)):
                    for tp, tq in ((t.a, t.b), (t.b, t.a)):
                        if _dist(sp_, tp) > tol or _dist(sq, tq) < max(s.length, t.length):
                            continue
                        joint = sp_
                        others = [o for o in segs if o is not s and o is not t
                                  and min(_dist(o.a, joint), _dist(o.b, joint)) <= 2.5 * w]
                        if others:
                            continue
                        merged = Segment(sq, tq, max(s.width, t.width), s.subpaths | t.subpaths)
                        segs = [o for o in segs if o is not s and o is not t] + [merged]
                        changed = True
                        break
                    if changed:
                        break
                if changed:
                    break
            if changed:
                break
    return segs


class Trace:
    """Everything read from one figure box."""

    def __init__(self):
        self.rect = None
        self.subpaths = []
        self.glyphs = []
        self.body_font = None
        self.L = 14.0
        self.w = 1.0
        self.graph = nx.Graph()
        self.components = []
        self.circles = []
        self.labels = []


def _bond_length(segs, w):
    lengths = sorted(s.length for s in segs if s.length > 5 * w)
    return lengths[len(lengths) // 2] if lengths else 14.0


def _group_parallels(segs, L, w):
    """Double and triple bonds: lines parallel to a bond, close beside it, overlapping it."""
    parent = list(range(len(segs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, s in enumerate(segs):
        for j in range(i + 1, len(segs)):
            t = segs[j]
            if not _parallel(s, t):
                continue
            long_, short = (s, t) if s.length >= t.length else (t, s)
            off, overlap = _offset(long_, short)
            if 1.7 * w <= off <= 0.42 * L and overlap >= 0.5 * short.length:
                parent[find(i)] = find(j)
    groups = collections.defaultdict(list)
    for i in range(len(segs)):
        groups[find(i)].append(segs[i])
    return list(groups.values())


def _endpoint_degree(seg, others, tol):
    return sum(1 for o in others for e in (o.a, o.b) for p in (seg.a, seg.b) if _dist(e, p) <= tol)


def _bases(segs, L, w):
    groups = _group_parallels(segs, L, w)
    bases = []
    for group in groups:
        if len(group) == 1:
            bases.append(group[0])
            continue
        others = [s for s in segs if s not in group]
        scored = sorted(group, key=lambda s: (-_endpoint_degree(s, others, 0.25 * L), -s.length))
        top = scored[0]
        second = scored[1]
        same = (_endpoint_degree(top, others, 0.25 * L) == _endpoint_degree(second, others, 0.25 * L)
                and abs(top.length - second.length) < 0.15 * top.length)
        if same and len(group) == 2:
            # a centred double bond (C=O drawn as two equal lines): the bond is their midline
            a, b = top.a, top.b
            c, d = (second.a, second.b) if _dist(top.a, second.a) < _dist(top.a, second.b) \
                else (second.b, second.a)
            base = Segment(((a[0] + c[0]) / 2, (a[1] + c[1]) / 2),
                           ((b[0] + d[0]) / 2, (b[1] + d[1]) / 2), w, top.subpaths | second.subpaths)
        else:
            base = Segment(top.a, top.b, w, set(top.subpaths))
            for s in group:
                if s is not top:
                    base.subpaths |= s.subpaths
        base.order = min(3, len(group))
        base.parallels = [s for s in group if s is not top]
        bases.append(base)
    return bases


# ------------------------------------------------------------------------------------------------
# labels
# ------------------------------------------------------------------------------------------------

class Label:
    def __init__(self, text, glyphs):
        self.text = text                  # main characters + scripts, e.g. "NH2", "OCH3"
        self.glyphs = glyphs              # every glyph, scripts included
        xs0 = [g.bbox[0] for g in glyphs]
        ys0 = [g.bbox[1] for g in glyphs]
        xs1 = [g.bbox[2] for g in glyphs]
        ys1 = [g.bbox[3] for g in glyphs]
        self.bbox = (min(xs0), min(ys0), max(xs1), max(ys1))
        self.tokens = []                  # (element, count, x0, x1)
        self.charge = ""
        self.wild = False                 # a letter for a group, matched to a SMILES [*]
        self.hidden = collections.Counter()   # atoms inside brackets: the (CH3)2 of CH(CH3)2

    @property
    def heavy(self):
        out = collections.Counter()
        for el, n, _x0, _x1 in self.tokens:
            if el != "H":
                out[el] += n
        for el, n in self.hidden.items():
            if el != "H":
                out[el] += n
        return out

    @property
    def hydrogens(self):
        return sum(n for el, n, _x0, _x1 in self.tokens if el == "H") + self.hidden.get("H", 0)

    def anchor(self, x):
        """The element a bond arriving at horizontal position x attaches to."""
        heavy = [t for t in self.tokens if t[0] != "H"]
        if not heavy:
            return None
        inside = [t for t in self.tokens if t[2] - 0.5 <= x <= t[3] + 0.5]
        pick = inside[0] if inside else min(self.tokens, key=lambda t: min(abs(x - t[2]), abs(x - t[3])))
        if pick[0] == "H":
            pick = min(heavy, key=lambda t: min(abs(pick[2] - t[3]), abs(pick[3] - t[2])))
        return pick[0]


def _bracketed(text):
    """([(element, count)] outside brackets, Counter of atoms inside) for "CH(CH3)2", or None."""
    top, hidden, stack = [], collections.Counter(), []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "(":
            stack.append(collections.Counter())
            i += 1
        elif ch == ")":
            if not stack:
                return None
            group = stack.pop()
            m = re.match(r"\d*", text[i + 1:])
            mult = int(m.group(0)) if m.group(0) else 1
            i += 1 + len(m.group(0))
            target = stack[-1] if stack else hidden
            for el, n in group.items():
                target[el] += n * mult
        else:
            m = re.match(r"([A-Z][a-z]?)(\d*)", text[i:])
            if not m:
                return None
            el, n = m.group(1), int(m.group(2)) if m.group(2) else 1
            if stack:
                stack[-1][el] += n
            else:
                top.append((el, n))
            i += len(m.group(0))
    return None if stack else (top, hidden)


def _attach_scripts(glyphs):
    """Small characters set beside a bigger one are its subscript or superscript."""
    for g in glyphs:
        # ...within about half a letter of the host's baseline: smaller text on the line ABOVE
        # is not a superscript (q012's "30 V" read as scripts of "(a)" without this)
        hosts = [h for h in glyphs if h is not g and h.size * 0.8 > g.size
                 and -1.5 <= g.bbox[0] - h.bbox[2] <= 2.5
                 and g.bbox[1] < h.bbox[3] and g.bbox[3] > h.bbox[1]
                 and abs(g.origin[1] - h.origin[1]) < 0.6 * h.size]
        if hosts:
            host = min(hosts, key=lambda h: abs(g.bbox[0] - h.bbox[2]))
            g.host = host
            mid_g = (g.bbox[1] + g.bbox[3]) / 2
            mid_h = (host.bbox[1] + host.bbox[3]) / 2
            g.script = "sub" if mid_g > mid_h else "sup"


def _words(glyphs):
    """Main-size glyphs grouped into words on their baseline, each with its scripts."""
    mains = [g for g in glyphs if g.script is None]
    scripts = collections.defaultdict(list)
    for g in glyphs:
        if g.script:
            h = g.host
            while h is not None and h.script:
                h = h.host
            if h is not None:
                scripts[id(h)].append(g)
    # lines first (a baseline shared within a third of the type size), then left to right in each
    lines = []
    for g in sorted(mains, key=lambda g: g.origin[1]):
        for line in lines:
            # ...and in one size: 2017_A q012 sets "(a)" a hair below "30 V", and read as one
            # line the two interleaved into "(3a) V"
            if abs(g.origin[1] - line[0].origin[1]) < 0.3 * max(g.size, line[0].size) \
                    and abs(g.size - line[0].size) < 0.6:
                line.append(g)
                break
        else:
            lines.append([g])
    # Words by the GAP on the page, not by space characters: 2017_A q083 sets "CH3I" with a space
    # inside it, where the subscript sits. A word space is about a quarter of the type size.
    words = []
    for line in lines:
        cur = []
        for g in sorted((g for g in line if not g.c.isspace()), key=lambda g: g.bbox[0]):
            if cur:
                p = cur[-1]
                right = max([p.bbox[2]] + [s.bbox[2] for s in scripts[id(p)]])
                if g.bbox[0] - right > 0.2 * p.size:
                    words.append(cur)
                    cur = []
            cur.append(g)
        if cur:
            words.append(cur)
    out = []
    for word in words:
        seq = []
        for g in word:
            seq.append(g)
            seq.extend(sorted(scripts[id(g)], key=lambda s: s.bbox[0]))
        out.append(seq)
    return out


def _labels_and_dash_bonds(glyphs):
    """Chemical labels, and the bonds a typeset formula writes as dashes ("NH - NH - C - NH2")."""
    labels, dash_bonds = [], []
    for word in _words(glyphs):
        # split on dashes inside a word: "H-NH2"
        parts, cur = [], []
        for g in word:
            if g.c in DASHES and g.script is None:
                if cur:
                    parts.append(cur)
                parts.append([g])
                cur = []
            else:
                cur.append(g)
        if cur:
            parts.append(cur)
        labels.extend(parts)
    built = []
    for part in labels:
        text = "".join(g.c for g in part if g.script != "sup")
        charge = "".join(g.c for g in part if g.script == "sup")
        lab = Label(text, part)
        lab.charge = charge
        if text in DASHES or text.strip() in DASHES:
            lab.tokens = None             # a dash
        elif LABEL.match(text) and all(t[0] in ELEMENTS for t in TOKEN.findall(text)):
            # token x-ranges from the glyphs that spell each token
            mains = [g for g in part if g.script is None]
            k = 0
            for el, digits in TOKEN.findall(text):
                if k + len(el) > len(mains):
                    # a LETTER set as a subscript (a physics label such as V_A): not a formula
                    lab.tokens = []
                    break
                gl = []
                for _ in el:
                    gl.append(mains[k])
                    k += 1
                x0, x1 = gl[0].bbox[0], gl[-1].bbox[2]
                lab.tokens.append((el, int(digits) if digits else 1, x0, x1))
                # subscripts belong to scripts, not mains, so k does not advance over digits
        elif "(" in text and re.fullmatch(r"(?:[A-Z][a-z]?\d*|\(|\)\d*)+", text)                 and _bracketed(text) is not None:
            # A CONDENSED GROUP WITH BRACKETS: CH(CH3)2, C(CH3)3. The atoms outside the brackets
            # are where a bond can arrive (tokens, with their x-range); those inside only count.
            top, hidden = _bracketed(text)
            mains = [g for g in part if g.script is None]
            letters = [(i, g) for i, g in enumerate(mains)]
            depth, k, ok = 0, 0, True
            main_text = "".join(g.c for g in mains)
            i = 0
            while i < len(main_text):
                ch = main_text[i]
                if ch == "(":
                    depth += 1
                    i += 1
                    continue
                if ch == ")":
                    depth -= 1
                    i += 1
                    continue
                m = re.match(r"[A-Z][a-z]?", main_text[i:])
                if not m:
                    i += 1
                    continue
                if depth == 0 and k < len(top):
                    el, n = top[k]
                    lab.tokens.append((el, n, mains[i].bbox[0], mains[i + len(m.group(0)) - 1].bbox[2]))
                    k += 1
                i += len(m.group(0))
            lab.hidden = hidden
            if not all(el in ELEMENTS for el, _n in top) or not all(el in ELEMENTS for el in hidden):
                lab.tokens = []
        elif re.fullmatch(r"[A-Z]", text) and text not in ELEMENTS:
            # A LETTER STANDING FOR A GROUP ("Y" on 2018_AA q064's arenium ions): the wildcard
            # [*] of a SMILES. Only ever an atom when a bond reaches it (see `molecular` below).
            g = [g for g in part if g.script is None][0]
            lab.tokens = [("*", 1, g.bbox[0], g.bbox[2])]
            lab.wild = True
        else:
            lab.tokens = []
        built.append(lab)
    # dash bonds: label, dash, label on one line, close together
    chem = [b for b in built if b.tokens]
    dashes = [b for b in built if b.tokens is None]
    for d in dashes:
        dy = (d.bbox[1] + d.bbox[3]) / 2
        size = d.glyphs[0].size
        left = [c for c in chem if abs((c.bbox[1] + c.bbox[3]) / 2 - dy) < 0.6 * size
                and -1.0 <= d.bbox[0] - c.bbox[2] < 1.2 * size]
        right = [c for c in chem if abs((c.bbox[1] + c.bbox[3]) / 2 - dy) < 0.6 * size
                 and -1.0 <= c.bbox[0] - d.bbox[2] < 1.2 * size]
        if left and right:
            dash_bonds.append((max(left, key=lambda c: c.bbox[2]), min(right, key=lambda c: c.bbox[0]),
                               1 if d.text in DASHES else 2))
    return chem, dash_bonds, built


# ------------------------------------------------------------------------------------------------
# the trace
# ------------------------------------------------------------------------------------------------

def read(page, rect_pt, keep_words=()):
    """A Trace of the figure inside rect_pt = (x0, y0, x1, y1) on this page (PDF points).

    `keep_words`: words to keep even when they are set in the question's body font -- a physics
    spec's labels, which a booklet may letter in its text face."""
    tr = Trace()
    tr.rect = tuple(rect_pt)
    for drawing in page.get_drawings():
        if drawing.get("type") == "f" and _is_white(drawing.get("fill")):
            continue
        for sp in _subpaths(drawing):
            if not sp.points:
                continue
            box = sp.bbox
            if not _inside(box, tr.rect):
                continue
            if (box[2] - box[0]) > 0.95 * (tr.rect[2] - tr.rect[0]):
                continue                  # a frame round the figure, not part of it
            tr.subpaths.append(sp)
    # a zero-length stroke is a point the pen's round cap turns into a dot: nothing printed
    tr.subpaths = [sp for sp in tr.subpaths
                   if max(sp.bbox[2] - sp.bbox[0], sp.bbox[3] - sp.bbox[1]) > 0.05]
    tr.body_font = _body_font(page)
    # Every character printed in and just around the box, unfiltered: what a label check can
    # fall back on when a label is set on a slope or runs past the box edge (2018_AA q026, q035).
    near = (tr.rect[0] - 12, tr.rect[1] - 12, tr.rect[2] + 12, tr.rect[3] + 12)
    tr.nearby_text = "".join(g.c for g in _glyphs(page, near))
    glyphs = [g for g in _glyphs(page, tr.rect) if _inside(g.bbox, tr.rect, slack=0.5)]
    # The question's own words (its body font) are not the figure -- except the option and part
    # labels a figure is laid out by: 2017_A q052 sets "(1)".."(4)" beside its structures in it.
    keep = set()
    body = [g for g in glyphs if (g.font, round(g.size, 1)) == tr.body_font]
    for word in _words(body):
        if OPTION_LABEL.match("".join(g.c for g in word)) or                 "".join(g.c for g in word) in set(keep_words):
            keep |= {id(g) for g in word}
    tr.glyphs = [g for g in glyphs if (g.font, round(g.size, 1)) != tr.body_font or id(g) in keep]
    # A SUBSCRIPT JUST OUTSIDE A TIGHT BOX belongs to its letter inside it: 2018_AA q068's option
    # box ends between "CH" and its "3", and the label read CH -- one H where the print has three.
    edge = (tr.rect[0] - 4, tr.rect[1] - 4, tr.rect[2] + 4, tr.rect[3] + 4)
    outside = [g for g in _glyphs(page, edge) if not _inside(g.bbox, tr.rect, slack=0.5)]
    _attach_scripts(tr.glyphs + outside)
    inside_ids = {id(g) for g in tr.glyphs}
    tr.glyphs += [g for g in outside if g.script and g.host is not None and id(g.host) in inside_ids]
    _attach_scripts(tr.glyphs)
    # A full stop or comma standing alone belongs to the sentence the box clipped ("1." of the
    # solution's numbering, the stem's last stop), not to the figure.
    def alone(g):
        # a full stop ends something printed just before it on its line; one with nothing there
        # is the tail of a sentence or a numbering ("1.") the box cut through
        if g.c in ".,":
            left = [h for h in tr.glyphs if h is not g and not h.c.isspace()
                    and abs(h.origin[1] - g.origin[1]) < 0.3 * g.size
                    and -0.5 <= g.bbox[0] - h.bbox[2] <= 0.4 * g.size]
            if not left:
                return True
        reach = 1.2 * g.size
        cx, cy = (g.bbox[0] + g.bbox[2]) / 2, (g.bbox[1] + g.bbox[3]) / 2
        for h in tr.glyphs:
            if h is not g and h.c not in ".,:;" and not h.c.isspace():
                if abs((h.bbox[0] + h.bbox[2]) / 2 - cx) < reach and abs((h.bbox[1] + h.bbox[3]) / 2 - cy) < reach:
                    return False
        for sp in tr.subpaths:
            b = sp.bbox
            if b[0] - reach < cx < b[2] + reach and b[1] - reach < cy < b[3] + reach:
                return False
        return True
    tr.glyphs = [g for g in tr.glyphs if not (g.c in ".,:;" and alone(g))]
    # ...and a speck of ink standing alone is the same full stop drawn as a path
    def speck(sp):
        b = sp.bbox
        if max(b[2] - b[0], b[3] - b[1]) > 2.5:
            return False
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        reach = 8.0
        for o in tr.subpaths:
            if o is not sp:
                ob = o.bbox
                if ob[0] - reach < cx < ob[2] + reach and ob[1] - reach < cy < ob[3] + reach:
                    return False
        for g in tr.glyphs:
            if g.bbox[0] - reach < cx < g.bbox[2] + reach and g.bbox[1] - reach < cy < g.bbox[3] + reach:
                return False
        return True
    tr.subpaths = [sp for sp in tr.subpaths if not speck(sp)]

    tr.w = _stroke_width(tr.subpaths)
    raw, circles, _detail, heads, curve_ends = _raw_segments(tr.subpaths, tr.w)
    raw = _merge_duplicates(raw, tr.w)
    raw = _join_collinear(raw, tr.w)
    tr.L = _bond_length(raw, tr.w)
    # A figure with few drawn bonds (q061's scheme: one "||" under a typeset formula) has no
    # bond-length median worth the name; a bond is never much shorter than its labels are tall.
    sizes = sorted(g.size for g in tr.glyphs if g.script is None and not g.c.isspace())
    if sizes:
        # ...nor much longer: where arrows outnumber bonds the median is an arrow
        size = sizes[len(sizes) // 2]
        tr.L = min(max(tr.L, 1.2 * size), 2.2 * size)
    # An ARROW, not a bond: a straight line longer than any bond, and everything drawn in the
    # same outline with it (its head). Arrows are drawn back at their printed place, never bonded.
    arrow_paths = set()
    def into_head(seg):
        """The line runs INTO an arrowhead: one end inside the head, pointing at its middle."""
        for (b, centre) in heads:
            for near, far in ((seg.a, seg.b), (seg.b, seg.a)):
                if not (b[0] - tr.w <= near[0] <= b[2] + tr.w and b[1] - tr.w <= near[1] <= b[3] + tr.w):
                    continue
                dx, dy = near[0] - far[0], near[1] - far[1]
                hx, hy = centre[0] - far[0], centre[1] - far[1]
                n1, n2 = math.hypot(dx, dy), math.hypot(hx, hy)
                if n1 and n2 and (dx * hx + dy * hy) / (n1 * n2) > 0.95:
                    return True
        return False

    for s in raw:
        if s.length > 1.6 * tr.L:
            arrow_paths |= s.subpaths
    # ...or a line that runs into an arrowhead, however short (q080's second arrow is a bond
    # long); or the straight lead-in of a curved arrow, which runs on into the curve
    raw = [s for s in raw if not (s.subpaths & arrow_paths) and not into_head(s)
           and not any(min(_dist(s.a, e), _dist(s.b, e)) <= 2 * tr.w for e in curve_ends)]
    # a bond into a label is short (it stops at the letters), so the floor is low
    bonds = [s for s in raw if s.length >= 0.22 * tr.L]
    tr.circles = circles
    bases = _bases(bonds, tr.L, tr.w)

    chem, dash_bonds, _all = _labels_and_dash_bonds(tr.glyphs)
    tr.labels = chem

    # nodes: bond ends, merged when close, swallowed by a label they touch
    ends = []
    for k, s in enumerate(bases):
        ends.append((s.a, k, 0))
        ends.append((s.b, k, 1))
    labels_of, centres = _cluster([e[0] for e in ends], 0.22 * tr.L)
    node_of_end = {}
    G = tr.graph
    label_node = {}
    for i, lab in enumerate(chem):
        label_node[id(lab)] = ("L", i)
        G.add_node(("L", i), kind="label", label=lab, pos=((lab.bbox[0] + lab.bbox[2]) / 2,
                                                            (lab.bbox[1] + lab.bbox[3]) / 2),
                   anchors=[])
    # A bond's FREE end reaches for a label a little way off (the bond stops short of the
    # letters); a ring corner, where several bonds meet, is a label only when it sits on one -- a
    # neighbouring structure's OH beside a ring corner is not that ring's atom.
    meeting = collections.Counter(labels_of)
    for c, centre in enumerate(centres):
        pad = 0.4 * tr.L if meeting[c] == 1 else 0.15 * tr.L
        hit = None
        best = None
        for lab in chem:
            x0, y0, x1, y1 = lab.bbox
            dx = max(x0 - centre[0], 0, centre[0] - x1)
            dy = max(y0 - centre[1], 0, centre[1] - y1)
            d = math.hypot(dx, dy)
            if d <= pad and (best is None or d < best):
                hit, best = lab, d
        if hit is not None:
            node = label_node[id(hit)]
            G.nodes[node]["anchors"].append(centre[0])
        else:
            node = ("V", c)
            G.add_node(node, kind="vertex", pos=centre)
        node_of_end[c] = node
    for idx, (point, k, side) in enumerate(ends):
        pass
    end_nodes = collections.defaultdict(dict)
    for idx, (point, k, side) in enumerate(ends):
        end_nodes[k][side] = node_of_end[labels_of[idx]]
    for k, s in enumerate(bases):
        a, b = end_nodes[k].get(0), end_nodes[k].get(1)
        if a is None or b is None or a == b:
            continue
        G.add_edge(a, b, order=s.order, drawn=True, segment=s)
    for left, right, order in dash_bonds:
        G.add_edge(label_node[id(left)], label_node[id(right)], order=order, drawn=False,
                   segment=None)
        G.nodes[label_node[id(left)]]["anchors"].append(left.bbox[2])
        G.nodes[label_node[id(right)]]["anchors"].append(right.bbox[0])

    # A stub dangling from an atom and shorter than half a bond is a piece of an arrow or a
    # charge sign, not a bond: a bond to an unlabelled end carbon is a whole bond long.
    for u, v, data in list(G.edges(data=True)):
        seg = data.get("segment")
        if seg is None or seg.length >= 0.5 * tr.L:
            continue
        for end in (u, v):
            if G.nodes[end]["kind"] == "vertex" and G.degree(end) == 1:
                G.remove_edge(u, v)
                G.remove_node(end)
                break
    for node in [n for n in G.nodes if G.nodes[n]["kind"] == "vertex" and G.degree(n) == 0]:
        G.remove_node(node)

    # explicit H drawn on a bond ("H-C" of an aldehyde): a leaf, kept beside its atom
    for node in list(G.nodes):
        data = G.nodes[node]
        if data["kind"] == "label" and not data["label"].heavy and G.degree(node) == 1:
            nbr = next(iter(G.neighbors(node)))
            G.nodes[nbr]["explicit_h"] = G.nodes[nbr].get("explicit_h", 0) + 1
            G.nodes[nbr].setdefault("h_nodes", []).append(node)
            data["kind"] = "h_leaf"

    for comp in nx.connected_components(G):
        sub = G.subgraph(comp)
        core = [n for n in comp if G.nodes[n]["kind"] != "h_leaf"]
        drawn = any(d.get("drawn") for _u, _v, d in sub.edges(data=True))
        has_ring = bool(nx.cycle_basis(sub))
        has_label = any(G.nodes[n]["kind"] == "label" and not G.nodes[n]["label"].wild
                        for n in core)
        if not core:
            continue
        tr.components.append({"nodes": set(comp), "core": core, "drawn": drawn,
                              # one label on one loose line (a reagent beside an arrow's tail,
                              # 2018_AA q066's NaOH) is not a drawn molecule
                              "molecular": drawn and (has_ring or (has_label and len(core) > 2)),
                              "bonded": sub.number_of_edges() > 0})
    # reading order: top-to-bottom rows, left to right
    def key(c):
        xs = [G.nodes[n]["pos"][0] for n in c["core"]]
        ys = [G.nodes[n]["pos"][1] for n in c["core"]]
        return (round((min(ys) + max(ys)) / 2 / (2.5 * tr.L)), (min(xs) + max(xs)) / 2)
    tr.components.sort(key=key)
    return tr


# ------------------------------------------------------------------------------------------------
# matching a SMILES to a printed molecule
# ------------------------------------------------------------------------------------------------

#: Counter-ions a booklet writes INTO a label: "ONa", "COONa", "SO3K".
COUNTER_IONS = {"Li", "Na", "K", "Rb", "Cs"}


def _mol_graph(mol):
    M = nx.Graph()
    for atom in mol.GetAtoms():
        M.add_node(atom.GetIdx(), el=atom.GetSymbol(), hs=atom.GetTotalNumHs())
    for bond in mol.GetBonds():
        order = 0 if bond.GetIsAromatic() else int(round(bond.GetBondTypeAsDouble()))
        M.add_edge(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), order=order)
    # A SALT: the SMILES has Na+ as its own ion, the print writes it into the label (2018_AA
    # q066's "ONa", q068's "COONa"). Each lone alkali cation is joined to an anionic atom, so
    # the label's atoms are one group.
    cations = [a.GetIdx() for a in mol.GetAtoms()
               if a.GetSymbol() in COUNTER_IONS and a.GetDegree() == 0 and a.GetFormalCharge() > 0]
    anions = [a.GetIdx() for a in mol.GetAtoms()
              if a.GetSymbol() in ("O", "N", "S") and a.GetFormalCharge() < 0]
    for c, a in zip(cations, anions):
        M.add_edge(a, c, order=1)
    return M


def _label_anchor(data):
    lab = data["label"]
    xs = data.get("anchors") or [(lab.bbox[0] + lab.bbox[2]) / 2]
    found = {lab.anchor(x) for x in xs} - {None}
    return found.pop() if len(found) == 1 else (lab.anchor(xs[0]) if xs else None)


def match(trace, component, smiles):
    """{atom index -> printed node} when the SMILES IS this printed molecule, else (None, why)."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, "SMILES does not parse"
    mol = Chem.RemoveHs(mol)
    G = trace.graph
    P = G.subgraph(component["core"]).copy()
    for node in P.nodes:
        data = P.nodes[node]
        if data["kind"] == "label":
            data["anchor"] = _label_anchor(data)
    M = _mol_graph(mol)

    def node_match(m, p):
        if p["kind"] == "vertex":
            return m["el"] == "C"
        return m["el"] == p.get("anchor")

    def edge_match(m, p):
        if m["order"] == 0:                      # aromatic: printed single, double, or in a circle
            return p["order"] in (1, 2, 3)       # (RDKit calls benzyne's ring aromatic too)
        return m["order"] == p["order"]

    if P.number_of_nodes() > M.number_of_nodes():
        return None, "the printed molecule has more atoms than the SMILES"
    matcher = isomorphism.GraphMatcher(M, P, node_match=node_match, edge_match=edge_match)
    best_why = "no way to lay the SMILES on the printed bonds"
    for mapping in matcher.subgraph_isomorphisms_iter():
        inv = {p: m for m, p in mapping.items()}
        covered = set(mapping)
        ok = True
        for p, data in P.nodes(data=True):
            if data["kind"] != "label":
                continue
            a = inv[p]
            group, stack = {a}, [a]
            while stack:
                x = stack.pop()
                for y in M.neighbors(x):
                    if y not in mapping and y not in group:
                        group.add(y)
                        stack.append(y)
            if (group - {a}) & covered:
                ok = False
                break
            heavy = collections.Counter(M.nodes[x]["el"] for x in group)
            if heavy != data["label"].heavy:
                ok = False
                best_why = "label %s does not stand for the SMILES atoms %s" % (
                    data["label"].text, dict(heavy))
                break
            hs = sum(M.nodes[x]["hs"] for x in group)
            if hs != data["label"].hydrogens + data.get("explicit_h", 0):
                ok = False
                best_why = "label %s shows %d H, the SMILES has %d" % (
                    data["label"].text, data["label"].hydrogens + data.get("explicit_h", 0), hs)
                break
            covered |= group
        if ok and covered == set(M.nodes):
            return mapping, "ok"
        if ok:
            best_why = "the SMILES has atoms the drawing does not show"
    return None, best_why


def usable(trace):
    """True when the figure is a vector drawing with at least one structure in it: then its SMILES
    are checked against it and it is drawn on it. A scanned page has no paths and is not."""
    return any(c["molecular"] for c in trace.components)


def _component_formula_text(trace, component):
    return " ".join(sorted(trace.graph.nodes[n]["label"].text for n in component["core"]
                           if trace.graph.nodes[n]["kind"] == "label"))


def assign(trace, species_list):
    """Match every species of a card to a printed molecule.

    Returns (results, problems). results[i] = {"component": index or None, "shown_as": "structure" |
    "text" | None}. problems lists every drawn molecule no SMILES matches and every species neither
    drawn nor written in the figure."""
    results, problems, used = [], [], set()
    text_labels = [lab for lab in trace.labels]
    for n, species in enumerate(species_list, 1):
        smiles = species.get("smiles") or ""
        found, why_all = None, []
        for k, comp in enumerate(trace.components):
            if k in used or not comp["bonded"]:
                continue
            mapping, why = match(trace, comp, smiles)
            if mapping is not None:
                found = (k, mapping)
                break
            if comp["molecular"]:
                why_all.append(why)
        if found:
            used.add(found[0])
            results.append({"component": found[0], "mapping": found[1], "shown_as": "structure"})
            continue
        # written as a formula ("+ CH3I", "NH2-"): a lone label with the same atoms
        mol = Chem.MolFromSmiles(smiles)
        written = None
        if mol is not None:
            mol = Chem.AddHs(mol)
            heavy = collections.Counter(a.GetSymbol() for a in mol.GetAtoms() if a.GetSymbol() != "H")
            hs = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == "H")
            for lab in text_labels:
                if lab.heavy == heavy and lab.hydrogens in (hs, 0):
                    written = lab
                    break
        if written is not None:
            results.append({"component": None, "shown_as": "text", "label": written.text})
            continue
        results.append({"component": None, "shown_as": None})
        problems.append("species %d (%s) is not the printed structure: %s"
                        % (n, species.get("name") or smiles, "; ".join(sorted(set(why_all)))
                           or "no printed molecule or formula has its atoms"))
    for k, comp in enumerate(trace.components):
        if comp["molecular"] and k not in used:
            problems.append("a printed structure (labels: %s) has no SMILES in the card"
                            % (_component_formula_text(trace, comp) or "skeleton only"))
    return results, problems


# ------------------------------------------------------------------------------------------------
# drawing
# ------------------------------------------------------------------------------------------------

def _color(rgb):
    if rgb is None:
        return "none"
    return "#%02x%02x%02x" % tuple(int(round(c * 255)) for c in rgb[:3])


def _path_d(sp, ox, oy):
    out = []
    for cmd in sp.commands:
        if cmd[0] == "M":
            out.append("M%.2f %.2f" % (cmd[1][0] - ox, cmd[1][1] - oy))
        elif cmd[0] == "L":
            out.append("L%.2f %.2f" % (cmd[1][0] - ox, cmd[1][1] - oy))
        elif cmd[0] == "C":
            out.append("C%.2f %.2f %.2f %.2f %.2f %.2f" % (
                cmd[1][0] - ox, cmd[1][1] - oy, cmd[2][0] - ox, cmd[2][1] - oy,
                cmd[3][0] - ox, cmd[3][1] - oy))
        else:
            out.append("Z")
    return " ".join(out)


def svg(trace, keep_subpaths=None, keep_glyphs=None, box=None, scale=2.0, pad=3.0, styles=None):
    """The traced figure as SVG, in the print's own coordinates (points), scaled for screen.

    `keep_*` restrict it to one structure (a species' own image); `box` is the region to show.
    `styles` = {font: {"italic", "serif"}}: the booklets' fonts carry no style the PDF exposes, so
    a physics spec's labels say which printed font is italic (P, V, i, f) or serif (IV, III)."""
    styles = styles or {}
    x0, y0, x1, y1 = box or trace.rect
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    w, h = x1 - x0, y1 - y0
    parts = []
    by_drawing = collections.OrderedDict()
    for sp in trace.subpaths:
        if keep_subpaths is not None and id(sp) not in keep_subpaths:
            continue
        by_drawing.setdefault(id(sp.drawing), (sp.drawing, []))[1].append(sp)
    for drawing, sps in by_drawing.values():
        d = " ".join(_path_d(sp, x0, y0) for sp in sps)
        kind = drawing.get("type") or "f"
        attrs = []
        if "f" in kind:
            attrs.append('fill="%s"' % _color(drawing.get("fill") or (0, 0, 0)))
            if drawing.get("even_odd"):
                attrs.append('fill-rule="evenodd"')
        else:
            attrs.append('fill="none"')
        if "s" in kind:
            attrs.append('stroke="%s" stroke-width="%.2f" stroke-linecap="%s" stroke-linejoin="round"'
                         % (_color(drawing.get("color") or (0, 0, 0)), drawing.get("width") or 1.0,
                            "round"))
        parts.append('<path d="%s" %s/>' % (d, " ".join(attrs)))
    for g in trace.glyphs:
        if keep_glyphs is not None and id(g) not in keep_glyphs:
            continue
        if g.c.isspace():
            continue
        style = styles.get(g.font) or {}
        parts.append('<text x="%.2f" y="%.2f" font-family="%s" '
                     'font-size="%.2f"%s%s fill="%s">%s</text>'
                     % (g.origin[0] - x0, g.origin[1] - y0,
                        "'Times New Roman', Times, serif" if style.get("serif")
                        else "Arial, Helvetica, sans-serif", g.size * 0.98,
                        ' font-weight="bold"' if g.bold else "",
                        ' font-style="italic"' if style.get("italic") else "",
                        g.color if g.color != "#000000" else "#000", html.escape(g.c)))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.2f %.2f" width="%.1f" '
            'height="%.1f"><rect width="100%%" height="100%%" fill="#fff"/>%s</svg>'
            % (w, h, w * scale, h * scale, "".join(parts)))


def component_svg(trace, k, scale=2.0):
    """One printed structure on its own: its bonds, labels and anything printed on it."""
    comp = trace.components[k]
    G = trace.graph
    subs, glyphs = set(), set()
    xs, ys = [], []
    for u, v, data in G.subgraph(comp["nodes"]).edges(data=True):
        seg = data.get("segment")
        if seg is not None:
            subs |= seg.subpaths
            for s in seg.parallels:
                subs |= s.subpaths
            xs += [seg.a[0], seg.b[0]]
            ys += [seg.a[1], seg.b[1]]
    for n in comp["nodes"]:
        data = G.nodes[n]
        if data["kind"] in ("label", "h_leaf"):
            lab = data["label"]
            glyphs |= {id(g) for g in lab.glyphs}
            xs += [lab.bbox[0], lab.bbox[2]]
            ys += [lab.bbox[1], lab.bbox[3]]
    if not xs:
        return None
    box = (min(xs), min(ys), max(xs), max(ys))
    for (cx, cy, r), sp in trace.circles:
        if box[0] <= cx <= box[2] and box[1] <= cy <= box[3]:
            subs.add(id(sp))
    # charges and lone pairs printed on the structure
    for g in trace.glyphs:
        gx, gy = (g.bbox[0] + g.bbox[2]) / 2, (g.bbox[1] + g.bbox[3]) / 2
        if box[0] - 2 <= gx <= box[2] + 2 and box[1] - 2 <= gy <= box[3] + 2 and g.c in "⊕⊖+-–−":
            glyphs.add(id(g))
    return svg(trace, keep_subpaths=subs, keep_glyphs=glyphs, box=box, scale=scale)


def ring_style(trace, k):
    """'circle' when the printed rings of this structure carry an inner circle, else 'lines'."""
    comp = trace.components[k]
    G = trace.graph
    pts = [G.nodes[n]["pos"] for n in comp["core"]]
    if not pts:
        return None
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
    y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
    for (cx, cy, _r), _sp in trace.circles:
        if x0 <= cx <= x1 and y0 <= cy <= y1:
            return "circle"
    return "lines"
