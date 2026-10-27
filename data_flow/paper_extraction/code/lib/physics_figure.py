"""Render a figure SPEC into SVG: a diagram the pipeline owns, instead of a photocopy it inherited.

PAPER-PIPELINE COPY (2026-10-26) of ncert_extractions/code/render_figure.py, kept here because each
pipeline is self-contained. Added for the NEET booklets: capacitor, inductor, switch, battery and
spring primitives (2017_A q8 and q17 draw L-R-C and C-V circuits the pilot could not), component ink
defaulting to black because these booklets print in black, and `check_spec()` -- every claimed angle
recomputed from the coordinates, and a circuit's netlist compared with the connectivity its drawn
wires actually make (FIGURE_RENDERING_PLAN.md "Level 3").

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
        if arrow == "mid":
            # AN ARROW ON THE LINE, not at its end: the direction of a process on a P-V diagram
            # (2017_A q016 prints one at the middle of each of I-IV) or of a current along a wire.
            length, ux, uy, nx, ny = self._axis(a, b)
            mx, my = (a[0] + b[0]) / 2 + ux * 3.5, (a[1] + b[1]) / 2 + uy * 3.5
            size = 7.0
            self.polygon([(mx, my), (mx - ux * size + nx * size * 0.45, my - uy * size + ny * size * 0.45),
                          (mx - ux * size - nx * size * 0.45, my - uy * size - ny * size * 0.45)],
                         colour=colour, width=1.0, fill=colour)
            arrow = None
        # ARROWHEADS ARE DRAWN, NOT MARKERS. An SVG <marker> is dropped by some renderers (MuPDF,
        # several PDF and image converters), and with it every force arrow of 2017_A q036's
        # free-body diagrams -- the figure's whole content. A filled triangle at the tip is drawn
        # everywhere; the line stops at the head's base so the tip stays sharp.
        head = ""
        size = 11.0 / (self.scale or 1.0)
        length, ux, uy, nx, ny = self._axis(a, b)
        if arrow in ("end", "both") and length > size:
            self._head(b, ux, uy, nx, ny, size, colour)
            b = (b[0] - ux * size * 0.8, b[1] - uy * size * 0.8)
        if arrow in ("start", "both") and length > size:
            self._head(a, -ux, -uy, nx, ny, size, colour)
            a = (a[0] + ux * size * 0.8, a[1] + uy * size * 0.8)
        if dashed:
            # DOTS DRAWN AS DOTS, not a stroke-dasharray, which some renderers ignore and then
            # draw the dotted level lines of q004 and the axes of q037 solid.
            pixels = math.hypot(self.x(b[0]) - self.x(a[0]), self.y(b[1]) - self.y(a[1]))
            count = max(2, int(pixels / 6.0))
            dots = []
            for n in range(count + 1):
                t = n / float(count)
                px = self.x(a[0]) + (self.x(b[0]) - self.x(a[0])) * t
                py = self.y(a[1]) + (self.y(b[1]) - self.y(a[1])) * t
                dots.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/>'
                            % (px, py, max(0.7, width * 0.5), INK[colour]))
            self.body.append("".join(dots))
            return
        self.body.append(
            '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"%s/>'
            % (self.x(a[0]), self.y(a[1]), self.x(b[0]), self.y(b[1]), INK[colour], width, head))

    def _head(self, tip, ux, uy, nx, ny, size, colour):
        """A filled arrowhead with its point at `tip`, pointing along (ux, uy)."""
        base = (tip[0] - ux * size, tip[1] - uy * size)
        self.polygon([tip, (base[0] + nx * size * 0.38, base[1] + ny * size * 0.38),
                      (base[0] - nx * size * 0.38, base[1] - ny * size * 0.38)],
                     colour=colour, width=0.8, fill=colour)

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

    # OPEN by default in this copy. The pilot defaulted to closed (it drew conductors), and every one
    # of the 19 curves in 2017_A's specs -- isotherms, equipotentials, a U-tube -- omitted the key
    # and came out as a closed blob. A graph line is the common case; a closed shape says so.
    def curve(self, points, closed=False, colour="ink", width=1.8, fill="none", tension=1.0,
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

    def angle(self, vertex, r, start_deg, end_deg, colour="ink", width=1.3):
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

    def right_angle(self, vertex, size=7, towards=(1, 1), colour="ink", width=1.2):
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

    def label(self, text, at, anchor="middle", size=15, colour="ink", style="sans",
              baseline="middle", italic=False, sub=None, sup=None):
        """Text, optionally with a subscript or superscript.

        `sub` exists because the alternative is two labels at hand-chosen coordinates, and that is
        a standing invitation to misplace one: the first draft of the Wheatstone bridge positioned
        every `R` and every `2` separately, and the subscripts drifted onto the resistor zigzags.
        A tspan is positioned by the text engine relative to its own base, so it cannot drift.
        """
        # SANS BY DEFAULT: the NEET booklets letter their figures in Arial/Helvetica (R, L, C, P,
        # V, 700 K), and a serif label beside the exact printed copy read as a different figure.
        family = ("ui-serif,Georgia,'Times New Roman',serif" if style == "serif"
                  else "Arial,Helvetica,'Liberation Sans',sans-serif")
        if sub is None and sup is None:
            text, lifted_sup, lifted_sub = self._split_scripts(text)
            sup = lifted_sup or None
            sub = lifted_sub or None
        # The script is its OWN <text>, placed at an explicit x/y after the base's estimated
        # width -- not a <tspan dy>, which some renderers draw on top of the base letter (2017_A
        # q037's I0..I3 and q011's T1, K2 came out as one glyph over another).
        base_w = 0.56 * size * len(text)
        x0 = self.x(at[0]) - (base_w if anchor == "end" else base_w / 2 if anchor == "middle" else 0)
        y0 = self.y(at[1])
        common = 'font-family="%s" fill="%s"%s' % (family, INK[colour],
                                                   ' font-style="italic"' if italic else "")
        self.body.append('<text x="%s" y="%s" text-anchor="start" dominant-baseline="%s" '
                         'font-size="%s" %s>%s</text>'
                         % (round(x0, 2), y0, baseline, size, common, text))
        script, dy = (sub, size * 0.3) if sub is not None else (sup, -size * 0.45)
        if script is not None:
            self.body.append('<text x="%s" y="%s" text-anchor="start" dominant-baseline="%s" '
                             'font-size="%s" %s>%s</text>'
                             % (round(x0 + base_w + size * 0.04, 2), round(y0 + dy, 2), baseline,
                                round(size * 0.62, 1), common, script))

    # -- circuit components ----------------------------------------------------------------
    # A SCHEMATIC NEEDS SYMBOLS, NOT JUST SHAPES. A Wheatstone bridge is four resistors, a cell and
    # a galvanometer; drawing them from lines and circles each time would put the SYMBOL in every
    # spec instead of in the renderer, and two specs would then disagree about what a resistor looks
    # like. These three cover the circuits this corpus asks about. Anything beyond them -- real
    # component libraries, transistors, logic gates -- is where `schemdraw` earns its place and this
    # renderer should hand over rather than grow.
    def resistor(self, a, b, colour="ink", width=1.8, zigs=6, amp=7, lead=0.22):
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
        # SIZED TO THE PART, not fixed. Six zigs at amplitude 7 is right for a long resistor and a
        # black smear on a short one: 2017_A q008's resistors span ~25 units, so twelve strokes were
        # packed two units apart and printed as a solid block. The booklets draw 3-4 peaks whatever
        # the length, with the zig at least as long as it is tall.
        # ...so the COUNT stays (the booklets print ~5-6 small peaks) and the HEIGHT follows the
        # pitch: a zig about as tall as it is wide reads as a resistor at any length, where fewer,
        # taller zigs turned q022's resistors into three big teeth and q008's into one.
        zigs = max(4, min(zigs, 5))
        amp = min(amp, 1.6 * span / (2 * zigs))
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

    def cell(self, centre, plates=2, colour="ink", width=1.8, long=15, short=8, gap=7,
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

    def diode(self, a, b, colour="ink", width=1.8, size=11, filled=False):
        """A triangle pointing at a bar: the junction diode. HOLLOW by default, as the NEET
        booklets print it (2017_A q022); NCERT's filled triangle with `filled: true`."""
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
                     colour=colour, width=width, fill=colour if filled else "white")
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

    # -- two-terminal components between points, added for the paper corpus -----------------
    def _axis(self, a, b):
        (ax, ay), (bx, by) = a, b
        length = math.hypot(bx - ax, by - ay) or 1.0
        ux, uy = (bx - ax) / length, (by - ay) / length
        return length, ux, uy, -uy, ux

    def capacitor(self, a, b, colour="ink", width=1.8, gap=6, plate=16):
        """Two parallel plates across the middle of a-b, with leads to each end."""
        length, ux, uy, nx, ny = self._axis(a, b)
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        p1 = (mx - ux * gap / 2, my - uy * gap / 2)
        p2 = (mx + ux * gap / 2, my + uy * gap / 2)
        self.line(a, p1, colour=colour, width=width)
        self.line(p2, b, colour=colour, width=width)
        for p in (p1, p2):
            self.line((p[0] + nx * plate / 2, p[1] + ny * plate / 2),
                      (p[0] - nx * plate / 2, p[1] - ny * plate / 2), colour=colour, width=width + 0.4)

    def battery(self, a, b, plates=1, colour="ink", width=1.8, long=16, short=8, gap=6):
        """A cell or battery between two points: long (+) and short (-) plates, leads to the ends."""
        length, ux, uy, nx, ny = self._axis(a, b)
        n = plates * 2
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        first = (mx - ux * gap * (n - 1) / 2, my - uy * gap * (n - 1) / 2)
        last = (mx + ux * gap * (n - 1) / 2, my + uy * gap * (n - 1) / 2)
        self.line(a, first, colour=colour, width=width)
        self.line(last, b, colour=colour, width=width)
        for i in range(n):
            c = (first[0] + ux * gap * i, first[1] + uy * gap * i)
            half = (long if i % 2 == 0 else short) / 2
            self.line((c[0] + nx * half, c[1] + ny * half), (c[0] - nx * half, c[1] - ny * half),
                      colour=colour, width=width if i % 2 == 0 else width + 0.6)

    def inductor(self, a, b, colour="ink", width=1.8, loops=4, lead=0.2, height=10.0, count=None):
        """A coil: overlapping loops along a-b (a prolate trochoid), with straight leads.

        The pilot drew semicircles whose radius was half the pitch, so the coil was only as tall
        as its loops were wide -- on 2017_A q008's short inductors that came out as a row of small
        bumps, unrecognisable as an inductor. A printed coil is a run of LOOPS a fixed height
        tall: x = a.t - b.sin t, y = b(1 - cos t) with b = 2a draws exactly that, and the loop
        count follows from the length, so a short coil gets fewer loops, never flatter ones.
        """
        length, ux, uy, nx, ny = self._axis(a, b)
        start = (a[0] + ux * length * lead, a[1] + uy * length * lead)
        end = (b[0] - ux * length * lead, b[1] - uy * length * lead)
        self.line(a, start, colour=colour, width=width)
        self.line(end, b, colour=colour, width=width)
        span = math.hypot(end[0] - start[0], end[1] - start[1])
        radius = min(height / 2.0, span * 0.3)            # b: half the coil's height
        pitch = 2 * math.pi * radius / 2.0                 # a = b/2 -> one loop every 2*pi*a
        count = count or max(3, min(loops + 1, int(round(span / pitch))))
        rate = span / (2 * math.pi * count)                # a, refitted to land on `end`
        radius = min(radius, 3.2 * rate)                   # b/a ~3: full, overlapping loops
        # CENTRED on the wire, as printed: the loops straddle the line, entering at a loop's edge
        points = [start]
        steps = 40 * count
        for i in range(steps + 1):
            t = 2 * math.pi * count * i / steps
            along = rate * t - radius * math.sin(t)
            side = -radius * math.cos(t)
            points.append((start[0] + ux * along + nx * side, start[1] + uy * along + ny * side))
        points.append(end)
        pts = " ".join("%s,%s" % (self.x(px), self.y(py)) for px, py in points)
        self.body.append('<polyline points="%s" stroke="%s" stroke-width="%s" fill="none" '
                         'stroke-linejoin="round"/>' % (pts, INK[colour], width))

    def switch(self, a, b, closed=False, colour="ink", width=1.8):
        """A knife switch: a terminal at each end, the blade open at 25 degrees unless `closed`."""
        length, ux, uy, nx, ny = self._axis(a, b)
        # solid contact dots, as the booklets print a switch (q008), not NCERT's open terminals
        self.dot(a, r=2.4, colour=colour)
        self.dot(b, r=2.4, colour=colour)
        if closed:
            self.line(a, b, colour=colour, width=width)
            return
        angle = math.radians(25)
        tip = (a[0] + (ux * math.cos(angle) - uy * math.sin(angle)) * length * 0.95,
               a[1] + (uy * math.cos(angle) + ux * math.sin(angle)) * length * 0.95)
        self.line(a, tip, colour=colour, width=width)

    def spring(self, a, b, colour="ink", width=1.6, coils=8, amp=6, lead=0.12):
        """A spring: a COIL of loops, as the NEET booklets print it (2017_A q036's spring is a run
        of overlapping loops; a zigzag is the resistor symbol and read as one)."""
        # a FIXED number of tight loops whatever the length: q036 prints 6-7 small loops on a
        # spring the length of three inductor loops
        self.inductor(a, b, colour=colour, width=width, lead=lead, height=amp * 2, count=coils - 1)

    def band(self, corner, w, h, fill="ncertband", colour=None, width=1.0):
        """A filled rectangle given by its bottom-left corner -- a table header or row band."""
        x, y = corner
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        shape = " ".join("%s,%s" % (self.x(px), self.y(py)) for px, py in pts)
        self.body.append('<polygon points="%s" fill="%s"%s/>'
                         % (shape, self._fill(fill),
                            ' stroke="%s" stroke-width="%s"' % (INK[colour], width)
                            if colour else ""))

    def block(self, centre, w, h, deg=0, colour="ink", width=1.8, hatch=0, hatch_dir=1):
        """A rectangle, plain or hatched: a block, a slab, a wall, a ceiling.

        Rotation is given in degrees so an incline's block can be laid flat ON the slope by reusing
        the slope's own angle -- which is also the only way the two can be guaranteed to agree.

        PLAIN BY DEFAULT in this copy, and `hatch: true` means the standard 7-unit spacing. The pilot
        hatched every block at spacing 7, so plain boxes (2017_A q36's blocks A and B) came out
        hatched; and `"hatch": true` reached the arithmetic as 1, a hatch every unit -- q11's slabs
        rendered solid black. `hatch_dir` -1 slants the other way (q11 hatches its rods opposite
        ways). The hatching is CLIPPED to the box, so no line runs past its edge.
        """
        if hatch is True:
            hatch = 7
        hatch = float(hatch or 0)
        cx, cy = centre
        rad = math.radians(deg)
        ux, uy = math.cos(rad), math.sin(rad)
        nx, ny = -uy, ux
        corner = [(cx + ux * w / 2 + nx * h / 2, cy + uy * w / 2 + ny * h / 2),
                  (cx + ux * w / 2 - nx * h / 2, cy + uy * w / 2 - ny * h / 2),
                  (cx - ux * w / 2 - nx * h / 2, cy - uy * w / 2 - ny * h / 2),
                  (cx - ux * w / 2 + nx * h / 2, cy - uy * w / 2 + ny * h / 2)]
        self.polygon(corner, colour=colour, width=width)
        if hatch <= 0:
            return
        # 45-degree lines CLIPPED TO THE BOX BY ARITHMETIC, not by an SVG clipPath: a clip path is
        # ignored by some renderers and then every hatch line runs the full canvas -- q011's two
        # hatched rods became one hatched wall over the whole figure. In the box's own frame a line
        # is u = k + t*dir, v = t; it is cut to |u| <= w/2, |v| <= h/2.
        d = 1.0 if hatch_dir >= 0 else -1.0
        step = hatch * 1.414
        k = -(w + h)
        while k <= w + h:
            t1, t2 = (-w / 2 - k) / d, (w / 2 - k) / d
            lo, hi = max(-h / 2, min(t1, t2)), min(h / 2, max(t1, t2))
            if hi - lo > 0.2:
                ends = []
                for t in (lo, hi):
                    u, v = k + t * d, t
                    ends.append((cx + ux * u + nx * v, cy + uy * u + ny * v))
                self.body.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.9"/>'
                                 % (self.x(ends[0][0]), self.y(ends[0][1]), self.x(ends[1][0]),
                                    self.y(ends[1][1]), INK[colour]))
            k += step

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
    "capacitor": ("from", "to"), "battery": ("from", "to"), "inductor": ("from", "to"),
    "switch": ("from", "to"), "spring": ("from", "to"),
}
#: Components that join two circuit nodes -- the ones a netlist names. `id` on the item ties the
#: drawn component to its netlist entry; `meta` keys never reach the drawing.
TWO_TERMINAL = ("resistor", "capacitor", "battery", "inductor", "switch", "diode")
META_KEYS = ("id",)


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
        args = {k: v for k, v in item.items() if k != "kind" and k not in META_KEYS}
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
        elif kind in ("capacitor", "battery", "inductor", "switch", "spring"):
            getattr(canvas, kind)(args.pop("from"), args.pop("to"), **args)
    return canvas.svg(spec.get("title", ""))


