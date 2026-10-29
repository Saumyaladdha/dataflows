"""The PRINTED DESIGN of each NCERT book: page grid, furniture, palette and type.

    from lib.ncert_design import design_for, normalise_page
    d = design_for("BIO11L")          # or "BIO12O", "CHE11L", "PHY11L" ...
    d.trim_pt                         # (612.0, 784.0) -- the canonical sheet
    d.text_box(page_side="verso")     # (x0, y0, x1, y1) in points on that sheet

Why this module exists, and why it is keyed the way it is
---------------------------------------------------------
`export_ncert_chapter_html.py` keys every layout constant off the chapter id's first three
letters -- `BIO`, `CHE`, `PHY` -- so `BIO11L` and `BIO12O` get the same page. Measured against
the source PDFs that is wrong in both directions:

  * Class 11 Biology and Class 12 Biology are DIFFERENT designs. Class 11 prints a pale-green
    header band closed by a grey strip, with the folio in a white tab on that strip and a green
    bar across the foot. Class 12 prints a dark-green top rule with a brown block on the outer
    end, a leaf motif, no footer bar, and the folio in an orange tab two-thirds of the way down
    the outer margin. Keying on `BIO` alone means one of the two is always rendered as the
    other.

  * The older and the latest edition of the SAME class are the SAME design. BIO11O ch3 and
    BIO11L ch3 measure identically -- band #e1ecb6 to y 0.0804, grey strip to 0.0934, footer
    #cbdf7f from 0.9585, folio tab 0.0572 x 0.0460 of the sheet -- and so do BIO12O ch7 and
    BIO12L ch6 (top rule #4b7336, brown block #745a21, hero #d3ead4, divider #f7941d). The
    editions differ in their CONTENT (chapters renumber, sections are removed) and in the
    imprint line at the foot; they do not differ in their typography.

So the design key is (SUBJECT, CLASS) and the edition selects only the imprint line. That is
what lets "generate the new NCERT too" be a data change rather than a second renderer.

The canonical sheet, and why pages must be normalised onto it
-------------------------------------------------------------
Measured over 20 chapter PDFs, every NCERT Biology book sets the SAME text block in absolute
points, on a 612 x 784pt sheet (215.9 x 276.6 mm):

    recto (odd folio)   body x  60.0 -> 420.0      inner margin  60pt
    verso (even folio)  body x 192.0 -> 552.0      outer margin 192pt (the marginal rail)
    measure                     360.0pt            identical on both

    Class 11 text top  y ~104pt, foot ~714pt
    Class 12 text top  y  ~88pt, foot ~715pt

The scans do NOT all carry that sheet. `inputs/ncert/latest/Class_12th/Biology/Chapter_*.pdf`
are 568.8 x 777.6pt, and their body text sits at x 38.4 / 170.4 -> 530.4. That is not a
different book: 60.0 - 38.4 = 21.6 and 612.0 - 568.8 = 43.2 = 2 x 21.6, i.e. the SAME page with
21.6pt trimmed off each side and 3.2pt off the head and foot. Rendering those pages at their own
page size is what makes the new Class 12 book come out narrower than Class 11 and narrower than
its own older edition -- three page sizes for one physical book. `normalise_page` measures the
offset off the page's own text block and puts every page back on the canonical sheet, so a
fraction means the same thing in every book.

Two chapters in that folder (Class_12th/Biology/Chapter_1.pdf and Chapter_11.pdf) are A4
595.3 x 841.9pt with NO text layer at all -- pure scans. They cannot be normalised by
measurement and are the A2L agent's job, not this module's; `normalise_page` says so rather
than guessing an offset.

Every number below was measured, and the measurement is named next to it. Nothing here is
chosen for looks.
"""

# --------------------------------------------------------------------------------------------
# The canonical sheet. 612 x 784pt = 8.5 x 10.889in = 215.9 x 276.6mm.
# Measured as the page size of 18 of the 20 Biology chapter PDFs sampled across both editions
# and both classes (the two exceptions are the textless A4 scans named in the docstring).
CANONICAL_TRIM_PT = (612.0, 784.0)

_PT_PER_IN = 72.0
_MM_PER_IN = 25.4


def pt_to_mm(v):
    return v / _PT_PER_IN * _MM_PER_IN


class Design:
    """One book's printed design. Read-only; built from the table below."""

    def __init__(self, key, **kw):
        self.key = key
        self.__dict__.update(kw)

    # ---- the text block -------------------------------------------------------------------
    def text_box(self, page_side):
        """(x0, y0, x1, y1) in points of the body text block on the canonical sheet.

        `page_side` is "recto" (odd printed folio, binding on the left, wide margin RIGHT) or
        "verso" (even folio, wide margin LEFT). NCERT mirrors the rail every page; a renderer
        that does not mirror puts body text in the margin on half the book.
        """
        W = self.trim_pt[0]
        inner, measure = self.inner_margin_pt, self.measure_pt
        if page_side == "verso":
            x0 = W - inner - measure
        else:
            x0 = inner
        return (x0, self.text_top_pt, x0 + measure, self.text_foot_pt)

    def rail_box(self, page_side):
        """(x0, x1) in points of the WIDE outer margin -- where marginal figures and the folio
        tab live. This is the half of the page the current exporter throws away."""
        W = self.trim_pt[0]
        x0, _, x1, _ = self.text_box(page_side)
        return (x1, W) if page_side == "recto" else (0.0, x0)

    def frac(self, x_pt=None, y_pt=None):
        """Point -> fraction of the canonical sheet, for CSS written in percentages."""
        W, H = self.trim_pt
        if x_pt is not None and y_pt is not None:
            return (x_pt / W, y_pt / H)
        return (x_pt / W) if x_pt is not None else (y_pt / H)

    def imprint(self, edition):
        """The line NCERT prints at the foot. This is the ONLY thing the edition changes.

        Measured: older Biology prints a bare `2022-23`; the latest Class 11 prints `2024-25`;
        the latest Class 12 prints `Reprint 2026-27`. The extractor reads the real string off
        the page -- this is the fallback for a page whose foot did not extract, and the value a
        reviewer compares against.
        """
        return self.imprint_by_edition.get(edition, self.imprint_by_edition.get("L", ""))

    def __repr__(self):
        return f"<Design {self.key} {self.trim_pt[0]:.0f}x{self.trim_pt[1]:.0f}pt>"


