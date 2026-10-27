"""Remove NCERT's `© NCERT not to be republished` watermark from an open PDF, in memory.

Every page of an NCERT PDF carries the watermark as a page-sized form XObject that Acrobat
tagged `/PieceInfo ... /Private /Watermark` and put in the optional-content group `Watermark`.
Every crop the pipeline cut from a page -- figures, vector art, re-cut photographs, opener art
-- carried the grey diagonal text across it (BIO11L ch11 Figure 11.8). Switching the layer off
is not enough: the form names its group through an OCMD, which the renderer still draws. The
form's content is emptied instead, so nothing that renders the page draws the watermark.
The file on disk is never written.
"""
import re


def strip(doc):
    """Blank every watermark form in `doc` (a PyMuPDF document). Returns the number blanked."""
    ocgs = {x for x, o in (doc.get_ocgs() or {}).items()
            if "watermark" in (o.get("name") or "").lower()}
    n = 0
    for x in range(1, doc.xref_length()):
        try:
            obj = doc.xref_object(x, compressed=True)
        except Exception:
            continue
        if "/Subtype/Form" not in obj:
            continue
        hit = "/Private/Watermark" in obj
        m = re.search(r"/OC (\d+) 0 R", obj)
        if not hit and m and ocgs:
            oc = int(m.group(1))
            try:
                ocobj = doc.xref_object(oc, compressed=True)
            except Exception:
                ocobj = ""
            hit = oc in ocgs or any(re.search(rf"\b{w} 0 R", ocobj) for w in ocgs)
        if hit:
            doc.update_stream(x, b" ")
            n += 1
    return n
