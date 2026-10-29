"""PDF handling: rendering pages to PNG, reading the embedded text layer (page-wide or inside a
box), and cropping boxes to images. Built on PyMuPDF (`fitz`), the only third-party dependency
in M1 — picked because it renders, extracts text and crops regions natively with no external
binary (unlike pdfplumber/pdf2image, which lean on poppler/ghostscript), and because the real
NCERT PDFs in this project need exactly these three operations. Install: `pip install pymupdf`.

A real check against this project's own PDFs (inputs/ncert/latest/Class_12th/Biology/) confirmed
several chapters are 100% image-only with zero extractable text, so `extract_text_layer` and
`extract_text_in_box` must return "" gracefully for those pages rather than raising.
"""
import pymupdf as fitz  # PyMuPDF; "pymupdf" is the current import name, "fitz" is deprecated

from . import io as lib_io

DEFAULT_DPI = 200


def _open(pdf_path):
    return fitz.open(pdf_path)


def _get_page(doc, page_num):
    """page_num is 1-indexed, matching how the spec refers to pages ("pages 1-6", "one page")."""
    return doc[page_num - 1]


def _px_bbox_to_rect(bbox, dpi):
    """Convert a pixel bounding box, as measured on a page image rendered at `dpi`, into a
    fitz.Rect in native PDF points (72 points/inch) — the unit PyMuPDF's clip boxes use."""
    scale = 72.0 / dpi
    x0, y0, x1, y1 = bbox
    return fitz.Rect(x0 * scale, y0 * scale, x1 * scale, y1 * scale)


def _bbox_to_rect(bbox, dpi, unit):
    """bbox is (x0, y0, x1, y1). unit='px' (default) means pixels at `dpi`, matching the boxes a
    vision agent returns after looking at a page PNG rendered by render_page_to_png; unit='pt'
    means native PDF points directly."""
    if unit == "pt":
        return fitz.Rect(*bbox)
    if unit == "px":
        return _px_bbox_to_rect(bbox, dpi)
    raise ValueError(f"unknown unit {unit!r}; expected 'px' or 'pt'")


def page_count(pdf_path):
    """Return the number of pages in the PDF."""
    with _open(pdf_path) as doc:
        return doc.page_count


def render_page_to_png(pdf_path, page_num, dpi=DEFAULT_DPI, out_path=None):
    """Render one page (1-indexed) to a PNG at `dpi` and save it atomically to `out_path`.
    Returns `out_path`."""
    if not out_path:
        raise ValueError("out_path is required")
    with _open(pdf_path) as doc:
        page = _get_page(doc, page_num)
        pix = page.get_pixmap(dpi=dpi)
        data = pix.tobytes("png")
    lib_io.atomic_write_bytes(out_path, data)
    return out_path


def extract_text_layer(pdf_path, page_num):
    """Return the embedded text layer of one page (1-indexed), or "" if the page has no
    extractable text (an image-only scan) or anything goes wrong reading it. Never raises —
    several real chapters in this project are 100% image-only and must be handled, not crash."""
    try:
        with _open(pdf_path) as doc:
            page = _get_page(doc, page_num)
            return page.get_text() or ""
    except Exception:
        return ""


def extract_text_in_box(pdf_path, page_num, bbox, dpi=DEFAULT_DPI, unit="px"):
    """Return the embedded text inside a bounding box on one page (1-indexed); bbox defaults to
    pixel coordinates measured on a page image rendered at `dpi` (pass unit='pt' for native PDF
    points instead). Returns "" if the box is empty, the page has no text layer, or anything
    goes wrong — used for B2-style question-boundary cropping where a question may be scanned
    with no text layer at all."""
    try:
        with _open(pdf_path) as doc:
            page = _get_page(doc, page_num)
            rect = _bbox_to_rect(bbox, dpi, unit)
            return page.get_text("text", clip=rect) or ""
    except Exception:
        return ""


def blank_marks(page, marks):
    """Remove repeated VECTOR furniture from one in-memory page: `marks` = [(rect, fill), ...] as
    extract_paper_v2.document_vector_marks() measured them. Removed only when every drawing wholly
    inside the mark's box is the mark itself (that fill), so real line art there is never touched.
    Returns how many were removed."""
    import pymupdf
    removed = 0
    for rect, fill in marks:
        box = pymupdf.Rect(rect) + (-0.5, -0.5, 0.5, 0.5)
        inside = [d for d in page.get_drawings() if box.contains(d["rect"])]
        if not inside or any(tuple(round(c, 2) for c in (d.get("fill") or ())) != fill
                             for d in inside):
            continue
        page.add_redact_annot(box, fill=False)
        removed += 1
    if removed:
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                              text=pymupdf.PDF_REDACT_TEXT_NONE)
    return removed


