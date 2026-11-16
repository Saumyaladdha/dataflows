#!/usr/bin/env python3
"""Turn one D13 decision into the HTML that goes under a solution.

FOUR DECISIONS, THREE RENDERERS
-------------------------------
    annotate      the real image, with an SVG overlay of arrows and labels
    ncert_figure  the book's own figure, with the book's own caption
    draw          a schematic, drawn by the project's own render_figure
    none          nothing

EVERY NUMBER IS A PERCENTAGE, which is what makes `annotate` survive being resized. The
overlay is an SVG with `viewBox="0 0 100 100"` and `preserveAspectRatio="none"` laid exactly
over the image, so a mark at x=22 sits 22% across whatever width the card happens to be. The
alternative -- pixel coordinates against the stored image size -- breaks the moment the page
is read on a narrower screen, which is where these are read.

THE SPEC IS CHECKED BEFORE IT IS DRAWN. An agent that puts a coordinate at 140, names an
image that was not in its packet, or asks for a shape kind that does not exist gets its
figure dropped and counted, rather than rendering something misleading. A wrong diagram is
worse than no diagram.
"""

import html
import os
import re
import sys

#: THE DRAWINGS GO THROUGH THE PROJECT'S OWN RENDERER, NOT A NEW ONE.
#: The first version of this file carried a hand-rolled primitive set -- box, ellipse, line,
#: text -- and the drawings it produced were poor: a curling leaf had to be built from two
#: straight lines and read as an open-topped box. `ncert_extractions/code/render_figure.py`
#: already draws the physics figures in this project and is far richer: smooth curves with
#: tension and fill, rotated ellipses, polygons, dots, angles, labels that understand
#: subscripts, a named colour palette and arrowheads. It also refuses a spec written against
#: primitives it does not have, instead of half-drawing it. Biology uses that, so there is one
#: drawing vocabulary in the repo rather than two.
_RF = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "ncert_extractions", "code")
if _RF not in sys.path:
    sys.path.insert(0, _RF)
try:
    import render_figure as rf
except Exception:                                    # the page still builds without drawings
    rf = None

CSS = """
.sd{margin:14px 0 0;padding:13px 15px;background:#fff;border:1px solid #dfe8e3;border-radius:5px}
.sd .sd-h{font:700 10px -apple-system,sans-serif;letter-spacing:.07em;text-transform:uppercase;
 color:#5f7a6c;margin-bottom:9px}
.sd figure{margin:0}
.sd .sd-stack{position:relative;display:inline-block;max-width:100%}
.sd .sd-stack img{display:block;max-width:100%;height:auto;border-radius:3px}
.sd .sd-stack svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.sd figcaption{margin-top:8px;font:13px/1.55 Georgia,"Times New Roman",serif;color:#44564d}
.sd .sd-src{display:block;margin-top:4px;font:10px ui-monospace,Menlo,monospace;color:#8a968f}
.sd .sd-fig{overflow-x:auto}
.sd .sd-fig svg{display:block;max-width:100%;height:auto;background:#fff}
.sd .sd-pin{position:absolute;transform:translate(-50%,-50%);width:17px;height:17px;
 border-radius:50%;background:#b8492f;color:#fff;font:700 10px/17px -apple-system,sans-serif;
 text-align:center;box-shadow:0 0 0 2px #fff}
.sd .sd-legend{margin:10px 0 0;padding:0;list-style:none;counter-reset:none}
.sd .sd-legend li{display:flex;gap:8px;align-items:flex-start;padding:3px 0;
 font:13px/1.55 -apple-system,sans-serif;color:#33443c}
.sd .sd-legend b{flex:0 0 auto;width:17px;height:17px;border-radius:50%;background:#b8492f;
 color:#fff;font:700 10px/17px -apple-system,sans-serif;text-align:center}
.sd .sd-bad{font:12px -apple-system,sans-serif;color:#8a2318}
"""


def _n(v, lo=0.0, hi=100.0):
    """A coordinate, or None if it is not a number inside the canvas."""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f if lo <= f <= hi else None


#: Width of one character as a fraction of the label's font size. Measured off the renderer's
#: own serif output, and deliberately a little generous: a checker that under-estimates width
#: passes the overlaps it exists to catch.
_CHAR_W = 0.52


def _label_box(item):
    """(x0, y0, x1, y1) for a label, in the spec's own y-up frame."""
    size = float(item.get("size", 15))
    text = str(item.get("text") or "")
    w = _CHAR_W * size * max(len(text), 1)
    x, y = float(item["at"][0]), float(item["at"][1])
    anchor = item.get("anchor", "middle")
    x0 = x - w / 2.0 if anchor == "middle" else (x if anchor == "start" else x - w)
    return (x0, y - size * 0.36, x0 + w, y + size * 0.72)