# ================================================================================================
# THE MEASURED TABLE.
#
# Keys are (SUBJECT, CLASS). Edition is deliberately NOT part of the key -- see the module
# docstring for the measurement that says the two editions share one design.
#
# Furniture geometry is in POINTS on the canonical sheet, converted from the fractions measured
# with `page.get_drawings()` on the real PDFs. The measurement command and the page it was taken
# from is named on each block so a future change can be checked rather than argued about.
# ================================================================================================

# THE CLASS 11 PHYSICS SHEET. Measured on every page of
# source_pdfs/new/class_11/physics/Chapter_1.pdf (657.35 x 777.07pt) and on the first page of
# Chapters 10-14 (657.0 x 777.4 to 781.6pt) -- 231.9 x 274.1mm. That is a WIDER and slightly
# shorter page than Biology's 612 x 784pt (215.9 x 276.6mm), and it is not a crop of it: the
# measure is 474pt against Biology's 360pt. Physics is a different physical book and carries
# its own trim rather than being normalised onto Biology's.
PHY11_TRIM_PT = (657.3, 777.1)

# THE CLASS 12 PHYSICS SHEET. Measured on every page of
# source_pdfs/new/class_12/physics/Chapter_1.pdf: 612.0 x 777.6pt. The same WIDTH as Biology
# (612) on a slightly shorter page (777.6 against 784), and nothing like Class 11 Physics'
# 657.3 x 777.1 -- the two Physics books are not one design. Chapters 10-14 of this book scan
# at 567.0 x 766.8, the same page trimmed, which `normalise_page` puts back on this sheet.
PHY12_TRIM_PT = (612.0, 777.6)

_BIO_COMMON = dict(
    trim_pt=CANONICAL_TRIM_PT,
    # Measured identical in every Biology chapter sampled, both classes, both editions:
    # recto body x 60.0 -> 420.0, verso 192.0 -> 552.0, measure 360.0pt on all of them.
    inner_margin_pt=60.0,
    measure_pt=360.0,
    # Body type. 10.5pt is the modal span size reported by PyMuPDF on every Biology chapter
    # (`body_text_size_pt` in ncert/layout/*.json). Leading measured off consecutive baselines.
    body_pt=10.5,
    leading=1.27,
    body_font='"Bookman Old Style", Bookman, "TeX Gyre Bonum", Georgia, serif',
    display_font='"Century Gothic", "TeX Gyre Adventor", "URW Gothic", Avenir, sans-serif',
    sans_font="Arial, Helvetica, sans-serif",
    ink="#231f20",          # measured run colour of body text on every Biology page
    # THE WATERMARK IS DETECTED BUT NEVER DRAWN (owner's instruction, 2026-10-22).
    # It is a fixed-position IMAGE on every page -- bbox 65.7,192.3 -> 530.6,657.1 on BIO11L ch3,
    # identical on all 14 pages -- so it still has to be RECOGNISED (`is_watermark` below), or a
    # figure cutter files "(c) NCERT / not to be republished" as artwork. Recognising it and
    # drawing it are different decisions: these renders are an internal reading aid, the
    # watermark adds nothing to them, and it sits directly over the body text. So the detector
    # stays and the render omits it. There is deliberately no colour or angle here to draw from.
    draw_watermark=False,
)

