"""Sanitizes the known answer/solution overlay contamination found in this project's scraped
paper PDFs (neet.training / vedantu.com sources — see docs/MASTER_PLAN.md Section 2.1.1).

Confirmed real structure (inspected directly, not assumed): every question renders as its own
card -- stem, 4 options, then a "Hide solution" toggle, then a separate "CORRECT ANSWER: X"
block with a worked explanation, before the next question's number begins. The text layer
preserves this same ordering and boundary markers verbatim, making it reliably machine-parseable.
The correct option is ALSO visually marked in the page image itself (a green border + checkmark
on that one option, not a text change) -- a risk B3/B4 (which read the image) and especially B6
(the blind solver, whose entire value depends on not seeing the answer) must be defended against
separately from the text-layer fix, since removing text doesn't touch image-level color coding.

Two fixes were tried; only one is fully solved -- read both entries before relying on this module:

1. `strip_overlay_text` -- SOLVED, validated against 4 real papers spanning 2017/2020/2023/2025
   (see docs/OPEN_QUESTIONS.md, 2026-10-10 entry): removes the "Hide solution ... CORRECT
   ANSWER: ... <explanation>" span from extracted TEXT. Overlay-blocks-stripped matched the
   paper's real question count almost exactly on every paper tested (180/180, 180/180, 179/180).
   All 4 papers also had ~100% real text-layer coverage (0-4 pages out of 94-171 lacked one), so
   **the text layer should be B1-B6's PRIMARY source whenever it exists** -- this single fix
   removes the contamination for the large majority of real content.

2. `render_sanitized_crop` -- PARTIAL, and confirmed NOT sufficient on its own: grayscale removes
   the color (green background) marking the correct option, but the CHECKMARK ICON next to that
   option is a distinct shape, not a color, and remains clearly visible in a real rendered sample
   even after grayscale conversion. A vision agent reading the image can still identify the
   "correct" option by the icon alone. **Do not treat a grayscale crop as a safe B6 input by
   itself.** Use it only as a last resort when no text layer exists for a question, and treat the
   residual checkmark-visibility as a known, unresolved risk in that fallback path, not as fixed.
   A real fix (icon-region detection + masking, or hand-cropping bypassing the options row
   entirely) was not attempted here -- out of scope for this pass.
"""
import re

_OVERLAY_RE = re.compile(
    r"Hide solution\s*\nCORRECT ANSWER:\s*[A-Za-z]?\s*\n.*?(?=\n\d+\n|\Z)",
    re.DOTALL,
)


def strip_overlay_text(raw_text):
    """Remove every 'Hide solution ... CORRECT ANSWER: ... <explanation>' span from `raw_text`.

    Returns (clean_text, n_removed) -- n_removed is how many overlay blocks were found and cut,
    so a caller can confirm the expected number of questions on a page actually had their overlay
    stripped (e.g. flag a page where 0 were found despite questions being present, which would
    mean the known marker pattern didn't match and the page needs a different handling path
    rather than silently passing contaminated text through)."""
    if not raw_text:
        return raw_text, 0
    matches = list(_OVERLAY_RE.finditer(raw_text))
    clean = _OVERLAY_RE.sub("", raw_text)
    return clean, len(matches)


def render_sanitized_crop(pdf_path, page_num, bbox=None, out_path=None, dpi=200):
    """Render a page (or a bbox region of it, in PDF points) to a GRAYSCALE PNG, removing any
    color-coded answer-highlight before a vision agent (especially B6) ever sees the image.
    `bbox` is (x0, y0, x1, y1) in PDF points, or None for the whole page. Requires PyMuPDF."""
    import fitz
    doc = fitz.open(pdf_path)
    try:
        page = doc[page_num - 1]
        clip = fitz.Rect(*bbox) if bbox else None
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csGRAY)
        if out_path:
            pix.save(out_path)
        return out_path or pix.tobytes("png")
    finally:
        doc.close()