#: How close two drawn points must be to count as the same circuit node, in spec units.
NODE_TOL = 1.5
#: How far a claimed angle may sit from the drawn one before it is a contradiction, in degrees.
ANGLE_TOL = 1.5


def _angle_at(vertex, a, b):
    ax, ay = a[0] - vertex[0], a[1] - vertex[1]
    bx, by = b[0] - vertex[0], b[1] - vertex[1]
    cos = (ax * bx + ay * by) / ((math.hypot(ax, ay) * math.hypot(bx, by)) or 1.0)
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))


def _on_segment(p, a, b, tol=NODE_TOL):
    """Does point p lie on segment a-b (a T-junction)?"""
    length = math.hypot(b[0] - a[0], b[1] - a[1])
    if length < 1e-9:
        return math.hypot(p[0] - a[0], p[1] - a[1]) <= tol
    t = ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / length ** 2
    if t < -0.01 or t > 1.01:
        return False
    px, py = a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])
    return math.hypot(p[0] - px, p[1] - py) <= tol


def drawn_netlist(spec):
    """{component id: frozenset of the two node numbers it joins}, derived from the DRAWING.

    Nodes are found with union-find over every wire (`line`) and every terminal point: two points
    within NODE_TOL are one node, a wire joins its ends, and a point lying ON a wire joins that
    wire (a T-junction). A component then connects the nodes its two ends fall in. This is the
    connectivity a reader would see -- the thing a declared netlist must agree with.
    """
    points, wires, comps = [], [], []
    for item in spec.get("draw") or []:
        if item.get("kind") == "line":
            wires.append((tuple(item["from"]), tuple(item["to"])))
        elif item.get("kind") in TWO_TERMINAL and item.get("id"):
            comps.append((item["id"], tuple(item["from"]), tuple(item["to"])))
    for a, b in wires:
        points += [a, b]
    for _id, a, b in comps:
        points += [a, b]
    parent = list(range(len(points)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        parent[find(i)] = find(j)

    for i, p in enumerate(points):
        for j in range(i):
            if math.hypot(p[0] - points[j][0], p[1] - points[j][1]) <= NODE_TOL:
                union(i, j)
    for k, (a, b) in enumerate(wires):
        union(points.index(a), points.index(b))
        for i, p in enumerate(points):
            if _on_segment(p, a, b):
                union(i, points.index(a))
    out = {}
    for comp_id, a, b in comps:
        out[comp_id] = frozenset((find(points.index(a)), find(points.index(b))))
    return out


def netlist_matches(declared, drawn):
    """Is there ONE renaming of the declared node names onto the drawn nodes that makes every
    component join the same pair? Backtracking over components; circuits here are small."""
    comps = [c for c in declared if c.get("id") in drawn]
    missing = [c.get("id") for c in declared if c.get("id") not in drawn]
    if missing:
        return False, "netlist names %s but the drawing has no component with that id" % missing
    def solve(i, mapping):
        if i == len(comps):
            return True
        names = comps[i]["between"]
        target = sorted(drawn[comps[i]["id"]])
        if len(target) == 1:
            target = target * 2
        for x, y in ((target[0], target[1]), (target[1], target[0])):
            trial = dict(mapping)
            ok = True
            for name, node in ((names[0], x), (names[1], y)):
                if trial.get(name, node) != node or (name not in trial and node in trial.values()):
                    ok = False
                    break
                trial[name] = node
            if ok and solve(i + 1, trial):
                return True
        return False
    if solve(0, {}):
        return True, "ok"
    return False, ("the wires as drawn do not join the components the way the netlist says -- a "
                   "wire ends on the wrong node or two nodes are drawn merged")


def check_spec(spec):
    """[problem, ...]: the spec renders, every claimed angle is the drawn angle, the netlist holds."""
    problems = []
    try:
        render(spec)
    except (ValueError, KeyError, TypeError) as exc:
        return ["does not render: %s" % exc]
    for claim in spec.get("angles_claimed") or []:
        try:
            drawn = _angle_at(claim["vertex"], claim["ray_to"], claim["measured_from"])
        except (KeyError, TypeError):
            problems.append("angle claim needs vertex, ray_to and measured_from: %s" % claim)
            continue
        if abs(drawn - float(claim["degrees"])) > ANGLE_TOL:
            problems.append("an angle labelled %s degrees is drawn at %.1f degrees -- compute the "
                            "endpoint from the angle, never estimate it" % (claim["degrees"], drawn))
    if spec.get("netlist"):
        ok, message = netlist_matches(spec["netlist"], drawn_netlist(spec))
        if not ok:
            problems.append(message)
    return problems


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