def layout_problems(spec):
    """Labels that collide with each other, or fall off the canvas.

    WHY A CHECKER AND NOT BETTER INSTRUCTIONS. The agent places text by coordinate and cannot
    know how wide the rendered string will be, so "leave room between rows" is advice it has
    no way to follow reliably. The first drawings showed exactly that: "glycerol" printed
    through "3 fatty acids", "anal cerci" through "a pair of jointed filaments, in both
    sexes", and "counted back from the thorax" running off the left edge with its first
    letter cut away. None of it is visible in the JSON; all of it is arithmetic.

    So the geometry is measured here and the offending pairs are named, which is what lets a
    re-run fix the actual problem instead of nudging numbers blindly.
    """
    out = []
    labels = [i for i in (spec.get("draw") or [])
              if i.get("kind") == "label" and isinstance(i.get("at"), (list, tuple))
              and len(i["at"]) == 2]
    W, H = float(spec.get("width", 0)), float(spec.get("height", 0))
    boxes = []
    for item in labels:
        # A LABEL THAT CANNOT BE MEASURED IS REPORTED, NOT SKIPPED. The first version of this
        # checker swallowed the exception and moved on, and so passed a spec whose every
        # label carried `size: "normal"` -- a token from a superseded vocabulary. The renderer
        # does not validate it either; it writes `font-size="normal"`, the browser ignores it,
        # and the drawing comes out with the wrong type sizes and overlapping text while the
        # checker reports no problems at all. Silence has to mean measured, not unmeasurable.
        try:
            box = _label_box(item)
        except (TypeError, ValueError, IndexError):
            out.append('label "%s" has size %r -- it must be a NUMBER (the renderer writes it '
                       'straight into font-size, so a word there is silently ignored)'
                       % (str(item.get("text") or "")[:40], item.get("size")))
            continue
        boxes.append((box, str(item.get("text") or "")[:40]))
        x0, y0, x1, y1 = box
        if x0 < 0 or x1 > W or y0 < 0 or y1 > H:
            out.append('"%s" falls outside the %gx%g canvas (it spans x %.0f..%.0f, y %.0f..%.0f)'
                       % (item.get("text"), W, H, x0, x1, y0, y1))
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (ax0, ay0, ax1, ay1), at = boxes[i]
            (bx0, by0, bx1, by1), bt = boxes[j]
            if ax0 < bx1 and bx0 < ax1 and ay0 < by1 and by0 < ay1:
                out.append('"%s" overlaps "%s"' % (at, bt))
    return out


def check(d13, allowed_images):
    """Return a list of reasons this spec cannot be drawn. Empty list means it is fine."""
    bad = []
    dec = d13.get("decision")
    if dec not in ("annotate", "ncert_figure", "draw", "none"):
        return ["decision %r is not one of the four" % dec]
    if dec == "annotate":
        a = d13.get("annotate") or {}
        if a.get("image") not in allowed_images:
            bad.append("annotates an image that was not in its packet")
        marks = a.get("marks") or []
        if not marks:
            bad.append("annotate with no marks")
        for i, m in enumerate(marks):
            if _n(m.get("x")) is None or _n(m.get("y")) is None:
                bad.append("mark %d is outside 0-100" % i)
            if not (m.get("text") or "").strip():
                bad.append("mark %d has no text" % i)
    if dec == "ncert_figure":
        f = d13.get("ncert_figure") or {}
        if f.get("url") not in allowed_images:
            bad.append("names an NCERT figure that was not in its packet")
    if dec == "draw":
        spec = d13.get("draw") or {}
        if not (spec.get("draw") or []):
            bad.append("draw with no shapes")
        elif rf is None:
            bad.append("render_figure is not importable")
        else:
            # THE RENDERER IS THE CHECKER. It already refuses an unknown primitive and a
            # primitive missing a required key, with a message naming both -- so asking it
            # to draw is a stricter test than any list of keys kept in step with it here.
            try:
                rf.render(spec)
            except Exception as exc:
                bad.append("renderer refused it: %s" % exc)
            bad += layout_problems(spec)
    return bad


def _esc(s):
    return html.escape(str(s or ""))