_DESIGNS = {
    # --------------------------------------------------------------------------------------
    # CLASS 11 BIOLOGY -- "the green band book".
    # Measured on inputs/ncert/latest/Class_11th/Biology/Chapter_3.pdf (Plant Kingdom) and
    # inputs/ncert/older/Class_11th/Biology/"4 3. Plant Kingdom.pdf". The two are identical to
    # four decimal places on every rectangle below; only the imprint line differs.
    # --------------------------------------------------------------------------------------
    ("BIO", "11"): dict(
        _BIO_COMMON,
        name="NCERT Biology, Class XI",
        # Text grid. MEASURED ACROSS 81 PAGES of this design, body text only (furniture
        # filtered): tops run 64-67pt, bottoms 713-729pt. The earlier 104 -> 714 was a MEDIAN
        # page, not the block -- a median page starts low because it opens under a heading.
        # Using it as the block made the text area 2.5 to 4 lines shorter than the book's on
        # every page, so `fit_factor` reported pages needing up to 142% and the renderer
        # shrank and then clipped them. The block runs from just under the grey header strip
        # (ends 73.1pt) to just above the foot band. See code/measure_text_block.py.
        text_top_pt=88.0,
        text_foot_pt=729.0,
        # --- header band: pale green to y 63, then a grey strip to y 73 ---------------------
        # get_drawings on p002: #e1ecb6 full width y -0.0244 -> 0.0804 ; #d1d3d4 y -> 0.0934.
        header_band=dict(fill="#e1ecb6", y0_pt=0.0, y1_pt=63.0),
        header_strip=dict(fill="#d1d3d4", y0_pt=63.0, y1_pt=73.1),
        # --- folio: a WHITE rounded tab sitting on the grey strip, in the outer margin ------
        # #ffffff w 0.0572 h 0.0460, y 0.0638 -> 0.1098 ; x recto 0.8137, verso 0.1275.
        folio=dict(style="tab", fill="#ffffff", ink="#231f20",
                   w_pt=35.0, h_pt=36.0, y0_pt=50.0,
                   x_recto_pt=498.0, x_verso_pt=78.0,
                   radius_pt=8.0, font="display", size_pt=13.0, weight=700,
                   # The tab is open at the bottom: it is a rounded notch hanging off the band.
                   radius_corners="top"),
        # --- running head: on the grey strip, OUTSIDE the folio -----------------------------
        # Measured bbox y 0.0819 -> 0.0960 (= 64.1 -> 75.1pt), i.e. on the strip.
        # verso prints the SUBJECT ("Biology"), recto the CHAPTER TITLE ("Plant Kingdom"):
        # read off BIO11L ch3 p002 ("24 Biology") and p007 ("Plant Kingdom 29").
        running_head=dict(y_pt=64.0, size_pt=11.0, smallcaps=True, ink="#231f20",
                          font="body", verso="subject", recto="chapter_title",
                          # sits at the INNER end of the strip, the folio taking the outer end
                          inset_pt=78.0),
        # --- foot: a green bar across the full width, imprint centred on it -----------------
        # #cbdf7f x 0.0008 -> 0.9992, y 0.9585 -> 1.0238 (bleeds off the foot).
        footer_bar=dict(fill="#cbdf7f", y0_pt=751.5),
        imprint=dict(y_pt=747.0, size_pt=8.0, font="sans", ink="#000000"),
        # --- the chapter-opening page -------------------------------------------------------
        # p001 carries a full-bleed gradient IMAGE over the band, running green -> white.
        # Sampled down the page: #cde084 at y0.01, #d5e597 at 0.09, white by ~0.44.
        opener=dict(
            kind="gradient",
            gradient=("#cbdf7f", "#e1ecb6", "#f6f8e8", "#ffffff"),
            gradient_stops_pt=(0.0, 150.0, 285.0, 345.0),
            # QR code, measured bbox 449.0,85.9 -> 534.0,170.9 (85 x 85pt, outer margin).
            qr=dict(x_recto_pt=449.0, x_verso_pt=78.0, y_pt=86.0, size_pt=85.0),
            # Title block: "CHAPTER n" then the title, small caps, in the accent blue.
            # bbox 0.3224 -> 0.5784 x, 0.3244 -> 0.4084 y on p001 => x 197pt, y 254 -> 320pt.
            title=dict(x_pt=197.0, y_pt=254.0, chapter_size_pt=20.0, title_size_pt=24.0,
                       ink="#1b75bb", smallcaps=True, font="body", weight=700,
                       line_gap_pt=22.0),
            # Contents rail: italic cyan, left column, measured x 0.098 -> 0.243 (60 -> 149pt),
            # first entry y 0.4518 (354pt), pitch 0.0271 of the page (21.2pt).
            contents=dict(x_pt=60.0, y_pt=354.0, width_pt=132.0, size_pt=10.0,
                          ink="#00a9d4", italic=True, pitch_pt=21.2, panel_fill=None),
            # The opening prose starts beside the rail, not under it.
            body_x_pt=173.5, body_top_pt=354.0,
        ),
        accent="#1b75bb",          # chapter title / section heading blue, measured on p001
        heading_ink="#00a9d4",     # x.y section headings, measured on p002 ("3.1 ALGAE")
        heading_size_rel=1.24,     # measured size_rel of a section heading against body
        imprint_by_edition={"O": "2022-23", "L": "2024-25"},
    ),

    # --------------------------------------------------------------------------------------
    # CLASS 12 BIOLOGY -- "the brown-and-green rule book".
    # Measured on inputs/ncert/latest/Class_12th/Biology/Chapter_6.pdf (Evolution) and
    # inputs/ncert/older/Class_12th/Biology/Old_ncert_Bio_Chapter_7.pdf (the same chapter in
    # the older numbering). Identical furniture; the latest is the cropped scan, so its
    # fractions are converted through normalise_page before being compared.
    # --------------------------------------------------------------------------------------
    ("BIO", "12"): dict(
        _BIO_COMMON,
        name="NCERT Biology, Class XII",
        # Text grid: first body line top y 88pt (median over 5 older chapters; the latest
        # measures 84.4 + 3.2 crop = 87.6), foot 715pt.
        text_top_pt=88.0,
        text_foot_pt=715.0,
        # --- top rule: dark green across, brown block on the OUTER end ----------------------
        # #4b7336 y 0 -> 31.8pt full width; #745a21 from the outer edge, 146.3pt wide.
        header_band=dict(fill="#4b7336", y0_pt=0.0, y1_pt=31.8),
        header_corner=dict(fill="#745a21", w_pt=146.3),
        # The leaf-and-figure motif is a real IMAGE hanging below the rule on the outer end:
        # image block 0,0 -> 568.8,76.9 on p002 (the strip), motif occupying its outer 143px.
        header_motif=dict(w_pt=153.0, h_pt=100.0),
        # --- folio: an ORANGE tab bleeding off the outer edge, two-thirds down --------------
        # #f7941d x recto 0.8379 -> 1.0382, y 0.7850 -> 0.8259, plus a 0.0064-tall underbar
        # at y 0.8288 with a white gap between. Converted through the 21.6/3.2pt crop.
        folio=dict(style="bleed-tab", fill="#f7941d", ink="#ffffff",
                   w_pt=114.0, h_pt=31.8, y0_pt=613.6,
                   x_recto_pt=498.0, x_verso_pt=0.0,
                   underbar_h_pt=5.0, underbar_gap_pt=2.2,
                   font="sans", size_pt=15.0, weight=700,
                   # the number sits at the INNER end of the tab, the tab bleeding outward
                   align="inner", pad_pt=14.0, radius_pt=0.0, radius_corners=None),
        # --- running head: plain small sans, no strip --------------------------------------
        # 'BIOLOGY' bbox y 0.0766 -> 0.0869 => 62.8 -> 70.8pt; x 0.8717 -> 0.935 => 517 -> 553.
        running_head=dict(y_pt=62.8, size_pt=8.0, smallcaps=False, ink="#666666",
                          font="sans", verso="subject", recto="chapter_title",
                          inset_pt=60.0, uppercase=True, weight=700),
        # --- foot: no bar. Just the imprint, centred. ---------------------------------------
        footer_bar=None,
        imprint=dict(y_pt=758.0, size_pt=9.0, font="sans", ink="#000000"),
        # --- the chapter-opening page -------------------------------------------------------
        # Hero #d3ead4 y 31.7 -> 300.1pt full bleed; orange divider #f7941d y 308.9 -> 339.3
        # with a white gap above it; contents panel #ffe6cb x 79.4 -> 241.1, y 328.2 -> 569.3;
        # green plate #4c7335 behind the illustration x 336 -> 502, y 84.6 -> 181.1.
        opener=dict(
            kind="hero",
            hero=dict(fill="#d3ead4", y0_pt=31.8, y1_pt=300.1),
            divider=dict(fill="#f7941d", y0_pt=308.9, y1_pt=339.3, gap_fill="#ffffff"),
            qr=dict(x_recto_pt=76.0, x_verso_pt=76.0, y_pt=52.0, size_pt=96.0),
            # Illustration plate, outer half of the hero.
            plate=dict(fill="#4c7335", x_pt=336.0, y_pt=85.0, w_pt=166.0, h_pt=96.0),
            # "CHAPTER n" and the title, set LARGE in the display sans, ranged left.
            # bbox 0.0675 -> 0.3077 x, 0.2038 -> 0.2373 y => x 41pt, y 158pt; title y 214pt.
            title=dict(x_pt=41.0, y_pt=158.0, chapter_size_pt=26.0, title_size_pt=30.0,
                       ink="#231f20", smallcaps=False, font="display", weight=400,
                       line_gap_pt=56.0, letter_spacing_pt=-0.9),
            contents=dict(x_pt=79.4, y_pt=328.2, width_pt=161.7, size_pt=10.0,
                          ink="#231f20", italic=True, pitch_pt=24.0, panel_fill="#ffe6cb",
                          panel_radius_pt=12.0, panel_pad_pt=12.0,
                          # the grey shadow tab under the panel, measured #d7d9d8
                          panel_shadow="#d7d9d8"),
            body_x_pt=312.0, body_top_pt=328.2,
        ),
        accent="#00a744",          # section heading green, measured on "6.1 ORIGIN OF LIFE"
        heading_ink="#00a744",
        heading_size_rel=1.33,
        imprint_by_edition={"O": "2022-23", "L": "Reprint 2026-27"},
    ),
    # --------------------------------------------------------------------------------------
    # CLASS 11 PHYSICS -- "the cyan two-column book".
    # Measured on source_pdfs/new/class_11/physics/Chapter_1.pdf (Units and Measurement), all
    # twelve pages, with page.get_drawings() for the furniture and the text layer's own spans
    # for the block and the type. Every number is a measurement, named where it was taken.
    #
    # THESE PAGES ARE SCANS WITH A TEXT LAYER OVER THEM, not born-digital like Biology: each
    # page carries a 2480x3508 A4 raster of the printed page (bbox 26.5,-38.9 -> 630.8,815.9),
    # the standing watermark (90.1,190.9 -> 551.6,652.4) and, on the opener, the QR. The raster
    # is PAGE GROUND and must never be drawn -- see `is_page_ground`, which had to learn this
    # shape: typed as header art it was pasted under the text and every line rendered twice.
    # --------------------------------------------------------------------------------------
    ("PHY", "11"): dict(
        _BIO_COMMON,
        name="NCERT Physics, Class XI",
        trim_pt=PHY11_TRIM_PT,
        # Measured on all 12 pages: odd (recto) x 73.7 -> 547.7, even (verso) x 109.7 -> 583.7,
        # measure 474.0pt on both, confirmed by the cyan rule drawn exactly 474.0pt wide on
        # every page. Inner margin 73.7, outer 109.6 (657.3 - 73.7 - 474.0).
        inner_margin_pt=73.7,
        measure_pt=474.0,
        # TWO EQUAL COLUMNS, measured off the #d4effc example boxes, which are set to exactly
        # one column: 226.4pt, leaving a 21.2pt gutter (474.0 - 2 x 226.4 = 21.2).
        body_columns=2,
        column_pt=226.4,
        gutter_pt=21.2,
        text_top_pt=74.4,
        text_foot_pt=722.8,
        # Bookman-Light 10.0pt is the modal body span (26,540 characters against 8,581 at
        # 9.0pt). Leading measured off 504 consecutive baselines: 12.00pt, i.e. 1.200.
        body_pt=10.0,
        leading=1.200,
        # Running head y 50.7 -> 58.8, 8.0pt Bookman, ink #00aeef, on all 11 numbered pages:
        # the folio at the OUTER end, the subject (verso) or chapter title (recto) at the
        # inner, closed by a 4pt cyan rule at y 58.5 across the full measure.
        running_head=dict(y_pt=50.7, size_pt=8.0, smallcaps=False, ink="#00aeef",
                          font="body", verso="subject", recto="chapter_title",
                          inset_pt=73.7, rule="#00aeef", rule_h_pt=4.0, rule_y_pt=58.5),
        folio=dict(style="plain", fill=None, ink="#00aeef", w_pt=26.0, h_pt=8.1,
                   y0_pt=50.7, x_recto_pt=521.4, x_verso_pt=109.7, font="body",
                   size_pt=8.0, weight=400, radius_pt=0.0, radius_corners=None,
                   align="outer", pad_pt=0.0),
        header_band=None, header_strip=None, header_corner=None, header_motif=None,
        footer_bar=None,
        # Centred at the foot: measured x 314.0 -> 343.4 (the sheet's centre is 328.65),
        # y 754.5 -> 765.2, 8.0pt Arial, black, on every page.
        imprint=dict(y_pt=754.5, size_pt=8.0, font="sans", ink="#000000"),
        opener=dict(
            kind="centred-bars",
            # THE TWO GRADIENT BARS THE TITLE SITS BETWEEN. Measured on p001 by masking the
            # accent cyan in a 150dpi render: both run the full measure (x 73.7 -> 547.7) and
            # are 16.8pt deep; the upper sits at y 143.5, the lower at y 199.7, with the title
            # centred between them. They MIRROR: the upper is solid at the inner edge and fades
            # out towards the outer, the lower fades in towards the outer. They are painted into
            # the page scan, not drawn as vector, so nothing in the PDF's drawings carries them
            # and the opener rendered with no bars at all until they were taken from here.
            bars=dict(fill="#00aeef", h_pt=16.8, gradient=True,
                      x0_pt=73.7, x1_pt=547.7, top_y_pt=143.5, bottom_y_pt=199.7),
            # QR measured bbox 472.7,48.3 -> 557.7,133.2 (85 x 85pt, head of the outer margin).
            qr=dict(x_recto_pt=472.7, x_verso_pt=99.6, y_pt=48.3, size_pt=85.0),
            # Contents panel measured #c7eafb, bbox 74.2,255.9 -> 239.9,696.6, 1pt dark border.
            contents=dict(x_pt=74.2, y_pt=255.9, width_pt=165.7, size_pt=10.0,
                          ink="#00aeef", italic=False, pitch_pt=20.0, panel_fill="#c7eafb",
                          panel_border="#231f20", panel_y1_pt=696.6),
            body_x_pt=320.8, body_top_pt=255.9,
        ),
        # One cyan does all the work: the rule, the running head, the folio, the x.y headings,
        # the example-box text and the opener bars all measure #00aeef. Section headings are set
        # at the body's own 10.0pt, so there is no step up in size -- measured, not chosen.
        accent="#00aeef",
        heading_ink="#00aeef",
        heading_size_rel=1.0,
        box_fill="#d4effc",
        panel_fill="#c7eafb",
        table_fill="#d1d3d4",
        table_header_fill="#00aeef",
        example_marker=dict(open="\u25ba", close="\u25c4", ink="#00aeef", size_pt=10.0),
        imprint_by_edition={"O": "2022-23", "L": "2024-25"},
    ),

    # --------------------------------------------------------------------------------------
    # CLASS 12 PHYSICS -- "the cyan band and grey tab book".
    # Measured on source_pdfs/new/class_12/physics/Chapter_1.pdf (Electric Charges and Fields),
    # all 44 pages, with page.get_drawings() for the furniture and the text layer for the grid.
    #
    # A SINGLE COLUMN WITH A MARGINAL RAIL, not Class 11 Physics' two equal columns: figures and
    # their captions sit in the wide outer margin and the prose runs in one measure beside them.
    # The grid is Biology's -- inner margin 60.0, measure 360.0, mirrored with the spread -- on
    # a 612 x 777.6pt sheet. These pages are scans with a text layer over them, like Class 11
    # Physics: a 2480x3508 raster at (3.6,-38.9)->(608.3,816.5) is PAGE GROUND and is never
    # drawn, and the standing watermark sits at (67.3,191.1)->(529.1,652.9).
    # --------------------------------------------------------------------------------------
    ("PHY", "12"): dict(
        _BIO_COMMON,
        name="NCERT Physics, Class XII",
        trim_pt=PHY12_TRIM_PT,
        inner_margin_pt=60.0,
        measure_pt=360.0,
        body_columns=1,
        # Body block measured over all 44 pages with the head band and the folio filtered out.
        text_top_pt=100.1,
        text_foot_pt=739.7,
        # Bookman-Light 10.5pt is the modal body span (20,671 characters against 7,644 at
        # 9.5pt, which is the captions and the rail). Leading measured off 726 consecutive
        # baselines in 10.5pt blocks: 12.72pt, i.e. 1.211.
        body_pt=10.5,
        leading=1.211,
        # --- the head: a pale band closed by two cyan rules, with a grey tab on it -----------
        # #c7eafb x 6.6 -> 612.0, y -13.0 -> 48.2 (it bleeds off the head and both edges);
        # #42c8f4 x 95.0 -> 612.0 at y 35.9, then #00aeef full width at y 44.9, both 3.7 deep.
        header_band=dict(fill="#c7eafb", y0_pt=0.0, y1_pt=48.2),
        header_rules=[dict(fill="#42c8f4", y0_pt=35.9, y1_pt=39.6, x0_pt=95.0),
                      dict(fill="#00aeef", y0_pt=44.9, y1_pt=48.6, x0_pt=0.0)],
        # The running head sits in a GREY TAB hanging off the head band, on the OUTER edge:
        # #d1d3d4 x 78.0 -> 276.0, y -13.0 -> 93.4 on a verso. The verso prints the SUBJECT
        # ("Physics") in it; the recto prints the CHAPTER TITLE in Century Gothic 15pt #231f20
        # at x 375.8, y 54.3 (measured on p005, "Electric Charges").
        header_strip=None, header_corner=None, header_motif=None, footer_bar=None,
        running_head=dict(y_pt=54.3, size_pt=15.0, smallcaps=False, ink="#231f20",
                          font="display", verso="subject", recto="chapter_title",
                          inset_pt=78.0, tab_fill="#d1d3d4",
                          tab=dict(x_verso_pt=78.0, x_recto_pt=336.0, w_pt=198.0,
                                   y0_pt=0.0, y1_pt=93.4)),
        # --- the folio: a pale blue tab at the FOOT, in the outer corner --------------------
        # #c7eafb 36.0 x 17.3 at y 713.9, x 78.0 on a verso; mirrored to 498.0 on a recto
        # (612.0 - 78.0 - 36.0).
        folio=dict(style="tab", fill="#c7eafb", ink="#231f20", w_pt=36.0, h_pt=17.3,
                   y0_pt=713.9, x_recto_pt=498.0, x_verso_pt=78.0,
                   radius_pt=0.0, radius_corners=None, font="body", size_pt=10.5,
                   weight=700, align="outer", pad_pt=0.0),
        # Arial 8pt black, centred on the sheet: measured x 277.3, y 754.8 on every page.
        imprint=dict(y_pt=754.8, size_pt=8.0, font="sans", ink="#000000"),
        # --- the chapter opener --------------------------------------------------------------
        # A solid cyan band to y 90, then a pale hero panel, then a cyan stripe: measured
        # #00aeef -21.7 -> 391.8, #6dcff6 104.1 -> 376.0 and #c7eafb 90.1 -> 367.1, painted in
        # that order so the eye sees cyan / pale / #6dcff6 / #00aeef down the page. The title is
        # set LEFT in Century Gothic, not centred as Class 11 Physics sets it, and two 19pt
        # squares (#7d7e81 at 505.3,328.1 and #00aeef at 515.3,337.1) sit at the panel's foot.
        opener=dict(
            kind="band-hero",
            hero=dict(fill="#c7eafb", y0_pt=90.1, y1_pt=367.1,
                      band_fill="#00aeef", band_y1_pt=90.1,
                      stripe_fill="#6dcff6", stripe_y0_pt=367.1, stripe_y1_pt=376.0,
                      rule_fill="#00aeef", rule_y0_pt=376.0, rule_y1_pt=391.8),
            squares=[dict(fill="#7d7e81", x_pt=505.3, y_pt=328.1, size_pt=19.0),
                     dict(fill="#00aeef", x_pt=515.3, y_pt=337.1, size_pt=19.0)],
            # QR measured bbox 449.0,48.1 -> 534.0,133.0 (85 x 85pt), in a white box.
            qr=dict(x_recto_pt=449.0, x_verso_pt=78.0, y_pt=48.1, size_pt=85.0),
            title=dict(x_pt=85.0, y_pt=150.0, chapter_size_pt=22.0, title_size_pt=38.0,
                       ink="#231f20", smallcaps=False, font="display", weight=400,
                       line_gap_pt=44.0),
            body_top_pt=420.0,
        ),
        # --- colour ---------------------------------------------------------------------------
        # TWO heading inks, both measured: an x.y section heading is GREY #6d6f71 at 16.0pt
        # Bookman-Demi (14 of them), an x.y.z sub-heading is CYAN #00aeef at 12.0pt (10 of
        # them). Rendering both in one colour is the single most visible way to get this book
        # wrong. 16.0 / 10.5 = 1.524.
        accent="#00aeef",
        heading_ink="#6d6f71",
        heading_size_rel=1.524,
        subheading_ink="#00aeef",
        subheading_size_rel=1.143,
        box_fill="#c7eafb",
        panel_fill="#c7eafb",
        imprint_by_edition={"O": "2022-23", "L": "Reprint 2026-27"},
    ),
}

