#!/usr/bin/env python3
"""The page template for build_storage_artifact.py. Kept separate so the generator stays about
DATA and this file stays about PRESENTATION.

Palette and type are taken from the book being documented rather than chosen: #0074bd is the ink
NCERT prints its Class XI Biology chapter titles in, #00aeef its section headings and side notes,
#231f20 its body text and #6d6f71 its figure captions -- all measured from the PDF text layer by
scripts/extract_ncert_layout.py. Jost stands in for NCERT's AvantGarde chapter titles and Gelasio
for its Bookman body face.
"""

import json

CSS = """
:root{
  --blue:#0074bd; --cyan:#00aeef; --ink:#231f20; --grey:#6d6f71;
  --ground:#eef2f6; --card:#ffffff; --line:#d3dde6;
  --text:#1b2430; --text-2:#51606f; --text-3:#7d8b99;
  --code-bg:#f4f7fa; --chip:#e4ecf3;
  --key:#9b2d6f; --pos:#0074bd; --run:#0f7b5a;
  --paper-edge:#c3d0db;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --blue:#49b2ef; --cyan:#2fc6ff; --ink:#e8edf2; --grey:#9aa7b3;
    --ground:#0e1319; --card:#161d26; --line:#2a3542;
    --text:#e6ecf2; --text-2:#a3b1bf; --text-3:#78889a;
    --code-bg:#111821; --chip:#1f2a36;
    --key:#ef8fc4; --pos:#6cc0f5; --run:#4ccfa0;
    --paper-edge:#2a3542;
  }
}
:root[data-theme="dark"]{
  --blue:#49b2ef; --cyan:#2fc6ff; --ink:#e8edf2; --grey:#9aa7b3;
  --ground:#0e1319; --card:#161d26; --line:#2a3542;
  --text:#e6ecf2; --text-2:#a3b1bf; --text-3:#78889a;
  --code-bg:#111821; --chip:#1f2a36;
  --key:#ef8fc4; --pos:#6cc0f5; --run:#4ccfa0;
  --paper-edge:#2a3542;
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--text);
  font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;
  font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1180px; margin:0 auto; padding:0 24px 96px}

/* ---- masthead ---- */
.mast{padding:56px 0 34px; border-bottom:1px solid var(--line); margin-bottom:40px}
.eyebrow{
  font-size:12px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--text-3); font-weight:500; margin:0 0 14px;
}
h1{
  font-size:clamp(34px,5.2vw,54px); line-height:1.04; margin:0 0 18px;
  font-weight:500; letter-spacing:-.018em; text-wrap:balance; color:var(--text);
}
h1 .hl{color:var(--blue)}
.lede{font-size:18px; color:var(--text-2); max-width:65ch; margin:0 0 26px}
.chips{display:flex; flex-wrap:wrap; gap:10px}
.chip{
  display:inline-flex; align-items:baseline; gap:7px;
  background:var(--chip); border:1px solid var(--line); border-radius:999px;
  padding:5px 14px; font-size:13px; color:var(--text-2);
}
.chip b{font-size:14px; color:var(--text); font-weight:600; font-variant-numeric:tabular-nums}

/* ---- sections ---- */
section{margin:0 0 52px}
h2{
  font-size:13px; letter-spacing:.13em; text-transform:uppercase; font-weight:600;
  color:var(--text-3); margin:0 0 6px;
}
h2 + .sub{font-size:24px; font-weight:500; color:var(--text); margin:0 0 18px; letter-spacing:-.01em}
p.note{color:var(--text-2); max-width:68ch; margin:0 0 16px}

/* ---- key schema table ---- */
.tablewrap{overflow-x:auto; border:1px solid var(--line); border-radius:12px; background:var(--card)}
table{border-collapse:collapse; width:100%; min-width:620px; font-size:14px}
th{
  text-align:left; font-size:11px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--text-3); font-weight:600; padding:12px 16px; border-bottom:1px solid var(--line);
  white-space:nowrap;
}
td{padding:11px 16px; border-bottom:1px solid var(--line); vertical-align:top; color:var(--text-2)}
tr:last-child td{border-bottom:0}
td code, .mono{font-family:'IBM Plex Mono',ui-monospace,Menlo,monospace; font-size:13px}
td code{color:var(--text); background:var(--code-bg); padding:2px 6px; border-radius:5px; white-space:nowrap}

/* ---- the spread: scan + rows ---- */
.spread{
  display:grid; grid-template-columns:minmax(0,340px) minmax(0,1fr); gap:28px;
  align-items:start; margin:0 0 20px;
}
@media (max-width:860px){ .spread{grid-template-columns:1fr} }
.scanbox{position:sticky; top:20px}
.scan{
  position:relative; max-width:440px; background:#fff; border:1px solid var(--paper-edge);
  border-radius:8px; overflow:hidden; box-shadow:0 2px 14px rgba(16,30,48,.10);
  line-height:0;
}
.scan img{width:100%; height:auto; display:block}
.rect{
  position:absolute; border:1.5px solid rgba(0,174,239,.55); background:rgba(0,174,239,.09);
  border-radius:2px; cursor:pointer; transition:background .12s, border-color .12s;
}
.rect:hover{background:rgba(0,174,239,.22)}
.rect.on{
  border-color:var(--blue); background:rgba(0,116,189,.26);
  box-shadow:0 0 0 1.5px rgba(0,116,189,.35);
}
.rect.side{border-color:rgba(155,45,111,.6); background:rgba(155,45,111,.10)}
.rect.side.on{border-color:#9b2d6f; background:rgba(155,45,111,.28)}
.scancap{
  font-size:12.5px; color:var(--text-3); margin-top:10px; line-height:1.5;
}
.scancap b{color:var(--text-2); font-weight:600}

/* ---- row list ---- */
.rows{display:flex; flex-direction:column; gap:8px}
.row{
  border:1px solid var(--line); border-radius:10px; background:var(--card);
  overflow:hidden;
}
.row.on{border-color:var(--blue); box-shadow:0 0 0 1px var(--blue)}
.rowhead{
  display:grid; grid-template-columns:auto auto minmax(0,1fr) auto; gap:12px;
  align-items:center; padding:10px 14px; cursor:pointer; width:100%;
  background:none; border:0; text-align:left; font:inherit; color:inherit;
}
.rowhead:focus-visible{outline:2px solid var(--blue); outline-offset:-2px}
.sk{
  font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--text-3);
  white-space:nowrap;
}
.kind{
  font-size:11px; letter-spacing:.06em; text-transform:uppercase; font-weight:600;
  padding:3px 8px; border-radius:5px; white-space:nowrap;
  background:var(--chip); color:var(--text-2);
}
.kind[data-k="section_heading"],.kind[data-k="chapter_title"]{background:rgba(0,174,239,.15); color:var(--cyan)}
.kind[data-k="side_note"]{background:rgba(155,45,111,.14); color:var(--key)}
.kind[data-k="paragraph"],.kind[data-k="list"]{background:var(--chip); color:var(--text-2)}
.prev{
  font-family:'Gelasio',Georgia,serif; font-size:14px; color:var(--text-2);
  overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
}
.prev .sc{font-variant:small-caps; letter-spacing:.01em}
.prev strong{color:var(--text); font-weight:700}
.caret{color:var(--text-3); font-size:12px; transition:transform .15s}
.row.on .caret{transform:rotate(90deg)}
.rowbody{display:none; border-top:1px solid var(--line); background:var(--code-bg)}
.row.on .rowbody{display:block}
pre{
  margin:0; padding:16px; overflow-x:auto; font-family:'IBM Plex Mono',monospace;
  font-size:12.5px; line-height:1.65; color:var(--text-2); tab-size:2;
}
.k-key{color:var(--text-3)}
.k-key.is-key{color:var(--key); font-weight:600}
.k-key.is-pos{color:var(--pos); font-weight:600}
.k-key.is-run{color:var(--run); font-weight:600}
.renders{
  padding:12px 16px 16px; border-top:1px solid var(--line); background:var(--card);
}
.renders .lbl{
  font-size:10.5px; letter-spacing:.11em; text-transform:uppercase; color:var(--text-3);
  font-weight:600; margin-bottom:7px;
}
.renders .out{font-family:'Gelasio',Georgia,serif; color:var(--ink); font-size:15px; line-height:1.55}
.renders .out .sc{font-variant:small-caps}
.renders .out strong{font-weight:700}

/* ---- legend ---- */
.legend{display:flex; flex-wrap:wrap; gap:16px; margin:0 0 18px; font-size:13px; color:var(--text-2)}
.legend span{display:inline-flex; align-items:center; gap:7px}
.sw{width:13px; height:13px; border-radius:3px; display:inline-block}

/* ---- callout ---- */
.callout{
  border-left:3px solid var(--blue); background:var(--card); border-radius:0 10px 10px 0;
  padding:16px 20px; margin:0 0 18px; border-top:1px solid var(--line);
  border-right:1px solid var(--line); border-bottom:1px solid var(--line);
}
.callout h3{margin:0 0 7px; font-size:15px; font-weight:600; color:var(--text)}
.callout p{margin:0; color:var(--text-2); font-size:14.5px; max-width:70ch}
.callout code{font-family:'IBM Plex Mono',monospace; font-size:13px; background:var(--code-bg); padding:1px 5px; border-radius:4px; color:var(--text)}

/* ---- the two page panels, scan vs re-render ---- */
.panels{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:22px; margin:0 0 22px}
@media (max-width:760px){ .panels{grid-template-columns:1fr} }
.panel .ptitle{
  font-size:11px; letter-spacing:.11em; text-transform:uppercase; font-weight:600;
  color:var(--text-3); margin:0 0 9px; display:flex; align-items:center; gap:8px;
}
.panel .ptitle .dot{width:7px; height:7px; border-radius:50%; background:var(--cyan)}
.panel .ptitle.re .dot{background:var(--run)}

/* the page rebuilt from the stored rows */
.repage{
  position:relative; background:#fff; border:1px solid var(--paper-edge); border-radius:8px;
  box-shadow:0 2px 14px rgba(16,30,48,.10); overflow:hidden;
  font-family:'Gelasio',Georgia,serif; color:#231f20;
}
/* A HEADING MUST NOT WRAP. The stored bbox is the width the line occupies in NCERT's own
   AvantGarde/Bookman; re-set in a substitute face it runs slightly wider, and a wrapped heading
   pushes down into the paragraph stored beneath it -- `1.1 Diversity in the Living World` broke
   over two lines and collided with `If you look around you will see...`. Only flowing text
   (paragraphs and lists) wraps; single-line elements keep their line and overflow if they must,
   which shows the substitution honestly instead of corrupting the layout. */
.repage .el{position:absolute; margin:0; line-height:1.33; white-space:nowrap}
.repage .el.p{text-align:justify; white-space:normal}
/* A side note is flowing text too, just in a narrow measure -- NCERT breaks `1.1 Diversity in the
   Living World` over two lines in the margin. It wraps, but is NOT justified: justifying a
   two-word line stretches it across the whole rail. */
.repage .el.w{white-space:normal; text-align:left}
.repage .el .sc{font-variant:small-caps}
.repage .el strong{font-weight:700}
.repage .rail{position:absolute; top:0; bottom:0; background:rgba(0,174,239,.045)}

/* ---- console-style table ---- */
.dtable{min-width:900px; font-size:12.5px}
.dtable th{position:sticky; top:0; background:var(--card); z-index:1}
.dtable td{font-family:'IBM Plex Mono',monospace; font-size:12px; white-space:nowrap;
  color:var(--text-2); padding:8px 14px}
.dtable td.wide{white-space:normal; min-width:280px; max-width:360px;
  font-family:'Gelasio',Georgia,serif; font-size:13px}
.dtable td.pk{color:var(--key)}
.dtable td.sk{color:var(--key); font-weight:600}
.dtable td.pos{color:var(--pos)}
.dtable tr:hover td{background:var(--code-bg)}
.swatch{display:inline-block; width:10px; height:10px; border-radius:2px; margin-right:6px;
  border:1px solid var(--line); vertical-align:-1px}

footer{
  border-top:1px solid var(--line); padding-top:22px; color:var(--text-3); font-size:13px;
}
@media (prefers-reduced-motion:reduce){ *{transition:none !important} }
"""

