"""The booklet's own figure as clean vector lines, traced from a picture-printed page.

WHY. On a vector booklet (2017_A, 2018_AA) the pipeline's drawing is made from the publisher's own
paths (lib/print_trace.py), so the panel under each printed figure looks exactly like the print. A
picture-printed booklet (2016) has no paths: its figures are embedded images. Tracing the printed
picture with Potrace gives the same thing -- the publisher's figure, as scalable vector outlines --
so those booklets get the same "drawn on the booklet's own geometry" panel instead of a drawing in
RDKit's or the spec renderer's own style (2016_A q063's condensed H2N-CH(R)-COOH came out skeletal,
q034's gates floated off their wires).

HOW. The PNG crop is upscaled UPSCALE times (thin subscripts and dotted boxes survive the trace),
thresholded at THRESHOLD, traced, and written as one even-odd filled path at the crop's own size.
"""

import numpy as np
from PIL import Image

#: Upscaling before the trace keeps subscripts, primes and dotted lines from eroding.
UPSCALE = 3
#: Grey level (0-255) below which a pixel is ink; 170 keeps the printed stroke weight.
THRESHOLD = 170
#: Specks smaller than this many (upscaled) pixels are scan noise, not ink.
TURD_SIZE = 3


def trace_svg(png_path):
    """SVG text of the printed figure in `png_path`, traced to vector outlines; None if no ink."""
    import potrace                                              # potracer (pure-Python Potrace)
    grey = Image.open(png_path).convert("L")
    big = grey.resize((grey.width * UPSCALE, grey.height * UPSCALE), Image.LANCZOS)
    # potracer traces the regions that are False; ink is below the threshold
    bitmap = potrace.Bitmap(np.asarray(big) >= THRESHOLD)
    path = bitmap.trace(turdsize=TURD_SIZE, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,
                        alphamax=1.0, opticurve=True, opttolerance=0.2)
    parts = []
    for curve in path:
        start = curve.start_point
        d = ["M%.1f,%.1f" % (start.x, start.y)]
        for seg in curve:
            if seg.is_corner:
                d.append("L%.1f,%.1fL%.1f,%.1f" % (seg.c.x, seg.c.y, seg.end_point.x, seg.end_point.y))
            else:
                d.append("C%.1f,%.1f %.1f,%.1f %.1f,%.1f" % (seg.c1.x, seg.c1.y, seg.c2.x, seg.c2.y,
                                                          seg.end_point.x, seg.end_point.y))
        d.append("z")
        parts.append("".join(d))
    if not parts:
        return None
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
            '<rect width="100%%" height="100%%" fill="#fff"/>'
            '<path fill="#000" fill-rule="evenodd" d="%s"/></svg>'
            % (grey.width, grey.height, big.width, big.height, "".join(parts)))