# --------------------------------------------------------------------------------------------
# THE OTHER FOUR BOOKS.
#
# There are SIX designs across this corpus, not three. That is the finding the owner's nine
# reference pages settle, and it is why `_SUBJECT_PROFILES` in the old exporter -- keyed on
# `BIO`/`CHE`/`PHY` alone -- could never render more than a third of the books correctly:
#
#   CHE11  No header band anywhere. `UNIT n` set in red #ed1b2f at the top RIGHT, the title
#          under it in dark blue #2d2b7e closed by a cyan #8fd8ec rule. An Objectives panel in
#          the left column ruled cyan top and bottom, body text in TWO columns.
#   CHE12  A COMPLETELY different book from CHE11 -- not a variation of it. A mauve #c5a9c4
#          hero with an #b592b6 foot rule, a cream #ffedaa badge carrying `Unit` in a script
#          face over a 145pt drop number, the title reversed out in white over the mauve, and
#          an Objectives block ruled with a 21pt coral #e67e78 bar down its left edge. Body
#          pages set a script-face section title in the outer margin over a coral rule.
#   PHY11  Opener CENTRED (every other book ranges left): the chapter line, then the title
#          between two cyan #00abd0 gradient bars. Contents in a bordered #c7e7f0 box.
#          Body pages are TWO EQUAL COLUMNS under a running head closed by a 6pt cyan rule.
#   PHY12  The book already rendered as PHY12O-ch01, with marginal figure columns and a grey
#          running-header tab.
#
# They are registered so `design_for` resolves rather than raising, and everything measured so
# far is recorded -- but they are NOT in MEASURED_KEYS. Biology is the book that has been
# checked page by page against its own PDFs; rendering chemistry on a grid nobody has measured
# would state a fidelity it has not earned. `render_html.py` refuses an unmeasured book unless
# `--allow-unmeasured` is passed, and stamps the output when it is.
_PROVISIONAL = {
    ("CHE", "11"): dict(
        _BIO_COMMON, name="NCERT Chemistry, Class XI",
        text_top_pt=104.0, text_foot_pt=714.0,
        header_band=None, header_strip=None, header_corner=None, header_motif=None,
        footer_bar=None,
        folio=dict(style="plain", fill=None, ink="#231f20", w_pt=30.0, h_pt=14.0,
                   y0_pt=60.0, x_recto_pt=520.0, x_verso_pt=60.0, font="body",
                   size_pt=10.0, weight=700, radius_pt=0.0, radius_corners=None, align="inner",
                   pad_pt=0.0),
        running_head=dict(y_pt=62.0, size_pt=9.0, smallcaps=True, ink="#231f20",
                          font="body", verso="subject", recto="chapter_title", inset_pt=60.0),
        imprint=dict(y_pt=752.0, size_pt=9.0, font="sans", ink="#000000"),
        opener=None, accent="#00adef", heading_ink="#00adef", heading_size_rel=1.2,
        body_columns=2,
        imprint_by_edition={"O": "2022-23", "L": "2024-25"},
    ),
    ("CHE", "12"): dict(
        _BIO_COMMON, name="NCERT Chemistry, Class XII",
        text_top_pt=96.0, text_foot_pt=714.0,
        header_band=None, header_strip=None, header_corner=None, header_motif=None,
        footer_bar=None,
        folio=dict(style="underline", fill=None, ink="#666666", w_pt=145.0, h_pt=14.0,
                   y0_pt=640.0, x_recto_pt=467.0, x_verso_pt=0.0, font="body",
                   size_pt=10.0, weight=400, rule="#f5c437", radius_pt=0.0,
                   radius_corners=None, align="inner", pad_pt=0.0),
        running_head=None,
        imprint=dict(y_pt=748.0, size_pt=9.0, font="sans", ink="#000000"),
        opener=dict(kind="badge-hero",
                    hero=dict(fill="#c5a9c4", y0_pt=64.0, y1_pt=252.0,
                              rule_fill="#b592b6", rule_h_pt=14.0),
                    badge=dict(fill="#ffedaa", w_pt=116.0, h_pt=143.0)),
        accent="#ed191f", heading_ink="#ed191f", heading_size_rel=1.2,
        body_columns=1,
        imprint_by_edition={"O": "2022-23", "L": "Reprint 2026-27"},
    ),

}
for _k, _v in list(_PROVISIONAL.items()):
    _DESIGNS.setdefault(_k, _v)