JS = """
document.querySelectorAll('.rowhead').forEach(function(btn){
  btn.addEventListener('click', function(){
    var row = btn.closest('.row');
    var pg  = row.getAttribute('data-pg');
    var idx = row.getAttribute('data-idx');
    var open = row.classList.contains('on');
    document.querySelectorAll('.row[data-pg="'+pg+'"]').forEach(function(r){ r.classList.remove('on'); });
    document.querySelectorAll('.rect[data-pg="'+pg+'"]').forEach(function(r){ r.classList.remove('on'); });
    if(!open){
      row.classList.add('on');
      btn.setAttribute('aria-expanded','true');
      var rect = document.querySelector('.rect[data-pg="'+pg+'"][data-idx="'+idx+'"]');
      if(rect) rect.classList.add('on');
    } else {
      btn.setAttribute('aria-expanded','false');
    }
  });
});
document.querySelectorAll('.rect').forEach(function(rect){
  rect.addEventListener('click', function(){
    var pg = rect.getAttribute('data-pg'), idx = rect.getAttribute('data-idx');
    var head = document.querySelector('.row[data-pg="'+pg+'"][data-idx="'+idx+'"] .rowhead');
    if(head){ head.click(); head.scrollIntoView({block:'center', behavior:'smooth'}); }
  });
});
"""