def crop_boxes(pdf_path, jobs, dpi=DEFAULT_DPI, unit="px", hide_xrefs=(), hide_marks=None):
    """Render MANY crops out of one PDF with a single open. Returns the list of paths written.

    `jobs` is an iterable of (page_num, bbox, out_path), page numbers 1-indexed, exactly as
    `crop_box` takes them one at a time.

    WHY THIS EXISTS. `crop_box` opens the document, renders, and closes, which is right for one
    crop and badly wrong for a few thousand. Cutting one NEET booklet produces ~200 question crops
    plus its figures; three years of every booklet code is ~13,000 crops, and at one open of a
    70-to-85-page PDF per crop the pass does not finish in a usable time. Measured during the v2
    paper extraction: the per-crop version was still inside its first booklet after three minutes
    at full CPU.

    The behaviour is otherwise identical, including the atomic write, so a caller can switch
    between the two without changing anything else.
    """
    written, skipped = [], []
    with _open(pdf_path) as doc:
        # PAGE FURNITURE IS BLANKED BEFORE ANYTHING IS RENDERED. `hide_xrefs` are the images the
        # caller measured as repeating on most pages (extract_paper_v2.document_furniture): the
        # coaching watermark, a logo, a page-sized background. Every crop used to carry the pink
        # wash -- 2017 Code-A q008's circuit crop had it across its lower half. Blanked by XREF in
        # this in-memory copy only (the source file is never written), so a real raster figure,
        # which is never repeated across pages, is untouched even where the watermark covers it.
        hidden = set()
        for xref in hide_xrefs or ():
            for page in doc:
                if any(item[0] == xref for item in page.get_images(full=True)):
                    page.delete_image(xref)
                    hidden.add(xref)
                    break
        # ...and the publisher's VECTOR marks, {page index: [(rect, fill)]}: 2019 Code-P1 prints a
        # pale-grey "ed)" at one spot on four pages, and q078's option crop carried it
        for index, marks in (hide_marks or {}).items():
            blank_marks(doc[index], marks)
        for page_num, bbox, out_path in jobs:
            if not out_path:
                raise ValueError("out_path is required")
            page = _get_page(doc, page_num)
            rect = _bbox_to_rect(bbox, dpi, unit)
            # CLIP TO THE PAGE, and skip a box that leaves nothing. A box whose intersection with
            # the page is empty -- because it was measured in another coordinate space, or runs off
            # the edge -- makes PyMuPDF raise `FzErrorArgument: Invalid bandwriter header
            # dimensions` from inside the PNG writer. In a batch of several hundred crops that one
            # box used to abort every crop after it, which is how 2015_A ended up missing figures
            # for three questions whose reads all say `has_figure: true`.
            rect = rect & page.rect
            if rect.is_empty or rect.width < 1 or rect.height < 1:
                skipped.append((page_num, tuple(bbox), out_path))
                continue
            data = page.get_pixmap(dpi=dpi, clip=rect).tobytes("png")
            lib_io.atomic_write_bytes(out_path, data)
            written.append(out_path)
    if skipped:
        # Printed, never silent: a crop that was asked for and not produced is a gap the caller has
        # to be able to see, and a count alone does not say which question lost its figure.
        print("crop_boxes: %d box(es) did not intersect their page and were skipped" % len(skipped))
        for page_num, bbox, out_path in skipped[:8]:
            print("   page %-4s %s -> %s" % (page_num, bbox, out_path.rsplit("/", 1)[-1]))
    return written


def crop_box(pdf_path, page_num, bbox, out_path, dpi=DEFAULT_DPI, unit="px"):
    """Render just the region inside bbox on one page (1-indexed) to a PNG at `dpi` and save it
    atomically to `out_path`. Returns `out_path`."""
    if not out_path:
        raise ValueError("out_path is required")
    with _open(pdf_path) as doc:
        page = _get_page(doc, page_num)
        rect = _bbox_to_rect(bbox, dpi, unit)
        pix = page.get_pixmap(dpi=dpi, clip=rect)
        data = pix.tobytes("png")
    lib_io.atomic_write_bytes(out_path, data)
    return out_path


if __name__ == "__main__":
    import os
    import tempfile

    sample = lib_io.project_path(
        "inputs", "ncert", "latest", "Class_12th", "Chemistry", "Chapter_1.pdf"
    )
    image_only_sample = lib_io.project_path(
        "inputs", "ncert", "latest", "Class_12th", "Biology", "Chapter_1.pdf"
    )

    if os.path.exists(sample):
        n = page_count(sample)
        assert n > 0
        tmp_dir = tempfile.mkdtemp(prefix="pdf_selfcheck_")
        png_path = os.path.join(tmp_dir, "p1.png")
        render_page_to_png(sample, 1, dpi=200, out_path=png_path)
        assert os.path.getsize(png_path) > 0

        text = extract_text_layer(sample, 1)
        assert len(text.strip()) > 0, "Chemistry Chapter 1 page 1 should have a text layer"

        crop_path = os.path.join(tmp_dir, "crop.png")
        crop_box(sample, 1, (0, 0, 400, 300), crop_path, dpi=200)
        assert os.path.getsize(crop_path) > 0

        box_text = extract_text_in_box(sample, 1, (0, 0, 10000, 10000), dpi=200)
        assert box_text.strip() != "", "full-page box should recover the same text layer"

        print(f"pdf.py self-check OK on {sample}: {n} pages, rendered {png_path}, "
              f"text layer {len(text)} chars, crop {crop_path}")
    else:
        print("pdf.py self-check SKIPPED: sample PDF not found at", sample)

    if os.path.exists(image_only_sample):
        empty_text = extract_text_layer(image_only_sample, 1)
        assert empty_text == "", "image-only chapter must return '' gracefully, not raise"
        print("pdf.py self-check OK: image-only chapter handled gracefully ->", repr(empty_text))
    else:
        print("pdf.py self-check SKIPPED (image-only sample not found):", image_only_sample)

    bad_text = extract_text_layer("/no/such/file.pdf", 1)
    assert bad_text == ""
    print("pdf.py self-check OK: missing file handled gracefully ->", repr(bad_text))