# Only these two have been measured page by page against their own source PDFs.
MEASURED_KEYS = {("BIO", "11"), ("BIO", "12"), ("PHY", "11"), ("PHY", "12")}


def parse_book_id(book_id):
    """'BIO11L-ch03' or 'BIO11L' -> ('BIO', '11', 'L'). Raises on anything else.

    The edition letter is REQUIRED and is never inferred. A book id without it is the single
    most dangerous input this pipeline takes: the two editions renumber their chapters, so
    guessing the edition fetches a different chapter's text and presents it as this one's
    (CLAUDE.md records the case -- Principles of Inheritance is ch4 of the latest Class XII and
    ch5 of the older).
    """
    head = (book_id or "").split("-")[0].upper()
    if len(head) != 6 or not head[3:5].isdigit() or head[5] not in "LOM":
        raise ValueError(
            f"book id {book_id!r} is not <SUBJ><CLASS><EDITION> (e.g. BIO11L, BIO12O)")
    return head[:3], head[3:5], head[5]


def design_for(book_id):
    """The Design for a book id. Raises for a book whose design is not in the table."""
    subject, klass, _edition = parse_book_id(book_id)
    try:
        spec = _DESIGNS[(subject, klass)]
    except KeyError:
        raise KeyError(
            f"no measured design for {subject} class {klass}. Designs are keyed by "
            f"(subject, class) -- add one by measuring that book's own pages, never by "
            f"copying another class's numbers.") from None
    return Design(f"{subject}{klass}", **spec)


