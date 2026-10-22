#!/usr/bin/env python3
"""Asserts the invariants of an inorganic-chemistry export, so a fix for one page cannot quietly
break another.

    python3 scripts/check_inorganic_export.py CHE12L-ch05

This exists because it was needed. Working behaviour was broken three times while fixing smaller
faults, and each time the damage was found by the owner looking at a screenshot rather than by the
build: a change that routed untranscribed tables to text also stripped the salmon header off the
one table that WAS transcribed and blanked the chapter's only portrait; a change that stopped
figure crops swallowing stray prose also erased the content of the block being cropped. None of
those were visible in the build's own output, which happily reported success.

Every check below is a property the owner has already had to report by hand.
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
    html_path = os.path.join(review, "html", args.chapter + "_INORG_READER.html")
    fig_dir = os.path.join(review, args.chapter + "_inorg_figures")
    pdf_path = os.path.join(review, args.chapter + "_INORGANIC.pdf")
    page = open(html_path, encoding="utf-8").read()
    # Count only what is in the BODY. The stylesheet defines .fig-missing, and counting the whole
    # file reported that rule as a missing figure on every clean build.
    body = page.split("</style>", 1)[-1]
    m = model_mod.build(args.chapter, model_mod.load_measurement(args.chapter))

    text_only = re.sub(r"<[^>]+>", " ", page)
    fails, notes = [], []

    def check(ok, label, detail=""):
        (notes if ok else fails).append("%s %s%s" % ("PASS" if ok else "FAIL", label,
                                                     ("  -- " + detail) if detail else ""))

    # 1. every figure block has a crop on disk and an <img> on the page
    figs = [(p["page"], it["n"]) for p in m["pages"] for it in p["items"]
            if it["role"] == "figure"]
    missing = [f for f in figs
               if not os.path.exists(os.path.join(fig_dir, "p%03d_b%s.png" % f))]
    check(not missing, "every figure has a crop", "missing: %s" % (missing[:5],))
    check(body.count("fig-missing") == 0, "no 'no artwork found' notices",
          "%d present" % body.count("fig-missing"))

    # 2. a table A2S transcribed is a real table, not a picture and not bare text
    transcribed = [(p["page"], it["n"]) for p in m["pages"] for it in p["items"]
                   if it["role"] == "table" and (it.get("header") or [])]
    check(page.count('<table class="tbl"') >= len(transcribed),
          "every transcribed table renders as a real table",
          "%d rendered, %d transcribed" % (page.count('<table class="tbl"'), len(transcribed)))

    # 3. panel labels survive
    # Either form counts. The label may be set as text, or taken as vector from the page when the
    # book's display script is available -- what must hold is that the panel HAS its printed
    # label, not which way it was produced.
    labels = re.findall(r'<span class="label"><i>([^<]*)</i>', body)
    labels += re.findall(r'<span class="label label-svg"><img [^>]*alt="([^"]*)"', body)
    check(any(l.startswith("Example") for l in labels) and "Solution" in labels,
          "worked-example panels keep their printed labels", "found: %s" % labels[:4])

    # 4. no page silently loses its extracted text
    lost = []
    for p in m["pages"]:
        pid = 'id="p%03d"' % p["page"]
        if pid not in page:
            lost.append((p["page"], "page absent"))
            continue
        i = page.index(pid)
        j = page.find('<section class="sheet"', i + 1)
        seg = re.sub(r"\s+", "", re.sub(r"<[^>]+>", " ",
                                        page[i:j if j > 0 else len(page)])).lower()
        words = [w for w in re.findall(r"[a-z]{5,}",
                                       "".join(it["text"] for it in p["items"]).lower())]
        if words:
            gone = [w for w in words if w not in seg]
            if len(gone) / len(words) > 0.05:
                lost.append((p["page"], "%d/%d words" % (len(gone), len(words))))
    check(not lost, "no page loses its extracted text", "%s" % (lost[:4],))

    # 5. glyph repair held
    check("®" not in page, "no mis-mapped reaction arrows",
          "%d registered-trademark signs" % page.count("®"))

    # 6. section headings are TEXT -- complete, searchable, and impossible to crop
    heads = [it for p in m["pages"] for it in p["items"] if it["role"] == "margin_heading"]
    rendered = re.findall(r'<h2 class="sec-head[^"]*"[^>]*>(.*?)</h2>', body, re.S)
    # Either form. A heading set as text carries its words directly; one taken as vector carries
    # them in the alt text and a visually-hidden span, so the truncation test works on both.
    plain = [re.sub(r"<[^>]+>", " ", r) + " " + " ".join(re.findall(r'alt="([^"]*)"', r))
             for r in rendered]
    truncated = []
    for it in heads:
        want = re.sub(r"\s+", " ", it["text"].replace("\n", " ")).strip()
        tail = want.split()[-1] if want.split() else ""
        if tail and not any(tail in p for p in plain):
            truncated.append(want[:40])
    check(len(rendered) >= len(heads) and not truncated,
          "every section heading renders complete, as text",
          "%d rendered of %d; truncated: %s" % (len(rendered), len(heads), truncated[:3]))

    # 9. the book's typography survives. Italics in chemistry are meaning -- n-, o-, p-, in situ,
    # ortho -- and the colour coding shows which group reacts. Both were measured from the start
    # and were being discarded between the measurement and the page.
    ems = body.count("<em>")
    check(ems >= 30, "italics survive into the page", "%d italic spans" % ems)


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
