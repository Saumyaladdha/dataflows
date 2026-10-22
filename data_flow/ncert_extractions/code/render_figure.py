"""Render a figure SPEC into SVG: a diagram the pipeline owns, instead of a photocopy it inherited.

WHY REDRAW AT ALL
-----------------
The figures on the question cards are crops of a reprint, and three faults come with that and
cannot be cropped away. They are CLIPPED -- `2015_A q138` loses the top of its own stem, "direction
of current, if any, indu", because the drawing and the text share a region. They are RASTER at
booklet resolution, so the card blurs them when it scales them. And they carry the publisher's
watermark and page wash. `2015_A q180` shows the fourth fault: its three rays are LABELLED Blue,
Green and Red and drawn in identical black ink, because a photocopy has no colour -- the one thing
the question turns on is the thing the figure cannot show.

A redraw fixes all four, and costs a description.

A FIGURE IS A RECORD, NOT A PICTURE
-----------------------------------
This renderer deliberately makes no judgements, like every other script here. It takes a SPEC --
primitives and their coordinates, authored by whoever reads the original -- and draws exactly that.
The reading is the judgement and belongs to an agent; the drawing is mechanical and belongs here.
That split is what makes a redraw checkable: the original scan stays beside it on the card, so a
reviewer can see that the two agree, exactly as the booklet crop sits beside the extracted text.

COORDINATES ARE MATHEMATICAL, NOT SCREEN
----------------------------------------
y increases UPWARD, the origin is bottom-left, and the units are arbitrary. Anyone describing a
physics diagram thinks "the vector leaves the origin at 60 degrees", not "y is 143 pixels down", and
a spec written in screen coordinates is unreadable and unreviewable. The flip happens once, here.

NO THIRD-PARTY RENDERER
-----------------------
SVG is written directly. `schemdraw` is the better tool for a circuit and `drawsvg` for general
vector work, but the pages these figures land in must stay SELF-CONTAINED -- the shareable file
inlines every asset and the artifact viewer blocks external hosts - and plain SVG text embeds in
both with nothing to install. The moment a circuit needs real component symbols, schemdraw earns
its place; a coil, a ray and an arrow do not need it.
"""

import argparse
import json
import math
import os

#: One ink per role. `ink` is the drawing, `accent` picks out what the question turns on, and the
#: named colours exist because some figures are ABOUT colour -- see q180 in the module docstring.
INK = {"ink": "#11151d", "accent": "#1d3156", "muted": "#78808d",
       "blue": "#2f8fd0", "green": "#128a3f", "red": "#c02a2a",
       "violet": "#6a3f8f", "orange": "#cf6a1a", "yellow": "#c79f2c",
       # `white` is a FILL, not an ink, and it has to be a named colour here or a spec asking for
       # it falls through as a literal string: `fill: "card"` rendered BLACK, which turned Figure
       # 2.18's cavity into a black blob with its own labels invisible inside it.
       "white": "#ffffff", "card": "#ffffff",
       # A FILL and a LINE want different blues. NCERT's filled bodies are a light cyan that black
       # labels can sit on; its rays are a saturated blue that must read as a thin line.
       "bodyblue": "#4fb3e8", "palegrey": "#e8ecf2",
       # NCERT's own cyan. It prints circuit elements -- cell plates, node dots -- and its table
       # header bands in this colour, and a monochrome redraw of either is recognisably not the
       # same figure. Sampled from the PDF.
       "ncert": "#29abe2", "ncertband": "#e9eef3"}