def is_measured(book_id):
    subject, klass, _ = parse_book_id(book_id)
    return (subject, klass) in MEASURED_KEYS


# --------------------------------------------------------------------------------------------
# NORMALISING A CROPPED SCAN ONTO THE CANONICAL SHEET
# --------------------------------------------------------------------------------------------

def normalise_page(page_w_pt, page_h_pt, body_x0_pt, design, page_side):
    """(dx, dy, note) that puts a scanned page back on the canonical sheet.

    Add dx/dy to every point coordinate measured on the scan to get its position on the
    canonical sheet. Returns dx=dy=0.0 for a page that is already canonical.

    `body_x0_pt` is the left edge of the page's own body text block, which is what makes this a
    MEASUREMENT rather than a guess: the sheet may be cropped by any amount, but the text block
    is set at a known 60pt (recto) / 192pt (verso) from the trim in every Biology book, so the
    difference between where the text actually starts and where the book sets it IS the crop.

    A page with no body text block (an all-figure page, or a textless scan) cannot be measured
    this way. Rather than guess, it falls back to centring the scan on the canonical sheet and
    says so in `note` -- a caller that cares can refuse, and a reviewer can see which pages were
    placed rather than measured.
    """
    W, H = design.trim_pt
    if abs(page_w_pt - W) < 1.0 and abs(page_h_pt - H) < 1.0:
        return 0.0, 0.0, "canonical"

    expected_x0 = design.text_box(page_side)[0]
    if body_x0_pt is None:
        # Centre the crop. Honest, and labelled.
        return ((W - page_w_pt) / 2.0, (H - page_h_pt) / 2.0,
                "centred (no body text block to measure against)")

    dx = expected_x0 - body_x0_pt
    # The vertical crop is assumed symmetric with the horizontal one only when that is what the
    # page sizes say. Measured on the latest Class 12 Biology: 612 - 568.8 = 43.2 (21.6 a side)
    # and 784 - 777.6 = 6.4 (3.2 a side), so the two are NOT the same number and deriving one
    # from the other would be wrong by 18pt.
    dy = (H - page_h_pt) / 2.0
    # A crop should be a few points, not a different page. Anything larger means the page is not
    # this book's sheet at all (the two A4 textless Class 12 scans are the real case), and a
    # silent 100pt shift would put the text block through the header band.
    if abs(dx) > 0.12 * W or abs(dy) > 0.12 * H:
        return ((W - page_w_pt) / 2.0, (H - page_h_pt) / 2.0,
                f"centred (measured offset {dx:.1f},{dy:.1f}pt is too large to be a trim crop; "
                f"page is {page_w_pt:.1f}x{page_h_pt:.1f}pt, book sets {W:.0f}x{H:.0f}pt)")
    return dx, dy, f"uncropped by {dx:.1f},{dy:.1f}pt"