def rebuild_page(page, els, runs_preview, esc, width=420):
    """The page REBUILT from the stored rows alone -- nothing here reads the PDF.

    Each element is placed from its own `bbox` (fractions of the page) and sized from `size_rel`
    times the page's own body type size, with its stored `color` and `runs`. That is the whole
    render contract executed literally, which is the point: if the stored row is missing something
    the printed page has, this panel shows it missing rather than describing it as present.
    """
    pw, ph = page["page_width_pt"], page["page_height_pt"]
    scale = width / pw
    height = ph * scale
    body_px = page["body_text_size_pt"] * scale
    out = ['<div class="repage" style="width:%dpx;height:%dpx">' % (width, height)]
    if page.get("margin_side"):
        rail = [c for c in page["columns"] if c["name"] == "side"]
        if rail:
            out.append('<div class="rail" style="left:%.2f%%;width:%.2f%%"></div>'
                       % (rail[0]["x0"] * 100, (rail[0]["x1"] - rail[0]["x0"]) * 100))
    for el in els:
        b = el["bbox"]
        colour = el["runs"][0]["color"] if el["runs"] else "#231f20"
        fs = body_px * el["size_rel"]
        if el["role"] in ("paragraph", "list"):
            cls = "el p"
        elif el["role"] in ("side_note", "figure_caption"):
            cls = "el w"
        else:
            cls = "el"
        style = ("left:%.2f%%;top:%.2f%%;width:%.2f%%;font-size:%.2fpx;color:%s"
                 % (b[0] * 100, b[1] * 100, (b[2] - b[0]) * 100, fs, colour))
        if el["role"] in ("section_heading", "chapter_title"):
            style += ";font-weight:600"
        if el["role"] == "side_note":
            style += ";line-height:1.28"
        out.append('<p class="%s" style="%s">%s</p>' % (cls, style, runs_preview(el)))
    out.append("</div>")
    return "\n".join(out), int(height)