class Canvas:
    """Draws primitives in mathematical coordinates and emits one SVG document."""

    def __init__(self, width, height, pad=14, scale=1.0):
        self.w, self.h, self.pad, self.scale = width, height, pad, scale
        self.body = []
        self.used_heads = set()
        self.washes = set()

    # -- coordinates -----------------------------------------------------------------------
    def x(self, value):
        return round(self.pad + value * self.scale, 2)

    def y(self, value):
        """The single place the mathematical y-up frame becomes SVG's y-down one."""
        return round(self.pad + (self.h - value) * self.scale, 2)

    # -- primitives ------------------------------------------------------------------------
    def line(self, a, b, colour="ink", width=1.8, dashed=False, arrow=None):
        head = ""
        if arrow in ("end", "both"):
            head += ' marker-end="url(#head-%s)"' % colour
            self.used_heads.add(colour)
        if arrow in ("start", "both"):
            head += ' marker-start="url(#tail-%s)"' % colour
            self.used_heads.add(colour)
        self.body.append(
            '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"%s%s/>'
            % (self.x(a[0]), self.y(a[1]), self.x(b[0]), self.y(b[1]), INK[colour], width,
               ' stroke-dasharray="1 6"' if dashed else "", head))

    def circle(self, centre, r, colour="ink", width=1.8, fill="none"):
        self.body.append(
            '<circle cx="%s" cy="%s" r="%s" stroke="%s" stroke-width="%s" fill="%s"/>'
            % (self.x(centre[0]), self.y(centre[1]), round(r * self.scale, 2), INK[colour],
               width, self._fill(fill)))

    def ellipse(self, centre, rx, ry, deg=0, colour="ink", width=1.8, fill="none", dashed=False):
        """An ellipse. The missing primitive that blocked a whole class of figure.

        A ring, a disc, the end cap of a cylinder, a sphere's equator, an orbit seen at an angle --
        physics draws circles in perspective constantly, and `circle` cannot. Table 6.1's entire
        Figure column is ellipses, which is why that column kept coming out empty.
        """
        self.body.append(
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" stroke="%s" stroke-width="%s" fill="%s"%s%s/>'
            % (self.x(centre[0]), self.y(centre[1]), round(rx * self.scale, 2),
               round(ry * self.scale, 2), INK[colour], width, self._fill(fill),
               ' stroke-dasharray="4 4"' if dashed else "",
               ' transform="rotate(%s %s %s)" ' % (-deg, self.x(centre[0]), self.y(centre[1]))
               if deg else ""))

    def dot(self, centre, r=3.2, colour="ink"):
        self.body.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
                         % (self.x(centre[0]), self.y(centre[1]), round(r, 2), INK[colour]))

    def polygon(self, points, colour="ink", width=1.8, fill="none"):
        pts = " ".join("%s,%s" % (self.x(p[0]), self.y(p[1])) for p in points)
        self.body.append('<polygon points="%s" stroke="%s" stroke-width="%s" fill="%s" '
                         'stroke-linejoin="round"/>'
                         % (pts, INK[colour], width, self._fill(fill)))

    def curve(self, points, closed=True, colour="ink", width=1.8, fill="none", tension=1.0,
              dashed=False):
        """A SMOOTH curve through the given points -- the shape NCERT draws for a conductor.

        WHY A POLYGON WILL NOT DO
        -------------------------
        An electrostatics figure is full of irregular closed surfaces: a conducting body, a cavity,
        a Gaussian surface. They are smooth and they are not ellipses, and `polygon` draws straight
        edges while `circle` draws a circle. Drawing Figure 2.18's conductor as an ellipse produced
        something recognisably wrong -- the outline is the one part of that figure a reader uses to
        tell the conductor from its cavity.

        The curve is a CATMULL-ROM SPLINE converted to cubic Beziers. That conversion is the whole
        of the method: a Catmull-Rom segment through P1 and P2, with neighbours P0 and P3, is the
        cubic Bezier with control points P1 + (P2-P0)/6t and P2 - (P3-P1)/6t. It passes THROUGH
        every point given, which is what makes a spec readable -- the author lists points on the
        outline rather than control points that lie off it.
        """
        pts = list(points)
        if len(pts) < 3:
            return
        n = len(pts)
        d = ["M %s %s" % (self.x(pts[0][0]), self.y(pts[0][1]))]
        last = n if closed else n - 1
        for i in range(last):
            p0 = pts[(i - 1) % n] if closed else pts[max(i - 1, 0)]
            p1, p2 = pts[i % n], pts[(i + 1) % n]
            p3 = pts[(i + 2) % n] if closed else pts[min(i + 2, n - 1)]
            c1 = (p1[0] + (p2[0] - p0[0]) / (6 * tension),
                  p1[1] + (p2[1] - p0[1]) / (6 * tension))
            c2 = (p2[0] - (p3[0] - p1[0]) / (6 * tension),
                  p2[1] - (p3[1] - p1[1]) / (6 * tension))
            d.append("C %s %s %s %s %s %s"
                     % (self.x(c1[0]), self.y(c1[1]), self.x(c2[0]), self.y(c2[1]),
                        self.x(p2[0]), self.y(p2[1])))
        if closed:
            d.append("Z")
        self.body.append('<path d="%s" stroke="%s" stroke-width="%s" fill="%s"%s/>'
                         % (" ".join(d), INK[colour], width, self._fill(fill),
                            ' stroke-dasharray="4 5"' if dashed else ""))

    def _fill(self, fill):
        """A flat colour, `none`, or a named WASH -- a soft tonal fill, registered as a gradient.

        NCERT fills a conducting body with a pale tone that fades across it. A flat colour reads as
        a solid object and a white fill loses the body altogether, so the wash is its own thing.
        """
        if fill in ("none", None):
            return "none"
        if fill.startswith("wash"):
            key = fill.split(":", 1)[1] if ":" in fill else "accent"
            self.washes.add(key)
            return "url(#wash-%s)" % key
        return INK.get(fill, fill)

    def angle(self, vertex, r, start_deg, end_deg, colour="muted", width=1.4):
        """A small arc marking an angle at `vertex`, drawn the short way round."""
        a0, a1 = math.radians(start_deg), math.radians(end_deg)
        p0 = (vertex[0] + r * math.cos(a0), vertex[1] + r * math.sin(a0))
        p1 = (vertex[0] + r * math.cos(a1), vertex[1] + r * math.sin(a1))
        large = 1 if abs(end_deg - start_deg) > 180 else 0
        sweep = 0 if end_deg > start_deg else 1
        self.body.append(
            '<path d="M %s %s A %s %s 0 %d %d %s %s" stroke="%s" stroke-width="%s" fill="none"/>'
            % (self.x(p0[0]), self.y(p0[1]), round(r * self.scale, 2), round(r * self.scale, 2),
               large, sweep, self.x(p1[0]), self.y(p1[1]), INK[colour], width))

    def right_angle(self, vertex, size=7, towards=(1, 1), colour="muted", width=1.3):
        """The square that marks a right angle, opening towards `towards`."""
        dx, dy = towards
        a = (vertex[0] + size * dx, vertex[1])
        b = (vertex[0] + size * dx, vertex[1] + size * dy)
        c = (vertex[0], vertex[1] + size * dy)
        pts = " ".join("%s,%s" % (self.x(p[0]), self.y(p[1])) for p in (a, b, c))
        self.body.append('<polyline points="%s" stroke="%s" stroke-width="%s" fill="none"/>'
                         % (pts, INK[colour], width))

    #: Precomposed super/subscript characters, and the plain character each stands for. A label
    #: written `m⁻²` reads correctly in a spec and renders with a hole in it, because U+207B is
    #: absent from the serif stack and the system substitutes a different face mid-word. Mapping
    #: them onto the renderer's own tspan keeps one typeface across the whole label.
    SUPERS = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7",
              "⁸": "8", "⁹": "9", "⁻": "\u2212", "⁺": "+", "⁼": "=", "⁽": "(", "⁾": ")",
              "ⁿ": "n"}
    SUBS = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7",
            "₈": "8", "₉": "9", "₋": "\u2212", "₊": "+"}

    def _split_scripts(self, text):
        """(body, trailing superscript, trailing subscript) for a label written with precomposed
        characters. Only a RUN AT THE END is lifted -- a superscript in the middle of a label is
        left alone, because moving it would change where the rest of the text sits."""
        sup = sub = ""
        while text and text[-1] in self.SUPERS and not sub:
            sup = self.SUPERS[text[-1]] + sup
            text = text[:-1]
        while text and text[-1] in self.SUBS and not sup:
            sub = self.SUBS[text[-1]] + sub
            text = text[:-1]
        return text, sup, sub

    def label(self, text, at, anchor="middle", size=15, colour="ink", style="serif",
              baseline="middle", italic=False, sub=None, sup=None):
        """Text, optionally with a subscript or superscript.

        `sub` exists because the alternative is two labels at hand-chosen coordinates, and that is
        a standing invitation to misplace one: the first draft of the Wheatstone bridge positioned
        every `R` and every `2` separately, and the subscripts drifted onto the resistor zigzags.
        A tspan is positioned by the text engine relative to its own base, so it cannot drift.
        """
        family = ("ui-serif,Georgia,'Times New Roman',serif" if style == "serif"
                  else "ui-sans-serif,system-ui,sans-serif")
        if sub is None and sup is None:
            text, lifted_sup, lifted_sub = self._split_scripts(text)
            sup = lifted_sup or None
            sub = lifted_sub or None
        extra = ""
        if sub is not None:
            extra = ('<tspan font-size="%s" dy="%s">%s</tspan>'
                     % (round(size * 0.62, 1), round(size * 0.22, 1), sub))
        elif sup is not None:
            extra = ('<tspan font-size="%s" dy="%s">%s</tspan>'
                     % (round(size * 0.62, 1), round(-size * 0.42, 1), sup))
        self.body.append(
            '<text x="%s" y="%s" text-anchor="%s" dominant-baseline="%s" font-size="%s" '
            'font-family="%s" fill="%s"%s>%s%s</text>'
            % (self.x(at[0]), self.y(at[1]), anchor, baseline, size, family, INK[colour],
               ' font-style="italic"' if italic else "", text, extra))

    # -- circuit components ----------------------------------------------------------------
    # A SCHEMATIC NEEDS SYMBOLS, NOT JUST SHAPES. A Wheatstone bridge is four resistors, a cell and
    # a galvanometer; drawing them from lines and circles each time would put the SYMBOL in every
    # spec instead of in the renderer, and two specs would then disagree about what a resistor looks
    # like. These three cover the circuits this corpus asks about. Anything beyond them -- real
    # component libraries, transistors, logic gates -- is where `schemdraw` earns its place and this
    # renderer should hand over rather than grow.
    def resistor(self, a, b, colour="accent", width=1.8, zigs=6, amp=7, lead=0.22):
        """A zigzag between two points, with straight leads at each end."""
        ax, ay = a
        bx, by = b
        length = math.hypot(bx - ax, by - ay)
        if length < 1:
            return
        ux, uy = (bx - ax) / length, (by - ay) / length
        nx, ny = -uy, ux                                  # unit normal, for the zig amplitude
        start = (ax + ux * length * lead, ay + uy * length * lead)
        end = (bx - ux * length * lead, by - uy * length * lead)
        span = length * (1 - 2 * lead)
        points = [start]
        for i in range(1, zigs * 2):
            along = span * i / (zigs * 2)
            side = amp if i % 2 else -amp
            points.append((start[0] + ux * along + nx * side,
                           start[1] + uy * along + ny * side))
        points.append(end)
        self.line(a, start, colour=colour, width=width)
        self.line(end, b, colour=colour, width=width)
        pts = " ".join("%s,%s" % (self.x(px), self.y(py)) for px, py in points)
        self.body.append('<polyline points="%s" stroke="%s" stroke-width="%s" fill="none" '
                         'stroke-linejoin="round" stroke-linecap="round"/>'
                         % (pts, INK[colour], width))

    def cell(self, centre, plates=2, colour="accent", width=1.8, long=15, short=8, gap=7,
             horizontal=False):
        """A battery: alternating long and short plates, `plates` cells of them."""
        cx, cy = centre
        n = plates * 2
        for i in range(n):
            offset = (i - (n - 1) / 2) * gap
            half = (long if i % 2 == 0 else short) / 2
            if horizontal:
                self.line((cx + offset, cy - half), (cx + offset, cy + half),
                          colour=colour, width=width if i % 2 == 0 else width + 0.6)
            else:
                self.line((cx - half, cy + offset), (cx + half, cy + offset),
                          colour=colour, width=width if i % 2 == 0 else width + 0.6)

    def diode(self, a, b, colour="accent", width=1.8, size=11):
        """A triangle pointing at a bar: the junction diode, as NCERT prints it."""
        (ax, ay), (bx, by) = a, b
        length = math.hypot(bx - ax, by - ay) or 1.0
        ux, uy = (bx - ax) / length, (by - ay) / length
        nx, ny = -uy, ux
        mid = ((ax + bx) / 2, (ay + by) / 2)
        tip = (mid[0] + ux * size * 0.5, mid[1] + uy * size * 0.5)
        back = (mid[0] - ux * size * 0.5, mid[1] - uy * size * 0.5)
        self.line(a, back, colour=colour, width=width)
        self.line(tip, b, colour=colour, width=width)
        self.polygon([(back[0] + nx * size * 0.5, back[1] + ny * size * 0.5),
                      (back[0] - nx * size * 0.5, back[1] - ny * size * 0.5), tip],
                     colour=colour, width=width, fill=colour)
        self.line((tip[0] + nx * size * 0.55, tip[1] + ny * size * 0.55),
                  (tip[0] - nx * size * 0.55, tip[1] - ny * size * 0.55),
                  colour=colour, width=width + 0.4)

    def gate(self, at, gate="and", w=52, h=40, colour="ink", width=1.9):
        """An AND or OR gate, drawn left-to-right with `at` as the left edge's midpoint.

        The two shapes are what distinguishes them and both are curves, so they are paths rather
        than assembled from lines: an AND is a flat back with a semicircular nose, an OR is a
        concave back with a pointed nose. Getting those two outlines right is the whole of reading
        a logic diagram, so they belong in the renderer and not in a spec.
        """
        x, y = at
        top, bottom = y + h / 2, y - h / 2
        if gate == "and":
            d = ("M %s %s L %s %s L %s %s A %s %s 0 0 0 %s %s L %s %s Z"
                 % (self.x(x), self.y(top), self.x(x), self.y(bottom),
                    self.x(x + w - h / 2), self.y(bottom),
                    round(h / 2 * self.scale, 2), round(h / 2 * self.scale, 2),
                    self.x(x + w - h / 2), self.y(top), self.x(x), self.y(top)))
        else:
            d = ("M %s %s Q %s %s %s %s Q %s %s %s %s Q %s %s %s %s Z"
                 % (self.x(x), self.y(top),
                    self.x(x + w * 0.30), self.y(y), self.x(x), self.y(bottom),
                    self.x(x + w * 0.72), self.y(bottom - 1), self.x(x + w), self.y(y),
                    self.x(x + w * 0.72), self.y(top + 1), self.x(x), self.y(top)))
        self.body.append('<path d="%s" stroke="%s" stroke-width="%s" fill="none" '
                         'stroke-linejoin="round"/>' % (d, INK[colour], width))

    def band(self, corner, w, h, fill="ncertband", colour=None, width=1.0):
        """A filled rectangle given by its bottom-left corner -- a table header or row band."""
        x, y = corner
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        shape = " ".join("%s,%s" % (self.x(px), self.y(py)) for px, py in pts)
        self.body.append('<polygon points="%s" fill="%s"%s/>'
                         % (shape, self._fill(fill),
                            ' stroke="%s" stroke-width="%s"' % (INK[colour], width)
                            if colour else ""))

    def block(self, centre, w, h, deg=0, colour="ink", width=1.8, hatch=7):
        """A hatched rectangle: the block on an incline, as every mechanics figure draws it.

        Rotation is given in degrees so an incline's block can be laid flat ON the slope by reusing
        the slope's own angle -- which is also the only way the two can be guaranteed to agree.
        """
        cx, cy = centre
        rad = math.radians(deg)
        ux, uy = math.cos(rad), math.sin(rad)
        nx, ny = -uy, ux
        corner = [(cx + ux * w / 2 + nx * h / 2, cy + uy * w / 2 + ny * h / 2),
                  (cx + ux * w / 2 - nx * h / 2, cy + uy * w / 2 - ny * h / 2),
                  (cx - ux * w / 2 - nx * h / 2, cy - uy * w / 2 - ny * h / 2),
                  (cx - ux * w / 2 + nx * h / 2, cy - uy * w / 2 + ny * h / 2)]
        self.polygon(corner, colour=colour, width=width)
        # Hatching runs corner to corner inside the box, clipped by walking along its own edges.
        steps = max(2, int(w / hatch))
        for i in range(1, steps):
            t = i / steps
            a = (corner[3][0] + (corner[2][0] - corner[3][0]) * t,
                 corner[3][1] + (corner[2][1] - corner[3][1]) * t)
            b = (corner[0][0] + (corner[1][0] - corner[0][0]) * t,
                 corner[0][1] + (corner[1][1] - corner[0][1]) * t)
            # a 45-degree hatch: shift one end along the short edge
            self.line((a[0] + nx * h, a[1] + ny * h), b, colour=colour, width=0.9)

    def terminal(self, centre, r=4.0, colour="ink", width=1.7):
        """The small open circle NCERT puts on an input or output lead."""
        self.body.append('<circle cx="%s" cy="%s" r="%s" stroke="%s" stroke-width="%s" '
                         'fill="#ffffff"/>'
                         % (self.x(centre[0]), self.y(centre[1]), round(r * self.scale, 2),
                            INK[colour], width))

    def meter(self, centre, r, text, colour="ink", width=1.8, size=14):
        """An instrument: a circle with its letter, as NCERT draws a galvanometer."""
        self.circle(centre, r, colour=colour, width=width)
        self.label(text, centre, size=size, colour=colour, italic=True)

    # -- output ----------------------------------------------------------------------------
    def svg(self, title=""):
        defs = "".join(
            '<marker id="head-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="%s"/></marker>'
            '<marker id="tail-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="%s"/></marker>'
            % (c, INK[c], c, INK[c]) for c in sorted(self.used_heads))
        defs += "".join(
            '<linearGradient id="wash-%s" x1="0" y1="0" x2="0.35" y2="1">'
            '<stop offset="0%%" stop-color="%s" stop-opacity="0.34"/>'
            '<stop offset="55%%" stop-color="%s" stop-opacity="0.12"/>'
            '<stop offset="100%%" stop-color="%s" stop-opacity="0.26"/></linearGradient>'
            % (k, INK.get(k, k), INK.get(k, k), INK.get(k, k)) for k in sorted(self.washes))
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" '
                'width="%s" height="%s" role="img" aria-label="%s">'
                '<defs>%s</defs>%s</svg>'
                % (round(self.w * self.scale + 2 * self.pad, 1),
                   round(self.h * self.scale + 2 * self.pad, 1),
                   round(self.w * self.scale + 2 * self.pad, 1),
                   round(self.h * self.scale + 2 * self.pad, 1),
                   title.replace('"', "'"), defs, "".join(self.body)))