def page_side(printed_folio, page_index):
    """'recto' / 'verso' from the PRINTED folio, falling back to position in the chapter.

    The printed folio is the right answer and the chapter position is not: a chapter starting on
    an even page has every one of its sides flipped relative to its index. Measured on BIO12L
    ch3, whose first page is folio 41 (recto) and on BIO11L ch3, whose first page is folio 23.
    """
    if isinstance(printed_folio, int):
        return "recto" if printed_folio % 2 else "verso"
    return "recto" if page_index % 2 else "verso"


# --------------------------------------------------------------------------------------------
# FURNITURE THAT MUST NEVER BE TREATED AS CONTENT
# --------------------------------------------------------------------------------------------

# The watermark is an IMAGE at a fixed bbox on every page. Measured on BIO11L ch3: all 14 pages
# carry an image block at 65.7,192.3 -> 530.6,657.1 (0.76 x 0.59 of the sheet); BIO12L ch3
# carries the same thing at 45.7,191.1 -> 507.5,652.9. Emitting it as a figure pastes
# "(c) NCERT not to be republished" into the middle of the chapter as if it were artwork.
# 0.86, not 0.84: BIO12L ch01 p021 sets it 0.8400x wide (36,201 -> 500,664 on a 568.8pt
# page) and it went unrecognised by a hair, fusing every panel of Figure 1.15 into one.
_WATERMARK_W_FRAC = (0.70, 0.86)
_WATERMARK_H_FRAC = (0.52, 0.66)
_WATERMARK_CX_FRAC = (0.42, 0.58)
_WATERMARK_CY_FRAC = (0.47, 0.60)