def build(chapter, book, data, spreads, chapter_title, palette,
          json_html, runs_preview, shorten, esc, ROLE_ORDER):
    total_rows = sum(len(p["elements_in_reading_order"]) for p in data["pages"])
    n_pages = len(data["pages"])

    out = []
    out.append('<title>NCERT Page to Rows</title>')
    out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    out.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
               'family=Jost:wght@400;500;600&family=Gelasio:ital,wght@0,400;0,700;1,400'
               '&family=IBM+Plex+Mono:wght@400;600&display=swap">')
    out.append("<style>%s</style>" % CSS)
    out.append('<div class="wrap">')

    # ---------- masthead ----------
    out.append('<header class="mast">')
    SUBJ = {"BIO": "Biology", "CHE": "Chemistry", "PHY": "Physics"}
    ED = {"L": "latest", "O": "older"}
    out.append('<p class="eyebrow">%s &middot; Class %s %s &middot; %s edition</p>'
               % (esc(book), book[3:5], SUBJ[book[:3]], ED[book[5]]))
    out.append('<h1>A printed NCERT page,<br>saved as <span class="hl">DynamoDB rows</span></h1>')
    out.append('<p class="lede">Three real pages from <em>%s</em>, each beside the rows it becomes. '
               'The blue boxes on every scan are drawn from the <code class="mono">bbox</code> that '
               'is actually stored &mdash; click one, or click a row, to see the two line up.</p>'
               % esc(chapter_title))
    out.append('<div class="chips">')
    for label, val in (("pages in chapter", n_pages), ("rows from this chapter", total_rows),
                       ("rows shown here", sum(len(s["items"]) for s in spreads)),
                       ("source", "PDF text layer")):
        out.append('<span class="chip">%s <b>%s</b></span>' % (esc(str(label)), esc(str(val))))
    out.append('</div></header>')

    # ---------- the model ----------
    out.append('<section>')
    out.append('<h2>The model</h2><p class="sub">One table, one partition per chapter</p>')
    out.append('<p class="note">A chapter is one partition and its blocks sort by printed position, '
               'so the whole chapter, a single page, or one paragraph are each a single query with '
               'nothing to reassemble afterwards.</p>')
    out.append('<div class="tablewrap"><table><thead><tr>'
               '<th>PK &mdash; partition</th><th>SK &mdash; sort</th><th>What it holds</th>'
               '</tr></thead><tbody>')
    for pk, sk, what in [
        ("BOOK#%s" % book, "CH#01", "the chapter: title, page range, counts, measured palette"),
        ("BOOK#%s#CH#01" % book, "PG#003#BL#005",
         "one block &mdash; paragraph, heading, list, table, figure"),
        ("BOOK#%s#CH#01" % book, "PS#%s-CH01-P12" % book,
         "one passage &mdash; what an exam-question quote cites"),
        ("BOOK#%s#CH#01" % book, "LAYOUT#PG#003", "the page's geometry: size, columns, body type size"),
        ("PAIR#%s" % book[:5], "LATEST#01", "old &harr; new chapter pairing, matched on title"),
    ]:
        out.append("<tr><td><code>%s</code></td><td><code>%s</code></td><td>%s</td></tr>"
                   % (esc(pk), esc(sk), what))
    out.append("</tbody></table></div>")
    out.append('</section>')

    # ---------- spreads ----------
    for s in spreads:
        page = s["page"]
        pf = page["page_file"]
        cols = ", ".join("%s %.3f&ndash;%.3f" % (c["name"], c["x0"], c["x1"]) for c in page["columns"])
        out.append('<section>')
        out.append('<h2>Page %s%s</h2><p class="sub">%s</p>'
                   % (esc(pf),
                      " &middot; printed page %d" % s["printed"] if s["printed"] else "",
                      "%d rows &middot; %s" % (len(s["items"]),
                                               "two columns" if len(page["columns"]) > 1 else "single column")))
        out.append('<div class="legend">'
                   '<span><i class="sw" style="background:rgba(0,174,239,.45)"></i> body column</span>'
                   '<span><i class="sw" style="background:rgba(155,45,111,.45)"></i> side column</span>'
                   '<span class="mono">columns: %s</span></div>' % cols)
        out.append('<div class="panels">')

        # left panel: the scan, with every stored bbox drawn on top of it
        out.append('<div class="panel">')
        out.append('<p class="ptitle"><span class="dot"></span>As printed &mdash; the scan</p>')
        out.append('<div class="scan">')
        out.append('<img src="%s" alt="NCERT page %s as printed" width="%d" height="%d">'
                   % (s["uri"], esc(pf), s["w"], s["h"]))
        for i, (el, it) in enumerate(zip(s["els"], s["items"]), 1):
            b = el["bbox"]
            out.append('<button class="rect%s" data-pg="%s" data-idx="%d" '
                       'style="left:%.3f%%;top:%.3f%%;width:%.3f%%;height:%.3f%%" '
                       'title="%s &mdash; %s" aria-label="%s on page %s"></button>'
                       % (" side" if el["column"] == "side" else "", esc(pf), i,
                          b[0] * 100, b[1] * 100, (b[2] - b[0]) * 100, (b[3] - b[1]) * 100,
                          esc(it["SK"]), esc(el["role"]), esc(el["role"]), esc(pf)))
        out.append('</div>')
        out.append('<p class="scancap">Page size <b>%.0f&times;%.0f pt</b>, body type <b>%.1f pt</b>. '
                   'Every rectangle is one stored row, drawn from its <span class="mono">bbox</span>. '
                   'Click one.</p>'
                   % (page["page_width_pt"], page["page_height_pt"], page["body_text_size_pt"]))
        out.append('</div>')

        # right panel: the same page rebuilt from the rows alone
        rebuilt, _h = rebuild_page(page, s["els"], runs_preview, esc, width=440)
        out.append('<div class="panel">')
        out.append('<p class="ptitle re"><span class="dot"></span>Rebuilt from the rows</p>')
        out.append(rebuilt)
        out.append('<p class="scancap">Positioned only from each row\'s <span class="mono">bbox</span>, '
                   '<span class="mono">size_rel</span>, <span class="mono">color</span> and '
                   '<span class="mono">runs</span>. No PDF is read here. The shaded rail is the '
                   'stored <span class="mono">side</span> column.</p>')
        out.append('</div>')
        out.append('</div>')

        # the rows themselves
        out.append('<div class="rows">')
        for i, (el, it) in enumerate(zip(s["els"], s["items"]), 1):
            out.append('<div class="row" data-pg="%s" data-idx="%d">' % (esc(pf), i))
            out.append('<button class="rowhead" aria-expanded="false">')
            out.append('<span class="sk">%s</span>' % esc(it["SK"].split("#", 2)[-1]))
            out.append('<span class="kind" data-k="%s">%s</span>'
                       % (esc(el["role"]), esc(el["role"].replace("_", " "))))
            out.append('<span class="prev">%s</span>' % (runs_preview(el) or "&mdash;"))
            out.append('<span class="caret">&#9656;</span>')
            out.append('</button>')
            out.append('<div class="rowbody">')
            out.append("<pre>%s</pre>" % json_html(shorten(it)))
            out.append('<div class="renders"><p class="lbl">Renders as</p>'
                       '<div class="out">%s</div></div>' % (runs_preview(el) or "&mdash;"))
            out.append('</div></div>')
        out.append('</div></section>')

    # ---------- the table itself ----------
    out.append('<section>')
    out.append('<h2>The table</h2><p class="sub">Every row from these three pages</p>')
    out.append('<p class="note">This is the whole of what is stored, with nothing hidden: '
               '%d rows, one per printed block. <span class="mono">PK</span> is the chapter and '
               '<span class="mono">SK</span> the printed position, so the table is already in '
               'reading order &mdash; page 003 before 004, and within a page the side column before '
               'the body.</p>' % sum(len(sp["items"]) for sp in spreads))
    out.append('<div class="callout" style="margin:0 0 14px"><h3>Every row below shares one '
               'partition key</h3><p><code>PK = "BOOK#%s#CH#01"</code> on all %d of them. That is '
               'what makes the chapter a single query, so the column is stated here once instead of '
               'repeated on every line.</p></div>'
               % (esc(book), sum(len(sp["items"]) for sp in spreads)))
    out.append('<div class="tablewrap"><table class="dtable"><thead><tr>'
               '<th>SK &mdash; sort key</th><th>kind</th><th>column</th><th>bbox</th>'
               '<th>size_rel</th><th>color</th><th>runs</th><th>text</th>'
               '</tr></thead><tbody>')
    for sp in spreads:
        for el, it in zip(sp["els"], sp["items"]):
            fmt = []
            for r in it["runs"]:
                flags = "".join(k for k in ("b", "i", "sc", "sup", "sub") if r.get(k))
                fmt.append(flags or "\u2013")
            runcol = " &middot; ".join(fmt[:4]) + (" &hellip;" if len(fmt) > 4 else "")
            txt = it["text"]
            if len(txt) > 110:
                txt = txt[:110] + " \u2026"
            out.append(
                "<tr>"
                '<td class="sk">%s</td>'
                "<td>%s</td>"
                "<td>%s</td>"
                '<td class="pos">%s</td>'
                '<td class="pos">%s</td>'
                "<td><i class=\"swatch\" style=\"background:%s\"></i>%s</td>"
                "<td>%s</td>"
                '<td class="wide">%s</td>'
                "</tr>"
                % (esc(it["SK"]), esc(it["kind"]), esc(it["column"]),
                   esc("[" + ", ".join(it["bbox"]) + "]"), esc(it["size_rel"]),
                   esc(it.get("color", "#231f20")), esc(it.get("color", "")),
                   runcol, esc(txt)))
    out.append("</tbody></table></div>")
    out.append('<div class="callout" style="margin-top:18px"><h3>What the <span class="mono">runs</span> '
               'column means</h3>'
               '<p>One entry per run, listing only the flags that are set: <code>b</code> bold, '
               '<code>i</code> italic, <code>sc</code> small caps, <code>sup</code>/<code>sub</code> '
               'scripts, and <code>&ndash;</code> for a run with no formatting at all. A plain '
               'paragraph is a single <code>&ndash;</code>; the paragraph that defines '
               '<em>biodiversity</em> reads <code>&ndash; &middot; b &middot; &ndash;</code>, which '
               'is the bold term sitting between two stretches of body text.</p></div>')
    out.append('</section>')

    # ---------- fetching ----------
    out.append('<section>')
    out.append('<h2>Fetching</h2><p class="sub">Four queries cover every view</p>')
    out.append('<div class="tablewrap"><table><thead><tr><th>What you want</th><th>Query</th></tr>'
               '</thead><tbody>')
    for want, q in [
        ("The whole chapter, in printed order", 'PK = "BOOK#%s#CH#01"' % book),
        ("One page", 'PK = "BOOK#%s#CH#01" AND begins_with(SK, "PG#003")' % book),
        ("One paragraph on its own", 'GetItem(PK, SK = "PG#003#BL#007")'),
        ("The chapter's palette and page range", 'GetItem("BOOK#%s", "CH#01")' % book),
    ]:
        out.append("<tr><td>%s</td><td><code>%s</code></td></tr>" % (want, esc(q)))
    out.append("</tbody></table></div>")
    out.append('<div class="callout" style="margin-top:18px"><h3>Sorting is free</h3>'
               '<p><code>PG#003#BL#007</code> sorts after <code>PG#003#BL#006</code> and before '
               '<code>PG#004#BL#001</code>, so a chapter query returns printed reading order with no '
               'post-processing. Side-column blocks are numbered first within a page, which is why '
               'they lead.</p></div>')
    out.append('<div class="callout"><h3>Two attribute names need aliasing</h3>'
               '<p><code>class</code> and <code>text</code> are both DynamoDB reserved words. They '
               'store and read normally, but any expression naming them is rejected, so queries pass '
               '<code>ExpressionAttributeNames={"#cls":"class","#txt":"text"}</code>.</p></div>')
    out.append('</section>')

    # ---------- what the book's own ink is ----------
    out.append('<section>')
    out.append('<h2>Appearance</h2><p class="sub">The colours are measured, not chosen</p>')
    out.append('<p class="note">Each row stores the ink it is printed in. These were read from the '
               'PDF text layer, which is why a new-edition page renders in the new edition\'s colours '
               'rather than an approximation of them.</p>')
    out.append('<div class="legend">')
    for role in ROLE_ORDER:
        if role in palette and role != "image":
            out.append('<span><i class="sw" style="background:%s;border:1px solid var(--line)"></i>'
                       '<span class="mono">%s</span> %s</span>'
                       % (esc(palette[role]), esc(palette[role]), esc(role.replace("_", " "))))
    out.append('</div></section>')

    out.append('<footer>Generated by <span class="mono">scripts/build_storage_artifact.py</span> '
               'from <span class="mono">ncert/layout/%s.json</span>, which '
               '<span class="mono">scripts/extract_ncert_layout.py</span> reads out of the chapter '
               'PDF\'s text layer. Every row, colour and position on this page comes from that '
               'extraction &mdash; nothing here is hand-written. NCERT page images are reproduced for '
               'internal review of the extraction.</footer>' % esc(chapter))
    out.append('</div>')
    out.append("<script>%s</script>" % JS)
    return "\n".join(out)