def beside(a, b, offset, side=1):
    """A point `offset` away from the midpoint of a-b, perpendicular to it.

    WHY THE RENDERER PLACES THESE AND NOT THE SPEC
    ---------------------------------------------
    A label for a component belongs at a fixed distance to one side of it, and working that point
    out by hand means trigonometry per label and a collision whenever the arithmetic is loose. The
    Wheatstone bridge was authored that way twice and both times `R2` and `R4` landed on top of
    their own resistor zigzags -- which is the kind of fault that is invisible in a spec and
    obvious on screen. Given the two endpoints, there is exactly one right answer for where the
    label goes, so the renderer computes it.

    `side` is +1 or -1 and chooses which side of the line; for the arms of a diamond, +1 is away
    from the centre when the points are given anticlockwise.
    """
    (ax, ay), (bx, by) = a, b
    length = math.hypot(bx - ax, by - ay) or 1.0
    ux, uy = (bx - ax) / length, (by - ay) / length
    nx, ny = -uy * side, ux * side
    return [ (ax + bx) / 2 + nx * offset, (ay + by) / 2 + ny * offset ]


#: The spec vocabulary. Every entry is (name, required keys) -- a spec naming anything else is a
#: spec written against a renderer that does not exist, and is refused rather than half-drawn.
PRIMITIVES = {
    "line": ("from", "to"), "circle": ("centre", "r"), "dot": ("centre",),
    "polygon": ("points",), "angle": ("vertex", "r", "from_deg", "to_deg"),
    "right_angle": ("vertex",), "label": ("text",),
    "resistor": ("from", "to"), "cell": ("centre",), "meter": ("centre", "r", "text"),
    "diode": ("from", "to"), "gate": ("at",), "terminal": ("centre",),
    "block": ("centre", "w", "h"), "curve": ("points",), "band": ("corner", "w", "h"),
    "ellipse": ("centre", "rx", "ry"),
}