def is_watermark(bbox_frac):
    """True if this fractional bbox is the standing NCERT watermark rather than a figure."""
    x0, y0, x1, y1 = bbox_frac
    w, h = x1 - x0, y1 - y0
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    return (_WATERMARK_W_FRAC[0] <= w <= _WATERMARK_W_FRAC[1]
            and _WATERMARK_H_FRAC[0] <= h <= _WATERMARK_H_FRAC[1]
            and _WATERMARK_CX_FRAC[0] <= cx <= _WATERMARK_CX_FRAC[1]
            and _WATERMARK_CY_FRAC[0] <= cy <= _WATERMARK_CY_FRAC[1])


def is_page_ground(bbox_frac):
    """True if this image block is the full-page scan ground, not a figure.

    Every page carries one: BIO11L ch3 p003's image list is the figure (0.70 x 0.73), the page
    ground (0.99 x 1.00) and the watermark (0.76 x 0.59). Pasting the ground in as a figure
    reproduces the whole page inside itself.
    """
    x0, y0, x1, y1 = bbox_frac
    if (x1 - x0) > 0.97 and (y1 - y0) > 0.97:
        return True
    # A FULL-BLEED BAND AT THE FOOT is ground too. BIO11L ch01 p002 (the Ernst Mayr page)
    # fades to green from y 444pt to the trim as one full-width image. Typed as a figure it
    # merged with the portrait into one page-sized "figure", which then swallowed the
    # portrait's caption as a figure label -- the caption vanished from the page, and the
    # band was never drawn. No NCERT figure runs edge to edge and off the foot of the sheet.
    if (x1 - x0) > 0.97 and y1 > 0.99 and y0 > 0.3:
        return True
    # A SCAN GROUND THAT BLEEDS OFF BOTH HEAD AND FOOT. The Physics books are scans with a text
    # layer laid over them: an A4 raster (2480x3508) is placed on the wider 657.3 x 777.1pt
    # physics sheet, so it spans only 0.92 of the width and misses the 0.97 test above -- but it
    # runs off BOTH the head and the foot (measured y -0.050 -> 1.050 on PHY11L ch01, identical
    # on all 12 pages). Falling through to `is_header_art` (flush with the head, wider than
    # 0.90) it was typed as header furniture and pasted under the text, so every line of every
    # physics page rendered twice -- the whole page as a bitmap, with our own text on top of it.
    # No figure bleeds off the head AND the foot of the sheet.
    return y0 <= 0.005 and y1 >= 0.995 and (x1 - x0) > 0.80


def is_header_art(bbox_frac, design):
    """True if this image block is the page's own header furniture (the Class 11 gradient, the
    Class 12 motif strip) rather than a figure.

    Measured: BIO11L ch3 p001 carries 0,0 -> 612,340.9 (the opener gradient); BIO12L ch3 p002
    carries 0,0 -> 568.8,76.9 (the rule and the leaf motif). The motif strip is drawn MIRRORED
    on recto pages and comes back only 38pt wide once its negative-width bbox is squared up, so
    a width test alone missed it on every odd page -- measured on BIO12L ch6, eight pages each
    emitted a 21x75pt sliver at the trim edge as a figure. Anything flush with the head of the
    sheet and ending inside the header band is furniture; no NCERT figure starts at y=0.
    """
    x0, y0, x1, y1 = bbox_frac
    if y0 > 0.005:
        return False
    return (x1 - x0) > 0.90 or y1 <= 0.16


# The QR code NCERT prints on every chapter opener (it links to the chapter's e-resources).
# Measured 85 x 85pt on BIO11L ch3 p001 (bbox 449.0,85.9 -> 534.0,170.9) and 96 x 96pt on
# BIO12L ch6 p001. It is a real image and worth keeping, but it is FURNITURE: a figure cutter
# that treats it as artwork files it as "Figure 3.0" and an evidence step can quote it.
def is_qr_code(bbox_frac, design):
    x0, y0, x1, y1 = bbox_frac
    W, H = design.trim_pt
    w_pt, h_pt = (x1 - x0) * W, (y1 - y0) * H
    if not (60.0 <= w_pt <= 120.0 and 60.0 <= h_pt <= 120.0):
        return False
    if abs(w_pt - h_pt) > 0.12 * max(w_pt, h_pt):   # a QR is square
        return False
    return y1 < 0.30          # and sits in the head of the opener


__all__ = ["Design", "design_for", "is_measured", "parse_book_id", "normalise_page",
           "page_side", "is_watermark", "is_page_ground", "is_header_art", "is_qr_code",
           "CANONICAL_TRIM_PT", "MEASURED_KEYS", "pt_to_mm"]
