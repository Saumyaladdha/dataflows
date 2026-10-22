#!/usr/bin/env python3
"""Asserts the invariants of an organic-chemistry export.

    python3 scripts/check_organic_export.py CHE12L-ch09

Every check here corresponds to a defect the owner had to find by reading the PDF, because the
build reported success while shipping them. The organic flow went out without a checker at all --
inorganic had one and organic did not -- and the result was a 40-item defect list. These are the
properties that list says must hold.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner_core as rc  # noqa: E402
import chemistry_model as model_mod  # noqa: E402

# Where each chapter's SOURCE pdf lives, so the export can be compared against the book it claims
# to reproduce. Without this the checks can only ask whether the export is self-consistent, which
# is exactly how three badly-lossy pages passed every test.
_SOURCE_PDF = {
    "CHE12L-ch05": rc.pp("inputs", "ncert", "latest", "Class_12th", "Chemistry", "Chapter_5.pdf"),
    "CHE12L-ch09": rc.pp("inputs", "ncert", "latest", "Class_12th", "Chemistry", "Chapter_9.pdf"),
}



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    args = ap.parse_args()

    review = rc.pp("exports", "review")
    html_path = os.path.join(review, "html", args.chapter + "_ORG_READER.html")
    fig_dir = os.path.join(review, args.chapter + "_organic_figures")
    pdf_path = os.path.join(review, args.chapter + "_ORGANIC.pdf")
    page = open(html_path, encoding="utf-8").read()
    body = page.split("</style>", 1)[-1]
    m = model_mod.build(args.chapter, model_mod.load_measurement(args.chapter))

    fails, notes = [], []

    def check(ok, label, detail=""):
        (notes if ok else fails).append(
            "%s %s%s" % ("PASS" if ok else "FAIL", label, ("  -- " + detail) if detail else ""))

    # 1. no block renders as an apology. A placeholder is content the reader cannot read.
    placeholders = body.count("fig-missing")
    check(placeholders == 0, "no block renders as a 'not transcribed' placeholder",
          "%d present" % placeholders)

    # 2. every reaction that CAN be set as mathematics is.
    #
    # Counted against the equations that have a usable transcription, not against every equation
    # block. Three of this chapter's blocks cannot be rendered from the data: A2S returned
    # "unsure" for one and, for two more, copied the heading beside them instead of the equation.
    # Suppressing those is correct -- rendering them printed the chapter's heading three times --
    # so they are reported as the extraction gaps they are rather than counted as render failures.
    eqs = [it for p in m["pages"] for it in p["items"] if it["role"] == "equation"]
    import chemistry_render as _cr
    usable = [e for e in eqs if _cr._is_real_latex(e.get("latex") or "")]
    unusable = len(eqs) - len(usable)
    # A displayed structure drawn with vertical bonds is rendered as vector, not as mathematics
    # -- KaTeX cannot lay out a 2D structure -- so both forms count as "rendered".
    rendered = body.count('class="equation') + body.count('eq-structure')
    check(rendered >= len(usable) * 0.98, "every usable reaction renders",
          "%d rendered of %d usable (%d blocks unreadable from the data)"
          % (rendered, len(usable), unusable))

    # 3. every structure has an asset, and the asset is not empty
    # A figure inside a worked-example panel that carries no artwork is deliberately NOT cropped
    # -- its words are set as text by the panel -- so requiring an asset for it contradicts the
    # duplication check two tests below.
    figs = [(p["page"], it["n"]) for p in m["pages"] for it in p["items"]
            if it["role"] == "figure"
            and not (it.get("panel") and not it.get("has_artwork"))]
    missing, empty = [], []
    for pg, n in figs:
        # Either kind of asset counts. A structure may be shipped as a crop of the page
        # ("fig_") or as a depiction drawn from its transcribed SMILES ("mol_"); the question
        # this check asks is whether the reader gets a picture, not which route drew it.
        names = os.listdir(fig_dir) if os.path.isdir(fig_dir) else []
        crops = [f for f in names if f.startswith("fig_p%03d_b%s." % (pg, n))]
        mols = [f for f in names if f.startswith("mol_p%03d_b%s." % (pg, n))]
        if not crops and not mols:
            missing.append((pg, n))
        elif crops and min(os.path.getsize(os.path.join(fig_dir, f)) for f in crops) < 2000:
            # The floor applies to CROPS only. A crop that small caught no ink and is a blank
            # rectangle. A drawn depiction is compact by nature -- a correct benzene ring is
            # under 2 KB of SVG -- so the same floor would condemn good drawings.
            empty.append((pg, n))
    check(not missing and not empty, "every structure has a non-empty asset",
          "missing %s, near-empty %s" % (missing[:3], empty[:3]))

    # 4. no panel's content is also shipped as a picture of itself.
    # A figure block INSIDE a panel whose artwork is that panel's own text renders twice: once as
    # the panel's words and again as a crop of them. On p277 that nested a cropped Example 9.5
    # inside a freshly drawn Example 9.5.
    # Tested on what was SHIPPED, not on the model's own condition. An earlier version flagged
    # every figure that sits inside a panel, which is not a defect in itself -- the defect is a
    # crop of that panel existing on disk and being placed inside it.
    dupes = []
    for p in m["pages"]:
        for it in p["items"]:
            if it["role"] != "figure" or not it.get("panel") or it.get("has_artwork"):
                continue
            if os.path.isdir(fig_dir) and any(
                    f.startswith("fig_p%03d_b%s." % (p["page"], it["n"]))
                    for f in os.listdir(fig_dir)):
                dupes.append((p["page"], it["n"]))
    check(not dupes, "no panel is also rendered as a crop of itself", "%s" % (dupes[:4],))

    # 5. a question number is not a section heading.
    # "9.5 How will you convert:" is an exercise stem and matches the same pattern as the chapter's
    # section headings, so it was being set in the margin in the book's display face.
    heads = [it for p in m["pages"] for it in p["items"] if it["role"] == "margin_heading"]
    stems = [h["text"][:44] for h in heads
             if re.search(r"\b(convert|write|give|how|what|describe|arrange|account)\b",
                          h["text"], re.I)]
    check(not stems, "no exercise stem is styled as a section heading", "%s" % (stems[:3],))

    # 6. the folio is printed on every page but the opener
    first = m["pages"][0]["page"]
    want = [p["page"] for p in m["pages"] if p["page"] != first and p["folio"]]
    got = len(re.findall(r'class="folio folio-', body))
    check(got >= len(want), "every page but the opener carries its folio",
          "%d folios for %d pages" % (got, len(want)))

    # 7. headings are not broken mid-word
    broken = re.findall(r'<h2 class="sec-head"[^>]*>(?:(?!</h2>).)*?\w-\s*</h2>', body, re.S)
    check("overflow-wrap: anywhere" not in page, "headings cannot break mid-word",
          "stylesheet still allows it")

    # 8. sub/superscripts survive into the body
    scripts = body.count("<sub>") + body.count("<sup>")
    check(scripts >= 150, "formulae keep their sub/superscripts",
          "%d script spans" % scripts)

    # 9. the book's typography survives. Italics in chemistry are meaning -- n-, o-, p-, in situ,
    # ortho -- and the colour coding shows which group reacts. Both were measured from the start
    # and were being discarded between the measurement and the page.
    ems = body.count("<em>")
    check(ems >= 80, "italics survive into the page", "%d italic spans" % ems)


    # 10. blocks that matched no printed position.
    # A block with no position cannot be placed in a column, put inside a panel, or set beside a
    # figure. This is the single largest root cause of layout damage in this chapter -- 35 of 236
    # blocks -- and until now it produced no warning of any kind.
    unmatched = [(p["page"], it["n"]) for p in m["pages"] for it in p["items"]
                 if not it.get("bbox") and it["role"] != "chapter_title"]
    check(len(unmatched) <= len([i for p in m["pages"] for i in p["items"]]) * 0.08,
          "blocks are matched to a printed position",
          "%d unmatched, e.g. %s" % (len(unmatched), unmatched[:4]))

    # 11. placements made on a weak match are stated, not silently trusted.
    weak = [(p["page"], it["n"], it["match_score"]) for p in m["pages"] for it in p["items"]
            if it.get("match_score") is not None and it["match_score"] < 0.80]
    check(len(weak) <= 10, "blocks are placed on confident matches",
          "%d placed below 0.80, e.g. %s" % (len(weak), weak[:3]))

    # 12. (removed) comparing our page against the SOURCE belongs to step A2R, not here.
    #
    # It was tried and the attempt is worth recording. Comparing word-for-word against the book
    # cannot distinguish content that is MISSING from content that is present as ARTWORK -- Table
    # 9.1's structure column is drawn, so its words are correctly absent from our text layer.
    # Excluding artwork regions to compensate shrank the denominator so far that the same handful
    # of genuinely missing words became a large fraction, and nineteen correct pages began failing.
    #
    # The question "is anything the book prints absent from our page" needs to look at the two
    # pages and judge, which is what the a2r-render-reviewer agent exists for. A script can only
    # honestly ask the narrower question below: did the RENDERER drop anything the extraction gave
    # it. Extraction gaps are reported separately, by count, from the build.

    # A drawn panel must carry something. A2R found Example 9.1, 9.2 and 9.5 printed as
    # correctly-drawn, correctly-coloured, entirely EMPTY boxes: A2S returned no items for those
    # blocks, so the renderer had a panel and nothing to put inside it. An empty box is worse
    # than no box -- it reads as "the book has nothing here". chemistry_model's
    # fill_empty_from_measured now recovers that text from the page's own text layer; this is
    # what stops the silent version coming back.
    empty_panels = 0
    for pm in re.finditer(r'<(?:div|section)[^>]*class="[^"]*\bpanel\b[^"]*"[^>]*>(.*?)</(?:div|section)>',
                          body, re.S):
        chunk = pm.group(1)
        if "<img" in chunk or "<svg" in chunk:
            continue
        if len(re.sub(r"<[^>]+>", " ", chunk).strip()) < 3:
            empty_panels += 1
    check(empty_panels == 0, "no panel is drawn empty",
          "%d panels have neither text nor artwork" % empty_panels)

    # 13. a page that is mostly empty is a symptom worth surfacing.
    import pymupdf as _fitz
    blank = []
    if os.path.exists(pdf_path):
        outd = _fitz.open(pdf_path)
        for i in range(outd.page_count):
            pg = outd[i]
            blocks = [b for b in pg.get_text("blocks") if b[4].strip()]
            if blocks and i > 0:
                frac = 1 - (max(b[3] for b in blocks) / pg.rect.height)
                if frac > 0.28:
                    blank.append(i + 1)
        outd.close()
    check(not blank, "no page is left largely empty",
          "pages with >28%% empty at the foot: %s" % (blank,))

    for line in notes + fails:

        print("  " + line)
    print("\n%d checks, %d failed" % (len(notes) + len(fails), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