def _overlay(marks):
    """Numbered pins over the image, with the wording in a legend underneath.

    THE LABELS USED TO SIT ON THE PICTURE AND COLLIDED. Three marks on one muscle-tissue
    figure produced "striated, unbrar" truncated under "striated AND branched = cardiac",
    both printed across the tissue they were pointing at. There is no arrangement of
    free-floating text that is safe here: the agent cannot know how wide a rendered string
    will be, and the image is only a few hundred pixels across.

    So the image carries only a numbered pin and its arrow, and the words go in an ordered
    legend below it. Collisions become impossible, the diagram stays visible, and the text
    can be as long as the explanation needs.

    THE PIN IS AN HTML ELEMENT, NOT AN SVG CIRCLE. The arrow layer is stretched to the
    image's box with preserveAspectRatio="none", which squashes any circle drawn inside it
    into an ellipse. A positioned <b> stays round at any aspect ratio.
    """
    arrows = ['<svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">',
              '<defs><marker id="sdar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" '
              'markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#b8492f"/>'
              '</marker></defs>']
    pins = []
    for i, m in enumerate(marks, 1):
        x, y = _n(m.get("x")), _n(m.get("y"))
        tx, ty = _n(m.get("to_x")), _n(m.get("to_y"))
        if tx is not None and ty is not None:
            arrows.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#b8492f" '
                          'stroke-width="2" marker-end="url(#sdar)" '
                          'vector-effect="non-scaling-stroke" stroke-linecap="round"/>'
                          % (x, y, tx, ty))
        pins.append('<b class="sd-pin" style="left:%.2f%%;top:%.2f%%">%d</b>' % (x, y, i))
    arrows.append('</svg>')
    return "".join(arrows) + "".join(pins)


def _legend(marks):
    return ('<ol class="sd-legend">%s</ol>'
            % "".join('<li><b>%d</b><span>%s</span></li>' % (i, _esc(m.get("text")))
                      for i, m in enumerate(marks, 1)))


def _draw(spec):
    """One SVG from the project's figure renderer. Its own y-axis points up."""
    return '<div class="sd-fig">%s</div>' % rf.render(spec)


def source_line(key, meta):
    """Where this picture came from, in words a teacher can check.

    EVERY FIGURE ON THE PAGE SAYS ITS SOURCE. An NCERT figure names the book, the chapter and
    the printed page it was lifted from, and quotes the book's own caption; a marked booklet
    diagram says it is the booklet's; a drawing says it was drawn for this solution, so nobody
    mistakes it for something NCERT printed. The point is that a reader can always tell what
    is the book's and what is ours.
    """
    m = meta.get(key) or {}
    if m.get("chapter"):
        ch = re.match(r'([A-Z]+)(\d+)([LO])-CH(\d+)', m["chapter"])
        where = m["chapter"]
        if ch:
            subj = {"BIO": "Biology", "PHY": "Physics", "CHE": "Chemistry"}.get(ch.group(1),
                                                                                ch.group(1))
            roman = {"11": "XI", "12": "XII"}.get(ch.group(2), ch.group(2))
            where = "NCERT Class %s %s, Chapter %d" % (roman, subj, int(ch.group(4)))
            if ch.group(3) == "O":
                where += " (previous edition)"
        page = (", printed page %s" % m["printed_page"]) if m.get("printed_page") else ""
        return "%s%s" % (where, page)
    if m.get("from_booklet"):
        return "the diagram printed with this question in the booklet"
    return ""


def render(d13, allowed_images, image_src, meta=None):
    """(html, status). `image_src` maps a packet path/url to what the page should load."""
    meta = meta or {}
    if not d13 or d13.get("decision") == "none":
        return "", "none"
    bad = check(d13, allowed_images)
    if bad:
        return "", "spec rejected: " + "; ".join(bad[:2])

    dec = d13["decision"]
    cap = _esc(d13.get("caption"))
    if dec == "draw":
        body = _draw(d13.get("draw") or {})
        head = "Drawn for this solution"
        src = ('<span class="sd-src">Drawn for this solution from the NCERT lines quoted above '
               '&mdash; it is not a figure NCERT prints.</span>')
    else:
        if dec == "annotate":
            key = (d13.get("annotate") or {}).get("image")
            body = ('<span class="sd-stack"><img src="%s" alt="%s" loading="lazy">%s</span>'
                    % (_esc(image_src.get(key, key)), cap or "diagram",
                       _overlay((d13["annotate"].get("marks") or []))))
            body += _legend(d13["annotate"].get("marks") or [])
            head = "Marked on the printed diagram"
            where = source_line(key, meta)
            src = ('<span class="sd-src">Marks added by this pipeline &middot; %s</span>'
                   % _esc(where)) if where else ""
        else:
            f = d13.get("ncert_figure") or {}
            body = ('<span class="sd-stack"><img src="%s" alt="%s" loading="lazy"></span>'
                    % (_esc(image_src.get(f.get("url"), f.get("url"))), _esc(f.get("caption"))))
            head = "From the NCERT chapter"
            cap = cap or _esc(f.get("caption"))
            where = source_line(f.get("url"), meta)
            src = ('<span class="sd-src">%s%s</span>'
                   % (_esc(f.get("caption")), (" &middot; " + _esc(where)) if where else ""))
    return ('<div class="sd"><div class="sd-h">%s</div><figure>%s'
            '<figcaption>%s%s</figcaption></figure></div>'
            % (head, body, cap, src)), dec