def render(spec):
    canvas = Canvas(spec["width"], spec["height"], spec.get("pad", 14), spec.get("scale", 1.0))
    for item in spec["draw"]:
        kind = item.get("kind")
        if kind not in PRIMITIVES:
            raise ValueError("unknown primitive %r; the renderer draws %s"
                             % (kind, ", ".join(sorted(PRIMITIVES))))
        for key in PRIMITIVES[kind]:
            if key not in item:
                raise ValueError("%s needs %r" % (kind, key))
        if kind == "label" and not ("at" in item or "beside" in item):
            raise ValueError("label needs either `at` or `beside`")
        args = {k: v for k, v in item.items() if k != "kind"}
        # A label may name its position RELATIVE to a component instead of absolutely.
        if "beside" in args:
            spot = args.pop("beside")
            args["at"] = beside(spot["from"], spot["to"], spot.get("offset", 40),
                                spot.get("side", 1))
        if kind == "line":
            canvas.line(args.pop("from"), args.pop("to"), **args)
        elif kind == "circle":
            canvas.circle(args.pop("centre"), args.pop("r"), **args)
        elif kind == "dot":
            canvas.dot(args.pop("centre"), **args)
        elif kind == "polygon":
            canvas.polygon(args.pop("points"), **args)
        elif kind == "angle":
            canvas.angle(args.pop("vertex"), args.pop("r"), args.pop("from_deg"),
                         args.pop("to_deg"), **args)
        elif kind == "right_angle":
            canvas.right_angle(args.pop("vertex"), **args)
        elif kind == "label":
            canvas.label(args.pop("text"), args.pop("at"), **args)
        elif kind == "resistor":
            canvas.resistor(args.pop("from"), args.pop("to"), **args)
        elif kind == "cell":
            canvas.cell(args.pop("centre"), **args)
        elif kind == "meter":
            canvas.meter(args.pop("centre"), args.pop("r"), args.pop("text"), **args)
        elif kind == "diode":
            canvas.diode(args.pop("from"), args.pop("to"), **args)
        elif kind == "gate":
            canvas.gate(args.pop("at"), **args)
        elif kind == "terminal":
            canvas.terminal(args.pop("centre"), **args)
        elif kind == "block":
            canvas.block(args.pop("centre"), args.pop("w"), args.pop("h"), **args)
        elif kind == "curve":
            canvas.curve(args.pop("points"), **args)
        elif kind == "band":
            canvas.band(args.pop("corner"), args.pop("w"), args.pop("h"), **args)
        elif kind == "ellipse":
            canvas.ellipse(args.pop("centre"), args.pop("rx"), args.pop("ry"), **args)
    return canvas.svg(spec.get("title", ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("specs", nargs="+", help="figure spec JSON files")
    ap.add_argument("--out-dir", default="figures/svg")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    for path in args.specs:
        with open(path, encoding="utf-8") as fh:
            spec = json.load(fh)
        svg = render(spec)
        target = os.path.join(args.out_dir,
                              os.path.basename(path).replace(".json", ".svg"))
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(svg)
        print("  %-34s %5d bytes   %s" % (target, len(svg), spec.get("title", "")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
